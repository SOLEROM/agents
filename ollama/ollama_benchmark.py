#!/usr/bin/env python3
"""
ollama_bench_tokps_mem.py

Ollama benchmark (tok/s) + memory footprint on Jetson/embedded.

Defaults (no args):
- Bench ALL models from /api/tags
- sudo systemctl restart ollama BETWEEN models (hard isolation)
- Measures:
  * gen tok/s (eval_count / eval_duration)
  * prompt tok/s (prompt_eval_count / prompt_eval_duration) if present
  * wall time
  * Ollama process RSS baseline/peak/delta (MB) + VmHWM (peak RSS from /proc)
  * Optional tegrastats sampling (--tegrastats): RAM used peak + GR3D_FREQ peak

Single-model on demand:
  --model llama3.2:latest

Deps:
  pip install requests psutil

Optional (Jetson):
  --tegrastats requires passwordless sudo for "sudo -n tegrastats"
  restart mode requires passwordless sudo for "sudo -n systemctl restart ollama"
"""

import argparse
import json
import re
import statistics as stats
import subprocess
import threading
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import requests

try:
    import psutil
except ImportError:
    psutil = None


# ---------------- Defaults ----------------

OLLAMA_BASE_DEFAULT = "http://127.0.0.1:11434"
OLLAMA_SERVICE_DEFAULT = "ollama"

DEFAULT_PROMPT = "Explain mutex vs semaphore and give a short example."
DEFAULT_NUM_PREDICT = 256
DEFAULT_TEMPERATURE = 0.0
DEFAULT_WARMUP = 1
DEFAULT_REPEATS = 1

HTTP_TIMEOUT_S = 600
OLLAMA_START_TIMEOUT_S = 60


# ---------------- Data structures ----------------

@dataclass
class RunResult:
    model: str
    ok: bool
    error: str = ""

    wall_time_s: float = 0.0

    prompt_tokens: Optional[int] = None
    prompt_time_s: Optional[float] = None
    prompt_tok_s: Optional[float] = None

    gen_tokens: Optional[int] = None
    gen_time_s: Optional[float] = None
    gen_tok_s: Optional[float] = None

    # Memory (CPU) - ollama process
    rss_mb_baseline: Optional[float] = None
    rss_mb_peak: Optional[float] = None
    rss_mb_delta: Optional[float] = None
    vmhwm_mb: Optional[float] = None  # peak RSS from /proc/<pid>/status

    # tegrastats (optional)
    ram_mb_baseline: Optional[float] = None  # system RAM used at start (MB)
    ram_mb_peak: Optional[float] = None      # system RAM used peak (MB)
    gr3d_peak: Optional[float] = None        # GR3D_FREQ peak (% or MHz number parsed)


# ---------------- Utility helpers ----------------

def safe_div(a: Optional[float], b: Optional[float]) -> Optional[float]:
    if a is None or b is None or b == 0:
        return None
    return a / b


def fmt(x: Optional[float], w: int, p: int = 2) -> str:
    if x is None:
        return "-".rjust(w)
    return f"{x:.{p}f}".rjust(w)


def sh_quiet(cmd: List[str]) -> bool:
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


# ---------------- Ollama control ----------------

def wait_for_ollama(base: str, timeout_s: int = OLLAMA_START_TIMEOUT_S) -> bool:
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        try:
            requests.get(f"{base}/api/tags", timeout=2)
            return True
        except Exception:
            time.sleep(1)
    return False


def restart_ollama(service: str) -> None:
    # Passwordless sudo recommended
    ok = sh_quiet(["sudo", "-n", "systemctl", "restart", service])
    if not ok:
        raise RuntimeError(
            f"Failed to restart {service}. "
            f"Set passwordless sudo for: systemctl restart {service}"
        )


def get_models(base: str) -> List[str]:
    r = requests.get(f"{base}/api/tags", timeout=10)
    r.raise_for_status()
    return sorted(m["name"] for m in r.json().get("models", []) if m.get("name"))


# ---------------- Process memory sampling ----------------

def find_ollama_pid() -> Optional[int]:
    """
    Best-effort: locate the ollama server process PID.
    """
    if psutil:
        for p in psutil.process_iter(attrs=["name", "cmdline"]):
            try:
                name = (p.info.get("name") or "").lower()
                cmd = " ".join(p.info.get("cmdline") or []).lower()
                if "ollama" in name or "ollama" in cmd:
                    # Prefer the server daemon ("serve"), but accept base process
                    if "serve" in cmd or name == "ollama":
                        return p.pid
            except Exception:
                continue

    # Fallback
    try:
        out = subprocess.check_output(["pidof", "ollama"], text=True).strip()
        if out:
            return int(out.split()[0])
    except Exception:
        pass
    return None


def read_vmhwm_mb(pid: int) -> Optional[float]:
    """
    VmHWM is peak resident set size (kB) for the process.
    """
    try:
        with open(f"/proc/{pid}/status", "r") as f:
            for line in f:
                if line.startswith("VmHWM:"):
                    kb = float(line.split()[1])
                    return kb / 1024.0
    except Exception:
        return None
    return None


class RSSSampler:
    """
    Samples RSS of the ollama process during a run to capture a peak.
    """
    def __init__(self, pid: int, interval_s: float = 0.05):
        self.pid = pid
        self.interval_s = interval_s
        self._stop = threading.Event()
        self.rss_baseline_mb: Optional[float] = None
        self.rss_peak_mb: Optional[float] = None
        self._thread: Optional[threading.Thread] = None

        self._proc = psutil.Process(pid) if (psutil and pid) else None

    def start(self):
        if not self._proc:
            return
        try:
            self.rss_baseline_mb = self._proc.memory_info().rss / (1024 * 1024)
            self.rss_peak_mb = self.rss_baseline_mb
        except Exception:
            return

        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _loop(self):
        assert self._proc is not None
        while not self._stop.is_set():
            try:
                rss_mb = self._proc.memory_info().rss / (1024 * 1024)
                if self.rss_peak_mb is None:
                    self.rss_peak_mb = rss_mb
                else:
                    self.rss_peak_mb = max(self.rss_peak_mb, rss_mb)
            except Exception:
                pass
            time.sleep(self.interval_s)

    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=1.0)


# ---------------- tegrastats sampling (optional) ----------------

class TegrastatsSampler:
    """
    Runs tegrastats and extracts:
      - RAM used peak (MB): "RAM 1234/7777MB"
      - GR3D_FREQ peak: "GR3D_FREQ 0%" or "GR3D_FREQ 918MHz" (we parse the number)
    """
    def __init__(self):
        self.proc: Optional[subprocess.Popen] = None
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None

        self.ram_used_baseline_mb: Optional[float] = None
        self.ram_used_peak_mb: Optional[float] = None
        self.gr3d_peak: Optional[float] = None

        self.re_ram = re.compile(r"\bRAM\s+(\d+)\s*/\s*(\d+)MB\b")
        self.re_gr3d = re.compile(r"\bGR3D_FREQ\s+(\d+)(?:%|MHz)\b")

    def start(self):
        try:
            self.proc = subprocess.Popen(
                ["sudo", "-n", "tegrastats"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                bufsize=1,
            )
        except Exception:
            self.proc = None
            return

        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _loop(self):
        assert self.proc and self.proc.stdout
        for line in self.proc.stdout:
            if self._stop.is_set():
                break

            m = self.re_ram.search(line)
            if m:
                used = float(m.group(1))
                if self.ram_used_baseline_mb is None:
                    self.ram_used_baseline_mb = used
                if self.ram_used_peak_mb is None:
                    self.ram_used_peak_mb = used
                else:
                    self.ram_used_peak_mb = max(self.ram_used_peak_mb, used)

            g = self.re_gr3d.search(line)
            if g:
                v = float(g.group(1))
                if self.gr3d_peak is None:
                    self.gr3d_peak = v
                else:
                    self.gr3d_peak = max(self.gr3d_peak, v)

    def stop(self):
        self._stop.set()
        if self.proc:
            try:
                self.proc.terminate()
            except Exception:
                pass
        if self._thread:
            self._thread.join(timeout=1.0)
        self.proc = None


# ---------------- Core benchmark run ----------------

def run_once(
    base: str,
    model: str,
    prompt: str,
    num_predict: int,
    temperature: float,
    http_timeout_s: int,
    sample_mem: bool,
    sample_tegrastats: bool,
) -> RunResult:
    pid = find_ollama_pid() if sample_mem else None

    rss_sampler: Optional[RSSSampler] = None
    if sample_mem and psutil and pid:
        rss_sampler = RSSSampler(pid, interval_s=0.05)
        rss_sampler.start()

    tg: Optional[TegrastatsSampler] = None
    if sample_tegrastats:
        tg = TegrastatsSampler()
        tg.start()

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"num_predict": num_predict, "temperature": temperature},
    }

    t0 = time.perf_counter()
    try:
        r = requests.post(f"{base}/api/generate", json=payload, timeout=http_timeout_s)
        t1 = time.perf_counter()
        r.raise_for_status()
        j = r.json()
        ok = True
        err = ""
    except Exception as e:
        t1 = time.perf_counter()
        j = {}
        ok = False
        err = str(e)

    if rss_sampler:
        rss_sampler.stop()

    if tg:
        tg.stop()

    rr = RunResult(model=model, ok=ok, error=err, wall_time_s=(t1 - t0))

    # Parse Ollama stats (durations are typically ns)
    pe_count = j.get("prompt_eval_count")
    pe_dur_ns = j.get("prompt_eval_duration")
    ev_count = j.get("eval_count")
    ev_dur_ns = j.get("eval_duration")

    rr.prompt_tokens = pe_count if isinstance(pe_count, int) else None
    rr.prompt_time_s = (pe_dur_ns / 1e9) if isinstance(pe_dur_ns, (int, float)) else None
    rr.prompt_tok_s = safe_div(rr.prompt_tokens, rr.prompt_time_s)

    rr.gen_tokens = ev_count if isinstance(ev_count, int) else None
    rr.gen_time_s = (ev_dur_ns / 1e9) if isinstance(ev_dur_ns, (int, float)) else None
    rr.gen_tok_s = safe_div(rr.gen_tokens, rr.gen_time_s)

    # Memory sampling results
    if sample_mem and pid:
        rr.vmhwm_mb = read_vmhwm_mb(pid)
        if rss_sampler and rss_sampler.rss_baseline_mb is not None:
            rr.rss_mb_baseline = rss_sampler.rss_baseline_mb
            rr.rss_mb_peak = rss_sampler.rss_peak_mb
            if rr.rss_mb_peak is not None:
                rr.rss_mb_delta = rr.rss_mb_peak - rr.rss_mb_baseline

    # tegrastats results
    if tg:
        rr.ram_mb_baseline = tg.ram_used_baseline_mb
        rr.ram_mb_peak = tg.ram_used_peak_mb
        rr.gr3d_peak = tg.gr3d_peak

    return rr


def aggregate(model: str, runs: List[RunResult]) -> Dict[str, Any]:
    ok_runs = [r for r in runs if r.ok]

    def mean(field: str) -> Optional[float]:
        vals = []
        for r in ok_runs:
            v = getattr(r, field)
            if isinstance(v, (int, float)):
                vals.append(float(v))
        return stats.mean(vals) if vals else None

    def stdev(field: str) -> Optional[float]:
        vals = []
        for r in ok_runs:
            v = getattr(r, field)
            if isinstance(v, (int, float)):
                vals.append(float(v))
        return stats.pstdev(vals) if len(vals) > 1 else (0.0 if vals else None)

    out: Dict[str, Any] = {
        "model": model,
        "runs": len(runs),
        "ok_runs": len(ok_runs),
        "ok": bool(ok_runs),
        "error": (runs[-1].error if runs else "no runs"),
        "gen_tok_s_mean": mean("gen_tok_s"),
        "gen_tok_s_stdev": stdev("gen_tok_s"),
        "prompt_tok_s_mean": mean("prompt_tok_s"),
        "wall_time_s_mean": mean("wall_time_s"),
        "rss_mb_peak_mean": mean("rss_mb_peak"),
        "rss_mb_delta_mean": mean("rss_mb_delta"),
        "vmhwm_mb_mean": mean("vmhwm_mb"),
        "ram_mb_peak_mean": mean("ram_mb_peak"),
        "gr3d_peak_mean": mean("gr3d_peak"),
    }
    return out


# ---------------- Reporting ----------------

def print_report(aggs: List[Dict[str, Any]]) -> None:
    aggs = sorted(aggs, key=lambda a: (a.get("gen_tok_s_mean") or -1), reverse=True)

    header = (
        f"{'Model':28}  {'gen tok/s':10}  {'RSS ΔMB':8}  {'RSS pk':8}  {'VmHWM':7}  "
        f"{'wall s':7}  {'GR3D':6}  {'RAMpk':6}  {'ok':3}"
    )
    print("\n=== SUMMARY ===")
    print(header)
    print("-" * len(header))

    for a in aggs:
        ok = "yes" if a.get("ok") else "no"
        print(
            f"{str(a['model'])[:28].ljust(28)}  "
            f"{fmt(a.get('gen_tok_s_mean'),10,2)}  "
            f"{fmt(a.get('rss_mb_delta_mean'),8,1)}  "
            f"{fmt(a.get('rss_mb_peak_mean'),8,1)}  "
            f"{fmt(a.get('vmhwm_mb_mean'),7,1)}  "
            f"{fmt(a.get('wall_time_s_mean'),7,2)}  "
            f"{fmt(a.get('gr3d_peak_mean'),6,0)}  "
            f"{fmt(a.get('ram_mb_peak_mean'),6,0)}  "
            f"{ok.rjust(3)}"
        )

    fastest = next((a for a in aggs if a.get("ok")), None)
    if fastest and isinstance(fastest.get("gen_tok_s_mean"), (int, float)):
        print(
            f"\nFastest: {fastest['model']}  "
            f"{fastest['gen_tok_s_mean']:.2f} tok/s"
        )


# ---------------- Main flow ----------------

def bench_model(
    base: str,
    service: str,
    model: str,
    prompt: str,
    num_predict: int,
    temperature: float,
    warmup: int,
    repeats: int,
    restart_each: bool,
    sample_mem: bool,
    sample_tegrastats: bool,
) -> Dict[str, Any]:
    print(f"\n[{model}] warmup={warmup} repeats={repeats} num_predict={num_predict}")

    if restart_each:
        print("  restarting ollama …")
        try:
            restart_ollama(service)
        except Exception as e:
            return {"model": model, "ok": False, "error": str(e)}

        if not wait_for_ollama(base):
            return {"model": model, "ok": False, "error": "ollama did not come back up"}

    # warmup
    for _ in range(max(0, warmup)):
        try:
            _ = run_once(
                base, model, prompt, num_predict, temperature, HTTP_TIMEOUT_S,
                sample_mem=False, sample_tegrastats=False
            )
        except Exception:
            pass

    # measured runs
    runs: List[RunResult] = []
    for i in range(max(1, repeats)):
        rr = run_once(
            base, model, prompt, num_predict, temperature, HTTP_TIMEOUT_S,
            sample_mem=sample_mem, sample_tegrastats=sample_tegrastats
        )
        runs.append(rr)
        if rr.ok:
            print(
                f"  run {i+1}: gen_tok_s={rr.gen_tok_s:.2f} "
                f"rssΔ={rr.rss_mb_delta if rr.rss_mb_delta is not None else '-'}MB "
                f"rssPk={rr.rss_mb_peak if rr.rss_mb_peak is not None else '-'}MB "
                f"wall={rr.wall_time_s:.2f}s"
            )
        else:
            print(f"  run {i+1}: ERROR: {rr.error}")
            # If ollama died mid-run, continuing repeats is pointless
            break

    return aggregate(model, runs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="", help="Benchmark a single model (e.g. llama3.2:latest). Default: all models.")
    ap.add_argument("--ollama", default=OLLAMA_BASE_DEFAULT, help="Ollama base URL")
    ap.add_argument("--service", default=OLLAMA_SERVICE_DEFAULT, help="systemd service name for Ollama")
    ap.add_argument("--prompt", default=DEFAULT_PROMPT, help="Benchmark prompt")
    ap.add_argument("--num-predict", type=int, default=DEFAULT_NUM_PREDICT, help="Tokens to generate (num_predict)")
    ap.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE, help="Temperature (0 for stable)")
    ap.add_argument("--warmup", type=int, default=DEFAULT_WARMUP, help="Warmup runs per model (not recorded)")
    ap.add_argument("--repeats", type=int, default=DEFAULT_REPEATS, help="Measured runs per model")
    ap.add_argument("--no-restart", action="store_true", help="Do NOT restart ollama between models")
    ap.add_argument("--no-mem", action="store_true", help="Disable ollama RSS/VmHWM sampling")
    ap.add_argument("--tegrastats", action="store_true",
                    help="Also sample tegrastats (sudo -n). Captures RAM used peak + GR3D peak.")
    ap.add_argument("--csv", default="", help="Write aggregated results to CSV")
    ap.add_argument("--json", default="", help="Write aggregated results to JSON")
    args = ap.parse_args()

    if args.tegrastats:
        print("Note: --tegrastats uses 'sudo -n tegrastats' (passwordless sudo required).")
    if not args.no_restart:
        print("Note: default behavior restarts ollama between models via 'sudo -n systemctl restart ...'.")

    sample_mem = (not args.no_mem) and (psutil is not None)
    if (not args.no_mem) and (psutil is None):
        print("Warning: psutil not installed -> memory sampling disabled. Install: pip install psutil")

    # Single model mode
    if args.model:
        agg = bench_model(
            args.ollama, args.service, args.model,
            args.prompt, args.num_predict, args.temperature,
            args.warmup, args.repeats,
            restart_each=(not args.no_restart),
            sample_mem=sample_mem,
            sample_tegrastats=args.tegrastats,
        )
        print_report([agg])
        return

    # All models mode
    print("Discovering models …")
    models = get_models(args.ollama)
    if not models:
        raise SystemExit("No models found (is ollama running?)")

    aggs: List[Dict[str, Any]] = []
    for model in models:
        agg = bench_model(
            args.ollama, args.service, model,
            args.prompt, args.num_predict, args.temperature,
            args.warmup, args.repeats,
            restart_each=(not args.no_restart),
            sample_mem=sample_mem,
            sample_tegrastats=args.tegrastats,
        )
        aggs.append(agg)

    print_report(aggs)

    if args.csv:
        import csv
        keys = sorted({k for a in aggs for k in a.keys()})
        with open(args.csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            for a in aggs:
                w.writerow(a)
        print(f"\nWrote CSV: {args.csv}")

    if args.json:
        with open(args.json, "w") as f:
            json.dump(aggs, f, indent=2)
        print(f"Wrote JSON: {args.json}")


if __name__ == "__main__":
    main()

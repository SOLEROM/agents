# comapres


params:

```
gen tok/s   RSS ΔMB   RSS pk    VmHWM    wall s   GR3D    RAMpk   ok 

## gen tok/s (generation tokens per second)
 How fast the model produces output tokens, computed as:
 eval_count / eval_duration

## RSS ΔMB (resident set size delta, MB)
  The increase in Ollama process RAM during inference:
  RSS peak – RSS baseline
  Measured via /proc while the model is running.

## RSS pk (resident set size peak, MB)
  The maximum RAM used by the Ollama process during the run.  
  If this approaches total system RAM → crash risk

## VmHWM (high-water mark RSS, MB)
  Linux-reported peak RSS ever reached by the Ollama process (VmHWM in /proc/<pid>/status).
    RSS pk → measured during this run
    VmHWM → kernel’s lifetime max for the process
  Confirms whether allocator spikes occurred
  Helps detect hidden transient peaks (e.g. during model load)

## wall s (wall-clock seconds)
  Total real time for the request, including:
    model load (if cold)
    prompt processing
    generation
    kernel scheduling delays

## GR3D (Jetson GPU activity peak)
    Peak value reported by tegrastats for: GR3D_FREQ
    Usually a percentage or MHz, depending on JetPack.
    Confirms the model actually used the GPU
    Rough indicator of GPU saturation

## RAMpk (system RAM used peak, MB)
    Peak system-wide RAM usage (from tegrastats, not just Ollama).
    This shows global memory pressure, not just one process.

```

## jetson orion

```

=== SUMMARY ===
Model                         gen tok/s   RSS ΔMB   RSS pk    VmHWM    wall s   GR3D    RAMpk   ok 
---------------------------------------------------------------------------------------------------
llama3.2:latest                    21.25       3.5     113.5    122.4    12.62       -       -  yes
gemma3:latest                      16.97      63.2     143.6    143.8    15.89       -       -  yes
gpt-oss:latest                      7.68      70.1     133.6    133.6    34.18       -       -  yes
gemma3:12b                          7.25      62.8     132.0    132.1    36.19       -       -  yes
gemma3:27b                             -         -         -        -        -       -       -   no

Fastest: llama3.2:latest  21.25 tok/s

```

## GeForce RTX 2070 

```

``` 

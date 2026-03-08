# {{PROJECT_NAME}} — Testing

Testing is part of the product. If it’s not tested, it’s not done.

This doc defines:
- Test types and where they live
- Coverage expectations (by domain)
- Regression policy (every bug gets a test)
- How to run tests locally and in CI

---

## Testing pyramid (default)

1. **Unit** tests (fast, deterministic)
2. **Integration** tests (real dependencies where possible)
3. **E2E** tests (critical flows only)
4. **Regression** tests (golden sets / bug repros)

---

## Coverage & gates (by domain)

> Use these as defaults. If a project deviates, record the decision in `0l_DECISIONS.md`.

| Domain | Primary gate | Coverage target (meaningful code) | Notes |
|---|---|---:|---|
| BE | Unit + integration must pass | ≥90% | Focus on business logic, validators, adapters |
| FE | Unit/component + key flow tests | “Meaningful coverage” | Don’t chase vanity %; cover critical paths |
| ML | Reproducibility + eval gates + regression | ≥90% (transforms/validators) | Golden sets + baseline comparison required |
| SHARED | Unit + contract compatibility | ≥90% | Backward compatible APIs unless approved |

---

## Test types

### Unit tests

- What: pure functions, validators, feature builders, UI components
- Where: `**/tests/unit/`

#### Example (pytest)

```python
def test_parse_amount():
    assert parse_amount("₪12.30") == 12.30
```

### Integration tests

- What: service + DB, API + dependency, pipeline end-to-end
- Where: `**/tests/integration/`
- Prefer real infra via containers when feasible.

#### Example (FastAPI + TestClient)

```python
def test_health_endpoint(client):
    r = client.get("/health")
    assert r.status_code == 200
```

### E2E tests

- What: critical user flows across modules
- Where: `tests/e2e/` (shared suite)
- Keep small and stable.

#### Example (Playwright)

```ts
test("login flow", async ({ page }) => {
  await page.goto("/");
  // ...
});
```

### Regression tests (mandatory for bug fixes)

- Every bug fix must add a test that would fail before the fix.
- Keep a **golden set** where it makes sense (ML and critical data transforms).

---

## Mocks, fixtures, and global stubs

- Prefer **SynaptixLabs testing/mocks** when available (don’t build competing test harnesses).
- Shared fixtures should live under: `shared/testing/` (or equivalent).
- Module-specific fixtures go under the module test tree.

---

## How to run tests (examples)

> Replace with project-specific commands.

```bash
# Unit + integration (Python)
pytest -q

# Frontend
pnpm test

# E2E
pnpm test:e2e
```

---

## CLI/TUI Testing Requirements

### Async Subprocess Pattern (CRITICAL for CLI/TUI work)

Any external process invocation in a TUI or CLI tool **MUST** follow this pattern:

1. **Use async subprocess** — never blocking `subprocess.run()` in TUI contexts
2. **Implement cancellation** — user must be able to cancel long-running operations
3. **Stream output** — don't buffer entire output; stream line-by-line
4. **Test responsiveness** — UI must remain responsive during subprocess execution

#### Required Pattern (Python)

```python
import asyncio
from asyncio.subprocess import PIPE

async def run_external_command(cmd: list[str], timeout: float = 30.0):
    """
    Run external command with proper async handling.

    - Streams output
    - Supports cancellation
    - Has timeout protection
    """
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=PIPE,
        stderr=PIPE,
    )

    try:
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(),
            timeout=timeout
        )
        return proc.returncode, stdout.decode(), stderr.decode()
    except asyncio.TimeoutError:
        proc.kill()
        await proc.wait()
        raise
    except asyncio.CancelledError:
        proc.kill()
        await proc.wait()
        raise
```

#### Required Tests for CLI/TUI

| Test Type | What to Test | Example |
|-----------|--------------|---------|
| Responsiveness | UI remains interactive during long ops | Key events processed within 100ms |
| Cancellation | User can cancel running operations | Ctrl+C terminates subprocess cleanly |
| Timeout | Long operations don't hang forever | 30s timeout with graceful failure |
| Streaming | Output appears progressively | Lines appear as generated, not all at once |
| Error handling | Subprocess failures don't crash TUI | Non-zero exit shows error, doesn't crash |

#### Anti-Patterns (DO NOT USE)

```python
# ❌ WRONG: Blocks entire event loop
result = subprocess.run(["slow_command"], capture_output=True)

# ❌ WRONG: No timeout protection
await asyncio.create_subprocess_exec(*cmd)  # hangs forever if command hangs

# ❌ WRONG: Buffering entire output
output = await proc.stdout.read()  # OOM risk on large output
```

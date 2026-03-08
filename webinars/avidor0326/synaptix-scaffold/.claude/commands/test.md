# /project:test — Run Full Test Suite

Run the complete test suite for the current project. This command is project-type aware.

## Steps

1. **Identify the project type** from the current working directory and CLAUDE.md.
2. **Check if a dev server is required** (check CLAUDE.md `Start the Server` section).
3. **Start the server if needed** — confirm it's running before proceeding.
4. **Run tests in order:**
   - Unit tests (fast feedback)
   - Integration tests (requires services)
   - E2E tests last (full system, real browser)
5. **Report results** with pass/fail per layer, failures with file + line, server status.

## Node/Next.js projects
```bash
npm run test:unit          # Unit (Vitest)
npm run type-check         # TypeScript
npm run test:e2e           # E2E (Playwright, auto-starts server)
```

## Python/FastAPI projects
```bash
pytest -m unit modules/    # Unit tests
pytest -m integration      # Integration (requires services)
NIGHTINGALE_ENV=testing poetry run python -m tests --level e2e
```

## Output format

```
## Test Run — [PROJECT] — [DATE]

Server status: ✅ Running on port XXXX | ❌ Not running (E2E skipped)

### Unit Tests
Result: ✅ XX passed / ❌ XX failed
[failures if any — file:line:reason]

### Integration Tests
Result: ✅ XX passed / ❌ XX failed

### E2E Tests
Result: ✅ XX passed / ❌ XX failed

### Overall Gate
[ ] PASS — safe to mark feature done
[ ] FAIL — do not mark done, fix failures first
```

## Rules
- NEVER skip a layer without explicit Avi approval
- If server fails to start → report as test failure, do not proceed to E2E
- Save screenshots to `tests/screenshots/` for all GUI flows

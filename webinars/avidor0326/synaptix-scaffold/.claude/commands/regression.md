# /project:regression — Pre-Merge Regression Gate

Run before any merge to main or "done" declaration.

## Steps

1. **Confirm branch** — you're on the correct feature/sprint branch
2. **Run full test suite** (same as /project:test)
3. **Static checks:**
   - TypeScript: `npm run type-check` (Node projects)
   - Python types: `mypy .` (Python projects)
   - Lint: `npm run lint` / `ruff check .`
4. **Security scan:**
   - `git grep -i "api_key\|secret\|password\|token" -- "*.ts" "*.py" "*.js" "*.tsx"`
   - Confirm no `.env` files staged: `git status`
5. **Check docs:** CLAUDE.md and module docs up to date if architecture changed

## Regression Gate Checklist

```
### Code Quality
[ ] All unit tests pass
[ ] All integration tests pass
[ ] E2E smoke on critical paths pass
[ ] TypeScript / Python type check: CLEAN
[ ] Lint: CLEAN

### Security
[ ] No hardcoded secrets (API keys, passwords, tokens)
[ ] No .env files staged for commit
[ ] Input validation on new external inputs

### Documentation
[ ] CLAUDE.md updated if architecture or commands changed
[ ] docs/03_MODULES.md updated if capabilities changed
[ ] Module AGENTS.md updated if module behavior changed

### Gate decision
[ ] PASS — safe to merge
[ ] FAIL — [list every item that failed with file + line]
```

## Output

State **PASS** or **FAIL** explicitly at the top.
On FAIL: list every failing item with file + line number.
On PASS: print the full checklist with ✅ marks.

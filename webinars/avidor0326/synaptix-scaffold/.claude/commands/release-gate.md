# /project:release-gate — Pre-Production Release Checklist

Run before any production deployment or public demo. Requires all items green.

## Gate Checklist

### Code Quality
```
[ ] All tests pass (unit + integration + E2E)
[ ] No regressions vs previous release
[ ] Type errors: NONE
[ ] Lint: CLEAN
[ ] Code coverage meets minimum threshold (80%+)
```

### Security
```
[ ] No hardcoded secrets in codebase
[ ] .env files not committed (check git log)
[ ] Dependencies audited: npm audit / pip-audit (no critical CVEs)
[ ] Auth flows tested (login, registration, session expiry, token refresh)
[ ] Rate limiting in place on public endpoints
[ ] Input validation on all external inputs
```

### Infrastructure
```
[ ] Environment variables set in prod (not just local .env)
[ ] Database migrations applied to prod
[ ] Health endpoint responding (/health or equivalent)
[ ] Rollback plan defined (what to do if deploy fails)
[ ] Vercel / Railway / Docker config reviewed
```

### Documentation
```
[ ] CHANGELOG.md updated with version + date
[ ] README accurate and reflects current state
[ ] CLAUDE.md reflects current architecture
[ ] docs/03_MODULES.md current
[ ] API docs updated (if applicable)
```

### Demo Readiness
```
[ ] Demo script written and tested end-to-end
[ ] Test/seed data in place
[ ] No debug logs or console.logs in production output
[ ] Screenshots / recordings taken
[ ] Feature flags set correctly
```

## Final Sign-off

**Avi must explicitly approve before proceeding to production.**

Output: Full checklist with ✅/❌ per item + list of blockers + **GO / NO-GO** recommendation.

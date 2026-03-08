# {{PROJECT_NAME}} — Deployment

> Owner: `[CTO]`

---

## Environments

| Environment | URL | Branch | Auto-Deploy |
|-------------|-----|--------|-------------|
| Development | `http://localhost:{{DEV_PORT}}` | any | ✅ (local only) |
| Staging | `https://staging.{{domain}}` | `dev` (tagged) | ✅ on merge |
| Production | `https://{{domain}}` | `main` | ❌ manual |

---

## Deployment Flow

```
Feature Branch → dev → Staging → Production
       │          │        │          │
       │          │        │          └── Manual gate (CTO + FOUNDER)
       │          │        └── Auto on PR merge to dev
       │          └── Auto deploy after PR merge
       └── PR required; no direct pushes to dev/main
```

---

## Environment & Secrets Management

### Per-environment secrets

| Environment | Secrets location |
|-------------|-----------------|
| Development | `.env` (local, gitignored) |
| Staging | CI/CD vault → Railway / GitHub Secrets / Vercel env |
| Production | CI/CD vault → same platform, separate values |

### Env promotion rule

**Never copy `.env` values between environments.** Each environment must have independently configured secrets.

```bash
# On staging/prod deployment: always source from vault
# Never:
cp .env .env.staging   # ❌ WRONG

# Correct: set vars in CI platform UI or via CLI
railway variables set SECRET_KEY=<vault_value> --environment staging
```

### Environment variable checklist (before deploy to staging/prod)

- [ ] `APP_ENV` set to correct tier (`staging` | `production`)
- [ ] `DEBUG=false`
- [ ] `SECRET_KEY` is a new value (not dev key)
- [ ] `DATABASE_URL` points to correct tier DB
- [ ] `PUBLIC_URL` is the correct public URL
- [ ] `ALLOWED_ORIGINS` matches the actual frontend domain
- [ ] All `_KEY` variables rotated from previous tier
- [ ] `SENTRY_DSN` configured and `SENTRY_ENVIRONMENT` set correctly
- [ ] Feature flags reviewed — no experimental flags enabled in prod

---

## Pre-Deployment Checklist

### All environments
- [ ] All tests passing (unit + integration)
- [ ] Coverage target met
- [ ] Linting clean
- [ ] No known security vulnerabilities

### Staging
- [ ] All above +
- [ ] E2E tests pass
- [ ] Manual smoke test completed
- [ ] Performance acceptable

### Production
- [ ] All above +
- [ ] Rollback plan documented
- [ ] Monitoring + alerting configured
- [ ] `[CTO]` approval
- [ ] `/project:release-gate` passed

---

## Deploy Commands

```bash
# Staging (auto on merge, or manual tag)
git tag -a staging-$(date +%Y%m%d) -m "Staging deploy"
git push origin --tags
{{STAGING_DEPLOY_COMMAND}}

# Production
git checkout main && git merge dev
git push origin main
{{PROD_DEPLOY_COMMAND}}
```

---

## Rollback

```bash
# Quick rollback (< 5 min)
{{ROLLBACK_COMMAND}}

# Database rollback (only if migrations were run)
{{DB_ROLLBACK_COMMAND}}
```

---

## Infrastructure

| Service | Provider | Config location |
|---------|----------|----------------|
| Backend | {{BACKEND_HOST}} | `{{config_location}}` |
| Frontend | {{FRONTEND_HOST}} | `{{config_location}}` |
| Database | {{DB_HOST}} | `{{config_location}}` |
| Cache | {{CACHE_HOST}} | `{{config_location}}` |

---

## Monitoring

| Endpoint | Expected | Alert if |
|----------|----------|----------|
| `/health` | 200 | Non-200 for 1 min |
| `/api/health` | 200 | Non-200 for 1 min |

Alerts:
- Error rate > {{X}}%
- p95 response time > {{Y}}ms
- Memory > {{Z}}%

---

## Vibe Cost Reference

| Task | Vibes |
|------|-------|
| Standard deploy | 1–2 V |
| Deploy + migration | 2–4 V |
| Rollback | 1–2 V |
| Incident response | 5–15 V |
| Env rotation | 2–3 V |

---

*Last updated: {{DATE}}*

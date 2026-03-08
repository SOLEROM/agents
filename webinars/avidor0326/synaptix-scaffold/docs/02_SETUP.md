# {{PROJECT_NAME}} — Setup Guide

> Owner: `[CTO]`

---

## Prerequisites

| Tool | Version | Required |
|------|---------|----------|
| Python | >=3.11, <3.14 | ✅ (if BE) |
| Node.js | >=20.x LTS | ✅ (if FE) |
| pnpm | >=8.x | ✅ (if FE, preferred) |
| Docker | Latest | Optional |
| Git | Latest | ✅ |

### ⚠️ Python Version Gate

**Required:** Python 3.11, 3.12, or 3.13. Python 3.14+ is **NOT supported**.

```bash
python --version   # Must output: Python 3.11.x, 3.12.x, or 3.13.x

# pyenv
pyenv install 3.12.4 && pyenv local 3.12.4

# conda
conda create -n {{PROJECT_NAME}} python=3.12 && conda activate {{PROJECT_NAME}}
```

---

## Quick Setup

```bash
# 1. Clone repository
git clone {{REPO_URL}}
cd {{PROJECT_NAME}}

# 2. Install dependencies
{{INSTALL_COMMAND}}

# 3. Environment setup (see Environment Management below)
cp .env.development .env
# Edit .env with your local values

# 4. Database setup
{{DB_SETUP_COMMAND}}

# 5. Verify installation
{{VERIFY_COMMAND}}
```

---

## Environment Management

This project uses tiered environment files. **Only `.env.example` is committed to git.**

### Env file hierarchy

| File | Purpose | In git? |
|------|---------|---------|
| `.env.example` | Master reference — all variables documented | ✅ Yes |
| `.env.development` | Dev-safe defaults shape | ✅ Yes (no real secrets) |
| `.env.staging` | Staging shape — real values in CI vault | ✅ Yes (no real secrets) |
| `.env.production` | Prod shape — all values in CI vault | ✅ Yes (no real secrets) |
| `.env` | Your actual local values | ❌ Never |
| `.env.local` | Local overrides (highest priority) | ❌ Never |

### Env precedence (highest → lowest)

```
.env.local > .env > .env.{APP_ENV} > defaults in code
```

### Setting up locally

```bash
# Development (default)
cp .env.development .env
# Fill in DATABASE_URL, SECRET_KEY, API keys

# Staging (to simulate staging locally)
cp .env.staging .env
# Fill in real staging values from your vault
```

### Required variables (always needed)

| Variable | Description |
|----------|-------------|
| `APP_ENV` | `development` \| `staging` \| `production` |
| `DATABASE_URL` | DB connection string |
| `SECRET_KEY` | Min 32 chars — `openssl rand -hex 32` |
| `PUBLIC_URL` | Base URL for this instance |

See `.env.example` for full variable reference.

### Secrets management per environment

| Environment | Where secrets live |
|-------------|-------------------|
| Development | `.env` (local only, gitignored) |
| Staging | CI/CD vault (Railway / GitHub Secrets / Vercel env) |
| Production | CI/CD vault — never in files |

---

## Running the Application

### Development
```bash
{{DEV_RUN_COMMAND}}
```

### Production build
```bash
{{PROD_RUN_COMMAND}}
```

### With Docker
```bash
docker-compose up -d
```

---

## Running Tests

```bash
# All tests
{{TEST_ALL_COMMAND}}

# Unit tests only
{{TEST_UNIT_COMMAND}}

# With coverage
{{TEST_COVERAGE_COMMAND}}

# E2E
{{TEST_E2E_COMMAND}}
```

---

## Key Commands

```bash
# Development
{{DEV_COMMAND}}          # Start dev server
{{BUILD_COMMAND}}        # Production build
{{LINT_COMMAND}}         # Lint
{{TYPE_CHECK_COMMAND}}   # Type check

# Database (if applicable)
# npm run db:migrate     # Run migrations
# npm run db:seed        # Seed demo data
# npx prisma studio      # DB GUI
```

---

## IDE Setup

### Windsurf
Use `@role_cto`, `@role_cpo`, `@role_ux`, `@role_backend_dev`, `@role_frontend_dev` rules in `.windsurf/rules/`.

### VS Code
Recommended extensions:
- {{EXTENSION_1}}
- {{EXTENSION_2}}

---

## Troubleshooting

**Issue:** `{{COMMON_ISSUE_1}}`
```bash
{{SOLUTION_1}}
```

**Issue:** Env variable not loading
```bash
# Verify .env exists and has no BOM/encoding issues
cat -A .env | head -5
# Restart the dev server after any .env change
```

---

*Last updated: {{DATE}}*

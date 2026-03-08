# {{PROJECT_NAME}} — Claude Code Project Context

> **Stack:** {{TECH_STACK_SUMMARY}}
> **Template version:** SynaptixLabs Windsurf-Projects-Template
>
> This file is auto-loaded by Claude Code CLI when you open this project directory.
> Keep it current — it is the single source of truth for Claude's project awareness.

---

## 1. Project Identity

| Field | Value |
|---|---|
| **Name** | {{PROJECT_NAME}} |
| **Purpose** | {{PROJECT_DESCRIPTION}} |
| **Repo path** | `{{REPO_PATH}}` |
| **Production URL** | {{PRODUCTION_URL}} |
| **Current sprint** | {{CURRENT_SPRINT}} |
| **Dev port** | {{DEV_PORT}} (`{{DEV_COMMAND}}`) |

---

## 2. Start the Server

```bash
# {{STACK_TYPE: Node/Next.js}}
{{DEV_COMMAND}}    # Dev server → http://localhost:{{DEV_PORT}}

# {{STACK_TYPE: Python/FastAPI}}
# uvicorn app.main:app --reload    # API → http://localhost:8000
```

> ⚠️ **E2E tests auto-start the server.** Do NOT start manually when running E2E.

---

## 3. Key Commands

```bash
# Development
{{DEV_COMMAND}}                    # Start dev server
{{BUILD_COMMAND}}                  # Production build
{{TYPE_CHECK_COMMAND}}             # Type check
{{LINT_COMMAND}}                   # Lint

# Testing
{{TEST_UNIT_COMMAND}}              # Unit tests
{{TEST_UNIT_SINGLE_COMMAND}}       # Unit tests (single run)
{{TEST_E2E_COMMAND}}               # Full E2E (Playwright / pytest)
{{TEST_FAST_COMMAND}}              # Quick smoke test

# Database (if applicable)
# npm run db:seed                  # Seed demo data
# npm run db:migrate               # Run migrations
# npx prisma studio                # DB GUI
```

---

## 4. Testing Rules (non-negotiable gates)

```
FEATURE IS "DONE" ONLY WHEN:
  ✅ Unit tests pass
  ✅ TypeScript / type check clean
  ✅ Dev server runs and is functional
  ✅ E2E smoke on affected flows (Playwright or pytest E2E)
  ✅ Screenshots captured for GUI changes (tests/screenshots/)
  ✅ No regressions on full suite
  ✅ Avi sign-off
```

**NEVER mark done based on unit tests alone if a UI or API route was changed.**

---

## 5. Project Structure

```
{{PROJECT_STRUCTURE}}
```

> ⚠️ Before building anything new: check `docs/03_MODULES.md` — capability registry.
> Do not duplicate capabilities that already exist.

---

## 6. Architecture Non-Negotiables

{{ARCHITECTURE_NON_NEGOTIABLES}}

---

## 7. Environment Variables

Copy `{{ENV_EXAMPLE_FILE}}` → `{{ENV_LOCAL_FILE}}`. Required:

```
{{ENV_VARS_LIST}}
```

---

## 8. Sprint Context

| Sprint | Status | Key deliverables |
|---|---|---|
| {{CURRENT_SPRINT}} | 🟢 Active | {{SPRINT_GOAL}} |

Current sprint index: `docs/sprints/{{CURRENT_SPRINT}}/{{CURRENT_SPRINT}}_index.md`

---

## 9. Common Flows to Test (E2E)

{{E2E_FLOWS}}

---

## 10. Deployment

- **Platform:** {{DEPLOY_PLATFORM}}
- **Build command:** `{{BUILD_COMMAND}}`
- **Before any prod deploy:** run `/project:release-gate`

---

## 11. Role Tags (align with AGENTS.md)

| Tag | Who |
|---|---|
| `[FOUNDER]` | Avi — final decision maker |
| `[CTO]` | Architecture, tech debt, reliability |
| `[CPO]` | Product scope, acceptance criteria |
| `[DEV:<module>]` | Module-level implementation |

> Reading order: nearest `AGENTS.md` → root `AGENTS.md` → `docs/00_INDEX.md` → `docs/01_ARCHITECTURE.md`

---

## 12. Custom Commands Available

| Command | Purpose |
|---|---|
| `/project:test` | Run full test suite |
| `/project:e2e` | Playwright browser tests |
| `/project:plan` | Force plan mode before complex work |
| `/project:regression` | Pre-merge gate |
| `/project:release-gate` | Pre-prod checklist |
| `/project:sprint-report` | Current sprint status |

---

## 13. What NOT to Do

{{WHAT_NOT_TO_DO}}
- Do NOT silently expand scope
- Do NOT add new infra dependencies without a FLAG
- Do NOT mark features done without server + E2E verification (when applicable)
- Do NOT push directly to `main` — always use sprint branches

# Common Artifact Paths (repo conventions)

## Root-level (always)

| Artifact | Path | Owner |
|----------|------|-------|
| Global agent constitution (Tier-1) | `AGENTS.md` | `[CTO]` |
| Project README | `README.md` | `[CTO]` |
| Claude Code context | `CLAUDE.md` | `[CTO]` |
| Internal handbook | `CODEX.md` | `[CTO]` |
| Python config | `pyproject.toml` | `[CTO]` |
| Git ignore | `.gitignore` | `[CTO]` |

## Environment files

| Artifact | Path | In git? |
|----------|------|---------|
| Master reference | `.env.example` | ✅ Yes |
| Dev defaults | `.env.development` | ✅ Yes (no real values) |
| Staging shape | `.env.staging` | ✅ Yes (no real values) |
| Production shape | `.env.production` | ✅ Yes (no real values) |
| Local values | `.env` | ❌ Never |
| Local overrides | `.env.local` | ❌ Never |

## Windsurf rules

| Artifact | Path | Owner |
|----------|------|-------|
| Entry point | `.windsurf/rules/00_repo_entrypoint.md` | `[CTO]` |
| Synaptix ops (always-on) | `.windsurf/rules/00_synaptix_ops.md` | `[CTO]` |
| Artifact paths (this file) | `.windsurf/rules/01_artifact_paths.md` | `[CTO]` |
| Templates policy | `.windsurf/rules/02_templates_policy.md` | `[CTO]` |
| Module permissions | `.windsurf/rules/10_module_agent_permissions.md` | `[CTO]` |
| Context router | `.windsurf/rules/20_context_router.md` | `[CTO]` |
| CTO role | `.windsurf/rules/role_cto.md` | `[CTO]` |
| CPO role | `.windsurf/rules/role_cpo.md` | `[CPO]` |
| UX/ARIA role | `.windsurf/rules/role_ux.md` | `[DESIGNER]` |
| Backend dev role | `.windsurf/rules/role_backend_dev.md` | `[CTO]` |
| Frontend dev role | `.windsurf/rules/role_frontend_dev.md` | `[CTO]` |
| ML dev role | `.windsurf/rules/role_ml_dev.md` | `[CTO]` |
| Shared dev role | `.windsurf/rules/role_shared_dev.md` | `[CTO]` |

## Global standards

| Artifact | Path | Owner |
|----------|------|-------|
| Global dev standards | `_global/windsurf_global_rules.md` | `[CTO]` |
| Global README | `_global/README.md` | `[CTO]` |

## AGENTS.md tiers

| Tier | Path | Scope |
|------|------|-------|
| Tier-1 (global) | `AGENTS.md` | Entire repo |
| Tier-2 (backend) | `backend/AGENTS.md` | All BE modules |
| Tier-2 (frontend) | `frontend/AGENTS.md` | All FE modules |
| Tier-2 (ml-ai-data) | `ml-ai-data/AGENTS.md` | All ML modules |
| Tier-2 (shared) | `shared/AGENTS.md` | All shared modules |
| Tier-3 (module) | `<domain>/modules/<module>/AGENTS.md` | Specific module |

## Documentation structure

| Artifact | Path | Owner |
|----------|------|-------|
| Docs index | `docs/00_INDEX.md` | `[CPO]` |
| PRD | `docs/0k_PRD.md` | `[CPO]` |
| Architecture | `docs/01_ARCHITECTURE.md` | `[CTO]` |
| Setup guide | `docs/02_SETUP.md` | `[CTO]` |
| Module registry | `docs/03_MODULES.md` | `[CTO]` |
| Testing guide | `docs/04_TESTING.md` | `[CTO]` |
| Deployment guide | `docs/05_DEPLOYMENT.md` | `[CTO]` |
| Decisions log | `docs/0l_DECISIONS.md` | `[CTO]`/`[CPO]` |
| UI Kit | `docs/ui/UI_KIT.md` | `[DESIGNER]` |

## Sprint system

| Artifact | Path | Owner |
|----------|------|-------|
| Sprint index | `docs/sprints/<SPRINT_ID>/<SPRINT_ID>_index.md` | `[CTO]`/`[CPO]` |
| Sprint decisions | `docs/sprints/<SPRINT_ID>/<SPRINT_ID>_decisions_log.md` | `[CTO]` |
| Module todos | `docs/sprints/<SPRINT_ID>/todo/<SPRINT_ID>_team_dev_<module>_todo.md` | `[DEV:*]` |
| Module reports | `docs/sprints/<SPRINT_ID>/reports/<SPRINT_ID>_team_dev_<module>_report.md` | `[DEV:*]` |
| Requirements delta | `docs/sprints/<SPRINT_ID>/reviews/<SPRINT_ID>_requirements_delta.md` | `[CPO]` |
| Design reviews | `docs/sprints/<SPRINT_ID>/reviews/<SPRINT_ID>_DR_<topic>.md` | `[CTO]` |

## Templates

| Artifact | Path | Purpose |
|----------|------|---------|
| Sprint index template | `docs/templates/sprints/sprint_XX_index_TEMPLATE.md` | New sprints |
| Module todo template | `docs/templates/sprints/sprint_XX_team_dev_MODULE_todo_TEMPLATE.md` | Module todos |
| Module report template | `docs/templates/sprints/sprint_XX_team_dev_MODULE_report_TEMPLATE.md` | Module reports |
| Module AGENTS template | `docs/templates/module_AGENTS_TEMPLATE.md` | New module AGENTS.md |

## Domain structure

### Backend (`backend/`)

```
backend/
├── AGENTS.md                    # Tier-2 rules
├── modules/
│   ├── _example/                # Reference implementation
│   │   ├── README.md
│   │   ├── AGENTS.md            # Tier-3 rules
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── services.py
│   │   │   ├── api.py
│   │   │   └── cli.py
│   │   └── tests/
│   │       ├── unit/
│   │       └── integration/
│   └── <your_module>/           # Same structure
```

### Frontend (`frontend/`)

```
frontend/
├── AGENTS.md                    # Tier-2 rules
├── modules/
│   └── <module>/
│       ├── README.md
│       ├── AGENTS.md            # Tier-3 rules
│       ├── src/
│       │   ├── index.ts
│       │   ├── components/
│       │   ├── pages/
│       │   ├── hooks/
│       │   └── stores/
│       └── tests/
```

### ML/AI/Data (`ml-ai-data/`)

```
ml-ai-data/
├── AGENTS.md                    # Tier-2 rules
├── modules/
│   └── <module>/
│       ├── README.md
│       ├── AGENTS.md            # Tier-3 rules
│       ├── src/
│       │   ├── data/
│       │   ├── features/
│       │   ├── models/
│       │   ├── training/
│       │   └── evaluation/
│       ├── experiments/
│       └── tests/
```

### Shared (`shared/`)

```
shared/
├── AGENTS.md                    # Tier-2 rules
├── cli/                         # CLI plugin system
├── config/                      # Settings (Pydantic)
├── db/                          # Database utilities
├── exceptions/                  # Base exceptions
├── logging/                     # Logging setup
├── testing/                     # Test utilities
├── utils/                       # Common utilities
└── validation/                  # Validators
```

## Scripts

| Script | Path | Purpose |
|--------|------|---------|
| Repo audit | `scripts/audit_repo_structure.py` | Validate structure |

## SynaptixLabs framework (when vendored/installed)

| Artifact | Path | Notes |
|----------|------|-------|
| CLI | `agents/slagents_cli/` | Or configured path |
| Testing harness | `agents/**` | See AGENTS project docs |

## Decisions

| Artifact | Path | Notes |
|----------|------|-------|
| Primary decisions log | `docs/0l_DECISIONS.md` | Single source of truth |
| ADRs (optional) | `docs/adrs/ADR-*.md` | Must be referenced from decisions log |

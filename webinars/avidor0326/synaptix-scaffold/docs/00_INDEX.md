# {{PROJECT_NAME}} — Docs Index

This folder is the **source of truth** for how the project is specified, built, tested, and shipped.

---

## Quick links

| Doc | What it's for | Owner |
|-----|---------------|-------|
| [PRD](0k_PRD.md) | Product requirements + acceptance criteria | `[CPO]` |
| [Architecture](01_ARCHITECTURE.md) | System design, boundaries, NFRs | `[CTO]` |
| [Setup](02_SETUP.md) | Local dev setup + env management | `[CTO]` / `[DEV:*]` |
| [Modules](03_MODULES.md) | Module registry + ownership | `[CTO]` |
| [Testing](04_TESTING.md) | Testing policy + gates | `[CTO]` / `[DEV:*]` |
| [Deployment](05_DEPLOYMENT.md) | CI/CD + releases + rollback | `[CTO]` |
| [Decisions](0l_DECISIONS.md) | Project decision log | `[CTO]` / `[CPO]` |
| [UI Kit](ui/UI_KIT.md) | Design tokens, components, accessibility | `[DESIGNER]` / `[DEV:*|FE]` |

---

## Bootstrap docs (root-level)

| File | What it's for |
|------|---------------|
| `CLAUDE.md` | Claude Code context — loaded automatically by Claude CLI; keep current |
| `CODEX.md` | Internal project handbook — architecture, conventions, key decisions narrative |
| `AGENTS.md` | Global agent constitution — roles, tags, decision rights |

---

## Current sprint

- Sprint index: `sprints/{{SPRINT_ID}}/{{SPRINT_ID}}_index.md`
- Requirements delta: `sprints/{{SPRINT_ID}}/reviews/{{SPRINT_ID}}_requirements_delta.md`

---

## Reading order (recommended)

1. `00_INDEX.md` (this file)
2. `0k_PRD.md` — what we're building + why
3. `01_ARCHITECTURE.md` — how it fits together
4. `03_MODULES.md` — what each module owns
5. `04_TESTING.md` — Definition of Done gates
6. `05_DEPLOYMENT.md` — how we ship + rollback
7. `0l_DECISIONS.md` — why we made key calls

---

## Directory map

```text
docs/
├── 00_INDEX.md
├── 0k_PRD.md
├── 0l_DECISIONS.md
├── 01_ARCHITECTURE.md
├── 02_SETUP.md
├── 03_MODULES.md
├── 04_TESTING.md
├── 05_DEPLOYMENT.md
├── ui/
│   └── UI_KIT.md
├── sprints/
│   ├── README.md
│   └── sprint_XX/
│       ├── sprint_XX_index.md
│       ├── sprint_XX_decisions_log.md
│       ├── todo/
│       ├── reports/
│       └── reviews/
├── knowledge/           # Domain knowledge, research, reference docs
└── templates/
    ├── sprints/         # Copy-from templates for sprint artifacts
    ├── module_AGENTS_TEMPLATE.md
    ├── PRD_TEMPLATE.md
    ├── DECISIONS_TEMPLATE.md
    ├── CHANGELOG_TEMPLATE.md
    ├── SECURITY_TEMPLATE.md
    └── CPTO_agent_TEMPLATE.md
```

---

## Rules of the road

- **One source of truth:** if two docs say different things → raise a FLAG and resolve.
- **Keep docs runnable:** prefer concrete paths, commands, and acceptance criteria over prose.
- **When adding capabilities:** update `03_MODULES.md` + the owning module's README/AGENTS.

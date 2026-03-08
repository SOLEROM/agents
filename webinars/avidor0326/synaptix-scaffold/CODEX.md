# synaptix-scaffold — Platform CODEX

> **Audience:** Dev team + AI agents (internal)
> **Level:** Platform — project creation template
> **Was:** `Windsurf-Projects-Template`

---

## 1. Identity

| Field | Value |
|---|---|
| **Name** | synaptix-scaffold |
| **Purpose** | Tool-agnostic project bootstrap template for all SynaptixLabs projects |
| **Repo path** | `C:\Synaptix-Labs\projects\_platform\synaptix-scaffold` |
| **Status** | 📐 Stable — reference template |
| **Consumers** | All new SynaptixLabs projects |

---

## 2. What It Provides

| Component | Path | Purpose |
|---|---|---|
| Global rules | `_global/` | Shared Windsurf/Claude rules |
| Role prompts | `.windsurf/rules/role_*.md` | CTO, CPO, DEV role definitions |
| Tiered AGENTS | `AGENTS.md` (root + domains) | Agent constitution template |
| CODEX template | `CODEX.md` | Internal handbook template |
| CLAUDE template | `CLAUDE.md` | Thin agent bootstrap template |
| Docs templates | `docs/templates/` | PRD, DECISIONS, CHANGELOG, SECURITY |
| Module example | `backend/modules/_example/` | Reference module structure |
| Commands | `.claude/commands/` | Shared slash commands |

---

## 3. How to Use

**New project:**
1. Copy this scaffold into new project directory
2. Replace all `{{PLACEHOLDER}}` variables
3. Delete this CODEX, replace with project-specific one
4. Initialize git repo
5. Update workspace `CODEX.md` project registry

**Upgrade existing project:**
1. Copy relevant folders (`.windsurf/`, `.claude/`, `AGENTS.md` skeleton)
2. Merge with existing docs
3. Update placeholders

---

## 4. Maintenance Rules

- This is a **template** — no product logic, no real credentials
- Keep placeholders as `{{VARIABLE_NAME}}` format
- All templates must be tool-agnostic (no Windsurf-only content)
- Test template against a throwaway project before updating

---

*Last updated: 2026-02-24 | Owner: [CTO] + [FOUNDER]*

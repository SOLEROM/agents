# {{SPRINT_ID}} — Sprint Index

**Sprint window:** {{START_DATE}} → {{END_DATE}}  
**Owners:** `[FOUNDER]` / `[CTO]` / `[CPO]`

## Status

- Sprint status: {{Planned | Active | Review | Done}}
- Current focus: {{one-liner}}
- Key risks: {{bullets}}

---

## Required artifacts (this sprint)

- Requirements delta: `reviews/{{SPRINT_ID}}_requirements_delta.md`
- Decisions (sprint-local): `{{SPRINT_ID}}_decisions_log.md`
- Design reviews (as needed): `reviews/{{SPRINT_ID}}_DR_<topic>.md`
- Module todos: `todo/{{SPRINT_ID}}_team_dev_<module>_todo.md`
- Module reports: `reports/{{SPRINT_ID}}_team_dev_<module>_report.md`

---

## Quick links

### Deltas / reviews
- [Requirements delta](reviews/{{SPRINT_ID}}_requirements_delta.md)
- DRs: `reviews/` (add per topic)

### Todos (by module)
- `todo/{{SPRINT_ID}}_team_dev_<module>_todo.md`

### Reports (by module)
- `reports/{{SPRINT_ID}}_team_dev_<module>_report.md`

### Decisions (sprint-local)
- `{{SPRINT_ID}}_decisions_log.md`

---

## CTO Pre-Release Verification

> **MANDATORY** before closing this sprint or merging to main.
> See: `.windsurf/rules/role_cto.md` → "Pre-Release Verification" section

| Verification | Status | CTO Sign-off |
|--------------|--------|--------------|
| Code integrity | ⬜ | |
| Tests pass + coverage | ⬜ | |
| Environment verified | ⬜ | |
| Docs updated | ⬜ | |
| Architecture compliance | ⬜ | |
| Security review | ⬜ | |

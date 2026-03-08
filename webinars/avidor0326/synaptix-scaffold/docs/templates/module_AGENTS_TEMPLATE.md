# {{MODULE_NAME}} — AGENTS.md (Tier-3)

> **Module-specific rules.**  
> Inherits from: `{{PARENT_AGENTS_PATH}}` (Tier-2) → root `AGENTS.md` (Tier-1)

---

## Identity

**Module:** `{{MODULE_NAME}}`  
**Domain:** `{{DOMAIN}}` (backend | frontend | ml-ai-data | shared)  
**Purpose:** {{MODULE_PURPOSE}}  
**Role tag:** `[DEV:{{MODULE_NAME}}|{{DOMAIN_TAG}}]`  
Where `{{DOMAIN_TAG}}` is one of: `BE` | `FE` | `ML` | `SHARED`

---

## Scope

### What this module owns
- {{CAPABILITY_1}}
- {{CAPABILITY_2}}
- {{CAPABILITY_3}}

### What this module does NOT own
- {{OUT_OF_SCOPE_1}} → owned by `{{OTHER_MODULE_OR_ROLE}}`
- {{OUT_OF_SCOPE_2}} → escalate to `[CTO]`

---

## Contracts

### Dependencies

| Dependency | Usage | Notes |
|------------|-------|-------|
| `shared/config` | Settings | Required |
| `shared/logging` | Logging | Required |
| `shared/exceptions` | Base errors | Required |
| {{DEPENDENCY_1}} | {{USAGE}} | {{NOTES}} |

### Public surface (what this module exposes)

| Export | Type | Description |
|--------|------|-------------|
| {{EXPORT_1}} | endpoint / hook / artifact | {{DESC}} |
| {{EXPORT_2}} | endpoint / hook / artifact | {{DESC}} |

### Domain-specific hard constraints
- **BE:** {{BE_CONSTRAINTS_OR_NA}}
- **FE:** UI kit compliance + accessibility + responsiveness → {{FE_CONSTRAINTS_OR_NA}}
- **ML:** reproducibility + eval gates + golden set → {{ML_CONSTRAINTS_OR_NA}}
- **SHARED:** backward compatibility guarantees → {{SHARED_CONSTRAINTS_OR_NA}}

---

## Required reading order

Before any deep work, read in this order:

1. Root `AGENTS.md` (global roles + behaviors)
2. `{{PARENT_AGENTS_PATH}}` (domain Tier-2 rules)
3. `docs/00_INDEX.md`
4. `docs/0k_PRD.md`
5. `docs/01_ARCHITECTURE.md`
6. `docs/03_MODULES.md` (capability map — avoid duplication)
7. `docs/04_TESTING.md` (coverage gates)
8. Current sprint: `docs/sprints/{{SPRINT_ID}}/{{SPRINT_ID}}_index.md`
9. Your sprint todo: `docs/sprints/{{SPRINT_ID}}/todo/{{SPRINT_ID}}_team_dev_{{MODULE_NAME}}_todo.md`

**FE only:** also read `docs/ui/UI_KIT.md` before touching any component.

---

## Development flow

1. **Read** — complete reading order above
2. **Plan** — summarize intended changes + files; surface risks and assumptions
3. **Develop** — implement smallest slice; reuse-first from `shared/` and SynaptixLabs AGENTS framework
4. **Test** — TDD; run unit → integration → E2E/regression as applicable
5. **Report** — post short update to sprint report: what changed, what's left, risks
6. **Review** — respond to DR feedback fast; patch don't argue
7. **Finalize** — update module README + contract refs
8. **Acceptance** — crisp checklist; mark DONE only after `[FOUNDER]` acceptance

If blocked at any step: raise a **FLAG** (GOOD/BAD/UGLY + recommendation) and escalate.

---

## Definition of Done

- [ ] Code implemented per PRD + architecture constraints
- [ ] Tests pass (unit + integration + E2E/regression as applicable)
- [ ] Coverage meets gate (≥90% unit)
- [ ] Module README updated
- [ ] `docs/03_MODULES.md` updated if capabilities changed
- [ ] Sprint report written
- [ ] Cross-module changes reviewed by `[CTO]`
- [ ] `[FOUNDER]` acceptance recorded

---

## Testing

| Type | Location | Coverage Target |
|------|----------|-----------------|
| Unit | `tests/unit/` | ≥90% |
| Integration | `tests/integration/` | Key paths |
| Regression | `tests/regression/` | All bug fixes |

### Key test scenarios
- {{TEST_SCENARIO_1}}
- {{TEST_SCENARIO_2}}

---

## Escalation triggers

Escalate to `[CTO]` before:
- Adding new external dependencies
- Changing public API contracts
- Any cross-module or schema changes
- {{ESCALATION_MODULE_SPECIFIC_1}}
- {{ESCALATION_MODULE_SPECIFIC_2}}

---

## Extraction mode (if applicable)

> Fill if this module was created by extracting from existing code.

| Field | Value |
|-------|-------|
| Source path | `{{SOURCE_PATH}}` |
| Extraction date | `{{DATE}}` |
| Inventory file | `{{INVENTORY_PATH}}` |
| DR checkpoint | `{{DR_PATH}}` |

---

## Vibe costs

| Task | Vibes |
|------|-------|
| {{TASK_1}} | {{VIBES_1}} V |
| {{TASK_2}} | {{VIBES_2}} V |
| Bug fix + regression test | 2–4 V |

---

## Module-specific rules

{{MODULE_SPECIFIC_RULES}}

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| {{DATE}} | Initial creation | {{AUTHOR}} |

---

*Last updated: {{DATE}}*

# WINDSURF — GLOBAL RULES (VIBE CODING)

> Applies to **all** Windsurf Cascade conversations across **all** projects.
> The repo is truth. Chats are working memory.

---

## 0) Prime Directive
This is **VIBE CODING**.
- The primary workforce is **LLM agents** (not humans).
- Reduce drift via: **roles + artifacts + templates + gates**.
- Prefer deterministic outputs (docs/tests/code) over conversational text.
- **Measure everything in Vibes** (see §1a).

---

## 1a) Vibes: The Universal Measure

**1 Vibe = 1,000 tokens** (input + output combined)

All tasks are estimated and tracked in Vibes:

| Task Type | Typical Vibes | Example |
|-----------|---------------|---------|
| Simple fix | 1–3 V | Typo fix, config change |
| Single function + tests | 3–8 V | New API endpoint with tests |
| Module feature | 8–25 V | Auth flow with tests + docs |
| Cross-module work | 25–50 V | Integration between 2+ modules |
| Sprint (small) | 50–150 V | 3–5 features with tests |
| Sprint (medium) | 150–300 V | Full module implementation |

### Vibe Tracking Protocol

Every substantive response **should include**:

```
## Vibe Report
- Task: <description>
- Estimated: <X> V
- Consumed: <Y> V (this response)
- Remaining: <Z> V (if multi-turn)
```

### Vibe Budgets

| Scope | Budget | Escalation |
|-------|--------|------------|
| Single task | 50 V max | Split into subtasks if exceeded |
| Feature | 150 V max | Requires CTO approval to exceed |
| Sprint | 500 V max | Requires Founder approval to exceed |

**If approaching budget limit:** Stop, report status, request guidance before proceeding.

---

## 1) Always identify yourself
Every response must start with a role tag:
- `[CPO]` `[CTO]` `[DEV:<module>]` `[REVIEW]` `[FOUNDER]`

If unsure which role you are: default to `[CTO]` and ask for the intended role only if blocking.

---

## 2) Repo-first workflow
1) If a repo exists: **read** `docs/00_INDEX.md` first.
2) Treat documentation as the source of truth:
   - requirements in PRD
   - decisions in DECISIONS/ADR
   - architecture in ARCHITECTURE
   - capabilities in MODULE registry
3) If something is missing: create a minimal stub file in the correct location and proceed.

Never “invent” project structure. If structure is unknown, use the template structure defined by this organization.

---

## 3) No meetings (strict)
- **NO MEETINGS**. Ever.
- Coordination happens via:
  - sprint docs
  - PRs
  - decision logs

---

## 4) Communication protocol: Good / Bad / Ugly
Use this when reviewing docs, code, designs, DRs, or plans.
- **GOOD**: what works and should remain
- **BAD**: issues that reduce quality or cause drift
- **UGLY → FIX**: concrete patch proposals with file paths and exact edits

---

## 5) Quality gates (non-negotiable)
### Test data policy
- Default: **synthetic / fixtures / generated** test data.
- **No real customer/production data** in tests or demos unless explicitly approved and anonymized.

### Testing strategy
- Unit → Integration → System → E2E → Regression.
- TDD is preferred: tests before implementation.

### Coverage policy (pragmatic)
- Backend services: **>=90%** line coverage + critical-path integration tests.
- Frontend: prioritize **Playwright E2E** + key component tests (don’t game coverage).
- ML: pipeline tests + evaluation scripts; metrics gates matter more than coverage.

---

## 6) Artifact rules (what to write where)
### Mandatory docs (always expected in projects)
- `docs/00_INDEX.md`
- `docs/01_ARCHITECTURE.md`
- `docs/02_SETUP.md`
- `docs/03_MODULES.md` (capabilities / reuse registry)
- `docs/04_TESTING.md`
- `docs/05_DEPLOYMENT.md`

### Indexed core docs (recommended in this org)
- `docs/0k_PRD.md`
- `docs/0l_DECISIONS.md` (ADR-style, short entries)

### UI prerequisite
If the project has a frontend:
- require `docs/ui/UI_KIT.md` before serious FE work.

---

## 7) Sprint structure (organization standard)
Each sprint lives under `docs/sprints/sprint_XX/`.
Required:
- `sprint_XX_index.md` (goal + links)
- `todo/sprint_XX_team_dev_<module>_todo.md` (one per module)
- `reports/sprint_XX_team_dev_<module>_report.md` (one per module)
- `reviews/sprint_XX_DR_<topic>.md` (as needed)
- `reviews/sprint_XX_requirements_delta.md` (PRD delta for the sprint)
- `ARCHIVE/sprint_XX_decisions_log.md`

Not used in this org:
- `sprint_XX_team_cpo_todo.md`
- `sprint_XX_team_cto_todo.md`

---

## 8) Reuse-first policy
Before building anything:
1) Check `docs/03_MODULES.md` for existing capabilities.
2) If it exists, reuse it. Don’t duplicate.
3) Prefer SynaptixLabs framework libraries (agent runtime, CLI, testing runner, global mocks) when available.
4) Cross-project utilities go under `/shared/`.

---

## 9) AGENTS.md (directory-scoped rules)
- Follow `AGENTS.md` automatically when working inside its directory scope.
- Layering is expected:
  - root `AGENTS.md` (project-wide)
  - `frontend/AGENTS.md`, `backend/AGENTS.md`, `ml-ai-data/AGENTS.md`
  - module-level `*/<module>/AGENTS.md`

Keep each AGENTS.md short. Long content belongs in `/docs/` or `/docs/templates/`.

---

## 10) Output expectations
When producing work, always include:
- File path(s)
- What changed (bullets)
- If editing: provide “before → after” snippets for key lines
- Next steps (1–3 bullets)

Avoid wall-of-text. Prefer structured markdown.

---

## 11) Safety / correctness
- Don’t claim you ran code unless you actually did.
- Don’t assume unstated requirements.
- Ask only when blocked; otherwise proceed with best-effort and document assumptions.

---

## 12) Dependency & configuration safety (non-negotiable)
- **Dependencies:** do not add new third-party deps (or major upgrades) without explicit human approval.
  - When proposing: name, version, why needed, alternatives, risk, rollback.
- **Sensitive configs:** never overwrite or auto-edit:
  - `.env*`, secrets files, credentials, CI/CD configs, build configs
  - unless the human explicitly asks for it (and you show a patch first).
- Prefer minimal, reversible changes; document assumptions.

---

## 13) Mocking policy (dev/test allowed, prod forbidden)
- Mocks/stubs are allowed in:
  - **tests**, and
  - **local/dev** workflows (especially FE) **behind a clear switch** (flag/env/route).
- **Never ship mocks to production paths**.
- FE mock-first is encouraged to avoid BE blocking, but must remain contract-aligned (types/schema).

---

## 14) Scope discipline & cross-scope changes
- Default: modify files only within the current working scope implied by:
  - active path + nearest `AGENTS.md` + sprint todo.
- Cross-scope edits are allowed **only** when:
  - the repo’s ops/module-permissions rules explicitly allow it (e.g., sprint docs, module registry, decision logs), or
  - the human explicitly approves.
- If scope is unclear: raise a **FLAG** (GOOD/BAD/UGLY) with a recommended path.


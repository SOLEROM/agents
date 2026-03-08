# /project:sprint-kickoff — Create a New Sprint

Plan and scaffold a new sprint for this project.

## Steps

1. **Read** the previous sprint to understand what shipped and what carried over:
   - Find the latest completed sprint in `docs/sprints/`
   - Read its index, status tracker, and any DR/reports

2. **Read** current project state:
   - PRD / product backlog (`docs/0k_PRD.md` or equivalent)
   - Architecture constraints (`docs/01_ARCHITECTURE.md`)
   - Capability map (`docs/03_MODULES.md`)
   - Open decisions (`docs/0l_DECISIONS.md`)
   - `CLAUDE.md` — current sprint field

3. **Propose** to FOUNDER before creating any files:
   - Sprint goal (one sentence, demoable outcome)
   - Scope: what's IN, what's explicitly OUT
   - Teams needed and assignments
   - Key risks / dependencies
   - "First demo" definition

4. **After FOUNDER approval**, create the sprint scaffold:

   ```
   docs/sprints/sprint_XX/
   ├── 00_INDEX.md                  # Sprint overview, goals, teams, scope
   ├── SPRINT_CURRENT_STATE.md      # Quick-ref for agent kickoffs (update each cycle)
   ├── todo/
   │   ├── sprint_XX_team_dev_todo.md
   │   ├── sprint_XX_team_qa_todo.md
   │   └── sprint_XX_team_<other>_todo.md
   ├── reports/                     # (empty — filled during sprint)
   └── reviews/                     # (empty — filled during sprint)
   ```

5. **Each TODO file** must contain:
   - Team identity + scope boundaries
   - Ordered task list with acceptance criteria
   - File paths to create/modify
   - Dependencies on other teams (explicit)
   - Test deliverables (unit + E2E commands)
   - Estimated effort (vibes)

6. **Update** `CLAUDE.md` sprint context field.

## Definition of Done (per sprint)

- [ ] All sprint features meet acceptance criteria
- [ ] All tests pass (unit + integration + E2E)
- [ ] Type check clean
- [ ] Demo script verified
- [ ] Sprint report written and Avi sign-off received

## Output

Sprint index + all TODO files + `SPRINT_CURRENT_STATE.md` + updated `CLAUDE.md`.

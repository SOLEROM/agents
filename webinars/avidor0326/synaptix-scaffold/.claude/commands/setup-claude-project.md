# /project:setup-claude-project — Generate Claude Projects System Prompt

Generate a complete, paste-ready CTO agent for this project.

## What this command does

Reads the current project's PRD, architecture, and stack → fills in `CPTO_agent_TEMPLATE.md` → outputs a ready-to-paste Claude Projects system prompt AND a patched `role_cto.md` for Windsurf.

## Instructions for Claude

1. Read `docs/0k_PRD.md` and `docs/01_ARCHITECTURE.md`
2. Extract:
   - Project name + one-line purpose
   - Tech stack (languages, frameworks, DBs, hosting)
   - Team roles (DEV, QA, CPO — which are active?)
   - Coverage targets (use defaults if not specified: ≥80% logic, ≥60% infra)
   - Testing frameworks (Jest+Playwright for web, pytest for Python)
   - Key technical constraints (privacy, performance, compliance)
3. Fill in `docs/templates/CPTO_agent_TEMPLATE.md` with all project-specific values
4. Output the filled template as a code block (ready to copy into Claude Projects)
5. Also output a patched `.windsurf/rules/role_cto.md` with all placeholders resolved
6. List the files to upload as Project Knowledge (PRD, arch, modules, testing, current sprint)

## Output format

```
## Claude Projects System Prompt
[paste-ready content — copy this into Claude Projects]

## role_cto.md patch
[diff or full replacement for .windsurf/rules/role_cto.md]

## Project Knowledge files to upload
- docs/0k_PRD.md
- docs/01_ARCHITECTURE.md
- docs/03_MODULES.md
- docs/04_TESTING.md
- [current sprint index if exists]

## First query to run
"What is our project?"
```

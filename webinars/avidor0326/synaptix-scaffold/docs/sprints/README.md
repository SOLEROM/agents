# Sprints folder

Each sprint gets its own folder under `docs/sprints/`.

## Canonical structure

```text
docs/sprints/sprint_XX/
├── sprint_XX_index.md
├── sprint_XX_decisions_log.md                 # optional but recommended
├── reviews/
│   ├── sprint_XX_requirements_delta.md
│   └── sprint_XX_DR_<topic>.md
├── todo/
│   └── sprint_XX_team_dev_<module>_todo.md
└── reports/
    └── sprint_XX_team_dev_<module>_report.md
```

## Naming rules

- `sprint_XX_...` uses **zero-padded** sprint numbers (`sprint_00`, `sprint_01`, …).
- Module files must include the module name and team:
  - `team_dev_<module>_todo.md`
  - `team_dev_<module>_report.md`

## Templates

Copy from: `docs/templates/sprints/`

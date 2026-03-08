# /project:design-review — CTO Design Review

Perform a design review using the Good/Bad/Ugly method.

## Steps

1. **Identify scope** — what is being reviewed? (sprint deliverable, module, architecture change, PR)
2. **Read** all relevant source files, specs, and docs
3. **Assess** using the framework below
4. **Output** the review document to `docs/sprints/sprint_XX/reports/DR_<topic>_<date>.md`

## Review Framework

### GOOD (keep)
What works well and should be preserved. Give explicit credit.

### BAD (fix)
What needs fixing. Categorize by priority:
- **P0** — blocks merge/release
- **P1** — fix this sprint
- **P2** — fix next sprint
- **P3** — backlog / nice-to-have

### UGLY (systemic)
Patterns or architectural issues that aren't broken today but will cause pain. Needs strategic attention.

## For each issue

```
- ID: B01 / U01
- Severity: P0/P1/P2/P3
- Location: exact file path + line range
- Problem: what's wrong
- Fix: concrete recommendation
- Effort: ~X vibes
```

## Standard checks (all projects)

- [ ] TypeScript: no `any`, no suppressed errors
- [ ] No hardcoded strings (i18n compliance)
- [ ] No inline styles where a design system class exists
- [ ] Unit tests for all new logic
- [ ] E2E coverage for new user-facing flows
- [ ] No regressions on previously accepted features
- [ ] Module boundaries respected (no cross-module direct imports)
- [ ] AGENTS.md updated if module behavior changed
- [ ] No new dependencies added without CPTO FLAG

## Output

End with:
- Overall grade (A / B / C / D / F with +/−)
- Prioritized fix list (P0 first)
- What to cut or defer
- Explicit next steps

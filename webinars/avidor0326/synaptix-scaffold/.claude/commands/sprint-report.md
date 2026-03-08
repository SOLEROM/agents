# /project:sprint-report — Sprint Status Report Generator

Generate a concise, accurate sprint status report for the current project.

## Steps

1. **Read** the current sprint index: `docs/sprints/sprint_XX/sprint_XX_index.md`
2. **Read** all todo files: `docs/sprints/sprint_XX/todo/`
3. **Read** any existing reports: `docs/sprints/sprint_XX/reports/`
4. **Check** actual code state vs planned deliverables
5. **Synthesize** into the report below

## Output Format

```
## Sprint [XX] Status Report — [PROJECT] — [DATE]
**Branch:** [current branch]
**Sprint goal:** [one-line goal from index]

---

### ✅ Done (shipped + tested)
- [item] — [brief note on how verified]

### 🔄 In Progress
- [item] — [% complete estimate] — ETA: [estimate]

### ❌ Blocked
- [item] — Blocked by: [reason] — Needs: [what to unblock]

### ⏭️ Deferred (moved to backlog)
- [item] — Reason: [why deferred]

---

### 🎯 Sprint Goal Assessment
**Will we hit the sprint goal?** YES / AT RISK / NO
**Reason:** [1 sentence]

---

### Quality Gates
| Gate | Status |
|------|--------|
| Unit tests passing | ✅/❌ |
| E2E smoke passing | ✅/❌ |
| No regressions | ✅/❌ |
| Type check clean | ✅/❌ |
| Demo-ready | ✅/❌ |

---

### Next Actions (top 3)
1. [action] — Owner: [role] — Priority: P0/P1/P2
2. [action] — Owner: [role] — Priority: P0/P1/P2
3. [action] — Owner: [role] — Priority: P0/P1/P2

---

### Open Decisions Needed
- [decision 1] — Owner: [FOUNDER/CTO/CPO]
```

## After report

If sprint is **complete**: run `/project:regression` then request Avi sign-off.
If sprint is **at risk**: surface blockers to Avi immediately.

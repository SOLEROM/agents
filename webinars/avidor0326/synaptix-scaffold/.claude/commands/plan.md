# /project:plan — Force Plan Mode for Complex Tasks

**Invoke BEFORE starting any task that:**
- Touches more than 2 files
- Involves a user-facing flow change
- Crosses module boundaries
- Requires infrastructure/dependency changes
- Involves migration or extraction work

## What to produce

Before writing ANY code, produce this plan and **STOP**:

```
## Task: [description]
**Role:** [CTO / CPO / DEV:module]

### Impact assessment
Files to touch: [list with full paths]
Modules affected: [list]
Cross-boundary changes: YES/NO — [explain if yes]
One-way doors: YES/NO — [list if yes, propose mitigation]
New dependencies: YES/NO — [list if yes, requires CTO FLAG]

### Approach
Step 1: [action] → [file path]
Step 2: [action] → [file path]
Step 3: [action] → [file path]

### Test plan
- Unit: [what to test + command]
- Integration: [what to test + command]
- E2E: [user flows to verify]

### Risks / assumptions
- [risk/assumption 1]
- [risk/assumption 2]

### Scope boundary
✅ In scope: [explicit list]
❌ Out of scope: [explicit list]

### Estimate
~X Vibes (1 Vibe = 1K tokens)
```

## After producing the plan

**STOP. Wait for Avi approval before executing.**

Only proceed when Avi says "go", "approved", "proceed", or equivalent.

If in doubt: over-plan. Plans are cheap. Broken code is expensive.

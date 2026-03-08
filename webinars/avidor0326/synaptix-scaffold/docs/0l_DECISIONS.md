# {{PROJECT_NAME}} — Decision Log

> **Architecture Decision Records (ADR)**  
> Owner: CTO  
> Log all significant technical and product decisions here.

---

## How to Use

1. **Before making a decision:** Check if similar decision exists
2. **When deciding:** Create new entry using template below
3. **Status progression:** Proposed → Accepted → Superseded/Deprecated

---

## Decision Index

| ID | Title | Status | Date |
|----|-------|--------|------|
| ADR-001 | {{TITLE}} | Accepted | {{DATE}} |
| ADR-002 | {{TITLE}} | Proposed | {{DATE}} |

---

## Decisions

### ADR-001: {{DECISION_TITLE}}

**Status:** Accepted  
**Date:** {{DATE}}  
**Decider:** {{ROLE}}  
**Vibes:** {{X}} V (to implement)

#### Context
{{CONTEXT_DESCRIPTION}}

#### Decision
{{DECISION_DESCRIPTION}}

#### Consequences

**Positive:**
- {{POSITIVE_1}}
- {{POSITIVE_2}}

**Negative:**
- {{NEGATIVE_1}}

**Neutral:**
- {{NEUTRAL_1}}

#### Alternatives Considered

| Alternative | Pros | Cons | Why Rejected |
|-------------|------|------|--------------|
| {{ALT_1}} | {{PROS}} | {{CONS}} | {{REASON}} |
| {{ALT_2}} | {{PROS}} | {{CONS}} | {{REASON}} |

---

### ADR-002: [Template]

**Status:** Proposed | Accepted | Superseded | Deprecated  
**Date:** YYYY-MM-DD  
**Decider:** [CPO/CTO/Founder]  
**Vibes:** X V (estimated implementation cost)

#### Context
What is the issue that we're seeing that is motivating this decision?

#### Decision
What is the change that we're proposing and/or doing?

#### Consequences
What becomes easier or more difficult to do because of this change?

**Positive:**
- 

**Negative:**
- 

**Neutral:**
- 

#### Alternatives Considered
| Alternative | Pros | Cons | Why Rejected |
|-------------|------|------|--------------|
| | | | |

---

## Status Definitions

| Status | Meaning |
|--------|---------|
| **Proposed** | Under discussion, not yet decided |
| **Accepted** | Decision made, implementation allowed |
| **Superseded** | Replaced by another decision (link to new ADR) |
| **Deprecated** | No longer valid, should not be followed |

---

## Quick Add Template

```markdown
### ADR-XXX: {{Title}}

**Status:** Proposed  
**Date:** {{DATE}}  
**Decider:** {{ROLE}}  
**Vibes:** X V

#### Context
{{Why is this decision needed?}}

#### Decision
{{What did we decide?}}

#### Consequences
**Positive:**
- 

**Negative:**
- 
```

---

*Last updated: {{DATE}}*

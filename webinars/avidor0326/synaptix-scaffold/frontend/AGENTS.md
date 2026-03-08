# Frontend — AGENTS.md (Tier-2)

> Frontend-wide rules for this repo.
> Inherits from: `../AGENTS.md` (Tier-1), Windsurf Global Rules, and `.windsurf/rules/*` (workspace rules if present).
> Module-specific constraints belong in: `frontend/<module>/AGENTS.md` (Tier-3).

---

## Scope

**Directory:** `frontend/`
**What counts as frontend:** user-facing web UI / PWA, routing, client state, UI components, client-side integrations.

Concrete stack decisions are defined in:
- `docs/01_ARCHITECTURE.md` (frameworks, libraries, conventions)
- `docs/ui/UI_KIT.md` (design system + components)
- `docs/04_TESTING.md` (test tools + strategy)

---

## Mandatory tags (canonical)

Every frontend message MUST start with:
- `[DEV:<module>|FE]`

Examples:
- `[DEV:dashboard|FE]`
- `[DEV:auth-ui|FE]`
- `[DEV:admin-panel|FE]`

If you’re doing repo-wide FE platform work (rare):
- `[DEV:frontend-platform|FE]`

---

## Non-negotiables (frontend)

### 1) UI Kit is the source of truth (UI-KIT-first)
- **Serious FE work requires** `docs/ui/UI_KIT.md` (design tokens, components, UX rules, patterns).
- If `docs/ui/UI_KIT.md` is missing or incomplete:
  1) **Do not invent UI.**
  2) Ask `[FOUNDER]` / `[DESIGNER]` for missing decisions.
  3) Create a stub `docs/ui/UI_KIT.md` containing only: open questions, placeholders, and proposed options.

If SynaptixLabs framework provides shared UI-kit assets/components in this project:
- Use them as the implementation baseline.
- Do not fork or copy/paste the design system into ad-hoc local variants.

### 2) Reuse-first (do not reinvent the wheel)
- Prefer existing frameworks, component libraries, and patterns already in the repo.
- Agents are senior and should propose modern approaches, BUT:
  - no new major FE dependencies without `[CTO]` + `[FOUNDER]` approval
  - propose at least one “reuse what we already have” option before suggesting a new library
- open source or part of a popular framework.
- Before adding any new dependency:
  - check `docs/01_ARCHITECTURE.md` and `docs/03_MODULES.md`
  - propose alternatives that reuse what exists
  - escalate for approval if still needed

### 3) Usability & UX are first-class
- Treat usability and experience as part of the definition of done.
- Be **proactive**: if flows are confusing, inconsistent, or outdated, raise it.
- Accessibility is mandatory for interactive UI (keyboard, focus, semantics, labels).

### 4) PWA + responsiveness is the default pattern
- Design mobile-first responsive layouts by default.
- Treat installability and app-like behavior as a baseline when relevant (PWA).
- Consider slow-network/poor-device performance as a standard constraint.

---

## Recommended stack defaults (unless overridden)

Unless `docs/01_ARCHITECTURE.md` says otherwise, default to:
- **TypeScript** (strict)
- **React** (modern)
- **Next.js** (modern router)
- Utility-first styling (Tailwind) OR project design-system CSS
- **Playwright** for E2E

(Exact versions and tooling live in `docs/01_ARCHITECTURE.md`.)

---

## Mock-first development (essential)

Frontend should NOT be blocked by backend availability.

- Frontend must NOT be blocked by backend availability.
- If SynaptixLabs framework provides a global mock service / mock contract layer in this project: **use it**.
- Otherwise use a local mock server (e.g., MSW or equivalent per stack).
- Maintain stable mock fixtures aligned with API contracts.
- Prefer contract-driven mocks:
  - OpenAPI/proto/GraphQL schema → generate types → mock responses

If backend contract is missing/unstable:
- escalate to `[CTO]` with a short recommendation (contract-first).

---

## Testing requirements (frontend)

Follow org policy (Windsurf global rules), plus:

### 1) Component/unit tests
- Component behavior (props, events, states)
- Accessibility checks for critical components

### 2) Integration tests
- Key flows spanning multiple components (routing/state)

### 3) E2E tests (Playwright)
- Auth (login/logout)
- Core user journeys (happy path + 1–2 key edge paths)
- PWA/responsive smoke checks where relevant

**Do not chase coverage vanity metrics.** Focus on critical flows + regressions.

---

## Performance standards
- Optimize Core Web Vitals where relevant.
- Prefer Next.js/React-native optimizations: splitting, lazy loading, image optimization.
- Avoid heavy dependencies unless justified.

---

## Guardrails — when to stop & escalate

Escalate to `[CTO]` and/or `[FOUNDER]` (using GOOD/BAD/UGLY) before:
- Introducing a new UI kit / component library
- Introducing new state management libraries (beyond baseline)
- Major route/layout redesign impacting multiple modules
- Shipping UI that knowingly violates accessibility requirements
- Adding a new major FE platform dependency

---

## Tier-3 reminder

Every FE module MUST have `frontend/<module>/AGENTS.md` defining:
- module purpose + boundaries
- key flows + screens
- dependency contracts (APIs mocked vs real)
- UX constraints from the UI Kit
```

---

## Optional: ultra-short “UI_KIT missing” stub template

If you need a starter stub for `docs/ui/UI_KIT.md`, use:

```md
# UI KIT (Stub)

## Status
- Missing items: (list)
- Open decisions: (list)

## Foundations
- Typography:
- Colors:
- Spacing:
- Components:

## UX Rules
- Navigation patterns:
- Forms:
- Tables:
- Empty/loading/error states:

## Accessibility baseline
- Keyboard:
- Focus:
- Labels:
```

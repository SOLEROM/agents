# ML / AI / Data — AGENTS.md (Tier-2)

> ML/AI/Data-wide rules for this repo.
> Inherits from: `../AGENTS.md` (Tier-1), Windsurf Global Rules, and `.windsurf/rules/*` (workspace rules if present).
> Module-specific constraints belong in: `ml-ai-data/<module>/AGENTS.md` (Tier-3).

---

## Scope

**Directory:** `ml-ai-data/`

What counts as ML/AI/Data here:
- data ingestion/cleaning/transforms
- feature engineering + labeling
- training/inference pipelines
- evaluation harnesses + metric gates
- agentic/LLM components (orchestration, tools, prompt contracts, quality checks)

Concrete choices for stack/tools live in:
- `docs/01_ARCHITECTURE.md` (frameworks, runtimes, infra)
- `docs/04_TESTING.md` (test + eval strategy)
- `docs/03_MODULES.md` (capabilities + reuse map)

---

## Mandatory tags (canonical)

Every ML/AI/Data message MUST start with:
- `[DEV:<module>|ML]`

Examples:
- `[DEV:risk-scoring|ML]`
- `[DEV:feature-pipeline|ML]`
- `[DEV:agentic-orchestrator|ML]`

If you’re doing shared ML platform work (rare):
- `[DEV:ml-platform|ML]`

---

## Non-negotiables: SynaptixLabs Agentic Framework (core tech)
SynaptixLabs Agentic Framework is the default substrate for ALL projects in this org.

Therefore ML/AI/Data agents MUST:
1) If SynaptixLabs framework libraries are present in the project: **reuse them first** (agent runtime, orchestration, tool contracts, eval harnesses, CLI/testing/mocks).
2) If not yet integrated: **do not build a competing framework**. Implement only thin adapters and open a task to integrate the framework.
3) If a required capability is missing:
   - propose an extension to the framework (preferred), or
   - propose a minimal local adapter that conforms to the framework’s interfaces.

Before building anything new:
- check `docs/03_MODULES.md`
- check `/shared/` and SynaptixLabs packages used by this repo

---

## Reproducibility (operational, not aspirational)

### Environment
- Pin environments (lock files, Docker images, exact versions).
- Log runtime details (python/node versions, CUDA, driver info if relevant).

### Data
- Track dataset identity (versioned dataset, snapshot, or deterministic query + timestamp).
- Validate schema and ranges before training and inference.

### Experiments
- Every experiment run must record:
  - code version (git commit)
  - config/params
  - dataset identity
  - metrics
  - artifacts (model, tokenizer, prompts, configs)
- Use the project’s chosen tracking mechanism (defined in `docs/01_ARCHITECTURE.md`).

---

## Baselines, metrics, and evaluation gates

### Always start with a baseline
- Compare to a simple baseline (heuristic / linear model / previous best).

### Define metrics explicitly
- Classic ML: AUC/F1/PR-AUC, RMSE/MAE, calibration, latency/cost.
- Data pipelines: correctness checks, completeness, freshness, cost.
- Agentic/LLM (mandatory eval dimensions):
  - task success rate on a fixed golden set
  - tool-call correctness (schema + arguments + sequencing)
  - output faithfulness / hallucination controls where measurable
  - latency + cost budgets
  - regression gates vs last accepted version

### Required evaluation outputs
- train/val/test metrics (or offline eval splits)
- error analysis (top failures)
- regression comparison vs last accepted model
- group-wise metrics when fairness matters (healthcare especially)

**Rule:** do not ship a model/agent that is not clearly better than baseline or fails reproducibility.

---

## Data governance & safety

- No PII leakage in logs, artifacts, or exported datasets.
- Validate inputs at boundaries; fail loudly on schema mismatch.
- Keep sensitive features/labels documented (what, why, source, allowed use).
- If healthcare/regulatory constraints apply, escalate early.

---

## Serving & integration (contract-first)

- Wrap ML/agentic capabilities behind stable interfaces:
  - API endpoints, batch jobs, or tool interfaces per SynaptixLabs framework.
- Define typed I/O schemas.
- Add contract tests where possible.
- Measure and monitor:
  - latency + error rates
  - drift/quality regressions (when applicable)

---

## Testing requirements (ML/AI/Data)

Follow org policy (Windsurf global rules), plus:

### Unit tests
- transforms, validators, feature functions, prompt/tool formatters

### Integration tests
- pipeline smoke test: data in → artifact out → prediction out
- agentic smoke test: tool contracts + deterministic scenarios

### Regression tests (gates)
- golden-set tests for core tasks
- metric threshold checks vs last accepted version
- bug → test rule: every bug fix adds a regression test

Prefer deterministic subsets and fixtures to keep tests fast.

---

## Reuse-first (no reinventing wheels)

- Use existing SynaptixLabs abstractions for:
  - orchestration
  - tool interface contracts
  - eval harnesses
  - config/logging/testing helpers

New major dependencies (new MLOps stacks, new orchestration frameworks, new feature stores) require `[CTO]` + `[FOUNDER]` approval.

---

## Guardrails — when to stop & escalate

Escalate to `[CTO]` and/or `[FOUNDER]` (GOOD/BAD/UGLY) before:
- Changing target label definitions or ground-truth rules
- Introducing a new data source with unclear quality/bias/rights
- Shipping an irreproducible model/agent
- Introducing a new orchestration framework (non-SynaptixLabs)
- Deploying models with unclear fairness/ethics implications
- Moving fast by skipping eval/monitoring on user-facing ML

---

## Tier-3 reminder

Every ML module MUST have `ml-ai-data/<module>/AGENTS.md` defining:
- purpose + boundaries
- dataset(s) + ownership
- evaluation plan + acceptance gates
- integration contracts (API/tool)
- required SynaptixLabs components to reuse
```

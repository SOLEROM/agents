# Templates policy

Goal: **one source of truth** without duplication.

## Mandatory “living” docs
These are part of the repo’s canonical documentation and should live under:
- `docs/` 

Examples:
- PRD skeletons, architecture/testing/deployment stubs
- module README templates that you expect to keep updated

## Optional scaffolding / snippets
These are optional starter assets and should live under:
- `templates/`

Examples:
- boilerplate code snippets
- one-off examples, sample configs, demo skeletons

## Rule
If a template is intended to become a maintained doc:
- put it in `docs/` (or `docs/_templates/`)
Otherwise:
- put it in `templates/`

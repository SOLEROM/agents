# {{PROJECT_NAME}} — Module Registry

> **🚨 CRITICAL: Check Before Building**  
> Owner: CPO  
> **Always search this file before implementing new capabilities.**

---

## How to Use

1. **Before building:** Search this document
2. **If capability exists:** Reuse it
3. **If similar exists:** Extend it
4. **If new:** Add entry here after implementation

---

## Module Index

| Domain | Module | Path | Owner | Status | Capabilities |
|--------|--------|------|-------|--------|--------------|
| BE | `_example` | `backend/modules/_example/` | — | 📘 Reference | Template module |

> **Note:** `_example` is a reference implementation. Copy it to start new modules:
> ```bash
> cp -r backend/modules/_example backend/modules/{{your_module}}
> ```

**Status Key:** 🟢 Active | 🟡 WIP | 🔴 Deprecated | 📘 Reference

---

## Capability Registry

### Core Services (shared/)

| Capability | Provides | Location | Do NOT Re-implement |
|------------|----------|----------|---------------------|
| Settings | `get_settings()` | `shared/config/` | Ad-hoc `.env` parsing |
| Logging | `setup_logging()` | `shared/logging/` | Custom log formatters |
| Database | Connection pool | `shared/db/` | Per-module connection code |
| Exceptions | Base exceptions | `shared/exceptions/` | Module-specific base errors |
| CLI Registry | Plugin loader | `shared/cli/` | Separate CLI systems |
| Validation | Common validators | `shared/validation/` | Duplicate validation logic |
| Testing | Factories, fixtures | `shared/testing/` | Per-module test utilities |

### Backend Modules

| Module | Provides | Location | Vibes to Use |
|--------|----------|----------|--------------|
| `_example` | Reference patterns | `backend/modules/_example/` | 0 V (copy only) |

### Frontend Modules

| Module | Provides | Location | Vibes to Use |
|--------|----------|----------|--------------|
| — | — | — | — |

---

## Cross-Module Dependencies

```
┌─────────────────────────────────────────┐
│              Module A                    │
└───────────────────┬─────────────────────┘
                    │ ✗ Direct dependency
                    ▼
┌─────────────────────────────────────────┐
│              Module B                    │
└─────────────────────────────────────────┘

          ✓ Correct Pattern:

┌─────────┐     ┌─────────┐     ┌─────────┐
│Module A │────▶│ shared/ │◀────│Module B │
└─────────┘     └─────────┘     └─────────┘
```

**Rule:** Modules depend on `shared/`, never on each other directly.

---

## Adding New Capabilities

### Checklist Before Adding

- [ ] Searched this document
- [ ] Checked `shared/` for utilities
- [ ] Confirmed no similar module exists
- [ ] CTO approved (if cross-module)

### Entry Template

```markdown
| {{DOMAIN}} | `{{module}}` | `{{domain}}/modules/{{module}}/` | `[DEV:{{module}}]` | 🟡 WIP | {{capabilities}} |
```

---

## Deprecations

| Date | Module | What Changed | Replacement |
|------|--------|--------------|-------------|
| — | — | — | — |

---

## Search Tips

- Use `Ctrl+F` to search this document
- Search by: capability name, export name, or module name
- If unsure, ask: "Does X exist?" before building

---

*Last updated: {{DATE}}*

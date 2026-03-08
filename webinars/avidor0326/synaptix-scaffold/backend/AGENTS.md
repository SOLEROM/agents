# Backend — AGENTS.md (Tier-2)

> **Backend-wide rules** for this repo.
> Inherits from: `../AGENTS.md` (Tier-1), Windsurf Global Rules.
> Module-specific constraints belong in: `backend/<module>/AGENTS.md` (Tier-3).

---

## Scope

**Directory:** `backend/`  
**What counts as backend:** anything behind an API boundary (HTTP/gRPC/GraphQL/queues/jobs), plus persistence and integrations.

---

## Mandatory Tags

Every backend message MUST start with:
- `[DEV:<module>|BE]`

Examples: `[DEV:auth|BE]`, `[DEV:billing|BE]`

---

## Module Structure (Required)

```
backend/modules/<module>/
├── README.md           # Module docs (required)
├── AGENTS.md           # Tier-3 rules (required)
├── src/
│   ├── __init__.py     # Public exports
│   ├── models.py       # Data models
│   ├── services.py     # Business logic
│   ├── api.py          # API endpoints
│   └── cli.py          # CLI plugin (auto-registers)
└── tests/
    ├── unit/
    └── integration/
```

---

## CLI Auto-Registration (Mandatory)

Modules **must** auto-register CLI commands via the plugin system.

### Plugin Contract

```python
# src/cli.py
from shared.cli import CLIPlugin, register_command

class {{Module}}Plugin(CLIPlugin):
    """CLI commands for {{module}} module."""
    
    namespace = "{{module}}"
    version = "1.0.0"
    description = "{{Module}} management commands"

    @register_command(
        name="list",
        description="List {{resources}}",
        params=[
            {"name": "status", "type": "choice", "choices": ["active", "all"]},
            {"name": "limit", "type": "int", "default": 10},
        ]
    )
    async def list_cmd(self, status: str = "active", limit: int = 10):
        # Implementation
        return {"items": [...], "count": ...}

def get_plugin():
    """Factory function for plugin discovery."""
    return {{Module}}Plugin()
```

### Plugin Discovery

Plugins are discovered automatically if:
1. Module has `src/cli.py` with `get_plugin()` function
2. Or explicitly listed in `plugins.yaml`

---

## API Conventions

### Endpoints

```
GET    /api/v1/{{resource}}           # List
POST   /api/v1/{{resource}}           # Create
GET    /api/v1/{{resource}}/{id}      # Read
PUT    /api/v1/{{resource}}/{id}      # Update
DELETE /api/v1/{{resource}}/{id}      # Delete
```

### Response Format

```json
{
  "data": { ... },
  "meta": {
    "version": "{{LOGIC_VERSION}}",
    "timestamp": "2026-01-08T12:00:00Z"
  }
}
```

### Error Format

```json
{
  "error": {
    "code": "{{ERROR_CODE}}",
    "message": "Human-readable message",
    "details": { ... }
  }
}
```

---

## Testing Requirements

| Level | Location | Coverage |
|-------|----------|----------|
| Unit | `tests/unit/` | ≥90% |
| Integration | `tests/integration/` | Critical paths |

### Test Naming

```
test_<function>_<scenario>_<expected>

Examples:
- test_create_user_valid_returns_201
- test_create_user_duplicate_email_raises_conflict
```

---

## Vibe Reference

| Task | Vibes |
|------|-------|
| New endpoint + tests | 5–10 V |
| New service function | 3–5 V |
| Bug fix + regression test | 2–4 V |
| CLI command + tests | 3–5 V |
| Full module scaffold | 15–25 V |

---

## Guardrails — When to Escalate

Escalate to `[CTO]` before:
- Adding a new backend stack or runtime
- Adding a new datastore (DB/cache/queue)
- Changing a public API used by other modules
- Introducing breaking migrations
- Skipping observability/testing

---

*Inherits from: `../AGENTS.md`*

# {{PROJECT_NAME}} — Architecture

> **System Design & Technical Architecture**  
> Owner: CTO

---

## Overview

{{PROJECT_DESCRIPTION}}

### Architecture Style
- [ ] Monolith
- [ ] Modular Monolith
- [ ] Microservices
- [ ] Serverless
- [ ] Hybrid

---

## System Diagram

```
┌─────────────────────────────────────────────────────────┐
│                      Frontend                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Web App   │  │  Mobile App │  │     CLI     │     │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘     │
└─────────┼────────────────┼────────────────┼─────────────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
                    ┌──────▼──────┐
                    │   API Layer  │
                    └──────┬──────┘
                           │
┌──────────────────────────┼──────────────────────────────┐
│                    Backend Modules                       │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │
│  │ Module A │  │ Module B │  │ Module C │  │ Module D │   │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘   │
└───────┼────────────┼────────────┼────────────┼──────────┘
        │            │            │            │
        └────────────┴─────┬──────┴────────────┘
                           │
                    ┌──────▼──────┐
                    │   Database   │
                    └─────────────┘
```

---

## Tech Stack

**Core framework (mandatory):** SynaptixLabs **AGENTS** agentic framework (agents, CLI, testing/mocks).
If something is missing, extend/adapt the framework — don’t fork a parallel one without `[CTO]` approval.

### Backend
| Component | Technology | Version |
|-----------|------------|---------|
| Language | {{BACKEND_LANG}} | {{VERSION}} |
| Framework | {{BACKEND_FRAMEWORK}} | {{VERSION}} |
| Database | {{DATABASE}} | {{VERSION}} |
| Cache | {{CACHE}} | {{VERSION}} |

### Frontend
| Component | Technology | Version |
|-----------|------------|---------|
| Framework | {{FRONTEND_FRAMEWORK}} | {{VERSION}} |
| Styling | {{STYLING}} | {{VERSION}} |
| State | {{STATE_MGMT}} | {{VERSION}} |

### Infrastructure
| Component | Technology |
|-----------|------------|
| Hosting | {{HOSTING}} |
| CI/CD | GitHub Actions |
| Monitoring | {{MONITORING}} |

---

## Module Architecture

See [03_MODULES.md](03_MODULES.md) for capability registry.

### Module Structure
```
backend/modules/<module_name>/
├── AGENTS.md           # Module-specific rules
├── README.md           # Module documentation
├── src/
│   ├── __init__.py
│   ├── models.py       # Data models
│   ├── services.py     # Business logic
│   ├── api.py          # API endpoints
│   └── cli.py          # CLI commands (auto-register)
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```

---

## API Design

### Conventions
- RESTful endpoints
- Versioned: `/api/v1/...`
- JSON responses
- Standard error format

### Authentication
{{AUTH_APPROACH}}

---

## Data Flow

```
Request → Validation → Service → Repository → Database
                ↓
            Response ← Transform ← Result
```

---

## Security Considerations

- [ ] Authentication
- [ ] Authorization
- [ ] Input validation
- [ ] Rate limiting
- [ ] Audit logging
- [ ] Secrets management

---

## Scalability

### Current Design
{{SCALABILITY_NOTES}}

### Future Considerations
- {{SCALE_CONSIDERATION_1}}
- {{SCALE_CONSIDERATION_2}}

---

## Decisions

Major architectural decisions logged in [0l_DECISIONS.md](0l_DECISIONS.md).

---

*Last updated: {{DATE}}*

# Changelog

All notable changes to the **Windsurf Projects Template** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2026-02-19

### Added

#### 🟢 Claude Code CLI Infrastructure (Dual-Native Support)
- **`CLAUDE.md`**: Generic project context template with `{{PLACEHOLDERS}}` — auto-loaded by Claude Code CLI on session start. Covers identity, commands, testing gates, architecture non-negotiables, E2E flows, deployment, and role tags.
- **`.claude/settings.local.json`**: Pre-configured permissions covering npm, poetry, git, docker-compose, pytest, uvicorn, playwright, and common shell commands. Deny-list for destructive operations (`git push --force`, `rm -rf`, `npm publish`).
- **`.claude/commands/test.md`**: `/project:test` — structured full test suite runner with server-awareness.
- **`.claude/commands/e2e.md`**: `/project:e2e` — Playwright MCP browser tests with screenshot-every-step requirement.
- **`.claude/commands/plan.md`**: `/project:plan` — force plan mode before any task touching >2 files.
- **`.claude/commands/regression.md`**: `/project:regression` — pre-merge gate with full quality checklist.
- **`.claude/commands/release-gate.md`**: `/project:release-gate` — pre-production checklist (code, security, infra, docs, demo readiness).
- **`.claude/commands/sprint-report.md`**: `/project:sprint-report` — sprint status report generator.

#### 🟢 README: Claude CLI Section
- New **"Claude Code CLI Support"** section documenting what's included, setup steps, Windsurf vs Claude CLI comparison table, and updated Sprint-0 checklist (items 11-13).

### Changed

#### 🟡 README: Sprint-0 checklist extended
- Items 11-13 added for Claude CLI setup.

#### 🟡 Template structure
- `CLAUDE.md` and `.claude/` added to Template Structure diagram.

---

## [0.3.0] - 2025-01-12

### Added

#### 🟢 Extraction Mode Gates (Prevents Invented Code)
- **`00_synaptix_ops.md`**: New "Extraction vs Invention" section with hard rules for migrations
- **Sprint todo template**: Extraction gates checklist for migration/porting tasks
- **Module permissions**: References extraction requirements

#### 🟢 Developer Role Instance Templates
- **`role_backend_dev.md`**: Backend developer role with FastAPI/SQLAlchemy patterns
- **`role_frontend_dev.md`**: Frontend developer role with React/Next.js/Tailwind patterns
- **`role_ml_dev.md`**: ML/AI developer role with reproducibility requirements
- **`role_shared_dev.md`**: Shared frameworks developer with backward compatibility rules
- All roles include project-specific configuration tables (like CTO/CPO)

#### 🟢 Module AGENTS Generator Template
- **`docs/templates/module_AGENTS_TEMPLATE.md`**: Template for consistent Tier-3 AGENTS.md files
- Includes capability declaration, directory structure, testing gates, and escalation triggers

#### 🟢 Repository Audit Script
- **`scripts/audit_repo_structure.py`**: Validates template compliance
- Checks: structure, Python version, extraction gates, async subprocess docs
- Detects unassigned template variables (`{{PROJECT_NAME}}` → FAIL, `{{VAR:default}}` → WARN)
- Windows-compatible with UTF-8 encoding

#### 🟢 CTO Pre-Release Checklist
- Integrated into **`role_cto.md`** (not a separate file)
- Code integrity, testing, security, documentation, and deployment gates
- Includes extraction verification for migration tasks

#### 🟢 Async Subprocess Guidance (CLI/TUI)
- **`docs/04_TESTING.md`**: New section with patterns for async subprocess testing
- Required tests: responsiveness, cancellation, timeout, streaming
- Code examples for each pattern

### Changed

#### 🟡 Python Version Gate
- **`docs/02_SETUP.md`**: Explicit Python 3.11-3.13 requirement (NOT 3.14+)
- **`pyproject.toml`**: Prominent version comment at top
- DoD checklist includes interpreter verification

#### 🟡 Context Router & Module Permissions
- **`20_context_router.md`**: Comprehensive path-to-role mappings
- **`10_module_agent_permissions.md`**: Module ownership table with role instance references
- **`01_artifact_paths.md`**: Complete registry including new dev role templates

#### 🟡 Sprint Templates
- **Sprint index template**: References CTO pre-release checklist
- **Sprint todo template**: Includes extraction gates for migration tasks

### Deprecated
- None

### Removed
- `docs/release/CHECKLIST_CTO_PRE_RELEASE.md` (content moved into `role_cto.md`)

### Fixed
- None

### Security
- None

---

## [0.2.0] - 2025-01-08

### Added
- Vibe measurement system (1 Vibe = 1,000 tokens)
- `_example` module in `backend/modules/` as reference implementation
- Sprint system with todos, reports, and decisions
- UI Kit documentation (`docs/ui/UI_KIT.md`)

### Changed
- Restructured documentation index
- Improved module capability registry

---

## [0.1.0] - 2025-01-05

### Added
- Initial template structure
- Tiered AGENTS.md system (Tier-1 → Tier-2 → Tier-3)
- Role prompts for CTO and CPO
- Windsurf rules (`00_synaptix_ops`, `01_artifact_paths`, etc.)
- Documentation templates (PRD, DECISIONS, CHANGELOG, SECURITY)
- Basic project structure (backend, frontend, shared, ml-ai-data)

---

## Version Legend

| Badge | Meaning |
|-------|---------|
| 🟢 **Added** | New features |
| 🟡 **Changed** | Changes to existing functionality |
| 🟠 **Deprecated** | Features to be removed in future |
| 🔴 **Removed** | Features removed in this release |
| 🔵 **Fixed** | Bug fixes |
| 🟣 **Security** | Security-related changes |

---

[Unreleased]: https://github.com/SynaptixLabs/Windsurf-Projects-Template/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/SynaptixLabs/Windsurf-Projects-Template/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/SynaptixLabs/Windsurf-Projects-Template/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/SynaptixLabs/Windsurf-Projects-Template/releases/tag/v0.1.0

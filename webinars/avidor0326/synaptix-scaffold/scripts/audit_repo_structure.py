#!/usr/bin/env python3
"""
Repo Structure Audit Script

Checks project structure and stability against template requirements.
Provides actionable feedback on missing files, mismatched structure, and compliance issues.

Usage:
    python scripts/audit_repo_structure.py [--fix] [--verbose]

Options:
    --fix       Attempt to create missing files with templates
    --verbose   Show all checks, not just failures
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

# Enable UTF-8 output on Windows
if sys.platform == "win32":
    # Try to enable UTF-8 mode
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except (AttributeError, OSError):
        pass

# ANSI colors for terminal output (disable on Windows if not supported)
USE_COLORS = os.environ.get("NO_COLOR") is None and (
    sys.platform != "win32" or os.environ.get("TERM") or os.environ.get("WT_SESSION")
)

if USE_COLORS:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
else:
    RED = GREEN = YELLOW = BLUE = RESET = BOLD = ""


@dataclass
class AuditResult:
    """Result of a single audit check."""

    name: str
    status: Literal["pass", "warn", "fail"]
    message: str
    fix_hint: str | None = None


@dataclass
class AuditReport:
    """Complete audit report."""

    results: list[AuditResult] = field(default_factory=list)

    @property
    def passed(self) -> int:
        return sum(1 for r in self.results if r.status == "pass")

    @property
    def warnings(self) -> int:
        return sum(1 for r in self.results if r.status == "warn")

    @property
    def failures(self) -> int:
        return sum(1 for r in self.results if r.status == "fail")

    @property
    def total(self) -> int:
        return len(self.results)

    @property
    def score(self) -> float:
        if self.total == 0:
            return 100.0
        return (self.passed / self.total) * 100


def find_repo_root() -> Path:
    """Find the repository root by looking for AGENTS.md."""
    current = Path.cwd()
    while current != current.parent:
        if (current / "AGENTS.md").exists():
            return current
        current = current.parent
    # Fallback to cwd
    return Path.cwd()


class RepoAuditor:
    """Audits repository structure against template requirements."""

    def __init__(self, root: Path, verbose: bool = False):
        self.root = root
        self.verbose = verbose
        self.report = AuditReport()

    def add_result(self, name: str, status: str, message: str, fix_hint: str | None = None):
        """Add an audit result."""
        self.report.results.append(AuditResult(name, status, message, fix_hint))

    def check_file_exists(self, path: str, required: bool = True, description: str = "") -> bool:
        """Check if a file exists."""
        full_path = self.root / path
        exists = full_path.exists()

        if exists:
            self.add_result(
                f"File: {path}",
                "pass",
                f"✓ {description or path} exists"
            )
        elif required:
            self.add_result(
                f"File: {path}",
                "fail",
                f"✗ Missing required file: {path}",
                f"Create {path} using appropriate template"
            )
        else:
            self.add_result(
                f"File: {path}",
                "warn",
                f"⚠ Optional file missing: {path}",
                f"Consider creating {path}"
            )
        return exists

    def check_dir_exists(self, path: str, required: bool = True) -> bool:
        """Check if a directory exists."""
        full_path = self.root / path
        exists = full_path.is_dir()

        if exists:
            self.add_result(f"Dir: {path}", "pass", f"✓ Directory {path} exists")
        elif required:
            self.add_result(
                f"Dir: {path}",
                "fail",
                f"✗ Missing required directory: {path}",
                f"mkdir -p {path}"
            )
        else:
            self.add_result(
                f"Dir: {path}",
                "warn",
                f"⚠ Optional directory missing: {path}"
            )
        return exists

    def audit_root_structure(self):
        """Audit root-level required files."""
        print(f"\n{BOLD}=== Root Structure ==={RESET}")

        # Required root files
        self.check_file_exists("AGENTS.md", True, "Tier-1 AGENTS (global constitution)")
        self.check_file_exists("README.md", True, "Project README")
        self.check_file_exists("pyproject.toml", True, "Python project config")
        self.check_file_exists(".gitignore", True, "Git ignore file")

        # Required root directories
        self.check_dir_exists("docs", True)
        self.check_dir_exists("backend", True)
        self.check_dir_exists("frontend", True)
        self.check_dir_exists("ml-ai-data", True)
        self.check_dir_exists("shared", True)
        self.check_dir_exists(".windsurf/rules", True)

    def audit_windsurf_rules(self):
        """Audit Windsurf rules configuration."""
        print(f"\n{BOLD}=== Windsurf Rules ==={RESET}")

        rules_dir = ".windsurf/rules"
        required_rules = [
            ("00_repo_entrypoint.md", "Entry point rule"),
            ("00_synaptix_ops.md", "Synaptix ops (always-on)"),
            ("01_artifact_paths.md", "Artifact paths registry"),
            ("10_module_agent_permissions.md", "Module permissions"),
            ("20_context_router.md", "Context router"),
            ("role_cto.md", "CTO role instance"),
            ("role_cpo.md", "CPO role instance"),
        ]

        for rule_file, desc in required_rules:
            self.check_file_exists(f"{rules_dir}/{rule_file}", True, desc)

        # Check for dev role templates
        dev_roles = [
            ("role_backend_dev.md", "Backend dev role"),
            ("role_frontend_dev.md", "Frontend dev role"),
            ("role_ml_dev.md", "ML dev role"),
            ("role_shared_dev.md", "Shared dev role"),
        ]

        for role_file, desc in dev_roles:
            self.check_file_exists(f"{rules_dir}/{role_file}", False, desc)

    def audit_docs_structure(self):
        """Audit documentation structure."""
        print(f"\n{BOLD}=== Documentation Structure ==={RESET}")

        required_docs = [
            ("docs/00_INDEX.md", "Documentation index"),
            ("docs/0k_PRD.md", "Product requirements"),
            ("docs/01_ARCHITECTURE.md", "Architecture doc"),
            ("docs/02_SETUP.md", "Setup guide"),
            ("docs/03_MODULES.md", "Module registry"),
            ("docs/04_TESTING.md", "Testing guide"),
            ("docs/05_DEPLOYMENT.md", "Deployment guide"),
            ("docs/0l_DECISIONS.md", "Decisions log"),
        ]

        for doc_path, desc in required_docs:
            self.check_file_exists(doc_path, True, desc)

        # Check for templates
        self.check_dir_exists("docs/templates", True)
        self.check_dir_exists("docs/templates/sprints", True)
        self.check_dir_exists("docs/sprints", True)

        # Check for UI Kit (required for FE projects)
        self.check_file_exists("docs/ui/UI_KIT.md", False, "UI Kit documentation")

    def audit_domain_structure(self, domain: str, domain_tag: str):
        """Audit a domain directory structure."""
        print(f"\n{BOLD}=== {domain.title()} Domain ==={RESET}")

        # Tier-2 AGENTS.md
        self.check_file_exists(f"{domain}/AGENTS.md", True, f"Tier-2 {domain} AGENTS")

        # Modules directory
        modules_dir = self.root / domain / "modules"
        if modules_dir.is_dir():
            self.add_result(
                f"Dir: {domain}/modules",
                "pass",
                f"✓ {domain}/modules directory exists"
            )

            # Check each module has required files
            for module_dir in modules_dir.iterdir():
                if module_dir.is_dir() and not module_dir.name.startswith("."):
                    self.audit_module(domain, module_dir.name, domain_tag)
        else:
            self.add_result(
                f"Dir: {domain}/modules",
                "warn",
                f"⚠ {domain}/modules directory missing (no modules yet)"
            )

    def audit_module(self, domain: str, module_name: str, domain_tag: str):
        """Audit a specific module's structure."""
        module_path = f"{domain}/modules/{module_name}"

        # Required module files
        self.check_file_exists(
            f"{module_path}/README.md",
            True,
            f"Module README for {module_name}"
        )
        self.check_file_exists(
            f"{module_path}/AGENTS.md",
            True,
            f"Tier-3 AGENTS for {module_name}"
        )

        # Source directory
        self.check_dir_exists(f"{module_path}/src", True)

        # Tests directory
        self.check_dir_exists(f"{module_path}/tests", True)
        self.check_dir_exists(f"{module_path}/tests/unit", False)

    def audit_shared_modules(self):
        """Audit shared framework modules."""
        print(f"\n{BOLD}=== Shared Frameworks ==={RESET}")

        self.check_file_exists("shared/AGENTS.md", True, "Tier-2 shared AGENTS")

        expected_shared = [
            "cli",
            "config",
            "db",
            "exceptions",
            "logging",
            "testing",
            "utils",
            "validation",
        ]

        for module in expected_shared:
            module_path = f"shared/{module}"
            if (self.root / module_path).is_dir():
                self.add_result(
                    f"Shared: {module}",
                    "pass",
                    f"✓ shared/{module} exists"
                )
                # Check for __init__.py
                self.check_file_exists(
                    f"{module_path}/__init__.py",
                    False,
                    f"shared/{module} init"
                )
            else:
                self.add_result(
                    f"Shared: {module}",
                    "warn",
                    f"⚠ shared/{module} not found (may not be needed)"
                )

    def audit_python_version(self):
        """Audit Python version configuration."""
        print(f"\n{BOLD}=== Python Version ==={RESET}")

        pyproject = self.root / "pyproject.toml"
        if pyproject.exists():
            content = pyproject.read_text(encoding="utf-8")
            if ">=3.11" in content and "<3.14" in content:
                self.add_result(
                    "Python version",
                    "pass",
                    "✓ Python version constraint is correct (>=3.11, <3.14)"
                )
            elif "python" in content.lower():
                self.add_result(
                    "Python version",
                    "warn",
                    "⚠ Python version found but may not match recommended (>=3.11, <3.14)",
                    "Update pyproject.toml: python = \">=3.11,<3.14\""
                )
            else:
                self.add_result(
                    "Python version",
                    "fail",
                    "✗ No Python version constraint found",
                    "Add to pyproject.toml: python = \">=3.11,<3.14\""
                )

    def audit_extraction_gates(self):
        """Audit extraction mode gates in ops rules."""
        print(f"\n{BOLD}=== Extraction Gates ==={RESET}")

        ops_file = self.root / ".windsurf/rules/00_synaptix_ops.md"
        if ops_file.exists():
            content = ops_file.read_text(encoding="utf-8")
            if "Extraction vs Invention" in content or "Extract vs Invent" in content:
                self.add_result(
                    "Extraction gates",
                    "pass",
                    "✓ Extraction mode gates defined in ops rules"
                )
            else:
                self.add_result(
                    "Extraction gates",
                    "fail",
                    "✗ Extraction mode gates missing from ops rules",
                    "Add 'Extraction vs Invention' section to 00_synaptix_ops.md"
                )
        else:
            self.add_result(
                "Extraction gates",
                "fail",
                "✗ Cannot check - ops file missing"
            )

    def audit_async_subprocess_docs(self):
        """Audit async subprocess documentation."""
        print(f"\n{BOLD}=== Async Subprocess Docs ==={RESET}")

        testing_file = self.root / "docs/04_TESTING.md"
        if testing_file.exists():
            content = testing_file.read_text(encoding="utf-8")
            if "async subprocess" in content.lower() or "CLI/TUI" in content:
                self.add_result(
                    "Async subprocess",
                    "pass",
                    "✓ Async subprocess guidance in testing docs"
                )
            else:
                self.add_result(
                    "Async subprocess",
                    "warn",
                    "⚠ Async subprocess guidance not found in testing docs",
                    "Add CLI/TUI testing section to docs/04_TESTING.md"
                )
        else:
            self.add_result(
                "Async subprocess",
                "fail",
                "✗ Cannot check - testing doc missing"
            )

    def audit_unassigned_variables(self):
        """Audit for unassigned template variables in key files."""
        print(f"\n{BOLD}=== Template Variables ==={RESET}")

        import re

        # Pattern to match {{VAR}} or {{VAR:default}} - we flag vars without defaults
        var_pattern = re.compile(r'\{\{([A-Z_][A-Z0-9_]*)\}\}')
        var_with_default_pattern = re.compile(r'\{\{([A-Z_][A-Z0-9_]*):([^}]+)\}\}')

        # Files to check for unassigned variables
        files_to_check = [
            # Role files
            ".windsurf/rules/role_cto.md",
            ".windsurf/rules/role_cpo.md",
            ".windsurf/rules/role_backend_dev.md",
            ".windsurf/rules/role_frontend_dev.md",
            ".windsurf/rules/role_ml_dev.md",
            ".windsurf/rules/role_shared_dev.md",
            # Doc files
            "docs/0k_PRD.md",
            "docs/01_ARCHITECTURE.md",
            "docs/02_SETUP.md",
            "docs/03_MODULES.md",
            "docs/04_TESTING.md",
            "docs/05_DEPLOYMENT.md",
        ]

        # Required variables that MUST be set (no defaults allowed)
        required_vars = {"PROJECT_NAME"}

        total_unassigned = 0
        required_missing = []

        for file_path in files_to_check:
            full_path = self.root / file_path
            if not full_path.exists():
                continue

            try:
                content = full_path.read_text(encoding="utf-8")
            except Exception:
                continue

            # Find variables without defaults
            vars_no_default = var_pattern.findall(content)
            # Find variables with defaults
            vars_with_default = var_with_default_pattern.findall(content)

            # Check for required vars that are still templated
            for var in vars_no_default:
                if var in required_vars:
                    required_missing.append((file_path, var))

            # Count unassigned (vars without defaults)
            unassigned = [v for v in vars_no_default if v not in [vd[0] for vd in vars_with_default]]
            if unassigned:
                total_unassigned += len(unassigned)

        if required_missing:
            # Group by file
            by_file = {}
            for file_path, var in required_missing:
                by_file.setdefault(file_path, []).append(var)

            for file_path, vars in by_file.items():
                self.add_result(
                    f"Required vars: {file_path}",
                    "fail",
                    f"✗ Required variables not set: {', '.join(vars)}",
                    f"Edit {file_path} and replace {{{{VAR}}}} with actual values"
                )
        else:
            self.add_result(
                "Required variables",
                "pass",
                "✓ All required variables are set or have defaults"
            )

        if total_unassigned > 0:
            self.add_result(
                "Template variables",
                "warn",
                f"⚠ {total_unassigned} template variables without defaults found",
                "Review and set project-specific values in role files"
            )
        else:
            self.add_result(
                "Template variables",
                "pass",
                "✓ All template variables have defaults or are set"
            )

    def run_full_audit(self) -> AuditReport:
        """Run all audit checks."""
        print(f"\n{BOLD}{BLUE}============================================================{RESET}")
        print(f"{BOLD}{BLUE}           REPO STRUCTURE AUDIT                           {RESET}")
        print(f"{BOLD}{BLUE}============================================================{RESET}")
        print(f"Repository: {self.root}")

        self.audit_root_structure()
        self.audit_windsurf_rules()
        self.audit_docs_structure()
        self.audit_domain_structure("backend", "BE")
        self.audit_domain_structure("frontend", "FE")
        self.audit_domain_structure("ml-ai-data", "ML")
        self.audit_shared_modules()
        self.audit_python_version()
        self.audit_extraction_gates()
        self.audit_async_subprocess_docs()
        self.audit_unassigned_variables()

        return self.report

    def print_report(self):
        """Print the audit report."""
        report = self.report

        print(f"\n{BOLD}{'='*60}{RESET}")
        print(f"{BOLD}AUDIT SUMMARY{RESET}")
        print(f"{'='*60}")

        # Score
        score = report.score
        if score >= 90:
            score_color = GREEN
        elif score >= 70:
            score_color = YELLOW
        else:
            score_color = RED

        print(f"\nScore: {score_color}{BOLD}{score:.1f}%{RESET}")
        print(f"  {GREEN}✓ Passed:{RESET} {report.passed}")
        print(f"  {YELLOW}⚠ Warnings:{RESET} {report.warnings}")
        print(f"  {RED}✗ Failures:{RESET} {report.failures}")
        print(f"  Total checks: {report.total}")

        # Print failures
        failures = [r for r in report.results if r.status == "fail"]
        if failures:
            print(f"\n{RED}{BOLD}FAILURES (must fix):{RESET}")
            for f in failures:
                print(f"  {RED}✗{RESET} {f.name}: {f.message}")
                if f.fix_hint:
                    print(f"    {BLUE}Fix:{RESET} {f.fix_hint}")

        # Print warnings
        warnings = [r for r in report.results if r.status == "warn"]
        if warnings:
            print(f"\n{YELLOW}{BOLD}WARNINGS (should fix):{RESET}")
            for w in warnings:
                print(f"  {YELLOW}⚠{RESET} {w.name}: {w.message}")
                if w.fix_hint:
                    print(f"    {BLUE}Fix:{RESET} {w.fix_hint}")

        # Verbose: print passes
        if self.verbose:
            passes = [r for r in report.results if r.status == "pass"]
            if passes:
                print(f"\n{GREEN}{BOLD}PASSED:{RESET}")
                for p in passes:
                    print(f"  {GREEN}✓{RESET} {p.name}")

        print(f"\n{'='*60}\n")

        return report.failures == 0


def main():
    parser = argparse.ArgumentParser(
        description="Audit repository structure against template requirements"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Attempt to create missing files with templates (not yet implemented)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show all checks, not just failures"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root (default: auto-detect)"
    )

    args = parser.parse_args()

    root = args.root or find_repo_root()

    auditor = RepoAuditor(root, verbose=args.verbose)
    auditor.run_full_audit()
    success = auditor.print_report()

    if args.fix:
        print(f"{YELLOW}--fix not yet implemented. See fix hints above.{RESET}")

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

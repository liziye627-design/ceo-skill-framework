#!/usr/bin/env python3
"""
CEO Linter - Validates CEO skill policy and artifact integrity.

Usage:
    python3 ceo_lint.py [--path /path/to/ceo/skill]
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import List, Tuple


class CEOValidator:
    """Validates CEO skill and related artifacts."""

    REQUIRED_SKILL_SECTIONS = [
        "Hard Trigger Gate",
        "Purpose",
        "Default Mode",
        "Execution Switch",
        "Execution Mode Subagent Policy",
        "Contents-First Protocol",
        "Routing",
        "Constraints",
        "Output Format",
    ]

    REQUIRED_YAML_FIELDS = ["name", "description", "category", "tags"]

    AGENT_COLOR_PATTERN = r"#([0-9A-Fa-f]{6})"

    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.issues: List[str] = []
        self.warnings: List[str] = []

    def validate(self) -> bool:
        """Run all validations."""
        if not self.skill_path.exists():
            self.issues.append(f"Skill file not found: {self.skill_path}")
            return False

        content = self.skill_path.read_text()
        self._validate_yaml_frontmatter(content)
        self._validate_required_sections(content)
        self._validate_agent_colors(content)
        self._validate_role_schema(content)

        return len(self.issues) == 0

    def _validate_yaml_frontmatter(self, content: str) -> None:
        """Check YAML frontmatter."""
        if not content.startswith("---"):
            self.issues.append("Missing YAML frontmatter delimiter")
            return

        # Extract frontmatter
        frontmatter_end = content.find("---", 3)
        if frontmatter_end == -1:
            self.issues.append("Unclosed YAML frontmatter")
            return

        frontmatter = content[3:frontmatter_end]

        for field in self.REQUIRED_YAML_FIELDS:
            if f"{field}:" not in frontmatter:
                self.issues.append(f"Missing required YAML field: {field}")

    def _validate_required_sections(self, content: str) -> None:
        """Check for required markdown sections."""
        for section in self.REQUIRED_SKILL_SECTIONS:
            if section not in content:
                self.warnings.append(f"Missing recommended section: {section}")

    def _validate_agent_colors(self, content: str) -> None:
        """Validate agent color codes."""
        colors = re.findall(self.AGENT_COLOR_PATTERN, content)
        valid_colors = set()

        for color in colors:
            if len(color) != 6:
                self.issues.append(f"Invalid hex color: #{color}")
            valid_colors.add(f"#{color}")

        if len(valid_colors) < 10:
            self.warnings.append(f"Only {len(valid_colors)} unique agent colors found")

    def _validate_role_schema(self, content: str) -> None:
        """Check role output schema definitions."""
        if "Base schema (all roles):" not in content:
            self.warnings.append("Missing base schema definition")

        if "Role-specific required fields:" not in content:
            self.warnings.append("Missing role-specific schema")

    def print_report(self) -> None:
        """Print validation results."""
        if not self.issues and not self.warnings:
            print("✅ All checks passed!")
            return

        if self.issues:
            print("\n❌ Issues found:")
            for issue in self.issues:
                print(f"  - {issue}")

        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"  - {warning}")

        if self.issues:
            print("\n❌ Validation failed")
            sys.exit(1)
        else:
            print("\n⚠️  Validation passed with warnings")


def main():
    parser = argparse.ArgumentParser(description="Validate CEO skill configuration")
    parser.add_argument(
        "--path",
        type=Path,
        default=Path.home() / ".claude" / "skills" / "ceo" / "SKILL.md",
        help="Path to CEO skill file",
    )
    args = parser.parse_args()

    validator = CEOValidator(args.path)
    if validator.validate():
        validator.print_report()
    else:
        validator.print_report()


if __name__ == "__main__":
    main()

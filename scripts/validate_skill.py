#!/usr/bin/env python3
"""Deterministic structural and privacy checks for the skill repository."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "references/CORE_PRINCIPLES.md",
    "references/AUTHORIZATION_MODEL.md",
    "references/EVIDENCE_HIERARCHY.md",
    "references/TASK_MODES.md",
    "references/SCOPE_CONTROL.md",
    "references/PROTECTED_ASSETS.md",
    "references/FROZEN_CAPABILITIES.md",
    "references/VERIFICATION_CONTRACT.md",
    "references/RELEASE_CONTRACT.md",
    "references/PROJECT_PROFILE_TEMPLATE.md",
    "adapters/chatgpt.md",
    "adapters/codex.md",
    "adapters/claude.md",
    "adapters/generic-agent.md",
    "examples/generic-project-profile/PROFILE.md",
    "tests/pressure-scenarios.md",
]

# Generic privacy patterns. The public distilled repository must not contain
# machine-specific paths, non-example email addresses, or obvious secret assignments.
PRIVATE_PATTERNS = [
    (re.compile(r"(?i)\b[a-z]:\\(?:users|documents and settings|programdata|projects)\\"), "machine-specific Windows path"),
    (re.compile(r"(?i)(?<![\w.-])(?:[\w.+-]+)@(?!(?:example\.(?:com|org|net)|example\.invalid)\b)[a-z0-9.-]+\.[a-z]{2,}(?![\w.-])"), "non-example email address"),
    (re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}['\"]"), "probable credential assignment"),
]

REQUIRED_SKILL_TERMS = [
    "AUDIT",
    "IMPLEMENT",
    "PROTECTED_ACTION_PENDING",
    "UNRESOLVED",
    "OUT_OF_SCOPE_FINDING",
    "REOPEN_RECOMMENDED",
]

FRONTMATTER_RE = re.compile(
    r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL
)
LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def text_files() -> list[Path]:
    result: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.suffix.lower() in {".md", ".py", ".txt"}:
            result.append(path)
    return result


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")


def check_frontmatter(errors: list[str]) -> None:
    path = ROOT / "SKILL.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append("SKILL.md must start with YAML frontmatter")
        return
    body = match.group("body")
    name = re.search(r"^name:\s*(.+)$", body, re.MULTILINE)
    desc = re.search(r"^description:\s*(.+)$", body, re.MULTILINE)
    if not name or not re.fullmatch(r"[a-z0-9-]+", name.group(1).strip()):
        errors.append("frontmatter name must use lowercase letters, numbers, and hyphens")
    if not desc or not desc.group(1).strip().startswith("Use when"):
        errors.append('frontmatter description must start with "Use when"')
    if desc and len(desc.group(1).strip()) > 500:
        errors.append("frontmatter description must be <= 500 characters")
    if len(match.group(0)) > 1024:
        errors.append("frontmatter must be <= 1024 characters")


def check_required_terms(errors: list[str]) -> None:
    path = ROOT / "SKILL.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for term in REQUIRED_SKILL_TERMS:
        if term not in text:
            errors.append(f"SKILL.md missing governance term: {term}")


def check_privacy(errors: list[str]) -> None:
    for path in text_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern, label in PRIVATE_PATTERNS:
            if pattern.search(text):
                errors.append(f"privacy pattern found in {rel}: {label}")


def check_relative_links(errors: list[str]) -> None:
    for path in text_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in LINK_RE.findall(text):
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository in {path.relative_to(ROOT)}: {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken relative link in {path.relative_to(ROOT)}: {target}")


def check_skill_size(errors: list[str]) -> None:
    path = ROOT / "SKILL.md"
    if not path.exists():
        return
    word_count = len(re.findall(r"\b\w+[\w'-]*\b", path.read_text(encoding="utf-8")))
    if word_count > 650:
        errors.append(f"SKILL.md is too large for a discovery entrypoint: {word_count} words > 650")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_frontmatter(errors)
    check_required_terms(errors)
    check_privacy(errors)
    check_relative_links(errors)
    check_skill_size(errors)
    if errors:
        print("VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION: PASS")
    print(f"Checked {len(REQUIRED_FILES)} required files and {len(text_files())} text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

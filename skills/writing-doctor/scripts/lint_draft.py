#!/usr/bin/env python3
"""Lint Chinese commentary drafts for banned template sentence patterns.

Usage:
  python scripts/lint_draft.py < draft.txt
  python scripts/lint_draft.py draft.txt

The script intentionally scans only the final draft text passed to it. Do not
run it on SKILL.md itself, because the skill documentation contains examples
of banned patterns.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


WINDOW = r"[^。！？!?；;\n]{0,100}"

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("不是……而是", re.compile(rf"不是{WINDOW}而是")),
    ("并不是……而是", re.compile(rf"并不是{WINDOW}而是")),
    ("并非……而是", re.compile(rf"并非{WINDOW}而是")),
    ("不要……要", re.compile(rf"不要{WINDOW}要")),
    ("没有……而是", re.compile(rf"没有{WINDOW}而是")),
    ("不是……是", re.compile(rf"不是{WINDOW}是")),
    ("……而不是……", re.compile(rf"而不是{WINDOW}")),
    ("别……要", re.compile(rf"别{WINDOW}要")),
]


def read_input(paths: list[str]) -> str:
    if not paths:
        return sys.stdin.read()

    chunks: list[str] = []
    for raw_path in paths:
        path = Path(raw_path)
        chunks.append(path.read_text(encoding="utf-8-sig"))
    return "\n".join(chunks)


def context(text: str, start: int, end: int, radius: int = 18) -> str:
    left = max(0, start - radius)
    right = min(len(text), end + radius)
    return text[left:right].replace("\n", "\\n")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description="Reject banned Chinese template sentence patterns."
    )
    parser.add_argument("paths", nargs="*", help="Draft text files. Reads stdin if omitted.")
    args = parser.parse_args()

    text = read_input(args.paths)
    hits: list[tuple[int, int, str, str]] = []

    for label, pattern in PATTERNS:
        for match in pattern.finditer(text):
            start, end = match.span()
            if any(not (end <= old_start or start >= old_end) for old_start, old_end, _, _ in hits):
                continue
            hits.append((start, end, label, context(text, start, end)))

    if hits:
        hits.sort(key=lambda item: item[0])
        print(f"BANNED_PATTERNS_FOUND: {len(hits)}")
        for index, (_, _, label, snippet) in enumerate(hits, start=1):
            print(f"{index}. {label}: {snippet}")
        return 1

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

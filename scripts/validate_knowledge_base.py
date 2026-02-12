#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
AGENTS = ROOT / "AGENTS.md"
DOCS_INDEX = DOCS_DIR / "index.md"

MAX_AGENTS_LINES = 120
MAX_VERIFIED_AGE_DAYS = 90

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
KV_RE = re.compile(r"^\s*([a-zA-Z0-9_]+)\s*:\s*(.*?)\s*$", re.MULTILINE)

ALLOWED_STATUS = {"draft", "verified", "deprecated"}


@dataclass
class DocMeta:
    owner: str
    status: str
    last_verified: date | None


def fail(msg: str) -> None:
    print(msg, file=sys.stderr)


def parse_frontmatter(path: Path, text: str) -> DocMeta | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None

    block = m.group(1)
    kv = {k: v for k, v in KV_RE.findall(block)}
    owner = kv.get("owner", "").strip()
    status = kv.get("status", "").strip()
    last_verified_raw = kv.get("last_verified", "").strip()

    last_verified = None
    if last_verified_raw:
        try:
            last_verified = datetime.strptime(last_verified_raw, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(
                f"{path}: invalid last_verified date format. Expected YYYY-MM-DD."
            )

    return DocMeta(owner=owner, status=status, last_verified=last_verified)


def main() -> int:
    errors: list[str] = []

    # 1) AGENTS.md constraints
    if not AGENTS.exists():
        errors.append(
            "Missing AGENTS.md (agent map). Create AGENTS.md and link to docs/index.md."
        )
    else:
        agents_text = AGENTS.read_text(encoding="utf-8")
        line_count = agents_text.count("\n") + 1
        if line_count > MAX_AGENTS_LINES:
            errors.append(
                f"AGENTS.md too long: {line_count} lines (max {MAX_AGENTS_LINES}). "
                f"Refactor into docs/ and keep AGENTS.md as a table of contents."
            )
        if (
            "docs/index.md" not in agents_text
            and str(DOCS_INDEX.relative_to(ROOT)) not in agents_text
        ):
            errors.append(
                "AGENTS.md must link to docs/index.md as the primary knowledge base entry point."
            )

    # 2) docs/index.md existence
    if not DOCS_INDEX.exists():
        errors.append(
            "Missing docs/index.md (knowledge base entry point). Create it and link from AGENTS.md."
        )

    # 3) Frontmatter + freshness checks
    if DOCS_DIR.exists():
        today = date.today()
        for md in DOCS_DIR.rglob("*.md"):
            if md.name == "index.md":
                continue
            text = md.read_text(encoding="utf-8")

            meta = None
            try:
                meta = parse_frontmatter(md, text)
            except ValueError as e:
                errors.append(str(e))
                continue

            if meta is None:
                errors.append(
                    f"{md}: missing frontmatter.\n"
                    "Add at the top:\n"
                    "---\n"
                    "owner: <team-or-person>\n"
                    "status: draft|verified|deprecated\n"
                    "last_verified: YYYY-MM-DD\n"
                    "---"
                )
                continue

            if not meta.owner:
                errors.append(
                    f"{md}: frontmatter missing 'owner'. Set owner to responsible party."
                )
            if meta.status not in ALLOWED_STATUS:
                errors.append(
                    f"{md}: invalid status '{meta.status}'. Allowed: {', '.join(sorted(ALLOWED_STATUS))}."
                )

            if meta.status == "verified":
                if meta.last_verified is None:
                    errors.append(
                        f"{md}: status=verified requires last_verified: YYYY-MM-DD."
                    )
                else:
                    age = (today - meta.last_verified).days
                    if age > MAX_VERIFIED_AGE_DAYS:
                        errors.append(
                            f"{md}: verified doc is stale ({age} days old). "
                            f"Update content and bump last_verified, or downgrade status to draft."
                        )

    else:
        errors.append(
            "Missing docs/ directory. Create docs/ as the knowledge base system of record."
        )

    if errors:
        fail("\n=== KNOWLEDGE BASE INVARIANT FAILED ===\n")
        for e in errors:
            fail(f"- {e}")
        fail(
            "\nRemediation (for agent):\n"
            "1) Keep AGENTS.md short and link to docs/index.md.\n"
            "2) Move detailed guidance into docs/.\n"
            "3) Ensure every docs/*.md has frontmatter with owner/status/last_verified.\n"
            "4) Refresh stale verified docs or downgrade to draft.\n"
        )
        return 1

    print("Knowledge base invariant OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

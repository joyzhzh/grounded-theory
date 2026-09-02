from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "MISSION_PORTFOLIO.md"

# MISSION_PORTFOLIO.md is the single registry of planning identities. Any
# renumbering happens there first; every other document may only cite it.
PATTERNS = {
    "lane": re.compile(r"GT-M01-L\d{2}"),
    "cell": re.compile(r"GT-M02-C\d{2}"),
    "frame": re.compile(r"GT-M02-F\d{2}"),
}
EXPECTED = {
    "lane": {f"GT-M01-L{i:02d}" for i in range(1, 17)},
    "cell": {f"GT-M02-C{i:02d}" for i in range(1, 13)},
    "frame": {f"GT-M02-F{i:02d}" for i in range(1, 9)},
}


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


class IdentityRegistryTest(unittest.TestCase):
    def test_registry_is_exact(self) -> None:
        text = PORTFOLIO.read_text(encoding="utf-8")
        for kind, pattern in PATTERNS.items():
            with self.subTest(kind=kind):
                self.assertEqual(set(pattern.findall(text)), EXPECTED[kind])

    def test_no_document_cites_an_unregistered_identity(self) -> None:
        for path in markdown_files():
            text = path.read_text(encoding="utf-8")
            for kind, pattern in PATTERNS.items():
                unknown = set(pattern.findall(text)) - EXPECTED[kind]
                with self.subTest(file=str(path.relative_to(ROOT)), kind=kind):
                    self.assertEqual(unknown, set(), f"unregistered {kind} identities: {sorted(unknown)}")


if __name__ == "__main__":
    unittest.main()

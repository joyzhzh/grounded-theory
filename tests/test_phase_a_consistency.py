from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
START = "START_HERE__20260902.md"
STATE = "`FIRE ORDERS ISSUED 2026-09-02 — NOT EXECUTED`"
STATE_FILES = ("README.md", "STATUS.md", "MISSION_PORTFOLIO.md", "RESEARCH_AGENDA.md")
ENTRY_POINT_FILES = ("README.md", "STATUS.md", "AGENTS.md")
# Wording retired by dated decisions. DECISIONS.md is history and may quote it.
RETIRED_WORDING = (
    "UNFIRED — PHASE A ARCHITECTURE DRAFT",
    "ANALYST_RECONSTRUCTED",
    "RESEARCHER_RECONSTRUCTED",
    "user's private",
    "user's detailed seedance",
    "private seedance",
    "own seedance",
    "operator's own",
)
HISTORY_FILES = {"DECISIONS.md"}
PIN = re.compile(r"evidence-first-deep-research-v2@([0-9a-f]{40})")


def documents() -> list[Path]:
    files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "tests" not in p.parts]
    files += [p for p in ROOT.rglob("*.json") if ".git" not in p.parts and "tests" not in p.parts]
    return sorted(files)


class PhaseAConsistencyTest(unittest.TestCase):
    def test_state_string_is_uniform(self) -> None:
        for name in STATE_FILES:
            with self.subTest(file=name):
                self.assertIn(STATE, (ROOT / name).read_text(encoding="utf-8"))

    def test_start_memo_is_the_entry_point(self) -> None:
        self.assertTrue((ROOT / START).is_file())
        for name in ENTRY_POINT_FILES:
            with self.subTest(file=name):
                self.assertIn(START, (ROOT / name).read_text(encoding="utf-8"))

    def test_protocol_pin_is_identical_everywhere(self) -> None:
        revision = json.loads((ROOT / "PROTOCOL.lock.json").read_text(encoding="utf-8"))["revision"]
        self.assertIn(revision, (ROOT / START).read_text(encoding="utf-8"))
        for path in documents():
            for found in PIN.findall(path.read_text(encoding="utf-8")):
                with self.subTest(file=str(path.relative_to(ROOT))):
                    self.assertEqual(found, revision)

    def test_no_retired_wording_outside_history(self) -> None:
        for path in documents():
            if path.name in HISTORY_FILES:
                continue
            text = path.read_text(encoding="utf-8").lower()
            for phrase in RETIRED_WORDING:
                with self.subTest(file=str(path.relative_to(ROOT)), phrase=phrase):
                    self.assertNotIn(phrase.lower(), text)

    def test_schema_version_agrees_across_schema_fixture_and_contract(self) -> None:
        schema = json.loads((ROOT / "schemas" / "manifest.schema.json").read_text(encoding="utf-8"))
        version = schema["properties"]["schema_version"]["const"]
        fixture = json.loads((ROOT / "examples" / "synthetic" / "C001" / "MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(fixture["schema_version"], version)
        contract = (ROOT / "references" / "analysis-packet-contract.md").read_text(encoding="utf-8")
        self.assertIn(f"schema {version}", contract.splitlines()[0])

    def test_crosswalk_cites_the_current_request_schema_hash(self) -> None:
        digest = hashlib.sha256((ROOT / "schemas" / "sampling-request.schema.json").read_bytes()).hexdigest()
        crosswalk = (ROOT / "references" / "vocabulary-crosswalk.md").read_text(encoding="utf-8")
        self.assertIn(digest, crosswalk, "sampling-request.schema.json changed; update the crosswalk and add a DECISIONS row")


if __name__ == "__main__":
    unittest.main()

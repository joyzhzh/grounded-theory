from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_analysis_packet.py"


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


class AnalysisPacketValidationTest(unittest.TestCase):
    def make_packet(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="gtw-packet-test-"))
        manifest = {
            "schema_version": "0.1-phase-a",
            "study_id": "SYNTHETIC",
            "cycle_id": "C001",
            "created_at_utc": "2026-09-02T00:00:00Z",
            "input_manifest_sha256": "a" * 64,
            "protocol_revision": "b" * 40,
            "analysis_status": "WORKING",
            "release_status": "NON_RELEASE",
            "saturation_status": "NOT_ASSESSED",
        }
        (root / "MANIFEST.json").write_text(json.dumps(manifest) + "\n", encoding="utf-8")
        write_jsonl(
            root / "EPISODES.jsonl",
            [{
                "episode_id": "E001",
                "boundary_basis": "SOURCE_EXPLICIT",
                "outcome_status": "ACCEPTED",
                "source_refs": ["MNF-SYNTHETIC"],
            }],
        )
        write_jsonl(
            root / "INCIDENTS.jsonl",
            [{
                "incident_id": "I001",
                "episode_id": "E001",
                "ordinal": 1,
                "epistemic_class": "OBSERVED_ACTION",
                "description": "Synthetic creator repeats an input.",
                "source_ref": {"manifestation_id": "MNF-SYNTHETIC", "locator": "event:1"},
            }],
        )
        write_jsonl(
            root / "CODES.jsonl",
            [{
                "code_id": "CDE001",
                "label": "repeating an input",
                "level": "FIRST_ORDER",
                "status": "CURRENT",
                "incident_ids": ["I001"],
            }],
        )
        write_jsonl(
            root / "CATEGORY_MEMOS.jsonl",
            [{
                "memo_id": "MEM001",
                "category_id": "CAT001",
                "status": "EMERGING",
                "definition": "Synthetic category for validator testing only.",
                "not_this": "Not a substantive research finding.",
                "supporting_code_ids": ["CDE001"],
                "negative_case_ids": [],
                "rival_explanations": ["fixture construction"],
            }],
        )
        write_jsonl(
            root / "SAMPLING_REQUESTS.jsonl",
            [{
                "request_id": "REQ001",
                "discriminating_question": "Does a contrasting synthetic fixture validate?",
                "targets": ["contrast"],
                "counter_search": "seek a non-repetition fixture",
                "stop_rule": "one synthetic contrast",
                "claim_ceiling": "validator behavior only",
                "status": "PROPOSED",
            }],
        )
        return root

    def run_validator(self, packet: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-B", str(VALIDATOR), str(packet)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_valid_packet_passes(self) -> None:
        result = self.run_validator(self.make_packet())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS_ANALYSIS_PACKET_STRUCTURE", result.stdout)

    def test_saturation_declaration_fails(self) -> None:
        packet = self.make_packet()
        manifest = json.loads((packet / "MANIFEST.json").read_text(encoding="utf-8"))
        manifest["saturation_status"] = "SATURATED"
        (packet / "MANIFEST.json").write_text(json.dumps(manifest) + "\n", encoding="utf-8")
        result = self.run_validator(packet)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot declare saturation", result.stderr)

    def test_inference_without_basis_fails(self) -> None:
        packet = self.make_packet()
        write_jsonl(
            packet / "INCIDENTS.jsonl",
            [{
                "incident_id": "I001",
                "episode_id": "E001",
                "ordinal": 1,
                "epistemic_class": "ANALYST_INFERENCE",
                "description": "The creator believed the model was incapable.",
            }],
        )
        result = self.run_validator(packet)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("inference_basis_ids", result.stderr)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_analysis_packet.py"
FIXTURE = ROOT / "examples" / "synthetic" / "C001"


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value: dict[str, object]) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


class AnalysisPacketValidationTest(unittest.TestCase):
    """Every test mutates a private copy of the committed synthetic fixture."""

    def make_packet(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="gt-packet-test-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        packet = root / "C001"
        shutil.copytree(FIXTURE, packet)
        return packet

    def run_validator(self, packet: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-B", str(VALIDATOR), str(packet)],
            text=True,
            capture_output=True,
            check=False,
        )

    def assert_passes(self, packet: Path) -> None:
        result = self.run_validator(packet)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS_ANALYSIS_PACKET_STRUCTURE", result.stdout)

    def assert_fails(self, packet: Path, fragment: str) -> None:
        result = self.run_validator(packet)
        self.assertNotEqual(result.returncode, 0, "validator accepted a packet it must reject")
        self.assertIn(fragment, result.stderr)

    def test_committed_fixture_passes(self) -> None:
        self.assert_passes(FIXTURE)

    def test_valid_copy_passes(self) -> None:
        self.assert_passes(self.make_packet())

    def test_saturation_declaration_fails(self) -> None:
        packet = self.make_packet()
        manifest = read_json(packet / "MANIFEST.json")
        manifest["saturation_status"] = "SATURATED"
        write_json(packet / "MANIFEST.json", manifest)
        self.assert_fails(packet, "cannot declare saturation")

    def test_inference_without_basis_fails(self) -> None:
        packet = self.make_packet()
        incidents = read_jsonl(packet / "INCIDENTS.jsonl")
        for row in incidents:
            if row["epistemic_class"] == "ANALYST_INFERENCE":
                row.pop("inference_basis_ids", None)
        write_jsonl(packet / "INCIDENTS.jsonl", incidents)
        self.assert_fails(packet, "inference_basis_ids")

    # --- rules added when the validator began applying the schemas ---

    def test_schema_files_parse_and_cover_every_packet_file(self) -> None:
        names = {p.name for p in (ROOT / "schemas").glob("*.schema.json")}
        self.assertEqual(
            names,
            {"manifest.schema.json", "episode.schema.json", "incident.schema.json", "code.schema.json",
             "category-memo.schema.json", "sampling-request.schema.json"},
        )
        for path in (ROOT / "schemas").glob("*.schema.json"):
            with self.subTest(schema=path.name):
                self.assertIsInstance(read_json(path), dict)

    def test_dangling_negative_case_fails(self) -> None:
        packet = self.make_packet()
        memos = read_jsonl(packet / "CATEGORY_MEMOS.jsonl")
        memos[0]["negative_case_ids"] = ["I999"]
        write_jsonl(packet / "CATEGORY_MEMOS.jsonl", memos)
        self.assert_fails(packet, "negative_case_ids")

    def test_dangling_construct_basis_fails(self) -> None:
        packet = self.make_packet()
        incidents = read_jsonl(packet / "INCIDENTS.jsonl")
        incidents.append({
            "incident_id": "I900", "episode_id": "E001", "ordinal": 90,
            "epistemic_class": "THEORETICAL_CONSTRUCT",
            "description": "Synthetic construct citing nothing real.",
            "construct_basis_ids": ["CDE999"],
        })
        write_jsonl(packet / "INCIDENTS.jsonl", incidents)
        self.assert_fails(packet, "construct_basis_ids")

    def test_duplicate_ordinal_within_episode_fails(self) -> None:
        packet = self.make_packet()
        incidents = read_jsonl(packet / "INCIDENTS.jsonl")
        incidents[1]["ordinal"] = incidents[0]["ordinal"]
        write_jsonl(packet / "INCIDENTS.jsonl", incidents)
        self.assert_fails(packet, "duplicate ordinal")

    def test_incident_manifestation_outside_its_episode_fails(self) -> None:
        packet = self.make_packet()
        incidents = read_jsonl(packet / "INCIDENTS.jsonl")
        incidents[0]["source_ref"]["manifestation_id"] = "MNF-SYNTHETIC-OTHER"
        write_jsonl(packet / "INCIDENTS.jsonl", incidents)
        self.assert_fails(packet, "not among episode")

    def test_non_iso_timestamp_fails(self) -> None:
        packet = self.make_packet()
        manifest = read_json(packet / "MANIFEST.json")
        manifest["created_at_utc"] = "yesterday"
        write_json(packet / "MANIFEST.json", manifest)
        self.assert_fails(packet, "created_at_utc")

    def test_superseded_code_without_successor_fails(self) -> None:
        packet = self.make_packet()
        codes = read_jsonl(packet / "CODES.jsonl")
        codes[0]["status"] = "SUPERSEDED"
        write_jsonl(packet / "CODES.jsonl", codes)
        self.assert_fails(packet, "no successor")

    def test_explicit_supersession_passes(self) -> None:
        packet = self.make_packet()
        codes = read_jsonl(packet / "CODES.jsonl")
        codes[0]["status"] = "SUPERSEDED"
        codes.append({
            "code_id": "CDE010", "label": "submitting a specification", "level": "FIRST_ORDER",
            "status": "CURRENT", "incident_ids": codes[0]["incident_ids"],
            "supersedes": codes[0]["code_id"], "supersession_reason": "Synthetic relabel for the test.",
        })
        write_jsonl(packet / "CODES.jsonl", codes)
        self.assert_passes(packet)

    def test_supersession_without_reason_fails(self) -> None:
        packet = self.make_packet()
        codes = read_jsonl(packet / "CODES.jsonl")
        codes[0]["status"] = "SUPERSEDED"
        codes.append({
            "code_id": "CDE010", "label": "submitting a specification", "level": "FIRST_ORDER",
            "status": "CURRENT", "incident_ids": codes[0]["incident_ids"], "supersedes": codes[0]["code_id"],
        })
        write_jsonl(packet / "CODES.jsonl", codes)
        self.assert_fails(packet, "supersession_reason")

    def test_authorized_request_without_authority_ref_fails(self) -> None:
        packet = self.make_packet()
        requests = read_jsonl(packet / "SAMPLING_REQUESTS.jsonl")
        requests[0]["status"] = "AUTHORIZED"
        write_jsonl(packet / "SAMPLING_REQUESTS.jsonl", requests)
        self.assert_fails(packet, "authority_ref")

    def test_emerging_category_without_support_fails(self) -> None:
        packet = self.make_packet()
        memos = read_jsonl(packet / "CATEGORY_MEMOS.jsonl")
        memos[0]["supporting_code_ids"] = []
        write_jsonl(packet / "CATEGORY_MEMOS.jsonl", memos)
        self.assert_fails(packet, "supporting_code_ids")

    def test_manifestation_identity_must_be_mnf_prefixed(self) -> None:
        packet = self.make_packet()
        episodes = read_jsonl(packet / "EPISODES.jsonl")
        episodes[0]["source_refs"] = [""]
        write_jsonl(packet / "EPISODES.jsonl", episodes)
        self.assert_fails(packet, "source_refs")


if __name__ == "__main__":
    unittest.main()

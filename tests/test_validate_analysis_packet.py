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


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Validate the Phase A structure of a grounded-theory analysis cycle."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_FILES = (
    "MANIFEST.json",
    "EPISODES.jsonl",
    "INCIDENTS.jsonl",
    "CODES.jsonl",
    "CATEGORY_MEMOS.jsonl",
    "SAMPLING_REQUESTS.jsonl",
)

EPISTEMIC_CLASSES = {
    "OBSERVED_ACTION",
    "CREATOR_REPORTED_ACTION",
    "CREATOR_STATED_INTERPRETATION",
    "THIRD_PARTY_INTERPRETATION",
    "TECHNOLOGY_COMPANY_CLAIM",
    "ANALYST_INFERENCE",
    "THEORETICAL_CONSTRUCT",
}

SOURCE_BASED_CLASSES = EPISTEMIC_CLASSES - {
    "ANALYST_INFERENCE",
    "THEORETICAL_CONSTRUCT",
}


class PacketError(ValueError):
    """A deterministic packet-contract failure."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PacketError(message)


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PacketError(f"{path.name}: cannot read valid JSON: {exc}") from exc
    require(isinstance(value, dict), f"{path.name}: root must be an object")
    return value


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise PacketError(f"{path.name}: cannot read: {exc}") from exc
    for number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise PacketError(f"{path.name}:{number}: invalid JSON: {exc}") from exc
        require(isinstance(row, dict), f"{path.name}:{number}: row must be an object")
        row["__line__"] = number
        rows.append(row)
    return rows


def required_text(row: dict[str, Any], field: str, where: str) -> str:
    value = row.get(field)
    require(isinstance(value, str) and value.strip() != "", f"{where}: {field} must be nonempty text")
    return value


def required_list(row: dict[str, Any], field: str, where: str) -> list[Any]:
    value = row.get(field)
    require(isinstance(value, list) and len(value) > 0, f"{where}: {field} must be a nonempty list")
    return value


def unique_ids(rows: list[dict[str, Any]], field: str, filename: str) -> set[str]:
    seen: set[str] = set()
    for row in rows:
        where = f"{filename}:{row['__line__']}"
        value = required_text(row, field, where)
        require(value not in seen, f"{where}: duplicate {field} {value}")
        seen.add(value)
    return seen


def validate_manifest(manifest: dict[str, Any]) -> None:
    required_text(manifest, "study_id", "MANIFEST.json")
    cycle_id = required_text(manifest, "cycle_id", "MANIFEST.json")
    require(re.fullmatch(r"C[0-9]{3,}", cycle_id) is not None, "MANIFEST.json: cycle_id must match C###")
    require(manifest.get("schema_version") == "0.1-phase-a", "MANIFEST.json: unsupported schema_version")
    required_text(manifest, "created_at_utc", "MANIFEST.json")
    input_sha = required_text(manifest, "input_manifest_sha256", "MANIFEST.json")
    require(re.fullmatch(r"[0-9a-f]{64}", input_sha) is not None, "MANIFEST.json: invalid input_manifest_sha256")
    protocol = required_text(manifest, "protocol_revision", "MANIFEST.json")
    require(re.fullmatch(r"[0-9a-f]{40}", protocol) is not None, "MANIFEST.json: protocol_revision must be an exact commit")
    require(manifest.get("analysis_status") in {"WORKING", "SUBMITTED_FOR_REVIEW"}, "MANIFEST.json: invalid analysis_status")
    require(manifest.get("release_status") == "NON_RELEASE", "MANIFEST.json: cycle packets must be NON_RELEASE")
    require(
        manifest.get("saturation_status")
        in {"NOT_ASSESSED", "NOT_REACHED", "PROVISIONAL_SUFFICIENCY_CANDIDATE"},
        "MANIFEST.json: saturation_status cannot declare saturation",
    )


def validate_packet(root: Path) -> None:
    require(root.is_dir(), f"packet root is not a directory: {root}")
    for filename in REQUIRED_FILES:
        require((root / filename).is_file(), f"missing required file: {filename}")

    validate_manifest(read_json(root / "MANIFEST.json"))
    episodes = read_jsonl(root / "EPISODES.jsonl")
    incidents = read_jsonl(root / "INCIDENTS.jsonl")
    codes = read_jsonl(root / "CODES.jsonl")
    category_memos = read_jsonl(root / "CATEGORY_MEMOS.jsonl")
    sampling = read_jsonl(root / "SAMPLING_REQUESTS.jsonl")

    episode_ids = unique_ids(episodes, "episode_id", "EPISODES.jsonl")
    incident_ids = unique_ids(incidents, "incident_id", "INCIDENTS.jsonl")
    code_ids = unique_ids(codes, "code_id", "CODES.jsonl")
    unique_ids(category_memos, "memo_id", "CATEGORY_MEMOS.jsonl")
    unique_ids(sampling, "request_id", "SAMPLING_REQUESTS.jsonl")

    for row in episodes:
        where = f"EPISODES.jsonl:{row['__line__']}"
        require(row.get("boundary_basis") in {"SOURCE_EXPLICIT", "ANALYST_RECONSTRUCTED", "UNCERTAIN"}, f"{where}: invalid boundary_basis")
        require(row.get("outcome_status") in {"ACCEPTED", "TRANSFORMED", "SUBSTITUTED", "DECOMPOSED", "POSTPONED", "ABANDONED", "UNKNOWN"}, f"{where}: invalid outcome_status")
        required_list(row, "source_refs", where)

    for row in incidents:
        where = f"INCIDENTS.jsonl:{row['__line__']}"
        require(required_text(row, "episode_id", where) in episode_ids, f"{where}: unknown episode_id")
        require(isinstance(row.get("ordinal"), int) and row["ordinal"] > 0, f"{where}: ordinal must be a positive integer")
        epistemic_class = required_text(row, "epistemic_class", where)
        require(epistemic_class in EPISTEMIC_CLASSES, f"{where}: invalid epistemic_class")
        required_text(row, "description", where)
        if epistemic_class in SOURCE_BASED_CLASSES:
            require(isinstance(row.get("source_ref"), dict), f"{where}: source-based class requires source_ref")
            required_text(row["source_ref"], "manifestation_id", f"{where}.source_ref")
            required_text(row["source_ref"], "locator", f"{where}.source_ref")
        if epistemic_class == "CREATOR_STATED_INTERPRETATION":
            required_text(row, "quote_ref", where)
        if epistemic_class == "ANALYST_INFERENCE":
            required_list(row, "inference_basis_ids", where)
        if epistemic_class == "THEORETICAL_CONSTRUCT":
            required_list(row, "construct_basis_ids", where)

    for row in codes:
        where = f"CODES.jsonl:{row['__line__']}"
        required_text(row, "label", where)
        require(row.get("level") in {"FIRST_ORDER", "IN_VIVO"}, f"{where}: invalid level")
        require(row.get("status") in {"CURRENT", "SUPERSEDED", "RETIRED"}, f"{where}: invalid status")
        for incident_id in required_list(row, "incident_ids", where):
            require(incident_id in incident_ids, f"{where}: unknown incident_id {incident_id}")

    for row in category_memos:
        where = f"CATEGORY_MEMOS.jsonl:{row['__line__']}"
        required_text(row, "category_id", where)
        status = required_text(row, "status", where)
        require(status in {"SENSITIZING_ONLY", "EMERGING", "FOCUSED", "SUPERSEDED", "RETIRED"}, f"{where}: invalid status")
        required_text(row, "definition", where)
        required_text(row, "not_this", where)
        support = row.get("supporting_code_ids")
        require(isinstance(support, list), f"{where}: supporting_code_ids must be a list")
        for code_id in support:
            require(code_id in code_ids, f"{where}: unknown supporting code {code_id}")
        if status in {"EMERGING", "FOCUSED"}:
            require(len(support) > 0, f"{where}: {status} category requires supporting codes")
        require(isinstance(row.get("negative_case_ids"), list), f"{where}: negative_case_ids must be a list")
        require(isinstance(row.get("rival_explanations"), list), f"{where}: rival_explanations must be a list")

    for row in sampling:
        where = f"SAMPLING_REQUESTS.jsonl:{row['__line__']}"
        required_text(row, "discriminating_question", where)
        required_list(row, "targets", where)
        required_text(row, "counter_search", where)
        required_text(row, "stop_rule", where)
        required_text(row, "claim_ceiling", where)
        require(row.get("status") in {"PROPOSED", "AUTHORIZED", "RETURNED", "CLOSED"}, f"{where}: invalid status")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, help="cycle packet directory")
    args = parser.parse_args()
    try:
        validate_packet(args.packet.resolve())
    except PacketError as exc:
        print(f"FAIL_ANALYSIS_PACKET: {exc}", file=sys.stderr)
        return 1
    print("PASS_ANALYSIS_PACKET_STRUCTURE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

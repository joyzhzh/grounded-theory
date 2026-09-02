#!/usr/bin/env python3
"""Validate the Phase A structure of a grounded-theory analysis cycle.

Row shapes are defined once, in ``schemas/*.schema.json``, and applied here
with ``jsonschema``. This script adds only the cross-file rules a per-row
schema cannot express: identity uniqueness, referential integrity, ordinal
uniqueness, manifestation containment, and supersession lifecycle.

Exit codes: 0 = PASS, 1 = FAIL, 2 = usage or missing dependency.
A PASS establishes structure only, never source truth, coding fidelity,
category quality, groundedness, sufficiency, saturation, admission, or release.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError:  # pragma: no cover - exercised only on hosts without the dependency
    jsonschema = None


SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"

# (packet file, schema name, identity field)
PACKET_FILES = (
    ("MANIFEST.json", "manifest", None),
    ("EPISODES.jsonl", "episode", "episode_id"),
    ("INCIDENTS.jsonl", "incident", "incident_id"),
    ("CODES.jsonl", "code", "code_id"),
    ("CATEGORY_MEMOS.jsonl", "category-memo", "memo_id"),
    ("SAMPLING_REQUESTS.jsonl", "sampling-request", "request_id"),
)

Row = dict[str, Any]


class PacketError(ValueError):
    """A deterministic packet-contract failure."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PacketError(message)


def load_schema(name: str) -> Any:
    path = SCHEMA_DIR / f"{name}.schema.json"
    schema = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema)


def schema_errors(validator: Any, row: Row) -> list[str]:
    errors = sorted(validator.iter_errors(row), key=lambda e: list(e.path))
    messages = []
    for error in errors:
        location = "/".join(str(p) for p in error.path) or "<row>"
        messages.append(f"{location}: {error.message}")
    return messages


def read_json(path: Path) -> Row:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PacketError(f"{path.name}: cannot read valid JSON: {exc}") from exc
    require(isinstance(value, dict), f"{path.name}: root must be an object")
    return value


def read_jsonl(path: Path) -> list[Row]:
    rows: list[Row] = []
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


def where(filename: str, row: Row) -> str:
    return f"{filename}:{row.get('__line__', '?')}"


def apply_schema(filename: str, validator: Any, rows: list[Row]) -> None:
    for row in rows:
        clean = {k: v for k, v in row.items() if k != "__line__"}
        errors = schema_errors(validator, clean)
        if errors:
            raise PacketError(f"{where(filename, row)}: {errors[0]}")


def unique_ids(filename: str, rows: list[Row], field: str) -> dict[str, Row]:
    by_id: dict[str, Row] = {}
    for row in rows:
        identifier = row[field]
        require(identifier not in by_id, f"{where(filename, row)}: duplicate {field} {identifier}")
        by_id[identifier] = row
    return by_id


def check_lifecycle(filename: str, rows: list[Row], field: str) -> None:
    """Supersession is explicit: a successor names its predecessor, and any row
    marked SUPERSEDED inside a packet must have that successor in the packet."""
    by_id = {row[field]: row for row in rows}
    superseded_by: dict[str, str] = {}
    for row in rows:
        target = row.get("supersedes")
        if target is None:
            continue
        require(target != row[field], f"{where(filename, row)}: row cannot supersede itself")
        if target in by_id:
            require(
                by_id[target].get("status") in {"SUPERSEDED", "RETIRED"},
                f"{where(filename, row)}: supersedes {target}, whose status is not SUPERSEDED or RETIRED",
            )
        superseded_by[target] = row[field]
    for row in rows:
        if row.get("status") == "SUPERSEDED":
            require(
                row[field] in superseded_by,
                f"{where(filename, row)}: SUPERSEDED row has no successor in the packet; append the successor or keep the row CURRENT",
            )


def validate_packet(root: Path) -> None:
    require(root.is_dir(), f"packet root is not a directory: {root}")
    for filename, _, _ in PACKET_FILES:
        require((root / filename).is_file(), f"missing required file: {filename}")

    validators = {name: load_schema(name) for _, name, _ in PACKET_FILES}

    manifest = read_json(root / "MANIFEST.json")
    errors = schema_errors(validators["manifest"], manifest)
    if errors:
        if errors[0].startswith("saturation_status"):
            raise PacketError(f"MANIFEST.json: saturation_status cannot declare saturation ({errors[0]})")
        raise PacketError(f"MANIFEST.json: {errors[0]}")

    episodes = read_jsonl(root / "EPISODES.jsonl")
    incidents = read_jsonl(root / "INCIDENTS.jsonl")
    codes = read_jsonl(root / "CODES.jsonl")
    category_memos = read_jsonl(root / "CATEGORY_MEMOS.jsonl")
    sampling = read_jsonl(root / "SAMPLING_REQUESTS.jsonl")

    apply_schema("EPISODES.jsonl", validators["episode"], episodes)
    apply_schema("INCIDENTS.jsonl", validators["incident"], incidents)
    apply_schema("CODES.jsonl", validators["code"], codes)
    apply_schema("CATEGORY_MEMOS.jsonl", validators["category-memo"], category_memos)
    apply_schema("SAMPLING_REQUESTS.jsonl", validators["sampling-request"], sampling)

    episodes_by_id = unique_ids("EPISODES.jsonl", episodes, "episode_id")
    incidents_by_id = unique_ids("INCIDENTS.jsonl", incidents, "incident_id")
    codes_by_id = unique_ids("CODES.jsonl", codes, "code_id")
    unique_ids("CATEGORY_MEMOS.jsonl", category_memos, "memo_id")
    unique_ids("SAMPLING_REQUESTS.jsonl", sampling, "request_id")

    basis_ids = set(incidents_by_id) | set(codes_by_id)
    ordinals: dict[str, set[int]] = {}
    for row in incidents:
        loc = where("INCIDENTS.jsonl", row)
        episode = episodes_by_id.get(row["episode_id"])
        require(episode is not None, f"{loc}: unknown episode_id {row['episode_id']}")
        seen = ordinals.setdefault(row["episode_id"], set())
        require(row["ordinal"] not in seen, f"{loc}: duplicate ordinal {row['ordinal']} within episode {row['episode_id']}")
        seen.add(row["ordinal"])
        source_ref = row.get("source_ref")
        if source_ref is not None:
            require(
                source_ref["manifestation_id"] in episode["source_refs"],
                f"{loc}: source_ref manifestation {source_ref['manifestation_id']} is not among episode {row['episode_id']} source_refs",
            )
        for field in ("inference_basis_ids", "construct_basis_ids"):
            for basis in row.get(field, []):
                require(basis != row["incident_id"], f"{loc}: {field} cannot cite the incident itself")
                require(basis in basis_ids, f"{loc}: {field} cites unknown incident or code {basis}")

    for row in codes:
        loc = where("CODES.jsonl", row)
        for incident_id in row["incident_ids"]:
            require(incident_id in incidents_by_id, f"{loc}: unknown incident_id {incident_id}")
    check_lifecycle("CODES.jsonl", codes, "code_id")

    case_ids = set(incidents_by_id) | set(episodes_by_id)
    for row in category_memos:
        loc = where("CATEGORY_MEMOS.jsonl", row)
        for code_id in row["supporting_code_ids"]:
            require(code_id in codes_by_id, f"{loc}: unknown supporting code {code_id}")
        for case_id in row["negative_case_ids"]:
            require(case_id in case_ids, f"{loc}: negative_case_ids cites unknown incident or episode {case_id}")
    check_lifecycle("CATEGORY_MEMOS.jsonl", category_memos, "memo_id")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("packet", type=Path, help="cycle packet directory")
    args = parser.parse_args()
    if jsonschema is None:
        print("FAIL_ANALYSIS_PACKET: the jsonschema package is required (python3 -m pip install jsonschema)", file=sys.stderr)
        return 2
    try:
        validate_packet(args.packet.resolve())
    except PacketError as exc:
        print(f"FAIL_ANALYSIS_PACKET: {exc}", file=sys.stderr)
        return 1
    print("PASS_ANALYSIS_PACKET_STRUCTURE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

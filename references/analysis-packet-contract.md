# Analysis packet contract — schema 0.1 Phase A

Each analytical cycle is a new directory. Historical cycles are immutable.

```text
C001/
  MANIFEST.json
  EPISODES.jsonl
  INCIDENTS.jsonl
  CODES.jsonl
  CATEGORY_MEMOS.jsonl
  SAMPLING_REQUESTS.jsonl
```

## Manifest

Required fields:

- `schema_version`: `0.1-phase-a`
- `study_id`, `cycle_id`, and `created_at_utc`
- `input_manifest_sha256`: lowercase SHA-256 of the frozen input manifest
- `protocol_revision`: exact 40-character commit
- `analysis_status`: `WORKING` or `SUBMITTED_FOR_REVIEW`
- `release_status`: always `NON_RELEASE` for an analysis cycle
- `saturation_status`: `NOT_ASSESSED`, `NOT_REACHED`, or
  `PROVISIONAL_SUFFICIENCY_CANDIDATE`

## Episodes

Each row has a unique `episode_id`, `boundary_basis`, `outcome_status`, and
nonempty `source_refs`. Allowed boundary bases are `SOURCE_EXPLICIT`,
`ANALYST_RECONSTRUCTED`, and `UNCERTAIN`. Unknown endings remain `UNKNOWN`.

## Incidents

Each row has `incident_id`, `episode_id`, positive integer `ordinal`, exactly
one `epistemic_class`, and `description`.

- Source-based classes require `source_ref` with manifestation identity and
  exact locator.
- `CREATOR_STATED_INTERPRETATION` also requires `quote_ref`.
- `ANALYST_INFERENCE` requires nonempty `inference_basis_ids`.
- `THEORETICAL_CONSTRUCT` requires nonempty `construct_basis_ids` and normally
  belongs in category/memo records rather than raw incidents.

## Codes

Each row has `code_id`, `label`, `level`, `status`, and nonempty
`incident_ids`. Phase A permits `FIRST_ORDER` and `IN_VIVO`; statuses are
`CURRENT`, `SUPERSEDED`, and `RETIRED`.

## Category memos

Each row has `memo_id`, `category_id`, `status`, `definition`, `not_this`,
`supporting_code_ids`, `negative_case_ids`, and `rival_explanations`.
`EMERGING` and `FOCUSED` categories require support. A category without support
must remain `SENSITIZING_ONLY`.

## Sampling requests

Each row has `request_id`, `discriminating_question`, nonempty `targets`,
`counter_search`, `stop_rule`, `claim_ceiling`, and status `PROPOSED`,
`AUTHORIZED`, `RETURNED`, or `CLOSED`. The tool may propose; only the
appropriate authority may authorize collection.

## Row schemas and cross-file rules

Row shapes are defined once, in `schemas/*.schema.json` (one schema per
packet file), and the validator applies them with `jsonschema`. Identity
formats are fixed: `E###` episodes, `I###` incidents, `CDE###` codes,
`MEM###` memos, `CAT###` categories, `REQ###` requests, and `MNF-…`
manifestations minted by the study vault. Timestamps are ISO-8601 UTC with a
`Z` suffix.

The validator adds only what a per-row schema cannot express:

- identities are unique within their file;
- every cited incident, code, episode, or negative case exists in the packet,
  and a basis list never cites its own incident;
- ordinals are unique within an episode;
- an incident's source manifestation is among its episode's `source_refs`;
- supersession is explicit: a successor row carries `supersedes` and
  `supersession_reason`, a `RETIRED` row carries `retirement_reason`, and a
  row marked `SUPERSEDED` inside a packet has its successor in that packet;
- a sampling request with status `AUTHORIZED`, `RETURNED`, or `CLOSED`
  names its `authority_ref`; the tool itself may only write `PROPOSED`.

## Validator ceiling

`validate_analysis_packet.py` checks structure and referential integrity. Its
PASS does not establish source truth, coding fidelity, category quality,
groundedness, sufficiency, saturation, evidence admission, or release.

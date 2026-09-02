# Vault and paper interface

## Sampling request to evidence vault

The grounded-theory tool sends a bounded request containing:

- request ID and provisional category or relationship;
- discriminating question;
- support, contradiction, boundary, rival, or negative-case targets;
- eligible source classes, languages, periods, and regimes;
- lawful-access and processing constraints;
- stop rule and claim ceiling; and
- required return fields.

This is a proposal, not acquisition authority.

## Evidence return

The evidence vault returns an immutable package lock with:

- exact vault snapshot and package-manifest hash;
- source and manifestation IDs and hashes;
- episode/event IDs, locators, and epistemic classes;
- quotation, translation, rights, privacy, and access state;
- source-lineage and deduplication state;
- negative cases, limitations, and unknowns; and
- status: `SUBMITTED_FOR_REVIEW`, `UNADJUDICATED`, `NON_RELEASE` unless a
  later independent record says otherwise.

Discovery snippets and generic summaries do not cross as evidence. Sharing
bytes and provenance does not share conclusions, category membership,
admission verdicts, saturation judgments, or publication authority.

## Paper handoff

A claim-bearing handoff must bind only current, independently admitted records
whose use is compatible with rights, privacy, quotation, translation, and
access restrictions. It includes construct boundaries, rivals, negative cases,
claim-to-record bindings, falsifiers, unresolved questions, and exact claim
ceilings.

Drafting, acceptance, release, and publication are separate decisions. A
fresh release auditor must inspect the exact draft surface.

## Paper drafting

`draft-paper` requires a frozen charter and a separately authorized author
seat. It consumes only the immutable adjudicated `GT_LITE`, current admitted
record bindings, and approved author-framing instructions. Each substantive
sentence maps to a current claim ID; author framing is visibly distinct. The
draft status is `DRAFT_NON_RELEASE`.

The author may not retrieve new evidence, revive superseded records, infer a
creator belief from behavior, strengthen a claim beyond its ceiling, declare
saturation, or authorize submission/publication. A correction to evidence or
analysis invalidates downstream draft bindings until they are replayed.

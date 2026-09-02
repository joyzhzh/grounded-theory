---
name: grounded-theory
description: Conduct auditable grounded-theory-oriented analysis through episode reconstruction, initial coding, constant comparison, memoing, theoretical sampling, negative-case analysis, and provenance-bound paper handoff. Use for learning or applying grounded-theory techniques to an authorized qualitative study; do not use it to acquire evidence, infer cognition from behavior, or autonomously declare saturation.
---

# Grounded Theory

Build process theory from authorized data without collapsing observation,
interpretation, inference, and theory.

## Choose a mode

- `orient` — explain the method, inspect the proposed study boundary, and draft
  a study charter. Do not ingest data.
- `prepare` — validate data authority, the source manifest, episode boundary,
  methodological profile, and external-vault layout.
- `pilot-code` — reconstruct and initial-code one explicitly bounded input
  packet. Preserve temporal order and uncertainty.
- `compare` — perform constant comparison and append comparison records,
  category changes, negative cases, and memos.
- `sample` — prepare a bounded theoretical-sampling request. Do not acquire
  sources or contact people.
- `integrate` — propose a provisional process model with rivals, conditions,
  consequences, falsifiers, and unresolved questions.
- `audit` — independently replay source bindings, epistemic classes,
  comparisons, negative cases, category changes, and stop language.
- `paper-handoff` — export a reviewed `GT_LITE` package. Do not clear or
  publish a paper.
- `draft-paper` — in a separately authorized author seat, draft from one
  immutable, independently adjudicated `GT_LITE` and current evidence package.
  Produce `DRAFT_NON_RELEASE`; add no unbound claim or new evidence.

Read [references/grounded-theory-contract.md](references/grounded-theory-contract.md)
before `pilot-code`, `compare`, `integrate`, or `audit`. Read
[references/analysis-packet-contract.md](references/analysis-packet-contract.md)
before writing a cycle packet. Read
[references/vault-interface.md](references/vault-interface.md) before `sample`
or `paper-handoff`, and read
[templates/PAPER_DRAFT_CHARTER.md](templates/PAPER_DRAFT_CHARTER.md) before
`draft-paper`.

## Required preflight

Before reading real data, confirm:

1. the user named the study workspace and exact authorized inputs;
2. the methodological profile and research question are frozen for this cycle;
3. the `.vault-root` resolves outside this Git repository;
4. consent, privacy, retention, access, redaction, and model-processing
   authority are recorded;
5. every input has stable identity, hash, locator, and rights/privacy state;
6. the cycle ID and frozen input manifest are new; and
7. the analytical seat and independent reviewer are distinct.

If any requirement is unknown, stop before ingestion and report `HOLD` with the
unknown. Never interpret unknown as permission.

## Analytical cycle

1. Reconstruct complete episodes and mark inferred or uncertain boundaries.
2. Split episodes into chronologically ordered incidents.
3. Assign exactly one epistemic class to every incident.
4. Produce action-oriented or source-native initial codes close to the data.
5. Compare incidents, codes, episodes, creators, periods, outcomes, and
   contrary pathways, and append each comparison as a `COMPARISONS.jsonl`
   record naming what was compared, the relation, rivals, and what would
   discriminate.
6. Write descriptive, comparison, methodological, and theoretical memos as
   separate record types in `MEMOS.jsonl`.
7. Develop or revise categories only after recurring comparisons. Record the
   definition, exclusions, properties, conditions, consequences, rivals,
   supporting codes, the comparisons relied on, the counter-search performed,
   and negative cases.
8. Generate sampling requests that discriminate among explanations rather
   than merely seek more examples.
9. Validate the packet structurally with:

```bash
python3 -B <skill-dir>/scripts/validate_analysis_packet.py <cycle-dir>
```

10. Submit the packet for independent analytical review. The producing seat
    cannot clear it.

## Epistemic classes

Use exactly one:

- `OBSERVED_ACTION`
- `CREATOR_REPORTED_ACTION`
- `CREATOR_STATED_INTERPRETATION`
- `THIRD_PARTY_INTERPRETATION`
- `TECHNOLOGY_COMPANY_CLAIM`
- `ANALYST_INFERENCE`
- `THEORETICAL_CONSTRUCT`

An observed action cannot establish a creator belief. An inference must point
to its basis records. A construct must point to supporting codes and remains an
analytical proposal, not empirical evidence.

## Hard boundaries

- Keep sensitizing concepts outside initial coding.
- Never use the model's prior knowledge as empirical evidence.
- Never promote discovery snippets, generic summaries, or marketing claims to
  process evidence.
- Never overwrite historical analysis; append a successor or retirement.
- Never treat a validator PASS as substantive coding quality, evidence
  admission, theory acceptance, release, or publication.
- Never autonomously declare theoretical saturation. The strongest tool state
  is `PROVISIONAL_SUFFICIENCY_CANDIDATE` pending independent and human review.
- Never write real data or study outputs into this tool repository.
- Never acquire sources, contact creators, or launch a research campaign from
  a theoretical-sampling request without separate authority.
- Never let the analytical producer, evidence adjudicator, paper author, or
  release auditor silently collapse into one self-clearing seat.
- In `draft-paper`, every substantive sentence must bind to a current
  `GT_LITE` claim or be visibly marked as author framing; unresolved claims are
  omitted or labelled, never repaired from model prior knowledge.

## Output

Lead with what the current data support, then state rivals, negative cases,
unknowns, and the next discriminating sample. Prefer a small process model over
a long theme list. Always state what would be missed if only final successful
artifacts were observed.

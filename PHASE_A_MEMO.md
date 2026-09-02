# Phase A memo — Grounded Theory

**Date:** 2026-09-02
**Decision state:** architecture draft; superseded for authority by `START_HERE__20260902.md` (fire orders issued 2026-09-02)
**Provenance correction, 2026-09-02:** the pilot dataset is open-sourced third-party production-trace data, not the Operator's own traces; rulings 4 and 5 in the START memo govern its use
**Repository:** `joyzhzh/grounded-theory`
**First intended study:** creative realization through probabilistic AIGC

## Recommendation

Build a private research program and reusable tool that teach and enforce an
inductive process-analysis workflow without pretending that an LLM can make
grounded theory rigorous by producing themes. The tool should preserve the
chain from source manifestation to episode, incident, code, comparison,
category change, memo, theoretical-sampling request, and paper handoff.

Before that use, the program should run two separate research missions: an
Evidence-First methods mission and a grounded-theory-specific SOTA repository
Scout. The first use of the tool is the open-sourced Seedance feature-film
production-trace dataset the Operator holds, a group of creators' detailed
per-attempt traces, combined later with separately governed public archival
evidence. The tool
must remain reusable beyond AIGC.

## Method position

Until a methods review supports stronger language, describe the study as an
**inductive process study using grounded-theory techniques**. A live study must
freeze one declared profile before coding; the tool must not silently mix
Glaserian, Straussian, Charmaz, and Gioia conventions. A Gioia data structure
may later display findings, but it is not the analytical engine and is not
synonymous with grounded theory.

The broad opening question is:

> What happens when creators attempt to realize creative intentions through
> probabilistic generative technologies?

The chat history suggests potentially important ideas—generative
decomposition, coupled failure, capability beliefs, intention drift,
accommodation, differential realizability, and selection before audience
evaluation. They are **sensitizing possibilities only**. They must not become
starter codes, presumed mechanisms, or expected findings.

## Unit of analysis

The primary unit is a complete `REALIZATION_EPISODE`, not an isolated prompt
or final artifact. An episode begins with an attempt to realize an intended
creative outcome and ends in acceptance, substantial transformation,
substitution, decomposition, postponement, abandonment, or a truthful unknown
state. Temporal order and uncertain boundaries must be preserved.

This matters because the hidden empirical object is the path between intention
and artifact: generation, evaluation, persistence, respecification,
constraint, relaxation, decomposition, compromise, and stopping.

## Epistemic firewall

Every analytical item must carry exactly one level:

1. `OBSERVED_ACTION`
2. `CREATOR_REPORTED_ACTION`
3. `CREATOR_STATED_INTERPRETATION`
4. `THIRD_PARTY_INTERPRETATION`
5. `TECHNOLOGY_COMPANY_CLAIM`
6. `ANALYST_INFERENCE`
7. `THEORETICAL_CONSTRUCT`

A construct is not evidence. An observed prompt change does not establish what
the creator believed. A creator interpretation requires an attributable
statement and exact locator. Model prior knowledge and product marketing are
never evidence of creator behavior.

## Iterative analytical cycle

Each bounded cycle should:

1. freeze the exact input manifest;
2. reconstruct episodes and incidents with uncertainty visible;
3. conduct action-oriented and, where justified, in-vivo initial coding;
4. compare incident with incident, incident with code, and code with category;
5. keep descriptive, comparison, methodological, and theoretical memos
   distinct;
6. version categories with definitions, exclusions, properties, conditions,
   consequences, rivals, and negative cases;
7. generate sampling requests that discriminate among competing explanations;
8. actively seek contradictions, boundaries, and alternative mechanisms;
9. receive independent review of grounding and epistemic classification; and
10. append revisions, supersessions, or retirements without rewriting history.

The AI “learns” through these versioned artifacts. It does not fine-tune
itself, write hidden memory, or promote its own theory.

## Research agenda

`GT-M01` develops the evidence-backed methodological workflow. It uses the
full Evidence-First chain to admit claims about grounded-theory traditions,
constant comparison, memoing, theoretical sampling, negative cases,
sufficiency/saturation, archival and digital-trace data, AI-assisted coding,
process theorizing, Gioia reporting, and research ethics.

`GT-M02` runs a grounded-theory-specific `high-recall-map` of public
repositories, skills, packages, templates, datasets, evaluation artifacts,
and adjacent tooling. Its landed bundle belongs under
`joyzhzh/sota-repository-scout/campaigns/<run-date>__grounded-theory-methods-tooling/`.
That bundle is discovery and coverage memory only. It may supply leads to
`GT-M01`; it cannot admit methodological claims or authorize acquisition or
execution of candidate software.

The pre-existing `2026-07-28__theory-building` Scout campaign is a zero-credit
baseline for deduplication and vocabulary. The new Scout is narrower: grounded
theory and auditable qualitative-analysis machinery.

## Relationship to the AIGC evidence vault

The grounded-theory tool and `aigc-chouka-evidence` have separate authority.

The tool may issue a bounded theoretical-sampling request naming a
provisional uncertainty, discriminating contrast, eligible source class,
language/date boundary, stop rule, and claim ceiling. The vault returns a
hash-bound descriptive evidence package with locators, epistemic classes,
rights state, negative cases, and limitations.

Discovery snippets never cross as evidence. An unadjudicated return may inform
exploratory coding only while visibly marked; it cannot support a paper claim.
The vault does not decide codes, categories, relationships, saturation, or
paper claims. The tool does not acquire or clear source bytes.

## Paper handoff

The eventual tool output should be a `GT_LITE.md` and machine-readable claim
matrix containing:

- construct definitions and boundaries;
- process pathways and rival mechanisms;
- category properties and negative cases;
- propositions with proposition-specific falsifiers;
- claim-to-current-record bindings;
- unresolved questions and archive limitations; and
- exact ceilings on what the data do not establish.

Only independently admitted, rights-cleared current records may enter a
claim-bearing handoff. A separately authorized author seat may draft only from
the immutable adjudicated `GT_LITE` and evidence package, with every
substantive sentence bound to a current claim. The analytical producer and
evidence adjudicator do not self-clear that draft. A fresh release auditor
verifies the exact draft. Drafted, submitted, accepted, released, and
published remain different states.

## Phase A gates

- `G0 — Protocol pin`: exact Evidence-First revision and declared seat routing.
- `G1 — Data authority`: consent, privacy, retention, lawful access, redaction,
  and model-processing decisions before ingestion.
- `G2 — Custody`: source identity, hash, locator, rights state, and raw-to-
  normalized linkage.
- `G3 — Epistemic classification`: no unlabelled movement from behavior to
  interpretation, inference, or construct.
- `G4 — Cycle integrity`: frozen inputs, recorded tool/model identity,
  append-only outputs, and explicit supersession.
- `G5 — Grounded comparison`: categories require incident comparisons,
  disconfirming evidence, and documented boundaries.
- `G6 — Theoretical sampling`: new evidence requests must address an uncertainty,
  rival, boundary, or negative case.
- `G7 — Independent review`: the analytical seat cannot clear its own
  categories or paper claims.
- `G8 — Paper export`: only current admitted evidence and reviewed constructs,
  with quotation and privacy restrictions enforced.
- `G9 — Stop language`: the tool may recommend
  `PROVISIONAL_SUFFICIENCY_CANDIDATE`; it may not declare saturation by itself.

For evidence-acquisition lanes, each worker stops at exactly `R001`–`R010` and
creates no `R011`. Work requiring more evidence becomes a new, separately
authorized lane after audit; it never extends the same worker. Repetitive,
blocked, thin, or capped results remain unknown and cannot establish absence or
saturation.

## Main risks and controls

| Risk | Phase A control |
|---|---|
| Starter prompt reproduces the proposed theory | keep sensitizing concepts in a separate artifact and out of initial coding |
| Behavioral trace becomes a claim about cognition | exact epistemic class; interpretation needs creator-stated evidence |
| LLM themes masquerade as grounded theory | incident-level codes, comparison records, category-change logs, and sampling consequences |
| Trace data leaks through Git or cloud inference | ignored external vault and a required processing-authority gate |
| Categories stabilize because challenges stop | mandatory counter-search and negative-case review |
| Repetitive search is called saturation | candidate-only stop language plus unresolved-route register |
| Control machinery overwhelms analysis | one cycle history, small schemas, deterministic validation, no second ledger or receipt recursion |

## Phase A close condition

Phase A closes when this private program and tool scaffold, two-mission
research agenda, explicit mission/lane portfolio, Scout landing contract,
method contract, starter prompt, packet schema, validator, tests, pins, and
repository boundary are present and verified. It does not run either mission,
close a study, produce grounded theory, upload a Scout result, or authorize
Phase B.

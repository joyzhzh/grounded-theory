# Grounded Theory

A private Evidence-First research program and Codex skill for learning,
designing, and applying grounded-theory-oriented analysis. It combines a
methods research agenda with an auditable tool for episode reconstruction,
initial coding, constant comparison, memoing, theoretical sampling,
negative-case analysis, and provenance-bound paper drafting and handoff.

## Current state

- **Repository state:** `UNFIRED — PHASE A ARCHITECTURE DRAFT`
- **Proposed research missions:** 2; neither fired
- **Skill state:** structural prototype; no live study has run
- **Real data ingested:** none
- **Categories or theory produced:** none
- **Saturation assessed:** no
- **Paper or publication authorized:** no
- **Protocol pin:** `joyzhzh/evidence-first-deep-research-v2@fa6cc2e2f93136d2d7b5d29a3b5d5b3e7d445e1d`

Creating this repository does not activate a study. See [STATUS.md](STATUS.md)
and the [Phase A memo](PHASE_A_MEMO.md).

## What this is

The tool component follows the shape of
`joyzhzh/eisenhardt-case-study`: one installable skill, explicit modes and hard
boundaries, small deterministic validation code, synthetic tests, and no live
research corpus in the reusable tool repository.

It applies the custody principles of Evidence-First Deep Research: preserved
source identity, exact locators, explicit epistemic levels, append-only
correction, independent review, and a clean separation among discovery,
analysis, evidence admission, drafting, release, and publication.

The initial use case is AIGC creation under probabilistic generation, but the
tool is phenomenon-neutral. The focal AIGC question is:

> What happens when creators attempt to realize creative intentions through
> probabilistic generative technologies?

## What this is not

- It is not a one-pass theme generator.
- It does not infer cognition from behavior.
- It does not treat an LLM's prior knowledge as empirical evidence.
- It does not fine-tune or secretly update a model.
- It does not autonomously declare theoretical saturation.
- It does not admit evidence, clear a paper, or authorize publication.

Here, “AI learning” means accumulating versioned, inspectable analytical state
across cycles: incidents, codes, comparisons, category changes, memos, negative
cases, and sampling requests.

## Repository boundary

Private traces, source manifestations, transcripts, personal data, live study
outputs, and claim-bearing evidence stay outside Git in a private study vault
resolved by an ignored `.vault-root`. This repository contains only the
reusable method, schemas, templates, synthetic examples, validators, and tests.

## Install and invoke

During Phase A, clone the private repository into the Codex skills directory
only for controlled testing:

```bash
git clone https://github.com/joyzhzh/grounded-theory.git \
  ~/.codex/skills/grounded-theory
```

Then invoke:

```text
Use $grounded-theory to orient this study and prepare a method charter. Do not ingest data yet.
```

Read [SKILL.md](SKILL.md) for modes and
[references/grounded-theory-contract.md](references/grounded-theory-contract.md)
for the method contract.

The two proposed research missions and their explicit lane identities are in
[MISSION_PORTFOLIO.md](MISSION_PORTFOLIO.md); their questions, deliverables,
and claim ceilings are developed in [RESEARCH_AGENDA.md](RESEARCH_AGENDA.md).
The SOTA map is designed to land under
`joyzhzh/sota-repository-scout/campaigns`; it remains discovery input and never
substitutes for the Evidence-First methods mission.

## Structural validation

The Phase A validator checks a cycle packet's required files, statuses,
epistemic classes, IDs, and references. It does not judge substantive coding
quality or theory.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_analysis_packet.py examples/synthetic/C001
./scripts/doctor.sh
```

The validator applies the row schemas in `schemas/` and therefore needs the
`jsonschema` package (`python3 -m pip install jsonschema`).
`examples/synthetic/C001` is the invented fixture the tests copy. The doctor
script checks only that `.vault-root` resolves to an absolute, untracked path
outside this repository with no `.git` inside it. A repository-boundary test
fails if any media, capture, or oversized file is ever tracked.

## License

The reusable software and original tool documentation are MIT-licensed. That
license does not apply to study data, third-party material, transcripts,
quotes, or research outputs.

# Grounded Theory

[![Tests](https://github.com/joyzhzh/grounded-theory/actions/workflows/test.yml/badge.svg)](https://github.com/joyzhzh/grounded-theory/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Codex skill for qualitative analysis you can inspect: reconstruct episodes,
code exact source passages, compare incidents, revise categories after
counterexamples, and prepare a local handoff for review.

**Status: `USABLE_V1`.** The workflow has passed software checks and an
end-to-end fresh-session test on a wholly invented fixture. Human review of
interpretations remains necessary. See [status and limits](STATUS.md).

## What you get

- Episodes with explicit attempt relationships and preserved unknown endings.
- Source-linked incidents and action-oriented codes, with separate observation,
  attributed interpretation and analyst inference.
- Comparisons that explain what changes in the analysis, including negative cases.
- Descriptive, comparison, methodological and theoretical memos; earlier category
  and memo versions remain intact.
- A discriminating sampling proposal that stays unexecuted, plus a checked local
  handoff with source hashes and exact locators.

The agent interprets the input. Small Python helpers prepare, append, continue,
validate and seal analysis cycles. The helpers make no model or network calls.
Use the methodological label **inductive process study using grounded-theory
techniques**; software validation does not establish a theory's validity.

## Install

Requires Codex with local skill support, Git, and Python 3.9+ with `jsonschema`.
The helpers run on macOS, Linux or WSL; they use POSIX file locking.
Use a Python environment that permits installing dependencies.

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/joyzhzh/grounded-theory.git \
  ~/.codex/skills/grounded-theory
python3 -m pip install -r ~/.codex/skills/grounded-theory/requirements.txt
```

If the target already contains an installation, preserve it and update that
checkout instead of cloning over it. Keep the Git checkout: the helpers record
its revision and a hash of the actual runtime files.

## Try the skill

In a fresh Codex task, paste:

```text
Use $grounded-theory and the reusable prompt in its AGENT_STARTER.md.

Study question: How does a designer decide what to change when generated illustrations do not match a brief?
Input path: examples/synthetic/cloud_post.txt in the installed skill directory.
Output study path: a new grounded-theory-demo directory in my home folder, outside every Git checkout; use an unused suffix if needed.

The named fixture is wholly invented and authorized for this local synthetic
exercise. Copy its exact bytes into the study, preserve the original, and keep
all results SYNTHETIC / INVENTED / NON_RELEASE. Analyze the fixture yourself;
do not run a prewritten example analysis. Complete the readable report and
checked local handoff.
```

For your own data, use the [starter prompt](AGENT_STARTER.md) with your question,
exact authorized normalized-text inputs, and a new study directory. The agent
handles file formats and checks. Raw audiovisual inputs need a separately
authorized, traceable text/event export. No data-processing authority follows
from installing the skill or from historical project instructions.

## Use the helpers directly

The [workflow guide](references/workflow.md) documents input configuration,
supported commands, source and quote locators, supersession, and handoffs.
For a deterministic software demonstration with invented data and no model:

```bash
cd ~/.codex/skills/grounded-theory
python3 -B examples/synthetic/workflow.py \
  --output "$HOME/grounded-theory-scripted-demo"
```

The output path must be unused and outside every Git checkout. This example
creates two sealed cycles, including a category revision after counterevidence.
It is separate from using the agent to analyze the text fixture.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_analysis_packet.py examples/synthetic/C001
```

An optional machine-local `.vault-root` can point to a private study parent;
see [.vault-root.example](.vault-root.example) and `scripts/doctor.sh`. Helpers
always require an explicit study path and never inspect all studies implicitly.

## Data and review boundaries

Only reusable code, original documentation, schemas, templates and invented
fixtures belong in this repository. Real source bytes, transcripts, personal
data, media and study outputs stay outside Git. See [data policy](DATA_POLICY.md).

Preserve uncertainty and exact source links. Behavior alone does not establish
belief; a missing ending remains unknown. Sampling is proposed, never acquired
by the helper. A producer cannot provide independent review of its own analysis.
The tool does not certify saturation, admit evidence or authorize publication.
Analysis outputs remain `NON_RELEASE`; the public software release does not
change their status.

## Documentation

- [Skill modes](SKILL.md) and [analysis contract](references/grounded-theory-contract.md).
- [Packet contract](references/analysis-packet-contract.md) and [method limitations](references/methods-basis.md).
- [Development decisions](DECISIONS.md) and [current status](STATUS.md).
- [Historical project instructions](START_HERE__20260902.md), [mission portfolio](MISSION_PORTFOLIO.md)
  and [research agenda](RESEARCH_AGENDA.md). These preserve development context;
  their project-specific launch orders do not apply to a new user's study.

The runtime is self-contained. Linked companion repositories and external
development records are provenance context, not installation dependencies.

## License

[MIT](LICENSE) for the reusable software, original tool documentation and
explicitly invented examples. It does not license real study data,
third-party source material or research outputs.

# Historical launch prompts

The original project prompts below are retained for provenance. They are not
current startup instructions and do not authorize a new user's study. Use
[AGENT_STARTER.md](AGENT_STARTER.md) for the reusable workflow.

# Fire prompts — paste one per Codex session

Each prompt is self-contained for a fresh Codex session on any machine. Fill
the angle-bracket placeholders before pasting. `START_HERE__20260902.md`
governs; these prompts only get a session to it.

## Prompt A — `GT-PILOT-C001` producer

```text
You are the producer seat for GT-PILOT-C001, Order A in START_HERE__20260902.md of joyzhzh/grounded-theory. Authority is the delegated Operator rulings recorded there; nothing else authorizes work. You produce. You do not review your own work, ratify anything, draft a paper, start C002, or send any request to the evidence vault.

Fill in before running:
  <VAULT_ROOT>    absolute path of a directory outside every git repository
  <DATASET_PATH>  where the open-sourced Seedance feature-film production-trace dataset is on this machine (and its source URL if you know it)

Bootstrap. Stop with HOLD and report the failing step if any step fails:
  git clone https://github.com/joyzhzh/grounded-theory.git && cd grounded-theory
  git checkout bc9c82d38950a2ed8e564531e318e475b161f021   # main at or after this commit is acceptable only if START_HERE__20260902.md is unchanged
  python3 -m pip install "jsonschema>=4.18"
  printf '%s\n' '<VAULT_ROOT>' > .vault-root
  ./scripts/doctor.sh
  python3 -m unittest discover -s tests -v
  git rev-parse HEAD   # this is tool_revision

Read, in order: START_HERE__20260902.md (rulings 1-8 and Order A), SKILL.md, references/grounded-theory-contract.md, references/analysis-packet-contract.md, references/vocabulary-crosswalk.md, schemas/*.schema.json.

Execute Order A exactly.
1. Study root <VAULT_ROOT>/studies/GT-PILOT/ with raw/, normalized/, cycles/C001/.
2. From <DATASET_PATH> select two or three complete episodes for contrast: at least one accepted, at least one abandoned or transformed, plus one with an unknown ending if one exists. Copy them into raw/ (immutable) and hash them into raw/SHA256SUMS.
3. Normalize each into an event export under normalized/, minting MNF-GTPILOT-001 onward; each export names its raw source hash. Apply ruling 5's minimization before any model reads an export: creators by the dataset's own identifiers, no face or voice beyond what an incident needs, nothing outside the dataset joined in.
4. Write normalized/INPUT_MANIFEST.json: dataset name, source URL, license identifier, license-file hash, snapshot hash, and per-manifestation raw and normalized hashes. If the license cannot be identified, record license: UNKNOWN and continue. Its SHA-256 is input_manifest_sha256.
5. Run pilot-code, then compare, inside one cycle C001 at schema 0.2-phase-a (eight files). Exactly one epistemic class per incident; source-based classes carry source_ref; a creator-stated interpretation carries a hash-bound quote_ref. Initial codes close to the data. Record every comparison as a COMPARISONS row. Memos by type in MEMOS.jsonl. Category memos at SENSITIZING_ONLY or EMERGING only; FOCUSED is forbidden in C001. At least one SAMPLING_REQUESTS row with status PROPOSED conforming to schemas/sampling-request.schema.json. Keep the sensitizing concepts in PHASE_A_MEMO.md out of initial coding.
6. MANIFEST.json: protocol_revision fa6cc2e2f93136d2d7b5d29a3b5d5b3e7d445e1d; tool_revision from git rev-parse HEAD; producer_seat "codex-producer-<today>"; reviewer_seat "claude-reviewer-unassigned"; model_processing {"authority_ref": "GT-RULING-2026-09-02-05R", "models": ["<your exact model identifier>"]}; release_status NON_RELEASE; saturation_status NOT_ASSESSED.
7. Validate: python3 scripts/validate_analysis_packet.py <VAULT_ROOT>/studies/GT-PILOT/cycles/C001 must print PASS_ANALYSIS_PACKET_STRUCTURE. Then set analysis_status to SUBMITTED_FOR_REVIEW and hash cycles/C001/ into its SHA256SUMS.
8. Write cycles/C001/HANDOFF.md: what the data support, rivals, negative cases, unknowns, the next discriminating sample, what final artifacts alone would hide, and a contract friction log listing every place the packet contract, a schema, the validator, or the skill was wrong, missing, or awkward, with the row it affected.

Hard limits: at most three episodes, one cycle, one session. Never write study data or outputs into the repository. Commit nothing. Raw media never leaves the vault. Nothing you produce is evidence, a claim, or saturation.

Stop when PASS and HANDOFF.md exist, or at a truthful HOLD. Your final message: study root, packet SHA256SUMS digest, validator output, and the friction log verbatim.
```

## Prompt B — `GT-M02` Scout producer

```text
You are the producer seat for GT-M02, Order B in START_HERE__20260902.md of joyzhzh/grounded-theory: the grounded-theory methods and tooling Scout campaign, backlog card C30, execution rank 1. Authority is the delegated Operator rulings recorded there. You discover, screen, and record coverage. You do not gate, land, acquire, install, import, build, execute, or preserve any candidate, and you make no method claim. This needs web access; HOLD if you have none.

Fill in before running:
  <VAULT_ROOT>  absolute path of a directory outside every git repository

Bootstrap. Stop with HOLD and report the failing step if any step fails:
  git clone https://github.com/joyzhzh/grounded-theory.git && cd grounded-theory
  git checkout bc9c82d38950a2ed8e564531e318e475b161f021   # main at or after this commit is acceptable only if START_HERE__20260902.md is unchanged
  python3 -m pip install "jsonschema>=4.18"
  printf '%s\n' '<VAULT_ROOT>' > .vault-root
  ./scripts/doctor.sh
  python3 -m unittest discover -s tests -v
  cd .. && git clone https://github.com/joyzhzh/evidence-first-deep-research-v2.git && cd evidence-first-deep-research-v2
  git checkout fa6cc2e2f93136d2d7b5d29a3b5d5b3e7d445e1d
  (cd skills/sota-repository-scout && shasum -a 256 -c SHA256SUMS)
  cd .. && git clone https://github.com/joyzhzh/sota-repository-scout.git   # read-only: baseline at bd8f2152cb9ddb50f4c0a73603013393ae34e03d

Read: START_HERE__20260902.md Order B; plans/GT-M02_SOTA_REPOSITORY_SCOUT.md; MISSION_PORTFOLIO.md (cells GT-M02-C01 to C12 with their confusion negatives, frames GT-M02-F01 to F08); in the protocol clone, skills/sota-repository-scout/SKILL.md and skills/sota-repository-scout/references/lean-search-contract.md; the baseline campaign sota-repository-scout/campaigns/2026-07-28__theory-building/ for zero-credit deduplication and vocabulary.

Working root: <VAULT_ROOT>/scout/<today YYYY-MM-DD>__grounded-theory-methods-tooling/. Never inside a repository.

Freeze SCOPE.md before query 1 with: run_type high-recall-map; the question and unit from the plan; cutoff equal to today; English with justified Chinese routes; the twelve cells with their negatives; the eight frames; the zero-credit baseline path; inspection only; K = 2; two materially independent post-merge passes; a ceiling of four to six wall-clock hours across at most three sessions; claim ceiling "high-coverage, effort-bounded map as of <date>" or, at the ceiling with positive yield, "..., not saturated".

Run the lean bundle per the lean contract: SCOPE.md, SEARCH_LOG.jsonl, SCREENING.jsonl, EVIDENCE_LEDGER.jsonl, FINDINGS.md, SHA256SUMS, and nothing else in that directory. Every frame runs or gets an explicit partial, blocked, or not-applicable limitation. Every cell gets a disposition. Resolve GitHub candidates to stable repository id, canonical owner and name, default branch, exact commit, license manifestation, and fork or mirror relations. Validate mid-run and at the end:
  python3 ../evidence-first-deep-research-v2/skills/sota-repository-scout/scripts/validate_lean_bundle.py --partial <working-root>
  python3 ../evidence-first-deep-research-v2/skills/sota-repository-scout/scripts/validate_lean_bundle.py <working-root>
Record the printed bundle_sha256 in <VAULT_ROOT>/scout/GT-M02__RUN_NOTES.md together with session count, hours used, and plateau evidence. Keep that file outside the bundle.

Hard limits: no GATE_LOG.md, no landing, no edits to any repository, no candidate acquisition or execution, no GT-M01 lane. Stop at a working plateau by the skill's criteria or at the ceiling with the honest label.

Your final message: working root, bundle_sha256, coverage label, each cell's disposition, frames run or limited, top leads per cell with exact locators, limitations, and a friction log of what the plan or scope got wrong.
```

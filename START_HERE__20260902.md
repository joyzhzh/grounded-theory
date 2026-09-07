# START HERE — grounded-theory fire orders, 2026-09-02

> Historical project record. For current installation and use, start with
> [README.md](README.md) and [STATUS.md](STATUS.md). The dated instructions below
> apply only to their original project scope. They do not launch work, grant
> data-processing authority, or require companion repositories for public users.

**Read this first on any machine.** It carries the current Operator rulings
and the two fire orders that are live. Everything else in this repository is
method, contract, or plan; nothing else authorizes work.

**Authority.** The Operator delegated the blocking rulings in `STATUS.md` to
Claude (Fable 5.1) in chat on 2026-09-02 ("you rule for me"). Each ruling is
recorded as a dated row in `DECISIONS.md` with authority state
`Operator ruling, delegated 2026-09-02`. The Operator reverses any ruling by a
later dated row; until then these govern.

**State after this memo:** `FIRE ORDERS ISSUED 2026-09-02 — NOT EXECUTED`.
Two fire orders are live and may run in parallel in separate sessions:

| Order | Scope | Fires now |
|---|---|---|
| A | `GT-PILOT-C001`: one exploratory pilot-code cycle on the open-sourced Seedance feature-film production traces the Operator holds | yes |
| B | `GT-M02`: the grounded-theory methods and tooling Scout campaign, backlog card `C30`, rank 1 | yes |
| C | `GT-M01`: the Evidence-First methods mission | no; fires after B lands or closes with limitations |

Nothing in either order produces a paper, a theory claim, a saturation
statement, a release, or a sampling request to the evidence vault.

## Rulings

Numbered as in `STATUS.md`, "Blocking decisions before a live pilot".

1. **Portfolio and catalogs.** The sixteen `GT-M01` lane identities and the
   twelve `GT-M02` cells and eight frames are ratified as frozen identities
   (the identity-registry test guards them). `GT-M02` fires; `GT-M01`
   execution is deferred, and its first lanes when it fires are
   `GT-M01-L01` and `GT-M01-L08`.
2. **Method profile.** For the pilot: constructivist grounded-theory
   techniques within an inductive process study. Action-oriented gerund
   initial coding, constant comparison recorded as comparison rows, memos by
   type, theoretical sampling as request rows. No axial-coding paradigm. A
   Gioia data structure is permitted only as a later reporting surface.
   Permitted reporting label: "inductive process study using grounded-theory
   techniques". Provisional until `GT-M01-L01` is adjudicated.
3. **Question, unit, boundary.** The question is the Phase A question
   verbatim. The unit is the `REALIZATION_EPISODE`. An episode starts at the
   first specification or attempt addressed to a nameable intended outcome
   and ends in one of the packet's outcome states, or `UNKNOWN` when the
   trace ends without one. Every episode records its `boundary_basis`.
4. **Dataset** (revised 2026-09-02 after the Operator corrected its
   provenance). The open-sourced production-trace dataset the Operator
   holds: a group of creators using mainly Seedance to produce a
   feature-length film, with detailed per-attempt traces. It is third-party
   public data under its published license, not data the Operator
   produced. Pilot input: two or three complete episodes chosen for contrast,
   at least one accepted and at least one abandoned or transformed, plus one
   with an unknown ending if one exists. Before any coding the worker records
   the dataset's name, source URL, license identifier, license-file hash, and
   retrieved snapshot hash in `INPUT_MANIFEST.json`; no hash is pre-declared
   here. The Operator holds the dataset and its terms and ruled that this
   does not gate the pilot.
5. **Data authority** (revised 2026-09-02). Basis: the dataset's open-source
   license as published, recorded in the input manifest; if the license
   cannot be identified, record `license: UNKNOWN` and continue rather than
   `HOLD`, since every output is `NON_RELEASE`. Data minimization still
   applies: creators are referred to by the dataset's own identifiers, no
   face or voice is extracted beyond what an incident needs, and nothing
   outside the dataset is joined to it. Raw media never leaves the vault.
   Model processing, including cloud models, is permitted on normalized text
   or event exports, and the exact models used are recorded in
   `MANIFEST.json` under `model_processing` with `authority_ref`
   `GT-RULING-2026-09-02-05R`. Retention: vault only.
6. **Pins and seats.** Protocol
   `joyzhzh/evidence-first-deep-research-v2@fa6cc2e2f93136d2d7b5d29a3b5d5b3e7d445e1d`
   is ratified for both orders. The Scout method is the lean skill vendored
   in that protocol revision; the Scout repository's v0.6.4 controller is not
   adopted. `tool_revision` is the grounded-theory commit checked out at fire.
   Producer is the fired session. Reviewer or supervisor is a fresh session
   that did not produce the artifact, a different vendor when available.
   Accepted default (2026-09-02): producer sessions run on Codex, where the
   skill installs; reviewer, supervisor, and auditor sessions run on Claude.
7. **Approvals.** Order A with its reviewer role and Order B with its
   supervisor role are approved with the ceilings below.
8. **Beyond exploratory.** No. Every output is `NON_RELEASE`.

## Accepted defaults (2026-09-02)

The Operator accepted these on 2026-09-02 ("others can follow your rec"):

- **Seats.** Producer on Codex; reviewer, supervisor, and auditor on Claude.
- **Firing order.** All three orders across the two repositories may run in
  parallel. If capacity is tight: Order A, then Order B, then the vault's
  `ACE-M00-L01`.
- **Cloud model processing** of normalized exports: permitted, recorded in
  the manifest.
- **Vault.** One directory outside every Git repository on a synchronized
  provider with version history, named in `.vault-root` on each machine,
  with one offline copy before any package submission.

## Pasteable session prompts

`FIRE_PROMPTS__20260902.md` carries one self-contained prompt per order for
a fresh Codex producer session. They only get a session to this memo; this
memo governs.

## Bootstrap on any machine

```bash
git clone https://github.com/joyzhzh/grounded-theory.git
cd grounded-theory
python3 -m pip install "jsonschema>=4.18"
cp .vault-root.example .vault-root   # then edit: one absolute path outside every Git repository
./scripts/doctor.sh
python3 -m unittest discover -s tests -v
git rev-parse HEAD                    # this is tool_revision for Order A
```

`HOLD` if the doctor script or the tests fail. Never interpret a failure as
permission to continue.

## Order A — `GT-PILOT-C001`

**Purpose.** Test the packet contract and the skill on real episodes before
any catalog is ratified for execution. The friction log in step 7 is the
deliverable that matters most.

**Roots.** Study id `GT-PILOT`; study root `<vault>/studies/GT-PILOT/` with
`raw/`, `normalized/`, `cycles/C001/`, and a `SHA256SUMS` per directory.

**Steps.**

1. Copy the selected traces into `raw/`. Raw bytes are immutable. Hash them
   into `raw/SHA256SUMS`.
2. Normalize each trace into an event export under `normalized/`, minting
   manifestation identities `MNF-GTPILOT-001` onward. Each export names its
   raw source hash. Apply ruling 5's minimization before any model reads the
   export.
3. Write `normalized/INPUT_MANIFEST.json` listing every manifestation, its
   raw and normalized hashes, and redaction notes. Its SHA-256 is the
   manifest's `input_manifest_sha256`.
4. Read `SKILL.md`, `references/grounded-theory-contract.md`, and
   `references/analysis-packet-contract.md`. Run `pilot-code` and then
   `compare` inside this one cycle: reconstruct episodes and incidents with
   exactly one epistemic class each, write initial codes, record every
   comparison as a comparison row, write memos by type, and write category
   memos at `SENSITIZING_ONLY` or `EMERGING` only. `FOCUSED` is not permitted
   in `C001`. Write at least one sampling request with status `PROPOSED`.
5. Keep the sensitizing concepts in `PHASE_A_MEMO.md` out of initial coding.
   The starter template is orientation, not a code list.
6. Validate, then submit:

   ```bash
   python3 scripts/validate_analysis_packet.py <vault>/studies/GT-PILOT/cycles/C001
   ```

   On `PASS`, set `analysis_status` to `SUBMITTED_FOR_REVIEW` and hash
   `cycles/C001/` into its `SHA256SUMS`.
7. Write `cycles/C001/HANDOFF.md`: what the data support, rivals, negative
   cases, unknowns, the next discriminating sample, what final artifacts
   alone would hide, and a **contract friction log**: every place the packet
   contract, a schema, the validator, or the skill was wrong, missing, or
   awkward, with the row it affected.
8. Stop. Do not start `C002`, do not send the request to the vault, do not
   draft anything.

**Ceiling.** One producer session, at most three episodes, one cycle. Stop
at packet `PASS` plus handoff, or at a truthful `HOLD`.

**Review.** A fresh session runs `audit` mode over `C001`, writes
`cycles/C001/REVIEW.md`, and edits nothing in `C001`.

**Handback.** The friction log and review decide whether the packet schema
moves to 0.3 before any other grounded-theory work. That decision is a
`DECISIONS.md` row.

## Order B — `GT-M02` Scout campaign (`C30`, rank 1)

**Preconditions.** Clone the protocol at the pinned revision and verify the
vendored skill, then read the skill and its lean contract at that revision:

```bash
git clone https://github.com/joyzhzh/evidence-first-deep-research-v2.git
cd evidence-first-deep-research-v2
git checkout fa6cc2e2f93136d2d7b5d29a3b5d5b3e7d445e1d
(cd skills/sota-repository-scout && shasum -a 256 -c SHA256SUMS)
git clone https://github.com/joyzhzh/sota-repository-scout.git   # baseline and, later, landing
```

Read `skills/sota-repository-scout/SKILL.md` and
`skills/sota-repository-scout/references/lean-search-contract.md`.

**Working root.** `<vault>/scout/<run-date>__grounded-theory-methods-tooling/`.
Never inside any repository.

**Freeze `SCOPE.md` before query 1** from
`plans/GT-M02_SOTA_REPOSITORY_SCOUT.md`: `run_type: high-recall-map`; the
question and unit; cutoff equal to the run date; English with justified
Chinese routes; cells `GT-M02-C01`–`C12` with their confusion negatives from
`MISSION_PORTFOLIO.md`; frames `F01`–`F08`; the zero-credit baseline
`campaigns/2026-07-28__theory-building/`; inspection only, meaning no clone,
install, import, build, execute, or preserve; `K = 2`; two materially
independent post-merge passes; ceiling two to three sessions and four to six
wall-clock hours; claim ceiling `high-coverage, effort-bounded map as of
<date>` or, at the ceiling with positive yield, `..., not saturated`.

**Run.** Keep the lean bundle current. Validate mid-run with `--partial`
and at the end in FULL mode, and capture the printed `bundle_sha256`
programmatically:

```bash
python3 <protocol>/skills/sota-repository-scout/scripts/validate_lean_bundle.py --partial <working-root>
python3 <protocol>/skills/sota-repository-scout/scripts/validate_lean_bundle.py <working-root>
```

**Supervisor gate.** A fresh non-producing session runs the artifact gate
(FULL validator `PASS`) and the coverage gate (the skill's plateau criteria)
and writes `GATE_LOG.md`. Ruling on placement: the hash of record is the
FULL validator's `bundle_sha256` over the six-file bundle **before** any gate
record exists; `GATE_LOG.md` and any receipt then go under `acceptance/`,
never top-level, so `shasum -a 256 -c SHA256SUMS` remains the post-landing
verification. The pinned validator rejects extra files and nested
directories, so it is not re-run on a landed folder.

**Landing.** One deputized session on one device, per the Scout
repository's `PROTOCOL.md` §4: copy the exact accepted bundle to
`campaigns/<run-date>__grounded-theory-methods-tooling/`, add
`acceptance/GATE_LOG.md`, append one `INDEX.md` row, commit with the hash of
record quoted in the message, push, verify the remote. Then, in this
repository, add `handoffs/RECORD__GT-M02__<run-date>.md` naming the landed
path and hash, update `SCOUT.lock.json` (`result_exists`, landing revision),
and, in a separate Scout commit, tick `C30` in the backlog memo.

**Ceiling and stop.** Four to six wall-clock hours across two or three
sessions. Stop at a working plateau or at the ceiling with the honest label.

**Not authorized.** Acquiring, installing, or executing any candidate;
treating any finding as a method claim; firing any `GT-M01` lane.

## Order C — `GT-M01` (not fired)

Fires only after Order B lands or closes with explicit limitations. First
lanes: `GT-M01-L01` (lineages, which decides ruling 2) and `GT-M01-L08`
(stop doctrine, which decides the stop language). Each lane is one worker's
`R001`–`R010` handoff under the pinned protocol's three-file contract.

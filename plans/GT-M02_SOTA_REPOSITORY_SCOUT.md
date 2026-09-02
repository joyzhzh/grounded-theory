# GT-M02 prospective Scout contract — grounded-theory methods and tooling

**State:** prospective draft; not frozen; no query has run
**run_type:** `high-recall-map`
**Planned landing:** `joyzhzh/sota-repository-scout/campaigns/<run-date>__grounded-theory-methods-tooling/`

## Question and unit of analysis

**Question.** What public repositories, packages, skills, schemas, templates,
datasets, evaluation artifacts, and adjacent tools provide reusable machinery
for grounded-theory or auditable theory-building from qualitative data?

**Unit.** A stable artifact identity with one canonical repository, package,
dataset, skill, template, or evaluation work and explicitly related
manifestations. Forks, mirrors, releases, registry entries, and papers are not
independent artifacts by default.

## Boundaries

- **Cutoff:** freeze at actual campaign start.
- **Language:** English-primary plus justified Chinese search terms and native
  routes for AI-assisted qualitative analysis; label every language limitation.
- **Sources:** public metadata, official documentation, lawful public full
  text, repositories, registries, Zenodo/OSF, scholarly indexes, and linked
  evaluations.
- **Inspection only:** no candidate download, installation, import, build,
  execution, preservation, account connection, or maintainer contact.
- Search results, snippets, stars, citation counts, and model summaries are
  discovery metadata, not evidence of quality or usefulness.

## Include

Artifacts must directly implement or evaluate at least one proposed machinery
cell:

1. `GT-M02-C01` identity, lineage, and baseline deduplication;
2. `GT-M02-C02` episode/incident segmentation and temporal reconstruction;
3. `GT-M02-C03` initial/open/action-oriented/in-vivo coding;
4. `GT-M02-C04` inspectable constant comparison;
5. `GT-M02-C05` memo/codebook/category/property/version management;
6. `GT-M02-C06` theoretical-sampling, negative-case, and rival routing;
7. `GT-M02-C07` saturation/sufficiency and unresolved-route tracking;
8. `GT-M02-C08` provenance, quotes, timestamps, translation, rights/privacy;
9. `GT-M02-C09` multi-coder or human/AI review and adjudication;
10. `GT-M02-C10` process-model/Gioia/proposition/claim-evidence export;
11. `GT-M02-C11` benchmarks, reliability, drift, and documented failures; or
12. `GT-M02-C12` maintenance, interoperability, version, license, and adoption
    seams.

## Exclude or hold as context

- empirical papers merely using grounded theory;
- generic thematic analysis or sentiment/topic-modeling tools with no relevant
  workflow;
- generic note-taking, transcription, literature-review, survey-analysis, or
  chatbot products;
- proprietary product pages without inspectable reusable machinery;
- substantive “grounded theory” in unrelated scientific senses;
- repository popularity as a quality proxy; and
- candidates whose identity, license scope, or current manifestation cannot be
  resolved.

## Planned retrieval frames

1. `F01` terminology, exact-title, topic, README, and code discovery across
   GitHub and other public forges.
2. `F02` scholarly index, Zenodo, OSF, and research-software catalog searches.
3. `F03` citation, author, maintainer, organization, dependency, sibling, and
   reverse-snowball graph traversals.
4. `F04` package and extension registries with upstream-repository resolution.
5. `F05` exact capability probes for the proposed machinery cells.
6. `F06` negative, criticism, failure, disagreement, reliability, and
   terminology-confusion searches.
7. `F07` zero-credit import and deduplication against
   `2026-07-28__theory-building` and other relevant landed campaigns.
8. `F08` thin-cell, recency, and justified Chinese-language backstops.

Every frame runs or receives an explicit `partial`, `blocked`, or
`not-applicable` limitation. GitHub candidates resolve to stable repository ID,
canonical owner/name, default branch, exact commit, license manifestation, and
fork/mirror/move relations.

## Review and scoring

Discovery does not score its own rows. A non-authoring reviewer may apply the
Scout six-dimension rubric—authority, task relevance, reusable machinery,
provenance precision, license clarity, and maintenance evidence—with exact
locators. Scores prioritize inspection; they do not establish correctness,
methodological validity, license compatibility, or acquisition authority.

## Resource and stop draft

- Resource ceiling: two to three sessions and approximately four to six total
  wall-clock hours unless the Operator freezes another bound.
- Marginal-yield threshold: `K = 2` retained qualified identities per
  materially independent post-merge pass.
- Working plateau requires every machinery cell dispositioned, every planned
  frame run or limited, no high-priority unresolved frontier, and two
  independent post-merge passes adding zero new classes and no more than `K`
  retained identities each.
- Any new plausible identity or class resets the relevant clock.
- At the ceiling with positive yield, close `high-coverage, effort-bounded,
  not saturated`.

## Bundle and landing

Produce only the lean bundle:

```text
SCOPE.md
SEARCH_LOG.jsonl
SCREENING.jsonl
EVIDENCE_LEDGER.jsonl
FINDINGS.md
SHA256SUMS
```

Validate from the pinned lean Scout skill, obtain independent review, then land
only the exact accepted six-file bundle under the canonical Scout repository
path. Verify the remote tree, commit, and manifest after push. Campaign-level
prose belongs outside the validator-bound directory unless a later Scout
contract explicitly changes its allowlist.

The canonical Scout repository's current `main` is supervised beta and is not
an execution-method qualification. This plan uses the lean skill pinned by the
Evidence-First protocol and treats the Scout repository only as the future
campaign landing target unless the Operator separately ratifies its controller.

## Handoff ceiling

The landed Scout bundle is discovery and coverage memory. Each claim used by
`GT-M01` must be reconstructed as an Evidence-First record from the actual
manifestation. Nothing in the bundle admits evidence, licenses acquisition,
validates software, establishes completeness, or authorizes the grounded-
theory tool design.

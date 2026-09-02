# GT-M01 lane catalog — Evidence-First grounded-theory methods

**State:** proposed; unfired; not a launch instrument
**Mission:** `GT-M01`
**Catalog size:** 15 evidence-acquisition worker lanes plus one mission-level
synthesis step
**Acquisition-lane handoff:** exactly `R001`–`R010`; a worker creates no
`R011`

`GT-M01-L01`–`L15` are bounded Evidence-First worker questions and handoffs. If
an acquisition question cannot be answered within ten records, the lane closes
partial and a later architecture amendment must split the unresolved question
into a new lane. An audit or resume never extends the same worker beyond
`R010`. `GT-M01-L16` is the one non-acquisition commander synthesis step; it is
expressly exempt from `records.jsonl`, `searchlog.md`, retained-source bytes,
and the `R001`–`R010` rule.

## Shared lane contract

Before query 1, each live acquisition-lane constitution must name its exact root, worker,
attempt, cutoff, search mode, source ownership, vault, rights rule, and
independent reviewer. It returns only the protocol's three-file handoff plus
retained bytes and `SHA256SUMS` in the authorized external vault.

A lane with `search_engine: scout` also retains the exact six-file lean Scout
bundle in the authorized campaign workspace or external vault. It must receive
a FULL structural validation; its displayed `bundle_sha256` is captured
programmatically into the lane `searchlog.md` and batch handoff beside the
exact bundle path. Scout query/screening rows remain canonical in the bundle
and are not mirrored into `searchlog.md`. Scout findings remain discovery
provenance: every claim entering synthesis still requires an ordinary
Evidence-First record bound to the retained manifestation and independent
adjudication.

Unless a lane freezes a stricter rule, it may stop short of ten only after one
of these is documented:

1. at least three independent source families, including meaningful
   rival/null/contrary evidence;
2. two consecutive reasonable searches adding nothing load-bearing; or
3. lawful-access blocks.

`closed-partial` is truthful completion. Blocked, thin, inaccessible, capped,
or positive-tail routes remain unknown. Discovery metadata, Scout output, and
repository claims are not admitted evidence.

## Frozen planning catalog

| Lane | Search engine | Bounded question and owned source classes | Rival/null duty | Dependency and exact handoff |
|---|---|---|---|---|
| `GT-M01-L01` | `scout: high-recall-map` | Which shared commitments and incompatible assumptions distinguish Glaserian, Straussian, constructivist, and explicitly adjacent grounded-theory profiles? Own foundational and lineage-defining methods manifestations. | Locate disputes and evidence against an undisclosed hybrid profile. | Dependency-free; hand off a lineage comparison with claims bound to exact current records. |
| `GT-M01-L02` | `direct` | How should an analyst reconstruct episodes and incidents from process traces while preserving uncertain boundaries and temporal order? Own named process-method and archival-trace sources. | Find cases where segmentation creates false sequence or inferred intent. | Dependency-free; hand off an episode/incident boundary contract. |
| `GT-M01-L03` | `direct` | How should initial, open, action-oriented, in-vivo, and bilingual coding move from incident to provisional concept? Own coding-method and translation-method sources. | Find early abstraction, forced coding, or translation choices that erase action or participant terms. | Uses `L01` vocabulary only after admission; hand off an initial-coding contract and bilingual cautions. |
| `GT-M01-L04` | `direct` | What must constant-comparison records preserve across incident–incident, incident–code, and code–category comparisons? Own constant-comparison sources. | Locate nominal comparison practices with no inspectable contrast or consequence. | Uses `L02` incident definition; hand off a comparison-record specification. |
| `GT-M01-L05` | `direct` | How should memo types, reflexivity, category properties, dimensions, boundaries, and version changes remain inspectable? Own memoing and category-development sources. | Find overwrite, prompt anchoring, or memo practices that conceal category change. | Uses `L03` and `L04`; hand off memo and category-version requirements. |
| `GT-M01-L06` | `direct` | How should theoretical sampling follow a category uncertainty, rival, boundary, or relationship rather than a fixed topical checklist? Own theoretical-sampling sources. | Find requests that cannot discriminate among explanations or would merely add examples. | Uses `L05`; hand off a sampling-request contract and refusal cases. |
| `GT-M01-L07` | `direct` | How should negative and deviant cases revise, split, bound, or retire categories and proposed mechanisms? Own negative-case and rival-explanation sources. | Find workflows that label counterevidence yet leave the theory unchanged. | Uses `L04`–`L06`; hand off category-change consequences and rival duties. |
| `GT-M01-L08` | `scout: high-recall-map` | What do saturation, theoretical sufficiency, information power, and adjacent stop doctrines permit in bounded archival work? Own the stop-doctrine landscape; deduplicate versions and debates. | Preserve positive tails, thin cells, language limits, and critiques of premature saturation. | Dependency-free; hand off permissible stop language and unresolved disputes. |
| `GT-M01-L09` | `scout: high-recall-map` | What evidentiary and inferential rules apply to screen recordings, livestreams, making-of material, walkthroughs, diaries, interviews, and digital traces without researcher-conducted interviews? Own archival/public-process methods sources. | Contrast observed action, creator-stated interpretation, edited retrospection, context-only material, and missing sequence. | Uses `L02`; hand off a source-strata and epistemic-class contract. |
| `GT-M01-L10` | `scout: rapid-scout` | How should same-creator longitudinal evidence and earlier sequential, hybrid, and newer direct-generation regimes be compared without equating release date, product capability, and observed workflow? Own longitudinal and technological-regime method sources. | Seek unchanged workflows, direct control successes, and alternative cost/access explanations. | Uses `L02` and `L09`; hand off a longitudinal/regime comparison design. |
| `GT-M01-L11` | `direct` | How should temporal bracketing, turning points, pathways, mechanisms, and boundary conditions support process theorizing? Own named process-theory methods sources. | Find cross-sectional theme structures that cannot account for transitions. | Uses `L02`, `L04`, and `L10`; hand off a process-model contract. |
| `GT-M01-L12` | `scout: high-recall-map` | What can CAQDAS, computational qualitative methods, and LLM assistance validly automate or assist? Own empirical evaluation and failure manifestations, not product marketing. | Seek bias, leakage, drift, hallucination, non-reproducibility, and automation-induced forcing. | Uses `L01` profile constraints; hand off an assistance/abstention boundary and evaluation requirements. |
| `GT-M01-L13` | `scout: rapid-scout` | What review designs make human/AI disagreement, adjudication, provenance, reliability, and reproducibility inspectable? Own human/AI evaluation and audit-method sources. | Find self-scoring, circular criteria, superficial agreement, and unstable model/prompt cases. | Uses `L12`; hand off independent-review and drift-test requirements. |
| `GT-M01-L14` | `direct` | How do Gioia data structures and management-research reporting relate to, but differ from, grounded theory and evidence admission? Own named reporting/editorial sources. | Find polished structures or propositions unsupported by incident-level records. | Uses `L01`, `L04`, and `L11`; hand off reporting and paper-boundary rules. |
| `GT-M01-L15` | `direct` | What ethics, consent, privacy, rights, retention, translation, reflexivity, authorship, model-processing, and release controls govern the first pilot? Own authoritative ethics, law/policy, platform, and research-governance sources within the frozen jurisdiction. | Find technically traceable but impermissible, unsafe, or misleading practices. | Cross-cutting; hand off a decision register with unresolved authority questions, not legal conclusions. |
| `GT-M01-L16` | `synthesis; no search` | What bounded method profile and tool controls are justified by current independently adjudicated records from `L01`–`L15`? Own no new external sources. | Preserve unresolved disputes, rivals, negative cases, and proposition-specific falsifiers; reject unsupported integration. | Commander step only after upstream adjudication; hand off the single `GT_LITE` synthesis and claim-to-record matrix. No worker, Scout bundle, three-file acquisition handoff, or `R###` records. |

## Source-ownership and overlap law

- Each exact manifestation has one owning lane. Another lane references its
  stable ID and hash instead of reacquiring or silently extracting it again.
- `GT-M02` owns only artifact identity, documented machinery, license and
  maintenance state, and evaluation leads. `GT-M01-L12` and `L13` own any
  admitted methodological-validity or empirical-performance claims.
- `GT-M02` may identify process-model or Gioia exporters; `GT-M01-L14` decides
  what those forms can methodologically represent.
- `GT-M02` may identify segmentation and provenance machinery;
  `GT-M01-L02` and `L09` decide the analysis and inference rules.
- The Evidence-First mission does not consume Scout scores, stars, snippets,
  or validator status as evidence.

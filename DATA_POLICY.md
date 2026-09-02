# Data policy

## Repository contents

Git may contain only reusable method documentation, code, schemas, synthetic
fixtures, and non-claim-bearing tool tests. A private repository is still not a
source vault.

## External study vault

Real studies use an ignored `.vault-root` pointing to a private location such
as:

```text
<vault>/studies/<study-id>/
  manifestations/
  raw/
  normalized/
  cycles/C001/
  handoff/
  quarantine/
  SHA256SUMS
```

Each cycle freezes an input manifest and appends analysis outputs. Raw source
bytes are immutable. Normalized material keeps a hash-bound link to its source.
Correction uses explicit successors; deletion, redaction, and erasure require
their own authority and receipts.

## Privacy and processing

Before any ingestion, record lawful access, consent or other authority,
retention, access class, redaction, cloud-model eligibility, and whether a
source includes personal, confidential, or proprietary material. Local
possession does not imply permission to upload to a model provider.

## Research outputs

Codes, memos, categories, and propositions may themselves be sensitive. They
remain in the study workspace until an independent review authorizes a
sanitized package. No tool license grants rights in study data or third-party
material.

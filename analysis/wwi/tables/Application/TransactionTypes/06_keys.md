---
id: wwi:object:1765581328
subject: wwi/tables/Application/TransactionTypes
item: 06
topic: keys
tier: minimum
summary: Primary key unique and gapless; TransactionTypeName is declared unique.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-18T20:32:00Z
step: S08-061
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ab99183e84a70c79c56e7558ecb1bf1eb540afb1bb72a065d9070c0c89f4bbcf
last_checked_at: 2026-10-18T20:32:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=686f522d33a3aaf4 | recheck=a unique constraint changes | text: Declared unique besides the primary key: UQ_Application_TransactionTypes_TransactionTypeName (TransactionTypeName).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=5bf2df42b3d3567f | recheck=the key range changes | text: The key runs from 1 to 13 with no gap.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=686f522d33a3aaf4 | recheck=a foreign key changes | text: 1 declared foreign key, all enabled and trusted: LastEditedBy -> Application.People.PersonID.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=686f522d33a3aaf4 | recheck=every new extract, or a schema change | text: Business key candidate: the unique name (TransactionTypeName is declared unique); the numeric key is the source's surrogate.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

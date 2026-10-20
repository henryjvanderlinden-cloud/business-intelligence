---
id: wwi:object:98099390
subject: wwi/tables/Warehouse/PackageTypes
item: 27
topic: peculiarities
tier: minimum
summary: Nothing beyond the batch-edit signature of the audit columns.
confidence: high
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 0263ce1739bb24cfa1adc545bdeab338bb4e156512ec4dcf93e55e467793997d
last_checked_at: 2026-10-20T08:31:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=16ad09f897cb33f1 | recheck=the empty-column patterns change | text: Test 8: 1 distinct pattern of empty columns; the most common: 14 rows with none empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=16ad09f897cb33f1 | recheck=a row breaks a dependency | text: Test 1: 0 functional dependencies between non-key columns over the whole extract (0 involving audit columns, a batch-edit signature, not listed).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=16ad09f897cb33f1 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=16ad09f897cb33f1 | recheck=every new extract, or a schema change | text: Tests 1 to 18 find nothing further, apart from LastEditedBy and ValidFrom determining each other, which shows rows changed in batches by one editor at a time.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

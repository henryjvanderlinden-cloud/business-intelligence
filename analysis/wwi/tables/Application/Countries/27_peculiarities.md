---
id: wwi:object:1461580245
subject: wwi/tables/Application/Countries
item: 27
topic: peculiarities
tier: minimum
summary: See claims.
confidence: high
claims: 7
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 4840337d7b437a1e0ba71ae6b072f3f504e276f802274f763ad925b52a0bcc05
last_checked_at: 2026-10-20T05:44:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f4e8a61674553cd9 | recheck=the empty-column patterns change | text: Test 8: 1 distinct pattern of empty columns; the most common: 190 rows with none empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f4e8a61674553cd9 | recheck=a row breaks a dependency | text: Test 1: 1 functional dependency between non-key columns over the whole extract (1 involving audit columns, a batch-edit signature, not listed): Subregion -> Region.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f4e8a61674553cd9 | recheck=the structured columns change | text: Test 6: Border holds geography.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f4e8a61674553cd9 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f4e8a61674553cd9 | recheck=every new extract, or a schema change | text: Tests 1 to 18 find nothing further, apart from LastEditedBy and ValidFrom determining each other, which shows rows changed in batches by one editor at a time.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f4e8a61674553cd9 | recheck=every new extract, or a schema change | text: CountryType has one value (UN Member State) in all 190 rows; Subregion determines Region.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f4e8a61674553cd9 | recheck=every new extract, or a schema change | text: The geography column Border holds country boundaries; large values (the countries file is 0.97 MB for 190 rows).

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

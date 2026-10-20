---
id: wwi:object:290100074
subject: wwi/tables/Application/StateProvinces
item: 27
topic: peculiarities
tier: minimum
summary: A sales attribute (SalesTerritory) lives in geography; one state has no boundary.
confidence: high
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: b85fd6a1b65683d407663a7b52ebc7c96f376f8345323ada5a5fc81b70edef97
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=42d1716e974f6792 | recheck=the empty-column patterns change | text: Test 8: 2 distinct patterns of empty columns; the most common: 52 rows with none empty; 1 rows with Border empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=42d1716e974f6792 | recheck=the pattern changes | text: Test 8, by SalesTerritory (partial): SalesTerritory=Southeast (12 rows): empty -; filled Border | SalesTerritory=Plains (7 rows): empty -; filled Border | SalesTerritory=Far West (6 rows): empty -; filled Border | SalesTerritory=New England (6 rows): empty -; filled Border | SalesTerritory=Mideast (6 rows): empty -; filled Border | SalesTerritory=Rocky Mountain (5 rows): empty -; filled Border | SalesTerritory=Great Lakes (5 rows): empty -; filled Border | SalesTerritory=Southwest (4 rows): empty -; filled Border | SalesTerritory=External (2 rows): empty -; filled -; partly empty Border (1 empty).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=42d1716e974f6792 | recheck=a row breaks a dependency | text: Test 1: 0 functional dependencies between non-key columns over the whole extract (1 involving audit columns, a batch-edit signature, not listed).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=42d1716e974f6792 | recheck=the structured columns change | text: Test 6: Border holds geography.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=42d1716e974f6792 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=42d1716e974f6792 | recheck=every new extract, or a schema change | text: Test 1: SalesTerritory is an organisational grouping held on a geographic table: one entity riding on another.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

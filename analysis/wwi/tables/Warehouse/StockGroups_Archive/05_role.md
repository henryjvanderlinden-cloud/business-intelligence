---
id: wwi:object:274100017
subject: wwi/tables/Warehouse/StockGroups_Archive
item: 05
topic: role
tier: minimum
summary: History of Warehouse.StockGroups (earlier row versions), not a separate entity.
confidence: high
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: e95d0e414e870e18e624d3a1e63d4219e1116a6fc359fd638fb4ba9a22247f02
last_checked_at: 2026-10-19T09:21:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ac07b33aa08ecae8 | recheck=a foreign key changes | text: It refers to no table and is referred to by no table.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ac07b33aa08ecae8 | recheck=the temporal type changes | text: This is a history table of system-versioning.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ac07b33aa08ecae8 | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ac07b33aa08ecae8,e0bdeee03e2c4729 | recheck=every new extract, or a schema change | text: History table of Warehouse.StockGroups: one row per earlier version of a Warehouse.StockGroups row, current from ValidFrom to ValidTo; 1 rows for 1 distinct StockGroupID values; versions ended between 2016-01-01 and 2016-01-01.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ac07b33aa08ecae8 | recheck=every new extract, or a schema change | text: Role: not a separate entity; it holds the earlier versions of Warehouse.StockGroups and never the current one.

## Reasoning

The catalogue declares the table a history table of Warehouse.StockGroups; the period columns bound each version.

## Uncertainties

None.

## For a person

None.

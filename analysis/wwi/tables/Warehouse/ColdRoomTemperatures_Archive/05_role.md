---
id: wwi:object:1413580074
subject: wwi/tables/Warehouse/ColdRoomTemperatures_Archive
item: 05
topic: role
tier: minimum
summary: The readings history of the four cold-room sensors (3.7 million readings), stored as the history of a latest-state table.
confidence: high
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 14944a147c4e342c01346a89c29d042ac1cf08b8a5e6a7295cf5942e81465a82
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a3812e9428769e55 | recheck=a foreign key changes | text: It refers to no table and is referred to by no table.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a3812e9428769e55 | recheck=the temporal type changes | text: This is a history table of system-versioning.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a3812e9428769e55 | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: RecordedWhen; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a3812e9428769e55,fe99989aa94f128c | recheck=every new extract, or a schema change | text: History table of Warehouse.ColdRoomTemperatures: one row per earlier version of a Warehouse.ColdRoomTemperatures row, current from ValidFrom to ValidTo; 3,676,804 rows for 3,676,804 distinct ColdRoomTemperatureID values; versions ended between 2015-12-20 and 2016-06-01.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a3812e9428769e55 | recheck=every new extract, or a schema change | text: Role: technically the history of Warehouse.ColdRoomTemperatures, which holds only the latest reading per sensor; in substance the earlier readings themselves (next claim).
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=832defd8d73a4d23 | recheck=every new extract, or a schema change | text: Unlike the other history tables, this one holds the bulk of the data: 3,676,804 rows, 919,201 for each of the four sensors, recorded from 2015-12-20 to 2016-06-01, each with ValidFrom equal to its RecordedWhen - each version is one earlier reading.

## Reasoning

The catalogue declares the table a history table of Warehouse.ColdRoomTemperatures; the period columns bound each version.

## Uncertainties

None.

## For a person

None.

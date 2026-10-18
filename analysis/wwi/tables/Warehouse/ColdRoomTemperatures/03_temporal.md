---
id: wwi:object:1179151246
subject: wwi/tables/Warehouse/ColdRoomTemperatures
item: 03
topic: temporal
tier: minimum
summary: System-versioned with a twist: each new reading supersedes the sensor's row, so the history table holds the readings history (3.7 million readings since 2015-12-20).
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 14944a147c4e342c01346a89c29d042ac1cf08b8a5e6a7295cf5942e81465a82
last_checked_at: 2026-10-18T13:20:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=17b318403896763e | recheck=the temporal type changes | text: The table is system-versioned: SQL Server keeps every earlier version of a row in Warehouse.ColdRoomTemperatures_Archive, with the period columns ValidFrom and ValidTo.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=07d5cc7116d2d8eb | recheck=every new extract | text: Between the extracts of 31 May and 1 June 2016: 4 inserted, 4 deleted, 0 updated; columns updated: none.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=17b318403896763e | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: RecordedWhen; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=a time zone is found in documentation | text: The time zone of RecordedWhen is not established; the catalogue states none.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=d661ae2a5f707ded | recheck=every new extract, or a schema change | text: The current rows were recorded at 2016-06-01 23:59:29; their earlier readings are versions in Warehouse.ColdRoomTemperatures_Archive.
- C6 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=17b318403896763e | recheck=every new extract, or a schema change | text: For analysis the history table is the event table; this table is only the latest state.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

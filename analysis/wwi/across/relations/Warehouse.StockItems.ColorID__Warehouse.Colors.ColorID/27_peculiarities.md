---
id: wwi:fk:FK_Warehouse_StockItems_ColorID_Warehouse_Colors
subject: wwi/across/relations/Warehouse.StockItems.ColorID__Warehouse.Colors.ColorID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, current versions.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 7f2be19c3bec3dfaa2cf1d0d972280f70a5b83ca8275da11edc46e79ce32b255
last_checked_at: 2026-10-20T08:31:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of either table
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a3ec82e828529934 | recheck=every new extract | text: Fan-out: joined from Warehouse.Colors to Warehouse.StockItems, a Warehouse.Colors row repeats up to 51 times (median 9), so a measure of Warehouse.Colors summed after the join is counted once per referring row.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a3ec82e828529934 | recheck=the temporal type changes | text: Warehouse.Colors is system-versioned and the extract holds its current versions: joined in the extract, a row of Warehouse.StockItems that names a row of Warehouse.Colors gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

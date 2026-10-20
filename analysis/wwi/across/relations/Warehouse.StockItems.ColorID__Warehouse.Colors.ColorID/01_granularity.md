---
id: wwi:fk:FK_Warehouse_StockItems_ColorID_Warehouse_Colors
subject: wwi/across/relations/Warehouse.StockItems.ColorID__Warehouse.Colors.ColorID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Warehouse.StockItems to Warehouse.Colors; up to 51 rows of Warehouse.StockItems per row of Warehouse.Colors.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 7f2be19c3bec3dfaa2cf1d0d972280f70a5b83ca8275da11edc46e79ce32b255
last_checked_at: 2026-10-20T05:51:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a3ec82e828529934 | recheck=the foreign key changes | text: Declared foreign key FK_Warehouse_StockItems_ColorID_Warehouse_Colors from Warehouse.StockItems.ColorID to Warehouse.Colors.ColorID, the primary key of Warehouse.Colors: each row of Warehouse.StockItems names at most one row of Warehouse.Colors.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a3ec82e828529934 | recheck=every new extract | text: In this extract 128 of 227 rows of Warehouse.StockItems name one of 7 referenced rows of Warehouse.Colors (of 36); children per referenced parent: from 2 to 51, median 9; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a3ec82e828529934 | recheck=every new extract | text: Joined from Warehouse.StockItems to Warehouse.Colors, the result keeps the grain of Warehouse.StockItems: one row per row of Warehouse.StockItems (an inner join drops the 99 rows where ColorID is empty). Joined the other way, each row of Warehouse.Colors repeats once per row of Warehouse.StockItems that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

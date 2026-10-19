---
id: wwi:fk:FK_Sales_OrderLines_PackageTypeID_Warehouse_PackageTypes
subject: wwi/across/relations/Sales.OrderLines.PackageTypeID__Warehouse.PackageTypes.PackageTypeID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.OrderLines to Warehouse.PackageTypes; up to 221,108 rows of Sales.OrderLines per row of Warehouse.PackageTypes.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 6ec6db0daaefc5126117aa00224ac9f501cdb894baeefdb8d83d089ce099dd19
last_checked_at: 2026-10-19T20:31:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=44309cee7cdb9590 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_OrderLines_PackageTypeID_Warehouse_PackageTypes from Sales.OrderLines.PackageTypeID to Warehouse.PackageTypes.PackageTypeID, the primary key of Warehouse.PackageTypes: each row of Sales.OrderLines names at most one row of Warehouse.PackageTypes.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=44309cee7cdb9590 | recheck=every new extract | text: In this extract 231,581 of 231,581 rows of Sales.OrderLines name one of 4 referenced rows of Warehouse.PackageTypes (of 14); children per referenced parent: from 1,044 to 221,108, median 4,714.5; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=44309cee7cdb9590 | recheck=every new extract | text: Joined from Sales.OrderLines to Warehouse.PackageTypes, the result keeps the grain of Sales.OrderLines: one row per row of Sales.OrderLines. Joined the other way, each row of Warehouse.PackageTypes repeats once per row of Sales.OrderLines that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

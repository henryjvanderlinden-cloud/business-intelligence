---
id: wwi:fk:FK_Purchasing_PurchaseOrderLines_PackageTypeID_Warehouse_PackageTypes
subject: wwi/across/relations/Purchasing.PurchaseOrderLines.PackageTypeID__Warehouse.PackageTypes.PackageTypeID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.PurchaseOrderLines to Warehouse.PackageTypes; up to 5,779 rows of Purchasing.PurchaseOrderLines per row of Warehouse.PackageTypes.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 52aea873bfad767fb478c98b26e0deb4a904de2bea1769eb74bb6d7cee9c2b30
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2e6764acf424b782 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_PurchaseOrderLines_PackageTypeID_Warehouse_PackageTypes from Purchasing.PurchaseOrderLines.PackageTypeID to Warehouse.PackageTypes.PackageTypeID, the primary key of Warehouse.PackageTypes: each row of Purchasing.PurchaseOrderLines names at most one row of Warehouse.PackageTypes.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2e6764acf424b782 | recheck=every new extract | text: In this extract 8,376 of 8,376 rows of Purchasing.PurchaseOrderLines name one of 3 referenced rows of Warehouse.PackageTypes (of 14); children per referenced parent: from 9 to 5,779, median 2,588; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2e6764acf424b782 | recheck=every new extract | text: Joined from Purchasing.PurchaseOrderLines to Warehouse.PackageTypes, the result keeps the grain of Purchasing.PurchaseOrderLines: one row per row of Purchasing.PurchaseOrderLines. Joined the other way, each row of Warehouse.PackageTypes repeats once per row of Purchasing.PurchaseOrderLines that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

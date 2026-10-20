---
id: wwi:fk:FK_Purchasing_Suppliers_SupplierCategoryID_Purchasing_SupplierCategories
subject: wwi/across/relations/Purchasing.Suppliers.SupplierCategoryID__Purchasing.SupplierCategories.SupplierCategoryID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.Suppliers to Purchasing.SupplierCategories; up to 6 rows of Purchasing.Suppliers per row of Purchasing.SupplierCategories.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 7095eed2c5b53b68acacfebfd7dba9faed29c90ddae3ad76579ad1581e94d64a
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0b103f7d0f8528d0 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_Suppliers_SupplierCategoryID_Purchasing_SupplierCategories from Purchasing.Suppliers.SupplierCategoryID to Purchasing.SupplierCategories.SupplierCategoryID, the primary key of Purchasing.SupplierCategories: each row of Purchasing.Suppliers names at most one row of Purchasing.SupplierCategories.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0b103f7d0f8528d0 | recheck=every new extract | text: In this extract 13 of 13 rows of Purchasing.Suppliers name one of 8 referenced rows of Purchasing.SupplierCategories (of 9); children per referenced parent: from 1 to 6, median 1; 7 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0b103f7d0f8528d0 | recheck=every new extract | text: Joined from Purchasing.Suppliers to Purchasing.SupplierCategories, the result keeps the grain of Purchasing.Suppliers: one row per row of Purchasing.Suppliers. Joined the other way, each row of Purchasing.SupplierCategories repeats once per row of Purchasing.Suppliers that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

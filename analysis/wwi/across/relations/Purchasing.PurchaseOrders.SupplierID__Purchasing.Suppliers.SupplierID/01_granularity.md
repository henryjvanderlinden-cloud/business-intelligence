---
id: wwi:fk:FK_Purchasing_PurchaseOrders_SupplierID_Purchasing_Suppliers
subject: wwi/across/relations/Purchasing.PurchaseOrders.SupplierID__Purchasing.Suppliers.SupplierID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.PurchaseOrders to Purchasing.Suppliers; up to 1,056 rows of Purchasing.PurchaseOrders per row of Purchasing.Suppliers.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 3d59c7196fb503ddc827836282e1c08c87f7e19face754e7b256c4d417da0956
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=b03c22ce446e89d3 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_PurchaseOrders_SupplierID_Purchasing_Suppliers from Purchasing.PurchaseOrders.SupplierID to Purchasing.Suppliers.SupplierID, the primary key of Purchasing.Suppliers: each row of Purchasing.PurchaseOrders names at most one row of Purchasing.Suppliers.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=b03c22ce446e89d3 | recheck=every new extract | text: In this extract 2,076 of 2,076 rows of Purchasing.PurchaseOrders name one of 7 referenced rows of Purchasing.Suppliers (of 13); children per referenced parent: from 1 to 1,056, median 10; 1 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=b03c22ce446e89d3 | recheck=every new extract | text: Joined from Purchasing.PurchaseOrders to Purchasing.Suppliers, the result keeps the grain of Purchasing.PurchaseOrders: one row per row of Purchasing.PurchaseOrders. Joined the other way, each row of Purchasing.Suppliers repeats once per row of Purchasing.PurchaseOrders that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

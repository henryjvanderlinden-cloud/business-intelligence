---
id: wwi:relation:Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID
subject: wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: header join.
confidence: high
claims: 1
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 664bf3ce1e6055fd58b043e3d15e68a5454133c32d67454d5cd298527fed3ba5
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3f3748bd53d11df3 | recheck=every new extract | text: Header join: joined on PurchaseOrderID alone, the two tables give 43,007 rows instead of the 8,367 that the full combination gives: every referring row is paired with every row of Purchasing.PurchaseOrderLines for the same PurchaseOrderID.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence. The tests for roles, chasm traps, system-versioning and two routes are run on declared foreign keys only; for this undeclared relation they were not run.

## Uncertainties

None.

## For a person

None.

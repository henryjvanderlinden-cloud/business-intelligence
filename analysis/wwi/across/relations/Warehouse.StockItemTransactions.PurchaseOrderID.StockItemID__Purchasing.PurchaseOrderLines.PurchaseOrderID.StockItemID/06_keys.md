---
id: wwi:relation:Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID
subject: wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID
item: 06
topic: keys
tier: minimum
summary: Undeclared: Warehouse.StockItemTransactions.PurchaseOrderID + StockItemID against Purchasing.PurchaseOrderLines.PurchaseOrderID + StockItemID, unique in this extract.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 664bf3ce1e6055fd58b043e3d15e68a5454133c32d67454d5cd298527fed3ba5
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3f3748bd53d11df3 | recheck=a constraint is declared | text: Child side: Warehouse.StockItemTransactions.PurchaseOrderID + StockItemID, not declared as a foreign key; parent side: Purchasing.PurchaseOrderLines.PurchaseOrderID + StockItemID, not declared unique.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3f3748bd53d11df3 | recheck=every new extract | text: In this extract PurchaseOrderID + StockItemID is unique over all 8,376 rows of Purchasing.PurchaseOrderLines.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

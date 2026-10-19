---
id: wwi:relation:Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID
subject: wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID
item: 02
topic: meaning
tier: minimum
summary: A stock receipt is the receipt of one purchase-order line; 9 lines have no receipt yet. Undeclared.
confidence: unknown
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

- C1 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3f3748bd53d11df3,a2e0c315ed6cbd6f,196f36476eced6f4 | recheck=every new extract, or a description changes | text: A stock receipt records the receipt of one purchase-order line: 8,367 receipts match 8,367 lines one-to-one on (PurchaseOrderID, StockItemID); 9 lines have no receipt in this extract. Nothing declares it; (PurchaseOrderID, StockItemID) is unique in both tables in this extract (round 1).
- C2 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=none | recheck=a second extract with a partial receipt, or the generating script, settles it | text: How a receipt in parts is recorded - several movements per line, one movement updated, or a movement only once the line is complete - is not established: one extract shows one movement per received line and nothing else.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

The receipt lifecycle of a purchase-order line.

## For a person

None.

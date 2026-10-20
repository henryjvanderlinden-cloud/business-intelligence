---
id: wwi:fk:FK_Warehouse_StockItemTransactions_PurchaseOrderID_Purchasing_PurchaseOrders
subject: wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID
item: 06
topic: keys
tier: minimum
summary: Warehouse.StockItemTransactions.PurchaseOrderID refers to the primary key Purchasing.PurchaseOrders.PurchaseOrderID, enforced.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: abd4db31387266f8dd2ffeedb2855f9677180a94426c561e7b4f576d7d7fde6d
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3057590bbabac1bd | recheck=the foreign key changes | text: Child side: Warehouse.StockItemTransactions.PurchaseOrderID, int, nullable; a foreign key, enabled and trusted; on delete no action.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3057590bbabac1bd | recheck=the primary key changes | text: Parent side: Purchasing.PurchaseOrders.PurchaseOrderID, the declared primary key of Purchasing.PurchaseOrders.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3057590bbabac1bd | recheck=every new extract | text: No other column of Purchasing.PurchaseOrders that is unique in this extract holds all values of PurchaseOrderID: the primary key is the only key the values fit.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

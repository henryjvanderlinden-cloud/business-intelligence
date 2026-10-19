---
id: wwi:fk:FK_Warehouse_StockItemTransactions_SupplierID_Purchasing_Suppliers
subject: wwi/across/relations/Warehouse.StockItemTransactions.SupplierID__Purchasing.Suppliers.SupplierID
item: 02
topic: meaning
tier: minimum
summary: Supplier for this stock transaction (if applicable)
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 64f9c755200145c5a0f3c045d46a5e6a0cc04d2761cbf34329dd4550a470e63d
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ae6e827f1610550e | recheck=the description changes | text: The source describes Warehouse.StockItemTransactions.SupplierID as "Supplier for this stock transaction (if applicable)".
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ae6e827f1610550e | recheck=every new extract, or a description changes | text: For receipts, the supplier the stock came from; it equals both the purchase order's supplier and the item's usual supplier on all 8,367 receipts (27).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

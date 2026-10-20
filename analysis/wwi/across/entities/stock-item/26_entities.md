---
id: wwi:entity:stock-item
subject: wwi/across/entities/stock-item
item: 26
topic: entities
tier: best-effort
summary: Warehouse.StockItems, versioned, with a one-to-one holding row, many-to-many stock groups, and lines and movements that name it.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: readings by claude-opus-5-5 linking the claims that own each fact; written by prototypes/information_analysis/write_glossary.py (blob ffcc3813a793cc9facce4b98cc396d0f16cffa08)
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: none
last_checked_at: 2026-10-20T05:51:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: a linked claim changes
---

## Claims

- C1 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Warehouse.StockItemHoldings is a one-to-one extension of the item outside system-versioning (across/relations/Warehouse.StockItemHoldings.StockItemID__Warehouse.StockItems.StockItemID/02_meaning.md#C2).
- C2 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Items and stock groups are many-to-many through Warehouse.StockItemStockGroups (across/relations/Warehouse.StockItemStockGroups.StockGroupID__Warehouse.StockGroups.StockGroupID/27_peculiarities.md#C4).
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Joined in the extract, invoice lines, order lines, purchase-order lines and stock movements get the item's current version; the versions current at their dates differ from it only in CustomFields and Tags, other audit and period columns not compared (across/relations/Sales.InvoiceLines.StockItemID__Warehouse.StockItems.StockItemID/03_temporal.md#C3, #C4; the same claims in the 03 files of Sales.OrderLines.StockItemID, Purchasing.PurchaseOrderLines.StockItemID and Warehouse.StockItemTransactions.StockItemID to Warehouse.StockItems).

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.

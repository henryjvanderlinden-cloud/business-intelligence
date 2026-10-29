---
id: nsdn:rv:link:stock_movement__purchase_order
kind: link
name: lnk_stock_movement__purchase_order
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 49
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: movement purchase order
from: hub_stock_movement
to: hub_purchase_order
driving: hub_stock_movement
optional: yes
effectivity: event
effectivity_start: Warehouse.StockItemTransactions.TransactionOccurredWhen
subject_area: ledgers
optional_note: receipts only
---

## Columns

- Warehouse.StockItemTransactions.PurchaseOrderID | names=hub_purchase_order

## Relations

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID

## Evidence

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID/02_meaning.md#C2
- analysis/wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID/07_population.md#C2

---
id: nsdn:rv:link:purchase_order_line__stock_item
kind: link
name: lnk_purchase_order_line__stock_item
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 40
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: purchase-order line item
from: hub_purchase_order_line
to: hub_stock_item
driving: hub_purchase_order_line
optional: no
effectivity: event
effectivity_start: unknown
subject_area: purchasing
---

## Columns

- Purchasing.PurchaseOrderLines.StockItemID | names=hub_stock_item

## Relations

- analysis/wwi/across/relations/Purchasing.PurchaseOrderLines.StockItemID__Warehouse.StockItems.StockItemID

## Evidence

- analysis/wwi/across/relations/Purchasing.PurchaseOrderLines.StockItemID__Warehouse.StockItems.StockItemID/07_population.md#C2

## Notes

148 gives this link an event start, but its driving hub, a line, has no event date of its own (147 section 5), so the start is unknown until the author rules; see ARC-OP-29.

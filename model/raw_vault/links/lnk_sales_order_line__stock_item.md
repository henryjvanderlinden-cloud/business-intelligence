---
id: nsdn:rv:link:sales_order_line__stock_item
kind: link
name: lnk_sales_order_line__stock_item
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 27
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: order line item
from: hub_sales_order_line
to: hub_stock_item
driving: hub_sales_order_line
optional: no
effectivity: event
subject_area: sales
---

## Columns

- Sales.OrderLines.OrderLineID | end=from | effectivity_start=unknown
- Sales.OrderLines.StockItemID | end=to

## Relations

- analysis/wwi/across/relations/Sales.OrderLines.StockItemID__Warehouse.StockItems.StockItemID

## Evidence

- analysis/wwi/across/relations/Sales.OrderLines.StockItemID__Warehouse.StockItems.StockItemID/01_granularity.md#C1

## Notes

148 gives this link an event start, but its driving hub, a line, has no event date of its own (147 section 5), so the start is unknown until the author rules; see ARC-OP-29.

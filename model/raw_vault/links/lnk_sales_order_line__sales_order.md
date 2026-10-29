---
id: nsdn:rv:link:sales_order_line__sales_order
kind: link
name: lnk_sales_order_line__sales_order
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 26
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: order line of order
from: hub_sales_order_line
to: hub_sales_order
driving: hub_sales_order_line
optional: no
effectivity: event
effectivity_start: unknown
subject_area: sales
---

## Columns

- Sales.OrderLines.OrderID | names=hub_sales_order

## Relations

- analysis/wwi/across/relations/Sales.OrderLines.OrderID__Sales.Orders.OrderID

## Evidence

- analysis/wwi/across/relations/Sales.OrderLines.OrderID__Sales.Orders.OrderID/02_meaning.md#C2

## Notes

148 gives this link an event start, but its driving hub, a line, has no event date of its own (147 section 5), so the start is unknown until the author rules; see ARC-OP-29.

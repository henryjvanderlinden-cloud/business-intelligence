---
id: nsdn:rv:link:purchase_order_line__purchase_order
kind: link
name: lnk_purchase_order_line__purchase_order
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 39
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: purchase-order line of order
from: hub_purchase_order_line
to: hub_purchase_order
driving: hub_purchase_order_line
optional: no
effectivity: event
subject_area: purchasing
---

## Columns

- Purchasing.PurchaseOrderLines.PurchaseOrderLineID | end=from | effectivity_start=unknown
- Purchasing.PurchaseOrderLines.PurchaseOrderID | end=to

## Relations

- analysis/wwi/across/relations/Purchasing.PurchaseOrderLines.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID

## Evidence

- analysis/wwi/across/relations/Purchasing.PurchaseOrderLines.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID/02_meaning.md#C2

## Notes

148 gives this link an event start, but its driving hub, a line, has no event date of its own (147 section 5), so the start is unknown until the author rules; see ARC-OP-29.

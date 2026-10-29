---
id: nsdn:rv:link:sales_order__backorder
kind: link
name: lnk_sales_order__backorder
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 25
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: backorder named
from: hub_sales_order
to: hub_sales_order
driving: hub_sales_order
optional: yes
effectivity: event
subject_area: sales
---

## Columns

- Sales.Orders.OrderID | end=from | effectivity_start=Sales.Orders.OrderDate
- Sales.Orders.BackorderOrderID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Orders.BackorderOrderID__Sales.Orders.OrderID

## Evidence

- analysis/wwi/across/relations/Sales.Orders.BackorderOrderID__Sales.Orders.OrderID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.Orders.BackorderOrderID__Sales.Orders.OrderID/02_meaning.md#C3
- analysis/wwi/across/relations/Sales.Orders.BackorderOrderID__Sales.Orders.OrderID/07_population.md#C2

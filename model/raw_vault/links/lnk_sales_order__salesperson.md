---
id: nsdn:rv:link:sales_order__salesperson
kind: link
name: lnk_sales_order__salesperson
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 22
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: order salesperson
from: hub_sales_order
to: hub_person
driving: hub_sales_order
optional: no
effectivity: event
subject_area: sales
---

## Columns

- Sales.Orders.OrderID | end=from | effectivity_start=Sales.Orders.OrderDate
- Sales.Orders.SalespersonPersonID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Orders.SalespersonPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Sales.Orders.SalespersonPersonID__Application.People.PersonID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.Orders.SalespersonPersonID__Application.People.PersonID/02_meaning.md#C3

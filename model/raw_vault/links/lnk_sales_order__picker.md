---
id: nsdn:rv:link:sales_order__picker
kind: link
name: lnk_sales_order__picker
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 24
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: order picker
from: hub_sales_order
to: hub_person
driving: hub_sales_order
optional: yes
effectivity: milestone
subject_area: sales
---

## Columns

- Sales.Orders.OrderID | end=from | effectivity_start=Sales.Orders.PickingCompletedWhen
- Sales.Orders.PickedByPersonID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Orders.PickedByPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Sales.Orders.PickedByPersonID__Application.People.PersonID/02_meaning.md#C3
- analysis/wwi/across/relations/Sales.Orders.PickedByPersonID__Application.People.PersonID/07_population.md#C2

---
id: nsdn:rv:link:sales_order__contact
kind: link
name: lnk_sales_order__contact
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 23
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: order customer contact
from: hub_sales_order
to: hub_person
driving: hub_sales_order
optional: no
effectivity: event
effectivity_start: Sales.Orders.OrderDate
subject_area: sales
---

## Columns

- Sales.Orders.ContactPersonID | names=hub_person

## Relations

- analysis/wwi/across/relations/Sales.Orders.ContactPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Sales.Orders.ContactPersonID__Application.People.PersonID/02_meaning.md#C3

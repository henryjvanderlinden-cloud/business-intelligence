---
id: nsdn:rv:link:purchase_order__contact
kind: link
name: lnk_purchase_order__contact
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 38
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: purchase order contact
from: hub_purchase_order
to: hub_person
driving: hub_purchase_order
optional: no
effectivity: event
effectivity_start: Purchasing.PurchaseOrders.OrderDate
subject_area: purchasing
---

## Columns

- Purchasing.PurchaseOrders.ContactPersonID | names=hub_person

## Relations

- analysis/wwi/across/relations/Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID/02_meaning.md#C2
- analysis/wwi/across/relations/Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID/02_meaning.md#C3
- analysis/wwi/across/relations/Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID/02_meaning.md#C4

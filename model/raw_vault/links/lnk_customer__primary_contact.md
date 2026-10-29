---
id: nsdn:rv:link:customer__primary_contact
kind: link
name: lnk_customer__primary_contact
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 8
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: customer primary contact
from: hub_customer
to: hub_person
driving: hub_customer
optional: no
effectivity: load
subject_area: parties
---

## Columns

- Sales.Customers.CustomerID | end=from | effectivity_start=load
- Sales.Customers.PrimaryContactPersonID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Customers.PrimaryContactPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Sales.Customers.PrimaryContactPersonID__Application.People.PersonID/02_meaning.md#C3

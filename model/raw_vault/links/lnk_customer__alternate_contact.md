---
id: nsdn:rv:link:customer__alternate_contact
kind: link
name: lnk_customer__alternate_contact
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 9
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: customer alternate contact
from: hub_customer
to: hub_person
driving: hub_customer
optional: yes
effectivity: load
effectivity_start: load
subject_area: parties
---

## Columns

- Sales.Customers.AlternateContactPersonID | names=hub_person

## Relations

- analysis/wwi/across/relations/Sales.Customers.AlternateContactPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Sales.Customers.AlternateContactPersonID__Application.People.PersonID/02_meaning.md#C3
- analysis/wwi/across/relations/Sales.Customers.AlternateContactPersonID__Application.People.PersonID/07_population.md#C2

---
id: nsdn:rv:link:supplier__primary_contact
kind: link
name: lnk_supplier__primary_contact
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 12
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: supplier primary contact
from: hub_supplier
to: hub_person
driving: hub_supplier
optional: no
effectivity: load
subject_area: parties
---

## Columns

- Purchasing.Suppliers.SupplierID | end=from | effectivity_start=load
- Purchasing.Suppliers.PrimaryContactPersonID | end=to

## Relations

- analysis/wwi/across/relations/Purchasing.Suppliers.PrimaryContactPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Purchasing.Suppliers.PrimaryContactPersonID__Application.People.PersonID/02_meaning.md#C2
- analysis/wwi/across/relations/Purchasing.Suppliers.PrimaryContactPersonID__Application.People.PersonID/07_population.md#C2

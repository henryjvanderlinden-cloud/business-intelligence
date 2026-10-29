---
id: nsdn:rv:link:invoice__contact
kind: link
name: lnk_invoice__contact
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 32
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: invoice customer contact
from: hub_invoice
to: hub_person
driving: hub_invoice
optional: no
effectivity: event
subject_area: sales
---

## Columns

- Sales.Invoices.InvoiceID | end=from | effectivity_start=Sales.Invoices.InvoiceDate
- Sales.Invoices.ContactPersonID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Invoices.ContactPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Sales.Invoices.ContactPersonID__Application.People.PersonID/02_meaning.md#C3

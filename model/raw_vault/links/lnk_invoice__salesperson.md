---
id: nsdn:rv:link:invoice__salesperson
kind: link
name: lnk_invoice__salesperson
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 31
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: invoice salesperson
from: hub_invoice
to: hub_person
driving: hub_invoice
optional: no
effectivity: event
effectivity_start: Sales.Invoices.InvoiceDate
subject_area: sales
---

## Columns

- Sales.Invoices.SalespersonPersonID | names=hub_person

## Relations

- analysis/wwi/across/relations/Sales.Invoices.SalespersonPersonID__Application.People.PersonID

## Evidence

- analysis/wwi/across/relations/Sales.Invoices.SalespersonPersonID__Application.People.PersonID/02_meaning.md#C3

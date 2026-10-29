---
id: nsdn:rv:link:invoice_line__invoice
kind: link
name: lnk_invoice_line__invoice
status: accepted
ruled_in: ADR-0031, ADR-0030, ADR-0034
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 35
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: invoice line of invoice
from: hub_invoice_line
to: hub_invoice
driving: hub_invoice_line
optional: no
effectivity: event
subject_area: sales
---

## Columns

- Sales.InvoiceLines.InvoiceLineID | end=from | effectivity_start=unknown
- Sales.InvoiceLines.InvoiceID | end=to

## Relations

- analysis/wwi/across/relations/Sales.InvoiceLines.InvoiceID__Sales.Invoices.InvoiceID

## Evidence

- analysis/wwi/across/relations/Sales.InvoiceLines.InvoiceID__Sales.Invoices.InvoiceID/02_meaning.md#C2

## Notes

148 gives this link an event start, but its driving hub, a line, has no event date of its own (147 section 5); the author ruled that the start stays unknown (ADR-0034 decision 4).

---
id: nsdn:rv:link:invoice_line__invoice
kind: link
name: lnk_invoice_line__invoice
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 35
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: invoice line of invoice
from: hub_invoice_line
to: hub_invoice
driving: hub_invoice_line
optional: no
effectivity: event
effectivity_start: unknown
subject_area: sales
---

## Columns

- Sales.InvoiceLines.InvoiceID | names=hub_invoice

## Relations

- analysis/wwi/across/relations/Sales.InvoiceLines.InvoiceID__Sales.Invoices.InvoiceID

## Evidence

- analysis/wwi/across/relations/Sales.InvoiceLines.InvoiceID__Sales.Invoices.InvoiceID/02_meaning.md#C2

## Notes

148 gives this link an event start, but its driving hub, a line, has no event date of its own (147 section 5), so the start is unknown until the author rules; see ARC-OP-29.

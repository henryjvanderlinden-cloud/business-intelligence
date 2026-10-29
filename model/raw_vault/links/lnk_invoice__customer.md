---
id: nsdn:rv:link:invoice__customer
kind: link
name: lnk_invoice__customer
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 29
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: invoice customer (delivered to)
from: hub_invoice
to: hub_customer
driving: hub_invoice
optional: no
effectivity: event
subject_area: sales
---

## Columns

- Sales.Invoices.InvoiceID | end=from | effectivity_start=Sales.Invoices.InvoiceDate
- Sales.Invoices.CustomerID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID

## Evidence

- analysis/wwi/across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2

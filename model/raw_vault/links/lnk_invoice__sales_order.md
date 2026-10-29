---
id: nsdn:rv:link:invoice__sales_order
kind: link
name: lnk_invoice__sales_order
status: accepted
ruled_in: ADR-0031, ADR-0030, ADR-0034
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 28
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: invoice of order
from: hub_invoice
to: hub_sales_order
driving: hub_invoice
optional: yes
effectivity: event
subject_area: sales
optional_note: in the data, nullable
---

## Columns

- Sales.Invoices.InvoiceID | end=from | effectivity_start=Sales.Invoices.InvoiceDate
- Sales.Invoices.OrderID | end=to

## Relations

- analysis/wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID

## Evidence

- analysis/wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID/01_granularity.md#C4

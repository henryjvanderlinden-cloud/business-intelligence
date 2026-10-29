---
id: nsdn:rv:link:invoice__sales_order
kind: link
name: lnk_invoice__sales_order
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 28
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: invoice of order
from: hub_invoice
to: hub_sales_order
driving: hub_invoice
optional: yes
effectivity: event
effectivity_start: Sales.Invoices.InvoiceDate
subject_area: sales
optional_note: in the data, nullable
---

## Columns

- Sales.Invoices.OrderID | names=hub_sales_order

## Relations

- analysis/wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID

## Evidence

- analysis/wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID/01_granularity.md#C4

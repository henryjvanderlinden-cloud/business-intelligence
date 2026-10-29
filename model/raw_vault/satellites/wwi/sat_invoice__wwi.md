---
id: nsdn:rv:sat:invoice__wwi
kind: satellite
name: sat_invoice__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.4
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_invoice
source: wwi
source_table: Sales.Invoices
parent_key: Sales.Invoices.InvoiceID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: Sales.Invoices.InvoiceDate
class: internal
class_condition: personal in the instructions where the customer is an individual
subject_area: sales
---

## Columns

- InvoiceDate
- DeliveryMethodID | code=ref_delivery_method__wwi
- CustomerPurchaseOrderNumber
- IsCreditNote
- CreditNoteReason
- Comments
- DeliveryInstructions
- InternalComments
- TotalDryItems
- TotalChillerItems
- DeliveryRun
- RunPosition
- OrderID | as_delivered=lnk_invoice__sales_order

## Evidence

- analysis/wwi/tables/Sales/Invoices/03_temporal.md#C3
- analysis/wwi/tables/Sales/Invoices/19_sensitivity.md#C5
- analysis/wwi/tables/Sales/Invoices/19_sensitivity.md#C6

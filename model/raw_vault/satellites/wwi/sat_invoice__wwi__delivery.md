---
id: nsdn:rv:sat:invoice__wwi__delivery
kind: satellite
name: sat_invoice__wwi__delivery
status: accepted
ruled_in: ADR-0033, ADR-0028
defined_in: docs/10_architecture/149_wwi-satellites.md#3.4
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_invoice
source: wwi
source_table: Sales.Invoices
parent_key: Sales.Invoices.InvoiceID
satellite_kind: milestone
split_reason: milestone (ADR-0028) and sensitivity
valid_time: Sales.Invoices.ConfirmedDeliveryTime
class: personal
subject_area: sales
---

## Columns

- ReturnedDeliveryData
- ConfirmedDeliveryTime
- ConfirmedReceivedBy

## Evidence

- analysis/wwi/tables/Sales/Invoices/03_temporal.md#C5
- analysis/wwi/tables/Sales/Invoices/19_sensitivity.md#C4
- analysis/wwi/tables/Sales/Invoices/19_sensitivity.md#C7

---
id: nsdn:rv:sat:invoice_line__wwi
kind: satellite
name: sat_invoice_line__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.4
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_invoice_line
source: wwi
source_table: Sales.InvoiceLines
parent_key: Sales.InvoiceLines.InvoiceLineID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: unknown (no own date)
class: confidential
subject_area: sales
---

## Columns

- Description
- PackageTypeID | code=ref_package_type__wwi
- Quantity
- UnitPrice
- TaxRate
- TaxAmount
- LineProfit
- ExtendedPrice

## Evidence

- analysis/wwi/tables/Sales/InvoiceLines/03_temporal.md#C5
- analysis/wwi/tables/Sales/InvoiceLines/19_sensitivity.md#C3
- analysis/wwi/tables/Sales/InvoiceLines/09_derived.md

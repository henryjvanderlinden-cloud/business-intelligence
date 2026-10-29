---
id: nsdn:rv:sat:sales_order_line__wwi
kind: satellite
name: sat_sales_order_line__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.4
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_sales_order_line
source: wwi
source_table: Sales.OrderLines
parent_key: Sales.OrderLines.OrderLineID
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

## Evidence

- analysis/wwi/tables/Sales/OrderLines/03_temporal.md#C3
- analysis/wwi/tables/Sales/OrderLines/19_sensitivity.md

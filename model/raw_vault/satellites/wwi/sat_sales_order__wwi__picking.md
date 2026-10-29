---
id: nsdn:rv:sat:sales_order__wwi__picking
kind: satellite
name: sat_sales_order__wwi__picking
status: accepted
ruled_in: ADR-0033, ADR-0028
defined_in: docs/10_architecture/149_wwi-satellites.md#3.4
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_sales_order
source: wwi
source_table: Sales.Orders
parent_key: Sales.Orders.OrderID
satellite_kind: milestone
split_reason: milestone (ADR-0028)
valid_time: Sales.Orders.PickingCompletedWhen
class: internal
subject_area: sales
---

## Columns

- PickingCompletedWhen
- PickedByPersonID | as_delivered=lnk_sales_order__picker

## Evidence

- analysis/wwi/tables/Sales/Orders/03_temporal.md#C2
- analysis/wwi/tables/Sales/Orders/03_temporal.md#C7

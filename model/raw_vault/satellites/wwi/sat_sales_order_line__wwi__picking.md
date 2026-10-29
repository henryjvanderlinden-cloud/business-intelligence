---
id: nsdn:rv:sat:sales_order_line__wwi__picking
kind: satellite
name: sat_sales_order_line__wwi__picking
status: accepted
ruled_in: ADR-0033, ADR-0028
defined_in: docs/10_architecture/149_wwi-satellites.md#3.4
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_sales_order_line
source: wwi
source_table: Sales.OrderLines
parent_key: Sales.OrderLines.OrderLineID
satellite_kind: milestone
split_reason: milestone (ADR-0028)
valid_time: Sales.OrderLines.PickingCompletedWhen
class: internal
subject_area: sales
---

## Columns

- PickedQuantity
- PickingCompletedWhen

## Evidence

- analysis/wwi/tables/Sales/OrderLines/03_temporal.md#C2
- analysis/wwi/tables/Sales/OrderLines/03_temporal.md#C5

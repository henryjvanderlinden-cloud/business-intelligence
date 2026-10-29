---
id: nsdn:rv:sat:sales_order__wwi
kind: satellite
name: sat_sales_order__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.4
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_sales_order
source: wwi
source_table: Sales.Orders
parent_key: Sales.Orders.OrderID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: Sales.Orders.OrderDate
class: internal
subject_area: sales
---

## Columns

- OrderDate
- ExpectedDeliveryDate
- CustomerPurchaseOrderNumber
- IsUndersupplyBackordered
- Comments
- DeliveryInstructions
- InternalComments
- BackorderOrderID | as_delivered=lnk_sales_order__backorder

## Evidence

- analysis/wwi/tables/Sales/Orders/03_temporal.md#C2
- analysis/wwi/tables/Sales/Orders/03_temporal.md#C6

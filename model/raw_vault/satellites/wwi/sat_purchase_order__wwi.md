---
id: nsdn:rv:sat:purchase_order__wwi
kind: satellite
name: sat_purchase_order__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.5
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_purchase_order
source: wwi
source_table: Purchasing.PurchaseOrders
parent_key: Purchasing.PurchaseOrders.PurchaseOrderID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: Purchasing.PurchaseOrders.OrderDate (the undated finalisation: unknown)
class: internal
subject_area: purchasing
---

## Columns

- OrderDate
- DeliveryMethodID | code=ref_delivery_method__wwi
- ExpectedDeliveryDate
- SupplierReference
- IsOrderFinalized | valid_time=unknown (finalisation undated)
- Comments
- InternalComments

## Evidence

- analysis/wwi/tables/Purchasing/PurchaseOrders/03_temporal.md#C2
- analysis/wwi/tables/Purchasing/PurchaseOrders/03_temporal.md#C5

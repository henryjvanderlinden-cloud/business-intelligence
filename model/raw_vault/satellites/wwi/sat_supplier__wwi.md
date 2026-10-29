---
id: nsdn:rv:sat:supplier__wwi
kind: satellite
name: sat_supplier__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.2
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_supplier
source: wwi
source_table: Purchasing.Suppliers
parent_key: Purchasing.Suppliers.SupplierID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: unknown
class: internal
subject_area: parties
---

## Columns

- SupplierName
- SupplierCategoryID
- DeliveryMethodID | code=ref_delivery_method__wwi
- SupplierReference
- PaymentDays

## Evidence

- analysis/wwi/tables/Purchasing/Suppliers/06_keys.md#C5

---
id: nsdn:rv:sat:supplier__wwi__address
kind: satellite
name: sat_supplier__wwi__address
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.2
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_supplier
source: wwi
source_table: Purchasing.Suppliers
parent_key: Purchasing.Suppliers.SupplierID
satellite_kind: payload
split_reason: rate of change (DeliveryLocation, all 13)
valid_time: unknown
class: internal
subject_area: parties
---

## Columns

- PhoneNumber
- FaxNumber
- WebsiteURL
- DeliveryAddressLine1
- DeliveryAddressLine2
- DeliveryPostalCode
- DeliveryLocation
- PostalAddressLine1
- PostalAddressLine2
- PostalPostalCode

## Evidence

- analysis/wwi/tables/Purchasing/Suppliers/06_keys.md#C5

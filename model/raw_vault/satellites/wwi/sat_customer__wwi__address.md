---
id: nsdn:rv:sat:customer__wwi__address
kind: satellite
name: sat_customer__wwi__address
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.2
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_customer
source: wwi
source_table: Sales.Customers
parent_key: Sales.Customers.CustomerID
satellite_kind: payload
split_reason: sensitivity
valid_time: unknown
class: internal
class_condition: personal where the customer is an individual
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

- analysis/wwi/tables/Sales/Customers/19_sensitivity.md#C1
- analysis/wwi/tables/Sales/Customers/19_sensitivity.md#C4

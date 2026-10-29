---
id: nsdn:rv:sat:customer__wwi
kind: satellite
name: sat_customer__wwi
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
split_reason: none (main satellite)
valid_time: unknown
class: internal
class_condition: personal where the customer is an individual
subject_area: parties
---

## Columns

- CustomerName
- AccountOpenedDate
- DeliveryMethodID | code=ref_delivery_method__wwi
- DeliveryRun
- RunPosition
- BuyingGroupID | as_delivered=lnk_customer__buying_group
- AlternateContactPersonID | as_delivered=lnk_customer__alternate_contact

## Evidence

- analysis/wwi/tables/Sales/Customers/06_keys.md#C5
- analysis/wwi/tables/Sales/Customers/19_sensitivity.md#C4
- analysis/wwi/tables/Sales/Customers/19_sensitivity.md#C6

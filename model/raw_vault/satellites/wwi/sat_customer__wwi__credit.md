---
id: nsdn:rv:sat:customer__wwi__credit
kind: satellite
name: sat_customer__wwi__credit
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.2
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_customer
source: wwi
source_table: Sales.Customers
parent_key: Sales.Customers.CustomerID
satellite_kind: payload
split_reason: rate of change (CreditLimit, 46 customers) and sensitivity
valid_time: unknown
class: confidential
subject_area: parties
---

## Columns

- CreditLimit
- StandardDiscountPercentage
- IsStatementSent
- IsOnCreditHold
- PaymentDays

## Evidence

- analysis/wwi/tables/Sales/Customers/06_keys.md#C5

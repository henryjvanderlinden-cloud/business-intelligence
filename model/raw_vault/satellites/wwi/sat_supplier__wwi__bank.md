---
id: nsdn:rv:sat:supplier__wwi__bank
kind: satellite
name: sat_supplier__wwi__bank
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
split_reason: sensitivity (masked by the source itself)
valid_time: unknown
class: restricted
subject_area: parties
---

## Columns

- BankAccountName
- BankAccountBranch
- BankAccountCode
- BankAccountNumber
- BankInternationalCode

## Evidence

- analysis/wwi/tables/Purchasing/Suppliers/19_sensitivity.md#C4
- analysis/wwi/tables/Purchasing/Suppliers/19_sensitivity.md#C5

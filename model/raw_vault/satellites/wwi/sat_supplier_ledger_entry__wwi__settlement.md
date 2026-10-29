---
id: nsdn:rv:sat:supplier_ledger_entry__wwi__settlement
kind: satellite
name: sat_supplier_ledger_entry__wwi__settlement
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.6
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_supplier_ledger_entry
source: wwi
source_table: Purchasing.SupplierTransactions
parent_key: Purchasing.SupplierTransactions.SupplierTransactionID
satellite_kind: payload
split_reason: rate of change (settled later, as on the customer side)
valid_time: unknown: no write-back seen (ADR-0028, Consequences)
class: confidential
subject_area: ledgers
---

## Columns

- OutstandingBalance
- FinalizationDate
- IsFinalized

## Evidence

- analysis/wwi/tables/Purchasing/SupplierTransactions/03_temporal.md#C5
- analysis/wwi/tables/Purchasing/SupplierTransactions/03_temporal.md#C6
- analysis/wwi/_source/22_stability.md#C21

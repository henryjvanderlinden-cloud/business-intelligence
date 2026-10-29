---
id: nsdn:rv:sat:customer_ledger_entry__wwi__finalisation
kind: satellite
name: sat_customer_ledger_entry__wwi__finalisation
status: accepted
ruled_in: ADR-0033, ADR-0028
defined_in: docs/10_architecture/149_wwi-satellites.md#3.6
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_customer_ledger_entry
source: wwi
source_table: Sales.CustomerTransactions
parent_key: Sales.CustomerTransactions.CustomerTransactionID
satellite_kind: milestone
split_reason: milestone (ADR-0028)
valid_time: Sales.CustomerTransactions.FinalizationDate
class: confidential
subject_area: ledgers
---

## Columns

- OutstandingBalance
- FinalizationDate
- IsFinalized

## Evidence

- analysis/wwi/tables/Sales/CustomerTransactions/03_temporal.md#C5
- analysis/wwi/tables/Sales/CustomerTransactions/03_temporal.md#C6

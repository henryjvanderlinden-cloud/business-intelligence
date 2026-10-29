---
id: nsdn:rv:hub:customer_ledger_entry
kind: hub
name: hub_customer_ledger_entry
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 18
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: customer ledger entry
grain: one invoice or payment entry
subject_area: ledgers
---

## Business key

- Sales.CustomerTransactions.CustomerTransactionID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Sales/CustomerTransactions/06_keys.md#C1
- analysis/wwi/tables/Sales/CustomerTransactions/06_keys.md#C3
- analysis/wwi/tables/Sales/CustomerTransactions/03_temporal.md#C5

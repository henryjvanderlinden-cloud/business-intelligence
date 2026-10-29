---
id: nsdn:rv:hub:supplier_ledger_entry
kind: hub
name: hub_supplier_ledger_entry
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 19
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: supplier ledger entry
grain: one supplier invoice or payment
subject_area: ledgers
---

## Business key

- Purchasing.SupplierTransactions.SupplierTransactionID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Purchasing/SupplierTransactions/06_keys.md#C1
- analysis/wwi/tables/Purchasing/SupplierTransactions/06_keys.md#C3

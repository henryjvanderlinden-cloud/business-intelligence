---
id: nsdn:rv:sat:customer_ledger_entry__wwi
kind: satellite
name: sat_customer_ledger_entry__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.6
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_customer_ledger_entry
source: wwi
source_table: Sales.CustomerTransactions
parent_key: Sales.CustomerTransactions.CustomerTransactionID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: Sales.CustomerTransactions.TransactionDate
class: confidential
subject_area: ledgers
---

## Columns

- TransactionTypeID
- PaymentMethodID | code=ref_payment_method__wwi
- TransactionDate
- AmountExcludingTax
- TaxAmount
- TransactionAmount
- InvoiceID | as_delivered=lnk_customer_ledger_entry__invoice

## Evidence

- analysis/wwi/tables/Sales/CustomerTransactions/03_temporal.md#C3
- analysis/wwi/tables/Sales/CustomerTransactions/09_derived.md

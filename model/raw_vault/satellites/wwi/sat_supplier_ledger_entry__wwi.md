---
id: nsdn:rv:sat:supplier_ledger_entry__wwi
kind: satellite
name: sat_supplier_ledger_entry__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.6
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_supplier_ledger_entry
source: wwi
source_table: Purchasing.SupplierTransactions
parent_key: Purchasing.SupplierTransactions.SupplierTransactionID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: Purchasing.SupplierTransactions.TransactionDate
class: confidential
subject_area: ledgers
---

## Columns

- TransactionTypeID
- PaymentMethodID | code=ref_payment_method__wwi
- SupplierInvoiceNumber
- TransactionDate
- AmountExcludingTax
- TaxAmount
- TransactionAmount
- PurchaseOrderID | as_delivered=lnk_supplier_ledger_entry__purchase_order

## Evidence

- analysis/wwi/tables/Purchasing/SupplierTransactions/03_temporal.md#C3
- analysis/wwi/tables/Purchasing/SupplierTransactions/09_derived.md

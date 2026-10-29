---
id: nsdn:rv:link:supplier_ledger_entry__supplier
kind: link
name: lnk_supplier_ledger_entry__supplier
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 43
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: supplier entry account
from: hub_supplier_ledger_entry
to: hub_supplier
driving: hub_supplier_ledger_entry
optional: no
effectivity: event
subject_area: ledgers
---

## Columns

- Purchasing.SupplierTransactions.SupplierTransactionID | end=from | effectivity_start=Purchasing.SupplierTransactions.TransactionDate
- Purchasing.SupplierTransactions.SupplierID | end=to

## Relations

- analysis/wwi/across/relations/Purchasing.SupplierTransactions.SupplierID__Purchasing.Suppliers.SupplierID

## Evidence

- analysis/wwi/across/relations/Purchasing.SupplierTransactions.SupplierID__Purchasing.Suppliers.SupplierID/02_meaning.md#C2

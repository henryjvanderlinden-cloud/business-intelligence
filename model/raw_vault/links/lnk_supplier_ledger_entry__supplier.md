---
id: nsdn:rv:link:supplier_ledger_entry__supplier
kind: link
name: lnk_supplier_ledger_entry__supplier
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 43
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: supplier entry account
from: hub_supplier_ledger_entry
to: hub_supplier
driving: hub_supplier_ledger_entry
optional: no
effectivity: event
effectivity_start: Purchasing.SupplierTransactions.TransactionDate
subject_area: ledgers
---

## Columns

- Purchasing.SupplierTransactions.SupplierID | names=hub_supplier

## Relations

- analysis/wwi/across/relations/Purchasing.SupplierTransactions.SupplierID__Purchasing.Suppliers.SupplierID

## Evidence

- analysis/wwi/across/relations/Purchasing.SupplierTransactions.SupplierID__Purchasing.Suppliers.SupplierID/02_meaning.md#C2

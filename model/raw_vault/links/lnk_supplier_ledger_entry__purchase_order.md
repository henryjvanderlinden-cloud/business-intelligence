---
id: nsdn:rv:link:supplier_ledger_entry__purchase_order
kind: link
name: lnk_supplier_ledger_entry__purchase_order
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 44
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: supplier entry purchase order
from: hub_supplier_ledger_entry
to: hub_purchase_order
driving: hub_supplier_ledger_entry
optional: yes
effectivity: event
effectivity_start: Purchasing.SupplierTransactions.TransactionDate
subject_area: ledgers
optional_note: payments
---

## Columns

- Purchasing.SupplierTransactions.PurchaseOrderID | names=hub_purchase_order

## Relations

- analysis/wwi/across/relations/Purchasing.SupplierTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID

## Evidence

- analysis/wwi/across/relations/Purchasing.SupplierTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID/02_meaning.md#C2
- analysis/wwi/across/relations/Purchasing.SupplierTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID/07_population.md#C2

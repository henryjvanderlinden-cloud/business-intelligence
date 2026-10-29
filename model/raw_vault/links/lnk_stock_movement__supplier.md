---
id: nsdn:rv:link:stock_movement__supplier
kind: link
name: lnk_stock_movement__supplier
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 48
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: movement supplier
from: hub_stock_movement
to: hub_supplier
driving: hub_stock_movement
optional: yes
effectivity: event
subject_area: ledgers
optional_note: receipts only
---

## Columns

- Warehouse.StockItemTransactions.StockItemTransactionID | end=from | effectivity_start=Warehouse.StockItemTransactions.TransactionOccurredWhen
- Warehouse.StockItemTransactions.SupplierID | end=to

## Relations

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.SupplierID__Purchasing.Suppliers.SupplierID

## Evidence

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.SupplierID__Purchasing.Suppliers.SupplierID/02_meaning.md#C2
- analysis/wwi/across/relations/Warehouse.StockItemTransactions.SupplierID__Purchasing.Suppliers.SupplierID/07_population.md#C2

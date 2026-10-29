---
id: nsdn:rv:link:stock_movement__customer
kind: link
name: lnk_stock_movement__customer
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 46
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: movement customer (issued to)
from: hub_stock_movement
to: hub_customer
driving: hub_stock_movement
optional: yes
effectivity: event
subject_area: ledgers
optional_note: issues only
---

## Columns

- Warehouse.StockItemTransactions.StockItemTransactionID | end=from | effectivity_start=Warehouse.StockItemTransactions.TransactionOccurredWhen
- Warehouse.StockItemTransactions.CustomerID | end=to

## Relations

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.CustomerID__Sales.Customers.CustomerID

## Evidence

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2
- analysis/wwi/across/relations/Warehouse.StockItemTransactions.CustomerID__Sales.Customers.CustomerID/07_population.md#C2

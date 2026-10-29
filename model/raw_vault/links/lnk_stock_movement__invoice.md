---
id: nsdn:rv:link:stock_movement__invoice
kind: link
name: lnk_stock_movement__invoice
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 47
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: movement invoice
from: hub_stock_movement
to: hub_invoice
driving: hub_stock_movement
optional: yes
effectivity: event
subject_area: ledgers
optional_note: issues only
---

## Columns

- Warehouse.StockItemTransactions.StockItemTransactionID | end=from | effectivity_start=Warehouse.StockItemTransactions.TransactionOccurredWhen
- Warehouse.StockItemTransactions.InvoiceID | end=to

## Relations

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.InvoiceID__Sales.Invoices.InvoiceID

## Evidence

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.InvoiceID__Sales.Invoices.InvoiceID/02_meaning.md#C2
- analysis/wwi/across/relations/Warehouse.StockItemTransactions.InvoiceID__Sales.Invoices.InvoiceID/07_population.md#C2

---
id: nsdn:rv:link:stock_movement__stock_item
kind: link
name: lnk_stock_movement__stock_item
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 45
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: movement item
from: hub_stock_movement
to: hub_stock_item
driving: hub_stock_movement
optional: no
effectivity: event
effectivity_start: Warehouse.StockItemTransactions.TransactionOccurredWhen
subject_area: ledgers
---

## Columns

- Warehouse.StockItemTransactions.StockItemID | names=hub_stock_item

## Relations

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.StockItemID__Warehouse.StockItems.StockItemID

## Evidence

- analysis/wwi/across/relations/Warehouse.StockItemTransactions.StockItemID__Warehouse.StockItems.StockItemID/01_granularity.md#C1

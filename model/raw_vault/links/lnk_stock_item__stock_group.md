---
id: nsdn:rv:link:stock_item__stock_group
kind: link
name: lnk_stock_item__stock_group
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 15
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: stock item in stock group
from: hub_stock_item
to: hub_stock_group
driving: none
optional: no
effectivity: absence
subject_area: products and deals
---

## Columns

- Warehouse.StockItemStockGroups.StockItemID | end=from | effectivity_start=presence in a complete extract
- Warehouse.StockItemStockGroups.StockGroupID | end=to
- Warehouse.StockItemStockGroups.StockItemStockGroupID | kept=effectivity satellite, as delivered

## Relations

- analysis/wwi/across/relations/Warehouse.StockItemStockGroups.StockItemID__Warehouse.StockItems.StockItemID
- analysis/wwi/across/relations/Warehouse.StockItemStockGroups.StockGroupID__Warehouse.StockGroups.StockGroupID

## Evidence

- analysis/wwi/across/relations/Warehouse.StockItemStockGroups.StockItemID__Warehouse.StockItems.StockItemID/02_meaning.md#C2

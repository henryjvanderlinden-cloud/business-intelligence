---
id: nsdn:rv:link:special_deal__stock_item
kind: link
name: lnk_special_deal__stock_item
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 19
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: deal for stock item
from: hub_special_deal
to: hub_stock_item
driving: hub_special_deal
optional: yes
effectivity: load
effectivity_start: load
subject_area: products and deals
optional_note: empty: discounts only
---

## Columns

- Sales.SpecialDeals.StockItemID | names=hub_stock_item

## Relations

- analysis/wwi/across/relations/Sales.SpecialDeals.StockItemID__Warehouse.StockItems.StockItemID

## Evidence

- analysis/wwi/across/relations/Sales.SpecialDeals.StockItemID__Warehouse.StockItems.StockItemID/02_meaning.md#C2
- analysis/wwi/across/relations/Sales.SpecialDeals.StockItemID__Warehouse.StockItems.StockItemID/07_population.md#C2

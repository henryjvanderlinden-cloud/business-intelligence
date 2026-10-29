---
id: nsdn:rv:link:special_deal__stock_group
kind: link
name: lnk_special_deal__stock_group
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 20
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: deal for stock group
from: hub_special_deal
to: hub_stock_group
driving: hub_special_deal
optional: yes
effectivity: load
effectivity_start: load
subject_area: products and deals
---

## Columns

- Sales.SpecialDeals.StockGroupID | names=hub_stock_group

## Relations

- analysis/wwi/across/relations/Sales.SpecialDeals.StockGroupID__Warehouse.StockGroups.StockGroupID

## Evidence

- analysis/wwi/across/relations/Sales.SpecialDeals.StockGroupID__Warehouse.StockGroups.StockGroupID/02_meaning.md#C2

---
id: nsdn:rv:sat:stock_item__wwi__price
kind: satellite
name: sat_stock_item__wwi__price
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.3
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_stock_item
source: wwi
source_table: Warehouse.StockItems
parent_key: Warehouse.StockItems.StockItemID
satellite_kind: payload
split_reason: sensitivity (prices)
valid_time: unknown
class: confidential
subject_area: products and deals
---

## Columns

- TaxRate
- UnitPrice
- RecommendedRetailPrice

## Evidence

- analysis/wwi/tables/Warehouse/StockItems/09_derived.md
- analysis/wwi/tables/Warehouse/StockItems/19_sensitivity.md

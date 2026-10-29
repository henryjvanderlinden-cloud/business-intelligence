---
id: nsdn:rv:sat:stock_item__wwi__holding
kind: satellite
name: sat_stock_item__wwi__holding
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.3
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_stock_item
source: wwi
source_table: Warehouse.StockItemHoldings
parent_key: Warehouse.StockItemHoldings.StockItemID
satellite_kind: payload
split_reason: delivery (another table, overwritten daily, sampled)
valid_time: none; sampled
class: confidential
subject_area: products and deals
---

## Columns

- QuantityOnHand
- BinLocation
- LastStocktakeQuantity
- LastCostPrice
- ReorderLevel
- TargetStockLevel

## Evidence

- analysis/wwi/tables/Warehouse/StockItemHoldings/03_temporal.md#C5
- analysis/wwi/tables/Warehouse/StockItemHoldings/03_temporal.md#C6
- analysis/wwi/tables/Warehouse/StockItemHoldings/19_sensitivity.md#C3

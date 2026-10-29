---
id: nsdn:rv:sat:stock_item__wwi
kind: satellite
name: sat_stock_item__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.3
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_stock_item
source: wwi
source_table: Warehouse.StockItems
parent_key: Warehouse.StockItems.StockItemID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: unknown
class: internal
subject_area: products and deals
---

## Columns

- StockItemName
- ColorID
- UnitPackageID
- OuterPackageID | code=ref_package_type__wwi
- Brand
- Size
- LeadTimeDays
- QuantityPerOuter
- IsChillerStock
- Barcode
- TypicalWeightPerUnit
- MarketingComments
- InternalComments
- Photo

## Evidence

- analysis/wwi/tables/Warehouse/StockItems/06_keys.md#C5
- analysis/wwi/tables/Warehouse/StockItems/19_sensitivity.md#C3

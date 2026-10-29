---
id: nsdn:rv:sat:special_deal__wwi
kind: satellite
name: sat_special_deal__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.3
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_special_deal
source: wwi
source_table: Sales.SpecialDeals
parent_key: Sales.SpecialDeals.SpecialDealID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: Sales.SpecialDeals.StartDate
class: confidential
subject_area: products and deals
---

## Columns

- DealDescription
- StartDate
- EndDate
- DiscountAmount
- DiscountPercentage
- UnitPrice
- CustomerID | as_delivered=lnk_special_deal__customer
- BuyingGroupID | as_delivered=lnk_special_deal__buying_group
- CustomerCategoryID | as_delivered=lnk_special_deal__customer_category
- StockItemID | as_delivered=lnk_special_deal__stock_item
- StockGroupID | as_delivered=lnk_special_deal__stock_group

## Evidence

- analysis/wwi/tables/Sales/SpecialDeals/03_temporal.md#C5
- analysis/wwi/tables/Sales/SpecialDeals/19_sensitivity.md

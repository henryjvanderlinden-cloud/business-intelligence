---
id: nsdn:rv:hub:stock_group
kind: hub
name: hub_stock_group
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 10
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: stock group
grain: one stock group
subject_area: products and deals
---

## Business key

- Warehouse.StockGroups.StockGroupID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Warehouse/StockGroups/06_keys.md#C2
- analysis/wwi/tables/Warehouse/StockGroups/06_keys.md#C5
- analysis/wwi/tables/Warehouse/StockItemStockGroups/06_keys.md#C4

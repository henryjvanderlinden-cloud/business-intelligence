---
id: nsdn:rv:hub:stock_item
kind: hub
name: hub_stock_item
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 9
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: stock item
grain: one product
subject_area: products and deals
---

## Business key

- Warehouse.StockItems.StockItemID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Warehouse/StockItems/06_keys.md#C2
- analysis/wwi/tables/Warehouse/StockItems/06_keys.md#C4
- analysis/wwi/tables/Warehouse/StockItems/06_keys.md#C5
- analysis/wwi/tables/Warehouse/StockItems/columns/Barcode/02_meaning.md#C3

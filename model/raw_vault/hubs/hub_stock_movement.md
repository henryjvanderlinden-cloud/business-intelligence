---
id: nsdn:rv:hub:stock_movement
kind: hub
name: hub_stock_movement
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 20
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: stock movement
grain: one issue, receipt or adjustment
subject_area: ledgers
---

## Business key

- Warehouse.StockItemTransactions.StockItemTransactionID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Warehouse/StockItemTransactions/06_keys.md#C1
- analysis/wwi/tables/Warehouse/StockItemTransactions/06_keys.md#C3
- analysis/wwi/across/terms/transaction/25_terms.md#C3

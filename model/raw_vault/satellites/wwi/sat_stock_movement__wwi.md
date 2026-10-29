---
id: nsdn:rv:sat:stock_movement__wwi
kind: satellite
name: sat_stock_movement__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.6
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_stock_movement
source: wwi
source_table: Warehouse.StockItemTransactions
parent_key: Warehouse.StockItemTransactions.StockItemTransactionID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: Warehouse.StockItemTransactions.TransactionOccurredWhen
class: internal
subject_area: ledgers
---

## Columns

- TransactionTypeID | code=ref_transaction_type__wwi
- TransactionOccurredWhen
- Quantity
- CustomerID | as_delivered=lnk_stock_movement__customer
- InvoiceID | as_delivered=lnk_stock_movement__invoice
- SupplierID | as_delivered=lnk_stock_movement__supplier
- PurchaseOrderID | as_delivered=lnk_stock_movement__purchase_order

## Evidence

- analysis/wwi/tables/Warehouse/StockItemTransactions/03_temporal.md#C3
- analysis/wwi/tables/Warehouse/StockItemTransactions/03_temporal.md#C5
- analysis/wwi/tables/Warehouse/StockItemTransactions/09_derived.md

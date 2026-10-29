---
id: nsdn:rv:link:stock_item__supplier
kind: link
name: lnk_stock_item__supplier
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 14
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: stock item usual supplier
from: hub_stock_item
to: hub_supplier
driving: hub_stock_item
optional: no
effectivity: load
subject_area: products and deals
---

## Columns

- Warehouse.StockItems.StockItemID | end=from | effectivity_start=load
- Warehouse.StockItems.SupplierID | end=to

## Relations

- analysis/wwi/across/relations/Warehouse.StockItems.SupplierID__Purchasing.Suppliers.SupplierID

## Evidence

- analysis/wwi/across/relations/Warehouse.StockItems.SupplierID__Purchasing.Suppliers.SupplierID/02_meaning.md#C2

---
id: nsdn:rv:hub:sales_order
kind: hub
name: hub_sales_order
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 12
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: sales order (fulfilment order)
grain: one order as WWI fulfils it: an original or a backorder
subject_area: sales
---

## Business key

- Sales.Orders.OrderID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Sales/Orders/06_keys.md#C1
- analysis/wwi/tables/Sales/Orders/06_keys.md#C2
- analysis/wwi/tables/Sales/Orders/06_keys.md#C4
- analysis/wwi/tables/Sales/Orders/06_keys.md#C7
- analysis/wwi/across/terms/order/25_terms.md#C1

---
id: nsdn:rv:hub:purchase_order_line
kind: hub
name: hub_purchase_order_line
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 17
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: purchase-order line
grain: one line
subject_area: purchasing
---

## Business key

- Purchasing.PurchaseOrderLines.PurchaseOrderLineID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Purchasing/PurchaseOrderLines/01_granularity.md#C1
- analysis/wwi/tables/Purchasing/PurchaseOrderLines/01_granularity.md#C2
- analysis/wwi/tables/Purchasing/PurchaseOrderLines/01_granularity.md#C3

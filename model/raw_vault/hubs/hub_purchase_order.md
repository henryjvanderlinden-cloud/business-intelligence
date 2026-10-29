---
id: nsdn:rv:hub:purchase_order
kind: hub
name: hub_purchase_order
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 16
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: purchase order
grain: one order to a supplier
subject_area: purchasing
---

## Business key

- Purchasing.PurchaseOrders.PurchaseOrderID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Purchasing/PurchaseOrders/06_keys.md#C1
- analysis/wwi/tables/Purchasing/PurchaseOrders/06_keys.md#C3
- analysis/wwi/tables/Purchasing/PurchaseOrders/columns/SupplierReference/02_meaning.md#C4

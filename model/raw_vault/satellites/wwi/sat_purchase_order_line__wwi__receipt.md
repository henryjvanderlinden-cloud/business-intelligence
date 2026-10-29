---
id: nsdn:rv:sat:purchase_order_line__wwi__receipt
kind: satellite
name: sat_purchase_order_line__wwi__receipt
status: accepted
ruled_in: ADR-0033, ADR-0028
defined_in: docs/10_architecture/149_wwi-satellites.md#3.5
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_purchase_order_line
source: wwi
source_table: Purchasing.PurchaseOrderLines
parent_key: Purchasing.PurchaseOrderLines.PurchaseOrderLineID
satellite_kind: milestone
split_reason: milestone (ADR-0028), latest receipt only
valid_time: Purchasing.PurchaseOrderLines.LastReceiptDate
class: internal
subject_area: purchasing
---

## Columns

- ReceivedOuters
- LastReceiptDate

## Evidence

- analysis/wwi/tables/Purchasing/PurchaseOrderLines/03_temporal.md#C5
- analysis/wwi/_source/22_stability.md#C19

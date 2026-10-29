---
id: nsdn:rv:sat:purchase_order_line__wwi
kind: satellite
name: sat_purchase_order_line__wwi
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.5
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_purchase_order_line
source: wwi
source_table: Purchasing.PurchaseOrderLines
parent_key: Purchasing.PurchaseOrderLines.PurchaseOrderLineID
satellite_kind: payload
split_reason: none (main satellite)
valid_time: unknown (no own date; finalisation undated)
class: confidential
subject_area: purchasing
---

## Columns

- OrderedOuters
- Description
- PackageTypeID | code=ref_package_type__wwi
- ExpectedUnitPricePerOuter
- IsOrderLineFinalized

## Evidence

- analysis/wwi/tables/Purchasing/PurchaseOrderLines/03_temporal.md#C2
- analysis/wwi/tables/Purchasing/PurchaseOrderLines/09_derived.md

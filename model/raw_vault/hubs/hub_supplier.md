---
id: nsdn:rv:hub:supplier
kind: hub
name: hub_supplier
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 8
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: supplier
grain: one supplier organisation
subject_area: parties
---

## Business key

- Purchasing.Suppliers.SupplierID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Purchasing/Suppliers/06_keys.md#C1
- analysis/wwi/tables/Purchasing/Suppliers/06_keys.md#C4
- analysis/wwi/tables/Purchasing/Suppliers/06_keys.md#C5
- analysis/wwi/tables/Purchasing/Suppliers/columns/SupplierReference/02_meaning.md#C1

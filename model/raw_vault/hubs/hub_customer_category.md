---
id: nsdn:rv:hub:customer_category
kind: hub
name: hub_customer_category
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 6
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: customer category
grain: one category
subject_area: parties
---

## Business key

- Sales.CustomerCategories.CustomerCategoryID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Sales/CustomerCategories/06_keys.md#C2
- analysis/wwi/tables/Sales/CustomerCategories/06_keys.md#C5
- analysis/wwi/tables/Sales/SpecialDeals/06_keys.md#C2

---
id: nsdn:rv:hub:customer
kind: hub
name: hub_customer
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 5
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: customer
grain: one customer account: head office, branch or individual
subject_area: parties
---

## Business key

- Sales.Customers.CustomerID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Sales/Customers/06_keys.md#C1
- analysis/wwi/tables/Sales/Customers/06_keys.md#C2
- analysis/wwi/tables/Sales/Customers/06_keys.md#C5
- analysis/wwi/tables/Sales/Customers/01_granularity.md
- analysis/wwi/across/entities/customer/26_entities.md#C1

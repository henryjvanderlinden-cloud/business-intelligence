---
id: nsdn:rv:hub:person
kind: hub
name: hub_person
status: accepted
ruled_in: ADR-0029, ADR-0030
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 4
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: person
grain: one person: staff, customer or supplier contact, technical user
subject_area: parties
---

## Business key

- Application.People.PersonID | key_space=wwi | key_kind=record-identifier

## Evidence

- analysis/wwi/tables/Application/People/06_keys.md#C1
- analysis/wwi/tables/Application/People/06_keys.md#C4
- analysis/wwi/tables/Application/People/06_keys.md#C5
- analysis/wwi/tables/Application/People/columns/LogonName/02_meaning.md#C4
- analysis/wwi/across/entities/person/26_entities.md#C1

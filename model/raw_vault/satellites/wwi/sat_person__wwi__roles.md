---
id: nsdn:rv:sat:person__wwi__roles
kind: satellite
name: sat_person__wwi__roles
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.2
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_person
source: wwi
source_table: Application.People
parent_key: Application.People.PersonID
satellite_kind: payload
split_reason: sensitivity (internal, unlike the rest)
valid_time: unknown
class: internal
subject_area: parties
---

## Columns

- IsEmployee
- IsSalesperson
- IsSystemUser

## Evidence

- analysis/wwi/tables/Application/People/07_population.md#C6

---
id: nsdn:rv:sat:person__wwi__account
kind: satellite
name: sat_person__wwi__account
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.2
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_person
source: wwi
source_table: Application.People
parent_key: Application.People.PersonID
satellite_kind: payload
split_reason: sensitivity and rate of change (138 to 182 people changed)
valid_time: unknown
class: restricted
subject_area: parties
---

## Columns

- IsPermittedToLogon
- LogonName
- IsExternalLogonProvider
- HashedPassword | load=never (ADR-0033 decision 2)
- UserPreferences

## Evidence

- analysis/wwi/tables/Application/People/06_keys.md#C5
- analysis/wwi/tables/Application/People/19_sensitivity.md#C3
- analysis/wwi/tables/Application/People/19_sensitivity.md#C5
- analysis/wwi/tables/Application/People/19_sensitivity.md#C6

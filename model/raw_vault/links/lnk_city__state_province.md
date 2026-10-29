---
id: nsdn:rv:link:city__state_province
kind: link
name: lnk_city__state_province
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 1
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: city in state or province
from: hub_city
to: hub_state_province
driving: hub_city
optional: no
effectivity: load
effectivity_start: load
subject_area: geography
---

## Columns

- Application.Cities.StateProvinceID | names=hub_state_province

## Relations

- analysis/wwi/across/relations/Application.Cities.StateProvinceID__Application.StateProvinces.StateProvinceID

## Evidence

- analysis/wwi/across/relations/Application.Cities.StateProvinceID__Application.StateProvinces.StateProvinceID/02_meaning.md#C2
- analysis/wwi/across/relations/Application.Cities.StateProvinceID__Application.StateProvinces.StateProvinceID/07_population.md#C2

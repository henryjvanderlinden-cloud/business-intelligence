---
id: nsdn:rv:link:state_province__country
kind: link
name: lnk_state_province__country
status: accepted
ruled_in: ADR-0031, ADR-0030
defined_in: docs/10_architecture/148_wwi-relationships.md#3 link 2
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
label: state or province in country
from: hub_state_province
to: hub_country
driving: hub_state_province
optional: no
effectivity: load
subject_area: geography
---

## Columns

- Application.StateProvinces.StateProvinceID | end=from | effectivity_start=load
- Application.StateProvinces.CountryID | end=to | resolve=Application.Countries.CountryID to Application.Countries.IsoAlpha3Code, same extract

## Relations

- analysis/wwi/across/relations/Application.StateProvinces.CountryID__Application.Countries.CountryID

## Evidence

- analysis/wwi/across/relations/Application.StateProvinces.CountryID__Application.Countries.CountryID/02_meaning.md#C2
- analysis/wwi/across/relations/Application.StateProvinces.CountryID__Application.Countries.CountryID/07_population.md#C2

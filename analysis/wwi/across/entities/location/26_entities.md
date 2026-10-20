---
id: wwi:entity:location
subject: wwi/across/entities/location
item: 26
topic: entities
tier: best-effort
summary: Cities, state-provinces and countries form one geographic hierarchy; customers, suppliers and WWI itself have a delivery city and a postal city.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: readings by claude-opus-5-5 linking the claims that own each fact; written by prototypes/information_analysis/write_glossary.py (blob ffcc3813a793cc9facce4b98cc396d0f16cffa08)
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: none
last_checked_at: 2026-10-20T05:51:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: a linked claim changes
---

## Claims

- C1 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: City in state-province, state-province in country; all 53 state-provinces are in one country (across/relations/Application.Cities.StateProvinceID__Application.StateProvinces.StateProvinceID/02_meaning.md#C2; across/relations/Application.StateProvinces.CountryID__Application.Countries.CountryID/02_meaning.md#C2).
- C2 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: Customers, suppliers and the system parameters refer to a city twice, as delivery city and postal city: two roles of the same table (across/relations/Sales.Customers.DeliveryCityID__Application.Cities.CityID/27_peculiarities.md#C2).

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.

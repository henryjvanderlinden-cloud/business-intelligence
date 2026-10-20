---
id: wwi:fk:FK_Purchasing_Suppliers_DeliveryCityID_Application_Cities
subject: wwi/across/relations/Purchasing.Suppliers.DeliveryCityID__Application.Cities.CityID
item: 02
topic: meaning
tier: minimum
summary: ID of the delivery city for this address
confidence: low
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 6731121b96b01e540a87f05789e0d036d5bff51807a760c46d45f6643e765b1b
last_checked_at: 2026-10-20T05:51:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of either table
---

## Claims

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=63940b003f3cb635 | recheck=the description changes | text: The source describes Purchasing.Suppliers.DeliveryCityID as "ID of the delivery city for this address".
- C2 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=63940b003f3cb635 | recheck=a description is found | text: By the names: the join answers which row of Application.Cities is the one DeliveryCityID names for each row of Purchasing.Suppliers.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:fk:FK_Application_Cities_Application_People
subject: wwi/across/relations/Application.Cities.LastEditedBy__Application.People.PersonID
item: 02
topic: meaning
tier: minimum
summary: What the join means is read from the names; see the claims.
confidence: low
claims: 1
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: c3ea6dc65bea13fc769d06da287aeb7f7a111d40b8cb9e9e1e43a3e497af55f9
last_checked_at: 2026-10-20T08:31:00Z
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

- C1 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3887251b4d2f7f96 | recheck=a description is found | text: By the column's name: the join gives, for each row of Application.Cities, the person who last changed it; it says nothing of who created the row or of earlier editors (see the column file LastEditedBy/02_meaning.md of Application.Cities).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

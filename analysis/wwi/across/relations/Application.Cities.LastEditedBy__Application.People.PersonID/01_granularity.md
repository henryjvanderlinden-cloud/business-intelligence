---
id: wwi:fk:FK_Application_Cities_Application_People
subject: wwi/across/relations/Application.Cities.LastEditedBy__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Application.Cities to Application.People; up to 37,912 rows of Application.Cities per row of Application.People.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: c3ea6dc65bea13fc769d06da287aeb7f7a111d40b8cb9e9e1e43a3e497af55f9
last_checked_at: 2026-10-19T20:31:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3887251b4d2f7f96 | recheck=the foreign key changes | text: Declared foreign key FK_Application_Cities_Application_People from Application.Cities.LastEditedBy to Application.People.PersonID, the primary key of Application.People: each row of Application.Cities names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3887251b4d2f7f96 | recheck=every new extract | text: In this extract 37,940 of 37,940 rows of Application.Cities name one of 4 referenced rows of Application.People (of 1,111); children per referenced parent: from 5 to 37,912, median 11.5; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3887251b4d2f7f96 | recheck=every new extract | text: Joined from Application.Cities to Application.People, the result keeps the grain of Application.Cities: one row per row of Application.Cities. Joined the other way, each row of Application.People repeats once per row of Application.Cities that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

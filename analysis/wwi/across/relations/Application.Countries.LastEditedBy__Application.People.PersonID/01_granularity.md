---
id: wwi:fk:FK_Application_Countries_Application_People
subject: wwi/across/relations/Application.Countries.LastEditedBy__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Application.Countries to Application.People; up to 155 rows of Application.Countries per row of Application.People.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 33a2398e9a7d6eed93e259f4f3f66a8ab6afb54d94f3a970c181e5b9f417f136
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7cc2d80b58dfab00 | recheck=the foreign key changes | text: Declared foreign key FK_Application_Countries_Application_People from Application.Countries.LastEditedBy to Application.People.PersonID, the primary key of Application.People: each row of Application.Countries names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7cc2d80b58dfab00 | recheck=every new extract | text: In this extract 190 of 190 rows of Application.Countries name one of 4 referenced rows of Application.People (of 1,111); children per referenced parent: from 7 to 155, median 14; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7cc2d80b58dfab00 | recheck=every new extract | text: Joined from Application.Countries to Application.People, the result keeps the grain of Application.Countries: one row per row of Application.Countries. Joined the other way, each row of Application.People repeats once per row of Application.Countries that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

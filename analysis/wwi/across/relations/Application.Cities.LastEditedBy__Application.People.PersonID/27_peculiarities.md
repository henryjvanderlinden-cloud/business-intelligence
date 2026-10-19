---
id: wwi:fk:FK_Application_Cities_Application_People
subject: wwi/across/relations/Application.Cities.LastEditedBy__Application.People.PersonID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out.
confidence: low
claims: 2
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3887251b4d2f7f96 | recheck=every new extract | text: Fan-out: joined from Application.People to Application.Cities, a Application.People row repeats up to 37,912 times (median 11.5), so a measure of Application.People summed after the join is counted once per referring row.
- C2 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3887251b4d2f7f96 | recheck=a description is found | text: The relation records only the last edit; it cannot attribute a row's creation or earlier changes.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

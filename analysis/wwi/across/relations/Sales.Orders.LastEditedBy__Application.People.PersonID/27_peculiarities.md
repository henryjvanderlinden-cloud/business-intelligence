---
id: wwi:fk:FK_Sales_Orders_Application_People
subject: wwi/across/relations/Sales.Orders.LastEditedBy__Application.People.PersonID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, roles.
confidence: low
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 51805da5178a316233382b96b4193aac7558e4460d848a9ce9951eeae31a4a1e
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=989410f9c4d3f2a6 | recheck=every new extract | text: Fan-out: joined from Application.People to Sales.Orders, a Application.People row repeats up to 4,648 times (median 3,702.5), so a measure of Application.People summed after the join is counted once per referring row.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=989410f9c4d3f2a6 | recheck=a foreign key changes | text: Several paths between the same two tables: Sales.Orders also refers to Application.People through ContactPersonID, PickedByPersonID, SalespersonPersonID; a join of the two must say which role it means.
- C3 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=989410f9c4d3f2a6 | recheck=a description is found | text: The relation records only the last edit; it cannot attribute a row's creation or earlier changes.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

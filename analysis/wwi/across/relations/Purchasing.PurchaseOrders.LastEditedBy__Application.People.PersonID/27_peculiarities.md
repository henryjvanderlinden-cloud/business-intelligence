---
id: wwi:fk:FK_Purchasing_PurchaseOrders_Application_People
subject: wwi/across/relations/Purchasing.PurchaseOrders.LastEditedBy__Application.People.PersonID
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
input_schema_sha256: c56c9774597cf383e745c673a7fbb1a155c5f737cd06902ed049ec3e0a6851f7
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3e56be67625d506b | recheck=every new extract | text: Fan-out: joined from Application.People to Purchasing.PurchaseOrders, a Application.People row repeats up to 141 times (median 108.5), so a measure of Application.People summed after the join is counted once per referring row.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3e56be67625d506b | recheck=a foreign key changes | text: Several paths between the same two tables: Purchasing.PurchaseOrders also refers to Application.People through ContactPersonID; a join of the two must say which role it means.
- C3 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3e56be67625d506b | recheck=a description is found | text: The relation records only the last edit; it cannot attribute a row's creation or earlier changes.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

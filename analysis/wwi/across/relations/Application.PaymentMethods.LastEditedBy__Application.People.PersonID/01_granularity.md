---
id: wwi:fk:FK_Application_PaymentMethods_Application_People
subject: wwi/across/relations/Application.PaymentMethods.LastEditedBy__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Application.PaymentMethods to Application.People; up to 3 rows of Application.PaymentMethods per row of Application.People.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 93b56da7e7a81f419616caf09fe54a7c415b7e216e3ffeb115653ff7786d48a4
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=c51ef2efe164b0f3 | recheck=the foreign key changes | text: Declared foreign key FK_Application_PaymentMethods_Application_People from Application.PaymentMethods.LastEditedBy to Application.People.PersonID, the primary key of Application.People: each row of Application.PaymentMethods names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=c51ef2efe164b0f3 | recheck=every new extract | text: In this extract 4 of 4 rows of Application.PaymentMethods name one of 2 referenced rows of Application.People (of 1,111); children per referenced parent: from 1 to 3, median 2; 1 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=c51ef2efe164b0f3 | recheck=every new extract | text: Joined from Application.PaymentMethods to Application.People, the result keeps the grain of Application.PaymentMethods: one row per row of Application.PaymentMethods. Joined the other way, each row of Application.People repeats once per row of Application.PaymentMethods that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

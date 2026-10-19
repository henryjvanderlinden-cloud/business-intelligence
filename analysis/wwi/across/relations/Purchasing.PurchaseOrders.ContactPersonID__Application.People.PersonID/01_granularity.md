---
id: wwi:fk:FK_Purchasing_PurchaseOrders_ContactPersonID_Application_People
subject: wwi/across/relations/Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.PurchaseOrders to Application.People; up to 2,076 rows of Purchasing.PurchaseOrders per row of Application.People.
confidence: high
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=7a9ef25ccf258c66 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_PurchaseOrders_ContactPersonID_Application_People from Purchasing.PurchaseOrders.ContactPersonID to Application.People.PersonID, the primary key of Application.People: each row of Purchasing.PurchaseOrders names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=7a9ef25ccf258c66 | recheck=every new extract | text: In this extract 2,076 of 2,076 rows of Purchasing.PurchaseOrders name one of 1 referenced rows of Application.People (of 1,111); children per referenced parent: from 2,076 to 2,076, median 2,076; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=7a9ef25ccf258c66 | recheck=every new extract | text: Joined from Purchasing.PurchaseOrders to Application.People, the result keeps the grain of Purchasing.PurchaseOrders: one row per row of Purchasing.PurchaseOrders. Joined the other way, each row of Application.People repeats once per row of Purchasing.PurchaseOrders that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

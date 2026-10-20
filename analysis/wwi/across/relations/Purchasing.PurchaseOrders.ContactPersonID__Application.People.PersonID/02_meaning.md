---
id: wwi:fk:FK_Purchasing_PurchaseOrders_ContactPersonID_Application_People
subject: wwi/across/relations/Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID
item: 02
topic: meaning
tier: minimum
summary: Described as the order's primary contact; in fact a WWI employee and salesperson on every order, never the supplier's contact; the role it records is not established.
confidence: unknown
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: c56c9774597cf383e745c673a7fbb1a155c5f737cd06902ed049ec3e0a6851f7
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7a9ef25ccf258c66 | recheck=the description changes | text: The source describes Purchasing.PurchaseOrders.ContactPersonID as "The person who is the primary contact for this purchase order".
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7a9ef25ccf258c66 | recheck=every new extract | text: The people named: 2,076 of 2,076 rows name an employee of WWI (IsEmployee = 1), 2,076 a salesperson, 0 a person who is not an employee.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7a9ef25ccf258c66 | recheck=every new extract | text: Not a contact at the supplier in this extract: on all 2,076 orders it names an employee who is a salesperson (the people-named claim), and never the supplier's primary or alternate contact (27).
- C4 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a process description or the generating script settles it | text: What role the person plays for the order - buyer, approver, or a default - is not established.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

The role of the person named; one person is named on every order (Purchasing.PurchaseOrders 07).

## For a person

None.

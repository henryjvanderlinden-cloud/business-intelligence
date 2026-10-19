---
id: wwi:fk:FK_Sales_Customers_PrimaryContactPersonID_Application_People
subject: wwi/across/relations/Sales.Customers.PrimaryContactPersonID__Application.People.PersonID
item: 02
topic: meaning
tier: minimum
summary: Primary contact
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: beb4a67d9dbf8afd5b69421099df2d5f90e9db6ba0e71faac346f5906ff90ecc
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=f987fc172b77fd7a | recheck=the description changes | text: The source describes Sales.Customers.PrimaryContactPersonID as "Primary contact".
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=f987fc172b77fd7a | recheck=every new extract | text: The people named: 0 of 663 rows name an employee of WWI (IsEmployee = 1), 0 a salesperson, 663 a person who is not an employee.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=f987fc172b77fd7a | recheck=every new extract, or a description changes | text: The customer's primary contact person, one per customer; the contact on the customer's orders and invoices (their 27).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

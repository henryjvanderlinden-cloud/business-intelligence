---
id: wwi:fk:FK_Sales_Orders_SalespersonPersonID_Application_People
subject: wwi/across/relations/Sales.Orders.SalespersonPersonID__Application.People.PersonID
item: 02
topic: meaning
tier: minimum
summary: Salesperson for this order
confidence: medium
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=16e05537c5a37af4 | recheck=the description changes | text: The source describes Sales.Orders.SalespersonPersonID as "Salesperson for this order".
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=16e05537c5a37af4 | recheck=every new extract | text: The people named: 73,653 of 73,653 rows name an employee of WWI (IsEmployee = 1), 73,653 a salesperson, 0 a person who is not an employee.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=16e05537c5a37af4 | recheck=every new extract, or a description changes | text: The salesperson for the order.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

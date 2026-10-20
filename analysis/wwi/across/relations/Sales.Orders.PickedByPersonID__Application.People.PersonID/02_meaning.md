---
id: wwi:fk:FK_Sales_Orders_PickedByPersonID_Application_People
subject: wwi/across/relations/Sales.Orders.PickedByPersonID__Application.People.PersonID
item: 02
topic: meaning
tier: minimum
summary: Person who picked this shipment
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 51805da5178a316233382b96b4193aac7558e4460d848a9ce9951eeae31a4a1e
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f35899fc41d8d217 | recheck=the description changes | text: The source describes Sales.Orders.PickedByPersonID as "Person who picked this shipment".
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f35899fc41d8d217 | recheck=every new extract | text: The people named: 63,020 of 63,020 rows name an employee of WWI (IsEmployee = 1), 32,169 a salesperson, 0 a person who is not an employee.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f35899fc41d8d217,af410313550bceb2,c6e5d1bc0af05898 | recheck=every new extract, or a description changes | text: The staff member who picked the order. It is empty on 10,633 orders: as many as the 3,087 orders with no PickingCompletedWhen plus the 7,546 originals split into backorders, which were picked without a picker; the sum matches, the rows are not checked one by one.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:object:1154103152
subject: wwi/tables/Sales/Orders
item: 05
topic: role
tier: minimum
summary: Transaction header for the event "customer order raised", carrying one milestone (picking completed) filled in later; its lines are Sales.OrderLines.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-18T20:30:00Z
step: S08-061
method: reading of evidence written by prototypes/information_analysis/evidence_orders.py (blob 5b39164821d92e89109688e68c204752d9edeff5) and of catalogue queries through the sandbox request folder
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: df493a1a20d890a2e0931a1a6e6ddd9510bec9c2a6d09162f4d0a907b0bebca6
last_checked_at: 2026-10-18T20:30:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: analysis layout 1 of c7b7aa2 (moved out of the repository)
superseded_by: none
recheck_when: a schema change of Sales.Orders
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=597ef697da37cd0e,6b9b2e34cfa5d3e1 | recheck=a foreign key or the temporal type changes | text: A transaction header referring to master data: six declared, enabled and trusted foreign keys to Sales.Customers, Application.People and itself; not a history table.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=339f4ab018dfda14 | recheck=a second kind of update appears | text: It also carries state: the picking milestone is set in place after the order is raised; one row collects the milestones of an order over time.

## Reasoning

Declared foreign keys, the header-line pattern of 01_granularity.md#C2 and the update pattern agree.

## Uncertainties

None about the role.

## For a person

None.

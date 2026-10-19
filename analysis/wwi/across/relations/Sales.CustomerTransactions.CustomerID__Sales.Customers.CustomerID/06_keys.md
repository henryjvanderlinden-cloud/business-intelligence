---
id: wwi:fk:FK_Sales_CustomerTransactions_CustomerID_Sales_Customers
subject: wwi/across/relations/Sales.CustomerTransactions.CustomerID__Sales.Customers.CustomerID
item: 06
topic: keys
tier: minimum
summary: Sales.CustomerTransactions.CustomerID refers to the primary key Sales.Customers.CustomerID, enforced.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: dba303311da3e1c6d0f8dd3ca4dc6c701c7bbcbc7c941309c872bb30aa2359c5
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=4dd2845ea6a5f4f9 | recheck=the foreign key changes | text: Child side: Sales.CustomerTransactions.CustomerID, int, not nullable; a foreign key, enabled and trusted; on delete no action.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=4dd2845ea6a5f4f9 | recheck=the primary key changes | text: Parent side: Sales.Customers.CustomerID, the declared primary key of Sales.Customers.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=4dd2845ea6a5f4f9 | recheck=every new extract | text: No other column of Sales.Customers that is unique in this extract holds all values of CustomerID: the primary key is the only key the values fit.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

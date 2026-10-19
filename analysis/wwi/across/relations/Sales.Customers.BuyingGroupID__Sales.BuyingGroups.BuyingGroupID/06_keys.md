---
id: wwi:fk:FK_Sales_Customers_BuyingGroupID_Sales_BuyingGroups
subject: wwi/across/relations/Sales.Customers.BuyingGroupID__Sales.BuyingGroups.BuyingGroupID
item: 06
topic: keys
tier: minimum
summary: Sales.Customers.BuyingGroupID refers to the primary key Sales.BuyingGroups.BuyingGroupID, enforced.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 40a894a1eed1f9f7c2412da918168035be054343ffd71bf2cce4a670ff720f30
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=6b074e88d3798b05 | recheck=the foreign key changes | text: Child side: Sales.Customers.BuyingGroupID, int, nullable; a foreign key, enabled and trusted; on delete no action.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=6b074e88d3798b05 | recheck=the primary key changes | text: Parent side: Sales.BuyingGroups.BuyingGroupID, the declared primary key of Sales.BuyingGroups.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=6b074e88d3798b05 | recheck=every new extract | text: No other column of Sales.BuyingGroups that is unique in this extract holds all values of BuyingGroupID: the primary key is the only key the values fit.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

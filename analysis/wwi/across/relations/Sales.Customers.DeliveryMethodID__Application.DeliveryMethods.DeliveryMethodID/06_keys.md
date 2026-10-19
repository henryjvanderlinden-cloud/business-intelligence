---
id: wwi:fk:FK_Sales_Customers_DeliveryMethodID_Application_DeliveryMethods
subject: wwi/across/relations/Sales.Customers.DeliveryMethodID__Application.DeliveryMethods.DeliveryMethodID
item: 06
topic: keys
tier: minimum
summary: Sales.Customers.DeliveryMethodID refers to the primary key Application.DeliveryMethods.DeliveryMethodID, enforced.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 53292ed2d24b8a2b01c2edba3c93793b0f57a751260b0fe45c641df232692f49
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=49eabecb8c2d044c | recheck=the foreign key changes | text: Child side: Sales.Customers.DeliveryMethodID, int, not nullable; a foreign key, enabled and trusted; on delete no action.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=49eabecb8c2d044c | recheck=the primary key changes | text: Parent side: Application.DeliveryMethods.DeliveryMethodID, the declared primary key of Application.DeliveryMethods.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=49eabecb8c2d044c | recheck=every new extract | text: No other column of Application.DeliveryMethods that is unique in this extract holds all values of DeliveryMethodID: the primary key is the only key the values fit.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

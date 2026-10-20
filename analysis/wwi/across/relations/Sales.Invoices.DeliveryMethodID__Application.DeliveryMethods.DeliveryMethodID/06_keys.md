---
id: wwi:fk:FK_Sales_Invoices_DeliveryMethodID_Application_DeliveryMethods
subject: wwi/across/relations/Sales.Invoices.DeliveryMethodID__Application.DeliveryMethods.DeliveryMethodID
item: 06
topic: keys
tier: minimum
summary: Sales.Invoices.DeliveryMethodID refers to the primary key Application.DeliveryMethods.DeliveryMethodID, enforced.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2799a4e040de3e031ea0c4c2cec4dc92926a83019371d8f7fbb5a840647c2fae
last_checked_at: 2026-10-20T08:31:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f85aff68471e48d6 | recheck=the foreign key changes | text: Child side: Sales.Invoices.DeliveryMethodID, int, not nullable; a foreign key, enabled and trusted; on delete no action.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f85aff68471e48d6 | recheck=the primary key changes | text: Parent side: Application.DeliveryMethods.DeliveryMethodID, the declared primary key of Application.DeliveryMethods.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f85aff68471e48d6 | recheck=every new extract | text: No other column of Application.DeliveryMethods that is unique in this extract holds all values of DeliveryMethodID: the primary key is the only key the values fit.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

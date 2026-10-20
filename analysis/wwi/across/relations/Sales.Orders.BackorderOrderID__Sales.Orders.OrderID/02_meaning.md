---
id: wwi:fk:FK_Sales_Orders_BackorderOrderID_Sales_Orders
subject: wwi/across/relations/Sales.Orders.BackorderOrderID__Sales.Orders.OrderID
item: 02
topic: meaning
tier: minimum
summary: From an original order to the backorder split from it - the reverse of the declared description.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 4612536ddbfeaca86b725859e57bc3ca8e5ff41a12fbf23fa9e1e0bf48953fa7
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=57cb08c856e3e89c | recheck=the description changes | text: The source describes Sales.Orders.BackorderOrderID as "If this order is a backorder, this column holds the original order number".
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=c6e5d1bc0af05898 | recheck=every new extract | text: On all 7,546 filled rows the order named has a higher OrderID, an order date on or after the row's own, the same customer and the same customer purchase-order number, and the row's own order was picked without a picker (round 1, Sales/Orders/columns/BackorderOrderID/02_meaning.md#C2).
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=c6e5d1bc0af05898 | recheck=every new extract, or a description changes | text: So in this extract the relation points from the original order to the backorder split from it; the declared description (C1) says the reverse. A generalisation from one extract, against the declaration.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:object:1154103152:column:6
subject: wwi/tables/Sales/Orders/columns/BackorderOrderID
item: 02
topic: meaning
tier: best-effort
summary: Set on the original order and holds the OrderID of the backorder split from it; the declared description says the reverse.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-18T12:40:00Z
step: S08-042
method: reading of evidence written by prototypes/information_analysis/evidence_orders.py (blob 5b39164821d92e89109688e68c204752d9edeff5) and of catalogue queries through the sandbox request folder
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: df493a1a20d890a2e0931a1a6e6ddd9510bec9c2a6d09162f4d0a907b0bebca6
last_checked_at: 2026-10-19T07:30:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: analysis layout 1 of c7b7aa2 (moved out of the repository)
superseded_by: none
recheck_when: the description changes, or a new backorder is created
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b6da684f0b7581f7 | recheck=the description changes | text: The source describes the column as: "If this order is a backorder, this column holds the original order number".
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c6e5d1bc0af05898 | recheck=a filled row breaks one of the five conditions | text: The data says the reverse: on all 7,546 filled rows the referenced order has a higher OrderID, an order date on or after the row's own, the same customer and the same purchase order number, and the row's own order was picked without a picker - the pattern of an order partly fulfilled whose remainder became a new order. The column points from the original to its backorder.
- C3 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=0f9e0d3eb9dd8048 | recheck=Microsoft's description changes | text: Microsoft's description of the business agrees with the data's direction: some customers who order five items of which four are in stock "want to receive the four items and backorder the remaining item", which is "sent later in a separate shipment" - the backorder comes after the original.

## Reasoning

C1 and C2 are both kept: the contradiction is the finding. C3 adds the published description of the business, which describes the backorder as the later shipment and so agrees with C2; it says nothing about the column itself. Anyone building on the description would join the wrong way round.

## Uncertainties

The procedure that created backorders is not in the daily simulation, so the observed meaning cannot be checked against its code; nsdn_reader cannot read procedure definitions in the database.

## For a person

None: the data settles the direction. A person may want the description corrected in the context layer.

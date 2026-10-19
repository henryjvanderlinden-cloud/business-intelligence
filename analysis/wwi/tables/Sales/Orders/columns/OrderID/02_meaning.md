---
id: wwi:object:1154103152:column:1
subject: wwi/tables/Sales/Orders/columns/OrderID
item: 02
topic: meaning
tier: best-effort
summary: Numeric ID used for reference to an order within the database
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: df493a1a20d890a2e0931a1a6e6ddd9510bec9c2a6d09162f4d0a907b0bebca6
last_checked_at: 2026-10-19T07:28:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: the description changes, or every new extract
---

## Claims

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f61ebb431b7b9012 | recheck=the description changes | text: The source describes it as "Numeric ID used for reference to an order within the database" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f61ebb431b7b9012 | recheck=a column type changes | text: Declared as int, not nullable.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f61ebb431b7b9012 | recheck=a key changes | text: Part of the primary key PK_Sales_Orders; referred to by Sales.Invoices.OrderID, Sales.OrderLines.OrderID, Sales.Orders.BackorderOrderID.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=af410313550bceb2 | recheck=every new extract | text: Observed: filled on 73,653 of 73,653 rows; 73,653 distinct values; from 1 to 73,653.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.

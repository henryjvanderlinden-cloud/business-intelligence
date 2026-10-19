---
id: wwi:object:802101898:column:5
subject: wwi/tables/Sales/Customers/columns/BuyingGroupID
item: 02
topic: meaning
tier: best-effort
summary: The buying group the customer belongs to, if any: Tailspin Toys (201), Wingtip Toys (201), none (261).
confidence: medium
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f54b9d7dd163d0d1e3ce34f4adf4d1a76e8caeebe545ad0831277bb0e5b89fb6
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=the description changes | text: The source describes it as "Customer's buying group (optional)" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=a column type changes | text: Declared as int, nullable.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=a foreign key changes | text: Refers to Sales.BuyingGroups.BuyingGroupID (FK_Sales_Customers_BuyingGroupID_Sales_BuyingGroups, enabled and trusted).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=every new extract | text: Observed: filled on 402 of 663 rows; 2 distinct values; from 1 to 2; values empty (261), 1 (201), 2 (201).
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13,09d66348f676d4b5 | recheck=the description changes, or every new extract | text: The two buying groups used are Tailspin Toys and Wingtip Toys, 201 customers each, in Sales.BuyingGroups.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.

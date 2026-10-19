---
id: wwi:object:194099732:column:1
subject: wwi/tables/Warehouse/StockGroups/columns/StockGroupID
item: 02
topic: meaning
tier: best-effort
summary: Numeric ID used for reference to a stock group within the database
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: e95d0e414e870e18e624d3a1e63d4219e1116a6fc359fd638fb4ba9a22247f02
last_checked_at: 2026-10-19T09:21:00Z
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=38f00eb780b1f6ea | recheck=the description changes | text: The source describes it as "Numeric ID used for reference to a stock group within the database" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=38f00eb780b1f6ea | recheck=a column type changes | text: Declared as int, not nullable.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=38f00eb780b1f6ea | recheck=a key changes | text: Part of the primary key PK_Warehouse_StockGroups; referred to by Sales.SpecialDeals.StockGroupID, Warehouse.StockItemStockGroups.StockGroupID.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f17e21d7a1059397 | recheck=every new extract | text: Observed: filled on 10 of 10 rows; 10 distinct values; from 1 to 10.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.

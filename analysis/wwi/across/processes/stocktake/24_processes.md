---
id: wwi:process:stocktake
subject: wwi/across/processes/stocktake
item: 24
topic: processes
tier: best-effort
summary: Stocktakes fall on the last day of January, April, July and October - the quarter ends of a financial year starting 1 November.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-20T05:50:00Z
step: S08-092
method: counts by prototypes/information_analysis/processes.py (blob e3fc85d3ce7b1ef3ef3c73adff0cb80ee7681f8e); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 1cb41c9584d39083447719e6978f6e0cd2927f0fd3f48e26c0af0bb55651e19a
last_checked_at: 2026-10-20T05:50:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of the tables followed
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7f3415e8ec5c2a66 | recheck=every new extract | text: 44 stock adjustments at stocktake (type 12) on 41 items, on these dates (adjustments / distinct items): 2013-01-31 (1/1), 2013-04-30 (1/1), 2013-07-31 (2/2), 2013-10-31 (3/3), 2014-01-31 (4/4), 2014-04-30 (4/4), 2014-07-31 (5/5), 2014-10-31 (4/3), 2015-01-31 (4/4), 2015-04-30 (5/5), 2015-07-31 (1/1), 2015-10-31 (4/4), 2016-01-31 (1/1), 2016-04-30 (5/5).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7f3415e8ec5c2a66 | recheck=every new extract | text: Adjustment signs: negative 21, positive 19, zero 4.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7f3415e8ec5c2a66 | recheck=every new extract | text: LastStocktakeQuantity is filled on 227 of 227 holdings.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7f3415e8ec5c2a66 | recheck=every new extract | text: Every stocktake adjustment falls on the last day of January, April, July or October. With a financial year that starts on 1 November (analysis/wwi/_source/18_documentation.md#C2) these are the ends of the financial quarters: the stocktake is quarterly, at quarter end.
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7f3415e8ec5c2a66 | recheck=every new extract | text: Only a few items get an adjustment at each stocktake (1 to 5 distinct items per date), 4 adjustments have quantity zero, and LastStocktakeQuantity is filled for every holding but equals QuantityOnHand on only 2 (across/reconciliations/stock-holdings-vs-movements).
- C6 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a process description, the generating script or a second extract settles it | text: Whether every item is counted at each stocktake, and why some counts leave a movement of zero while others leave none, is not established.

## Reasoning

The stock adjustments (TransactionTypeID 12) are grouped by date; the holdings' stocktake column is counted.

## Uncertainties

Which items are counted; how LastStocktakeQuantity relates to the adjustments.

## For a person

None.

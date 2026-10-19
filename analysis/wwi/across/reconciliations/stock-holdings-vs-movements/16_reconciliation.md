---
id: wwi:reconciliation:stock-holdings-vs-movements
subject: wwi/across/reconciliations/stock-holdings-vs-movements
item: 16
topic: reconciliation
tier: best-effort
summary: QuantityOnHand cannot be derived from the stock movements: neither its level nor its change over one day matches them for any item.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-19T21:25:00Z
step: S08-085
method: counts by prototypes/information_analysis/reconcile.py (blob 09e7143e7fb2f20127e019cb64133674e1b89c41); readings by claude-opus-5-5 from those counts
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 1cb41c9584d39083447719e6978f6e0cd2927f0fd3f48e26c0af0bb55651e19a
last_checked_at: 2026-10-19T21:25:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of the tables compared
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ee9d0465afa52ea1 | recheck=every new extract | text: QuantityOnHand of none of the 227 items equals the sum of all its stock movements (greater on 218, less on 9).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ee9d0465afa52ea1 | recheck=every new extract | text: Between the extracts of 31 May and 1 June 2016, 176 movements were added (type 10: 167, type 11: 9), 0 earlier movements changed quantity and 0 were deleted; QuantityOnHand changed by a different amount than those movements on all 227 items (more on 218, less on 9); it rose on 211 items, fell on 15, was unchanged on 1.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ee9d0465afa52ea1 | recheck=every new extract | text: No item has a negative QuantityOnHand; LastStocktakeQuantity equals QuantityOnHand on 2 items.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ee9d0465afa52ea1 | recheck=every new extract | text: So in this extract a stock level cannot be derived from the movements, nor the change in QuantityOnHand between the two extracts from the movements added, changed or deleted between them: QuantityOnHand rose on 211 of 227 items while 9 receipts were added.
- C5 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=none | recheck=the daily simulation's procedures or a second transition settles it | text: Why the holdings and the movements disagree - stock added without a movement, movements missing from the extract, or a movement history that does not start from zero - is not established.

## Reasoning

Two tests: the level against the sum of all movements in the extract, and the change in QuantityOnHand between the extracts of 31 May and 1 June 2016 against the movements added between them.

## Uncertainties

The cause of the unexplained additions; whether the movement history starts from a stock of zero.

## For a person

None.

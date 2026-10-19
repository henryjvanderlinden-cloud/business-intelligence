---
id: wwi:object:94623380
subject: wwi/tables/Sales/OrderLines
item: 01
topic: granularity
tier: minimum
summary: One row per stock item on an order; (OrderID, StockItemID) is unique though not declared.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: c00930db9c641c1b31801c17473429ceaa1b6c45519761d89148dd23ed44a1e7
last_checked_at: 2026-10-19T09:21:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=10ba08f87c0c050b | recheck=the primary key changes | text: The declared primary key is OrderLineID (PK_Sales_OrderLines).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453 | recheck=the key stops being unique | text: The key is unique over all 231,581 rows, with no empty values.
- C3 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=babbcde9911fc351 | recheck=a duplicate (order, item) appears | text: OrderID and StockItemID together are unique over all 231,581 lines of this extract; not declared.
- C4 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=10ba08f87c0c050b | recheck=every new extract, or a schema change | text: Grain: one row per stock item ordered.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

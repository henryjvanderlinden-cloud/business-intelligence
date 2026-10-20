---
id: wwi:object:1554104577
subject: wwi/tables/Purchasing/PurchaseOrderLines
item: 01
topic: granularity
tier: minimum
summary: One row per stock item on a purchase order; (PurchaseOrderID, StockItemID) is unique though not declared; quantities in outer packages.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ff3afe91393905debcfd3922ce15e0214e6da79b9a15f2e41e4abf504040d77e
last_checked_at: 2026-10-20T05:44:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=9e1f3e773862db95 | recheck=the primary key changes | text: The declared primary key is PurchaseOrderLineID (PK_Purchasing_PurchaseOrderLines).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=the key stops being unique | text: The key is unique over all 8,376 rows, with no empty values.
- C3 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a2e0c315ed6cbd6f | recheck=a duplicate (order, item) appears | text: PurchaseOrderID and StockItemID together are unique over all 8,376 lines of this extract: one line per item per order here, not declared.
- C4 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=9e1f3e773862db95 | recheck=every new extract, or a schema change | text: Grain: one row per stock item ordered on a purchase order.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

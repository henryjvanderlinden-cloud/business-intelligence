---
id: wwi:object:1554104577:column:10
subject: wwi/tables/Purchasing/PurchaseOrderLines/columns/IsOrderLineFinalized
item: 02
topic: meaning
tier: best-effort
summary: Whether the line is finalized; the description warns that received quantities and weights are often not precise, so finalization is a decision, not an equality of ordered and received.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ff3afe91393905debcfd3922ce15e0214e6da79b9a15f2e41e4abf504040d77e
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=9e1f3e773862db95 | recheck=the description changes | text: The source describes it as "Is this purchase order line now considered finalized? (Receipted quantities and weights are often not precise)" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=9e1f3e773862db95 | recheck=a column type changes | text: Declared as bit, not nullable.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=every new extract | text: Observed: filled on 8,376 of 8,376 rows; 2 distinct values; from 0 to 1; values 1 (8,367), 0 (9).
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=9e1f3e773862db95,cd3cf333fabc9060 | recheck=the description changes, or every new extract | text: A line can be finalized with ReceivedOuters different from OrderedOuters; whether it happens here is not measured.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.

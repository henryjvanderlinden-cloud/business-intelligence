---
id: wwi:object:2018106230:column:5
subject: wwi/tables/Sales/Invoices/columns/DeliveryMethodID
item: 02
topic: meaning
tier: best-effort
summary: How the goods are delivered; 3 (Delivery Van) on every invoice.
confidence: medium
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: d89a1e72bf72f1577926929cb7c514b71af6cf08eb13a8181f4f8688da7f99ce
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=the description changes | text: The source describes it as "How these stock items are beign delivered" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a column type changes | text: Declared as int, not nullable.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a foreign key changes | text: Refers to Application.DeliveryMethods.DeliveryMethodID (FK_Sales_Invoices_DeliveryMethodID_Application_DeliveryMethods, enabled and trusted).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=every new extract | text: Observed: filled on 70,566 of 70,566 rows; 1 distinct value; from 3 to 3; the same value in every row: 3.
- C5 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0f9e0d3eb9dd8048 | recheck=Microsoft's description changes | text: Microsoft: "WWI delivers stock items to customers either via their own delivery vans or via other couriers or freight methods."
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a,7205fae275ae3694 | recheck=the description changes, or every new extract | text: Code 3 is Delivery Van in Application.DeliveryMethods; no other method is used on invoices.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:object:1669580986:column:1
subject: wwi/tables/Application/PaymentMethods/columns/PaymentMethodID
item: 02
topic: meaning
tier: best-effort
summary: Numeric ID used for reference to a payment type within the database
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 6ad07d5080cc67c9c57b9cf621509187e6f222d2624c74328488725ed956287d
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=065bbf4844346cbb | recheck=the description changes | text: The source describes it as "Numeric ID used for reference to a payment type within the database" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=065bbf4844346cbb | recheck=a column type changes | text: Declared as int, not nullable.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=065bbf4844346cbb | recheck=a key changes | text: Part of the primary key PK_Application_PaymentMethods; referred to by Purchasing.SupplierTransactions.PaymentMethodID, Sales.CustomerTransactions.PaymentMethodID.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=d7ebcd1cb8412d2d | recheck=every new extract | text: Observed: filled on 4 of 4 rows; 4 distinct values; from 1 to 4; values 1 (1), 2 (1), 3 (1), 4 (1).

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.

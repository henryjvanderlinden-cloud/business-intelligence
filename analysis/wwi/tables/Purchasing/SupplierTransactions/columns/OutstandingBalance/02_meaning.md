---
id: wwi:object:1682105033:column:11
subject: wwi/tables/Purchasing/SupplierTransactions/columns/OutstandingBalance
item: 02
topic: meaning
tier: best-effort
summary: What is still owed on the transaction: a state, set to 0 when matched; non-zero on 4 rows.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 10c8ac5e8c6792404fbdf9e86336cc8afb432c3106485f0c111b343ad363d85c
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=8516b26c8ecea17f | recheck=the description changes | text: The source describes it as "Amount still outstanding for this transaction" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=8516b26c8ecea17f | recheck=a column type changes | text: Declared as decimal(18,2), not nullable.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=every new extract | text: Observed: filled on 2,440 of 2,440 rows; 5 distinct values; from 0 to 1875081.9; values 0.00 (2,436), 1871894.10 (1), 849784.11 (1), 1875081.90 (1), 852596.89 (1).
- C4 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=8516b26c8ecea17f,be40a492ac908708 | recheck=the description changes, or every new extract | text: A balance carried on an event row (27_peculiarities.md, test 2).

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.

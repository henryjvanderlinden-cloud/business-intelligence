---
id: wwi:object:1765581328:column:2
subject: wwi/tables/Application/TransactionTypes/columns/TransactionTypeName
item: 02
topic: meaning
tier: best-effort
summary: The name of a transaction type: 13 types for customer, supplier and stock transactions in one list.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ab99183e84a70c79c56e7558ecb1bf1eb540afb1bb72a065d9070c0c89f4bbcf
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=686f522d33a3aaf4 | recheck=the description changes | text: The source describes it as "Full name of the transaction type" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=686f522d33a3aaf4 | recheck=a column type changes | text: Declared as nvarchar(50), not nullable.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=5bf2df42b3d3567f | recheck=every new extract | text: Observed: filled on 13 of 13 rows; 13 distinct values.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=686f522d33a3aaf4,5bf2df42b3d3567f | recheck=the description changes, or every new extract | text: The name also tells the subject area (customer, supplier, stock) and, for most types, the sign of the amount or quantity.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.

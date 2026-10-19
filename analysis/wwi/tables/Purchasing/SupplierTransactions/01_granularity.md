---
id: wwi:object:1682105033
subject: wwi/tables/Purchasing/SupplierTransactions
item: 01
topic: granularity
tier: minimum
summary: One row per financial transaction with a supplier - supplier invoices and payments issued - identified by SupplierTransactionID; one invoice per purchase order.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T07:26:00Z
step: S08-066
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 35cdfcd24713d6e9eb43784f7e3be5b8228ce8bb
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 10c8ac5e8c6792404fbdf9e86336cc8afb432c3106485f0c111b343ad363d85c
last_checked_at: 2026-10-19T07:26:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=8516b26c8ecea17f | recheck=the primary key changes | text: The declared primary key is SupplierTransactionID (PK_Purchasing_SupplierTransactions).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=the key stops being unique | text: The key is unique over all 2,440 rows, with no empty values.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=8516b26c8ecea17f,be40a492ac908708 | recheck=every new extract, or a schema change | text: Grain: one row per supplier ledger entry; two kinds of entry share the table (27_peculiarities.md#C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=7a92ab49afadb481 | recheck=every new extract, or a schema change | text: PurchaseOrderID is unique among the 2,074 rows that have one in this extract: one supplier invoice per purchase order here; no constraint enforces it.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:object:638625318
subject: wwi/tables/Warehouse/StockItemTransactions
item: 01
topic: granularity
tier: minimum
summary: One row per stock movement - an issue to a customer, a receipt from a supplier or a stocktake adjustment - identified by StockItemTransactionID.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: aa0ff84050dc38732c7bd5472378de21f412a1f72bdf0c9aa4958b125c232331
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=02947584dba54bc6 | recheck=the primary key changes | text: The declared primary key is StockItemTransactionID (PK_Warehouse_StockItemTransactions).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=the key stops being unique | text: The key is unique over all 236,843 rows, with no empty values.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=02947584dba54bc6,951d022fa77a5499 | recheck=every new extract, or a schema change | text: Grain: one row per movement of one stock item; three kinds share the table (27_peculiarities.md#C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=196f36476eced6f4 | recheck=every new extract, or a schema change | text: In this extract, among issues (InvoiceID, StockItemID) is unique (228,432 rows) and among receipts (PurchaseOrderID, StockItemID) is unique (8,367 rows): one movement per invoiced item and per received purchase line here; not declared.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:object:2018106230
subject: wwi/tables/Sales/Invoices
item: 05
topic: role
tier: minimum
summary: Transaction header for the event "invoice raised", carrying a delivery milestone.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: d89a1e72bf72f1577926929cb7c514b71af6cf08eb13a8181f4f8688da7f99ce
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=the description changes | text: The source describes the table as "Details of customer invoices".
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a foreign key changes | text: It refers to Application.DeliveryMethods, Application.People, Sales.Customers, Sales.Orders and is referred to by Sales.CustomerTransactions, Sales.InvoiceLines, Warehouse.StockItemTransactions.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=every new extract, or a schema change | text: Role: transaction header (sales), with the delivery outcome written back later: one row collects milestones over time.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

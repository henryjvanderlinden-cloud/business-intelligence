---
id: wwi:object:98099390
subject: wwi/tables/Warehouse/PackageTypes
item: 05
topic: role
tier: minimum
summary: Reference data: the list of package types that other tables refer to.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 0263ce1739bb24cfa1adc545bdeab338bb4e156512ec4dcf93e55e467793997d
last_checked_at: 2026-10-20T08:31:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1c7b301d8de3dc31 | recheck=the description changes | text: The source describes the table as "Ways that stock items can be packaged (ie: each, box, carton, pallet, kg, etc.".
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1c7b301d8de3dc31 | recheck=a foreign key changes | text: It refers to Application.People and is referred to by Purchasing.PurchaseOrderLines, Sales.InvoiceLines, Sales.OrderLines, Warehouse.StockItems.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1c7b301d8de3dc31 | recheck=every new extract, or a schema change | text: Role: reference data (a code list), not transactions.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

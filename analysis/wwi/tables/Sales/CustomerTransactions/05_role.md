---
id: wwi:object:366624349
subject: wwi/tables/Sales/CustomerTransactions
item: 05
topic: role
tier: minimum
summary: Accounts-receivable ledger: customer invoices and payments, with the outstanding balance per invoice.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T07:26:00Z
step: S08-066
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 35cdfcd24713d6e9eb43784f7e3be5b8228ce8bb
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 8e272ee961a192b88ad69f58e01cf2ccba809358d2e23ff34de608bfd295c067
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c67ed362aa832e0a | recheck=the description changes | text: The source describes the table as "All financial transactions that are customer-related".
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c67ed362aa832e0a | recheck=a foreign key changes | text: It refers to Application.PaymentMethods, Application.People, Application.TransactionTypes, Sales.Customers, Sales.Invoices and is referred to by no table.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c67ed362aa832e0a | recheck=every new extract, or a schema change | text: Role: financial transactions (customer ledger); events with a state on them (27_peculiarities.md#C3).

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

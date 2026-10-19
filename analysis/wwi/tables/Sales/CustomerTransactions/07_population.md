---
id: wwi:object:366624349
subject: wwi/tables/Sales/CustomerTransactions
item: 07
topic: population
tier: minimum
summary: 97,242 entries from 2013-01-01 to 2016-06-01: 70,566 invoices and 26,676 payments, for 263 customers; nothing filtered from the extracting account.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 8e272ee961a192b88ad69f58e01cf2ccba809358d2e23ff34de608bfd295c067
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=every new extract | text: 97,242 rows, with TransactionDate from 2013-01-01 to 2016-06-01.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c67ed362aa832e0a | recheck=a security policy or a count difference appears | text: Extraction visibility (R15): the owner, the read-only account nsdn_reader and the extract each see 97,242 rows.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c67ed362aa832e0a | recheck=a masking rule appears | text: No column is masked.
- C4 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c67ed362aa832e0a | recheck=permission to read security policies is granted | text: Whether a row-level security policy exists is not established: the catalogue shows nsdn_reader none, which it may not be allowed to see; the equal row counts above show none takes effect on this account.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1,54587972a7ff203e | recheck=every new extract, or a schema change | text: TransactionTypeID: 1 (customer invoice) 70,566, 3 (payment received) 26,676; no credit notes, refunds or contras; PaymentMethodID is 4 (EFT) on every payment.
- C6 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=round 2 checks the relation | text: Only 263 distinct customers appear, against 663 in Sales.Customers: entries are probably booked on the billing customer, not on the branch. Settled in round 2.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:object:802101898
subject: wwi/tables/Sales/Customers
item: 07
topic: population
tier: minimum
summary: 663 customers; 402 in a buying group, 261 not; many columns constant; nothing filtered from the extracting account.
confidence: unknown
claims: 7
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f54b9d7dd163d0d1e3ce34f4adf4d1a76e8caeebe545ad0831277bb0e5b89fb6
last_checked_at: 2026-10-20T05:44:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=every new extract | text: 663 rows, with AccountOpenedDate from 2013-01-01 to 2016-05-07.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=a security policy or a count difference appears | text: Extraction visibility (R15): the owner, the read-only account nsdn_reader and the extract each see 663 rows.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=a masking rule appears | text: No column is masked.
- C4 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=permission to read security policies is granted | text: Whether a row-level security policy exists is not established: the catalogue shows nsdn_reader none, which it may not be allowed to see; the equal row counts above show none takes effect on this account.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=person 1's share changes | text: 617 rows last edited by person 1 (who person 1 is: columns/LastEditedBy/02_meaning.md).
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13,09d66348f676d4b5 | recheck=every new extract, or a schema change | text: BuyingGroupID: 201 Tailspin Toys, 201 Wingtip Toys, 261 none; CustomerCategoryID takes 5 of 8 categories, 459 being novelty shops.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=every new extract, or a schema change | text: Constant in every row: DeliveryMethodID 3, StandardDiscountPercentage 0, IsStatementSent 0, IsOnCreditHold 0, PaymentDays 7; DeliveryRun and RunPosition always empty.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:object:610101214
subject: wwi/tables/Purchasing/Suppliers
item: 27
topic: peculiarities
tier: minimum
summary: Goods and service suppliers in one table; contact persons, addresses and bank details ride along as blocks of columns.
confidence: high
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 7bcb78223c92bb8418652485c9f8ee3acdcdaf5d5f711f56ade275cb0fd6aa98
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=the empty-column patterns change | text: Test 8: 6 distinct patterns of empty columns; the most common: 6 rows with InternalComments empty; 2 rows with DeliveryMethodID, InternalComments, DeliveryAddressLine1 empty; 2 rows with InternalComments, DeliveryAddressLine1 empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=the pattern changes | text: Test 8, by InternalComments (partial): InternalComments=(empty) (11 rows): empty -; filled -; partly empty DeliveryMethodID (3 empty), DeliveryAddressLine1 (4 empty) | InternalComments=Marcos is not in on Mondays (1 rows): empty -; filled DeliveryMethodID, DeliveryAddressLine1 | InternalComments=Only speak to Donald if Hubert really is not available (1 rows): empty DeliveryMethodID; filled DeliveryAddressLine1.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=the pattern changes | text: Test 8, by PaymentDays (partial): PaymentDays=30 (6 rows): empty InternalComments; filled -; partly empty DeliveryMethodID (1 empty), DeliveryAddressLine1 (2 empty) | PaymentDays=7 (4 rows): empty -; filled DeliveryAddressLine1; partly empty DeliveryMethodID (2 empty), InternalComments (2 empty) | PaymentDays=14 (3 rows): empty InternalComments; filled -; partly empty DeliveryMethodID (1 empty), DeliveryAddressLine1 (2 empty).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=a row breaks a dependency | text: Test 1: 36 functional dependencies between non-key columns over the whole extract (0 involving audit columns, a batch-edit signature, not listed): DeliveryCityID -> DeliveryMethodID; DeliveryCityID -> PostalCityID; DeliveryCityID -> BankAccountBranch; DeliveryCityID -> DeliveryPostalCode; DeliveryCityID -> DeliveryLocation; DeliveryCityID -> PostalPostalCode; PostalCityID -> DeliveryMethodID; PostalCityID -> DeliveryCityID; PostalCityID -> BankAccountBranch; PostalCityID -> DeliveryPostalCode; and 26 more in the evidence.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=the structured columns change | text: Test 6: DeliveryLocation holds geography.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=a column is added | text: Test 16: columns ending in digits, possible repeating groups: DeliveryAddressLine1, DeliveryAddressLine2, PostalAddressLine1, PostalAddressLine2.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1,baebb145f336a83d | recheck=every new extract, or a schema change | text: Test 8: service suppliers (categories courier, financial, marketing, insurance) have no delivery method; goods suppliers have one.
- C8 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=every new extract, or a schema change | text: Test 1: a delivery address, a postal address and a bank account are each a block of columns: entities riding along on the supplier.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

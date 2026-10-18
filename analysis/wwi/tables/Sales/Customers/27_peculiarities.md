---
id: wwi:object:802101898
subject: wwi/tables/Sales/Customers
item: 27
topic: peculiarities
tier: minimum
summary: Two kinds of customer (buying-group members and independents) told apart by filled columns; head offices and branches in one table, branches inheriting their head office's terms; addresses as column blocks.
confidence: high
claims: 10
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f54b9d7dd163d0d1e3ce34f4adf4d1a76e8caeebe545ad0831277bb0e5b89fb6
last_checked_at: 2026-10-18T13:20:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=the empty-column patterns change | text: Test 8: 2 distinct patterns of empty columns; the most common: 402 rows with CreditLimit, DeliveryRun, RunPosition empty; 261 rows with BuyingGroupID, AlternateContactPersonID, DeliveryRun, RunPosition empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=the pattern changes | text: Test 8, by BuyingGroupID (exact): BuyingGroupID=(empty) (261 rows): empty AlternateContactPersonID; filled CreditLimit | BuyingGroupID=1 (201 rows): empty CreditLimit; filled AlternateContactPersonID | BuyingGroupID=2 (201 rows): empty CreditLimit; filled AlternateContactPersonID.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=the pattern changes | text: Test 8, by CustomerCategoryID (partial): CustomerCategoryID=3 (459 rows): empty -; filled -; partly empty BuyingGroupID (57 empty), AlternateContactPersonID (57 empty), CreditLimit (402 empty) | CustomerCategoryID=4 (58 rows): empty BuyingGroupID, AlternateContactPersonID; filled CreditLimit | CustomerCategoryID=5 (51 rows): empty BuyingGroupID, AlternateContactPersonID; filled CreditLimit | CustomerCategoryID=6 (48 rows): empty BuyingGroupID, AlternateContactPersonID; filled CreditLimit | CustomerCategoryID=7 (47 rows): empty BuyingGroupID, AlternateContactPersonID; filled CreditLimit.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=a row breaks a dependency | text: Test 1: 23 functional dependencies between non-key columns over the whole extract (6 involving audit columns, a batch-edit signature, not listed): BillToCustomerID -> CustomerCategoryID; BillToCustomerID -> BuyingGroupID; BillToCustomerID -> CreditLimit; BillToCustomerID -> AccountOpenedDate; AlternateContactPersonID -> BuyingGroupID; DeliveryCityID -> PostalCityID; DeliveryCityID -> PhoneNumber; DeliveryCityID -> FaxNumber; DeliveryCityID -> DeliveryLocation; PostalCityID -> DeliveryCityID; and 13 more in the evidence.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=the structured columns change | text: Test 6: DeliveryLocation holds geography.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=a column is added | text: Test 16: columns ending in digits, possible repeating groups: DeliveryAddressLine1, DeliveryAddressLine2, PostalAddressLine1, PostalAddressLine2.
- C7 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=every new extract, or a schema change | text: Reading of the split by BuyingGroupID above: two kinds of customer, buying-group members and independents; a build should treat them as subtypes.
- C8 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42,0cbc424f80836d13 | recheck=every new extract, or a schema change | text: Test 10, a special value: CreditLimit is declared NULL if unlimited, so the 402 buying-group members have unlimited credit by declaration, not a missing value; a build must not read NULL as zero or unknown. Whether the group sets a limit elsewhere is not established.
- C9 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0cbc424f80836d13 | recheck=every new extract, or a schema change | text: Test 11: BillToCustomerID determines CustomerCategoryID, BuyingGroupID, CreditLimit and AccountOpenedDate, so branches carry their head office's values: a hierarchy of two levels in one table, with attributes inherited and repeated.
- C10 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4ffc9f716d8c1e42 | recheck=every new extract, or a schema change | text: Test 1: delivery address, postal address and location are blocks of columns: entities riding along on the customer.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

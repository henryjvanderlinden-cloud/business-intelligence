---
id: wwi:object:610101214
subject: wwi/tables/Purchasing/Suppliers
item: 06
topic: keys
tier: minimum
summary: SupplierID is the declared key, unique and gapless; SupplierName is declared unique.
confidence: medium
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0; C5 added 2026-10-26 by claude-opus-5-5 in step S10-003 from evidence_versions.py (blob cbe6cce7ec5676092c3eecfa4110fe576c205b43) on the extract of 2016-06-02
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=a unique constraint changes | text: Declared unique besides the primary key: UQ_Purchasing_Suppliers_SupplierName (SupplierName).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=69833227169e67f1 | recheck=the key range changes | text: The key runs from 1 to 13 with no gap.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=a foreign key changes | text: 7 declared foreign keies, all enabled and trusted: AlternateContactPersonID -> Application.People.PersonID; LastEditedBy -> Application.People.PersonID; DeliveryCityID -> Application.Cities.CityID; DeliveryMethodID -> Application.DeliveryMethods.DeliveryMethodID; PostalCityID -> Application.Cities.CityID; PrimaryContactPersonID -> Application.People.PersonID; SupplierCategoryID -> Purchasing.SupplierCategories.SupplierCategoryID.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3087bee387e117ef | recheck=every new extract, or a schema change | text: Business key candidate: SupplierName (declared unique) or SupplierReference (unique in the data), rather than the surrogate SupplierID.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-02 | observed=2026-10-26 | checked=2026-10-26 | evidence=acbe488696e7a5af | recheck=every new extract, or a schema change | text: Across the 26 versions of 13 SupplierID values held in the extract (current and history table together), SupplierID persists, and the columns whose value differs between the versions of one key are, with the number of keys concerned: DeliveryLocation (13); ValidFrom (13); ValidTo (13). SupplierName did not change for any key in the history held.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

---
id: wwi:object:1826105546
subject: wwi/tables/Sales/SpecialDeals
item: 05
topic: role
tier: minimum
summary: Pricing rules: reference data with validity, applied to sales prices.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T07:26:00Z
step: S08-066
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 35cdfcd24713d6e9eb43784f7e3be5b8228ce8bb
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 1fab0ac0c38feadfe9bfe300ae286a471a51b393aaa88d88466a89d9b333f329
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=da3666690fc688ae | recheck=the description changes | text: The source describes the table as "Special pricing (can include fixed prices, discount $ or discount %)".
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=da3666690fc688ae | recheck=a foreign key changes | text: It refers to Application.People, Sales.BuyingGroups, Sales.CustomerCategories, Sales.Customers, Warehouse.StockGroups, Warehouse.StockItems and is referred to by no table.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=da3666690fc688ae | recheck=every new extract, or a schema change | text: Role: business rules (price conditions) with a validity period, not transactions.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

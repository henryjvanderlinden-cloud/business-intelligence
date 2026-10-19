---
id: wwi:object:1301579675
subject: wwi/tables/Application/People
item: 05
topic: role
tier: minimum
summary: Master data about people, shared by every subject area; it also holds credentials and employee data.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 5f24e9163953099bd97211216302ba9edbe184de9237880789cd61681982e529
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=the description changes | text: The source describes the table as "People known to the application (staff, customer contacts, supplier contacts)".
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=a foreign key changes | text: It refers to Application.People and is referred to by Application.Cities, Application.Countries, Application.DeliveryMethods, Application.PaymentMethods, Application.People, Application.StateProvinces, Application.SystemParameters, Application.TransactionTypes, Purchasing.PurchaseOrderLines, Purchasing.PurchaseOrders, Purchasing.SupplierCategories, Purchasing.SupplierTransactions, Purchasing.Suppliers, Sales.BuyingGroups, Sales.CustomerCategories, Sales.CustomerTransactions, Sales.Customers, Sales.InvoiceLines, Sales.Invoices, Sales.OrderLines, Sales.Orders, Sales.SpecialDeals, Warehouse.Colors, Warehouse.PackageTypes, Warehouse.StockGroups, Warehouse.StockItemHoldings, Warehouse.StockItemStockGroups, Warehouse.StockItemTransactions, Warehouse.StockItems.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=every new extract, or a schema change | text: Role: master data for persons, referred to by every other table at least through LastEditedBy; one table for several kinds of person (employee, customer contact, supplier contact, technical user).

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.

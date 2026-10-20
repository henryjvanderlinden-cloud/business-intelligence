---
id: wwi:source:position
subject: wwi/_source
item: 29
topic: position
tier: best-effort
summary: Without the audit links, StockItems, Suppliers, Customers and Cities lie between the most tables; People is central through 12 roles, not paths; 2 tables are isolated; classes by rule agree with item 5 on 27 of 31 base tables.
confidence: medium
claims: 9
written_by: claude-opus-5-5
written_at: 2026-10-20T17:55:00Z
step: S08-103
method: measures by prototypes/information_analysis/structure.py (blob d233c4ccad6463612e1d19890d508485eb6b0fc4), claims by write_position.py (blob ecc1fbffc8f024846f4b6131ea07aea781e7610a); method docs/10_architecture/131_structural-position.md; readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: none
last_checked_at: 2026-10-20T17:55:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-02
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: a foreign key changes, or every new extract
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: The graph: 31 base tables, 98 declared links, of which 29 are LastEditedBy; 3 connected components, the isolated tables being Warehouse.ColdRoomTemperatures, Warehouse.VehicleTemperatures.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: Distortion check: with all links Application.People is referred to by 40 links from 28 tables and has betweenness 0.5966 (rank 1); without LastEditedBy, by 12 links from 5 tables, betweenness 0.0234 (rank 12).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: Hubs (betweenness at or above 0.1 without the excluded links): Warehouse.StockItems 0.2996; Purchasing.Suppliers 0.2357; Sales.Customers 0.2125; Application.Cities 0.1811.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: PageRank on the referring-to-referenced direction ranks Application.Countries first (0.0695): a sink at the end of a chain collects the rank of the chain, so PageRank is reported but not used to find hubs (131).
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a rule of 131 or the behaviour changes | text: Classes by the rules of 131: bridge 1 (Warehouse.StockItemStockGroups); configuration 1 (Application.SystemParameters); event 10 (Purchasing.PurchaseOrderLines, Purchasing.PurchaseOrders, Purchasing.SupplierTransactions, Sales.CustomerTransactions, Sales.InvoiceLines, Sales.Invoices, Sales.OrderLines, Sales.Orders, Warehouse.StockItemTransactions, Warehouse.VehicleTemperatures); extension 1 (Warehouse.StockItemHoldings); lookup 9 (Application.DeliveryMethods, Application.PaymentMethods, Application.TransactionTypes, Purchasing.SupplierCategories, Sales.BuyingGroups, Sales.CustomerCategories, Warehouse.Colors, Warehouse.PackageTypes, Warehouse.StockGroups); master 8 (Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Purchasing.Suppliers, Sales.Customers, Sales.SpecialDeals, Warehouse.StockItems); state 1 (Warehouse.ColdRoomTemperatures); and history 17 (the _Archive tables, outside the graph).
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes | text: Reach matrix - the master tables each event or state table reaches by following links: Purchasing.PurchaseOrderLines: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Purchasing.Suppliers, Warehouse.StockItems; Purchasing.PurchaseOrders: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Purchasing.Suppliers; Purchasing.SupplierTransactions: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Purchasing.Suppliers; Sales.CustomerTransactions: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Sales.Customers; Sales.InvoiceLines: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Purchasing.Suppliers, Sales.Customers, Warehouse.StockItems; Sales.Invoices: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Sales.Customers; Sales.OrderLines: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Purchasing.Suppliers, Sales.Customers, Warehouse.StockItems; Sales.Orders: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Sales.Customers; Warehouse.ColdRoomTemperatures: none; Warehouse.StockItemTransactions: Application.Cities, Application.Countries, Application.People, Application.StateProvinces, Purchasing.Suppliers, Sales.Customers, Warehouse.StockItems; Warehouse.VehicleTemperatures: none. Masters by the number of these 11 tables that reach them: Application.Cities 9; Application.Countries 9; Application.People 9; Application.StateProvinces 9; Purchasing.Suppliers 6; Sales.Customers 6; Warehouse.StockItems 4; Sales.SpecialDeals 0.
- C7 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes, or every new extract | text: The class by rule and the role read in item 5 (05_role.md of each table) agree on 27 of the 31 base tables. They differ on Countries, StateProvinces and Cities (master by rule, geographic reference data in item 5) and on SpecialDeals (master by rule, price conditions in item 5); the readings are recorded beside the class in those tables' 29_position.md, and the classes by rule are kept.
- C8 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes, or every new extract | text: Betweenness on a graph without direction counts the paths between two tables that refer to the same parent: Cities lies between customers, suppliers and the company's own addresses, and SpecialDeals between the customer side and the item side. A high betweenness says that a table connects parts of the schema; it does not establish that data or a process flows through it.
- C9 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=94bc8dbba39fcbfb | recheck=a foreign key changes, or every new extract | text: Rows referring and betweenness rank differently: Warehouse.StockItems is high on both (rank 1, 705,901 rows naming it), Purchasing.Suppliers is rank 2 with 13,110 rows naming it, and Warehouse.PackageTypes is rank 20 with 468,843.

## Reasoning

structure.py builds two graphs of the 31 base tables from their declared foreign keys - with all links, and without the links of the audit column LastEditedBy - and measures each table on both, so that the effect of leaving the audit links out is itself on record (docs/10_architecture/131_structural-position.md, distortion check). It adds rows and behaviour from three extracts, classes each table by the rules of 131 in order, and lists which master tables each event or state table reaches by following links. The 17 history tables carry no declared keys and stand outside the graph. The per-table files hold each table's measures and any reading beside its class.

## Uncertainties

Only declared foreign keys are links; the candidate relations without a declared key (across/candidates.md) are not in the graph. The hub threshold (betweenness 0.1) and the lookup rule (at most 2 attributes) are heuristics of 131, not facts of the source. Behaviour rests on two transitions of consecutive weekdays: a table that changes monthly or yearly, such as the geography or the lookups, looks unchanged in both, and a table that grows on some days only may look unchanged (analysis/README.md section 5).

## For a person

None.

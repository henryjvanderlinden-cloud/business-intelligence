---
id: nsdn:source:wwi
kind: source
name: wwi
status: accepted
ruled_in: ADR-0015, ADR-0027, ADR-0029, ADR-0033, ADR-0037
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#2 and docs/10_architecture/149_wwi-satellites.md#2
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py
title: Wide World Importers, one database instance
key_space: wwi
key_case: fold
extract: daily, each table complete, with a manifest of row counts and hashes (prototypes/wwi_sandbox/README.md)
by_rule: LastEditedBy to the hub's audit satellite (kept in reference tables); ValidFrom, ValidTo, LastEditedWhen as source system time
---

## Base tables

- Application.Cities | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Application.Cities_Archive | catalogue=analysis/wwi/tables/Application/Cities/evidence/b83a41fa256ce9db.json
- Application.Countries | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Application.Countries_Archive | catalogue=analysis/wwi/tables/Application/Countries/evidence/f3e79ea442f46838.json
- Application.DeliveryMethods | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Application.DeliveryMethods_Archive | catalogue=analysis/wwi/tables/Application/DeliveryMethods/evidence/4d0a658d91d44a61.json
- Application.PaymentMethods | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Application.PaymentMethods_Archive | catalogue=analysis/wwi/tables/Application/PaymentMethods/evidence/065bbf4844346cbb.json
- Application.People | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Application.People_Archive | catalogue=analysis/wwi/tables/Application/People/evidence/3654cc5be0d96b13.json
- Application.StateProvinces | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Application.StateProvinces_Archive | catalogue=analysis/wwi/tables/Application/StateProvinces/evidence/b4dd7fb18f3fa094.json
- Application.SystemParameters | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Application/SystemParameters/evidence/0c6c31f37cdc5cc9.json
- Application.TransactionTypes | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Application.TransactionTypes_Archive | catalogue=analysis/wwi/tables/Application/TransactionTypes/evidence/686f522d33a3aaf4.json
- Purchasing.PurchaseOrderLines | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Purchasing/PurchaseOrderLines/evidence/9e1f3e773862db95.json
- Purchasing.PurchaseOrders | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Purchasing/PurchaseOrders/evidence/ec7b7812547c43e1.json
- Purchasing.SupplierCategories | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Purchasing.SupplierCategories_Archive | catalogue=analysis/wwi/tables/Purchasing/SupplierCategories/evidence/a84296fdd02696bb.json
- Purchasing.SupplierTransactions | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Purchasing/SupplierTransactions/evidence/8516b26c8ecea17f.json
- Purchasing.Suppliers | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Purchasing.Suppliers_Archive | catalogue=analysis/wwi/tables/Purchasing/Suppliers/evidence/3087bee387e117ef.json
- Sales.BuyingGroups | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Sales.BuyingGroups_Archive | catalogue=analysis/wwi/tables/Sales/BuyingGroups/evidence/ee1eebac15b0a67f.json
- Sales.CustomerCategories | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Sales.CustomerCategories_Archive | catalogue=analysis/wwi/tables/Sales/CustomerCategories/evidence/1da3725d368ce960.json
- Sales.CustomerTransactions | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Sales/CustomerTransactions/evidence/c67ed362aa832e0a.json
- Sales.Customers | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Sales.Customers_Archive | catalogue=analysis/wwi/tables/Sales/Customers/evidence/4ffc9f716d8c1e42.json
- Sales.InvoiceLines | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Sales/InvoiceLines/evidence/21777813c14f1502.json
- Sales.Invoices | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Sales/Invoices/evidence/98f988a2bfe42550.json
- Sales.OrderLines | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Sales/OrderLines/evidence/10ba08f87c0c050b.json
- Sales.Orders | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Sales/Orders/evidence/f61ebb431b7b9012.json
- Sales.SpecialDeals | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Sales/SpecialDeals/evidence/da3666690fc688ae.json
- Warehouse.ColdRoomTemperatures | extract=full | system_time=ValidFrom, ValidTo | audit=none | history=Warehouse.ColdRoomTemperatures_Archive | catalogue=analysis/wwi/tables/Warehouse/ColdRoomTemperatures/evidence/17b318403896763e.json
- Warehouse.Colors | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Warehouse.Colors_Archive | catalogue=analysis/wwi/tables/Warehouse/Colors/evidence/ca4f1120f73d1d20.json
- Warehouse.PackageTypes | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Warehouse.PackageTypes_Archive | catalogue=analysis/wwi/tables/Warehouse/PackageTypes/evidence/1c7b301d8de3dc31.json
- Warehouse.StockGroups | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Warehouse.StockGroups_Archive | catalogue=analysis/wwi/tables/Warehouse/StockGroups/evidence/38f00eb780b1f6ea.json
- Warehouse.StockItemHoldings | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Warehouse/StockItemHoldings/evidence/80a4585b8f062d77.json
- Warehouse.StockItemStockGroups | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Warehouse/StockItemStockGroups/evidence/e2eab62afe77be4c.json
- Warehouse.StockItemTransactions | extract=full | system_time=LastEditedWhen | audit=LastEditedBy | history=none | catalogue=analysis/wwi/tables/Warehouse/StockItemTransactions/evidence/02947584dba54bc6.json
- Warehouse.StockItems | extract=full | system_time=ValidFrom, ValidTo | audit=LastEditedBy | history=Warehouse.StockItems_Archive | catalogue=analysis/wwi/tables/Warehouse/StockItems/evidence/fbbc435f3d190ff0.json
- Warehouse.VehicleTemperatures | extract=full | system_time=none | audit=none | history=none | catalogue=analysis/wwi/tables/Warehouse/VehicleTemperatures/evidence/9048f084eab5cb11.json

## Notes

The 31 base tables of the source and, for each, the columns handled by rule rather than declared: its source system time (149 Rule 2), its audit column (149 Rule 3) and its history table, loaded on the first day (ADR-0027 decision 2). The 17 history tables yield nothing of their own (147 section 4).

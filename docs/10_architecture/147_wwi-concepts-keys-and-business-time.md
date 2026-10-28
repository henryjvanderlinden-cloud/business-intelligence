# 147 — Wide World Importers: business concepts, business keys and business time (step A)

> **STATUS: RULED** 2026-10-28: the three cases of §6 in ADR-0028, the rest in ADR-0029. The hub's technical key is not decided here. Drafted 2026-10-26 in session 10 from handover 10. Reviewed on sol in two passes,
> both of which failed the first version ([keys](../30_research/notes/XREV_2026-10-26_147-keys_sol.md),
> [business time](../30_research/notes/XREV_2026-10-26_147-business-time_sol.md)); this is the revised text, itself
> unreviewed ([510](../50_process/510_external-review.md)). Open under [`ARC-OP-37`](../../registers/OPEN_POINTS.md).

## 1. What this note does

Handover 10 set step A of the author's route of 2026-10-21: for all 31 base tables of Wide World Importers (WWI),
which business concepts become hubs, on which business key, with each key's issuer or namespace and grain
([144](144_raw-vault-business-vault-calculation-engines.md) §3 item 2), and which tables yield no hub. With it goes the
per-table proposal owed under [ADR-0027](../20_decisions/0027-bitemporal-integration-layer.md) decision 4: which
column, if any, carries business valid time, which carries source system time, and where valid time is unknown.

Every choice cites the analysis claim it rests on. Paths in citations are relative to `analysis/wwi/tables/` unless
they begin with `across/`, which is `analysis/wwi/across/`, or with `analysis/`. Where no claim supports a choice, the note says so.
Relationships (step B), satellites (step C), loading and the model-file format are out of scope.

Three facts were missing from the record and were added to it before this note was written, under ADR-0022 decision
4, in step S10-003: for each of the 16 system-versioned base tables, which columns differ between the versions of one
key (`<table>/06_keys.md#C5`); and whether the country and state-province codes conform to the published ISO lists
(`Application/Countries/06_keys.md#C6`, `Application/StateProvinces/06_keys.md#C6`).

## 2. Three rules applied throughout

The rules and the tables below are the second version, revised after review by sol
([XREV keys](../30_research/notes/XREV_2026-10-26_147-keys_sol.md)), which failed the first.

**Rule 1: where no business identifier is evidenced, the hub key is the source's own record identifier, labelled as
such and qualified by the key space of its issuer, `wwi`.** Every table's declared primary key is described by the
source as a "Numeric ID used for reference to … within the database" (for example `Sales/Orders/06_keys.md#C1`; the
same wording in the `columns/<key>/02_meaning.md#C1` of each table), and it is the identifier every other table refers
to (the foreign-key claims in each `06_keys.md`). For no concept except country does the record show an identifier used
outside the database; whether `OrderID` is printed on documents is open (`Sales/Orders/06_keys.md#C7`). These keys are
therefore source-issued record identifiers, adopted because nothing better is evidenced, not proven business
identity. The declared-unique names are not used instead, for one reason the record now shows: names are renamed while
the identifier stays. Of the 16 system-versioned base tables, eight hold a key whose declared-unique name changed
between versions (`Application/Countries/06_keys.md#C5`, `Application/DeliveryMethods/06_keys.md#C5`,
`Application/PaymentMethods/06_keys.md#C5`, `Application/TransactionTypes/06_keys.md#C5`,
`Purchasing/SupplierCategories/06_keys.md#C5`, `Sales/CustomerCategories/06_keys.md#C5`, `Warehouse/Colors/06_keys.md#C5`,
`Warehouse/StockGroups/06_keys.md#C5`); in the data, Turkey became Türkiye and Gray became Steel Gray. A key built
on a name would have split one thing into two at each rename. Names stay as descriptive attributes.

The key-space code `wwi` names the issuer of these numbers, as 144 §3 item 2 requires: the identity numbering of this
WWI database instance, not the WWI software as a system. A replacement application, a migration that renumbers, or a
second instance is a different issuer and gets a code of its own, so a restarted sequence cannot merge two unrelated
things under one key; relating the old and the new numbers is a delivered crosswalk or business-vault matching
(144 §3 items 4 and 5). Each concept has its own hub, so numbers from different tables never meet; the three ledgers,
whose numbers come from one shared range, do not overlap either (`Sales/CustomerTransactions/06_keys.md#C3`). The only
governed namespace the record shows is ISO 3166-1 for countries (section 3, item 1).

**Rule 2: a code list becomes a hub when it takes part in a relationship of its own; a code list that only describes
one other concept is a reference table.** A relationship needs hubs at both ends, so a code list that is the far end of
a bridge, or the scope of another concept, is a hub: stock group (members through the bridge, and scope of special
deals), buying group and customer category (each classifies customers and is the scope of special deals;
`Sales/SpecialDeals/06_keys.md#C2`). Reference tables are keyed the same way (Rule 1), keep their history from the
source's history tables and get no hub; the tables that use them carry the code. The classes of
[131](131_structural-position.md) (`29_position.md` of each table) are cited as a description and were not used as the
mapping, as handover 10 requires.

**Rule 3: a line is a hub on its own record identifier.** An order line, an invoice line and a purchase-order line
each have a declared identifier that is unique across all lines of all headers, not within one header
(`Sales/OrderLines/01_granularity.md#C1`, `#C2`; `Sales/InvoiceLines/01_granularity.md#C1`, `#C2`;
`Purchasing/PurchaseOrderLines/01_granularity.md#C1`, `#C2`), and the source issues no line number within a header.
The shorter candidate (header, stock item) is observed unique in both extracts but not declared
(`Sales/OrderLines/01_granularity.md#C3`, the same `#C3` for the other two; `analysis/wwi/_source/22_stability.md#C3`),
so a key built on it would collapse two lines for one item the first time the source allows them. With a hub on the
line's own identifier, the line keeps one identity if its header or item were ever corrected, and its relationships
to header and item are links in step B. The lines are updated in place (picking, receipt), so they need their own
satellites in any case.

## 3. The hubs proposed: twenty-two tables, twenty-two concepts

Grain is one row of the hub per instance named. "Key space" is the issuer code of 144 §3; "ISO" means a governed
namespace and no key-space code. "Record identifier" marks a key adopted under Rule 1 without evidence of use outside
the database.

| # | Concept | Source table | Business key | Key space | Grain | Evidence |
|---|---|---|---|---|---|---|
| 1 | country | Application.Countries | `IsoAlpha3Code` | ISO 3166-1 | one country | `Application/Countries/06_keys.md#C6`, `#C5` (code never changed, name changed once), `columns/IsoAlpha3Code/02_meaning.md#C1`, `#C3` |
| 2 | state or province | Application.StateProvinces | `StateProvinceID` (record identifier) | `wwi` | one subdivision | `Application/StateProvinces/06_keys.md#C2`, `#C5`, `#C6` |
| 3 | city | Application.Cities | `CityID` (record identifier) | `wwi` | one city | `Application/Cities/06_keys.md#C1`, `#C3` (name not a key, nor name within state), `#C5` |
| 4 | person | Application.People | `PersonID` (record identifier) | `wwi` | one person: staff, customer or supplier contact, technical user | `Application/People/06_keys.md#C1`, `#C4`, `#C5`; `columns/LogonName/02_meaning.md#C4`; `across/entities/person/26_entities.md#C1` |
| 5 | customer | Sales.Customers | `CustomerID` (record identifier) | `wwi` | one customer account: head office, branch or individual | `Sales/Customers/06_keys.md#C1`, `#C2`, `#C5`; `Sales/Customers/01_granularity.md`; `across/entities/customer/26_entities.md#C1` |
| 6 | customer category | Sales.CustomerCategories | `CustomerCategoryID` (record identifier) | `wwi` | one category | `Sales/CustomerCategories/06_keys.md#C2`, `#C5` (renamed); `Sales/SpecialDeals/06_keys.md#C2` |
| 7 | buying group | Sales.BuyingGroups | `BuyingGroupID` (record identifier) | `wwi` | one buying group | `Sales/BuyingGroups/06_keys.md#C2`, `#C5`; `Sales/SpecialDeals/06_keys.md#C2` |
| 8 | supplier | Purchasing.Suppliers | `SupplierID` (record identifier) | `wwi` | one supplier organisation | `Purchasing/Suppliers/06_keys.md#C1`, `#C4`, `#C5`; `columns/SupplierReference/02_meaning.md#C1` |
| 9 | stock item | Warehouse.StockItems | `StockItemID` (record identifier) | `wwi` | one product | `Warehouse/StockItems/06_keys.md#C2`, `#C4`, `#C5`; `columns/Barcode/02_meaning.md#C3` |
| 10 | stock group | Warehouse.StockGroups | `StockGroupID` (record identifier) | `wwi` | one stock group | `Warehouse/StockGroups/06_keys.md#C2`, `#C5` (renamed); `Warehouse/StockItemStockGroups/06_keys.md#C4` |
| 11 | special deal | Sales.SpecialDeals | `SpecialDealID` (record identifier) | `wwi` | one deal record | `Sales/SpecialDeals/06_keys.md#C1`, `#C2`, `#C3` |
| 12 | sales order (fulfilment order) | Sales.Orders | `OrderID` (record identifier) | `wwi` | one order as WWI fulfils it: an original or a backorder | `Sales/Orders/06_keys.md#C1`, `#C2`, `#C4`, `#C7`; `across/terms/order/25_terms.md#C1` |
| 13 | sales order line | Sales.OrderLines | `OrderLineID` (record identifier) | `wwi` | one line | `Sales/OrderLines/01_granularity.md#C1` to `#C3` |
| 14 | invoice | Sales.Invoices | `InvoiceID` (record identifier) | `wwi` | one invoice | `Sales/Invoices/01_granularity.md#C1`, `#C2`, `#C4` |
| 15 | invoice line | Sales.InvoiceLines | `InvoiceLineID` (record identifier) | `wwi` | one line | `Sales/InvoiceLines/01_granularity.md#C1` to `#C3` |
| 16 | purchase order | Purchasing.PurchaseOrders | `PurchaseOrderID` (record identifier) | `wwi` | one order to a supplier | `Purchasing/PurchaseOrders/06_keys.md#C1`, `#C3`; `columns/SupplierReference/02_meaning.md#C4` |
| 17 | purchase-order line | Purchasing.PurchaseOrderLines | `PurchaseOrderLineID` (record identifier) | `wwi` | one line | `Purchasing/PurchaseOrderLines/01_granularity.md#C1` to `#C3` |
| 18 | customer ledger entry | Sales.CustomerTransactions | `CustomerTransactionID` (record identifier) | `wwi` | one invoice or payment entry | `Sales/CustomerTransactions/06_keys.md#C1`, `#C3`; `Sales/CustomerTransactions/03_temporal.md#C5` |
| 19 | supplier ledger entry | Purchasing.SupplierTransactions | `SupplierTransactionID` (record identifier) | `wwi` | one supplier invoice or payment | `Purchasing/SupplierTransactions/06_keys.md#C1`, `#C3` |
| 20 | stock movement | Warehouse.StockItemTransactions | `StockItemTransactionID` (record identifier) | `wwi` | one issue, receipt or adjustment | `Warehouse/StockItemTransactions/06_keys.md#C1`, `#C3`; `across/terms/transaction/25_terms.md#C3` |
| 21 | cold-room sensor | Warehouse.ColdRoomTemperatures | `ColdRoomSensorNumber` | `wwi` | one sensor | `Warehouse/ColdRoomTemperatures/06_keys.md#C2`; `03_temporal.md#C5`, `#C6`; `columns/ColdRoomSensorNumber/02_meaning.md#C1`, `#C4` |
| 22 | vehicle | Warehouse.VehicleTemperatures | `VehicleRegistration` | `wwi` | one delivery vehicle | `Warehouse/VehicleTemperatures/06_keys.md#C2`; `columns/VehicleRegistration/02_meaning.md#C1`, `#C3`, `#C4` |

Notes on single rows, where the table does not say enough:

*Country (1).* The only key proposed without the code `wwi`. All 190 countries carry an ISO 3166-1 code pair from the
published list, the source describes the code as "assigned to the country by ISO", and no code changed in the history
held. The evidence is medium, because the list was read through a summarising fetch. Other tables refer to countries
by `CountryID`, so loading those relationships needs a deterministic resolution of `CountryID` to the ISO code from the
same extract. This is the first weak case of section 6.

*State or province (2).* The state codes all occur among the ISO 3166-2:US subdivision codes
(`Application/StateProvinces/06_keys.md#C6`), but ISO's identifier is written with the country's two-letter code
(`US-WA`), which the source does not hold, and a composition of the three-letter country code with the state code
would be an identifier of our own making, not ISO's. The first version proposed it; review rejected it. The key is
therefore the record identifier, with the state code kept as an attribute from which a governed crosswalk could later
derive the ISO identifier.

*Person (4).* One hub for every kind of person, since the source holds them in one table under one identifier
(`across/entities/person/26_entities.md#C1`); staff, contact and salesperson are roles, carried by relationships and
flags. The banding of `PersonID` by kind of person (`Application/People/06_keys.md#C3`, low) is not used. Every table's
`LastEditedBy` refers to this hub for no business reason (ADR-0021's distortion principle); it is audit data and becomes
no business relationship in step B.

*Customer (5).* The delivered-to customer, the billed customer and the head office are roles of one concept, not three
concepts (`across/terms/customer/25_terms.md#C1` to `#C3`); they become relationships in step B. `CustomerName` is
declared unique and never changed in the history held (`Sales/Customers/06_keys.md#C1`, `#C5`), but Rule 1 applies.

*Supplier (8).* `SupplierReference` is WWI's account at the supplier, issued by the supplier and identifying WWI
(`Purchasing/Suppliers/columns/SupplierReference/02_meaning.md#C1`); it is not a key of the supplier.

*Stock item (9).* `Barcode` is filled for 8 of 227 items; whether the barcodes are GS1 identifiers is not established
(no claim exists), so it is an attribute.

*Special deal (11).* The record establishes no business identity for a deal beyond its record identifier: two rows, no
table refers to it (`Sales/SpecialDeals/06_keys.md#C1`, `#C2`). It is a hub on the record identifier, like the lines,
because a deal is scoped to one of three customer-side hubs and one of two item-side hubs, exactly one of each by check
constraint (`#C3`); a hub with links keeps that scope and the deal's own period and prices apart, where a single link
would need empty endpoints. A deal deleted and entered again gets a new identifier and is a new record; whether the
business regards it as the same deal is the kind of judgement the business vault holds.

*Sales order (12).* The hub is the fulfilment order, the row of `Sales.Orders`. The customer order as placed, an
original with its chain of backorders (`Sales/Orders/27_peculiarities.md#C12`, `#C4`), has no key in the source: the
customer's purchase-order number is shared across customers and cannot stand for it (`Sales/Orders/06_keys.md#C4`).
It is therefore not a raw-vault hub. It would be a business-vault concept derived from the backorder links, keyed by
the original order's `OrderID` (the link's direction: `Sales/Orders/columns/BackorderOrderID/02_meaning.md#C2`).

*Invoice (14).* `OrderID` identifies the invoice too in this extract, but no constraint enforces one invoice per order
(`Sales/Invoices/01_granularity.md#C4`), so it is a relationship, not a key.

*The three ledgers (18 to 20).* The three identifiers share one numbering and never overlap
(`Sales/CustomerTransactions/06_keys.md#C3`; `across/terms/transaction/25_terms.md#C1`, `#C2`), but they denote three
different things, two of money and one of goods (`#C3`), so they are three hubs. They are hubs rather than event-only
links because the customer ledger is updated in place on settlement (`Sales/CustomerTransactions/03_temporal.md#C5`), so
its state needs a satellite; the supplier and stock ledgers are hubs for uniformity, a choice step B may revisit.

*Sensors (21, 22).* `ColdRoomTemperatureID` identifies a reading and is renewed with every one; the sensor number is
what persists (`Warehouse/ColdRoomTemperatures/06_keys.md#C2`), consistent over 3.7 million readings in the history
table (`03_temporal.md#C5`). For vehicles, the natural key of a reading is (vehicle registration, chiller sensor number,
recorded time) (`Warehouse/VehicleTemperatures/06_keys.md#C2`); the vehicle is the concept with identity, a chiller
sensor is identified only within its vehicle, and the readings are events attached to the sensors in step B and C, not
hubs. Neither table has any column description: the readings of `VehicleRegistration` and `RecordedWhen` rest on
column names (`columns/VehicleRegistration/02_meaning.md#C4`, `columns/RecordedWhen/02_meaning.md#C4`, both low). A
registration plate is issued by a licensing authority, but no jurisdiction is in the data, so the code `wwi` stays. This
is the third weak case of section 6.

## 4. The nine tables that yield no hub

| Table | What it becomes | Evidence |
|---|---|---|
| Application.DeliveryMethods | reference table on `DeliveryMethodID` (`wwi`) | `Application/DeliveryMethods/06_keys.md#C2`, `#C5` (renamed) |
| Application.PaymentMethods | reference table on `PaymentMethodID` (`wwi`) | `Application/PaymentMethods/06_keys.md#C2`, `#C5` (renamed) |
| Application.TransactionTypes | reference table on `TransactionTypeID` (`wwi`) | `Application/TransactionTypes/06_keys.md#C2`, `#C5` (renamed) |
| Purchasing.SupplierCategories | reference table on `SupplierCategoryID` (`wwi`) | `Purchasing/SupplierCategories/06_keys.md#C2`, `#C5` (renamed) |
| Warehouse.Colors | reference table on `ColorID` (`wwi`) | `Warehouse/Colors/06_keys.md#C2`, `#C5` (renamed) |
| Warehouse.PackageTypes | reference table on `PackageTypeID` (`wwi`) | `Warehouse/PackageTypes/06_keys.md#C2`, `#C5` |
| Warehouse.StockItemHoldings | descriptive data of the stock item, sampled | `Warehouse/StockItemHoldings/06_keys.md#C3`; `across/entities/stock-item/26_entities.md#C1` |
| Warehouse.StockItemStockGroups | membership of a stock item in a stock group, a link in step B; `StockItemStockGroupID` is a surrogate | `Warehouse/StockItemStockGroups/06_keys.md#C1`, `#C4` |
| Application.SystemParameters | configuration: WWI's own addresses and settings, one row | `Application/SystemParameters/06_keys.md#C3`; `01_granularity.md` |

The 17 history tables (`*_Archive`) yield nothing of their own: each holds the earlier versions of its base table
(for example `Sales/Customers_Archive/05_role.md#C5`) and is loaded as that table's history on the first day, ordered
by source system time (ADR-0027 decision 2).

The six reference tables each describe one or two other concepts and take part in no relationship of their own; the
payment method and transaction type on ledger entries, the delivery method on customers, suppliers, orders and
invoices, the colour and package types on stock items and lines are codes carried by those concepts' satellites.

## 5. Business time per table

The three clocks of ADR-0027: business valid time (when it was true in the business), source system time (when the
source recorded it; stored and labelled, never presented as business time), and knowledge time (our load time, not
listed). "Unknown" means the satellites of that table carry valid time as explicitly unknown (ADR-0027 decision 1).
A milestone is a business time written back onto an existing row later, in place; how milestones enter valid time is
the second weak case of section 6, revised after review by sol
([XREV](../30_research/notes/XREV_2026-10-26_147-business-time_sol.md)). In the table, the "business valid time" of an
event table dates the event's existence, from the event's own date; a milestone dates only the milestone it names, at
its own grain, and never another column or a later version.

| Table | Business valid time | Milestones written back | Other business dates (attributes) | Source system time | Evidence |
|---|---|---|---|---|---|
| Application.Cities | unknown | — | — | `ValidFrom`, `ValidTo` | `Application/Cities/03_temporal.md#C3`, `#C4`, `#C5` |
| Application.Countries | unknown | — | — | `ValidFrom`, `ValidTo` | `Application/Countries/03_temporal.md#C5`, `#C6` |
| Application.DeliveryMethods | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Application.PaymentMethods | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Application.People | unknown | — | — | `ValidFrom`, `ValidTo` | `Application/People/03_temporal.md#C3`, `#C4` |
| Application.StateProvinces | unknown | — | — | `ValidFrom`, `ValidTo` | `Application/StateProvinces/03_temporal.md#C4` |
| Application.SystemParameters | unknown | — | — | `LastEditedWhen` | `Application/SystemParameters/03_temporal.md#C1`, `#C3` |
| Application.TransactionTypes | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Purchasing.PurchaseOrderLines | none of its own | `LastReceiptDate`, of the latest receipt only (overwritten; receipts in parts never observed); finalisation has no date | header's `OrderDate` is context, through the relationship | `LastEditedWhen` | `Purchasing/PurchaseOrderLines/03_temporal.md#C2`, `#C5`; `columns/LastReceiptDate/02_meaning.md#C1`; `analysis/wwi/_source/22_stability.md#C19` |
| Purchasing.PurchaseOrders | `OrderDate` | finalisation has no date | `ExpectedDeliveryDate` (planned) | `LastEditedWhen` | `Purchasing/PurchaseOrders/03_temporal.md#C3`, `#C5`, `#C6`; `columns/OrderDate/02_meaning.md#C1` |
| Purchasing.SupplierCategories | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Purchasing.SupplierTransactions | `TransactionDate` | none established: no settlement was ever seen written back | `FinalizationDate` (meaning as a milestone unproven) | `LastEditedWhen` | `Purchasing/SupplierTransactions/03_temporal.md#C3`, `#C5`, `#C6`; `columns/TransactionDate/02_meaning.md#C1`; `analysis/wwi/_source/22_stability.md#C21` |
| Purchasing.Suppliers | unknown | — | — | `ValidFrom`, `ValidTo` | `Purchasing/Suppliers/03_temporal.md#C4`, `#C5` |
| Sales.BuyingGroups | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Sales.CustomerCategories | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Sales.CustomerTransactions | `TransactionDate` | `FinalizationDate` | — | `LastEditedWhen` | `Sales/CustomerTransactions/03_temporal.md#C3`, `#C5`, `#C6` |
| Sales.Customers | unknown | — | `AccountOpenedDate` (start of the account) | `ValidFrom`, `ValidTo` | `Sales/Customers/03_temporal.md#C3`, `#C4`; `columns/AccountOpenedDate/02_meaning.md#C1` |
| Sales.InvoiceLines | none of its own | — | header's `InvoiceDate` is context, through the relationship | `LastEditedWhen` | `Sales/InvoiceLines/03_temporal.md#C3`, `#C5` |
| Sales.Invoices | `InvoiceDate` | `ConfirmedDeliveryTime` | — | `LastEditedWhen` | `Sales/Invoices/03_temporal.md#C3`, `#C5`, `#C6`; `columns/InvoiceDate/02_meaning.md#C1` |
| Sales.OrderLines | none of its own | `PickingCompletedWhen`, the line's own, distinct from the header's | header's `OrderDate` is context, through the relationship | `LastEditedWhen` | `Sales/OrderLines/03_temporal.md#C3`, `#C5` |
| Sales.Orders | `OrderDate` | `PickingCompletedWhen` | `ExpectedDeliveryDate` (planned) | `LastEditedWhen` | `Sales/Orders/03_temporal.md#C2`, `#C5`, `#C6`, `#C7`; `columns/OrderDate/02_meaning.md#C1` |
| Sales.SpecialDeals | `StartDate` (the deal's own period, ending `EndDate`) | — | — | `LastEditedWhen` | `Sales/SpecialDeals/03_temporal.md#C3`, `#C5` |
| Warehouse.ColdRoomTemperatures | `RecordedWhen` (of each reading) | — | — | `ValidFrom`, `ValidTo` (equal to `RecordedWhen` in the history) | `Warehouse/ColdRoomTemperatures/03_temporal.md#C3`, `#C5`; `columns/RecordedWhen/02_meaning.md#C4` |
| Warehouse.Colors | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Warehouse.PackageTypes | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Warehouse.StockGroups | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Warehouse.StockItemHoldings | none; sampled | — | — | `LastEditedWhen` | `Warehouse/StockItemHoldings/03_temporal.md#C5`, `#C6`; ADR-0027 Consequences |
| Warehouse.StockItemStockGroups | unknown; an ended membership leaves no trace | — | — | `LastEditedWhen` | `Warehouse/StockItemStockGroups/03_temporal.md#C3`, `#C5` |
| Warehouse.StockItemTransactions | `TransactionOccurredWhen` | — | — | `LastEditedWhen` | `Warehouse/StockItemTransactions/03_temporal.md#C3`, `#C5`; `columns/TransactionOccurredWhen/02_meaning.md#C1` |
| Warehouse.StockItems | unknown | — | — | `ValidFrom`, `ValidTo` | `Warehouse/StockItems/03_temporal.md#C4` |
| Warehouse.VehicleTemperatures | `RecordedWhen` | — | — | none | `Warehouse/VehicleTemperatures/03_temporal.md#C3`, `#C5`; `columns/RecordedWhen/02_meaning.md#C4` |

Where the table writes "`03_temporal.md#C3`" without a table, it is that table's own file.

The pattern is simple. The sixteen system-versioned master and lookup tables carry no business time at all: their versions are dated
only by the database, and the record shows that those dates are edit times, from a 2022 edit by Microsoft
(`Application/Countries/03_temporal.md#C5`) to a closing batch that re-versioned every stock item within twelve minutes
(`Warehouse/StockItems/03_temporal.md#C4`). Under ADR-0027 their valid time is unknown, and their history is ordered by
source system time. The event tables carry the date of the event, and four tables carry a milestone with a date: order and order line
(picking), invoice (delivery) and customer ledger (finalisation); the purchase-order line carries the date of its
latest receipt only. The line tables carry no event date of their own; their header's date is document context,
reached through the relationship in the business vault, because looking it up during loading would be interpretation
in the raw vault (144 §2). It never dates a line's own milestone: line and header picking are different facts at
different grains, and the source sets the header's only when all lines are picked (`Sales/Orders/03_temporal.md#C3`,
low).

Four consequences follow from the review, and step C would have to honour them. First, a mutable attribute that is
not a milestone has explicitly unknown valid time before it is first observed and for every later change the source
does not date; a milestone retained on a row is evidence for its own milestone only. Second, a milestone corrected in
the source is a replacing assertion: at the later knowledge time it supersedes the earlier assertion over its whole
claimed validity, and "valid to" is derived from the next row only within one knowledge-time slice, after that
supersession. Third, between two daily extracts a milestone may happen twice or be overwritten (`LastReceiptDate`),
and no valid time can recover the state in between; such history is labelled sampled (127), and an "as of" answer
between two observations is not claimed correct. Fourth, the supplier ledger's `FinalizationDate` is kept as an
attribute and dates nothing until a settlement is seen written back, which neither transition showed
(`Purchasing/SupplierTransactions/03_temporal.md#C5`; `analysis/wwi/_source/22_stability.md#C21`).

`AccountOpenedDate` is a business date, but of the customer's existence, not of the version: it does not say when a
customer's current credit limit became true, which is what the versions record
(`Sales/Customers/03_temporal.md#C4`; `Sales/Customers/06_keys.md#C5` shows that `CreditLimit` is the only business column that ever changed). The
deals are the one source with a business validity period of their own, which ADR-0027's insert-only rule keeps as
data: `StartDate` is stored as valid time, `EndDate` as the source's stated end.

## 6. Weak cases for the author

*Ruled 2026-10-28 in [ADR-0028](../20_decisions/0028-wwi-country-key-milestones-and-sensors.md): all three as
recommended; for item 2, option (c), with each milestone a satellite of its own and the accumulating snapshot built in
the marts.*

Three cases, each with a recommendation. Everything else in this note rests on claims of high or medium confidence
and is proposed for ruling as a whole once reviewed.

1. **The country keyed on its ISO code without a key-space code (section 3, item 1).** The evidence is that every
   code conforms to the ISO 3166-1 list (medium: list read second-hand), the source's own description of the code, and
   codes that never changed. Against it: the source refers to countries by its own identifier, so every relationship
   to a country needs a deterministic lookup when loaded, and a later non-ISO row would have no key. Recommendation:
   the ISO key, as proposed, because it is the only identifier here that a second source could share without
   matching. (The first version proposed ISO keys for states too; review showed that the source cannot form ISO's
   subdivision identifier, and states now use the record identifier.)
2. **How milestones enter valid time.** `PickingCompletedWhen` (orders and order lines, separately),
   `ConfirmedDeliveryTime` (invoices), `FinalizationDate` (customer ledger) and `LastReceiptDate` (purchase-order
   lines) are business times written back later, in place, and seen only as the sampled states of daily extracts
   (`Sales/Orders/03_temporal.md#C7`, `Sales/Invoices/03_temporal.md#C5`, `Sales/CustomerTransactions/03_temporal.md#C5`).
   Two changes carry no date at all: finalising a purchase order and a purchase-order line. The options: (a) valid
   time of every version is the event date, and milestone stamps are plain attributes; (b) a version's valid time is
   the latest milestone stamp it shows; (c) the event's existence is valid from its event date, and each milestone is
   a fact of its own at its own grain, valid from its stamp, with the four consequences above. The first version of
   this note recommended (b); review by sol showed that it fails: an order raised on 2015-12-29 and picked on
   2016-06-01, loaded on the first day as one version valid from its picking, would not exist in an "as of" query for
   January, although its order date is evidence that it did; and a retained stamp would date later, undated changes.
   Recommendation: (c). Option (a) is honest too but answers no question about when picking, delivery or settlement
   happened.
3. **The two sensor tables.** Neither has a description; `RecordedWhen`, `VehicleRegistration` and the sensor numbers
   are read from their names. Recommendation: proceed as proposed (hubs for cold-room sensor and vehicle, readings as
   events, `RecordedWhen` as business time), since the data agree with the reading in every row
   (`Warehouse/ColdRoomTemperatures/03_temporal.md#C5`) and nothing else depends on these tables
   (`Warehouse/VehicleTemperatures/29_position.md`: isolated).

## 7. Uncertainties carried, not put to anyone

No time zone is established for any date-and-time column (each table's `03_temporal.md#C4`), so a date-typed event
date and a date-and-time milestone cannot be ordered within a day with certainty, and nobody available can settle it.
Much of the source's version history was generated rather than recorded by live system-versioning (versions stamped at
the initial load on 2013-01-01 and in batches at 16:00: `Application/Cities/03_temporal.md#C4`,
`Purchasing/Suppliers/03_temporal.md#C5`); source system time therefore orders versions reliably within a key but is
not a clock to compare across tables. Whether `OrderID` is known outside the database stays open
(`Sales/Orders/06_keys.md#C7`) and, under Rule 1, changes nothing here.

## 8. What this note does not decide

Relationships, including the roles of customer and person, the backorder chain and the membership and scope structures
of section 4 (step B); satellites and their splits (step C, and `ARC-OP-37` item 1); the model-file format and loading
(`ARC-OP-29`, `ARC-OP-20`). The rules of 144 §3 it applies (`ARC-OP-37` item 2) remain unruled; this note shows them on
real tables, as handover 10 suggested for judging them.

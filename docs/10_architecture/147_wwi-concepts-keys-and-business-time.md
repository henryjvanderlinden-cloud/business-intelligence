# 147 — Wide World Importers: business concepts, business keys and business time (step A)

> **STATUS: PROPOSED, not ruled.** Drafted 2026-10-26 in session 10 from handover 10. Unreviewed on another model
> ([510](../50_process/510_external-review.md)). Open under [`ARC-OP-37`](../../registers/OPEN_POINTS.md).

## 1. What this note does

Handover 10 set step A of the author's route of 2026-10-21: for all 31 base tables of Wide World Importers (WWI),
which business concepts become hubs, on which business key, with each key's issuer or namespace and grain
([144](144_raw-vault-business-vault-calculation-engines.md) §3 item 2), and which tables yield no hub. With it goes the
per-table proposal owed under [ADR-0027](../20_decisions/0027-bitemporal-integration-layer.md) decision 4: which
column, if any, carries business valid time, which carries source system time, and where valid time is unknown.

Every choice cites the analysis claim it rests on. Paths in citations are relative to `analysis/wwi/tables/` unless
they begin with `across/`, which is `analysis/wwi/across/`. Where no claim supports a choice, the note says so.
Relationships (step B), satellites (step C), loading and the model-file format are out of scope.

Three facts were missing from the record and were added to it before this note was written, under ADR-0022 decision
4, in step S10-003: for each of the 16 system-versioned base tables, which columns differ between the versions of one
key (`<table>/06_keys.md#C5`); and whether the country and state-province codes conform to the published ISO lists
(`Application/Countries/06_keys.md#C6`, `Application/StateProvinces/06_keys.md#C6`).

## 2. Three rules applied throughout

**Rule 1: the key is the source's own identifier, qualified by the key space `wwi`, unless the record shows a governed
namespace.** Every table's declared primary key is described by the source as a "Numeric ID used for reference to … within
the database" (for example `Sales/Orders/06_keys.md#C1`; the same wording in `columns/<key>/02_meaning.md#C1` of each table),
and it is the identifier every other table refers to (the foreign-key claims in each `06_keys.md`). The declared-unique
names are not used as keys, although many tables declare them unique, for one reason the record now shows: names are
renamed while the identifier stays. Of the 16 system-versioned base tables, eight hold a key whose declared-unique
name changed between versions (`Application/Countries/06_keys.md#C5`, `Application/DeliveryMethods/06_keys.md#C5`,
`Application/PaymentMethods/06_keys.md#C5`, `Application/TransactionTypes/06_keys.md#C5`,
`Purchasing/SupplierCategories/06_keys.md#C5`, `Sales/CustomerCategories/06_keys.md#C5`, `Warehouse/Colors/06_keys.md#C5`,
`Warehouse/StockGroups/06_keys.md#C5`); in the data, Turkey became Türkiye and Gray became Steel Gray. A key built
on a name would have split one thing into two at each rename. Names stay as descriptive attributes.

The key-space code `wwi` names the issuer, the WWI application database, as 144 §3 item 2 requires for keys issued
independently; 144 §5 already proposed it for this sandbox. Whether an identifier is also known outside the database,
open for `OrderID` (`Sales/Orders/06_keys.md#C7`), does not change this: being shown on a document does not make a
namespace governed, so the code stays either way. The only governed namespaces the record shows are the ISO codes of
countries and of US states (section 3, items 1 and 2).

**Rule 2: a hub is a concept the business identifies, refers to and that has a life of its own. A code list that only
classifies is a reference table.** Reference tables are keyed the same way as hubs (Rule 1) and keep their history
from the source's history tables, but get no hub; the tables that use them carry the code. This applies to the nine
lookups of section 4. The classes of [131](131_structural-position.md) (`29_position.md` of each table) are cited as a
description and were not used as the mapping, as handover 10 requires.

**Rule 3: a line is not a hub.** An order line, an invoice line and a purchase-order line are identified only within
their header (the source's own descriptions: "a line on an Order within the database",
`Sales/OrderLines/columns/OrderLineID/02_meaning.md#C1`). They become relationships between header and stock item in
step B, with the declared line identifier as the dependent-child key, because the shorter candidate (header, stock item)
is observed unique but not declared (`Sales/OrderLines/06_keys.md#C3`, `Sales/InvoiceLines/06_keys.md#C3`,
`Purchasing/PurchaseOrderLines/06_keys.md#C3`), and a key that rests only on an observation would collapse two lines for
the same item the first time the source allows them.

## 3. The hubs proposed: sixteen tables, sixteen concepts

Grain is one row of the hub per instance named. "Key space" is the issuer code of 144 §3; "ISO" means a governed
namespace and no key-space code.

| # | Concept | Source table | Business key | Key space | Grain | Evidence |
|---|---|---|---|---|---|---|
| 1 | country | Application.Countries | `IsoAlpha3Code` | ISO 3166-1 | one country | `Application/Countries/06_keys.md#C6`, `#C5` (code never changed, name changed once), `columns/IsoAlpha3Code/02_meaning.md#C1`, `#C3` |
| 2 | state or province | Application.StateProvinces | country's `IsoAlpha3Code` + `StateProvinceCode` | ISO 3166-2 | one subdivision | `Application/StateProvinces/06_keys.md#C6`, `#C5`, `#C4`; `columns/StateProvinceCode/02_meaning.md#C1`; all 53 in one country: `across/entities/location/26_entities.md#C1` |
| 3 | city | Application.Cities | `CityID` | `wwi` | one city | `Application/Cities/06_keys.md#C1`, `#C3` (name not a key, nor name within state), `#C5` |
| 4 | person | Application.People | `PersonID` | `wwi` | one person: staff, customer or supplier contact, technical user | `Application/People/06_keys.md#C1`, `#C4`, `#C5`; `columns/LogonName/02_meaning.md#C4`; `across/entities/person/26_entities.md#C1` |
| 5 | customer | Sales.Customers | `CustomerID` | `wwi` | one customer account: head office, branch or individual | `Sales/Customers/06_keys.md#C1`, `#C2`, `#C5`; `Sales/Customers/01_granularity.md`; `across/entities/customer/26_entities.md#C1` |
| 6 | supplier | Purchasing.Suppliers | `SupplierID` | `wwi` | one supplier organisation | `Purchasing/Suppliers/06_keys.md#C1`, `#C4`, `#C5`; `columns/SupplierReference/02_meaning.md#C1` |
| 7 | stock item | Warehouse.StockItems | `StockItemID` | `wwi` | one product | `Warehouse/StockItems/06_keys.md#C2`, `#C4`, `#C5`; `columns/Barcode/02_meaning.md#C3` |
| 8 | special deal | Sales.SpecialDeals | `SpecialDealID` | `wwi` | one pricing agreement | `Sales/SpecialDeals/06_keys.md#C1`, `#C3`; `Sales/SpecialDeals/03_temporal.md#C5` |
| 9 | sales order (fulfilment order) | Sales.Orders | `OrderID` | `wwi` | one order as WWI fulfils it: an original or a backorder | `Sales/Orders/06_keys.md#C1`, `#C2`, `#C4`, `#C7`; `across/terms/order/25_terms.md#C1` |
| 10 | invoice | Sales.Invoices | `InvoiceID` | `wwi` | one invoice | `Sales/Invoices/01_granularity.md#C1`, `#C2`, `#C4` |
| 11 | purchase order | Purchasing.PurchaseOrders | `PurchaseOrderID` | `wwi` | one order to a supplier | `Purchasing/PurchaseOrders/06_keys.md#C1`, `#C3`; `columns/SupplierReference/02_meaning.md#C4` |
| 12 | customer ledger entry | Sales.CustomerTransactions | `CustomerTransactionID` | `wwi` | one invoice or payment entry | `Sales/CustomerTransactions/06_keys.md#C1`, `#C3`; `Sales/CustomerTransactions/03_temporal.md#C5` |
| 13 | supplier ledger entry | Purchasing.SupplierTransactions | `SupplierTransactionID` | `wwi` | one supplier invoice or payment | `Purchasing/SupplierTransactions/06_keys.md#C1`, `#C3` |
| 14 | stock movement | Warehouse.StockItemTransactions | `StockItemTransactionID` | `wwi` | one issue, receipt or adjustment | `Warehouse/StockItemTransactions/06_keys.md#C1`, `#C3`; `across/terms/transaction/25_terms.md#C3` |
| 15 | cold-room sensor | Warehouse.ColdRoomTemperatures | `ColdRoomSensorNumber` | `wwi` | one sensor | `Warehouse/ColdRoomTemperatures/06_keys.md#C2`; `03_temporal.md#C5`, `#C6`; `columns/ColdRoomSensorNumber/02_meaning.md#C1`, `#C4` |
| 16 | vehicle | Warehouse.VehicleTemperatures | `VehicleRegistration` | `wwi` | one delivery vehicle | `Warehouse/VehicleTemperatures/06_keys.md#C2`; `columns/VehicleRegistration/02_meaning.md#C1`, `#C3`, `#C4` |

Notes on single rows, where the table does not say enough:

*Country and state or province (1, 2).* These are the only keys proposed without the code `wwi`. All 190 countries
carry an ISO 3166-1 code pair from the published list, and all 53 state codes are ISO 3166-2:US subdivision codes; the
source itself describes the country code as "assigned to the country by ISO", and no code changed in the history held.
The evidence is medium, not high, because the reference lists were read through a summarising fetch. ISO's own
subdivision code is written with the country's two-letter code (`US-WA`); the source holds only the three-letter code,
so the composition proposed is the three-letter code with the state code. Because other tables refer to countries and
states by `CountryID` and `StateProvinceID`, loading their relationships needs a deterministic resolution of those
identifiers to the ISO codes. This is the first weak case of section 6.

*Person (4).* One hub for every kind of person, since the source holds them in one table under one identifier
(`across/entities/person/26_entities.md#C1`); staff, contact and salesperson are roles, carried by relationships and
flags. The banding of `PersonID` by kind of person (`Application/People/06_keys.md#C3`, low) is not used. Every table's
`LastEditedBy` refers to this hub for no business reason (ADR-0021's distortion principle); it is audit data and becomes
no business relationship in step B.

*Customer (5).* The delivered-to customer, the billed customer and the head office are roles of one concept, not three
concepts (`across/terms/customer/25_terms.md#C1` to `#C3`); they become relationships in step B. `CustomerName` is
declared unique and never changed in the history held (`Sales/Customers/06_keys.md#C1`, `#C5`), but Rule 1 applies.

*Supplier (6).* `SupplierReference` is WWI's account at the supplier, issued by the supplier and identifying WWI
(`Purchasing/Suppliers/columns/SupplierReference/02_meaning.md#C1`); it is not a key of the supplier.

*Stock item (7).* `Barcode` is filled for 8 of 227 items; whether the barcodes are GS1 identifiers is not established
(no claim exists), so it is an attribute.

*Special deal (8).* Proposed as a hub because a deal is an agreement with its own identity and its own validity period
(`Sales/SpecialDeals/03_temporal.md#C5`), not a classification. No table refers to it, and whether invoice prices
were derived from a deal is not established; if step B finds nothing that relates to it, it could as well be a
reference table. Two rows make the choice cheap either way.

*Sales order (9).* The hub is the fulfilment order, the row of `Sales.Orders`. The customer order as placed, an
original with its chain of backorders (`Sales/Orders/27_peculiarities.md#C12`, `#C4`), has no key in the source: the
customer's purchase-order number is shared across customers and cannot stand for it (`Sales/Orders/06_keys.md#C4`).
It is therefore not a raw-vault hub. It would be a business-vault concept derived from the backorder links, keyed by
the original order's `OrderID` (the link's direction: `Sales/Orders/columns/BackorderOrderID/02_meaning.md#C2`).

*Invoice (10).* `OrderID` identifies the invoice too in this extract, but no constraint enforces one invoice per order
(`Sales/Invoices/01_granularity.md#C4`), so it is a relationship, not a key.

*The three ledgers (12 to 14).* The three identifiers share one numbering and never overlap
(`Sales/CustomerTransactions/06_keys.md#C3`; `across/terms/transaction/25_terms.md#C1`, `#C2`), but they denote three
different things, two of money and one of goods (`#C3`), so they are three hubs; since they do not overlap, a single
key space `wwi` serves all three without collision. They are hubs rather than event-only links because the two money
ledgers are updated in place on settlement (`Sales/CustomerTransactions/03_temporal.md#C5`), so their state needs a
satellite; the stock ledger is append-only as observed (`Warehouse/StockItemTransactions/03_temporal.md#C5`) and is a
hub for uniformity, a choice step B may revisit.

*Sensors (15, 16).* `ColdRoomTemperatureID` identifies a reading and is renewed with every one; the sensor number is
what persists (`Warehouse/ColdRoomTemperatures/06_keys.md#C2`), consistent over 3.7 million readings in the history
table (`03_temporal.md#C5`). For vehicles, the natural key of a reading is (vehicle registration, chiller sensor number,
recorded time) (`Warehouse/VehicleTemperatures/06_keys.md#C2`); the vehicle is the concept with identity, a chiller
sensor is identified only within its vehicle, and the readings are events attached to the sensors in step B and C, not
hubs. Neither table has any column description: the readings of `VehicleRegistration` and `RecordedWhen` rest on
column names (`columns/VehicleRegistration/02_meaning.md#C4`, `columns/RecordedWhen/02_meaning.md#C4`, both low). A
registration plate is issued by a licensing authority, but no jurisdiction is in the data, so the code `wwi` stays. This
is the third weak case of section 6.

## 4. The fifteen tables that yield no hub

| Table | What it becomes | Evidence |
|---|---|---|
| Application.DeliveryMethods | reference table on `DeliveryMethodID` (`wwi`) | `Application/DeliveryMethods/06_keys.md#C2`, `#C5` (renamed) |
| Application.PaymentMethods | reference table on `PaymentMethodID` (`wwi`) | `Application/PaymentMethods/06_keys.md#C2`, `#C5` (renamed) |
| Application.TransactionTypes | reference table on `TransactionTypeID` (`wwi`) | `Application/TransactionTypes/06_keys.md#C2`, `#C5` (renamed) |
| Purchasing.SupplierCategories | reference table on `SupplierCategoryID` (`wwi`) | `Purchasing/SupplierCategories/06_keys.md#C2`, `#C5` (renamed) |
| Sales.CustomerCategories | reference table on `CustomerCategoryID` (`wwi`) | `Sales/CustomerCategories/06_keys.md#C2`, `#C5` (renamed) |
| Sales.BuyingGroups | reference table on `BuyingGroupID` (`wwi`) | `Sales/BuyingGroups/06_keys.md#C2`, `#C5` |
| Warehouse.Colors | reference table on `ColorID` (`wwi`) | `Warehouse/Colors/06_keys.md#C2`, `#C5` (renamed) |
| Warehouse.PackageTypes | reference table on `PackageTypeID` (`wwi`) | `Warehouse/PackageTypes/06_keys.md#C2`, `#C5` |
| Warehouse.StockGroups | reference table on `StockGroupID` (`wwi`) | `Warehouse/StockGroups/06_keys.md#C2`, `#C5` (renamed) |
| Sales.OrderLines | relationship order to stock item, dependent child `OrderLineID` (Rule 3) | `Sales/OrderLines/06_keys.md#C1`, `#C3` |
| Sales.InvoiceLines | relationship invoice to stock item, dependent child `InvoiceLineID` (Rule 3) | `Sales/InvoiceLines/06_keys.md#C1`, `#C3` |
| Purchasing.PurchaseOrderLines | relationship purchase order to stock item, dependent child `PurchaseOrderLineID` (Rule 3) | `Purchasing/PurchaseOrderLines/06_keys.md#C1`, `#C3` |
| Warehouse.StockItemHoldings | descriptive data of the stock item, sampled | `Warehouse/StockItemHoldings/06_keys.md#C3`; `across/entities/stock-item/26_entities.md#C1` |
| Warehouse.StockItemStockGroups | membership of a stock item in a stock group; `StockItemStockGroupID` is a surrogate | `Warehouse/StockItemStockGroups/06_keys.md#C1`, `#C4` |
| Application.SystemParameters | configuration: WWI's own addresses and settings, one row | `Application/SystemParameters/06_keys.md#C3`; `01_granularity.md` |

The 17 history tables (`*_Archive`) yield nothing of their own: each holds the earlier versions of its base table
(for example `Sales/Customers_Archive/05_role.md#C5`) and is loaded as that table's history on the first day, ordered
by source system time (ADR-0027 decision 2).

Two of the reference tables are used beyond classifying one other table: stock groups are linked to stock items many
to many through the bridge, and stock groups, buying groups and customer categories define the scope of a special deal
(`Sales/SpecialDeals/06_keys.md#C2`). Under Rule 2 that does not make them hubs; the membership and the scope become
structures in steps B and C that carry the reference code. If the author prefers a hub wherever a relationship
involves a lookup, stock group, buying group and customer category would become hubs; nothing in the record forces
either reading.

## 5. Business time per table

The three clocks of ADR-0027: business valid time (when it was true in the business), source system time (when the
source recorded it; stored and labelled, never presented as business time), and knowledge time (our load time, not
listed). "Unknown" means the satellites of that table carry valid time as explicitly unknown (ADR-0027 decision 1).
A milestone is a business time written back onto an existing row later, in place; how milestones enter valid time is
the second weak case of section 6.

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
| Purchasing.PurchaseOrderLines | none of its own | `LastReceiptDate` (latest receipt only); finalisation has no date | header's `OrderDate` through the relationship | `LastEditedWhen` | `Purchasing/PurchaseOrderLines/03_temporal.md#C2`, `#C5`; `columns/LastReceiptDate/02_meaning.md#C1` |
| Purchasing.PurchaseOrders | `OrderDate` | finalisation has no date | `ExpectedDeliveryDate` (planned) | `LastEditedWhen` | `Purchasing/PurchaseOrders/03_temporal.md#C3`, `#C5`, `#C6`; `columns/OrderDate/02_meaning.md#C1` |
| Purchasing.SupplierCategories | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Purchasing.SupplierTransactions | `TransactionDate` | `FinalizationDate` | — | `LastEditedWhen` | `Purchasing/SupplierTransactions/03_temporal.md#C3`, `#C6`; `columns/TransactionDate/02_meaning.md#C1` |
| Purchasing.Suppliers | unknown | — | — | `ValidFrom`, `ValidTo` | `Purchasing/Suppliers/03_temporal.md#C4`, `#C5` |
| Sales.BuyingGroups | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Sales.CustomerCategories | unknown | — | — | `ValidFrom`, `ValidTo` | `03_temporal.md#C3` |
| Sales.CustomerTransactions | `TransactionDate` | `FinalizationDate` | — | `LastEditedWhen` | `Sales/CustomerTransactions/03_temporal.md#C3`, `#C5`, `#C6` |
| Sales.Customers | unknown | — | `AccountOpenedDate` (start of the account) | `ValidFrom`, `ValidTo` | `Sales/Customers/03_temporal.md#C3`, `#C4`; `columns/AccountOpenedDate/02_meaning.md#C1` |
| Sales.InvoiceLines | none of its own | — | header's `InvoiceDate` through the relationship | `LastEditedWhen` | `Sales/InvoiceLines/03_temporal.md#C3`, `#C5` |
| Sales.Invoices | `InvoiceDate` | `ConfirmedDeliveryTime` | — | `LastEditedWhen` | `Sales/Invoices/03_temporal.md#C3`, `#C5`, `#C6`; `columns/InvoiceDate/02_meaning.md#C1` |
| Sales.OrderLines | none of its own | `PickingCompletedWhen` | header's `OrderDate` through the relationship | `LastEditedWhen` | `Sales/OrderLines/03_temporal.md#C3`, `#C5` |
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
source system time. The event tables carry the date of the event, the documents' own dates, and four of them carry
milestones. The line tables carry no date of their own; their header's date is reached through the relationship in
the business vault, because looking it up during loading would be interpretation in the raw vault (144 §2).

`AccountOpenedDate` is a business date, but of the customer's existence, not of the version: it does not say when a
customer's current credit limit became true, which is what the versions record
(`Sales/Customers/03_temporal.md#C4`; `Sales/Customers/06_keys.md#C5` shows that `CreditLimit` is the only business column that ever changed). The
deals are the one source with a business validity period of their own, which ADR-0027's insert-only rule keeps as
data: `StartDate` is stored as valid time, `EndDate` as the source's stated end.

## 6. Weak cases for the author

Three cases, each with a recommendation. Everything else in this note rests on claims of high or medium confidence
and is proposed for ruling as a whole once reviewed.

1. **Keys from ISO for country and state or province (section 3, items 1 and 2).** The evidence is that every code
   conforms to the ISO lists (medium: lists read second-hand), the source's own description of the country code, and
   codes that never changed. Against it: the source refers to countries and states by its own identifiers, so every
   relationship to them needs a deterministic lookup when loaded, and a later non-ISO row would have no key.
   Recommendation: ISO keys for both, as proposed, because they are the only identifiers here that a second source
   could share without matching.
2. **How milestones enter valid time.** `PickingCompletedWhen` (orders and order lines), `ConfirmedDeliveryTime`
   (invoices), `FinalizationDate` (both money ledgers) and `LastReceiptDate` (purchase-order lines) are business times
   written back later, in place, and seen only as the sampled states of daily extracts (`Sales/Orders/03_temporal.md#C7`,
   `Sales/Invoices/03_temporal.md#C5`, `Sales/CustomerTransactions/03_temporal.md#C5`). Two changes carry no date at
   all: finalising a purchase order and a purchase-order line. The options: (a) valid time of every version is the
   event date, and milestone stamps are plain attributes; (b) a version's valid time is the latest milestone stamp it
   shows, or the event date if it shows none, and a change with no date gets unknown valid time; (c) each milestone
   gets a structure of its own in step C. Recommendation: (b), because it states for each version the moment the
   source says it became true, which is what ADR-0027 asks; on the first day a row already past its milestone loads
   as one version, valid from its milestone, and its earlier state is not invented.
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

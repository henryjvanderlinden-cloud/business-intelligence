# 149 — Wide World Importers: the satellites (step C)

> **STATUS: RULED** 2026-10-29 in [ADR-0033](../20_decisions/0033-wwi-step-c-satellites.md). Drafted 2026-10-29 in session 10, after steps A and B were ruled
> ([ADR-0029](../20_decisions/0029-wwi-step-a-concepts-and-keys.md), [ADR-0031](../20_decisions/0031-wwi-step-b-links.md)).
> Reviewed on sol, which failed the first version ([XREV](../30_research/notes/XREV_2026-10-29_149-satellites_sol.md));
> this is the revised text, itself unreviewed ([510](../50_process/510_external-review.md)). Open under
> [`ARC-OP-37`](../../registers/OPEN_POINTS.md) item 1.

## 1. What this note does

Step C of the route of 2026-10-21: how the descriptive columns of the 31 base tables of Wide World Importers are held,
in satellites on the twenty-two hubs of [147](147_wwi-concepts-keys-and-business-time.md) and the forty-nine links of
[148](148_wwi-relationships.md), in reference tables, and in the structures that steps A and B left owed: an effectivity
satellite per link (ADR-0031), the optional relationship columns kept as delivered (148 Rule 4), and the milestone
satellites of [ADR-0028](../20_decisions/0028-wwi-country-key-milestones-and-sensors.md). For every satellite it states
its columns, why it is split from its neighbours, where its business valid time comes from, and a proposed sensitivity
class.

Citations follow 147: paths relative to `analysis/wwi/tables/`, or beginning with `across/` or `analysis/`. In the
tables, "versions" means the table's `06_keys.md#C5` (which columns ever differ between the versions of one key, in the
history held) and "transition" its `03_temporal.md#C2` (which columns were updated between two extracts).

## 2. Ten rules applied throughout

**Rule 1: a satellite holds what one source row asserts about one hub or link, and splits only for a stated reason**
(144 §2). The reasons used here are five: *audit* (who and when the source recorded a change, Rule 3), *sensitivity*
(columns whose access must differ), *rate of change* (columns that change where the rest never does), *milestone* (a
fact with its own business time, ADR-0028), and *delivery* (another source table, or a reading series). Every satellite
filled from one source row carries the same load time and batch (144 §2; ADR-0031 decision 2). Satellites are named
`sat_<hub or link>__wwi[__<part>]`, the source code in the name from the first load (144 §5).

**Rule 2: every satellite row carries the three clocks of ADR-0027 and a source-version identifier as metadata, not as
payload.** Knowledge time (load time and batch), business valid time (from the column 147 §5 and this note name, or
explicitly unknown), and source system time (`ValidFrom` of a system-versioned table, `LastEditedWhen` of the others),
labelled and never presented as business time. The *source version* is the record source with the source system time
of the row it came from: it identifies one version of one source row, it is the same in every satellite filled from
that version, and it is part of every satellite row's key, with the parent key and the load time. Review showed why
it is needed ([XREV](../30_research/notes/XREV_2026-10-29_149-satellites_sol.md) findings 1, 2 and 5): without it, the
versions of the first day's history all share one load time and collide, and satellites split from one row cannot be
put back together as the source held them. The source moves `LastEditedWhen` on every update seen in both transitions
(`Sales/Orders/03_temporal.md#C2`; `Sales/Invoices/03_temporal.md#C2`; `Warehouse/StockItemHoldings/03_temporal.md#C2`),
so it serves as the version stamp of the tables that are not system-versioned. A table with neither, such as the
vehicle readings, is append-only and its rows are identified by their own key (Rule 10).

**Rule 3: the audit columns go into an audit satellite of their own on every hub, which is the source's version log.**
`LastEditedBy` names a person on every table for no business reason (ADR-0021) and changes with every edit, as does
source system time. The audit satellite holds `LastEditedBy` with the source system time, and its change detection
includes both, so that every version the source recorded is one row there. The payload satellites detect change on
their payload and business valid time only (ADR-0027, Consequences), so that an edit that changed nothing visible, such
as the person versioned on 2016-06-01 without any column changing (`Application/People/03_temporal.md#C4`), adds a row
to the audit satellite and none to the others. A satellite therefore holds a row per source version in which its own
columns changed, not one per source version; "which versions did the source record" is answered by the audit
satellite, and "what did the source hold at instant *t*" by the point-in-time rule of Rule 10.

**Rule 4: a source-computed column stays where the source puts it.** Eight columns are declared computed by the source
(claim C2 of each such column's own `columns/<column>/02_meaning.md`, for example `Application/People/columns/SearchName/02_meaning.md#C2`); they are what
the system said and load as delivered (144 §2, provenance), next to the columns they are computed from.

**Rule 5: optional relationship columns are kept as delivered in the naming hub's main satellite** (148 Rule 4), as the
source's business key of the named row or empty. Mandatory relationship columns are carried by links only.

**Rule 6: every link gets an effectivity satellite** (ADR-0031 decision 3), `eff_<link>__wwi`, keyed on the link and
recording, per driving key, from when the link is the current one and when it was ended; its business start comes from
148's column *Effectivity* (load, event date, milestone, or absence in a complete extract).

**Rule 7: every hub loaded from a full extract gets a status-tracking satellite**, `sts_<hub>__wwi`, with a row for every
change of a key's status between complete extracts: *present*, *absent-unresolved* (missing from a complete extract),
*deletion-confirmed* (once the conditions of 127, "Absence is not deletion", are met), and *reappeared*. A confirmed
deletion is a new row; the absence that preceded it is kept. A "current" query takes, per key, the latest status at or
before its knowledge time, so a key absent on day 2 is not current on day 3 even if it was present on day 1, and a key
that returns is the same key, marked reappeared ([XREV](../30_research/notes/XREV_2026-10-29_149-satellites_sol.md)
finding 4). The extracts are full, with a manifest of row counts and hashes
(`prototypes/wwi_sandbox/README.md`), which is the evidence of completeness 127 asks for.

**Rule 8: a code list without a hub is a reference table with its history**, `ref_<table>__wwi`, holding every version
the source holds, with source system time; it is small and changes rarely, so its audit column stays in it.

**Rule 9: each satellite has a proposed sensitivity class**: *open* (public reference data), *internal* (ordinary
business data), *confidential* (commercial terms, prices, costs, margins), *personal* (data about identifiable people),
*restricted* (credentials, bank details, employment terms, position tracks). These are readings, not legal advice,
following each table's `19_sensitivity.md`; access rules per class are not decided here, and regulatory requirements
apply from production on ([ADR-0016](../20_decisions/0016-regulatory-requirements-from-production.md)).

**Rule 10: reconstruction is by source version, and readings are events.** The state of a hub as the source held it at
source system time *t* is, per satellite, the row with the latest source version at or before *t*; because every
satellite of one row shares that version, the parts of a split row recombine into a state the source actually held,
never into a mix of two versions. For business "as of" queries the same rule runs on business valid time where a
satellite has one, and on knowledge time for "as we knew it". A reading series is not the changing description of a
sensor or vehicle but a stream of immutable events, several per day for the same sensor: each reading is a row of its
own, keyed by its own identifier, inserted once and never superseded (finding 3).

## 3. Satellites on the hubs

Every hub also has its audit satellite (Rule 3) and its status-tracking satellite (Rule 7); they are not repeated in the
tables. Valid time "unknown" is ADR-0027's explicit unknown.

### 3.1 Geography

| Satellite | Columns | Split reason | Valid time | Class | Evidence |
|---|---|---|---|---|---|
| `sat_country__wwi` | CountryID, CountryName, FormalName, IsoNumericCode, CountryType, Continent, Region, Subregion | — | unknown | open | `Application/Countries/06_keys.md#C5` |
| `sat_country__wwi__population` | LatestRecordedPopulation | rate of change (35 of 190 changed) | unknown | open | `Application/Countries/06_keys.md#C5` |
| `sat_country__wwi__border` | Border | delivery (a large geography value) | unknown | open | `Application/Countries/06_keys.md#C5` |
| `sat_state_province__wwi` | StateProvinceCode, StateProvinceName, SalesTerritory | — | unknown | open | `Application/StateProvinces/06_keys.md#C5` |
| `sat_state_province__wwi__population` | LatestRecordedPopulation | rate of change (34 of 53) | unknown | open | `Application/StateProvinces/06_keys.md#C5` |
| `sat_state_province__wwi__border` | Border | rate of change (52 of 53) and size | unknown | open | `Application/StateProvinces/06_keys.md#C5` |
| `sat_city__wwi` | CityName, Location | — | unknown | open | `Application/Cities/06_keys.md#C5` |
| `sat_city__wwi__population` | LatestRecordedPopulation | rate of change (the only column that changed) | unknown | open | `Application/Cities/06_keys.md#C5` |

`CountryID` stays in the country's satellite because the hub is keyed on the ISO code (ADR-0028) and other tables refer
to the source's identifier.

### 3.2 Parties

| Satellite | Columns | Split reason | Valid time | Class | Evidence |
|---|---|---|---|---|---|
| `sat_person__wwi` | FullName, PreferredName, SearchName (computed), PhoneNumber, FaxNumber, EmailAddress, Photo | — | unknown | personal | `Application/People/19_sensitivity.md#C1`, `#C3`; `06_keys.md#C5` (never changed) |
| `sat_person__wwi__roles` | IsEmployee, IsSalesperson, IsSystemUser | sensitivity (internal, unlike the rest) | unknown | internal | `Application/People/07_population.md#C6` |
| `sat_person__wwi__account` | IsPermittedToLogon, LogonName, IsExternalLogonProvider, HashedPassword, UserPreferences | sensitivity and rate of change (138 to 182 people changed) | unknown | restricted | `Application/People/06_keys.md#C5`; `19_sensitivity.md#C3`, `#C5`, `#C6` |
| `sat_person__wwi__employment` | CustomFields, OtherLanguages (computed) | sensitivity (employment terms, commission) | unknown | restricted | `Application/People/19_sensitivity.md#C4`, `#C6` |
| `sat_customer__wwi` | CustomerName, AccountOpenedDate, DeliveryMethodID (code), DeliveryRun, RunPosition, BuyingGroupID and AlternateContactPersonID as delivered | — | unknown | internal; personal where the customer is an individual | `Sales/Customers/06_keys.md#C5`; `19_sensitivity.md#C4`, `#C6` |
| `sat_customer__wwi__credit` | CreditLimit, StandardDiscountPercentage, IsStatementSent, IsOnCreditHold, PaymentDays | rate of change (CreditLimit, 46 customers) and sensitivity | unknown | confidential | `Sales/Customers/06_keys.md#C5` |
| `sat_customer__wwi__address` | PhoneNumber, FaxNumber, WebsiteURL, DeliveryAddressLine1, DeliveryAddressLine2, DeliveryPostalCode, DeliveryLocation, PostalAddressLine1, PostalAddressLine2, PostalPostalCode | sensitivity | unknown | personal where the customer is an individual | `Sales/Customers/19_sensitivity.md#C1`, `#C4` |
| `sat_customer_category__wwi` | CustomerCategoryName | — | unknown | open | `Sales/CustomerCategories/06_keys.md#C5` |
| `sat_buying_group__wwi` | BuyingGroupName | — | unknown | internal | `Sales/BuyingGroups/06_keys.md#C5` |
| `sat_supplier__wwi` | SupplierName, SupplierCategoryID and DeliveryMethodID (codes), SupplierReference, PaymentDays | — | unknown | internal | `Purchasing/Suppliers/06_keys.md#C5` |
| `sat_supplier__wwi__address` | PhoneNumber, FaxNumber, WebsiteURL, DeliveryAddressLine1, DeliveryAddressLine2, DeliveryPostalCode, DeliveryLocation, PostalAddressLine1, PostalAddressLine2, PostalPostalCode | rate of change (DeliveryLocation, all 13) | unknown | internal | `Purchasing/Suppliers/06_keys.md#C5` |
| `sat_supplier__wwi__bank` | BankAccountName, BankAccountBranch, BankAccountCode, BankAccountNumber, BankInternationalCode | sensitivity (masked by the source itself) | unknown | restricted | `Purchasing/Suppliers/19_sensitivity.md#C4`, `#C5` |
| `sat_supplier__wwi__internal` | InternalComments | sensitivity (remarks about named people) | unknown | personal | `Purchasing/Suppliers/19_sensitivity.md#C6` |

### 3.3 Products and deals

| Satellite | Columns | Split reason | Valid time | Class | Evidence |
|---|---|---|---|---|---|
| `sat_stock_item__wwi` | StockItemName, ColorID, UnitPackageID and OuterPackageID (codes), Brand, Size, LeadTimeDays, QuantityPerOuter, IsChillerStock, Barcode, TypicalWeightPerUnit, MarketingComments, InternalComments, Photo | — | unknown | internal | `Warehouse/StockItems/06_keys.md#C5`; `19_sensitivity.md#C3` |
| `sat_stock_item__wwi__price` | TaxRate, UnitPrice, RecommendedRetailPrice | sensitivity (prices) | unknown | confidential | `Warehouse/StockItems/09_derived.md`; `19_sensitivity.md` |
| `sat_stock_item__wwi__tags` | CustomFields, Tags (computed), SearchDetails (computed) | rate of change (every item, in one batch) | unknown | internal | `Warehouse/StockItems/06_keys.md#C5`; `03_temporal.md#C4` |
| `sat_stock_item__wwi__holding` | QuantityOnHand, BinLocation, LastStocktakeQuantity, LastCostPrice, ReorderLevel, TargetStockLevel | delivery (another table, overwritten daily, sampled) | none; sampled | confidential | `Warehouse/StockItemHoldings/03_temporal.md#C5`, `#C6`; `19_sensitivity.md#C3` |
| `sat_stock_group__wwi` | StockGroupName | — | unknown | open | `Warehouse/StockGroups/06_keys.md#C5` |
| `sat_special_deal__wwi` | DealDescription, StartDate, EndDate, DiscountAmount, DiscountPercentage, UnitPrice; CustomerID, BuyingGroupID, CustomerCategoryID, StockItemID, StockGroupID as delivered | — | `StartDate` | confidential | `Sales/SpecialDeals/03_temporal.md#C5`; `19_sensitivity.md` |

The holding satellite has its own audit columns from its own table; they go to the stock item's audit satellite with
the holding table named as record source, so that the item's version log and the holding's daily overwrite stay
distinguishable.

### 3.4 Sales

| Satellite | Columns | Split reason | Valid time | Class | Evidence |
|---|---|---|---|---|---|
| `sat_sales_order__wwi` | OrderDate, ExpectedDeliveryDate, CustomerPurchaseOrderNumber, IsUndersupplyBackordered, Comments, DeliveryInstructions, InternalComments; BackorderOrderID as delivered | — | `OrderDate` | internal | `Sales/Orders/03_temporal.md#C2`, `#C6` |
| `sat_sales_order__wwi__picking` | PickingCompletedWhen; PickedByPersonID as delivered | milestone (ADR-0028) | `PickingCompletedWhen` | internal | `Sales/Orders/03_temporal.md#C2`, `#C7` |
| `sat_sales_order_line__wwi` | Description, PackageTypeID (code), Quantity, UnitPrice, TaxRate | — | unknown (no own date) | confidential | `Sales/OrderLines/03_temporal.md#C3`; `19_sensitivity.md` |
| `sat_sales_order_line__wwi__picking` | PickedQuantity, PickingCompletedWhen | milestone (ADR-0028) | `PickingCompletedWhen` | internal | `Sales/OrderLines/03_temporal.md#C2`, `#C5` |
| `sat_invoice__wwi` | InvoiceDate, DeliveryMethodID (code), CustomerPurchaseOrderNumber, IsCreditNote, CreditNoteReason, Comments, DeliveryInstructions, InternalComments, TotalDryItems, TotalChillerItems, DeliveryRun, RunPosition; OrderID as delivered | — | `InvoiceDate` | internal; personal in the instructions where the customer is an individual | `Sales/Invoices/03_temporal.md#C3`; `19_sensitivity.md#C5`, `#C6` |
| `sat_invoice__wwi__delivery` | ReturnedDeliveryData, ConfirmedDeliveryTime (computed), ConfirmedReceivedBy (computed) | milestone (ADR-0028) and sensitivity | `ConfirmedDeliveryTime` | personal | `Sales/Invoices/03_temporal.md#C5`; `19_sensitivity.md#C4`, `#C7` |
| `sat_invoice_line__wwi` | Description, PackageTypeID (code), Quantity, UnitPrice, TaxRate, TaxAmount, LineProfit, ExtendedPrice | — | unknown (no own date) | confidential | `Sales/InvoiceLines/03_temporal.md#C5`; `19_sensitivity.md#C3`; `09_derived.md` |

### 3.5 Purchasing

| Satellite | Columns | Split reason | Valid time | Class | Evidence |
|---|---|---|---|---|---|
| `sat_purchase_order__wwi` | OrderDate, DeliveryMethodID (code), ExpectedDeliveryDate, SupplierReference, IsOrderFinalized, Comments, InternalComments | — | `OrderDate` for the order; unknown for the undated finalisation | internal | `Purchasing/PurchaseOrders/03_temporal.md#C2`, `#C5` |
| `sat_purchase_order_line__wwi` | OrderedOuters, Description, PackageTypeID (code), ExpectedUnitPricePerOuter, IsOrderLineFinalized | — | unknown (no own date; finalisation undated) | confidential | `Purchasing/PurchaseOrderLines/03_temporal.md#C2`; `09_derived.md` |
| `sat_purchase_order_line__wwi__receipt` | ReceivedOuters, LastReceiptDate | milestone (ADR-0028), latest receipt only | `LastReceiptDate` | internal | `Purchasing/PurchaseOrderLines/03_temporal.md#C5`; `analysis/wwi/_source/22_stability.md#C19` |

### 3.6 The ledgers

| Satellite | Columns | Split reason | Valid time | Class | Evidence |
|---|---|---|---|---|---|
| `sat_customer_ledger_entry__wwi` | TransactionTypeID and PaymentMethodID (codes), TransactionDate, AmountExcludingTax, TaxAmount, TransactionAmount; InvoiceID as delivered | — | `TransactionDate` | confidential | `Sales/CustomerTransactions/03_temporal.md#C3`; `09_derived.md` |
| `sat_customer_ledger_entry__wwi__finalisation` | OutstandingBalance, FinalizationDate, IsFinalized (computed) | milestone (ADR-0028) | `FinalizationDate` | confidential | `Sales/CustomerTransactions/03_temporal.md#C5`, `#C6` |
| `sat_supplier_ledger_entry__wwi` | TransactionTypeID and PaymentMethodID (codes), SupplierInvoiceNumber, TransactionDate, AmountExcludingTax, TaxAmount, TransactionAmount; PurchaseOrderID as delivered | — | `TransactionDate` | confidential | `Purchasing/SupplierTransactions/03_temporal.md#C3`; `09_derived.md` |
| `sat_supplier_ledger_entry__wwi__settlement` | OutstandingBalance, FinalizationDate, IsFinalized (computed) | rate of change (settled later, as on the customer side) | unknown: no write-back seen (ADR-0028, Consequences) | confidential | `Purchasing/SupplierTransactions/03_temporal.md#C5`, `#C6`; `analysis/wwi/_source/22_stability.md#C21` |
| `sat_stock_movement__wwi` | TransactionTypeID (code), TransactionOccurredWhen, Quantity; CustomerID, InvoiceID, SupplierID, PurchaseOrderID as delivered | — | `TransactionOccurredWhen` | internal | `Warehouse/StockItemTransactions/03_temporal.md#C3`, `#C5`; `09_derived.md` |

### 3.7 Sensors

| Satellite | Columns | Split reason | Valid time | Class | Evidence |
|---|---|---|---|---|---|
| `sat_cold_room_sensor__wwi__reading` | ColdRoomTemperatureID (reading key), RecordedWhen, Temperature | delivery (a reading series: one row per reading, Rule 10) | `RecordedWhen` | open | `Warehouse/ColdRoomTemperatures/06_keys.md#C1`, `#C2`; `03_temporal.md#C5`, `#C6` |
| `sat_vehicle__wwi__chiller_reading` | VehicleTemperatureID (reading key), ChillerSensorNumber, RecordedWhen, Temperature, IsCompressed | delivery (a reading series: one row per reading, Rule 10) | `RecordedWhen` | internal | `Warehouse/VehicleTemperatures/06_keys.md#C1`, `#C2`; `03_temporal.md#C5` |
| `sat_vehicle__wwi__position` | VehicleTemperatureID (reading key), RecordedWhen, FullSensorData, CompressedSensorData | sensitivity (position history that can track a driver) | `RecordedWhen` | restricted | `Warehouse/VehicleTemperatures/19_sensitivity.md#C2`, `#C3` |

The reading satellites are keyed by the hub and the reading's own identifier, which is unique and gapless for the
vehicle readings and runs without a gap across the cold-room history and current rows
(`Warehouse/VehicleTemperatures/06_keys.md#C1`; `Warehouse/ColdRoomTemperatures/03_temporal.md#C5`); a day's extract
brings many readings per sensor, and none replaces another. The cold-room readings of the history table, 3.7 million
rows from 2015-12-20, load on the first day as the reading series of the four sensors, ordered by `RecordedWhen`, which equals their source system time in every row
(`Warehouse/ColdRoomTemperatures/03_temporal.md#C5`). The sensor tables have no audit columns, so their audit
satellites hold source system time only (`ValidFrom` for the cold room, none for the vehicle).

## 4. Links, reference tables and configuration

**Effectivity.** Forty-nine effectivity satellites, one per link of 148 §3, with the business start named in its column
*Effectivity*: from the load where the source gives none (links 1 to 14 and 16 to 20), from the naming event's date
(links 21 to 23 and 25 to 49), from `PickingCompletedWhen` for the picker (link 24), and from presence in a complete
extract for the stock-group membership (link 15), whose end is an absence resolved under 127 because an ended
membership leaves no trace in the source (`Warehouse/StockItemStockGroups/03_temporal.md#C5`).

**Link satellites.** None. No link in 148 carries descriptive columns of its own: the bridge's only other column is its
surrogate (`Warehouse/StockItemStockGroups/06_keys.md#C1`), kept in the effectivity satellite as delivered.

**Reference tables (Rule 8).** `ref_delivery_method__wwi`, `ref_payment_method__wwi`, `ref_transaction_type__wwi`,
`ref_supplier_category__wwi`, `ref_color__wwi`, `ref_package_type__wwi`, each holding the code, the name and
`LastEditedBy` per version, from the source's history tables (`06_keys.md#C5` of each, for the renames).

**Configuration.** `ref_system_parameters__wwi` holds the one row of `Application.SystemParameters` with its history
as delivered: WWI's own addresses, its two city codes and `ApplicationSettings`
(`Application/SystemParameters/06_keys.md#C3`; `19_sensitivity.md`).

## 5. Loading the first day and every day after

On the first day each system-versioned table loads its history table and its current rows together, in the order of
source system time, so that each recorded version becomes a row of the audit satellite and, where its payload
changed, of the payload satellites; all carry the first load's knowledge time and their own source version (Rule 2),
which keeps them apart although they share one load time (ADR-0027 decision 2). The history table holds only earlier
versions and never the current one (for example `Sales/Customers_Archive/05_role.md#C5`), so the two do not overlap;
the load nevertheless removes any duplicate source version before inserting, so that a boundary row delivered twice
is loaded once. The tables without history load their current state once. From the second day, each complete
extract loads as one batch (ADR-0031 decision 2). The engines' results (ADR-0024, ADR-0025) are a source of their own
and get satellites when the first engine is designed.

## 6. Weak case for the author

*Ruled 2026-10-29 in [ADR-0033](../20_decisions/0033-wwi-step-c-satellites.md): password hashes are never loaded;
`HashedPassword` stays in `sat_person__wwi__account` as an always-empty column, so the satellite mirrors the source.*

**Whether credentials are loaded at all.** `HashedPassword` holds password hashes for 157 people
(`Application/People/19_sensitivity.md#C3`), credentials with no analytical use, and the legal basis of the people data
is not established (`#C7`). The raw vault's principle is to keep everything delivered (144 §2), and regulatory
requirements apply from production on (ADR-0016). Recommendation: do not load `HashedPassword`, as the one exception to
keeping everything, because a credential is a risk without a purpose; keep the rest of the person's account data in the
restricted satellite. The other personal and restricted data load as proposed, in their own satellites, so that access
can be ruled per class before production.

## 7. What this note does not decide

The access rules per sensitivity class; which customers are individuals (`Sales/Customers/19_sensitivity.md#C6`);
the business vault and marts; the declaration format and the generator (ADR-0032); the hash algorithm and key
preparation (ADR-0030). Nothing is built.

# 148 — Wide World Importers: the relationships between the hubs (step B)

> **STATUS: PROPOSED, not ruled.** Drafted 2026-10-28 in session 10, after step A was ruled
> ([ADR-0029](../20_decisions/0029-wwi-step-a-concepts-and-keys.md)). Unreviewed on another model
> ([510](../50_process/510_external-review.md)). Open under [`ARC-OP-37`](../../registers/OPEN_POINTS.md).

## 1. What this note does

Step B of the route of 2026-10-21: the relationships between the twenty-two hubs of
[147](147_wwi-concepts-keys-and-business-time.md) §3, as Data Vault links. For each link it states the hubs it joins,
the role that distinguishes it from other links between the same hubs, its driving side, whether it is optional, and
the claim it rests on. Links are keyed on hash keys ([ADR-0030](../20_decisions/0030-hub-and-link-keys-are-hash-keys.md)).
Satellites, including the effectivity satellites some links will need, are step C; this note only says which links
need one.

Citations follow 147: paths relative to `analysis/wwi/tables/`, or beginning with `across/` or `analysis/`. In the
tables of section 3, the column *Relation* names the folder under `analysis/wwi/across/relations/` that the analysis
record keeps for the source's relationship, and *Evidence* cites claims in that folder by file number and claim
(`02#C2` is `<folder>/02_meaning.md#C2`, `07#C2` is `<folder>/07_population.md#C2`, `01#C4` is
`<folder>/01_granularity.md#C4`).

## 2. Eight rules applied throughout

**Rule 1: one link per relationship the source states between two hubs, distinguished by its role.** Two links between
the same hubs are two links when their meaning differs: an invoice names the customer delivered to and the customer
billed, which differ on 44,279 invoices (`across/relations/Sales.Invoices.BillToCustomerID__Sales.Customers.CustomerID/02_meaning.md#C2`,
`across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2`), and are two links, as
144 §3 item 3 requires ("defined by its participating business keys, its meaning and its grain").

**Rule 2: links are binary, each from the hub that names to the hub named.** The alternative is one wide link per
source row, joining an order to its customer, salesperson and contact at once, to keep the row's unit of work. Here
every event is a hub of its own (147 §3), and each of its binary links carries the event's hash key and the same load
time and batch, so the combination of an order's customer, salesperson and contact is recovered by joining on the
order; nothing of the unit of work is lost. Binary links are generated from one template, change independently, and
each needs at most one effectivity satellite.

**Rule 3: a link holds what the source stated, also where it repeats another route.** Several event columns repeat a
relationship reachable another way: an invoice's customer is its order's customer on every invoice
(`across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID/27_peculiarities.md#C5`), its billed customer
the customer's head office (`across/relations/Sales.Invoices.BillToCustomerID__Sales.Customers.CustomerID/02_meaning.md#C2`),
a stock receipt's supplier the purchase order's (`across/relations/Warehouse.StockItemTransactions.SupplierID__Purchasing.Suppliers.SupplierID/02_meaning.md#C2`),
and every copy agrees again in the second extract (`analysis/wwi/_source/22_stability.md#C5`). Each copy is the
source's assertion at the time of the event and loads as its own link (144 §2: the raw vault holds what a system
said). The business vault chooses one route per question, and the agreement of the routes becomes a plausibility test
(`ARC-OP-31`) rather than an assumption.

**Rule 4: an empty column gives no link row.** No zero or ghost key is used in links. Where emptiness carries a declared
meaning it is kept as that meaning, not as a missing link: a special deal with no customer applies to all customers
(`across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2`). Because the deal hub
and its satellite are loaded from the same row, the absence of a scope link is evidence that the scope was empty; the
business vault reads it so.

**Rule 5: every link has a driving side, the hub that names.** Each row of the naming table names at most one row of
the named table per role (each relation's `01_granularity.md#C1`), so the naming hub's key drives the link. A link
needs an effectivity satellite in step C wherever the naming row can be re-pointed. In the history held, no
relationship column of any system-versioned master ever changed: only `CreditLimit` among customers' business columns
(`Sales/Customers/06_keys.md#C5`), only `DeliveryLocation` among suppliers' (`Purchasing/Suppliers/06_keys.md#C5`),
only `CustomFields` and `Tags` among stock items' (`Warehouse/StockItems/06_keys.md#C5`), only population among
cities' (`Application/Cities/06_keys.md#C5`). In the event tables, the only relationship column updated in either
transition is `Sales.Orders.PickedByPersonID` (`Sales/Orders/03_temporal.md#C2`; `analysis/wwi/_source/22_stability.md#C1`).
The masters can nevertheless be edited in the source, so their links get effectivity satellites; event links whose
column was never updated get none until it is seen, and the picker link is dated by its milestone (Rule 6).

**Rule 6: the picker link is part of the picking milestone.** `PickedByPersonID` is written back with
`PickingCompletedWhen` (`Sales/Orders/03_temporal.md#C2`), so the link from an order to its picker is valid from the
picking stamp, like the milestone satellite of [ADR-0028](../20_decisions/0028-wwi-country-key-milestones-and-sensors.md)
decision 3. It is empty on the 7,546 originals split into backorders, which were picked without a picker
(`across/relations/Sales.Orders.PickedByPersonID__Application.People.PersonID/02_meaning.md#C3`).

**Rule 7: a relationship the source states only by matching values is derived in the business vault.** A stock issue
names an invoice and an item but not an invoice line; that each issue is the movement of exactly one line rests on
(`InvoiceID`, `StockItemID`) being unique on both sides
(`across/relations/Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID/02_meaning.md#C1`).
The same holds for a stock receipt and its purchase-order line, for a customer order as placed and its chain of
backorders (147 §3, item 12), and for a payment and the invoices it settles, for which the source holds no key at all
(`across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID/02_meaning.md#C2`). These are
interpretation (144 §3 item 4) and are built in the business vault (section 4).

**Rule 8: no link to a reference table, and none for the audit column.** A code from one of the six reference tables
(147 §4) stays a code in the naming hub's satellite (ADR-0029, Rule 2). `LastEditedBy` names a person on every table
for no business reason and becomes no link ([ADR-0021](../20_decisions/0021-position-in-the-schema.md), 147 §3 note on
person). The two city references of `Application.SystemParameters`, which has no hub (147 §4), stay codes in its
configuration record (`Application.SystemParameters.DeliveryCityID__Application.Cities.CityID`,
`Application.SystemParameters.PostalCityID__Application.Cities.CityID`). The holding row shares the stock item's key
one to one (`Warehouse.StockItemHoldings.StockItemID__Warehouse.StockItems.StockItemID`, 02#C2) and is a satellite of
the stock item (147 §4), not a link.

## 3. The links proposed: forty-nine

Optional means the naming column may be empty (Rule 4). Effectivity says whether step C should give the link an
effectivity satellite (Rule 5): *yes* for masters, *milestone* for the picker link, *no* for event links whose column
was never updated.

### 3.1 Geography, parties and products (masters)

| # | Link | From (driving) → to | Relation | Optional | Effectivity | Evidence |
|---|---|---|---|---|---|---|
| 1 | city in state or province | city → state or province | `Application.Cities.StateProvinceID__Application.StateProvinces.StateProvinceID` | no | yes | 02#C2, 07#C2 |
| 2 | state or province in country | state or province → country | `Application.StateProvinces.CountryID__Application.Countries.CountryID` | no | yes | 02#C2, 07#C2 |
| 3 | customer delivery city | customer → city | `Sales.Customers.DeliveryCityID__Application.Cities.CityID` | no | yes | 07#C2 |
| 4 | customer postal city | customer → city | `Sales.Customers.PostalCityID__Application.Cities.CityID` | no | yes | 07#C2 |
| 5 | customer billed to (head office) | customer → customer | `Sales.Customers.BillToCustomerID__Sales.Customers.CustomerID` | no | yes | 02#C2, 07#C2 |
| 6 | customer in buying group | customer → buying group | `Sales.Customers.BuyingGroupID__Sales.BuyingGroups.BuyingGroupID` | yes | yes | 07#C2 |
| 7 | customer in category | customer → customer category | `Sales.Customers.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID` | no | yes | 07#C2 |
| 8 | customer primary contact | customer → person | `Sales.Customers.PrimaryContactPersonID__Application.People.PersonID` | no | yes | 02#C3 |
| 9 | customer alternate contact | customer → person | `Sales.Customers.AlternateContactPersonID__Application.People.PersonID` | yes | yes | 02#C3, 07#C2 |
| 10 | supplier delivery city | supplier → city | `Purchasing.Suppliers.DeliveryCityID__Application.Cities.CityID` | no | yes | 07#C2 |
| 11 | supplier postal city | supplier → city | `Purchasing.Suppliers.PostalCityID__Application.Cities.CityID` | no | yes | 07#C2 |
| 12 | supplier primary contact | supplier → person | `Purchasing.Suppliers.PrimaryContactPersonID__Application.People.PersonID` | no | yes | 02#C2, 07#C2 |
| 13 | supplier alternate contact | supplier → person | `Purchasing.Suppliers.AlternateContactPersonID__Application.People.PersonID` | no | yes | 02#C2, 07#C2 |
| 14 | stock item usual supplier | stock item → supplier | `Warehouse.StockItems.SupplierID__Purchasing.Suppliers.SupplierID` | no | yes | 02#C2 |
| 15 | stock item in stock group | stock item ↔ stock group (no driving side) | `Warehouse.StockItemStockGroups.StockItemID__Warehouse.StockItems.StockItemID` and `Warehouse.StockItemStockGroups.StockGroupID__Warehouse.StockGroups.StockGroupID` | no | yes | 02#C2 |

Link 2 reaches the country through the source's `CountryID`, resolved to the ISO code from the same extract
(ADR-0028 decision 1). Link 15 is the bridge of `Warehouse.StockItemStockGroups`; a membership has no driving side, its
surrogate `StockItemStockGroupID` is not part of the link key (`Warehouse/StockItemStockGroups/06_keys.md#C1`, `#C4`),
and an ended membership leaves no trace in the source (`Warehouse/StockItemStockGroups/03_temporal.md#C5`), so its
effectivity has to come from the membership's absence in a complete extract (127, "Absence is not deletion").

### 3.2 Special deals

| # | Link | From (driving) → to | Relation | Optional | Effectivity | Evidence |
|---|---|---|---|---|---|---|
| 16 | deal for customer | special deal → customer | `Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID` | yes (empty: all customers) | yes | 02#C2, 07#C2 |
| 17 | deal for buying group | special deal → buying group | `Sales.SpecialDeals.BuyingGroupID__Sales.BuyingGroups.BuyingGroupID` | yes | yes | 02#C2 |
| 18 | deal for customer category | special deal → customer category | `Sales.SpecialDeals.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID` | yes | yes | 02#C2, 07#C2 |
| 19 | deal for stock item | special deal → stock item | `Sales.SpecialDeals.StockItemID__Warehouse.StockItems.StockItemID` | yes (empty: discounts only) | yes | 02#C2, 07#C2 |
| 20 | deal for stock group | special deal → stock group | `Sales.SpecialDeals.StockGroupID__Warehouse.StockGroups.StockGroupID` | yes | yes | 02#C2 |

Links 16, 18 and 19 have no row in the data: both deals leave those columns empty. They are declared so that a deal
that uses them loads without a change to the model.

### 3.3 Sales: orders, invoices and their lines

| # | Link | From (driving) → to | Relation | Optional | Effectivity | Evidence |
|---|---|---|---|---|---|---|
| 21 | order customer | sales order → customer | `Sales.Orders.CustomerID__Sales.Customers.CustomerID` | no | no | 02#C2 |
| 22 | order salesperson | sales order → person | `Sales.Orders.SalespersonPersonID__Application.People.PersonID` | no | no | 02#C2, 02#C3 |
| 23 | order customer contact | sales order → person | `Sales.Orders.ContactPersonID__Application.People.PersonID` | no | no | 02#C3 |
| 24 | order picker | sales order → person | `Sales.Orders.PickedByPersonID__Application.People.PersonID` | yes | milestone | 02#C3, 07#C2 |
| 25 | backorder of | sales order (original) → sales order (backorder) | `Sales.Orders.BackorderOrderID__Sales.Orders.OrderID` | yes | no | 02#C2, 02#C3, 07#C2 |
| 26 | order line of order | sales order line → sales order | `Sales.OrderLines.OrderID__Sales.Orders.OrderID` | no | no | 02#C2 |
| 27 | order line item | sales order line → stock item | `Sales.OrderLines.StockItemID__Warehouse.StockItems.StockItemID` | no | no | 01#C1 |
| 28 | invoice of order | invoice → sales order | `Sales.Invoices.OrderID__Sales.Orders.OrderID` | no in the data, nullable | no | 02#C2, 01#C4 |
| 29 | invoice customer (delivered to) | invoice → customer | `Sales.Invoices.CustomerID__Sales.Customers.CustomerID` | no | no | 02#C2 |
| 30 | invoice customer billed | invoice → customer | `Sales.Invoices.BillToCustomerID__Sales.Customers.CustomerID` | no | no | 02#C2 |
| 31 | invoice salesperson | invoice → person | `Sales.Invoices.SalespersonPersonID__Application.People.PersonID` | no | no | 02#C3 |
| 32 | invoice customer contact | invoice → person | `Sales.Invoices.ContactPersonID__Application.People.PersonID` | no | no | 02#C3 |
| 33 | invoice accounts contact | invoice → person | `Sales.Invoices.AccountsPersonID__Application.People.PersonID` | no | no | 02#C3 |
| 34 | invoice packer | invoice → person | `Sales.Invoices.PackedByPersonID__Application.People.PersonID` | no | no | 02#C3 |
| 35 | invoice line of invoice | invoice line → invoice | `Sales.InvoiceLines.InvoiceID__Sales.Invoices.InvoiceID` | no | no | 02#C2 |
| 36 | invoice line item | invoice line → stock item | `Sales.InvoiceLines.StockItemID__Warehouse.StockItems.StockItemID` | no | no | 01#C1 |

Link 25 runs from the original order to the backorder split from it, against the source's description: on all 7,546
filled rows the order named is later and has the same customer and purchase-order number (02#C2, 02#C3). The direction
rests on one extract; if a new backorder ever shows the declared direction, the roles swap and the link's key does not
change.

### 3.4 Purchasing

| # | Link | From (driving) → to | Relation | Optional | Effectivity | Evidence |
|---|---|---|---|---|---|---|
| 37 | purchase order supplier | purchase order → supplier | `Purchasing.PurchaseOrders.SupplierID__Purchasing.Suppliers.SupplierID` | no | no | 07#C2 |
| 38 | purchase order contact | purchase order → person | `Purchasing.PurchaseOrders.ContactPersonID__Application.People.PersonID` | no | no | 02#C2, 02#C3, 02#C4 |
| 39 | purchase-order line of order | purchase-order line → purchase order | `Purchasing.PurchaseOrderLines.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID` | no | no | 02#C2 |
| 40 | purchase-order line item | purchase-order line → stock item | `Purchasing.PurchaseOrderLines.StockItemID__Warehouse.StockItems.StockItemID` | no | no | 07#C2 |

Link 38 keeps the source's name, contact, although every order names a WWI salesperson and never the supplier's
contact, and the role it records is not established (02#C3, 02#C4). The role is a reading for the business vault; the
link loads what the source states either way.

### 3.5 The three ledgers

| # | Link | From (driving) → to | Relation | Optional | Effectivity | Evidence |
|---|---|---|---|---|---|---|
| 41 | customer entry account (billed) | customer ledger entry → customer | `Sales.CustomerTransactions.CustomerID__Sales.Customers.CustomerID` | no | no | 02#C2 |
| 42 | customer entry invoice | customer ledger entry → invoice | `Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID` | yes (payments) | no | 02#C2, 07#C2 |
| 43 | supplier entry account | supplier ledger entry → supplier | `Purchasing.SupplierTransactions.SupplierID__Purchasing.Suppliers.SupplierID` | no | no | 02#C2 |
| 44 | supplier entry purchase order | supplier ledger entry → purchase order | `Purchasing.SupplierTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID` | yes (payments) | no | 02#C2, 07#C2 |
| 45 | movement item | stock movement → stock item | `Warehouse.StockItemTransactions.StockItemID__Warehouse.StockItems.StockItemID` | no | no | 01#C1 |
| 46 | movement customer (issued to) | stock movement → customer | `Warehouse.StockItemTransactions.CustomerID__Sales.Customers.CustomerID` | yes (issues only) | no | 02#C2, 07#C2 |
| 47 | movement invoice | stock movement → invoice | `Warehouse.StockItemTransactions.InvoiceID__Sales.Invoices.InvoiceID` | yes (issues only) | no | 02#C2, 07#C2 |
| 48 | movement supplier | stock movement → supplier | `Warehouse.StockItemTransactions.SupplierID__Purchasing.Suppliers.SupplierID` | yes (receipts only) | no | 02#C2, 07#C2 |
| 49 | movement purchase order | stock movement → purchase order | `Warehouse.StockItemTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID` | yes (receipts only) | no | 02#C2, 07#C2 |

The account a customer ledger entry is booked on is the customer billed, not the customer delivered to: it equals the
invoice's billed customer on every invoice entry (link 41, 02#C2; `across/terms/customer/25_terms.md#C3`). Link 41
therefore carries the role *billed*, like link 30.

## 4. Relationships derived in the business vault

| Derived relationship | Built from | Evidence |
|---|---|---|
| stock issue ↔ invoice line, one to one | links 45, 47 and 35, 36, matched on invoice and item | `across/relations/Warehouse.StockItemTransactions.InvoiceID.StockItemID__Sales.InvoiceLines.InvoiceID.StockItemID/02_meaning.md#C1` |
| stock receipt ↔ purchase-order line, one to one | links 45, 49 and 39, 40, matched on purchase order and item | `across/relations/Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID/02_meaning.md#C1`, `#C2`, `#C3` |
| customer order as placed: an original and its backorders | link 25, followed to the end of the chain | `Sales/Orders/27_peculiarities.md#C12`, `#C4` |
| payment ↔ invoices it settles | the ledger entries, matched by customer and day | `across/reconciliations/customer-payments-vs-invoices/16_reconciliation.md#C2`; `analysis/wwi/_source/22_stability.md#C6` |

Each is a judgement with a rule and, for the payments, a confidence; it is stored with proposal, decision and
publication kept apart (144 §3 item 4). The matching of payments to invoices involves a business rule, so under
[ADR-0024](../20_decisions/0024-calculation-engines-are-a-versioned-source.md) it is an engine's.

## 5. What this note does not decide

The effectivity satellites themselves and every other satellite (step C); the link names in the model files and the
model-file format (`ARC-OP-29`); the hash algorithm and key preparation (ADR-0030, Consequences); the marts. Nothing is
built.

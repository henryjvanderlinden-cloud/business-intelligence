# XREV 2026-10-18 — round-1 dossiers of Sales.Invoices and Sales.CustomerTransactions — sol

```yaml
object:        analysis/wwi/tables/Sales/Invoices/ and Sales/CustomerTransactions/, as committed on 2026-10-18 (5cf9db1).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; brief restricted to Markdown and JSON after an
               earlier single pass over more tables never arrived. Run in parallel with a second sol pass.
assignment:    against ADR-0017 (hard effort, no guessing, confidence supported by the cited evidence) and ADR-0020
               (describe the as-is): up to three false or overstated claims; up to two unsupported confidences or
               guesses; any design advice or future decision. 350 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the dossiers' judgement claims and the generator of their
               mechanical claims.
verdict:       FAILS [code meanings and nested delivery-event contents asserted without evidence that observes them]
```

Sol's answer, verbatim:

1. Claims false or overstated against their cited evidence:

   - `analysis/wwi/tables/Sales/CustomerTransactions/07_population.md#C5`: “TransactionTypeID: 1 (customer invoice) ... 3 (payment received) ... PaymentMethodID is 4 (EFT).” `62d71a286e682cb1` shows only the numeric value counts and empty-value patterns. It contains no lookup-table values establishing any of those three labels, so the semantic readings and “no credit notes, refunds or contras” exceed the evidence.
   - `analysis/wwi/tables/Sales/Invoices/19_sensitivity.md#C4`: “the delivery JSON repeats it with event times, a driver id and latitude and longitude.” `b7b43b18cf6be97a` reports only that all JSON parses and the top-level key shapes are `DeliveredWhen,Events,ReceivedBy` or `Events`; its code does not inspect nested event fields. Driver ID and coordinates are not evidenced.
   - `analysis/wwi/tables/Sales/CustomerTransactions/27_peculiarities.md#C9`: “OutstandingBalance is ... updated when the invoice is paid; summing it over time double counts.” `62d71a286e682cb1` is a one-extract profile: it shows 56 positive and 97,186 zero balances, but no updates, payments, or repeated observations over time. The transition and aggregation warning are not established by the cited evidence.

2. Unsupported confidence or guessing:

   - `analysis/wwi/tables/Sales/Invoices/01_granularity.md#C4` assigns `high` to one-invoice-per-order. `71b944fc0f813bf5` establishes uniqueness only in one extract; no unique constraint or mechanism explains why it must hold. Under the repository scale this is at most `medium`, with persistence uncertain.
   - `analysis/wwi/tables/Sales/CustomerTransactions/01_granularity.md#C4` likewise assigns `high` and concludes “each invoice is booked once.” `0e11b74e56590c9a` establishes that only for the one extract; no enforcing mechanism is cited. The durable claim should be uncertain or confined explicitly to this extract.

3. None found beyond the admitted round-2 cross-table deferrals.

VERDICT: FAILS + code meanings and nested delivery-event contents are asserted without evidence that observes them.

## Dispositions

All five findings accepted and fixed on 2026-10-19 (step S08-066):

1. **Code labels without evidence.** `evidence_shared.py more` now writes a labels evidence per table from the code
   tables of the same extract (TransactionTypes, PaymentMethods, DeliveryMethods, PackageTypes, SupplierCategories,
   CustomerCategories, BuyingGroups, StockGroups): counts per code with the code table's name, no other rows.
   CustomerTransactions 07 C5 cites 54587972a7ff203e. The same gap existed wherever a claim names a code, so the
   labels evidence is now cited in SupplierTransactions, StockItemTransactions, Invoices, Customers, PurchaseOrders,
   Suppliers, InvoiceLines, OrderLines, PurchaseOrderLines, SpecialDeals and StockItemStockGroups.
2. **Nested delivery events.** A new evidence (3163d80faa939828) counts the keys inside the events of
   ReturnedDeliveryData: 141,076 events with Event, EventTime and ConNote; 70,510 with DriverID, Latitude and
   Longitude; 63,339 with Status; 7,171 with Comment. Invoices 19 C4 and 27 now cite it and state counts.
3. **OutstandingBalance updated in place.** The claim now also cites the transition evidence (34c668954c133c3d), which
   shows 84 rows updated between the extracts in OutstandingBalance together with FinalizationDate and IsFinalized,
   and is reworded to what that shows: a sum over rows of different dates adds states, not movements.
4. **One invoice per order** and 5. **each invoice booked once**: lowered to medium and confined to this extract, with
   "no constraint enforces it". The same holds for every other uniqueness observed but not declared, so the
   candidate-key claims of PurchaseOrderLines, OrderLines, InvoiceLines, SupplierTransactions, StockItemTransactions and
   VehicleTemperatures were lowered to medium as well. README section 5 now says how counts and generalisations differ.

Section 3: none found.

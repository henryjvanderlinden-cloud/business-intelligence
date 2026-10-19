# XREV 2026-10-19 — round-2 relation dossiers on customers, invoices and backorders — sol

```yaml
object:        seven relation folders under analysis/wwi/across/relations/ (customer roles, the ledger, backorders), as first generated on 2026-10-19 (uncommitted; moved to scratch/_superseded/across_r2_v1).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by astra on other relations.
assignment:    against ADR-0017 and ADR-0019 (the relation minimum 01, 02, 06, 07, 27 with hard effort, no guessing),
               analysis/README.md section 5 and ADR-0020: up to three false or overstated claims; up to three
               confidences breaking section 5; the most important missed cross-table warning; any design advice.
               450 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the readings, the generator and the evidence script the
               same evening.
verdict:       FAILS [CustomerTransactions.InvoiceID 27 C1 asserted payment semantics and no alternative link without evidence that tests them]
```

Sol's answer, verbatim:

1. False or overstated against cited evidence:

   - `analysis/wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID/27_peculiarities.md#C1` says the 26,676 rows without `InvoiceID` are payments and that no other column relates a payment to an invoice. `ac63b1601c4a225b` establishes only 26,676 empty values, the declared FK, and other tables referring to `Invoices`; it neither classifies those rows nor searches payment-allocation keys.
   - `analysis/wwi/across/relations/Warehouse.StockItemTransactions.CustomerID__Sales.Customers.CustomerID/02_meaning.md#C2` calls all 228,432 filled rows stock issues and all 8,411 empty rows receipts or stocktake adjustments. `83bb5422947dae2d` shows the null count and agreement with invoice customer routes, but contains no transaction-type breakdown.
   - `analysis/wwi/across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID/27_peculiarities.md#C3` says every listed sibling relation has several children per customer and therefore produces a chasm multiplication. `3b8ebb7b87283001` measures multiplicity only for `Invoices.CustomerID`; for the siblings it supplies names only.

2. Confidence or uncertainty failures:

   - `analysis/wwi/across/relations/Sales.Orders.BackorderOrderID__Sales.Orders.OrderID/02_meaning.md#C3` assigns high confidence to an intended meaning inferred from one extract, despite contradicting the declared description. Section 5 permits medium for that generalisation; `c6e5d1bc0af05898` proves only the observed patterns.
   - The same unsupported high confidence recurs at `analysis/wwi/across/relations/Sales.Orders.BackorderOrderID__Sales.Orders.OrderID/27_peculiarities.md#C1`.
   - Every reviewed `07_population.md` says `Uncertainties: None`, but none of its evidence addresses ADR-0019's required row-level-security, masking, or extracting-account-versus-unrestricted visibility check. Each dossier owes an `unknown` claim stating what would settle that visibility question.

3. `analysis/wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID/27_peculiarities.md` misses an unenforced fan-out warning. `ac63b1601c4a225b` observes one child per invoice now, while `01_granularity.md#C4` records that no unique constraint on child `InvoiceID` enforces this. Multiple customer transactions per invoice are therefore permitted by the as-is schema, despite the extract's apparent one-to-one cardinality.

4. None found. The join-role and double-counting statements are consequence warnings allowed by ADR-0020, not model, KPI, reporting-date, loading, or exclusion proposals.

VERDICT: FAILS + `Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID/27_peculiarities.md#C1` asserts payment semantics and absence of alternative links that its cited evidence never tests.

## Dispositions

All findings accepted and fixed the same evening (step S08-079), in every relation, not only the seven reviewed:

1. **Payments and transaction types.** relations.py now counts each child's rows by TransactionTypeID (with the type's
   name from Application.TransactionTypes) and by whether the referring column is filled. The ledger's empty InvoiceID
   rows are all Customer Payment Received (26,676); the stock movements' empty CustomerID rows are Stock Receipt
   (8,367) and Stock Adjustment at Stocktake (44). The claims cite that count. "No other column relates a payment to an
   invoice" is restated as what was tested (no other declared foreign key, no undeclared ...ID column) at medium, with
   what was not tested (non-key columns).
2. **Chasm traps from names only.** The evidence of each relation now carries the multiplicity of every other
   referring column of the same parent, and the chasm claim lists only those with several rows per parent, with their
   maximum.
3. **BackorderOrderID at high.** Lowered to medium in 02 and 27, worded as holding in this extract against the
   declaration.
4. **Extraction visibility.** Every 07 now states the owner, reader and extract row counts of both tables and the
   masked columns, and carries an unknown claim on row-level security (not visible to the reader).
5. **One-to-one not enforced.** A generic warning in 27 wherever a relation is one-to-one in the extract without a
   unique constraint: ten relations, among them the two ledgers on their documents, Invoices.OrderID,
   Orders.BackorderOrderID, StockItemHoldings and the customers' and suppliers' contact persons.

Section 4: none found.

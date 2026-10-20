# XREV 2026-10-20 — measures, derived columns and arithmetic (items 8, 9, 28), readings — astra

```yaml
object:        items 8, 9 and 28 as first written on 2026-10-20 (uncommitted): prototypes/information_analysis/measures.py
               and write_measures.py, their evidence (first run, now in scratch/_superseded/measures_v1), and the
               08_measures.md, 09_derived.md and 28_arithmetic.md files of 17 tables, written from
               scratch/ia_specs/measures_notes.py.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file.
assignment:    against ADR-0017, ADR-0020 and analysis/README.md sections 4 to 6: readings beyond their evidence or links;
               numeric columns misclassified or left unstated; any design advice. Praise and summary forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote measures.py, write_measures.py and the readings the same
               evening.
verdict:       FAILS [equal-and-opposite quantities do not establish copying; the cited TargetStockLevel description does not establish a
               threshold]
```

Astra's answer, verbatim:

1. `analysis/wwi/tables/Sales/OrderLines/08_measures.md#C6`: "exists only as Quantity x UnitPrice with tax at TaxRate" is marked observed/high. Evidence `a0e8eae83042ac04` tests whether four particular column names exist; it neither computes an order value nor compares that formula with a source total or implementation. Absence of a stored amount does not establish the source's valuation formula. The admitted rounding uncertainty does not cover this inference.

   `analysis/wwi/tables/Warehouse/StockItemTransactions/09_derived.md#C1`: "a copy, not an independent count." The cited reconciliation C1 establishes equal-and-opposite quantities; C2 establishes one-to-one matching. Neither establishes how either quantity was produced. Independently recorded quantities that agree, or two values generated from a common upstream quantity, satisfy both tests. Numerical redundancy is observed; copying is an unverified process reading, not observed/high.

   `analysis/wwi/tables/Sales/InvoiceLines/28_arithmetic.md#C1`: "So tax is rounded half up, per line." The evidence establishes exact reproduction by that candidate calculation, not the source's implementation. For example, rounding ties toward positive infinity gives identical results for these positive tax amounts but differs from half-up on negative ties. The count can remain high; the asserted arithmetic policy needs qualification or implementation evidence.

2. `analysis/wwi/tables/Warehouse/StockItemHoldings/08_measures.md#C6` calls `TargetStockLevel` a "threshold" with high confidence. Its cited evidence `b0419db382f5f388` describes it as "Typical quantity ordered", whereas `ReorderLevel` is explicitly the quantity below which reordering occurs. Testing ReorderLevel <= TargetStockLevel does not resolve whether the latter is an order quantity or a target holding level. That disagreement is unstated.

   `analysis/wwi/tables/Application/Cities/08_measures.md#C2` calls `LatestRecordedPopulation` an "attribute" without establishing its additivity. Failure to reconcile city totals to province totals does not establish non-additivity across disjoint cities; missing populations and different reference dates could explain it. Its nature as a population count, temporal restriction, and unresolved geographic comparability are not captured by the attribute label or "Uncertainties: None."

3. No explicit design proposal or future decision found in the reviewed item files. Statements about summing, averaging and join repetition describe arithmetic consequences within ADR-0020's scope.

VERDICT: FAILS + equal-and-opposite quantities do not establish copying; the cited TargetStockLevel description does not establish a threshold.

## Dispositions

All findings accepted and fixed the same evening (step S08-116):

1. **OrderLines C6, an order's value "exists only as" a formula.** The claim now says only that no amount column exists
   and that the order tables store no value of a line or an order.
2. **StockItemTransactions 09 C1, "a copy".** Now: the issue adds no quantity the line does not hold; whether one is
   copied from the other, or both come from one source, is not established.
3. **InvoiceLines 28 C1, "tax is rounded half up".** Now "consistent with" rounding half up per line, with the note that
   no tax is negative, so half up is not told apart from rounding ties towards positive infinity; the same qualification
   is added to the recommended retail price in Warehouse.StockItems 28, and the summary says "reproduced by".
4. **TargetStockLevel called a threshold.** A separate low-confidence claim now says its description ("Typical quantity
   ordered") and its name disagree, and which it is is not established; ReorderLevel alone is called a threshold.
5. **Cities population called an attribute.** Now a count of people at an unstated date; the shortfall against the
   province is recorded with both explanations (missing cities, different dates) left open.

Section 3: none found.

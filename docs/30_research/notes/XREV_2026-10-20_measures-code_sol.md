# XREV 2026-10-20 — measures, derived columns and arithmetic (items 8, 9, 28), code and counts — sol

```yaml
object:        items 8, 9 and 28 as first written on 2026-10-20 (uncommitted): prototypes/information_analysis/measures.py
               and write_measures.py, their evidence (first run, now in scratch/_superseded/measures_v1), and the
               08_measures.md, 09_derived.md and 28_arithmetic.md files of 17 tables, written from
               scratch/ia_specs/measures_notes.py.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file.
assignment:    places where the code computes something other than the claim says; claims whose numbers misstate the
               evidence. Praise and summary forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote measures.py, write_measures.py and the readings the same
               evening.
verdict:       FAILS [exact ratios 0.351 and 0.354 would be reported as one distinct ratio]
```

Sol's answer, verbatim:

1. 
   - `t_stock_items` quantizes `LastCostPrice / UnitPrice` to two decimals before both counting and taking `len(cost_ratio)`. It therefore computes distinct two-decimal buckets, not distinct ratios. For example, exact ratios `0.351` and `0.354` collapse to one `0.35` bucket.
   - `t_ledger` compares each party's aggregate `sum(TransactionAmount)` with aggregate `sum(OutstandingBalance)`. That can pass despite wrong row balances whenever errors cancel (for example, two balances overstated and understated by 10). It does not establish the reports' stronger reading that the sum is what the party owes; it establishes only equality between two internally computed aggregates.
   - `t_purchase_order_lines` compares every historical line's `ExpectedUnitPricePerOuter` with the *current-extract* `StockItemHoldings.LastCostPrice`. A full match shows a snapshot coincidence, not that the expected price was derived from the cost applicable when each order was made. No temporal reference is selected.

2. 
   - `analysis/wwi/tables/Warehouse/StockItems/09_derived.md#C3`: “37 distinct ratios over the items.” Evidence `b17e57ffdf4ef125` contains 37 distinct ratios only *after two-decimal quantization*. The exact-ratio count is not computed, so 37 misstates the evidence.

VERDICT: FAILS + exact ratios 0.351 and 0.354 would be reported as one distinct ratio

## Dispositions

All findings accepted and fixed the same evening (step S08-116):

1. **Distinct cost ratios counted after rounding.** measures.py now counts exact ratios (as fractions) beside the
   rounded buckets; Warehouse.StockItems 09 reports 74 distinct exact ratios over 227 items (37 when rounded to two
   decimals). The earlier 37 was the rounded count.
2. **The per-party sum can pass with cancelling errors.** The ledger reading no longer says what a party owes; it states
   the equality and refers to the row-level test (09_derived.md#C3: OutstandingBalance is 0 or the full amount on every
   row, nothing else), which is what excludes cancelling errors.
3. **Purchase-order prices compared with the current cost.** The claim now says that LastCostPrice and QuantityPerOuter
   are taken as they stand in this extract, not when the order was placed; the uncertainty that the price might follow
   a later change in cost was already stated and stays.

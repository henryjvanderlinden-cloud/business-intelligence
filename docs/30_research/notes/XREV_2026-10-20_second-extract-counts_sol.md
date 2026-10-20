# XREV 2026-10-20 — second-extract recheck, mechanical claims — sol

```yaml
object:        analysis/wwi/_source/22_stability.md C1 to C16, recheck.py and write_stability.py, after astra's fixes (uncommitted).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file.
               A first, broader pass (scratch/xrev_ia_stab_sol_brief.md) wrote nothing in eleven minutes and was
               taken as lost; this narrower pass was sent after astra's fixes.
assignment:    against ADR-0017, ADR-0019, analysis/README.md sections 4 to 6 and ADR-0020: false or overstated claims;
               comparisons that are not like for like; confidences breaking section 5 or rules claimed confirmed but
               not tested; any design advice. Praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote recheck.py, write_stability.py and the readings the same
               morning.
verdict:       FAILS [C3 reported key-filled counts as table rows]
```

Sol's answer, verbatim:

1. Claims that misstate the evidence:

- C3 says `Purchasing.SupplierTransactions (PurchaseOrderID, 2,076 rows)` and similarly labels filtered counts as table rows. The evidence says `rows=2,442`, `rows_with_all_filled=2,076`; for Sales.CustomerTransactions it is 97,371 versus 70,673, and for Warehouse.StockItemTransactions 237,214 versus 228,794/8,376. These are non-null key populations, not row counts.
- C4 says `15 relations with at most one child per parent`. The evidence has 15 with `max_children=1` plus three with `max_children=null` because all two child rows are empty: Sales.SpecialDeals.CustomerCategoryID, CustomerID, and StockItemID. Those relations also have at most one observed child, so the claim mistakes “maximum exactly one” for “at most one.”
- C16 calls the reported 5,517/5,616 counts `cold-room readings`. The evidence keys explicitly count `Warehouse.ColdRoomTemperatures_Archive_rows...`; it does not count the four live Warehouse.ColdRoomTemperatures rows shown by the transition evidence. The claim broadens archive-only counts to all readings.

2. Comparisons/probes that are not like for like:

- The telemetry follow-up reads both the base-day and new-day cold-room/vehicle counts from `rd(new, t)`. A day comparison therefore uses only the new extract, rather than base day from `rd(base, t)` and new day from `rd(new, t)`.
- The purchase-order follow-up reports `movements=1` using a counter over every movement in the new extract. It never subtracts movements already present in the base extract, so it cannot show that one movement occurred during the base-to-new transition.

VERDICT: FAILS + C3 reports 2,076 SupplierTransactions rows where the evidence reports 2,442.

## Dispositions

All findings accepted and fixed the same morning (step S08-099):

1. **C3: rows.** Now "rows with the key filled".
2. **C4: at most one.** The 3 relations of Sales.SpecialDeals with no filled child row are now counted and named apart.
3. **C16: cold-room readings.** Now names the history table's rows and says the current table holds the latest four.
4. **Telemetry from the new extract only.** Kept, and stated in the claim: both days are counted in the extract of
   2016-06-02, which holds both.
5. **Movements of the open purchase-order lines.** recheck.py now counts them in both extracts: 0 on 2016-06-01, 1 on
   2016-06-02 for each of the 9 lines, so the movement was made in the transition.

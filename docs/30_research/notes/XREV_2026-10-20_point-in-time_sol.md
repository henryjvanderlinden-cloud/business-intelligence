# XREV 2026-10-20 — point-in-time and processes — sol

```yaml
object:        item 03 of five relations under analysis/wwi/across/relations/ and the processes order-to-cash and procure-to-pay, as first generated on 2026-10-20 (uncommitted; evidence moved to scratch/_superseded/temporal_v1 and processes_v1).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by astra on the stocktake, terms and entities.
assignment:    against ADR-0017, ADR-0019, analysis/README.md sections 4 and 5 and ADR-0020: up to three false or
               overstated claims; up to two places where code or a link says something else than the claim; up to two
               confidences breaking section 5; any design advice. 450 words; praise, summary and general assessment
               forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the scripts, readings and links the same morning.
verdict:       FAILS [the 'current version' test ignored ValidTo; procure-to-pay asserted full line-level receipt without measuring it]
```

Sol's answer, verbatim:

1. 

- `analysis/wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID/03_temporal.md#C4`: “an invoice carries its order's date, except for backorders” is contradicted by C3's 15 non-backorders invoiced later. “Invoiced when supplied” is also not tested: the evidence compares only order and invoice dates.
- `analysis/wwi/across/processes/procure-to-pay/24_processes.md#C3`: “received in full in one receipt per line” is unsupported. The code records only whether a purchase order has any stock transaction and whether all its lines are finalized; it neither matches receipts to lines nor compares received and ordered quantities.
- `analysis/wwi/across/relations/Sales.InvoiceLines.StockItemID__Warehouse.StockItems.StockItemID/03_temporal.md#C4`: “No other attribute” is false as a description of the test. `PERIOD` excludes `LastEditedBy` and `LastEditedWhen` from comparison, although `LastEditedBy` is not a temporal boundary. The same overstatement occurs in the other three specified system-versioned relations' C4.

2. 

- `analysis/wwi/across/relations/Sales.CustomerTransactions.CustomerID__Sales.Customers.CustomerID/03_temporal.md#C2`: “version ... current” is not what `as_of` measures. It selects the last version whose `ValidFrom <= t` but never checks `t < ValidTo`; gaps or overlaps would be silently misclassified. This affects C2-C4 in all four specified system-versioned relations.
- `analysis/wwi/across/processes/order-to-cash/24_processes.md#C5`: the cited `Sales.Invoices.OrderID__Sales.Orders.OrderID/03_temporal.md` supports date/backorder counts, not “A shortage” or “the original is picked without a picker.” The process code does not inspect stock shortages or `PickedByPersonID` either.

3. 

- `analysis/wwi/across/processes/order-to-cash/24_processes.md#C5`: medium is too high for the unmeasured causal reading that a shortage causes the split; this should be unknown pending process evidence, or split from the observed counts.
- `analysis/wwi/across/processes/procure-to-pay/24_processes.md#C4`: calling missing downstream rows “the open end ... at the extract date” guesses censoring from one extract. Medium should be unknown unless status/process evidence establishes that those orders and invoices are still open.

4. None.

VERDICT: FAILS + the temporal “current version” test ignores `ValidTo`, and procure-to-pay asserts full line-level receipt without measuring lines or quantities.

## Dispositions

All findings accepted and fixed the same morning (step S08-092), in every relation and process:

1. **Invoices.OrderID 03 C4.** Restated with the counts: 66,087 invoices on the order date, 4,464 of the 4,479 later
   ones for backorders; "invoiced when supplied" removed.
2. **"Received in full in one receipt per line".** processes.py now compares ReceivedOuters with OrderedOuters per
   line: every line of every received order is received in full (0 differ), and the claim links the composite
   relation for one movement per line.
3. **"No other attribute".** The claim now says that LastEditedBy, LastEditedWhen and the period columns are not
   compared.
4. **ValidTo ignored.** relations_temporal.py now requires the child's time to fall before the chosen version's
   ValidTo and counts a gap otherwise; there are no gaps (0 rows), so the counts are unchanged, now by a test that
   could fail.
5. **The shortage and the picker in order-to-cash.** Split: the counts of split and backorder orders and late
   invoices (medium), and round 1's picker finding with the shortage as an untested reading (low).
6. **"The open end of the process".** Replaced by an unknown claim: whether the 2 unreceived orders and 4 unpaid
   invoices will complete is not established from one extract.

Section 4: none found.

# XREV 2026-10-20 — second-extract recheck, readings and links — astra

```yaml
object:        analysis/wwi/_source/22_stability.md C17 to C24 and the claims they link, and tables/Sales/Orders/07_population.md#C12, as first written on 2026-10-20 (uncommitted).
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file.
assignment:    against ADR-0017, ADR-0019, analysis/README.md sections 4 to 6 and ADR-0020: false or overstated claims;
               comparisons that are not like for like; confidences breaking section 5 or rules claimed confirmed but
               not tested; any design advice. Praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote recheck.py, write_stability.py and the readings the same
               morning.
verdict:       FAILS [backorder membership does not establish a stock shortage or settle why 3,078 orders remain unpicked]
```

Astra's answer, verbatim:

1. `analysis/wwi/_source/22_stability.md#C18`: "a queue, not an artefact" and "backorders waiting for stock" exceed `c02a9c797b00f222`. The probe establishes backorder-target membership and picking/invoicing, not stock availability or why 3,078 remain unpicked. Four completions do not settle the remaining backlog's origin. `analysis/wwi/tables/Sales/Orders/07_population.md#C12` compounds this with "C7 holds only for those 5", improperly discharging the uncertainty for all remaining backorders.

   `analysis/wwi/_source/22_stability.md#C22`: "a person's row is rewritten every day with the same values" drops the alternative explicitly preserved in `tables/Application/People/03_temporal.md#C4`: changed values rendered identically by extraction. The evidence establishes unchanged visible values and one version per observed transition, not the rewrite mechanism or an everyday rule.

2. `prototypes/information_analysis/write_stability.py`, `mechanical()`, emits `22_stability.md#C11`'s "are the same" without comparing base and new attribute sets: it enumerates only `pit["new"]`. A newly differing attribute would still produce that assertion. The saved evidence happens to agree; the writer cannot detect disagreement.

   The same function emits `22_stability.md#C8`'s "equals ... none" unconditionally, and calls the sum of *all* `change_against_movements_added` buckets the number that "differs". An equality bucket would therefore be counted as disagreement. Present evidence supports C8, but the reporting logic cannot falsify it.

3. `22_stability.md#C19` claims "a purchase order is received whole, once". `follow_ups()` checks final quantities and movement counts per line, not whether all lines were received together. Separate line receipts within the interval, or accumulated receipts represented by one movement, fit these observations. The linked relation's `02_meaning.md#C2` explicitly leaves such recording mechanisms unknown; medium confidence cannot confirm this untested rule.

   `22_stability.md#C17` says the rules "are now observed twice". For supplier-payment timing and matching, `b32a2ce5d028571e` contains the identical 366 payments and 2,070 finalized invoices in both extracts. Re-reading unchanged historical events establishes persistence, not a second observed execution of those rules.

4. No design advice or future design decision found in the reviewed readings and linked claims.

VERDICT: FAILS + backorder membership does not establish stock shortage or settle the origin of the 3,078 still-unpicked orders.

## Dispositions

All findings accepted and fixed the same morning (step S08-099):

1. **"A queue, not an artefact"; "C7 holds only for those 5".** C18 now says that almost all unpicked orders are
   backorders not yet supplied, and that why they remain unpicked is not tested; Orders 07 C12 says C7 stays open,
   narrowed.
2. **"Rewritten every day with the same values".** C22 now keeps both alternatives of People 03 C4 open.
3. **C11 not comparing base and new.** write_stability.py now compares the two sets of differing attributes and says
   for how many relations they are the same.
4. **C8's count of disagreements.** It now counts equal and different changes separately.
5. **"Received whole, once".** C19 now says each line was received in full with one movement, and that whether lines are
   received together, or one movement stands for several deliveries, is not tested.
6. **"Observed twice" for rules without new events.** C17 now separates the rules exercised on new rows from the supplier
   payment rule, which gained no new row and was only re-read.

Section 4: none found.

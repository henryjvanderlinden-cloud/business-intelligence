# XREV 2026-10-26 — 147 section 5 and weak case 2: business time per table and how milestones enter valid time — sol

```yaml
object:        docs/10_architecture/147_wwi-concepts-keys-and-business-time.md §5 and §6 item 2, as committed in 1e16609.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write sandbox,
               no browsing; answer written to the ignored scratch/ folder with apply_patch.
assignment:    assume the per-table assignment fails ADR-0027 and try to show it; up to six findings with failure cases;
               recommendation (b) to be tested against two milestones between loads, a corrected milestone, a later
               undated change, header and line milestones disagreeing, and the first-day load; time zones, generated
               history, ADR-0027 itself and satellite splits excluded; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 10 on 2026-10-26; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [a first-day completed row has evidenced existence before its milestone, while recommendation (b)
               can represent either that existence or the completed whole-row state, but not both]. Resolved in the
               revised text by recommending (c), unreviewed.
```

## sol's answer, verbatim


## 1. Recommendation (b) dates an undated change from an old milestone

**Quoted text:** “a version's valid time is the latest milestone stamp it shows, or the event date if it shows none, and a change with no date gets unknown valid time”; and the rows “Purchasing.PurchaseOrderLines | none of its own | `LastReceiptDate` (latest receipt only); finalisation has no date” and “Purchasing.PurchaseOrders | `OrderDate` | finalisation has no date”.

**What is wrong:** The rules give two answers for the same version. A purchase-order-line version whose only change is `IsOrderLineFinalized` still *shows* its old `LastReceiptDate`, so the first clause assigns that receipt date while the last clause requires unknown. A finalized purchase order shows no milestone, so the fallback assigns its original `OrderDate` while the last clause again requires unknown. A timestamp retained on a row is evidence for the milestone it names, not for every later state of that row. Dating the whole version with it violates ADR-0027's “valid time only from source evidence”.

**Concrete failure case:** Extract D1 has purchase-order line L with `LastReceiptDate=2020-01-10`, `ReceivedOuters=10`, `IsOrderLineFinalized=0`. Between D1 and D2 the line is finalized without another receipt; D2 differs only in `IsOrderLineFinalized=1` and edit metadata. Recommendation (b) loads the D2 version valid from 2020-01-10. Under the latest knowledge, an as-of query for 2020-01-11 says the line was already finalized, although the source supplies no date for finalization and it may have happened weeks later. For a purchase-order header, the same failure backdates finalization all the way to `OrderDate`.

**Minimal correction:** State that a carried-forward milestone never dates a later version. If changed attributes have no source business timestamp, that version's valid time is explicitly unknown. Preferably put each dated milestone in its own effectivity/event structure and keep undated row-state changes on knowledge time only.

**Citation check:** `Purchasing/PurchaseOrderLines/03_temporal.md#C2` and `#C5` say that receipt and finalization fields co-changed in one observed daily transition. They do not establish that they always co-change, that finalization occurred on `LastReceiptDate`, or that a retained `LastReceiptDate` dates later changes. `Purchasing/PurchaseOrders/03_temporal.md#C3`, `#C5`, and `#C6` establish column types, one day's finalization changes, and future expected dates; none supplies a finalization date. The note claims more than these claims say.

**Confidence:** high.

## 2. A corrected milestone cannot be represented by “next row” valid-to derivation

**Quoted text:** “a version's valid time is the latest milestone stamp it shows” together with ADR-0027's rule, incorporated by the note, that the raw vault is insert-only, change detection includes time, and valid-to is derived from the next row.

**What is wrong:** A correction of a milestone timestamp is a replacement assertion, not a second business transition. Recommendation (b) has no retraction or supersession rule. Merely inserting the correction and deriving intervals from valid-time order either preserves the erroneous assertion as a real interval or makes the corrected assertion end at the erroneous timestamp. Knowledge time records when the correction was learned but does not by itself say which valid-time assertion the new row supersedes.

**Concrete failure case:** D1 observes an order raised on 2020-01-01. D2 observes `PickingCompletedWhen=2020-01-05 12:00`. D3 observes a timestamp-only correction to `2020-01-04 12:00`; ADR-0027 correctly requires change detection to retain D3. At knowledge time D3, sorting by valid-from and taking the next row gives the corrected D3 version the interval 4 January to 5 January and leaves the erroneous D2 version current from 5 January onward. A current “when was this order picked?” query therefore returns the superseded 5 January value. If the correction moves the stamp later instead, the model manufactures a period during which the source is treated as having changed from one completion instant to another.

**Minimal correction:** Define correction semantics: at each knowledge-time slice, a newer assertion for the same milestone supersedes the older assertion over its whole claimed validity, while prior knowledge slices retain the old assertion. Derive valid-to only after applying that knowledge-time supersession, or represent the milestone as its own bitemporal fact with an assertion identity and retraction.

**Citation check:** `Sales/Orders/03_temporal.md#C5` says no correction was observed in one transition; it does not justify omitting correction semantics. None of the cited claims describes a corrected milestone. The recommendation therefore exceeds its evidence for the required later-extract case.

**Confidence:** high.

## 3. Daily snapshots lose two milestones between loads

**Quoted text:** “`LastReceiptDate` (latest receipt only)” and “milestones ... [are] seen only as the sampled states of daily extracts”, followed by the recommendation that the latest milestone stamp becomes the version's valid time.

**What is wrong:** The note recognizes sampling but still recommends a model that cannot produce correct business-as-of answers from the stated inputs. `LastReceiptDate` is destructive: a second receipt overwrites the first date, and one daily extract can observe only the second cumulative state. No choice of valid-from can reconstruct the intermediate receipt state. Calling the final row valid from the second receipt avoids inventing the first state but makes any answer within the missing interval incomplete; backdating it to the first would invent the later cumulative quantity.

**Concrete failure case:** D1 has line L with `ReceivedOuters=0`, `LastReceiptDate=NULL`. At 09:00 on D2 it receives 4 outers and at 15:00 it receives 6 more; the D2 nightly extract has `ReceivedOuters=10`, `LastReceiptDate=D2` (a date, not a time). Recommendation (b) loads only the state 10 valid from D2. An as-of query for D2 12:00 can return 10, 0, or no known state depending on boundary convention, but can never return the correct 4. On the first-day load, all earlier partial receipts are likewise irrecoverable.

**Minimal correction:** State that correct intraday or between-extract business-as-of answers are impossible for overwritten milestones from daily full extracts. Require CDC/a source log if those answers are in scope; otherwise expose an explicit coverage gap and do not claim correctness between observations. Model each observed receipt separately only when the source actually supplies those events.

**Citation check:** `columns/LastReceiptDate/02_meaning.md#C1` says only “the last date” and expressly says behavior was not verified beyond the other claims. `Purchasing/PurchaseOrderLines/03_temporal.md#C2` and `#C5` observe one aggregate transition; they do not show that there was only one receipt between extracts. The note's “latest receipt only” is supported, but using the citation to imply reconstructible milestone history would exceed it.

**Confidence:** high.

## 4. The first-day rule erases evidenced existence before the milestone

**Quoted text:** “on the first day a row already past its milestone loads as one version, valid from its milestone, and its earlier state is not invented.”

**What is wrong:** Avoiding an invented pre-milestone row state is necessary, but replacing the whole row's valid-from with the milestone also discards a different fact for which the source *does* provide evidence: the order, invoice, or transaction existed from its event date. The milestone dates completion, delivery, or finalization, not entity existence. A single whole-row valid-from cannot honestly express both. Returning no row before the milestone is an incorrect negative, not an explicit unknown attribute state.

**Concrete failure case:** The first-day 2016 load contains order O with `OrderDate=2015-12-29` and `PickingCompletedWhen=2016-06-01` (the pattern actually reported by `Sales/Orders/03_temporal.md#C7`). Loading the only version valid from 1 June makes an as-of query on 2016-01-15 report that O did not exist, although `OrderDate` is source evidence that it had been raised. Loading it from 29 December instead would wrongly assert that its picked state and current payload were true then. The same collision occurs for an already-finalized ledger row whose `TransactionDate` precedes `FinalizationDate`.

**Minimal correction:** Split the event/existence fact, valid from `OrderDate`/`InvoiceDate`/`TransactionDate`, from independently dated milestone facts. Leave the historical values of mutable non-milestone attributes explicitly unknown before their first observation. This is recommendation (c), not (b).

**Citation check:** `Sales/Orders/03_temporal.md#C7` supports “raised, then picked, sometimes long after”; `columns/OrderDate/02_meaning.md#C1` says `OrderDate` is the date the order was raised. These claims contradict using only the later milestone as the whole row's first valid-from. The analogous transaction-table citations establish date columns and current finalization patterns, but not a recoverable complete pre-finalization row image.

**Confidence:** high.

## 5. “None of its own” does not specify the required unknown validity for line state

**Quoted text:** “Sales.OrderLines | none of its own | `PickingCompletedWhen` | header's `OrderDate` through the relationship” and “Sales.Orders | `OrderDate` | `PickingCompletedWhen`”; also, “The line tables carry no date of their own; their header's date is reached through the relationship”.

**What is wrong:** ADR-0027 permits only an evidenced valid time or an explicit unknown. Section 5 uses “unknown” for other tables but a different, undefined value—“none of its own”—for line tables, then supplies the header date through a relationship. That leaves the modeller without an ADR-compliant instruction for an unpicked line's satellite: omitting valid time violates “every satellite carries” it, while copying the header's `OrderDate` asserts without evidence that the line's whole payload became true then. Header and line completion stamps also mean different predicates and need not agree: the source procedure sets the header only when all lines are picked. They cannot repair the missing validity by becoming one document clock.

**Concrete failure case:** D1 first observes order O, dated D0, with two unpicked lines. If “header's `OrderDate` through the relationship” supplies line valid time, a D0 as-of query exposes the D1-observed quantities and prices as though the source had dated them D0; if “none” means no valid-time value, the loader has not recorded validity as explicitly unknown. Later L1 has `PickingCompletedWhen=10:00`, L2 has `PickingCompletedWhen=12:00`, and the header has `PickingCompletedWhen=12:05`. At 11:00 the correct answers are “L1 picked” and “order not fully picked”. A shared document clock would make one of those answers wrong. Separate clocks can answer correctly, but recommendation (b)'s whole-row version rule and the table's “none” value do not specify them.

**Minimal correction:** Replace “none of its own” with “explicitly unknown for line-state satellites”. State that milestone validity is predicate- and grain-specific: line picking, header picking, and their relationship remain separate facts, and header `OrderDate` supplies document context but never the valid-from of a line milestone or line-state version. “As of” views must select each fact on its own valid axis before joining.

**Citation check:** `Sales/Orders/03_temporal.md#C3` (low confidence) says the header is set only when all lines are picked. `Sales/OrderLines/03_temporal.md#C2` and `#C5` show line-level picking changes. The cited claims support distinct grains; they do not support a shared document clock. The section-5 line-row citations `#C3` and `#C5` establish the line's own timestamp, so the later unqualified sentence “line tables carry no date of their own” claims more than those claims say.

**Confidence:** high.

## 6. `SupplierTransactions.FinalizationDate` is assigned milestone semantics without evidence of write-back

**Quoted text:** “Purchasing.SupplierTransactions | `TransactionDate` | `FinalizationDate`” and “`FinalizationDate` (both money ledgers) ... [is a] business time[] written back later, in place”.

**What is wrong:** The supplier-side cited evidence does not show a write-back transition at all. It shows two inserts and zero updates in the only compared day, plus a cross-sectional association between null finalization, outstanding balance, and four current rows. A row may be inserted already finalized, populated retrospectively, or follow the customer-ledger behavior, but only the last possibility supports the note's assignment. Under ADR-0027, an analogy to the other ledger is not source evidence.

**Concrete failure case:** A supplier transaction first appears in the D2 extract already finalized, with `TransactionDate=2020-01-01`, `FinalizationDate=2020-01-03`, and `OutstandingBalance=0`. Recommendation (b) interprets `FinalizationDate` as a later write-back milestone and loads the sole whole-row version valid from 3 January. An as-of query for 2 January suppresses the transaction even though `TransactionDate` evidences its existence; constructing an open version for 1–3 January would instead invent a source state never observed. The source may have inserted the row already finalized on D2, so neither inference is licensed.

**Minimal correction:** Until a supplier transaction transition or source implementation proves the behavior, retain `TransactionDate` as evidenced event time, store `FinalizationDate` as a business-date attribute with its semantics marked unproven, and do not use it to date a row version. Promote it to a separate milestone fact only when source evidence establishes what it timestamps.

**Citation check:** `Purchasing/SupplierTransactions/03_temporal.md#C3` establishes only the column types. `#C6` establishes only the current null/balance association. `#C5`, which section 5 does not cite, explicitly says settlement updates were not seen. The note therefore claims materially more than its citations say. The section-6 sentence cites only the sales tables and supplies no supplier-side support.

**Confidence:** high.

FAILS [a first-day completed row has evidenced existence before its milestone, while recommendation (b) can represent either that existence or the completed whole-row state, but not both without a wrong as-of answer]

## Dispositions

1. **Accepted.** A milestone retained on a row dates its own milestone only; a change the source does not date has
   unknown valid time. Section 5 states it as the first consequence.
2. **Accepted.** A corrected milestone is a replacing assertion that supersedes the earlier one over its whole claimed
   validity at the later knowledge time; "valid to" from the next row is derived within one knowledge-time slice,
   after supersession. Section 5, second consequence. This refines ADR-0027's consequence "valid to is derived in
   views from the next row" without changing its decision; to be put to the author with step C.
3. **Accepted.** Overwritten and repeated milestones between extracts are not recoverable; such history is labelled
   sampled and "as of" answers between observations are not claimed correct. Section 5, third consequence, citing
   that receipts in parts were never observed (`_source/22_stability.md#C19`).
4. **Accepted; the decisive finding.** Recommendation (b) is withdrawn for (c): existence valid from the event date,
   each milestone a fact of its own valid from its stamp. Weak case 2 rewritten.
5. **Accepted.** Line and header picking are distinct facts at distinct grains; the header's date is context for a
   line and never dates its milestone. The sentence "line tables carry no date of their own" is corrected to "no
   event date". Section 5.
6. **Accepted.** No settlement of a supplier invoice was seen in either transition
   (`Purchasing/SupplierTransactions/03_temporal.md#C5`, `_source/22_stability.md#C21`); `FinalizationDate` of the
   supplier ledger is an attribute whose milestone meaning is unproven, and dates nothing. The citation that claimed
   more is replaced.

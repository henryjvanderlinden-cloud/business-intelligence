# XREV 2026-10-28 — 148: the links between the hubs of Wide World Importers — sol

```yaml
object:        docs/10_architecture/148_wwi-relationships.md §2 rules 1 to 7 and the Effectivity column of §3, as
               committed in 005a3d5.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write sandbox,
               no browsing; answer written to the ignored scratch/ folder with apply_patch. A first brief (rules, all
               forty-nine links, section 4, five citations to check, other files open to read) wrote nothing in 14
               minutes; this second brief, confined to the note alone, wrote in about 1.
assignment:    assume a Data Vault 2.0 practitioner rejects the rules and the effectivity assignment; up to five findings
               with failure cases; nothing built, other satellites, the hub list, hashing and time zones excluded; praise,
               summary and general assessment forbidden. Because the reviewer read only the note, its citations were
               not checked against the record in this pass.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 10 on 2026-10-28; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [D1 records O→C1 and D2 corrects O→C2: an event link marked Effectivity = no leaves both targets
               current]. Resolved in the revised text, unreviewed.
```

## sol's answer, verbatim

1. **Quoted text:** “Links are binary… each of its binary links carries the event's hash key and the same load time and batch, so the combination of an order's customer, salesperson and contact is recovered by joining on the order; nothing of the unit of work is lost.”

   **What is wrong:** Equal load metadata is an asserted loading convention, not a constraint that makes independently stored binary relationships one atomic assertion. Joining each link at its latest state can construct a combination that no source row ever stated, especially after a correction or a partial/retried load.

   **Concrete failure case:** Extract D1 contains `(order O, customer C1, salesperson P1, contact K1)`. On D2 the source corrects the row to `(O, C2, P2, K2)`, but only the salesperson and contact link loads succeed; the customer-link load is retried later. A “current order” query that independently selects the latest link returns `(O, C1, P2, K2)`, which occurs in neither extract. With the proposed `Effectivity = no`, it may later return multiple customers, salespeople, and contacts and produce their Cartesian combinations.

   **Minimal correction:** Either retain the source row's multi-hub relationship as one transaction-grain link, or specify and enforce batch-consistent as-of reconstruction for the binary links, including rejection or quarantine of incomplete relationship sets and effectivity for every component that can be corrected.

   **Confidence:** High.

2. **Quoted text:** “An empty column gives no link row… the absence of a scope link is evidence that the scope was empty; the business vault reads it so.”

   **What is wrong:** Absence of a link row is not positive evidence of “all customers.” It is observationally identical to a failed link load, a late-arriving referenced key, a filtered extract, or a query taken before that part of the batch completed. An effectivity satellite cannot close or qualify the initial universal state because there is no link instance to which that state can attach.

   **Concrete failure case:** D1 contains deal `D` with `CustomerID = NULL`, intended to apply to all customers. D2 changes `D` to `CustomerID = C7`. The vault has no D1 relationship row and first receives `D–C7` on D2. The same stored rows result if D1 actually contained `C3` but its link load failed. An as-of-D1 pricing query therefore cannot distinguish “discount every customer” from “relationship missing,” and may discount everyone incorrectly.

   **Minimal correction:** Persist an explicit, historized relationship assertion for the universal scope, with a value distinguishable from missing or failed data, and end-date that assertion when a customer-specific scope begins. Do not derive universal applicability from an anti-join alone.

   **Confidence:** High.

3. **Quoted text:** “Event links whose column was never updated get none until it is seen,” reflected by `Effectivity = no` for links 21–49 except the picker, while “the picker link is dated by its milestone.”

   **What is wrong:** Observed stability is not a temporal model. Once an append-only link without effectivity receives a second target for the same driving key, the link rows alone cannot say which target is current or when the first stopped being valid. The picker milestone supplies a business start time but does not define how a later correction supersedes the prior picker.

   **Concrete failure case:** D1 has `(OrderID O, CustomerID C1)`. D2 corrects it to `(O, C2)`. Both `O–C1` and `O–C2` remain valid-looking link rows, so “current customer for O” returns two rows. Likewise, D1 has no picker, D2 reports `(O, P1, PickingCompletedWhen=t)`, and D3 corrects the picker to `P2` without changing `t`; milestone dating alone makes both picker links valid from `t`.

   **Minimal correction:** Define mutability as a source-contract decision, not as “not yet observed.” Give every re-pointable relationship driving-key effectivity from its first load, with deterministic start, end, correction, and late-arrival rules; alternatively enforce immutability and quarantine any second target instead of loading an ambiguous link.

   **Confidence:** High.

4. **Quoted text:** “Link 25 runs from the original order to the backorder split from it, against the source's description… if a new backorder ever shows the declared direction, the roles swap and the link's key does not change.”

   **What is wrong:** In a recursive link, the two appearances of the same hub have different semantic roles. Swapping those roles changes the assertion even if the unordered pair of business keys is unchanged. Letting observed chronology reverse the source-defined roles makes traversal semantics data-dependent and can create a chain whose arrows do not have one meaning.

   **Concrete failure case:** D1 has row `O1` naming `O2`, and the implementation records `O1 (original) → O2 (backorder)` based on the observed dates. D2 has a new row `O3` whose source column names `O2` in the declared direction; the proposed rule swaps roles and records `O2 (original) → O3 (backorder)`. If the source semantics actually mean “this row is the backorder of the named order,” the real chain is `O1 ← O2 ← O3`, while following the stored arrows yields `O1 → O2 → O3` and reports the wrong original order for O3.

   **Minimal correction:** Fix the two recursive roles from the source column's declared semantics and hash/store them in that order. Treat rows that contradict chronology or the declared meaning as data-quality exceptions; do not reverse roles per row.

   **Confidence:** High.

5. **Quoted text:** “A relationship the source states only by matching values is derived in the business vault,” including “payment ↔ invoices it settles | the ledger entries, matched by customer and day” and “stock issue ↔ invoice line, one to one… matched on invoice and item.”

   **What is wrong:** Equality on a non-identifying tuple can produce candidates, not necessarily a relationship. Uniqueness observed in extracts does not establish a durable business key, and customer-plus-day payment matching is inherently ambiguous when several invoices or payments share that day. Publishing the result as a relationship gives downstream queries unjustified settlement and lineage facts.

   **Concrete failure case:** On day D, customer C has invoices `I1 = 60` and `I2 = 40` and one payment `P = 60`. Matching by `(C, D)` associates P with both invoices, or arbitrarily chooses one; a query for “unpaid invoices” can incorrectly mark I2 paid or double-count the payment as 120. Similarly, if a later extract contains two invoice lines for the same `(InvoiceID, StockItemID)`, one stock issue matches both despite the claimed one-to-one relation.

   **Minimal correction:** Materialize only candidate matches unless a versioned rule supplies deterministic cardinality, tie-breaking, and reconciliation constraints. On any non-unique match, withhold the asserted relationship and expose the ambiguity rather than selecting or multiplying matches.

   **Confidence:** High.

FAILS [D1 records O→C1 and D2 corrects O→C2: an event link marked `Effectivity = no` leaves both targets current].

## Dispositions

1. **Partly accepted.** Accepted: binary links are safe only if the links of one extract become visible together, and
   an "as of" reconstruction selects all links of an event at one knowledge time; Rule 2 now says so, and notes that the
   sandbox's runner already publishes the warehouse only after a whole load succeeds and never skips a failed date.
   Not accepted: one wide link per source row. The event is a hub, the binary links share its key, and effectivity on
   every link (finding 3) ends a corrected component, so the combination a row stated is recoverable.
2. **Accepted.** The naming hub's satellite keeps every optional relationship column as delivered, empty values
   included; "all customers" is read from a recorded empty value, never from a missing link. Rule 4 rewritten.
3. **Accepted; the decisive finding.** Every link gets driving-key effectivity in step C; the column now says where its
   business start comes from (load, event, milestone, absence). A corrected picker ends the earlier picker link at the
   correction's knowledge time. Rule 5 rewritten.
4. **Partly accepted.** Accepted: the two roles of the recursive link are fixed by the source column (the row's order,
   the order named in `BackorderOrderID`) and never swapped per row. Not accepted: fixing the roles' meaning from the
   declared description, which every one of the 7,546 filled rows contradicts; the meaning (which is the original) is
   a reading for the business vault, and a contradicting row is a data-quality exception.
5. **Accepted.** Matches are candidates until a versioned rule fixes cardinality, tie-breaking and a reconciling check;
   ambiguous matches are withheld. For payments the record supplies the check (`analysis/wwi/_source/22_stability.md#C6`);
   a day that fails it gets no match. Section 4 extended.

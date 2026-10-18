# XREV 2026-10-18 — round-1 dossiers of Customers, Suppliers and StockItemTransactions — astra

```yaml
object:        analysis/wwi/tables/Sales/Customers/, Purchasing/Suppliers/ and Warehouse/StockItemTransactions/, as
               generated on 2026-10-18 before this review (uncommitted; the reviewed text is reproduced in the
               dispositions where it changed).
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by sol on three other tables.
assignment:    against ADR-0017 (hard effort, no guessing, confidence supported by evidence) and item 27 of 129: up to
               three false or overstated claims; up to two guesses or unsupported confidences in minimum items; the most
               important missed peculiarity. 450 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the dossiers' judgement claims and the generator of their
               mechanical claims the same day.
verdict:       FAILS [44 stocktake adjustments contradict an "exact", high-confidence filled-reference claim]
```

Astra's answer, verbatim:

1. `analysis/wwi/tables/Warehouse/StockItemTransactions/27_peculiarities.md#C2` says “SupplierID=(empty) (228,476 rows) ... filled CustomerID, InvoiceID”, labelled “exact”. In the 2016-06-01 extract, 44 of those rows have both fields empty; only 228,432 have both filled. Evidence `e43a4464d83ea5fb` rounds empty shares to three decimals: 44/228,476 becomes 0.000. Rounded zero was incorrectly promoted to an exception-free assertion, contradicting C1 and C3 in the same file.

   `analysis/wwi/tables/Sales/Customers/03_temporal.md#C3` says “date-and-time columns without a time zone: none”. Its cited catalogue evidence `4ffc9f716d8c1e42` explicitly lists ValidFrom and ValidTo as datetime2(7). Both occur in the extract. Their system-period role does not remove them from the timestamp inventory; their time-zone interpretation needs its own evidence.

2. `analysis/wwi/tables/Purchasing/Suppliers/03_temporal.md#C3` assigns high confidence to “artefacts of the initial load, not business changes”. Evidence `1a07097101184900` profiles only the current table. Independently inspecting Suppliers_Archive confirms 13 versions ending at 2013-01-01 00:05, but synchronized timestamps do not establish why the changes happened. Initialization is a hypothesis; the generating script or an authoritative process description would settle it.

   `analysis/wwi/tables/Warehouse/StockItemTransactions/19_sensitivity.md#C2` says “personal only where the customer is an individual”, with medium confidence. Its own evidence `02947584dba54bc6` declares LastEditedBy -> Application.People.PersonID. All 236,843 extracted movements carry an editor, spanning 19 IDs. Attribution to identifiable editors is another potential personal-data dimension, independent of customer type. Whether those identities represent real people is unestablished; “only” and the summary “Not personal” are unsupported.

3. The most consequential missed peculiarity is the special meaning of null CreditLimit in Customers. Catalogue evidence `4ffc9f716d8c1e42` describes it as “Credit limit for this customer (NULL if unlimited)”; profile `792f27b06185a023` and the extract show null for all 402 buying-group members, versus finite limits for 261 others. This is a finite/unlimited distinction within one numeric column, relevant to item 27's subtype analysis. `analysis/wwi/tables/Sales/Customers/27_peculiarities.md#C7` substitutes “whose credit is the group's”, which the null pattern cannot establish. A build treating null as missing, zero, or an instruction to inherit a group limit would lose the declared meaning. Group-credit ownership remains unknown pending business-rule evidence.

VERDICT: FAILS — 44 stocktake adjustments contradict an “exact”, high-confidence filled-reference claim.

## Dispositions

All five findings accepted and fixed the same day, before the dossiers were committed:

1. **"Exact" from rounded shares.** The profile rounded empty shares to three decimals, so 44 of 228,476 showed as 0 and
   the generator called the split exact. `profile_tables.py` now records empty counts per value, and the generator
   decides exactness from counts; every table's evidence was regenerated. The claim now reads "partial", naming the
   44 rows.
2. **Period columns left out of the timestamp inventory.** The temporal claim now lists ValidFrom and ValidTo as
   system-time period columns, datetime2 without a zone.
3. **"Artefacts of the initial load" at high confidence.** Split into the observed timing (high) and the reading
   (intended, low, cause not established).
4. **"Not personal" where every row names an editor.** The generator adds, for every table with LastEditedBy, that each
   row attributes work to identifiable staff; the judgement summaries no longer say "not personal".
5. **CreditLimit NULL means unlimited.** Added as a declared special value (test 10); the unsupported reading "whose
   credit is the group's" was removed.

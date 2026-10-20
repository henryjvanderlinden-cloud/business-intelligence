# XREV 2026-10-20 — position in the schema (item 29), readings and method — astra

```yaml
object:        item 29 as first written on 2026-10-20 (uncommitted): docs/10_architecture/131_structural-position.md,
               docs/20_decisions/0021-position-in-the-schema.md, and the readings in analysis/wwi/_source/29_position.md
               and analysis/wwi/tables/*/*/29_position.md with the files they link to.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file.
assignment:    against ADR-0017, ADR-0020, ADR-0021 and analysis/README.md sections 4 to 6: readings beyond their
               evidence or links; places where 131 would mislead on another source; whether the author's distortion
               principle is stated faithfully and applied consistently, behaviour included; any design advice. Praise,
               summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote 131, ADR-0021, structure.py, write_position.py and the
               readings the same evening.
verdict:       FAILS [an established stock disagreement presented as open; the extension rule overstates parent coverage]
```

Astra's answer, verbatim:

1. `analysis/wwi/tables/Warehouse/StockItemHoldings/29_position.md#C7`: "stock levels whose agreement with the movements is open". The linked `analysis/wwi/across/reconciliations/stock-holdings-vs-movements/16_reconciliation.md#C1-C4` establishes disagreement for both levels and daily changes in the tested extracts. Only its cause is unknown (C5). Calling agreement open obscures an established negative finding.

   `analysis/wwi/_source/29_position.md#C8`: "without any process running along those paths". Evidence `db4260aed02cacc4` measures schema paths, not process absence. The process dossiers follow selected order, procurement and stocktake chains; they do not establish that no process uses these paths, particularly SpecialDeals. "Betweenness does not establish process flow" follows; the categorical negative, at medium confidence, does not.

2. In `docs/10_architecture/131_structural-position.md` section 5, extension means "one row per row of another table". A child primary key that is also a foreign key establishes at most one child per parent, not complete parent coverage. A parent with two rows and an extension containing only one satisfies the rule but contradicts its explanation. Coverage needs separate evidence.

   Section 8's instruction to set `SOURCE`, `DAYS` and `BASE`, then run the writer, is insufficient for another source. `prototypes/information_analysis/write_position.py` hardcodes `analysis/wwi` and `wwi` identities, and selects its evidence there. The transition probe also delegates to separately configured `profile_tables.py`. Changing the named constants in `structure.py` does not configure the whole pipeline; the text omits those dependencies.

3. Both documents faithfully quote the author: "The lesson is not to always exclude audit attributes, but to be cautious and sensitive to excluding attributes etc. that give a distorted picture of reality." The graph comparison implements that principle. Behaviour applies it incompletely: `analysis/wwi/tables/Application/People/29_position.md#C8` still says "It changes without growing" although only ValidFrom changed; linked temporal C4 explicitly distinguishes a new version from a visible change. StockItemHoldings C4 retains "every row updated daily"; C6 exposes the audit-only contribution, but C7 does not explain it and incorrectly says QuantityOnHand changed "on all but one" in both transitions. The readings module now contains the explicit audit qualification and distinct counts, but the written record does not. Recording changed columns makes distortion inspectable; it does not itself qualify the behaviour label.

4. No model, KPI, reporting-date or loading proposal found in the reviewed item-29 readings. Graph exclusions and structural "hubs" describe the adopted analysis method, not a warehouse design under ADR-0020.

VERDICT: FAILS — established stock-reconciliation disagreement is presented as open, and the extension rule overstates parent coverage.

## Dispositions

All findings accepted and fixed the same evening (step S08-107):

1. **Holdings "agreement ... is open".** The reading now says the levels disagree with the movements in level and in
   daily change (16_reconciliation.md#C1, #C2), for a cause the record leaves unknown.
2. **"Without any process running along those paths".** The source claim now says that a high betweenness does not
   establish that data or a process flows through a table; the Cities reading names the three processes recorded and
   says another process is not tested.
3. **Extension "one row per row".** 131 and the rule text now say *at most* one row per parent row; a new claim per
   extension table counts its rows against the parent's (227 for 227).
4. **Section 8 not enough to run on another source.** `write_position.py` now takes the source as an argument and no
   longer names WWI; 131 section 8 lists every place the prototypes name the source (structure.py, profile_tables.py,
   relations.py) and the order of runs.
5. **Behaviour labels not qualified by the distortion principle.** The behaviour is now computed on the columns other than
   the key and the audit columns, from a row-by-row comparison: People is labelled "only audit or system-time columns
   change", StockItemHoldings "changes without growing" (226 and 225 of 227 rows changed in a business column). 131
   section 3, point 5 says so. The stale People and Holdings texts astra quoted were a writer run that preceded the last
   edit of the readings; the files were regenerated.

Section 4: none found.

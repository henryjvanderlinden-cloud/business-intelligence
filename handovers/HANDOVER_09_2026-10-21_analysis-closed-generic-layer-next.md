# nsdn — Handover 09: the information analysis of Wide World Importers is closed; the generic integration layer is next
## Written 2026-10-21 at the close of session 08

> **STATUS: CURRENT.**

---

## First actions

1. `git status`, then `git log --oneline -15`. Expect HEAD at the commit that closed S08 (message begins "Close session
   08"). The author pushes himself; if `origin/main` is behind, say so, do not push.
2. `python tools/check_repo.py` — must pass (the 7 known errors under `scratch/vdl-diaa-logo` excepted, if that folder
   is still there). **On the desktop's Linux shell the full check takes minutes and hits the 180-second limit**; see
   *Traps*. Expect 8 sessions, S08 closed with `AUD-S08-1`.
3. Read, in this order: [ADR-0022](../docs/20_decisions/0022-the-analysis-stage-closes.md) (what the analysis is now),
   the `ARC-OP-36` paragraph *Close of the analysis stage* (what it covers), [`analysis/README.md`](../analysis/README.md)
   (how the record is laid out), then [140](../docs/10_architecture/140_data-vault-automation.md),
   [142](../docs/10_architecture/142_the-data-model.md), [127](../docs/10_architecture/127_temporal-behaviour.md) and
   [ADR-0013](../docs/20_decisions/0013-data-vault-or-equivalent.md), [ADR-0015](../docs/20_decisions/0015-sandbox-warehouse-dbt-duckdb.md).
4. Ask the sandbox job for its status (handover 08, *Driving the sandbox*). Expect simulated date 2016-06-02; 17.2 GB was
   free on 2026-10-21.
5. Open session S09 in `records/sessions.jsonl` and log from S09-001.

## Where we stand

**The analysis stage of the first trial is closed** (ADR-0022, ruled by the author 2026-10-20 21:51). Under
`analysis/wwi/` the record holds 1,303 item files and 4,892 claims, each with its confidence and evidence:

- **every table**: granularity, temporal behaviour, role, keys, population, sensitivity and peculiarities (the minimum
  and item 27) for the 31 base tables; role and position in the schema (item 29) also for the 17 history tables; the
  meaning of all 368 columns;
- **numbers**: measures, derived columns and arithmetic (items 8, 9, 28) for the 17 tables with numeric columns;
- **across tables**: 100 relations with their minimum items and point-in-time behaviour, 6 reconciliations, 3 processes
  (order to cash, procure to pay, stocktake), 8 terms, 5 entities, `across/candidates.md` for undeclared relations;
- **the source**: documentation, stability against a second day, position in the schema.

187 files carry a claim of unknown confidence: the record's open questions (`grep -rl "confidence: unknown"
analysis/`). The files describe the extract of 2016-06-01; `_source/22_stability.md` rechecks them against 2016-06-02.
The lessons of the trial are in
[2026-10-20-information-analysis-trial-lessons](../docs/30_research/notes/2026-10-20-information-analysis-trial-lessons.md).

**The method is reusable**: 129 (the inventory), `analysis/README.md` (the record), 131 (position in the schema), and
the scripts in [`prototypes/information_analysis/`](../prototypes/information_analysis/README.md) with their run order.
Turning it into skills is held (`PRC-OP-8`) until the author asks.

**Nothing is built on the extracts yet**: no load, no integration layer, no mart, no test.

## Task for the next session, in one sentence

With the author, design the generic integration layer for Wide World Importers (Data Vault or a functional equivalent,
ADR-0013) from the analysis record, and put to him as decisions whether it is bitemporal and how derived measures and
calculations are handled.

## Scope

**In.** The integration layer's structures for the 31 base tables and their history tables: what becomes a business
key, a relationship, a descriptive set, and with what history (140, 142, `ARC-OP-29` on the model as text). The
temporal question: SQL Server keeps system time on 17 tables; business dates sit on the events; milestones are written
back onto rows later (picking, delivery, invoice finalisation, payment); the record is per table under item 03 and per
relation under `across/relations/*/03_temporal.md` (127, 190, `ARC-OP-13`, `ARC-OP-27`). Derived values and
calculation: items 8, 9 and 28 hold what the source computes and how it rounds (160 and 162 on plausibility and tests,
`ARC-OP-31`). The two customer roles the author noted for this phase (`ARC-OP-36`, round-2 paragraph).

**Out unless he asks.** Loading code and dbt models (ADR-0015 says where they will run, not when); marts, KPIs and
reports; a second source; the agent team (`ARC-OP-34`); quality gates (`ARC-OP-33`); the skills (`PRC-OP-8`).

**Where the record helps most.** Keys and candidate keys: `tables/*/*/06_keys.md`. Relations and their cardinality,
optionality and orphans: `across/relations/`. Entities and terms: `across/entities/`, `across/terms/`. Subtypes,
exclusive arcs, events carrying state, aggregates on headers: `tables/*/*/27_peculiarities.md`. Class of each table
(event header or record, master, lookup, bridge, extension, configuration, state, history): `29_position.md`, with
business readings beside the class. Measures and formulas: `08_measures.md`, `09_derived.md`, `28_arithmetic.md`.

## How to work with the author

As in handovers 07 and 08: plain English, numbered points; propose, let him react, write what he settles; quote him
verbatim; everything tentative until he rules it. **ADR-0020's restraint no longer binds the conversation**: design
questions - keys, model, temporality, measures - may now be put to him (ADR-0022, decision 5). It still binds the files
under `analysis/`: design goes into `docs/`, ADRs and the model's own files, which cite the analysis claims they rest
on; a fact found while modelling goes into the record as a claim with evidence. Review on sol and astra in parallel,
framed against the standard the object must meet (`PRC-OP-7`). Minimise his manual work and count what you ask of him.

## Traps and warnings

**Expect your first version to fail review.** All 19 cross-model reviews of the analysis failed the first version, 9
of 11 recorded defect entries for claiming more than the evidence shows: a reading presented as an observation, a
formula called the source's rule because the data fit it, a comparison that could not fail. In design work the
equivalent is a structure justified by a fact the record does not hold. Cite the claim (`path#Cn`) behind each design
choice; where there is none, say so.

**The distortion principle** (the author's, ADR-0021): be cautious about leaving out attributes that would distort the
picture, and say why when you do. `LastEditedBy` ties every table to `Application.People`; audit and system-time columns
make rows look changed when no business value changed. Both graphs and both behaviours are recorded.

**Do not turn classes into designs silently.** Item 29's classes (event, master, lookup, ...) look like a ready-made
mapping to hubs, links and satellites. They are a description of the source; the mapping is the design work, and the
cases where the class and the business reading differ (the geography tables, `Sales.SpecialDeals`) are exactly where
it needs the author.

**Things the source does that a model must not lose**: an order's value is stored nowhere (order lines carry quantity,
price and tax rate only); an invoice's tax is the sum of rounded line taxes, not a rate on the total; `LineProfit` and
the expected purchase price follow the *current* cost price; `OutstandingBalance` is a state overwritten on payment, and
no key links a payment to the invoices it settles; `TotalDryItems` counts lines, not goods; stock levels in
`Warehouse.StockItemHoldings` disagree with the movements for a reason not established; "orders" means two things
(item 27). All with their claims in the record.

**The record ages.** Its files describe 2016-06-01. If the simulation is advanced, rerun the recheck
(`recheck.py`, `write_stability.py`) rather than editing files; ADR-0022 keeps the record open, not unattended.

**Generated files are regenerated, never edited by hand.** Every item file comes from a writer script and a readings
module (`scratch/ia_specs/*.py`). Edit the readings, rerun the writer, and check the output before review: once in S08
a stale file went to review. Evidence is content-addressed: a rerun gives a new hash; move the old evidence to
`scratch/_superseded/` (deletion on the desktop needs the author's approval) and never edit evidence. Timestamps in
readings modules (`NOW`) must not lie in the future; the desktop shell's clock is UTC.

**The desktop shell is slow; the cloud workspace is fast.** Whole-repository checks take minutes on the desktop's Linux
shell and time out; the same `tools/check_repo.py` runs in under a second on a copy in the cloud workspace. What worked
in S08: zip the repository on the desktop (include `handovers/`, `prototypes/`, `tests/`, `spec/`, or their links show
as broken), stage the zip, check and run heavy scripts in the cloud, send results back as a zip and unpack with Python.
`networkx` is not installed on the desktop shell.

**git on the desktop leaves lock files** because deleting in a connected folder is not approved: after each commit,
rename `.git/HEAD.lock`, `.git/index.lock` and `.git/objects/maintenance.lock` if present (mv to `.git/stale-...`),
never under `.git/refs`.

**Codex calls time out at the bridge after 60 seconds by design**; the run continues. Have the reviewer write to
`scratch/` and read the file. A broad brief to sol sometimes writes nothing; a narrower one does.

**The step-log labels for analysis work are contested.** `AUD-S08-1` agreed with the recorder on task type for 6 of 20
steps: the recorder labelled information-analysis work *modelling*, the auditor *profiling* or *matching*; the
vocabulary has no type for information analysis. From now on *modelling* will be the right label for most work, which
makes the distinction matter. Whether to add a type, or read the existing ones differently, is the author's to rule;
do not change the vocabulary silently.

## Outstanding for the author, not the model

**Push** (he pushes himself). **The task type for information analysis** (above). **The two guards** from session 06,
still unruled since handover 07: no de-anonymising business-for-sale listings; no named individuals.

## Driving the sandbox

Unchanged from handover 08: request files in `data/wwi/requests/`, four actions (`status`, `advance`, `export`,
`query`), one request per job run, the newest three extracts kept (now 2016-05-31, 2016-06-01, 2016-06-02),
`data/frozen` never touched, no row edits, no `setup.ps1 -Reset`. The author said on 2026-10-20 to keep the simulation
at two days for now: do not advance it without asking.

## What session 08 did

Session 08 ran from 10 to 21 October. It began on loads, scheduling and change capture and on BCBS 239 (152,
`ARC-OP-35`), then turned, on the author's point of 2026-10-18, to an information analysis before anything is built:
the inventory (129, ADR-0017), its record (`analysis/README.md`, ADR-0018), two rounds (ADR-0019), the as-is rule
(ADR-0020), round 1 for every table and column, round 2 across tables, a second simulated day and its recheck,
position in the schema (131, ADR-0021) and the numeric items, and closed the stage (ADR-0022). It held the distilling
of the work into skills (`PRC-OP-8`). It closed with the blind audit `AUD-S08-1`.

## Do not reopen

Everything in handovers 06 to 08, plus:

- The analysis precedes building, best effort beyond the minimum, never a hard gate (ADR-0017); its record and layout
  (ADR-0018, ADR-0019); two rounds, per table then across tables (ADR-0019).
- The analysis files describe the as-is and carry no design, now and after the stage (ADR-0020, ADR-0022).
- Item 29, its method and classes, and the distortion principle (ADR-0021, 131).
- The analysis stage of this trial is closed; its record stays open for facts (ADR-0022).
- The sandbox holds test data, so its sensitive columns may be loaded (the author's ruling of 2026-10-18, step S08-058).
- Source data rows are never committed; evidence holds aggregates only.
- Windows-side repairs are the author's; Codex's sandbox stays read-only for anything on Windows and writes only its
  review answers to `scratch/`.

## What was not done

No integration layer, load or test exists. Items 10 to 13 and 15 to 17 are not recorded as items of their own;
provenance, ownership and demand (14, 20, 21) could not be done without people. The 187 questions of unknown confidence
are open. No rule of the record has been seen on a weekend, at a period end, or over more than two transitions.

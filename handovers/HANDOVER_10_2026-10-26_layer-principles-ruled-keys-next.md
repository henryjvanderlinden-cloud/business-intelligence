# nsdn — Handover 10: the integration layer's principles are ruled; concepts and keys for Wide World Importers are next
## Written 2026-10-26 at the close of session 09

> **STATUS: CURRENT.**

---

## First actions

1. `git status`, then `git log --oneline -15`. Expect HEAD at the commit that closed S09 (message begins "Close session
   09"). The author pushes himself; if `origin/main` is behind, say so, do not push.
2. `python tools/check_repo.py` — must pass, apart from the 7 known errors under `scratch/vdl-diaa-logo`. Do not run it
   on the desktop's shell, which is too slow (see *Traps*); run it on a copy in the cloud workspace. Expect 9 sessions,
   S09 closed with `AUD-S09-1`.
3. Read, in this order: [ADR-0027](../docs/20_decisions/0027-bitemporal-integration-layer.md) (time),
   [144](../docs/10_architecture/144_raw-vault-business-vault-calculation-engines.md) §2, §3 and §5 (the raw/business
   line, several sources, what it means for WWI), [ADR-0024](../docs/20_decisions/0024-calculation-engines-are-a-versioned-source.md)
   and [ADR-0025](../docs/20_decisions/0025-engine-results-in-the-raw-vault.md) (engines),
   [ADR-0026](../docs/20_decisions/0026-conformed-dimensions-and-fact-table-changes.md) and
   [146](../docs/10_architecture/146_fact-tables-and-new-questions.md) (marts), then the register row `ARC-OP-37`. Then
   handover 09's paragraph *Where the record helps most*, which still holds, and
   [`analysis/README.md`](../analysis/README.md).
4. Ask the sandbox job for its status (handover 08, *Driving the sandbox*). Expect simulated date 2016-06-02; 18.51 GB
   was free on 2026-10-21.
5. Open session S10 in `records/sessions.jsonl` and log from S10-001.

## Where we stand

Session 09 settled the principles of the generic integration layer with the author, in his rulings of 25 and 26
October, each recorded verbatim:

- **Calculation engines** ([ADR-0024](../docs/20_decisions/0024-calculation-engines-are-a-versioned-source.md)):
  business rules and calculations beyond basic arithmetic run in versioned software (Python), not SQL; every result is
  stored with its engine version and is a separate source; recompute everything on a new version when affordable; a
  new version, and a rerun with corrected inputs, are new rows even when the values are unchanged.
- **Engine results land in the raw vault**; when recomputation cannot be afforded, a cut-off date first, then going
  forward only, each step adjudicated ([ADR-0025](../docs/20_decisions/0025-engine-results-in-the-raw-vault.md)).
- **Marts**: conformed dimensions; design is about fact tables; extending a fact table is a fundamental, adjudicated
  decision, except a minor extension, which needs none
  ([ADR-0026](../docs/20_decisions/0026-conformed-dimensions-and-fact-table-changes.md)); 146 holds the considerations
  and the preconditions for "minor".
- **Time**: the layer is bitemporal on evidence, with source system time as a labelled third timestamp; the agent
  proposes each table's business time and the author rules only on weak evidence
  ([ADR-0027](../docs/20_decisions/0027-bitemporal-integration-layer.md)).

Proposed and **not ruled**, under `ARC-OP-37`: the raw/business line as revised after review (provenance decides; item
1), the rules for several sources (key composition by issuer, collision codes, links by meaning, matching kept in
proposal/decision/publication; item 2), the engine conditions added after review (environment digest, input manifest,
run record, fallback policy record; item 4), and where marts take their data from (item 8). The author's route of
2026-10-21 (concepts and keys, relationships, descriptive sets, time, derived values, write-up) was not ruled as a
whole; on 2026-10-26 at 16:16 he asked to start the next conversation with step A and the business-time proposal.

**Nothing is built**: no model files, no load, no dbt model, no test.

## Task for the next session, in one sentence

Propose, for all 31 base tables of Wide World Importers and from the analysis record, the business concepts with their
business keys (step A: what becomes a hub, with each key's composition and key space) and each table's business-time
column (ADR-0027 decision 4), citing the claim behind every choice, review them on another model, and bring the author
only the cases where the evidence is weak.

## Scope

**In.** Concepts and business keys for the 31 base tables and their history tables: which tables yield a hub, on which
key, with the key's issuer or namespace and grain (144 §3 item 2), and which do not (lookups, configuration, bridges,
extensions; 131's classes are a description, not the mapping). The business-time proposal per table: which column, if
any, is business valid time, which is source system time (the period columns of the 17 system-versioned tables,
`LastEditedWhen`), and where valid time is unknown. Where the record lacks a fact, add it to the record as a claim with
evidence (ADR-0022), not to the design.

**Out unless he asks.** Relationships (step B) beyond what a key needs; satellites (step C); loading code, dbt models
and the model-file format (`ARC-OP-29`, `ARC-OP-20`); engines; marts; quality gates (`ARC-OP-33`); the skills
(`PRC-OP-8`).

**Where to look.** Keys: `analysis/wwi/tables/*/*/06_keys.md`. Time: `03_temporal.md` per table and
`across/relations/*/03_temporal.md`. Classes and business readings: `29_position.md`. Entities and terms:
`analysis/wwi/across/entities/`, `across/terms/`. The two customer roles and the two meanings of "orders": `ARC-OP-36`
round-2 paragraph and item 27 files.

## How to work with the author

Plain English, numbered points; propose, let him react, write what he settles; quote him verbatim; everything tentative
until he rules it. He asked that only weak-evidence cases come to him: count what you ask of him. Review on sol (and
astra if it answers), framed against the standard the object must meet (`PRC-OP-7`). When he rules, record it the same
turn, in an ADR or the register, and commit.

## Traps and warnings

**Expect your first version to fail review.** All four sol passes of 2026-10-26 failed the first version: a placement
test that a source-computed value passes both ways; a migration split loaded as same-as; a rerun that leaves no row;
"minor" fact-table changes that alter totals. Two citations claimed more than their claims say. Cite `path#Cn` for
every key and time choice, and say so where there is none.

**WWI's keys are integer identifiers whose issuing scope is not established** (144 §5); for `OrderID`, whether it is
known outside the database is open (`Sales/Orders/06_keys.md#C7`). Under 144 §3 such keys get a key-space code unless
there is evidence of a governed namespace. Do not assume either way.

**Database edit time is not business time.** The period columns of the system-versioned tables record edits (a
`Countries` version stamped 2022; all stock items re-versioned on 2016-05-31 23:00-23:12). Milestone stamps
(`PickingCompletedWhen`, `ConfirmedDeliveryTime`, `FinalizationDate`) are written back later, in place: they are
business times of the milestone, captured only as sampled states. These are exactly the weak-evidence cases.

**Do not turn item 29's classes into hubs silently**, and keep the distortion principle (ADR-0021): `LastEditedBy` ties
every table to `Application.People` for no business reason.

**Astra did not answer on 2026-10-26.** Two attempts (one broad, one narrow) wrote nothing in 13 and 12 minutes; the
same briefs on sol wrote in about 3 minutes. What worked: a narrow brief naming `apply_patch` and an answer file directly
in `scratch/`, not in a subfolder; Codex calls time out at the bridge after 60 seconds by design and keep running.

**The desktop shell.** `check_repo.py`, zip and `git archive` all hit the 180-second limit there. What worked:
`tar -czf` of the repository (without `.git` and `data/raw`, `data/warehouse`, `data/derived`) to the shell's local disk
(`$HOME/xfer`), then `cp` into `scratch/_transfer/` (about 2.5 minutes in all), stage it and check in the cloud. For
small changes, stage only the changed files onto a cloud copy. Background jobs do not survive between calls. Git is
slow because `.git/objects` holds 7,769 loose objects, no pack, and over 6,700 `tmp_obj` files it cannot delete; the
author's `git gc` from Windows would fix it.

**The desktop's clock is UTC**, and step timestamps in local time were twice set in the future in S09 and had to be
corrected. Take the time from the shell before writing a step.

**Git leaves lock files** (deletion not approved): after each commit, `mv` `.git/HEAD.lock`, `.git/index.lock` and
`.git/objects/maintenance.lock` to `.git/stale-...`, never under `.git/refs`.

**Step labels for design work.** The checker requires `assets` on every step of a data task type, `modelling`
included, so design conversation in S09 was labelled `planning`. The blind audit `AUD-S09-1` read 15 of those 20
steps as `modelling` (task type agreed on 2 of 20). Whether to add a task type, relax the checker for design work, or
read `planning` this way is the author's to rule; do not change the vocabulary or the checker silently. Step A will
touch the analysis record and the extracts, which are assets, so `modelling` with `assets` may fit it.

## Outstanding for the author, not the model

**Push** (6 commits were unpushed before the close). **`git gc`** in `C:\Git\business-intelligence`. **The task type for
design and information analysis** (above, with `AUD-S09-1`). **`ARC-OP-37` items 1, 2, 4 and 8**, best judged once
step A shows them on real tables. **The two guards** from session 06, unruled since handover 07. **Two commits of
2026-10-25** (`0951076`, `5d3d777`, the financial-services notes and ADR-0023) were made in another conversation and
appear in no session's step log; whether they belong to S09 is for him to say.

## Driving the sandbox

Unchanged from handover 08: request files in `data/wwi/requests/`, four actions (`status`, `advance`, `export`,
`query`), one request per job run, the newest three extracts kept (2016-05-31, 2016-06-01, 2016-06-02), `data/frozen`
never touched, no row edits, no `setup.ps1 -Reset`. The author said on 2026-10-20 to keep the simulation at two days; do
not advance it without asking.

## What session 09 did

Session 09 began on 2026-10-15 with the BCBS 239 tangent (152, ADR-0016, `ARC-OP-35`, steps S09-001 to S09-007), picked
up handover 09 on 2026-10-21, and on 25 and 26 October worked through the author's questions on the raw and business
vault, several sources for one entity, calculation engines, marts and time. It wrote 144 and 146, ADR-0024 to ADR-0027
and `ARC-OP-37`, corrected note 030, ran four review passes on sol (all failed the first version, all applied, four
XREV notes), and closed with the blind audit `AUD-S09-1`.

## Do not reopen

Everything in handovers 06 to 09, plus:

- Business rules and calculations run in versioned engines; results stored with their version; a new version and a
  corrected rerun are new rows even with equal values (ADR-0024).
- Engine results land in the raw vault; the recomputation fallback (ADR-0025).
- Conformed dimensions; fact-table extension is adjudicated, minor extensions are not, under 146's preconditions
  (ADR-0026 and its note).
- The layer is bitemporal on evidence; source system time is labelled and never business time; the agent proposes
  business time per table (ADR-0027).
- Note 030 §2 item 5 is corrected; the raw vault holds what systems delivered, including source-computed values.

## What was not done

Step A and the business-time proposal. A ruling on the route beyond step A. Review of ADR-0027 and of the texts
revised after the four reviews. Any counter-review on astra. `ARC-OP-37` items 1, 2, 4 and 8.

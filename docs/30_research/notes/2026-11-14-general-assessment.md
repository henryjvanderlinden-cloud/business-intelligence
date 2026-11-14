# A general assessment of the repository, as it stood on 2026-11-14

**Status: written 2026-11-14, session 12, by Claude Fable 5.2 (`claude-fable-5-2`), a different model from the one that
drafted the repository, in a conversation separate from the one that ran S12-001 to S12-027; unreviewed.** The question
it answers is the author's, verbatim:

> Could you please go over the entire project that is in the GIT repository called business-intelligence (see the
> attached folder), and give me your general assessment of it ?

Having read it, he asked: "please store this assessment somewhere appropriate, maybe point to it from the open
register." The pointer is in [`PRC-OP-1`](../../../registers/OPEN_POINTS.md).

**Added 2026-11-14, 19:15.** The author then opened [`PRC-OP-10`](../../../registers/OPEN_POINTS.md), as an exception, to
work through these points with Opus and see where each lands. The note itself is unchanged.

**What this note is and is not.** It is one reader's impression of the whole repository at commit `21d47cf`. It is not
an external review pass: [510](../../50_process/510_external-review.md) asks for one object per pass and a determinate
question, forbids general assessment, and warns that a whole-corpus read returns weaker findings than a refutation of
one object. Weigh it accordingly. It decides nothing and opens no register row. Points 16 to 19 are suggestions the
author has not ruled on.

**What was read and run.** Read: the entry documents ([`README.md`](../../../README.md),
[`AGENTS.md`](../../../AGENTS.md)), the concept and process documents, the ADR index and several ADRs,
[handover 12](../../../handovers/HANDOVER_12_2026-11-03_declarations-viewer-and-pg-pass-done-generator-next.md), parts
of the register, the generator and sandbox code, and samples of the analysis record, the step log and the review notes.
Not read: every one of the 2,745 tracked files; most of the 84 research notes; most of the register's 71 rows in full.
Run, on a copy of the tracked files: `python tools/check_repo.py` (passed, with the 3 known warnings in `S07.jsonl`)
and `python prototypes/vault_generator/generate.py --check` (510 generated files, 0 problems). Not run: the load suite
(`test_load.py`) and the PostgreSQL catalogue test, so every load figure below is the repository's own, taken from
[the generator's README](../../../prototypes/vault_generator/README.md) and `records/steps/S12.jsonl`.

## In one sentence

This is a serious, unusually disciplined piece of work whose engineering core is sound; its main weakness is that the
claim the project exists to test is still untested, while a lot of effort has gone into the part that was always going
to work.

## What is strong

1. **The architecture holds together.** Models stay out of the data path
   ([ADR-0004](../../20_decisions/0004-models-out-of-the-data-path.md)), autonomy is tiered by kind of claim
   ([ADR-0005](../../20_decisions/0005-three-autonomy-tiers.md)), and declarations feed a generator that writes plain
   SQL ([ADR-0032](../../20_decisions/0032-generated-sql-machinery.md)). The author's own requirements are met: small
   text files, lightweight open source, and a runner that works with the agent layer down.
2. **The raw vault is real and well tested.** It covers all 31 Wide World Importers base tables as 216 vault tables,
   with 777 tests per load. Five simulated days are recorded as loading identically on two machines (S12-025), and
   every delivered version is recorded as reconstructing exactly from the satellites.
3. **The analysis record is the most reusable asset.** It holds about 1,300 item files and 4,910 claims, each with
   evidence, a confidence and a recheck trigger ([`analysis/README.md`](../../../analysis/README.md)). This, with the
   [catalogue pass](../../../prototypes/catalogue_pass/README.md) and the
   [schema viewer](../../../prototypes/schema_viewer/build.py), is what carries to a client's PostgreSQL database.
4. **Cross-model review earns its keep.** The reviewer found real defects, such as rows of a failed rebuild surviving
   its retry ([XREV of 2026-11-04](XREV_2026-11-04_143-generated-sql_sol.md), finding 1).
5. **The repository is honest about itself.** Handovers state what was not done, and refuted arguments stay visible.

## What gives concern

6. **The central bet is untested.** [410](../../40_roadmap/410_first-vertical-slice.md) says the one thing that is
   "either true or not" is whether business keys and cross-source entity identity can be machine-proposed at a useful
   precision. Wide World Importers is a single, clean, documented source with declared keys, so it cannot test that.
   The Utrecht sandbox touched it (three of three right on a blind answer key,
   [post-mortem of session 06](2026-09-26-session-06-post-mortem.md) lesson 5) and was parked. `EVI-OP-1`, the ground
   truth, has been open since session 01, and `PRC-OP-1` already records that every review pass has stepped around
   this claim.
7. **Generality is asserted, not shown.** [`generate.py`](../../../prototypes/vault_generator/generate.py) handles
   exactly one source, maps SQL Server types only, and lives under the WWI sandbox. A client case with a PostgreSQL
   database, extract feeds from other sources and probably weak keys would meet all three.
   [ADR-0037](../../20_decisions/0037-vault-generator.md) names a second source as a reason to revisit, and the general
   rules for several sources are open under `ARC-OP-37`.
8. **Nothing a business user would see exists.** There is no business vault, mart or analysis yet (`ARC-OP-37`;
   phase 3 of [400](../../40_roadmap/400_phasing.md)), so there is nothing to show a prospect beyond the schema viewer.
9. **The "agent layer" is a chat session plus conventions.** No context layer, adjudication queue or agent loop exists
   as software. `PRC-OP-8`, on turning the procedures of the work into skills, is held, yet that is arguably the
   product.
10. **Adjudication is thin.** In the analysis record 4,908 claims are still `proposed` and 3 are retracted; no item file has a `reviewed_by` or a `ruled_by`, although review notes cover the work in batches. The
    generator's design was ruled with "agree, agree, agree" (ADR-0037). The tests protect the vault; nothing comparable
    protects the claims about meaning.
11. **Load time is a warning sign.** A daily load takes 572 seconds on the author's machine after the fix of generator
    0.2.1, and took about 1,330 before it (S12-025, S12-027), on a small sample database, because full extracts and
    whole histories are read again each day. ADR-0037 already names slow loads as a reason to revisit.
12. **The register only grows.** It has 71 rows and none has ever been closed (64 open, 6 ruled, 1 held). It is one
    file of 3,190 lines, against rule 6 of `AGENTS.md` (split at roughly 400). `CON-OP-2`, the economics figure
    described in session 01 as cheap and to be done early, still has no number. `PRC-OP-5` and `PRC-OP-2` say the same
    of the register and the apparatus in the repository's own words.
13. **The conceptual foundation was left half-finished.** Section III of the
    [manifesto](../../00_concept/005_manifesto.md) has carried its "under challenge" notice since 2026-09-19
    (`CON-OP-5` to `CON-OP-8`), and the [mission statement](../../00_concept/002_mission-statement.md) is unratified
    (`CON-OP-15`).
14. **The step log cannot yet support the maintenance measure.** The blind audits in
    [`records/audits.jsonl`](../../../records/audits.jsonl) agree with the recorder on work class in between 7 of 15
    and 19 of 20 sampled steps, and in 13 of 20 in the latest (`AUD-S11-1`); `CON-OP-16` depends on that field
    (`PRC-OP-6`). Of the 522 steps logged up to S12-027, 152 (about 29%) are classed overhead or rework.
15. **Housekeeping is behind.** On 2026-11-14, 20 commits, the whole generator among them, were not pushed to GitHub.
    Session 12 had been open for ten days with no handover. `README.md`, `AGENTS.md` and 400 still say that nothing is
    built, and `AGENTS.md` still forbids code. Handover 12, the current one, says nothing of the warehouse exists.

## Suggested next steps, in order, not ruled

16. Push, close session 12, and correct `README.md` and `AGENTS.md`.
17. Build one thin mart and one analysis on the existing vault, so the chain is complete end to end.
18. Add a second, messy source with an answer key, so that point 6 is tested before the client engagement.
19. Triage the register: archive what the build has overtaken, and compute the economics number of `CON-OP-2`.

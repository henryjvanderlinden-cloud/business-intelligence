# nsdn — Handover 15: the second source and its hidden answer key are built and experiment E1 is frozen; the matching is next
## Written 2026-11-23 at the close of session 14

> **STATUS: CURRENT.**

---

## First actions

1. **Check that `C:\nsdn-holdout` is NOT among this session's connected folders** (`get_device_info`,
   `connectedFolders`). If it is, stop and tell the author: this session proposes matches, and
   [430](../docs/40_roadmap/430_second-source-and-answer-key.md) §3 forbids it access to the hidden folder. Do not list,
   read or count anything in it, whatever is connected.
2. `git status`, then `git log --oneline -15`. Expect HEAD at the commit that closed S14 (message begins "Close session
   14"). The author pushes himself; if `origin/main` is behind, say so, do not push.
3. `python tools/check_repo.py` on a copy outside the mounted folder (*Traps*). It passes with the three known warnings
   in `S07.jsonl`. Expect 14 sessions, S14 closed with `AUD-S14-1`, 45 ADRs.
4. Read, in this order: this handover; [430](../docs/40_roadmap/430_second-source-and-answer-key.md) whole, §5, §6 and
   §9 above all; [ADR-0043](../docs/20_decisions/0043-second-source-a-crm-derived-from-wwi.md) and
   [ADR-0044](../docs/20_decisions/0044-answer-key-harness-for-the-second-source.md);
   [410](../docs/40_roadmap/410_first-vertical-slice.md); `EVI-OP-1` in the register;
   [144](../docs/10_architecture/144_raw-vault-business-vault-calculation-engines.md) §3; the
   [sandbox README](../prototypes/wwi_sandbox/README.md), *The customer system*.
5. Ask the sandbox job for its status (handover 08, *Driving the sandbox*). Expect simulated date 2016-06-06, the runner
   `loaded` or `idle` with `last_ok_date` 2016-06-06, and `data/frozen/E1/` present.
6. Open session S15 in `records/sessions.jsonl` and log from S15-001.

## Where we stand

Session 14 ran from 2026-11-17 to 2026-11-23, on Claude Opus 5.5.

- **The repository is dedicated to the public domain under CC0 1.0**
  ([ADR-0041](../docs/20_decisions/0041-cc0-public-domain-dedication.md)); third-party material is named in the README
  and [`THIRD-PARTY-NOTICES.md`](../THIRD-PARTY-NOTICES.md), and the checker enforces both. A client may read nsdn at a
  distance at a recorded reading point instead of holding a fixed release
  ([ADR-0042](../docs/20_decisions/0042-reading-at-a-distance.md), amending ADR-0035 and ADR-0036). Both came from a
  note the author brought from another conversation.
- **The second source exists.** A customer system derived from Wide World Importers (ADR-0043): its generator, freeze
  and scorer were written by sol in `C:\nsdn-holdout\`, outside the repository, reviewed by Astra (failing twice, then
  holding), and installed by the author's setup run of 2026-11-23. After every export the job generates
  `data/raw/crm/<date>/` (`Customers.csv.gz`, 11 columns, and a manifest). The job's new actions `generate`, `freeze`
  and `score` pass on only results rebuilt from allowed fields (430 §4 and §9).
- **Experiment E1 is frozen** on 2016-06-06 in `data/frozen/E1/`: the WWI extract, the customer extract (686 records)
  and `development_records.csv` (483 records, the development part). The key and the held-back part stay hidden.
- **The thresholds are fixed** (ADR-0044, 430 §6): automatic merges at least 0.98 precise; the queue worth reading at
  0.60; the model at least 0.05 more recall than cheap signals at the automatic tier, each method's cutoff locked on
  development. The difficulty was calibrated against a ceiling only: a cheap baseline in the hidden folder reaches a
  recall of about 0.8 at 0.98 precision.
- A parallel session (2026-11-19 and 20) built the sales viewer, a proof of concept
  ([ADR-0045](../docs/20_decisions/0045-sales-viewer-proof-of-concept.md)); its steps are in S14's log, reconstructed.

## Task for the next session, in one sentence

Propose, for every customer record of E1, its WWI customer or none, first by cheap signals only and then with the
model, score each on the development part within the schedule, and release the held-back part once, so that the
falsifiable core of 410 gets its first figure.

## Scope

**In.** In this order, each put to the author before it is built where it is a design choice:

1. **Know the new source as any source**: the catalogue pass and the per-table analysis of `data/frozen/E1/crm/`, as
   for WWI, kept to what matching needs. It is a new source to the agentic layer; treat it so.
2. **The cheap-signal method**: deterministic standardisation and comparison, no model; a versioned script under
   `prototypes/`, its proposals file in `data/proposals/E1/` in the scorer's format (430 §9, the build report's header
   `record_number,wwi_customer_number,confidence,method,version`; duplicates
   `record_number_a,record_number_b,confidence`). Register each version in the step log **before** scoring it.
3. **The model method**: the agentic layer proposing with the context it has; same format, its own method label.
4. **Development scoring**: at most five runs per method, figures only. Read 430 §5.2 on what the development list is
   for.
5. **The held-back release**, once: both methods' last development files, byte for byte, with their cutoffs exactly as
   the scorer reported them (a decimal string, or `none`), in one `score` request with `part` `holdback`.
6. **A findings note** with the held-back figures, cheap and model apart, against the three thresholds; then
   `EVI-OP-1` and the 410 question answered for this instance, saying plainly that the differences were planted.

**Out unless he asks.** What the second source asks of the vault generator (handover 14, scope item 4; 144 §3; the
generator stops on more than one source); loading the customer system into the vault; the published benchmark (ADR-0043,
option B); the rest of the general assessment.

## How to work with the author

Plain English, numbered points; propose, let him react, write what he settles; quote him verbatim; everything tentative
until he rules it. He asked that only weak-evidence cases come to him. When he rules, record it the same turn, in an ADR
or the register, and commit. The main goal is generally applicable knowledge; WWI is only an example: say what is
general and what belongs to one source.

## Traps and warnings

**The hidden folder is out of bounds for this session.** Never read, list or count `C:\nsdn-holdout\`, never ask sol,
Astra or the author about the kinds of difference, the seed, the split or the key, and use scores only within the
schedule. A breach retires E1 (430 §5.1, §7). The author connected the folder to S14, a building session, on its
promise not to read it; that does not carry over.

**sol's sessions end a few minutes after the call times out.** A Codex call returns "did not respond within 80s"; the
session keeps working for one to three minutes and then stops. Short reviews finish; builds do not. For long work,
have sol keep its own state notes and a progress file, and continue with short follow-up calls. Poll for answer files.

**Every first version has failed review**, in every session since S09; in S14 five first versions failed (the
licence work, 430, the job, the hidden code, the fix of 2026-11-23). Build the time in.

**The checker's asset rule bends labels.** Data task types (generation, modelling, matching, ...) require `assets`;
S14 relabelled two steps to pass the check, and the audit found task type and tier agreement at 9 and 7 of 20
(`AUD-S14-1`). Matching steps should be labelled `matching` with their assets; register the assets in
`records/assets.jsonl` rather than avoiding the label.

**Workspace restarts** reset the delete permission git needs: commits then leave `.git/index.lock` and `tmp_obj_*`
files. Ask for deletion permission on the repository folder, remove the stale lock (no git process running), retry.
Setting the author in the commit with `$(git log -1 --format=%an)` inside the command was slow enough on the mounted
folder to make commits fail silently; give `user.name` and `user.email` literally.

**`check_repo.py` is slow on the mounted folder.** Keep a copy in the workspace (`rsync -a --exclude data --exclude
scratch --exclude .git`, about two minutes the first time), copy changed files into it, and run the check there (two
seconds).

**Setup needs the execution policy bypassed**:
`powershell -NoProfile -ExecutionPolicy Bypass -File C:\Git\business-intelligence\prototypes\wwi_sandbox\setup.ps1`,
as administrator, never `-Reset`. If its end-to-end test stops, the runner task stays disabled until setup completes.

**A re-export rewrites the WWI manifest.** The generator now identifies its input by the table files' content, not the
manifest (430 §9 item 7); the first generation of 2016-06-06 was retired for that reason, its public extract in
`scratch/_legacy/`.

## Outstanding for the author, not the model

**The ceiling of the calibration** (430 §9 item 5): simple matching must stay below a recall of 0.9 at 0.98 precision;
it reaches about 0.8. Put to him on 2026-11-21, not answered. From handover 14, still open: rule or reject 030; the phase
gate of 400 and ADR-0006; `PRC-OP-10` points 1 to 7, 9, 10, 12 to 15 and 19; the tolerances of the maintenance baseline;
`git gc` (done by him on 2026-11-20); the task type for design work; `ARC-OP-37` items 2 and 4; which customers are
individuals and access rules per sensitivity class before production; the two guards of session 06; two commits of
2026-10-25 not in any step log. From the parallel session: whether verify.py's checks become standing ones (`ARC-OP-31`,
`ARC-OP-33`).

## Driving the sandbox

Unchanged from handover 08, with three actions more (the sandbox README): `generate` (a date whose WWI extract is
present), `freeze` (done for E1; do not freeze again without cause) and `score`:

```json
{"action":"score","experiment":"E1","part":"development","proposals":"data/proposals/E1/<file>.csv","duplicates":"data/proposals/E1/<file>.csv"}
{"action":"score","experiment":"E1","part":"holdback","cheap":"...","model":"...","cheap_cutoff":"<as reported>","model_cutoff":"<as reported or none>"}
```

A refused request answers with a fixed code only (`UNKNOWN_RECORD`, `RUN_LIMIT`, `CUTOFF_MISMATCH`, ...; the list is in
`job.ps1`). Advance at most two days at a time unless the author says otherwise; E1 does not depend on later days.

## Do not reopen

Everything in handovers 06 to 14, plus:

- ADR-0041: the CC0 dedication; third-party material named, not rewritten.
- ADR-0042: reading at a distance as a second way for a client to use nsdn.
- ADR-0043: the second source is a customer system derived from WWI, generated by a model other than the proposer.
- ADR-0044 and 430: the hidden folder, the job running the generator, figures only, the identity-group split, the
  held-back part released once, the three thresholds and their reading (confirmed by the author 2026-11-21).
- ADR-0045: the sales viewer is a proof of concept.

## What was not done

No proposal and no score: the falsifiable core is still untested. The second source is not in the vault. The
revisions after the last reviews of the job (sol) are tested on Linux stand-ins and in the author's setup run, not
reviewed again. The ceiling of the calibration is the author's to confirm. No retirement command exists for an
experiment (430 §9 item 4).

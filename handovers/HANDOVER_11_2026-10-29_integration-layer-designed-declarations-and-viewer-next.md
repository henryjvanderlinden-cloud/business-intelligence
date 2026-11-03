# nsdn — Handover 11: the integration layer for Wide World Importers is designed; declarations and the viewer are next
## Written 2026-10-29 at the close of session 10

> **STATUS: HISTORICAL (superseded 2026-11-03)** by [handover 12](HANDOVER_12_2026-11-03_declarations-viewer-and-pg-pass-done-generator-next.md).

---

## First actions

1. `git status`, then `git log --oneline -15`. Expect HEAD at the commit that closed S10 (message begins "Close session
   10"). The author pushes himself; if `origin/main` is behind, say so, do not push.
2. `python tools/check_repo.py` on a copy in the cloud workspace, not on the desktop's shell (see *Traps*). It must pass
   apart from the 7 known errors under `scratch/vdl-diaa-logo`. Expect 10 sessions, S10 closed with `AUD-S10-1`, 33 ADRs.
3. Read, in this order: [142](../docs/10_architecture/142_the-data-model.md) §2 to §6 (what is declared, the text is
   the truth, the human view), [ADR-0032](../docs/20_decisions/0032-generated-sql-machinery.md) (the machinery), then the
   design to be declared: [147](../docs/10_architecture/147_wwi-concepts-keys-and-business-time.md) §2 to §5,
   [148](../docs/10_architecture/148_wwi-relationships.md) §2 to §4, [149](../docs/10_architecture/149_wwi-satellites.md)
   §2 to §5, with their rulings ADR-0027 to ADR-0033. Then the register row `ARC-OP-29` and its notes of 2026-10-29,
   which hold the author's viewer request verbatim.
4. Ask the sandbox job for its status (handover 08, *Driving the sandbox*). Expect simulated date 2016-06-02; 18.17 GB
   was free on 2026-10-26.
5. Open session S11 in `records/sessions.jsonl` and log from S11-001.

## Where we stand

Session 10 designed the integration layer for Wide World Importers in full, each part proposed with evidence, failed
and revised on sol, and ruled by the author:

- **Step A, hubs and business time** (147; [ADR-0028](../docs/20_decisions/0028-wwi-country-key-milestones-and-sensors.md),
  [ADR-0029](../docs/20_decisions/0029-wwi-step-a-concepts-and-keys.md)): twenty-two hubs keyed on the source's record
  identifiers in the key space `wwi`, the country on ISO 3166-1; existence dated by the event date and each milestone
  a fact of its own.
- **Keys** ([ADR-0030](../docs/20_decisions/0030-hub-and-link-keys-are-hash-keys.md)): hash keys of key-space code and
  business key.
- **Step B, links** (148; [ADR-0031](../docs/20_decisions/0031-wwi-step-b-links.md)): forty-nine binary links, every
  link with driving-key effectivity, one batch per extract.
- **Step C, satellites** (149; [ADR-0033](../docs/20_decisions/0033-wwi-step-c-satellites.md)): splits only for
  audit, sensitivity, rate of change, milestone or delivery; three clocks and a source-version identifier on every
  satellite row; audit and status-tracking satellites per hub; readings one row each; password hashes never loaded,
  their column kept empty.
- **The machinery** (ADR-0032): declarations, a generator of our own, generated plain SQL as dbt models in folders; no
  DDL files; the runner and dbt orchestrate.

The analysis record gained 18 claims (which columns change between versions; ISO conformance) from two new evidence
scripts in `prototypes/information_analysis/`.

**Nothing is built**: no declaration file, no generator, no dbt model beyond the staging prototype, no test.

## Task for the next session, in one sentence

Propose the declaration format for the model files, write the Wide World Importers raw vault of 147 to 149 in it, and
build the first version of the lightweight viewer the author asked for, reading those files and the raw source
catalogue.

## Scope

**In.** The declaration format (`ARC-OP-29`): one small text file per hub, link, satellite and reference table, holding
only what 142 §3 says is declared, with stable identifiers, and checked by `tools/check_repo.py` (AGENTS rule 11).
Writing the WWI raw vault in it, every file citing the note and ADR it comes from. The viewer as proposed under
`ARC-OP-29` (2026-10-29): a static, read-only HTML page, no server, generated from the declarations and, for the raw
source layer, from the analysis record (`analysis/wwi/tables/*/*/06_keys.md`, `across/relations/`); black background,
light-green tables; a focus view with the selected table large in the centre and its neighbours smaller around it,
placed by a force-directed layout like Gephi's; compact cards with keys and relationships and an ellipsis with the
count of other columns; a details panel per table; layers for the raw source schema and the raw vault; satellites
collapsed on their hub until opened (about 260 raw-vault tables). Show the author a draft early.

**Out unless he asks.** The generator and the SQL (they come after the format settles); the business vault and marts;
the calculation engines' runner step; access rules per sensitivity class; quality gates (`ARC-OP-33`).

## How to work with the author

Plain English, numbered points; propose, let him react, write what he settles; quote him verbatim; everything tentative
until he rules it. He asked that only weak-evidence cases come to him. Review on sol, framed against the standard the
object must meet (`PRC-OP-7`), and with the brief confined to the object (see *Traps*). When he rules, record it the
same turn, in an ADR or the register, and commit. Label his rulings `adjudication` in the step log (`AUD-S10-1`).

## Traps and warnings

**Every first version failed review in S10, as in S09.** Seven passes on sol, seven FAILS on the first version, all
applied. Expect it, and build the time in.

**Codex briefs: confine the reviewer to the object.** Two broad briefs (several files to read, many citations to check)
wrote nothing in 13 and 14 minutes; briefs that said "read only this file" wrote in 1 to 3 minutes. Citations are then
unchecked by the reviewer, so check them yourself with a script: S10 resolved every `path#Cn` in 147, 148 and 149 against
the record before review (216, 150 and 103 citations).

**Edit tables by named column, not by cell index.** A script that rewrote 148's Effectivity column by position
overwrote the evidence column instead; it was restored from the committed version.

**The desktop's clock is UTC, and step timestamps ran ahead of their commits** five times in S10 and had to be pulled
back. Take the time from the shell immediately before writing a step, and do not round up.

**The desktop shell.** `check_repo.py` is too slow there. What worked: `tar -czf` of `analysis/` alone (about a minute)
and of the rest without `.git`, `data/raw`, `data/warehouse`, `data/derived`, `scratch/_transfer`, `scratch/_superseded`
and `scratch/*.zip` (about ten seconds), into `$HOME/xfer`, copied to `scratch/_transfer/`, staged, extracted and checked
in the cloud. Changes go back as a tarball committed into `scratch/_transfer/` and extracted with `tar --overwrite`
(plain `tar -x` fails: deletion is not approved). After each commit, `mv` the lock files `.git/HEAD.lock`,
`.git/index.lock`, `.git/objects/maintenance.lock` to `.git/stale-...`; git warns about `tmp_obj` files it cannot
delete, which is harmless. The author's `git gc` would help.

**The viewer is a reader, never a source of truth** (142 §3). It must not grow its own copy of the model. Libraries
from a CDN need the desktop online; whether to vendor them into the repository is a choice to put to the author.

**The runner refuses Python models and dbt packages** (ADR-0015, ADR-0032). The generator and the viewer's build run
outside it, by a person or the agent layer.

## Outstanding for the author, not the model

**Push** (14 commits of S10 at the close). **`git gc`** in `C:\Git\business-intelligence`. **The task type for design
work** (raised in handover 10 with `AUD-S09-1`; `AUD-S10-1` shows the same pattern). **`ARC-OP-37` items 2, 4 and 8**:
the general rules for several sources, the conditions on engines, where marts take their data from. **Which customers
are individuals**, and the access rules per sensitivity class, before production. **The two guards** from session 06.
**Two commits of 2026-10-25** (`0951076`, `5d3d777`), not in any step log.

## Driving the sandbox

Unchanged from handover 08: request files in `data/wwi/requests/`, four actions (`status`, `advance`, `export`,
`query`), one request per job run, the newest three extracts kept, `data/frozen` never touched, no row edits, no
`setup.ps1 -Reset`. Keep the simulation at two days unless the author says otherwise. Status was answered in S10 in
about 35 seconds.

## What session 10 did

Picked up handover 10 on 2026-10-26; added the facts step A lacked to the record; proposed, reviewed and revised step A
(147) and brought three weak cases to the author, ruled on 2026-10-28 (ADR-0028); step A accepted as a whole and hash
keys chosen the same day (ADR-0029, ADR-0030); step B (148) proposed, failed, revised and accepted on 2026-10-29
(ADR-0031); the machinery outline accepted (ADR-0032); step C (149) proposed, failed, revised and accepted with the
password ruling (ADR-0033); the author's viewer request recorded under `ARC-OP-29`; closed with the blind audit
`AUD-S10-1`.

## Do not reopen

Everything in handovers 06 to 10, plus:

- The twenty-two hubs and their keys; record identifiers in the key space `wwi`; the country on ISO 3166-1; states on
  their record identifier (ADR-0028, ADR-0029).
- Existence dated by the event date; each milestone a satellite of its own; the accumulating snapshot built in the
  marts (ADR-0028).
- Hash keys of key-space code and business key (ADR-0030).
- Forty-nine binary links, effectivity on every link, one batch per extract (ADR-0031).
- The satellites of 149, the source-version identifier, and password hashes never loaded (ADR-0033).
- Generated plain SQL as dbt models, from declarations, by a generator of our own (ADR-0032).

## What was not done

No declaration file, generator, SQL or test. The revised texts of 147, 148 and 149 were not reviewed again after their
revision. The business vault, the marts, and the engines' runner step are undesigned.

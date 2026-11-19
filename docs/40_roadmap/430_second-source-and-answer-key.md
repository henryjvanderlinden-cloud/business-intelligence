# 430 — The second source and its answer key: a customer system derived from Wide World Importers

*Design, 2026-11-19, session 14. Adopts nothing by itself: what the author ruled on 2026-11-19 is in
[ADR-0044](../20_decisions/0044-answer-key-harness-for-the-second-source.md); the choice of source is
[ADR-0043](../20_decisions/0043-second-source-a-crm-derived-from-wwi.md). Unreviewed until the review note says
otherwise.*

## 1. What this is for, and what in it is general

[410](410_first-vertical-slice.md) names one claim that is either true or not: that business keys and entity identity
across sources can be machine-proposed at a precision that makes adjudication worth a person's time. Wide World
Importers (WWI) cannot test it, being one clean source with declared keys. This note designs a second source that can,
and the means of scoring proposals against a key the proposing model never sees.

Most of it is general and would serve any client: the hidden-key arrangement (§3), the scoring rules (§5), the
thresholds fixed before scoring (§6) and the conduct rules for the proposing model (§7). Only the generator (§2) belongs
to WWI. Loading the new source into the vault, its analysis record and what it asks of the vault generator are handover
14's scope items 3 and 4, and are not designed here.

## 2. The source: WWI's customers as another system would hold them

A customer system, a CRM or a web shop's customer table, that holds WWI's customers as an independently built system
would: with a key space of its own and with the differences two systems built by different teams accumulate. It is
delivered as an extract beside WWI's.

**Content.** Customers only, to start: a customer number of the system's own, name, contact person, phone, e-mail,
delivery address, postcode, city, a segment label of the system's own, a creation date and an active flag. Some WWI
customers are absent, some customers exist only in this system, some appear twice in it, and a few of its records merge
two WWI customers.

**The kinds of difference** (spelling, formatting, abbreviation, merges and so on) are chosen by sol and kept from the
proposing model, list included. If the proposing model knew the list, it could tune to it, and the test would measure
the list.

**Requirements on the generator**, which sol writes:

1. It reads only the day's WWI extract (`data/raw/wwi/<date>/`), in practice the customer, people, city, province,
   category and buying-group files.
2. It is deterministic: the same extract and the same hidden seed give the same output, byte for byte. A customer keeps
   its number in the new system from day to day; customers WWI adds appear in it by the generator's rule.
3. Its output carries no artefact that two independent systems would not share: no WWI customer number, nothing derived
   from one (a hash included), no numbering, row order or file order that follows WWI's. Attributes that genuinely
   describe the same customer, a name, a phone number, an opening date, may agree or differ as real systems do.
4. It writes `data/raw/crm/<date>/` atomically, as the WWI export does: gzipped CSV in the same dialect and a
   `manifest.json` with rows, bytes and SHA-256 per file. Retention matches WWI's: the newest three dated folders.
5. It writes the key for the day, and the split of §5, into the hidden folder only.
6. It uses the Python standard library only, so that it runs in the runner's pinned environment without a new package.
7. It is tested by sol: determinism, stability of numbers across two consecutive days, and absence of the artefacts of
   point 3.

## 3. The hidden folder, and who sees what

`C:\nsdn-holdout\`, outside the repository, created once by the author. It holds the generator, the list of kinds of
difference, the seed, the key per day, the split, the scorer and the scoring log. It is never connected to the proposing
model's session. sol writes there, and only there, while building and testing the generator and scorer: a narrow
exception to the author's ruling of 2026-10-07 that Codex's sandbox stays read-only (handover 08). The author may read
it at any time.

The proposing model never reads the folder, never asks sol about its contents, and frames every call to sol so that sol
answers without them (§7). The arrangement rests on that tool boundary and on the step log, which records every call; it
is not absolute, since the proposing model directs the calls ([ADR-0043](../20_decisions/0043-second-source-a-crm-derived-from-wwi.md),
Consequences).

## 4. Running it every simulated day

`setup.ps1` copies the generator and the scorer from `C:\nsdn-holdout\` into the job's pinned folder
(`C:\ProgramData\nsdn-wwi\holdout\`, writable by administrators only), as it copies the job itself, so their code never
passes through the repository. The key, the seed and the split stay in `C:\nsdn-holdout\`.

After each export, the job runs the generator with the runner's Python on the new extract. If the generator fails, the
WWI extract stands and the response says so; the next export runs it again. A day's customer extract therefore always
belongs to a WWI extract of the same date.

Changing `job.ps1` and `setup.ps1` for this, and for the action of §5, is one batch, followed by one rerun of
`setup.ps1` by the author.

## 5. Scoring

**What is proposed.** For a given date, a proposals file in the repository with, for each customer of the new system,
either the WWI customer it is or "no counterpart", a confidence between 0 and 1 and a method label; and, separately,
pairs of its own records proposed to be the same customer. One file per method run: *cheap signals only* (deterministic
standardisation of names, phones, postcodes and addresses, no model) and *with the model*, reported apart, as 410
requires.

**Who scores.** A new job action, `score`, with the date, the proposals file and the part. The job runs the scorer, which
reads the key and returns figures only: never a per-customer verdict, which would leak the key.

**The figures.** For each method: proposed links, abstentions, precision (right links over proposed links), recall
(right links over true links), the share of abstentions that are right, precision of the 50 highest-confidence links, and
precision and recall in two tiers: links at or above the automatic-merge confidence, and links below it (the queue a
person would read). For the system's own duplicates: precision and recall of the proposed pairs. A link to either of the
WWI customers a merged record holds counts as right; merges are also reported apart.

**The held-back part.** The generator assigns each customer of the new system, by the hidden seed, to a development part
(about 70%) or a held-back part (about 30%). Proposals always cover all customers. During development the scorer reports
on the development part only; the held-back part is scored once, at the end, and the scorer refuses it a second time.

**Few runs.** Every development run reveals a little of the key, and repeated runs could be used to probe it. A
development run is made only for a new version of a proposing method, each recorded in the step log with the method's
version; the scorer's own log in the hidden folder lets the author check that.

## 6. Thresholds, fixed before the first score

Proposed by the model and ruled by the author on 2026-11-19 (ADR-0044):

1. **Automatic merges**: precision of at least 0.98 among links at or above the automatic-merge confidence, since a wrong
   merge mixes two customers' sales.
2. **The queue**: worth a person's reading when at least 0.60 of its links are right.
3. **The model's contribution**: at the automatic-merge tier's precision, recall with the model at least 0.05 higher than
   with cheap signals only. Less is itself the finding 410 anticipates.

The automatic-merge confidence is set per method on the development part, before the held-back part is scored. The
held-back figures are the ones reported.

## 7. Conduct of the proposing model

It does not read `C:\nsdn-holdout\` or the job's pinned `holdout\` folder, ask sol or the author about the kinds of
difference, the seed, the split or the key, or use a score for anything but a method's version. sol's build and review
assignments instruct it to report on the generator and scorer without naming the kinds of difference. A breach, or a
suspected one, makes the test void; it is recorded, and the generator is rerun by sol with a new seed and new kinds of
difference.

## 8. What the author does

Creates `C:\nsdn-holdout\` once, and reruns `setup.ps1` once, after the generator, the scorer and the job's changes
exist. Nothing else, unless something breaks on the Windows side, which remains his to repair.

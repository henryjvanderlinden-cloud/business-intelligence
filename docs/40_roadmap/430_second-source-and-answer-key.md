# 430 — The second source and its answer key: a customer system derived from Wide World Importers

*Design, 2026-11-19, session 14. Adopts nothing by itself: what the author ruled on 2026-11-19 is in
[ADR-0044](../20_decisions/0044-answer-key-harness-for-the-second-source.md); the choice of source is
[ADR-0043](../20_decisions/0043-second-source-a-crm-derived-from-wwi.md). Failed its first review on sol on
2026-11-19 ([XREV](../30_research/notes/XREV_2026-11-19_430-second-source_sol.md)); sections 4 to 7 revised in
response, unreviewed since.*

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
   `manifest.json` with rows, bytes and SHA-256 per file. Publication and retention are as §4 describes.
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

The boundary is on the session that **proposes matches**. A session that only builds, the generator, the scorer or the
job's changes, may have the folder connected, provided it never reads it. On 2026-11-21 the author connected it to
session 14, which builds and proposes nothing; it is not read there, at his instruction, verbatim: "just promise not to
look into it!". Proposals are made in a later session with only the repository connected, whose first check is that
`C:\nsdn-holdout\` is not among its folders.

## 4. Running it every simulated day

`setup.ps1` copies the generator and the scorer from `C:\nsdn-holdout\` into the job's pinned folder
(`C:\ProgramData\nsdn-wwi\holdout\`, writable by administrators only), as it copies the job itself, so their code never
passes through the repository. The key, the seed and the split stay in `C:\nsdn-holdout\`. Setup enables the job only
after the Python environment the generator needs is installed and the hidden folder is found writable.

**A generation is one unit.** After each export the job runs the generator on the new extract. Each run writes, in this
order: the customer extract to a staging folder; the key and the split for that date into the hidden folder; then, last,
a readiness record in the hidden folder naming the SHA-256 of the WWI manifest it read, of the customer manifest it
wrote and of the key; and only then moves the staging folder into place as `data/raw/crm/<date>/`, whose manifest
names the WWI manifest's SHA-256 as its input. A date without a readiness record whose hashes match the published
folders has no generation, whatever files exist; the scorer refuses it.

**Failure.** A failed generation leaves the advance and the WWI export committed; the response reports the export as
done and the generation as failed, with a fixed message and an error code. Details, which may contain hidden content,
go to the scorer's and generator's log in the hidden folder only, never into a response or the job's log in the
repository. A new job action, `generate`, reruns the generator for a date whose WWI extract is still present, without
advancing. Staging folders of failed runs are removed before the next run.

**Retention is joint.** A customer extract is kept exactly as long as the WWI extract it was made from; when the job
deletes a WWI date, it deletes that date's customer extract with it. Keys and readiness records in the hidden folder are
kept. Before generating, the job checks free space on the repository's volume and on the hidden folder's, against a
floor of its own.

The runner reads only WWI today. When it is taught the second source (scope items 3 and 4), it must treat a date as
ready only when both extracts and the readiness of the generation are present, never on the WWI extract alone.

Changing `job.ps1` and `setup.ps1` for this, and for the action of §5, is one batch, followed by one rerun of
`setup.ps1` by the author.

## 5. Scoring

### 5.1 The experiment is frozen

Daily generation feeds the pipeline; it does not feed the measurement. The measurement uses an **experiment**, frozen
once, before any development:

1. One simulated date is chosen. Its WWI extract and its customer extract are copied into `data/frozen/E1/`, which the
   job and the runner never touch, and their manifests' SHA-256 are recorded.
2. Its key, its split and the scorer's version are copied into `C:\nsdn-holdout\experiments\E1\` with a record of the
   same hashes. Customers that later days add never enter E1.
3. Every score request names the experiment, and the scorer checks the frozen hashes before it reads anything.

A breach of §7 retires the experiment; the next one is generated with a new seed and new kinds of difference, and
starts with no scoring history.

### 5.2 The split is by identity group, and the development part is not secret

The split is drawn over **identity groups**: a WWI customer together with every customer-system record that holds it,
duplicates and merges included, closed transitively; a customer-system record with no WWI counterpart is a group of its
own. About 70% of groups go to development and 30% are held back, by the hidden seed, once, for the experiment.

The list of development record numbers is published with the experiment, without their counterparts. Development
membership is therefore not something scoring can reveal, and no identity can be learnt on one side of the split and
used on the other. The development labels are not secret either: aggregate feedback over many runs can reveal some of
them, and that is accepted, since development data exists to be developed on. The development schedule is fixed before
the first run: at most five development runs per method, each a new version of the method recorded in the step log
before it is scored.

### 5.3 The scoring contract

**The proposals file.** One file per method run, UTF-8 CSV, one row per customer-system record of the experiment and no
other rows: the record's number; the proposed WWI customer number, or empty for "no counterpart"; a confidence between 0
and 1; the method label and version. A separate file lists proposed duplicate pairs of customer-system records with a
confidence. A file with a missing, repeated or unknown record, an unknown WWI customer, or a confidence outside 0 to 1
is rejected whole, with the reason, and is not scored.

**The truth.** Each customer-system record has an acceptable set: the WWI customers it holds; one for most records, two
or more for a merge, none for a record with no counterpart.

**Cross-source figures**, over the records of the part being scored:

1. A *link* is a row with a WWI customer. It is *right* when that customer is in the record's acceptable set.
2. *Precision* is right links over links.
3. *Recall* is right links over *eligible records*: records whose acceptable set is not empty. Duplicate records are
   each an opportunity of their own; WWI customers with no record in the customer system are outside this measure.
4. *Abstention accuracy* is, among rows with no WWI customer, the share whose acceptable set is empty.
5. *The two tiers* split the links at the method's automatic-merge cutoff (§6): links at or above it are the automatic
   tier, links below it the queue. Each tier's precision is over its own links; each tier's recall is over all eligible
   records, so the two recalls add up to the method's recall.
6. *Precision of the top 50*: links ordered by confidence, highest first, ties broken by record number ascending; over
   all links when there are fewer than 50, which is reported.
7. A figure whose denominator is zero is reported as undefined, never as 0 or 1.

**Duplicate figures.** Proposed pairs are unordered; a repeated pair is rejected with the file. A pair is right when both
records have non-empty acceptable sets that share a customer. Precision is right pairs over proposed pairs; recall is
right pairs over all such pairs in the part.

**What comes back** is these figures, per method and part, with the experiment, the scorer's version and the date.
Never a per-record verdict.

### 5.4 The held-back part is released once

When development is over, both method files, cheap signals and with the model, are submitted together in one request,
each with its automatic-merge cutoff, which was fixed on the development part by the rule of §6. The scorer records the
consumption of the held-back part durably before it computes, then returns both results in one response. The same
request repeated, byte for byte, returns the same results; any other held-back request for the experiment is refused.

## 6. Thresholds, fixed before the first score

Proposed by the model and ruled by the author on 2026-11-19 (ADR-0044); their reading below was made precise after the
review of 2026-11-19 and confirmed by the author on 2026-11-21.

**The automatic-merge cutoff** of a method is fixed on the development part, before the held-back release: the lowest
confidence at which the links at or above it have a precision of at least 0.98, links of equal confidence counted
together; if no confidence gives 0.98, the method has no automatic tier. It is then locked.

1. **Automatic merges**: on the held-back part, precision of the automatic tier at least 0.98. A method with no
   automatic links does not meet it.
2. **The queue**: on the held-back part, precision of the queue at least 0.60. A method with no queue links does not
   meet it.
3. **The model's contribution**: both methods meet threshold 1, and the model's automatic-tier recall exceeds the cheap
   signals' by at least 0.05, each at its own locked cutoff. This is recall at a common precision floor, not at exactly
   equal precision. If the cheap signals miss threshold 1 and the model meets it, the model's contribution is reported
   as such; if the model misses it, threshold 3 is not met. Less than 0.05 is itself the finding 410 anticipates.

The held-back figures are the ones reported; the development figures are reported beside them as such.

## 7. Conduct of the proposing model

It does not read `C:\nsdn-holdout\` or the job's pinned `holdout\` folder, ask sol or the author about the kinds of
difference, the seed, the split beyond the published development list, or the key, or use a score for anything but a
method's version within the schedule of §5.2. sol's build and review assignments instruct it to report on the generator
and scorer without naming the kinds of difference. A breach, or a suspected one, retires the experiment (§5.1) and is
recorded.

## 8. What the author does

Creates `C:\nsdn-holdout\` once, and reruns `setup.ps1` once, after the generator, the scorer and the job's changes
exist. Nothing else, unless something breaks on the Windows side, which remains his to repair.

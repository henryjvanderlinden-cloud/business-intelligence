# nsdn — Handover 01: the repository exists, the argument is under attack
## Written 2026-09-19 at the close of session 01, for a fresh session

> **STATUS: HISTORICAL (superseded 2026-09-20)** — succeeded by
> [HANDOVER_02_2026-09-20_faculties-ruled-spine-candidate.md](HANDOVER_02_2026-09-20_faculties-ruled-spine-candidate.md).

> *Revised through the session as the work landed, then rewritten whole at close. Earlier
> states are in git for anyone who wants them.*

---

## First actions

1. `git log --oneline -8` — expect six commits, head `Record the canon-cost argument`
   or later.
2. `python tools/check_repo.py` — must pass before anything is changed.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority
   on what is open; this handover is orientation only, and where the two disagree the
   register wins.
4. Read [`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md),
   noting the challenge banner on §III, and
   [`../docs/10_architecture/190_machine-authored-design-canon.md`](../docs/10_architecture/190_machine-authored-design-canon.md).
   Those two documents are where the argument currently lives and where it is currently
   contested.

## Outstanding action for the author, not the model

**The repository has never been pushed.** `origin` is configured to
`https://github.com/henryjvanderlinden-cloud/business-intelligence.git`, the repo does
not exist on GitHub yet, and this session's sandbox holds no credentials. The author
creates the empty repository — no README, no .gitignore, no licence — and runs
`git push -u origin main` from `C:\Git\business-intelligence`. Visibility was discussed
and left undecided; the reasoning favoured private until the Mode 1 gate, since
private-to-public is one click and the reverse is not.

## Where the project stands

Session 01 took a long-form brief from the author — twenty-six years in business
intelligence, proposing an agent-driven system that discovers, models and exploits an
organisation's data landscape — preserved it verbatim, critiqued it, built an
architecture around the critique, stated the argument as a manifesto, ran the first
adversarial pass against that manifesto, and watched it fail.

Seven ADRs are settled. Thirty-four register rows are open. Nothing has been built,
nothing has been verified, and no data has been touched.

**The intellectual position, honestly stated.** The reframing the architecture rests on
is that autonomy is tiered — structural, semantic, teleological — and that the binding
constraint moves from construction to adjudication. That still stands. The *justification*
offered for it in the manifesto, the statability argument, is under challenge and losing.
A candidate replacement arrived at the end of the session from the author rather than the
model, and is stronger in kind: the canon-cost argument, which is empirically checkable
against an existing literature rather than defensible only against philosophy.

## Task for the next session, in one sentence

Rewrite [`005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III against
`CON-OP-5`, `CON-OP-6`, `CON-OP-7` and `CON-OP-8` — or, if that is judged premature,
run `ARC-OP-14` or `EVI-OP-2` first and leave §III challenged.

## The three candidates, ranked

**The §III rewrite (`CON-OP-5`, `-6`, `-7`, `-8`, `-9`).** Owed, and not a patch. If the
`CON-OP-5` repair holds, statability reduces to articulability plus generality plus
observability, and the section is restructured rather than annotated. `CON-OP-8` — whether
the canon-cost argument becomes the spine — is decided inside this work, not before it.
`CON-OP-7(a)`, which decides whether §III's central example survives at all, should be
settled first if it can be. `CON-OP-9` settles the vocabulary in the same pass: whether
data belongs in the set at all (it does not — it is the substrate), and what the three
are collectively called. **Do not rename anything across the repository until that row
closes**; renaming twice costs more than deciding late.

One phrase worth carrying into the rewrite, from the author: the third thing finds
**case-specific meaning**. That is the generality failure in plainer English than anything
in the current draft, and it may be the better formulation to build on.

**The canon survey (`ARC-OP-14`).** Needs no code, runs entirely in Mode 1, and begins
with verifying claims that `190` makes from general knowledge and has not checked —
Anchor Modelling, SQL:2011 temporal features, and the stated rejection reasons for
Kimball and 6NF. Separate designs rejected for *authoring* cost from those rejected for
*runtime* cost; only the first set is reopened by machine authorship.

**The public dataset survey (`EVI-OP-2`).** Also needs no code. Sources must be
independently built, must genuinely share entities, and must permit identity to be
established by hand for a sample. Dutch public registers are the leading structural
candidate. This is the one task that makes progress regardless of how the argument
turns out.

Two smaller ones worth folding into whichever is chosen: register triage (`PRC-OP-5`),
and continuing the external review (`PRC-OP-1`), whose ranked target list has the
falsifiable core first and still untouched.

## Traps and warnings

**The repository is more confident than the project is.** Twenty-two documents written in
one sitting read as a settled design. One section has been tested and it failed on every
question. Do not mistake fluency for consensus.

**Nothing here has been verified.** [`050_prior-art.md`](../docs/00_concept/050_prior-art.md)
is a register of unchecked leads and says so. `190` §6 flags its own unverified claims.
The economics have no number (`CON-OP-2`). The repository is, at present, entirely
assertion apart from two citations and one review pass.

**A review note is not an edit.** §III carries a challenge banner and its text is
unchanged. That is deliberate. Dispositions become register rows; documents change
later, once, on purpose.

**The assignment for the first external pass was set by the model that wrote the object,**
so the question selection is unreviewed by construction. A second pass should be assigned
by someone else, or at minimum instructed to attack what the assignment failed to ask.

**Chain the thread; do not widen the prompt.** The first attempt at that pass sent the
whole assignment at once, exceeded the device bridge's sixty-second ceiling and orphaned
the Codex session. [`510_external-review.md`](../docs/50_process/510_external-review.md)
says this in as many words and was ignored anyway. One question per turn, word-capped.

**The apparatus now exceeds the work, visibly.** Fifty-one files, thirty-four open
rows, a register, a handover series, a process convention and a checker — and no code,
no data, no verified fact. `PRC-OP-2` holds this open deliberately. The next session
should add no new conventions and no new documents unless a specific failure demands one.

**The author's intuitions are data.** The contributions that changed the direction of
this session were an external attack, the author's hunch about bitemporality, and his
correction of an inherited convention the model was enforcing beyond its intent. None
came from the model drafting alone. `PRC-OP-4` records the ratio and what to do about it;
`PRC-OP-2` records the convention failure and its general form is in
[`../docs/50_process/500_working-method.md`](../docs/50_process/500_working-method.md).

When the author's instinct and the written argument disagree, the instinct is a
compressed report from twenty-six years of observation. Find out what it is compressing
before arguing with it.

**Git mechanics.** Deletion in the connected folder is disabled by default, so git leaves
stale `.git/index.lock` and temp objects behind after a commit until deletion is
permitted. If git misbehaves, check for `.git/index.lock` first.

## Do not reopen

- Models never operate in the data path — [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md).
- Autonomy is tiered — [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).
  *(The tiering is settled as this project's frame. Whether it is original is `CON-OP-1`
  and remains open.)*
- Argument, then proof of concept on public data, then offering — [ADR-0006](../docs/20_decisions/0006-project-mode.md).
- `nsdn` as the handle, the biological metaphor kept private — [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md).
- The register, handover and enforcement apparatus — [ADR-0007](../docs/20_decisions/0007-register-and-handover-apparatus.md).
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).

## What session 01 did not do

No prior-art verification. No cost arithmetic. No dataset survey. No code. No data. No
review of anything except one section of one document. No push to GitHub.

# nsdn — Handover 02: the vocabulary is ruled, and the argument has a candidate spine
## Written 2026-09-20 at the close of session 02, for a fresh session

> **STATUS: HISTORICAL (superseded 2026-09-20)** — succeeded by
> [HANDOVER_03_2026-09-20_spine-candidate-failed.md](HANDOVER_03_2026-09-20_spine-candidate-failed.md).
> Its candidate spine, `CON-OP-11`, failed external review the same day.

---

## First actions

1. `git log --oneline -8` — expect head at the session 02 documentation commits.
2. `python tools/check_repo.py` — must pass before anything is changed.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority
   on what is open; this handover is orientation only, and where the two disagree the
   register wins. It has grown by a third since Handover 01 and is now the largest object
   in the repository.
4. Read [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md), then
   `CON-OP-11` and `ARC-OP-17` in the register, then
   [`../docs/10_architecture/190_machine-authored-design-canon.md`](../docs/10_architecture/190_machine-authored-design-canon.md).
   That is where the argument now lives.

## Outstanding action for the author, not the model

**The repository has still never been pushed.** Unchanged from Handover 01. `origin` is
configured to `https://github.com/henryjvanderlinden-cloud/business-intelligence.git`, the
repository does not exist on GitHub, and these sessions hold no credentials. The author
creates the empty repository — no README, no .gitignore, no licence — and runs
`git push -u origin main` from `C:\Git\business-intelligence`. Visibility remains
undecided; the reasoning favoured private until the Mode 1 gate.

## Where the project stands

Session 02 was a conversation, not a drafting session. The author read back the project in
his own words — three faculties on a substrate of data, deterministic engines for data
logistics, the second faculty applying broad and specific generalisations, the human ideally
there only for final adjudication — and asked what the model thought. The model agreed with
part, attacked the rest, and the author accepted the attack. The session then documented the
exchange and wrote nothing else.

Eight ADRs are settled. Forty-five register rows are live, eleven of them opened in this
session. Nothing has been built, nothing has been verified, and no data has been touched.

**What was ruled.** [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md):
data is the substrate, the three are faculties, each has a mandate, and a faculty is named
by its function and never by its implementation. `CON-OP-9` closes to `RULED` on that, with
the repository-wide rename as its residual. `CON-OP-13` rules the sensing-versus-memory
distinction: data in flight is sensory, data captured and stored is memory, and the
selection between them is where pruning lives.

**What was found, and it may matter more than what was ruled.** The author's distinction
between broad and specific generalisations supplies the middle term
[`005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III lacks, and supplies it by
conceding the external pass's Q3 finding rather than resisting it. Generalisations occupy an
axis of domain size; what collapsed is the threshold at which a generalisation repays its own
authorship. On that reading the canon-cost argument and the statability argument are one
claim at two altitudes, and `CON-OP-8`'s either/or dissolves. That is `CON-OP-11`, and it is
the candidate spine for the rewrite.

It is also unexamined by anyone. It was produced inside one exchange, at the moment a tidy
synthesis was most welcome, by the model that will set its review assignment.

## Task for the next session, in one sentence

Rewrite [`005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III against `CON-OP-5`,
`CON-OP-6`, `CON-OP-7`, `CON-OP-8` and `CON-OP-11`, settling `CON-OP-10`'s naming and
executing `CON-OP-9`'s rename in the same pass.

## Why that task and not another

`PRC-OP-2` resumed this session on its own stated condition — the register passed forty live
rows — and `PRC-OP-5`'s triage moved from cheap to overdue. The register grew by a third in
one conversation and not one row closed. **The next session should close rows or execute
residuals, and should treat opening a new one as a cost.**

The §III rewrite is the instrument that does most of that at once: it decides `CON-OP-5`,
`CON-OP-6`, `CON-OP-7`, `CON-OP-8`, `CON-OP-10` and `CON-OP-11`, and executing the rename
closes `CON-OP-9`'s residual and lands the check that
[ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md) deliberately deferred.
`CON-OP-13`'s residual — sensing versus memory into
[`020_critique.md`](../docs/00_concept/020_critique.md) §5 and
[`030_glossary.md`](../docs/00_concept/030_glossary.md) — travels in the same pass, since it
touches the same documents.

The alternatives from Handover 01 are unchanged and still unstarted: the canon survey
(`ARC-OP-14`), the public dataset survey (`EVI-OP-2`), and the external review of the
falsifiable core (`PRC-OP-1`). The dataset survey remains the one task that makes progress
regardless of how the argument turns out, and it has now been deferred twice.

## Traps and warnings

**The register is now the apparatus failure it was written to prevent.** Forty-five live
rows, no priority, dependencies stated in prose inside the rows, and three clusters that
must be worked together (`CON-OP-11` and its five dependents; `ARC-OP-17` with `ARC-OP-18`,
`ARC-OP-5`, `ARC-OP-6` and `EVI-OP-1`; `ARC-OP-19` with `ARC-OP-20` and `ARC-OP-15`). This
project's sharpest architectural argument is that an unranked queue wastes the scarce
resource that has to answer it. The register has now violated that finding at a third again
the scale at which it was first noticed.

**`CON-OP-11` is the most attractive idea in the repository and the least examined.** It
arrived as a synthesis, it resolves two open rows at once, it makes the manifesto's problem
go away, and it was written by the model in the same exchange that produced it. Every one of
those is a reason for suspicion rather than confidence. Its falsifier is `EVI-OP-5` and its
nearest prior art is `CON-OP-12`; neither has been touched.

**Correlated error is the finding most likely to be forgotten, and it is load-bearing.**
`ARC-OP-17` says that a system reasoning through locally-general rules breaks the calibration
mechanism [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) rests on, and breaks
it silently — a precision figure computed the current way looks exactly as trustworthy as one
computed correctly. If `CON-OP-11` survives review, this row is not optional.

**Do not treat the author's agreement as adjudication by a third party.** The author agreed
with every counter the model raised in this session. That is one reader agreeing with one
writer, and [`500_working-method.md`](../docs/50_process/500_working-method.md)'s model-switch
rule is unsatisfied by it.

**Everything from Handover 01 still applies**, and two items especially: nothing in this
repository has been verified, and the apparatus still exceeds the work. Add no new
conventions and no new documents unless a specific failure demands one.

**Git mechanics.** Deletion in the connected folder is disabled by default, so git leaves a
stale `.git/index.lock` and temporary objects behind after a commit until deletion is
permitted. If git misbehaves, check for `.git/index.lock` first.

## Do not reopen

- Models never operate in the data path — [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md).
- Autonomy is tiered — [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).
  *(`ARC-OP-19` asks whether the enumeration is complete. That extends the tiering; it does
  not reopen it.)*
- Argument, then proof of concept on public data, then offering — [ADR-0006](../docs/20_decisions/0006-project-mode.md).
- `nsdn` as the handle, the biological metaphor kept private — [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md).
- The register, handover and enforcement apparatus — [ADR-0007](../docs/20_decisions/0007-register-and-handover-apparatus.md).
- Data is the substrate; the three are faculties; each has a mandate; a faculty is never
  named after its implementation — [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md).
  *(The second faculty's own name is `CON-OP-10` and is open. The collective noun is not.)*
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).

## What session 02 did not do

No prior-art verification. No cost arithmetic. No dataset survey. No code. No data. No push
to GitHub. No document was edited: every finding landed in the register or in ADR-0008, and
[`005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III still carries its challenge
banner and its unchanged text.

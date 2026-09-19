# nsdn — Handover 01: the repository is established, the argument is untested
## Written 2026-09-19 at the end of session 01, for a fresh session

> **STATUS: CURRENT.**

### Where we stand

Repository at `C:\Git\business-intelligence`, branch `main`, remote
`https://github.com/henryjvanderlinden-cloud/business-intelligence.git`. Whether the
first push has happened depends on the author; the remote is configured and the push is
his to run, since this session's sandbox holds no GitHub credentials.

Three commits expected at handover time:

- the scaffold — concept, critique, architecture, ADRs 0001–0005, roadmap;
- ADR-0006 and the resolution of open questions 1 and 2;
- this apparatus — register, handovers, process conventions, checker, ADR-0007.

**First actions for a fresh session**, in order: `git log --oneline -5`; read
[`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md); read
[`../docs/00_concept/020_critique.md`](../docs/00_concept/020_critique.md) and
[`../docs/10_architecture/105_autonomy-tiers.md`](../docs/10_architecture/105_autonomy-tiers.md),
which carry the argument everything else rests on; run `python tools/check_repo.py` and
confirm it passes before changing anything.

### What session 01 actually did

Took a long-form brief from the author — twenty-six years in business intelligence,
proposing an agent-driven system that discovers, models and exploits an organisation's
data landscape — preserved it verbatim, critiqued it, and built an architecture around
the critique's central reframing: that autonomy is not uniform but tiered, structural to
semantic to teleological.

Settled seven decisions (ADRs 0001–0007), including the project's mode — argument first,
then proof of concept on public practice data, then offering — and the adoption of the
compendium's register, handover and enforcement apparatus.

Wrote [`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) last,
at the author's request: the argument stated plainly, organised around the shift from two
components to three and the relocation of the bottleneck from construction to
adjudication. It is the document most likely to become public at the Mode 1 gate and the
one most in need of the external pass, since it asserts more than the rest of the
repository does.

### The external pass ran, and the manifesto lost

[XREV_2026-09-19_manifesto-statability_sol](../docs/30_research/notes/XREV_2026-09-19_manifesto-statability_sol.md)
— manifesto §III, adversarial, on gpt-5.6-sol. FAILS on all three questions.
`CON-OP-5`, `CON-OP-6` and `CON-OP-7` opened; `CON-OP-4` folded. §III now carries a
challenge banner and is **unchanged** — the rewrite is deliberate and has not happened.

**The next session's most likely first job is that rewrite**, and it is not a patch.
If the `CON-OP-5` repair holds, statability reduces to articulability plus generality
plus observability, and §III is restructured rather than annotated. `CON-OP-7(a)` should
be settled first if possible, since it decides whether the section's central example
survives at all.

Note for whoever runs the next pass: the assignment was set by the model that wrote the
object, so the questions are unreviewed by construction. A second pass should be
assigned by someone else, or at minimum should include the instruction to attack what the
assignment failed to ask about.

### A third candidate arrived late, and it may outrank the other two

[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md),
from the author's observation that bitemporal validity has a third axis — the rule set
that produced the derived data. Generalised: every methodology in this field is a
compromise between correctness and human maintenance cost, and the canon is full of
designs rejected on the cost side of a trade whose terms have changed.

`ARC-OP-14` is the research programme that follows: survey the canon, separate designs
rejected for *authoring* cost from those rejected for *runtime* cost, re-evaluate the
first set. It needs no code, runs in Mode 1, and starts with verifying claims that
document makes from general knowledge and has not checked.

`CON-OP-8` asks the larger question: whether this framing should replace statability as
the manifesto's spine, given that §III is losing its own review. It is empirically
checkable against an existing literature rather than defensible only against philosophy —
but it is also a narrower claim, explaining modelling choices while saying nothing about
semantic inference. Decide it inside the §III rewrite.

`ARC-OP-15` is the tension it creates and the one to watch: if ruling is the scarce act,
machine-optimal storage still owes a human-comprehensible surface to rule on.

### This session's task, in one sentence

There isn't one yet — the next session's task is chosen by the author, and the two
candidates are stated below.

### The two live candidates

**Candidate A — continue the external review (`PRC-OP-1`, partly discharged).** One
document of twenty-two has been reviewed. The falsifiable core — that business keys are
machine-proposable at adjudication-worthy precision — is ranked first in the convention
and remains untouched, as does the three-tier distinction (`CON-OP-1`). Adversarially,
one object per pass,
per [`../docs/50_process/510_external-review.md`](../docs/50_process/510_external-review.md).
Codex is already wired as a local MCP server, so the transport exists.

**Candidate B — the public dataset survey (`EVI-OP-2`).** Needs no code, no review
apparatus and no decisions. Produces the thing Mode 2 cannot start without. Dutch public
registers are the leading structural candidate.

A is the higher-value and more uncomfortable of the two — as the first pass demonstrated.
B is the one that makes progress regardless of how A turns out. They are independent and
could run in either order; running A first risks discovering that the architecture needs
rewriting before the survey is spent, which is an argument for A.

Ahead of both sits the §III rewrite, which is now owed.

### Traps and warnings

**Chain the thread; do not widen the prompt.** The first attempt at the external pass
sent the whole assignment at once and exceeded the device bridge's sixty-second ceiling,
orphaning the Codex session. The convention in
[`../docs/50_process/510_external-review.md`](../docs/50_process/510_external-review.md)
says this in as many words and was ignored anyway. One question per turn, word-capped.

**The repository is more confident than the project is.** Twenty architecture documents
written in one sitting read as a settled design. They are one model's first pass on one
person's brief. The prose is deliberately subjunctive; do not let a fresh session mistake
fluency for consensus.

**`020_critique.md` is the load-bearing document, not the architecture.** If the critique
is wrong — particularly §1, the three kinds of analysis — most of the architecture
follows it into the ground. Review it before building on it.

**The author's own framing is the thing to preserve.** He supplies intuitions and
domain judgement; the model supplies structure and prior art. A session that takes over
the intuition half produces something confident and hollow. When his instinct and the
argument disagree, the instinct is data.

**Do not expand the apparatus.** See `PRC-OP-2`. This repository now has a register, a
handover series, a process convention and a checker while containing no code. That is
justified at this size and stops being justified quickly.

**The sandbox cannot push to GitHub**, and `git` deletion in the connected folder is
disabled by default — the first commit left stale `.git` lock files behind until
deletion was permitted. If git misbehaves in a fresh session, check for
`.git/index.lock` first.

### Do not reopen

- Models never operate in the data path — [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md).
- Autonomy is tiered — [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).
  *(The tiering itself is settled as this project's frame; whether it is original is
  `CON-OP-1` and is open.)*
- Argument, then proof of concept on public data, then offering — [ADR-0006](../docs/20_decisions/0006-project-mode.md).
- `nsdn` as the handle, metaphor private — [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md).
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).

### What this session did not do

No prior-art verification — [050_prior-art.md](../docs/00_concept/050_prior-art.md) is a
register of leads, every one of them unchecked, and it says so. No cost arithmetic
(`CON-OP-2`). No external review. No code. No dataset survey.

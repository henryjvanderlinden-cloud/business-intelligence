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

### This session's task, in one sentence

There isn't one yet — the next session's task is chosen by the author, and the two
candidates are stated below.

### The two live candidates

**Candidate A — the external review pass (`PRC-OP-1`).** Everything in this repository
was drafted by one model in one session and is unreviewed by construction. The argument
has exactly one reader and that reader wrote it. Attack the manifesto's core claims
(`CON-OP-4`), the three-tier distinction (`CON-OP-1`) and the machine-proposable-keys
claim, adversarially, one object per pass,
per [`../docs/50_process/510_external-review.md`](../docs/50_process/510_external-review.md).
Codex is already wired as a local MCP server, so the transport exists.

**Candidate B — the public dataset survey (`EVI-OP-2`).** Needs no code, no review
apparatus and no decisions. Produces the thing Mode 2 cannot start without. Dutch public
registers are the leading structural candidate.

A is the higher-value and more uncomfortable of the two. B is the one that makes
progress regardless of how A turns out. They are independent and could run in either
order; running A first risks discovering that the architecture needs rewriting before
the survey is spent, which is an argument for A.

### Traps and warnings

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

# ADR-0008 — Three faculties act on a substrate, each under a mandate

- **Status:** Accepted
- **Date:** 2026-09-20
- **Supersedes:** —
- **Superseded by:** —

## Context

[005_manifesto.md](../00_concept/005_manifesto.md) calls the three things that build a
data environment **components**, which is serviceable and under-claims. The distinction
the manifesto draws is not only what each can do but what each is *entitled* to do:
deterministic machinery executes and asserts nothing, the second faculty proposes, humans
rule and set purpose. That is an authority structure, and
[ADR-0005](0005-three-autonomy-tiers.md) is an assignment of mandates rather than of
capabilities.

`CON-OP-9` opened the vocabulary question on 2026-09-19 and observed that a category
error came first: the brief and the manifesto both list data alongside the three, and no
single word fits all four because the list mixes material with agency. The three do work;
data is what they work on.

The row recorded a provisional recommendation and an instruction not to rename anything
across the repository until it closed, on the grounds that renaming twice costs more than
deciding late. On 2026-09-20 the author ratified the recommendation, in his own
formulation: *three faculties — the deterministic engines, the second faculty for
analysis and design, the human for adjudication — all on a substrate of data.*

A second question arose in the same exchange. The author named the second faculty after
its current implementation. That is the one naming move this repository has so far
avoided, and it is worth forbidding explicitly rather than by habit.

## Options considered

*Components.* Neutral, standard, already in use, and it costs nothing to keep. Rejected
because it describes parts of a mechanism and is silent on authority, which is the
dimension the whole architecture turns on. A component has a function; a faculty has a
warrant.

*Capacities.* The same work without the organism connotation, and safe. Rejected as
duller with no compensating precision.

*Powers* or *offices.* These carry the authority dimension most exactly, and *office* is
principled rather than decorative given the manifesto's argument that this infrastructure
is substantially a bureaucratic artifact. Rejected on register: the author writes
political theory, and the vocabulary would read as imported from it.

*Tiers* or *layers.* Ruled out for implying a stacking that is false and for colliding
with the autonomy tiers of [ADR-0005](0005-three-autonomy-tiers.md).

*Agents* or *actors.* Unusable. Total collision with "AI agent".

*Faculties.* Adopted. A faculty is a power to do a kind of work, carrying authority in
the older sense, with no collision anywhere in data or machine-learning vocabulary. Its
acknowledged cost is that faculties conventionally belong to one mind, which smuggles
back the organism metaphor [ADR-0003](0003-codename-nsdn.md) set aside. That cost is
accepted: ADR-0003 keeps the metaphor as a private generative heuristic rather than
banning it, and the collective noun is the weakest place the metaphor could re-enter.

## Decision

**Data is the substrate.** It is not a member of the set. The substrate is what the
faculties act on, and a list that mixes the two is a category error.

**The three are faculties.** Deterministic machinery; the second faculty, which
interprets and designs; and the human faculty.

**Each faculty has a mandate** — the grant of authority that says what it is entitled to
do, as distinct from what it is able to do. The term is the author's own, from
[010_vision.md](../00_concept/010_vision.md): *"a properly instructed LLM with enough
mandate."* The vocabulary for the authority dimension is therefore native to this project
rather than imported into it. [ADR-0005](0005-three-autonomy-tiers.md)'s tiers are the
mandate of the second faculty, stated per kind of claim.

**A faculty is named by its function and never by its implementation.** *The LLM*, *the
model* and *the AI* are not names of a faculty. Models are the current substrate of the
second faculty's work; they are not the faculty, they will be replaced, and a vocabulary
that names the faculty after them dates the argument and reduces it to a claim about a
technology.

## Consequences

**A rename is owed and is not done.** The repository says *components* throughout, and
[100_system-overview.md](../10_architecture/100_system-overview.md) calls the second
faculty's capability *Sense-making*. `CON-OP-9` stays live as `RULED` for exactly this
reason: the ruling is taken, the work is not.

**The second faculty has no name.** The ruling forecloses the implementation names and
the author's own formulation, *analysis and design*, collides with the automated analyses
of Phase 3. `CON-OP-10` holds the question and it is blocking, because every document the
§III rewrite touches needs the word.

**The enumeration exposes a gap in [ADR-0005](0005-three-autonomy-tiers.md).** Naming the
second faculty's work as interpretation *and design* makes visible that design claims —
which modelling pattern, which grain, which compile target — are not classified by any of
the three autonomy tiers. That is `ARC-OP-19`, and it extends the tiering rather than
reopening it.

**This vocabulary is unenforced.** Per [`../../AGENTS.md`](../../AGENTS.md) rule 11 a
convention without a check is decoration. No check is added here, deliberately: a check
forbidding *component* or *the LLM faculty* would fire on every document in the
repository until the rename is done, which is noise rather than enforcement. The check
lands in the same commit as the rename, and until then this ADR is marked as an
unenforced convention.

**Revisit** if the second faculty's name cannot be settled without changing the
collective noun, or if *faculties* is found in practice to drag the organism metaphor
into documents written for outside readers, which is the specific failure ADR-0003 exists
to prevent.

# 145 — Entropy and pruning

The component the brief omits, and the one most likely to decide whether the system is
an asset or a liability in year two.

## The failure it prevents

A system that proposes, builds and enriches continuously, with no opposing force,
accretes without limit. The end state is familiar from every large data platform that
has ever existed, except faster: thousands of objects, hundreds of marts with no
consumers, a catalogue in which the true entries are indistinguishable from the stale
ones, and a maintenance burden that exceeds the value of what is maintained. Automation
does not avoid this outcome; it accelerates arrival at it.

The metaphor in the brief supplies the answer better than the brief realises. Synaptic
pruning is not damage. It is the mechanism by which a developing network becomes
capable — connections are overproduced, then removed on the basis of use. A system built
on a neural analogy that models growth and not pruning has taken half the metaphor.

## Demand justification

Every artifact the system creates carries a reason to exist, recorded at creation:

- the **question** it answers, or the **decision** in the register it serves;
- the **consumer** — a named person, team, report or downstream artifact;
- an expected **review date**.

An artifact with none of these is not built. This is a stronger constraint than it
sounds, and it is deliberately stronger at Tier 3 than at Tier 1: a profiling record
needs no consumer, a mart does.

## Usage as evidence

Justifications decay, so they must be tested against observation: query logs against
generated objects, dashboard access, downstream dependency, adjudication activity. An
artifact whose stated consumer has not touched it in two quarters has a justification
that is no longer true, and the system should say so rather than wait to be asked.

## The pruning process

Pruning runs on a cadence, with the same standing as construction, and proceeds in
stages rather than by deletion: **flag** (justification appears void, reported to the
owner), **deprecate** (marked in the catalogue, consumers warned, still built),
**dormant** (no longer refreshed, definition retained), **archived** (definition
retained in git, objects dropped).

Because every artifact is generated from a declarative definition under version control,
archival is cheap and reversal is cheaper — which is what makes aggressive pruning
safe. This is the same property that makes the vault the right target model: nothing
that was learned is lost by removing what was built from it.

## Pruning the context layer

Objects are not the only thing that accretes. Assertions age, hypotheses are superseded,
cards describe tables that no longer exist. Retired material is marked and kept, not
deleted — a retired hypothesis is evidence that a question was already considered, and
an agent that cannot see it will raise it again. But it must be *marked*, or it will be
read as current.

## Reporting

Pruning is the part of an autonomous system that most needs to be visible, because it is
the part humans most need to trust. A periodic report — what was flagged, deprecated,
archived, and on what evidence — is the minimum. It also doubles as the clearest
possible demonstration that the system is not merely productive.

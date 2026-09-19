# 190 — The design canon under machine authorship

Opened 2026-09-19, session 01, from the author's observation about bitemporality. This
document may be more important than its position in the numbering suggests; see §5.

## 1. The observation

Bitemporal tables record two time axes: **valid time**, when a fact was true in the
world, and **transaction time**, when the system came to believe it. The author's point
adds a third thing that also moves — **the rule set**. Derived data is a function of raw
data *and* of the logic that refined it, and that logic has versions. Three different
questions follow, and they have three different answers:

- *What do we now believe was true then?* — valid time, current rules. Restatement.
- *What did we report then?* — transaction time, rules as of then. Audit.
- *What would we have reported then, knowing what we know now?* — historical valid time,
  current rules. The reconciliation between the first two.

Financial restatement, regulatory reporting, insurance reserving and clinical data all
need the distinction, and most warehouses handle it by archaeology: find the old code in
version control, find the old data in a backup, and hope. It is a known problem with a
known shape, and it is not solved because maintaining the third axis by hand is
punishing.

## 2. The correction to the intuition

The author's instinct is that language models are "more comfortable" navigating this than
humans. That formulation should be resisted, because it is the flattering version and it
is not what is true.

Models are not reliably better at interval logic. Overlapping-interval reasoning across
three axes is a place where they make errors, and asking one to *reason* about temporal
validity at query time would be a direct violation of
[ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md).

What has actually changed is the **cost of authorship and maintenance**. The burden of
bitemporality has never been conceptual — the theory is settled and has been for decades
— it is that someone must write the interval predicates correctly, keep every downstream
query consistent with them, and re-derive them whenever anything changes. That work is
mechanical given a declaration. It is exactly the compile-judgement-into-determinism move
this whole project rests on: the model emits the temporal machinery once, deterministic
engines execute it forever, and no model reasons about an interval at runtime.

So the principle is not *models are good at time*. It is:

> **A design's cost is not its intrinsic complexity but its authoring and maintenance
> burden, and that burden has collapsed. Designs that were correct-but-unaffordable are
> now merely correct.**

## 3. The generalisation, which is the valuable part

Once stated that way, bitemporality is an instance rather than the point. **Every
methodology in this discipline is a compromise between correctness and human maintenance
cost, and the canon is full of designs that were rejected on the cost side of that
trade.**

Kimball's star schema is explicitly a usability compromise — denormalise so that humans
can query and maintain it. Data Vault's object count is its acknowledged price, which
[140_data-vault-automation.md](140_data-vault-automation.md) already argues stops
mattering under machine authorship. Anchor Modeling takes the same logic to 6NF, is
formally superior on schema evolution, and is almost unused. None of these were rejected
because they were wrong.

A provisional list of candidates, each of which is a claim to be tested rather than a
recommendation:

**Rule-versioned bitemporality**, as above. The payoff is that reproducing the April
board pack exactly becomes a query rather than an excavation.

**Sixth normal form and anchor-style modelling.** Every attribute its own table, fully
temporal. Its property is lossless schema evolution — adding an attribute never migrates
anything — and its cost is object count and join complexity, one of which no longer
matters. See the caveat in §4.

**Insert-only everything.** Never update, never delete. Storage is cheap; the reason
people still overwrite is the query complexity of reconstructing current state, which is
generated view logic.

**Column-level lineage, exhaustively.** Most organisations maintain lineage at table
level because column level is too much work by hand. It is mechanically derivable from
parsed SQL, and it is what makes impact analysis and the semantic regression in
[160_evaluation-and-regression.md](160_evaluation-and-regression.md) actually work.

**Per-fact provenance.** Every derived row carrying the rule version, source records and
assertions it depended on. Prohibitive by hand; close to free when generated, and it is
what makes the audit story in
[150_trust-and-blast-radius.md](150_trust-and-blast-radius.md) real rather than claimed.

**Explicit units, currencies, timezones and grain on every measure.** Humans shortcut
this constantly and it is a large share of silent error in real warehouses.

**Redundant physical representations.** The same content as vault, star and wide table
for different consumers was unmaintainable when a human maintained each; from one
declaration it is a compile-target problem.

**Assertions at maximum granularity**, generated from profiles and pruned by usage.

## 4. What did not change, and the live tension

Two disciplines are needed to keep this from becoming a licence to generate anything.

**Separate designs rejected for authoring cost from designs rejected for runtime cost.**
6NF's join explosion was a query-performance objection as much as a maintenance one.
Columnar engines and cheap compute have moved that too, but not by the same mechanism and
not to the same degree, and conflating the two would let this document justify designs
that are still slow. Every candidate in §3 needs its rejection reason identified before
it is re-evaluated.

**Machine-optimal storage still owes a human-comprehensible projection.** This is the
sharper constraint, and it is in direct tension with the rest of this project. If ruling
is the scarce act, then everything the human must rule on has to be comprehensible to a
human. A four-thousand-table anchor model that nobody can hold in their head is not a
problem for the machinery and is very much a problem for adjudication. The resolution is
presumably that the physical model optimises for machine authorship while the
*adjudication surface* optimises for human comprehension, and that these are different
artifacts generated from the same declaration — but that is an assertion, not a design,
and it is open as `ARC-OP-15`.

## 5. Why this may matter more than its numbering

[005_manifesto.md](../00_concept/005_manifesto.md) §III is currently under challenge and
losing: the external pass of 2026-09-19 found its central distinction equivocal and its
claimed novelty unsustainable at the level of mechanism.

This document may contain a sturdier framing of the same underlying thesis, and it was
the author's intuition rather than the model's. It makes an **empirically checkable claim
about an existing literature** — that the canon contains known-correct designs rejected
for human-cost reasons, and that the cost has changed — rather than a conceptual claim
about kinds of knowledge that must be defended against forty years of tacit-knowledge
philosophy. It also yields a concrete research programme: go through the canon, identify
every design rejected on maintenance-burden grounds, separate those from designs rejected
on runtime grounds, and re-evaluate the first set.

That is a better shape of argument than the one the manifesto currently rests on. Whether
it should become the manifesto's spine is `CON-OP-8`, and it should be decided as part of
the §III rewrite rather than separately.

## 6. Unverified

Anchor Modelling, SQL:2011's temporal features, and the specific rejection reasons
attributed above to Kimball and to 6NF are stated from general knowledge and have **not**
been checked against sources in this session. Per [`../../AGENTS.md`](../../AGENTS.md)
rule 8 they are hypotheses. Verifying them is the first half of `ARC-OP-14`.

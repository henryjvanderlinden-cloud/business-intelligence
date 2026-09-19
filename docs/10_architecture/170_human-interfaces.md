# 170 — Human interfaces

The brief names four points of human contact: help accessing sources, help understanding
meaning, help obtaining external data, and discussion of insights. They are treated here
as four surfaces with one shared principle.

## The principle

Human attention is the binding constraint on the entire system, more than cost, more
than model capability, and more than access. Every interface is therefore designed
around a single question: *what is the smallest, best-targeted demand we can make on a
person's time, and what does it buy us?*

A system that asks opportunistically will exhaust its welcome within a fortnight, and a
system nobody answers degenerates into whatever it can infer alone — which is to say,
into a profiling tool.

## Surface 1 — The adjudication queue

The primary interface. A ranked list of open questions, each with the hypothesis, the
evidence for it, what depends on it, and the cost of getting it wrong.

Ranking is by **expected information gain**: how many downstream hypotheses this
question unblocks, weighted by their own importance. This is computable over the
hypothesis graph and is the component of this design most clearly absent from existing
catalogue tooling, which typically presents metadata gaps in arbitrary or alphabetical
order.

Questions are routed to the person most likely to know — inferred from source ownership,
commit history, query logs, and previous adjudications — and batched so that one sitting
resolves a coherent group. A ruling is recorded as an assertion with the ruler's name
attached, permanently.

Disagreement between adjudicators is represented, not resolved. Two named people
asserting different things about the same column is a fact about the organisation and
frequently a more valuable finding than either assertion.

The first implementation is pull-request review, per
[120_context-layer.md](120_context-layer.md). It is unlovely and it works on day one.

## Surface 2 — Source onboarding

Where a human supplies what no crawl can: that a source exists, who owns it, what it is
for, what the legal basis is, and which of its tables are junk. This surface produces
source contracts and is the gate through which the system's reach expands. It is
deliberately a human act.

## Surface 3 — The decision register

The teleological anchor. A maintained record of the decisions the organisation makes —
recurring and one-off, with cadence, owner, and the evidence currently used. Every mart
and every analysis cites an entry.

This is the surface most likely to be skipped, because it looks like documentation and
produces nothing immediately. It is also the one that determines whether the automated
analysis layer produces anything anyone acts on. A system with a rich context layer and
an empty decision register will be impressively well-informed about nothing in
particular.

## Surface 4 — Findings

Where the system reports what it has concluded: analyses with their narrative, quality
issues with suggested fixes, gaps with suggested external sources, pruning proposals,
and its own cost.

The design constraint here is credibility rather than presentation. Every finding
carries its lineage, its confidence, and the assertions it depends on, so that a reader
can disagree with it specifically rather than dismissing it generally. A finding that
cannot be interrogated will be ignored the second time it is wrong.

This surface is also the natural place for the system to report its own uncertainty —
what it does not know, what it is guessing about, and which unanswered question is
currently costing the most.

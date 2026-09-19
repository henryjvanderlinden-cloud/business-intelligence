# 130 — The agent loop

How work actually gets done, and why it should be many small jobs rather than one long
mind.

## Jobs, not a loop

The tempting design is a long-running agent that surveys the landscape and decides what
to do next. It is the wrong shape. It is expensive, unresumable, hard to test, hard to
attribute cost to, and impossible to reason about when it goes wrong at hour six.

The alternative is a **queue of small, typed, idempotent jobs**, each with a declared
input (a set of card URNs), a declared output (a diff to the context layer, or a
generated artifact), a budget, and a completion test. A scheduler chooses what to run.
An agent runs one job, writes its result as a proposed diff, and exits.

This yields the properties that matter: any job can be retried; any job's cost is
attributable; any job's output is reviewable as a diff; and the system's state lives in
the context layer rather than in a conversation.

## Job types

Roughly one per capability, and each small enough to state in a sentence.

*Profile this dataset. Describe this dataset. Propose business keys for this dataset.
Test this joinability hypothesis. Formulate the question that would resolve this
hypothesis. Generate the vault objects implied by this set of assertions. Propose a mart
for this decision. Write the analysis for this mart. Review this assertion set as a
second model. Find artifacts that have lost their justification.*

## The proposal–review discipline

No job writes an assertion directly. Every job emits a **proposal**: a diff to the
context layer with its evidence attached. Proposals are accepted automatically at Tier 1
(structural facts, where re-computation is the check), on evidence threshold or
adjudication at Tier 2, and only by a human at Tier 3.

This is the mechanism by which "enough mandate", in the brief's phrase, becomes
something an organisation can actually grant, because the mandate is expressed as an
acceptance policy rather than as trust.

## Model routing

Tier 1 jobs are high-volume and mechanical; they should run on the smallest model that
passes their evaluation. Tier 2 jobs are few and consequential; they justify the
strongest available reasoning and a second opinion. A cheap and plausible quality
mechanism is **cross-model review**: one vendor's model proposes semantic assertions,
another's reviews them, and disagreement is routed to the adjudication queue rather than
resolved automatically. Disagreement between models is a useful signal precisely because
it is uncorrelated with either model's own confidence.

## Budget as a first-class input

Every job carries a token budget and a source-read budget, and reports actual against
both. Cost is attributed to the artifact it produced, which is what later makes it
possible to ask whether an artifact was worth its upkeep. A system that cannot answer
that question cannot prune honestly.

## Determinism where possible

Any step that can be deterministic should be. If a model has established that a column
is a business key, the generation of the hub is a template, not a generation. The model's
output is the *declaration*; the artifact is compiled from it. This keeps model cost
proportional to the number of decisions rather than to the number of objects, which is
the difference between a system that scales and one that does not.

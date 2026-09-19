# 410 — The first vertical slice

What to build first, and what it is meant to prove.

## The claim under test

*Business keys and cross-source entity identity can be machine-proposed at a precision
that makes human adjudication worth a person's time.*

Everything else in the design is engineering. This is the part that is either true or
not, and it can be tested in weeks rather than quarters. If it fails, the honest
response is to re-scope the project as a documentation and profiling tool, which would
still be useful and much smaller.

## Shape of the slice

Two sources that plausibly share entities but were built by different teams at different
times — the more different, the better the test. One business question that a real
person actually asks. End to end, narrow:

discover → profile → card → key hypotheses → adjudication → assertions → raw vault →
one mart → one analysis → tests that fire when something drifts.

Nothing is generalised. Every shortcut is permitted except in the hypothesis-generation
step, which is the thing being measured.

## What is measured

**Precision of key hypotheses** at the top of the ranking, scored against the
adjudicator's rulings. The headline number.

**Adjudication burden**: minutes of human time per correct assertion gained. If this
exceeds what a competent analyst would spend doing the same work unaided, the system has
no case.

**Evidence value**: which signals actually carried the correct hypotheses — sketch
overlap, naming, observed join predicates in query logs, or model inference. This
determines where subsequent effort goes, and the answer may well be that the cheap
signals do most of the work and the model's contribution is concentrated in a narrow
band. That would itself be a finding worth having.

**Cost** per source, per hypothesis, per assertion.

## Success and failure

*Success* is an adjudicator saying that the ranked queue told them something they did
not already know, or saved them work they would otherwise have done, and doing so at a
precision that made reading the list worthwhile.

*Failure* is a queue of plausible, fluent, wrong hypotheses — the specific failure mode
of language models on semantic tasks — or a queue that is right but only about things
that were already obvious from the column names.

Both outcomes are worth the weeks. The second failure is the more instructive, and the
more likely.

## Environment

[ADR-0006](../20_decisions/0006-project-mode.md) settles that the first environment is
built from public practice datasets. That is a better answer than the synthetic
landscape originally proposed here, and for a reason worth stating: public data is
*genuinely* messy, and its messiness was not designed by the person being tested. A
synthetic landscape flatters whoever built it; that failure mode is subtle, and it does
not announce itself.

The thing public data does not supply is an answer key. Precision against an
adjudicator's opinion is a weaker measurement than precision against ground truth, and
the falsifiable core of this project is a precision figure.

The resolution is to select public sources that satisfy three conditions
simultaneously, which is a stronger constraint than it first appears:

**They were built independently.** Different publishers, different eras, different
keying conventions. Two extracts from the same warehouse test nothing, because their
keys already agree.

**They genuinely share entities.** The same companies, addresses, vehicles,
institutions or municipalities, referred to by different identifiers. This is what makes
key hypothesis a real question rather than a string-matching exercise.

**Identity is establishable by hand for a sample.** Not for the whole population — for a
few hundred entities, carefully, once. That sample is the answer key, and building it is
a day of tedious work that makes every later number mean something. It should be built
*before* the system is pointed at the data, and by someone who has not seen the system's
hypotheses.

Dutch open data is unusually well suited to this, because several public registers
describe overlapping real-world entities with entirely different keying conventions and
independent institutional histories. The same holds for equivalent registers elsewhere;
the point is the structural property, not the jurisdiction. A candidate survey belongs
in [`../30_research/`](../30_research/) and is a good early Mode 1 task, since it can be
done before any code exists.

Two guards against self-flattery. Freeze the answer-key sample before development
begins, and hold part of it back entirely. And report separately the precision of the
cheap structural signals alone — sketch overlap, naming, observed join predicates —
because the project's claim is not that hypotheses can be generated, but that a model
adds something beyond what profiling already tells you. If it does not, that is the
finding.

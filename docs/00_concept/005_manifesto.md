# 005 — The third component

*The argument this project exists to test, stated as plainly as it can be stated. Written
2026-09-19. Unreviewed — see `PRC-OP-1`.*

## I. Two components

Every data environment ever built has been made of exactly two kinds of thing.

There is **deterministic machinery**: SQL, extraction jobs, schedulers, transformations,
models, tests. It executes reliably, at any scale, for as long as it is maintained, and
it understands nothing whatsoever. It cannot tell a customer identifier from a lottery
number; it applies rules it was given, faithfully, including the wrong ones.

And there is **the human factor**: the analyst who knows that the six customer tables
are not the same population, that the status code changed meaning in the 2019 migration,
that the number in the board report has been quietly wrong since somebody fixed a join
the wrong way. This component understands, and it neither scales nor executes.

The entire history of the discipline is the history of the boundary between them. Every
methodology — Kimball, Inmon, Data Vault, the semantic layer, the modern data stack — is
an attempt to move work across it: to take something a human had to decide each time and
turn it into something the machinery could execute every time. Conformed dimensions,
slowly changing dimension types, hub-and-satellite separation, declarative
transformation, tests as code. All of it is the same move, repeated for forty years.
**The progress of the field has been the migration of judgement into determinism.**

## II. Where the migration stalled

That migration has a hard boundary, and it is not a boundary of effort or tooling. It is
a boundary of *statability*.

Judgement migrates when it can be written down as a rule. Kimball could formalise
conformed dimensions because it is possible to say, in general, what a conformed
dimension is. Nobody has ever formalised *which of these six customer tables is
authoritative*, because the answer is not a rule. It is a fact about one organisation, on
one date, produced by a history of mergers, migrations and departures that nobody
recorded. There is no general form of it to state.

So the migration stopped, and what it left behind is what the human factor has actually
consisted of for the last twenty years: **not the interesting part of the work — the
unformalisable part.** Reading a schema nobody documented. Asking the one person who
remembers. Discovering, three weeks in, that the join everyone assumed was safe drops
eleven percent of the rows.

This residue is where data projects are slow, where they are expensive, and where they
fail. It is also, not coincidentally, the part no vendor has ever sold a product for.

## III. The third component

What has arrived is not a faster deterministic machine and not a cheaper analyst. It is a
third kind of component, and it is worth being precise about the three properties that
distinguish it, because every consequence follows from one of them.

**It forms judgements about particulars.** This is the new thing. Deterministic machinery
applies general rules. The third component reads a specific undocumented schema, in a
specific organisation, and forms a proposition about what it is for. It operates exactly
where the migration stalled — on the material that has no general form.

**Its throughput is of a different order.** An analyst cannot form ten thousand
hypotheses about column identity; the idea is not merely slow but incoherent. A machine
can, and this changes the shape of the problem rather than its speed. Ten thousand
hypotheses, each carrying its evidence, ranked, most of them right, converts an
intractable task — *understand this landscape* — into a tractable one: *rule on a ranked
list*.

**It is wrong at a rate deterministic machinery is not.** Not often, but irreducibly, and
— the dangerous part — it is wrong fluently, in well-formed sentences that carry no
signal of their own unreliability. Every safeguard in this project's architecture exists
because of this third property.

## IV. The re-partition

Three components, then, and the temptation is to describe the third as an assistant to
the other two. That is the wrong description. What has happened is a re-partition of the
whole work, and each component's job is best stated by what kind of thing it handles.

**Deterministic machinery handles everything statable as a rule.** Unchanged in kind.
Vastly expanded in volume, because the third component can write far more of it than
humans ever could. It remains the only trustworthy way to move data, and it should be
*more* jealously protected now, not less: the moment a probabilistic component enters
the data path, reproducibility, auditability and cost predictability are all forfeited at
once.

**The third component handles everything that requires reading particulars and forming a
proposition about them.** It proposes. It never disposes.

**The human factor handles adjudication and purpose.** Ruling on what is true, and
deciding what is worth knowing.

And here is the claim that matters, the one this project exists to test: the human
contribution does not so much shrink as change character. It moves from *doing the
unformalisable work* to *ruling on machine proposals about the unformalisable work*. The
same knowledge, applied at a different point, through far fewer hours, each worth far
more.

## V. The bottleneck moves

The most useful consequence of the re-partition is not that capacity increases. It is
that **the binding constraint relocates**, and almost every design mistake available here
comes from failing to notice that it has.

For forty years the bottleneck was construction. Everything the discipline built —
methodology, tooling, division of labour, the shape of a project plan, the shape of a
career — was organised around the scarcity of people who could build things correctly.

In a three-component world, construction is abundant. The bottleneck is **adjudication**:
the rate at which people who actually know can rule on what the machine proposes. It will
bind immediately, and it will bind hard, because the third component's output exceeds
human reviewing capacity from the first day and the gap widens from there.

Everything follows from this. A system that generates hypotheses without ranking them by
what their answers unlock is not using the new capability; it is wasting a human being.
A system that builds without pruning converts abundance into a maintenance liability. A
system that cannot say how it knows something forces re-adjudication of everything, which
is the same as having adjudicated nothing. The architecture in this repository is, in
its entirety, an answer to one question: *given that ruling is now the scarce act, how
should everything else be arranged around it?*

## VI. What does not change

Three things, stated because the enthusiasm around the third component routinely denies
all of them.

**Meaning still lives in the organisation, not in the data.** The third component cannot
conjure semantics that were never recorded. It can hypothesise them far better and far
faster than anything before it, and then it must ask. This is a permanent property of the
problem, not a limitation of current models.

**Purpose still comes from people.** Nothing in the third component knows what a business
is trying to decide. An analytic system with no model of the decisions an organisation
actually makes will produce observations that are statistically true and practically
worthless, at scale, forever.

**Determinism remains the only trustworthy execution.** The third component's value is in
deciding *what* the machinery should do. It should never be the machinery.

## VII. The honest counter

A manifesto that states only its good news is a sales document, and this project's whole
method is to state the condition under which it is wrong.

The claim in section IV — that the human contribution concentrates rather than
disappears — assumes that adjudication capacity is itself hard to commoditise, and that
the market can identify and will pay for judgement that is difficult to demonstrate in
advance and visible mainly when absent. Neither assumption is obviously true. If
capability is being commoditised because it can be, then adjudication may follow on the
same schedule, merely later. The test is observable and worth watching deliberately:
whether organisations begin buying review and assurance of machine-built data work as a
distinct, separately priced service, or absorb it into delivery at the old rate. That is
`BIZ-OP-1`, and it is the premise here most likely to be wrong.

A second, narrower counter. The falsifiable core of this project is that the third
component genuinely adds judgement rather than re-ranking evidence that profiling,
naming conventions and query logs already supply. If the cheap structural signals do most
of the work, then what has arrived is a very good interpreter of existing evidence rather
than a new component at all, and this document overstates the change. That is `EVI-OP-3`,
and it is answerable by a prototype rather than by argument.

## VIII. What this project is

An attempt to build the third component into a data environment deliberately rather than
incidentally: to take the work that was left behind when judgement stopped migrating into
determinism, and to move as much of it as possible into machine proposal and human
ruling — while conceding, in the architecture rather than in a footnote, everything that
cannot move.

Whether that is possible is an empirical question with a number attached. The rest of
this repository is the attempt to find out.

---

*Read next: [020_critique.md](020_critique.md) for the argument in detail,
[105_autonomy-tiers.md](../10_architecture/105_autonomy-tiers.md) for the tiering this
rests on, and [`../../registers/OPEN_POINTS.md`](../../registers/OPEN_POINTS.md) for what
is still open.*

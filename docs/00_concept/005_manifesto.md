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
unstatable part.** Reading a schema nobody documented. Asking the one person who
remembers. Discovering, three weeks in, that the join everyone assumed was safe drops
eleven percent of the rows.

This residue is where data projects are slow, where they are expensive, and where they
fail. It is also, not coincidentally, the part no vendor has ever sold a product for.

Section III sets out what statability is, in what way this material fails it, and why
that particular failure is the one the third component happens to answer.

## III. What statability is

> **⛔ UNDER CHALLENGE, 2026-09-19.** An adversarial pass on gpt-5.6-sol returned FAILS
> against every claim in this section:
> [XREV_2026-09-19_manifesto-statability_sol](../30_research/notes/XREV_2026-09-19_manifesto-statability_sol.md).
> Stability is not individually necessary (`CON-OP-5`); the conditions are not jointly
> sufficient, observability being absent (`CON-OP-6`); the articulability argument
> equivocates between a conclusion and the knowledge that warrants it (`CON-OP-7`); and
> the claimed distinction from Autor 2014 does not survive at the level of mechanism
> (`CON-OP-4`). **The text below is unchanged and stands as written** — a review note is
> not an edit, and the rewrite happens deliberately, once. Read it knowing that its
> central distinction is contested and currently losing.

The word is doing enough work in this argument to need defining.

**A piece of knowledge is *statable* when it can be expressed as a rule that a
deterministic machine can apply correctly to cases it has not yet seen.**

Three conditions have to hold together, and it is the failure of one in particular that
shaped the last twenty years of this field.

**Articulability.** It can be put into words or symbols at all. Some competence is held
only in the practitioner — the senior analyst who knows a number is wrong before she can
say why, and who, pressed, produces a reconstruction rather than the actual reason.

**Generality.** The statement covers cases that were not individually enumerated. It has
a domain wider than the instance that produced it. A rule with a domain of one is not a
rule; it is a fact wearing a rule's clothing.

**Stability.** The statement stays true long enough to be worth encoding and maintaining.
A rule that expires faster than it can be written, tested and deployed is not an asset;
it is a liability that looks like one.

### The three ways it fails

**Failing articulability** is the classic case and the rarest in data work. It is real
— the smell test, the judgement of significance, the sense that a finding matters — but
it is not what makes building a warehouse slow.

**Failing generality is the dominant case, and it is the one that matters here.** Take
the sentence *KLANTNR in the billing system denotes the legal entity, not the contact,
and has done since the 2019 migration.* That sentence is perfectly articulable. Any
analyst who knows it can say it in ten seconds, write it down, and be understood. What
cannot be stated is a **general rule that would produce that fact** — for this column, in
this company, on this date — and there is no such rule, because the fact was manufactured
by a history of mergers, system replacements and individual decisions that has no form.

There are millions of such sentences in a corporate landscape. Each is true locally,
cheap to say, and impossible to derive. Collectively they *are* the semantics of the
data estate, and no methodology has ever been able to absorb them, because methodology
traffics in generality and these facts have none.

This is worth being precise about, because it is easily mistaken for tacit knowledge and
it is not tacit at all. Nobody is failing to articulate anything. The knowledge is
**articulable but not generalisable**, and that distinction determines which remedies can
possibly work.

**Failing stability** is the quiet one. The source team revises its code list every
quarter and tells nobody; the definition of an active customer moves when the commercial
policy moves. Statable today, false in March. Encoding such a fact as a rule produces
something that executes confidently and is wrong, which is worse than not having encoded
it — and it is the same decay that afflicts every metadata catalogue anyone has ever
built.

### Why this locates the third component exactly

The deterministic migration needs **all three** conditions. A rule that is articulable
but particular cannot be written; a rule that is general but unstable should not be.

**The third component needs only the first.**

It does not need generality, because it re-derives the answer for each instance at a
marginal cost approaching zero — so a fact with a domain of one is no longer useless,
merely cheap. And it does not need stability, because it can re-derive on a cadence
rather than encode once; a fact that expires quarterly is simply a fact that is checked
quarterly.

That is the whole claim of this document in one sentence: **the third component operates
on knowledge that is articulable but neither general nor stable — which is precisely the
material the deterministic migration had to leave behind.**

It also draws the boundary of what the third component can never reach. Knowledge that
fails *articulability* remains human, permanently, and not as a matter of current model
capability. Where a person can say it, the machine can hypothesise it and ask. Where
nobody can say it, there is nothing to hypothesise and nothing to ask for. That residue
is small, and it is what section VII's argument about the human contribution ultimately
rests on.

### Statability is a gradient, and the gradient is economic

None of these conditions is binary. A rule that would take six months of interviews to
state is not statable in any sense that matters, and the history of this discipline is
better described as a cost curve than as a boundary: the migration absorbed whatever was
cheap enough to state, in the order of its cheapness, and stopped where the cost of
stating exceeded the value of executing.

Read that way, **the third component does not move the logical boundary at all. It moves
the price.** Which is why the argument here is ultimately empirical and has a number
attached to it — see `CON-OP-2`.

Note also that statability is necessary but not sufficient. A rule may be perfectly
statable and still not worth encoding, and the third component's ability to state things
cheaply is exactly what makes it capable of generating enormous quantities of
correct, useless machinery. That is why pruning is an architectural component here rather
than an operational afterthought.

### Prior art, stated honestly

The first condition is Michael Polanyi's: *we can know more than we can tell.*<sup>1</sup>
Its role as a limit on automation is David Autor's Polanyi's paradox — tasks resist
automation when the rules governing them are tacit, because what cannot be articulated
cannot be programmed.<sup>2</sup> The standard resolution offered since has been machine
learning from examples: infer the tacit rule from demonstrations rather than from
statements.

The claim being made here is different, and its distinctness is exactly what `CON-OP-4`
tests. Data work does not stall at condition one. It stalls at condition two — and
inferring a rule from examples cannot help, because **there is no general rule to
infer.** There is only a particular situation to be read and a proposition to be formed
about it. The capability that matters is therefore situated inference rather than pattern
learning, which is a different thing and has only recently existed.

<sup>1</sup> Michael Polanyi, *The Tacit Dimension* (Garden City, NY: Doubleday, 1966), 4.
<sup>2</sup> David H. Autor, "Polanyi's Paradox and the Shape of Employment Growth," NBER
Working Paper 20485 (Cambridge, MA: National Bureau of Economic Research, 2014).

## IV. The third component

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

## V. The re-partition

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

## VI. The bottleneck moves

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

## VII. What does not change

Three things, stated because the enthusiasm around the third component routinely denies
all of them.

**Meaning still lives in the organisation, not in the data.** The third component cannot
conjure semantics that were never recorded. It can hypothesise them far better and far
faster than anything before it, and then it must ask. This is a permanent property of the
problem, not a limitation of current models.

Section III makes the point sharper, and the sharper version is the more useful one:
because this knowledge fails *generality* rather than *articulability*, a person can
always state it once asked — which is exactly why adjudication is a viable mechanism and
why asking is not a fallback but the design. What cannot be reached at all is the
material that fails articulability, where there is nothing to hypothesise and nobody who
can confirm.

**Purpose still comes from people.** Nothing in the third component knows what a business
is trying to decide. An analytic system with no model of the decisions an organisation
actually makes will produce observations that are statistically true and practically
worthless, at scale, forever.

**Determinism remains the only trustworthy execution.** The third component's value is in
deciding *what* the machinery should do. It should never be the machinery.

## VIII. The honest counter

A manifesto that states only its good news is a sales document, and this project's whole
method is to state the condition under which it is wrong.

The claim in section V — that the human contribution concentrates rather than
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

## IX. What this project is

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

# nsdn — Handover 04: the canon was checked, an example was lost, and a second interaction failed on the first one's axis
## Written 2026-09-20 at the close of session 04, for a fresh session

> **STATUS: CURRENT.**

---

## First actions

1. `git log --oneline -8` — expect HEAD at the commit closing session 04, with the work at
   `9875537`, "Verify the canon instead of arguing about it".
2. `python tools/check_repo.py` — must pass before anything is changed. Expect 49 rows, all
   live.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority on
   what is open; this handover is orientation only, and where the two disagree the register
   wins.
4. Then, in this order: `CON-OP-8`, whose disposition is now complete enough to execute;
   [`../docs/30_research/notes/2026-09-20-canon-survey.md`](../docs/30_research/notes/2026-09-20-canon-survey.md),
   which is the session's substance; and
   [`../docs/30_research/notes/XREV_2026-09-20_canon-survey-interaction_sol.md`](../docs/30_research/notes/XREV_2026-09-20_canon-survey-interaction_sol.md),
   whose Q3 changes how the manifesto may argue.

## Outstanding actions for the author, not the model

**The repository has still never been pushed.** Unchanged through four handovers. `origin`
is configured to `https://github.com/henryjvanderlinden-cloud/business-intelligence.git`, the
repository does not exist on GitHub, and these sessions hold no credentials. The author
creates the empty repository — no README, no .gitignore, no licence — and runs
`git push -u origin main` from `C:\Git\business-intelligence`.

**`CON-OP-15` is the author's to rule.** Unchanged. A model can sharpen it and has, four
times; ratifying it is not a model's job.

**`EVI-OP-6` asks for a licence, not just a decision.** It is the first row that requires
running something rather than reading or arguing, which is Mode 2 work under
[ADR-0006](../docs/20_decisions/0006-project-mode.md). It is small — a synthetic schema and
a fixed query set — but it is a phase exception and the author should say whether it may run.

## Where the project stands

Eight ADRs settled. Forty-nine register rows live, up from forty-seven. **Session 04 broke
the pattern the last three handovers recorded: it verified rather than wrote.** Seven claims
were checked against sources, and four of them moved.

**The first half of `ARC-OP-14` is discharged.** Anchor's schema-evolution property holds.
SQL:2011 supplies valid and transaction time and is silent on versioning derivation logic, so
the author's third axis is outside the standard rather than merely underused — a stronger
position than §190 claimed for it.

**§190 §3 lost one of its three headline examples.** Kimball gives two reasons, not one, and
argues that normalised ER modelling is *unsuitable* for decision support rather than
correct-but-expensive. He is not an instance of the rejected-on-cost pattern, and the
sentence is struck in place.

**The runtime relief the whole programme rests on is conditional.** Snowflake eliminates a
join only where key constraints are declared and carry `RELY`; BigQuery wants them
`NOT ENFORCED`; neither enforces them, and both warn that violated constraints can return
wrong results. That is `ARC-OP-22`, and its consequence is that a business-key assertion is a
runtime-correctness dependency rather than only a semantic claim.

**The Data Vault assumption came back adverse.** `ARC-OP-14` was promoted partly to settle
whether Data Vault's burden is the kind machine authorship absorbs. It is not, or not in the
way the mission assumed: the method presupposes generation, mature metadata-driven generators
supply it today with no model in the pipeline, and what they need as input is the model
metadata — hub, business key, link — which is the **second** thesis's output.
[002_mission-statement.md](../docs/00_concept/002_mission-statement.md) is annotated and
deliberately not reworded.

**The classification produced the finding nobody asked for.** The eight candidates in §3 are
three designs, two emitted artifacts and three declaration disciplines. Explicit units is
bound by semantic determination and maximum-granularity assertions by adjudication volume;
neither is a design cheap authorship re-opens, and counting them as evidence for the first
thesis counts its dependencies as its support.

**A second interaction candidate was drafted and refuted within the hour**, on the same axis
as the first: the dependency attaches to decomposition, which a conventionally authored 6NF
warehouse shares. The second objection is the one to carry forward — most keys decomposition
generates are mechanical or surrogate, not hypotheses about business identity.

## Task for the next session, in one sentence

Rewrite [`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III as
two declared theses per `CON-OP-8`, against `CON-OP-5`, `CON-OP-6`, `CON-OP-7`, `CON-OP-11`
and `CON-OP-4`, carrying the canon survey's F1–F4 and stating the absence of a demonstrated
interaction, and settling `CON-OP-10`'s naming and executing `CON-OP-9`'s rename in the same
pass.

## Why that task and not another

Three handovers have named it, and it is now the task with the fewest missing inputs rather
than the most. The disposition is ruled, the interaction question has a determinate answer —
absent, two candidates refuted on the same axis — and the survey supplies what the rewrite
needs in order not to overclaim. `CON-OP-10` blocks every document that needs the second
faculty's name, and it is cheap.

The rewrite is also now *allowed to be honest in a way it previously was not*, which is the
XREV's Q3 and the single most useful line to carry into it: a demonstrated **adverse**
coupling is stronger evidence that the theses describe one system, not weaker. The repository
has been conflating the strength of the object with the attractiveness of the conclusion.

**`CON-OP-2` remains the cheapest decisive thing in the register and is now five handovers
deferred.** It needs published token prices and an afternoon. If the rewrite stalls on
`CON-OP-10`, do that instead of drafting around the block.

## Traps and warnings

**The single-axis error was committed again, by the session that was warned about it in
writing.** F5 counted table count where the quantity that matters is the number of
independently uncertain identities. Handover 03 named this pattern; naming it did not
prevent it. The mechanical form of the check is better than the warning: for any quantity a
claim says scales, ask what *else* would have to scale with it, and whether the two are the
same quantity under a different name.

**Two interaction candidates have now failed the same way.** Both connected the second thesis
to a property conventional warehouses already have — materialisation, then decomposition. A
third should not be drafted without first stating, in one sentence, how it attaches to *cheap
machine authorship* specifically. If that sentence cannot be written, there is no candidate.

**A verified finding is not a verified argument.** The survey checked seven claims and the
pass reviewed one finding out of five. F1 through F4 are unreviewed by construction and
include the two that matter most — the heterogeneity of §3's list, and the adverse Data Vault
comparison. Do not treat them as settled because they were sourced.

**Vendor documentation says when an optimisation is permitted, not that performance depends
on it.** The survey elided that and Q2 caught it. The same error is available wherever this
repository reasons from a capability's existence to its necessity.

**The falsifiable core is unreviewed after five passes.** Unchanged from Handover 03, and now
a five-session pattern rather than a four-session one: that business keys are machine-proposable
at adjudication-worthy precision has never been the object of a pass. `EVI-OP-1` and
[510_external-review.md](../docs/50_process/510_external-review.md)'s standing list both name
it first.

**Deletion is now permitted in the working folder for the session that holds it, and was not
in earlier ones.** The stale `.git/index.lock` trap from Handover 03 fired again on the first
commit attempt. If git reports `Unable to create index.lock`, remove it and retry; a fresh
session may have to request the permission again.

**Do not reword the mission statement to absorb F4.** It was annotated instead, on purpose.
Four of six versions were refused, protections have twice been lost to rewrites for cadence,
and the statement's practical test survives the finding intact — it is the *argument* that
reaches the test through cheap authorship alone that does not.

## Do not reopen

- Models never operate in the data path — [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md).
- Autonomy is tiered — [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).
  *(`ARC-OP-19` asks whether the enumeration is complete; `ARC-OP-22` asks whether a declared
  key constraint is a tier-appropriate artifact. Both extend the tiering; neither reopens it.)*
- Argument, then proof of concept on public data, then offering — [ADR-0006](../docs/20_decisions/0006-project-mode.md).
  *(`EVI-OP-6` asks for a scoped exception, not a phase change.)*
- `nsdn` as the handle, the biological metaphor kept private — [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md).
- The register, handover and enforcement apparatus — [ADR-0007](../docs/20_decisions/0007-register-and-handover-apparatus.md).
- Data is the substrate; the three are faculties; each has a mandate; a faculty is never named
  after its implementation — [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md).
  *(The second faculty's own name is `CON-OP-10` and is open. The collective noun is not.)*
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).
- **The amortisation-threshold synthesis.** `CON-OP-11` failed. The 6NF counterexample that
  refuted it survives; its wording — *almost unused* — does not, and should not be requoted.
- **The auditability interaction**, and now **the key-constraint interaction**. Both tried,
  both refuted, both recorded against `CON-OP-8`.
- **The obstacle taxonomy.** Authoring versus runtime versus comprehensibility is not a
  classification of obstacle kinds; it is where lifecycle work lands. §190 §4 is annotated
  accordingly.
- **Kimball as a cost-side rejection.** Checked against the 1997 manifesto and struck. If the
  claim returns, it needs a different source, not a rewording.

## What session 04 did not do

Did not execute the §III rewrite, for the fourth handover running. Did not read Date, Darwen
and Lorentzos, so 6NF's definition remains second-hand, nor Linstedt and Olschimke, so the
Data Vault finding rests on practitioner testimony and vendor material. Did not price
anything: `CON-OP-2` is untouched and now five handovers old. Did not attempt `ARC-OP-14`'s
second half, because F1 changed which designs are eligible for it. Did not review F1–F4. Did
not push.

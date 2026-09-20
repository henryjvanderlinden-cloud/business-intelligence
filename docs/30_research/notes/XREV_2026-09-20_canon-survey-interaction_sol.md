# XREV 2026-09-20 — the canon survey's interaction candidate (F5) — sol

```yaml
object:        docs/30_research/notes/2026-09-20-canon-survey.md, finding F5, uncommitted.
               At commit 81cba08.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0, cwd
               C:\Git\business-intelligence, sandbox read-only, thread
               01a0c07a-60a0-7643-b2d2-c09689d216a2
assignment:    three determinate questions, adversarial framing, general assessment
               explicitly forbidden, 400 words total, reading explicitly forbidden — the
               apparatus was stated inline per the transport lesson of the third pass.
               Out of scope: the survey's verification verdicts, the two theses
               themselves, the project's merit.
second reader: assignment set by Claude Opus 5, which drafted F5 in the same session and
               named in Q1 the attack it expected to be fatal. That steers the finding and
               is unreviewed by construction. Q3 was included precisely because it could
               not be steered that way: it asks whether the repository's own standing
               framing is wrong, and the answer came back against the framing.
verdict:       FAILS on Q1 with a counterexample; the premise in Q2 FAILS as a general
               claim; and Q3 returns a correction to `CON-OP-8`'s own reasoning.
```

Fourth external pass; further partly discharges `PRC-OP-1`. The falsifiable core remains
unreviewed after five passes.

## Q1 — does F5 fail the way the previous interaction candidate failed?

**Yes, and on the same axis.** The reviewer's counterexample: *a conventionally authored 6NF
warehouse uses many narrow tables and relies on declared, non-enforced keys for join
elimination. It incurs exactly the alleged adjudication demand without T1.* The dependency
attaches to decomposition, not to cheap machine authorship — which is verbatim the failure
mode of the auditability candidate refuted earlier the same day.

A second objection lands independently and is the more interesting of the two: **many
PK/FK constraints are mechanical consequences of decomposition or use surrogate
identifiers; they are not T2-style hypotheses about business identity.** Splitting one
entity into forty attribute tables generates thirty-nine keys that restate a decision
already made, not thirty-nine new claims about the world. F5 counted them as though they
were.

The minimal premise that would rescue (d), quoted:

> the marginal decompositions made economical specifically by machine authorship require
> previously unknown business-key or cross-source identity assertions, and acceptable
> performance requires optimisations that depend on declaring those assertions.

With a rider: it must also be shown that adjudication grows with **independently uncertain
identities**, not with table count, since many tables can reuse one already-adjudicated key.
That rider is the sharper half. It says the quantity that scales is not decomposition but
the number of distinct identity questions, and those are not the same quantity.

## Q2 — is join elimination a general condition of decomposed-design performance?

**No.** The reviewer names the alternatives: columnar storage, partition and micro-partition
pruning, clustering, predicate and projection pushdown, join ordering, broadcast and hash
joins, caching, materialised views, prejoined serving layers, and workloads that touch only
a few narrow relations at modest volume.

What would have to be true for the survey's (b) to hold: the workload must frequently
reconstruct wide entities through otherwise redundant joins; those joins must materially
violate the latency or cost target; alternative physical optimisations or materialisations
must be unavailable or insufficient; and constraint-dependent elimination must actually
remove the bottleneck. The vendor documentation establishes **when that optimisation is
permitted, not that performance generally depends on it** — which is the distinction the
survey elided, and it is the single-axis error the handovers keep recording.

## Q3 — is an adverse coupling a weaker object than two unconnected theses?

The repository's standing position, recorded in `CON-OP-8`, is that two adjacent capability
claims with no demonstrated interaction are a weaker object than one thesis; the survey
inherited it and added that an adverse coupling "is not mutual support" and must not be
written as though it were. The reviewer answers against that framing:

> A demonstrated adverse coupling is stronger evidence that the theses describe one system.
> It supplies a causal relationship … That may make the combined system less feasible or
> reduce T1's claimed economic benefit, but it is analytically stronger than merely placing
> two independent theses beside each other. "Adverse" concerns the interaction's
> consequences; it does not make the evidence of interaction weaker.

The distinction is between the strength of the *object* and the attractiveness of the
*conclusion*, and this repository has been running them together. An interaction that raises
the cost of the combined system is still an interaction, and demonstrating one would
discharge what `CON-OP-8` asks for even while making the project's own economics worse.

That is a finding about how the manifesto should be written, not merely about F5: **the §III
rewrite is not obliged to find a favourable interaction, and should stop treating the
absence of a favourable one as the absence of one.**

## What this pass did not review

The survey's seven verification verdicts, which were out of scope and remain checked only
against the sources cited in them. The two theses themselves. Whether the minimal premise in
Q1 is *true* — the reviewer stated what would rescue F5, not that it obtains.

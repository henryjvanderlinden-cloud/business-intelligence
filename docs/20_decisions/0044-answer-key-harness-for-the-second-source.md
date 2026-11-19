# ADR-0044 — The second source's answer key is held outside the proposing model's reach, generated and scored by the sandbox job, with a held-back part and thresholds fixed before the first score

- **Status:** Accepted
- **Date:** 2026-11-19
- **Supersedes:** —
- **Superseded by:** —

## Context

[ADR-0043](0043-second-source-a-crm-derived-from-wwi.md) chose the second, messy source: a customer system derived from
Wide World Importers, generated and scored by sol so that the model proposing matches neither designs the differences
nor sees the key. It left open what the generator produces, how the key is held and scored, and what precision counts
as useful (handover 14, scope items 1 and 2; `EVI-OP-1`).

On 2026-11-17 the model put nine points to the author: customers only, with the content listed in
[430](../40_roadmap/430_second-source-and-answer-key.md) §2; the kinds of difference chosen by sol and kept from the
proposing model, since knowing them would let it tune to them, which is also why the generator's code is hidden; a
hidden folder `C:\nsdn-holdout\` outside the repository, where sol works and the proposing model never looks; the
generator run by the Windows job after each export, copied in by `setup.ps1` from the hidden folder (route a), rather
than run by sol after each day (route b), which would have had Codex writing against the author's ruling of 2026-10-07;
scoring by figures only, never per customer; cheap signals and the model reported apart, as
[410](../40_roadmap/410_first-vertical-slice.md) requires; a held-back part of about 30% scored once, at the end; three
thresholds fixed before any score; and a separation of what is general from what belongs to WWI. The author ruled on
2026-11-19 at 09:06, verbatim:

> Sounds great and thorough, please go ahead.

## Options considered

*Route b, sol runs the generator after each simulated day.* Its case: no change to the job and no rerun of setup. Against
it: Codex would write files every day, against the 2026-10-07 ruling, and the daily source would depend on a model call.
*Route a, the job runs it.* Adopted.

*Per-customer feedback from the scorer.* Its case: faster improvement of a method. Rejected: it hands the key over one
customer at a time.

*No held-back part.* Its case: every customer counts in the figure. Rejected: development against the whole key makes
the final figure a fit, not a measurement (410: freeze the sample and hold part back).

*Thresholds set after the first scores.* Rejected: a threshold chosen with the results in view measures nothing.

## Decision

1. **The source and its generator are as [430](../40_roadmap/430_second-source-and-answer-key.md) §2 describes**, the
   kinds of difference chosen by sol and kept from the proposing model.
2. **The hidden folder** `C:\nsdn-holdout\` holds the generator, the kinds of difference, the seed, the key, the split,
   the scorer and the scoring log (430 §3). sol writes there and only there, a narrow exception to the ruling of
   2026-10-07 that Codex's sandbox stays read-only.
3. **The job generates the source after each export, and scores on request** through a new action `score`, both from
   copies `setup.ps1` installs in the job's pinned folder (430 §4 and §5). The author reruns setup once.
4. **The scorer returns figures only**, for cheap signals and for the model apart, on the development part during
   development and on the held-back part once (430 §5).
   *Made precise 2026-11-19 after review, in 430 §5, and put to the author: the measurement uses an experiment frozen
   once, not the daily data; the split is drawn over identity groups and the development list is published without
   counterparts; at most five development runs per method; one scoring contract; both methods' held-back results
   released together, once.*
5. **The thresholds are fixed now** (430 §6): automatic merges at least 0.98 precise; the queue worth reading at 0.60;
   the model at least 0.05 more recall than cheap signals at the automatic tier's precision.
   *Made precise 2026-11-19 after review, in 430 §6, and put to the author: each method's automatic-merge cutoff is
   fixed on the development part and locked; the comparison is of recall at those cutoffs with both methods at least
   0.98 precise; a method with no links in a tier does not meet that tier's threshold.*
6. **The proposing model keeps to the conduct of 430 §7**; a breach voids the test and is recorded.

## Consequences

The general part (hidden key, scoring rules, thresholds, conduct) can be carried to a client case unchanged; the
generator cannot. The job gains its first action that runs code not written in this repository, installed only by the
author's own rerun of setup from a folder he controls. A breach of the conduct rules is detectable only through the step
log and the scorer's log; the arrangement is a discipline as much as a boundary.

**Revisit** if the planted differences prove too easy or too hard to tell anything, if the key is seen by the proposing
model, or when the published benchmark (ADR-0043, option B) is taken up.

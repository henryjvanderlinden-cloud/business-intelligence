# XREV 2026-11-21 — the hidden folder's generator, freeze and scorer — Astra

```yaml
object:        C:\nsdn-holdout\code (generate_crm.py, common.py, freeze.py, score.py), its tests and KINDS.md, as built by
               sol on 2026-11-21, against note 430 sections 2, 4, 5 and 6 and ADR-0044. Not readable by the proposing
               model; read by the reviewer in place.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, working directory
               C:\nsdn-holdout, instructed to change nothing; answer written to the repository's ignored scratch/ folder.
assignment:    assume the implementation is wrong and show it, as an evaluation methodologist who has run
               entity-resolution benchmarks with hidden ground truth: leakage through published files, outputs or
               errors; the figures and thresholds against 430; the held-back release and the identity-group split;
               whether the difficulty can discriminate; whether the tests catch what they claim. Up to five findings,
               never naming a kind of difference, the seed or counts per kind.
second reader: assignment set by Claude Opus 5.5 in session 14, which has not seen the code. The code was written by
               sol; Astra reviewed it so that neither the builder nor the proposing model grades it.
verdict:       FAILS [private-path confinement, split validation and exact cutoff reporting require correction; the
               difficulty is too easy]. Disposition: all five sent to sol to fix in the hidden folder.
```

## Astra's answer, verbatim

1. **FAILS — Q1: private output paths are not confined.** `freeze.freeze()` accepts an arbitrary `holdout` and does not resolve or reject junctions in its private destination; `score.score()` inherits that destination for its history and release record. Concrete counterexample: with the normal hidden root, an `experiments` junction targeting a repository scratch directory causes freeze to copy `key.json` and `split.json` outside the hidden folder. The later inventory check examines descendants, not the junction through which the root was reached. This is a filesystem configuration counterexample, not a claim that such a junction currently exists. Minimal fix: validate the resolved private root and every private destination against the permitted hidden tree, reject junction/symlink traversal before creating or copying anything, and apply the same policy to scoring state. Publishing `development_records.csv` itself is expressly authorized by 430 §5.2; its disclosure of membership is not a defect.

2. **FAILS — Q3: freeze accepts a split that exposes held-back identities during development.** `freeze.freeze()` checks only that the flattened membership has the same record keys as the answer key. It does not check exclusive membership or the transitive identity closure required by 430 §5.2. The concrete counterexample already exists in `ScoreTests.setUp()`: its synthetic key connects development and held-back records through a shared source identity, yet freeze accepts the fixture and development scoring proceeds. A record placed in both partitions would also pass the set comparison and be scored in both. Minimal fix: derive the connected components from the private acceptable sets, include source-only identities as required, and reject any split that duplicates records or separates a component. The generator's intended grouping does not substitute for checking this invariant at freeze. The normal release path does record consumption before computing figures, replay a completed identical request, and reject a changed request; the failure here is the prerequisite separation of identities.

3. **FAILS — Q2: the reported cutoff is not necessarily the locked cutoff.** `choose_cutoff()` and the scoring log preserve `Decimal` precision, but `figures()` converts the cutoff to a binary float for JSON. An in-memory synthetic probe with confidence `0.90000000000000001` returns cutoff `0.9`. Submitting that returned value for held-back scoring fails `CUTOFF_MISMATCH`, even though the caller followed the published result. This also makes the reported boundary inaccurate. Minimal fix: return an exact decimal string and accept that same representation on release, or define and enforce a fixed confidence precision before selecting cutoffs. The cross-source and duplicate formulas, tier denominators, top-50 ordering, undefined values, cutoff selection arithmetic and three verdict rules otherwise follow §§5.3 and 6 on inspection; this finding concerns their cutoff interface, not an invented alternative scoring rule.

4. **FAILS — Q5: the tests leave their central separation and boundary claims untested.** `test_freeze_and_readiness()` accepts the invalid identity split described above and checks the published membership list against that same fixture. `test_identifier_and_order_independence()` tests renumbering and ordering, but cannot establish output-path confinement. `test_cutoff_lock()` uses a short decimal and never round-trips the returned cutoff. These are concrete cases where the present tests accept or miss the preceding failures. `test_stability()` also examines only the intersection of account numbers: changing some persistent accounts' numbers can escape its equality assertions while the intersection remains large enough. Minimal fix: independently assert component separation and unique partition membership; add redirected-destination rejection and exact-cutoff round-trip cases; compare persistent identities across days rather than only surviving account numbers. The suites were read, not executed, because their setup writes additional files; the numerical counterexample was checked without filesystem writes.

5. **FAILS — Q4: difficulty is too easy.** The needed class of change is independently calibrated challenge construction, with difficulty validated against a fixed inexpensive baseline before the experiment is frozen.

VERDICT: FAILS — private-path confinement, split validation and exact cutoff reporting require correction.

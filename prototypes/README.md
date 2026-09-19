# Prototypes

Throwaway code, each piece answering exactly one question, each in its own directory
with a `README.md` stating the question and, when finished, the answer.

Prototypes are not maintained, not tested, and not imported by anything. A prototype
whose answer matters graduates: it is rewritten under `src/`, with tests, referenced by
an ADR. The original stays here as the record of how the answer was obtained.

Candidates, drawn from [`../docs/40_roadmap/410_first-vertical-slice.md`](../docs/40_roadmap/410_first-vertical-slice.md):

- How much joinability evidence do MinHash sketches yield across two schemas, at what
  cost, without moving data?
- How much key evidence is recoverable from query logs via sqlglot, compared with
  profiling alone?
- Does a language model's key-hypothesis precision exceed that of the structural signals
  it is given, or is it mostly re-ranking them?
- What does a card actually look like, and does an agent navigate a hundred of them
  within the three-load retrieval contract?

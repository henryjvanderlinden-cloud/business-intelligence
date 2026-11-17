# ADR-0041 — The repository is dedicated to the public domain under CC0 1.0; third-party material keeps its own licence and is named in the README

- **Status:** Accepted
- **Date:** 2026-11-17
- **Supersedes:** —
- **Superseded by:** —

## Context

The author made this repository public on GitHub before 2026-11-17. It had no licence file. On 2026-11-17 at 13:32 he
wrote, verbatim:

> i want to apply a certain license to everything in the business-intelligence repository, so that it can be used by
> me (and potentially others) in other projects too. I've made the repo public.

He brought a note written in another conversation on 2026-11-17, whose first lesson proposes the licence. Its
reasoning, which the note itself calls a reasoned proposal and not legal advice, is the source of the legal statements
in this paragraph. Without a licence the author grants no general permission to reuse: others may read the repository
and use its ideas, which are not protected, but may not copy, adapt or distribute its text and code without permission,
outside the statutory exceptions; that holds for a client applying the method too. CC0 1.0 waives copyright and
neighbouring rights as far as the law allows, and where a waiver is not possible (in the Netherlands the moral rights
remain, for example) it falls back to an unconditional licence. It says nothing of patents or trademarks, and it cannot
cover what others made.

The aim is the author's: the knowledge should be free to use, a mention is welcome but not required, and a client that
adopts the method and must later carry on without him needs certainty that it may. The main goal of the project is
generally applicable knowledge, Wide World Importers only an example (his words, 2026-11-06).

Before applying it, the model looked for material in the repository that is not the author's. It found the Wide World
Importers sample database (MIT, Microsoft's `license.txt` read on 2026-11-17), 14 evidence files quoting a Microsoft
Learn page (CC BY 4.0, per the `LICENSE` of `MicrosoftDocs/sql-docs`, read the same day), one quoting Microsoft's
simulation procedures, and two holding ISO 3166 code lists read from Wikipedia (CC BY-SA 4.0). The open data sources
of `records/sources.jsonl` are described in the repository but none of their data is tracked: `data/` is ignored.

The model proposed four points: CC0 for the whole repository; the official text in a `LICENSE` file; the note's README
paragraph with a section naming third-party material, the Microsoft Learn excerpts named rather than rewritten; and this
ADR with a check. The author ruled on 2026-11-17 at 13:53, verbatim: "1 - 4 agree".

## Options considered

*No licence*, the state until now. Its case: nothing is given away, and the author keeps every option. Against it:
it defeats the stated aim, since it gives no one, the author's own clients included, a general permission to copy the
material; copying would rest on a statutory exception or on permission he grants case by case.

*MIT or CC BY 4.0.* Their case: both are widely understood, and both secure credit for the author, which has
reputational value for a one-person company. Rejected because both make attribution a condition, and the author wants
it appreciated, never required.

*MIT No Attribution (MIT-0).* Its case: no attribution, and the wording software users know. Rejected because it is
written for software, and this repository is mostly prose; CC0 is written for any work.

*CC0 for the prose and MIT-0 for the code.* Its case: each licence used for what it was written for. Rejected: prose,
declarations, generated SQL and code interleave here, and a boundary between two regimes would itself need upkeep.

*CC0 1.0 for everything the author made.* Adopted.

*Third-party excerpts rewritten as paraphrases*, so that nothing in the repository carries a condition. Its case: no
exceptions to explain. Rejected for now: the excerpts are evidence for claims, their exact wording is the point, and
naming them costs one section.

## Decision

1. **Everything the author made in this repository is dedicated to the public domain under CC0 1.0 Universal**: text,
   code, declarations, generated SQL, records and findings. The official text stands unchanged in
   [`LICENSE`](../../LICENSE), taken from GitHub's licence template and identical, apart from line wrapping, to the
   SPDX list's copy.
2. **A mention is appreciated, never required.** The README says so in its License section.
3. **Third-party material keeps its own licence** and is named in the README's
   [Third-party material](../../README.md#third-party-material) section, with the notices its licences ask to be kept
   with copies in [`THIRD-PARTY-NOTICES.md`](../../THIRD-PARTY-NOTICES.md). Whoever adds third-party material names
   it there in the same commit. What the author writes about such material is his and falls under CC0.
4. **Contributions are accepted under the same dedication.** Whoever contributes agrees that the contribution is
   dedicated under CC0 1.0 as well.
5. **The checker enforces** that `LICENSE` holds the CC0 1.0 text, that the README has its License and Third-party
   material sections, and that every host cited by an evidence file of kind `web source` is named in
   `THIRD-PARTY-NOTICES.md`. That every other piece of third-party material is named is not enforced (AGENTS rule 11).

## Consequences

Anyone, a client of the author included, may copy, adapt and build on the repository without asking. That is what the
second lesson of the same note relies on, decided on its own in [ADR-0042](0042-reading-at-a-distance.md). The dedication cannot be
withdrawn from what has been published under it; later material could be licensed differently, but what was taken
stays free. Credit can no longer be enforced. CC0 gives no rights to the names Microsoft, SQL Server or Wide World
Importers, nor to any patent.

The correction of `SRC-018` in `records/sources.jsonl` follows from reading Microsoft's `license.txt`: the licence was
recorded as "not yet read".

**Revisit** if third-party material is found whose licence forbids redistribution, if a contribution arrives whose
author cannot dedicate it, or if the author wants new material under a different licence.

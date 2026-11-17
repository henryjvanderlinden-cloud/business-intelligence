# ADR-0035 — nsdn keeps Wide World Importers as its reference case; each client gets a repository of its own with a tagged release of nsdn

- **Status:** Accepted
- **Date:** 2026-10-29
- **Supersedes:** —
- **Superseded by:** —
- **Amended by:** [ADR-0042](0042-reading-at-a-distance.md) (point 3: a fixed release, or a recorded reading point)

## Context

On 2026-10-29 the author asked whether the analysis, the declarations and the viewer can be reused at a client, whose
database he described as spaghetti: PostgreSQL, about 100 tables, foreign keys probably declared, a large-ish
production database and two further sources delivering daily extracts; whether its metadata may leave the client's
premises is open, and the client has Claude subscriptions of its own. He proposed, verbatim, "splitting this repository
were working on, because we now have three parts, which is anything related to the process, the use cases (wwi and the
dutch companies) and the website is also in here", and "pulling the nsdn repository at the client site and set up a
separate repository their for their data environment".

The model counted what a three-way split would cut: 56 relative links from the general documents into the WWI
material, mostly to the claims they cite as evidence, and 70 the other way, all enforced by the checker, and WWI's
ADRs (0028 to 0031, 0033, part of 0034) inside the one sequence that is never renumbered. The company material, logo
work, sits in the ignored `scratch/` folder, and no website file is tracked. It proposed instead (option B): keep WWI in
the nsdn repository as its reference case, move the company material out, and give each client a repository of its own
that holds a fixed release of nsdn. The author replied on 2026-10-29 at 16:07, verbatim:

> Okay, there is something to be said for including the WWI set as a reference case. It's open, and provides a lot of
> practical examples. So option B. I think we should indeed pull a tagged release into a client repository. If the
> repository is improved, what do you suggest we do? Occasionally have a summary written and read that back into the
> main repository? And sometimes the other way back, if there are improvements in my main repository? Not sure what you
> want to do with the Postgress pass, but sounds plausible, so please go ahead.

## Options considered

*Option A, three repositories* (process, use cases, website). Its case: each repository holds one concern, and the
process repository carries no practice data. Against it, here: the link and ADR surgery above, for material that is
public practice data and is what the general documents cite as their evidence.

*Option B.* Adopted.

*A client working inside the nsdn repository.* Rejected without discussion: this repository is synced to the author's
GitHub account, and client material must not enter it.

## Decision

1. **The nsdn repository keeps Wide World Importers as its reference case**: the worked example the method is shown on,
   and the regression case of generic tooling, which must reproduce what the record holds. The parked PAR/OSM sandbox
   stays as a closed example.
2. **Company material (VDL-DIAA's logo and website) does not belong in the nsdn repository** and moves to a place of its
   own; none of it is tracked here now.
3. **Each client has a repository of its own** for its data environment: its analysis record, its declarations, its
   register, its decisions and its step log, with **a tagged release of nsdn** inside it, at a fixed version.
   *Amended 2026-11-17 by [ADR-0042](0042-reading-at-a-distance.md): or, when the client takes over the knowledge rather than running nsdn's tooling
   unchanged, no copy of nsdn at all but a recorded reading point.*
4. **The catalogue pass for PostgreSQL is built** as a prototype under `prototypes/catalogue_pass/`, with the viewer's
   raw-source mode, for that first client.

## Consequences

nsdn now needs releases: a tag, with release notes saying what changed, why and with what intended impact, the practice
the author described for regression testing. *Amended 2026-11-17 by [ADR-0042](0042-reading-at-a-distance.md): releases are
needed only for a client that holds a fixed release.* How improvements travel between the main repository and client
repositories is open, with a proposal, under `PRC-OP-9`; how the release sits inside a client repository (a git
submodule at a tag, or the release archive copied in) is part of it.

Generic tooling is tested on WWI before it reaches a client. Nothing from a client repository enters this one except
what `PRC-OP-9` lets through.

**Revisit** if the WWI material grows to dominate the repository, if a second reference case is added, or if a client's
terms forbid the release from referring to a public repository.

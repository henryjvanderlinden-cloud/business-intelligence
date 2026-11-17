# ADR-0042 — A client may use nsdn as a source to learn from: read at a distance at a recorded reading point, what it adopts made its own; a fixed release only when it runs nsdn's tooling unchanged

- **Status:** Accepted
- **Date:** 2026-11-17
- **Supersedes:** —
- **Superseded by:** —
- **Amends:** [ADR-0035](0035-reference-case-and-client-repositories.md) (point 3: a client repository holds a
  fixed release or a recorded reading point); [ADR-0036](0036-releases-and-upstream-notes.md) (points 1 and 2 apply
  only to a fixed release; point 3 lets one note hold several lessons, allows abstract examples and releases an
  accepted note only once a release exists; point 4 ties the first release to a client that chooses one; its
  Consequences' need for releases limited to that variant)

## Context

[ADR-0035](0035-reference-case-and-client-repositories.md) (point 3) and
[ADR-0036](0036-releases-and-upstream-notes.md) (points 1, 2 and 4) assume that a client repository holds a fixed
version of nsdn: a tagged release, as a git submodule or as a copied folder that is never edited, with improvements
coming back as upstream notes.

On 2026-11-17 the author brought a note written in another conversation, read against commit `c109545` of this
repository. Its second lesson describes a lighter way of using nsdn, which fits a client that wants to take over the
knowledge rather than run the tooling unchanged. The method is read online and not copied into the client's
repositories; the client records the commit it has read up to, a reading point; what it adopts becomes its own,
adapted to its situation, with its provenance recorded once; and lessons come back as notes. The note's reasoning: in
that situation nsdn is a source to learn from while the client builds up, not a dependency. A fixed version is needed
when a client runs nsdn's code unchanged, which is not the case there; and a copy the client adds to mixes the generic
with the specific, so that updating it and bringing lessons back grow steadily harder.

The note was itself written in this way. It names its reading point, carries no client material, and was checked by
two models against the client's list of terms before the author carried it over by hand. It depends on the first
lesson of the same note: under [ADR-0041](0041-cc0-public-domain-dedication.md) anyone may adopt and adapt the
repository without asking.

The model proposed adopting the lesson as two variants a client chooses between; marking ADR-0035 and ADR-0036
amended rather than "partly superseded", since amendment is the form this repository uses for a partial change
(ADR-0017, ADR-0018, ADR-0020); stating that the variant depends on this public repository staying reachable;
deferring a process document until a client uses the variant; and annotating `PRC-OP-9`. The author ruled on
2026-11-17 at 13:53, verbatim:

> 6 - 10 agree, as for 8, i intend for it to stay open and available.

Point 8 was the dependence on the public repository.

## Options considered

*Only a fixed release, as ruled in ADR-0036.* Its case: a client sees every line of what it installed, and every change
a new release makes in its record is attributed to a release note or treated as a regression. Against it, for a client
that learns rather than runs: a dependency it does not need, and releases cut before any client runs the tooling.

*A copy of nsdn that the client extends.* Its case: everything is local, nothing depends on a network or on this
repository. Against it: the generic and the specific mix, and both updating and bringing lessons back grow harder with
every change.

*A shared fork*, rejected in ADR-0036 because it would carry client material back by construction; nothing here
changes that.

*Both a fixed release and reading at a distance, the client choosing by how it uses nsdn.* Adopted.

## Decision

1. **A client chooses between two variants.** (a) **A fixed release** in its repository, as ADR-0036 points 1 and 2
   rule, when it runs nsdn's tooling unchanged. (b) **Reading at a distance**, when it takes over the knowledge and
   makes it its own.
2. **Under (b), nsdn is read and not taken in.** It is read online; no copy, fork, submodule or mirror of it goes into
   the client's repositories. The commit is the version: the client records a reading point, the commit of nsdn it has
   read up to. Before work that leans on the method it looks at what has changed since its reading point, and then
   moves the reading point on. No release is needed.
3. **Under (b), adopting is making it one's own.** What the client adopts, principles, way of working or code, becomes
   part of its own repositories, adapted to its own situation, and its provenance (the path and commit in nsdn) is
   recorded once. The aim is that the client's repositories stand on their own in time, without nsdn.
4. **Lessons come back as notes, in both variants** (ADR-0036 point 3): without client material, with examples on
   Wide World Importers or abstract. Under (b) a note is written now and then as a comparison at the level of concepts;
   a second model checks it for client terms, and the author carries only the checked version over by hand. One note
   may hold several lessons, provided each can be judged and refused on its own. A patch in a note is made against the
   release in use or against the reading point. An accepted note is applied here and tested on Wide World Importers;
   it reaches a release only once a client uses one (point 5).
5. **Releases become optional** (ADR-0036 point 4): the first is cut when a client chooses (a), not before.
6. **ADR-0035 and ADR-0036 stay Accepted, amended by this record**; ADR-0036 point 5, that the analysis at a client runs
   under the client's own Claude, is unchanged.
7. **A description of reading at a distance in `docs/50_process/` waits** until a client uses it; until then this
   record holds the rules.

## Consequences

Variant (b) relies on this repository staying public and reachable at the commits clients have recorded as reading
points. The author intends it to: "i intend for it to stay open and available" (2026-11-17).

Under (b) there are no release notes to attribute a change to; what a client adopted is carried by its own tests and
checks. The two checks ADR-0036 names, the release folder's checksum and upstream notes free of client terms, concern
variant (a) and the notes; the reading point and the provenance records of variant (b) live in the client's
repositories, where this repository's checker cannot reach them, so they are unenforced here (AGENTS rule 11). As
before, nothing from a client repository enters this one except through a note.

**Revisit** if this repository goes private or moves, if a client under (b) starts running nsdn's tooling unchanged
(then (a) applies), or if notes prove too costly to keep free of client material.

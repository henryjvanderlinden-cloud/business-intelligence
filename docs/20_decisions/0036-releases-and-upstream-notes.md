# ADR-0036 — nsdn travels to clients as numbered releases with release notes, and improvements come back as upstream notes without client material

- **Status:** Accepted
- **Date:** 2026-11-03
- **Supersedes:** —
- **Superseded by:** —

## Context

[ADR-0035](0035-reference-case-and-client-repositories.md) gave each client a repository of its own with a tagged
release of nsdn, and the author asked how improvements should travel between the main repository and a client
repository, in both directions. The model proposed three points under `PRC-OP-9` on 2026-10-29: numbered releases
with release notes going downstream; the release held in a client repository as a git submodule at the tag, or as the
release archive copied in, and never edited there; and, coming upstream, one note per proposed improvement instead of
periodic summaries, with no client names, metadata or data.

The author replied on 2026-11-03 at 19:21, verbatim:

> With regards to the open points:
>
> 8. okay, sounds good
> 9. not yet, too early
> 10. when the a branch of the repository is located on the clients side, I will use the clients' Claude instance to
> have the analysis performed.

Point 8 was the proposal of `PRC-OP-9`; point 9, whether to prepare a first release `v0.1` now; point 10, the
client's consent to its metadata leaving its premises and being read by a model.

## Options considered

*Periodic summaries read back into the main repository*, the author's first idea. Its case: little ceremony. Against
it: a summary bundles changes that must be judged one by one, cannot be refused in part, and invites client detail
into the main repository. *Upstream notes, one per improvement*: adopted.

*A shared fork that clients and the main repository both push to.* Rejected: it would carry client material back by
construction.

## Decision

1. **Downstream.** nsdn is released as numbered tags, each with release notes saying what changed, why and with what
   intended impact. A client repository moves to a new release in one commit of its own, after which its checker and
   the release's own tests run; a change the release makes in the client's record is attributed to a release note or
   treated as a regression.
2. **In the client repository.** The release is a git submodule at the tag where the client's network reaches the
   author's GitHub repository, and otherwise the release archive copied into a folder `nsdn/`, with its version and
   checksum recorded. The client repository never edits that folder.
3. **Upstream.** An improvement found at a client is written as an upstream note in the client repository: what to
   change in nsdn, why, the evidence, and, where it is code, a patch against the release in use. A note carries no
   client names, metadata or data; an example is restated on the Wide World Importers reference case. The author
   carries notes into the main repository, where each is applied or declined on its own, tested on WWI, and released.
4. **No release yet.** The first release is cut when a client repository is about to be set up, not now.
5. **At a client, the analysis runs under the client's own Claude.** When the client repository sits on the client's
   side, the analysis is performed with the client's Claude instance, so the client's metadata is read under the
   client's own arrangement with Anthropic. Whether other models (such as the cross-model review on sol) may read it is
   the client's to decide.

## Consequences

The checker could enforce two parts of this: that the release folder in a client repository matches its recorded
checksum, and that upstream notes name no client table or column. Neither check exists; both belong to the first
client repository, and until then the rules are unenforced (AGENTS rule 11).

Release notes are owed from the first release on. The step log of a client repository is the client's, so the
post-mortem dataset of `CON-OP-16` spans repositories from then on.

**Revisit** when the first client repository is set up, if a client forbids any reference to a public repository, or
if upstream notes prove too costly to keep free of client material.

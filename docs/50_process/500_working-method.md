# 500 — Working method

How this project is conducted, as distinct from what it proposes. Adapted from practices
developed expensively in the author's compendium repository and inherited here rather
than relearned.

## The division of labour

The author supplies intuitions, domain judgement, and the thing no model has:
twenty-six years of watching how data projects actually fail. The model supplies
structure, prior art, adversarial pressure, and the patience to write down what was
decided. Neither half is decorative.

The failure mode specific to this arrangement is that the model is fluent and the author
is busy, so the model's framing quietly becomes the project's framing. When the author's
instinct and the written argument disagree, **the instinct is data** — it is a
compressed report from twenty-six years of observation, and the correct response is to
find out what it is compressing, not to talk him out of it.

## Write the check, not the sentence

The compendium's hardest-won process rule, adopted here verbatim in substance:

> **A newly-written rule is unenforced until something mechanical enforces it.**

Four rules there failed at the hands of the very corpus that wrote them, each existing
only as prose in a register. The rule transfers, and transfers with a pleasing symmetry:
it is the same principle as
[ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md) at a different scale.
Judgement is compiled into something deterministic, and the deterministic thing is what
runs. A repository proposing that architecture and not obeying it would be making an
argument it does not believe.

`tools/check_repo.py` is the enforcement. A convention added to this repository without
a corresponding check is decoration, and should be marked as such or not added.

## The model-switch rule

Material drafted by a model is reviewed on a *different* model before it is treated as
settled. Material added by the model that set a review assignment is unreviewed by
construction and must be marked as such.

This applies to the contents of this repository in full, which is why `PRC-OP-1` is open:
everything here was drafted in one session by one model and has exactly one reader.

## Session shape

A session opens by reading [`../../handovers/CURRENT.md`](../../handovers/CURRENT.md),
the register, and the documents its task touches; it runs `python tools/check_repo.py`
before changing anything and again before committing; it closes by writing the next
handover and updating the register in the same commit as the work.

A session that ends without completing its task says so in the handover. A handover
reporting success it did not achieve is worse than none.

## Registers over memory

What is open lives in [`../../registers/OPEN_POINTS.md`](../../registers/OPEN_POINTS.md),
not in a conversation, not in a model's context, and not in the author's head. What was
decided lives in an ADR. Anything that lives only in a chat transcript is lost, and the
rate at which it is lost is not obvious from inside the conversation.

## Supersede, do not delete

Stated in [`../../AGENTS.md`](../../AGENTS.md) and refined by the compendium's practice:
superseded text is retained and must be introduced by a phrase containing the word
**superseded**, which opens the historical block. Nothing after it is a current claim.
The word is load-bearing and machine-read.

## Commit discipline

One coherent change per commit, with a message that says why. Register updates travel in
the same commit as the work they describe, so that the register cannot drift from the
repository it documents.

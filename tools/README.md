# `tools/` — mechanical checks

Written against the standing rule in
[`../docs/50_process/500_working-method.md`](../docs/50_process/500_working-method.md):

> **A newly-written rule is unenforced until something mechanical enforces it.
> Write the check, not the sentence.**

## The one command

```
python tools/check_repo.py
```

Run it before changing anything and again before committing. Nonzero exit on failure;
warnings do not fail the run.

## What it checks

| check | asks | exact? |
| --- | --- | --- |
| register state rule | does every row begin with exactly one valid state token, dated where the token requires it? | **yes** |
| identifier discipline | are ids well-formed, in a known scope, and unique? | **yes** |
| partial settlement | does any row's name claim a settlement its state does not have? | no — word-matching, and it can be silenced by saying `PARTLY` |
| ADR index | is every ADR indexed, and does every indexed ADR exist? | **yes** |
| handovers | is there exactly one current handover, and does `CURRENT.md` point at it? | **yes** |
| links | does every relative markdown link resolve? | **yes** |
| supersession | does a document with struck-through text say `superseded`? | no — a warning only |

Standard library only, by design: a check that needs installing is a check that stops
being run.

## What it deliberately does not check

Prose quality, argument soundness, and whether a register row is *true*. Those need a
reader, and per
[`../docs/50_process/510_external-review.md`](../docs/50_process/510_external-review.md)
they need a reader on a different model from the one that wrote the text.

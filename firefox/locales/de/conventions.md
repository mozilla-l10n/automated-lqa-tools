# de — conventions and review instructions

_Counted over the whole de tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 810, `curly-double` 69, `german-double` 14, `curly-single` 2 | **straight-double** |
| apostrophe | `typographic` 6, `straight` 120 | **straight** |
| ellipsis | `char` 465 | **char** |
| dash | `em` 16, `en` 87 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 12, `formal` 4235 | **formal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- The quote convention is unsettled: the tree mixes straight `"` with German `„…“`. Treat this as one open decision for the locale team, not as individual defects.

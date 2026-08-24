# en-GB — conventions and review instructions

_Counted over the whole en-GB tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 597, `curly-single` 101, `straight-double` 58 | **curly-double** |
| apostrophe | `typographic` 1121, `straight` 56 | **typographic** |
| ellipsis | `char` 461, `ascii` 1 | **char** |
| dash | `em` 108, `en` 4 | **em** |
| nbsp | `total` 5, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

## Instructions for the reviewer

- "web site" / "web sites" as two words is the house form where en-US writes
  "website" / "websites". It is deliberate; never flag it, and never suggest
  closing it up to match the source.
- "Backwards" and "Forwards" are the house forms where en-US writes "Back"
  and "Forward" — including in navigation labels and accessibility
  descriptions. Deliberate; never flag either, and do not report the two
  spellings coexisting in one file as an inconsistency.
- "Post Code" is the deliberate rendering of the en-US "Postal Code". Do not
  flag the spacing or capitalisation, and do not suggest "Postcode".

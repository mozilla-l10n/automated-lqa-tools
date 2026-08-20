# fr — conventions and review instructions

_Counted over the whole fr tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1132, `straight-double` 31, `curly-double` 2, `curly-single` 1 | **guillemet** |
| apostrophe | `typographic` 5633, `straight` 10 | **typographic** |
| ellipsis | `char` 472 | **char** |
| dash | `em` 68, `en` 8 | **em** |
| nbsp | `total` 4446, `before-punctuation` 1997 | _mixed_ |
| register | `formal` 3186 | **formal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- The no-break space before `? ! ; :` is U+00A0, not U+202F. Both are correct French; this locale has settled on U+00A0.
- Quotes are `« »` and the apostrophe is `’`.
- Language and region names are correctly localized.

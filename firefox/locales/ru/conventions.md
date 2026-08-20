# ru — conventions and review instructions

_Counted over the whole ru tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1174, `straight-double` 28, `curly-double` 8, `curly-single` 7 | **guillemet** |
| apostrophe | `typographic` 11, `straight` 16 | _mixed_ |
| ellipsis | `char` 463, `ascii` 6 | **char** |
| dash | `em` 168, `en` 5 | **em** |
| nbsp | `total` 5, `before-punctuation` 2, `space-before-punctuation` 7 | _mixed_ |
| register | `informal` 1051, `formal` 3592 | **formal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- Brand terms take a `$case` parameter; this is correct Russian declension and has no en-US equivalent.
- The `несколько ({ $n })` plural strategy and the extra `$count` interpolation are deliberate.
- Example passwords and search-keyword lists that look like defects are intentional.
- Access keys were kept from English rather than remapped — one systemic decision.

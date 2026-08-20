# es-MX — conventions and review instructions

_Counted over the whole es-MX tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 504, `straight-double` 158, `curly-single` 84, `guillemet` 1 | **curly-double** |
| apostrophe | `typographic` 96, `straight` 38 | _mixed_ |
| ellipsis | `char` 433, `ascii` 21 | **char** |
| dash | `em` 75, `en` 1 | **em** |
| nbsp | `total` 14, `narrow` 10, `before-punctuation` 10, `space-before-punctuation` 8 | _mixed_ |
| inverted marks | `open-question` 367, `open-exclamation` 84 | **open-question** |
| register | `informal` 1359, `formal` 237 | **informal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- Inverted `¿` and `¡` are used correctly throughout.
- Access keys were kept from English rather than remapped. This is one decision for the locale team, reported systemically.

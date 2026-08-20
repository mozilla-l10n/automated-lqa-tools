# es-ES — conventions and review instructions

_Counted over the whole es-ES tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 497, `straight-double` 150, `curly-single` 44, `guillemet` 1 | **curly-double** |
| apostrophe | `typographic` 59, `straight` 76 | _mixed_ |
| ellipsis | `char` 440 | **char** |
| dash | `em` 76, `en` 1 | **em** |
| nbsp | `total` 9, `before-punctuation` 3, `space-before-punctuation` 6 | _mixed_ |
| inverted marks | `open-question` 348, `open-exclamation` 79 | **open-question** |
| register | `informal` 3, `formal` 1367 | **formal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- Peninsular spelling: `vídeo`, not `video`.
- `¿` and `¡` are required at the start of questions and exclamations.
- The register skews to *usted* but is not consistent; treat normalization as one decision rather than per-string defects.

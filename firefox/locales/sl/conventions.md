# sl — conventions and review instructions

_Counted over the whole sl tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 303, `straight-double` 285, `curly-single` 54, `guillemet` 7 | _mixed_ |
| apostrophe | `typographic` 54, `straight` 52 | _mixed_ |
| ellipsis | `char` 420, `ascii` 40 | **char** |
| dash | `em` 13, `en` 150 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 9 | _mixed_ |
| register | `informal` 11, `formal` 605 | **formal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- The dual is used correctly throughout: `one` / `two` / `few` / `other` are all present and right. Never flag plural coverage.
- Short button labels use the informal singular imperative by convention.
- Prompt strings in `genai.ftl` use the informal imperative on purpose — they address the model, not the user.
- Brand terms are declined with a `sklon` (case) parameter. This is correct Slovenian and has no en-US equivalent.
- The typo in `cclear-data-for-site-permissions` is upstream in en-US.

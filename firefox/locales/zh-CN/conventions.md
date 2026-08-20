# zh-CN — conventions and review instructions

_Counted over the whole zh-CN tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 979, `straight-double` 46, `curly-single` 41 | **curly-double** |
| apostrophe | `typographic` 46, `straight` 20 | _mixed_ |
| ellipsis | `char` 439, `ascii` 13 | **char** |
| dash | `em` 78, `en` 2 | **em** |
| fullwidth | `punctuation` 9514 | **punctuation** |
| register | `informal` 15, `formal` 1742 | **formal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- Punctuation is fullwidth: `，。？！：；` and `“ ”`.
- The register is formal `您`; flag only a mix of `你` and `您`.
- Half-width commas inside `quickactions-cmd-*` keyword lists are correct — they match en-US.
- Access keys are meaningless for Chinese; the check is disabled.

# ja — conventions and review instructions

_Counted over the whole ja tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 490, `curly-single` 193, `straight-double` 122, `corner` 7 | _mixed_ |
| apostrophe | `typographic` 270, `straight` 12 | **typographic** |
| ellipsis | `ascii` 459 | **ascii** |
| dash | `em` 81, `en` 1 | **em** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 11 | _mixed_ |
| fullwidth | `punctuation` 5726 | **punctuation** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- The ellipsis is three ASCII dots, not `…`. This is deliberate and the opposite of most locales.
- Access keys are unadapted English letters. This is correct: the platform appends the key in parentheses, e.g. `(W)`. Never flag them.
- Quotes are `“ ”`; parentheses are halfwidth with a leading space; `？` and `！` are fullwidth; sentences end with `。`.
- A trailing `。` where en-US has `.` is the convention, not a defect.
- `.label` and `.aria-label` use the noun form while `.title` uses `〜します`. This accounts for most apparent cross-file inconsistency.
- `toolkit/toolkit/global/neterror/nsserrors.ftl` is deliberately left in English.
- `マスターパスワード` for “Primary Password” is a deliberate legacy term.

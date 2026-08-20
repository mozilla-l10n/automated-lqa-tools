# nl — conventions and review instructions

_Counted over the whole nl tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 890, `straight-double` 25, `curly-double` 9 | **curly-single** |
| apostrophe | `typographic` 1136 | **typographic** |
| ellipsis | `char` 460 | **char** |
| dash | `en` 135 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `formal` 3089 | **formal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- The register is formal `u` / `uw`, used exclusively.
- The apostrophe is `’`; quotes are both `‘…’` and `“…”`.
- The **en dash** `–` is the house dash. The em dash in `browser-main-window-titles*` is the deviation, and the en dash in `downloadUtils.ftl` is deliberate despite the en-US comment saying “em dash”.
- Labels are sentence case; menu commands and checkboxes use the infinitive.
- Closed one-word compounds are correct Dutch, not typos.
- Where en-US wraps a single variant in `{ $n -> *[other] … }` and the Dutch flattens it, that is not a defect.
- A term reference passing a parameter the Dutch term ignores is harmless in Fluent.

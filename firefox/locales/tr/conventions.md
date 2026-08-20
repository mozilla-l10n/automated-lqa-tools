# tr — conventions and review instructions

_Counted over the whole tr tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 670, `curly-single` 166, `straight-double` 29 | **curly-double** |
| apostrophe | `typographic` 952, `straight` 50 | **typographic** |
| ellipsis | `char` 459 | **char** |
| dash | `em` 72, `en` 2 | **em** |
| nbsp | `total` 9, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 2, `formal` 58 | **formal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- Quotes are `“…”` and the apostrophe is `’` (U+2019).
- The register is formal *siz*.
- A suffix attached to a term reference **without** an apostrophe is correct when the term is a common noun (`{ -smart-window-brand-name }yi`). Only true proper nouns take `’`.
- `ön izleme` as two words is settled convention.
- Several en-US strings are themselves defective (`import-safari-permissions-string`, the `about-logging-unknown-*` family, `about-telemetry-data-details-current`); those are upstream, not Turkish defects.

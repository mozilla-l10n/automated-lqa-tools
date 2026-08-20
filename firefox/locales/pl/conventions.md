# pl — conventions and review instructions

_Counted over the whole pl tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 1552, `straight-double` 36, `german-double` 7, `curly-double` 2 | **polish-double** |
| apostrophe | `straight` 1 | **straight** |
| ellipsis | `char` 459 | **char** |
| dash | `em` 170, `en` 12 | **em** |
| nbsp | `total` 5383, `narrow` 3, `before-punctuation` 49, `space-before-punctuation` 21 | **total** |
| register | `informal` 79 | **informal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- Quotes are `„…”` (U+201E/U+201D) and the ellipsis is `…`.
- A no-break space follows one-letter words; this is applied ~99% of the time and the remaining gaps are mostly string-initial or inside `genai.ftl` prompt bodies.
- Brand terms take grammatical-case parameters (`{ -brand-short-name(case: "gen") }`) with keys nom/gen/dat/acc/ins/loc plus lower/upper. Naive plural-category checks flag these; they are correct.
- Plural sets are `one` / `few` / `*[many]` with no `other`. Correct.
- The impersonal `Można…` construction is house style.
- Slang in `quickactions-cmd-*` (`apdejt`, `skrin`, `laborki`) and the unaccented `przegladarka` in `findbar-match-diacritics` are deliberate, not typos.

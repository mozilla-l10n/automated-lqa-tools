# fy-NL — conventions and review instructions

_Counted over the whole fy-NL tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 875, `straight-double` 27, `curly-double` 18 | **curly-single** |
| apostrophe | `typographic` 1645 | **typographic** |
| ellipsis | `char` 461 | **char** |
| dash | `em` 26, `en` 95 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 7 | _mixed_ |

## Instructions for the reviewer

<!-- Add rules here, e.g.:
- Access keys are intentionally left as English letters; never flag them.
- The en dash is the house dash; do not suggest an em dash.
- "Primary Password" is deliberately translated with the legacy term.
-->

- A capitalised word whose other letters are lowercase never carries a
  diacritic on its first letter: `Ut`, `Us`, `Untskoattelje`, `Ofspylsnelheid`,
  `Unbetroubere` are correct. Diacritics are written on lowercase letters
  (`ûnbekend`) and in words written entirely in capitals (`ÛNBEKEND`). Never
  suggest adding a diacritic to a capitalised initial. A diacritic missing from
  a lowercase letter is still a defect.

# zh-TW — conventions and review instructions

_Counted over the whole zh-TW tree on 2026-10-16. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 890, `straight-double` 34, `curly-single` 9, `curly-double` 6 | **corner** |
| apostrophe | `typographic` 9, `straight` 9 | _mixed_ |
| ellipsis | `char` 400 | **char** |
| dash | `em` 52, `en` 1 | **em** |
| nbsp | `total` 1, `space-before-punctuation` 5 | **space-before-punctuation** |
| fullwidth | `punctuation` 8324 | **punctuation** |

## Instructions for the reviewer

<!-- Add rules here, e.g.:
- Access keys are intentionally left as English letters; never flag them.
- The en dash is the house dash; do not suggest an em dash.
- "Primary Password" is deliberately translated with the legacy term.
-->

- Do not raise a finding that only replaces an accurate translation with a
  synonym or equally valid wording, such as 報表 for 報告 in a crash report,
  or a different measure word. Flag it only when meaning is changed or lost
  ("older than %S months" rendered as "%S months ago"), when it breaks the
  glossary, or when English is left untranslated.

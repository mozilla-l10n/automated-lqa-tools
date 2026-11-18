# zh-TW — conventions and review instructions

_Counted over the whole zh-TW tree on 2026-10-16. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `corner` 24 | **corner** |
| ellipsis | `char` 21 | **char** |
| fullwidth | `punctuation` 1071 | **punctuation** |

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

- Put a space between Chinese characters and adjacent Latin letters, digits
  or placeholders (`Firefox Sync 已連結到 %@`), and never between full-width
  punctuation such as `「」（），。` and the characters next to it
  (`「coords」屬性`, not `「coords」 屬性`). The tree is consistent on both.
  A placeholder is spaced by what it expands to: in `自 %s起` the date
  renders as `YYYY 年 MM 月 DD 日`, which ends in a Chinese character, so no
  space follows it.
- "Passkey" stays in English, as the glossary says. A string that
  translates it as 密碼金鑰 is the inconsistent one; never suggest
  translating "Passkey".
- A status indicator uses the bare verb: 啟用 for "Enabled" is correct.
  Chinese has no perfect tense, so never flag a status label for lacking
  已.

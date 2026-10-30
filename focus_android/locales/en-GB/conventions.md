# en-GB — conventions and review instructions

_Counted over the whole en-GB tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 15, `curly-single` 1 | **curly-double** |
| apostrophe | `typographic` 168 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 4 | **em** |

## Instructions for the reviewer

- "web site" / "web sites" as two words is the house form where en-US writes
  "website" / "websites". It is deliberate; never flag it, and never suggest
  closing it up to match the source.
- "Backwards" and "Forwards" are the house forms where en-US writes "Back"
  and "Forward" — including in navigation labels and accessibility
  descriptions. Deliberate; never flag either, and do not report the two
  spellings coexisting in one file as an inconsistency.
- "Post Code" is the deliberate rendering of the en-US "Postal Code". Do not
  flag the spacing or capitalisation, and do not suggest "Postcode".
- Spelling out the en-US "sync" family is the house form: "synchronise",
  "synchronised", "synchronising", "synchronisation" (and the -ize/-ized
  spellings) are all acceptable renderings of "sync", "synced", "syncing",
  "sync'd". Never flag the expansion as a mistranslation or as added words,
  never suggest shortening it back to "sync", and do not report the short and
  spelled-out forms coexisting in one file as an inconsistency.

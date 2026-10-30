# it — conventions and review instructions

_Counted over the whole it tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 25 | **curly-double** |
| apostrophe | `typographic` 171 | **typographic** |
| ellipsis | `char` 24 | **char** |
| dash | `em` 2 | **em** |
| register | `informal` 90, `formal` 4 | **informal** |

## Instructions for the reviewer

- Dropping a trailing `!` from the source and ending the sentence with `.`
  is a deliberate choice, not an omission. Italian UI text uses the
  exclamation mark far more sparingly than English. Never report a missing
  or changed final `!`.
- `crittare`, and its forms `critta`, `crittato`, `crittati`, is the correct
  Italian verb for "to encrypt". It is not a typo for `criptare`, and it is
  not a truncation of anything. Never report it as a misspelling.
- The expected pair is `Attiva`/`Attivo`/`Attivi` for the positive and
  `Disattivata`/`Disattivato`/`Disattivati` for the negative. The asymmetry
  is intentional: never propose `Attivata`/`Attivato`/`Attivati` to make the
  two sides match.

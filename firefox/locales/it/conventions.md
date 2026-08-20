# it — conventions and review instructions

_Counted over the whole it tree on 2026-08-20. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 1046, `straight-double` 25 | **curly-double** |
| apostrophe | `typographic` 1925, `straight` 6 | **typographic** |
| ellipsis | `char` 481 | **char** |
| dash | `em` 75, `en` 18 | **em** |
| nbsp | `total` 12, `before-punctuation` 4, `space-before-punctuation` 6 | _mixed_ |
| register | `informal` 760, `formal` 59 | **informal** |

## Instructions for the reviewer

_Carried over from the hand-written review; these are maintainer decisions, not guesses._

- Access keys are localized and correctly paired with their labels.
- `Elenco lettura` for Safari's Reading List is correct; it is not an inconsistency with Edge's `Elenco di lettura`.
- In DevTools, the CSS keyword `grid` stays English — do not suggest `griglia`.
- The `enterprise/` and FELT files exist only in this locale and are legitimate; they have no en-US counterpart.
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

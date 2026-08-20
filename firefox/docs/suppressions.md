# Flagging false positives

Every locale does something that looks like a defect and is not. Japanese
writes ellipsis as three ASCII dots. Dutch uses an en dash where en-US uses
an em dash. Polish and Slovenian decline brand names through a case
parameter that en-US has no concept of. Turkish attaches suffixes to term
references without an apostrophe. None of these are errors, and a system
that re-raises them every run is a system nobody reads.

There are two places to record that, and the difference matters.

## 1. `conventions.md` — stop it being raised

`firefox/locales/<code>/conventions.md` is prose, injected verbatim into
every review prompt. Anything written there is what the model is told to
treat as correct.

**Prefer this.** It is cheaper (no finding is ever created), it explains the
*why* to the next reader, and it generalizes — "access keys are deliberately
English" covers strings that do not exist yet.

The top of the file is a table of conventions counted over the whole tree.
It is generated, but you should correct it if the counting got something
wrong. Below it, write instructions in plain language:

```markdown
## Instructions for the reviewer

- The ellipsis is three ASCII dots, not `…`. Deliberate.
- Access keys are unadapted English letters — the platform appends `(W)`.
- `マスターパスワード` for "Primary Password" is a deliberate legacy term.
- `toolkit/toolkit/neterror/nsserrors.ftl` is deliberately left in English.
```

## 2. `suppressions.yaml` — filter it afterwards

`firefox/locales/<code>/suppressions.yaml` is structured and applied after
findings exist. Use it for what prose cannot reach: the **deterministic
checks**, which have no prompt to read, and anything the model raises
anyway.

```yaml
rules:
  - id: ja-english-accesskeys
    reason: >-
      Access keys are intentionally English; the platform appends `(W)`.
    match:
      check: accesskey

  - id: pl-brand-case-params
    reason: >-
      Brand terms carry grammatical-case parameters; correct Polish.
    match:
      check: term_params
      text: case

  - id: it-critta
    reason: >-
      `critta` is correct — `crittare` means to encrypt. Maintainer confirmed.
    match:
      string_id: credit-card-save-doorhanger-description
```

Every rule needs an `id` and a `reason`. A rule with no reason is rejected,
because six months from now nobody will remember why it is there.

### Match fields

Conditions inside `match` are ANDed.

| Field | Matches against |
|---|---|
| `check` | which check raised it: `variables`, `selectors`, `term_params`, `accesskey`, `markup`, `typography`, or `llm` |
| `category` | the report category, `A`–`E` |
| `string_id` | exact, `prefix*`, or `re:<regex>` |
| `file` | exact, `prefix*`, or `re:<regex>` |
| `text` | case-insensitive substring of the summary, rationale or current value |

Be as narrow as the truth allows. `check: typography` silences every
typography finding for the locale forever, including ones you would want to
see; `check: typography` plus `text: ellipsis` silences only the ellipsis
class.

## How rules behave over time

- **They are retroactive.** Rules are re-applied to the *whole* backlog on
  every run, not just to new findings. Write a rule today and every matching
  finding ever raised is retired — no re-review, no API call.
- **They are reversible.** Delete a rule and its findings return to `open`
  on the next run. The suppressed state is stored with the rule id that
  caused it, so nothing is lost.
- **Nothing is deleted.** Suppressed findings stay in
  `state/<code>/findings.json` and appear in the report appendix, grouped by
  rule, with their reason. A wrong rule is visible rather than silent.

## Things that are not false positives

A few classes are handled elsewhere; do not write rules for them.

- **Missing or untranslated strings.** Reported in the health check, never
  raised as findings. They need translating, not suppressing.
- **A check firing on hundreds of strings.** That is collapsed automatically
  into a single systemic item in section 2 of the report — one decision for
  the locale team, not N bugs. The threshold is `systemic_threshold` in
  `config.yaml`.
- **A convention the tree is genuinely split on.** Checks only flag
  deviations from the locale's own clear majority. Where counting shows a
  real mix — German's quote style, for instance — nothing is flagged at all,
  and the report says `_mixed_`.
- **A defect that is upstream in en-US.** Worth recording as a note in
  `conventions.md` so the model stops attributing it to the locale, but it
  is a real bug — just not this locale's.

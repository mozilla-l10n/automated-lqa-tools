# Saying a finding is fine

Three mechanisms, and the difference is scope. Reach for the narrowest one
that fits.

## One string you have read — `dismissed.txt`

You looked at the finding, the translation is fine, move on. One line in
`firefox_ios/locales/<code>/dismissed.txt`:

```
browser_menu_summarize_page_badge — "Novità" is the agreed wording
```

No id to invent, no match expression, no scope to get wrong. Where the same
string id exists in more than one file, qualify it:

```
recent_tabs_header @ mozilla-mobile/fenix/ — fine in this context
```

The text after the dash is kept with the finding and printed in the report,
so the next person can see why it was dropped.

## A class of finding that will recur — `suppressions.yaml`

Not one string but a kind: every access key, anything quoting `critta`, a
whole file that is deliberately untranslated. Worth the ceremony of an id, a
reason and a match expression, because it will apply to strings nobody has
written yet. See below.

## Something the reviewer should never raise at all — `conventions.md`

Best of the three when it fits. Prose, injected into every review prompt, so
no finding is created and no tokens are spent. "The ellipsis is three ASCII
dots." "Access keys are deliberately English."

---

All three are re-applied to the whole backlog on every run, so any of them
retires findings raised months ago, and removing an entry brings them back.
Nothing is deleted from `state/`: a dismissed or suppressed finding keeps
its reason and appears in the report appendix.

# Rules for a whole class

Every locale does something that looks like a defect and is not — a
deliberate ellipsis style, a house dash, a term left in English on purpose.
None of these are errors, and a system that re-raises them every run is a
system nobody reads.

There are two places to record that, and the difference matters.

## 1. `conventions.md` — stop it being raised

`firefox_ios/locales/<code>/conventions.md` is prose, injected verbatim into
every review prompt. Anything written there is what the model is told to
treat as correct.

**Prefer this.** No finding is ever created, it explains the *why* to the
next reader, and it generalizes — "access keys are deliberately
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

`firefox_ios/locales/<code>/suppressions.yaml` is structured and applied after
findings exist. Use it for what prose cannot reach: the **deterministic
checks**, which have no prompt to read, and anything the model raises
anyway.

```yaml
rules:
  - id: it-onboarding-brevity
    reason: >-
      Onboarding strings are deliberately terser than the English to fit a
      phone screen; the developer notes set the limits.
    match:
      check: llm
      file: Shared/Supporting Files/en.lproj/Onboarding.strings

  - id: it-critta
    reason: >-
      `critta` is correct — `crittare` means to encrypt. Maintainer confirmed.
    match:
      string_id: some_string_id
```

Every rule needs an `id` and a `reason`. A rule with no reason is rejected,
because six months from now nobody will remember why it is there.

### Match fields

Conditions inside `match` are ANDed.

| Field | Matches against |
|---|---|
| `check` | which check raised it: `placeholders`, `ui_references`, `typography`, `variant_spelling`, or `llm` |
| `category` | the report category, `A`–`E` |
| `string_id` | exact, `prefix*`, or `re:<regex>` |
| `file` | exact, `prefix*`, or `re:<regex>` |
| `text` | the summary, rationale or current value |
| `suggest` | the proposed replacement — use this when the rule is about a correction that must never be accepted, rather than about the string being corrected |

`text` and `suggest` are case-insensitive substrings, or a full regex with a
`re:` prefix. Reach for the regex when a substring would over-match: the
Italian rule against proposing `Attivato` has to be written
`re:\battivat[aoie]\b`, because plain `attivat` also matches `disattivato`.

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

## When a check itself was wrong

Suppressions are for correct localization that a check misreads. If the
*check* is wrong — it would misfire the same way on any locale — fix the
check instead, and add the case to `tools/selftest.py` so it cannot come
back.

Findings that disappear because a check changed its mind are recorded as
**withdrawn**, not fixed: the string never moved, so nobody fixed anything.
They are listed separately in the report appendix, which keeps the fixed
count honest.

## Re-checking an existing backlog

`--recheck` re-verifies every open finding against the tree as it stands,
instead of only those the run's delta points at:

```bash
python lib/run.py --project firefox --locale it --recheck \
    --l10n-dir ... --source-dir ...
```

It closes findings whose quoted text has gone, and sends back to the
reviewer the ones where the string moved but text matching cannot settle
whether the defect went with it.

**Do not put it in the scheduled workflow.** A normal run already resolves
a finding whenever its string changes -- that is judged against the hash
recorded when the finding was raised, so it holds however long ago that
was. `--recheck` exists for the case a normal run cannot cover: the
*checking logic itself* changed, so conclusions reached under the old logic
need revisiting. That is a thing you do deliberately after editing
`lib/findings.py` or importing a backlog, not every night.

It is also the more expensive path. It re-queues moved strings for the
reviewer regardless of the delta, and on a large backlog that is a much
bigger batch than the handful a normal run looks at.

## Things that are not false positives

A few classes are handled elsewhere; do not write rules for them.

- **Missing or untranslated strings.** Reported in the health check, never
  raised as findings. They need translating, not suppressing.
- **A check firing on hundreds of strings.** That is collapsed automatically
  into a single systemic item in section 2 of the report — one decision for
  the locale team, not N bugs. The threshold is `systemic_threshold` in
  `firefox_ios/config.yaml`.
- **A convention the tree is genuinely split on.** Checks only flag
  deviations from the locale's own clear majority. Where counting shows a
  real mix — German's quote style, for instance — nothing is flagged at all,
  and the report says `_mixed_`.
- **A defect that is upstream in en-US.** Worth recording as a note in
  `conventions.md` so the model stops attributing it to the locale, but it
  is a real bug — just not this locale's.

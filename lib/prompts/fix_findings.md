You are correcting {language} ({locale}) localization strings. An earlier
review raised findings against them, in these groups:

{groups}

Each fix you make is sent to Pontoon as a
suggestion that a {language} reviewer accepts or rejects by hand, so a wrong
or gratuitous edit costs them time.

For every string you get the en-US source, the current translation (as
Pontoon displays it), and the findings raised against it. Judge each finding
on its own and give it one verdict:

- `fix` — the finding is right, and the defect can be removed with a small
  literal edit. Supply the edit.
- `false_positive` — the finding is wrong: the translation is correct as it
  stands. Use it only when you are sure. Typical cases: en-US has the very
  same feature (a straight quote, a missing period, an odd word) — a locale
  is never at fault for its source; the "defect" is a convention this locale
  measurably uses (see below); the finding misreads the source or quotes
  text that is not in the translation. Your reason is shown to a person who
  will check it, and a string dismissed this way is hidden from every later
  review until somebody removes the line, so when in doubt say `skip`.
- `skip` — anything else: you are not certain either way, fixing it needs
  rewording beyond the defect, it would need a placeholder or markup changed,
  or it depends on context you do not have.

Rules for edits:

1. **Fix the defect the finding names, and only that.** The finding's
   `suggest` is the reviewer's idea, not a patch: it often rewrites wording
   beyond the defect or covers only a fragment. Make the smallest edit that
   removes the defect. Do not reword, do not fix other things you notice.
2. **Never introduce a convention the locale does not use.** The measured
   counts below say what the {language} tree actually does (apostrophes,
   quotes, dashes, ellipsis, spaces before punctuation, register). Follow the
   majority; where usage is split, do not "correct" either way.
3. **Placeholders and markup are untouchable.** Anything that looks like
   `{{ $var }}`, `%1$s`, `%@`, `<b>`, `</a>`, `{{ -brand-name }}` must survive
   exactly, and the same number of times. An edit may move text around them
   but never into, out of, or across them.
4. Each edit is a literal `find`/`replace` pair. `find` is copied exactly
   from the translation as shown, lies entirely within the text between two
   placeholders, and appears exactly `occurrences` times in the whole string
   (all attributes and plural variants included); every one of those
   occurrences is replaced. Make `find` long enough to be unambiguous.
5. Write invisible characters as JSON escapes: ` ` no-break space,
   ` ` narrow no-break space, `‌` ZWNJ, `‏` RLM. Never paste
   them raw.
6. A string with no `fix` verdict gets no edits. A string with several `fix`
   verdicts gets the edits for all of them.

Call `report_fixes` exactly once, covering every string and every finding
you were given.

## Conventions recorded for {locale}

{conventions}

## Measured usage in the {locale} tree

```json
{measured}
```

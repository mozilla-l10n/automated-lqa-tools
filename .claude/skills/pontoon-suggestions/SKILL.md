---
name: pontoon-suggestions
description: Fix one category of open findings for a project and locale by editing copies of the localized files, then submit the fixes to Pontoon as unreviewed suggestions. Use when asked to "fix the E findings for android fa", "send suggestions to Pontoon", or similar.
---

# Submitting fixes to Pontoon as suggestions

Arguments: a **project** (`android`, `firefox`, `firefox_ios`), a **locale**
(`fa`), a **category** (`A`–`E`, see `CATEGORIES` in `lib/findings.py`; `E` is
typography, punctuation and spacing). Ask for any that are missing, and for the
clone path if the defaults below do not exist.

Clones: `~/github/android-l10n` (android, pass it once — it is its own
reference), `~/github/firefoxios-l10n` (firefox_ios), and for firefox
`--l10n-dir ~/mozilla-source/git/firefox-l10n --source-dir
~/mozilla-source/git/firefox-quarantine`. They
are used exactly as they are on disk. If the user has not pulled recently, say
so before starting: `upload` drops every string that has moved in Pontoon since
then.

All the mechanics are in `lib/suggest.py`. Edits go to copies under
`work/suggestions/<project>/<locale>/<category>/files/` (gitignored). **Never
edit the clone**: `run.py` reads it as-is and would mark findings fixed that
nobody in Pontoon has accepted.

## 1. Prepare

```bash
.venv/bin/python lib/suggest.py prepare --project android --locale fa --category E \
    --l10n-dir ~/github/android-l10n
```

This writes `worklist.json`: one entry per open finding with the full
`translation`, the `source`, the reviewer's `summary`, `rationale` and
`suggest`, the `localized` file to edit, and `moved` (the string changed after
the finding was raised, so re-read it before believing the finding). It
refuses to overwrite an existing work directory, since that may hold edits.
Pass `--reset` only if the user agrees to discard them.

Before editing, read `<project>/locales/<locale>/conventions.md` and
`<project>/state/<locale>/conventions.json`. What the tree measurably does is
the standard. Never introduce a convention the locale does not use.

## 2. Edit

For each finding, edit the string in the copy under `files/`:

- **Fix the defect the finding names, and only that.** `suggest` is the
  reviewer's idea, not a patch: it often rewrites wording beyond the category,
  or covers only a fragment of the string. Make the smallest edit that removes
  the defect. A one-morpheme correction in a fragment you are already editing
  (for example a wrong suffix right next to the misplaced colon) is fine.
  Rewording a sentence is not.
- **Skip findings you do not believe.** Compare with the source. If en-US has
  the same issue, or the finding is wrong, leave the string alone and list it
  in your summary with the reason. Do not dismiss or edit state yourself.
- **Edit only strings that have a finding.** If you see the same defect in
  another string, report it and don't fix it. `diff` refuses unlisted edits.
  If the user then asks for it to be fixed too, record that first:

  ```bash
  .venv/bin/python lib/suggest.py include --project android --locale fa --category E \
      --string-id <id> --reason "Same <defect> as <id> (<fid>); no finding raised."
  ```

  `--file` (the reference path) is needed only when the id is not unique.
  This copies the file into the work directory if it is not there already.
- **An empty `source`** means the string has no en-US counterpart in this
  repository (Firefox's `enterprise/` files). Fix only what holds without
  English, such as a typographic convention the tree measurably uses. Do not
  guess what the English said.
- **Keep the file's own encoding** of the value: CDATA, `\'`, `&amp;`,
  `‌` versus a literal character. Copy whatever that file already does.
- **Invisible characters** (ZWNJ U+200C, RLM U+200F, NBSP U+00A0, NNBSP
  U+202F) cannot be reliably typed into an Edit call. Apply such edits with a
  short Python script that spells them as `\u` escapes, replaces exact
  substrings and asserts each matches exactly once. Anchor on the string's
  `name=`/id when the fragment is not unique in the file. When showing such
  strings to the user, render them as `<ZWNJ>` and so on.

## 3. Check

```bash
.venv/bin/python lib/suggest.py diff --project android --locale fa --category E
```

This lists every changed string (old/new, in Pontoon's own rendering) with the
finding ids it addresses. It exits non-zero if an edited file does not parse,
if placeholders or markup were added, dropped or altered, or if a string with
no finding was touched. Fix everything it reports. Show the user the diff, with
invisible characters made visible.

## 4. Upload

Dry run first, always:

```bash
.venv/bin/python lib/suggest.py upload --project android --locale fa --category E
```

For each changed string this fetches Pontoon's current approved translation and
skips the string (`SKIP …`) if it differs from the clone or already equals the
fix. It then writes one partial file per Pontoon resource, containing only the
changed strings, under `upload/`. Report the SKIP lines and the resources.
"No approved translation in Pontoon" usually means en-US changed the
message's shape and the locale's translation is obsolete there. Leave it.
Which Pontoon project a path goes to is the `pontoon:` block of the project's
`config.yaml`. Firefox's `enterprise/` files go to `firefox-enterprise`.

Submitting publishes suggestions under the user's Pontoon account, and that
cannot be undone from here. **Only add `--submit` after the user has seen the
dry run and explicitly said to send it.** It needs a Personal Access Token from
<https://pontoon.mozilla.org/settings/> in `PONTOON_TOKEN`, with translator
rights for the locale. Have the user export it themselves, and never echo,
store or commit it.

```bash
PONTOON_TOKEN=... .venv/bin/python lib/suggest.py upload --project android \
    --locale fa --category E --submit
```

Each response reports `created`, `restored` (a previously rejected identical
suggestion was revived), `unchanged`, `failed_checks` (rejected by Pontoon's
checks; report each) and `undefined_keys`. A log is appended to
`uploaded.json` in the work directory. Re-running is harmless, since identical
suggestions come back as `unchanged`.

Do not touch `state/`: findings close on their own when an accepted suggestion
reaches the repository and the next run sees the string move.

## Summary for the user

List the strings suggested, the findings skipped as unconvincing (with
reasons), the strings dropped by verification, and any same-defect strings you
noticed that have no finding. Leave out cost figures.

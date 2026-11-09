# Focus for Android l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f7a886b5b048` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f7a886b5b048` |
| **Previous run** | 2026-11-09 @ `bf7b409a0435` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 245 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sl: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### ↩︎ Withdrawn — no longer considered a defect (0)

_Nothing withdrawn._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 1 |
| Strings | 245 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 17, `curly-double` 2 | **straight-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 5 | **en** |
| register | `informal` 4, `formal` 90 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

### Proposed conventions — not applied (1)

Recurring reasons in this locale's tool-written dismissals. Nothing here reaches the reviewer until a person adds it to `focus_android/locales/sl/conventions.md`; an inferred reason is a model's guess at why a Pontoon reviewer said no.

- Short UI command labels (buttons, links, menu items, toggles and setting labels) use the 2nd-person singular imperative, e.g. "Obnovi podatke", "Posodobi", "Omogoči". This is the normal form for labels and does not break the formal register, so do not flag it. It also applies when running text quotes a button label: the quote must match the label's actual wording (e.g. "Obnovi podatke"), not a formal "Obnovite …" header. Still flag: full sentences, descriptions and messages addressed to the user that use informal ti-forms instead of the formal vi-forms, and quoted label text that differs from the referenced label string.
    _Behind it: 6 dismissals, 2 of them rejected in Pontoon._

    - `backup-file-moz-browser-restore-step-2-1` (firefox) — _rejected, reviewer's comment_: vX1Hk3se1FZ1WU5PoOJOALMcZjw: <p>Sprememba na narobe. Citirani niz (backup-folder-name) je "Obnovi podatke". https://pontoon.mozilla.org/sl/firefox/browser/browser/backupSettings.ftl/?string=324818</p>
    - `backup-file-other-browser-restore-step-3-1` (firefox) — _rejected, reason inferred_: The quoted text is probably a button label, and this locale's convention is that short button labels use the informal singular imperative, so "Obnovi podatke" likely matches the actual button rather than the "Obnovite podatke" header the finding compared it to.
    - `link_sharing_toggle_title` (android) — _model_: Slovenian UI labels and toggles conventionally use the 2nd-person singular imperative (e.g. "Shrani", "Prikaži"), which is not a register violation.
    - `onboarding_term_of_service_line_three_link_text` (android) — _model_: Slovenian UI command labels (buttons/links) normally use the singular imperative (e.g. 'Shrani', 'Prekliči'), independent of the formal register used in prose.
    - `preference_enhanced_tracking_protection_custom_global_privacy_control` (android) — _model_: Setting labels in sl use this imperative form (cf. "Omogoči"), and the suggested "sporoči" is the same 2nd-person singular, so there is no register mismatch.
    - `Onboarding.Modern.BrandRefresh.TermsOfUse.AgreementButtonTitle.v148` (firefox_ios) — _model_: Singular imperative is the standard Slovenian button form (cf. "Posodobi", "Dovoli"); the reviewer's own suggestion keeps "nadaljuj".

---

## 3. Open findings (10)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 5 |
| 3 | Degraded language (grammar, spelling, terminology) | 4 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `dismiss_no_suggestions_prompt_button` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Dismiss" is translated as "V redu" (OK), which is a different action label.
    - Current: `V redu`
    - Source: `Dismiss`
    - Suggest: `Opusti`
    - The source button dismisses the message; "V redu" means "OK", not "dismiss".
- `preference_auto_battery_theme` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Set by Battery Saver" is rendered as an imperative "Set the battery saver", reversing the meaning.
    - Current: `Nastavi ohranjevalnik baterije`
    - Source: `Set by Battery Saver`
    - Suggest: `Nastavi ohranjevalnik baterije → "Nastavi ohranjevalnik baterije" naj bo "Nastavi varčevanje z baterijo" (tj. "Določi ohranjevalnik baterije")`
    - The source means the theme is determined by the Battery Saver setting; the Slovenian reads as a command to set/configure the battery saver, i.e. the battery saver becomes the object rather than the agent.
- `preference_exceptions_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "disabled content blocking" is translated as "onemogočili zavračanje vsebine" but with a term inconsistent with the rest; more importantly the sense of blocking is rendered oddly.
    - Current: `Za ta spletna mesta ste onemogočili zavračanje vsebine.`
    - Source: `You have disabled content blocking for these websites.`
    - Suggest: `Za ta spletna mesta ste onemogočili blokiranje vsebine.`
    - Focus uses "blokiranje vsebine" for content blocking; "zavračanje vsebine" is a different term used inconsistently.
- `preference_https_only_summary3` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — The translation drops "to sites" from "connect to sites using the HTTPS encryption protocol".
    - Current: `Za večjo varnost poskuša samodejno vzpostaviti povezavo s šifrirnim protokolom HTTPS.`
    - Source: `Automatically attempts to connect to sites using the HTTPS encryption protocol for increased security.`
    - Suggest: `Za večjo varnost poskuša samodejno vzpostaviti povezavo s spletnimi mesti prek šifrirnega protokola HTTPS.`
    - Source says it attempts to connect to sites using HTTPS; the target says it connects to the protocol itself, losing the object of the connection.
- `search_add_error_duplicate_name` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "An installed search engine" is rendered as definite "Nameščeni iskalnik", changing the meaning.
    - Current: `Nameščeni iskalnik že uporablja to ime.`
    - Source: `An installed search engine is already using that name.`
    - Suggest: `To ime že uporablja eden od nameščenih iskalnikov.`
    - The source says some installed search engine already uses that name (indefinite); the Slovenian reads as "The installed search engine already uses this name".

### C. Grammar, agreement & spelling

- `share_dialog_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "preko" with genitive is a non-standard preposition use; standard Slovene is "prek".
    - Current: `Deli preko`
    - Source: `Share via`
    - Suggest: `Deli prek`
    - Slovene style guides prefer "prek"; "Deli preko" is a colloquialism.

### D. Terminology, register & consistency

- `preference_privacy_secure_mode` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Stealth" is translated as "Skrivni način" (secret mode) rather than a stealth/hidden-mode term matching the feature name.
    - Current: `Skrivni način`
    - Source: `Stealth`
    - Suggest: `Prikrit način`
    - The developer comment describes Stealth mode as hiding app content; "skrivni" (secret) suggests private browsing, which is a different Focus concept.
- `preference_switch_autocomplete_topsites` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Top sites" is translated as "glavne strani", inconsistent with the top-site strings elsewhere in the file.
    - Current: `Za glavne strani`
    - Source: `For top sites`
    - Suggest: `Za glavne strani (priljubljene strani)`
    - Terminology for "top sites" should be consistent across the Top Sites section (remove_top_site/rename_top_site context).
- `social` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Tracker category "Social" is rendered with the masculine adjective "Družbeni" instead of the established category noun.
    - Current: `Družbeni`
    - Source: `Social`
    - Suggest: `Družbena omrežja`
    - This is a tracker category label; "Družbeni" alone is an incomplete adjective with no noun and does not name the category the way other categories do.

### E. Typography, punctuation & spacing

- `preference_https_only_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Uses straight double quotes where the source has none and Slovenian typography would use „ “ or none at all.
    - Current: `Način "samo HTTPS"`
    - Source: `HTTPS-Only Mode`
    - Suggest: `Način samo HTTPS`
    - The source title "HTTPS-Only Mode" contains no quotation marks; the added quotes are gratuitous.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sl/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (2)

- `menu_share` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string 76af4239): Slovenian typography and the sl Mozilla localization put a space before an ellipsis that follows a complete word (e.g. "Shrani kot …").
- `preference_licensing_info` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — auto-suggest (2026-11-03, string a487408b): "Dovoljenje" is the standard Slovenian term for a software licence (e.g. GPL = "Splošno javno dovoljenje GNU").

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/sl/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (6)

- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_privacy_should_block_cookies_cross_site_option` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_privacy_should_block_cookies_yes_option2` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `preference_safe_browsing_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — fixed 2026-11-05

# Focus for Android l10n QA — sl

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 250 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

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
| Strings | 250 |
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
| quotes | `straight-double` 14, `curly-double` 4 | **straight-double** |
| ellipsis | `char` 21 | **char** |
| dash | `en` 5 | **en** |
| register | `informal` 4, `formal` 94 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (18)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 8 |
| 3 | Degraded language (grammar, spelling, terminology) | 8 |
| 4 | Cosmetic (typography, spacing) | 2 |

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
- `preference_licensing_info` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Licensing information" is rendered as "Podatki o dovoljenjih" (permissions), not licences.
    - Current: `Podatki o dovoljenjih`
    - Source: `Licensing information`
    - Suggest: `Podatki o licencah`
    - The developer comment says this links to Focus licensing information; "dovoljenja" means permissions, while software licences are "licence".
- `preference_privacy_should_block_cookies_cross_site_option` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Block cross-site cookies" is rendered as "Zavračaj spletne piškotke" (block web cookies), losing the "cross-site" qualifier.
    - Current: `Zavračaj spletne piškotke`
    - Source: `Block cross-site cookies`
    - Suggest: `Zavračaj piškotke med spletnimi mesti`
    - The source restricts blocking to cross-site cookies; "spletne piškotke" means simply "web cookies", i.e. all cookies, which is a different (and misleading) setting.
- `preference_privacy_should_block_cookies_yes_option2` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "Yes please" is translated as "Da!", dropping the polite "please" and adding an exclamation mark.
    - Current: `Da!`
    - Source: `Yes please`
    - Suggest: `Da, prosim`
    - The source is a polite option label paired with "No thanks" (translated "Ne, hvala"); the Slovenian loses the politeness marker and changes the punctuation.
- `search_add_error_duplicate_name` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "An installed search engine" is rendered as definite "Nameščeni iskalnik", changing the meaning.
    - Current: `Nameščeni iskalnik že uporablja to ime.`
    - Source: `An installed search engine is already using that name.`
    - Suggest: `To ime že uporablja eden od nameščenih iskalnikov.`
    - The source says some installed search engine already uses that name (indefinite); the Slovenian reads as "The installed search engine already uses this name".
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — The translation says "we never save your tabs" (plural) and then refers to "it", garbling the source's "we never save and cannot restore this tab".
    - Current: `Kot zaseben brskalnik nikoli ne shranimo vaših zavihkov in ga ne moremo obnoviti.`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `Kot zasebni brskalnik tega zavihka nikoli ne shranimo in ga ne moremo obnoviti.`
    - Source refers to a single tab ("this tab"); the target introduces "vaših zavihkov" (your tabs, plural) leaving the following singular pronoun "ga" without a matching antecedent.

### C. Grammar, agreement & spelling

- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — "ni potrebno" should be "ni treba" in standard Slovenian.
    - Current: `Aplikacije vam ni potrebno niti odpreti`
    - Source: `Notifications let you erase your %1$s session with a tap. You don’t need to open the app or see what’s running in your browser.`
    - Suggest: `Aplikacije vam ni treba niti odpreti`
    - With an infinitive the correct impersonal construction is "ni treba"; "ni potrebno" is a well-known non-standard usage.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Plural "custom URLs" translated as singular.
    - Current: `Odstrani URL po meri`
    - Source: `Remove custom URLs`
    - Suggest: `Odstrani URL-je po meri`
    - Source is "Remove custom URLs" (plural, screen for removing multiple URLs); the target is singular.
- `preference_safe_browsing_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Adjective agreement error: "Zavrni morebitne nevarne" should be "morebiti nevarne", and the verb form is inconsistent with the other block-preference titles.
    - Current: `Zavrni morebitne nevarne in zavajajoče strani`
    - Source: `Block potentially dangerous and deceptive sites`
    - Suggest: `Zavračaj morebitno nevarne in zavajajoče strani`
    - "morebitne nevarne" stacks two adjectives ungrammatically; the intended sense is "potentially dangerous" ("morebiti/morebitno nevarne"). Other Block* titles use the imperfective "Zavračaj".
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

- `menu_share` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — Space inserted before the ellipsis character.
    - Current: `Deli …`
    - Source: `Share…`
    - Suggest: `Deli…`
    - The source "Share…" has no space before the ellipsis; Slovenian typography also attaches the ellipsis directly to the word.
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

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `onboarding_first_screen_title` — `mozilla-mobile/focus-android/app/src/main/res/values-sl/strings.xml` — raised by `placeholders`, withdrawn 2026-08-24

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

# Focus for Android l10n QA — hu

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

Also for hu: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `polish-double` 16 | **polish-double** |
| ellipsis | `char` 23 | **char** |
| dash | `en` 4 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (17)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 11 |
| 3 | Degraded language (grammar, spelling, terminology) | 6 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `content_description_dismiss_input` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Dismiss" (close the overlay) rendered as "Elutasítás" (reject).
    - Current: `Elutasítás`
    - Source: `Dismiss`
    - Suggest: `Bezárás`
    - Per the developer comment the action dismisses the overlay and returns to the browser; "Elutasítás" means rejecting/declining, which is a different action.
- `dialog_addtohomescreen_tracking_protection2` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Translation says the shortcut opens "the application" instead of opening with Enhanced Tracking Protection disabled.
    - Current: `Az ikon fokozott követés elleni védelem nélkül fogja megnyitni az alkalmazást`
    - Source: `Shortcut will open with Enhanced Tracking Protection disabled`
    - Suggest: `A parancsikon kikapcsolt fokozott követés elleni védelemmel fog megnyílni`
    - The source states the shortcut will open with Enhanced Tracking Protection disabled; the Hungarian adds "the application" as an object, changing the meaning.
- `menu_add_to_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Add to Shortcuts" is translated as "Add to Home screen", duplicating menu_add_to_home_screen and losing the distinction between the two separate menu items.
    - Current: `Hozzáadás a kezdőképernyőhöz`
    - Source: `Add to Shortcuts`
    - Suggest: `Hozzáadás a parancsikonokhoz`
    - The source is "Add to Shortcuts" (adding the site to the Shortcuts list); the separate string menu_add_to_home_screen is "Add to Home screen". Rendering both identically makes the menu ambiguous and mistranslates "Shortcuts", which is elsewhere rendered "Parancsikonok" (see firstrun_shortcut_title).
- `menu_custom_tab_branding` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Powered by %1$s" is rendered as "A motorháztető alatt: %1$s" ("Under the hood"), which does not convey the source meaning.
    - Current: `A motorháztető alatt: %1$s`
    - Source: `Powered by %1$s`
    - Suggest: `Működteti: %1$s`
    - The source is a branding line meaning the tab is powered by the app; "A motorháztető alatt" means "under the hood", a different statement.
- `menu_remove_from_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Remove from Shortcuts" is translated as "Remove from Home screen", mistranslating the Shortcuts term.
    - Current: `Eltávolítás a kezdőképernyőről`
    - Source: `Remove from Shortcuts`
    - Suggest: `Eltávolítás a parancsikonok közül`
    - The developer comment and source refer to the Shortcuts list, not the device home screen; "Shortcuts" is rendered "Parancsikonok" elsewhere.
- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "see what's running in your browser" is rendered as "what runs in it (the app)", losing the browser reference.
    - Current: `sem megnéznie, hogy mi fut benne`
    - Source: `Notifications let you erase your %1$s session with a tap. You don’t need to open the app or see what’s running in your browser.`
    - Suggest: `sem megnéznie, hogy mi fut a böngészőjében`
    - The source says the user doesn't need to see what's running in their browser; the target's "benne" ambiguously refers back to the app.
- `preference_auto_battery_theme` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Battery Saver" is translated as "Energiagazdálkodás" (power management) instead of the Android feature name "Akkumulátorkímélő mód".
    - Current: `Energiagazdálkodás által beállítva`
    - Source: `Set by Battery Saver`
    - Suggest: `Az akkumulátorkímélő mód által beállítva`
    - The source refers to Android's Battery Saver feature, whose Hungarian name is "Akkumulátorkímélő"; "Energiagazdálkodás" names a different concept.
- `preference_autocomplete_add_title` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Singular "URL to add" rendered as plural.
    - Current: `Hozzáadandó webcímek`
    - Source: `URL to add`
    - Suggest: `Hozzáadandó webcím`
    - The source is singular (label for a single URL input field); the Hungarian uses the plural.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — The source "provide and improve %1$s for everyone" is rendered as "fejlesztéséhez és támogatásához" and drops "for everyone".
    - Current: `csak azt gyűjtse, ami a %1$s fejlesztéséhez és támogatásához szükséges`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `csak azt gyűjtse, ami a %1$s biztosításához és fejlesztéséhez szükséges mindenki számára`
    - The en-US string says Mozilla collects only what is needed to provide and improve the app for everyone; the translation omits "for everyone".
- `preference_privacy_should_block_cookies_third_party_only_option` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Block" is translated as "törlése" (delete) instead of "blokkolása" (block).
    - Current: `Csak a harmadik féltől származó sütik törlése`
    - Source: `Block 3rd-party cookies only`
    - Suggest: `Csak a harmadik féltől származó sütik blokkolása`
    - The source is "Block 3rd-party cookies only"; the sibling options all use "blokkolása". "Törlése" means deleting, which is a different action.
- `search_add_confirmation` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Confirmation that a search engine was added is rendered as an action/noun phrase ("Adding a new search engine") instead of a completed statement.
    - Current: `Új keresőszolgáltatás hozzáadása.`
    - Source: `New search engine added.`
    - Suggest: `Új keresőszolgáltatás hozzáadva.`
    - Source "New search engine added." is a past-tense confirmation; the Hungarian nominal form means "Add new search engine".

### C. Grammar, agreement & spelling

- `crash_report_send_crash_label` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Grammatical error: duplicated possessive suffix in "Összeomlási jelentése elküldése".
    - Current: `Összeomlási jelentése elküldése a Mozillának`
    - Source: `Send crash report to Mozilla`
    - Suggest: `Összeomlási jelentés elküldése a Mozillának`
    - "jelentése elküldése" is ungrammatical; the source is "Send crash report to Mozilla".
- `preference_autocomplete_add_hint` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Wrong definite article before a consonant-initial word.
    - Current: `Illessze be, vagy adja meg az webcímet`
    - Source: `Paste or enter URL`
    - Suggest: `Illessze be, vagy adja meg a webcímet`
    - Hungarian uses "a" before consonant-initial words; "az webcímet" is ungrammatical.
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — Misspelled "rendeleteben" and the word "Qualified" (minősített) is dropped from the sentence.
    - Current: `Az (EU) 2024/1183 rendeleteben meghatározottak szerint.`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Minősített az (EU) 2024/1183 rendeletben meghatározottak szerint.`
    - "rendeleteben" should be "rendeletben"; also the source states the certificate is "Qualified as specified in…", which the target omits.

### D. Terminology, register & consistency

- `snackbar_added_to_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "shortcuts" is rendered as "indítóikonokhoz" (launcher icons) instead of the consistent term for shortcuts.
    - Current: `Hozzáadva az indítóikonokhoz.`
    - Source: `Added to shortcuts!`
    - Suggest: `Hozzáadva a parancsikonokhoz.`
    - Other Focus strings use "parancsikon" for shortcuts; "indítóikon" is inconsistent terminology on the same surface.
- `tab_crash_report_headline` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Sorry." is translated in first person singular ("Sajnálom"), while the app speaks as "we" in the same string set.
    - Current: `Sajnálom. Probléma van ezzel a lapon.`
    - Source: `Sorry. We’re having a problem with this tab.`
    - Suggest: `Sajnáljuk. Probléma van ezzel a lappal.`
    - Source "We’re having a problem with this tab" uses first person plural; also "probléma van ezzel a lapon" should be "ezzel a lappal" (problem with the tab, not on the tab).
- `trackers_count_note` — `mozilla-mobile/focus-android/app/src/main/res/values-hu/strings.xml` — "Trackers" is rendered as "nyomkövetők" here while the neighbouring string uses "követők".
    - Current: `Blokkolt nyomkövetők %s óta`
    - Source: `Trackers blocked since %s`
    - Suggest: `Blokkolt követők %s óta`
    - The adjacent string trackers_and_scripts translates "Trackers" as "követők"; using "nyomkövetők" on the same tracking-protection surface is inconsistent terminology.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/hu/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

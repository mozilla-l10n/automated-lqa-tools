# Focus for Android l10n QA — id

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 241 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for id: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| Strings | 241 |
| Missing strings | 9 |
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

**9 strings** are not translated yet, concentrated in:

- `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — 9

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 11, `straight-double` 5 | _mixed_ |
| ellipsis | `char` 21 | **char** |
| dash | `em` 3 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (15)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 7 |
| 3 | Degraded language (grammar, spelling, terminology) | 8 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "for more security" is mistranslated as "untuk keandalan keamanan" (for security reliability).
    - Current: `untuk keandalan keamanan`
    - Source: `%1$s tries to use an HTTPS connection whenever possible for more security. <a href="%2$s">Learn more{ </a> } { <br/> }{ <br/> } Change this setting in Settings > Privacy &amp; Security > Security.`
    - Suggest: `untuk keamanan lebih`
    - The source means increased security, not "security reliability".
- `errorpage_httpsonly_title2` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "This site" is translated as "Laman ini" (this page) instead of "Situs ini".
    - Current: `Laman ini tidak mendukung HTTPS`
    - Source: `This site doesn’t support HTTPS`
    - Suggest: `Situs ini tidak mendukung HTTPS`
    - The source says "site", and elsewhere in the same file "site" is rendered as "situs" (e.g. "Perlindungan DINONAKTIFKAN untuk situs ini"); "laman" is used for "page".
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "continuing could be risky" is rendered as an instruction not to continue.
    - Current: `dan sebaiknya Anda tidak melanjutkan`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `dan melanjutkan bisa berisiko`
    - The source states that continuing could be risky, not that the user should not continue.
- `onboarding_second_screen_subtitle_two` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Mistranslation: "Make Focus your default" became "Make Focus the default protection of your data".
    - Current: `Jadikan %1$s sebagai perlindungan baku data Anda dengan setiap tautan yang Anda buka.`
    - Source: `Make %1$s your default to protect your data with every link you open.`
    - Suggest: `Jadikan %1$s peramban baku Anda untuk melindungi data Anda pada setiap tautan yang Anda buka.`
    - The source asks the user to set the app as their default (browser) in order to protect data; the target says to make the app the "default protection of your data", which changes the meaning.
- `phone_feature_blocked_step_feature` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "Toggle ... to ON" is rendered as "Aktifkan/Nonaktifkan" (enable/disable), losing the instruction to turn the permission ON.
    - Current: `3. Aktifkan/Nonaktifkan { <b> }%1$s{ </b> }`
    - Source: `3. Toggle { <b> }%1$s{ </b> } to ON`
    - Suggest: `3. Aktifkan { <b> }%1$s{ </b> }`
    - The source tells the user to switch the permission to ON; the translation offers an ambiguous enable/disable action.
- `preference_exceptions_description` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "these websites" is rendered as "situs ini" dropping the plural/web sense.
    - Current: `Pemblokiran Konten untuk situs ini`
    - Source: `You have disabled content blocking for these websites.`
    - Suggest: `pemblokiran konten untuk situs web ini`
    - Source says "these websites"; target says "this site" and capitalizes "Pemblokiran Konten" unlike the source's lowercase "content blocking".
- `preference_general_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Translation adds "tab" which is not in the source "Default browser, language".
    - Current: `Peramban, tab, dan bahasa baku`
    - Source: `Default browser, language`
    - Suggest: `Peramban baku, bahasa`
    - Source lists only two items: default browser and language. The target adds "tab" and restructures the list, stating content not in the source.
- `promote_search_widget_dialog_picture_content_description` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — "Search widget" (a noun phrase naming the widget) is translated as the imperative "Cari widget" ("Search for a widget").
    - Current: `Cari widget`
    - Source: `Search widget`
    - Suggest: `Widget pencarian`
    - The developer comment says this describes a picture of the search widget; the source is a noun phrase, not a command to search for widgets.
- `search_add_manually_example` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — The example domain example.com was altered to contoh.id.
    - Current: `contoh.id/search/?q=%s`
    - Source: `Example: example.com/search/?q=%s`
    - Suggest: `example.com/search/?q=%s`
    - example.com is a reserved example domain used as a literal URL format sample; contoh.id is a real, unrelated domain and should not replace it.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Duplicated word "menyamar menyamar" and missing preposition in the Indonesian sentence.
    - Current: `Seseorang mungkin berusaha menyamar menyamar laman ini`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `Seseorang mungkin berusaha menyamar sebagai situs ini`
    - Source reads "Someone could be trying to impersonate the site"; the target repeats "menyamar" and lacks the preposition, producing ungrammatical text.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — English plural "URLs" left in Indonesian text where plurality is not marked with -s.
    - Current: `Hapus URLs ubahsuai`
    - Source: `Remove custom URLs`
    - Suggest: `Hapus URL ubahsuai`
    - Indonesian does not form plurals with -s; other strings in the same screen use "URL ubahsuai".
- `preference_autocomplete_user_list_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Missing "agar" makes the sentence read "Enable %s" instead of "Enable to have %s autocomplete...".
    - Current: `Aktifkan %s melengkapi otomatis URL favorit Anda.`
    - Source: `Enable to have %s autocomplete your favorite URLs.`
    - Suggest: `Aktifkan agar %s melengkapi otomatis URL favorit Anda.`
    - The parallel string preference_autocomplete_topsite_summary2 correctly uses "Aktifkan agar %s melengkapi otomatis..."; without "agar" the clause is ungrammatical.

### D. Terminology, register & consistency

- `analytics` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Tracker category "Analytics" rendered with the adjective "Analitis" instead of the noun "Analitik".
    - Current: `Analitis`
    - Source: `Analytics`
    - Suggest: `Analitik`
    - The string is a tracker category name (a noun, parallel to "Periklanan", "Konten"); "analitis" is the adjective "analytical".
- `cfr_for_toolbar_shield_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Informal second-person "memata-mataimu" breaks the formal "Anda" address used elsewhere in the app.
    - Current: `memata-mataimu`
    - Source: `Got ‘em! We stopped this site from spying on you. Tap the shield any time to see what we’re blocking.`
    - Suggest: `memata-matai Anda`
    - Other Focus strings (e.g. cfr_for_start_browsing, biometric_prompt_subtitle) consistently use the formal "Anda"; the -mu clitic is an informal register violation.
- `preference_category_search` — `mozilla-mobile/focus-android/app/src/main/res/values-in/strings.xml` — Category heading "Search" translated as the verb "Cari" instead of the noun "Pencarian".
    - Current: `Cari`
    - Source: `Search`
    - Suggest: `Pencarian`
    - This is a preference category title (a noun), so the noun form "Pencarian" is required rather than the imperative verb "Cari".

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/id/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

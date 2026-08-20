# Firefox l10n QA — it

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `2ecee41489f8` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `2ecee41489f8` |
| **Previous run** | 2026-08-20 @ `11bf53751a76` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,908 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (6)

- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — "Department" as an administrative division is rendered "Reparto" (store/hospital department).
  - Current: `Reparto`
  - Source: `Department`
  - Suggest: `Dipartimento`
  - The developer comment states this is the administrative division used in countries like Nicaragua and Colombia; the Italian name for that division is "dipartimento". "Reparto" means a section of a shop or hospital ward and names the wrong thing in an address form.
- `ip_protection_locations_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Dangling feminine participle with no subject: "Passata alla posizione consigliata."
  - Current: `Passata alla posizione consigliata.`
  - Source: `Switched to the recommended location.`
  - Suggest: `Si è passati alla posizione consigliata.`
  - Source is "Switched to the recommended location." In Italian a bare "Passata" has no antecedent to agree with, making the sentence ungrammatical as a standalone card description.
- `open_in_app_cfr_info_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Says the app must be set as default browser; the source is about opening links in apps automatically.
  - Current: `È possibile impostare %1$s come browser predefinito per aprire i link nelle app.`
  - Source: `You can set %1$s to automatically open links in apps.`
  - Suggest: `Puoi impostare %1$s in modo che apra automaticamente i link nelle app.`
  - Source: "You can set %1$s to automatically open links in apps." The CFR points to the "Open links in apps" setting, not to the default-browser setting; the Italian introduces "come browser predefinito" and drops "automatically", pointing the user at a different feature.
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Wrong article: "La schede" instead of "Le schede" (plural feminine).
  - Current: `La schede che non visualizzi da due settimane vengono spostate nella sezione Inattive.`
  - Source: `Tabs you haven’t viewed for two weeks get moved to the inactive section.`
  - Suggest: `Le schede che non visualizzi da due settimane vengono spostate nella sezione Inattive.`
  - "schede" is plural, so the article must be "Le"; "La schede" is ungrammatical and visible in the Tabs settings screen.
- `tab_manager_empty_private_tabs_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Adds "per questa finestra", a concept absent from the source and from the Android UI.
  - Current: `%1$s non salverà alcuna cronologia o cookie per questa finestra. I segnalibri aggiunti verranno comunque conservati sul dispositivo.`
  - Source: `%1$s won’t remember any of your history or cookies, but new bookmarks will be saved.`
  - Suggest: `%1$s non salverà la cronologia o i cookie, ma i nuovi segnalibri verranno conservati.`
  - Source: "%1$s won’t remember any of your history or cookies, but new bookmarks will be saved." The scope is private browsing, not a "window"; Android has no browser windows, so the added qualifier misstates what is not saved.
- `tabs_header_tab_group_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — Past participle not agreeing with the plural noun in the plural variant.
  - Current: `Aperto %1$d gruppi di schede. Tocca per cambiare scheda.`
  - Source: `{$quantity ->} [one] %1$d tab group open. Tap to switch tabs. [other] %1$d tab groups open. Tap to switch tabs.`
  - Suggest: `Aperti %1$d gruppi di schede. Tocca per cambiare scheda.`
  - "gruppi" is masculine plural, so the participle must be "Aperti"; the singular item correctly uses "Aperto". This string is read aloud by screen readers.

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
| Files | 43 |
| Strings | 2,908 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 25 | **curly-double** |
| apostrophe | `typographic` 173 | **typographic** |
| ellipsis | `char` 24 | **char** |
| dash | `em` 2 | **em** |
| register | `informal` 89, `formal` 4 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (1)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 1 |
| 2 | Wrong content (says something other than the English) | 0 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

_Nothing in this category._

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

_Nothing in this category._

### E. Typography, punctuation & spacing

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — Message quotes a button label that does not match the actual button text
  - Current: `Selezionare “Riprova” per passare alla modalità in linea e ricaricare la pagina.`
  - Source: `{ <p> }The browser is operating in its offline mode and cannot connect to the requested item.{ </p> } { <ul> } { <li> }Is the device connected to an active network?{ </li> } { <li> }Press “Try Again” to switch to online…`
  - Suggest: `Selezionare “Riprovare” per passare alla modalità in linea e ricaricare la pagina.`
  - The button on the error page (mozac_browser_errorpages_page_refresh) is labelled "Riprovare"; the message tells the user to press "Riprova", so the quoted label does not exist on screen.

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (12)

- `mozac_browser_errorpages_offline_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_addons_status_unsigned` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_addons_updater_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `mozac_feature_contextmenu_open_image_in_new_tab` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `addresses_department` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `ip_protection_locations_unavailable_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `open_in_app_cfr_info_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `preferences_inactive_tabs_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `tab_manager_empty_private_tabs_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `tabs_header_tab_group_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `content_description_trackers_blocked` — `mozilla-mobile/focus-android/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20
- `external_app_prompt_no_app_title` — `mozilla-mobile/focus-android/app/src/main/res/values-it/strings.xml` — fixed 2026-08-20

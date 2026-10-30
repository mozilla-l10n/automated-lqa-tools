# Focus for Android l10n QA — cs

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

Also for cs: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `german-double` 20 | **german-double** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 1, `en` 4 | **en** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (18)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 11 |
| 3 | Degraded language (grammar, spelling, terminology) | 7 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `menu_about` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "About" (about the app) is translated as "O nás" (About us).
    - Current: `O nás`
    - Source: `About`
    - Suggest: `O aplikaci`
    - The menu item opens information about the application, not about the organisation.
- `menu_custom_tab_branding` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "Powered by %1$s" is rendered as "Pohání %1$s", which reverses the subject and reads as "%1$s powers (something)".
    - Current: `Pohání %1$s`
    - Source: `Powered by %1$s`
    - Suggest: `Používá technologii %1$s`
    - The source means the tab is powered by the app; the Czech word order makes the app the actor of an incomplete sentence and loses the passive meaning.
- `mozac_browser_errorpages_security_bad_cert_message` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Czech adds a clause not present in the source ("a můžete to zkusit znovu později").
    - Current: `je možná chyba jenom dočasná, a můžete to zkusit znovu později`
    - Source: `This could be a problem with the server’s configuration, or it could be someone trying to impersonate the server. { <br/> }{ <br/> } If you’ve connected to this server successfully in the past, the error may be temporar…`
    - Suggest: `je možné, že je chyba jen dočasná`
    - The source only says the error may be temporary; the added suggestion to retry later is not in the en-US text.
- `notification_browsing_session_channel_description` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Translation says notifications of app %1$s let you erase history, while the source says notifications let you erase your %1$s session.
    - Current: `Oznámení aplikace %1$s vám umožní smazat historii jedním klepnutím.`
    - Source: `Notifications let you erase your %1$s session with a tap. You don’t need to open the app or see what’s running in your browser.`
    - Suggest: `Oznámení vám umožní smazat relaci prohlížeče %1$s jediným klepnutím.`
    - The placeholder in the source modifies "session" (your %1$s session), not "notifications"; the Czech reassigns the app name and replaces "session" with "history".
- `preference_autocomplete_add_example2` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — The example domain mozilla.org was changed to mozilla.cz, altering the referenced domain.
    - Current: `Příklad: mozilla.cz`
    - Source: `Example: mozilla.org`
    - Suggest: `Příklad: mozilla.org`
    - Source uses the domain mozilla.org as the example; mozilla.cz is a different domain and the sibling string preference_autocomplete_add_example keeps example.com unchanged.
- `preference_autocomplete_topsite_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Translation omits "in the address bar" from the source.
    - Current: `Po zapnutí bude %s našeptávat více než 450 populárních URL adres.`
    - Source: `Enable to have %s autocomplete over 450 popular URLs in the address bar.`
    - Suggest: `Po zapnutí bude %s v adresním řádku našeptávat více než 450 populárních URL adres.`
    - The source specifies autocompletion happens "in the address bar"; this information is missing in the Czech string.
- `preference_block_autoplay_audio_only` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "Block audio only" is translated as "Block autoplay of sounds", losing the "only" contrast with the audio+video option.
    - Current: `Blokovat automatické přehrávání zvuků`
    - Source: `Block audio only`
    - Suggest: `Blokovat pouze zvuk`
    - The source contrasts "Block audio only" with "Block audio and video"; the Czech drops "only", so the two options no longer differ in meaning as intended.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Translation drops "only what we need to provide" and "for everyone", changing the meaning.
    - Current: `Mozilla sbírá jenom ty informace, které potřebuje pro další vylepšování aplikace %1$s.`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `Mozilla se snaží sbírat jenom ty informace, které potřebuje k poskytování a vylepšování aplikace %1$s pro všechny.`
    - Source says Mozilla "strives to collect only what we need to provide and improve %1$s for everyone"; the Czech omits "strives", "provide" and "for everyone".
- `preference_privacy_and_security_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "data choices" translated as "možnosti hlášení" (reporting options).
    - Current: `Sledování, cookies, možnosti hlášení`
    - Source: `Tracking, cookies, data choices`
    - Suggest: `Sledování, cookies, nakládání s daty`
    - The source refers to choices about data collection, not to reports.
- `preference_privacy_block_ads` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "Block ad trackers" is rendered as "Blokovat sledující reklamy" (block tracking ads) instead of ad trackers.
    - Current: `Blokovat sledující reklamy`
    - Source: `Block ad trackers`
    - Suggest: `Blokovat reklamní sledovací prvky`
    - The source blocks trackers used by ads, not the ads themselves; sibling strings render "trackers" as "sledovací prvky".
- `search_add_manually_string` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "Search string to use" is rendered as an imperative "Use search string" instead of a noun label.
    - Current: `Použít řetězec pro vyhledávání`
    - Source: `Search string to use`
    - Suggest: `Řetězec pro vyhledávání`
    - The source is a field label (noun phrase) naming the search string to be used, not a command to use it.

### C. Grammar, agreement & spelling

- `biometric_auth_image_description` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Content description uses accusative case instead of nominative for "Fingerprint icon".
    - Current: `Ikonu otisku prstu`
    - Source: `Fingerprint icon`
    - Suggest: `Ikona otisku prstu`
    - The source is a noun phrase label "Fingerprint icon"; Czech should use nominative "Ikona otisku prstu", not accusative "Ikonu".
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Misspelling "pokračovaní" and missing reflexive/preposition in "vydávat za zmiňovaný server"; source also says "site", not "server".
    - Current: `Někdo se může snažit vydávat za zmiňovaný server a pokračovaní může být riskantní.`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `Někdo se může snažit vydávat za tento server a pokračování může být riskantní.`
    - "pokračovaní" is a spelling error (correct: "pokračování"); "zmiňovaný" has no counterpart in the source.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Misspelling "shromážďování" and missing comma before "jako".
    - Current: `Slouží k shromážďování, analýze a měření aktivit jako je klepnutí nebo posouvání`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `Slouží ke shromažďování, analýze a měření aktivit, jako je klepnutí nebo posouvání`
    - Correct Czech spelling is "shromažďování"; a comma is required before the comparative clause "jako je…".
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Wrong abbreviation for the European Union: "EÚ" is Slovak, Czech uses "EU".
    - Current: `(EÚ)`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `(EU)`
    - The source reads "Regulation (EU) 2024/1183"; the Czech abbreviation of Evropská unie is "EU", not the Slovak "EÚ".

### D. Terminology, register & consistency

- `preference_category_search` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — Preference category title "Search" rendered as a verb ("Hledat") instead of a noun heading.
    - Current: `Hledat`
    - Source: `Search`
    - Suggest: `Vyhledávání`
    - This is a settings category heading alongside nouns like "Výkon", "Soukromí", "Zabezpečení"; the imperative verb form is inconsistent and wrong for a category label.
- `preference_privacy_block_analytics` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "analytic trackers" translated as "analytické prvky", dropping the "tracker" term used consistently in sibling strings.
    - Current: `Blokovat analytické prvky`
    - Source: `Block analytic trackers`
    - Suggest: `Blokovat analytické sledovací prvky`
    - Neighbouring settings render "trackers" as "sledovací prvky"; here the tracking notion is lost.
- `preference_site_permissions` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — "Site permissions" rendered as "Oprávnění serverů" instead of the site terminology used elsewhere.
    - Current: `Oprávnění serverů`
    - Source: `Site permissions`
    - Suggest: `Oprávnění stránek`
    - Elsewhere in this file "sites" is consistently translated as "stránky" (e.g. "Blokovat potenciálně nebezpečné a podvodné stránky"); "servery" means servers.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/cs/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (4)

- `contextmenu_erased_images_note2` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — fixed 2026-10-18
- `errorpage_httpsonly_message2` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — fixed 2026-10-18
- `preference_remote_debugging` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — fixed 2026-10-18
- `preference_switch_autocomplete_user_list` — `mozilla-mobile/focus-android/app/src/main/res/values-cs/strings.xml` — fixed 2026-10-18

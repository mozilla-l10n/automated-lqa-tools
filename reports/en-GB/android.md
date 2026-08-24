# Android l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `85004d56fca7` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `85004d56fca7` |
| **Previous run** | 2026-08-24 @ `85004d56fca7` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 2,911 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-GB: [firefox](firefox.md) · [firefox_ios](firefox_ios.md)

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
| Files | 43 |
| Strings | 2,911 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 15, `curly-single` 1 | **curly-double** |
| apostrophe | `typographic` 168 | **typographic** |
| ellipsis | `char` 21 | **char** |
| dash | `em` 4 | **em** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (7)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 2 |
| 3 | Degraded language (grammar, spelling, terminology) | 5 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `addresses_state` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "State" has been changed to "County", which is a different address field and duplicates the separate addresses_county label.
    - Current: `County`
    - Source: `State`
    - Suggest: `State`
    - The developer comment says this is the header for the subregion of an address when "state" should be used; there is already a distinct addresses_county string for county. "State" is understood in en-GB and must not be replaced with a different administrative division.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `bookmark_empty_list_guest_cta` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "sync" is the Firefox Sync feature name and should not be expanded to "synchronise".
    - Current: `Sign in to synchronise`
    - Source: `Sign in to sync`
    - Suggest: `Sign in to sync`
    - The source refers to the Sync feature (sync authentication per the developer comment); "sync" is standard in en-GB Firefox UI and is not an Americanism requiring adaptation.
- `delete_history_prompt_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "synced" was expanded to "synchronised", departing from the Sync feature terminology used elsewhere in the locale.
    - Current: `synchronised`
    - Source: `Removes history (including history synced from other devices)`
    - Suggest: `synced`
    - "Synced" is the product term tied to Firefox Sync and is used consistently in en-GB; "synchronised" is not a required British adaptation and introduces terminology inconsistency.
- `nova_onboarding_sync_button` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Start syncing" was expanded to "Start synchronising", which is not a British-English adaptation and diverges from the product term "sync" used elsewhere.
    - Current: `Start synchronising`
    - Source: `Start syncing`
    - Suggest: `Start syncing`
    - "Sync"/"syncing" is the established Firefox feature term (Firefox Sync) and is identical in en-GB; there is no British spelling requirement to replace it with "synchronising".
- `onboarding_redesign_sync_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Start syncing" was expanded to "Start synchronising", inconsistent with the locale's use of "Sync"/"syncing" elsewhere.
    - Current: `Start synchronising`
    - Source: `Start syncing`
    - Suggest: `Start syncing`
    - en-GB keeps the product term "Sync" untranslated in neighbouring strings ("Sync is on", "Sync everywhere you use Firefox"); changing the verb to "synchronising" here is an over-correction and inconsistent.
- `tab_manager_empty_synced_tabs_page_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "synced tabs" is rendered as "synchronised tabs", departing from the product term used elsewhere in the locale.
    - Current: `Sign in to manage synchronised tabs from all your devices.`
    - Source: `Sign in to manage synced tabs from all your devices.`
    - Suggest: `Sign in to manage synced tabs from all your devices.`
    - "Synced tabs" is the established Firefox feature name (see the sibling synced tabs strings, which keep "synced"); expanding it to "synchronised" is an unnecessary and inconsistent change, not a British-spelling requirement.
- `tabs_header_synced_tabs_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Synced" was changed to "Synchronised", inconsistent with the Sync feature terminology used elsewhere in en-GB.
    - Current: `Synchronised Tabs Open: %1$s. Tap to switch tabs.`
    - Source: `Synced Tabs Open: %1$s. Tap to switch tabs.`
    - Suggest: `Synced Tabs Open: %1$s. Tap to switch tabs.`
    - "Synced" refers to the Firefox Sync feature and is the standard term in en-GB Firefox; expanding it to "Synchronised" is an over-correction that breaks consistency with other synced-tabs strings.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (3)

- `cookie_banner_exception_panel_description_state_on_for_site` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "shopping baskets" is the house form here; reviewed and accepted
- `mozac_feature_prompts_no_more_dialogs` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-en-rGB/strings.xml` — "dialogues" is the house form here; reviewed and accepted
- `share_hiscore` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-en-rGB/strings.xml` — "hi-score" is the house form here; reviewed and accepted

_One line each in `locales/en-GB/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (58)

- **`en-GB-backwards-forwards`** (11) — "Backwards" and "Forwards" are the en-GB house forms for the en-US "Back" and "Forward", in navigation labels and accessibility descriptions alike. See conventions.md.
    - `add_login_navigate_back_button_content_description`, `bookmark_navigate_back_button_content_description`, `debug_drawer_back_button_content_description`, `edit_login_navigate_back_button_content_description`, `ip_protection_locations_navigate_back_button_content_description`, `ip_protection_navigate_back_button_content_description`, `login_details_navigate_back_button_content_description`, `stories_back_button_content_description`, `content_description_back`, `content_description_forward` …and 1 more
- **`en-GB-post-code`** (1) — "Post Code" is the deliberate en-GB rendering of the en-US "Postal Code"; "Postcode" must not be suggested in its place. See conventions.md.
    - `addresses_postal_code`
- **`en-GB-web-site-two-words`** (46) — "web site" / "web sites" is the en-GB house form; a suggestion to close it up to the en-US "website" must never be accepted. See conventions.md.
    - `mozac_browser_errorpages_content_crashed_message`, `mozac_browser_errorpages_corrupted_content_message`, `mozac_browser_errorpages_invalid_content_encoding_message`, `mozac_browser_errorpages_security_bad_cert_techInfo`, `mozac_browser_errorpages_security_bad_hsts_cert_message`, `mozac_browser_errorpages_security_bad_hsts_cert_title`, `mozac_browser_errorpages_security_ssl_message`, `mozac_browser_errorpages_unsafe_content_type_message`, `mozac_feature_addons_permissions_all_urls_description`, `mozac_feature_addons_permissions_all_urls_description_for_update` …and 36 more

_Suppressions live in `locales/en-GB/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

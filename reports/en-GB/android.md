# Android l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-08-24 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `e8622a909368` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `e8622a909368` |
| **Previous run** | 2026-08-22 @ `eda9938ab8c3` |
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

## 3. Open findings (68)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 7 |
| 3 | Degraded language (grammar, spelling, terminology) | 61 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `add_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Navigate back" was changed to "Navigate backwards", altering the meaning of the back-navigation control description with no British-English justification.
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - The en-US source is "Navigate back", describing the back button. "Navigate backwards" is not a British variant form and changes the wording of a screen-reader description unnecessarily; elsewhere in the locale (e.g. action_bar_up_description) the source wording is kept.
- `addresses_state` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "State" has been changed to "County", which is a different address field and duplicates the separate addresses_county label.
    - Current: `County`
    - Source: `State`
    - Suggest: `State`
    - The developer comment says this is the header for the subregion of an address when "state" should be used; there is already a distinct addresses_county string for county. "State" is understood in en-GB and must not be replaced with a different administrative division.
- `debug_drawer_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — Content description reworded from "Navigate back" to "Navigate backwards" without any en-GB reason.
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - The en-US source is "Navigate back"; "back" is equally standard in British English, so the change is an unnecessary and inconsistent deviation from the source wording used for back-navigation content descriptions.
- `edit_login_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Navigate back" was changed to "Navigate backwards", diverging from the source and from the identical en-GB string etp_back_button_content_description.
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - The en-US source is "Navigate back"; British English requires no change here, and the sibling string etp_back_button_content_description keeps "Navigate back", so this is an inconsistent, unnecessary alteration.
- `login_details_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — Content description changed from "Navigate back" to "Navigate backwards" without any en-GB reason.
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - The en-US source is "Navigate back"; "back" is equally standard in British English, and the related string logins_navigate_back_button_content_description uses "Back". The alteration is an unwarranted change of wording.
- `stories_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — The content description for the back button was changed from "Navigate back" to "Navigate backwards", which is not a British-English requirement and alters the standard accessibility label.
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - The en-US source is "Navigate back"; no en-GB convention requires "backwards" here, and the change makes the screen-reader label inconsistent with the standard control name.
- `go_back` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "Go back" was changed to "Go backwards", altering the meaning of the navigate-back button's content description with no en-GB requirement.
    - Current: `Go backwards`
    - Source: `Go back`
    - Suggest: `Go back`
    - The source "Go back" describes navigating back in history; "Go backwards" is a directional phrase and is not standard British usage for this control. No en-GB convention requires the change.

### C. Grammar, agreement & spelling

_Nothing in this category._

### D. Terminology, register & consistency

- `mozac_browser_errorpages_content_crashed_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-en-rGB/strings.xml` — "website" was changed to the outdated two-word form "web site", inconsistent with the rest of the locale.
    - Current: `Please contact the web site owners to inform them of this problem.`
    - Source: `{ <p> }The page you are trying to view cannot be shown because an error in the data transmission was detected.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } { </ul> }`
    - Suggest: `Please contact the website owners to inform them of this problem.`
    - The en-US source says "website"; en-GB uses "website" elsewhere (e.g. connection failure, HTTPS-only strings refer to websites). "web site" is not a British-English adaptation.
- `mozac_browser_errorpages_corrupted_content_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-en-rGB/strings.xml` — "website" was changed to the outdated two-word form "web site".
    - Current: `Please contact the web site owners to inform them of this problem.`
    - Source: `{ <p> }The page you are trying to view cannot be shown because an error in the data transmission was detected.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } { </ul> }`
    - Suggest: `Please contact the website owners to inform them of this problem.`
    - The en-US source says "website" and en-GB does not require splitting it into two words; this is an unnecessary and inconsistent alteration.
- `mozac_browser_errorpages_invalid_content_encoding_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-en-rGB/strings.xml` — "website" was changed to the outdated two-word form "web site".
    - Current: `Please contact the web site owners to inform them of this problem.`
    - Source: `{ <p> }The page you are trying to view cannot be shown because it uses an invalid or unsupported form of compression.{ </p> } { <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } {…`
    - Suggest: `Please contact the website owners to inform them of this problem.`
    - The en-US source says "website"; en-GB consistently uses "website" elsewhere in this file, so this deviation is inconsistent.
- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-en-rGB/strings.xml` — "Websites" was changed to the outdated two-word form "Web sites", which is not a British/American spelling difference.
    - Current: `Web sites prove their identity via certificates.`
    - Source: `{ <label> }Someone could be trying to impersonate the site and you should not continue.{ </label> } { <br> }{ <br> } { <label> }Websites prove their identity via certificates. %1$s does not trust { <b> }%2$s{ </b> } bec…`
    - Suggest: `Websites prove their identity via certificates.`
    - en-US source uses "Websites"; en-GB uses the same single-word modern form and other strings in this file keep "website" (e.g. unknown_host, safe browsing strings). The split form is an unnecessary and inconsistent alteration.
- `mozac_browser_errorpages_security_bad_hsts_cert_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-en-rGB/strings.xml` — "website" rendered as "web site" three times, inconsistent with the rest of the locale.
    - Current: `because this web site requires a secure connection.{ </li> } { <li> }The issue is most likely with the web site, and there is nothing you can do to resolve it.{ </li> } { <li> }You can notify the web site’s administrato…`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because this website requires a secure connection.{ </li> } { <li> }The issue is most likely with the website, and there is nothing you can do to resolve…`
    - Suggest: `because this website requires a secure connection.{ </li> } { <li> }The issue is most likely with the website, and there is nothing you can do to resolve it.{ </li> } { <li> }You can notify the website’s administrator a…`
    - The source uses "website"; this is not a US/GB spelling difference, and other en-GB strings in this same file retain "website".
- `mozac_browser_errorpages_security_bad_hsts_cert_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-en-rGB/strings.xml` — "This website" changed to "This web site", inconsistent with other en-GB strings in the file.
    - Current: `This web site requires a secure connection.`
    - Source: `This website requires a secure connection.`
    - Suggest: `This website requires a secure connection.`
    - The source reads "website"; splitting it is not an en-GB convention and conflicts with the "website" form used elsewhere in this locale's file.
- `mozac_browser_errorpages_security_ssl_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-en-rGB/strings.xml` — "website owners" changed to "web site owners", inconsistent with the rest of the locale.
    - Current: `Please contact the web site owners to inform them of this problem.`
    - Source: `{ <ul> } { <li> }The page you are trying to view cannot be shown because the authenticity of the received data could not be verified.{ </li> } { <li> }Please contact the website owners to inform them of this problem.{ <…`
    - Suggest: `Please contact the website owners to inform them of this problem.`
    - The source uses "website"; the split spelling is not a British variant requirement and is inconsistent with other strings in this file that keep "website".
- `mozac_browser_errorpages_unsafe_content_type_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-en-rGB/strings.xml` — "website" was changed to the non-standard two-word form "web site".
    - Current: `web site owners`
    - Source: `{ <ul> } { <li> }Please contact the website owners to inform them of this problem.{ </li> } { </ul> }`
    - Suggest: `website owners`
    - The en-US source says "website"; en-GB also uses the single word "website" and elsewhere in the locale. "web site" is an unnecessary and inconsistent alteration.
- `mozac_feature_addons_permissions_all_urls_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-en-rGB/strings.xml` — "websites" has been changed to "web sites", which is not a British English convention and is inconsistent with the rest of the locale.
    - Current: `Access your data for all web sites`
    - Source: `Access your data for all websites`
    - Suggest: `Access your data for all websites`
    - British English uses "website" as one word, just like en-US; there is no en-GB rule requiring "web site", and other en-GB strings keep "website".
- `mozac_feature_addons_permissions_all_urls_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-en-rGB/strings.xml` — "websites" rendered as "web sites" without any en-GB justification.
    - Current: `Access your data for all web sites.`
    - Source: `Access your data for all websites.`
    - Suggest: `Access your data for all websites.`
    - en-GB does not split "website" into two words; this is an unwarranted departure from the source and from the rest of the locale.
- `mozac_feature_addons_permissions_data_collection_websiteActivity_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-en-rGB/strings.xml` — "website activity" changed to "web site activity" with no en-GB basis.
    - Current: `Share web site activity with extension developer`
    - Source: `Share website activity with extension developer`
    - Suggest: `Share website activity with extension developer`
    - The permission name is websiteActivity; en-GB spells "website" as one word, matching the source.
- `mozac_feature_addons_permissions_data_collection_websiteActivity_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-en-rGB/strings.xml` — "website activity" changed to "web site activity" with no en-GB basis.
    - Current: `web site activity`
    - Source: `website activity`
    - Suggest: `website activity`
    - en-GB uses "website" as a single word; splitting it is an unjustified change from the source.
- `mozac_feature_addons_permissions_data_collection_websiteContent_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-en-rGB/strings.xml` — "website" was needlessly split into "web site", which is not the en-GB house form used elsewhere in the locale.
    - Current: `Share web site content with extension developer`
    - Source: `Share website content with extension developer`
    - Suggest: `Share website content with extension developer`
    - en-GB uses "website" as one word, consistent with other strings in this locale (e.g. "sites"/"website" usages); "web site" is an unwarranted deviation from the source term.
- `mozac_feature_addons_permissions_data_collection_websiteContent_short_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-en-rGB/strings.xml` — "website" rendered as "web site", inconsistent with the locale's one-word form.
    - Current: `web site content`
    - Source: `website content`
    - Suggest: `website content`
    - The source term is "website content"; en-GB does not split "website" into two words, so this is an unnecessary and inconsistent deviation.
- `mozac_feature_prompts_no_more_dialogs` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-en-rGB/strings.xml` — "dialogs" in the UI/technical sense was changed to "dialogues", which is an over-correction of a technical term.
    - Current: `Prevent this page from creating additional dialogues`
    - Source: `Prevent this page from creating additional dialogs`
    - Suggest: `Prevent this page from creating additional dialogs`
    - In software UI, "dialog" (a dialog box) is the standard term in en-GB as well; "dialogue" means a conversation. Elsewhere in this locale the developer comments and related strings use "dialog" (e.g. month chooser dialog, time picker dialog).
- `mozac_feature_pwa_default_shortcut_label` — `mozilla-mobile/android-components/components/feature/pwa/src/main/res/values-en-rGB/strings.xml` — "Website" was needlessly split into "Web site", which is not an en-GB convention and is inconsistent with the rest of the locale.
    - Current: `Web site`
    - Source: `Website`
    - Suggest: `Website`
    - The en-US source reads "Website"; British English uses the same closed compound. Splitting it is an over-correction that changes the term for no locale reason.
- `mozac_feature_sitepermissions_notification_permission_rationale_dialog_message` — `mozilla-mobile/android-components/components/feature/sitepermissions/src/main/res/values-en-rGB/strings.xml` — "website" was changed to "web site", which is not an en-GB convention and is inconsistent with the rest of the locale.
    - Current: `web site`
    - Source: `You’ll need to allow notifications in %1$s to receive them from this website.`
    - Suggest: `website`
    - en-US source uses "website", the standard form in en-GB as well; the tree uses "website" elsewhere (e.g. developer comments and other site permission strings), so splitting it into "web site" is an unnecessary and inconsistent alteration.
- `share_hiscore` — `mozilla-mobile/fenix/app/longfox/src/main/res/values-en-rGB/strings.xml` — "hiscore" was hyphenated to "hi-score", diverging from the term used unchanged in the related strings and from the developer comment.
    - Current: `Share hi-score`
    - Source: `Share hiscore`
    - Suggest: `Share hiscore`
    - The developer comment states hiscore is an abbreviation for "Highest Score"; the sibling string `hiscore` keeps "HISCORE" unchanged, so hyphenating here is an inconsistent, unnecessary alteration with no en-GB rule requiring it.
- `add_to_homescreen_continue` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "website" was split into "web site", which is not standard British usage and is inconsistent with the rest of the locale.
    - Current: `Continue to web site`
    - Source: `Continue to website`
    - Suggest: `Continue to website`
    - British English uses "website" as one word, exactly as in the en-US source; "web site" is an unwarranted change.
- `add_to_homescreen_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "website" was split into "web site", which is not standard British usage.
    - Current: `add this web site to`
    - Source: `You can easily add this website to your device’s Home screen to have instant access and browse faster with an app-like experience.`
    - Suggest: `add this website to`
    - The en-US source reads "website"; British English also writes it as one word, so this alteration degrades the language and is inconsistent.
- `addons_permissions_allow_for_all_sites_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "website" was split into "web site", which is not a British spelling difference and is inconsistent with the rest of the locale.
    - Current: `every web site`
    - Source: `If you trust this extension, you can give it permission on every website.`
    - Suggest: `every website`
    - en-GB does not use "web site" as a variant spelling; the source's "website" is standard in British English and used elsewhere in the locale.
- `bookmark_empty_list_guest_cta` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "sync" is the Firefox Sync feature name and should not be expanded to "synchronise".
    - Current: `Sign in to synchronise`
    - Source: `Sign in to sync`
    - Suggest: `Sign in to sync`
    - The source refers to the Sync feature (sync authentication per the developer comment); "sync" is standard in en-GB Firefox UI and is not an Americanism requiring adaptation.
- `bookmark_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Navigate back" was needlessly reworded to "Navigate backwards".
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - "Navigate back" is equally idiomatic in en-GB; the change departs from the source wording used elsewhere for back-button content descriptions with no British-English justification.
- `clear_site_data_dialog_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was needlessly split into "web sites", which is not the en-GB house form.
    - Current: `might log you out of web sites`
    - Source: `Removing cookies and site data for { <b> }%s{ </b> } might log you out of websites and clear shopping carts.`
    - Suggest: `might log you out of websites`
    - en-US source uses "websites"; en-GB uses the same single-word form throughout the tree, so "web sites" is an inconsistent, unwarranted change.
- `default_browser_experiment_card_text` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was needlessly split into "web sites", which is not an en-GB adaptation and conflicts with the locale's usual "websites".
    - Current: `web sites`
    - Source: `Set links from websites, emails, and messages to open automatically in Firefox.`
    - Suggest: `websites`
    - en-US source uses "websites"; British English also writes "websites" as one word, and other en-GB strings use "sites"/"websites". The split form is an over-correction.
- `delete_history_prompt_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "synced" was expanded to "synchronised", departing from the Sync feature terminology used elsewhere in the locale.
    - Current: `synchronised`
    - Source: `Removes history (including history synced from other devices)`
    - Suggest: `synced`
    - "Synced" is the product term tied to Firefox Sync and is used consistently in en-GB; "synchronised" is not a required British adaptation and introduces terminology inconsistency.
- `enhanced_tracking_protection_exceptions` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was changed to "web sites", which is not a British English convention and is inconsistent with the rest of the locale.
    - Current: `Enhanced Tracking Protection is off for these web sites`
    - Source: `Enhanced Tracking Protection is off for these websites`
    - Suggest: `Enhanced Tracking Protection is off for these websites`
    - "Website" is the standard single-word form in en-GB as well as en-US; splitting it introduces an inconsistent, dated spelling not used elsewhere in the locale.
- `errorpage_httpsonly_message_summary` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "website" was changed to "web site", an unnecessary and inconsistent alteration.
    - Current: `If you continue to the web site, you should not enter any sensitive info.`
    - Source: `However, it’s also possible that an attacker is involved. If you continue to the website, you should not enter any sensitive info. If you continue, HTTPS-Only mode will be turned off temporarily for the site.`
    - Suggest: `If you continue to the website, you should not enter any sensitive info.`
    - en-GB uses "website" as one word, same as the en-US source; the split form is inconsistent even within this string, which later says "the site".
- `errorpage_httpsonly_message_title` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "website" was changed to "web site", an unnecessary and inconsistent alteration.
    - Current: `Most likely, the web site simply does not support HTTPS.`
    - Source: `Most likely, the website simply does not support HTTPS.`
    - Suggest: `Most likely, the website simply does not support HTTPS.`
    - en-GB writes "website" as one word, matching the en-US source and the rest of the locale.
- `etp_redirect_trackers_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was needlessly split into "web sites", which is not an en-GB adaptation.
    - Current: `known tracking web sites`
    - Source: `Clears cookies set by redirects to known tracking websites.`
    - Suggest: `known tracking websites`
    - British English uses "website" as one word, exactly as en-US does; "web sites" is an unnecessary and inconsistent alteration of the source.
- `etp_tracking_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "website functionality" rendered as "web site functionality".
    - Current: `May affect some web site functionality.`
    - Source: `Stops outside ads, videos, and other content from loading that contains tracking code. May affect some website functionality.`
    - Suggest: `May affect some website functionality.`
    - "Website" is a single word in en-GB as in en-US; splitting it departs from the source without any locale justification.
- `firefox_labs_website_isolation_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites"/"website compatibility" split into "web sites"/"web site compatibility".
    - Current: `An extra barrier between web sites that helps protect your data across tabs. May affect performance, stability, web site compatibility and how browsing history is saved.`
    - Source: `An extra barrier between websites that helps protect your data across tabs. May affect performance, stability, website compatibility, and how browsing history is saved.`
    - Suggest: `An extra barrier between websites that helps protect your data across tabs. May affect performance, stability, website compatibility, and how browsing history is saved.`
    - "Website" is one word in en-GB; also the serial comma before "and how browsing history is saved" present in the source was dropped, changing the list punctuation unnecessarily.
- `firefox_labs_website_isolation_title` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — Feature title "Website isolation" changed to "Web site isolation".
    - Current: `Web site isolation`
    - Source: `Website isolation`
    - Suggest: `Website isolation`
    - "Website" is a single word in British English too; the split form is a non-standard alteration of the feature name.
- `homepage_shortcuts_add_website` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Website" has been changed to "Web site", which is not en-GB usage and is inconsistent with the rest of the locale.
    - Current: `Add web site`
    - Source: `Add website`
    - Suggest: `Add website`
    - en-GB uses "website" as one word, the same as en-US; splitting it is an unwarranted over-correction and also drops the capitalisation pattern of the source.
- `homepage_shortcuts_add_website_title` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Website" has been changed to "Web site", which is not en-GB usage.
    - Current: `Enter a Web site URL`
    - Source: `Enter a Website URL`
    - Suggest: `Enter a Website URL`
    - en-GB writes "website" as a single word, matching en-US; the split form is an over-correction inconsistent with the locale.
- `ip_protection_locations_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Navigate back" was needlessly changed to "Navigate backwards", which is not a British-English requirement and diverges from the standard back-button content description.
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - The en-US source is "Navigate back"; en-GB uses the same wording for back-button content descriptions and no spelling or vocabulary rule requires "backwards" here.
- `ip_protection_navigate_back_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Navigate back" was needlessly changed to "Navigate backwards", which is not a British-English requirement and diverges from the source wording used elsewhere for back buttons.
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - The en-US source is "Navigate back"; British English uses the same phrase for a back-button content description, so the alteration is an unnecessary and inconsistent divergence.
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
- `preference_accessibility_force_enable_zoom` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was split into "web sites", an unnecessary and inconsistent change for en-GB.
    - Current: `Zoom on all web sites`
    - Source: `Zoom on all websites`
    - Suggest: `Zoom on all websites`
    - en-GB uses "websites" as one word, as elsewhere in the locale (e.g. preference_doh strings use "sites"/"website"); splitting it is not a British convention and departs from the source without reason.
- `preference_accessibility_force_enable_zoom_summary` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" rendered as "web sites" without justification in en-GB.
    - Current: `even on web sites that prevent this gesture`
    - Source: `Enable to allow pinch and zoom, even on websites that prevent this gesture.`
    - Suggest: `even on websites that prevent this gesture`
    - British English writes "websites" as a single word; the split form is an unwarranted departure from the en-US source and inconsistent with other strings.
- `preference_accessibility_text_size_summary` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" rendered as "web sites" without justification in en-GB.
    - Current: `Make text on web sites larger or smaller`
    - Source: `Make text on websites larger or smaller`
    - Suggest: `Make text on websites larger or smaller`
    - British English writes "websites" as one word; the split form is an unwarranted change from the source and inconsistent with the rest of the locale.
- `preference_doh_summary` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "website" was changed to "web site", a form not used in en-GB and inconsistent with the rest of the locale.
    - Current: `which web site you’re about to access`
    - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access. %1$s`
    - Suggest: `which website you’re about to access`
    - en-US source uses "website"; en-GB uses the same single-word form throughout (e.g. "Cookies from unvisited sites", other website strings). "web site" is an unnecessary and inconsistent alteration.
- `preference_enhanced_tracking_protection_custom_cookies_3` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was changed to "web sites", an inconsistent and unidiomatic form for en-GB.
    - Current: `All third-party cookies (may cause web sites to break)`
    - Source: `All third-party cookies (may cause websites to break)`
    - Suggest: `All third-party cookies (may cause websites to break)`
    - The en-US source reads "websites"; British English uses the same one-word spelling, and the locale is otherwise consistent with "website".
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was changed to "web sites", an inconsistent and unidiomatic form for en-GB.
    - Current: `All cookies (will cause web sites to break)`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `All cookies (will cause websites to break)`
    - The en-US source reads "websites"; British English uses the same one-word spelling, and the locale is otherwise consistent with "website".
- `preference_enhanced_tracking_protection_custom_global_privacy_control` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was changed to "web sites", which is not an en-GB convention and is inconsistent with the rest of the locale.
    - Current: `Tell web sites not to share & sell data`
    - Source: `Tell websites not to share & sell data`
    - Suggest: `Tell websites not to share & sell data`
    - en-GB uses "websites" as a single word, as elsewhere in this file (e.g. preference_exceptions, preference_phone_feature_camera developer comments and other strings). Splitting it into "web sites" is an unnecessary and inconsistent alteration of the en-US source.
- `preferences_passwords_autofill_description` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "websites" was split into "web sites", which is inconsistent with the rest of the locale.
    - Current: `web sites`
    - Source: `Fill and save usernames and passwords in websites while using %1$s.`
    - Suggest: `websites`
    - The en-US source uses "websites", and elsewhere in en-GB (e.g. sibling password strings) the single-word form is used; "web sites" is not a British-English adaptation.
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
- `uninstall_survey_option_2_v2` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Websites" has been split into "Web sites", which is not an en-GB convention and is inconsistent with the rest of the locale.
    - Current: `Web sites didn’t work properly`
    - Source: `Websites didn’t work properly`
    - Suggest: `Websites didn’t work properly`
    - en-GB uses the closed compound "websites" exactly as en-US does; "Web sites" is an unnecessary and inconsistent alteration of the source.
- `webcompat_reporter_edit_url_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "website" was split into "web site", which is not the form used elsewhere in en-GB.
    - Current: `Edit web site URL`
    - Source: `Edit website URL`
    - Suggest: `Edit website URL`
    - en-GB writes "website" as one word, consistent with other strings in this locale (e.g. broken site/website usage); "web site" is an unnecessary and inconsistent alteration of the source.
- `accessibility_announcement_loading_finished` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "Website" was needlessly split into "Web site", which is not a British-English convention and is inconsistent with other en-GB strings.
    - Current: `Web site loaded`
    - Source: `Website loaded`
    - Suggest: `Website loaded`
    - en-GB uses "website" exactly as en-US does; there is no spelling difference. Other strings in this file (e.g. cfr_for_toolbar_shield_icon2 uses "site", content_description_lock) do not use the split form, so this is an inconsistent over-correction.
- `content_description_back` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "Navigate back" changed to "Navigate backwards", which alters the source wording without any en-GB requirement.
    - Current: `Navigate backwards`
    - Source: `Navigate back`
    - Suggest: `Navigate back`
    - The source is "Navigate back" (the back button label). "Back" is equally standard in British English; the added "-wards" is an unnecessary deviation and is inconsistent with the paired forward string.
- `content_description_forward` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "Navigate forward" changed to "Navigate forwards" without any en-GB requirement.
    - Current: `Navigate forwards`
    - Source: `Navigate forward`
    - Suggest: `Navigate forward`
    - The source is "Navigate forward", describing the forward button. "Forward" is standard in British English too; the change is an unnecessary deviation from the source wording.
- `content_description_reload` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "Reload website" rendered as "Reload web site", an unnecessary and inconsistent change.
    - Current: `Reload web site`
    - Source: `Reload website`
    - Suggest: `Reload website`
    - British English spells "website" as one word, identical to en-US; splitting it is an over-correction and inconsistent with the rest of the locale.
- `content_description_stop` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "Stop loading website" rendered as "Stop loading web site", an unnecessary and inconsistent change.
    - Current: `Stop loading web site`
    - Source: `Stop loading website`
    - Suggest: `Stop loading website`
    - British English spells "website" as one word, identical to en-US; splitting it is an over-correction and inconsistent with the rest of the locale.
- `cookie_banner_exception_panel_description_state_on_for_site` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "shopping carts" changed to "shopping baskets" departs from the en-US term used consistently in Mozilla e-commerce strings.
    - Current: `empty shopping baskets`
    - Source: `%1$s will clear this site’s cookies and refresh the page. Clearing all cookies may sign you out or empty shopping carts.`
    - Suggest: `empty shopping carts`
    - The source term "shopping cart" is the standard term in Mozilla UI strings and is understood in en-GB; the substitution introduces an inconsistent vocabulary variant.
- `preference_exceptions_description` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "websites" rendered as two words "web sites", which is not an en-GB adaptation and is inconsistent with the rest of the locale.
    - Current: `these web sites`
    - Source: `You have disabled content blocking for these websites.`
    - Suggest: `these websites`
    - en-GB uses "websites" as one word, same as the en-US source; splitting it is an unnecessary and inconsistent change.
- `preference_exceptions_remove_all_button_label` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "websites" rendered as two words "web sites".
    - Current: `Remove all web sites`
    - Source: `Remove all websites`
    - Suggest: `Remove all websites`
    - The en-US source is "Remove all websites"; en-GB does not split "websites" into two words, and other strings in the locale use "websites".
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-en-rGB/strings.xml` — "website" was needlessly split into "web site", an unidiomatic form not used in en-GB.
    - Current: `when a web site is already open in %s`
    - Source: `Unlock using fingerprint if you’ve added Shortcuts or when a website is already open in %s.`
    - Suggest: `when a website is already open in %s`
    - en-US source says "website"; British English also writes "website" as one word. "web site" is an over-correction and inconsistent with other en-GB strings that use "sites"/"website".

### E. Typography, punctuation & spacing

- `addresses_postal_code` — `mozilla-mobile/fenix/app/src/main/res/values-en-rGB/strings.xml` — "Post Code" is inconsistently capitalised/spelled; British usage is "Postcode".
    - Current: `Post Code`
    - Source: `Postal Code`
    - Suggest: `Postcode`
    - In en-GB the standard term is the single word "Postcode"; "Post Code" as two capitalised words is not the British form.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/en-GB/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

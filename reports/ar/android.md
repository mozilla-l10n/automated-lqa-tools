# Firefox for Android l10n QA — ar

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 2,390 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for ar: [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md) · [Focus for Android](focus_android.md)

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
| Files | 42 |
| Strings | 2,390 |
| Missing strings | 163 |
| Obsolete strings | 0 |
| Files absent from the locale | 2 |
| Files with no en-US counterpart | 0 |
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

**163 strings** are not translated yet, concentrated in:

- `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — 114
- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values/strings.xml` — 23
- `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ar/strings.xml` — 9
- `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ar/strings.xml` — 9
- `mozilla-mobile/android-components/components/compose/awesomebar/src/main/res/values-ar/strings.xml` — 4
- `mozilla-mobile/android-components/components/compose/menu/src/main/res/values/strings.xml` — 2
- `mozilla-mobile/android-components/components/feature/ipprotection/src/main/res/values-ar/strings.xml` — 1
- `mozilla-mobile/android-components/components/feature/protection-dashboard/src/main/res/values-ar/strings.xml` — 1

**Files absent from the locale:**

- `mozilla-mobile/android-components/components/compose/menu/src/main/res/values/strings.xml`
- `mozilla-mobile/android-components/components/feature/listentopage/src/main/res/values/strings.xml`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Focus for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 14, `curly-double` 3, `guillemet` 2 | **straight-double** |
| ellipsis | `char` 20 | **char** |
| dash | `em` 1 | **em** |
| nbsp | `total` 1 | **total** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (124)

> **Reads as a deliberate edit (4).** The translation makes the product assert something the en-US never said. Whether that was intended cannot be told from the text, which is the problem: a user cannot tell either. Read these first.

- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The subtitle promises the user will always be protected, where the source only says they will stay up to date on how to stay protected.
    - Current: `لتبقى محميًا دائمًا`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `لتبقى على اطلاع دائم بكيفية الحفاظ على حمايتك`
    - The source is about staying informed on how to stay protected. The Arabic says notifications keep the user protected at all times, which is a guarantee the product never made.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "that you use it" is rendered as "how you use" Firefox, which says usage details are shared with marketing partners.
    - Current: `كيفية اكتشافك واستخدامك لـ Firefox`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `كيف اكتشفت Firefox وأنك تستخدمه`
    - The source shares only how the user found Firefox and the fact that they use it. The Arabic says information about how they use Firefox is shared, which is a wider data-sharing claim.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "that you use it" is rendered as "how you use" Firefox, which says usage details are shared with marketing partners.
    - Current: `كيفية اكتشافك واستخدامك لـ Firefox`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `كيف اكتشفت Firefox وأنك تستخدمه`
    - The source and the developer comment limit the data to discovery and the fact of use. The Arabic says information about how the user uses Firefox is shared, which is more data collection than the product does.
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "helps stop" became "is sufficient to prevent", turning a hedged claim into a guarantee.
    - Current: `نقرة واحدة كفيلة بمنع الشركات من التجسس`
    - Source: `One tap helps stop companies spying on your clicks.`
    - Suggest: `نقرة واحدة تساعد في منع الشركات من التجسس`
    - The source only says one tap helps stop companies from spying. The Arabic says one tap is enough to prevent it, which promises a protection the product does not claim.

_Also listed under their own category below._

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 52 |
| 3 | Degraded language (grammar, spelling, terminology) | 67 |
| 4 | Cosmetic (typography, spacing) | 5 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `mozac_browser_errorpages_httpsonly_title` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ar/strings.xml` — The title adds "feature" (خاصية), so it says a secure-site feature is unavailable rather than the secure version of the site.
    - Current: `خاصية الموقع الآمن غير متاحة`
    - Source: `Secure Site Not Available`
    - Suggest: `الموقع الآمن غير متاح`
    - The source "Secure Site Not Available" means there is no HTTPS version of the site (see the developer comment). "خاصية" (feature/property) changes the meaning to a missing browser feature.
- `mozac_browser_errorpages_net_reset_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ar/strings.xml` — The last bullet tells the user to check the computer's network connection instead of the device's data or Wi-Fi connection.
    - Current: `تثبّت من اتصال الحاسوب بالشبكة`
    - Source: `{ <p> }The network link was interrupted while negotiating a connection. Please try again.{ </p> } { <ul> } { <li> }The site could be temporarily unavailable or too busy. Try again in a few moments.{ </li> } { <li> }If y…`
    - Suggest: `تحقّق من اتصال الجهاز بشبكة البيانات أو الشبكة اللاسلكية`
    - The source says "check your device’s data or Wi-Fi connection". The translation says "computer" (الحاسوب) and drops data and Wi-Fi, which is wrong on Android. The same bullet is already translated correctly in connection_failure_message.
- `mozac_browser_errorpages_redirect_loop_message` — `mozilla-mobile/android-components/components/browser/errorpages/src/main/res/values-ar/strings.xml` — "your device" is rendered as "your computer" (حاسوبك), which is wrong on a mobile browser.
    - Current: `وليس حاسوبك`
    - Source: `{ <p> }The browser has stopped trying to retrieve the requested item. The site is redirecting the request in a way that will never complete.{ </p> } { <ul> } { <li> }Have you disabled or blocked cookies required by this…`
    - Suggest: `وليس جهازك`
    - The source says "not your device". On Android, "computer" names the wrong device; the wording appears carried over from desktop.
- `mozac_feature_addons_optional_permissions_with_data_collection_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — "يتطلب" means "requires" where the source says "requests", which misrepresents optional permissions as mandatory.
    - Current: `يتطلب %1$s`
    - Source: `%1$s requests additional settings`
    - Suggest: `يطلب %1$s`
    - The comment says the dialog asks the user to grant optional permissions; "requests" is "يطلب", while "يتطلب" means the add-on needs them.
- `mozac_feature_addons_optional_permissions_with_data_collection_only_dialog_title` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — "يتطلب" means "requires" where the source says "requests", which misrepresents optional data collection as mandatory.
    - Current: `يتطلب %1$s`
    - Source: `%1$s requests additional data collection`
    - Suggest: `يطلب %1$s`
    - The comment describes these as optional data collection permissions; "requests" is "يطلب".
- `mozac_feature_addons_permissions_data_collection_websiteActivity_long_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — "Website activity" is translated as "browsing activity", which makes it the same as the browsingActivity permission.
    - Current: `مشاركة نشاط التصفح مع مطور الامتداد`
    - Source: `Share website activity with extension developer`
    - Suggest: `مشاركة نشاط الموقع مع مطور الامتداد`
    - The source says 'website activity', and the matching short description correctly uses نشاط الموقع. The long description uses نشاط التصفح (browsing activity), which is the text of a different data-collection permission, so users cannot tell the two apart.
- `mozac_feature_addons_permissions_find_description_for_update` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — "Read the text" is translated as "display the content".
    - Current: `عرض محتوى جميع التبويبات المفتوحة.`
    - Source: `Read the text of all open tabs.`
    - Suggest: `قراءة نصوص جميع التبويبات المفتوحة.`
    - The permission lets the add-on read the text of open tabs. عرض means display/view, which is not the same thing, and the non-update variant correctly uses قراءة.
- `mozac_feature_addons_permissions_management_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — "Monitor extension usage" is translated as "manage extension usage".
    - Current: `إدارة استخدام الامتدادات`
    - Source: `Monitor extension usage and manage themes`
    - Suggest: `مراقبة استخدام الامتدادات`
    - The source says the add-on can monitor extension usage, and the _for_update variant correctly uses مراقبة. إدارة (manage) describes a different and broader permission.
- `mozac_feature_addons_permissions_one_site_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — The wording says roughly "enable your data's access to the site" instead of "access your data on the site".
    - Current: `تمكين وصول بياناتك لـ %1$s`
    - Source: `Access your data for %1$s`
    - Suggest: `الوصول إلى بياناتك في %1$s`
    - The source means the add-on accesses the user's data for the host. The Arabic makes the data the thing doing the accessing, and it doesn't match the wording of the sibling strings (الوصول إلى بياناتك).
- `mozac_feature_addons_permissions_sites_in_domain_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — Translation reads as enabling sites' access to the user's data rather than the extension accessing the user's data for sites in the domain.
    - Current: `تمكين وصول بياناتك للمواقع في نطاق %1$s`
    - Source: `Access your data for sites in the %1$s domain`
    - Suggest: `الوصول إلى بياناتك للمواقع ضمن النطاق %1$s`
    - Source 'Access your data for sites in the %1$s domain' describes the extension's access; 'تمكين وصول بياناتك للمواقع' is garbled and suggests granting sites access to data. The _for_update variant is rendered correctly.
- `mozac_feature_addons_permissions_user_scripts_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — 'unverified' is rendered as 'untrusted' (غير الموثوقة).
    - Current: `غير الموثوقة`
    - Source: `Allow unverified third-party scripts to access your data`
    - Suggest: `غير المُتحقَّق منها`
    - The source says the scripts are unverified (not checked), not that they are untrusted; غير الموثوقة states a different fact.
- `mozac_feature_addons_permissions_user_scripts_extra_warning` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — 'Unverified scripts' is rendered as 'untrusted scripts'.
    - Current: `السكربتات غير الموثوقة`
    - Source: `Unverified scripts can pose security and privacy risks. Only run scripts from extensions or sources you trust.`
    - Suggest: `السكربتات غير المُتحقَّق منها`
    - Source says 'Unverified scripts'; غير الموثوقة means untrusted, which is a different claim.
- `mozac_feature_autofill_search_suggestions` — `mozilla-mobile/android-components/components/feature/autofill/src/main/res/values-ar/strings.xml` — "Search %1$s" (search within the app) is rendered as "search for %1$s", making the app name the search target.
    - Current: `البحث عن %1$s`
    - Source: `Search %1$s`
    - Suggest: `البحث في %1$s`
    - The developer comment says %1$s is the app name (e.g. Firefox), and the item opens a screen for searching logins stored in that app. "البحث عن" means "search for", so the label reads as searching for Firefox itself. It should say "search in".
- `mozac_ui_tabcounter_duplicate_tab` — `mozilla-mobile/android-components/components/ui/tabcounter/src/main/res/values-ar/strings.xml` — The menu action 'Duplicate tab' is translated as a noun phrase meaning 'a duplicated tab'.
    - Current: `تبويب مُكرر`
    - Source: `Duplicate tab`
    - Suggest: `تكرار التبويب`
    - The developer comment says this is a menu option to duplicate the current tab, so it needs an action like the other menu items (e.g. 'إغلاق التبويب'), not a description of a tab.
- `about_content` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Subject and object are reversed: the Arabic says the app produced Mozilla.
    - Current: `أنتج %1$s Mozilla.`
    - Source: `%1$s is produced by Mozilla.`
    - Suggest: `%1$s من إنتاج Mozilla.`
    - In Arabic verb-subject-object order, 'أنتج %1$s Mozilla' reads '%1$s produced Mozilla', the reverse of the source, which says %1$s is produced by Mozilla.
- `addresses_country` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Country or region" is rendered as "region or territory", dropping "country".
    - Current: `المنطقة أو الإقليم`
    - Source: `Country or region`
    - Suggest: `البلد أو المنطقة`
    - The source and comment refer to the country or region of an address; the translation means 'region or territory' and never mentions country (البلد), as used in addresses_country_only.
- `addresses_county` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "County" is rendered as "البلدة" (town), which names a different administrative unit.
    - Current: `البلدة`
    - Source: `County`
    - Suggest: `المقاطعة`
    - A county is an administrative division above the town level; البلدة means 'town' and is also used for 'Township' in addresses_village_township, so the two field labels clash.
- `alternative_app_icon_option_light` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Light" (the light colour variant, counterpart of "Dark") is translated as "إضاءة" (lighting/illumination).
    - Current: `إضاءة`
    - Source: `Light`
    - Suggest: `فاتح`
    - The icon variant is the light-coloured counterpart to "Dark" (translated "داكن"); "إضاءة" means "lighting", not a light colour tone. "فاتح" is the standard antonym of "داكن".
- `beta_feature` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The 'BETA' label was translated even though the developer comment says it must not be.
    - Current: `النسخة التجريبية`
    - Source: `BETA`
    - Suggest: `BETA`
    - The developer comment says 'Beta' should not be translated because it is used as an icon-styled element. The translation also makes the tag much longer.
- `bookmark_item_menu_button_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — 'Item Menu' is rendered as 'menu/list of items' (plural) instead of the menu for a single item.
    - Current: `قائمة العناصر لـ %s`
    - Source: `Item Menu for %s`
    - Suggest: `قائمة العنصر %s`
    - The source describes the overflow menu of one bookmark item. 'قائمة العناصر' reads as a list of several items, so a screen reader would describe the control wrongly.
- `bookmark_select_folder_new_folder_button_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "New folder" is translated as "New file".
    - Current: `ملف جديد`
    - Source: `New folder`
    - Suggest: `مجلد جديد`
    - ملف means 'file'; the source and comment refer to adding a new bookmark folder (مجلد).
- `bookmark_sort_menu_content_desc` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Sorting options" (a noun phrase) is translated as an in-progress action, "Sorting the options…".
    - Current: `جارٍ فرز الخيارات`
    - Source: `Sorting options`
    - Suggest: `خيارات الفرز`
    - The comment says this is an accessibility label for the sorting options menu, not a progress message.
- `create_collection_save_to_collection_tab_selected` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The singular string uses the plural noun "تبويبات" (tabs) for a single selected tab.
    - Current: `%d تبويبات محدّدة`
    - Source: `%d tab selected`
    - Suggest: `%d تبويب محدّد`
    - The source "%d tab selected" is the one-tab variant. The translation copies the plural string, so it shows "1 تبويبات", which is ungrammatical and says "tabs".
- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Press back" is rendered as "press the delete button", and "drag from top" as "drag upward".
    - Current: `اسحب للأعلى واضغط على زر الحذف للخروج`
    - Source: `Drag from top & press back to exit`
    - Suggest: `اسحب من الأعلى واضغط على زر الرجوع للخروج`
    - The source tells the user to drag from the top and press back. The translation says drag upward and press delete, which is the wrong instruction.
- `exit_fullscreen_with_gesture_short` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Drag from top" is rendered as "drag upward".
    - Current: `اسحب للأعلى`
    - Source: `Drag from top & use back gesture to exit`
    - Suggest: `اسحب من الأعلى`
    - Dragging from the top edge is a downward swipe. "للأعلى" tells the user to swipe the opposite way.
- `expanded_tab_group_header_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — For zero tabs the text says "no tab group" and drops the group name and colour.
    - Current: `لا مجموعة لسان`
    - Source: `{$quantity ->} [one] %1$s tab group with %2$d tab, color %3$s [other] %1$s tab group with %2$d tabs, color %3$s`
    - Suggest: `مجموعة لسان %1$s بلا ألسنة، لون %3$s`
    - The source describes a named tab group containing zero tabs. The translation says there is no tab group at all.
- `history_search_group_site_1` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "صفحة %d" reads as "page number %d", not as a count of one page.
    - Current: `صفحة %d`
    - Source: `%d page`
    - Suggest: `%d صفحة`
    - The comment says this counts the pages in a group. In Arabic, a noun followed by a number reads as an ordinal page number.
- `history_search_group_sites_1` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The page count has a definite article and the number comes after the noun, so it reads like "the pages 5" instead of "5 pages".
    - Current: `الصفحات %d`
    - Source: `%d pages`
    - Suggest: `%d صفحات`
    - The source is a count, "%d pages". In Arabic the number should come first and the noun should not have "ال". As written it reads as a label or page number, not a count.
- `history_search_hint` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Search history" (search your history) is translated as a noun phrase meaning "the history of your searches".
    - Current: `سجل البحث`
    - Source: `Search history`
    - Suggest: `ابحث في التأريخ`
    - The comment says this is placeholder text in the history search bar, so "search" is a verb here. "سجل البحث" means "the record of searches", which is a different thing.
- `ip_protection_data_reset_info` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "يُصفّر" means "is zeroed", so "zeroed to 50 GB" contradicts itself; the source means the allowance is reset to the full amount.
    - Current: `يُصفّر إلى`
    - Source: `Resets to %1$.0f GB on the first of every month.`
    - Suggest: `يُعاد ضبطه إلى`
    - The source 'Resets to X GB' means the allowance goes back to the full X GB. تصفير means setting something to zero, which conflicts with 'to X GB'.
- `nova_onboarding_add_search_widget_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Brand name Firefox transliterated into Arabic script although the comment says it is intentionally hardcoded.
    - Current: `فايرفوكس`
    - Source: `Start every search from your phone’s home screen and know Firefox’s automatic protections have your back.`
    - Suggest: `Firefox`
    - Developer comment: 'Firefox' is intentionally hardcoded; brand names must stay untranslated and all other strings keep 'Firefox' in Latin script.
- `nova_onboarding_app_icon_prompt_body` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — 'Home screen' rendered as 'home page' (browser start page) instead of the device home screen.
    - Current: `الصفحة الرئيسية`
    - Source: `Give your home screen a personal touch.`
    - Suggest: `الشاشة الرئيسية`
    - The prompt is about choosing an app icon shown on the phone's home screen; الصفحة الرئيسية means the browser's home page.
- `nova_onboarding_notifications_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The subtitle promises the user will always be protected, where the source only says they will stay up to date on how to stay protected.
    - Current: `لتبقى محميًا دائمًا`
    - Source: `Discover the latest privacy features in Firefox so you’re always up to date on how to stay protected.`
    - Suggest: `لتبقى على اطلاع دائم بكيفية الحفاظ على حمايتك`
    - The source is about staying informed on how to stay protected. The Arabic says notifications keep the user protected at all times, which is a guarantee the product never made.
- `nova_onboarding_theme_selection_light_label` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Light" theme option is translated as "إضاءة" (lighting/illumination) instead of the light-theme adjective.
    - Current: `إضاءة`
    - Source: `Light`
    - Suggest: `فاتحة`
    - The option is the light theme, the opposite of "داكنة" (dark). "إضاءة" is a noun meaning lighting, so the two options don't match.
- `nova_onboarding_tou_subtitle` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "won't sell you out" is rendered as "will never let you down", which loses the point about not betraying the user or selling their data.
    - Current: `لن يخذلك أبداً`
    - Source: `Speedy, safe, and won’t sell you out. Browsing just got better.`
    - Suggest: `لن يبيع بياناتك`
    - "Sell you out" means betray or sell the user's data, a privacy point. "يخذلك" means disappoint, which is a different and broader claim.
- `onboarding_marketing_body_1` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "that you use it" is rendered as "how you use" Firefox, which says usage details are shared with marketing partners.
    - Current: `كيفية اكتشافك واستخدامك لـ Firefox`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `كيف اكتشفت Firefox وأنك تستخدمه`
    - The source shares only how the user found Firefox and the fact that they use it. The Arabic says information about how they use Firefox is shared, which is a wider data-sharing claim.
- `onboarding_marketing_redesign_opt_out_checkbox` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "that you use it" is rendered as "how you use" Firefox, which says usage details are shared with marketing partners.
    - Current: `كيفية اكتشافك واستخدامك لـ Firefox`
    - Source: `Share how you discovered Firefox, and that you use it, with Mozilla’s marketing partners. This data is never sold.`
    - Suggest: `كيف اكتشفت Firefox وأنك تستخدمه`
    - The source and the developer comment limit the data to discovery and the fact of use. The Arabic says information about how the user uses Firefox is shared, which is more data collection than the product does.
- `onboarding_redesign_set_default_browser_body` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "helps stop" became "is sufficient to prevent", turning a hedged claim into a guarantee.
    - Current: `نقرة واحدة كفيلة بمنع الشركات من التجسس`
    - Source: `One tap helps stop companies spying on your clicks.`
    - Suggest: `نقرة واحدة تساعد في منع الشركات من التجسس`
    - The source only says one tap helps stop companies from spying. The Arabic says one tap is enough to prevent it, which promises a protection the product does not claim.
- `open_all_warning_confirm` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The button label is a noun phrase meaning "the open tabs" when it should be the action "open tabs".
    - Current: `التبويبات المفتوحة`
    - Source: `Open tabs`
    - Suggest: `افتح التبويبات`
    - The developer comment says this button confirms opening all tabs, so "Open" is a verb. The Arabic reads as "the opened tabs".
- `preference_enhanced_tracking_protection_custom_cookies_4` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "will cause websites to break" is rendered as "may cause", so a certain outcome now reads as only possible.
    - Current: `يمكن أن تتسبب في تعطيل المواقع`
    - Source: `All cookies (will cause websites to break)`
    - Suggest: `سيتسبب في تعطيل المواقع`
    - The source says blocking all cookies will break sites, unlike the third-party option, which says 'may'. The translation seems to have copied the 'may' wording from that option.
- `preferences_downloads_delete_from_device_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The description of this option uses the past tense, so it says the file has already been deleted.
    - Current: `حُذف الملف من جهازك وأُزيل من تأريخ التنزيلات`
    - Source: `File is deleted from your device and removed from download history`
    - Suggest: `يُحذف الملف من جهازك ويُزال من تأريخ التنزيلات`
    - The source describes what happens if the user picks this option ('File is deleted'). The past tense tells the user the deletion has already happened.
- `preferences_downloads_remove_from_download_history_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The description of this option uses the past tense, so it says the file has already been removed from the history.
    - Current: `أُزيل الملف من تأريخ تنزيلاتك`
    - Source: `File is removed from your download history, but is still saved on your device`
    - Suggest: `يُزال الملف من تأريخ تنزيلاتك`
    - The source describes what this option does ('File is removed'). The past tense tells the user the removal has already happened.
- `qr_code_display_share_nearby` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The heading says "share the nearby link" instead of "share the link with people nearby".
    - Current: `شارك الرابط القريب`
    - Source: `Share link nearby`
    - Suggest: `شارك الرابط مع من حولك`
    - In the source, "nearby" means the people near you who will scan the code (see the instructions string). In Arabic, the adjective القريب modifies الرابط, so the heading reads "the nearby link", which means something else.
- `restart_warning_dialog_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "May close" is rendered as "may stop working", which suggests a malfunction.
    - Current: `قد يتوقف التطبيق عن العمل`
    - Source: `The app may close. Just tap your shiny new icon to reopen %1$s.`
    - Suggest: `قد يُغلَق التطبيق`
    - The source and the developer comment say only that the app may close after the icon changes. "يتوقف عن العمل" usually means the app stops working or crashes. The related string restart_and_shortcuts_removal_warning_dialog_body already uses "قد يُغلَق".
- `search_engine_suggestions_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Search %s" (search using engine %s) is rendered as "search for %s", making the engine name the search term.
    - Current: `ابحث عن %s`
    - Source: `Search %s`
    - Suggest: `ابحث في %s`
    - The developer comment states %s is the name of the suggested search engine; "ابحث عن" means "search for", so the string tells the user to look up the engine rather than search with it.
- `settings_search_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Search settings" (search is a verb) is rendered as the noun phrase "search settings" (settings of search).
    - Current: `إعدادات البحث`
    - Source: `Search settings`
    - Suggest: `ابحث في الإعدادات`
    - The developer comment says "Search" is a verb: the screen searches within Settings. The Arabic reads as the settings for search, which names a different screen.
- `shortcut_url_hint` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Shortcut URL" is rendered as "link shortcut/shortening the link" instead of "the shortcut's URL".
    - Current: `اختصار الرابط`
    - Source: `Shortcut URL`
    - Suggest: `رابط الاختصار`
    - The hint is for the URL field of a shortcut; the idafa order is reversed, producing "shortcut of the link".
- `snackbar_private_tab_closed` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The confirmation "Private tab closed" is rendered with the verbal noun "closing the private tab", which reads like an action label.
    - Current: `إغلاق التبويب الخاص`
    - Source: `Private tab closed`
    - Suggest: `أُغلق التبويب الخاص`
    - The snackbar confirms a completed action; the verbal noun reads like a "Close private tab" command.
- `snackbar_tab_closed` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The confirmation "Tab closed" is rendered with the verbal noun "closing the tab", which reads like an action label.
    - Current: `إغلاق التبويب`
    - Source: `Tab closed`
    - Suggest: `أُغلق التبويب`
    - The snackbar confirms a completed action; the verbal noun reads like a "Close tab" command.
- `sync_sent_tabs_snackbar_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Snackbar confirmation rendered as a noun phrase "the sent tabs" rather than a statement that tabs were sent.
    - Current: `التبويبات المُرسلة`
    - Source: `Tabs sent`
    - Suggest: `تم إرسال التبويبات`
    - The snackbar confirms tabs have been sent; the singular counterpart correctly uses "تم إرسال التبويب". "التبويبات المُرسلة" reads as a label/heading 'Sent tabs'.
- `tab_manager_empty_normal_tabs_page_header` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The Arabic says "open a new window" instead of "create a new tab".
    - Current: `فتح نافذة جديدة`
    - Source: `Create a new tab to start searching`
    - Suggest: `أنشئ تبويبًا جديدًا`
    - The source says 'Create a new tab'. نافذة means 'window', a different UI concept.
- `tab_manager_open_tab_search` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The Arabic reads as "open the search tab" instead of "open search in tabs".
    - Current: `فتح تبويب البحث`
    - Source: `Open tab search`
    - Suggest: `فتح البحث في التبويبات`
    - The comment says this button opens the Tab Search feature for searching through tabs. The current Arabic names a tab called 'search'.
- `tab_tray_close_tabs_banner_positive_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "View options" (verb + object) is rendered as "display options" (a noun phrase).
    - Current: `خيارات العرض`
    - Source: `View options`
    - Suggest: `اعرض الخيارات`
    - The button opens Settings so the user can see the auto-close options. "خيارات العرض" means view/display settings, which is a different thing.

### C. Grammar, agreement & spelling

- `mozac_feature_addons_cant_install_extension` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — "الامتدادة" is a misspelling of "الامتداد", the term used everywhere else.
    - Current: `الامتدادة`
    - Source: `Can’t install extension`
    - Suggest: `الامتداد`
    - The word for extension is masculine "الامتداد" throughout the surface; the added taa marbuta is a spelling error.
- `mozac_feature_addons_failed_to_install_incompatible_error` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — Typo: "ثبيت" is missing its first letter and should be "تثبيت".
    - Current: `تعذر ثبيت`
    - Source: `%1$s could not be installed because it is not compatible with %2$s %3$s.`
    - Suggest: `تعذر تثبيت`
    - "Installed" is rendered as "تثبيت" in every other string; "ثبيت" is not a word.
- `mozac_feature_addons_failed_to_load_extensions` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — Typo: "الامتدادت" is missing the alif of the plural "الامتدادات".
    - Current: `الامتدادت`
    - Source: `Couldn’t load extensions. Try again later.`
    - Suggest: `الامتدادات`
    - The correct plural form, used in other strings, is "الامتدادات".
- `mozac_feature_addons_permissions_browser_data_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — The conjunction و ("and") is written as a separate word, with a space after it.
    - Current: `الحديث و ملفات تعريف الارتباط و البيانات`
    - Source: `Clear recent browsing history, cookies, and related data`
    - Suggest: `الحديث وملفات تعريف الارتباط والبيانات`
    - In Arabic the conjunction و is joined to the word that follows it. Writing it as a separate word is an orthographic error; the _for_update version of this string spells it correctly.
- `mozac_feature_addons_permissions_none_required_data_collection_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — After the verb قال, the particle must be إنّ, not أن.
    - Current: `يقول المطور أن`
    - Source: `The developer says this extension doesn’t require data collection.`
    - Suggest: `يقول المطور إنّ`
    - In standard Arabic grammar, reported speech after قال and its derived forms takes إنّ.
- `mozac_feature_addons_permissions_privacy_description` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — 'اطّلع' is misspelled with a hamza, 'و' is detached from the next word, and the imperative form is inconsistent with the other permission descriptions.
    - Current: `إطّلع على إعدادات الخصوصية و عدّلها`
    - Source: `Read and modify privacy settings`
    - Suggest: `قراءة إعدادات الخصوصية وتعديلها`
    - The imperative of اطّلع starts with a hamzat wasl and is written without a hamza. The conjunction و must attach to the next word. The _for_update variant and the other permissions use the verbal-noun form.
- `mozac_feature_addons_status_softblocked_2` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — The first letter has a double damma (ٌ) where a single damma (ُ) belongs.
    - Current: `قٌيّد`
    - Source: `This extension is restricted and has been disabled. You can enable it, but this may be risky.`
    - Suggest: `قُيّد`
    - The passive verb قُيِّد takes a single damma on the first letter. The double damma is a noun ending and is wrong here.
- `mozac_feature_addons_updater_notification_short_intro` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — The first letter has a double damma (ٌ) where a single damma (ُ) belongs.
    - Current: `يٌرجى`
    - Source: `Cancel to keep your current version and settings.`
    - Suggest: `يُرجى`
    - The passive verb يُرجى takes a single damma. The double damma is a misspelling.
- `mozac_feature_extensions_manager_notification_content_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — The feminine 'إحدى' is used with the masculine noun 'امتداد'.
    - Current: `توقفت إحدى الامتدادات`
    - Source: `One or more extensions stopped working, making your system unstable.`
    - Suggest: `توقف أحد الامتدادات`
    - امتداد is masculine, so it takes أحد and a masculine verb.
- `mozac_feature_extensions_manager_notification_title_text` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — Two hamza errors: 'ايقاف' is missing its hamza, and 'الإمتدادات' has one it should not have.
    - Current: `تم ايقاف الإمتدادات مؤقتًا`
    - Source: `Extensions are temporarily disabled`
    - Suggest: `تم إيقاف الامتدادات مؤقتًا`
    - The correct spellings are إيقاف (the hamza goes under the alif) and الامتدادات (the alif of the pattern takes no hamza). The second spelling also differs from 'الامتدادات' as used in the other strings.
- `mozac_feature_contextmenu_snackbar_new_tab_opened` — `mozilla-mobile/android-components/components/feature/contextmenu/src/main/res/values-ar/strings.xml` — Spelling error: "قتح" is a typo for "فتح" (open).
    - Current: `تم قتح تبويب جديد`
    - Source: `New tab opened`
    - Suggest: `تم فتح تبويب جديد`
    - The source says "New tab opened". The verb for "open" is فتح, and the matching private-tab string spells it correctly. "قتح" is not a word.
- `mozac_feature_media_sharing_camera_and_microphone` — `mozilla-mobile/android-components/components/feature/media/src/main/res/values-ar/strings.xml` — The conjunction "و" is written as a separate word instead of being attached to the next word.
    - Current: `الكاميرا و الميكروفون`
    - Source: `Camera and microphone are on`
    - Suggest: `الكاميرا والميكروفون`
    - Arabic spelling attaches the conjunction و directly to the word that follows it.
- `mozac_feature_prompts_suggest_strong_password_updated_snackbar_title` — `mozilla-mobile/android-components/components/feature/prompts/src/main/res/values-ar/strings.xml` — The word for "updated" is misspelled as تحديت instead of تحديث.
    - Current: `تحديت`
    - Source: `Password updated`
    - Suggest: `تحديث`
    - The Arabic word for 'update' is تحديث, which ends in ث. Writing it with ت is a spelling mistake in the snackbar that confirms the password was updated.
- `mozac_summarize_info_error_title` — `mozilla-mobile/android-components/components/feature/summarize/src/main/res/values-ar/strings.xml` — The verbal noun تلخيص stands alone with no article and no object, so the sentence is ungrammatical.
    - Current: `لا يمكن تلخيص الآن`
    - Source: `Can’t summarize right now`
    - Suggest: `لا يمكن التلخيص الآن`
    - After لا يمكن, a bare indefinite masdar needs either the definite article or a complement. «لا يمكن التلخيص الآن» correctly says 'Can't summarize right now'.
- `add_tab` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The noun after the verbal noun إضافة is wrongly in the accusative with tanween instead of the genitive.
    - Current: `إضافة تبويبًا`
    - Source: `Add tab`
    - Suggest: `إضافة تبويب`
    - Here إضافة is a verbal noun in an idafa construction, so the following noun must be genitive (إضافة تبويب). The sibling string add_private_tab correctly uses 'إضافة تبويب خاص'.
- `automatic_translation_header_preference` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The verb in the quoted option 'never translate' is misspelled as 'تترجمة'.
    - Current: `لا تترجمة أبدًا`
    - Source: `Select a language to manage ”always translate“ and ”never translate“ preferences.`
    - Suggest: `لا تترجم أبدًا`
    - 'تترجمة' is not a valid verb form. The imperative is 'لا تترجم', which is how the option title itself is rendered (automatic_translation_option_never_translate_title_preference).
- `bookmark_sort_menu_newest` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Spelling mistake: تريب instead of ترتيب.
    - Current: `تريب`
    - Source: `Sort by newest`
    - Suggest: `ترتيب`
    - The word for 'sort' is ترتيب, as the neighbouring sort strings spell it.
- `bookmark_sort_menu_oldest` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Spelling mistake: تريب instead of ترتيب.
    - Current: `تريب`
    - Source: `Sort by oldest`
    - Suggest: `ترتيب`
    - The word for 'sort' is ترتيب, as the neighbouring sort strings spell it.
- `browser_menu_default_banner_subtitle_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The passive verb is misspelled: the ص carries a double damma (ٌ) where it needs a single damma (ُ).
    - Current: `وصٌنع`
    - Source: `Fast, private, and made for you.`
    - Suggest: `وصُنع`
    - The source says "made for you", so the passive verb صُنع is correct, but it takes a single damma. The double damma (tanween) is only used on indefinite nouns, so this is a spelling error.
- `browser_menu_sign_in_caption_3` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The phrase for "bookmarks" is malformed: the definite article is on the adjective instead of the noun, and the conjunction و is followed by a stray space.
    - Current: `و علامات المرجعية`
    - Source: `Sync passwords, bookmarks, and more`
    - Suggest: `والعلامات المرجعية`
    - In Arabic, "bookmarks" is العلامات المرجعية, a noun and adjective that must agree in definiteness. "علامات المرجعية" is not grammatical. The conjunction و should also be written attached to the next word.
- `browser_menu_try_a_recommended_extension_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The word for "one of" is in the feminine form (إحدى), but the noun it goes with, الامتدادات ("extensions"), is masculine.
    - Current: `إحدى الامتدادات`
    - Source: `Try a recommended extension`
    - Suggest: `أحد الامتدادات`
    - امتداد ("extension") is a masculine noun, so "one of the extensions" needs the masculine أحد, not the feminine إحدى.
- `credit_cards_number_validation_error_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The adjective describing the object of أدخِل lacks the accusative tanween alif.
    - Current: `رقم بطاقة سليم`
    - Source: `Enter a valid card number`
    - Suggest: `رقم بطاقة سليمًا`
    - رقم is the object of the verb أدخِل, so it is accusative. The indefinite adjective that agrees with it must also be accusative: سليمًا.
- `delete_browsing_data_prompt_message_3` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The shadda in المحددّة sits on the wrong letter.
    - Current: `المحددّة`
    - Source: `%s will delete the selected browsing data.`
    - Suggest: `المحدّدة`
    - The word is المحدَّدة ("selected"), with the doubled consonant on the first dal. Putting the shadda on the second dal is a spelling error.
- `edit_tab_group_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The title uses a wrong preposition and reads as 'edit on the group', which is ungrammatical.
    - Current: `حرّر على المجموعة`
    - Source: `Edit group`
    - Suggest: `تعديل المجموعة`
    - The source 'Edit group' is a screen title. 'حرّر' doesn't take 'على' to mean 'edit', so the phrase is ungrammatical. The other edit titles in this batch use the noun form 'تعديل …' (تعديل المجلد، تعديل العلامة).
- `etp_suspected_fingerprinters_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Typo: "تكمين" should be "تمكين" (enable).
    - Current: `تكمين`
    - Source: `Enables fingerprinting protection to stop suspected fingerprinters.`
    - Suggest: `تمكين`
    - The letters are transposed. The word as written does not exist.
- `extension_process_crash_dialog_disable_extensions_button_text` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "الامدادات" (supplies) is a misspelling of "الامتدادات" (extensions).
    - Current: `الامدادات`
    - Source: `Continue with extensions disabled`
    - Suggest: `الامتدادات`
    - A letter is missing, which turns the word into a different one, and it does not match the term used in the other strings.
- `extension_process_crash_dialog_message` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "الامتدادت" is misspelled; the plural is "الامتدادات". The same misspelling occurs several times in this string.
    - Current: `ستبقى الامتدادت متوقفة`
    - Source: `One or more extensions stopped working, making your system unstable. %1$s unsuccessfully tried to restart the extension(s).  Extensions won’t be restarted during your current session.  Removing or disabling extensions m…`
    - Suggest: `ستبقى الامتدادات متوقفة`
    - The alef of the feminine plural ending is missing. The same error appears in "الامتداد/الامتدادت" and "إزالة الامتدادت".
- `extension_process_crash_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Hamza errors: "ايقاف" should be "إيقاف", and "الإمتدادات" should be "الامتدادات".
    - Current: `تم ايقاف الإمتدادات مؤقتًا`
    - Source: `Extensions are temporarily disabled`
    - Suggest: `تم إيقاف الامتدادات مؤقتًا`
    - "إيقاف" takes hamzat qat', while the alef in "امتداد" is hamzat wasl and takes no hamza.
- `likert_scale_option_confusing_or_hard_to_use` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The sentence starts with "أنه" (hamza above), which is wrong at the start of a sentence; it should be "إنه".
    - Current: `أنه مُربِك`
    - Source: `It’s confusing or hard to use`
    - Suggest: `إنه مُربِك`
    - Arabic grammar requires إنّ (hamza below the alif) when it opens a sentence, so "أنه" here is a spelling error.
- `likert_scale_option_slow_or_buggy` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The sentence starts with "أنه" (hamza above), which is wrong at the start of a sentence; it should be "إنه".
    - Current: `أنه بطيء`
    - Source: `It’s slow or buggy`
    - Suggest: `إنه بطيء`
    - Arabic grammar requires إنّ (hamza below the alif) when it opens a sentence, so "أنه" here is a spelling error.
- `microsurvey_describe_your_experience_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The verb "يوصف" is the wrong form. The active verb "to describe" is "يصف", and "best" is left out.
    - Current: `ما الذي يوصف تجربتك حتى الآن؟`
    - Source: `Help us improve Firefox. Which best describes your experience so far?`
    - Suggest: `ما الذي يصف تجربتك على أفضل نحو حتى الآن؟`
    - The present tense of وصف is يصف. "يوصف" is not the right form for "describes" here. The en-US also asks which option *best* describes the experience, and the translation drops that.
- `mozac_browser_awesomebar_remove_suggestion` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Misspelled demonstrative "هذ" instead of "هذا", and the phrase reads as 'record of this search' rather than 'this history entry'.
    - Current: `حذف سجل هذ البحث`
    - Source: `Delete this history entry`
    - Suggest: `حذف مدخل السجل هذا`
    - "هذ" is not a word; the source refers to deleting a browsing history entry, not the record of a search.
- `nova_onboarding_app_icon_prompt_body` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Imperative of أعطى is missing its hamza.
    - Current: `اعطِ`
    - Source: `Give your home screen a personal touch.`
    - Suggest: `أعطِ`
    - Form IV verb imperative is spelled with hamzat qat': أعطِ.
- `onboarding_preferences_dialog_crash_reporting_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "الإنهيار" is misspelled with a hamza, and it doesn't match the title's term "الأعطال" for crash reports.
    - Current: `تقارير الإنهيار`
    - Source: `Crash reports allow us to diagnose and fix issues with the browser. Reports may include personal or sensitive data.`
    - Suggest: `تقارير الأعطال`
    - انهيار starts with a hamzat wasl, so it should be written without a hamza. The title of the same option renders "crash reports" as تقارير الأعطال.
- `pbm_authentication_leave_private_tabs` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The adjective is missing the definite article, so it doesn't agree with the definite noun «التبويبات».
    - Current: `مغادرة التبويبات خاصة`
    - Source: `Leave private tabs`
    - Suggest: `مغادرة التبويبات الخاصة`
    - In Arabic an adjective describing a definite noun must also take «ال». «التبويبات خاصة» reads as a separate statement ('the tabs are private') instead of 'private tabs'. Related strings in the batch correctly use «التبويبات الخاصة».
- `preference_doh_default_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Imperative 'Use' is misspelled with a hamza, turning it into first-person 'I use'.
    - Current: `أستخدم محلل`
    - Source: `Use your default DNS resolver if there is a problem with the secure DNS provider`
    - Suggest: `استخدم محلل`
    - The source is the imperative/descriptive 'Use'; 'أستخدم' means 'I use'. The correct imperative is 'استخدم', as in the other bullets.
- `preference_doh_increased_protection_info_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Imperative 'Use' is misspelled with a hamza, turning it into first-person 'I use'.
    - Current: `أستخدم فقط`
    - Source: `Only use your default DNS resolver if there is a problem with secure DNS`
    - Suggest: `استخدم فقط`
    - The source is 'Only use…'; 'أستخدم' means 'I use'. It should be 'استخدم', which matches max_protection_info_1.
- `preference_doh_increased_protection_summary` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — 'إختيار' wrongly carries a hamza (it takes hamzat wasl), and the conjunction 'و' is detached.
    - Current: `و إختيار`
    - Source: `You control when to use secure DNS and choose your provider.`
    - Suggest: `واختيار`
    - The verbal noun of form VIII (اختيار) is written without a hamza, and the conjunction و attaches to the following word.
- `preferences_category_select_default_search_engine_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Ungrammatical construction: definite adjective after an indefinite noun in the possessive phrase.
    - Current: `محرك بحث المبدئي`
    - Source: `Normal browsing default search engine`
    - Suggest: `محرك البحث المبدئي`
    - In the phrase محرك بحث, the second noun is indefinite, so the adjective المبدئي can't take the article. The correct form is محرك البحث المبدئي.
- `preferences_category_select_private_search_engine` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Ungrammatical construction: definite adjective after an indefinite noun in the possessive phrase.
    - Current: `محرك بحث المبدئي`
    - Source: `Private browsing default search engine`
    - Suggest: `محرك البحث المبدئي`
    - In the phrase محرك بحث, the second noun is indefinite, so the adjective المبدئي can't take the article. The correct form is محرك البحث المبدئي.
- `preferences_downloads_ask_when_to_delete_files` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The first-person verb 'احذف' is missing its hamza and reads as the imperative 'delete'.
    - Current: `عندما احذف`
    - Source: `Ask when I delete files`
    - Suggest: `عندما أحذف`
    - The source says 'when I delete', so the verb is first-person present 'أحذف'. Without the hamza, 'احذف' is the imperative, which is a spelling error.
- `preferences_passwords_exceptions_description_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Missing preposition لـ before هذه المواقع makes the sentence ungrammatical.
    - Current: `كلمات المرور هذه المواقع`
    - Source: `%s won’t save passwords for these sites.`
    - Suggest: `كلمات المرور لهذه المواقع`
    - Source says 'won't save passwords for these sites'; without لـ the Arabic reads 'passwords these sites', which is ungrammatical. The sibling empty-state string correctly uses للمواقع.
- `private_tab_cfr_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The first word is misspelled: "اتستخدام" is not a valid Arabic word.
    - Current: `اتستخدام قفل الشاشة`
    - Source: `Use screen lock to hide private tabs?`
    - Suggest: `أتستخدم قفل الشاشة`
    - The source is the question "Use screen lock to hide private tabs?". The word "اتستخدام" looks like a mix of "أتستخدم" (question form) and "استخدام" (noun). Either one alone would be correct, but the mix is a spelling error.
- `review_prompt_feedback_header` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The app name sits straight after "خدماتنا" (our services), so the sentence is ungrammatical.
    - Current: `تحسين خدماتنا %1$s`
    - Source: `We’re sorry you’re having issues. Let us know how we can improve %1$s.`
    - Suggest: `تحسين %1$s`
    - The source says "improve %1$s". Putting "خدماتنا" before the app name makes it read "improve our services Firefox", which is broken Arabic.
- `snackbar_num_tabs_closed` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Misspelling of "closed": المغقلة instead of المغلقة.
    - Current: `المغقلة`
    - Source: `Tabs closed: %1$s`
    - Suggest: `المغلقة`
    - Typo; the correct word is المغلقة.
- `sync_scan_code` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Typo: "الرز" (rice) instead of "الرمز" (the code).
    - Current: `الرز`
    - Source: `Scan the code`
    - Suggest: `الرمز`
    - Source says 'Scan the code'; "الرز" means rice, a missing letter in "الرمز".
- `top_sites_edit_dialog_url_error` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The adjective describing the object of أدخل lacks the accusative ending; it should be صالحًا, not صالح.
    - Current: `عنوان URL صالح`
    - Source: `Enter a valid URL`
    - Suggest: `عنوان URL صالحًا`
    - "عنوان" is the indefinite direct object of the imperative أدخل, so the adjective that agrees with it has to be accusative (منصوب). In written text that ending appears as the alif tanween: صالحًا.
- `uninstall_survey_option_3_v2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The verb يفتقر is missing its required preposition إلى.
    - Current: `يفتقر الميزات`
    - Source: `Missing features I need`
    - Suggest: `يفتقر إلى الميزات`
    - In Arabic, افتقر/يفتقر takes its object through إلى. Without it the sentence is ungrammatical.
- `unsubmitted_crash_requested_by_devs_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The pronoun in إرسالها is feminine, but it refers to the masculine singular تقرير.
    - Current: `سيساعدنا إرسالها`
    - Source: `You have an unsent crash report related to crashes being investigated. Sending it will help us improve %1$s. Closing this notification will ignore this report.`
    - Suggest: `سيساعدنا إرساله`
    - This string is about a single report (تقرير, masculine singular), so the pronoun must be masculine. The feminine form belongs to the plural version of this string.

### D. Terminology, register & consistency

- `mozac_lib_crash_dialog_checkbox` — `mozilla-mobile/android-components/components/lib/crash/src/main/res/values-ar/strings.xml` — 'Crash report' is rendered as تقرير العطل here, but as بلاغ/بلاغات الأعطال in the other crash reporter strings.
    - Current: `تقرير العطل`
    - Source: `Send crash report to %1$s`
    - Suggest: `بلاغ العطل`
    - The same source term 'crash report' is translated بلاغ in mozac_lib_crash_activity_title, mozac_lib_crash_no_crashes and mozac_lib_send_crash_report_in_progress. Using تقرير only here makes the terminology inconsistent within the same crash reporter feature.
- `collection_delete` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Collection" is rendered as "المجموعة" (the term used for tab groups) instead of "التجميعة" used for collections elsewhere.
    - Current: `حذف المجموعة`
    - Source: `Delete collection`
    - Suggest: `حذف التجميعة`
    - The other collection strings (collections_header, collection_name_hint, collection_menu_button_content_description) use التجميعة/التجميعات, while مجموعة is used for tab groups on the same surface, so the delete-collection action can be confused with deleting a tab group.
- `collection_rename` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Collection" is rendered as "المجموعة" instead of the established "التجميعة".
    - Current: `إعادة تسمية المجموعة`
    - Source: `Rename collection`
    - Suggest: `إعادة تسمية التجميعة`
    - This is inconsistent with التجميعة/التجميعات used for collections in the same menu and header, and it clashes with مجموعة, which is used for tab groups.
- `create_collection_tabs_saved_new_collection_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Collection" is translated as "المجموعة", not "التجميعة" as in the rest of the collection flow.
    - Current: `تم حفظ المجموعة`
    - Source: `Collection saved`
    - Suggest: `تم حفظ التجميعة`
    - Every other collection string uses "تجميعة", and "مجموعة" is the word used for tab groups, so the two features get mixed up.
- `create_tab_group_content_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Tab" is translated as "لسان" here, but the sheet title for the same action uses "تبويب".
    - Current: `أنشئ مجموعة لسان`
    - Source: `Create tab group`
    - Suggest: `أنشئ مجموعة تبويب`
    - The create tab group title is "أنشئ مجموعة تبويب", and the surrounding strings use "تبويب" for tab. The button that opens that sheet should use the same term.
- `delete_history_prompt_body_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "history" is rendered as "السجل" while the surrounding history-deletion strings use "التأريخ".
    - Current: `السجل`
    - Source: `Removes history (including history synced from other devices)`
    - Suggest: `التأريخ`
    - The same source term 'history' is translated as التأريخ in delete_from_history and download_delete_dialog_from_history; using السجل here is inconsistent on the same deletion surface.
- `felt_privacy_info_card_subtitle_3` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Tabs" is rendered as "التبويبات" here, while the tab-group string uses "لسان".
    - Current: `التبويبات الخاصة`
    - Source: `%1$s deletes your cookies, history, and site data when you close all your private tabs.`
    - Suggest: `الألسنة الخاصة`
    - The same UI term is translated two different ways in the browser.
- `ip_protection_location_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "Location" is "المكان" here but "الموقع" in ip_protection_location_section on the same VPN settings screen.
    - Current: `المكان`
    - Source: `Location`
    - Suggest: `الموقع`
    - Both strings say 'Location' and appear on the same VPN settings screen, so they should use the same term.
- `onboarding_firefox_account_sync_is_on` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Sync is rendered "التزامن" here but "المزامنة" in the sync onboarding button.
    - Current: `التزامن يعمل`
    - Source: `Sync is on`
    - Suggest: `المزامنة تعمل`
    - Sync is translated two different ways across the onboarding screens. "التزامن" means simultaneity; "المزامنة" is the term used for the sync feature.
- `preference_etp_exceptions_icon_description` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Enhanced Tracking Protection is rendered as "المحسّنة", which does not match the preference title's "الموسّعة".
    - Current: `الحماية المحسّنة من التعقب`
    - Source: `Enhanced tracking protection exception preference icon`
    - Suggest: `الحماية الموسّعة من التعقب`
    - The same feature name should be rendered the same way across ETP settings. The preference title uses "الحماية الموسّعة من التعقب".
- `preferences_passwords_saved_logins_description_empty_learn_more_link_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Sync is rendered as «التزامن» (simultaneity/concurrency) instead of «المزامنة», the term used for Sync in the surrounding strings.
    - Current: `حول التزامن`
    - Source: `Learn more about sync`
    - Suggest: `حول المزامنة`
    - The comment says this is about the Sync feature. The neighbouring strings render sync as «مزامنة» («مزامنة كلمات المرور», «مزامنتها»). «التزامن» means 'synchronicity', not data syncing.
- `saved_login_password_required_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — This error message uses a noun ("entering a password") where the matching field errors tell the user to do something.
    - Current: `إدخال كلمة مرور`
    - Source: `Enter a password`
    - Suggest: `أدخل كلمة مرور`
    - The source "Enter a password" is an instruction. The matching messages for the username and web address fields are rendered "أدخل اسم مستخدم" and "أدخل عنوان ويب", so this one is inconsistent on the same screen.
- `setup_checklist_subtitle_5_steps_initial_state` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — "set up" is rendered as "install" (تثبيت), which doesn't match the 3- and 6-step versions that use إعداد.
    - Current: `لتثبيت %1$s`
    - Source: `Complete all 5 steps to set up %1$s for the best browsing experience.`
    - Suggest: `لإعداد %1$s`
    - The source means configuring an app that is already installed, not installing it. The matching 3- and 6-step strings correctly use لإعداد.
- `sync_reconnect` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Sync rendered as "التزامن" while other Sync strings use "«المزامنة»".
    - Current: `أعِد الاتصال بالتزامن`
    - Source: `Reconnect to Sync`
    - Suggest: `أعِد الاتصال بـ«المزامنة»`
    - Sync (the Firefox Sync service) is rendered as "«المزامنة»" in sync_sign_in and synced_tabs_sign_in_button; "التزامن" means synchronicity and is inconsistent on the same share dialog.
- `tabs_header_tab_group_counter_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Uses "لسان/الألسنة" for tab, where every other tab-tray string uses "تبويب/تبويبات", and "اضغط" where its siblings use "انقر".
    - Current: `مجموعة لسان مفتوحة. اضغط للتبديل بين الألسنة.`
    - Source: `{$quantity ->} [one] %1$d tab group open. Tap to switch tabs. [other] %1$d tab groups open. Tap to switch tabs.`
    - Suggest: `مجموعة تبويبات مفتوحة. انقر للانتقال بين التبويبات.`
    - The sibling counter strings (normal, private and synced tabs) say "التبويبات" and "انقر للانتقال بين التبويبات". Screen reader users get inconsistent terms on the same surface.
- `terms_of_use_prompt_message_2` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Addresses the user in the plural ("تأخذوا"), while the locale otherwise uses the singular.
    - Current: `نرجو أن تأخذوا`
    - Source: `Please take a moment to review and accept. %1$s.`
    - Suggest: `نرجو أن تأخذ`
    - Other strings address the user in the singular (يمكنك، تعرضها), so this plural form breaks the locale's established form of address.
- `unsubmitted_crash_dialog_positive_button` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — The button calls a crash report بلاغ انهيار, while the same dialog uses تقارير الأعطال.
    - Current: `أرسِل بلاغ انهيار`
    - Source: `Send crash report`
    - Suggest: `أرسِل تقرير العطل`
    - The same source term, crash report, appears as تقارير الأعطال in this dialog's body and checkbox. Using a different term on the button is inconsistent.

### E. Typography, punctuation & spacing

- `mozac_feature_addons_permissions_content_description_item` — `mozilla-mobile/android-components/components/feature/addons/src/main/res/values-ar/strings.xml` — There is an extra comma between the position number and "of" (من).
    - Current: `%2$d، من`
    - Source: `%1$s, %2$d of %3$d`
    - Suggest: `%2$d من`
    - The source is '%1$s, %2$d of %3$d'. The translation puts a comma after the position, so the screen reader reads '2, of 6' and breaks up the phrase.
- `mozac_feature_downloads_time_remaining` — `mozilla-mobile/android-components/components/feature/downloads/src/main/res/values-ar/strings.xml` — There is no space between the preposition "في" and the time-remaining value.
    - Current: `في%1$s`
    - Source: `in %1$s`
    - Suggest: `في %1$s`
    - The source has a space ("in %1$s"). Without it the text renders as "في5 دقائق", with the preposition stuck to the time value.
- `close_tab_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Uses curly quotes around the tab title where the locale convention is straight double quotes.
    - Current: `”%s“`
    - Source: `Close tab %s`
    - Suggest: `"%s"`
    - The locale's established quote style is straight double quotes.
- `download_item_in_progress_description_pending` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — Missing space after the slash between downloaded size and total size.
    - Current: `%1$s /%2$s`
    - Source: `%1$s / %2$s • pending`
    - Suggest: `%1$s / %2$s`
    - The source has a space on both sides of the slash ("%1$s / %2$s"), and the other progress strings in this locale keep that spacing. Here the space after the slash is missing in visible text.
- `preference_enhanced_tracking_protection_allow_list_dialog_title` — `mozilla-mobile/fenix/app/src/main/res/values-ar/strings.xml` — There is a doubled space between "تريد" and "تعطيل".
    - Current: `تريد  تعطيل`
    - Source: `Are you sure you want to turn off fixes?`
    - Suggest: `تريد تعطيل`
    - The extra space is visible to users in the dialog title.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ar/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

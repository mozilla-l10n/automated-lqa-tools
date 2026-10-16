# Firefox l10n QA — ar

| | |
|---|---|
| **Generated** | 2026-10-16 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `db2cfca9d18c` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `af4e7312bee1` |
| **Previous run** | 2026-10-16 @ `db2cfca9d18c` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 13,329 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.




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
| Files | 323 |
| Strings | 13,329 |
| Missing strings | 3,187 |
| Obsolete strings | 0 |
| Files absent from the locale | 5 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 12 |
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 6 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 13 |

### Completeness

**3,187 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 358
- `dom/chrome/dom/dom.properties` — 214
- `browser/browser/aiWindow.ftl` — 161
- `devtools/client/tooltips.ftl` — 98
- `dom/chrome/layout/htmlparser.properties` — 94
- `devtools/client/netmonitor.properties` — 92
- `devtools/client/debugger.properties` — 83
- `dom/chrome/security/security.properties` — 81
- `browser/browser/ipProtection.ftl` — 80
- `toolkit/toolkit/about/aboutGlean.ftl` — 66
- `toolkit/toolkit/about/aboutSupport.ftl` — 66
- `toolkit/toolkit/about/aboutWebauthn.ftl` — 66

**Files absent from the locale:**

- `browser/browser/autoTabGrouping.ftl`
- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/about/pdfFeaturesNotification.ftl`
- `toolkit/toolkit/global/viewSource.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 96, `curly-double` 74, `curly-single` 9, `guillemet` 3 | _mixed_ |
| apostrophe | `typographic` 55 | **typographic** |
| ellipsis | `char` 366, `ascii` 13 | **char** |
| dash | `em` 35 | **em** |
| nbsp | `total` 160, `space-before-punctuation` 3 | **total** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (345)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 200 |
| 2 | Wrong content (says something other than the English) | 114 |
| 3 | Degraded language (grammar, spelling, terminology) | 19 |
| 4 | Cosmetic (typography, spacing) | 12 |

### A. Functional, markup, variables & plurals

- `about-logins-error-message-duplicate-login-with-link` — `browser/browser/aboutLogins.ftl` — The variable holding the website title is presented as the username, reversing what the message tells the user.
    - Current: `جلسة الولوج باسم المستخدم { $loginTitle } موجودة.`
    - Source: `An entry for { $loginTitle } with that username already exists. <a data-l10n-name="duplicate-link">Go to existing entry?</a>`
    - Suggest: `يوجد بالفعل مُدخل لـ { $loginTitle } بنفس اسم المستخدم.`
    - The developer comment states “$loginTitle - The title of the website associated with the login”, and en-US reads “An entry for { $loginTitle } with that username already exists.” The Arabic labels the website title as the username, so the user is told a username exists that is in fact a site name.
- `about-private-browsing-cookie-banners-promo-body` — `browser/browser/aboutPrivateBrowsing.ftl` — “so you can get tracked less” is rendered as “so you can track yourself less”.
    - Current: `حتى تتمكن من تتبعك بشكل أقل`
    - Source: `We now automatically refuse many cookie banners so you can get tracked less and go back to distraction-free browsing.`
    - Suggest: `حتى يقلّ تعقّبك`
    - en-US says the user gets tracked less (passive); the Arabic makes the user the agent of the tracking, which is not what the sentence states.
- `account-multiple-tabs-arriving-from-multiple-devices` — `browser/browser/accounts.ftl` — `account-multiple-tabs-arriving-from-multiple-devices` is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] وصل لسان من أجهزتك المتصلة [two] وصل لسانان من أجهزتك المتصلة [few] وصلت { $tabCount } ألسنة من أجهزتك المتصلة [many] وصل { $tabCount } لسانًا من أجهزتك المتصلة [other] وصل { $tabCount } لسان من أجه…`
    - Source: `{$tabCount ->} [one] { $tabCount } tab has arrived from your connected devices [other] { $tabCount } tabs have arrived from your connected devices`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `account-multiple-tabs-arriving-from-single-device` — `browser/browser/accounts.ftl` — `account-multiple-tabs-arriving-from-single-device` is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] وصل لسان من { $deviceName } [two] وصل لسانان من { $deviceName } [few] وصلت { $tabCount } ألسنة من { $deviceName } [many] وصل { $tabCount } لسانًا من { $deviceName } [other] وصل { $tabCount } لسانًا…`
    - Source: `{$tabCount ->} [one] { $tabCount } tab has arrived from { $deviceName } [other] { $tabCount } tabs have arrived from { $deviceName }`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `account-multiple-tabs-arriving-from-unknown-device` — `browser/browser/accounts.ftl` — `account-multiple-tabs-arriving-from-unknown-device` is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] وصل لسان [two] وصل لسانان [few] وصلت { $tabCount } ألسنة [many] وصل { $tabCount } لسانًا [other] وصل { $tabCount } لسان`
    - Source: `{$tabCount ->} [one] { $tabCount } tab has arrived [other] { $tabCount } tabs have arrived`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `account-multiple-tabs-arriving-title` — `browser/browser/accounts.ftl` — The multiple-tabs notification title is singular, identical to the single-tab title.
    - Current: `وصل لسان`
    - Source: `Tabs Received`
    - Suggest: `وصلت ألسنة`
    - en-US is “Tabs Received” (plural) and is used only when several tabs arrive; the Arabic duplicates the singular string used for account-single-tab-arriving-title.
- `xpinstall-prompt-never-allow-and-report` — `browser/browser/addonNotifications.ftl` — Access key `إ` of `xpinstall-prompt-never-allow-and-report` is not present in its label
    - Current: `إ`
    - Source: `accesskey: R label: Report Suspicious Site`
    - The label is “أبلغ عن موقع مشبوه”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `smart-window-ungrouped-row-label` — `browser/browser/aiWindowContent.ftl` — “Ungrouped N tabs” is rendered as “N tabs were cancelled”, losing the grouping action.
    - Current: `أُلغيَ لسان واحد`
    - Source: `{$count ->} [one] Ungrouped { $count } tab [other] Ungrouped { $count } tabs`
    - Suggest: `أُلغي تجميع لسان واحد`
    - en-US “Ungrouped { $count } tab” refers to removing tabs from a group; “أُلغيَ لسان” says the tab itself was cancelled, and the [zero] variant “لا ألسنة لإلغائها” compounds this.
- `backup-file-name` — `browser/browser/backupSettings.ftl` — A generated file name is translated as an imperative sentence.
    - Current: `اعمل نسخة احتياطية إلى { -brand-product-name }`
    - Source: `{ -brand-product-name }Backup`
    - Suggest: `نسخة-{ -brand-product-name }-الاحتياطية`
    - The developer comment says this string is the generated backup file name, to which the profile name, date and “.html” are appended; en-US is the noun compound “{ -brand-product-name }Backup”. The Arabic renders it as the command “Make a backup to Firefox”.
- `trustpanel-social-tracking-blocking-tab-header` — `browser/browser/browser.ftl` — “social media tracker” is rendered as “media tracker”.
    - Current: `{ -brand-product-name } حظر { $count } متعقِّب وسائط`
    - Source: `{$count ->} [one] { -brand-product-name } blocked { $count } social media tracker [other] { -brand-product-name } blocked { $count } social media trackers`
    - Suggest: `{ -brand-product-name } حظر { $count } متعقِّب وسائل تواصل اجتماعي`
    - en-US says “social media tracker”; the same file renders the term correctly as “متعقّب وسائل التواصل الاجتماعي” in trustpanel-list-label-social-tracking, so “وسائط” names a different category.
- `clear-data-for-site-cache` — `browser/browser/clearDataForSite.ftl` — “Cached pages” is rendered as “newspapers”.
    - Current: `الملفات والصحف المخبّأة`
    - Source: `Cached files and pages`
    - Suggest: `الملفات والصفحات المخبّأة`
    - en-US is “Cached files and pages”; “الصحف” means newspapers, not web pages, so the dialog misstates what will be cleared.
- `confirmation-hint-password-updated` — `browser/browser/confirmationHints.ftl` — “Password updated” is rendered with a verb meaning “spoke/talked”.
    - Current: `تحدّثت كلمة السر`
    - Source: `Password updated`
    - Suggest: `حُدِّثت كلمة السر`
    - “تحدّثت” is the verb “to speak”; the passive of “update” is “حُدِّثت”, as used in confirmation-hint-address-updated and confirmation-hint-credit-card-updated in the same file.
- `customize-mode-uidensity-menu-compact-unsupported` — `browser/browser/customizeMode.ftl` — Access key `C` of `customize-mode-uidensity-menu-compact-unsupported` is not present in its label
    - Current: `C`
    - Source: `accesskey: C label: Compact (not supported) tooltiptext: Compact (not supported)`
    - The label is “الدمج (غير مدعوم)”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `customkeys-nav-home` — `browser/browser/customkeys.ftl` — The Home button is translated as the word for a dwelling.
    - Current: `المنزل`
    - Source: `Home`
    - Suggest: `البداية`
    - “Home” here is the browser home page shortcut; appmenu.ftl and browser.ftl render it “البداية”. “المنزل” names a house and does not identify the command.
- `customkeys-view-separate-split-view` — `browser/browser/customkeys.ftl` — An action label is rendered as a noun phrase, contrary to the developer comment.
    - Current: `عرض مقسم منفصل`
    - Source: `Separate Split View`
    - Suggest: `افصل العرض المنقسم`
    - The comment says “Separate is a verb”; the Arabic reads “a separate split view”, naming a thing instead of the action, and also spells it “مقسم” where the rest of the file uses “منقسم”.
- `splitview-onboarding-callout-subtitle-1` — `browser/browser/featureCallout.ftl` — “see two tabs at once” is rendered as “view the tab at once”, dropping the number.
    - Current: `لعرض اللسان في وقتٍ واحد`
    - Source: `Right-click this tab and choose “Add Split View” to see two tabs at once.`
    - Suggest: `لعرض لسانين في وقتٍ واحد`
    - The whole point of split view is showing two tabs simultaneously; splitview-onboarding-callout-title-2 in the same file keeps “لسانين”.
- `windows-10-eos-sync-urgency-subtitle-1` — `browser/browser/featureCallout.ftl` — “{ -brand-short-name } settings” becomes “the settings of your brand”, and “Sync now” is misspelled.
    - Current: `مزامن الآن للحفاظ على علاماتك وكلمات سرك والإعدادات الخاصة بعلامتك التجارية { -brand-short-name } آمنة`
    - Source: `Sync now to keep your { -brand-short-name } bookmarks, passwords, and settings safe and easy to restore.`
    - Suggest: `زامِن الآن للحفاظ على علاماتك وكلمات سرك وإعدادات { -brand-short-name } آمنة`
    - en-US is “Sync now to keep your { -brand-short-name } bookmarks, passwords, and settings safe”. The Arabic reads the placeholder as the user's own commercial brand (“علامتك التجارية”), inventing a possession the product never mentions, and “مزامن” is not the imperative “زامِن”.
- `ip-protection-bandwidth-left-this-month-mb` — `browser/browser/ipProtection.ftl` — The megabyte figure is labelled as gigabytes.
    - Current: `{ $usageLeft } ج.بايت من أصل { $maxUsage } ج.بايت متبقية في هذا الشهر`
    - Source: `{ $usageLeft } MB of { $maxUsage } GB left this month`
    - Suggest: `{ $usageLeft } م.بايت من أصل { $maxUsage } ج.بايت متبقية في هذا الشهر`
    - The developer comment states $usageLeft is in MB and en-US reads “{ $usageLeft } MB of { $maxUsage } GB left this month”; using ج.بايت overstates the remaining data by a factor of 1000.
- `ipprotection-button-turn-vpn-off` — `browser/browser/ipProtection.ftl` — A button that turns the VPN off is labelled as a status reading “VPN is off”.
    - Current: `ال VPN متوقف`
    - Source: `Turn off VPN`
    - Suggest: `أوقِف VPN`
    - The developer comment says “Button to turn off the VPN” and en-US is “Turn off VPN”. The Arabic states the current state instead of the action, and since the button only appears while the VPN is on, it asserts the opposite of the truth. ipprotection-button-turn-vpn-off-excluded-site has the same problem.
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — Access key `ق` of `menu-help-share-ideas` is not present in its label
    - Current: `ق`
    - Source: `accesskey: S label: Share Ideas and Feedback…`
    - The label is “شارك الأفكار والانطباعات...”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `migration-no-permissions-message` — `browser/browser/migrationWizard.ftl` — “other browsers’ profiles” rendered as “other browsers’ files”.
    - Current: `ملفات المتصفحات الأخرى المثبتة على هذا الجهاز`
    - Source: `{ -brand-short-name } does not have access to other browsers’ profiles installed on this device.`
    - Suggest: `الملفات الشخصية للمتصفحات الأخرى المثبتة على هذا الجهاز`
    - The en-US speaks of profiles, which is what the permission concerns; ملفات alone means files, and the next string correctly refers to مجلّد الملفّ الشّخصي.
- `cfr-doorhanger-feature-notification` — `browser/browser/newtab/asrouter.ftl` — The feature-recommendation notification announces an extension recommendation.
    - Current: `نُوصيك بامتداد`
    - Source: `(value): Recommendation a11y-announcement: Feature recommendation available tooltiptext: Feature recommendation`
    - Suggest: `نُوصيك بميزة`
    - en-US has .tooltiptext = “Feature recommendation” and .a11y-announcement = “Feature recommendation available”; the ar copies the extension-notification wording (امتداد) for both attributes, naming the wrong kind of recommendation.
- `newtab-section-following-button` — `browser/browser/newtab/newtab.ftl` — The “Following” state label is in the third person.
    - Current: `يتابع`
    - Source: `Following`
    - Suggest: `تتابِع`
    - en-US “Following” describes the user’s own state; “يتابع” reads as “he/it follows”, inconsistent with the second-person forms used in the neighbouring toast (أنت الآن تتابع { $topic }).
- `newtab-topic-selection-privacy-link` — `browser/browser/newtab/newtab.ftl` — The coordination is broken and leaves “data management” dangling.
    - Current: `تعرّف على كيف نحمي بياناتك وإدارة البيانات`
    - Source: `Learn how we protect and manage data`
    - Suggest: `تعرّف على كيفية حمايتنا للبيانات وإدارتها`
    - en-US: “Learn how we protect and manage data”; the ar coordinates a verbal clause with a bare noun phrase, so the sentence does not say that we manage the data.
- `fx100-upgrade-thanks-keep-body` — `browser/browser/newtab/onboarding.ftl` — “Keep Firefox one click away” is rendered as “keep Firefox away”, and “الإصدار رفم” is a typo.
    - Current: `هذا الإصدار  رفم 100! شكرا لكونك طرفا في مجتمعنا. أبق { -brand-short-name } بعيدا بنقرة واحدة لأجل ال100 القادمة.`
    - Source: `It’s our 100th release! Thanks for being a part of our community. Keep { -brand-short-name } one click away for the next 100.`
    - Suggest: `هذا الإصدار رقم 100! شكرا لكونك طرفا في مجتمعنا. أبقِ { -brand-short-name } على بعد نقرة واحدة لأجل الـ100 القادمة.`
    - “رفم” should be “رقم”; and “أبقِ … بعيدًا” reads as “keep it away”, the opposite of the source’s “one click away” (rendered elsewhere in the tree as “على بعد نقرة واحدة”).
- `origin-controls-state-always-on` — `browser/browser/originControls.ftl` — Subject changed from the extension to the user: “you can always read and change data”.
    - Current: `يمكنك دائمًا قراءة البيانات وتغييرها على هذا الموقع`
    - Source: `Can always read and change data on this site`
    - Suggest: `يمكنه دائمًا قراءة البيانات وتغييرها على هذا الموقع`
    - The string describes what the extension is permitted to do; origin-controls-state-temporary-access correctly uses يمكنه. As written it tells the user they themselves may read and change site data.
- `places-bookmarks-search` — `browser/browser/places.ftl` — “Search bookmarks” rendered as the noun phrase “bookmarks of the search”.
    - Current: `علامات البحث`
    - Source: `placeholder: Search bookmarks`
    - Suggest: `ابحث في العلامات`
    - Same reversal as places-history-search; places-search-bookmarks in the same file correctly uses ابحث في العلامات.
- `places-history-search` — `browser/browser/places.ftl` — “Search history” (a verb phrase) rendered as the noun phrase “the history of the search”.
    - Current: `تأريخ البحث`
    - Source: `placeholder: Search history`
    - Suggest: `ابحث في التأريخ`
    - The section comment states “Search History” stands for “Search through the browser's history”; the sibling places-search-history correctly uses ابحث في التأريخ, so this placeholder reverses the head noun.
- `places-share-folder2` — `browser/browser/places.ftl` — “Share Folder” translated as “share a file”.
    - Current: `شارك ملف`
    - Source: `badge: New label: Share Folder`
    - Suggest: `شارك المجلد`
    - The developer comment says this shares the bookmark “Folder”; ملف means file, not folder (مجلد is used for Folder everywhere else in the file).
- `places-bookmarks-restore-alert-title` — `browser/browser/placesPrompts.ftl` — “Revert Bookmarks” translated as “invert/reverse the bookmarks”.
    - Current: `اعكس العلامات`
    - Source: `Revert Bookmarks`
    - Suggest: `استعِد العلامات`
    - اعكس means reverse/flip direction (it is used for “Switch Text Direction” in menubar.ftl); the dialog restores bookmarks from a backup.
- `autofill-address-county` — `browser/browser/preferences/formAutofill.ftl` — “County” translated as “البلد” (country), colliding with the Country field
    - Current: `البلد`
    - Source: `County`
    - Suggest: `المقاطعة`
    - “County” is an administrative subdivision, not a country; the same form already uses “البلد” for autofill-address-country-only, so two distinct fields carry the identical, wrong label.
- `autofill-address-post-town` — `browser/browser/preferences/formAutofill.ftl` — “Post town” rendered as the verb “أنزل” (download/lower), not an address field label
    - Current: `أنزل`
    - Source: `Post town`
    - Suggest: `المدينة البريديّة`
    - The developer comment says this is a secondary address level used in GB/NO/SE. “أنزل” is an imperative verb meaning “download/bring down” and is not an address label at all; the user sees a nonsensical field name.
- `autofill-address-townland` — `browser/browser/preferences/formAutofill.ftl` — “Townland” rendered as the generic “الأرض” (the land)
    - Current: `الأرض`
    - Source: `Townland`
    - Suggest: `البلدة الريفيّة`
    - The comment marks this as an Irish sublocality (a named rural land division); “الأرض” just means “land” and does not identify an address level, leaving the field label meaningless next to المدينة/الحي.
- `autofill-card-invalid-number` — `browser/browser/preferences/formAutofill.ftl` — Validation error asks for a valid card *name* instead of a valid card *number*
    - Current: `رجاءً أدخِل اسم بطاقة سليم`
    - Source: `Please enter a valid card number`
    - Suggest: `رجاءً أدخِل رقم بطاقة سليمًا`
    - en-US is “Please enter a valid card number”. The error appears under the card-number field, so telling the user to fix the name misdirects them.
- `containers-disable-alert-desc` — `browser/browser/preferences/preferences.ftl` — `containers-disable-alert-desc` is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] إذا عطلت الألسنة الحاوية الآن فسيغلق لسان حاو. أمتأكد أنك تريد تعطيل الألسنة الحاوية؟ [two] إذا عطلت الألسنة الحاوية الآن فسيغلق لسانين حاويين. أمتأكد أنك تريد تعطيل الألسنة الحاوية؟ [few] إذا عطلت…`
    - Source: `{$tabCount ->} [one] If you disable Container Tabs now, { $tabCount } container tab will be closed. Are you sure you want to disable Container Tabs? [other] If you disable Container Tabs now, { $tabCount } container tab…`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `containers-disable-alert-ok-button` — `browser/browser/preferences/preferences.ftl` — `containers-disable-alert-ok-button` is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] أغلق اللسان الحاوي [two] أغلق اللسانين الحاويين [few] أغلق { $tabCount } ألسنة حاوية [many] أغلق { $tabCount } لسانًا حاويًا [other] أغلق { $tabCount } لسان حاو`
    - Source: `{$tabCount ->} [one] Close { $tabCount } Container Tab [other] Close { $tabCount } Container Tabs`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `containers-remove-alert-msg` — `browser/browser/preferences/preferences.ftl` — `containers-remove-alert-msg` is missing the ['zero'] plural form
    - Current: `{$count ->} [one] إذا أزلت هذه الحاوية الآن فسيغلق لسان حاو. أمتأكد أنك تريد إزالة هذه الحاوية؟ [two] إذا أزلت هذه الحاوية الآن فسيغلق لسانين حاويين. أمتأكد أنك تريد إزالة هذه الحاوية؟ [few] إذا أزلت هذه الحاوية الآن فس…`
    - Source: `{$count ->} [one] If you remove this Container now, { $count } container tab will be closed. Are you sure you want to remove this Container? [other] If you remove this Container now, { $count } container tabs will be cl…`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `permissions-block-popups2` — `browser/browser/preferences/preferences.ftl` — Access key `ظ` of `permissions-block-popups2` is not present in its label
    - Current: `ظ`
    - Source: `accesskey: B label: Block pop-ups and third-party redirects`
    - The label is “احجب النوافذ المنبثقة وعمليات إعادة التوجيه من جهات خارجية”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `sync-engine-payment-methods2` — `browser/browser/preferences/preferences.ftl` — Access key `n` of `sync-engine-payment-methods2` is not present in its label
    - Current: `n`
    - Source: `accesskey: n label: Payment methods tooltiptext: Names, card numbers, and expiry dates`
    - The label is “طرق الدفع”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `delete-profile-autofill` — `browser/browser/profiles.ftl` — “Autofill data” (a list item) rendered as a misspelled imperative “fill in automatically the data”.
    - Current: `املء آليًا البيانات (العناوين، طُرق الدفع)`
    - Source: `Autofill data (addresses, payment methods)`
    - Suggest: `بيانات الملء الآلي (العناوين، طُرق الدفع)`
    - This is a row label in the delete-profile table listing data categories, not a command; املء is also a misspelling of املأ. migrationWizard uses بيانات الملء الآلي for the same term.
- `new-profile-page-done-button` — `browser/browser/profiles.ftl` — “Done editing” rendered as the passive verb “was edited”.
    - Current: `حُرِّر`
    - Source: `label: Done editing`
    - Suggest: `تمّ التحرير`
    - The button confirms the user has finished editing; حُرِّر states that something was edited, not that editing is finished.
- `lockwise-scanned-text-breached-logins` — `browser/browser/protections.ftl` — “may have been exposed in a data breach” stated as a fact: “appeared in a data breach”.
    - Current: `ظهرت كلمة سر واحدة في تسرّب بيانات.`
    - Source: `{$count ->} [one] 1 password may have been exposed in a data breach. [other] { $count } passwords may have been exposed in a data breach.`
    - Suggest: `ربما ظهرت كلمة سر واحدة في تسرّب بيانات.`
    - The en-US hedges with “may have been exposed”; the Arabic asserts the exposure happened, which changes a possibility reported by the dashboard into a confirmed breach of the user's password.
- `protections-panel-cookie-banner-blocker-view-turn-on-description` — `browser/browser/protectionsPanel.ftl` — “Turn on and { -brand-short-name } will try…” rendered as “Turn on { -brand-short-name } and it will try…”.
    - Current: `شغّل { -brand-short-name } وسيحاول رفض لافتات`
    - Source: `Turn on and { -brand-short-name } will try to automatically refuse cookie banners on this site.`
    - Suggest: `شغّل الميزة وسيحاول { -brand-short-name } رفض لافتات`
    - The user is asked to turn on the cookie-banner blocker, not to start the browser; the Arabic makes the brand the object of the imperative.
- `protections-panel-cookie-banner-blocker-view-turn-on-for-site` — `browser/browser/protectionsPanel.ftl` — “for this site” rendered as “for this link”.
    - Current: `أشغل مانع لافتات ملفات تعريف الارتباط لهذا الرابط؟`
    - Source: `Turn on Cookie Banner Blocker for this site?`
    - Suggest: `أشغل مانع لافتات الكعكات لهذا الموقع؟`
    - الرابط means link; the setting applies to the site, as the paired turn-off string and the en-US both say.
- `protections-panel-cookie-banner-handling-enabled` — `browser/browser/protectionsPanel.ftl` — Status “On for this site” rendered as the command “enable it for this site”.
    - Current: `فعله لهذا الموقع`
    - Source: `On for this site`
    - Suggest: `مُفعّل لهذا الموقع`
    - This string reports the current state (the paired -disabled string has the same problem with عطله); the toggle descriptions elsewhere in the panel correctly use مُفعّل/مُعطّل لهذا الموقع.
- `auto-safe-mode-description` — `browser/browser/safeMode.ftl` — “other problems” rendered as “other programs”.
    - Current: `أحد الإضافات أو البرامج الأخرى`
    - Source: `{ -brand-short-name } closed unexpectedly while starting. This might be caused by add-ons or other problems. You can try to resolve the problem by troubleshooting in Safe Mode.`
    - Suggest: `أحد الإضافات أو مشاكل أخرى`
    - The en-US says the crash might be caused by add-ons or other problems; البرامج names software instead.
- `protections-header` — `browser/browser/siteProtections.ftl` — “Protections for { $host }” reads as “protection levels from { $host }”.
    - Current: `مستويات الحماية من { $host }`
    - Source: `Protections for { $host }`
    - Suggest: `الحماية في { $host }`
    - من reverses the relation — it suggests protection against the host — and مستويات (levels) is not in the source; the panel header labels the protections applied on that site.
- `protections-not-blocking-cookies-all` — `browser/browser/siteProtections.ftl` — “Not Blocking Cookies” narrowed to “tracking cookies”, duplicating another row.
    - Current: `الكعكات المتعقِّبة - غير محجوبة`
    - Source: `title: Not Blocking Cookies`
    - Suggest: `كل الكعكات - غير محجوبة`
    - This is the all-cookies category (protections-blocking-cookies-all is كل الكعكات); as translated it names the tracking-cookie category, which already has its own row (protections-not-blocking-cross-site-tracking-cookies).
- `move-to-new-profile` — `browser/browser/tabContextMenu.ftl` — “Move to { $profileName }” rendered as “Go to { $profileName }”.
    - Current: `انتقل إلى { $profileName }`
    - Source: `label: Move to { $profileName }`
    - Suggest: `انقل إلى { $profileName }`
    - The command moves the tab to another profile; the neighbouring move-to-start/end/new-window items all use انقل إلى, while انتقل tells the user to navigate.
- `split-view-menuitem-separate-tabs` — `browser/browser/tabbrowser.ftl` — “Separate Tabs” (verb) rendered as the noun phrase “separate tabs”.
    - Current: `ألسنة منفصلة`
    - Source: `label: Separate Tabs`
    - Suggest: `افصل الألسنة`
    - The developer comment states “Separate” is a verb, as in separate the split view tabs; the translation turns the command into a description.
- `tab-context-separate-split-view` — `browser/browser/tabbrowser.ftl` — “Separate Split View” (verb) rendered as the noun phrase “a separate split view”.
    - Current: `عرض مقسم منفصل`
    - Source: `accesskey: t label: Separate Split View`
    - Suggest: `افصل العرض المنقسم`
    - The developer comment marks Separate as a verb; the item also writes مقسم where the rest of the file uses منقسم.
- `tab-group-context-open-saved-group-in-new-window` — `browser/browser/tabbrowser.ftl` — “Open Group in New Window” rendered as “Open in a new tab group”.
    - Current: `افتح في مجموعة لسان جديدة`
    - Source: `label: Open Group in New Window`
    - Suggest: `افتح المجموعة في نافذة جديدة`
    - The destination is a new window, not a new group; the sibling item correctly reads افتح المجموعة في هذه النافذة.
- `tabbrowser-close-tabs-button` — `browser/browser/tabbrowser.ftl` — `tabbrowser-close-tabs-button` (`.tooltiptext`) is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] أغلِق اللسان [two] أغلِق اللسانين [few] أغلِق { $tabCount } ألسنة [many] أغلِق { $tabCount } لسانًا [other] أغلِق { $tabCount } لسان`
    - Source: `tooltiptext: {$tabCount ->} [one] Close tab [other] Close { $tabCount } tabs`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `tabbrowser-confirm-caretbrowsing-message` — `browser/browser/tabbrowser.ftl` — “F7 turns Caret Browsing on or off” rendered as “F7 disables Caret Browsing”.
    - Current: `ضغط F7 يعطّل التصفّح بالمؤشّر`
    - Source: `Pressing F7 turns Caret Browsing on or off. This feature places a moveable cursor in web pages, allowing you to select text with the keyboard. Do you want to turn Caret Browsing on?`
    - Suggest: `ضغط F7 يفعّل التصفّح بالمؤشّر أو يعطّله`
    - The dialog explains that the key toggles the feature, and the same dialog then asks whether to turn it on; stating only “disables” misdescribes what the shortcut does.
- `tabbrowser-mute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-mute-tab-audio-background-tooltip` (`.label`) is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] اكتم اللسان [two] اكتم اللسانين [few] اكتم { $tabCount } ألسنة [many] اكتم { $tabCount } لسانًا [other] اكتم { $tabCount } لسان`
    - Source: `label: {$tabCount ->} [one] Mute tab [other] Mute { $tabCount } tabs`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `tabbrowser-mute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-mute-tab-audio-tooltip` (`.label`) is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] اكتم اللسان ({ $shortcut }) [two] اكتم اللسانين ({ $shortcut }) [few] اكتم { $tabCount } ألسنة ({ $shortcut }) [many] اكتم { $tabCount } لسانًا ({ $shortcut }) [other] اكتم { $tabCount } لسان ({ $sh…`
    - Source: `label: {$tabCount ->} [one] Mute tab ({ $shortcut }) [other] Mute { $tabCount } tabs ({ $shortcut })`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `tabbrowser-unblock-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-unblock-tab-audio-tooltip` (`.label`) is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] شغِّل اللسان [two] شغِّل اللسانين [few] شغِّل { $tabCount } ألسنة [many] شغِّل { $tabCount } لسانًا [other] شغِّل { $tabCount } لسان`
    - Source: `label: {$tabCount ->} [one] Play tab [other] Play { $tabCount } tabs`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `tabbrowser-unmute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-unmute-tab-audio-background-tooltip` (`.label`) is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] أطلِق صوت اللسان [two] أطلِق صوت اللسانين [few] أطلِق صوت { $tabCount } ألسنة [many] أطلِق صوت { $tabCount } لسانًا [other] أطلِق صوت { $tabCount } لسان`
    - Source: `label: {$tabCount ->} [one] Unmute tab [other] Unmute { $tabCount } tabs`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — `tabbrowser-unmute-tab-audio-tooltip` (`.label`) is missing the ['zero'] plural form
    - Current: `{$tabCount ->} [one] أطلِق صوت اللسان ({ $shortcut }) [two] أطلِق صوت اللسانين ({ $shortcut }) [few] أطلِق صوت { $tabCount } ألسنة ({ $shortcut }) [many] أطلِق صوت { $tabCount } لسانًا ({ $shortcut }) [other] أطلِق صوت…`
    - Source: `label: {$tabCount ->} [one] Unmute tab ({ $shortcut }) [other] Unmute { $tabCount } tabs ({ $shortcut })`
    - This locale uses ['few', 'many', 'one', 'other', 'two', 'zero'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `unified-extensions-item-messagebar-softblocked2` — `browser/browser/unifiedExtensions.ftl` — “is restricted” rendered as “is blocked”.
    - Current: `محظور. قد يكون استخدامه محفوفًا بالمخاطر.`
    - Source: `{ $extensionName } is restricted. Using it may be risky.`
    - Suggest: `مقيّد. قد يكون استخدامه محفوفًا بالمخاطر.`
    - This bar is shown for an extension the user has re-enabled and is still using, so محظور (blocked/banned) overstates the state; unified-extensions-mb-blocklist-warning-single2 uses مقيدة for the same English word.
- _…and 70 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `newtab-clock-city-pk-karachi` — `browser/browser/newtab/newtab.ftl` — Karachi is misspelled in Arabic.
    - Current: `كراجي`
    - Source: `Karachi`
    - Suggest: `كراتشي`
    - The standard Arabic spelling of the Pakistani city Karachi is كراتشي; كراجي is not the city’s name.
- `ForgotFileEnctypeWarning` — `dom/chrome/layout/HtmlForm.properties` — Space inserted inside the code value “multipart/form-data”.
    - Current: `enctype=multipart /form-data`
    - Source: `Form contains a file input, but is missing method=POST and enctype=multipart/form-data on the form.  The file will not be sent.`
    - Suggest: `enctype=multipart/form-data`
    - The en-US token is the literal HTML enctype value and must not be altered; the inserted space makes the value shown to the author invalid.
- `PEPseudoSelBadName` — `dom/chrome/layout/css.properties` — Keyword typo: “seudo-class” missing its initial p.
    - Current: `معرّفا ل‍ seudo-class أو pseudo-element`
    - Source: `Expected identifier for pseudo-class or pseudo-element but found ‘%1$S’.`
    - Suggest: `معرّفا ل‍ pseudo-class أو pseudo-element`
    - en-US: “Expected identifier for pseudo-class or pseudo-element…”. The CSS term is misspelled in the ar, unlike the correct ”pseudo-element“ beside it and PEPseudoSelUnknown.
- `39` — `dom/chrome/layout/xmlparser.properties` — Reserved prefix named as (xml) instead of (xmlns).
    - Current: `السّابقة المحجوزة (xml) يجب ألّا يصرّح عنها أو يلغى تصريحها`
    - Source: `reserved prefix (xmlns) must not be declared or undeclared`
    - Suggest: `السّابقة المحجوزة (xmlns) يجب ألّا يصرّح عنها أو يلغى تصريحها`
    - en-US error 39 is “reserved prefix (xmlns) must not be declared or undeclared”; error 38 is the (xml) one. Naming the wrong prefix points the author at the wrong code.

### C. Grammar, agreement & spelling

- `genai-onboarding-chatgpt-tooltip` — `browser/browser/genai.ftl` — The ChatGPT brand name is miscapitalised.
    - Current: `chatGPT`
    - Source: `title: ChatGPT`
    - Suggest: `ChatGPT`
    - ChatGPT is a product name that must be reproduced as in en-US; genai-settings-chat-chatgpt-links in the same file writes it correctly.
- `migration-wizard-migrator-display-name-file-password-csv` — `browser/browser/migrationWizard.ftl` — File format acronym CSV misspelled as CVS.
    - Current: `كلمات السر من ملف CVS`
    - Source: `Passwords from CSV file`
    - Suggest: `كلمات السر من ملف CSV`
    - CSV is a format identifier that must not be altered; the same file writes CSV correctly in migration-passwords-from-file-csv-filter-title.
- `mr1-onboarding-theme-label-alpenglow` — `browser/browser/newtab/onboarding.ftl` — The Alpenglow theme name is translated although the developer comment says to keep it in English.
    - Current: `شفق ألبي (Alpenglow)`
    - Source: `Alpenglow`
    - Suggest: `Alpenglow`
    - The comment states: “‘Alpenglow’ here is the name of the theme, and should be kept in English.” The locale prepends an Arabic translation of the name.
- `mr2022-onboarding-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — “Mozilla Foundation” is transliterated as موزيلا instead of keeping the Mozilla brand in Latin script.
    - Current: `مدعوم من مؤسسة موزيلا`
    - Source: `Thank you for using { -brand-short-name }, backed by the Mozilla Foundation. With your support, we’re working to make the internet more open, accessible, and better for everyone.`
    - Suggest: `مدعوم من مؤسسة Mozilla`
    - brand.ftl states the Mozilla brand cannot be transliterated or translated; the same screen family (onboarding-gratitude-security-and-privacy-subtitle) correctly writes “مؤسسة Mozilla”.
- `policy-AllowedDomainsForApps` — `browser/browser/policies/policies-descriptions.ftl` — The product name “Google Workspace” is translated/transliterated.
    - Current: `مساحة عمل جوجل`
    - Source: `Define domains allowed to access Google Workspace.`
    - Suggest: `Google Workspace`
    - Google Workspace is a brand name; neighbouring policy strings keep Microsoft Entra, PDF.js, SameSite etc. in Latin script.
- `policy-Windows10SSO` — `browser/browser/policies/policies-descriptions.ftl` — “Microsoft” is transliterated here but kept in Latin in the adjacent policy.
    - Current: `حسابات ميكروسوفت`
    - Source: `Allow Windows single sign-on for Microsoft, work, and school accounts.`
    - Suggest: `حسابات Microsoft`
    - The next entry, policy-MicrosoftEntraSSO, writes “Microsoft Entra” in Latin script; brand names should not be transliterated.
- `appearance-browser-icon-unlocked` — `browser/browser/preferences/browserIcon.ftl` — Definite article misplaced: “أيقونات الإضافية” is ungrammatical
    - Current: `لقد فتحت جميع أيقونات الإضافية!`
    - Source: `message: You unlocked all of the bonus icons!`
    - Suggest: `لقد فتحت جميع الأيقونات الإضافية!`
    - The noun must carry the definite article to agree with its adjective (الأيقونات الإضافية); as written the noun-adjective agreement is broken.
- `fonts-langgroup-cyrillic` — `browser/browser/preferences/fonts.ftl` — “Cyrillic” misspelled as “سريلي” (missing yāʾ)
    - Current: `سريلي`
    - Source: `label: Cyrillic`
    - Suggest: `سيريلي`
    - The script name is transliterated سيريلي / كيريلي in Arabic; “سريلي” drops a letter and reads as a non-word.
- `permissions-exceptions-saved-passwords-desc` — `browser/browser/preferences/permissions.ftl` — Typo: “يحفط” instead of “يحفظ”
    - Current: `لن يحفط`
    - Source: `{ -brand-short-name } won’t save passwords for sites listed here.`
    - Suggest: `لن يحفظ`
    - Letter ط typed for ظ; “يحفط” is not a word.
- `permissions-exceptions-shutdown-clearing-window` — `browser/browser/preferences/permissions.ftl` — Dialog title misspells “الاستثناءات” as “الاستثنائات”
    - Current: `الاستثنائات - امحُ التأريخ عند الإغلاق`
    - Source: `style: { permissions-window2.style } title: Exceptions - Clear History on Shutdown`
    - Suggest: `الاستثناءات - امحُ التأريخ عند الإغلاق`
    - Every other dialog title in the file spells it “الاستثناءات”; the hamza carrier here is wrong.
- `permissions-site-notification-desc` — `browser/browser/preferences/permissions.ftl` — Missing preposition in “السماح الإشعارات”
    - Current: `التي تطلب السماح الإشعارات`
    - Source: `The following websites have requested to send you notifications. You can specify which websites are allowed to send you notifications. You can also block new requests asking to allow notifications.`
    - Suggest: `التي تطلب السماح بالإشعارات`
    - السماح requires the preposition بـ; the phrase is ungrammatical as written (also repeated in permissions-site-notification-disable-label).
- `site-data-clear-all-prompt-text` — `browser/browser/preferences/siteDataSettings.ftl` — Typo: “مل الكعكات” instead of “كل الكعكات”
    - Current: `يمسح مل الكعكات`
    - Source: `Selecting ‘Clear Now’ will clear all cookies and site data stored by { -brand-short-name }. This may sign you out of websites and remove offline web content.`
    - Suggest: `يمسح كل الكعكات`
    - “مل” is not a word here; en-US says “will clear all cookies”.
- `add-engine-post-data` — `browser/browser/search.ftl` — The HTTP method POST is dropped and the field label turned into an imperative.
    - Current: `أرسل البيانات باستخدام %s بدلاً من مصطلح البحث`
    - Source: `POST data with %s in place of search term (leave empty for GET)`
    - Suggest: `بيانات POST مع %s بدلاً من مصطلح البحث`
    - The developer comment states POST and GET refer to the HTTP methods; GET is kept but POST is replaced by a verb, so the field no longer identifies which data it holds.
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — “Beta” translated although the comment says it must not be.
    - Current: `ترجم هذه الصفحة - تجريبي`
    - Source: `tooltiptext: Translate this page - Beta`
    - Suggest: `ترجم هذه الصفحة - Beta`
    - The developer comment states Beta should not be translated because it mirrors the un-localized BETA icon in the panel; urlbar-translations-button-intro has the same problem.
- `midi.shareSysexWithFile` — `browser/chrome/browser/browser.properties` — Technical term “SysEx” misspelled as “SynEx”
    - Current: `رسائل SynEx`
    - Source: `Allow this local file to access your MIDI devices and send/receive SysEx messages?`
    - Suggest: `رسائل SysEx`
    - SysEx is a MIDI protocol term that must be kept verbatim; the rest of the tree (sitePermissions.properties, extensions.ftl) correctly writes SysEx.
- `midi.shareSysexWithSite` — `browser/chrome/browser/browser.properties` — Technical term “SysEx” misspelled as “SynEx”
    - Current: `رسائل SynEx`
    - Source: `Allow %S to access your MIDI devices and send/receive SysEx messages?`
    - Suggest: `رسائل SysEx`
    - Same misspelling of the MIDI System Exclusive protocol term, which must not be altered; other files in the tree use SysEx.
- `clientSocketMisconfiguration` — `browser/chrome/overrides/appstrings.properties` — Brand name transliterated while the rest of the file keeps “Firefox” in Latin
    - Current: `لا يعرف فَيَرفُكس كيف يتصل بالخادوم.`
    - Source: `Firefox doesn’t know how to communicate with the server.`
    - Suggest: `لا يعرف Firefox كيف يتصل بالخادوم.`
    - Every other string in this file (fileNotFound, connectionFailure, netOffline, proxyResolveFailure, …) writes the brand as “Firefox”; this single transliteration is inconsistent within the same error-page surface.
- `ExecShell` — `browser/installer/override.properties` — The NSIS internal identifier “ExecShell” is translated as “install shell”.
    - Current: `قشرة التثبيت:`
    - Source: `"ExecShell: "`
    - Suggest: `ExecShell:`
    - “ExecShell” is the name of an NSIS instruction echoed in the installer log, like the neighbouring Exec/Extract entries; translating it as “قشرة التثبيت” both localizes a code identifier and states something the source does not.
- `htmlContent` — `dom/chrome/accessibility/mac/accessible.properties` — Misspelling “محتوي” for “محتوى”.
    - Current: `محتوي HTML`
    - Source: `HTML Content`
    - Suggest: `محتوى HTML`
    - The word is spelled with final yāʾ instead of alif maqṣūra; other files in the partition spell it ”محتوى“ (e.g. contentinfo = معلومات المحتوى).
- `basicHttpAuthDisabled` — `dom/chrome/appstrings.properties` — Garbled clause “قد يسرقة”.
    - Current: `قد يحاول شخصٌ ما انتحال هوية الموقع قد يسرقة معلوماتك.`
    - Source: `Someone pretending to be the site could try to steal your info. Your connection settings could also be set up incorrectly.`
    - Suggest: `قد يحاول شخصٌ ما انتحال هوية الموقع كي يسرق معلوماتك.`
    - en-US: “Someone pretending to be the site could try to steal your info.” ”قد يسرقة“ is not a valid verb form and leaves the two clauses unconnected.
- `proxyConnectFailure` — `dom/chrome/appstrings.properties` — Typo “لاتصال” for “الاتصال”.
    - Current: `رُفِض لاتصال أثناء محاولة الوصول`
    - Source: `The connection was refused when attempting to contact the proxy server you have configured. Please check your proxy settings and try again.`
    - Suggest: `رُفِض الاتصال أثناء محاولة الوصول`
    - Missing alif in the definite article; connectionFailure in the same file spells it ”رُفِض الاتصال“.
- `FormValidationTextTooLong` — `dom/chrome/dom/dom.properties` — Stray English “s” left on “حرفًاs”.
    - Current: `%S حرفًاs`
    - Source: `Please shorten this text to %S characters or less (you are currently using %S characters).`
    - Suggest: `%S حرفًا`
    - The English plural marker was left attached to the Arabic word, so the validation message shows ”حرفًاs“ to the user.
- `PointerLockDeniedNotInDocument` — `dom/chrome/dom/dom.properties` — “قفل” misspelled “فقل” in the pointer-lock messages.
    - Current: `رُفض طلب فقل المؤشر`
    - Source: `Request for pointer lock was denied because the requesting element is not in a document.`
    - Suggest: `رُفض طلب قفل المؤشر`
    - Letters transposed; PointerLockDeniedDisabled spells it correctly as ”قفل المؤشر“. The same typo appears in PointerLockDeniedHidden, PointerLockDeniedNotFocused and PointerLockDeniedMovedDocument.
- `SEC_ERROR_BAD_DATABASE` — `security/manager/chrome/pipnss/nsserrors.properties` — Misspelling of “سيئة”.
    - Current: `قاعدة بيانات شيئة`
    - Source: `security library: bad database.`
    - Suggest: `قاعدة بيانات سيئة`
    - ”شيئة“ is not a word; the file renders “bad” as ”سيئة“ elsewhere (e.g. SEC_ERROR_BAD_DATA).
- `SEC_ERROR_CANNOT_MOVE_SENSITIVE_KEY` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo “غلى” for “إلى”.
    - Current: `لا يمكن نقله غلى الفتحة`
    - Source: `A sensitive key cannot be moved to the slot where it is needed.`
    - Suggest: `لا يمكن نقله إلى الفتحة`
    - ”غلى“ is a misspelling of the preposition ”إلى“.
- `SEC_ERROR_INADEQUATE_KEY_USAGE` — `security/manager/chrome/pipnss/nsserrors.properties` — Misspelling of “الشهادة”.
    - Current: `استخدام مفتاح الشهاجة غير كاف لعملية المجرّبة.`
    - Source: `Certificate key usage inadequate for attempted operation.`
    - Suggest: `استخدام مفتاح الشهادة غير كافٍ للعملية المجرّبة.`
    - ”الشهاجة“ is a typo for ”الشهادة“; ”لعملية المجرّبة“ also lacks the definite article agreement (للعملية المجرّبة).
- `SEC_ERROR_LOCKED_PASSWORD` — `security/manager/chrome/pipnss/nsserrors.properties` — Misspelling of “كلمة السر”.
    - Current: `كلمة الصر مقفلة.`
    - Source: `The password is locked.`
    - Suggest: `كلمة السر مقفلة.`
    - ”الصر“ is a typo for ”السر“; every other occurrence in the file spells it ”كلمة السر“.
- `SSL_ERROR_ILLEGAL_PARAMETER_ALERT` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo: “غير قبول” for “غير مقبول”.
    - Current: `لأن محتواها غير قبول`
    - Source: `SSL peer rejected a handshake message for unacceptable content.`
    - Suggest: `لأن محتواها غير مقبول`
    - en-US: “…rejected a handshake message for unacceptable content.” ”قبول“ is a noun; the adjective ”مقبول“ is required.
- `SSL_ERROR_INAPPROPRIATE_FALLBACK_ALERT` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo “يدعك” for “يدعمه”.
    - Current: `أقل مما يدعك الخادوم`
    - Source: `The server rejected the handshake because the client downgraded to a lower TLS version than the server supports.`
    - Suggest: `أقل مما يدعمه الخادوم`
    - en-US: “…a lower TLS version than the server supports.” ”يدعك“ (leaves you) is a typo for ”يدعمه“ (supports it).
- `SSL_ERROR_SYM_KEY_UNWRAP_FAILURE` — `security/manager/chrome/pipnss/nsserrors.properties` — Space misplaced inside a word: “تبادلم فتاح”.
    - Current: `رسالة تبادلم فتاح العميل`
    - Source: `Failure to unwrap the Symmetric key in Client Key Exchange message.`
    - Suggest: `رسالة تبادل مفتاح العميل`
    - The space fell inside ”مفتاح“, producing two non-words; the same phrase is spelled correctly in SSL_ERROR_RX_MALFORMED_CLIENT_KEY_EXCH.
- `pageInfo_Privacy_Encrypted2` — `security/manager/chrome/pippki/pippki.properties` — Missing verbal noun leaves the sentence incomplete.
    - Current: `تصعّب التعمية غير المخوّلين على المعلومات المرسلة بين الحواسيب.`
    - Source: `Encryption makes it difficult for unauthorized people to view information traveling between computers. It is therefore unlikely that anyone read this page as it traveled across the network.`
    - Suggest: `تصعّب التعمية على غير المخوّلين الاطلاع على المعلومات المرسلة بين الحواسيب.`
    - en-US: “Encryption makes it difficult for unauthorized people to view information traveling between computers.” The ar omits ”الاطلاع“ and misplaces ”على“, so the clause has no predicate for what is made difficult.
- `send-no-client-certificate` — `security/manager/security/certificates/certManager.ftl` — Ungrammatical rendering of “Send no client certificate”.
    - Current: `أرسل لا شهادة العميل`
    - Source: `Send no client certificate`
    - Suggest: `لا ترسل أي شهادة عميل`
    - The negation is placed as a noun phrase (”أرسل لا شهادة“), which is not Arabic; the string is a user-selectable option meaning the browser should send no client certificate at all.
- `about-service-workers-title` — `toolkit/toolkit/about/aboutServiceWorkers.ftl` — The group comment states that "Service Workers" and "Workers" must not be translated, but the whole file renders them as "عمّال الخدمة".
    - Current: `عن عمّال الخدمة`
    - Source: `About Service Workers`
    - Suggest: `عن Service Workers`
    - The file-level comment `### The term "Service Workers" and "Workers" should not be translated` is explicit; the term is translated in the title, main title, warnings and unregister-error.
- `about-webauthn-auth-info-true` — `toolkit/toolkit/about/aboutWebauthn.ftl` — "True" is translated as "صحيح" against the developer comment, while the paired False stays in English.
    - Current: `صحيح`
    - Source: `True`
    - Suggest: `True`
    - The comment reads "True should not be translated"; about-webauthn-auth-info-false keeps "False".
- `about-webauthn-auth-option-true` — `toolkit/toolkit/about/aboutWebauthn.ftl` — "True" is translated as "صحيح" although the developer comment says True should not be translated, while the paired False is left in English.
    - Current: `صحيح`
    - Source: `True`
    - Suggest: `True`
    - The comment above the string reads "True should not be translated"; the adjacent about-webauthn-auth-option-false correctly keeps "False", so the pair now mixes a translated and an untranslated boolean.
- `-fakespot-brand-name` — `toolkit/toolkit/branding/brandings.ftl` — The brand name Fakespot is literally translated as "fake spot".
    - Current: `بقعة وهمية`
    - Source: `Fakespot`
    - Suggest: `Fakespot`
    - The file header states these feature names must be treated as a brand and cannot be translated or transliterated; every other entry in the file keeps the Latin brand, and -fakespot-website-name / -fakespot-brand-full-name keep "Fakespot".
- `-firefox-suggest-brand-name` — `toolkit/toolkit/branding/brandings.ftl` — The product name "Firefox Suggest" is rendered as the sentence "Firefox suggests".
    - Current: `يقترح Firefox`
    - Source: `Firefox Suggest`
    - Suggest: `اقتراحات Firefox`
    - The comment allows localizing "Suggest" but it is a feature name; يقترح is a finite verb, so the term reads as a statement about what Firefox does rather than as the name of the feature.
- `autofill-card-network-discover` — `toolkit/toolkit/formautofill/formAutofill.ftl` — The payment-card brand "Discover" is rendered as the verb "discover".
    - Current: `اكتشف`
    - Source: `Discover`
    - Suggest: `Discover`
    - The group comment says these are brand names, only to be translated when a locale-specific name is in common use; "اكتشف" is the imperative verb, not the card network, and neighbouring brands (JCB, MIR, Diners Club) are kept.
- `process-type-utility-actor-mf-media-engine` — `toolkit/toolkit/global/processTypes.ftl` — The Windows API name "Media Foundation" is translated as "multimedia organization".
    - Current: `محرك مؤسسة الوسائط المتعددة`
    - Source: `Utility Media Foundation Engine`
    - Suggest: `محرك Media Foundation`
    - "Media Foundation" is a Microsoft component name, not a foundation/organization; the adjacent string process-type-utility-actor-audio-decoder-wmf keeps "Windows Media Foundation" in English.

### D. Terminology, register & consistency

- `about-logins-import-report-row-description-modified2` — `browser/browser/aboutLogins.ftl` — Gender disagreement: feminine verb and adjective with the masculine noun “الولوج”.
    - Current: `حُدّثت الولوج الموجودة`
    - Source: `Existing entry updated`
    - Suggest: `حُدّث الولوج الموجود`
    - “الولوج” is masculine, so “حُدّثت … الموجودة” does not agree with it.
- `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl` — Misspelled hamza in “لإضافة”.
    - Current: `لاضافة`
    - Source: `Select the plus sign button above to add a password now. You can also <a data-l10n-name="import-browser-link">import passwords from another browser</a> or <a data-l10n-name="import-file-link">from a file</a>.`
    - Suggest: `لإضافة`
    - The word requires hamzat qatʿ under the alif (لإضافة); “لاضافة” is a spelling error.
- `about-unloads-intro` — `browser/browser/aboutUnloads.ftl` — “انهيار” misspelled with hamzat qatʿ, and the tab reference disagrees in gender.
    - Current: `لمنع إنهيار التطبيق`
    - Source: `{ -brand-short-name } has a feature that automatically unloads tabs to prevent the application from crashing due to insufficient memory when the system’s available memory is low. The next tab to be unloaded is chosen ba…`
    - Suggest: `لمنع انهيار التطبيق`
    - “انهيار” takes hamzat wasl; the same paragraph also has “اللسان … إلغاء تحميلها” mixing masculine noun with feminine pronoun.
- `addon-install-error-admin-install-only` — `browser/browser/addonNotifications.ftl` — “باستخدام” misspelled with hamzat qatʿ.
    - Current: `بإستخدام`
    - Source: `You cannot install { $addonName } as an end user, it can only be installed by an organization using enterprise policies.`
    - Suggest: `باستخدام`
    - “استخدام” takes hamzat wasl, so the prefixed form is “باستخدام”.
- `addon-install-error-network-failure` — `browser/browser/addonNotifications.ftl` — The sentence ends with a dangling preposition, leaving it incomplete.
    - Current: `تعذر تنزيل الإضافة بسبب فشل في الاتصال مع.`
    - Source: `The add-on could not be downloaded because of a connection failure.`
    - Suggest: `تعذر تنزيل الإضافة بسبب فشل في الاتصال.`
    - en-US is “…because of a connection failure.”; the stray “مع” before the full stop leaves the Arabic sentence unfinished.
- `site-permission-install-first-prompt-midi-header` — `browser/browser/addonNotifications.ftl` — The MIDI expansion is a garbled word sequence.
    - Current: `(الآلة الموسيقية الواجهة الرقمية)`
    - Source: `This site is requesting access to your MIDI (Musical Instrument Digital Interface) devices. Device access can be enabled by installing an add-on.`
    - Suggest: `(الواجهة الرقمية للآلات الموسيقية)`
    - “Musical Instrument Digital Interface” is rendered as two unlinked noun phrases, which does not read as a term in Arabic.
- `smart-window-confirm-open-tabs` — `browser/browser/aiWindowContent.ftl` — Dual object in the nominative instead of the accusative after an imperative verb.
    - Current: `افتح لسانان`
    - Source: `{$count ->} [one] Open { $count } tab [other] Open { $count } tabs`
    - Suggest: `افتح لسانين`
    - As the object of “افتح”, the dual must be “لسانين”.
- `smart-window-opened-tabs-summary-group` — `browser/browser/aiWindowContent.ftl` — Masculine verb with the feminine noun “مجموعة”.
    - Current: `أُنشئ مجموعة`
    - Source: `{$count ->} [other] Created the group “{ $label }” and opened { $count } tabs.`
    - Suggest: `أُنشئت مجموعة`
    - “مجموعة” is feminine, so the passive verb must be “أُنشئت”; this error repeats in every plural variant of the message.
- `appmenu-update-restart2` — `browser/browser/appMenuNotifications.ftl` — Typo in the Dismiss label (letters transposed).
    - Current: `أهِمل`
    - Source: `buttonaccesskey: U buttonlabel: Update and restart label: Update available secondarybuttonaccesskey: m secondarybuttonlabel: Dismiss`
    - Suggest: `أهمِل`
    - Every other Dismiss label in the same file is “أهمِل”; here the diacritic sits on the wrong letter, producing a non-word.
- `appmenu-nova-switch-device-promo` — `browser/browser/appmenu.ftl` — Accusative ending on a noun governed by a preposition.
    - Current: `هل ستحصل على جهازًا جديدًا قريبًا؟`
    - Source: `message: Getting a new device soon? Take { -brand-short-name } with you!`
    - Suggest: `هل ستحصل على جهاز جديد قريبًا؟`
    - After “على” the noun must be in the genitive: “جهاز جديد”.
- `fxa-menu-create-profile-description` — `browser/browser/appmenu.ftl` — Malformed “كلمات السرك” (definite article plus possessive suffix) and missing preposition after “احتفظ”.
    - Current: `احتفظ علاماتك وكلمات السرك وتأريخ تصفحك`
    - Source: `Keep your bookmarks, passwords, and history separate for work and personal browsing.`
    - Suggest: `احتفظ بعلاماتك وكلمات سرك وتأريخ تصفحك`
    - “السرك” combines the definite article with a possessive suffix, which is ungrammatical, and “احتفظ” requires the preposition “بـ”.
- `default-browser-notification-privacy-header-text` — `browser/browser/backgroundtasks/defaultagent.ftl` — Imperative of بقي misspelled «ابقى» instead of «ابقَ»
    - Current: `ابقى مع { -brand-short-name }؟`
    - Source: `Stay with { -brand-short-name }?`
    - Suggest: `ابقَ مع { -brand-short-name }؟`
    - The imperative of the defective verb بقي is «ابقَ»; writing a final alif maqsura is an orthographic error in a user-facing notification headline.
- `backup-folder-name` — `browser/browser/backupSettings.ftl` — “استعِدة” is not a word; the backup folder gets a misspelled name.
    - Current: `استعِدة { -brand-product-name }`
    - Source: `Restore { -brand-product-name }`
    - Suggest: `استعادة { -brand-product-name }`
    - en-US “Restore { -brand-product-name }” is a noun phrase; “استعِدة” is a malformed blend of the imperative “استعِد” and the noun “استعادة”, and this string becomes a real folder name on disk.
- `backup-service-error-unsupported-version` — `browser/browser/backupSettings.ftl` — “اخترته” spelled with hamzat qatʿ and “آخر” written as “أخر”.
    - Current: `الملف الذي أخترته لا يتوافق مع نسخة { -brand-short-name }. اختر ملف أخر وحاول مجددًا.`
    - Source: `heading: This file isn’t working message: The file you chose isn’t compatible with this version of { -brand-short-name }. Choose a different file and try again.`
    - Suggest: `الملف الذي اخترته لا يتوافق مع نسخة { -brand-short-name }. اختر ملفًا آخر وحاول مجددًا.`
    - “اختار” takes hamzat wasl in the perfect, and “آخر” (other) requires madda; both errors recur in the neighbouring backup-service-error strings.
- `change-backup-encryption-header` — `browser/browser/backupSettings.ftl` — Broken genitive construction: a definite noun followed by another definite noun.
    - Current: `غيِّر كلمة السر النسخ الاحتياطي`
    - Source: `Change backup password`
    - Suggest: `غيِّر كلمة سر النسخ الاحتياطي`
    - In an iḍāfa the first term cannot carry the definite article: “كلمة سر النسخ الاحتياطي”.
- `restore-from-backup-header` — `browser/browser/backupSettings.ftl` — Same non-word “استعِدة” in the restore dialog heading.
    - Current: `استعِدة بياناتك`
    - Source: `Restore your data`
    - Suggest: `استعِد بياناتك`
    - “استعِدة” is not a valid form; the imperative is “استعِد” (used correctly in settings-data-backup-restore-scheduled-on).
- `settings-data-toggle-encryption-label2` — `browser/browser/backupSettings.ftl` — “بياناتك” is missing its first letter.
    - Current: `انسخ احتياطيًا ياناتك الحساسة`
    - Source: `description: Back up your passwords and payment methods, plus keep all your data safe with encryption. label: Back up your sensitive data`
    - Suggest: `انسخ احتياطيًا بياناتك الحساسة`
    - “ياناتك” is a typo for “بياناتك”, visible as the label of the sensitive-data toggle.
- `firefox-relay-offer-legal-notice` — `browser/browser/browser.ftl` — Missing space before the quoted button name, and the link wraps the wrong words.
    - Current: `بالنقر على"أستخدم قناع البريد"، أنت توافق على شروط <label data-l10n-name="tos-url"> للخدمة </label>`
    - Source: `By clicking “Use email mask”, you agree to the <label data-l10n-name="tos-url">Terms of Service</label> and <label data-l10n-name="privacy-url">Privacy Notice</label>.`
    - Suggest: `بالنقر على ”استخدم قناع البريد“، أنت توافق على <label data-l10n-name="tos-url">شروط الخدمة</label>`
    - “على"أستخدم” runs two words together with no space, and the link text is “للخدمة” alone rather than “شروط الخدمة”, leaving “شروط” outside the link.
- `picture-in-picture-panel-header` — `browser/browser/browser.ftl` — “فيديو” is misspelled “فديو” while the adjacent string spells it correctly.
    - Current: `فديو معترِض`
    - Source: `Picture-in-Picture`
    - Suggest: `فيديو معترِض`
    - picture-in-picture-panel-body in the same panel uses “مقاطع الفيديو”, so the panel shows two spellings of the same word and “فديو” is the wrong one.
- `quickactions-cmd-addons3` — `browser/browser/browser.ftl` — Keyword list spells “الامتدادات/امتداد” with hamzat qatʿ.
    - Current: `اﻹمتدادات, إمتداد`
    - Source: `extensions, themes, addons, add-ons`
    - Suggest: `الامتدادات, امتداد`
    - “امتداد” takes hamzat wasl; the rest of the tree consistently writes “الامتدادات”, so these search keywords are misspelled.
- `reset-pbm-panel-heading2` — `browser/browser/browser.ftl` — An imperative verb coordinated with a verbal noun.
    - Current: `امحُ البيانات وبدء جلسة خاصة جديدة؟`
    - Source: `Clear data and start a fresh private session?`
    - Suggest: `أتريد محو البيانات وبدء جلسة خاصة جديدة؟`
    - en-US is a question (“Clear data and start a fresh private session?”); the Arabic mixes the command “امحُ” with the masdar “بدء”, so the two halves do not agree.
- `sharing-warning-window` — `browser/browser/browser.ftl` — Subject in the accusative/genitive instead of the nominative.
    - Current: `يقدر الآخرين على رؤيتك`
    - Source: `You are sharing { -brand-short-name }. Other people can see when you switch to a new tab.`
    - Suggest: `يقدر الآخرون على رؤيتك`
    - As the subject of “يقدر”, the sound masculine plural must be “الآخرون”; the same error appears in sharing-warning-screen.
- `trustpanel-tracking-content-not-blocking-tab-header` — `browser/browser/browser.ftl` — “سمح” is missing the preposition it requires.
    - Current: `{ -brand-product-name } سمح { $count } متعقِّب`
    - Source: `{$count ->} [one] { -brand-product-name } allowed { $count } tracker [other] { -brand-product-name } allowed { $count } trackers`
    - Suggest: `{ -brand-product-name } سمح بـ{ $count } متعقِّب`
    - The parallel strings in the same panel correctly write “سمح ب{ $count }”; without “بـ” the verb has no object marker.
- `contextual-manager-passwords-breached-origin-heading-and-message` — `browser/browser/contextual-manager.ftl` — “أو” written without its hamza.
    - Current: `سُرقت او سُربت`
    - Source: `heading: Password change recommended message: Passwords from this website were reported stolen or leaked. Change your password to protect your account.`
    - Suggest: `سُرقت أو سُرّبت`
    - The conjunction is “أو”; “او” is a spelling error.
- `customkeys-dev-profiler-toggle` — `browser/browser/customkeys.ftl` — “ابدأ” misspelled as “ابدء”.
    - Current: `ابدء/أوقف محلّل الأداء`
    - Source: `Start/Stop the Performance Profiler`
    - Suggest: `ابدأ/أوقف محلّل الأداء`
    - The imperative of “بدأ” ends in hamza on alif: “ابدأ”.
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — `default-browser-guidance-notification-body-instruction-win10` quotes “مستعرض الويب” but the string it names, `desktop-entry-generic-name`, reads “متصفح الوِب”
    - Current: `الخطوة 1: انتقل إلى الإعدادات > التطبيقات الافتراضية الخطوة 2: انتقل لأسفل إلى "مستعرض الويب" الخطوة 3: حدد واختر { -brand-short-name }`
    - Source: `Step 1: Go to Settings > Default apps Step 2: Scroll down to “Web browser” Step 3: Select and choose { -brand-short-name }`
    - Suggest: `متصفح الوِب`
    - In the source this string quotes “Web browser”, which is exactly the value of `desktop-entry-generic-name` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `callout-pdfjs-edit-body-b` — `browser/browser/featureCallout.ftl` — “دوّن” misspelled as “دوّين”.
    - Current: `دوّين الملاحظات`
    - Source: `Skip the search for free online editors. Fill out forms, add comments, or take notes directly in { -brand-short-name }.`
    - Suggest: `دوّن الملاحظات`
    - The imperative of “دوّن” has no yāʾ; “دوّين” is not a word.
- `fxa-adoption-passwords-title` — `browser/browser/featureCallout.ftl` — Masculine verb with the feminine subject “كلمة السر”.
    - Current: `حُفظ كلمة السر`
    - Source: `Password saved. Let’s back it up.`
    - Suggest: `حُفظت كلمة السر`
    - confirmationHints.ftl renders the same sentence “حُفظت كلمة السر”; the masculine form does not agree with “كلمة”.
- `sidebar-callout-survey-saved-websites-2` — `browser/browser/featureCallout.ftl` — Definite adjective with an indefinite noun.
    - Current: `وصول السريع إلى علاماتك`
    - Source: `Quick access to your bookmarks`
    - Suggest: `الوصول السريع إلى علاماتك`
    - “وصول السريع” mismatches definiteness; it must be “الوصول السريع”.
- `windows-10-eos-sync-new-device-subtitle-2` — `browser/browser/featureCallout.ftl` — Malformed “كلمات السرك”.
    - Current: `علاماتك وكلمات السرك وإعداداتك`
    - Source: `No matter how often you use { -brand-short-name }, syncing protects your bookmarks, passwords, and settings.`
    - Suggest: `علاماتك وكلمات سرك وإعداداتك`
    - “السرك” attaches a possessive suffix to a word that already carries the definite article, which is ungrammatical.
- `firefox-relay-opt-in-subtitle-b` — `browser/browser/firefoxRelay.ftl` — “احمِ” written with hamzat qatʿ.
    - Current: `إحمِ صندوق بريدك`
    - Source: `Protect your inbox from spam`
    - Suggest: `احمِ صندوق بريدك`
    - firefox-relay-opt-in-title-1 in the same file spells the same imperative correctly as “احمِ”.
- `firefoxview-choose-browser-button` — `browser/browser/firefoxView.ftl` — “اختر” spelled with hamzat qatʿ.
    - Current: `أختر متصفح`
    - Source: `(value): Choose browser title: Choose browser`
    - Suggest: `اختر متصفحًا`
    - The imperative of “اختار” takes hamzat wasl (“اختر”), as written everywhere else in the tree; the object also needs the accusative. The following string has the same error in “أجعل”.
- `firefoxview-import-history-header` — `browser/browser/firefoxView.ftl` — The preposition “من” is duplicated.
    - Current: `استورِد من التأريخ من متصفح آخر…`
    - Source: `Import history from another browser`
    - Suggest: `استورِد التأريخ من متصفح آخر`
    - en-US is “Import history from another browser”; the extra “من” before “التأريخ” makes the object a source as well.
- `firefoxview-syncedtabs-loading-header` — `browser/browser/firefoxView.ftl` — “جارٍ” misspelled with tanwīn fatḥ on the wrong letter.
    - Current: `جارً المزامنة`
    - Source: `Sync in progress`
    - Suggest: `جارٍ المزامنة`
    - “جارً” is not a valid form; the active participle here is “جارٍ”.
- `firefoxview-tabpickup-fxa-admin-disabled-header` — `browser/browser/firefoxView.ftl` — Passive verb vocalisation used with an explicit agent.
    - Current: `عُطّلت منظّمتك المزامنة`
    - Source: `Your organization has disabled sync`
    - Suggest: `عطّلت منظّمتك المزامنة`
    - en-US is “Your organization has disabled sync” (active). With the damma, “عُطّلت” is passive, so the sentence reads “your organization was disabled …”.
- `genai-menu-ask-generic-2` — `browser/browser/genai.ftl` — “آلي” written without the madda.
    - Current: `اسأل ألي دردشة AI`
    - Source: `accesskey: z label: Ask AI Chatbot`
    - Suggest: `اسأل آلي دردشة AI`
    - The same file writes “آلي محادثة” elsewhere; “ألي” is a different word.
- `genai-menu-remove-generic` — `browser/browser/genai.ftl` — “الاصطناعي” misspelled and the phrase is left unlinked.
    - Current: `أزِل روبوت المحادثة الذكاء الاصناعي`
    - Source: `label: Remove AI Chatbot`
    - Suggest: `أزِل روبوت المحادثة بالذكاء الاصطناعي`
    - “الاصناعي” drops the ṭāʾ of “الاصطناعي”, and the two definite nouns are juxtaposed with no linking preposition.
- `ipprotection-experiment-badge` — `browser/browser/ipProtection.ftl` — Definiteness mismatch in the beta badge.
    - Current: `نسخة التجريبية`
    - Source: `label: BETA`
    - Suggest: `النسخة التجريبية`
    - “نسخة التجريبية” pairs an indefinite noun with a definite adjective; it must be “النسخة التجريبية”.
- `migration-passwords-from-file-no-valid-data` — `browser/browser/migrationWizard.ftl` — Imperative “choose” written with hamzat qaṭʿ (أختر) instead of اختر.
    - Current: `أختر ملفا آخر.`
    - Source: `The file doesn’t include any valid password data. Pick another file.`
    - Suggest: `اختر ملفًا آخر.`
    - The imperative of اختار is اختر; the same file writes اختر correctly in migration-select-all-option-label and elsewhere.
- `fxa-menu-message-backup-sync-secondary-text` — `browser/browser/newtab/asrouter.ftl` — Wrong pronoun: “تستخدمه { -brand-short-name }” instead of “تستخدم فيه”.
    - Current: `في أي مكان تستخدمه { -brand-short-name }`
    - Source: `Sync backs up most of your data so you can access it everywhere you use { -brand-short-name }.`
    - Suggest: `في أي مكان تستخدم فيه { -brand-short-name }`
    - The relative clause needs the locative pronoun فيه, as in the parallel string fxa-menu-message-sync-devices-secondary-text (“في أي مكان تستخدم فيه”); as written the object pronoun duplicates the brand name.
- `mr2022-background-update-toast-title` — `browser/browser/newtab/asrouter.ftl` — “اقل” is missing its hamza.
    - Current: `متعقبات اقل`
    - Source: `New { -brand-short-name }. More private. Fewer trackers. No compromises.`
    - Suggest: `متعقبات أقل`
    - أقل takes hamzat qat‘; spelled without it the word is misspelled.
- `newtab-custom-web-notifications-toggle` — `browser/browser/newtab/newtab.ftl` — “إختصاراتهم” has the wrong hamza and the wrong pronoun for non-human plural.
    - Current: `أظهر إشعارات من مواقعك على إختصاراتهم`
    - Source: `description: Show notifications from your sites on their shortcuts label: Web notifications`
    - Suggest: `أظهر إشعارات من مواقعك على اختصاراتها`
    - اختصارات takes hamzat wasl, and the referent (مواقع) is a non-human plural taking ـها, not ـهم.
- `newtab-report-ads-reason-not-interested` — `browser/browser/newtab/newtab.ftl` — Missing accusative ending after ليس.
    - Current: `أنا لست مهتم`
    - Source: `label: I’m not interested`
    - Suggest: `أنا لست مهتمًا`
    - The predicate of ليس must be in the accusative (خبر ليس منصوب).
- `newtab-report-content-spam-misleading` — `browser/browser/newtab/newtab.ftl` — Definite article on the second coordinate makes the phrase ungrammatical.
    - Current: `سخام أو المضلل`
    - Source: `label: Spam or misleading`
    - Suggest: `سخام أو محتوى مضلل`
    - en-US “Spam or misleading”; coordinating an indefinite noun with a definite adjective (المضلل) is ungrammatical in Arabic.
- `newtab-wallpaper-light-green` — `browser/browser/newtab/newtab.ftl` — “اخضر” is missing its hamza.
    - Current: `اخضر فاتح`
    - Source: `Light green`
    - Suggest: `أخضر فاتح`
    - The adjacent entry newtab-wallpaper-green spells it أخضر.
- `newtab-wallpaper-light-mountain` — `browser/browser/newtab/newtab.ftl` — “ابيض” is missing its hamza.
    - Current: `جبل ابيض`
    - Source: `White mountain`
    - Suggest: `جبل أبيض`
    - أبيض takes hamzat qat‘; the same word is written correctly in newtab-wallpaper-white-mountains (جبال بيضاء) and other colour strings.
- `newtab-wallpaper-light-purple` — `browser/browser/newtab/newtab.ftl` — “ارجواني” is missing its hamza.
    - Current: `ارجواني فاتح`
    - Source: `Light purple`
    - Suggest: `أرجواني فاتح`
    - The neighbouring colour entries spell it أرجواني (newtab-wallpaper-dark-purple = أرجواني داكن).
- `mr2022-onboarding-set-default-title` — `browser/browser/newtab/onboarding.ftl` — “أجعل” is misspelled; the imperative is “اجعل”.
    - Current: `أجعل { -brand-short-name } متصفحك الأساسي`
    - Source: `Make { -brand-short-name } your go-to browser`
    - Suggest: `اجعل { -brand-short-name } متصفحك الأساسي`
    - The imperative of جعل takes hamzat wasl (اجعل); “أجعل” is the first-person indicative. The rest of the tree uses “اجعل”.
- `onboarding-infrequent-import-subtitle` — `browser/browser/newtab/onboarding.ftl` — “إستيراد” uses the wrong hamza.
    - Current: `تستطيع إستيراد العلامات`
    - Source: `Whether you’re settling in or just stopping by, remember you can import your bookmarks, passwords, and more.`
    - Suggest: `تستطيع استيراد العلامات`
    - استيراد takes hamzat wasl; the locale writes it correctly everywhere else (e.g. policy-DisableProfileImport context, استورِد).
- `return-to-amo-extension-install-complete-label` — `browser/browser/newtab/onboarding.ftl` — Feminine verb with the masculine noun الامتداد.
    - Current: `ثُبتت الامتداد`
    - Source: `Extension installed`
    - Suggest: `ثُبّت الامتداد`
    - الامتداد is masculine, so the verb must be ثُبّت; the feminine form belongs to the theme string (ثُبتت السمة).
- `policy-DisableFirefoxStudies` — `browser/browser/policies/policies-descriptions.ftl` — “الدارسات” is a typo for “الدراسات” (studies).
    - Current: `من تشغيل الدارسات`
    - Source: `Prevent { -brand-short-name } from running studies.`
    - Suggest: `من تشغيل الدراسات`
    - en-US “from running studies”; الدارسات means “female students”, not “studies”.
- `delete-profile-description` — `browser/browser/profiles.ftl` — Garbled sentence: “the command will lead { -brand-short-name } to delete…”.
    - Current: `سيؤدي الأمر { -brand-short-name } إلى حذف`
    - Source: `{ -brand-short-name } will permanently delete the following data from this device:`
    - Suggest: `سيحذف { -brand-short-name } البيانات التالية نهائيًا`
    - الأمر leaves the brand name with no syntactic role, producing an ungrammatical sentence where the source simply says Firefox will permanently delete the data.
- `multiprofile-data-collection-message` — `browser/browser/profiles.ftl` — Broken construct “ملفات الشخصية” instead of “الملفات الشخصية”.
    - Current: `جميع ملفات الشخصية الموجودة`
    - Source: `<strong>Data collection settings changed.</strong> The changes made in another profile apply to all profiles on this device.`
    - Suggest: `جميع الملفات الشخصية الموجودة`
    - An iḍāfa cannot take the article on the second term here; the rest of the file writes الملفات الشخصية.
- `profile-window-body` — `browser/browser/profiles.ftl` — Agreement error: ملفات شخصي (plural noun with masculine singular adjective).
    - Current: `أنشئ ملفات شخصي لكل من يستخدم هذا الجهاز`
    - Source: `Keep your work and personal browsing, including things like passwords and bookmarks, totally separate. Or create profiles for everyone who uses this device.`
    - Suggest: `أنشئ ملفات شخصية لكل من يستخدم هذا الجهاز`
    - Non-human plural noun requires ملفات شخصية, as used throughout the rest of the file.
- `profiles-green-theme-title` — `browser/browser/profiles.ftl` — “green” misspelled (الخصراء instead of الخضراء).
    - Current: `طبّق السمة الخصراء`
    - Source: `title: Apply green theme`
    - Suggest: `طبّق السمة الخضراء`
    - Plain spelling error in a user-visible tooltip; profiles-green-theme spells أخضر correctly.
- `protection-report-page-summary` — `browser/browser/protections.ftl` — Ungrammatical يمكنه followed by an explicit subject.
    - Current: `يمكنه { -brand-short-name } حماية خصوصيتك`
    - Source: `{ -brand-short-name } can protect your privacy behind the scenes while you browse. This is a personalized summary of those protections, including tools to take control of your online security.`
    - Suggest: `يمكن لـ{ -brand-short-name } حماية خصوصيتك`
    - يمكنه already carries the pronoun subject, so repeating the brand name as subject is ungrammatical.
- `smartblock-placeholder-desc` — `browser/browser/protectionsPanel.ftl` — Verb/subject agreement: منع with the feminine plural إعدادات.
    - Current: `لقد منع إعدادات { -brand-short-name }`
    - Source: `Your { -brand-short-name } settings blocked this content from tracking you across sites or being used for ads.`
    - Suggest: `لقد منعت إعدادات { -brand-short-name }`
    - إعدادات is a non-human plural and takes feminine singular agreement (منعت).
- `safeb-blocked-unwanted-page-title` — `browser/browser/safebrowsing/blockedSite.ftl` — Number/gender disagreement: singular noun with plural feminine adjective
    - Current: `قد يحتوي هذا الموقع برنامج ضارة`
    - Source: `The site ahead may contain harmful programs`
    - Suggest: `قد يحتوي هذا الموقع برامج ضارة`
    - “harmful programs” is plural; «برنامج» is singular and does not agree with «ضارة», producing an ungrammatical page title.
- `clear-data-settings-label` — `browser/browser/sanitize.ftl` — Ungrammatical “عندما إغلاقه” (عندما + noun).
    - Current: `عندما إغلاقه`
    - Source: `When closed, { -brand-short-name } should automatically clear all`
    - Suggest: `عند إغلاقه`
    - عندما introduces a clause, not a verbal noun; the parallel string sanitize-on-shutdown-description correctly uses عند إغلاق.
- `item-formdata-description` — `browser/browser/sanitize.ftl` — Misspelled verb يمحُ.
    - Current: `يمحُ بيانات مثل الأسماء`
    - Source: `Clears things like names, emails, and other items you enter in forms`
    - Suggest: `يمحو بيانات مثل الأسماء`
    - The correct form is يمحو, as written in sanitize-dialog-title2 (امحُ is the imperative, not the present).
- _…and 69 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `appmenu-help-share-ideas` — `browser/browser/appmenu.ftl` — `appmenu-help-share-ideas` uses three dots where this locale uses …
    - Current: `شارك الأفكار والتعليقات...`
    - Source: `accesskey: S label: Share Ideas and Feedback…`
    - The tree uses … 366 times against 13 ASCII runs.
- `menu-share-mac-picker-multiple` — `browser/browser/browser.ftl` — `menu-share-mac-picker-multiple` uses three dots where this locale uses …
    - Current: `الرسائل والبريد والمزيد...`
    - Source: `accesskey: M label: Messages, Mail, and More…`
    - The tree uses … 366 times against 13 ASCII runs.
- `main-context-menu-pdfjs-save-page` — `browser/browser/browserContext.ftl` — `main-context-menu-pdfjs-save-page` uses three dots where this locale uses …
    - Current: `احفظ التحديد باسم...`
    - Source: `label: Save selection as…`
    - The tree uses … 366 times against 13 ASCII runs.
- `content-sharing-modal-generating-page` — `browser/browser/contentSharing.ftl` — `content-sharing-modal-generating-page` uses three dots where this locale uses …
    - Current: `يولّد الصفحة...`
    - Source: `label: Generating page…`
    - The tree uses … 366 times against 13 ASCII runs.
- `continuous-onboarding-firefox-view-tab-pickup-subtitle` — `browser/browser/featureCallout.ftl` — “bookmarks” rendered with a term the rest of the tree never uses.
    - Current: `الإشارات المرجعية`
    - Source: `Access your open tabs from any device. Plus sync your bookmarks, passwords, and more.`
    - Suggest: `العلامات`
    - Bookmarks are consistently “العلامات” across browser.ftl, appmenu.ftl and firefoxView.ftl, including in neighbouring callouts; “الإشارات المرجعية” is an isolated alternative in the same surface.
- `fxviewtabrow-mute-tab` — `browser/browser/fxviewTabList.ftl` — “Mute tab” uses two different verbs in the same surface.
    - Current: `أصمت اللسان`
    - Source: `(value): Mute Tab accesskey: M`
    - Suggest: `اكتم اللسان`
    - fxviewtabrow-mute-tab-button-no-context in the same file, and quickactions-mute in browser.ftl, use “اكتم”; “أصمت” is not the established rendering.
- `genai-chatbot-summarize-sidebar-generic-subtitle` — `browser/browser/genai.ftl` — A stray straight quotation mark after the closing curly quote.
    - Current: `واختر “لخص الصفحة”".`
    - Source: `Right-click the sparkles button in the sidebar and choose “Summarize Page”. The first time, you’ll also choose an AI chatbot.`
    - Suggest: `واختر ”لخص الصفحة“.`
    - The quoted command is closed twice, leaving a visible extra quote character in the UI text.
- `ipprotection-connection-status-connecting-1` — `browser/browser/ipProtection.ftl` — `ipprotection-connection-status-connecting-1` uses three dots where this locale uses …
    - Current: `يتصل VPN...`
    - Source: `(value): VPN is connecting… aria-label: VPN is connecting…`
    - The tree uses … 366 times against 13 ASCII runs.
- `menu-file-share-qrcode` — `browser/browser/menubar.ftl` — `menu-file-share-qrcode` uses three dots where this locale uses …
    - Current: `ولّد رمز QR...`
    - Source: `accesskey: Q label: Generate QR Code…`
    - The tree uses … 366 times against 13 ASCII runs.
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — `menu-help-share-ideas` uses three dots where this locale uses …
    - Current: `شارك الأفكار والانطباعات...`
    - Source: `accesskey: S label: Share Ideas and Feedback…`
    - The tree uses … 366 times against 13 ASCII runs.
- `menu-profiles-manage-profiles` — `browser/browser/menubar.ftl` — “Profiles” rendered as ملفات الإعدادات (settings files) in the same menu that uses ملفات شخصية.
    - Current: `أدِر ملفات الإعدادات`
    - Source: `label: Manage Profiles`
    - Suggest: `أدِر الملفات الشخصية`
    - menu-profiles-menu and all of profiles.ftl use الملف الشخصي/ملفات شخصية for Profiles; ملفات الإعدادات names configuration files instead.
- `menu-view-full-zoom` — `browser/browser/menubar.ftl` — The “Zoom” submenu and its “Zoom In” item carry the identical label قرّب.
    - Current: `قرّب`
    - Source: `accesskey: Z label: Zoom`
    - Suggest: `التقريب`
    - menu-view-full-zoom is the parent submenu (noun) and menu-view-full-zoom-enlarge is “Zoom In”; giving both the same imperative label makes two items in one menu indistinguishable.
- `welcome-back-spotlight-subtitle` — `browser/browser/newtab/asrouter.ftl` — The string switches from singular to plural address mid-sentence.
    - Current: `لحماية بياناتكم أينما كنتم`
    - Source: `Welcome back to the only major browser backed by a non-profit. We take extra steps to protect your data wherever you roam.`
    - Suggest: `لحماية بياناتك أينما كنت`
    - The same string opens with singular “مرحبًا بك مجددًا” and the rest of the file addresses the user in the singular; the plural forms here break the established form of address.
- `mr2022-onboarding-pin-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — “Dock” is rendered two different ways within the same file (التصريفة vs الإرساء).
    - Current: `ثبّت { -brand-short-name } على التصريفة`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } in Dock [other] Pin { -brand-short-name } to taskbar`
    - Suggest: `ثبّت { -brand-short-name } في الإرساء`
    - mr2022-upgrade-onboarding-pin-private-window-primary-button-label in the same file uses “الإرساء” for macOS Dock, while this string and fx100-thank-you-pin-primary-button-label use “التصريفة”; one term should be used for the same UI element.
- `onboarding-live-language-installing` — `browser/browser/newtab/onboarding.ftl` — `onboarding-live-language-installing` uses three dots where this locale uses …
    - Current: `جارٍ تثبيت حزمة اللغة لـ{ $negotiatedLanguage }...`
    - Source: `Installing the language pack for { $negotiatedLanguage }…`
    - The tree uses … 366 times against 13 ASCII runs.
- `onboarding-live-language-waiting-button` — `browser/browser/newtab/onboarding.ftl` — `onboarding-live-language-waiting-button` uses three dots where this locale uses …
    - Current: `جارٍ الحصول على اللغات المتاحة...`
    - Source: `Getting available languages…`
    - The tree uses … 366 times against 13 ASCII runs.
- `panic-button-delete-history` — `browser/browser/panicButton.ftl` — “History” rendered as السجل where the locale uses التأريخ.
    - Current: `تحذف <strong>السجل</strong> الحديث`
    - Source: `Delete Recent <strong>History</strong>`
    - Suggest: `تحذف <strong>التأريخ</strong> الحديث`
    - panelUI.ftl's forget-button message and the whole browser tree use التأريخ for History, including the menu entry that opens this panel.
- `connection-proxy-socks-remote-dns` — `browser/browser/preferences/connection.ftl` — “Proxy DNS” rendered as a noun phrase “the proxy’s DNS server”, unlike the identical SOCKS v4 string
    - Current: `خادوم عناوين نطاقات الوسيط أثناء استخدام SOCKS v5`
    - Source: `accesskey: D label: Proxy DNS when using SOCKS v5`
    - Suggest: `وسّط DNS عند استخدام SOCKS v5`
    - The adjacent connection-proxy-socks4-remote-dns correctly renders the same en-US pattern as the verb “وسّط DNS”; here the checkbox reads as naming a server belonging to the proxy rather than the action of proxying DNS lookups.
- `permissions-exceptions-manage-doh-desc` — `browser/browser/preferences/permissions.ftl` — “subdomains” uses “مجالات” while the same dialog uses “النطاق” for domain
    - Current: `مجالاتها الفرعية`
    - Source: `{ -brand-short-name } won’t use secure DNS on these sites and their subdomains.`
    - Suggest: `نطاقاتها الفرعية`
    - The same dialog labels the column النطاق and the input اسم نطاق الموقع; switching to مجال for the same concept one line later is inconsistent within one surface.
- `sync-syncing-across-devices-empty-state2` — `browser/browser/preferences/preferences.ftl` — `sync-syncing-across-devices-empty-state2` uses three dots where this locale uses …
    - Current: `أنت لا تُزامن أي شيء... حتى الآن. ابدأ المزامنة للحصول على جميع بياناتك على جميع أجهزتك.`
    - Source: `description: You aren’t syncing anything… yet. Start syncing to get all of your data on all your devices. label: Manage synced data`
    - The tree uses … 366 times against 13 ASCII runs.
- `sync-syncing-across-devices-empty-state3` — `browser/browser/preferences/preferences.ftl` — `sync-syncing-across-devices-empty-state3` uses three dots where this locale uses …
    - Current: `لم تُزامِن أي شيء... حتى الآن. اختر ما تريد مُزامنته على هذا الجهاز.`
    - Source: `description: You aren’t syncing anything… yet. Choose what to sync on this device. label: Manage synced data`
    - The tree uses … 366 times against 13 ASCII runs.
- `site-data-removing-header` — `browser/browser/preferences/siteDataSettings.ftl` — “Cookies” rendered as “ملفات تعريف الارتباط” in the Removing section while the rest of the same dialog uses “الكعكات”
    - Current: `إزالة ملفات تعريف الارتباط و بيانات المواقع`
    - Source: `Removing Cookies and Site Data`
    - Suggest: `إزالة الكعكات و بيانات المواقع`
    - The same file (and clear-site-data / permissions) consistently uses “الكعكات”; three adjacent strings (removing-header, removing-desc, removing-single-desc) switch to a different term for the same thing in one dialog flow.
- `preonboarding-checklist-crash-reports-description` — `browser/browser/preonboarding.ftl` — “Crash reports” called تقارير الإنهيار in the description but تقارير الأعطال in its own label, and الإنهيار is misspelled.
    - Current: `تقارير الإنهيار`
    - Source: `Crash reports allow us to diagnose and fix issues with the browser. Reports may include personal or sensitive data.`
    - Suggest: `تقارير الأعطال`
    - The label immediately above uses تقارير الأعطال for the same term, and الإنهيار should be الانهيار (hamzat waṣl).
- `profiles-gray-theme-title` — `browser/browser/profiles.ftl` — “theme” rendered as المظهر here while every sibling tooltip uses السمة.
    - Current: `طبّق المظهر الرمادي`
    - Source: `title: Apply gray theme`
    - Suggest: `طبّق السمة الرمادية`
    - All other profiles-*-theme-title strings in the same selector use السمة; the lone المظهر is inconsistent in one surface.
- `protections-panel-cookie-banner-blocker-header` — `browser/browser/protectionsPanel.ftl` — “Cookie” rendered as ملفات تعريف الارتباط in the same panel that calls them الكعكات.
    - Current: `مانع لافتة ملفات تعريف الارتباط`
    - Source: `Cookie Banner Blocker`
    - Suggest: `مانع لافتة الكعكات`
    - protections-panel-cookie-banner-view-cookie-clear-warning and protections-panel-cross-site-tracking-cookies in this same panel use الكعكات; two names for one object in one surface.
- `safeb-blocked-unwanted-page-error-desc-override` — `browser/browser/safebrowsing/blockedSite.ftl` — “harmful software” rendered identically to the malware string
    - Current: `يحتوي برمجيات خبيثة`
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing harmful software</a>. You can <a data-l10n-name='ignore_warning_link'>ignore the risk</a> and go t…`
    - Suggest: `يحتوي برمجيات ضارة`
    - The unwanted-software page is meant to say “containing harmful software”, distinct from the malware page's “malicious software”; using «برمجيات خبيثة» makes the two blocking pages indistinguishable. Same in safeb-blocked-unwanted-page-error-desc-no-override.
- `sanitize-calculating-size` — `browser/browser/sanitize.ftl` — `sanitize-calculating-size` uses three dots where this locale uses …
    - Current: `يحسب...`
    - Source: `Calculating…`
    - The tree uses … 366 times against 13 ASCII runs.
- `sanitize-dialog-title2` — `browser/browser/sanitize.ftl` — Dialog title calls cookies ملفات تعريف الارتباط while its own checkbox calls them الكعكات.
    - Current: `امحُ بيانات التصفح وملفات تعريف الارتباط`
    - Source: `style: min-width: 34em title: Clear browsing data and cookies`
    - Suggest: `امحُ بيانات التصفح والكعكات`
    - item-cookies and item-cookies-site-data in the same dialog use الكعكات; one surface should not name the same object two ways.
- `sidebar-menu-close-ai-chatbot-tooltip-generic` — `browser/browser/sidebar.ftl` — “AI” left in Latin script where the paired open-tooltip translates it.
    - Current: `أغلق روبوت المحادثة AI`
    - Source: `Close AI chatbot ({ $shortcut })`
    - Suggest: `أغلق محادثة الذكاء الاصطناعي`
    - sidebar-menu-open-ai-chatbot-tooltip-generic renders AI as الذكاء الاصطناعي; the close tooltip of the same control should match.
- `sidebar-menu-history-header` — `browser/browser/sidebar.ftl` — “History” rendered as the indefinite تاريخ (date) where the same panel uses التأريخ.
    - Current: `تاريخ`
    - Source: `heading: History`
    - Suggest: `التأريخ`
    - sidebar-menu-history-label, sidebar-history-clear and sidebar-menu-open-history-tooltip in the same file use التأريخ; تاريخ alone reads as “a date”. sidebar-history-title has the same issue.
- `tab-group-editor-title-create` — `browser/browser/tabbrowser.ftl` — “Tab group” rendered as مجموعة لسان (a group of one tab) in several strings while others use مجموعة ألسنة.
    - Current: `أنشئ مجموعة لسان`
    - Source: `Create tab group`
    - Suggest: `أنشئ مجموعة ألسنة`
    - tab-groups-list-empty-button and tab-groups-list-title use مجموعة ألسنة/مجموعات الألسنة for the same feature; the singular لسان misnames it.
- `existing-user-tou-message` — `browser/browser/termsofuse.ftl` — “Privacy Notice” named “Privacy Policy” in the infobar but “Privacy Notice” in the sibling strings.
    - Current: `سياسة الخصوصية`
    - Source: `<strong>Update</strong> We’ve introduced a { -brand-short-name } <a data-l10n-name="terms-of-use-link">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice-link">Privacy Notice</a>. Please take a moment to…`
    - Suggest: `إشعار الخصوصية`
    - existing-user-privacy-notice-update-message and the Spotlight body in the same feature use إشعار الخصوصية; سياسة الخصوصية names a different document from the one the link points to.
- `unified-extensions-notice-safe-mode` — `browser/browser/unifiedExtensions.ftl` — “Troubleshoot Mode” rendered differently from the locale's established name.
    - Current: `وضع استكشاف الأخطاء وإصلاحها`
    - Source: `message: All extensions have been disabled by Troubleshoot Mode.`
    - Suggest: `وضع مواجهة الأعطال`
    - menubar.ftl and safeMode.ftl consistently name this feature وضع مواجهة الأعطال; a second name for the same mode leaves the user unable to match the notice to the menu item.
- `evaluateInConsole.label` — `devtools/client/debugger.properties` — “console” rendered as الطرفية (terminal) where the tree consistently uses المِعراض.
    - Current: `نفّذ في الطرفية`
    - Source: `Evaluate in console`
    - Suggest: `نفّذ في المِعراض`
    - startup.properties (ToolboxTabWebconsole.label), webconsole.properties (consoleCleared, webconsole.console.settings.menu.button.tooltip), inspector.properties (inspectorUseInConsole.label) and even eventlisteners.log.label in this same file all use المِعراض for Console.
- `inspectorEditAttribute.label` — `devtools/client/inspector.properties` — “Attribute” rendered as الخاصية (property) inside the same submenu that calls attributes صفات.
    - Current: `حرر الخاصية ”%S“`
    - Source: `Edit Attribute “%S”`
    - Suggest: `حرر الصفة ”%S“`
    - inspectorAttributesSubmenu.label (الصفات), inspectorAddAttribute.label (أضف صفة) and markupView.newAttribute.label (صفة جديدة) use صفة, while inspectorShowDOMProperties.label uses خصائص for properties; using الخاصية here conflates the two in one menu (same for inspectorRemoveAttribute.label and inspectorCopyAttributeValue.label).
- `responsive.deviceDetails.UA` — `devtools/client/responsive.properties` — “User agent” rendered as عميل المستخدم in one tooltip and وكيل المستخدم elsewhere in the same panel.
    - Current: `عميل المستخدم: %1$S`
    - Source: `UA: %1$S`
    - Suggest: `وكيل المستخدم: %1$S`
    - responsive.deviceAdderUserAgent2 (نص وكيل المستخدم), responsive.reloadConditions.userAgent and responsive.showUserAgentInput all use وكيل المستخدم; عميل means “client”, not “agent”.
- `storage-cookie-edit-error` — `devtools/client/storage.ftl` — “Cookie” rendered as ملف تعريف الارتباط while the whole Storage panel uses كعكة.
    - Current: `تعذر تحديث ملف تعريف الارتباط`
    - Source: `Cookie could not be updated: “{ $errorString }”.`
    - Suggest: `تعذّر تحديث الكعكة`
    - storage-tree-labels-cookies, storage-table-type-cookies-hint, storage-context-menu-delete-all-session-cookies and netmonitor all use الكعكات; the two terms appear in the same panel.
- `clientSendOOBHash` — `devtools/shared/debugger.properties` — Space placed before the colon instead of after it.
    - Current: `شهادتي :%1$S`
    - Source: `My Cert: %1$S`
    - Suggest: `شهادتي: %1$S`
    - Arabic, like the en-US source, attaches the colon to the preceding word; the same inversion is in clientSendOOBToken (الرمز :%1$S), while every other label in the tree uses “نص: قيمة”.
- `ConsoleAPIDisabled` — `devtools/shared/webconsole.properties` — “Web Console” rendered as مرقاب الوب (“web monitor”) instead of the established معراض الوِب.
    - Current: `API التابعة لسجل مرقاب الوب`
    - Source: `The Web Console logging API (console.log, console.info, console.warn, console.error) has been disabled by a script on this page.`
    - Suggest: `API التابعة لسجل معراض الوِب`
    - MenuWebconsole.label and ToolboxWebconsole.tooltip2 render Web Console as معراض الوِب; مرقاب is the word used for the Network Monitor (netmonitor.tooltip2 = مراقب الشبكة), so it names the wrong tool.
- `about-mozilla-from-6-27` — `toolkit/toolkit/about/aboutMozilla.ftl` — "Mozilla" is kept in Latin script in the page title but transliterated as "موزيلا" in the attribution line directly below it.
    - Current: `من <strong>كتاب موزيلا،</strong> ٦:‏٢٧`
    - Source: `from <strong>The Book of Mozilla,</strong> 6:27`
    - Suggest: `من <strong>كتاب Mozilla،</strong> ٦:‏٢٧`
    - Both strings render the same work title on the same page; about-mozilla-title-6-27 writes "كتاب Mozilla".
- `profiles-title` — `toolkit/toolkit/about/aboutProfiles.ftl` — "Profile" is rendered three different ways on the same page: "لاحة", "الملف الشخصي" and "ملف الإعدادات".
    - Current: `عن اللاحات`
    - Source: `About Profiles`
    - Suggest: `عن الملفات الشخصية`
    - The page heading and create button say "لاحة" while every other row says "الملف الشخصي" and profiles-in-use-profile/profiles-delete-profile-failed-message say "ملف الإعدادات"; a user cannot tell these name the same object.
- `about-webauthn-auth-info-force-pin-change` — `toolkit/toolkit/about/aboutWebauthn.ftl` — PIN is left as "رمز PIN" here while every other field on the page says "رقم التعريف الشخصي".
    - Current: `أجبر تغيير رمز PIN`
    - Source: `Force PIN change`
    - Suggest: `أجبر تغيير رقم التعريف الشخصي`
    - about-webauthn-pin-section-title, -min-pin-length, -pin-protocols and -clientpin all render PIN as "رقم التعريف الشخصي" in the same list of fields.
- `autofill-insecure-field-warning-description` — `toolkit/toolkit/formautofill/formAutofill.ftl` — "Form Autofill" is rendered as "secure form filling" instead of the feature name used elsewhere.
    - Current: `عُطّل الملء الآمن للاستمارات مؤقتا`
    - Source: `{ -brand-short-name } has detected an insecure site. Form Autofill is temporarily disabled.`
    - Suggest: `عُطّل الملء الآلي للاستمارات مؤقتا`
    - The feature is الملء الآلي للاستمارات in autofill-options-link and credit-card-doorhanger-options-button; الآمن (secure) names a non-existent feature and muddles the security warning.

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

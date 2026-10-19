# Firefox l10n QA — uk

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `ba8eba5819d0` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `2d5e7eb1f225` |
| **Previous run** | 2026-10-16 @ `db2cfca9d18c` |
| **Mode** | incremental |
| **Strings reviewed this run** | 81 of 15,270 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for uk: [android](android.md)

---

## Changes in this run

### 🆕 New findings (4)

- `about-sync-log-search-input` — `toolkit/services/aboutSyncLog.ftl` — The preposition "в" falls between two consonants where Ukrainian requires "у".
    - Current: `Пошук в журналах`
    - Source: `aria-label: Search logs placeholder: Search logs`
    - Suggest: `Пошук у журналах`
    - Ukrainian euphony rules call for "у" between consonants. "Пошук" ends in a consonant and "журналах" starts with one, so "у журналах" is correct. This applies to both the aria-label and the placeholder.
- `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — This string uses the typographic apostrophe, but the locale's convention is the straight apostrophe.
    - Current: `об’єднання`
    - Source: `Split, merge, and more. <a data-l10n-name="features-link">See PDF features</a>`
    - Suggest: `об'єднання`
    - The uk tree uses the straight apostrophe as its convention (717 straight vs 126 typographic).
- `smartwindow-group-tabs-loading` — `browser/browser/autoTabGrouping.ftl` — The translation says the browser is checking whether groups by tab topic already exist, not that it is looking through the tabs for useful new groups.
    - Current: `Перевірка наявності груп за темою вкладки…`
    - Source: `Checking tabs for useful groups…`
    - Suggest: `Пошук корисних груп серед вкладок…`
    - The developer comment says the model is forming new groups from the open tabs and is explicitly not searching for tab groups that already exist. 'Перевірка наявності груп' means 'checking for the existence of groups', which is the reading the comment rules out. The word 'useful' is also missing.
- `speech-recognition-model-download-progressbar` — `browser/browser/permissions.ftl` — 'Процес' ('process') is used where the English says 'progress' ('Прогрес'). It looks like a typo.
    - Current: `Процес завантаження`
    - Source: `aria-label: Speech recognition model download progress`
    - Suggest: `Прогрес завантаження`
    - The source says 'download progress'. This is the accessible name of a progress bar, so it should name the progress ('Прогрес' or 'Хід'), not the process.

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
| Files | 326 |
| Strings | 15,270 |
| Missing strings | 1,250 |
| Obsolete strings | 0 |
| Files absent from the locale | 2 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 1 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 4 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 1 |
| Typography deviations from this locale's own norm | 81 |

### Completeness

**1,250 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 377
- `browser/browser/ipProtection.ftl` — 62
- `browser/browser/newtab/onboarding.ftl` — 56
- `browser/browser/preferences/preferences.ftl` — 40
- `toolkit/toolkit/pdfviewer/viewer.ftl` — 36
- `browser/browser/newtab/asrouter.ftl` — 34
- `toolkit/toolkit/global/theme-picker.ftl` — 30
- `toolkit/toolkit/about/url-classifier.ftl` — 26
- `browser/browser/appmenu.ftl` — 26
- `browser/browser/firefoxView.ftl` — 26
- `toolkit/toolkit/about/aboutAddons.ftl` — 24
- `toolkit/toolkit/neterror/netError.ftl` — 23

**Files absent from the locale:**

- `toolkit/toolkit/global/theme-picker.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 507, `straight-double` 128, `curly-single` 112 | **curly-double** |
| apostrophe | `typographic` 127, `straight` 717 | **straight** |
| ellipsis | `char` 383, `ascii` 4 | **char** |
| dash | `em` 12, `en` 99 | **en** |
| nbsp | `total` 4, `space-before-punctuation` 7 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

- **typography — 81 strings** — 81 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `BlockMixedActiveContent`, `ForgotFileEnctypeWarning`, `ForgotPostWarning`, `FullscreenDeniedContainerNotAllowed`, `FullscreenDeniedPiP`, `ImageMapCircleNegativeRadius`, `ImageMapCircleWrongNumberOfCoords`, `ImageMapPolyOddNumberOfCoords`, `ImageMapPolyWrongNumberOfCoords`, `ImageMapRectBoundsError`, `IneligibleResource`, `LoadingMixedActiveContent2` …and 67 more

---

## 3. Open findings (200)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 112 |
| 2 | Wrong content (says something other than the English) | 82 |
| 3 | Degraded language (grammar, spelling, terminology) | 4 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `about-private-browsing-spotlight-basics-activity-seen` — `browser/browser/aboutPrivateBrowsing.ftl` — "Some activity may still be seen" is widened to "can still see your activity".
    - Current: `Вебсайти, пошукові системи, постачальники інтернету чи ваш роботодавець все одно можуть бачити вашу діяльність.`
    - Source: `Some activity may still be seen by sites, search engines, internet providers, or your employer.`
    - Suggest: `Деяку вашу діяльність все одно можуть бачити вебсайти, пошукові системи, постачальники інтернету чи ваш роботодавець.`
    - The source limits the exposure to "some activity"; dropping the quantifier in a privacy disclosure tells the user that all of their activity is visible to those parties.
- `crashed-request-auto-submit-title` — `browser/browser/aboutTabCrashed.ftl` — "Report background tabs" is rendered as "Report tab crashes without my involvement".
    - Current: `Повідомляти про збої вкладок без моєї участі`
    - Source: `Report background tabs`
    - Suggest: `Повідомляти про збої фонових вкладок`
    - The source scopes this setting to tabs that crash in the background; the Ukrainian drops that scope and instead describes automatic submission, which is what the following checkbox already says.
- `about-unloads-column-sortweight` — `browser/browser/aboutUnloads.ftl` — The column name "Secondary Weight" is rendered as "Less loaded".
    - Current: `Менш навантажені`
    - Source: `(value): Secondary Weight title: If available, tabs are sorted by this value after being sorted by the base weight. The value derives from tab’s memory usage and the count of processes.`
    - Suggest: `Вторинна вага`
    - Like about-unloads-column-weight, this is the name of a sorting weight derived from memory usage and process count, not a statement that the tabs are less loaded.
- `about-unloads-column-weight` — `browser/browser/aboutUnloads.ftl` — The column name "Base Weight" is rendered as the comparative "More loaded".
    - Current: `Навантаженіші`
    - Source: `(value): Base Weight title: Tabs are first sorted by this value, which derives from some special attributes such as playing a sound, WebRTC, etc.`
    - Suggest: `Базова вага`
    - This is a column header naming the sorting weight value, not a comparison of tabs; its own tooltip explains the value derives from attributes such as playing sound, and the sibling tooltip refers back to "the base weight".
- `account-single-tab-arriving-title` — `browser/browser/accounts.ftl` — "Tab Received" is rendered as "Sent tab", reversing the direction of the action.
    - Current: `Відправлена вкладка`
    - Source: `Tab Received`
    - Suggest: `Отримана вкладка`
    - This notification is shown when a tab sent from another device arrives on this one; the plural counterpart account-multiple-tabs-arriving-title correctly uses "Отримані вкладки". "Відправлена" tells the user they sent a tab.
- `ai-window-smart-cursor-in-smart-window` — `browser/browser/aiFeatures.ftl` — "Show shortcuts when selecting text" is rendered as "Show keyboard shortcuts".
    - Current: `Показувати комбінації клавіш під час вибору тексту`
    - Source: `description: Get quick access to summarize, explain, and more. label: Show shortcuts when selecting text`
    - Suggest: `Показувати ярлики під час вибору тексту`
    - The feature shows action shortcuts (summarize, explain, …) when text is selected, as its own description says; "комбінації клавіш" means key combinations, which is a different thing and is the term used in customkeys.ftl for real keyboard shortcuts.
- `press-tab-label` — `browser/browser/browser.ftl` — "Press tab" (the Tab key) is translated as "press the [browser] tab".
    - Current: `Натисніть вкладку, щоб вибрати:`
    - Source: `Press tab to select:`
    - Suggest: `Натисніть Tab, щоб вибрати:`
    - The string instructs the user to press the Tab key to select an address-bar action (cf. urlbar-result-action-before-tabtosearch-web, which correctly keeps "Tab"). "Вкладку" means a browser tab, so the instruction is unfollowable.
- `trustpanel-description-disabled` — `browser/browser/browser.ftl` — "{ -brand-product-name } is off-duty" is rendered as "{ -brand-product-name } is not working".
    - Current: `{ -brand-product-name } не працює.`
    - Source: `{ -brand-product-name } is off-duty. We suggest turning protections back on.`
    - Suggest: `{ -brand-product-name } відпочиває.`
    - The source says the protections are idle because the user turned them off; the Ukrainian states the browser itself is not functioning, which a user would read as a malfunction rather than a paused protection.
- `urlbar-local-network-blocked` — `browser/browser/browser.ftl` — "local network connections" is translated as "local device connections", duplicating the localhost tooltip.
    - Current: `Ви заблокували під'єднання до локальних пристроїв для цього вебсайту.`
    - Source: `tooltiptext: You have blocked local network connections for this website.`
    - Suggest: `Ви заблокували під'єднання до локальної мережі для цього вебсайту.`
    - en-US distinguishes urlbar-localhost-blocked ("local device connections") from urlbar-local-network-blocked ("local network connections"); the Ukrainian text is identical for both, so the user cannot tell which permission was blocked.
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — "Search Actions" (search within Actions) is rendered as "Actions with search".
    - Current: `Дії з пошуком`
    - Source: `Search Actions`
    - Suggest: `Шукати в діях`
    - The group comment states "In these actions 'Search' is a verb, followed by where the search is performed", and the sibling strings follow that pattern ("Шукати в закладках", "Шукати в історії", "Шукати у вкладках"). Here the verb is lost.
- `main-context-menu-bidi-switch-text` — `browser/browser/browserContext.ftl` — "Switch Text Direction" is translated identically to "Switch Page Direction".
    - Current: `Перемкнути напрям тексту на сторінці`
    - Source: `accesskey: w label: Switch Text Direction`
    - Suggest: `Перемкнути напрям тексту`
    - main-context-menu-bidi-switch-page has the same Ukrainian label, so the two distinct context-menu commands are indistinguishable; the text-direction item should not say "на сторінці".
- `contextual-manager-passwords-remove-all-confirm-button` — `browser/browser/contextual-manager.ftl` — `contextual-manager-passwords-remove-all-confirm-button` references ['count'], which en-US does not pass
    - Current: `{$total ->} [one] Вилучити [few] Вилучити { $count } [many] Вилучити { $count } [other] Вилучити все`
    - Source: `{$total ->} [1] Remove [other] Remove all`
    - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.
- `downloads-details` — `browser/browser/downloads.ftl` — The noun phrase "Download details" is rendered as the imperative "Download the details".
    - Current: `Завантажити подробиці`
    - Source: `title: Download details`
    - Suggest: `Подробиці завантаження`
    - The developer comment says this is the title shown at the top of the download details sub-panel, i.e. a heading, not an action; "Завантажити" is the verb "to download".
- `actions-callout-subtitle` — `browser/browser/featureCallout.ftl` — The example keyword "очистити" does not match the localized quick-action keyword, so the demonstrated action won't appear.
    - Current: `або “очистити”, щоб стерти історію`
    - Source: `Try typing an action like “print” to print a page, or “clear” to clear your history.`
    - Suggest: `або “стерти”, щоб стерти історію`
    - The developer comment explicitly ties this example to quickactions-cmd-clearrecenthistory2 and says the translations must match; that string uses "стерти" ("стерти недавню історію"), not "очистити", so typing the suggested word produces no action button.
- `genai-prompts-proofread` — `browser/browser/genai.ftl` — "the selection" is rendered as "розділ" (section/chapter) in the proofreading prompt.
    - Current: `Перевірте розділ на наявність орфографічних і граматичних помилок.`
    - Source: `label: Proofread value: Please proofread the selection for spelling and grammar errors. Identify any mistakes and provide a corrected version of the text. Maintain the meaning and factual accuracy and output the list of…`
    - Suggest: `Перевірте вибране на наявність орфографічних і граматичних помилок.`
    - All other prompts in this group render "the selection" as "вибране"; here the chatbot is told to proofread a "section", which is not what is being sent.
- `genai-prompts-quiz` — `browser/browser/genai.ftl` — The quiz prompt instruction "Please quiz me on this selection" is rendered as "Clarify the selection".
    - Current: `Уточнити вибране.`
    - Source: `label: Quiz me value: Please quiz me on this selection. Ask me a variety of types of questions, for example multiple choice, true or false, and short answer. Wait for my response before moving on to the next question.`
    - Suggest: `Поставте мені запитання щодо вибраного.`
    - This text is the instruction actually sent to the chatbot. "Уточнити" means to clarify/refine, which asks the chatbot to do something different from quizzing the user, contradicting the rest of the prompt about asking question types and waiting for answers.
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Malformed closing tag `</a >` in `genai-settings-chat-gemini-links`
    - Current: `Вибираючи Google Gemini, ви погоджуєтеся із <a data-l10n-name="link1">Загальними положеннями та умовами Google</a>, <a data-l10n-name="link2">Правилами щодо забороненого використання генеративного ШІ</a > та <a data-l10…`
    - Source: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
    - Whitespace inside a closing tag makes it render as literal text.
- `link-preview-settings-long-press` — `browser/browser/genai.ftl` — "Shortcut:" before a click-and-hold gesture is rendered as "Keyboard shortcut:".
    - Current: `Комбінація клавіш: натисніть і утримуйте посилання протягом 1 секунди (тривале натискання)`
    - Source: `label: Shortcut: Click and hold the link for 1 second (long press)`
    - Suggest: `Ярлик: натисніть і утримуйте посилання протягом 1 секунди (тривале натискання)`
    - The gesture described is a long mouse press on a link, not a key combination, so "Комбінація клавіш" contradicts the rest of the same sentence.
- `fxa-menu-message-backup-sync-secondary-text` — `browser/browser/newtab/asrouter.ftl` — "most of your data" rendered as "your data", widening what Sync is claimed to back up.
    - Current: `За допомогою синхронізації створюється резервна копія ваших даних, щоб ви могли отримати до них доступ усюди, де використовуєте { -brand-short-name }.`
    - Source: `Sync backs up most of your data so you can access it everywhere you use { -brand-short-name }.`
    - Suggest: `За допомогою синхронізації створюється резервна копія більшості ваших даних, щоб ви могли отримати до них доступ усюди, де використовуєте { -brand-short-name }.`
    - en-US: "Sync backs up most of your data…". Dropping "most of" makes the product promise a complete backup of the user's data, a claim the English deliberately avoids.
- `newtab-widget-lists-empty-cta` — `browser/browser/newtab/newtab.ftl` — Empty-state invitation "Add one" rendered as "Add more".
    - Current: `Можливості безмежні. Додайте ще.`
    - Source: `The possibilities are endless. Add one.`
    - Suggest: `Можливості безмежні. Додайте запис.`
    - The developer comment states that "Add one" means adding a new task to the list, and the string is shown when the list is empty; "Додайте ще" asks the user to add more items to a list that contains none.
- `newtab-widget-lists-name-label-checklist` — `browser/browser/newtab/newtab.ftl` — "Checklist" translated as "Список завдань" (Task list), colliding with the Task list label.
    - Current: `Список завдань`
    - Source: `label: Checklist`
    - Suggest: `Контрольний список`
    - en-US value is "Checklist"; the sibling string newtab-widget-lists-name-label-default ("Task list") already uses "Список завдань", and newtab-widget-lists-name-default / newtab-widget-lists-name-placeholder-checklist2 render "Checklist" as "Контрольний список". The two distinct list types end up with the same name on the same surface.
- `panic-button-open-new-window` — `browser/browser/panicButton.ftl` — A pending action in the “Proceeding will:” list is stated as already done.
    - Current: `Відкрито нове чисте вікно`
    - Source: `Open a new clean Window`
    - Suggest: `відкриття нового чистого вікна`
    - This item completes the sentence “Це призведе до:” describing what will happen; the past passive “Відкрито” tells the user a new clean window has already been opened.
- `places-details-pane-select-an-item-description` — `browser/browser/places.ftl` — “Select an item to view and edit its properties” is rendered as “Add an item to the view and edit its properties”.
    - Current: `Додати елемент до перегляду та редагувати його властивості`
    - Source: `Select an item to view and edit its properties`
    - Suggest: `Виберіть елемент, щоб переглянути та змінити його властивості`
    - The en-US instructs the user to select an existing item; the Ukrainian tells them to add an item, which is a different action the Library details pane does not perform.
- `policy-AppUpdatePin` — `browser/browser/policies/policies-descriptions.ftl` — The verb "updated" is missing, leaving a sentence that does not say what the policy does.
    - Current: `Не дозволяти { -brand-short-name } після вказаної версії.`
    - Source: `Prevent { -brand-short-name } from being updated beyond the specified version.`
    - Suggest: `Не дозволяти оновлювати { -brand-short-name } після вказаної версії.`
    - en-US: "Prevent { -brand-short-name } from being updated beyond the specified version." The Ukrainian reads "Do not allow Firefox after the specified version", which omits the update action entirely and leaves an administrator unable to tell what the policy controls.
- `policy-DisabledCiphers` — `browser/browser/policies/policies-descriptions.ftl` — "Disable ciphers" rendered as "disable encryption".
    - Current: `Вимкнути шифрування.`
    - Source: `Disable ciphers.`
    - Suggest: `Вимкнути шифри.`
    - en-US "Disable ciphers" refers to disabling individual TLS cipher suites; "Вимкнути шифрування" tells the administrator the policy turns off encryption as such, a materially different and much broader action.
- `clear-site-data-description` — `browser/browser/preferences/clearSiteData.ftl` — The reassurance that clearing cache does not affect logins is missing from the dialog description.
    - Current: `Стирання всіх файлів cookie та даних сайтів, що зберігаються в { -brand-short-name }, може призвести до виходу на вебсайтах та вилучення автономного вебвмісту.`
    - Source: `Clearing all cookies and site data stored by { -brand-short-name } may sign you out of websites and remove offline web content. Clearing cache data will not affect your logins.`
    - Suggest: `Стирання всіх файлів cookie та даних сайтів, що зберігаються в { -brand-short-name }, може призвести до виходу на вебсайтах та вилучення автономного вебвмісту. Стирання даних кешу не вплине на ваші входи.`
    - The en-US string ends with “Clearing cache data will not affect your logins.”, which the Ukrainian omits, so the user loses the information distinguishing the two checkboxes in the dialog.
- `fonts-langgroup-trad-chinese` — `browser/browser/preferences/fonts.ftl` — The “(Taiwan)” qualifier is dropped, leaving two near-identical Traditional Chinese entries.
    - Current: `fonts-langgroup-trad-chinese =     .label = Традиційна китайська`
    - Source: `label: Traditional Chinese (Taiwan)`
    - Suggest: `fonts-langgroup-trad-chinese =     .label = Традиційна китайська (Тайвань)`
    - en-US is “Traditional Chinese (Taiwan)” and the neighbouring entry is “Traditional Chinese (Hong Kong)” (translated with “(Гонконг)”). Without the qualifier the list gives no way to tell the two font groups apart.
- `autofill-address-county` — `browser/browser/preferences/formAutofill.ftl` — “County” (an administrative subdivision) is rendered as “Країна”, which means “country”.
    - Current: `autofill-address-county = Країна`
    - Source: `County`
    - Suggest: `autofill-address-county = Округ`
    - The en-US label is “County”, a level below the country. The Ukrainian says “Країна” (country), which is the exact translation already used for autofill-address-country, so the address form shows two identical “Країна” fields and the county field asks for the wrong information.
- `autofill-address-department` — `browser/browser/preferences/formAutofill.ftl` — “Department” as a territorial division is translated as “Відділ” (an office/section).
    - Current: `autofill-address-department = Відділ`
    - Source: `Department`
    - Suggest: `autofill-address-department = Департамент`
    - The developer comment says the field is “Used in Nicaragua (NI), Colombia (CO) as primary address information (1 level below the country level)” — i.e. a territorial department. “Відділ” means a department/section of an organization and makes the address field meaningless.
- `permissions-searchbox` — `browser/browser/preferences/permissions.ftl` — The placeholder reads as “search within the site” instead of “search the list of websites”.
    - Current: `.placeholder = Пошук по сайту`
    - Source: `placeholder: Search Website`
    - Suggest: `.placeholder = Пошук вебсайтів`
    - The box filters the list of websites shown in the exceptions dialog; “Пошук по сайту” tells the user they are searching inside a site. The parallel string in siteDataSettings.ftl correctly uses “Пошук вебсайтів”.
- `avatar-selector-icon-tab` — `browser/browser/profiles.ftl` — The “Icon” tab label is rendered as “Avatar”.
    - Current: `Аватар`
    - Source: `Icon`
    - Suggest: `Піктограма`
    - This is one of two tabs (Icon / Custom) inside the avatar picker; calling the tab “Аватар” loses the contrast with the Custom tab and duplicates the section heading edit-profile-page-avatar-header-2.
- `profiles-appmenu-callout-tour-subtitle` — `browser/browser/profiles.ftl` — “spin up another [profile]” is rendered as “open another profile” instead of creating one.
    - Current: `відкрити інший профіль`
    - Source: `In the ☰ menu, tap your profile name to spin up another, edit this one, or hop between your digital lives.`
    - Suggest: `створити інший профіль`
    - The developer comment states explicitly that “Spin up another” means creating another profile; the Ukrainian describes opening an existing one, so the described way to create a profile is lost.
- `split-view-menuitem-separate-tabs` — `browser/browser/tabbrowser.ftl` — “Separate Tabs” (undo the split view) is rendered as “Split the tabs”.
    - Current: `Розділити вкладки`
    - Source: `label: Separate Tabs`
    - Suggest: `Роз'єднати вкладки`
    - The comment says “Separate” means separating the split-view tabs and displaying them normally; “Розділити” reads as creating a split (“розділений екран” is the locale's term for split view), i.e. the opposite action.
- `translations-panel-settings-always-translate-unknown-language` — `browser/browser/translations.ftl` — “Always translate this language” (source language) is rendered as “always translate INTO this language”.
    - Current: `Завжди перекладати цією мовою`
    - Source: `label: Always translate this language`
    - Suggest: `Завжди перекладати цю мову`
    - The instrumental case (цією мовою) marks the target language in this file (cf. translations-panel-to-label “Перекласти мовою”), so the setting reads as choosing a target language, while the option actually always translates pages written in the detected source language.
- `translations-panel-settings-never-translate-unknown-language` — `browser/browser/translations.ftl` — “Never translate this language” (source language) is rendered as “never translate INTO this language”.
    - Current: `Ніколи не перекладати цією мовою`
    - Source: `label: Never translate this language`
    - Suggest: `Ніколи не перекладати цю мову`
    - Same case error as the always-translate variant: instrumental marks the target language, but the option concerns the page's source language.
- `webrtc-screen-system-menu` — `browser/browser/webrtcIndicator.ftl` — “a window or a screen” is narrowed to “a window”.
    - Current: `Ви надаєте доступ до вікна. Натисніть для керування спільним доступом.`
    - Source: `label: You are sharing a window or a screen. Click to control sharing.`
    - Suggest: `Ви надаєте доступ до вікна або екрана. Натисніть для керування спільним доступом.`
    - The tooltip is shown for both window and full-screen sharing; dropping “or a screen” tells a user sharing their whole screen that only a window is being shared.
- `webrtc-sharing-menu` — `browser/browser/webrtcIndicator.ftl` — “Tabs sharing devices” is reversed to “Devices with access to tabs”.
    - Current: `Пристрої з доступом до вкладок`
    - Source: `accesskey: d label: Tabs sharing devices`
    - Suggest: `Вкладки, що використовують пристрої`
    - The menu lists tabs that are currently using camera/microphone/screen devices. The Ukrainian inverts subject and object, telling the user devices have access to their tabs.
- `accessibility.contrast.annotation.AA` — `devtools/client/accessibility.properties` — The conformance level “AA” is dropped from the contrast annotation.
    - Current: `accessibility.contrast.annotation.AA = Відповідає стандартам WCAG для доступного тексту. %S`
    - Source: `Meets WCAG AA standards for accessible text. %S`
    - Suggest: `accessibility.contrast.annotation.AA = Відповідає стандартам WCAG AA для доступного тексту. %S`
    - The AAA counterpart keeps its level, so the user cannot tell the AA result from the AAA result, and the FAIL string is also level-less; the specific level is the information this annotation carries.
- `accessibility.simulation.contrastLoss` — `devtools/client/accessibility.properties` — “Contrast loss” is rendered as “Contrasting losses”.
    - Current: `accessibility.simulation.contrastLoss = Контрастні втрати`
    - Source: `Contrast loss`
    - Suggest: `accessibility.simulation.contrastLoss = Втрата контрасту`
    - “Контрастні втрати” reads as losses that are contrasty; the simulation option is about loss of contrast.
- `pauseOnCaughtExceptionsItem` — `devtools/client/debugger.properties` — “caught exceptions” is rendered as “defined/specified exceptions”.
    - Current: `pauseOnCaughtExceptionsItem = Призупиняти на визначених винятках`
    - Source: `Pause on caught exceptions`
    - Suggest: `pauseOnCaughtExceptionsItem = Призупиняти на перехоплених винятках`
    - “Визначених” means defined/specified; the checkbox controls pausing on exceptions that are caught by a handler, so the Ukrainian describes a different behaviour.
- `scopes.block` — `devtools/client/debugger.properties` — The noun “Block” (a block of code in the Scopes pane) is rendered as the verb “Block (something)”.
    - Current: `scopes.block = Блокувати`
    - Source: `Block`
    - Suggest: `scopes.block = Блок`
    - The comment says it refers to a block of code shown as a scope name; “Блокувати” is an imperative verb and reads as an action in a list of scopes.
- `colorPickerTooltip.contrastAgainstBgTitle` — `devtools/client/inspector.properties` — “Calculated against background” is rendered with “врозріз” (crosswise/contrary to).
    - Current: `colorPickerTooltip.contrastAgainstBgTitle = Розраховано врозріз тла: %S`
    - Source: `Calculated against background: %S`
    - Suggest: `colorPickerTooltip.contrastAgainstBgTitle = Розраховано відносно тла: %S`
    - “Врозріз” means "against the grain / contrary to" and is not the comparative "against" of the source; the label becomes unintelligible.
- `markupView.scrollableBadge.interactive.tooltip` — `devtools/client/inspector.properties` — “scrollable overflow” is rendered as “scroll overlay” (накладання).
    - Current: `markupView.scrollableBadge.interactive.tooltip = Цей елемент має накладання прокручування. Клацніть, щоб виявити елементи, що спричиняють накладання.`
    - Source: `This element has scrollable overflow. Click to reveal elements that are causing the overflow.`
    - Suggest: `markupView.scrollableBadge.interactive.tooltip = Цей елемент має вміст, що прокручується (переповнення). Клацніть, щоб виявити елементи, що спричиняють переповнення.`
    - “Накладання” means overlay; the badge is about content overflowing, and the non-interactive variant of the same tooltip correctly says “вміст, що прокручується”, so the user is told to look for overlays that do not exist.
- `heapview.field.retainedSize` — `devtools/client/memory.properties` — “Retained Size” is rendered as “Unallocated size”.
    - Current: `heapview.field.retainedSize = Нерозподілений розмір (байт)`
    - Source: `Retained Size (Bytes)`
    - Suggest: `heapview.field.retainedSize = Утриманий розмір (байт)`
    - “Нерозподілений” means not allocated, the opposite of memory retained (kept alive) by an object; it also contradicts the column's own tooltip which describes the sum of sizes kept alive.
- `heapview.field.shallowSize` — `devtools/client/memory.properties` — “Shallow Size” is rendered as “Small size”.
    - Current: `heapview.field.shallowSize = Малий розмір (байт)`
    - Source: `Shallow Size (Bytes)`
    - Suggest: `heapview.field.shallowSize = Поверхневий розмір (байт)`
    - “Малий” means small; shallow size is a technical term for the size of the object itself, as the column's tooltip says.
- `netmonitor.headers.referrerPolicy` — `devtools/client/netmonitor.properties` — “Referrer Policy” is rendered as “Redirect policy”.
    - Current: `netmonitor.headers.referrerPolicy = Політика перенаправлення`
    - Source: `Referrer Policy`
    - Suggest: `netmonitor.headers.referrerPolicy = Політика referrer`
    - “Перенаправлення” is redirection; the row shows the Referrer-Policy header value, so the label names a different HTTP mechanism than the value displayed next to it.
- `netmonitor.timings.requestTiming` — `devtools/client/netmonitor.properties` — “Request Timing” is rendered with reversed head noun: “Request of time”.
    - Current: `netmonitor.timings.requestTiming = Запит часу`
    - Source: `Request Timing`
    - Suggest: `netmonitor.timings.requestTiming = Час запиту`
    - The sibling heading netmonitor.timings.serverTiming is correctly “Час сервера”; “Запит часу” names a request for time rather than the request's timings.
- `netmonitor.toolbar.filter.media` — `devtools/client/netmonitor.properties` — The “Media” request-type filter is labelled “Матеріал” (material).
    - Current: `netmonitor.toolbar.filter.media = Матеріал`
    - Source: `Media`
    - Suggest: `netmonitor.toolbar.filter.media = Медіа`
    - The button filters audio/video requests; “Матеріал” does not denote media files and sits oddly among HTML/CSS/JS/Шрифти/Зображення.
- `responsive.deviceDetails.touch` — `devtools/client/responsive.properties` — The tooltip field label “Touch:” is rendered as the imperative “Tap!”.
    - Current: `responsive.deviceDetails.touch = Торкніться: %1$S`
    - Source: `Touch: %1$S`
    - Suggest: `responsive.deviceDetails.touch = Дотик: %1$S`
    - The string labels a boolean value for touch support; “Торкніться” is an imperative verb, and the combined tooltip (responsive.deviceDetails) correctly uses the noun “Дотик”.
- `storage-table-headers-extension-storage-area` — `devtools/client/storage.ftl` — “Storage Area” is rendered as “Storage volume/size”.
    - Current: `storage-table-headers-extension-storage-area = Обсяг сховища`
    - Source: `Storage Area`
    - Suggest: `storage-table-headers-extension-storage-area = Область сховища`
    - The column shows the extension storage area (local/sync), not a size; “Обсяг” tells the user to expect a quantity.
- `styleeditor-pretty-print-button` — `devtools/client/styleeditor.ftl` — The button action “Pretty print style sheet” is turned into the noun phrase “Style sheet for pretty printing”.
    - Current: `.title = Таблиця стилів для структурного друку`
    - Source: `title: Pretty print style sheet`
    - Suggest: `.title = Структурно надрукувати таблицю стилів`
    - The title describes what the button does; as translated it labels an object rather than the action, unlike the disabled variants which keep the verb.
- `options-stylesheet-autocompletion-tooltip` — `devtools/client/toolbox-options.ftl` — CSS “selectors” is rendered as “вибірок” (samples/selections).
    - Current: `Автоматичне доповнення властивостей, значень і вибірок CSS у редакторі стилів під час набирання`
    - Source: `title: Autocomplete CSS properties, values and selectors in Style Editor as you type`
    - Suggest: `Автоматичне доповнення властивостей, значень і селекторів CSS у редакторі стилів під час набирання`
    - The locale uses “селектор” for CSS selectors throughout (styleinspector.properties, screenshot.properties); “вибірка” names something else.
- `accessibility.text.label.issue.heading.content` — `devtools/shared/accessibility.properties` — “Headings should have visible text content” is rendered as “must have a visible text label”.
    - Current: `accessibility.text.label.issue.heading.content = Заголовки повинні мати видиму текстову мітку.`
    - Source: `Headings should have visible text content.`
    - Suggest: `accessibility.text.label.issue.heading.content = Заголовки повинні мати видимий текстовий вміст.`
    - The audit checks for visible text content, not a label; the counterpart string in accessibility.ftl correctly says “видимий текстовий вміст”, so the advice here tells the developer to fix the wrong thing.
- `whypaused-promise-rejection` — `devtools/shared/debugger-paused-reasons.ftl` — The JavaScript term “promise” is rendered as “перспектива” (prospect/outlook).
    - Current: `whypaused-promise-rejection = Призупинено на відхиленні перспективи`
    - Source: `Paused on promise rejection`
    - Suggest: `whypaused-promise-rejection = Призупинено на відхиленні Promise`
    - “Перспектива” is not the JS Promise object; the pause reason no longer names the construct the debugger stopped on.
- `rule.status.PARENT_MATCH` — `devtools/shared/styleinspector.properties` — “Parent Match” is rendered as “Matching source”, dropping the parent-element meaning.
    - Current: `rule.status.PARENT_MATCH = Відповідне джерело`
    - Source: `Parent Match`
    - Suggest: `rule.status.PARENT_MATCH = Збіг на батьківському елементі`
    - The status says the rule matched a parent node, not that a source matched; as translated the user cannot distinguish it from a plain match.
- `webconsole.filterInput.placeholder` — `devtools/shared/webconsole.properties` — “Filter Output” (filter the output) is rendered as “Filter's output”.
    - Current: `webconsole.filterInput.placeholder = Вивід фільтру`
    - Source: `Filter Output`
    - Suggest: `webconsole.filterInput.placeholder = Фільтрувати вивід`
    - The genitive construction names the output produced by a filter, not the action the input performs; comparable inputs in the tree use “Фільтрувати…”.
- `webconsole.input.selector.top` — `devtools/shared/webconsole.properties` — “Top” (the page's primary execution thread/context) is rendered as the direction “Up”.
    - Current: `webconsole.input.selector.top = Вгору`
    - Source: `Top`
    - Suggest: `webconsole.input.selector.top = Верхній`
    - The developer comment states this is the term for the primary thread of execution; “Вгору” is a direction adverb ("upwards"), so the context selector reads as a movement command instead of naming the top-level context.
- `webconsole.navigated` — `devtools/shared/webconsole.properties` — “Navigated to %S” is rendered as “Transferred/handed over to %S”.
    - Current: `webconsole.navigated = Передано до %S`
    - Source: `Navigated to %S`
    - Suggest: `webconsole.navigated = Перейдено до %S`
    - “Передано” means "was handed over/transmitted"; the message reports that the inspected page navigated to a new URL, which is a different event from something being transferred.
- `graphic` — `dom/chrome/accessibility/AccessFu.properties` — Accessibility role “graphic” rendered as “графік” (chart/schedule).
    - Current: `graphic = графік`
    - Source: `graphic`
    - Suggest: `graphic = графіка`
    - The role names an image/graphic; “графік” means a chart or a timetable, so screen-reader users hear the wrong role name.
- `summary` — `dom/chrome/accessibility/mac/accessible.properties` — Role description for <summary> rendered as “звіт” (report).
    - Current: `summary = звіт`
    - Source: `summary`
    - Suggest: `summary = зведення`
    - The comment says this is the roleDescription for the summary element (the disclosure label of <details>), not a report; screen readers would announce “report”.
- _…and 35 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `smartwindow-group-tabs-loading` — `browser/browser/autoTabGrouping.ftl` — The translation says the browser is checking whether groups by tab topic already exist, not that it is looking through the tabs for useful new groups.
    - Current: `Перевірка наявності груп за темою вкладки…`
    - Source: `Checking tabs for useful groups…`
    - Suggest: `Пошук корисних груп серед вкладок…`
    - The developer comment says the model is forming new groups from the open tabs and is explicitly not searching for tab groups that already exist. 'Перевірка наявності груп' means 'checking for the existence of groups', which is the reading the comment rules out. The word 'useful' is also missing.
- `places-load-js-data-url-error` — `browser/browser/placesPrompts.ftl` — The scheme “javascript:” lost its colon.
    - Current: `URL “javascript” або “data:”`
    - Source: `For security reasons, “javascript:” or “data:” URLs cannot be loaded from the history window or sidebar.`
    - Suggest: `URL “javascript:” або “data:”`
    - The developer comment marks `javascript:` and `data:` as untranslatable scheme identifiers; dropping the colon from one of them while keeping it on the other misstates the scheme.
- `language-name-dz` — `toolkit/toolkit/intl/languageNames.ftl` — Dzongkha is named after the country Bhutan rather than the language.
    - Current: `Бутанська`
    - Source: `Dzongkha`
    - Suggest: `Дзонг-ке`
    - The en-US is Dzongkha, a specific language; "Бутанська" means "Bhutanese", naming the country rather than the language, which no other entry in this list does.
- `language-name-ee` — `toolkit/toolkit/intl/languageNames.ftl` — Ewe is given a name that matches no language.
    - Current: `Ава`
    - Source: `Ewe`
    - Suggest: `Еве`
    - The en-US is Ewe, rendered in Ukrainian as "еве". "Ава" corresponds to no language name and is likely a corruption.
- `language-name-ie` — `toolkit/toolkit/intl/languageNames.ftl` — Interlingue is given the same name as Interlingua.
    - Current: `Інтерлінгва`
    - Source: `Interlingue`
    - Suggest: `Інтерлінгве`
    - language-name-ia (Interlingua) already uses "Інтерлінгва". Interlingue (Occidental) is a different constructed language, so two distinct entries collide in the language list.
- `language-name-kn` — `toolkit/toolkit/intl/languageNames.ftl` — Kannada is named "Canadian".
    - Current: `Канадська`
    - Source: `Kannada`
    - Suggest: `Каннада`
    - "Канадська" means Canadian. The en-US is Kannada, the Dravidian language of Karnataka, which in Ukrainian is "каннада".
- `language-name-su` — `toolkit/toolkit/intl/languageNames.ftl` — Sundanese is named "Sudanese".
    - Current: `Суданська`
    - Source: `Sundanese`
    - Suggest: `Сунданська`
    - The en-US is Sundanese (of West Java); "Суданська" names Sudan. The missing "н" turns it into a different country's adjective.
- `language-name-tn` — `toolkit/toolkit/intl/languageNames.ftl` — Tswana is named after the whole Bantu language family.
    - Current: `Банту`
    - Source: `Tswana`
    - Suggest: `Тсвана`
    - The en-US is Tswana, a single language; "Банту" is the name of a family of hundreds of languages, so the entry names something else.
- `region-name-dm` — `toolkit/toolkit/intl/regionNames.ftl` — Dominica rendered in the wrong form.
    - Current: `Домінік`
    - Source: `Dominica`
    - Suggest: `Домініка`
    - The en-US is Dominica, whose Ukrainian name is "Домініка"; "Домінік" is a personal name, not the country.
- `region-name-nu` — `toolkit/toolkit/intl/regionNames.ftl` — Niue is misnamed.
    - Current: `Нія`
    - Source: `Niue`
    - Suggest: `Ніуе`
    - The en-US is Niue; the established Ukrainian name is "Ніуе". "Нія" is not a country name.
- `region-name-xp` — `toolkit/toolkit/intl/regionNames.ftl` — Paracel Islands labelled as the Faroe Islands.
    - Current: `Фарерські острови`
    - Source: `Paracel Islands`
    - Suggest: `Парасельські острови`
    - The en-US for region-name-xp is "Paracel Islands" (South China Sea). The locale duplicates the name used for region-name-fo (Faroe Islands), so two unrelated territories carry the same name.

### C. Grammar, agreement & spelling

- `about-logins-import-dialog-items-error` — `browser/browser/aboutLogins.ftl` — "(not imported)" is left in English although the sibling strings translate it.
    - Current: `<span data-l10n-name="meta">(not imported)</span>`
    - Source: `{$count ->} [other] <span>Errors:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
    - Suggest: `<span data-l10n-name="meta">(не імпортовано)</span>`
    - about-logins-import-dialog-items-no-change2 and the import-report strings all render the same phrase as "(не імпортовано)"; this one row shows English in an otherwise Ukrainian dialog.
- `genai-menu-open-generic` — `browser/browser/genai.ftl` — "Open AI Chatbot" was read as the brand "OpenAI", producing "OpenAI chatbot".
    - Current: `Чат-бот Open AI`
    - Source: `label: Open AI Chatbot`
    - Suggest: `Відкрити чат-бот з ШІ`
    - "Open" is the verb here, matching genai-menu-open-provider ("Відкрити { $provider }") and genai-menu-remove-generic ("Вилучити чат-бот з ШІ"). The translation instead names an unrelated company, regardless of which provider is configured.
- `media-image-type` — `browser/browser/pageInfo.ftl` — English word order kept: “{ $type } Зображення”.
    - Current: `{ $type } Зображення`
    - Source: `value: { $type } Image`
    - Suggest: `Зображення { $type }`
    - Ukrainian places the type after the noun, as the sibling string media-animated-image-type already does (“Зображення { $type } (анімація…)”); the current order renders as e.g. “JPEG Зображення”.
- `speech-recognition-model-download-progressbar` — `browser/browser/permissions.ftl` — 'Процес' ('process') is used where the English says 'progress' ('Прогрес'). It looks like a typo.
    - Current: `Процес завантаження`
    - Source: `aria-label: Speech recognition model download progress`
    - Suggest: `Прогрес завантаження`
    - The source says 'download progress'. This is the accessible name of a progress bar, so it should name the progress ('Прогрес' or 'Хід'), not the process.
- `policy-StartDownloadsInTempDirectory` — `browser/browser/policies/policies-descriptions.ftl` — Double space inside the visible text.
    - Current: `в локальне тимчасове розташування,  а не в усталений каталог завантаження`
    - Source: `Force downloads to start off in a local, temporary location rather than the default download directory.`
    - Suggest: `в локальне тимчасове розташування, а не в усталений каталог завантаження`
    - There are two spaces after the comma in the rendered description text.
- `safeb-blocked-unwanted-page-error-desc-override` — `browser/browser/safebrowsing/blockedSite.ftl` — "reported as containing harmful software" is rendered with the same wording as the malware string, "містить зловмисні програми" (malicious software), losing the unwanted/harmful-software distinction.
    - Current: `як такий, що містить зловмисні програми`
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing harmful software</a>. You can <a data-l10n-name='ignore_warning_link'>ignore the risk</a> and go t…`
    - Suggest: `як такий, що містить шкідливе програмне забезпечення`
    - In the same safe-browsing surface the malware strings (safeb-blocked-malware-page-error-desc-*) already use "містить зловмисні програми", while the file's own unwanted-software strings elsewhere use "небажане програмне забезпечення" (safeb-blocked-unwanted-page-learn-more) and "небезпечні програми" (title). Both safeb-blocked-unwanted-page-error-desc-override and -no-override reuse the malware wo…
- `protections-blocking-cryptominers` — `browser/browser/siteProtections.ftl` — Misspelling of “криптомайнерів”.
    - Current: `Заблоковано криптомайренів`
    - Source: `title: Cryptominers Blocked`
    - Suggest: `Заблоковано криптомайнерів`
    - “криптомайренів” is a typo; every other occurrence in the tree spells it “криптомайнер(ів)”.
- `inactive-css-position-property-on-unpositioned-box-fix` — `devtools/client/tooltips.ftl` — The CSS property name inside <strong> is translated, although the section comment says CSS properties must not be translated.
    - Current: `Спробуйте налаштувати його властивість <strong>позиції</strong> на щось інше, ніж <strong>static</strong>.`
    - Source: `Try setting its <strong>position</strong> property to something other than <strong>static</strong>. { learn-more }`
    - Suggest: `Спробуйте налаштувати його властивість <strong>position</strong> на щось інше, ніж <strong>static</strong>.`
    - The group comment states “CSS properties and values in <strong> tags should not be translated”; “позиції” is not a CSS keyword a developer can type.
- `inactive-css-position-property-on-unpositioned-box-fix-1` — `devtools/client/tooltips.ftl` — Same translated CSS property name inside <strong> in the no-link variant of the fix message.
    - Current: `inactive-css-position-property-on-unpositioned-box-fix-1 = Спробуйте налаштувати його властивість <strong>позиції</strong> на щось інше, ніж <strong>static</strong>.`
    - Source: `Try setting its <strong>position</strong> property to something other than <strong>static</strong>.`
    - Suggest: `inactive-css-position-property-on-unpositioned-box-fix-1 = Спробуйте налаштувати його властивість <strong>position</strong> на щось інше, ніж <strong>static</strong>.`
    - Same do-not-translate rule as the -fix variant: the CSS property name `position` must stay in English.
- `PushMessageBadEncryptionHeader` — `dom/chrome/dom/dom.properties` — Header name “Encryption” translated despite do-not-translate comment.
    - Current: `Заголовок ‘Шифрування’`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. The ‘Encryption’ header must include a unique ‘salt‘ parameter for each message. See https://tools.ietf.org/html/draft-ietf-httpbis-encryption-encodin…`
    - Suggest: `Заголовок ‘Encryption’`
    - The developer comment says: Do not translate “ServiceWorker”, “Encryption”, and “salt”. A translated header name cannot be matched against the actual HTTP header.
- `ServiceWorkerNoFetchHandler` — `dom/chrome/dom/dom.properties` — Event name “Fetch” translated as “Отримання”.
    - Current: `Отримання обробників події повинно бути додано`
    - Source: `Fetch event handlers must be added during the worker script’s initial evaluation.`
    - Suggest: `Обробники події Fetch повинні бути додані`
    - The developer comment states: Do not translate “Fetch”. The translation also reads as “obtaining handlers” rather than “Fetch event handlers”.
- `PEPRInheritsFieldMissing` — `dom/chrome/layout/css.properties` — CSS descriptor “inherits” translated as “спадкоємець”.
    - Current: `Відсутній дескриптор-спадкоємець @property.`
    - Source: `@property inherits descriptor is missing.`
    - Suggest: `Відсутній дескриптор inherits для @property.`
    - The developer comment says: Do not translate “inherits” because it is a technical term. The author needs the literal descriptor name. PEPRInheritsFieldInvalid has the same substitution.
- `BlockFileScriptWithWrongMimeType` — `dom/chrome/security/security.properties` — “file: URI” scheme translated as “файлу:”.
    - Current: `Завантаження скрипту з файлу: URI (“%1$S”)`
    - Source: `Loading script from file: URI (“%1$S”) was blocked because its MIME type (“%2$S”) is not a valid JavaScript MIME type.`
    - Suggest: `Завантаження скрипту з file: URI (“%1$S”)`
    - The developer comment states: Do not translate “file: URI”.
- `BlockRedirectToDataURI` — `dom/chrome/security/security.properties` — “data: URI” scheme translated as “даних:”.
    - Current: `Перенаправлення до даних: URI не дозволено`
    - Source: `Redirecting to data: URI not allowed (Blocked loading of: “%1$S”)`
    - Suggest: `Перенаправлення до data: URI не дозволено`
    - The comment says do not translate “data: URI”; BlockTopLevelDataURINavigation above keeps “data: URI” untranslated.
- `XTCOWithMIMEValueMissing` — `dom/chrome/security/security.properties` — Header name partially translated: “X-Content-Type-Опції”.
    - Current: `(X-Content-Type-Опції: nosniff)`
    - Source: `The resource from “%1$S” was not rendered due to an unknown, incorrect or missing MIME type (X-Content-Type-Options: nosniff).`
    - Suggest: `(X-Content-Type-Options: nosniff)`
    - The comment says do not translate “X-Content-Type-Options” or “nosniff”; MimeTypeMismatch2 in the same file keeps the header intact.
- `about-sync-log-search-input` — `toolkit/services/aboutSyncLog.ftl` — The preposition "в" falls between two consonants where Ukrainian requires "у".
    - Current: `Пошук в журналах`
    - Source: `aria-label: Search logs placeholder: Search logs`
    - Suggest: `Пошук у журналах`
    - Ukrainian euphony rules call for "у" between consonants. "Пошук" ends in a consonant and "журналах" starts with one, so "у журналах" is correct. This applies to both the aria-label and the placeholder.
- `autofill-card-network-amex` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Brand name contains a Cyrillic homoglyph instead of a Latin letter.
    - Current: `Аmerican Express`
    - Source: `American Express`
    - Suggest: `American Express`
    - The initial "А" is Cyrillic U+0410, not Latin "A". The section comment says these are brand names; a mixed-script string breaks search, matching and screen-reader pronunciation of the card brand.
- `autofill-card-network-cartebancaire` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Brand name contains a Cyrillic homoglyph instead of a Latin letter.
    - Current: `Сarte Bancaire`
    - Source: `Carte Bancaire`
    - Suggest: `Carte Bancaire`
    - The initial "С" is Cyrillic U+0421, not Latin "C", in a string the comment marks as a brand name that should stay as-is.
- `autofill-card-network-diners` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Brand name contains a Cyrillic homoglyph instead of a Latin letter.
    - Current: `Dіners Club`
    - Source: `Diners Club`
    - Suggest: `Diners Club`
    - The second character is Cyrillic "і" (U+0456), not Latin "i", in a brand name the section comment says must not be altered.
- `autofill-card-network-discover` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Brand name contains a Cyrillic homoglyph instead of a Latin letter.
    - Current: `Dіscover`
    - Source: `Discover`
    - Suggest: `Discover`
    - The second character is Cyrillic "і" (U+0456), not Latin "i", in a brand name that should remain untouched.
- `autofill-card-network-mastercard` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Brand name contains a Cyrillic homoglyph instead of a Latin letter.
    - Current: `MasterCаrd`
    - Source: `MasterCard`
    - Suggest: `MasterCard`
    - The "а" after "MasterC" is Cyrillic U+0430, not Latin "a", in a brand name the section comment says must not be altered.
- `autofill-card-network-unionpay` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Brand name contains a Cyrillic homoglyph instead of a Latin letter.
    - Current: `Uniоn Pay`
    - Source: `Union Pay`
    - Suggest: `Union Pay`
    - The "о" in "Union" is Cyrillic U+043E, not Latin "o", in a brand name that should remain untouched.
- `autofill-card-network-visa` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Brand name contains a Cyrillic homoglyph instead of a Latin letter.
    - Current: `Vіsa`
    - Source: `Visa`
    - Suggest: `Visa`
    - The second character is Cyrillic "і" (U+0456), not Latin "i", in a brand name the section comment says must not be altered.
- `btp-warning-tracker-purged` — `toolkit/toolkit/global/antiTracking.ftl` — "bounce tracker" translated despite a do-not-translate comment.
    - Current: `елемент стеження відмов`
    - Source: `The state of “{ $siteHost }” was recently purged because it was detected as a bounce tracker.`
    - Suggest: `"bounce tracker"`
    - The developer comment says "Do not translate 'bounce tracker'", and the sibling string btp-warning-tracker-classified correctly keeps the English term. "елемент стеження відмов" is both a translation of a DNT term and an unrecognizable coinage.

### D. Terminology, register & consistency

- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — The [1] variant uses the plural "паролів" where a single password is being removed.
    - Current: `[1] Ця дія призведе до вилучення паролів, збережених у { -brand-short-name }, на всіх синхронізованих пристроях`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices. This will also remove any breach alerts that appear here. You cannot undo this action. [other] This will remove al…`
    - Suggest: `[1] Ця дія призведе до вилучення пароля, збереженого у { -brand-short-name }, на всіх синхронізованих пристроях`
    - en-US uses the singular "the password" in the [1] variant, and the non-synced counterpart about-logins-confirm-remove-all-dialog-message2 correctly uses "пароля" there; this variant claims all passwords will be deleted.
- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — `backup-file-moz-browser-restore-step-2-1` quotes “Відновити дані” but the string it names, `restore-from-backup-header`, reads “Відновіть свої дані”
    - Current: `Натисніть “Відновити дані” та виберіть цей файл`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Відновіть свої дані`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — `backup-file-other-browser-restore-step-3-1` quotes “Відновити дані” but the string it names, `restore-from-backup-header`, reads “Відновіть свої дані”
    - Current: `Натисніть “Відновити дані” та виберіть цей файл`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Відновіть свої дані`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `menu-edit-bidi-switch-text-direction` — `browser/browser/menubar.ftl` — “Switch Text Direction” is rendered identically to “Switch Page Direction”.
    - Current: `Перемкнути напрям тексту на сторінці`
    - Source: `accesskey: w label: Switch Text Direction`
    - Suggest: `Перемкнути напрям тексту`
    - The Edit-menu command switches the direction of text in the focused field, not of the page; the added “на сторінці” duplicates menu-view-bidi-switch-page-direction, leaving the two distinct commands indistinguishable.
- `multi-cta-fox-doodle-msix-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — Wrong case after "закріпіть на": accusative instead of locative.
    - Current: `закріпіть його на панель завдань і в меню Пуск`
    - Source: `Keep your favorite privacy-focused browser just one click away. Set { -brand-short-name } as your default browser for opening links and pin it to your taskbar and Start menu.`
    - Suggest: `закріпіть його на панелі завдань і в меню Пуск`
    - Same agreement error as in multi-cta-fox-doodle-privacy-focused-subtitle; "закріпити" requires "на панелі завдань", the form used throughout the rest of the file.
- `multi-cta-fox-doodle-privacy-focused-subtitle` — `browser/browser/newtab/asrouter.ftl` — Wrong case after "закріпіть на": accusative instead of locative.
    - Current: `закріпіть його на панель завдань`
    - Source: `{$sel_1 ->} [macos] Keep your favorite privacy-focused browser just one click away. Set { -brand-short-name } as your default browser for opening links and keep it in your Dock. [other] Keep your favorite privacy-focuse…`
    - Suggest: `закріпіть його на панелі завдань`
    - "Закріпити" (to pin something somewhere) governs the locative: "на панелі завдань", as used everywhere else in this file (spotlight-pin-primary-button, multi-cta-fox-doodle-pin-checkbox, windows-10-eos-challenger-pin-callout-subtitle).
- `windows-10-eos-challenger-sync-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — Dangling adverbial participle: its subject does not match the main clause.
    - Current: `Створивши резервну копію закладок і паролів { -brand-product-name }, вам буде легше перенести улюблений браузер на інший пристрій.`
    - Source: `When you back up your { -brand-product-name } bookmarks and passwords, it’s easier to bring the browser you chose to your next device.`
    - Suggest: `Якщо ви створите резервну копію закладок і паролів { -brand-product-name }, вам буде легше перенести улюблений браузер на інший пристрій.`
    - A дієприслівниковий зворот must share its subject with the main clause; here the main clause is impersonal ("вам буде легше"), so the participle has no valid subject.
- `fx-backup-confirmation-screen-easy-setup-item-text-1` — `browser/browser/newtab/onboarding.ftl` — Case disagreement in the list after the impersonal "Включено".
    - Current: `Включено закладки, історія, налаштування та інші дані`
    - Source: `Bookmarks, history, settings, and other data included`
    - Suggest: `Включено закладки, історію, налаштування та інші дані`
    - The impersonal predicate "включено" takes the accusative; "історія" is nominative and does not agree with the surrounding accusative items.
- `onboarding-new-user-survey-familiarity-based-option-4` — `browser/browser/newtab/onboarding.ftl` — Gendered masculine past-tense form used to address the user.
    - Current: `Користувався в минулому`
    - Source: `I used it in the past, but it’s been a while`
    - Suggest: `Користуюся в минулому → e.g. "Користувач(ка) у минулому" or a gender-neutral noun phrase such as "Раніше був досвід користування"`
    - The other options in the same survey use gender-neutral phrasing ("Новий користувач", "Користуюся певний час"); the masculine "Користувався" misgenders users who are not male.
- `onboarding-personalization-title` — `browser/browser/newtab/onboarding.ftl` — English-style noun adjunct: the brand name is used as an attribute before a noun.
    - Current: `Налаштуйте свою { -brand-short-name } роботу`
    - Source: `Customize your { -brand-short-name } experience`
    - Suggest: `Налаштуйте свою роботу з { -brand-short-name }`
    - Ukrainian does not place an unmarked noun (the brand) before another noun as a modifier; the phrase is ungrammatical. Compare onboarding-personalization-subtitle in the same file, which correctly uses "роботу з { -brand-short-name }".
- `autofill-card-billing-address` — `browser/browser/preferences/formAutofill.ftl` — Adjective does not agree with the feminine noun “адреса”.
    - Current: `autofill-card-billing-address = Платіжний адреса`
    - Source: `Billing Address`
    - Suggest: `autofill-card-billing-address = Платіжна адреса`
    - Gender agreement error: feminine “адреса” requires “Платіжна”.
- `autofill-card-billing-address-2` — `browser/browser/preferences/formAutofill.ftl` — Adjective does not agree with the feminine noun “адреса”.
    - Current: `Платіжний адреса`
    - Source: `label: Billing address`
    - Suggest: `Платіжна адреса`
    - “адреса” is feminine, so the attribute must be “Платіжна”, not the masculine “Платіжний”. Same error appears in autofill-card-billing-address.
- `fxa-qrcode-pair-step3` — `browser/browser/preferences/fxaPairDevice.ftl` — The word “Cканувати” starts with a Latin “C” instead of the Cyrillic “С”.
    - Current: `<strong>Cканувати</strong>`
    - Source: `3. Tap <strong>Ready to Scan</strong> and hold your phone over this code`
    - Suggest: `<strong>Сканувати</strong>`
    - The first character is U+0043 LATIN CAPITAL LETTER C, not U+0421 CYRILLIC CAPITAL LETTER ES; this is the only mixed-script word in the whole preferences partition and breaks search, spell check and font rendering of the word.
- `profiles-purple-theme-title` — `browser/browser/profiles.ftl` — The purple theme tooltip says “violet”, duplicating the violet theme tooltip.
    - Current: `Застосувати фіолетову тему`
    - Source: `title: Apply purple theme`
    - Suggest: `Застосувати бузкову тему`
    - The purple theme is labelled “Бузкова” but its tooltip says “фіолетову”, which is the exact text of profiles-violet-theme-title, so the two adjacent swatches get identical tooltips.
- `clearSiteDataPromptText` — `browser/chrome/browser/siteData.properties` — Dangling adverbial participle: "Вибравши…, усі файли … будуть стерті" attaches the gerund to an inanimate passive subject, which is ungrammatical in Ukrainian; the quotation marks are also straight "…" instead of the tree's “…”.
    - Current: `Вибравши "Стерти зараз", усі файли cookie та дані сайтів, які зберігаються в %S, будуть стерті.`
    - Source: `Selecting ‘Clear Now’ will clear all cookies and site data stored by %S. This may sign you out of websites and remove offline web content.`
    - Suggest: `Якщо вибрати “Стерти зараз”, усі файли cookie та дані сайтів, які зберігаються в %S, будуть стерті.`
    - A дієприслівниковий зворот must share its subject with the main clause; here the gerund ("вибравши") has the user as agent while the main clause's subject is "файли", a standard grammatical error. Separately, the rest of the uk browser tree uses typographic “…” (118 occurrences) and this string uses ASCII quotes.
- `UN_SURVEY_CHECKBOX_LABEL` — `browser/installer/custom.properties` — Missing comma before the subordinate clause.
    - Current: `Розкажіть Mozilla чому ви видалили $BrandShortName`
    - Source: `Tell Mozilla why you uninstalled $BrandShortName`
    - Suggest: `Розкажіть Mozilla, чому ви видалили $BrandShortName`
    - Ukrainian punctuation requires a comma before a subordinate clause introduced by "чому".
- `MUI_UNTEXT_WELCOME_INFO_TEXT` — `browser/installer/mui.properties` — Missing comma after the fronted adverbial clause.
    - Current: `Перш ніж почати переконайтеся, що $BrandFullNameDA не запущено.`
    - Source: `This wizard will guide you through the uninstallation of $BrandFullNameDA.  Before starting the uninstallation, make sure $BrandFullNameDA is not running.  $_CLICK`
    - Suggest: `Перш ніж почати, переконайтеся, що $BrandFullNameDA не запущено.`
    - The subordinate clause "Перш ніж почати" must be separated from the main clause by a comma.
- `inspector.showThreePaneMode` — `devtools/client/inspector.properties` — Ungrammatical “Увімкнути на 3-панельний інспектор” (stray preposition carried over from “Toggle on”).
    - Current: `inspector.showThreePaneMode = Увімкнути на 3-панельний інспектор`
    - Source: `Toggle on the 3-pane inspector`
    - Suggest: `inspector.showThreePaneMode = Увімкнути 3-панельний інспектор`
    - “Увімкнути” takes a direct object; the preposition “на” leaves the tooltip ungrammatical, and the paired hideThreePaneMode string has no such preposition.
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “Локального режиму” but the string it names, `options-local-mode-label`, reads “Локальний режим”
    - Current: `Цей документ також можна завантажити з “{ $url }” за допомогою “Локального режиму” в DevTools, який можна ввімкнути на панелі налаштувань.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Локальний режим`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `webconsole-commands-usage-unblock` — `devtools/shared/webconsole-commands.ftl` — “the exact same string previously passed to :block” becomes “the string that previously walked/passed to :block”.
    - Current: `Приймається лише один аргумент – такий самий рядок, який раніше пройшов до :block.`
    - Source: `:unblock URL_STRING  Stop blocking network requests    It accepts only one argument, the exact same string previously passed to :block.`
    - Suggest: `Приймається лише один аргумент – той самий рядок, який ви раніше передали команді :block.`
    - “Пройшов до” makes the string the subject of an intransitive motion verb, so the usage help no longer says the user passed it to the command.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — `preventedConsoleClear` quotes “Persist Logs” but the string it names, `webconsole.console.settings.menu.item.enablePersistentLogs.label`, reads “Постійне журналювання”
    - Current: `console.clear() було заблоковано через “Persist Logs”`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `Постійне журналювання`
    - In the source this string quotes “Persist Logs”, which is exactly the value of `webconsole.console.settings.menu.item.enablePersistentLogs.label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `CannotEncodeAllUnicode` — `dom/chrome/layout/HtmlForm.properties` — Garbled word “наділана” instead of “надіслана”.
    - Current: `Форма була наділана у кодуванні %S`
    - Source: `A form was submitted in the %S encoding which cannot encode all Unicode characters, so user input may get corrupted. To avoid this problem, the page should be changed so that the form is submitted in the UTF-8 encoding…`
    - Suggest: `Форму було надіслано в кодуванні %S`
    - “наділана” is not a Ukrainian word in this sense; en-US is “A form was submitted in the %S encoding”.
- `EncMetaTooLate` — `dom/chrome/layout/htmlparser.properties` — Missing conjunction after “намагається заявити,”.
    - Current: `Метатег намагається заявити, кодування символів оголошено запізно`
    - Source: `A meta tag attempting to declare the character encoding declaration was found too late, and the encoding was guessed from content instead. The meta tag needs to be moved to the start of the head part of the document.`
    - Suggest: `Метатег намагається заявити, що кодування символів оголошено запізно`
    - The subordinate clause has no “що”, unlike the parallel EncMetaTooLateFrame, leaving the sentence broken.
- `errNonSpaceInColgroupInFragment` — `dom/chrome/layout/htmlparser.properties` — Misspelling “анлізі”.
    - Current: `при анлізі фрагмента`
    - Source: `Non-space in “colgroup” when parsing fragment.`
    - Suggest: `при аналізі фрагмента`
    - Letter omission in “аналізі”.
- `errStartTagSeenWithoutRuby` — `dom/chrome/layout/htmlparser.properties` — Missing space before the quoted element name.
    - Current: `без відкритого елемента“ruby”`
    - Source: `Start tag “%1$S” seen without a “ruby” element being open.`
    - Suggest: `без відкритого елемента “ruby”`
    - The word and the quoted tag name run together in the rendered console message.
- `CompositorAnimationWarningTransformSVG` — `dom/chrome/layout/layout_errors.properties` — Misspelling “елементаї”.
    - Current: `на елементаї з SVG-трансформаціями`
    - Source: `Animations of ‘transform’ on elements with SVG transforms cannot be run on the compositor`
    - Suggest: `на елементах з SVG-трансформаціями`
    - “елементаї” is not a word; the locative plural is “елементах”.
- `accessError` — `dom/chrome/nsWebBrowserPersist.properties` — Sentence contains two conflicting predicates.
    - Current: `Неможливо зберегти %S не може бути збережений, тому що ви не можете міняти вміст вказаної теки.`
    - Source: `%S could not be saved, because you cannot change the contents of that folder.  Change the folder properties and try again, or try saving in a different location.`
    - Suggest: `Неможливо зберегти %S, тому що ви не можете змінювати вміст вказаної теки.`
    - “Неможливо зберегти %S” and “не може бути збережений” are stacked, leaving an ungrammatical sentence in a user-facing error dialog.
- `DeprecatedTLSVersion2` — `dom/chrome/security/security.properties` — Duplicated preposition “оновіть до TLS до версії”.
    - Current: `Будь ласка, оновіть до TLS до версії 1.2 або 1.3.`
    - Source: `This site uses a deprecated version of TLS. Please upgrade to TLS 1.2 or 1.3.`
    - Suggest: `Будь ласка, оновіть TLS до версії 1.2 або 1.3.`
    - “до” appears twice, leaving an ungrammatical sentence in a user-visible console warning.
- `xslt-nodeset-expected` — `dom/dom/xslt.ftl` — Wrong case form “типа” instead of “типу”.
    - Current: `повернути значення типа NodeSet`
    - Source: `An XPath expression was expected to return a NodeSet.`
    - Suggest: `повернути значення типу NodeSet`
    - The Ukrainian genitive of “тип” is “типу”; “типа” is a Russianism.
- `CookieRejectedEmptyNameAndValue` — `netwerk/necko.properties` — Ungrammatical “Файл cookie з без назви”.
    - Current: `Файл cookie з без назви та значення відхилено.`
    - Source: `Cookie with an empty name and an empty value has been rejected.`
    - Suggest: `Файл cookie без назви та значення відхилено.`
    - “з” and “без” are stacked; only one preposition belongs here.
- `MOZILLA_PKIX_ERROR_VALIDITY_TOO_LONG` — `security/manager/chrome/pipnss/nsserrors.properties` — Two stacked verbs: “який є діє занадто довго”.
    - Current: `сертифікат, який є діє занадто довго`
    - Source: `The server presented a certificate that is valid for too long.`
    - Suggest: `сертифікат, який діє занадто довго`
    - A leftover copula before “діє” makes the clause ungrammatical.
- `delete-email-cert-impact` — `security/manager/security/certificates/certManager.ftl` — Sentence ends on a dangling adjective; the noun is missing.
    - Current: `ви більше не зможете надсилати їй шифровані.`
    - Source: `If you delete a person’s e-mail certificate, you will no longer be able to send encrypted e-mail to that person.`
    - Suggest: `ви більше не зможете надсилати їй шифровані листи.`
    - en-US: “you will no longer be able to send encrypted e-mail to that person.” The object (“листи”/“повідомлення”) is absent, so the sentence breaks off mid-phrase.
- `button-accept` — `toolkit/chrome/global/dialog.properties` — The "OK" button label mixes Latin O with Cyrillic К.
    - Current: `OК`
    - Source: `OK`
    - Suggest: `OK`
    - The second character is Cyrillic "К" (U+041A) while the first is Latin "O". Everywhere else in the tree (commonDialogs.properties, popupnotification.ftl, crashreporter.ftl) the label is plain Latin "OK".
- `restartMessageNoUnlockerMac` — `toolkit/chrome/mozapps/profile/profileSelection.properties` — An untranslated English word "can" is left inside the Ukrainian sentence.
    - Current: `Лише одна копія %S can може бути відкрита одночасно.`
    - Source: `A copy of %S is already open. Only one copy of %S can be open at a time.`
    - Suggest: `Лише одна копія %S може бути відкрита одночасно.`
    - The English auxiliary "can" from the source was not removed when the sentence was translated, leaving a stray foreign word mid-sentence.
- `crashreporter-report-info` — `toolkit/crashreporter/crashreporter.ftl` — Misspelling: "місить" instead of "містить".
    - Current: `Цей звіт також місить інформацію`
    - Source: `This report also contains technical information about the state of the application when it crashed.`
    - Suggest: `Цей звіт також містить технічну інформацію`
    - "місить" means "kneads"; the intended verb is "містить" (contains). The en-US "technical information" is also reduced to plain "інформацію".
- `colorway-removal-notice-message` — `toolkit/toolkit/about/aboutAddons.ftl` — Doubled preposition "на на" in the message text.
    - Current: `нові версії на         на сайті додатків.`
    - Source: `heading: Your colorway theme(s) were removed. message: { -brand-product-name } updated its colorways collection. We removed the old version(s) from your “Saved Themes” list. Get new versions on the add-ons site.`
    - Suggest: `нові версії на сайті додатків.`
    - The preposition "на" is repeated at the line break, producing "нові версії на на сайті додатків" in the rendered notice.
- `shortcuts-duplicate-warning-message2` — `toolkit/toolkit/about/aboutAddons.ftl` — Ungrammatical "використовується більше одного випадку".
    - Current: `використовується більше одного випадку`
    - Source: `message: { $shortcut } is being used as a shortcut in more than one case. Duplicate shortcuts may cause unexpected behavior.`
    - Suggest: `використовується більш ніж в одному випадку`
    - "більше одного випадку" after "використовується" lacks the required preposition/case; as written the sentence is not grammatical Ukrainian.
- `about-processes-web-process` — `toolkit/toolkit/about/aboutProcesses.ftl` — "веб процес" written as two words.
    - Current: `Спільний веб процес`
    - Source: `Shared Web Process ({ $pid })`
    - Suggest: `Спільний вебпроцес`
    - The prefix веб- is written solid in Ukrainian and consistently so across this tree (вебсайт, вебсокети, вебсумісність); the spaced form is a spelling error.
- `user-js-description` — `toolkit/toolkit/about/aboutSupport.ftl` — Leftover English word: "файл user.js file".
    - Current: `файл user.js file`
    - Source: `Your profile folder contains a <a data-l10n-name="user-js-link">user.js file</a>, which includes preferences that were not created by { -brand-short-name }.`
    - Suggest: `файл user.js`
    - The English noun "file" was left in after the Ukrainian "файл" was added, so the link text duplicates the word.
- `uses-tiling` — `toolkit/toolkit/about/aboutSupport.ftl` — "тайлинг" spelled with Russian-style "и" while the adjacent row uses "тайлінг".
    - Current: `Використовує тайлинг`
    - Source: `Uses Tiling`
    - Suggest: `Використовує тайлінг`
    - The very next entry (content-uses-tiling) spells it "тайлінг", which follows Ukrainian transliteration rules; "тайлинг" is a misspelling.
- `about-telemetry-page-title` — `toolkit/toolkit/about/aboutTelemetry.ftl` — Misspelling "Данні" instead of "Дані" in the page title.
    - Current: `Данні телеметрії`
    - Source: `Telemetry Data`
    - Suggest: `Дані телеметрії`
    - "Данні" is a misspelling; the correct Ukrainian plural is "дані", used everywhere else in the same file (e.g. "Поточні дані", "Загальні дані").
- `third-party-icon-warning` — `toolkit/toolkit/about/aboutThirdParty.ftl` — Wrong genitive form "модулю" instead of "модуля".
    - Current: `зазнав збій коду від цього модулю`
    - Source: `alt: { -brand-short-name } crashed in code from this module title: { -brand-short-name } crashed in code from this module`
    - Suggest: `зазнав збою в коді цього модуля`
    - "цього модулю" is an incorrect genitive (should be "модуля"), and "зазнав збій" requires the genitive "збою".
- `third-party-tag-shellex` — `toolkit/toolkit/about/aboutThirdParty.ftl` — Wrong genitive form "модулю" instead of "модуля".
    - Current: `Цей тип модулю завантажується`
    - Source: `(value): Shell Extension title: This type of module is loaded when you open the system file dialog.`
    - Suggest: `Цей тип модуля завантажується`
    - The genitive of "модуль" in this meaning is "модуля"; the rest of the file correctly uses "модуля"/"модуль".
- `about-webauthn-results-pin-invalid-error` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Verb agreement error in the [few] variant: singular "залишилася" with plural "спроби".
    - Current: `У вас залишилася { $retriesLeft } спроби.`
    - Source: `{$retriesLeft ->} [0] Error: Incorrect PIN. Try again. [one] Error: Incorrect PIN. Try again. You have one attempt left. [other] Error: Incorrect PIN. Try again. You have { $retriesLeft } attempts left.`
    - Suggest: `У вас залишилося { $retriesLeft } спроби.`
    - With numerals 2–4 plus the plural "спроби" the impersonal neuter form "залишилося" is required; "залишилася" is feminine singular and does not agree.
- `about-webauthn-samples-still-needed` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Agreement error in the [many] variant: "потрібні … зразків".
    - Current: `Все ще потрібні { $repeatCount } зразків.`
    - Source: `{$repeatCount ->} [one] { $repeatCount } sample still needed. [other] { $repeatCount } samples still needed.`
    - Suggest: `Все ще потрібно { $repeatCount } зразків.`
    - The genitive plural "зразків" requires the impersonal predicate "потрібно"; the plural adjective "потрібні" cannot govern a genitive.
- `about-webauthn-text-select-device` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Typo: "токер" instead of "токен" (security token).
    - Current: `Виберіть потрібний токер безпеки, торкнувшись пристрою.`
    - Source: `Please select your desired security token by touching the device.`
    - Suggest: `Виберіть потрібний токен безпеки, торкнувшись пристрою.`
    - "токер" is not a Ukrainian word; every other string in this file uses "токен безпеки".
- `about-webrtc-sdp-set-at-timestamp-local` — `toolkit/toolkit/about/aboutWebrtc.ftl` — Case agreement error: "для Локальний SDP".
    - Current: `Встановити для Локальний SDP відмітку часу`
    - Source: `Set Local SDP at timestamp { $timestamp }`
    - Suggest: `Встановлено для локального SDP відмітку часу`
    - The preposition "для" requires the genitive ("локального SDP"); the nominative phrase was inserted unchanged.
- `about-webrtc-sdp-set-at-timestamp-remote` — `toolkit/toolkit/about/aboutWebrtc.ftl` — Case agreement error: "для Віддалений SDP".
    - Current: `Встановити для Віддалений SDP відмітку часу`
    - Source: `Set Remote SDP at timestamp { $timestamp }`
    - Suggest: `Встановлено для віддаленого SDP відмітку часу`
    - "для" requires the genitive ("віддаленого SDP"); the nominative form was inserted unchanged.
- `contentanalysis-block-message` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — Wrong case after "запобігання" — inconsistent with the sibling warning string.
    - Current: `для запобігання втрати даних`
    - Source: `Your organization uses data-loss prevention software that has blocked this content: { $content }.`
    - Suggest: `для запобігання втраті даних`
    - "Запобігання" governs the dative, and contentanalysis-warndialogtext in the same file correctly uses "запобігання втраті даних" for the same en-US term "data-loss prevention".
- `user-context-color-cyan` — `toolkit/toolkit/global/contextual-identity.ftl` — Colour swatch labels mix masculine and feminine adjective forms.
    - Current: `Бірюзова`
    - Source: `label: Cyan`
    - Suggest: `Бірюзовий`
    - The rest of the swatch list is masculine (Блакитний, Зелений, Жовтий, Червоний…); only user-context-color-cyan ("Бірюзова"), user-context-color-violet ("Фіолетова") and user-context-color-gray ("Сіра") are feminine, so the three disagree with their neighbours in the same list.
- `prompt-to-launch-existing-app-message` — `toolkit/toolkit/global/run-from-dmg.ftl` — Imperative "Use the installed application" rendered as a future-tense statement.
    - Current: `Скористаєтеся встановленою програмою`
    - Source: `You already have { -brand-short-name } installed. Use the installed application to stay up to date and prevent data loss.`
    - Suggest: `Скористайтеся встановленою програмою`
    - "Скористаєтеся" is the 2nd-person future indicative ("you will use"); the source gives an instruction, which requires the imperative "Скористайтеся".
- `portrait` — `toolkit/toolkit/printing/printDialogs.ftl` — Page orientation "Portrait" spelled "Книжна".
    - Current: `Книжна`
    - Source: `accesskey: P label: Portrait`
    - Suggest: `Книжкова`
    - The standard Ukrainian term for portrait orientation is "книжкова", which is what printUI.ftl uses (printui-portrait-2). "Книжна" means bookish/literary. printpreview-portrait in printPreview.ftl has the same form.
- `webauthn-pin-invalid-long-prompt` — `toolkit/toolkit/webauthnDialog.ftl` — Ungrammatical clause makes the consequence of further wrong PINs unreadable.
    - Current: `до остаточної втратити доступу до облікових даних на цьому пристрої`
    - Source: `{$retriesLeft ->} [one] Incorrect PIN. You have { $retriesLeft } attempt left before you permanently lose access to the credentials on this device. [other] Incorrect PIN. You have { $retriesLeft } attempts left before y…`
    - Suggest: `перш ніж ви остаточно втратите доступ до облікових даних на цьому пристрої`
    - "до остаточної втратити доступу" mixes an adjective with an infinitive and a genitive object; the phrase does not parse in Ukrainian, so the warning that the credentials will be lost is not conveyed. All three plural variants carry the same broken clause.

### E. Typography, punctuation & spacing

- `login-list-name-reverse-option` — `browser/browser/aboutLogins.ftl` — The same en-US term "Name" is rendered two different ways in one sort dropdown, and the A-Z variant collides with "Username".
    - Current: `Назва (Я-А)`
    - Source: `Name (Z-A)`
    - Suggest: `Ім'я (Я-А)`
    - login-list-name-option uses "Ім'я (А-Я)" and login-list-name-reverse-option uses "Назва (Я-А)" for the same label in the same menu; additionally "Ім'я" duplicates the first word of "Ім'я користувача" (Username), so the two sort options are hard to distinguish. One rendering should be used for both.
- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — The window mode name "Classic" is rendered as "звичайних" instead of the established "класичне".
    - Current: `Навчатися з історії перегляду в звичайних і { -smart-window-brand-name }`
    - Source: `label: Learn from browsing in Classic and { -smart-window-brand-name }`
    - Suggest: `Навчатися з історії перегляду в класичних і { -smart-window-brand-name }`
    - "Classic Window" is a named mode rendered as "Класичне вікно" throughout aiWindow.ftl (appmenuitem-new-classic-window, ai-window-toggleview-switch-classic); using "звичайних" here breaks the link to that mode in the same settings surface.
- `main-context-menu-media-show-controls` — `browser/browser/browserContext.ftl` — "Controls" is rendered as the non-standard "керувальники" while the paired item uses "елементи керування".
    - Current: `Показати керувальники`
    - Source: `accesskey: C label: Show Controls`
    - Suggest: `Показати елементи керування`
    - main-context-menu-media-hide-controls uses "Сховати елементи керування" for the same term in the same mutually exclusive menu pair; "керувальники" is not the term used elsewhere in the tree.
- `link-preview-first-time-setup-message` — `browser/browser/genai.ftl` — "key points" is rendered as "ключові пункти" here but "ключові тези" everywhere else in the file.
    - Current: `Наступного разу ви побачите ключові пункти швидше.`
    - Source: `This may take a moment. You’ll see key points more quickly next time.`
    - Suggest: `Наступного разу ви побачите ключові тези швидше.`
    - link-preview-key-points-header, link-preview-setup-faster-next-time (the identical en-US sentence) and the other link-preview strings all use "ключові тези" for the same feature name.
- `safeb-blocked-phishing-page-error-desc-no-override` — `browser/browser/safebrowsing/blockedSite.ftl` — Stray space at the end of the link text produces a visible space before the sentence-final period.
    - Current: `повідомити про невідповідність цієї інформації </a>.`
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as a deceptive site</a>. You can <a data-l10n-name='report_detection'>report a detection problem</a>.`
    - Suggest: `повідомити про невідповідність цієї інформації</a>.`
    - The space sits inside the rendered link label, so the user sees "…цієї інформації ." with a gap before the full stop; the parallel string safeb-blocked-phishing-page-error-desc-override has no such space.
- `webrtc-stop-sharing-button` — `browser/browser/webrtcIndicator.ftl` — Button label ends with a full stop.
    - Current: `Припинити спільний доступ.`
    - Source: `Stop Sharing`
    - Suggest: `Припинити спільний доступ`
    - The en-US button label has no terminal punctuation, and no other button label in this file carries one.
- `accessibility.badge.textLabel` — `devtools/client/accessibility.properties` — “text label” on the badge uses “ярлик” while the matching filter and tooltips use “мітка”.
    - Current: `accessibility.badge.textLabel = текстовий ярлик`
    - Source: `text label`
    - Suggest: `accessibility.badge.textLabel = текстова мітка`
    - In the same panel accessibility.filter.textLabel is “Текстові мітки” and accessibility-text-label-header is “Текстові мітки та імена”; “ярлик” (shortcut/tag) is a different term for the same check.
- `heapview.noAllocationStacks` — `devtools/client/memory.properties` — “call stacks” is rendered as “алокації стеків” here but “стеки викликів” elsewhere, and the instruction becomes a noun phrase.
    - Current: `heapview.noAllocationStacks = Не знайдено алокації стеків. Запис алокації стеків перед створенням знімку купи.`
    - Source: `No call stacks found. Record call stacks before taking a snapshot.`
    - Suggest: `heapview.noAllocationStacks = Стеків викликів не знайдено. Записуйте стеки викликів перед створенням знімку купи.`
    - checkbox.recordAllocationStacks in the same panel uses “стеки викликів”; “алокації стеків” inverts the term and the second sentence loses the imperative instruction.
- `responsive.changeDevicePixelRatio` — `devtools/client/responsive.properties` — “device pixel ratio” is rendered as “resolution”, unlike the DPR field label in the same panel.
    - Current: `responsive.changeDevicePixelRatio = Змінити роздільну здатність точки огляду пристрою`
    - Source: `Change device pixel ratio of the viewport`
    - Suggest: `responsive.changeDevicePixelRatio = Змінити піксельне співвідношення (DPR) точки огляду`
    - responsive.deviceAdderPixelRatio2 in the same tool uses “Піксельне співвідношення пристрою (DPR)”; DPR is not resolution, so the dropdown tooltip names a different setting than the field it controls.
- `options-context-inspector` — `devtools/client/toolbox-options.ftl` — The Inspector panel is called “Ревізор” here, while the whole tree calls it “Інспектор”.
    - Current: `options-context-inspector = Ревізор`
    - Source: `Inspector`
    - Suggest: `options-context-inspector = Інспектор`
    - startup.properties (inspector.label), inspector.properties and the Settings tooltips all use “Інспектор”; “Ревізор” (auditor) names no panel the user can find.
- `evaluationNotifcation.noOriginalVariableMapping.msg` — `devtools/shared/webconsole.properties` — The quoted checkbox name does not match the actual checkbox label in the Scopes panel.
    - Current: `встановіть прапорець "Показати вихідні змінні" на панелі областей налагоджувача`
    - Source: ``Original variables name mapping in the debugger is disabled. Evaluation results might not be accurate. Click the `Show original variables` checkbox in the debugger scopes panel to enable.``
    - Suggest: `встановіть прапорець "Показати оригінальні змінні" на панелі областей налагоджувача`
    - The comment says `Show original variables` must be kept in sync with the Scopes panel checkbox, which is translated as “Показати оригінальні змінні” (debugger.properties scopes.showOriginalScopes); users are told to look for a control that does not exist under that name.
- `preventedConsoleClear` — `devtools/shared/webconsole.properties` — The quoted setting name is left in English while the setting itself is translated.
    - Current: `preventedConsoleClear = console.clear() було заблоковано через “Persist Logs”`
    - Source: `console.clear() was prevented due to “Persist Logs”`
    - Suggest: `preventedConsoleClear = console.clear() було заблоковано через “Постійне журналювання”`
    - The comment says this must stay in sync with webconsole.console.settings.menu.item.enablePersistentLogs.label, which is translated as “Постійне журналювання”, so the user cannot match the quoted name to any menu item.
- `shortcuts-remove-button` — `toolkit/toolkit/about/aboutAddons.ftl` — Keyboard shortcut called "ярлик" (desktop shortcut icon) instead of "комбінація клавіш".
    - Current: `Видалити ярлик`
    - Source: `aria-label: Remove shortcut`
    - Suggest: `Видалити комбінацію клавіш`
    - Every other string in this surface renders "shortcut" as "комбінація клавіш" (shortcuts-input, shortcuts-duplicate, shortcuts-system); "ярлик" means a file/desktop shortcut and is wrong here.
- `about-glean-feedback-settings-and-ping` — `toolkit/toolkit/about/aboutGlean.ftl` — "ping" rendered as "сигнал" here while the rest of the page uses "пінг".
    - Current: `Налаштування застосовано та сигнал відправлено!`
    - Source: `message: Settings applied and ping sent!`
    - Suggest: `Налаштування застосовано та пінг надіслано!`
    - Across about:glean the term is consistently "пінг" (e.g. about-glean-no-ping-label, about-glean-ping-list-optgroup-built-in); "сигнал" names a different thing in the same surface.
- `app-basics-update-dir` — `toolkit/toolkit/about/aboutSupport.ftl` — Folder/Directory platform variants are swapped relative to en-US.
    - Current: `[linux] Тека оновлення`
    - Source: `{$sel_1 ->} [linux] Update Directory [other] Update Folder`
    - Suggest: `[linux] Каталог оновлення`
    - en-US has Directory on Linux and Folder elsewhere; the locale uses "тека" for Folder and "каталог" for Directory (see show-dir-label), so the two variants are reversed here.
- `certificate-viewer-inc-country` — `toolkit/toolkit/about/certviewer.ftl` — "Inc. Country" rendered identically to plain "Country", erasing the distinction.
    - Current: `Країна`
    - Source: `Inc. Country`
    - Suggest: `Країна реєстрації компанії`
    - The comment explains Inc. means Incorporated; certificate-viewer-country already uses "Країна", so the two different rows become indistinguishable, unlike certificate-viewer-inc-locality which is differentiated.
- `pdf-features-notification-message` — `toolkit/toolkit/about/pdfFeaturesNotification.ftl` — This string uses the typographic apostrophe, but the locale's convention is the straight apostrophe.
    - Current: `об’єднання`
    - Source: `Split, merge, and more. <a data-l10n-name="features-link">See PDF features</a>`
    - Suggest: `об'єднання`
    - The uk tree uses the straight apostrophe as its convention (717 straight vs 126 typographic).

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/uk/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

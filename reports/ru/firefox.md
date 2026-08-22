# Firefox l10n QA — ru

| | |
|---|---|
| **Generated** | 2026-08-22 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `9441127ed8c4` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `60f24d17564f` |
| **Previous run** | 2026-08-21 @ `bd0ff4b2f741` |
| **Mode** | incremental |
| **Strings reviewed this run** | 8 of 18,169 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for ru: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (2)

- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — Superfluous comma before the coordinating conjunction «или» in a two-part enumeration.
    - Current: `</label>, <label data-l10n-name="helpus-getInvolvedLink">присоединяйтесь!</label>`
    - Source: `Want to help? <label data-l10n-name="helpus-donateLink">Make a donation</label>, <label data-l10n-name="helpus-shareFirefoxLink">share { -brand-product-name }</label>, or <label data-l10n-name="helpus-getInvolvedLink">g…`
    - Suggest: `</label> <label data-l10n-name="helpus-getInvolvedLink">присоединяйтесь!</label>`
    - In Russian a comma is not placed before a single «или» joining homogeneous members; the en-US comma before "or" reflects English punctuation rules only. The comma should move: «Сделайте пожертвование, поделитесь … или присоединяйтесь!»
- `appmenu-referrals2` — `browser/browser/appmenu.ftl` — Menu label uses «Поделитесь { -brand-product-name }» without the required instrumental case, so the brand name is left in the wrong grammatical form.
    - Current: `Поделитесь { -brand-product-name }`
    - Source: `accesskey: r label: Share { -brand-product-name }`
    - Suggest: `Поделитесь { -brand-product-name(case: "ablative") }`
    - The verb «поделиться» governs the instrumental case («поделиться Firefox'ом» / «поделиться браузером»); the brand term supports a $case parameter per the locale conventions, and omitting it produces an ungrammatical nominative form.

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
| Files | 360 |
| Strings | 18,169 |
| Missing strings | 11 |
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
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 144 |
| Markup & `data-l10n-name` defects | 3 |
| Typography deviations from this locale's own norm | 6 |

### Completeness

**11 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 7
- `browser/browser/sharePanel.ftl` — 2
- `browser/browser/preferences/formAutofill.ftl` — 1
- `dom/chrome/accessibility/AccessFu.properties` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `guillemet` 1174, `straight-double` 28, `curly-double` 8, `curly-single` 7 | **guillemet** |
| apostrophe | `typographic` 11, `straight` 16 | _mixed_ |
| ellipsis | `char` 463, `ascii` 6 | **char** |
| dash | `em` 168, `en` 5 | **em** |
| nbsp | `total` 5, `before-punctuation` 2, `space-before-punctuation` 7 | _mixed_ |
| register | `informal` 1051, `formal` 3593 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **accesskey — 144 strings** — 144 strings. The locale kept en-US access keys rather than remapping them to its own labels. Remapping is a single decision for the locale team; it is not tracked as individual defects.
    - Affected: `addon-install-or-update-from-file`, `addressbar-locbar-engines-option-1`, `addressbar-locbar-showrecentsearches-option-2`, `appmenu-theme-installed`, `appmenu-update-available2`, `appmenu-update-manual2`, `autofill-addresses-checkbox`, `autofill-addresses-checkbox-message`, `autofill-addresses-manage-addresses-button`, `autofill-payment-methods-checkbox-submessage`, `autofill-payment-methods-manage-payments-button`, `autofill-reauth-payment-methods-checkbox` …and 132 more

---

## 3. Open findings (595)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 50 |
| 2 | Wrong content (says something other than the English) | 266 |
| 3 | Degraded language (grammar, spelling, terminology) | 214 |
| 4 | Cosmetic (typography, spacing) | 65 |

### A. Functional, markup, variables & plurals

- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — Malformed closing tag `</span >` in `about-logins-import-dialog-items-no-change2`
    - Current: `{$count ->} [one] <span>Обнаружена повторяющаяся запись:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(не импортирована)</span > [few] <span>Обнаружены повторяющиеся записи:</span> <…`
    - Source: `{$count ->} [other] <span>Duplicate entries found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
    - Suggest: `{$count ->} [other] <span>Duplicate entries found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
    - Whitespace inside a closing tag makes it render as literal text.
- `urlbar-input-dismiss-autofill` — `browser/browser/browser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: i label: Dismiss this suggestion`
- `urlbar-input-remove-from-history` — `browser/browser/browser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: e label: Remove from history`
- `urlbar-view-context-menu-open-in-container-tab` — `browser/browser/browser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: i label: Open in New Container Tab`
- `urlbar-view-context-menu-open-in-tab` — `browser/browser/browser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: w label: Open in New Tab`
- `main-context-menu-link-send-to-mobile` — `browser/browser/browserContext.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: n label: Send Link to Mobile`
- `main-context-menu-send-to-mobile-2` — `browser/browser/browserContext.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: n label: Send to Mobile`
- `fxviewtabrow-send-to-mobile` — `browser/browser/fxviewTabList.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `(value): Send to Mobile accesskey: n`
- `genai-menu-ask-generic-2` — `browser/browser/genai.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: z label: Ask AI Chatbot`
- `genai-menu-ask-provider-2` — `browser/browser/genai.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: z label: Ask { $provider }`
- `genai-menu-ask-smart-window` — `browser/browser/genai.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: z label: Ask…`
- `genai-menu-no-provider-2` — `browser/browser/genai.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: z label: Ask an AI Chatbot`
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Malformed closing tag `</a >` in `genai-settings-chat-gemini-links`
    - Current: `Выбирая Google Gemini, вы соглашаетесь с <a data-l10n-name="link1">Условиями использования Google</a>, <a data-l10n-name="link2">Политикой запрещённого использования генеративного ИИ</a > и <a data-l10n-name="link3">Уве…`
    - Source: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
    - Suggest: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
    - Whitespace inside a closing tag makes it render as literal text.
- `newtab-sports-widget-group-a` — `browser/browser/newtab/newtab.ftl` — Cyrillic А while groups B–L all use Latin letters
    - Source: `Group A`
- `newtab-widget-lists-completed-list` — `browser/browser/newtab/newtab.ftl` — the parentheses of the en-US format are dropped, leaving a bare number
    - Source: `Completed ({ $number })`
- `mr2-onboarding-thank-you-text` — `browser/browser/newtab/onboarding.ftl` — the dash is U+4E00, the CJK ideograph for "one", not an em dash
    - Source: `{ -brand-short-name } is an independent browser backed by a non-profit. Together, we’re making the web safer, healthier, and more private.`
- `mr2022-onboarding-live-language-switch-to` — `browser/browser/newtab/onboarding.ftl` — onboarding-live-language-button-label-downloading, onboarding-live-language-installing, mr2022-onboarding-live-language-switch-to — onboarding.ftl — stray square brackets around { $negotiatedLanguage } that are not in en-US (mr2022-onboarding-live-language-continue-in has none)
    - Source: `Switch to { $negotiatedLanguage }`
- `onboarding-live-language-button-label-downloading` — `browser/browser/newtab/onboarding.ftl` — onboarding-live-language-button-label-downloading, onboarding-live-language-installing, mr2022-onboarding-live-language-switch-to — onboarding.ftl — stray square brackets around { $negotiatedLanguage } that are not in en-US (mr2022-onboarding-live-language-continue-in has none)
    - Source: `Downloading the language pack for { $negotiatedLanguage }…`
- `onboarding-live-language-installing` — `browser/browser/newtab/onboarding.ftl` — onboarding-live-language-button-label-downloading, onboarding-live-language-installing, mr2022-onboarding-live-language-switch-to — onboarding.ftl — stray square brackets around { $negotiatedLanguage } that are not in en-US (mr2022-onboarding-live-language-continue-in has none)
    - Source: `Installing the language pack for { $negotiatedLanguage }…`
- `data-collection-backlogged-crash-reports` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: c description: This helps { -vendor-short-name } diagnose and fix issues with the browser. Reports may include personal or sensitive data. label: Automatically send crash reports`
- `history-shutdown-exceptions` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: x label: Manage Exceptions`
- `network-proxy-connection-settings2` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: p description: Changing these settings may cause connections issues label: Configure proxy`
- `preferences-doh-manage-exceptions2` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: x label: Manage exceptions`
- `preferences-fonts-size` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: s label: Font size`
- `privacy-panel-breach-alerts` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: s label: Show breach messages`
- `sitedata-cookies-exceptions3` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: x description: Choose how specific sites handle cookies and site data. label: Manage exceptions`
- `sitedata-delete-on-close2` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: c label: Clear cookies and site data every time you close { -brand-short-name }`
- `sitedata-settings3` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: s label: Clear data for specific sites`
- `update-application-suppress-prompts-2` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: n label: Show fewer update reminders`
- `windows-launch-on-login-open-new-tab` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: n label: Also open a new tab`
- `tab-context-close-duplicate-tabs2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: x label: Close Duplicates of This Tab`
- `tab-context-move-split-view` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: v label: Move Split View to`
- `tab-context-move-tabs2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: v label: {$tabCount ->} [1] Move Tab to [other] Move { $tabCount } Tabs to`
- `tab-context-open-in-new-container-tab2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: e label: Open in a New Container Tab`
- `tab-context-send-to-device2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: n label: Send to Your Devices`
- `tab-context-send-to-mobile` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: n label: {$tabCount ->} [1] Send to Mobile [other] Send { $tabCount } Tabs to Mobile`
- `tab-context-share-selected-tabs` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: a label: Create Shareable Link`
- `tab-context-unpin-tab2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: p label: Unpin`
- `tab-context-reverse-split-view` — `browser/browser/tabbrowser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: r label: Reverse Tabs`
- `tabbrowser-context-unmute-tab2` — `browser/browser/tabbrowser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `accesskey: m label: Unmute`
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — Malformed closing tag `</a >` in `tou-existing-user-spotlight-body`
    - Current: `Мы ввели <a data-l10n-name="terms-of-use">Условия использования</a> и обновили наше <a data-l10n-name="privacy-notice">Уведомление о конфиденциальности</a >.<br><br> Пожалуйста, потратьте немного времени, чтобы ознакоми…`
    - Source: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
    - Suggest: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
    - Whitespace inside a closing tag makes it render as literal text.
- `unified-extensions-mb-blocklist-warning-multiple` — `browser/browser/unifiedExtensions.ftl` — the entire first sentence is missing ("Some of your extensions have been disabled for violating Mozilla's policies")
    - Source: `heading: {$extensionsCount ->} [other] { $extensionsCount } extensions disabled message: Some of your extensions have been disabled for violating Mozilla’s policies. You can enable them in settings, but this may be risk…`
    - Suggest: `.message`
- `about-glean-about-data-list-item-dictionary` — `toolkit/toolkit/about/aboutGlean.ftl` — the link text is just { -glean-brand-name }, dropping "Dictionary", so the link no longer names its target
    - Source: `To browse the list of data collected by { -glean-brand-name } per application, please consult the <a data-l10n-name="glean-dictionary-link">{ -glean-brand-name } Dictionary</a>.`
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — the second clause has no predicate at all ("…а по умолчанию для всех остальных метрик пинг metrics"), plus a stray trailing space
    - Source: `Select from the preceding list the ping your instrumentation is in. If it’s in a <a data-l10n-name="custom-ping-link">custom ping</a>, choose that one. Otherwise, the default for <code>event</code> metrics is the <code>…`
- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — guillemets wrapped around <q>…</q>, which renders its own quotes → double-quoted text
    - Source: `To see a full view of all recorded metrics, you can use the { -profiler-brand-name }. First you must <a data-l10n-name="firefox-profiler-link">capture a performance profile</a>. Once you capture the profile, select <q>M…`
    - Suggest: `double-quoted text`
- `about-telemetry-no-search-results` — `toolkit/toolkit/about/aboutTelemetry.ftl` — square brackets around { $sectionName } where en-US and the sibling about-telemetry-no-data-to-display use guillemets
    - Current: `{ $sectionName }`
    - Source: `Sorry! There are no results in { $sectionName } for “{ $currentSearchText }”`
- `popup-notification-default-button` — `toolkit/toolkit/global/popupnotification.ftl` — the OK button is Cyrillic ОК (U+041E U+041A)
    - Source: `accesskey: O label: OK!`
    - Suggest: `.label`
- `tabmodalprompt-ok-button` — `toolkit/toolkit/global/tabprompts.ftl` — same Cyrillic ОК
    - Source: `label: OK`
    - Suggest: `.label`
- `webauthn-allow` — `toolkit/toolkit/webauthnDialog.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `(value): Allow accesskey: A`
- `webauthn-block` — `toolkit/toolkit/webauthnDialog.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
    - Source: `(value): Block accesskey: B`

### B. Mistranslation, reversed meaning, wrong names & brand

- `pocket-panel-signup-cta-a-fix` — `browser/browser/aboutPocket.ftl` — Current: Ваша кнопка сохранения из Интернета → Suggest: …для Интернета
    - Current: `Ваша кнопка сохранения из Интернета`
    - Source: `Your save button for the internet`
    - Suggest: `…для Интернета`
- `about-private-browsing-focus-promo-cta` — `browser/browser/aboutPrivateBrowsing.ftl` — a button label as a noun. Current: Скачивание { -focus-brand-name } → Suggest: Скачать { -focus-brand-name }
    - Current: `Скачивание { -focus-brand-name }`
    - Source: `Download { -focus-brand-name }`
    - Suggest: `Скачать { -focus-brand-name }`
- `about-unloads-learn-more` — `browser/browser/aboutUnloads.ftl` — about-unloads-page-title, about-unloads-intro, about-unloads-learn-more — aboutUnloads.ftl — the feature unloads tabs in general. Current: Выгрузка вкладки → Suggest: Выгрузка вкладок
    - Current: `Выгрузка вкладки`
    - Source: `See <a data-l10n-name="doc-link">Tab Unloading</a> to learn more about the feature and this page.`
    - Suggest: `Выгрузка вкладок`
- `about-unloads-page-title` — `browser/browser/aboutUnloads.ftl` — about-unloads-page-title, about-unloads-intro, about-unloads-learn-more — aboutUnloads.ftl — the feature unloads tabs in general. Current: Выгрузка вкладки → Suggest: Выгрузка вкладок
    - Current: `Выгрузка вкладки`
    - Source: `Tab Unloading`
    - Suggest: `Выгрузка вкладок`
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — the comment requires the quoted "Learn from…" text to match the two settings labels; the ru quotes «Узнать из…», which matches neither
    - Source: `Existing memories will be deleted. If you don’t want any new memories created, uncheck the options to “Learn from…” in { -smart-window-brand-name } settings.`
- `ai-window-memories-section` — `browser/browser/aiFeatures.ftl` — en-US "can learn from your activity". Current: { -brand-short-name } может учиться на своей работе (learn from its own work) → Suggest: …может учиться на основе вашей активности
    - Current: `{ -brand-short-name } может учиться на своей работе`
    - Source: `description: { -brand-short-name } can learn from your activity to create memories. They’re used to help personalize responses and are stored locally on this device. label: Memories`
    - Suggest: `…может учиться на основе вашей активности`
- `aiwindow-starter-writing-improve` — `browser/browser/aiWindow.ftl` — Current: Улучши правописание (spelling) → Suggest: Улучши текст
    - Current: `Улучши правописание`
    - Source: `Improve writing`
    - Suggest: `Улучши текст`
- `action-log-read-page` — `browser/browser/aiWindowContent.ftl` — the dev comment says "Read is past tense, to indicate that the action has been completed", but the value uses the same aspect as the in-progress action-log-reading-page. Current: Чтение содержимого страницы → Suggest: Содержимое страницы прочитано
    - Current: `Чтение содержимого страницы`
    - Source: `Read page content`
    - Suggest: `Содержимое страницы прочитано`
- `action-log-searching-history` — `browser/browser/aiWindowContent.ftl` — aiWindowContent.ftl and appmenu-search-history (.label) — appmenu.ftl — en-US "Searching history" / "Search history". Current (both): Журнал поиска (= search log) → Suggest: Поиск в журнале
    - Current: `Журнал поиска`
    - Source: `Searching history`
    - Suggest: `Поиск в журнале`
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — smartwindow-nl-retry-message, smartwindow-nl-retry-group-tabs-message — aiWindowContent.ftl — the UI "card" became "карта" (map). Suggest: карточке
    - Source: `If you still want to group tabs, choose <strong>Retry</strong> and select which ones in the card that opens.`
- `smartwindow-nl-retry-message` — `browser/browser/aiWindowContent.ftl` — smartwindow-nl-retry-message, smartwindow-nl-retry-group-tabs-message — aiWindowContent.ftl — the UI "card" became "карта" (map). Suggest: карточке
    - Source: `If you still want to close tabs, choose <strong>Retry</strong> and make your selection in the card that opens.`
- `appmenu-help-and-report-header` — `browser/browser/appmenu.ftl` — appmenu.ftl — the "Report" half is dropped. Current: Помощь и поддержка → Suggest: Справка и жалобы
    - Current: `Помощь и поддержка`
    - Source: `title: Help and Report`
    - Suggest: `Справка и жалобы`
- `appmenu-referrals2` — `browser/browser/appmenu.ftl` — Menu label uses «Поделитесь { -brand-product-name }» without the required instrumental case, so the brand name is left in the wrong grammatical form.
    - Current: `Поделитесь { -brand-product-name }`
    - Source: `accesskey: r label: Share { -brand-product-name }`
    - Suggest: `Поделитесь { -brand-product-name(case: "ablative") }`
    - The verb «поделиться» governs the instrumental case («поделиться Firefox'ом» / «поделиться браузером»); the brand term supports a $case parameter per the locale conventions, and omitting it produces an ungrammatical nominative form.
- `appmenuitem-help-and-report` — `browser/browser/appmenu.ftl` — appmenu.ftl — the "Report" half is dropped. Current: Помощь и поддержка → Suggest: Справка и жалобы
    - Current: `Помощь и поддержка`
    - Source: `label: Help and Report`
    - Suggest: `Справка и жалобы`
- `default-browser-notification-privacy-body-text` — `browser/browser/backgroundtasks/defaultagent.ftl` — en-US "Your default changed" is singular. Current: Ваши браузеры по умолчанию изменены. → Suggest: Ваш браузер по умолчанию изменён.
    - Current: `Ваши браузеры по умолчанию изменены.`
    - Source: `Your default changed. Come back to { -brand-short-name } for built-in privacy and protection.`
    - Suggest: `Ваш браузер по умолчанию изменён.`
- `backup-service-error-recovery-failed` — `browser/browser/backupSettings.ftl` — it is the user's data that couldn't be restored, not Firefox. Current heading: Не удалось восстановить { -brand-short-name } → Suggest: { -brand-short-name } не смог выполнить восстановление, and in the message …попробуйте восстановить данные из резервной копии снова
    - Current: `Не удалось восстановить { -brand-short-name }`
    - Source: `heading: { -brand-short-name } couldn’t restore message: Restart { -brand-short-name } and try restoring your backup again.`
    - Suggest: `{ -brand-short-name } не смог выполнить восстановление`
- `press-tab-label` — `browser/browser/browser.ftl` — "tab" here is the Tab key. Current: Нажмите вкладку для выбора: → Suggest: Нажмите Tab для выбора: (cf. urlbar-result-action-before-tabtosearch-web)
    - Current: `Нажмите вкладку для выбора:`
    - Source: `Press tab to select:`
    - Suggest: `Нажмите Tab для выбора:`
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — Current: Поисковые действия → Suggest: Поиск по действиям (matching the sibling aria-labels)
    - Current: `Поисковые действия`
    - Source: `aria-label: Search actions placeholder: Enter search terms`
    - Suggest: `Поиск по действиям`
- `main-context-menu-bidi-switch-text` — `browser/browser/browserContext.ftl` — translated identically to main-context-menu-bidi-switch-page, losing the text/page distinction. Same defect in menu-edit-bidi-switch-text-direction (menubar.ftl). Suggest: Переключить направление текста
    - Source: `accesskey: w label: Switch Text Direction`
    - Suggest: `.label`
- `main-context-menu-save-link` — `browser/browser/browserContext.ftl` — en-US "Save Link As…". Current: Сохранить объект как… → Suggest: Сохранить ссылку как…
    - Current: `Сохранить объект как…`
    - Source: `accesskey: k label: Save Link As…`
    - Suggest: `Сохранить ссылку как…`
- `main-context-menu-visual-search-2` — `browser/browser/browserContext.ftl` — the action searches using the image. Current: Поиск изображений с помощью { $engine } → Suggest: Найти это изображение с помощью { $engine }
    - Current: `Поиск изображений с помощью { $engine }`
    - Source: `accesskey: e label: Search Image with { $engine }`
    - Suggest: `Найти это изображение с помощью { $engine }`
- `window-zoom-command` — `browser/browser/browserSets.ftl` — the macOS Window-menu "Zoom" maximizes the window. Current: Изменить масштаб → Suggest: Масштабировать окно
    - Current: `Изменить масштаб`
    - Source: `label: Zoom`
    - Suggest: `Масштабировать окно`
- `clear-data-for-site-cookies` — `browser/browser/clearDataForSite.ftl` — as written the cookies are what sign you out. Suggest: Куки и данные сайтов — их удаление может привести к выходу из аккаунта на сайте
    - Source: `Cookies and site data, which may sign you out of the site`
- `content-sharing-modal-description-signed-in` — `browser/browser/contentSharing.ftl` — Current: Мы сделали страницу со ссылками лёгкой для передачи. → Suggest: Мы создали страницу с вашими ссылками, которой легко поделиться.
    - Current: `Мы сделали страницу со ссылками лёгкой для передачи.`
    - Source: `We made an easy to share page with your links. It can’t be edited or deleted and expires after 7 days.`
    - Suggest: `Мы создали страницу с вашими ссылками, которой легко поделиться.`
- `customize-mode-uidensity` — `browser/browser/customizeMode.ftl` — en-US "Density". Current: Значки (= Icons) → Suggest: Плотность (customize-mode-uidensity-link already uses "плотности окон")
    - Current: `Значки`
    - Source: `label: Density`
    - Suggest: `Плотность`
- `customkeys-search-input` — `browser/browser/customkeys.ftl` — customkeys-search-input (.aria-label, .placeholder) — customkeys.ftl — en-US "Search shortcuts" (dev comment: "Search is a verb"). Current: Значки поисковых систем — "search engine icons", apparently copy-pasted from search-popover in touchbar.ftl; it has nothing to do with the string → Suggest: Поиск сочетаний клавиш
    - Source: `aria-label: Search shortcuts placeholder: Search shortcuts`
    - Suggest: `Поиск сочетаний клавиш`
- `firefox-relay-opt-in-confirmation-enable-button` — `browser/browser/firefoxRelay.ftl` — en-US "Use email mask" (a button). Current: Используйте псевдонимы электронной почты → Suggest: Использовать псевдоним эл. почты; note firefox-relay-offer-legal-notice quotes this button as «Использовать псевдоним электронной почты», so the two currently disagree
    - Current: `Используйте псевдонимы электронной почты`
    - Source: `accesskey: U label: Use email mask`
    - Suggest: `Использовать псевдоним эл. почты`
- `firefoxview-search-text-box-clear-button` — `browser/browser/firefoxView.ftl` — en-US "Clear". Current: Удалить → Suggest: Очистить
    - Current: `Удалить`
    - Source: `title: Clear`
    - Suggest: `Очистить`
- `firefoxview-syncedtabs-adddevice-header-3` — `browser/browser/firefoxView.ftl` — en-US "Your tabs called." is a playful idiom. Current: Ваши вкладки вызваны. reads as "your tabs have been summoned" → Suggest something idiomatic, e.g. Ваши вкладки на связи. Они на вашем телефоне.
    - Current: `Ваши вкладки вызваны.`
    - Source: `Your tabs called. They’re on your phone.`
    - Suggest: `Ваши вкладки на связи. Они на вашем телефоне.`
- `firefoxview-tabpickup-header` — `browser/browser/firefoxView.ftl` — "Tab pickup" is about resuming tabs from other devices. Current: Выбор вкладки → Suggest: Вкладки с других устройств
    - Current: `Выбор вкладки`
    - Source: `Tab pickup`
    - Suggest: `Вкладки с других устройств`
- `genai-chatbot-summarize-sidebar-generic-subtitle` — `browser/browser/genai.ftl` — the "sparkles button". Current: по кнопке с блестками → Suggest: с блёстками (and see §3.H for the missing ё)
    - Current: `по кнопке с блестками`
    - Source: `Right-click the sparkles button in the sidebar and choose “Summarize Page”. The first time, you’ll also choose an AI chatbot.`
    - Suggest: `с блёстками`
- `genai-onboarding-select-description` — `browser/browser/genai.ftl` — en-US "you can also write in your own prompts" = type your own. Current: Вы также можете писать в своих собственных запросах. → Suggest: Вы также можете вводить свои собственные запросы.
    - Current: `Вы также можете писать в своих собственных запросах.`
    - Source: `When you select text, we’ll suggest prompts you can send to the chatbot. You can also write in your own prompts.`
    - Suggest: `Вы также можете вводить свои собственные запросы.`
- `genai-settings-chat-lechat-links-2` — `browser/browser/genai.ftl` — en-US attributes the documents to "Mistral AI"; the ru drops the vendor (the older -lechat-links keeps it)
    - Source: `By choosing Mistral Vibe, you agree to the Mistral AI <a data-l10n-name="link1">Terms of Service</a> and <a data-l10n-name="link2">Privacy Policy</a>.`
- `link-preview-first-time-setup-message` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
    - Source: `This may take a moment. You’ll see key points more quickly next time.`
    - Suggest: `ключевые моменты`
- `link-preview-generation-error-missing-data-v2` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
    - Source: `{ -brand-short-name } can’t generate key points for this webpage.`
    - Suggest: `ключевые моменты`
- `link-preview-key-points-disclaimer` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
    - Source: `Key points are AI-generated and may have mistakes.`
    - Suggest: `ключевые моменты`
- `link-preview-key-points-header` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
    - Source: `Key points`
    - Suggest: `ключевые моменты`
- `link-preview-optin-message` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
    - Source: `{ -brand-short-name } uses AI to read the beginning of the page and generate a few key points. To prioritize your privacy, this happens on your device.`
    - Suggest: `ключевые моменты`
- `link-preview-settings-key-points` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
    - Source: `label: Allow AI to read the beginning of the page and generate key points`
    - Suggest: `ключевые моменты`
- `link-preview-setup-faster-next-time` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
    - Source: `You’ll see key points more quickly next time.`
    - Suggest: `ключевые моменты`
- `ip-protection-bandwidth-warning-infobar-message-75` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
    - Source: `<strong>Getting close to your VPN limit.</strong> You have { $usageLeft } GB left. Your data will reset at the start of next month.`
    - Suggest: `Лимиты встроенного VPN…`
- `ipprotection-feature-introduction-link-text-captive-portal-1` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
    - Source: `Get <a data-l10n-name="learn-more-vpn">extra privacy</a> by choosing from several locations to hide where you browse.`
    - Suggest: `Лимиты встроенного VPN…`
- `ipprotection-feature-introduction-link-text-privacy-2` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
    - Source: `<a data-l10n-name="learn-more-vpn">{ -brand-product-name }’s built-in VPN</a> helps protect your browsing. Choose from multiple locations to keep where you browse more private.`
    - Suggest: `Лимиты встроенного VPN…`
- `ipprotection-location-selection-callout-description-1` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
    - Source: `<a data-l10n-name="learn-more-vpn">{ -brand-product-name }’s built-in VPN</a> lets you choose from several browsing locations, or let us pick the fastest one for you.`
    - Suggest: `Лимиты встроенного VPN…`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
    - Source: `heading: Getting close to your VPN limit message: You have { $usageLeft } GB of { $maxUsage } GB left this month.`
    - Suggest: `Лимиты встроенного VPN…`
- `ipprotection-message-continuous-onboarding-site-settings` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
    - Source: `{ -brand-short-name } will remember which websites you’ve set to use VPN. Update these in <a data-l10n-name="setting-link">settings</a> anytime.`
    - Suggest: `Лимиты встроенного VPN…`
- `ipprotection-summer-promo-offramp-generic-title` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
    - Source: `Your built-in VPN limits reset September 1`
    - Suggest: `Лимиты встроенного VPN…`
- `menu-bookmarks-all-tabs` — `browser/browser/menubar.ftl` — the target of the action is dropped. Current: Добавить все вкладки… → Suggest: Добавить все вкладки в закладки…
    - Current: `Добавить все вкладки…`
    - Source: `label: Bookmark All Tabs…`
    - Suggest: `Добавить все вкладки в закладки…`
- `import-from-chrome-beta` — `browser/browser/migration.ftl` — import-from-chrome-beta (.label) — migration.ftl and migration-wizard-migrator-display-name-chrome-beta — migrationWizard.ftl — Current: Chrome Бета while "Microsoft Edge Beta" and "Chrome Dev" stay intact in the same lists
    - Source: `accesskey: B label: Chrome Beta`
    - Suggest: `.label`
- `annotations-default-pdf-handler-body` — `browser/browser/newtab/asrouter.ftl` — dev comment: "'Go-to' … refers to something that is used often". Current: популярные подписи → Suggest: часто используемые подписи
    - Current: `популярные подписи`
    - Source: `Draw, type, or upload your signature, then place it exactly where you want. Save your go-to signatures for next time.`
    - Suggest: `часто используемые подписи`
- `cfr-protections-panel-body` — `browser/browser/newtab/asrouter.ftl` — en-US "many of the most common". Current: большинства наиболее известных трекеров overstates the claim → Suggest: многих наиболее распространённых трекеров
    - Current: `большинства наиболее известных трекеров`
    - Source: `Keep your data to yourself. { -brand-short-name } protects you from many of the most common trackers that follow what you do online.`
    - Suggest: `многих наиболее распространённых трекеров`
- `relay-50-masks-announcement-title` — `browser/browser/newtab/asrouter.ftl` — dev comment: "'on us' … means 'for free'". Current: 50 псевдонимов электронной почты на нас is a literal calque with no such meaning → Suggest: …— бесплатно
    - Current: `50 псевдонимов электронной почты на нас`
    - Source: `50 email masks, on us`
    - Suggest: `…— бесплатно`
- `windows-10-eos-challenger-callout-title` — `browser/browser/newtab/asrouter.ftl` — en-US "That's the point." Current: В этом ключ. (not an idiomatic Russian phrase) → Suggest: В этом и суть.
    - Current: `В этом ключ.`
    - Source: `{ -brand-product-name } isn’t preloaded like other Big Tech browsers. That’s the point.`
    - Suggest: `В этом и суть.`
- `windows-10-eos-feature-toast-subtitle` — `browser/browser/newtab/asrouter.ftl` — Current: По популярным запросам, → Suggest: По многочисленным просьбам (and drop the comma)
    - Current: `По популярным запросам,`
    - Source: `By popular request, { -brand-product-name } just dropped new features to keep your browsing streamlined and focused.`
    - Suggest: `По многочисленным просьбам`
- `newtab-clock-city-id-makassar` — `browser/browser/newtab/newtab.ftl` — Current: Макасар → Suggest: Макассар
    - Current: `Макасар`
    - Source: `Makassar`
    - Suggest: `Макассар`
- `newtab-privacy-modal-paragraph-2` — `browser/browser/newtab/newtab.ftl` — en-US "dishing up captivating stories" = serving/showing. Current: Помимо сохранения увлекательных статей → Suggest: Помимо публикации увлекательных статей
    - Current: `Помимо сохранения увлекательных статей`
    - Source: `In addition to dishing up captivating stories, we also show you relevant, highly-vetted content from select sponsors. Rest assured, <strong>your browsing data never leaves your personal copy of { -brand-product-name }</…`
    - Suggest: `Помимо публикации увлекательных статей`
- `newtab-sports-widget-match-full-time` — `browser/browser/newtab/newtab.ftl` — newtab.ftl sports/stocks widget: newtab-sports-widget-view-matches and newtab-sports-widget-loading-more translate football "matches" as search "совпадения"; newtab-sports-widget-watch-stream-select-games-only reads "Select" as an imperative when the comment shows it is an adjective; newtab-sports-widget-match-full-time = Полное время is not a football term (→ Основное время / Матч окончен); newt…
    - Current: `Полное время`
    - Source: `Full time`
    - Suggest: `Основное время`
- `newtab-sports-widget-team-name-label-civ` — `browser/browser/newtab/newtab.ftl` — ASCII apostrophe in Кот-д'Ивуар
    - Source: `label: Ivory Coast`
    - Suggest: `.label`
- `newtab-wallpaper-blue-flowers` — `browser/browser/newtab/newtab.ftl` — Wallpaper descriptions — newtab.ftl — newtab-wallpaper-light-landscape renders "mist" as дым (smoke); newtab-wallpaper-blue-flowers says цветов с голубыми цветами (repeats the word, loses "petaled"); newtab-wallpaper-celestial-eclipse-time-lapse renders "time lapse" as Хронометраж; newtab-wallpaper-celestial-river renders "satellite" as Космический
    - Source: `Closeup photography of blue-petaled flowers in bloom`
- `newtab-wallpaper-celestial-eclipse-time-lapse` — `browser/browser/newtab/newtab.ftl` — Wallpaper descriptions — newtab.ftl — newtab-wallpaper-light-landscape renders "mist" as дым (smoke); newtab-wallpaper-blue-flowers says цветов с голубыми цветами (repeats the word, loses "petaled"); newtab-wallpaper-celestial-eclipse-time-lapse renders "time lapse" as Хронометраж; newtab-wallpaper-celestial-river renders "satellite" as Космический
    - Source: `Lunar eclipse time lapse`
- _…and 204 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `helpus-referrals` — `browser/browser/aboutDialog.ftl` — Spurious comma: before a single или in elevation-more-elevated, pleaseSelect, policy-Bookmarks, safeb-blocked-phishing-page-error-desc-override, helpus-referrals, aiwindow-firstrun-memories-subtitle; before и in mr2022-onboarding-mobile-download-subtitle, newtab-wallpaper-feature-highlight-subtitle, details-notification-hard-blocked-other; after a leading prepositional phrase in abuse-report-sett…
    - Current: `или`
    - Source: `Want to help? <label data-l10n-name="helpus-donateLink">Make a donation</label>, <label data-l10n-name="helpus-shareFirefoxLink">Share { -brand-short-name }</label>, or <label data-l10n-name="helpus-getInvolvedLink">get…`
- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — about-logins-confirm-remove-all-sync-dialog-message3 (all 4 variants) — всех отображаемых здесь предупреждениях о взломе → предупреждений
    - Current: `всех отображаемых здесь предупреждениях о взломе`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices. This will also remove any breach alerts that appear here. You cannot undo this action. [other] This will remove al…`
    - Suggest: `предупреждений`
- `about-logins-copy-password-os-auth-dialog-message-win` — `browser/browser/aboutLogins.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
    - Source: `To copy your password, enter your Windows login credentials. This helps protect the security of your accounts.`
    - Suggest: `-location-desc`
- `about-logins-import-dialog-items-no-change` — `browser/browser/aboutLogins.ftl` — about-logins-import-dialog-items-no-change ([few], [many]) — Найдены повторяющие логины → повторяющиеся логины
    - Current: `Найдены повторяющие логины`
    - Source: `{$count ->} [other] <span>Duplicate logins found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
    - Suggest: `повторяющиеся логины`
- `about-logins-import-report-modified2` — `browser/browser/aboutLogins.ftl` — about-logins-import-report-modified2 ([many]) — существующих записей обновлены → обновлено
    - Current: `существующих записей обновлены`
    - Source: `{$count ->} [other] <div data-l10n-name="count">{ $count }</div> <div data-l10n-name="details">Existing entries updated</div>`
    - Suggest: `обновлено`
- `active-policies-tab` — `browser/browser/aboutPolicies.ftl` — aboutPolicies.ftl — a predicative short form used as a nav label: Активны → Активные
    - Current: `Активны`
    - Source: `Active`
    - Suggest: `Активные`
- `active-policies-tab-title` — `browser/browser/aboutPolicies.ftl` — aboutPolicies.ftl — a predicative short form used as a nav label: Активны → Активные
    - Current: `Активны`
    - Source: `title: Active`
    - Suggest: `Активные`
- `about-private-browsing-cookie-banners-promo-body` — `browser/browser/aboutPrivateBrowsing.ftl` — от многих уведомлениях о куки → от многих уведомлений о куках
    - Current: `от многих уведомлениях о куки`
    - Source: `We now automatically refuse many cookie banners so you can get tracked less and go back to distraction-free browsing.`
    - Suggest: `от многих уведомлений о куках`
- `ai-window-no-memories-learning-off` — `browser/browser/aiFeatures.ftl` — Обучение через активности отключены → Обучение на основе активности отключено
    - Current: `Обучение через активности отключены`
    - Source: `description: Learning from activity is off, so { -smart-window-brand-name } isn’t creating memories. label: No memories to show`
    - Suggest: `Обучение на основе активности отключено`
- `smart-window-block-description-chats` — `browser/browser/aiFeatures.ftl` — smartwindow-nl-retry-message, restore-from-backup-profiles-disabled-message, smart-window-block-description-chats — see §3.H for the ё issues in these
    - Source: `This will delete your { -smart-window-brand-name } chats.`
- `aiwindow-ai-chat-grid-grid-view` — `browser/browser/aiWindow.ftl` — aiwindow-ai-chat-grid-grid-view (.aria-label) — Переключение режим → Переключение режима
    - Current: `Переключение режим`
    - Source: `aria-label: Switch mode: Grid View tooltiptext: Grid View`
    - Suggest: `Переключение режима`
- `aiwindow-firstrun-memories-subtitle` — `browser/browser/aiWindow.ftl` — Spurious comma: before a single или in elevation-more-elevated, pleaseSelect, policy-Bookmarks, safeb-blocked-phishing-page-error-desc-override, helpus-referrals, aiwindow-firstrun-memories-subtitle; before и in mr2022-onboarding-mobile-download-subtitle, newtab-wallpaper-feature-highlight-subtitle, details-notification-hard-blocked-other; after a leading prepositional phrase in abuse-report-sett…
    - Current: `или`
    - Source: `{ -smart-window-brand-name } can learn from your chats, browsing, or both to create memories. They make answers more helpful over time.`
- `action-log-checking-world-cup-live` — `browser/browser/aiWindowContent.ftl` — прямых трансляции → прямых трансляций
    - Current: `прямых трансляции`
    - Source: `Checking live World Cup matches`
    - Suggest: `прямых трансляций`
- `smart-window-closed-tabs-summary` — `browser/browser/aiWindowContent.ftl` — smart-window-closed-tabs-summary ([one]) — aiWindowContent.ftl — Вкладка закрыты → Вкладка закрыта
    - Current: `Вкладка закрыты`
    - Source: `{$count ->} [one] Done! Tab closed. [other] Done! Tabs closed.`
    - Suggest: `Вкладка закрыта`
- `smart-window-restore-success-summary` — `browser/browser/aiWindowContent.ftl` — smart-window-restore-success-summary ([one]) — Вкладки закрыта → Вкладка закрыта
    - Current: `Вкладки закрыта`
    - Source: `{$count ->} [one] Tab closed, then restored. [other] Tabs closed, then restored.`
    - Suggest: `Вкладка закрыта`
- `smartwindow-nl-retry-message` — `browser/browser/aiWindowContent.ftl` — smartwindow-nl-retry-message, restore-from-backup-profiles-disabled-message, smart-window-block-description-chats — see §3.H for the ё issues in these
    - Source: `If you still want to close tabs, choose <strong>Retry</strong> and make your selection in the card that opens.`
- `restore-from-backup-profiles-disabled-message` — `browser/browser/backupSettings.ftl` — smartwindow-nl-retry-message, restore-from-backup-profiles-disabled-message, smart-window-block-description-chats — see §3.H for the ё issues in these
    - Source: `This will replace all your current { -brand-short-name } data with your backup.`
- `trustpanel-insecure-description` — `browser/browser/browser.ftl` — the pronoun does not agree with данные. Current: Его можно просмотреть → Suggest: Их можно просмотреть
    - Current: `Его можно просмотреть`
    - Source: `The data you’re sending to this site isn’t encrypted. It could be viewed, stolen, or altered.`
    - Suggest: `Их можно просмотреть`
- `trustpanel-tracking-cookies-not-blocking-tab-header` — `browser/browser/browser.ftl` — trustpanel-tracking-cookies-not-blocking-tab-header ([one]) — { $count } межсайтовых отслеживающих куки → { $count } межсайтовый отслеживающий куки
    - Current: `{ $count } межсайтовых отслеживающих куки`
    - Source: `{$count ->} [one] { -brand-product-name } allowed { $count } cross-site tracking cookie [other] { -brand-product-name } allowed { $count } cross-site tracking cookies`
    - Suggest: `{ $count } межсайтовый отслеживающий куки`
- `urlbar-result-explanation-last-visited-weeks-2` — `browser/browser/browser.ftl` — urlbar-result-explanation-last-visited-weeks-2 ([one]) — { $weeksAgo } неделя назад → неделю назад (the v1 string is correct)
    - Current: `{ $weeksAgo } неделя назад`
    - Source: `{$weeksAgo ->} [one] Last visited { $weeksAgo } week ago [other] Last visited { $weeksAgo } weeks ago`
    - Suggest: `неделю назад`
- `requested-crash-reports-message-new` — `browser/browser/contentCrash.ftl` — requested-crash-reports-message-new ([many]) — contentCrash.ftl — { $reportCount } неотправленных отчёта → отчётов (the [few] variant is correct)
    - Current: `{ $reportCount } неотправленных отчёта`
    - Source: `{$reportCount ->} [one] You have an unsent crash report related to crashes being investigated, sending it will help us improve { -brand-product-name }. Closing this notification will ignore this report. [other] You have…`
    - Suggest: `отчётов`
- `contextual-manager-passwords-copy-password-os-auth-dialog-message-win` — `browser/browser/contextual-manager.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
    - Source: `To copy your password, enter your Windows login credentials. This helps protect the security of your accounts.`
    - Suggest: `-location-desc`
- `contextual-manager-passwords-remove-all-message` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-remove-all-message ([few], [many]) — При этом будет удалены пароли → будут удалены
    - Current: `При этом будет удалены пароли`
    - Source: `{$total ->} [1] This will remove your password saved to { -brand-short-name } and any breach alerts. You cannot undo this action. [other] This will remove the passwords saved to { -brand-short-name } and any breach aler…`
    - Suggest: `будут удалены`
- `contextual-manager-passwords-remove-all-message-sync` — `browser/browser/contextual-manager.ftl` — о утечках → об утечках
    - Current: `о утечках`
    - Source: `{$total ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices and remove any breach alerts. You cannot undo this action. [other] This will remove all passwords saved to { -brand…`
    - Suggest: `об утечках`
- `contextual-manager-view-alert-button` — `browser/browser/contextual-manager.ftl` — contextual-manager-view-alert-button (.tooltiptext) — garbled and reversed: Уведомление об проверке → Просмотреть уведомление
    - Current: `Уведомление об проверке`
    - Source: `tooltiptext: Review alert`
    - Suggest: `Просмотреть уведомление`
- `sidebar-callout-survey-keep-website-open` — `browser/browser/featureCallout.ftl` — открытыми → открытым
    - Current: `открытыми`
    - Source: `Keep a website, like email or calendar, open in the sidebar as you browse`
    - Suggest: `открытым`
- `ip-protection-bandwidth-help-text` — `browser/browser/ipProtection.ftl` — Сбрасывается на { $maxUsage } ГБ → до { $maxUsage } ГБ
    - Current: `Сбрасывается на { $maxUsage } ГБ`
    - Source: `Resets to { $maxUsage } GB on the first of every month.`
    - Suggest: `до { $maxUsage } ГБ`
- `ip-protection-vpn-upgrade-link-1` — `browser/browser/ipProtection.ftl` — ipprotection-locations-subview-promo (.message) and ip-protection-vpn-upgrade-link-1 (.description) — ipProtection.ftl — the ungrammatical на до 5 устройствах → Suggest: не более чем на 5 устройствах
    - Current: `на до 5 устройствах`
    - Source: `description: Choose from 300+ locations and protect all your apps on up to 5 devices. label: Take protection further with { -mozilla-vpn-brand-name }`
    - Suggest: `не более чем на 5 устройствах`
- `ipprotection-bandwidth-reset-title` — `browser/browser/ipProtection.ftl` — the subject is the GB of data. Current: { $maxUsage } ГБ VPN, обновлён → Suggest: обновлены
    - Current: `{ $maxUsage } ГБ VPN, обновлён`
    - Source: `{ $maxUsage } GB of VPN, refreshed and ready to go`
    - Suggest: `обновлены`
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — ipprotection-locations-subview-promo (.message) and ip-protection-vpn-upgrade-link-1 (.description) — ipProtection.ftl — the ungrammatical на до 5 устройствах → Suggest: не более чем на 5 устройствах
    - Current: `на до 5 устройствах`
    - Source: `heading: Take protection further with { -mozilla-vpn-brand-name } message: Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `не более чем на 5 устройствах`
- `ipprotection-summer-promo-offramp-default-browser-incentive-description` — `browser/browser/ipProtection.ftl` — метоположений → местоположений
    - Current: `метоположений`
    - Source: `Make { -brand-product-name } your go-to browser and get more than 20 extra places to browse from after August 31.`
    - Suggest: `местоположений`
- `menu-application-referrals` — `browser/browser/menubar.ftl` — menu-application-set-as-default (.label), menu-application-referrals (.label), menu-referrals (.label) — menubar.ftl — 2nd-person imperatives in menu labels where every other label uses the infinitive
    - Source: `label: Share { -brand-shorter-name }`
    - Suggest: `.label`
- `menu-application-set-as-default` — `browser/browser/menubar.ftl` — menu-application-set-as-default (.label), menu-application-referrals (.label), menu-referrals (.label) — menubar.ftl — 2nd-person imperatives in menu labels where every other label uses the infinitive
    - Source: `label: Set { -brand-shorter-name } as Default Browser`
    - Suggest: `.label`
- `menu-referrals` — `browser/browser/menubar.ftl` — menu-application-set-as-default (.label), menu-application-referrals (.label), menu-referrals (.label) — menubar.ftl — 2nd-person imperatives in menu labels where every other label uses the infinitive
    - Source: `label: Share { -brand-shorter-name }`
    - Suggest: `.label`
- `cfr-doorhanger-milestone-heading2` — `browser/browser/newtab/asrouter.ftl` — cfr-doorhanger-milestone-heading2 (all three variants) — asrouter.ftl — the exclamation mark now falls mid-sentence, after the date, because the clause order was inverted.
    - Source: `{$blockedCount ->} [other] { -brand-short-name } blocked over <b>{ $blockedCount }</b> trackers since { $date }!`
- `cookie-banner-blocker-onboarding-header` — `browser/browser/newtab/asrouter.ftl` — asrouter.ftl — уведомление о куки → о куках; меньше куки → меньше кук
    - Current: `уведомление о куки`
    - Source: `{ -brand-short-name } just refused a cookie banner for you`
    - Suggest: `о куках`
- `firefoxview-spotlight-promo-subtitle` — `browser/browser/newtab/asrouter.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
    - Source: `Want that open tab on your phone? Grab it. Need that site you just visited? Poof, it’s back with { -firefoxview-brand-name }.`
    - Suggest: `-location-desc`
- `newtab-activation-window-message-values-focus-message` — `browser/browser/newtab/newtab.ftl` — the second half is a dangling fragment with no predicate
    - Source: `{ -brand-product-name } lets you browse the way you like, with a more personal way to start your day online. Make { -brand-product-name } your own.`
- `newtab-error-fallback-info` — `browser/browser/newtab/newtab.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
    - Source: `Oops, something went wrong loading this content.`
    - Suggest: `-location-desc`
- `newtab-picture-set-wallpaper` — `browser/browser/newtab/newtab.ftl` — newtab.ftl — a noun for an action button: Установка обоев → Установить обои (its own .aria-label already uses the verb)
    - Current: `Установка обоев`
    - Source: `aria-label: Set today’s picture as your wallpaper label: Set wallpaper title: Set wallpaper`
    - Suggest: `Установить обои`
- `newtab-privacy-message-first-protection` — `browser/browser/newtab/newtab.ftl` — продолжать requires an infinitive: будет продолжать блокировки → блокировать
    - Current: `будет продолжать блокировки`
    - Source: `Keep browsing, { -brand-short-name } will keep blocking.`
    - Suggest: `блокировать`
- `newtab-privacy-message-info-6` — `browser/browser/newtab/newtab.ftl` — это does not agree with данные, and en-US's factual "might" became a conditional
    - Current: `это`
    - Source: `Keep your data with { -brand-short-name }. We never sell it, but other browsers might.`
    - Suggest: `данные`
- `newtab-report-ads-reason-seen-it-too-many-times` — `browser/browser/newtab/newtab.ftl` — tense: Я вижу это слишком много раз → Я видел это слишком много раз
    - Current: `Я вижу это слишком много раз`
    - Source: `label: I’ve seen it too many times`
    - Suggest: `Я видел это слишком много раз`
- `newtab-section-mangage-topics-followed-topics-empty-state` — `browser/browser/newtab/newtab.ftl` — genitive-under-negation, and see §3.J for the follow terminology
    - Source: `You have not followed any topics yet.`
- `create-backup-screen-1-flair` — `browser/browser/newtab/onboarding.ftl` — a badge on a single tile: Рекомендуемые → Рекомендуется
    - Current: `Рекомендуемые`
    - Source: `Recommended`
    - Suggest: `Рекомендуется`
- `mr2022-onboarding-mobile-download-subtitle` — `browser/browser/newtab/onboarding.ftl` — Spurious comma: before a single или in elevation-more-elevated, pleaseSelect, policy-Bookmarks, safeb-blocked-phishing-page-error-desc-override, helpus-referrals, aiwindow-firstrun-memories-subtitle; before и in mr2022-onboarding-mobile-download-subtitle, newtab-wallpaper-feature-highlight-subtitle, details-notification-hard-blocked-other; after a leading prepositional phrase in abuse-report-sett…
    - Current: `или`
    - Source: `Grab tabs from one device and pick up where you left off on another. Plus sync your bookmarks and passwords anywhere you use { -brand-product-name }.`
- `origin-controls-option-all-domains` — `browser/browser/originControls.ftl` — origin-controls-option-all-domains (.label), origin-controls-state-no-access, origin-controls-state-always-on — originControls.ftl — en-US "site(s)" rendered as страницах, while origin-controls-state-quarantined and the toolbar tooltip in the same file correctly use сайт
    - Source: `label: On All Sites`
    - Suggest: `.label`
- `origin-controls-state-always-on` — `browser/browser/originControls.ftl` — origin-controls-option-all-domains (.label), origin-controls-state-no-access, origin-controls-state-always-on — originControls.ftl — en-US "site(s)" rendered as страницах, while origin-controls-state-quarantined and the toolbar tooltip in the same file correctly use сайт
    - Source: `Can always read and change data on this site`
    - Suggest: `.label`
- `origin-controls-state-no-access` — `browser/browser/originControls.ftl` — origin-controls-option-all-domains (.label), origin-controls-state-no-access, origin-controls-state-always-on — originControls.ftl — en-US "site(s)" rendered as страницах, while origin-controls-state-quarantined and the toolbar tooltip in the same file correctly use сайт
    - Source: `Can’t read and change data on this site`
    - Suggest: `.label`
- `policy-Bookmarks` — `browser/browser/policies/policies-descriptions.ftl` — Spurious comma: before a single или in elevation-more-elevated, pleaseSelect, policy-Bookmarks, safeb-blocked-phishing-page-error-desc-override, helpus-referrals, aiwindow-firstrun-memories-subtitle; before и in mr2022-onboarding-mobile-download-subtitle, newtab-wallpaper-feature-highlight-subtitle, details-notification-hard-blocked-other; after a leading prepositional phrase in abuse-report-sett…
    - Current: `или`
    - Source: `Create bookmarks in the Bookmarks toolbar, Bookmarks menu, or a specified folder inside them.`
- `permissions-site-notification-desc` — `browser/browser/preferences/permissions.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
    - Source: `The following websites have requested to send you notifications. You can specify which websites are allowed to send you notifications. You can also block new requests asking to allow notifications.`
    - Suggest: `-location-desc`
- `containers-card-header2` — `browser/browser/preferences/preferences.ftl` — таим образом → таким образом
    - Current: `таим образом`
    - Source: `description: Separate cookies by container so you can use different accounts on the same site and limit cross-site tracking. label: Containers`
    - Suggest: `таким образом`
- `cookie-banner-blocker-checkbox-label` — `browser/browser/preferences/preferences.ftl` — cookie-banner-blocker-checkbox-label (.label) and cookie-banner-blocker-header — preferences.ftl — prepositional instead of genitive after от, wrong number, and куки left undeclined
    - Source: `label: Automatically refuse cookie banners`
    - Suggest: `.label`
- `cookie-banner-blocker-header` — `browser/browser/preferences/preferences.ftl` — cookie-banner-blocker-checkbox-label (.label) and cookie-banner-blocker-header — preferences.ftl — prepositional instead of genitive after от, wrong number, and куки left undeclined
    - Source: `Cookie Banner Blocker`
    - Suggest: `.label`
- `open-external-link-next-to-active-tab` — `browser/browser/preferences/preferences.ftl` — open-external-link-next-to-active-tab (.label), settings-tabs-drag-to-create-tab-groups (.label) — preferences.ftl — imperatives where every other checkbox label uses the infinitive
    - Source: `label: Open links from apps next to your active tab`
    - Suggest: `.label`
- `privacy-panel-breach-alerts` — `browser/browser/preferences/preferences.ftl` — a persistent checkbox needs the imperfective: Показать → Показывать
    - Current: `Показать`
    - Source: `accesskey: s label: Show breach messages`
    - Suggest: `Показывать`
- `security-privacy-issue-warning-ech2` — `browser/browser/preferences/preferences.ftl` — скрыть, как сайты вы собираетесь посетить → какие сайты вы собираетесь посетить (also missing the final period that en-US and the parallel -doh2 have)
    - Current: `скрыть, как сайты вы собираетесь посетить`
    - Source: `description: Encrypted Client Hello helps hide what sites you’re about to visit from your network provider. label: Encrypted Client Hello is disabled`
    - Suggest: `какие сайты вы собираетесь посетить`
- `settings-tabs-drag-to-create-tab-groups` — `browser/browser/preferences/preferences.ftl` — open-external-link-next-to-active-tab (.label), settings-tabs-drag-to-create-tab-groups (.label) — preferences.ftl — imperatives where every other checkbox label uses the infinitive
    - Source: `label: Drag tabs together to create tab groups`
    - Suggest: `.label`
- `avatar-selector-custom-tab` — `browser/browser/profiles.ftl` — a dangling feminine adjective for "Custom" next to Значок: Персональная → Свой
    - Current: `Персональная`
    - Source: `Custom`
    - Suggest: `Свой`
- `briefcase-avatar-tooltip` — `browser/browser/profiles.ftl` — с портфелей → с портфелем
    - Current: `с портфелей`
    - Source: `tooltiptext: Apply briefcase avatar`
    - Suggest: `с портфелем`
- _…and 92 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — `backup-file-moz-browser-restore-step-2-1` quotes “Восстановить ваши данные” but the string it names, `restore-from-backup-header`, reads “Восстановите свои данные”
    - Current: `Нажмите «Восстановить ваши данные» и выберите этот файл`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Восстановите свои данные`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — `backup-file-other-browser-restore-step-3-1` quotes “Восстановить ваши данные” but the string it names, `restore-from-backup-header`, reads “Восстановите свои данные”
    - Current: `Нажмите «Восстановить ваши данные» и выберите этот файл`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Восстановите свои данные`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `firefox-relay-offer-legal-notice` — `browser/browser/browser.ftl` — firefox-relay-offer-legal-notice Примечанием о конфиденциальности vs Уведомлением… in -notice-1 right below
    - Source: `By clicking “Use email mask”, you agree to the <label data-l10n-name="tos-url">Terms of Service</label> and <label data-l10n-name="privacy-url">Privacy Notice</label>.`
    - Suggest: `Примечанием о конфиденциальности`
- `quickactions-cmd-clearrecenthistory2` — `browser/browser/browser.ftl` — 3. кеш (46) vs кэш — the locale's choice is кеш; the one straggler is sitedata-heading (.description). (quickactions-cmd-clearrecenthistory2 listing both is intentional.)
    - Current: `кеш`
    - Source: `cookies, clear cookies, cache, clear cache, browsing data, clear browsing data, history, clear recent history`
    - Suggest: `кэш`
- `trustpanel-clear-cookies-description` — `browser/browser/browser.ftl` — trustpanel-clear-cookies-description and item-cookies-site-data-description use the slang разлогин where clearDataForSite.ftl uses выход из аккаунта
    - Source: `Removing cookies and site data might log you out of websites and clear shopping carts.`
- `contextual-manager-passwords-import-success-message-2` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-import-success-message-2 Новое: vs Добавлено: in -import-success-message
    - Source: `New: { $added }, Updated: { $modified }, Duplicates: { $no_change }, Errors: { $error }`
    - Suggest: `Новое:`
- `customkeys-conflict-confirm-title` — `browser/browser/customkeys.ftl` — 9. ярлык for keyboard shortcuts — customkeys.ftl (customkeys-shortcut-unassigned, customkeys-shortcut-input, customkeys-conflict-confirm-title, customkeys-reset-all-confirm-body) and shortcuts-remove-button, where the rest uses сочетание клавиш. Worse, customkeys-conflict-confirm-body, -unusable-title, -unusable-body use ключ (a cryptographic key) for a keyboard key.
    - Current: `ярлык`
    - Source: `Remove another shortcut?`
- `customkeys-reset-all-confirm-body` — `browser/browser/customkeys.ftl` — 9. ярлык for keyboard shortcuts — customkeys.ftl (customkeys-shortcut-unassigned, customkeys-shortcut-input, customkeys-conflict-confirm-title, customkeys-reset-all-confirm-body) and shortcuts-remove-button, where the rest uses сочетание клавиш. Worse, customkeys-conflict-confirm-body, -unusable-title, -unusable-body use ключ (a cryptographic key) for a keyboard key.
    - Current: `ярлык`
    - Source: `Any custom keyboard shortcuts you’ve created will be removed.`
- `customkeys-shortcut-input` — `browser/browser/customkeys.ftl` — 9. ярлык for keyboard shortcuts — customkeys.ftl (customkeys-shortcut-unassigned, customkeys-shortcut-input, customkeys-conflict-confirm-title, customkeys-reset-all-confirm-body) and shortcuts-remove-button, where the rest uses сочетание клавиш. Worse, customkeys-conflict-confirm-body, -unusable-title, -unusable-body use ключ (a cryptographic key) for a keyboard key.
    - Current: `ярлык`
    - Source: `Shortcut for: { $keyLabel }`
- `customkeys-shortcut-unassigned` — `browser/browser/customkeys.ftl` — 9. ярлык for keyboard shortcuts — customkeys.ftl (customkeys-shortcut-unassigned, customkeys-shortcut-input, customkeys-conflict-confirm-title, customkeys-reset-all-confirm-body) and shortcuts-remove-button, where the rest uses сочетание клавиш. Worse, customkeys-conflict-confirm-body, -unusable-title, -unusable-body use ключ (a cryptographic key) for a keyboard key.
    - Current: `ярлык`
    - Source: `placeholder: Add shortcut`
- `ipprotecion-locations-subview-recommended-label` — `browser/browser/ipProtection.ftl` — ipprotection-location-country-button Местонахождение vs Местоположение; ipprotecion-locations-subview-recommended-label Рекомендуемые (plural) vs Рекомендуемое
    - Source: `Recommended`
    - Suggest: `Местонахождение`
- `ipprotection-location-country-button` — `browser/browser/ipProtection.ftl` — ipprotection-location-country-button Местонахождение vs Местоположение; ipprotecion-locations-subview-recommended-label Рекомендуемые (plural) vs Рекомендуемое
    - Source: `Location: { $country }`
    - Suggest: `Местонахождение`
- `set-default-menu-message-row-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — set-default-menu-message-row-layout-subtitle uses конфиденциальность where the scope uses приватность
    - Source: `Get speed, safety and privacy every time you browse.`
    - Suggest: `конфиденциальность`
- `newtab-privacy-message-milestone-year` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-milestone-year (all variants) — same
    - Source: `{$count ->} [one] { $count } tracker blocked this year. That’s a powerful year of protecting your privacy. [other] { $count } trackers blocked this year. That’s a powerful year of protecting your privacy.`
- `newtab-section-mangage-topics-followed-topics-empty-state` — `browser/browser/newtab/newtab.ftl` — newtab-section-toast-follow/-unfollow and newtab-section-mangage-topics-followed-topics-empty-state use читаете/отслеживаете while every button and aria-label uses подписаться/отписаться, per the dev comment
    - Source: `You have not followed any topics yet.`
    - Suggest: `-unfollow`
- `newtab-section-toast-follow` — `browser/browser/newtab/newtab.ftl` — newtab-section-toast-follow/-unfollow and newtab-section-mangage-topics-followed-topics-empty-state use читаете/отслеживаете while every button and aria-label uses подписаться/отписаться, per the dev comment
    - Source: `message: You’re now following { $topic }.`
    - Suggest: `-unfollow`
- `create-backup-screen-2-easy-list-1` — `browser/browser/newtab/onboarding.ftl` — fx-backup-confirmation-screen-easy-setup-item-text-1 журнал vs create-backup-screen-2-easy-list-1 история
    - Source: `Bookmarks, history, settings, and more`
    - Suggest: `журнал`
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — sync-to-mobile-button-label vs desktop-to-mobile-subtitle — the subtitle instructs the user to select a label that doesn't match the actual button
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
- `fx-backup-confirmation-screen-easy-setup-item-text-1` — `browser/browser/newtab/onboarding.ftl` — fx-backup-confirmation-screen-easy-setup-item-text-1 журнал vs create-backup-screen-2-easy-list-1 история
    - Source: `Bookmarks, history, settings, and other data included`
    - Suggest: `журнал`
- `sync-to-mobile-button-label` — `browser/browser/newtab/onboarding.ftl` — sync-to-mobile-button-label vs desktop-to-mobile-subtitle — the subtitle instructs the user to select a label that doesn't match the actual button
    - Source: `Sync to mobile`
- `policy-CNSA2KeyAgreementEnabled` — `browser/browser/policies/policies-descriptions.ftl` — policy-CNSA2KeyAgreementEnabled соглашение о ключе (a legal agreement) vs согласование ключей in policy-PostQuantumKeyAgreementEnabled
    - Source: `Enable the CNSA 2.0 ML-KEM-1024 key agreement for TLS.`
    - Suggest: `соглашение о ключе`
- `policy-PostQuantumKeyAgreementEnabled` — `browser/browser/policies/policies-descriptions.ftl` — policy-CNSA2KeyAgreementEnabled соглашение о ключе (a legal agreement) vs согласование ключей in policy-PostQuantumKeyAgreementEnabled
    - Source: `Enable post-quantum key agreement for TLS.`
    - Suggest: `соглашение о ключе`
- `search-filtering-for-add-engine` — `browser/browser/preferences/preferences.ftl` — "поисковик" (colloquial) in search-filtering-for-add-engine vs поисковая система everywhere else
    - Source: `Add Engine`
    - Suggest: `поисковая система`
- `item-cookies-site-data-description` — `browser/browser/sanitize.ftl` — trustpanel-clear-cookies-description and item-cookies-site-data-description use the slang разлогин where clearDataForSite.ftl uses выход из аккаунта
    - Source: `May sign you out of sites or empty shopping carts`
- `screenshot-toolbar-button` — `browser/browser/screenshots.ftl` — 8. скриншот vs снимок экрана — mixed inside devtools/shared/screenshot.properties (6 vs 3 entries) and between screenshots.ftl's screenshot-toolbarbutton and screenshot-toolbar-button.
    - Current: `скриншот`
    - Source: `label: Screenshot tooltiptext: Take a screenshot ({ $shortcut })`
    - Suggest: `снимок экрана`
- `fxa-menu-sign-in-promo-heading` — `browser/browser/sync.ftl` — "Sync": Синхронизацию capitalized vs lowercase, inside syncSetup.properties (2 strings) and between fxa-menu-sign-in-promo-heading and sync-setup-verify-heading
    - Current: `Синхронизацию`
    - Source: `Sign in to sync`
- `sync-setup-verify-heading` — `browser/browser/sync.ftl` — "Sync": Синхронизацию capitalized vs lowercase, inside syncSetup.properties (2 strings) and between fxa-menu-sign-in-promo-heading and sync-setup-verify-heading
    - Current: `Синхронизацию`
    - Source: `Are you sure you want to sign in to sync?`
- `editor_ink_opacity` — `browser/pdfviewer/viewer.properties` — 10. Прозрачность for opacity — colorpicker-tooltip-alpha-slider-title and editorinkopacity (see §3.B).
    - Current: `Прозрачность`
    - Source: `Opacity`
- `changes.contextmenu.copyDeclaration` — `devtools/client/changes.properties` — styleinspector.contextmenu.copyDeclaration and changes.contextmenu.copyDeclaration use декларацию where rule.jumpDeclaration.title uses объявление
    - Source: `Copy Declaration`
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “Остановить на…” but the string it names, `watchpoints.submenu`, reads “Приостанавливаться на…”
    - Current: `Щёлкните правой кнопкой мыши по элементу в Инспекторе и выберите «Остановить на…», чтобы добавить точку останова`
    - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
    - Suggest: `Приостанавливаться на…`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `skipPausingTooltip.label` — `devtools/client/debugger.properties` — skipPausingTooltip.label / undoSkipPausingTooltip.label collapse the global Deactivate/Activate toggle onto the same strings as the per-breakpoint Disable/Enable commands, making them indistinguishable
    - Source: `Deactivate breakpoints`
- `undoSkipPausingTooltip.label` — `devtools/client/debugger.properties` — skipPausingTooltip.label / undoSkipPausingTooltip.label collapse the global Deactivate/Activate toggle onto the same strings as the per-breakpoint Disable/Enable commands, making them indistinguishable
    - Source: `Activate breakpoints`
- `colorpicker-tooltip-alpha-slider-title` — `devtools/client/inspector.ftl` — 10. Прозрачность for opacity — colorpicker-tooltip-alpha-slider-title and editorinkopacity (see §3.B).
    - Current: `Прозрачность`
    - Source: `Opacity`
- `eventsTooltip.Bubbling` — `devtools/client/inspector.properties` — storage-tree-labels-session-storage-class and eventsTooltip.Capturing vs eventsTooltip.Bubbling (participle vs noun)
    - Source: `Bubbling`
- `eventsTooltip.Capturing` — `devtools/client/inspector.properties` — storage-tree-labels-session-storage-class and eventsTooltip.Capturing vs eventsTooltip.Bubbling (participle vs noun)
    - Source: `Capturing`
- `inspector.colorSchemeSimulationLight.tooltip` — `devtools/client/inspector.properties` — inspector.colorSchemeSimulationLight.tooltip / ...Dark.tooltip render "color scheme" as тема (a distinct Firefox concept) and "simulation" as имитация, unlike rule.colorSchemeSimulation.tooltip
    - Source: `Toggle light color scheme simulation for the page`
    - Suggest: `...Dark.tooltip`
- `flexbox.backButtonLabel` — `devtools/client/layout.properties` — flexbox.flexContainer / flexbox.backButtonLabel use Flex-блок where flexbox.noFlexboxeOnThisPage uses Flex-контейнер
    - Source: `Back to Flex Container`
- `flexbox.flexContainer` — `devtools/client/layout.properties` — flexbox.flexContainer / flexbox.backButtonLabel use Flex-блок where flexbox.noFlexboxeOnThisPage uses Flex-контейнер
    - Source: `Flex Container`
- `flexbox.noFlexboxeOnThisPage` — `devtools/client/layout.properties` — flexbox.flexContainer / flexbox.backButtonLabel use Flex-блок where flexbox.noFlexboxeOnThisPage uses Flex-контейнер
    - Source: `Select a Flex container or item to continue.`
- `layout.toggleGridHighlighter` — `devtools/client/layout.properties` — layout.toggleGridHighlighter is the only place CSS Grid becomes сетка/grade in devtools
    - Source: `Toggle Grid Highlighter`
    - Suggest: `сетка`
- `eyedropper.label` — `devtools/client/menus.properties` — eyedropper.label (menus.properties) uses the term reserved for the colour picker
    - Source: `Eyedropper`
- `netmonitor.headers.status` — `devtools/client/netmonitor.properties` — webconsole.logsFilterButton.label singular Лог vs plural siblings; netmonitor.headers.status Состояние vs Статус in adjacent labels; netmonitor.toolbar.resetColumns Восстановить колонки vs Сбросить сортировку/столбца; netmonitor.ws.context.copyFrameAsHex breaks the Копировать как X pattern
    - Source: `Status`
    - Suggest: `Лог`
- `netmonitor.toolbar.resetColumns` — `devtools/client/netmonitor.properties` — webconsole.logsFilterButton.label singular Лог vs plural siblings; netmonitor.headers.status Состояние vs Статус in adjacent labels; netmonitor.toolbar.resetColumns Восстановить колонки vs Сбросить сортировку/столбца; netmonitor.ws.context.copyFrameAsHex breaks the Копировать как X pattern
    - Source: `Reset Columns`
    - Suggest: `Лог`
- `netmonitor.ws.context.copyFrameAsHex` — `devtools/client/netmonitor.properties` — webconsole.logsFilterButton.label singular Лог vs plural siblings; netmonitor.headers.status Состояние vs Статус in adjacent labels; netmonitor.toolbar.resetColumns Восстановить колонки vs Сбросить сортировку/столбца; netmonitor.ws.context.copyFrameAsHex breaks the Копировать как X pattern
    - Source: `Copy as Hex`
    - Suggest: `Лог`
- `throttling.profile.description` — `devtools/client/network-throttling.properties` — закачка (colloquial) does not pair with выгрузка
    - Current: `закачка`
    - Source: `download %1$S%2$S, upload %3$S%4$S, latency %5$Sms`
    - Suggest: `выгрузка`
- `responsive.changeDevicePixelRatio` — `devtools/client/responsive.properties` — responsive.leftAlignViewport / responsive.changeDevicePixelRatio leave viewport Latin while responsive.rotate / responsive.screenshot use окно просмотра
    - Source: `Change device pixel ratio of the viewport`
- `responsive.leftAlignViewport` — `devtools/client/responsive.properties` — responsive.leftAlignViewport / responsive.changeDevicePixelRatio leave viewport Latin while responsive.rotate / responsive.screenshot use окно просмотра
    - Source: `Left-align Viewport`
- `responsive.rotate` — `devtools/client/responsive.properties` — responsive.leftAlignViewport / responsive.changeDevicePixelRatio leave viewport Latin while responsive.rotate / responsive.screenshot use окно просмотра
    - Source: `Rotate viewport`
- `responsive.screenshot` — `devtools/client/responsive.properties` — responsive.leftAlignViewport / responsive.changeDevicePixelRatio leave viewport Latin while responsive.rotate / responsive.screenshot use окно просмотра
    - Source: `Take a screenshot of the viewport`
- `storage-tree-labels-session-storage` — `devtools/client/storage.ftl` — storage-tree-labels-session-storage-class and eventsTooltip.Capturing vs eventsTooltip.Bubbling (participle vs noun)
    - Source: `Session Storage`
- `toolbox-meatball-menu-splitconsole-label` — `devtools/client/toolbox.ftl` — toolbox-meatball-menu-splitconsole-label / -hideconsole-label use positional wording where toolbox-options.ftl uses разделённая консоль
    - Source: `Show Split Console`
    - Suggest: `-hideconsole-label`
- `toolbox.parentProcessBrowserToolboxTitle` — `devtools/client/toolbox.properties` — toolbox.parentProcessBrowserToolboxTitle-class and options-enable-service-workers-http- (three forms of "Service Workers" in one file)
    - Source: `Parent process Browser Toolbox`
    - Suggest: `options-enable-service-workers-http-`
- `rule.colorSchemeSimulation.tooltip` — `devtools/shared/styleinspector.properties` — inspector.colorSchemeSimulationLight.tooltip / ...Dark.tooltip render "color scheme" as тема (a distinct Firefox concept) and "simulation" as имитация, unlike rule.colorSchemeSimulation.tooltip
    - Source: `Toggle color-scheme simulation for the page`
    - Suggest: `...Dark.tooltip`
- `rule.jumpDeclaration.title` — `devtools/shared/styleinspector.properties` — styleinspector.contextmenu.copyDeclaration and changes.contextmenu.copyDeclaration use декларацию where rule.jumpDeclaration.title uses объявление
    - Source: `Jump to declaration`
- `styleinspector.contextmenu.copyDeclaration` — `devtools/shared/styleinspector.properties` — styleinspector.contextmenu.copyDeclaration and changes.contextmenu.copyDeclaration use декларацию where rule.jumpDeclaration.title uses объявление
    - Source: `Copy Declaration`
- `evaluationNotifcation.noOriginalVariableMapping.msg` — `devtools/shared/webconsole.properties` — evaluationNotifcation.noOriginalVariableMapping.msg and webconsole.input.selector.tooltip use оценка (assessment) where JS evaluation is вычисление everywhere else — the only two occurrences in all of devtools
    - Source: `Original variables name mapping in the debugger is disabled. Evaluation results might not be accurate. Click the `Show original variables` checkbox in the debugger scopes panel to enable.`
- `webconsole.input.selector.tooltip` — `devtools/shared/webconsole.properties` — evaluationNotifcation.noOriginalVariableMapping.msg and webconsole.input.selector.tooltip use оценка (assessment) where JS evaluation is вычисление everywhere else — the only two occurrences in all of devtools
    - Source: `Select evaluation context`
- `webconsole.logsFilterButton.label` — `devtools/shared/webconsole.properties` — webconsole.logsFilterButton.label singular Лог vs plural siblings; netmonitor.headers.status Состояние vs Статус in adjacent labels; netmonitor.toolbar.resetColumns Восстановить колонки vs Сбросить сортировку/столбца; netmonitor.ws.context.copyFrameAsHex breaks the Копировать как X pattern
    - Source: `Logs`
    - Suggest: `Лог`
- `webconsole.message.commands.startTracingToProfiler` — `devtools/shared/webconsole.properties` — webconsole.message.commands.startTracingToProfiler names the same panel twice, once English and once transliterated
    - Source: `Started tracing to the Profiler. The traces will be displayed in the profiler on stop.`
- `devmgr-button-enable-fips` — `security/manager/security/certificates/deviceManager.ftl` — two metaphors in one dialog
    - Source: `accesskey: F label: Enable FIPS`
- _…and 4 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `community-exp` — `browser/browser/aboutDialog.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
    - Source: `<label data-l10n-name="community-exp-mozillaLink">{ -vendor-short-name }</label> is a <label data-l10n-name="community-exp-creditsLink">global community</label> working together to keep the Web open, public and accessib…`
- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — Superfluous comma before the coordinating conjunction «или» in a two-part enumeration.
    - Current: `</label>, <label data-l10n-name="helpus-getInvolvedLink">присоединяйтесь!</label>`
    - Source: `Want to help? <label data-l10n-name="helpus-donateLink">Make a donation</label>, <label data-l10n-name="helpus-shareFirefoxLink">share { -brand-product-name }</label>, or <label data-l10n-name="helpus-getInvolvedLink">g…`
    - Suggest: `</label> <label data-l10n-name="helpus-getInvolvedLink">присоединяйтесь!</label>`
    - In Russian a comma is not placed before a single «или» joining homogeneous members; the en-US comma before "or" reflects English punctuation rules only. The comma should move: «Сделайте пожертвование, поделитесь … или присоединяйтесь!»
- `pocket-panel-home-most-recent-saves-loading` — `browser/browser/aboutPocket.ftl` — `pocket-panel-home-most-recent-saves-loading` uses three dots where this locale uses …
    - Current: `Загрузка недавних сохранений...`
    - Source: `Recent saves loading…`
    - Suggest: `…`
    - The tree uses … 463 times against 6 ASCII runs.
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — “default-browser-agent.enabled” and “DisableDefaultBrowserAgent” → « »
    - Current: `“DisableDefaultBrowserAgent”`
    - Source: `The Default Browser Agent task checks when the default changes from { -brand-short-name } to another browser. If the change happens under suspicious circumstances, it will prompt users to change back to { -brand-short-n…`
    - Suggest: `« »`
- `settings-data-backup-in-progress-button` — `browser/browser/backupSettings.ftl` — `settings-data-backup-in-progress-button` uses three dots where this locale uses …
    - Current: `Выполняется резервное копирование...`
    - Source: `Backup in progress…`
    - Suggest: `…`
    - The tree uses … 463 times against 6 ASCII runs.
- `contextual-manager-password-login-line-with-alert` — `browser/browser/contextual-manager.ftl` — (предупреждение) lowercase while the origin/username variants capitalize it
    - Source: `aria-label: Copy password (Warning) title: Copy password (Warning)`
- `sidebar-callout-survey-features-question` — `browser/browser/featureCallout.ftl` — same
    - Source: `The following are potential sidebar features. Which would improve your productivity in { -brand-short-name } the most?`
- `firefoxview-opentabs-bookmarked-pinned-tab` — `browser/browser/firefoxView.ftl` — firefoxview-opentabs-bookmarked-pinned-tab vs -bookmarked-tab — firefoxView.ftl — (закладки) vs (Закладки)
    - Source: `title: Switch to (Bookmarked) { $tabTitle }`
    - Suggest: `-bookmarked-tab`
- `genai-settings-chat-lechat-links` — `browser/browser/genai.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
    - Source: `By choosing Le Chat Mistral, you agree to the Mistral AI <a data-l10n-name="link1">Terms of Service</a> and <a data-l10n-name="link2">Privacy Policy</a>.`
- `ip-protection-not-opted-in-button` — `browser/browser/ipProtection.ftl` — nova-early-access-infobar-primary-button-class: ip-protection-not-opted-in-button and device-migration-fxa-spotlight--primary-button render "Get started" as the noun Начало работы where the siblings use Начать
    - Source: `Get started`
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `accesskey: S label: Share Ideas and Feedback…`
- `nova-early-access-infobar-primary-button` — `browser/browser/newtab/asrouter.ftl` — nova-early-access-infobar-primary-button-class: ip-protection-not-opted-in-button and device-migration-fxa-spotlight--primary-button render "Get started" as the noun Начало работы where the siblings use Начать
    - Source: `(value): Got it accesskey: G`
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `{$sel_1 ->} [macos] Make it your default and keep it in your Dock. [other] Get faster browsing and automatic privacy protection.`
- `newtab-wallpaper-error-max-file-size` — `browser/browser/newtab/newtab.ftl` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
    - Source: `The image exceeded the file size limit of { $file_size }MB. Please try uploading a smaller file.`
- `newtab-widget-message-copy` — `browser/browser/newtab/newtab.ftl` — same
    - Source: `From quick reminders to daily to-dos, focus sessions to stretch breaks — stay on task and on time.`
- `create-backup-screen-1-subtitle` — `browser/browser/newtab/onboarding.ftl` — 1-2 минуты → 1–2 минуты (a numeric range takes an en dash; en-US has 1–2)
    - Current: `1-2 минуты`
    - Source: `Automatically protect your passwords, bookmarks, and more in 1–2 minutes.`
    - Suggest: `1–2 минуты`
- `multi-profile-spotlight-body` — `browser/browser/newtab/onboarding.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `Easily switch between browsing for work and fun. Profiles keep your browsing info, including search history and passwords, totally separate so you can stay organized.`
- `panic-button-open-new-window` — `browser/browser/panicButton.ftl` — новое чистое Окно → lowercase
    - Current: `новое чистое Окно`
    - Source: `Open a new clean Window`
    - Suggest: `lowercase`
- `policy-DisableFeedbackCommands` — `browser/browser/policies/policies-descriptions.ftl` — `policy-DisableFeedbackCommands` uses three dots where this locale uses …
    - Current: `Отключает команды отправки отзывов в меню Справка («Отправить отзыв...» и «Сообщить о поддельном сайте...»).`
    - Source: `Disable commands to send feedback from the Help menu (Submit Feedback and Report Deceptive Site).`
    - Suggest: `…`
    - The tree uses … 463 times against 6 ASCII runs.
- `policy-GenerativeAI` — `browser/browser/policies/policies-descriptions.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `Configure generative AI features.`
- `policy-LegacyProfiles` — `browser/browser/policies/policies-descriptions.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `Disable the feature enforcing a separate profile for each installation.`
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
    - Source: `label: { $locale } [{ $code }]`
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `accesskey: t label: Use the tab key to move focus between form controls and links`
- `certs-thirdparty-toggle` — `browser/browser/preferences/preferences.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `accesskey: t label: Allow { -brand-short-name } to automatically trust third-party root certificates you install`
- `content-blocking-etp-standard-tcp-title` — `browser/browser/preferences/preferences.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `Includes Total Cookie Protection, our most powerful privacy feature ever`
- `extension-controlled-enable` — `browser/browser/preferences/preferences.ftl` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `To enable the extension go to <img data-l10n-name="addons-icon"/> Add-ons in the <img data-l10n-name="menu-icon"/> menu.`
    - Suggest: `Apple App Store .`
- `preferences-etp-level-warning-message` — `browser/browser/preferences/preferences.ftl` — ”Устранить проблему с сайтом" — a closing curly quote used as an opener plus an ASCII straight quote as the closer. The only straight-" deviation in translated values in the whole tree.
    - Source: `heading: Heads up! Some sites may not work as expected. message: Some sites build trackers into their features or content. When { -brand-short-name } blocks them, the site looks broken. Try using “Fix site issue” or tur…`
    - Suggest: `.message`
- `security-privacy-issue-warning-ech2` — `browser/browser/preferences/preferences.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `description: Encrypted Client Hello helps hide what sites you’re about to visit from your network provider. label: Encrypted Client Hello is disabled`
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `To add a site, open the <img data-l10n-name="translations-icon"/> translation panel, select <img data-l10n-name="settings-icon"/> translation settings, then choose “Never translate this site”`
    - Suggest: `Apple App Store .`
- `sync-syncing-across-devices-empty-state2` — `browser/browser/preferences/preferences.ftl` — `sync-syncing-across-devices-empty-state2` uses three dots where this locale uses …
    - Current: `Вы ничего не синхронизируете... пока. Запустите синхронизацию, чтобы получить все ваши данные на всех ваших устройствах.`
    - Source: `description: You aren’t syncing anything… yet. Start syncing to get all of your data on all your devices. label: Manage synced data`
    - Suggest: `…`
    - The tree uses … 463 times against 6 ASCII runs.
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `{$count ->} [other] Using the { -mozilla-vpn-brand-name } encrypts all your traffic and hides your location — on up to { $count } devices. Get the most from your subscription — add it from the <a data-l10n-name="playsto…`
    - Suggest: `Apple App Store .`
- `auto-safe-mode-description` — `browser/browser/safeMode.ftl` — в Безопасном Режиме → в безопасном режиме
    - Current: `в Безопасном Режиме`
    - Source: `{ -brand-short-name } closed unexpectedly while starting. This might be caused by add-ons or other problems. You can try to resolve the problem by troubleshooting in Safe Mode.`
    - Suggest: `в безопасном режиме`
- `sidebar-history-date-today` — `browser/browser/sidebar.ftl` — sidebar-history-date-today, sidebar-history-date-yesterday (.heading) — sidebar.ftl — ASCII hyphen as the sentence dash
    - Source: `heading: Today - { $date }`
- `sidebar-history-date-yesterday` — `browser/browser/sidebar.ftl` — sidebar-history-date-today, sidebar-history-date-yesterday (.heading) — sidebar.ftl — ASCII hyphen as the sentence dash
    - Source: `heading: Yesterday - { $date }`
- `tabbrowser-tab-label-tab-split-view-right` — `browser/browser/tabbrowser.ftl` — capitalized where the -left pair is lowercase
    - Source: `{ $label }, Split view right`
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — urlbar-translations-button2, urlbar-translations-button-intro (.tooltiptext) — translations.ftl — same
    - Source: `tooltiptext: Try private translations in { -brand-shorter-name } - Beta`
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — urlbar-translations-button2, urlbar-translations-button-intro (.tooltiptext) — translations.ftl — same
    - Source: `tooltiptext: Translate this page - Beta`
- `ERROR_DOWNLOAD_CONT` — `browser/installer/nsisstrings.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `Hmm. For some reason, we could not install $BrandShortName. Choose OK to start over.`
    - Suggest: `Apple App Store .`
- `print_progress_percent` — `browser/pdfviewer/viewer.properties` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
    - Source: `{{progress}}%`
- `editorNotificationFooter.noOriginalScopes` — `devtools/client/debugger.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `Original variables name mapping is turned off, so all inline and tooltip previews are disabled. Click the `%S` checkbox in the scopes panel to turn them on.`
    - Suggest: `Apple App Store .`
- `network-menu-summary-tooltip-load` — `devtools/client/netmonitor.ftl` — network-menu-summary-tooltip-domcontentloaded (.title) and network-menu-summary-tooltip-load (.title) — devtools/client/netmonitor.ftl — “DOMContentLoaded”, “load” → « »
    - Current: `“load”`
    - Source: `title: Time when “load” event occurred`
    - Suggest: `« »`
- `charts.totalSecondsNonBlocking` — `devtools/client/netmonitor.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `Non blocking time: #1 second;Non blocking time: #1 seconds`
    - Suggest: `Apple App Store .`
- `netmonitor.timings.handledByServiceWorker` — `devtools/client/netmonitor.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `Handle fetch:`
    - Suggest: `Apple App Store .`
- `networkMenu.ws.summary.framesCount2` — `devtools/client/netmonitor.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `#1 message;#1 messages`
    - Suggest: `Apple App Store .`
- `throttling.profile.label` — `devtools/client/network-throttling.properties` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
    - Source: `%1$S (↓ %2$S%3$S ↑ %4$S%5$S ⏲ %6$Sms)`
- `perftools-onboarding-message` — `devtools/client/perftools.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
    - Source: `<b>New</b>: { -profiler-brand-name } is now integrated into Developer Tools. <a>Learn more</a> about this powerful new tool.`
- `toolbox-mode-parent-process-sub-label` — `devtools/client/toolbox.ftl` — (быстро) vs (Медленнее) on the paired label
    - Current: `(быстро)`
    - Source: `(Fast)`
    - Suggest: `(Медленнее)`
- `inactive-css-no-size-containment-fix` — `devtools/client/tooltips.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
    - Source: `Try setting its <strong>display</strong> property to something else than <strong>none</strong>, <strong>contents</strong>, <strong>table</strong>, or <strong>inline-table</strong> and make sure it’s not within a table o…`
- `webconsole.menu.openInNetworkPanel.label` — `devtools/shared/webconsole.properties` — audio-backend-class stray Title Case: support-remote-experiments-title/-features-title (see §3.J), shortest-paths.header/shortest-paths.select-node (memory.properties, Кратчайшие Пути (от Корней Сборщика Мусора)), ssl-error-sym-key-context-failure/-unwrap-failure and ssl-error-unknown-ca-alert (nsserrors.ftl), pageInfoCertificateTransparencyCompliant (pippki.properties), netmonitor.timings.servic…
    - Current: `Панели Сеть`
    - Source: `Open in Network Panel`
    - Suggest: `панели «Сеть»`
- `MathML_DeprecatedStixgeneralOperatorStretchingWarning` — `dom/chrome/dom/dom.properties` — `MathML_DeprecatedStixgeneralOperatorStretchingWarning` uses straight double quotes
    - Current: `Поддержка визуализации "stretched" операторов MathML с использованием шрифтов STIXGeneral устарела и может быть удалена в будущем. Для получения сведений о новых шрифтах, поддержка которых будет продолжена, обратитесь к…`
    - Source: `Support for rendering stretched MathML operators with STIXGeneral fonts is deprecated and may be removed at a future date. For details about newer fonts that will continue to be supported, see %S`
    - Suggest: `«stretched»`
    - The locale's quote convention is `guillemet` (1174 occurrences).
- `timer.end` — `mobile/android/chrome/browser.properties` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
    - Source: `%1$S: %2$Sms`
- `console-timer-end` — `mobile/android/mobile/android/geckoViewConsole.ftl` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
    - Source: `{ $name }: { $duration }ms`
- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — see §3.A (guillemets plus <q>)
    - Source: `To see a full view of all recorded metrics, you can use the { -profiler-brand-name }. First you must <a data-l10n-name="firefox-profiler-link">capture a performance profile</a>. Once you capture the profile, select <q>M…`
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
    - Source: `{ -brand-short-name } is made available to you under the terms of the <a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>. This means you may use, copy and distribute { -brand-short-name } to othe…`
- `a11y-handler-used` — `toolkit/toolkit/about/aboutSupport.ftl` — обработчик Доступности → lowercase
    - Current: `обработчик Доступности`
    - Source: `Accessible Handler Used`
    - Suggest: `lowercase`
- `blocked-mismatched-version` — `toolkit/toolkit/about/aboutSupport.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `Blocked for your graphics driver version mismatch between registry and DLL.`
- `experimental-features-ime-search-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — ASCII hyphen inside the gloss
    - Source: `An IME (Input Method Editor) is a tool that allows you to enter complex symbols, such as those used in East Asian or Indic written languages, using a standard keyboard. Enabling this experiment will keep the address bar…`
- `permission-dialog-set-change-app-link` — `toolkit/toolkit/global/handlerDialog.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
    - Source: `Choose a different application.`
- `fp-certerror-not-yet-valid-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
    - Source: `Sites use certificates issued by a certificate authority to prove they’re really who they say they are. { -brand-short-name } doesn’t trust this site because it looks like the certificate will not be valid until { $date…`
    - Suggest: `Apple App Store .`
- `neterror-load-error-connection` — `toolkit/toolkit/neterror/netError.ftl` — neterror-load-error-connection, neterror-load-error-firewall, neterror-proxy-resolve-failure-firewall — netError.ftl — – (en dash) used as the sentence dash where the tree uses — (163×)
    - Source: `If you are unable to load any pages, check your computer’s network connection.`
- _…and 5 more; see `state/` for the full list._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/ru/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (172)

- `about-unloads-intro` — `browser/browser/aboutUnloads.ftl` — fixed 2026-08-07
- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — fixed 2026-08-07
- `smart-window-block-description-chats` — `browser/browser/aiFeatures.ftl` — fixed 2026-08-07
- `aiwindow-firstrun-model-allpurpose-body` — `browser/browser/aiWindow.ftl` — fixed 2026-08-07
- `aiwindow-input-model-select-menu-item-description-custom` — `browser/browser/aiWindow.ftl` — fixed 2026-08-07
- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — fixed 2026-08-07
- `smart-window-cancelled-label` — `browser/browser/aiWindowContent.ftl` — fixed 2026-08-07
- `smartwindow-nl-retry-message` — `browser/browser/aiWindowContent.ftl` — fixed 2026-08-07
- `backup-file-restore-file-validation-error` — `browser/browser/backupSettings.ftl` — fixed 2026-08-07
- `backup-service-error-incorrect-password` — `browser/browser/backupSettings.ftl` — fixed 2026-08-07
- `restore-from-backup-profiles-disabled-message` — `browser/browser/backupSettings.ftl` — fixed 2026-08-07
- `sharing-warning-screen` — `browser/browser/browser.ftl` — fixed 2026-08-07
- `sharing-warning-window` — `browser/browser/browser.ftl` — fixed 2026-08-07
- `confirmation-hint-address-updated` — `browser/browser/confirmationHints.ftl` — fixed 2026-08-07
- `confirmation-hint-password-removed` — `browser/browser/confirmationHints.ftl` — fixed 2026-08-07
- `content-sharing-modal-too-many-pages` — `browser/browser/contentSharing.ftl` — fixed 2026-08-07
- `contextual-manager-passwords-delete-password-success-heading` — `browser/browser/contextual-manager.ftl` — fixed 2026-08-07
- `contextual-manager-passwords-remove-all-message` — `browser/browser/contextual-manager.ftl` — fixed 2026-08-07
- `customkeys-conflict-confirm-body` — `browser/browser/customkeys.ftl` — fixed 2026-08-07
- `callout-firefox-view-colorways-reminder-subtitle` — `browser/browser/featureCallout.ftl` — fixed 2026-08-07
- `sidebar-deprecation-callout-title` — `browser/browser/featureCallout.ftl` — fixed 2026-08-07
- `firefoxview-recentlyclosed-empty-description` — `browser/browser/firefoxView.ftl` — fixed 2026-08-07
- `genai-chatbot-summarize-sidebar-generic-subtitle` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `genai-onboarding-claude-learn` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `genai-settings-chat-chatgpt-links` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — fixed 2026-08-07
- `migration-wizard-progress-done-with-warnings-header` — `browser/browser/migrationWizard.ftl` — fixed 2026-08-07
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-07
- `windows-10-eos-feature-toast-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-07
- `newtab-personalize-icon-label` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-personalize-settings-icon-label` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-privacy-message-info-4` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-settings-button` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-shortcuts-pinned-area` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-sports-widget-view-matches` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-sports-widget-watch-stream-select-games-only` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-stocks-menu-search` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07
- `newtab-wallpaper-feature-highlight-subtitle` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-07

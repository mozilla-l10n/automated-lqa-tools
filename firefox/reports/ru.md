# Firefox l10n QA — ru

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `443328fa7930` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `443328fa7930` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,161 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (0)

_No new findings._

### ✅ Fixed since the last run (0)

_Nothing was fixed._

### 🔁 String changed, defect not verifiable — needs a re-read (0)

_Nothing to re-read._

### 🗑 Retired — the string no longer exists upstream (0)

_Nothing retired._

---

## 1. Health check

| Check | Result |
|---|---|
| Files | 360 |
| Strings | 18,161 |
| Missing strings | 2 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Access keys not in their label | 144 |
| Markup & `data-l10n-name` defects | 3 |
| Typography deviations from this locale's own norm | 6 |

### Completeness

**2 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1

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
| register | `informal` 1051, `formal` 3592 | **formal** |

---

## 2. Systemic items (decisions, not line items)

- **accesskey — 144 strings** — 144 strings. The locale kept en-US access keys rather than remapping them to its own labels. Remapping is a single decision for the locale team; it is not tracked as individual defects.
  - Affected: `addon-install-or-update-from-file`, `addressbar-locbar-engines-option-1`, `addressbar-locbar-showrecentsearches-option-2`, `appmenu-theme-installed`, `appmenu-update-available2`, `appmenu-update-manual2`, `autofill-addresses-checkbox`, `autofill-addresses-checkbox-message`, `autofill-addresses-manage-addresses-button`, `autofill-payment-methods-checkbox-submessage`, `autofill-payment-methods-manage-payments-button`, `autofill-reauth-payment-methods-checkbox` …and 132 more

---

## 3. Open findings (591)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 50 |
| 2 | Wrong content (says something other than the English) | 263 |
| 3 | Degraded language (grammar, spelling, terminology) | 214 |
| 4 | Cosmetic (typography, spacing) | 64 |

### A. Functional, markup, variables & plurals

- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — Malformed closing tag `</span >` in `about-logins-import-dialog-items-no-change2`
  - Current: `{$count ->} [one] <span>Обнаружена повторяющаяся запись:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(не импортирована)</span > [few] <span>Обнаружены повторяющиеся записи:</span> <…`
  - en-US: `{$count ->} [other] <span>Duplicate entries found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
  - Whitespace inside a closing tag makes it render as literal text.
- `urlbar-input-dismiss-autofill` — `browser/browser/browser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `urlbar-input-remove-from-history` — `browser/browser/browser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `urlbar-view-context-menu-open-in-container-tab` — `browser/browser/browser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `urlbar-view-context-menu-open-in-tab` — `browser/browser/browser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `main-context-menu-link-send-to-mobile` — `browser/browser/browserContext.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `main-context-menu-send-to-mobile-2` — `browser/browser/browserContext.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `fxviewtabrow-send-to-mobile` — `browser/browser/fxviewTabList.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `genai-menu-ask-generic-2` — `browser/browser/genai.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `genai-menu-ask-provider-2` — `browser/browser/genai.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `genai-menu-ask-smart-window` — `browser/browser/genai.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `genai-menu-no-provider-2` — `browser/browser/genai.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Malformed closing tag `</a >` in `genai-settings-chat-gemini-links`
  - Current: `Выбирая Google Gemini, вы соглашаетесь с <a data-l10n-name="link1">Условиями использования Google</a>, <a data-l10n-name="link2">Политикой запрещённого использования генеративного ИИ</a > и <a data-l10n-name="link3">Уве…`
  - en-US: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
  - Whitespace inside a closing tag makes it render as literal text.
- `newtab-sports-widget-group-a` — `browser/browser/newtab/newtab.ftl` — Cyrillic А while groups B–L all use Latin letters
- `newtab-widget-lists-completed-list` — `browser/browser/newtab/newtab.ftl` — the parentheses of the en-US format are dropped, leaving a bare number
- `mr2-onboarding-thank-you-text` — `browser/browser/newtab/onboarding.ftl` — the dash is U+4E00, the CJK ideograph for "one", not an em dash
- `mr2022-onboarding-live-language-switch-to` — `browser/browser/newtab/onboarding.ftl` — onboarding-live-language-button-label-downloading, onboarding-live-language-installing, mr2022-onboarding-live-language-switch-to — onboarding.ftl — stray square brackets around { $negotiatedLanguage } that are not in en-US (mr2022-onboarding-live-language-continue-in has none)
- `onboarding-live-language-button-label-downloading` — `browser/browser/newtab/onboarding.ftl` — onboarding-live-language-button-label-downloading, onboarding-live-language-installing, mr2022-onboarding-live-language-switch-to — onboarding.ftl — stray square brackets around { $negotiatedLanguage } that are not in en-US (mr2022-onboarding-live-language-continue-in has none)
- `onboarding-live-language-installing` — `browser/browser/newtab/onboarding.ftl` — onboarding-live-language-button-label-downloading, onboarding-live-language-installing, mr2022-onboarding-live-language-switch-to — onboarding.ftl — stray square brackets around { $negotiatedLanguage } that are not in en-US (mr2022-onboarding-live-language-continue-in has none)
- `data-collection-backlogged-crash-reports` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `history-shutdown-exceptions` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `network-proxy-connection-settings2` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `preferences-doh-manage-exceptions2` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `preferences-fonts-size` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `privacy-panel-breach-alerts` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `sitedata-cookies-exceptions3` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `sitedata-delete-on-close2` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `sitedata-settings3` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `update-application-suppress-prompts-2` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `windows-launch-on-login-open-new-tab` — `browser/browser/preferences/preferences.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-close-duplicate-tabs2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-move-split-view` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-move-tabs2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-open-in-new-container-tab2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-send-to-device2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-send-to-mobile` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-share-selected-tabs` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-unpin-tab2` — `browser/browser/tabContextMenu.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tab-context-reverse-split-view` — `browser/browser/tabbrowser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tabbrowser-context-unmute-tab2` — `browser/browser/tabbrowser.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — Malformed closing tag `</a >` in `tou-existing-user-spotlight-body`
  - Current: `Мы ввели <a data-l10n-name="terms-of-use">Условия использования</a> и обновили наше <a data-l10n-name="privacy-notice">Уведомление о конфиденциальности</a >.<br><br> Пожалуйста, потратьте немного времени, чтобы ознакоми…`
  - en-US: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
  - Whitespace inside a closing tag makes it render as literal text.
- `unified-extensions-mb-blocklist-warning-multiple` — `browser/browser/unifiedExtensions.ftl` — the entire first sentence is missing ("Some of your extensions have been disabled for violating Mozilla's policies")
  - en-US: `.message`
- `about-glean-about-data-list-item-dictionary` — `toolkit/toolkit/about/aboutGlean.ftl` — the link text is just { -glean-brand-name }, dropping "Dictionary", so the link no longer names its target
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — the second clause has no predicate at all ("…а по умолчанию для всех остальных метрик пинг metrics"), plus a stray trailing space
- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — guillemets wrapped around <q>…</q>, which renders its own quotes → double-quoted text
  - en-US: `double-quoted text`
- `about-telemetry-no-search-results` — `toolkit/toolkit/about/aboutTelemetry.ftl` — square brackets around { $sectionName } where en-US and the sibling about-telemetry-no-data-to-display use guillemets
  - Current: `{ $sectionName }`
- `popup-notification-default-button` — `toolkit/toolkit/global/popupnotification.ftl` — the OK button is Cyrillic ОК (U+041E U+041A)
  - en-US: `.label`
- `tabmodalprompt-ok-button` — `toolkit/toolkit/global/tabprompts.ftl` — same Cyrillic ОК
  - en-US: `.label`
- `webauthn-allow` — `toolkit/toolkit/webauthnDialog.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…
- `webauthn-block` — `toolkit/toolkit/webauthnDialog.ftl` — Access keys. The locale remaps access keys to Cyrillic thoroughly — 998 of 1052 are Cyrillic, and 88% of those appear in their own label. The actionable subset is the 34 access keys still carrying the en-US Latin letter, which a user typing in a Cyrillic layout cannot reach: tab-context-unpin-tab2, tab-context-open-in-new-container-tab2, tab-context-close-duplicate-tabs2, tab-context-move-tabs2,…

### B. Mistranslation, reversed meaning, wrong names & brand

- `pocket-panel-signup-cta-a-fix` — `browser/browser/aboutPocket.ftl` — Current: Ваша кнопка сохранения из Интернета → Suggest: …для Интернета
  - Current: `Ваша кнопка сохранения из Интернета`
  - en-US: `…для Интернета`
- `about-private-browsing-focus-promo-cta` — `browser/browser/aboutPrivateBrowsing.ftl` — a button label as a noun. Current: Скачивание { -focus-brand-name } → Suggest: Скачать { -focus-brand-name }
  - Current: `Скачивание { -focus-brand-name }`
  - en-US: `Скачать { -focus-brand-name }`
- `about-unloads-learn-more` — `browser/browser/aboutUnloads.ftl` — about-unloads-page-title, about-unloads-intro, about-unloads-learn-more — aboutUnloads.ftl — the feature unloads tabs in general. Current: Выгрузка вкладки → Suggest: Выгрузка вкладок
  - Current: `Выгрузка вкладки`
  - en-US: `Выгрузка вкладок`
- `about-unloads-page-title` — `browser/browser/aboutUnloads.ftl` — about-unloads-page-title, about-unloads-intro, about-unloads-learn-more — aboutUnloads.ftl — the feature unloads tabs in general. Current: Выгрузка вкладки → Suggest: Выгрузка вкладок
  - Current: `Выгрузка вкладки`
  - en-US: `Выгрузка вкладок`
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — the comment requires the quoted "Learn from…" text to match the two settings labels; the ru quotes «Узнать из…», which matches neither
- `ai-window-memories-section` — `browser/browser/aiFeatures.ftl` — en-US "can learn from your activity". Current: { -brand-short-name } может учиться на своей работе (learn from its own work) → Suggest: …может учиться на основе вашей активности
  - Current: `{ -brand-short-name } может учиться на своей работе`
  - en-US: `…может учиться на основе вашей активности`
- `aiwindow-starter-writing-improve` — `browser/browser/aiWindow.ftl` — Current: Улучши правописание (spelling) → Suggest: Улучши текст
  - Current: `Улучши правописание`
  - en-US: `Улучши текст`
- `action-log-read-page` — `browser/browser/aiWindowContent.ftl` — the dev comment says "Read is past tense, to indicate that the action has been completed", but the value uses the same aspect as the in-progress action-log-reading-page. Current: Чтение содержимого страницы → Suggest: Содержимое страницы прочитано
  - Current: `Чтение содержимого страницы`
  - en-US: `Содержимое страницы прочитано`
- `action-log-searching-history` — `browser/browser/aiWindowContent.ftl` — aiWindowContent.ftl and appmenu-search-history (.label) — appmenu.ftl — en-US "Searching history" / "Search history". Current (both): Журнал поиска (= search log) → Suggest: Поиск в журнале
  - Current: `Журнал поиска`
  - en-US: `Поиск в журнале`
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — smartwindow-nl-retry-message, smartwindow-nl-retry-group-tabs-message — aiWindowContent.ftl — the UI "card" became "карта" (map). Suggest: карточке
- `smartwindow-nl-retry-message` — `browser/browser/aiWindowContent.ftl` — smartwindow-nl-retry-message, smartwindow-nl-retry-group-tabs-message — aiWindowContent.ftl — the UI "card" became "карта" (map). Suggest: карточке
- `appmenu-help-and-report-header` — `browser/browser/appmenu.ftl` — appmenu.ftl — the "Report" half is dropped. Current: Помощь и поддержка → Suggest: Справка и жалобы
  - Current: `Помощь и поддержка`
  - en-US: `Справка и жалобы`
- `appmenuitem-help-and-report` — `browser/browser/appmenu.ftl` — appmenu.ftl — the "Report" half is dropped. Current: Помощь и поддержка → Suggest: Справка и жалобы
  - Current: `Помощь и поддержка`
  - en-US: `Справка и жалобы`
- `default-browser-notification-privacy-body-text` — `browser/browser/backgroundtasks/defaultagent.ftl` — en-US "Your default changed" is singular. Current: Ваши браузеры по умолчанию изменены. → Suggest: Ваш браузер по умолчанию изменён.
  - Current: `Ваши браузеры по умолчанию изменены.`
  - en-US: `Ваш браузер по умолчанию изменён.`
- `backup-service-error-recovery-failed` — `browser/browser/backupSettings.ftl` — it is the user's data that couldn't be restored, not Firefox. Current heading: Не удалось восстановить { -brand-short-name } → Suggest: { -brand-short-name } не смог выполнить восстановление, and in the message …попробуйте восстановить данные из резервной копии снова
  - Current: `Не удалось восстановить { -brand-short-name }`
  - en-US: `{ -brand-short-name } не смог выполнить восстановление`
- `press-tab-label` — `browser/browser/browser.ftl` — "tab" here is the Tab key. Current: Нажмите вкладку для выбора: → Suggest: Нажмите Tab для выбора: (cf. urlbar-result-action-before-tabtosearch-web)
  - Current: `Нажмите вкладку для выбора:`
  - en-US: `Нажмите Tab для выбора:`
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — Current: Поисковые действия → Suggest: Поиск по действиям (matching the sibling aria-labels)
  - Current: `Поисковые действия`
  - en-US: `Поиск по действиям`
- `main-context-menu-bidi-switch-text` — `browser/browser/browserContext.ftl` — translated identically to main-context-menu-bidi-switch-page, losing the text/page distinction. Same defect in menu-edit-bidi-switch-text-direction (menubar.ftl). Suggest: Переключить направление текста
  - en-US: `.label`
- `main-context-menu-save-link` — `browser/browser/browserContext.ftl` — en-US "Save Link As…". Current: Сохранить объект как… → Suggest: Сохранить ссылку как…
  - Current: `Сохранить объект как…`
  - en-US: `Сохранить ссылку как…`
- `main-context-menu-visual-search-2` — `browser/browser/browserContext.ftl` — the action searches using the image. Current: Поиск изображений с помощью { $engine } → Suggest: Найти это изображение с помощью { $engine }
  - Current: `Поиск изображений с помощью { $engine }`
  - en-US: `Найти это изображение с помощью { $engine }`
- `window-zoom-command` — `browser/browser/browserSets.ftl` — the macOS Window-menu "Zoom" maximizes the window. Current: Изменить масштаб → Suggest: Масштабировать окно
  - Current: `Изменить масштаб`
  - en-US: `Масштабировать окно`
- `clear-data-for-site-cookies` — `browser/browser/clearDataForSite.ftl` — as written the cookies are what sign you out. Suggest: Куки и данные сайтов — их удаление может привести к выходу из аккаунта на сайте
- `content-sharing-modal-description-signed-in` — `browser/browser/contentSharing.ftl` — Current: Мы сделали страницу со ссылками лёгкой для передачи. → Suggest: Мы создали страницу с вашими ссылками, которой легко поделиться.
  - Current: `Мы сделали страницу со ссылками лёгкой для передачи.`
  - en-US: `Мы создали страницу с вашими ссылками, которой легко поделиться.`
- `customize-mode-uidensity` — `browser/browser/customizeMode.ftl` — en-US "Density". Current: Значки (= Icons) → Suggest: Плотность (customize-mode-uidensity-link already uses "плотности окон")
  - Current: `Значки`
  - en-US: `Плотность`
- `customkeys-search-input` — `browser/browser/customkeys.ftl` — customkeys-search-input (.aria-label, .placeholder) — customkeys.ftl — en-US "Search shortcuts" (dev comment: "Search is a verb"). Current: Значки поисковых систем — "search engine icons", apparently copy-pasted from search-popover in touchbar.ftl; it has nothing to do with the string → Suggest: Поиск сочетаний клавиш
  - en-US: `Поиск сочетаний клавиш`
- `firefox-relay-opt-in-confirmation-enable-button` — `browser/browser/firefoxRelay.ftl` — en-US "Use email mask" (a button). Current: Используйте псевдонимы электронной почты → Suggest: Использовать псевдоним эл. почты; note firefox-relay-offer-legal-notice quotes this button as «Использовать псевдоним электронной почты», so the two currently disagree
  - Current: `Используйте псевдонимы электронной почты`
  - en-US: `Использовать псевдоним эл. почты`
- `firefoxview-search-text-box-clear-button` — `browser/browser/firefoxView.ftl` — en-US "Clear". Current: Удалить → Suggest: Очистить
  - Current: `Удалить`
  - en-US: `Очистить`
- `firefoxview-syncedtabs-adddevice-header-3` — `browser/browser/firefoxView.ftl` — en-US "Your tabs called." is a playful idiom. Current: Ваши вкладки вызваны. reads as "your tabs have been summoned" → Suggest something idiomatic, e.g. Ваши вкладки на связи. Они на вашем телефоне.
  - Current: `Ваши вкладки вызваны.`
  - en-US: `Ваши вкладки на связи. Они на вашем телефоне.`
- `firefoxview-tabpickup-header` — `browser/browser/firefoxView.ftl` — "Tab pickup" is about resuming tabs from other devices. Current: Выбор вкладки → Suggest: Вкладки с других устройств
  - Current: `Выбор вкладки`
  - en-US: `Вкладки с других устройств`
- `genai-chatbot-summarize-sidebar-generic-subtitle` — `browser/browser/genai.ftl` — the "sparkles button". Current: по кнопке с блестками → Suggest: с блёстками (and see §3.H for the missing ё)
  - Current: `по кнопке с блестками`
  - en-US: `с блёстками`
- `genai-onboarding-select-description` — `browser/browser/genai.ftl` — en-US "you can also write in your own prompts" = type your own. Current: Вы также можете писать в своих собственных запросах. → Suggest: Вы также можете вводить свои собственные запросы.
  - Current: `Вы также можете писать в своих собственных запросах.`
  - en-US: `Вы также можете вводить свои собственные запросы.`
- `genai-settings-chat-lechat-links-2` — `browser/browser/genai.ftl` — en-US attributes the documents to "Mistral AI"; the ru drops the vendor (the older -lechat-links keeps it)
- `link-preview-first-time-setup-message` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
  - en-US: `ключевые моменты`
- `link-preview-generation-error-missing-data-v2` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
  - en-US: `ключевые моменты`
- `link-preview-key-points-disclaimer` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
  - en-US: `ключевые моменты`
- `link-preview-key-points-header` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
  - en-US: `ключевые моменты`
- `link-preview-optin-message` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
  - en-US: `ключевые моменты`
- `link-preview-settings-key-points` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
  - en-US: `ключевые моменты`
- `link-preview-setup-faster-next-time` — `browser/browser/genai.ftl` — "key points" as "ключевые точки" — genai.ftl — a geometric term. Affects link-preview-key-points-header, link-preview-key-points-disclaimer, link-preview-settings-key-points, link-preview-optin-message, link-preview-generation-error-missing-data-v2, link-preview-setup-faster-next-time, link-preview-first-time-setup-message (7 strings) → Suggest: ключевые моменты / основные тезисы
  - en-US: `ключевые моменты`
- `ip-protection-bandwidth-warning-infobar-message-75` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
  - en-US: `Лимиты встроенного VPN…`
- `ipprotection-feature-introduction-link-text-captive-portal-1` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
  - en-US: `Лимиты встроенного VPN…`
- `ipprotection-feature-introduction-link-text-privacy-2` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
  - en-US: `Лимиты встроенного VPN…`
- `ipprotection-location-selection-callout-description-1` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
  - en-US: `Лимиты встроенного VPN…`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
  - en-US: `Лимиты встроенного VPN…`
- `ipprotection-message-continuous-onboarding-site-settings` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
  - en-US: `Лимиты встроенного VPN…`
- `ipprotection-summer-promo-offramp-generic-title` — `browser/browser/ipProtection.ftl` — several: ipprotection-summer-promo-offramp-generic-title ("built-in" modifies VPN, not the limits → Лимиты встроенного VPN…); ipprotection-feature-introduction-link-text-privacy-2 and ipprotection-location-selection-callout-description-1 hardcode "5 местоположений" where en-US says "multiple"/"several"; ipprotection-feature-introduction-link-text-captive-portal-1 drops and inverts the "hide where…
  - en-US: `Лимиты встроенного VPN…`
- `menu-bookmarks-all-tabs` — `browser/browser/menubar.ftl` — the target of the action is dropped. Current: Добавить все вкладки… → Suggest: Добавить все вкладки в закладки…
  - Current: `Добавить все вкладки…`
  - en-US: `Добавить все вкладки в закладки…`
- `import-from-chrome-beta` — `browser/browser/migration.ftl` — import-from-chrome-beta (.label) — migration.ftl and migration-wizard-migrator-display-name-chrome-beta — migrationWizard.ftl — Current: Chrome Бета while "Microsoft Edge Beta" and "Chrome Dev" stay intact in the same lists
  - en-US: `.label`
- `annotations-default-pdf-handler-body` — `browser/browser/newtab/asrouter.ftl` — dev comment: "'Go-to' … refers to something that is used often". Current: популярные подписи → Suggest: часто используемые подписи
  - Current: `популярные подписи`
  - en-US: `часто используемые подписи`
- `cfr-protections-panel-body` — `browser/browser/newtab/asrouter.ftl` — en-US "many of the most common". Current: большинства наиболее известных трекеров overstates the claim → Suggest: многих наиболее распространённых трекеров
  - Current: `большинства наиболее известных трекеров`
  - en-US: `многих наиболее распространённых трекеров`
- `relay-50-masks-announcement-title` — `browser/browser/newtab/asrouter.ftl` — dev comment: "'on us' … means 'for free'". Current: 50 псевдонимов электронной почты на нас is a literal calque with no such meaning → Suggest: …— бесплатно
  - Current: `50 псевдонимов электронной почты на нас`
  - en-US: `…— бесплатно`
- `windows-10-eos-challenger-callout-title` — `browser/browser/newtab/asrouter.ftl` — en-US "That's the point." Current: В этом ключ. (not an idiomatic Russian phrase) → Suggest: В этом и суть.
  - Current: `В этом ключ.`
  - en-US: `В этом и суть.`
- `windows-10-eos-feature-toast-subtitle` — `browser/browser/newtab/asrouter.ftl` — Current: По популярным запросам, → Suggest: По многочисленным просьбам (and drop the comma)
  - Current: `По популярным запросам,`
  - en-US: `По многочисленным просьбам`
- `newtab-clock-city-id-makassar` — `browser/browser/newtab/newtab.ftl` — Current: Макасар → Suggest: Макассар
  - Current: `Макасар`
  - en-US: `Макассар`
- `newtab-privacy-modal-paragraph-2` — `browser/browser/newtab/newtab.ftl` — en-US "dishing up captivating stories" = serving/showing. Current: Помимо сохранения увлекательных статей → Suggest: Помимо публикации увлекательных статей
  - Current: `Помимо сохранения увлекательных статей`
  - en-US: `Помимо публикации увлекательных статей`
- `newtab-sports-widget-match-full-time` — `browser/browser/newtab/newtab.ftl` — newtab.ftl sports/stocks widget: newtab-sports-widget-view-matches and newtab-sports-widget-loading-more translate football "matches" as search "совпадения"; newtab-sports-widget-watch-stream-select-games-only reads "Select" as an imperative when the comment shows it is an adjective; newtab-sports-widget-match-full-time = Полное время is not a football term (→ Основное время / Матч окончен); newt…
  - Current: `Полное время`
  - en-US: `Основное время`
- `newtab-sports-widget-team-name-label-civ` — `browser/browser/newtab/newtab.ftl` — ASCII apostrophe in Кот-д'Ивуар
  - en-US: `.label`
- `newtab-wallpaper-blue-flowers` — `browser/browser/newtab/newtab.ftl` — Wallpaper descriptions — newtab.ftl — newtab-wallpaper-light-landscape renders "mist" as дым (smoke); newtab-wallpaper-blue-flowers says цветов с голубыми цветами (repeats the word, loses "petaled"); newtab-wallpaper-celestial-eclipse-time-lapse renders "time lapse" as Хронометраж; newtab-wallpaper-celestial-river renders "satellite" as Космический
- `newtab-wallpaper-celestial-eclipse-time-lapse` — `browser/browser/newtab/newtab.ftl` — Wallpaper descriptions — newtab.ftl — newtab-wallpaper-light-landscape renders "mist" as дым (smoke); newtab-wallpaper-blue-flowers says цветов с голубыми цветами (repeats the word, loses "petaled"); newtab-wallpaper-celestial-eclipse-time-lapse renders "time lapse" as Хронометраж; newtab-wallpaper-celestial-river renders "satellite" as Космический
- `newtab-wallpaper-celestial-river` — `browser/browser/newtab/newtab.ftl` — Wallpaper descriptions — newtab.ftl — newtab-wallpaper-light-landscape renders "mist" as дым (smoke); newtab-wallpaper-blue-flowers says цветов с голубыми цветами (repeats the word, loses "petaled"); newtab-wallpaper-celestial-eclipse-time-lapse renders "time lapse" as Хронометраж; newtab-wallpaper-celestial-river renders "satellite" as Космический
- _…and 203 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `helpus-referrals` — `browser/browser/aboutDialog.ftl` — Spurious comma: before a single или in elevation-more-elevated, pleaseSelect, policy-Bookmarks, safeb-blocked-phishing-page-error-desc-override, helpus-referrals, aiwindow-firstrun-memories-subtitle; before и in mr2022-onboarding-mobile-download-subtitle, newtab-wallpaper-feature-highlight-subtitle, details-notification-hard-blocked-other; after a leading prepositional phrase in abuse-report-sett…
  - Current: `или`
- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — about-logins-confirm-remove-all-sync-dialog-message3 (all 4 variants) — всех отображаемых здесь предупреждениях о взломе → предупреждений
  - Current: `всех отображаемых здесь предупреждениях о взломе`
  - en-US: `предупреждений`
- `about-logins-copy-password-os-auth-dialog-message-win` — `browser/browser/aboutLogins.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
  - en-US: `-location-desc`
- `about-logins-import-dialog-items-no-change` — `browser/browser/aboutLogins.ftl` — about-logins-import-dialog-items-no-change ([few], [many]) — Найдены повторяющие логины → повторяющиеся логины
  - Current: `Найдены повторяющие логины`
  - en-US: `повторяющиеся логины`
- `about-logins-import-report-modified2` — `browser/browser/aboutLogins.ftl` — about-logins-import-report-modified2 ([many]) — существующих записей обновлены → обновлено
  - Current: `существующих записей обновлены`
  - en-US: `обновлено`
- `active-policies-tab` — `browser/browser/aboutPolicies.ftl` — aboutPolicies.ftl — a predicative short form used as a nav label: Активны → Активные
  - Current: `Активны`
  - en-US: `Активные`
- `active-policies-tab-title` — `browser/browser/aboutPolicies.ftl` — aboutPolicies.ftl — a predicative short form used as a nav label: Активны → Активные
  - Current: `Активны`
  - en-US: `Активные`
- `about-private-browsing-cookie-banners-promo-body` — `browser/browser/aboutPrivateBrowsing.ftl` — от многих уведомлениях о куки → от многих уведомлений о куках
  - Current: `от многих уведомлениях о куки`
  - en-US: `от многих уведомлений о куках`
- `ai-window-no-memories-learning-off` — `browser/browser/aiFeatures.ftl` — Обучение через активности отключены → Обучение на основе активности отключено
  - Current: `Обучение через активности отключены`
  - en-US: `Обучение на основе активности отключено`
- `smart-window-block-description-chats` — `browser/browser/aiFeatures.ftl` — smartwindow-nl-retry-message, restore-from-backup-profiles-disabled-message, smart-window-block-description-chats — see §3.H for the ё issues in these
- `aiwindow-ai-chat-grid-grid-view` — `browser/browser/aiWindow.ftl` — aiwindow-ai-chat-grid-grid-view (.aria-label) — Переключение режим → Переключение режима
  - Current: `Переключение режим`
  - en-US: `Переключение режима`
- `aiwindow-firstrun-memories-subtitle` — `browser/browser/aiWindow.ftl` — Spurious comma: before a single или in elevation-more-elevated, pleaseSelect, policy-Bookmarks, safeb-blocked-phishing-page-error-desc-override, helpus-referrals, aiwindow-firstrun-memories-subtitle; before и in mr2022-onboarding-mobile-download-subtitle, newtab-wallpaper-feature-highlight-subtitle, details-notification-hard-blocked-other; after a leading prepositional phrase in abuse-report-sett…
  - Current: `или`
- `action-log-checking-world-cup-live` — `browser/browser/aiWindowContent.ftl` — прямых трансляции → прямых трансляций
  - Current: `прямых трансляции`
  - en-US: `прямых трансляций`
- `smart-window-closed-tabs-summary` — `browser/browser/aiWindowContent.ftl` — smart-window-closed-tabs-summary ([one]) — aiWindowContent.ftl — Вкладка закрыты → Вкладка закрыта
  - Current: `Вкладка закрыты`
  - en-US: `Вкладка закрыта`
- `smart-window-restore-success-summary` — `browser/browser/aiWindowContent.ftl` — smart-window-restore-success-summary ([one]) — Вкладки закрыта → Вкладка закрыта
  - Current: `Вкладки закрыта`
  - en-US: `Вкладка закрыта`
- `smartwindow-nl-retry-message` — `browser/browser/aiWindowContent.ftl` — smartwindow-nl-retry-message, restore-from-backup-profiles-disabled-message, smart-window-block-description-chats — see §3.H for the ё issues in these
- `restore-from-backup-profiles-disabled-message` — `browser/browser/backupSettings.ftl` — smartwindow-nl-retry-message, restore-from-backup-profiles-disabled-message, smart-window-block-description-chats — see §3.H for the ё issues in these
- `trustpanel-insecure-description` — `browser/browser/browser.ftl` — the pronoun does not agree with данные. Current: Его можно просмотреть → Suggest: Их можно просмотреть
  - Current: `Его можно просмотреть`
  - en-US: `Их можно просмотреть`
- `trustpanel-tracking-cookies-not-blocking-tab-header` — `browser/browser/browser.ftl` — trustpanel-tracking-cookies-not-blocking-tab-header ([one]) — { $count } межсайтовых отслеживающих куки → { $count } межсайтовый отслеживающий куки
  - Current: `{ $count } межсайтовых отслеживающих куки`
  - en-US: `{ $count } межсайтовый отслеживающий куки`
- `urlbar-result-explanation-last-visited-weeks-2` — `browser/browser/browser.ftl` — urlbar-result-explanation-last-visited-weeks-2 ([one]) — { $weeksAgo } неделя назад → неделю назад (the v1 string is correct)
  - Current: `{ $weeksAgo } неделя назад`
  - en-US: `неделю назад`
- `requested-crash-reports-message-new` — `browser/browser/contentCrash.ftl` — requested-crash-reports-message-new ([many]) — contentCrash.ftl — { $reportCount } неотправленных отчёта → отчётов (the [few] variant is correct)
  - Current: `{ $reportCount } неотправленных отчёта`
  - en-US: `отчётов`
- `contextual-manager-passwords-copy-password-os-auth-dialog-message-win` — `browser/browser/contextual-manager.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
  - en-US: `-location-desc`
- `contextual-manager-passwords-remove-all-message` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-remove-all-message ([few], [many]) — При этом будет удалены пароли → будут удалены
  - Current: `При этом будет удалены пароли`
  - en-US: `будут удалены`
- `contextual-manager-passwords-remove-all-message-sync` — `browser/browser/contextual-manager.ftl` — о утечках → об утечках
  - Current: `о утечках`
  - en-US: `об утечках`
- `contextual-manager-view-alert-button` — `browser/browser/contextual-manager.ftl` — contextual-manager-view-alert-button (.tooltiptext) — garbled and reversed: Уведомление об проверке → Просмотреть уведомление
  - Current: `Уведомление об проверке`
  - en-US: `Просмотреть уведомление`
- `sidebar-callout-survey-keep-website-open` — `browser/browser/featureCallout.ftl` — открытыми → открытым
  - Current: `открытыми`
  - en-US: `открытым`
- `ip-protection-bandwidth-help-text` — `browser/browser/ipProtection.ftl` — Сбрасывается на { $maxUsage } ГБ → до { $maxUsage } ГБ
  - Current: `Сбрасывается на { $maxUsage } ГБ`
  - en-US: `до { $maxUsage } ГБ`
- `ip-protection-vpn-upgrade-link-1` — `browser/browser/ipProtection.ftl` — ipprotection-locations-subview-promo (.message) and ip-protection-vpn-upgrade-link-1 (.description) — ipProtection.ftl — the ungrammatical на до 5 устройствах → Suggest: не более чем на 5 устройствах
  - Current: `на до 5 устройствах`
  - en-US: `не более чем на 5 устройствах`
- `ipprotection-bandwidth-reset-title` — `browser/browser/ipProtection.ftl` — the subject is the GB of data. Current: { $maxUsage } ГБ VPN, обновлён → Suggest: обновлены
  - Current: `{ $maxUsage } ГБ VPN, обновлён`
  - en-US: `обновлены`
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — ipprotection-locations-subview-promo (.message) and ip-protection-vpn-upgrade-link-1 (.description) — ipProtection.ftl — the ungrammatical на до 5 устройствах → Suggest: не более чем на 5 устройствах
  - Current: `на до 5 устройствах`
  - en-US: `не более чем на 5 устройствах`
- `ipprotection-summer-promo-offramp-default-browser-incentive-description` — `browser/browser/ipProtection.ftl` — метоположений → местоположений
  - Current: `метоположений`
  - en-US: `местоположений`
- `menu-application-referrals` — `browser/browser/menubar.ftl` — menu-application-set-as-default (.label), menu-application-referrals (.label), menu-referrals (.label) — menubar.ftl — 2nd-person imperatives in menu labels where every other label uses the infinitive
  - en-US: `.label`
- `menu-application-set-as-default` — `browser/browser/menubar.ftl` — menu-application-set-as-default (.label), menu-application-referrals (.label), menu-referrals (.label) — menubar.ftl — 2nd-person imperatives in menu labels where every other label uses the infinitive
  - en-US: `.label`
- `menu-referrals` — `browser/browser/menubar.ftl` — menu-application-set-as-default (.label), menu-application-referrals (.label), menu-referrals (.label) — menubar.ftl — 2nd-person imperatives in menu labels where every other label uses the infinitive
  - en-US: `.label`
- `cfr-doorhanger-milestone-heading2` — `browser/browser/newtab/asrouter.ftl` — cfr-doorhanger-milestone-heading2 (all three variants) — asrouter.ftl — the exclamation mark now falls mid-sentence, after the date, because the clause order was inverted.
- `cookie-banner-blocker-onboarding-header` — `browser/browser/newtab/asrouter.ftl` — asrouter.ftl — уведомление о куки → о куках; меньше куки → меньше кук
  - Current: `уведомление о куки`
  - en-US: `о куках`
- `firefoxview-spotlight-promo-subtitle` — `browser/browser/newtab/asrouter.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
  - en-US: `-location-desc`
- `newtab-activation-window-message-values-focus-message` — `browser/browser/newtab/newtab.ftl` — the second half is a dangling fragment with no predicate
- `newtab-error-fallback-info` — `browser/browser/newtab/newtab.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
  - en-US: `-location-desc`
- `newtab-picture-set-wallpaper` — `browser/browser/newtab/newtab.ftl` — newtab.ftl — a noun for an action button: Установка обоев → Установить обои (its own .aria-label already uses the verb)
  - Current: `Установка обоев`
  - en-US: `Установить обои`
- `newtab-privacy-message-first-protection` — `browser/browser/newtab/newtab.ftl` — продолжать requires an infinitive: будет продолжать блокировки → блокировать
  - Current: `будет продолжать блокировки`
  - en-US: `блокировать`
- `newtab-privacy-message-info-6` — `browser/browser/newtab/newtab.ftl` — это does not agree with данные, and en-US's factual "might" became a conditional
  - Current: `это`
  - en-US: `данные`
- `newtab-report-ads-reason-seen-it-too-many-times` — `browser/browser/newtab/newtab.ftl` — tense: Я вижу это слишком много раз → Я видел это слишком много раз
  - Current: `Я вижу это слишком много раз`
  - en-US: `Я видел это слишком много раз`
- `newtab-section-mangage-topics-followed-topics-empty-state` — `browser/browser/newtab/newtab.ftl` — genitive-under-negation, and see §3.J for the follow terminology
- `create-backup-screen-1-flair` — `browser/browser/newtab/onboarding.ftl` — a badge on a single tile: Рекомендуемые → Рекомендуется
  - Current: `Рекомендуемые`
  - en-US: `Рекомендуется`
- `mr2022-onboarding-mobile-download-subtitle` — `browser/browser/newtab/onboarding.ftl` — Spurious comma: before a single или in elevation-more-elevated, pleaseSelect, policy-Bookmarks, safeb-blocked-phishing-page-error-desc-override, helpus-referrals, aiwindow-firstrun-memories-subtitle; before и in mr2022-onboarding-mobile-download-subtitle, newtab-wallpaper-feature-highlight-subtitle, details-notification-hard-blocked-other; after a leading prepositional phrase in abuse-report-sett…
  - Current: `или`
- `origin-controls-option-all-domains` — `browser/browser/originControls.ftl` — origin-controls-option-all-domains (.label), origin-controls-state-no-access, origin-controls-state-always-on — originControls.ftl — en-US "site(s)" rendered as страницах, while origin-controls-state-quarantined and the toolbar tooltip in the same file correctly use сайт
  - en-US: `.label`
- `origin-controls-state-always-on` — `browser/browser/originControls.ftl` — origin-controls-option-all-domains (.label), origin-controls-state-no-access, origin-controls-state-always-on — originControls.ftl — en-US "site(s)" rendered as страницах, while origin-controls-state-quarantined and the toolbar tooltip in the same file correctly use сайт
  - en-US: `.label`
- `origin-controls-state-no-access` — `browser/browser/originControls.ftl` — origin-controls-option-all-domains (.label), origin-controls-state-no-access, origin-controls-state-always-on — originControls.ftl — en-US "site(s)" rendered as страницах, while origin-controls-state-quarantined and the toolbar tooltip in the same file correctly use сайт
  - en-US: `.label`
- `policy-Bookmarks` — `browser/browser/policies/policies-descriptions.ftl` — Spurious comma: before a single или in elevation-more-elevated, pleaseSelect, policy-Bookmarks, safeb-blocked-phishing-page-error-desc-override, helpus-referrals, aiwindow-firstrun-memories-subtitle; before и in mr2022-onboarding-mobile-download-subtitle, newtab-wallpaper-feature-highlight-subtitle, details-notification-hard-blocked-other; after a leading prepositional phrase in abuse-report-sett…
  - Current: `или`
- `permissions-site-notification-desc` — `browser/browser/preferences/permissions.ftl` — Missing comma before a subordinate clause or participial phrase: permissions-site-notification-desc, -location-desc, -xr-desc, -camera-desc, -microphone-desc (permissions.ftl, 5 strings; the speaker and cookie siblings do it correctly); startup-cache-dialog-title2 (aboutSupport.ftl); about-logins-copy-password-os-auth-dialog-message-win and contextual-manager-passwords-copy-password-os-auth-dialo…
  - en-US: `-location-desc`
- `containers-card-header2` — `browser/browser/preferences/preferences.ftl` — таим образом → таким образом
  - Current: `таим образом`
  - en-US: `таким образом`
- `cookie-banner-blocker-checkbox-label` — `browser/browser/preferences/preferences.ftl` — cookie-banner-blocker-checkbox-label (.label) and cookie-banner-blocker-header — preferences.ftl — prepositional instead of genitive after от, wrong number, and куки left undeclined
  - en-US: `.label`
- `cookie-banner-blocker-header` — `browser/browser/preferences/preferences.ftl` — cookie-banner-blocker-checkbox-label (.label) and cookie-banner-blocker-header — preferences.ftl — prepositional instead of genitive after от, wrong number, and куки left undeclined
  - en-US: `.label`
- `open-external-link-next-to-active-tab` — `browser/browser/preferences/preferences.ftl` — open-external-link-next-to-active-tab (.label), settings-tabs-drag-to-create-tab-groups (.label) — preferences.ftl — imperatives where every other checkbox label uses the infinitive
  - en-US: `.label`
- `privacy-panel-breach-alerts` — `browser/browser/preferences/preferences.ftl` — a persistent checkbox needs the imperfective: Показать → Показывать
  - Current: `Показать`
  - en-US: `Показывать`
- `security-privacy-issue-warning-ech2` — `browser/browser/preferences/preferences.ftl` — скрыть, как сайты вы собираетесь посетить → какие сайты вы собираетесь посетить (also missing the final period that en-US and the parallel -doh2 have)
  - Current: `скрыть, как сайты вы собираетесь посетить`
  - en-US: `какие сайты вы собираетесь посетить`
- `settings-tabs-drag-to-create-tab-groups` — `browser/browser/preferences/preferences.ftl` — open-external-link-next-to-active-tab (.label), settings-tabs-drag-to-create-tab-groups (.label) — preferences.ftl — imperatives where every other checkbox label uses the infinitive
  - en-US: `.label`
- `avatar-selector-custom-tab` — `browser/browser/profiles.ftl` — a dangling feminine adjective for "Custom" next to Значок: Персональная → Свой
  - Current: `Персональная`
  - en-US: `Свой`
- `briefcase-avatar-tooltip` — `browser/browser/profiles.ftl` — с портфелей → с портфелем
  - Current: `с портфелей`
  - en-US: `с портфелем`
- _…and 92 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `firefox-relay-offer-legal-notice` — `browser/browser/browser.ftl` — firefox-relay-offer-legal-notice Примечанием о конфиденциальности vs Уведомлением… in -notice-1 right below
  - en-US: `Примечанием о конфиденциальности`
- `quickactions-cmd-clearrecenthistory2` — `browser/browser/browser.ftl` — 3. кеш (46) vs кэш — the locale's choice is кеш; the one straggler is sitedata-heading (.description). (quickactions-cmd-clearrecenthistory2 listing both is intentional.)
  - Current: `кеш`
  - en-US: `кэш`
- `trustpanel-clear-cookies-description` — `browser/browser/browser.ftl` — trustpanel-clear-cookies-description and item-cookies-site-data-description use the slang разлогин where clearDataForSite.ftl uses выход из аккаунта
- `contextual-manager-passwords-import-success-message-2` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-import-success-message-2 Новое: vs Добавлено: in -import-success-message
  - en-US: `Новое:`
- `customkeys-conflict-confirm-title` — `browser/browser/customkeys.ftl` — 9. ярлык for keyboard shortcuts — customkeys.ftl (customkeys-shortcut-unassigned, customkeys-shortcut-input, customkeys-conflict-confirm-title, customkeys-reset-all-confirm-body) and shortcuts-remove-button, where the rest uses сочетание клавиш. Worse, customkeys-conflict-confirm-body, -unusable-title, -unusable-body use ключ (a cryptographic key) for a keyboard key.
  - Current: `ярлык`
- `customkeys-reset-all-confirm-body` — `browser/browser/customkeys.ftl` — 9. ярлык for keyboard shortcuts — customkeys.ftl (customkeys-shortcut-unassigned, customkeys-shortcut-input, customkeys-conflict-confirm-title, customkeys-reset-all-confirm-body) and shortcuts-remove-button, where the rest uses сочетание клавиш. Worse, customkeys-conflict-confirm-body, -unusable-title, -unusable-body use ключ (a cryptographic key) for a keyboard key.
  - Current: `ярлык`
- `customkeys-shortcut-input` — `browser/browser/customkeys.ftl` — 9. ярлык for keyboard shortcuts — customkeys.ftl (customkeys-shortcut-unassigned, customkeys-shortcut-input, customkeys-conflict-confirm-title, customkeys-reset-all-confirm-body) and shortcuts-remove-button, where the rest uses сочетание клавиш. Worse, customkeys-conflict-confirm-body, -unusable-title, -unusable-body use ключ (a cryptographic key) for a keyboard key.
  - Current: `ярлык`
- `customkeys-shortcut-unassigned` — `browser/browser/customkeys.ftl` — 9. ярлык for keyboard shortcuts — customkeys.ftl (customkeys-shortcut-unassigned, customkeys-shortcut-input, customkeys-conflict-confirm-title, customkeys-reset-all-confirm-body) and shortcuts-remove-button, where the rest uses сочетание клавиш. Worse, customkeys-conflict-confirm-body, -unusable-title, -unusable-body use ключ (a cryptographic key) for a keyboard key.
  - Current: `ярлык`
- `ipprotecion-locations-subview-recommended-label` — `browser/browser/ipProtection.ftl` — ipprotection-location-country-button Местонахождение vs Местоположение; ipprotecion-locations-subview-recommended-label Рекомендуемые (plural) vs Рекомендуемое
  - en-US: `Местонахождение`
- `ipprotection-location-country-button` — `browser/browser/ipProtection.ftl` — ipprotection-location-country-button Местонахождение vs Местоположение; ipprotecion-locations-subview-recommended-label Рекомендуемые (plural) vs Рекомендуемое
  - en-US: `Местонахождение`
- `set-default-menu-message-row-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — set-default-menu-message-row-layout-subtitle uses конфиденциальность where the scope uses приватность
  - en-US: `конфиденциальность`
- `newtab-privacy-message-milestone-year` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-milestone-year (all variants) — same
- `newtab-section-mangage-topics-followed-topics-empty-state` — `browser/browser/newtab/newtab.ftl` — newtab-section-toast-follow/-unfollow and newtab-section-mangage-topics-followed-topics-empty-state use читаете/отслеживаете while every button and aria-label uses подписаться/отписаться, per the dev comment
  - en-US: `-unfollow`
- `newtab-section-toast-follow` — `browser/browser/newtab/newtab.ftl` — newtab-section-toast-follow/-unfollow and newtab-section-mangage-topics-followed-topics-empty-state use читаете/отслеживаете while every button and aria-label uses подписаться/отписаться, per the dev comment
  - en-US: `-unfollow`
- `create-backup-screen-2-easy-list-1` — `browser/browser/newtab/onboarding.ftl` — fx-backup-confirmation-screen-easy-setup-item-text-1 журнал vs create-backup-screen-2-easy-list-1 история
  - en-US: `журнал`
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — sync-to-mobile-button-label vs desktop-to-mobile-subtitle — the subtitle instructs the user to select a label that doesn't match the actual button
- `fx-backup-confirmation-screen-easy-setup-item-text-1` — `browser/browser/newtab/onboarding.ftl` — fx-backup-confirmation-screen-easy-setup-item-text-1 журнал vs create-backup-screen-2-easy-list-1 история
  - en-US: `журнал`
- `sync-to-mobile-button-label` — `browser/browser/newtab/onboarding.ftl` — sync-to-mobile-button-label vs desktop-to-mobile-subtitle — the subtitle instructs the user to select a label that doesn't match the actual button
- `policy-CNSA2KeyAgreementEnabled` — `browser/browser/policies/policies-descriptions.ftl` — policy-CNSA2KeyAgreementEnabled соглашение о ключе (a legal agreement) vs согласование ключей in policy-PostQuantumKeyAgreementEnabled
  - en-US: `соглашение о ключе`
- `policy-PostQuantumKeyAgreementEnabled` — `browser/browser/policies/policies-descriptions.ftl` — policy-CNSA2KeyAgreementEnabled соглашение о ключе (a legal agreement) vs согласование ключей in policy-PostQuantumKeyAgreementEnabled
  - en-US: `соглашение о ключе`
- `search-filtering-for-add-engine` — `browser/browser/preferences/preferences.ftl` — "поисковик" (colloquial) in search-filtering-for-add-engine vs поисковая система everywhere else
  - en-US: `поисковая система`
- `item-cookies-site-data-description` — `browser/browser/sanitize.ftl` — trustpanel-clear-cookies-description and item-cookies-site-data-description use the slang разлогин where clearDataForSite.ftl uses выход из аккаунта
- `screenshot-toolbar-button` — `browser/browser/screenshots.ftl` — 8. скриншот vs снимок экрана — mixed inside devtools/shared/screenshot.properties (6 vs 3 entries) and between screenshots.ftl's screenshot-toolbarbutton and screenshot-toolbar-button.
  - Current: `скриншот`
  - en-US: `снимок экрана`
- `fxa-menu-sign-in-promo-heading` — `browser/browser/sync.ftl` — "Sync": Синхронизацию capitalized vs lowercase, inside syncSetup.properties (2 strings) and between fxa-menu-sign-in-promo-heading and sync-setup-verify-heading
  - Current: `Синхронизацию`
- `sync-setup-verify-heading` — `browser/browser/sync.ftl` — "Sync": Синхронизацию capitalized vs lowercase, inside syncSetup.properties (2 strings) and between fxa-menu-sign-in-promo-heading and sync-setup-verify-heading
  - Current: `Синхронизацию`
- `editor_ink_opacity` — `browser/pdfviewer/viewer.properties` — 10. Прозрачность for opacity — colorpicker-tooltip-alpha-slider-title and editorinkopacity (see §3.B).
  - Current: `Прозрачность`
- `changes.contextmenu.copyDeclaration` — `devtools/client/changes.properties` — styleinspector.contextmenu.copyDeclaration and changes.contextmenu.copyDeclaration use декларацию where rule.jumpDeclaration.title uses объявление
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — noDomMutationBreakpoints.notice quotes a menu item whose actual label in the same file is different
- `skipPausingTooltip.label` — `devtools/client/debugger.properties` — skipPausingTooltip.label / undoSkipPausingTooltip.label collapse the global Deactivate/Activate toggle onto the same strings as the per-breakpoint Disable/Enable commands, making them indistinguishable
- `undoSkipPausingTooltip.label` — `devtools/client/debugger.properties` — skipPausingTooltip.label / undoSkipPausingTooltip.label collapse the global Deactivate/Activate toggle onto the same strings as the per-breakpoint Disable/Enable commands, making them indistinguishable
- `colorpicker-tooltip-alpha-slider-title` — `devtools/client/inspector.ftl` — 10. Прозрачность for opacity — colorpicker-tooltip-alpha-slider-title and editorinkopacity (see §3.B).
  - Current: `Прозрачность`
- `eventsTooltip.Bubbling` — `devtools/client/inspector.properties` — storage-tree-labels-session-storage-class and eventsTooltip.Capturing vs eventsTooltip.Bubbling (participle vs noun)
- `eventsTooltip.Capturing` — `devtools/client/inspector.properties` — storage-tree-labels-session-storage-class and eventsTooltip.Capturing vs eventsTooltip.Bubbling (participle vs noun)
- `inspector.colorSchemeSimulationLight.tooltip` — `devtools/client/inspector.properties` — inspector.colorSchemeSimulationLight.tooltip / ...Dark.tooltip render "color scheme" as тема (a distinct Firefox concept) and "simulation" as имитация, unlike rule.colorSchemeSimulation.tooltip
  - en-US: `...Dark.tooltip`
- `flexbox.backButtonLabel` — `devtools/client/layout.properties` — flexbox.flexContainer / flexbox.backButtonLabel use Flex-блок where flexbox.noFlexboxeOnThisPage uses Flex-контейнер
- `flexbox.flexContainer` — `devtools/client/layout.properties` — flexbox.flexContainer / flexbox.backButtonLabel use Flex-блок where flexbox.noFlexboxeOnThisPage uses Flex-контейнер
- `flexbox.noFlexboxeOnThisPage` — `devtools/client/layout.properties` — flexbox.flexContainer / flexbox.backButtonLabel use Flex-блок where flexbox.noFlexboxeOnThisPage uses Flex-контейнер
- `layout.toggleGridHighlighter` — `devtools/client/layout.properties` — layout.toggleGridHighlighter is the only place CSS Grid becomes сетка/grade in devtools
  - en-US: `сетка`
- `eyedropper.label` — `devtools/client/menus.properties` — eyedropper.label (menus.properties) uses the term reserved for the colour picker
- `netmonitor.headers.status` — `devtools/client/netmonitor.properties` — webconsole.logsFilterButton.label singular Лог vs plural siblings; netmonitor.headers.status Состояние vs Статус in adjacent labels; netmonitor.toolbar.resetColumns Восстановить колонки vs Сбросить сортировку/столбца; netmonitor.ws.context.copyFrameAsHex breaks the Копировать как X pattern
  - en-US: `Лог`
- `netmonitor.toolbar.resetColumns` — `devtools/client/netmonitor.properties` — webconsole.logsFilterButton.label singular Лог vs plural siblings; netmonitor.headers.status Состояние vs Статус in adjacent labels; netmonitor.toolbar.resetColumns Восстановить колонки vs Сбросить сортировку/столбца; netmonitor.ws.context.copyFrameAsHex breaks the Копировать как X pattern
  - en-US: `Лог`
- `netmonitor.ws.context.copyFrameAsHex` — `devtools/client/netmonitor.properties` — webconsole.logsFilterButton.label singular Лог vs plural siblings; netmonitor.headers.status Состояние vs Статус in adjacent labels; netmonitor.toolbar.resetColumns Восстановить колонки vs Сбросить сортировку/столбца; netmonitor.ws.context.copyFrameAsHex breaks the Копировать как X pattern
  - en-US: `Лог`
- `throttling.profile.description` — `devtools/client/network-throttling.properties` — закачка (colloquial) does not pair with выгрузка
  - Current: `закачка`
  - en-US: `выгрузка`
- `responsive.changeDevicePixelRatio` — `devtools/client/responsive.properties` — responsive.leftAlignViewport / responsive.changeDevicePixelRatio leave viewport Latin while responsive.rotate / responsive.screenshot use окно просмотра
- `responsive.leftAlignViewport` — `devtools/client/responsive.properties` — responsive.leftAlignViewport / responsive.changeDevicePixelRatio leave viewport Latin while responsive.rotate / responsive.screenshot use окно просмотра
- `responsive.rotate` — `devtools/client/responsive.properties` — responsive.leftAlignViewport / responsive.changeDevicePixelRatio leave viewport Latin while responsive.rotate / responsive.screenshot use окно просмотра
- `responsive.screenshot` — `devtools/client/responsive.properties` — responsive.leftAlignViewport / responsive.changeDevicePixelRatio leave viewport Latin while responsive.rotate / responsive.screenshot use окно просмотра
- `storage-tree-labels-session-storage` — `devtools/client/storage.ftl` — storage-tree-labels-session-storage-class and eventsTooltip.Capturing vs eventsTooltip.Bubbling (participle vs noun)
- `toolbox-meatball-menu-splitconsole-label` — `devtools/client/toolbox.ftl` — toolbox-meatball-menu-splitconsole-label / -hideconsole-label use positional wording where toolbox-options.ftl uses разделённая консоль
  - en-US: `-hideconsole-label`
- `toolbox.parentProcessBrowserToolboxTitle` — `devtools/client/toolbox.properties` — toolbox.parentProcessBrowserToolboxTitle-class and options-enable-service-workers-http- (three forms of "Service Workers" in one file)
  - en-US: `options-enable-service-workers-http-`
- `rule.colorSchemeSimulation.tooltip` — `devtools/shared/styleinspector.properties` — inspector.colorSchemeSimulationLight.tooltip / ...Dark.tooltip render "color scheme" as тема (a distinct Firefox concept) and "simulation" as имитация, unlike rule.colorSchemeSimulation.tooltip
  - en-US: `...Dark.tooltip`
- `rule.jumpDeclaration.title` — `devtools/shared/styleinspector.properties` — styleinspector.contextmenu.copyDeclaration and changes.contextmenu.copyDeclaration use декларацию where rule.jumpDeclaration.title uses объявление
- `styleinspector.contextmenu.copyDeclaration` — `devtools/shared/styleinspector.properties` — styleinspector.contextmenu.copyDeclaration and changes.contextmenu.copyDeclaration use декларацию where rule.jumpDeclaration.title uses объявление
- `evaluationNotifcation.noOriginalVariableMapping.msg` — `devtools/shared/webconsole.properties` — evaluationNotifcation.noOriginalVariableMapping.msg and webconsole.input.selector.tooltip use оценка (assessment) where JS evaluation is вычисление everywhere else — the only two occurrences in all of devtools
- `webconsole.input.selector.tooltip` — `devtools/shared/webconsole.properties` — evaluationNotifcation.noOriginalVariableMapping.msg and webconsole.input.selector.tooltip use оценка (assessment) where JS evaluation is вычисление everywhere else — the only two occurrences in all of devtools
- `webconsole.logsFilterButton.label` — `devtools/shared/webconsole.properties` — webconsole.logsFilterButton.label singular Лог vs plural siblings; netmonitor.headers.status Состояние vs Статус in adjacent labels; netmonitor.toolbar.resetColumns Восстановить колонки vs Сбросить сортировку/столбца; netmonitor.ws.context.copyFrameAsHex breaks the Копировать как X pattern
  - en-US: `Лог`
- `webconsole.message.commands.startTracingToProfiler` — `devtools/shared/webconsole.properties` — webconsole.message.commands.startTracingToProfiler names the same panel twice, once English and once transliterated
- `devmgr-button-enable-fips` — `security/manager/security/certificates/deviceManager.ftl` — two metaphors in one dialog
- `devmgr-button-login` — `security/manager/security/certificates/deviceManager.ftl` — two metaphors in one dialog
- `crashreporter-plea` — `toolkit/crashreporter/crashreporter.ftl` — crashreporter-plea отчёт о сбое vs сообщение о падении in the rest of the file and aboutcrashes.ftl
  - en-US: `отчёт о сбое`
- _…and 2 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `community-exp` — `browser/browser/aboutDialog.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
- `pocket-panel-home-most-recent-saves-loading` — `browser/browser/aboutPocket.ftl` — `pocket-panel-home-most-recent-saves-loading` uses three dots where this locale uses …
  - Current: `Загрузка недавних сохранений...`
  - en-US: `…`
  - The tree uses … 463 times against 6 ASCII runs.
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — “default-browser-agent.enabled” and “DisableDefaultBrowserAgent” → « »
  - Current: `“DisableDefaultBrowserAgent”`
  - en-US: `« »`
- `settings-data-backup-in-progress-button` — `browser/browser/backupSettings.ftl` — `settings-data-backup-in-progress-button` uses three dots where this locale uses …
  - Current: `Выполняется резервное копирование...`
  - en-US: `…`
  - The tree uses … 463 times against 6 ASCII runs.
- `contextual-manager-password-login-line-with-alert` — `browser/browser/contextual-manager.ftl` — (предупреждение) lowercase while the origin/username variants capitalize it
- `sidebar-callout-survey-features-question` — `browser/browser/featureCallout.ftl` — same
- `firefoxview-opentabs-bookmarked-pinned-tab` — `browser/browser/firefoxView.ftl` — firefoxview-opentabs-bookmarked-pinned-tab vs -bookmarked-tab — firefoxView.ftl — (закладки) vs (Закладки)
  - en-US: `-bookmarked-tab`
- `genai-settings-chat-lechat-links` — `browser/browser/genai.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
- `ip-protection-not-opted-in-button` — `browser/browser/ipProtection.ftl` — nova-early-access-infobar-primary-button-class: ip-protection-not-opted-in-button and device-migration-fxa-spotlight--primary-button render "Get started" as the noun Начало работы where the siblings use Начать
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `nova-early-access-infobar-primary-button` — `browser/browser/newtab/asrouter.ftl` — nova-early-access-infobar-primary-button-class: ip-protection-not-opted-in-button and device-migration-fxa-spotlight--primary-button render "Get started" as the noun Начало работы where the siblings use Начать
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `newtab-wallpaper-error-max-file-size` — `browser/browser/newtab/newtab.ftl` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
- `newtab-widget-message-copy` — `browser/browser/newtab/newtab.ftl` — same
- `create-backup-screen-1-subtitle` — `browser/browser/newtab/onboarding.ftl` — 1-2 минуты → 1–2 минуты (a numeric range takes an en dash; en-US has 1–2)
  - Current: `1-2 минуты`
  - en-US: `1–2 минуты`
- `multi-profile-spotlight-body` — `browser/browser/newtab/onboarding.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `panic-button-open-new-window` — `browser/browser/panicButton.ftl` — новое чистое Окно → lowercase
  - Current: `новое чистое Окно`
  - en-US: `lowercase`
- `policy-DisableFeedbackCommands` — `browser/browser/policies/policies-descriptions.ftl` — `policy-DisableFeedbackCommands` uses three dots where this locale uses …
  - Current: `Отключает команды отправки отзывов в меню Справка («Отправить отзыв...» и «Сообщить о поддельном сайте...»).`
  - en-US: `…`
  - The tree uses … 463 times against 6 ASCII runs.
- `policy-GenerativeAI` — `browser/browser/policies/policies-descriptions.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `policy-LegacyProfiles` — `browser/browser/policies/policies-descriptions.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `certs-thirdparty-toggle` — `browser/browser/preferences/preferences.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `content-blocking-etp-standard-tcp-title` — `browser/browser/preferences/preferences.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `extension-controlled-enable` — `browser/browser/preferences/preferences.ftl` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `preferences-etp-level-warning-message` — `browser/browser/preferences/preferences.ftl` — ”Устранить проблему с сайтом" — a closing curly quote used as an opener plus an ASCII straight quote as the closer. The only straight-" deviation in translated values in the whole tree.
  - en-US: `.message`
- `security-privacy-issue-warning-ech2` — `browser/browser/preferences/preferences.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `sync-syncing-across-devices-empty-state2` — `browser/browser/preferences/preferences.ftl` — `sync-syncing-across-devices-empty-state2` uses three dots where this locale uses …
  - Current: `Вы ничего не синхронизируете... пока. Запустите синхронизацию, чтобы получить все ваши данные на всех ваших устройствах.`
  - en-US: `…`
  - The tree uses … 463 times against 6 ASCII runs.
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `auto-safe-mode-description` — `browser/browser/safeMode.ftl` — в Безопасном Режиме → в безопасном режиме
  - Current: `в Безопасном Режиме`
  - en-US: `в безопасном режиме`
- `sidebar-history-date-today` — `browser/browser/sidebar.ftl` — sidebar-history-date-today, sidebar-history-date-yesterday (.heading) — sidebar.ftl — ASCII hyphen as the sentence dash
- `sidebar-history-date-yesterday` — `browser/browser/sidebar.ftl` — sidebar-history-date-today, sidebar-history-date-yesterday (.heading) — sidebar.ftl — ASCII hyphen as the sentence dash
- `tabbrowser-tab-label-tab-split-view-right` — `browser/browser/tabbrowser.ftl` — capitalized where the -left pair is lowercase
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — urlbar-translations-button2, urlbar-translations-button-intro (.tooltiptext) — translations.ftl — same
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — urlbar-translations-button2, urlbar-translations-button-intro (.tooltiptext) — translations.ftl — same
- `ERROR_DOWNLOAD_CONT` — `browser/installer/nsisstrings.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `print_progress_percent` — `browser/pdfviewer/viewer.properties` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
- `editorNotificationFooter.noOriginalScopes` — `devtools/client/debugger.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `network-menu-summary-tooltip-load` — `devtools/client/netmonitor.ftl` — network-menu-summary-tooltip-domcontentloaded (.title) and network-menu-summary-tooltip-load (.title) — devtools/client/netmonitor.ftl — “DOMContentLoaded”, “load” → « »
  - Current: `“load”`
  - en-US: `« »`
- `charts.totalSecondsNonBlocking` — `devtools/client/netmonitor.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `netmonitor.timings.handledByServiceWorker` — `devtools/client/netmonitor.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `networkMenu.ws.summary.framesCount2` — `devtools/client/netmonitor.properties` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `throttling.profile.label` — `devtools/client/network-throttling.properties` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
- `perftools-onboarding-message` — `devtools/client/perftools.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
- `toolbox-mode-parent-process-sub-label` — `devtools/client/toolbox.ftl` — (быстро) vs (Медленнее) on the paired label
  - Current: `(быстро)`
  - en-US: `(Медленнее)`
- `inactive-css-no-size-containment-fix` — `devtools/client/tooltips.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
- `webconsole.menu.openInNetworkPanel.label` — `devtools/shared/webconsole.properties` — audio-backend-class stray Title Case: support-remote-experiments-title/-features-title (see §3.J), shortest-paths.header/shortest-paths.select-node (memory.properties, Кратчайшие Пути (от Корней Сборщика Мусора)), ssl-error-sym-key-context-failure/-unwrap-failure and ssl-error-unknown-ca-alert (nsserrors.ftl), pageInfoCertificateTransparencyCompliant (pippki.properties), netmonitor.timings.servic…
  - Current: `Панели Сеть`
  - en-US: `панели «Сеть»`
- `MathML_DeprecatedStixgeneralOperatorStretchingWarning` — `dom/chrome/dom/dom.properties` — `MathML_DeprecatedStixgeneralOperatorStretchingWarning` uses straight double quotes
  - Current: `Поддержка визуализации "stretched" операторов MathML с использованием шрифтов STIXGeneral устарела и может быть удалена в будущем. Для получения сведений о новых шрифтах, поддержка которых будет продолжена, обратитесь к…`
  - en-US: `«stretched»`
  - The locale's quote convention is `guillemet` (1174 occurrences).
- `timer.end` — `mobile/android/chrome/browser.properties` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
- `console-timer-end` — `mobile/android/mobile/android/geckoViewConsole.ftl` — Missing space between number and unit: timer.end (mobile/android/chrome/browser.properties), console-timer-end (geckoViewConsole.ftl), throttling.profile.label (network-throttling.properties — spaced in …description, unspaced here), newtab-wallpaper-error-max-file-size ({ $filesize }МБ), printprogresspercent (browser/pdfviewer/viewer.properties — space added before %), pdfjs-print-progress-percen…
- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — see §3.A (guillemets plus <q>)
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — Locale-only double spaces: community-exp (aboutDialog.ftl), inactive-css-no-size-containment-fix and -fix-1 (tooltips.ftl), rights-intro-point-1 (aboutRights.ftl), settings-pp-not-wanted (toolkit/preferences/preferences.ftl), perftools-onboarding-message (double space after the colon), genai-settings-chat-lechat-links (genai.ftl), languages-code-format (.label, languages.ftl), CSPROTrustedTypesPo…
- `a11y-handler-used` — `toolkit/toolkit/about/aboutSupport.ftl` — обработчик Доступности → lowercase
  - Current: `обработчик Доступности`
  - en-US: `lowercase`
- `blocked-mismatched-version` — `toolkit/toolkit/about/aboutSupport.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `experimental-features-ime-search-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — ASCII hyphen inside the gloss
- `permission-dialog-set-change-app-link` — `toolkit/toolkit/global/handlerDialog.ftl` — Trailing period added or dropped vs en-US: dropped in policy-GenerativeAI, policy-LegacyProfiles, multi-profile-spotlight-body, set-default-menu-message-split-layout-subtitle ([macos]), security-privacy-issue-warning-ech2, blocked-mismatched-version, menu-help-share-ideas (.label, missing the source's ellipsis), permission-dialog-set-change-app-link; added in browsing-use-full-keyboard-navigation…
- `fp-certerror-not-yet-valid-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — Stray space before punctuation: protections-vpn-header-content-subscribed (Apple App Store .), extension-controlled-enable and settings-translations-subpage-never-translate-sites-description (preferences.ftl), fp-certerror-not-yet-valid-why-dangerous-body (certError.ftl), PEAttSelNoBar and PEAttSelUnexpected (css.properties), networkMenu.ws.summary.framesCount2 and charts.totalSecondsNonBlocking…
  - en-US: `Apple App Store .`
- `neterror-load-error-connection` — `toolkit/toolkit/neterror/netError.ftl` — neterror-load-error-connection, neterror-load-error-firewall, neterror-proxy-resolve-failure-firewall — netError.ftl — – (en dash) used as the sentence dash where the tree uses — (163×)
- `neterror-load-error-firewall` — `toolkit/toolkit/neterror/netError.ftl` — neterror-load-error-connection, neterror-load-error-firewall, neterror-proxy-resolve-failure-firewall — netError.ftl — – (en dash) used as the sentence dash where the tree uses — (163×)
- _…and 4 more; see `state/` for the full list._

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Resolved to date (172)

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

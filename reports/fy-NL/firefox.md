# Firefox l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `bd0ff4b2f741` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `60f24d17564f` |
| **Previous run** | 2026-08-21 @ `5cbe42651962` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,131 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fy-NL: [android](android.md)

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
| Files | 360 |
| Strings | 18,131 |
| Missing strings | 49 |
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
| Typography deviations from this locale's own norm | 2 |

### Completeness

**49 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 21
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/preferences/preferences.ftl` — 6
- `browser/browser/aboutPrivateBrowsing.ftl` — 3
- `browser/browser/appmenu.ftl` — 2
- `browser/browser/menubar.ftl` — 2
- `browser/browser/sharePanel.ftl` — 2
- `browser/browser/aboutDialog.ftl` — 1
- `browser/browser/preferences/formAutofill.ftl` — 1
- `dom/chrome/accessibility/AccessFu.properties` — 1
- `toolkit/toolkit/about/aboutProcesses.ftl` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 875, `straight-double` 27, `curly-double` 18 | **curly-single** |
| apostrophe | `typographic` 1645 | **typographic** |
| ellipsis | `char` 461 | **char** |
| dash | `em` 26, `en` 95 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 7 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (588)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 26 |
| 2 | Wrong content (says something other than the English) | 151 |
| 3 | Degraded language (grammar, spelling, terminology) | 253 |
| 4 | Cosmetic (typography, spacing) | 158 |

### A. Functional, markup, variables & plurals

- `error-try-again` — `browser/browser/aboutRobots.ftl` — .label2 left in English while the value is translated
    - Source: `(value): Try Again label2: Please do not press this button again.`
- `about-unloads-last-updated` — `browser/browser/aboutUnloads.ftl` — Left in English: "Last updated: …"
    - Source: `Last updated: { $date }`
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — </a > — stray space inside the closing tag.
    - Source: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
- `cfr-doorhanger-milestone-heading2` — `browser/browser/newtab/asrouter.ftl` — [one] variant has b>{ $blockedCount }</b> — the opening < is missing, so the raw text b> shows. The [other] variant is correct.
    - Current: `[one]`
    - Source: `{$blockedCount ->} [other] { -brand-short-name } blocked over <b>{ $blockedCount }</b> trackers since { $date }!`
- `return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — Both spaces around <img data-l10n-name="icon"/> were dropped: Litte wy no<img …/><b>…</b> ophelje.
    - Source: `Now let’s get you <img data-l10n-name="icon"/> <b>{ $addon-name }</b>.`
- `safeb-blocked-addon-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — Stray trailing </p> with no opening tag; not present in en-US.
    - Source: `{ -brand-short-name } blocked this page because one of your add-ons tried to open it. This site could be used to steal your info — like passwords or credit card numbers.`
- `tabbrowser-empty-private-tab-title` — `browser/browser/tabbrowser.ftl` — Soft hyphen inside privee­ljepblêd. Possibly intentional for line breaking — verify before removing.
    - Source: `New Private Tab`
- `styleeditor-pretty-print-button` — `devtools/client/styleeditor.ftl` — Left in English ("Stylesheet Pretty Print") while both siblings are translated
    - Source: `title: Pretty print style sheet`
- `css-compatibility-default-message` — `devtools/client/tooltips.ftl` — Same stray spaces inside <strong>.
    - Source: `<strong>{ $property }</strong> is not supported in the following browsers:`
- `inactive-css-not-grid-or-flex-container-or-multicol-container` — `devtools/client/tooltips.ftl` — <strong> { $property } </strong> — stray spaces inside the tag; en-US has none.
    - Source: `<strong>{ $property }</strong> has no effect on this element since it’s not a flex container, a grid container, or a multi-column container.`
- `inactive-css-not-grid-or-flex-container-or-multicol-container-fix` — `devtools/client/tooltips.ftl` — CSS keyword garbled: colums:2 → columns:2
    - Current: `colums:2`
    - Source: `Try adding either <strong>display:grid</strong>, <strong>display:flex</strong>, or <strong>columns:2</strong>. { learn-more }`
    - Suggest: `columns:2`
- `inactive-css-not-table-fix` — `devtools/client/tooltips.ftl` — Wrong CSS keyword — see section C
    - Source: `Try adding <strong>display:table</strong> or <strong>display:inline-table</strong>. { learn-more }`
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — CSS property translated inside <strong>: lettertypegrutte → font-size
    - Current: `lettertypegrutte`
    - Source: `Try changing the <strong>font-size</strong> of the ruby text. { learn-more }`
- `addon-badge-line3` — `toolkit/toolkit/about/aboutAddons.ftl` — Comment hard-codes Mozilla so forks don't show "by Fork"; the locale added "Firefox": troch Mozilla Firefox boude útwreiding
    - Source: `aria-label: { addon-badge-line3.title } title: Official extension built by Mozilla. Meets security and performance standards`
- `addon-badge-line4` — `toolkit/toolkit/about/aboutAddons.ftl` — Comment hard-codes Mozilla so forks don't show "by Fork"; the locale added "Firefox": troch Mozilla Firefox boude útwreiding
    - Source: `title: Official extension built by Mozilla. Meets security and performance standards`
- `recommended-theme-1` — `toolkit/toolkit/about/aboutAddons.ftl` — Stray leading space inside the <a data-l10n-name="link"> text — renders as underlined whitespace.
    - Source: `Feeling creative? <a data-l10n-name="link">Build your own theme with Firefox Color.</a>`
- `about-glean-button-dictionary-link` — `toolkit/toolkit/about/aboutGlean.ftl` — Comment: "Docs" = documentation. Dokuminten → Dokumintaasje
    - Current: `Dokuminten`
    - Source: `Docs`
    - Suggest: `Dokumintaasje`
- `app-basics-update-dir` — `toolkit/toolkit/about/aboutSupport.ftl` — Comment says "Update" is a noun. Map fernije → Fernijingsmap (both variants)
    - Current: `Map fernije`
    - Source: `{$sel_1 ->} [linux] Update Directory [other] Update Folder`
    - Suggest: `Fernijingsmap`
- `url-classifier-content-classifier-col-important` — `toolkit/toolkit/about/url-classifier.ftl` — Comment says "Important" must not be translated; currently Wichtich
    - Source: `Important`
- `url-classifier-content-classifier-loading-url` — `toolkit/toolkit/about/url-classifier.ftl` — URL lade (imperative) → Ladende URL (noun label, per comment)
    - Current: `URL lade`
    - Source: `Loading URL`
    - Suggest: `Ladende URL`
- `url-classifier-content-classifier-loading-url-enabled` — `toolkit/toolkit/about/url-classifier.ftl` — Laden fan URL ynskeakelje → Ladende URL ynskeakelje
    - Current: `Laden fan URL ynskeakelje`
    - Source: `Enable loading URL`
    - Suggest: `Ladende URL ynskeakelje`
- `region-name-ne` — `toolkit/toolkit/intl/regionNames.ftl` — Value is Nigeria, identical to region-name-ng. Niger has no correct name in the list. → Niger
    - Source: `Niger`
    - Suggest: `Niger`
- `sec-error-ocsp-bad-signature` — `toolkit/toolkit/neterror/nsserrors.ftl` — OCSP response left in English; the file uses OCSP-antwurd
    - Current: `OCSP response`
    - Source: `OCSP response has an invalid signature.`
- `pdfjs-printing-not-ready` — `toolkit/toolkit/pdfviewer/viewer.ftl` — Warning: left in English
    - Source: `Warning: The PDF is not fully loaded for printing.`
- `pdfjs-printing-not-supported` — `toolkit/toolkit/pdfviewer/viewer.ftl` — Warning: left in English
    - Source: `Warning: Printing is not fully supported by this browser.`
- `printui-paper-jis-b4` — `toolkit/toolkit/printing/printUI.ftl` — Value is JIS-B5 — duplicates printui-paper-jis-b5, so the B4 paper size is unselectable/mislabelled. → JIS-B4
    - Source: `JIS-B4`

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-import-report-page-title` — `browser/browser/aboutLogins.ftl` — Gearfettend rapport ymportearje → Rapport ymportgearfetting
    - Current: `Gearfettend rapport ymportearje`
    - Source: `Import Summary Report`
    - Suggest: `Rapport ymportgearfetting`
- `confirm-discard-changes-dialog-title` — `browser/browser/aboutLogins.ftl` — Dizze wizigingen ferwerpe? → Net-bewarre wizigingen ferwerpe?
    - Current: `Dizze wizigingen ferwerpe?`
    - Source: `Discard unsaved changes?`
    - Suggest: `Net-bewarre wizigingen ferwerpe?`
- `pocket-panel-header-my-saves` — `browser/browser/aboutPocket.ftl` — Myn Opgeslagen items besjen → Myn bewarre items besjen
    - Current: `Myn Opgeslagen items besjen`
    - Source: `View My Saves`
    - Suggest: `Myn bewarre items besjen`
- `pocket-panel-saved-error-no-internet` — `browser/browser/aboutPocket.ftl` — 2nd sentence: Kontrolearje jo ferbining → Meitsje ferbining mei it ynternet
    - Current: `Kontrolearje jo ferbining`
    - Source: `You must be connected to the Internet in order to save to { -pocket-brand-name }. Please connect to the Internet and try again.`
    - Suggest: `Meitsje ferbining mei it ynternet`
- `pocket-panel-saved-removed-updated` — `browser/browser/aboutPocket.ftl` — Opgeslagen items → Bewarre items
    - Current: `Opgeslagen items`
    - Source: `Page Removed from Saves`
    - Suggest: `Bewarre items`
- `restore-page-list-header` — `browser/browser/aboutSessionRestore.ftl` — Skermen en ljepblêden → Finsters en ljepblêden
    - Current: `Skermen en ljepblêden`
    - Source: `label: Windows and Tabs`
    - Suggest: `Finsters en ljepblêden`
- `restore-page-window-label` — `browser/browser/aboutSessionRestore.ftl` — Skerm #{ $windowNumber } → Finster { $windowNumber }
    - Current: `Skerm #{ $windowNumber }`
    - Source: `Window { $windowNumber }`
    - Suggest: `Finster { $windowNumber }`
- `addon-confirm-install-some-unsigned-message` — `browser/browser/addonNotifications.ftl` — Entire string is Dutch: "Waarschuwing: deze website wil … Ga verder op eigen risico."
    - Source: `{$addonCount ->} [other] Caution: This site would like to install { $addonCount } add-ons in { -brand-short-name }, some of which are unverified. Proceed at your own risk.`
- `addon-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — de ferwachte add-on { -brand-short-name } → de add-on dy’t { -brand-short-name } ferwachte
    - Current: `de ferwachte add-on { -brand-short-name }`
    - Source: `The add-on could not be installed because it does not match the add-on { -brand-short-name } expected.`
    - Suggest: `de add-on dy’t { -brand-short-name } ferwachte`
- `addon-local-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — de ferwachte add-on { -brand-short-name } → de add-on dy’t { -brand-short-name } ferwachte
    - Current: `de ferwachte add-on { -brand-short-name }`
    - Source: `This add-on could not be installed because it does not match the add-on { -brand-short-name } expected.`
    - Suggest: `de add-on dy’t { -brand-short-name } ferwachte`
- `appmenu-recently-closed-windows` — `browser/browser/appmenu.ftl` — Koartlyn sluten skermen → … finsters
    - Current: `Koartlyn sluten skermen`
    - Source: `label: Recently closed windows`
    - Suggest: `… finsters`
- `profiler-popup-presets-ml-description` — `browser/browser/appmenu.ftl` — masineoersettingsbugs → masinaal-learenbugs (ML ≠ MT)
    - Current: `masineoersettingsbugs`
    - Source: `Preset for investigating machine learning bugs in { -brand-shorter-name }.`
- `backup-file-how-to-restore-header` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
    - Current: `reparearje`
    - Source: `How to restore:`
    - Suggest: `werstelle`
- `backup-file-title` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
    - Current: `reparearje`
    - Source: `Restore { -brand-short-name }`
    - Suggest: `werstelle`
- `backup-folder-name` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
    - Current: `reparearje`
    - Source: `Restore { -brand-product-name }`
    - Suggest: `werstelle`
- `restore-from-backup-header` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
    - Current: `reparearje`
    - Source: `Restore your data`
    - Suggest: `werstelle`
- `browser-window-restore-down-button` — `browser/browser/browser.ftl` — Omleech opnij ynstelle → Ferlytsje
    - Current: `Omleech opnij ynstelle`
    - Source: `tooltiptext: Restore Down`
    - Suggest: `Ferlytsje`
- `eme-notifications-drm-content-playing` — `browser/browser/browser.ftl` — Relation inverted: as written Firefox is what gets limited. en-US: "…which may limit what { -brand-short-name } can let you do with it."
    - Source: `Some audio or video on this site uses DRM software, which may limit what { -brand-short-name } can let you do with it.`
- `enable-devtools-popup-description2` — `browser/browser/browser.ftl` — it menu Ekstra → it menu Browserhelpmidelen
    - Current: `it menu Ekstra`
    - Source: `To use the F12 shortcut, first open DevTools via the Browser Tools menu.`
    - Suggest: `it menu Browserhelpmidelen`
- `identity-https-only-info-no-upgrade` — `browser/browser/browser.ftl` — HTTP-ferbining net fernije → ferbining net opwurdearje fan HTTP
    - Current: `HTTP-ferbining net fernije`
    - Source: `Unable to upgrade connection from HTTP.`
    - Suggest: `ferbining net opwurdearje fan HTTP`
- `identity-weak-encryption` — `browser/browser/browser.ftl` — swakke befeiliging → swakke fersifering
    - Current: `swakke befeiliging`
    - Source: `This page uses weak encryption.`
    - Suggest: `swakke fersifering`
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — Sykaksjes → Sykje yn aksjes / Aksjes trochsykje ("Search" is a verb)
    - Current: `Sykaksjes`
    - Source: `aria-label: Search actions placeholder: Enter search terms`
    - Suggest: `Sykje yn aksjes`
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — Sykaksjes → Sykje yn aksjes / Aksjes trochsykje ("Search" is a verb)
    - Current: `Sykaksjes`
    - Source: `Search Actions`
    - Suggest: `Sykje yn aksjes`
- `urlbar-search-tips-onboard` — `browser/browser/browser.ftl` — Sykje nei { $engineName } → Sykje mei { $engineName }
    - Current: `Sykje nei { $engineName }`
    - Source: `Type less, find more: Search { $engineName } right from your address bar.`
    - Suggest: `Sykje mei { $engineName }`
- `urlbar-searchmode-no-keyword2` — `browser/browser/browser.ftl` — Sykje nei trefwurden → Sykjen mei trefwurden
    - Current: `Sykje nei trefwurden`
    - Source: `title: Keyword search is disabled`
    - Suggest: `Sykjen mei trefwurden`
- `main-context-menu-stop` — `browser/browser/browserContext.ftl` — Beëinigje → Stopje
    - Current: `Beëinigje`
    - Source: `accesskey: S aria-label: Stop`
    - Suggest: `Stopje`
- `customize-mode-overflow-list-description` — `browser/browser/customizeMode.ftl` — hjirnei ta → hjirhinne
    - Current: `hjirnei ta`
    - Source: `Drag and drop items here to keep them within reach but out of your toolbar…`
    - Suggest: `hjirhinne`
- `customkeys-dev-storage` — `browser/browser/customkeys.ftl` — Unthâld-ynspektor → Opslach-ynspektor
    - Current: `Unthâld-ynspektor`
    - Source: `Storage Inspector`
- `default-browser-guidance-notification-info-page` — `browser/browser/defaultBrowserNotification.ftl` — Toane: → Sjen litte
    - Current: `Toane:`
    - Source: `Show me`
    - Suggest: `Sjen litte`
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — "{ $num } bestanden niet gedownload." — the [one] variant is Frisian
    - Source: `{$num ->} [one] File not downloaded. [other] { $num } files not downloaded.`
- `sidebar-callout-survey-neutral` — `browser/browser/featureCallout.ftl` — Gemiddeld → Neutraal
    - Current: `Gemiddeld`
    - Source: `Neutral`
    - Suggest: `Neutraal`
- `split-dismiss-button-show-fewer-option` — `browser/browser/featureCallout.ftl` — "Mear oanrekommandaasjes toane" — en-US: "Show fewer recommendations"
    - Source: `label: Show fewer recommendations`
- `genai-input-ask-smart-window` — `browser/browser/genai.ftl` — Fragen… → Freegje…
    - Current: `Fragen…`
    - Source: `placeholder: Ask…`
    - Suggest: `Freegje…`
- `genai-menu-ask-smart-window` — `browser/browser/genai.ftl` — Fragen… → Freegje…
    - Current: `Fragen…`
    - Source: `accesskey: z label: Ask…`
    - Suggest: `Freegje…`
- `genai-page-warning` — `browser/browser/genai.ftl` — is dit foar in part de gearfetting → is dit in dielgearfetting
    - Current: `is dit foar in part de gearfetting`
    - Source: `message: Since the page is long, this is a partial summary.`
    - Suggest: `is dit in dielgearfetting`
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — Entire string is Dutch
    - Source: `heading: { $provider } won’t get your full selection message: {$selectionLength ->} [other] You’ve selected about { $selectionLength } characters. The number of characters we can send to { $provider } is about { $maxLen…`
- `genai-shortcuts-selected-warning-generic` — `browser/browser/genai.ftl` — Entire string is Dutch: "U hebt ongeveer … kunnen sturen is ongeveer …" (also has a doubled period geselecteerd..)
    - Source: `heading: AI chatbot won’t get your full selection message: {$selectionLength ->} [other] You’ve selected about { $selectionLength } characters. The number of characters we can send to the AI chatbot is about { $maxLengt…`
- `menu-history-undo-window-menu` — `browser/browser/menubar.ftl` — Koartlyn sluten skermen → … finsters
    - Current: `Koartlyn sluten skermen`
    - Source: `label: Recently Closed Windows`
    - Suggest: `… finsters`
- `fxa-adoption-addresses-backup-subtitle` — `browser/browser/newtab/asrouter.ftl` — "jo bewarre wachtwurden" on the addresses card — en-US: "your saved addresses"
    - Source: `Protect your saved addresses by syncing them to your devices with encryption.`
- `newtab-privacy-message-streak` — `browser/browser/newtab/newtab.ftl` — "op rige" dropped in the singular variant only
    - Source: `{$count ->} [one] You’ve been protected { $count } day in a row. [other] You’ve been protected { $count } days in a row.`
- `newtab-section-following-button` — `browser/browser/newtab/newtab.ftl` — Folgjend ("next") → Folge ("following")
    - Current: `Folgjend`
    - Source: `Following`
    - Suggest: `Folge`
- `newtab-section-unfollow-button-label` — `browser/browser/newtab/newtab.ftl` — Folgjend ("next") → Folge ("following")
    - Current: `Folgjend`
    - Source: `aria-label: Following: Unfollow { $topic }`
    - Suggest: `Folge`
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — foar de hân → by de hân
    - Current: `foar de hân`
    - Source: `Your favorites at your fingertips`
    - Suggest: `by de hân`
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — Mear oerienkomsten lade… → Mear wedstriden lade…
    - Current: `Mear oerienkomsten lade…`
    - Source: `Loading more matches…`
    - Suggest: `Mear wedstriden lade…`
- `newtab-topsites-edit-topsites-header` — `browser/browser/newtab/newtab.ftl` — "Topwebsite tafoegje" — en-US: "Edit Top Site"
    - Source: `Edit Top Site`
- `mr2022-onboarding-pin-private-image-alt` — `browser/browser/newtab/onboarding.ftl` — út in ferskine — the noun hoed is missing
    - Current: `út in ferskine`
    - Source: `aria-label: Magic wand makes { -brand-product-name } private browsing logo appear out of a hat`
    - Suggest: `hoed`
- `onboarding-easy-setup-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — troch in non-profitorganisaasje browser — stipe missing, bedriuwen duplicated
    - Current: `troch in non-profitorganisaasje browser`
    - Source: `Our non-profit backed browser helps stop companies from secretly following you around the web.`
    - Suggest: `stipe`
- `policy-Backup` — `browser/browser/policies/policies-descriptions.ftl` — reparearje → weromsette (restore, not repair)
    - Current: `reparearje`
    - Source: `Disable backup or restore of profile data.`
    - Suggest: `weromsette`
- `policy-DisableSecurityBypass` — `browser/browser/policies/policies-descriptions.ftl` — befeiligingsynstellingen → befeiligingswarskôgingen
    - Current: `befeiligingsynstellingen`
    - Source: `Prevent the user from bypassing certain security warnings.`
    - Suggest: `befeiligingswarskôgingen`
- `policy-OfferToSaveLoginsDefault` — `browser/browser/policies/policies-descriptions.ftl` — Spurious ôftwingje carried over from policy-OfferToSaveLogins
    - Current: `ôftwingje`
    - Source: `Set the default value for allowing { -brand-short-name } to offer to remember saved logins and passwords. Both true and false values are accepted.`
- `containers-icon-briefcase` — `browser/browser/preferences/containers.ftl` — Sammeling → Aktetaske
    - Current: `Sammeling`
    - Source: `label: Briefcase`
    - Suggest: `Aktetaske`
- `permissions-site-microphone-desc` — `browser/browser/preferences/permissions.ftl` — Says "jo kamera" in the microphone dialog — copy-paste from the camera string
    - Source: `The following websites have requested to access your microphone. You can specify which websites are allowed to access your microphone. You can also block new requests asking to access your microphone.`
- `appearance-window-density-touch` — `browser/browser/preferences/preferences.ftl` — lykas klikdoelen → en klikdoelen
    - Current: `lykas klikdoelen`
    - Source: `description: Larger window elements and click targets, optimized for touch screens label: Touch`
    - Suggest: `en klikdoelen`
- `confirm-on-close-multiple-tabs` — `browser/browser/preferences/preferences.ftl` — Warskôgje by → Befêstigje foar
    - Current: `Warskôgje by`
    - Source: `accesskey: m label: Confirm before closing multiple tabs`
    - Suggest: `Befêstigje foar`
- `data-collection-run-studies` — `browser/browser/preferences/preferences.ftl` — in keur oan brûkers → willekeurich brûkers ("randomly" lost)
    - Current: `in keur oan brûkers`
    - Source: `description: { -brand-short-name } randomly selects users to test features, which helps improve quality for everyone. label: Allow { -brand-short-name } to run feature studies`
    - Suggest: `willekeurich brûkers`
- `performance-allow-hw-accel` — `browser/browser/preferences/preferences.ftl` — hardware-acceleratie → hardwarefersnelling
    - Source: `accesskey: r label: Use hardware acceleration when available`
    - Suggest: `hardwarefersnelling`
- `search-one-click-header2` — `browser/browser/preferences/preferences.ftl` — Fluchkeppelingen sykje (imperative) → Sykfluchkeppelingen (noun heading)
    - Current: `Fluchkeppelingen sykje`
    - Source: `Search Shortcuts`
    - Suggest: `Sykfluchkeppelingen`
- `windows-launch-on-login-disabled` — `browser/browser/preferences/preferences.ftl` — Link text Apps → Opstart-apps (Windows "Startup Apps")
    - Current: `Apps`
    - Source: `This preference has been disabled in Windows. To change, visit <a data-l10n-name="startup-link">Startup Apps</a> in System settings.`
- `windows-passkey-settings-label` — `browser/browser/preferences/preferences.ftl` — Wachtwurden beheare → Tagongskaaien beheare (passkeys ≠ passwords)
    - Current: `Wachtwurden beheare`
    - Source: `Manage passkeys in system settings`
    - Suggest: `Tagongskaaien beheare`
- `profiles-pink-theme-title` — `browser/browser/profiles.ftl` — Rôze → Rôs (its own label is Rôs)
    - Current: `Rôze`
    - Source: `title: Apply pink theme`
    - Suggest: `Rôs`
- _…and 91 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `settings-update-unsupported` — `browser/browser/aboutDialog.ftl` — fernijngen → fernijingen
    - Current: `fernijngen`
    - Source: `You can not perform further updates on this system. <a data-l10n-name="unsupported-link">Learn more</a>`
    - Suggest: `fernijingen`
- `update-unsupported` — `browser/browser/aboutDialog.ftl` — fernijngen → fernijingen
    - Current: `fernijngen`
    - Source: `You can not perform further updates on this system. <label data-l10n-name="unsupported-link">Learn more</label>`
    - Suggest: `fernijingen`
- `create-new-login-button` — `browser/browser/aboutLogins.ftl` — Nij oanmelding → Nije oanmelding
    - Current: `Nij oanmelding`
    - Source: `title: Create new login`
    - Suggest: `Nije oanmelding`
- `login-item-new-login-title` — `browser/browser/aboutLogins.ftl` — Nij oanmelding → Nije oanmelding
    - Current: `Nij oanmelding`
    - Source: `Create New Login`
    - Suggest: `Nije oanmelding`
- `login-list-intro-description` — `browser/browser/aboutLogins.ftl` — Wannear jo → Wannear’t jo
    - Current: `Wannear jo`
    - Source: `When you save a password in { -brand-product-name }, it will show up here.`
    - Suggest: `Wannear’t jo`
- `pocket-panel-saved-error-tag-length` — `browser/browser/aboutPocket.ftl` — beheint → beheind
    - Current: `beheint`
    - Source: `Tags are limited to 25 characters`
    - Suggest: `beheind`
- `about-private-browsing-nova-info-subheader2` — `browser/browser/aboutPrivateBrowsing.ftl` — al jo priveefinster → al jo priveefinsters
    - Current: `al jo priveefinster`
    - Source: `We’ll erase every search and sign-in when you close all your Private Windows. { -brand-short-name }’s built-in protections are on here too, like blocking trackers.`
    - Suggest: `al jo priveefinsters`
- `welcome-back-restore-some-label` — `browser/browser/aboutSessionRestore.ftl` — dy’t jo winske (past) → dy’t jo winskje
    - Current: `dy’t jo winske`
    - Source: `Restore only the ones you want`
    - Suggest: `dy’t jo winskje`
- `about-unloads-column-sortweight` — `browser/browser/aboutUnloads.ftl` — ôflaad → ôflaat
    - Current: `ôflaad`
    - Source: `(value): Secondary Weight title: If available, tabs are sorted by this value after being sorted by the base weight. The value derives from tab’s memory usage and the count of processes.`
    - Suggest: `ôflaat`
- `about-unloads-column-weight` — `browser/browser/aboutUnloads.ftl` — alteart → allearst; ôflaad → ôflaat
    - Current: `alteart`
    - Source: `(value): Base Weight title: Tabs are first sorted by this value, which derives from some special attributes such as playing a sound, WebRTC, etc.`
    - Suggest: `allearst`
- `addon-install-full-screen-blocked` — `browser/browser/addonNotifications.ftl` — Add-on-installaasje → Add-on-ynstallaasje
    - Source: `Add-on installation is not allowed while in or before entering fullscreen mode.`
- `aiwindow-starter-browsing-compare` — `browser/browser/aiWindow.ftl` — ljeplêden → ljepblêden
    - Current: `ljeplêden`
    - Source: `Compare tabs`
    - Suggest: `ljepblêden`
- `smartbar-placeholder` — `browser/browser/aiWindow.ftl` — in URL type → in URL typje
    - Current: `in URL type`
    - Source: `placeholder: Ask, search, or type a URL`
    - Suggest: `in URL typje`
- `smart-window-opened-tabs-row-label` — `browser/browser/aiWindowContent.ftl` — ljeplêden → ljepblêden
    - Current: `ljeplêden`
    - Source: `Opened tabs`
    - Suggest: `ljepblêden`
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — Dangling hokker ljepblêden at the end
    - Source: `If you still want to group tabs, choose <strong>Retry</strong> and select which ones in the card that opens.`
- `appmenu-remote-tabs-tabsnotsyncing` — `browser/browser/appmenu.ftl` — ljepblêdsyngroanisaasje → ljepblêdsyngronisaasje
    - Current: `ljepblêdsyngroanisaasje`
    - Source: `Turn on tab syncing to view a list of tabs from your other devices.`
    - Suggest: `ljepblêdsyngronisaasje`
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — Two occurrences of wannear → wannear’t
    - Current: `wannear`
    - Source: `The Default Browser Agent task checks when the default changes from { -brand-short-name } to another browser. If the change happens under suspicious circumstances, it will prompt users to change back to { -brand-short-n…`
    - Suggest: `wannear’t`
- `data-reporting-notification-message` — `browser/browser/browser.ftl` — ferstjoerd → ferstjoert
    - Current: `ferstjoerd`
    - Source: `{ -brand-short-name } automatically sends some data to { -vendor-short-name } so that we can improve your experience.`
    - Suggest: `ferstjoert`
- `identity-https-only-info-turn-off2` — `browser/browser/browser.ftl` — te wurkje → te wurkjen
    - Current: `te wurkje`
    - Source: `If the page seems broken, you may want to turn off HTTPS-Only Mode for this site to reload using insecure HTTP.`
    - Suggest: `te wurkjen`
- `onboarding-aw-finish-setup-button` — `browser/browser/browser.ftl` — Ynstellen { -brand-short-name } → Ynstellen fan { -brand-short-name }
    - Current: `Ynstellen { -brand-short-name }`
    - Source: `label: Finish setup tooltiptext: Finish setting up { -brand-short-name }`
    - Suggest: `Ynstellen fan { -brand-short-name }`
- `activist-colorway-description` — `browser/browser/colorways.ftl` — en lit oaren leauwe → en litte oaren leauwe
    - Current: `en lit oaren leauwe`
    - Source: `You leave the world a better place than you found it and lead others to believe.`
    - Suggest: `en litte oaren leauwe`
- `dreamer-colorway-description` — `browser/browser/colorways.ftl` — Idiom garbled + wrong subject agreement
    - Source: `You believe that fortune favors the bold and inspire others to be brave.`
- `contextual-manager-passwords-remove-all-message` — `browser/browser/contextual-manager.ftl` — wachtwurd dy’t → wachtwurd dat (neuter) in the [one] variants
    - Current: `wachtwurd dy’t`
    - Source: `{$total ->} [1] This will remove your password saved to { -brand-short-name } and any breach alerts. You cannot undo this action. [other] This will remove the passwords saved to { -brand-short-name } and any breach aler…`
    - Suggest: `wachtwurd dat`
- `customize-mode-downloads-button-autohide` — `browser/browser/customizeMode.ftl` — wannear leech → wannear’t dizze leech is
    - Current: `wannear leech`
    - Source: `label: Hide button when empty`
    - Suggest: `wannear’t dizze leech is`
- `default-browser-prompt-message-pin` — `browser/browser/defaultBrowserNotification.ftl` — hantberik → hânberik
    - Current: `hantberik`
    - Source: `Keep { -brand-short-name } at your fingertips — make it your default browser and pin it to your taskbar.`
    - Suggest: `hânberik`
- `bookmarks-toolbar-callout-2b-title` — `browser/browser/featureCallout.ftl` — blêdwizerakbalke → blêdwizerarkbalke
    - Current: `blêdwizerakbalke`
    - Source: `Keep your bookmarks toolbar open?`
    - Suggest: `blêdwizerarkbalke`
- `callout-firefox-view-colorways-subtitle` — `browser/browser/featureCallout.ftl` — it kleur dy’t → it kleur dat (neuter)
    - Current: `it kleur dy’t`
    - Source: `Choose the shade that speaks to you with colorways. Only in { -brand-product-name }.`
    - Suggest: `it kleur dat`
- `sidebar-callout-survey-features-question` — `browser/browser/featureCallout.ftl` — in { -brand-short-name } → yn { -brand-short-name }
    - Current: `in { -brand-short-name }`
    - Source: `The following are potential sidebar features. Which would improve your productivity in { -brand-short-name } the most?`
    - Suggest: `yn { -brand-short-name }`
- `vertical-tabs-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — Doubled fluch
    - Source: `Try our new vertical tabs layout to quickly scan your list of tabs. Early testers report this layout helps them feel more organized. Switch anytime.`
- `vertical-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — list mei ljeppers → list mei ljepblêden
    - Current: `list mei ljeppers`
    - Source: `This layout makes it easy to quickly scan your list of tabs. Plus, you can adjust the width to see more or less of your tab titles.`
    - Suggest: `list mei ljepblêden`
- `windows-10-eos-sync-split-dismiss-button-show-fewer-option` — `browser/browser/featureCallout.ftl` — Minder oanrekommandearre toane → Minder oanrekommandaasjes toane
    - Current: `Minder oanrekommandearre toane`
    - Source: `label: Show fewer recommendations`
    - Suggest: `Minder oanrekommandaasjes toane`
- `windows-10-eos-sync-urgency-subtitle-1` — `browser/browser/featureCallout.ftl` — -ynstelling → -ynstellingen
    - Current: `-ynstelling`
    - Source: `Sync now to keep your { -brand-short-name } bookmarks, passwords, and settings safe and easy to restore.`
    - Suggest: `-ynstellingen`
- `firefox-relay-get-reusable-masks-failed` — `browser/browser/firefoxRelay.ftl` — Stray nij: gjin nij opnij brûkbere maskers
    - Current: `nij`
    - Source: `{ -relay-brand-name } could not find reusable masks. HTTP error code: { $status }.`
    - Suggest: `gjin nij opnij brûkbere maskers`
- `firefoxview-opentabs-header` — `browser/browser/firefoxView.ftl` — ljeplêden → ljepblêden
    - Current: `ljeplêden`
    - Source: `Open tabs`
    - Suggest: `ljepblêden`
- `firefoxview-opentabs-nav` — `browser/browser/firefoxView.ftl` — ljeplêden → ljepblêden
    - Current: `ljeplêden`
    - Source: `(value): Open tabs title: Open tabs`
    - Suggest: `ljepblêden`
- `genai-prompts-proofread` — `browser/browser/genai.ftl` — krekten → krektens
    - Current: `krekten`
    - Source: `label: Proofread value: Please proofread the selection for spelling and grammar errors. Identify any mistakes and provide a corrected version of the text. Maintain the meaning and factual accuracy and output the list of…`
    - Suggest: `krektens`
- `ipprotection-connection-status-blocked-error-description-1` — `browser/browser/ipProtection.ftl` — Comma splits subject from verb
    - Source: `Local laws and restrictions limit where you can use VPN. <a data-l10n-name="learn-more-link">Learn more</a>`
- `ipprotection-connection-status-network-error-description` — `browser/browser/ipProtection.ftl` — dernei → dêrnei
    - Current: `dernei`
    - Source: `Connect to the internet, then try turning VPN on.`
    - Suggest: `dêrnei`
- `ipprotection-locations-subview-recommended-description` — `browser/browser/ipProtection.ftl` — Fyn (imperative) → Fynt
    - Current: `Fyn`
    - Source: `Finds the fastest location`
    - Suggest: `Fynt`
- `menu-application-hide-other` — `browser/browser/menubar.ftl` — Oare ferstopje → Oaren ferstopje
    - Current: `Oare ferstopje`
    - Source: `label: Hide Others`
    - Suggest: `Oaren ferstopje`
- `migration-list-autofill-label` — `browser/browser/migrationWizard.ftl` — gegevens automatysk ynfolje → gegevens foar automatysk ynfoljen
    - Current: `gegevens automatysk ynfolje`
    - Source: `autofill data`
    - Suggest: `gegevens foar automatysk ynfoljen`
- `july-jam-body` — `browser/browser/newtab/asrouter.ftl` — feilich en flugge tagong → feilige en flugge tagong
    - Current: `feilich en flugge tagong`
    - Source: `Every month, { -brand-short-name } blocks an average of 3,000+ trackers per user, giving you safe, speedy access to the good internet.`
    - Suggest: `feilige en flugge tagong`
- `nova-early-access-infobar-title` — `browser/browser/newtab/asrouter.ftl` — úterlik → uterlik (spurious accent)
    - Current: `úterlik`
    - Source: `<strong>{ -brand-product-name } is getting a new look.</strong> You’re previewing an early, unpolished version before the launch later this year.`
    - Suggest: `uterlik`
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — Untfang flugger sneupe → … sneupen
    - Current: `Untfang flugger sneupe`
    - Source: `{$sel_1 ->} [macos] Make it your default and keep it in your Dock. [other] Get faster browsing and automatic privacy protection.`
    - Suggest: `… sneupen`
- `spotlight-public-wifi-vpn-body` — `browser/browser/newtab/asrouter.ftl` — wylst it navigearjen → wylst jo navigearje
    - Current: `wylst it navigearjen`
    - Source: `To hide your location and browsing activity, consider a Virtual Private Network. It will help keep you protected when browsing in public places like airports and coffee shops.`
    - Suggest: `wylst jo navigearje`
- `windows-10-eos-challenger-pin-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — jo it nedich binne → jo it nedich hawwe
    - Current: `jo it nedich binne`
    - Source: `Pin { -brand-shorter-name } to your taskbar so the browser you chose is always there when you need it.`
    - Suggest: `jo it nedich hawwe`
- `newtab-empty-section-topstories` — `browser/browser/newtab/newtab.ftl` — Kin jo net wachtsje? → Kinne jo net wachtsje?
    - Current: `Kin jo net wachtsje?`
    - Source: `You’ve caught up. Check back later for more top stories from { $provider }. Can’t wait? Select a popular topic to find more great stories from around the web.`
    - Suggest: `Kinne jo net wachtsje?`
- `newtab-empty-section-topstories-generic` — `browser/browser/newtab/newtab.ftl` — Kin jo net wachtsje? → Kinne jo net wachtsje?
    - Current: `Kin jo net wachtsje?`
    - Source: `You’ve caught up. Check back later for more stories. Can’t wait? Select a popular topic to find more great stories from around the web.`
    - Suggest: `Kinne jo net wachtsje?`
- `newtab-privacy-message-promo-monitor-1` — `browser/browser/newtab/newtab.ftl` — foar komme → foarkomme
    - Current: `foar komme`
    - Source: `Find out if your personal info shows up in a data breach.`
    - Suggest: `foarkomme`
- `newtab-privacy-message-promo-relay-1` — `browser/browser/newtab/newtab.ftl` — reagistraasjes → registraasjes
    - Current: `reagistraasjes`
    - Source: `Save your real email for people you trust; use an email mask for sign-ups.`
    - Suggest: `registraasjes`
- `newtab-section-unblock-topic` — `browser/browser/newtab/newtab.ftl` — Blokkearring { $topic } opheffe → Blokkearring fan { $topic } opheffe
    - Current: `Blokkearring { $topic } opheffe`
    - Source: `aria-label: Unblock { $topic }`
    - Suggest: `Blokkearring fan { $topic } opheffe`
- `newtab-sports-widget-message-wallpapers-semifinals-body` — `browser/browser/newtab/newtab.ftl` — Meitsje ien dekôr → Meitsje it dekôr
    - Current: `Meitsje ien dekôr`
    - Source: `Set the stage for the World Cup’s biggest matches.`
    - Suggest: `Meitsje it dekôr`
- `newtab-wallpaper-abstract-purple-green` — `browser/browser/newtab/newtab.ftl` — Pears en griene → Pearze en griene
    - Current: `Pears en griene`
    - Source: `Purple and green light gradient`
    - Suggest: `Pearze en griene`
- `newtab-wallpaper-light-landscape` — `browser/browser/newtab/newtab.ftl` — Berch lânskip → Berchlânskip
    - Current: `Berch lânskip`
    - Source: `Blue mist mountain landscape`
    - Suggest: `Berchlânskip`
- `newtab-wallpaper-palm-trees` — `browser/browser/newtab/newtab.ftl` — wylst gouden oere → tidens it gouden oere
    - Current: `wylst gouden oere`
    - Source: `Silhouette of coconut palm trees during golden hour`
    - Suggest: `tidens it gouden oere`
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — meitjse → meitsje (letters transposed)
    - Current: `meitjse`
    - Source: `Upgrading to Windows 11? Let’s back up your { -brand-product-name } data.`
    - Suggest: `meitsje`
- `mr2022-onboarding-colorway-description-activist` — `browser/browser/newtab/onboarding.ftl` — en lit oaren leauwe → en litte oaren leauwe
    - Current: `en lit oaren leauwe`
    - Source: `<b>You are an Activist.</b> You leave the world a better place than you found it and lead others to believe.`
    - Suggest: `en litte oaren leauwe`
- `mr2022-onboarding-colorway-description-dreamer` — `browser/browser/newtab/onboarding.ftl` — Verb agrees with gelok instead of Jo
    - Current: `gelok`
    - Source: `<b>You are a Dreamer.</b> You believe that fortune favors the bold and inspire others to be brave.`
    - Suggest: `Jo`
- `mr2022-upgrade-onboarding-pin-private-window-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — fêst meitsje → fêstmeitsje
    - Current: `fêst meitsje`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } private browsing in Dock [other] Pin { -brand-short-name } private browsing to taskbar`
    - Suggest: `fêstmeitsje`
- `onboarding-new-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — sybalkeynstellingen → sidebalkeynstellingen
    - Current: `sybalkeynstellingen`
    - Source: `Switch it up whenever you want in the sidebar settings.`
    - Suggest: `sidebalkeynstellingen`
- _…and 177 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `navbar-home` — `browser/browser/browser.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `label: Home tooltiptext: { -brand-short-name } Home Page`
    - Suggest: `Begjinside`
- `quickactions-cmd-manageai` — `browser/browser/browser.ftl` — Also: quickactions-cmd-manageai (browser/browser/browser.ftl) lists ai útskeakelje, ai útskeakelje, ai beheare — the first keyword is duplicated, so one of en-US's three search keywords ("off ai") is unreachable.
    - Source: `disable ai, off ai, manage ai`
- `more-from-moz-solo-description` — `browser/browser/preferences/moreFromMozilla.ftl` — Free (gratis) — fergees / fergese / fergeze: more-from-moz-firefox-relay-description, more-from-moz-mozilla-monitor-card, more-from-moz-solo-description (moreFromMozilla.ftl); newtab-privacy-message-promo-relay-2, -relay-3, -monitor-2 (newtab.ftl); relay-50-masks-announcement-subtitle (asrouter.ftl).
    - Current: `fergees`
    - Source: `Create your website instantly and connect your own custom domain for free.`
    - Suggest: `fergese`
- `home-homepage-title` — `browser/browser/preferences/preferences.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `label: Homepage`
    - Suggest: `Begjinside`
- `permissions-block-popups-exceptions-button4` — `browser/browser/preferences/preferences.ftl` — Third-party redirects — three renderings: permissions-block-popups-exceptions-button4.description (trochliedingen), permissions-block-popups2 (omliedingen), permissions.ftl (trochferwizingen).
    - Source: `accesskey: E description: Add websites that can open pop-ups and use third-party redirects. label: Manage exceptions searchkeywords: popups`
    - Suggest: `trochliedingen`
- `permissions-block-popups2` — `browser/browser/preferences/preferences.ftl` — Third-party redirects — three renderings: permissions-block-popups-exceptions-button4.description (trochliedingen), permissions-block-popups2 (omliedingen), permissions.ftl (trochferwizingen).
    - Source: `accesskey: B label: Block pop-ups and third-party redirects`
    - Suggest: `trochliedingen`
- `preferences-doh-overview-custom` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
    - Current: `Feilige DNS`
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior. label: Custom`
    - Suggest: `Befeilige DNS`
- `preferences-doh-overview-default` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
    - Current: `Feilige DNS`
    - Source: `description: Use secure DNS in regions where it’s available. label: Default protection`
    - Suggest: `Befeilige DNS`
- `preferences-doh-radio-custom` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
    - Current: `Feilige DNS`
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior label: Custom`
    - Suggest: `Befeilige DNS`
- `preferences-doh-radio-default` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
    - Current: `Feilige DNS`
    - Source: `description: Use secure DNS in regions where it’s available label: Default`
    - Suggest: `Befeilige DNS`
- `preferences-web-appearance-choice-light2` — `browser/browser/preferences/preferences.ftl` — Appearance — útstrieling vs uterlik: preferences-web-appearance-choice-light2, -dark2, -tooltip-light, -tooltip-dark.
    - Current: `útstrieling`
    - Source: `label: Light title: Use a light appearance for website backgrounds and content.`
    - Suggest: `uterlik`
- `search-show-suggestions-url-bar-option` — `browser/browser/preferences/preferences.ftl` — Search suggestions — sykfoarstellen vs syksuggestjes: search-show-suggestions-option, search-suggestions-option, search-show-suggestions-url-bar-option, addressbar-locbar-showtrendingsuggestions-option.
    - Current: `sykfoarstellen`
    - Source: `accesskey: l label: Show search suggestions in address bar results`
    - Suggest: `syksuggestjes`
- `search-suggestions-option` — `browser/browser/preferences/preferences.ftl` — Search suggestions — sykfoarstellen vs syksuggestjes: search-show-suggestions-option, search-suggestions-option, search-show-suggestions-url-bar-option, addressbar-locbar-showtrendingsuggestions-option.
    - Current: `sykfoarstellen`
    - Source: `accesskey: s label: Provide search suggestions`
    - Suggest: `syksuggestjes`
- `security-privacy-issue-warning-doh` — `browser/browser/preferences/preferences.ftl` — Network provider — netwurkbehearder (administrator) vs ynternetoanbieder: security-privacy-issue-warning-doh, security-privacy-issue-warning-ech (vs their -doh2/-ech2 variants).
    - Current: `netwurkbehearder`
    - Source: `description: DNS over HTTPS hides what sites you visit from your network provider. label: DNS over HTTPS is disabled`
    - Suggest: `ynternetoanbieder`
- `security-privacy-issue-warning-ech` — `browser/browser/preferences/preferences.ftl` — Network provider — netwurkbehearder (administrator) vs ynternetoanbieder: security-privacy-issue-warning-doh, security-privacy-issue-warning-ech (vs their -doh2/-ech2 variants).
    - Current: `netwurkbehearder`
    - Source: `description: Encrypted Client Hello hides what sites you visit from your network provider. label: Encrypted Client Hello is disabled`
    - Suggest: `ynternetoanbieder`
- `addon-detail-homepage-label` — `toolkit/toolkit/about/aboutAddons.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `Homepage`
    - Suggest: `Begjinside`

### E. Typography, punctuation & spacing

- `aboutdialog-update-downloading` — `browser/browser/aboutDialog.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
    - Source: `Downloading update — <label data-l10n-name="download-status">{ $transfer }</label>`
- `settings-update-downloading` — `browser/browser/aboutDialog.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
    - Source: `<img data-l10n-name="icon"/>Downloading update — <label data-l10n-name="download-status">{ $transfer }</label>`
- `about-logins-import-report-description2` — `browser/browser/aboutLogins.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Passwords imported to { -brand-short-name }.`
- `about-logins-import-report-error` — `browser/browser/aboutLogins.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `{$count ->} [other] <div data-l10n-name="count">{ $count }</div> <div data-l10n-name="details">Errors</div> <div data-l10n-name="not-imported">(not imported)</div>`
- `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Select the plus sign button above to add a password now. You can also <a data-l10n-name="import-browser-link">import passwords from another browser</a> or <a data-l10n-name="import-file-link">from a file</a>.`
- `appmenuitem-monitor-description2` — `browser/browser/appmenu.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Get alerts about data breaches`
- `fxa-menu-sync-status-off` — `browser/browser/appmenu.ftl` — fxa-menu-sync-status-off (Syngronisaasje is Ut → … is út) · add-exception-expired-short (Alde Ynformaasje) · menu-tools-extensions-and-themes (Utwreidingen en Tema’s) · skip-troubleshoot-refresh-profile (sentence starts lowercase).
    - Current: `Syngronisaasje is Ut`
    - Source: `Sync is Off`
    - Suggest: `… is út`
- `profiler-popup-presets-networking-with-logs-description` — `browser/browser/appmenu.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Preset for investigating networking bugs in { -brand-shorter-name }, including networking logs. These logs may contain sensitive information such as the URLs you visit.`
- `filepicker-blocked-infobar` — `browser/browser/browser.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Your organization has blocked access to local files on this computer`
- `popup-show-popup-menuitem` — `browser/browser/browser.ftl` — rights-webservices-term-4 ("as-is") · protections-vpn-banner-content (TechRadar quote in "…") · popup-show-popup-menuitem.label (uses “…” where the adjacent popup-trigger-redirect-menuitem uses ‘…’).
    - Source: `label: Show “{ $popupURI }”`
    - Suggest: `"as-is"`
- `popup-trigger-redirect-menuitem` — `browser/browser/browser.ftl` — rights-webservices-term-4 ("as-is") · protections-vpn-banner-content (TechRadar quote in "…") · popup-show-popup-menuitem.label (uses “…” where the adjacent popup-trigger-redirect-menuitem uses ‘…’).
    - Source: `label: Show “{ $redirectURI }”`
    - Suggest: `"as-is"`
- `quickactions-plugins` — `browser/browser/browser.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
    - Source: `Manage plugins`
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `{$popupCount ->} [0] { -brand-short-name } prevented this site from redirecting. [1] { -brand-short-name } prevented this site from opening a pop-up window and redirecting. [other] { -brand-short-name } prevented this s…`
- `main-context-menu-bookmark-page` — `browser/browser/browserContext.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
    - Source: `accesskey: m aria-label: Bookmark Page… tooltiptext: Bookmark page`
- `main-context-menu-edit-bookmark` — `browser/browser/browserContext.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
    - Source: `accesskey: m aria-label: Edit Bookmark… tooltiptext: Edit bookmark`
- `default-browser-guidance-notification-info-page` — `browser/browser/defaultBrowserNotification.ftl` — Added: import-source-page-title · findbar-fast-find-links.placeholder · app-basics-disk-available · detail-rating.value · default-browser-guidance-notification-info-page · inactive-css-at-position-try-not-supported.
    - Source: `Show me`
- `bookmark-overlay-tags-empty-description` — `browser/browser/editBookmarkOverlay.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `placeholder: Separate tags with commas`
- `sidebar-customization-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `The { -brand-product-name } sidebar gives you quick access to your browsing history, tabs from other devices, and an AI chatbot — all without leaving your main view.`
- `splitview-onboarding-callout-subtitle-2` — `browser/browser/featureCallout.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `No extra windows. No tab flipping. Right-click this tab and choose “Add Split View.”`
- `firefox-relay-and-fxa-popup-notification-second-sentence-with-domain-and-value-prop` — `browser/browser/firefoxRelay.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `First, sign up or sign in to your account to use an email mask.`
- `firefoxview-tabpickup-description` — `browser/browser/firefoxView.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Open pages from other devices.`
- `genai-chatbot-summarize-footer-generic-subtitle` — `browser/browser/genai.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Add an AI chatbot to the { -brand-short-name } sidebar to quickly summarize pages.`
- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `description: Get extra privacy by hiding your location while browsing. label: Built-in VPN`
- `ipprotection-feature-introduction-link-text-privacy-3` — `browser/browser/ipProtection.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Get <a data-l10n-name="learn-more-vpn">extra privacy</a> by choosing from multiple locations to hide where you browse.`
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — ipprotection-locations-subview-promo.message (mear as300) · support-remote-experiments-see-about-studies (missing space before the placeable) · about-logging-unknown-error (bard :) · download-ui-confirm-quit-cancel-downloads-mac (stopje ,) · about-httpsonly-explanation-continue (útskeakele .) · experimental-features-custom-wallpaper-description (Nij-ljepblêdside .) · plus the 47 doubled-space str…
    - Source: `heading: Take protection further with { -mozilla-vpn-brand-name } message: Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `mear as300`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `heading: Getting close to your VPN limit message: You have { $usageLeft } GB of { $maxUsage } GB left this month.`
- `ipprotection-site-settings-callout-subtitle` — `browser/browser/ipProtection.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Turn VPN off for a specific site and we’ll remember it next time you visit.`
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `accesskey: S label: Share Ideas and Feedback…`
- `import-source-page-title` — `browser/browser/migration.ftl` — Added: import-source-page-title · findbar-fast-find-links.placeholder · app-basics-disk-available · detail-rating.value · default-browser-guidance-notification-info-page · inactive-css-at-position-try-not-supported.
    - Source: `Import Settings and Data`
- `migration-chrome-windows-password-import-step1` — `browser/browser/migrationWizard.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Open the main menu <img data-l10n-name="chrome-icon-3dots"/> and go to Passwords and Autofill > Google Password Manager.`
- `migration-safari-password-import-step2` — `browser/browser/migrationWizard.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Select the <img data-l10n-name="safari-icon-3dots"/> button and choose “Export All Passwords”`
- `firefoxview-spotlight-promo-primarybutton` — `browser/browser/newtab/asrouter.ftl` — places-locked-prompt · protections-panel-cross-site-tracking-cookies · screenshots-generic-error-title · tabbrowser-confirm-caretbrowsing-message · security-browsing-protection · firefoxview-spotlight-promo-primarybutton · fxa-menu-message-sync-devices-secondary-text2 · mr2022-onboarding-pin-image-alt.aria-label · safeb-blocked-unwanted-page-title · about-debugging-setup-intro · webauthn-register…
    - Source: `See how it works`
- `fxa-menu-message-sync-devices-secondary-text2` — `browser/browser/newtab/asrouter.ftl` — places-locked-prompt · protections-panel-cross-site-tracking-cookies · screenshots-generic-error-title · tabbrowser-confirm-caretbrowsing-message · security-browsing-protection · firefoxview-spotlight-promo-primarybutton · fxa-menu-message-sync-devices-secondary-text2 · mr2022-onboarding-pin-image-alt.aria-label · safeb-blocked-unwanted-page-title · about-debugging-setup-intro · webauthn-register…
    - Source: `Instantly get your bookmarks, passwords, and more — everywhere you’re signed in to { -brand-short-name }.`
- `home-mode-choice-custom-srd` — `browser/browser/newtab/newtab.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `label: Custom URLs…`
- `newtab-label-source-read-time` — `browser/browser/newtab/newtab.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `{ $source } · { $timeToRead } min`
- `newtab-widget-lists-menu-delete` — `browser/browser/newtab/newtab.ftl` — website-remove-language-button.aria-label and .title (en-US: "Remove { $locale }") · newtab-widget-lists-menu-delete (en-US: "Delete this list") · delete-ca-cert-confirm (en-US is declarative).
    - Source: `Delete this list`
    - Suggest: `.title`
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Upgrading to Windows 11? Let’s back up your { -brand-product-name } data.`
- `mr1-onboarding-theme-description-dark` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `aria-description: Use a dark theme for buttons, menus, and windows.`
    - Suggest: `‘Root Certs‘`
- `mr1-onboarding-theme-description-light` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `aria-description: Use a light theme for buttons, menus, and windows.`
    - Suggest: `‘Root Certs‘`
- `mr1-onboarding-theme-tooltip-dark` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `title: Use a dark theme for buttons, menus, and windows.`
    - Suggest: `‘Root Certs‘`
- `mr1-onboarding-theme-tooltip-light` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
    - Source: `title: Use a light theme for buttons, menus, and windows.`
    - Suggest: `‘Root Certs‘`
- `mr2022-onboarding-pin-image-alt` — `browser/browser/newtab/onboarding.ftl` — places-locked-prompt · protections-panel-cross-site-tracking-cookies · screenshots-generic-error-title · tabbrowser-confirm-caretbrowsing-message · security-browsing-protection · firefoxview-spotlight-promo-primarybutton · fxa-menu-message-sync-devices-secondary-text2 · mr2022-onboarding-pin-image-alt.aria-label · safeb-blocked-unwanted-page-title · about-debugging-setup-intro · webauthn-register…
    - Source: `aria-label: Person working on a laptop surrounded by stars and flowers`
- `onboarding-gratitude-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Thank you for using { -brand-short-name }, backed by the Mozilla Foundation. With your support, we’re working to make the internet safer and more accessible for everyone.`
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
- `onboarding-refresh-import-title` — `browser/browser/newtab/onboarding.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Make { -brand-short-name } feel more like home`
- `no-page-title` — `browser/browser/pageInfo.ftl` — Dropped: no-page-title.value.
    - Source: `value: Untitled Page:`
- `page-info-frame` — `browser/browser/pageInfo.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
    - Source: `title: Frame Info — { $website }`
- `page-info-page` — `browser/browser/pageInfo.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
    - Source: `title: Page Info — { $website }`
- `places-locked-prompt` — `browser/browser/places.ftl` — places-locked-prompt · protections-panel-cross-site-tracking-cookies · screenshots-generic-error-title · tabbrowser-confirm-caretbrowsing-message · security-browsing-protection · firefoxview-spotlight-promo-primarybutton · fxa-menu-message-sync-devices-secondary-text2 · mr2022-onboarding-pin-image-alt.aria-label · safeb-blocked-unwanted-page-title · about-debugging-setup-intro · webauthn-register…
    - Source: `The bookmarks and history system will not be functional because one of { -brand-short-name }’s files is in use by another application. Some security software can cause this problem.`
- `policy-DefaultDownloadDirectory` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Set the default download directory.`
- `policy-DisableThirdPartyModuleBlocking` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Prevent the user from blocking third-party modules that get injected into the { -brand-short-name } process.`
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Configure default application handlers.`
- `policy-LegacyProfiles` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Disable the feature enforcing a separate profile for each installation.`
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `2. Go to the menu (<img data-l10n-name="ios-menu-icon"/> on iOS or <img data-l10n-name="android-menu-icon"/> on Android) and tap <strong>Sync and save data</strong>`
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `label: { $locale } [{ $code }]`
- `choose-language-description` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Choose your preferred language for displaying pages`
- `confirm-browser-language-change-description` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Restart { -brand-short-name } to apply these changes`
- `download-always-ask-where2` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `accesskey: A label: Ask where to save files before downloading`
- `extension-controlled-enable` — `browser/browser/preferences/preferences.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `To enable the extension go to <img data-l10n-name="addons-icon"/> Add-ons in the <img data-l10n-name="menu-icon"/> menu.`
- `forms-master-pw-change` — `browser/browser/preferences/preferences.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `accesskey: M label: Change Master Password…`
- _…and 98 more; see `state/` for the full list._

---

## 4. Appendix

### Dismissed by hand (4)

- `expand-sidebar-on-hover` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `sidebar-context-menu-unpin-extension` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `sidebar-open-tools-from-sidebar` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `sidebar-resize-splitter` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)

_One line each in `locales/fy-NL/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — raised by `legacy`, withdrawn 2026-08-20

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (245)

- `shortcuts-remove-button` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-08-21
- `aboutdialog-update-downloading` — `browser/browser/aboutDialog.ftl` — fixed 2026-08-11
- `helpus-referrals` — `browser/browser/aboutDialog.ftl` — fixed 2026-08-11
- `about-logins-export-password-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-11
- `about-logins-import-dialog-items-modified2` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-11
- `about-logins-import-report-row-description-modified2` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-11
- `about-logins-intro-import2` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-11
- `restore-page-restore-header` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-08-11
- `restore-page-tab-title` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-08-11
- `restore-page-try-again-button` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-08-11
- `crashed-comment` — `browser/browser/aboutTabCrashed.ftl` — fixed 2026-08-11
- `addon-install-error-not-signed` — `browser/browser/addonNotifications.ftl` — fixed 2026-08-11
- `aiwindow-feedback-add-details` — `browser/browser/aiWindow.ftl` — fixed 2026-08-11
- `smartbar-placeholder-hint-1` — `browser/browser/aiWindow.ftl` — fixed 2026-08-11
- `appmenu-update-other-instance` — `browser/browser/appMenuNotifications.ftl` — fixed 2026-08-11
- `appmenu-bookmarks-sync-promo-connectdevice` — `browser/browser/appmenu.ftl` — fixed 2026-08-11
- `profiler-popup-presets-networking-description` — `browser/browser/appmenu.ftl` — fixed 2026-08-11
- `backup-file-header` — `browser/browser/backupSettings.ftl` — fixed 2026-08-11
- `backup-file-other-browser-restore-step-2` — `browser/browser/backupSettings.ftl` — fixed 2026-08-11
- `qrcode-save-filename-base` — `browser/browser/browser.ftl` — fixed 2026-08-11
- `qrcode-save-filename-with-domain-base` — `browser/browser/browser.ftl` — fixed 2026-08-11
- `quickactions-cmd-labs` — `browser/browser/browser.ftl` — fixed 2026-08-11
- `toolbar-button-open-file` — `browser/browser/browser.ftl` — fixed 2026-08-11
- `toolbar-button-save-page` — `browser/browser/browser.ftl` — fixed 2026-08-11
- `unified-extensions-button-blocklisted` — `browser/browser/browser.ftl` — fixed 2026-08-11
- `urlbar-screen-blocked` — `browser/browser/browser.ftl` — fixed 2026-08-11
- `main-context-menu-frame-add-bookmark` — `browser/browser/browserContext.ftl` — fixed 2026-08-11
- `main-context-menu-video-save-as` — `browser/browser/browserContext.ftl` — fixed 2026-08-11
- `contextual-manager-passwords-breached-origin-link-message` — `browser/browser/contextual-manager.ftl` — fixed 2026-08-11
- `customkeys-conflict-confirm-title` — `browser/browser/customkeys.ftl` — fixed 2026-08-11
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — fixed 2026-08-11
- `customkeys-shortcut-input` — `browser/browser/customkeys.ftl` — fixed 2026-08-11
- `customkeys-shortcut-unassigned` — `browser/browser/customkeys.ftl` — fixed 2026-08-11
- `sidebar-customization-callout-callout-button` — `browser/browser/featureCallout.ftl` — fixed 2026-08-11
- `genai-onboarding-description` — `browser/browser/genai.ftl` — fixed 2026-08-11
- `genai-prompts-summarize` — `browser/browser/genai.ftl` — fixed 2026-08-11
- `link-preview-first-time-setup-message` — `browser/browser/genai.ftl` — fixed 2026-08-11
- `menu-history-restore-last-session` — `browser/browser/menubar.ftl` — fixed 2026-08-11
- `menu-tools-extensions-and-themes` — `browser/browser/menubar.ftl` — fixed 2026-08-11
- `menu-tools-extensions-and-themes` — `browser/browser/menubar.ftl` — fixed 2026-08-11

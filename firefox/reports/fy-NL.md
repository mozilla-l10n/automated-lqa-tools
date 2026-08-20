# Firefox l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `443328fa7930` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `443328fa7930` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,131 |

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
| Strings | 18,131 |
| Missing strings | 32 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

**32 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 15
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/preferences/preferences.ftl` — 4
- `browser/browser/aboutPrivateBrowsing.ftl` — 3
- `toolkit/toolkit/about/aboutProcesses.ftl` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1
- `toolkit/toolkit/global/processTypes.ftl` — 1

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

## 3. Open findings (593)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 27 |
| 2 | Wrong content (says something other than the English) | 151 |
| 3 | Degraded language (grammar, spelling, terminology) | 257 |
| 4 | Cosmetic (typography, spacing) | 158 |

### A. Functional, markup, variables & plurals

- `error-try-again` — `browser/browser/aboutRobots.ftl` — .label2 left in English while the value is translated
- `about-unloads-last-updated` — `browser/browser/aboutUnloads.ftl` — Left in English: "Last updated: …"
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — </a > — stray space inside the closing tag.
- `cfr-doorhanger-milestone-heading2` — `browser/browser/newtab/asrouter.ftl` — [one] variant has b>{ $blockedCount }</b> — the opening < is missing, so the raw text b> shows. The [other] variant is correct.
  - Current: `[one]`
- `return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — Both spaces around <img data-l10n-name="icon"/> were dropped: Litte wy no<img …/><b>…</b> ophelje.
- `safeb-blocked-addon-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — Stray trailing </p> with no opening tag; not present in en-US.
- `tabbrowser-empty-private-tab-title` — `browser/browser/tabbrowser.ftl` — Soft hyphen inside privee­ljepblêd. Possibly intentional for line breaking — verify before removing.
- `styleeditor-pretty-print-button` — `devtools/client/styleeditor.ftl` — Left in English ("Stylesheet Pretty Print") while both siblings are translated
- `css-compatibility-default-message` — `devtools/client/tooltips.ftl` — Same stray spaces inside <strong>.
- `inactive-css-not-grid-or-flex-container-or-multicol-container` — `devtools/client/tooltips.ftl` — <strong> { $property } </strong> — stray spaces inside the tag; en-US has none.
- `inactive-css-not-grid-or-flex-container-or-multicol-container-fix` — `devtools/client/tooltips.ftl` — CSS keyword garbled: colums:2 → columns:2
  - Current: `colums:2`
  - en-US: `columns:2`
- `inactive-css-not-table-fix` — `devtools/client/tooltips.ftl` — Wrong CSS keyword — see section C
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — CSS property translated inside <strong>: lettertypegrutte → font-size
  - Current: `lettertypegrutte`
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — Literal argument name garbled: URLSTRING → URLSTRING
  - Current: `URLSTRING`
- `addon-badge-line3` — `toolkit/toolkit/about/aboutAddons.ftl` — Comment hard-codes Mozilla so forks don't show "by Fork"; the locale added "Firefox": troch Mozilla Firefox boude útwreiding
- `addon-badge-line4` — `toolkit/toolkit/about/aboutAddons.ftl` — Comment hard-codes Mozilla so forks don't show "by Fork"; the locale added "Firefox": troch Mozilla Firefox boude útwreiding
- `recommended-theme-1` — `toolkit/toolkit/about/aboutAddons.ftl` — Stray leading space inside the <a data-l10n-name="link"> text — renders as underlined whitespace.
- `about-glean-button-dictionary-link` — `toolkit/toolkit/about/aboutGlean.ftl` — Comment: "Docs" = documentation. Dokuminten → Dokumintaasje
  - Current: `Dokuminten`
  - en-US: `Dokumintaasje`
- `app-basics-update-dir` — `toolkit/toolkit/about/aboutSupport.ftl` — Comment says "Update" is a noun. Map fernije → Fernijingsmap (both variants)
  - Current: `Map fernije`
  - en-US: `Fernijingsmap`
- `url-classifier-content-classifier-col-important` — `toolkit/toolkit/about/url-classifier.ftl` — Comment says "Important" must not be translated; currently Wichtich
- `url-classifier-content-classifier-loading-url` — `toolkit/toolkit/about/url-classifier.ftl` — URL lade (imperative) → Ladende URL (noun label, per comment)
  - Current: `URL lade`
  - en-US: `Ladende URL`
- `url-classifier-content-classifier-loading-url-enabled` — `toolkit/toolkit/about/url-classifier.ftl` — Laden fan URL ynskeakelje → Ladende URL ynskeakelje
  - Current: `Laden fan URL ynskeakelje`
  - en-US: `Ladende URL ynskeakelje`
- `region-name-ne` — `toolkit/toolkit/intl/regionNames.ftl` — Value is Nigeria, identical to region-name-ng. Niger has no correct name in the list. → Niger
  - en-US: `Niger`
- `sec-error-ocsp-bad-signature` — `toolkit/toolkit/neterror/nsserrors.ftl` — OCSP response left in English; the file uses OCSP-antwurd
  - Current: `OCSP response`
- `pdfjs-printing-not-ready` — `toolkit/toolkit/pdfviewer/viewer.ftl` — Warning: left in English
- `pdfjs-printing-not-supported` — `toolkit/toolkit/pdfviewer/viewer.ftl` — Warning: left in English
- `printui-paper-jis-b4` — `toolkit/toolkit/printing/printUI.ftl` — Value is JIS-B5 — duplicates printui-paper-jis-b5, so the B4 paper size is unselectable/mislabelled. → JIS-B4

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-import-report-page-title` — `browser/browser/aboutLogins.ftl` — Gearfettend rapport ymportearje → Rapport ymportgearfetting
  - Current: `Gearfettend rapport ymportearje`
  - en-US: `Rapport ymportgearfetting`
- `confirm-discard-changes-dialog-title` — `browser/browser/aboutLogins.ftl` — Dizze wizigingen ferwerpe? → Net-bewarre wizigingen ferwerpe?
  - Current: `Dizze wizigingen ferwerpe?`
  - en-US: `Net-bewarre wizigingen ferwerpe?`
- `pocket-panel-header-my-saves` — `browser/browser/aboutPocket.ftl` — Myn Opgeslagen items besjen → Myn bewarre items besjen
  - Current: `Myn Opgeslagen items besjen`
  - en-US: `Myn bewarre items besjen`
- `pocket-panel-saved-error-no-internet` — `browser/browser/aboutPocket.ftl` — 2nd sentence: Kontrolearje jo ferbining → Meitsje ferbining mei it ynternet
  - Current: `Kontrolearje jo ferbining`
  - en-US: `Meitsje ferbining mei it ynternet`
- `pocket-panel-saved-removed-updated` — `browser/browser/aboutPocket.ftl` — Opgeslagen items → Bewarre items
  - Current: `Opgeslagen items`
  - en-US: `Bewarre items`
- `restore-page-list-header` — `browser/browser/aboutSessionRestore.ftl` — Skermen en ljepblêden → Finsters en ljepblêden
  - Current: `Skermen en ljepblêden`
  - en-US: `Finsters en ljepblêden`
- `restore-page-window-label` — `browser/browser/aboutSessionRestore.ftl` — Skerm #{ $windowNumber } → Finster { $windowNumber }
  - Current: `Skerm #{ $windowNumber }`
  - en-US: `Finster { $windowNumber }`
- `addon-confirm-install-some-unsigned-message` — `browser/browser/addonNotifications.ftl` — Entire string is Dutch: "Waarschuwing: deze website wil … Ga verder op eigen risico."
- `addon-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — de ferwachte add-on { -brand-short-name } → de add-on dy’t { -brand-short-name } ferwachte
  - Current: `de ferwachte add-on { -brand-short-name }`
  - en-US: `de add-on dy’t { -brand-short-name } ferwachte`
- `addon-local-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — de ferwachte add-on { -brand-short-name } → de add-on dy’t { -brand-short-name } ferwachte
  - Current: `de ferwachte add-on { -brand-short-name }`
  - en-US: `de add-on dy’t { -brand-short-name } ferwachte`
- `appmenu-recently-closed-windows` — `browser/browser/appmenu.ftl` — Koartlyn sluten skermen → … finsters
  - Current: `Koartlyn sluten skermen`
  - en-US: `… finsters`
- `profiler-popup-presets-ml-description` — `browser/browser/appmenu.ftl` — masineoersettingsbugs → masinaal-learenbugs (ML ≠ MT)
  - Current: `masineoersettingsbugs`
- `backup-file-how-to-restore-header` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
  - Current: `reparearje`
  - en-US: `werstelle`
- `backup-file-title` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
  - Current: `reparearje`
  - en-US: `werstelle`
- `backup-folder-name` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
  - Current: `reparearje`
  - en-US: `werstelle`
- `restore-from-backup-header` — `browser/browser/backupSettings.ftl` — reparearje → werstelle. The file's own instructions quote the button label "Jo gegevens werstelle", so text and referenced label no longer match.
  - Current: `reparearje`
  - en-US: `werstelle`
- `browser-window-restore-down-button` — `browser/browser/browser.ftl` — Omleech opnij ynstelle → Ferlytsje
  - Current: `Omleech opnij ynstelle`
  - en-US: `Ferlytsje`
- `eme-notifications-drm-content-playing` — `browser/browser/browser.ftl` — Relation inverted: as written Firefox is what gets limited. en-US: "…which may limit what { -brand-short-name } can let you do with it."
- `enable-devtools-popup-description2` — `browser/browser/browser.ftl` — it menu Ekstra → it menu Browserhelpmidelen
  - Current: `it menu Ekstra`
  - en-US: `it menu Browserhelpmidelen`
- `identity-https-only-info-no-upgrade` — `browser/browser/browser.ftl` — HTTP-ferbining net fernije → ferbining net opwurdearje fan HTTP
  - Current: `HTTP-ferbining net fernije`
  - en-US: `ferbining net opwurdearje fan HTTP`
- `identity-weak-encryption` — `browser/browser/browser.ftl` — swakke befeiliging → swakke fersifering
  - Current: `swakke befeiliging`
  - en-US: `swakke fersifering`
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — Sykaksjes → Sykje yn aksjes / Aksjes trochsykje ("Search" is a verb)
  - Current: `Sykaksjes`
  - en-US: `Sykje yn aksjes`
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — Sykaksjes → Sykje yn aksjes / Aksjes trochsykje ("Search" is a verb)
  - Current: `Sykaksjes`
  - en-US: `Sykje yn aksjes`
- `urlbar-search-tips-onboard` — `browser/browser/browser.ftl` — Sykje nei { $engineName } → Sykje mei { $engineName }
  - Current: `Sykje nei { $engineName }`
  - en-US: `Sykje mei { $engineName }`
- `urlbar-searchmode-no-keyword2` — `browser/browser/browser.ftl` — Sykje nei trefwurden → Sykjen mei trefwurden
  - Current: `Sykje nei trefwurden`
  - en-US: `Sykjen mei trefwurden`
- `main-context-menu-stop` — `browser/browser/browserContext.ftl` — Beëinigje → Stopje
  - Current: `Beëinigje`
  - en-US: `Stopje`
- `customize-mode-overflow-list-description` — `browser/browser/customizeMode.ftl` — hjirnei ta → hjirhinne
  - Current: `hjirnei ta`
  - en-US: `hjirhinne`
- `customkeys-dev-storage` — `browser/browser/customkeys.ftl` — Unthâld-ynspektor → Opslach-ynspektor
  - Current: `Unthâld-ynspektor`
- `default-browser-guidance-notification-info-page` — `browser/browser/defaultBrowserNotification.ftl` — Toane: → Sjen litte
  - Current: `Toane:`
  - en-US: `Sjen litte`
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — "{ $num } bestanden niet gedownload." — the [one] variant is Frisian
- `sidebar-callout-survey-neutral` — `browser/browser/featureCallout.ftl` — Gemiddeld → Neutraal
  - Current: `Gemiddeld`
  - en-US: `Neutraal`
- `split-dismiss-button-show-fewer-option` — `browser/browser/featureCallout.ftl` — "Mear oanrekommandaasjes toane" — en-US: "Show fewer recommendations"
- `genai-input-ask-smart-window` — `browser/browser/genai.ftl` — Fragen… → Freegje…
  - Current: `Fragen…`
  - en-US: `Freegje…`
- `genai-menu-ask-smart-window` — `browser/browser/genai.ftl` — Fragen… → Freegje…
  - Current: `Fragen…`
  - en-US: `Freegje…`
- `genai-page-warning` — `browser/browser/genai.ftl` — is dit foar in part de gearfetting → is dit in dielgearfetting
  - Current: `is dit foar in part de gearfetting`
  - en-US: `is dit in dielgearfetting`
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — Entire string is Dutch
- `genai-shortcuts-selected-warning-generic` — `browser/browser/genai.ftl` — Entire string is Dutch: "U hebt ongeveer … kunnen sturen is ongeveer …" (also has a doubled period geselecteerd..)
- `menu-history-undo-window-menu` — `browser/browser/menubar.ftl` — Koartlyn sluten skermen → … finsters
  - Current: `Koartlyn sluten skermen`
  - en-US: `… finsters`
- `fxa-adoption-addresses-backup-subtitle` — `browser/browser/newtab/asrouter.ftl` — "jo bewarre wachtwurden" on the addresses card — en-US: "your saved addresses"
- `newtab-privacy-message-streak` — `browser/browser/newtab/newtab.ftl` — "op rige" dropped in the singular variant only
- `newtab-section-following-button` — `browser/browser/newtab/newtab.ftl` — Folgjend ("next") → Folge ("following")
  - Current: `Folgjend`
  - en-US: `Folge`
- `newtab-section-unfollow-button-label` — `browser/browser/newtab/newtab.ftl` — Folgjend ("next") → Folge ("following")
  - Current: `Folgjend`
  - en-US: `Folge`
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — foar de hân → by de hân
  - Current: `foar de hân`
  - en-US: `by de hân`
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — Mear oerienkomsten lade… → Mear wedstriden lade…
  - Current: `Mear oerienkomsten lade…`
  - en-US: `Mear wedstriden lade…`
- `newtab-topsites-edit-topsites-header` — `browser/browser/newtab/newtab.ftl` — "Topwebsite tafoegje" — en-US: "Edit Top Site"
- `mr2022-onboarding-pin-private-image-alt` — `browser/browser/newtab/onboarding.ftl` — út in ferskine — the noun hoed is missing
  - Current: `út in ferskine`
  - en-US: `hoed`
- `onboarding-easy-setup-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — troch in non-profitorganisaasje browser — stipe missing, bedriuwen duplicated
  - Current: `troch in non-profitorganisaasje browser`
  - en-US: `stipe`
- `policy-Backup` — `browser/browser/policies/policies-descriptions.ftl` — reparearje → weromsette (restore, not repair)
  - Current: `reparearje`
  - en-US: `weromsette`
- `policy-DisableSecurityBypass` — `browser/browser/policies/policies-descriptions.ftl` — befeiligingsynstellingen → befeiligingswarskôgingen
  - Current: `befeiligingsynstellingen`
  - en-US: `befeiligingswarskôgingen`
- `policy-OfferToSaveLoginsDefault` — `browser/browser/policies/policies-descriptions.ftl` — Spurious ôftwingje carried over from policy-OfferToSaveLogins
  - Current: `ôftwingje`
- `containers-icon-briefcase` — `browser/browser/preferences/containers.ftl` — Sammeling → Aktetaske
  - Current: `Sammeling`
  - en-US: `Aktetaske`
- `permissions-site-microphone-desc` — `browser/browser/preferences/permissions.ftl` — Says "jo kamera" in the microphone dialog — copy-paste from the camera string
- `appearance-window-density-touch` — `browser/browser/preferences/preferences.ftl` — lykas klikdoelen → en klikdoelen
  - Current: `lykas klikdoelen`
  - en-US: `en klikdoelen`
- `confirm-on-close-multiple-tabs` — `browser/browser/preferences/preferences.ftl` — Warskôgje by → Befêstigje foar
  - Current: `Warskôgje by`
  - en-US: `Befêstigje foar`
- `data-collection-run-studies` — `browser/browser/preferences/preferences.ftl` — in keur oan brûkers → willekeurich brûkers ("randomly" lost)
  - Current: `in keur oan brûkers`
  - en-US: `willekeurich brûkers`
- `performance-allow-hw-accel` — `browser/browser/preferences/preferences.ftl` — hardware-acceleratie → hardwarefersnelling
  - en-US: `hardwarefersnelling`
- `search-one-click-header2` — `browser/browser/preferences/preferences.ftl` — Fluchkeppelingen sykje (imperative) → Sykfluchkeppelingen (noun heading)
  - Current: `Fluchkeppelingen sykje`
  - en-US: `Sykfluchkeppelingen`
- `windows-launch-on-login-disabled` — `browser/browser/preferences/preferences.ftl` — Link text Apps → Opstart-apps (Windows "Startup Apps")
  - Current: `Apps`
- `windows-passkey-settings-label` — `browser/browser/preferences/preferences.ftl` — Wachtwurden beheare → Tagongskaaien beheare (passkeys ≠ passwords)
  - Current: `Wachtwurden beheare`
  - en-US: `Tagongskaaien beheare`
- `profiles-pink-theme-title` — `browser/browser/profiles.ftl` — Rôze → Rôs (its own label is Rôs)
  - Current: `Rôze`
  - en-US: `Rôs`
- _…and 91 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `settings-update-unsupported` — `browser/browser/aboutDialog.ftl` — fernijngen → fernijingen
  - Current: `fernijngen`
  - en-US: `fernijingen`
- `update-unsupported` — `browser/browser/aboutDialog.ftl` — fernijngen → fernijingen
  - Current: `fernijngen`
  - en-US: `fernijingen`
- `create-new-login-button` — `browser/browser/aboutLogins.ftl` — Nij oanmelding → Nije oanmelding
  - Current: `Nij oanmelding`
  - en-US: `Nije oanmelding`
- `login-item-new-login-title` — `browser/browser/aboutLogins.ftl` — Nij oanmelding → Nije oanmelding
  - Current: `Nij oanmelding`
  - en-US: `Nije oanmelding`
- `login-list-intro-description` — `browser/browser/aboutLogins.ftl` — Wannear jo → Wannear’t jo
  - Current: `Wannear jo`
  - en-US: `Wannear’t jo`
- `pocket-panel-saved-error-tag-length` — `browser/browser/aboutPocket.ftl` — beheint → beheind
  - Current: `beheint`
  - en-US: `beheind`
- `about-private-browsing-nova-info-subheader2` — `browser/browser/aboutPrivateBrowsing.ftl` — al jo priveefinster → al jo priveefinsters
  - Current: `al jo priveefinster`
  - en-US: `al jo priveefinsters`
- `welcome-back-restore-some-label` — `browser/browser/aboutSessionRestore.ftl` — dy’t jo winske (past) → dy’t jo winskje
  - Current: `dy’t jo winske`
  - en-US: `dy’t jo winskje`
- `about-unloads-column-sortweight` — `browser/browser/aboutUnloads.ftl` — ôflaad → ôflaat
  - Current: `ôflaad`
  - en-US: `ôflaat`
- `about-unloads-column-weight` — `browser/browser/aboutUnloads.ftl` — alteart → allearst; ôflaad → ôflaat
  - Current: `alteart`
  - en-US: `allearst`
- `addon-install-full-screen-blocked` — `browser/browser/addonNotifications.ftl` — Add-on-installaasje → Add-on-ynstallaasje
- `aiwindow-starter-browsing-compare` — `browser/browser/aiWindow.ftl` — ljeplêden → ljepblêden
  - Current: `ljeplêden`
  - en-US: `ljepblêden`
- `smartbar-placeholder` — `browser/browser/aiWindow.ftl` — in URL type → in URL typje
  - Current: `in URL type`
  - en-US: `in URL typje`
- `smart-window-opened-tabs-row-label` — `browser/browser/aiWindowContent.ftl` — ljeplêden → ljepblêden
  - Current: `ljeplêden`
  - en-US: `ljepblêden`
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — Dangling hokker ljepblêden at the end
- `appmenu-remote-tabs-tabsnotsyncing` — `browser/browser/appmenu.ftl` — ljepblêdsyngroanisaasje → ljepblêdsyngronisaasje
  - Current: `ljepblêdsyngroanisaasje`
  - en-US: `ljepblêdsyngronisaasje`
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — Two occurrences of wannear → wannear’t
  - Current: `wannear`
  - en-US: `wannear’t`
- `data-reporting-notification-message` — `browser/browser/browser.ftl` — ferstjoerd → ferstjoert
  - Current: `ferstjoerd`
  - en-US: `ferstjoert`
- `identity-https-only-info-turn-off2` — `browser/browser/browser.ftl` — te wurkje → te wurkjen
  - Current: `te wurkje`
  - en-US: `te wurkjen`
- `onboarding-aw-finish-setup-button` — `browser/browser/browser.ftl` — Ynstellen { -brand-short-name } → Ynstellen fan { -brand-short-name }
  - Current: `Ynstellen { -brand-short-name }`
  - en-US: `Ynstellen fan { -brand-short-name }`
- `activist-colorway-description` — `browser/browser/colorways.ftl` — en lit oaren leauwe → en litte oaren leauwe
  - Current: `en lit oaren leauwe`
  - en-US: `en litte oaren leauwe`
- `dreamer-colorway-description` — `browser/browser/colorways.ftl` — Idiom garbled + wrong subject agreement
- `contextual-manager-passwords-remove-all-message` — `browser/browser/contextual-manager.ftl` — wachtwurd dy’t → wachtwurd dat (neuter) in the [one] variants
  - Current: `wachtwurd dy’t`
  - en-US: `wachtwurd dat`
- `customize-mode-downloads-button-autohide` — `browser/browser/customizeMode.ftl` — wannear leech → wannear’t dizze leech is
  - Current: `wannear leech`
  - en-US: `wannear’t dizze leech is`
- `default-browser-prompt-message-pin` — `browser/browser/defaultBrowserNotification.ftl` — hantberik → hânberik
  - Current: `hantberik`
  - en-US: `hânberik`
- `bookmarks-toolbar-callout-2b-title` — `browser/browser/featureCallout.ftl` — blêdwizerakbalke → blêdwizerarkbalke
  - Current: `blêdwizerakbalke`
  - en-US: `blêdwizerarkbalke`
- `callout-firefox-view-colorways-subtitle` — `browser/browser/featureCallout.ftl` — it kleur dy’t → it kleur dat (neuter)
  - Current: `it kleur dy’t`
  - en-US: `it kleur dat`
- `sidebar-callout-survey-features-question` — `browser/browser/featureCallout.ftl` — in { -brand-short-name } → yn { -brand-short-name }
  - Current: `in { -brand-short-name }`
  - en-US: `yn { -brand-short-name }`
- `vertical-tabs-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — Doubled fluch
- `vertical-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — list mei ljeppers → list mei ljepblêden
  - Current: `list mei ljeppers`
  - en-US: `list mei ljepblêden`
- `windows-10-eos-sync-split-dismiss-button-show-fewer-option` — `browser/browser/featureCallout.ftl` — Minder oanrekommandearre toane → Minder oanrekommandaasjes toane
  - Current: `Minder oanrekommandearre toane`
  - en-US: `Minder oanrekommandaasjes toane`
- `windows-10-eos-sync-urgency-subtitle-1` — `browser/browser/featureCallout.ftl` — -ynstelling → -ynstellingen
  - Current: `-ynstelling`
  - en-US: `-ynstellingen`
- `firefox-relay-get-reusable-masks-failed` — `browser/browser/firefoxRelay.ftl` — Stray nij: gjin nij opnij brûkbere maskers
  - Current: `nij`
  - en-US: `gjin nij opnij brûkbere maskers`
- `firefoxview-opentabs-header` — `browser/browser/firefoxView.ftl` — ljeplêden → ljepblêden
  - Current: `ljeplêden`
  - en-US: `ljepblêden`
- `firefoxview-opentabs-nav` — `browser/browser/firefoxView.ftl` — ljeplêden → ljepblêden
  - Current: `ljeplêden`
  - en-US: `ljepblêden`
- `genai-prompts-proofread` — `browser/browser/genai.ftl` — krekten → krektens
  - Current: `krekten`
  - en-US: `krektens`
- `ipprotection-connection-status-blocked-error-description-1` — `browser/browser/ipProtection.ftl` — Comma splits subject from verb
- `ipprotection-connection-status-network-error-description` — `browser/browser/ipProtection.ftl` — dernei → dêrnei
  - Current: `dernei`
  - en-US: `dêrnei`
- `ipprotection-locations-subview-recommended-description` — `browser/browser/ipProtection.ftl` — Fyn (imperative) → Fynt
  - Current: `Fyn`
  - en-US: `Fynt`
- `menu-application-hide-other` — `browser/browser/menubar.ftl` — Oare ferstopje → Oaren ferstopje
  - Current: `Oare ferstopje`
  - en-US: `Oaren ferstopje`
- `migration-list-autofill-label` — `browser/browser/migrationWizard.ftl` — gegevens automatysk ynfolje → gegevens foar automatysk ynfoljen
  - Current: `gegevens automatysk ynfolje`
  - en-US: `gegevens foar automatysk ynfoljen`
- `july-jam-body` — `browser/browser/newtab/asrouter.ftl` — feilich en flugge tagong → feilige en flugge tagong
  - Current: `feilich en flugge tagong`
  - en-US: `feilige en flugge tagong`
- `nova-early-access-infobar-title` — `browser/browser/newtab/asrouter.ftl` — úterlik → uterlik (spurious accent)
  - Current: `úterlik`
  - en-US: `uterlik`
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — Untfang flugger sneupe → … sneupen
  - Current: `Untfang flugger sneupe`
  - en-US: `… sneupen`
- `spotlight-public-wifi-vpn-body` — `browser/browser/newtab/asrouter.ftl` — wylst it navigearjen → wylst jo navigearje
  - Current: `wylst it navigearjen`
  - en-US: `wylst jo navigearje`
- `windows-10-eos-challenger-pin-callout-subtitle` — `browser/browser/newtab/asrouter.ftl` — jo it nedich binne → jo it nedich hawwe
  - Current: `jo it nedich binne`
  - en-US: `jo it nedich hawwe`
- `newtab-empty-section-topstories` — `browser/browser/newtab/newtab.ftl` — Kin jo net wachtsje? → Kinne jo net wachtsje?
  - Current: `Kin jo net wachtsje?`
  - en-US: `Kinne jo net wachtsje?`
- `newtab-empty-section-topstories-generic` — `browser/browser/newtab/newtab.ftl` — Kin jo net wachtsje? → Kinne jo net wachtsje?
  - Current: `Kin jo net wachtsje?`
  - en-US: `Kinne jo net wachtsje?`
- `newtab-privacy-message-promo-monitor-1` — `browser/browser/newtab/newtab.ftl` — foar komme → foarkomme
  - Current: `foar komme`
  - en-US: `foarkomme`
- `newtab-privacy-message-promo-relay-1` — `browser/browser/newtab/newtab.ftl` — reagistraasjes → registraasjes
  - Current: `reagistraasjes`
  - en-US: `registraasjes`
- `newtab-section-unblock-topic` — `browser/browser/newtab/newtab.ftl` — Blokkearring { $topic } opheffe → Blokkearring fan { $topic } opheffe
  - Current: `Blokkearring { $topic } opheffe`
  - en-US: `Blokkearring fan { $topic } opheffe`
- `newtab-sports-widget-message-wallpapers-semifinals-body` — `browser/browser/newtab/newtab.ftl` — Meitsje ien dekôr → Meitsje it dekôr
  - Current: `Meitsje ien dekôr`
  - en-US: `Meitsje it dekôr`
- `newtab-wallpaper-abstract-purple-green` — `browser/browser/newtab/newtab.ftl` — Pears en griene → Pearze en griene
  - Current: `Pears en griene`
  - en-US: `Pearze en griene`
- `newtab-wallpaper-light-landscape` — `browser/browser/newtab/newtab.ftl` — Berch lânskip → Berchlânskip
  - Current: `Berch lânskip`
  - en-US: `Berchlânskip`
- `newtab-wallpaper-palm-trees` — `browser/browser/newtab/newtab.ftl` — wylst gouden oere → tidens it gouden oere
  - Current: `wylst gouden oere`
  - en-US: `tidens it gouden oere`
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — meitjse → meitsje (letters transposed)
  - Current: `meitjse`
  - en-US: `meitsje`
- `mr2022-onboarding-colorway-description-activist` — `browser/browser/newtab/onboarding.ftl` — en lit oaren leauwe → en litte oaren leauwe
  - Current: `en lit oaren leauwe`
  - en-US: `en litte oaren leauwe`
- `mr2022-onboarding-colorway-description-dreamer` — `browser/browser/newtab/onboarding.ftl` — Verb agrees with gelok instead of Jo
  - Current: `gelok`
  - en-US: `Jo`
- `mr2022-upgrade-onboarding-pin-private-window-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — fêst meitsje → fêstmeitsje
  - Current: `fêst meitsje`
  - en-US: `fêstmeitsje`
- `onboarding-new-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — sybalkeynstellingen → sidebalkeynstellingen
  - Current: `sybalkeynstellingen`
  - en-US: `sidebalkeynstellingen`
- _…and 177 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `navbar-home` — `browser/browser/browser.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
  - Current: `Startside`
  - en-US: `Begjinside`
- `quickactions-cmd-manageai` — `browser/browser/browser.ftl` — Also: quickactions-cmd-manageai (browser/browser/browser.ftl) lists ai útskeakelje, ai útskeakelje, ai beheare — the first keyword is duplicated, so one of en-US's three search keywords ("off ai") is unreachable.
- `more-from-moz-solo-description` — `browser/browser/preferences/moreFromMozilla.ftl` — Free (gratis) — fergees / fergese / fergeze: more-from-moz-firefox-relay-description, more-from-moz-mozilla-monitor-card, more-from-moz-solo-description (moreFromMozilla.ftl); newtab-privacy-message-promo-relay-2, -relay-3, -monitor-2 (newtab.ftl); relay-50-masks-announcement-subtitle (asrouter.ftl).
  - Current: `fergees`
  - en-US: `fergese`
- `home-homepage-title` — `browser/browser/preferences/preferences.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
  - Current: `Startside`
  - en-US: `Begjinside`
- `permissions-block-popups-exceptions-button4` — `browser/browser/preferences/preferences.ftl` — Third-party redirects — three renderings: permissions-block-popups-exceptions-button4.description (trochliedingen), permissions-block-popups2 (omliedingen), permissions.ftl (trochferwizingen).
  - en-US: `trochliedingen`
- `permissions-block-popups2` — `browser/browser/preferences/preferences.ftl` — Third-party redirects — three renderings: permissions-block-popups-exceptions-button4.description (trochliedingen), permissions-block-popups2 (omliedingen), permissions.ftl (trochferwizingen).
  - en-US: `trochliedingen`
- `preferences-doh-overview-custom` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
  - Current: `Feilige DNS`
  - en-US: `Befeilige DNS`
- `preferences-doh-overview-default` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
  - Current: `Feilige DNS`
  - en-US: `Befeilige DNS`
- `preferences-doh-radio-custom` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
  - Current: `Feilige DNS`
  - en-US: `Befeilige DNS`
- `preferences-doh-radio-default` — `browser/browser/preferences/preferences.ftl` — Secure DNS — Feilige DNS vs Befeilige DNS: preferences-doh-overview-default, preferences-doh-radio-default, preferences-doh-overview-custom, preferences-doh-radio-custom.
  - Current: `Feilige DNS`
  - en-US: `Befeilige DNS`
- `preferences-web-appearance-choice-light2` — `browser/browser/preferences/preferences.ftl` — Appearance — útstrieling vs uterlik: preferences-web-appearance-choice-light2, -dark2, -tooltip-light, -tooltip-dark.
  - Current: `útstrieling`
  - en-US: `uterlik`
- `search-show-suggestions-url-bar-option` — `browser/browser/preferences/preferences.ftl` — Search suggestions — sykfoarstellen vs syksuggestjes: search-show-suggestions-option, search-suggestions-option, search-show-suggestions-url-bar-option, addressbar-locbar-showtrendingsuggestions-option.
  - Current: `sykfoarstellen`
  - en-US: `syksuggestjes`
- `search-suggestions-option` — `browser/browser/preferences/preferences.ftl` — Search suggestions — sykfoarstellen vs syksuggestjes: search-show-suggestions-option, search-suggestions-option, search-show-suggestions-url-bar-option, addressbar-locbar-showtrendingsuggestions-option.
  - Current: `sykfoarstellen`
  - en-US: `syksuggestjes`
- `security-privacy-issue-warning-doh` — `browser/browser/preferences/preferences.ftl` — Network provider — netwurkbehearder (administrator) vs ynternetoanbieder: security-privacy-issue-warning-doh, security-privacy-issue-warning-ech (vs their -doh2/-ech2 variants).
  - Current: `netwurkbehearder`
  - en-US: `ynternetoanbieder`
- `security-privacy-issue-warning-ech` — `browser/browser/preferences/preferences.ftl` — Network provider — netwurkbehearder (administrator) vs ynternetoanbieder: security-privacy-issue-warning-doh, security-privacy-issue-warning-ech (vs their -doh2/-ech2 variants).
  - Current: `netwurkbehearder`
  - en-US: `ynternetoanbieder`
- `expand-sidebar-on-hover` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl).
  - Current: `sydbalke`
  - en-US: `sidebalke`
- `sidebar-context-menu-unpin-extension` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl).
  - Current: `sydbalke`
  - en-US: `sidebalke`
- `sidebar-open-tools-from-sidebar` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl).
  - Current: `sydbalke`
  - en-US: `sidebalke`
- `sidebar-resize-splitter` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl).
  - Current: `sydbalke`
  - en-US: `sidebalke`
- `addon-detail-homepage-label` — `toolkit/toolkit/about/aboutAddons.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
  - Current: `Startside`
  - en-US: `Begjinside`

### E. Typography, punctuation & spacing

- `aboutdialog-update-downloading` — `browser/browser/aboutDialog.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
- `settings-update-downloading` — `browser/browser/aboutDialog.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
- `about-logins-import-report-description2` — `browser/browser/aboutLogins.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `about-logins-import-report-error` — `browser/browser/aboutLogins.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `appmenuitem-monitor-description2` — `browser/browser/appmenu.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `fxa-menu-sync-status-off` — `browser/browser/appmenu.ftl` — fxa-menu-sync-status-off (Syngronisaasje is Ut → … is út) · add-exception-expired-short (Alde Ynformaasje) · menu-tools-extensions-and-themes (Utwreidingen en Tema’s) · skip-troubleshoot-refresh-profile (sentence starts lowercase).
  - Current: `Syngronisaasje is Ut`
  - en-US: `… is út`
- `profiler-popup-presets-networking-with-logs-description` — `browser/browser/appmenu.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `filepicker-blocked-infobar` — `browser/browser/browser.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `popup-show-popup-menuitem` — `browser/browser/browser.ftl` — rights-webservices-term-4 ("as-is") · protections-vpn-banner-content (TechRadar quote in "…") · popup-show-popup-menuitem.label (uses “…” where the adjacent popup-trigger-redirect-menuitem uses ‘…’).
  - en-US: `"as-is"`
- `popup-trigger-redirect-menuitem` — `browser/browser/browser.ftl` — rights-webservices-term-4 ("as-is") · protections-vpn-banner-content (TechRadar quote in "…") · popup-show-popup-menuitem.label (uses “…” where the adjacent popup-trigger-redirect-menuitem uses ‘…’).
  - en-US: `"as-is"`
- `quickactions-plugins` — `browser/browser/browser.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `main-context-menu-bookmark-page` — `browser/browser/browserContext.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
- `main-context-menu-edit-bookmark` — `browser/browser/browserContext.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
- `default-browser-guidance-notification-info-page` — `browser/browser/defaultBrowserNotification.ftl` — Added: import-source-page-title · findbar-fast-find-links.placeholder · app-basics-disk-available · detail-rating.value · default-browser-guidance-notification-info-page · inactive-css-at-position-try-not-supported.
- `bookmark-overlay-tags-empty-description` — `browser/browser/editBookmarkOverlay.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `sidebar-customization-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `splitview-onboarding-callout-subtitle-2` — `browser/browser/featureCallout.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `firefox-relay-and-fxa-popup-notification-second-sentence-with-domain-and-value-prop` — `browser/browser/firefoxRelay.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `firefoxview-tabpickup-description` — `browser/browser/firefoxView.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `genai-chatbot-summarize-footer-generic-subtitle` — `browser/browser/genai.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `ip-protection-description-1` — `browser/browser/ipProtection.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `ipprotection-feature-introduction-link-text-privacy-3` — `browser/browser/ipProtection.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — ipprotection-locations-subview-promo.message (mear as300) · support-remote-experiments-see-about-studies (missing space before the placeable) · about-logging-unknown-error (bard :) · download-ui-confirm-quit-cancel-downloads-mac (stopje ,) · about-httpsonly-explanation-continue (útskeakele .) · experimental-features-custom-wallpaper-description (Nij-ljepblêdside .) · plus the 47 doubled-space str…
  - en-US: `mear as300`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `ipprotection-site-settings-callout-subtitle` — `browser/browser/ipProtection.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
- `import-source-page-title` — `browser/browser/migration.ftl` — Added: import-source-page-title · findbar-fast-find-links.placeholder · app-basics-disk-available · detail-rating.value · default-browser-guidance-notification-info-page · inactive-css-at-position-try-not-supported.
- `migration-chrome-windows-password-import-step1` — `browser/browser/migrationWizard.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `migration-safari-password-import-step2` — `browser/browser/migrationWizard.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `firefoxview-spotlight-promo-primarybutton` — `browser/browser/newtab/asrouter.ftl` — places-locked-prompt · protections-panel-cross-site-tracking-cookies · screenshots-generic-error-title · tabbrowser-confirm-caretbrowsing-message · security-browsing-protection · firefoxview-spotlight-promo-primarybutton · fxa-menu-message-sync-devices-secondary-text2 · mr2022-onboarding-pin-image-alt.aria-label · safeb-blocked-unwanted-page-title · about-debugging-setup-intro · webauthn-register…
- `fxa-menu-message-sync-devices-secondary-text2` — `browser/browser/newtab/asrouter.ftl` — places-locked-prompt · protections-panel-cross-site-tracking-cookies · screenshots-generic-error-title · tabbrowser-confirm-caretbrowsing-message · security-browsing-protection · firefoxview-spotlight-promo-primarybutton · fxa-menu-message-sync-devices-secondary-text2 · mr2022-onboarding-pin-image-alt.aria-label · safeb-blocked-unwanted-page-title · about-debugging-setup-intro · webauthn-register…
- `home-mode-choice-custom-srd` — `browser/browser/newtab/newtab.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
- `newtab-label-source-read-time` — `browser/browser/newtab/newtab.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `newtab-widget-lists-menu-delete` — `browser/browser/newtab/newtab.ftl` — website-remove-language-button.aria-label and .title (en-US: "Remove { $locale }") · newtab-widget-lists-menu-delete (en-US: "Delete this list") · delete-ca-cert-confirm (en-US is declarative).
  - en-US: `.title`
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `mr1-onboarding-theme-description-dark` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
  - en-US: `‘Root Certs‘`
- `mr1-onboarding-theme-description-light` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
  - en-US: `‘Root Certs‘`
- `mr1-onboarding-theme-tooltip-dark` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
  - en-US: `‘Root Certs‘`
- `mr1-onboarding-theme-tooltip-light` — `browser/browser/newtab/onboarding.ftl` — load-module-help-root-certs-module-name.value (‘Root Certs‘ — inherited from en-US) · protocolhandler-mailto-handler-set (dy‘t) · mr1-onboarding-theme-tooltip-light.title, mr1-onboarding-theme-description-light.aria-description, mr1-onboarding-theme-tooltip-dark.title, mr1-onboarding-theme-description-dark.aria-description (all menu‘s).
  - en-US: `‘Root Certs‘`
- `mr2022-onboarding-pin-image-alt` — `browser/browser/newtab/onboarding.ftl` — places-locked-prompt · protections-panel-cross-site-tracking-cookies · screenshots-generic-error-title · tabbrowser-confirm-caretbrowsing-message · security-browsing-protection · firefoxview-spotlight-promo-primarybutton · fxa-menu-message-sync-devices-secondary-text2 · mr2022-onboarding-pin-image-alt.aria-label · safeb-blocked-unwanted-page-title · about-debugging-setup-intro · webauthn-register…
- `onboarding-gratitude-security-and-privacy-subtitle` — `browser/browser/newtab/onboarding.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `onboarding-refresh-import-title` — `browser/browser/newtab/onboarding.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `no-page-title` — `browser/browser/pageInfo.ftl` — Dropped: no-page-title.value.
- `page-info-frame` — `browser/browser/pageInfo.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
- `page-info-page` — `browser/browser/pageInfo.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
- `places-locked-prompt` — `browser/browser/places.ftl` — places-locked-prompt · protections-panel-cross-site-tracking-cookies · screenshots-generic-error-title · tabbrowser-confirm-caretbrowsing-message · security-browsing-protection · firefoxview-spotlight-promo-primarybutton · fxa-menu-message-sync-devices-secondary-text2 · mr2022-onboarding-pin-image-alt.aria-label · safeb-blocked-unwanted-page-title · about-debugging-setup-intro · webauthn-register…
- `policy-DefaultDownloadDirectory` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `policy-DisableThirdPartyModuleBlocking` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `policy-LegacyProfiles` — `browser/browser/policies/policies-descriptions.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `languages-code-format` — `browser/browser/preferences/languages.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `choose-language-description` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `confirm-browser-language-change-description` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `download-always-ask-where2` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
- `extension-controlled-enable` — `browser/browser/preferences/preferences.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
- `forms-master-pw-change` — `browser/browser/preferences/preferences.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
- _…and 98 more; see `state/` for the full list._

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Resolved to date (245)

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
- `launch-on-login-spotlight-title` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-11

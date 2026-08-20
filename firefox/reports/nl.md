# Firefox l10n QA — nl

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b95608d528c8` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `d411ef0407f1` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,148 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

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
| Strings | 18,148 |
| Missing strings | 15 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**15 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 9
- `browser/browser/aboutPrivateBrowsing.ftl` — 2
- `browser/browser/preferences/preferences.ftl` — 1
- `toolkit/toolkit/about/aboutProcesses.ftl` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1
- `toolkit/toolkit/global/processTypes.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 891, `straight-double` 25, `curly-double` 9 | **curly-single** |
| apostrophe | `typographic` 1137 | **typographic** |
| ellipsis | `char` 461 | **char** |
| dash | `en` 135 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |
| register | `formal` 3090 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (400)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 24 |
| 2 | Wrong content (says something other than the English) | 136 |
| 3 | Degraded language (grammar, spelling, terminology) | 210 |
| 4 | Cosmetic (typography, spacing) | 30 |

### A. Functional, markup, variables & plurals

- `about-logins-copy-password-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — about-logins-edit-login-os-auth-dialog-message-macosx, about-logins-reveal-password-os-auth-dialog-message-macosx, about-logins-copy-password-os-auth-dialog-message-macosx — browser/browser/aboutLogins.ftl — the comment says to supply only the reason, which macOS prefixes with "Firefox is trying to …". These are imperatives, so the resulting sentence breaks. Current: "bewerk de opgeslagen aanmeld…
  - en-US: `…message2-macosx`
- `about-logins-edit-login-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — about-logins-edit-login-os-auth-dialog-message-macosx, about-logins-reveal-password-os-auth-dialog-message-macosx, about-logins-copy-password-os-auth-dialog-message-macosx — browser/browser/aboutLogins.ftl — the comment says to supply only the reason, which macOS prefixes with "Firefox is trying to …". These are imperatives, so the resulting sentence breaks. Current: "bewerk de opgeslagen aanmeld…
  - en-US: `…message2-macosx`
- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — same defect in both plural variants: <span data-l10n-name="meta">(niet geïmporteerd)</span > → Suggest: </span>
- `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl` — double space before the second link (… of <a data-l10n-name="import-file-link">).
- `about-logins-reveal-password-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — about-logins-edit-login-os-auth-dialog-message-macosx, about-logins-reveal-password-os-auth-dialog-message-macosx, about-logins-copy-password-os-auth-dialog-message-macosx — browser/browser/aboutLogins.ftl — the comment says to supply only the reason, which macOS prefixes with "Firefox is trying to …". These are imperatives, so the resulting sentence breaks. Current: "bewerk de opgeslagen aanmeld…
  - en-US: `…message2-macosx`
- `xpinstall-prompt-never-allow-and-report` — `browser/browser/addonNotifications.ftl` — Access key `m` of `xpinstall-prompt-never-allow-and-report` is not present in its label
  - Current: `m`
  - The label is “Verdachte website rapporteren”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `contextual-manager-passwords-copy-password-os-auth-dialog-message-macosx` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-reveal-password-os-auth-dialog-message-macosx, contextual-manager-passwords-copy-password-os-auth-dialog-message-macosx — browser/browser/contextual-manager.ftl — same defect; …edit-password-os-auth-dialog-message-macosx in the same file is correct.
- `contextual-manager-passwords-reveal-password-os-auth-dialog-message-macosx` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-reveal-password-os-auth-dialog-message-macosx, contextual-manager-passwords-copy-password-os-auth-dialog-message-macosx — browser/browser/contextual-manager.ftl — same defect; …edit-password-os-auth-dialog-message-macosx in the same file is correct.
- `tab-groups-2026-onboarding-cta-button` — `browser/browser/featureCallout.ftl` — the comment asks for "under ~15 characters so it fits in the callout UI"; "Een groep starten" is 17. Soft limit, worth a shorter form (e.g. "Groep starten").
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — malformed closing tag </a > (space inside the tag), so the second link will not render. Current: …generatieve AI</a > en de… → Suggest: …generatieve AI</a> en de…
- `cfr-doorhanger-milestone-heading2` — `browser/browser/newtab/asrouter.ftl` — cfr-doorhanger-milestone-heading2 ([one] variant) — browser/browser/newtab/asrouter.ftl — the opening <b> is corrupted to b>, and "over" is dropped. Current: … b>{ $blockedCount }</b> tracker geblokkeerd! → Suggest: … meer dan <b>{ $blockedCount }</b> tracker geblokkeerd!
- `return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — double space around <img data-l10n-name="icon"/>.
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — double space after <img data-l10n-name="translations-icon"/>.
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — stray space inside the link text, producing a trailing underlined space. Current: <a data-l10n-name="appstore-link">Apple App Store </a> → Suggest: …Apple App Store</a>
- `inactive-css-not-grid-or-flex-container-or-multicol-container-fix` — `devtools/client/tooltips.ftl` — the CSS keyword inside <strong> is misspelled, so the suggested fix is wrong code. Current: <strong>colums:2</strong> → Suggest: <strong>columns:2</strong>
- `inactive-css-not-grid-or-flex-container-or-multicol-container-fix` — `devtools/client/tooltips.ftl` — Also in this bucket: the CSS keyword items already listed in section A (inactive-css-not-grid-or-flex-container-or-multicol-container-fix, inactive-css-ruby-element-fix, webconsole-commands-usage-block).
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — inactive-css-ruby-element-fix, inactive-css-ruby-element-fix-1 — devtools/client/tooltips.ftl — the CSS property name inside <strong> was translated, against the section's developer comment. Current: <strong>lettergrootte</strong> → Suggest: <strong>font-size</strong>
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — Also in this bucket: the CSS keyword items already listed in section A (inactive-css-not-grid-or-flex-container-or-multicol-container-fix, inactive-css-ruby-element-fix, webconsole-commands-usage-block).
- `inactive-css-ruby-element-fix-1` — `devtools/client/tooltips.ftl` — inactive-css-ruby-element-fix, inactive-css-ruby-element-fix-1 — devtools/client/tooltips.ftl — the CSS property name inside <strong> was translated, against the section's developer comment. Current: <strong>lettergrootte</strong> → Suggest: <strong>font-size</strong>
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — Also in this bucket: the CSS keyword items already listed in section A (inactive-css-not-grid-or-flex-container-or-multicol-container-fix, inactive-css-ruby-element-fix, webconsole-commands-usage-block).
- `addon-badge-line3` — `toolkit/toolkit/about/aboutAddons.ftl` — addon-badge-line3 (.title), addon-badge-line4 (.title) — toolkit/toolkit/about/aboutAddons.ftl — the dev comment states that "Mozilla" is hard-coded on purpose "because … we don't want forks to display 'by Fork'". nl adds "Firefox". Current: "Officiële door Mozilla Firefox gebouwde extensie." → Suggest: "Officiële door Mozilla gebouwde extensie."
  - en-US: `"Officiële door Mozilla gebouwde extensie."`
- `addon-badge-line4` — `toolkit/toolkit/about/aboutAddons.ftl` — addon-badge-line3 (.title), addon-badge-line4 (.title) — toolkit/toolkit/about/aboutAddons.ftl — the dev comment states that "Mozilla" is hard-coded on purpose "because … we don't want forks to display 'by Fork'". nl adds "Firefox". Current: "Officiële door Mozilla Firefox gebouwde extensie." → Suggest: "Officiële door Mozilla gebouwde extensie."
  - en-US: `"Officiële door Mozilla gebouwde extensie."`
- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — both <q> items are literal Profiler UI labels; "Marker Chart" was kept but "Telemetry" was translated. Suggest: <q>Telemetry</q>
  - Current: `<q>`
- `btp-warning-tracker-purged` — `toolkit/toolkit/global/antiTracking.ftl` — the dev comment says not to translate "bounce tracker"; nl closes it into one word here but keeps two in btp-warning-tracker-classified. Suggest: "bounce tracker" in both.
- `chooser-dialog-description` — `toolkit/toolkit/global/handlerDialog.ftl` — the noun is missing, leaving a broken sentence. Current: "Kies een toepassing om de { $scheme }-mee te openen." → Suggest: "Kies een toepassing om de { $scheme }-koppeling te openen." (en-US: "to open the { $scheme } link")
  - Current: `{ $scheme }`

### B. Mistranslation, reversed meaning, wrong names & brand

- `addon-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — addon-install-error-incorrect-hash, addon-local-install-error-incorrect-hash — addonNotifications.ftl — relative clause collapsed. Current: "…niet overeenkomt met de verwachte add-on { -brand-short-name }." → Suggest: "…niet overeenkomt met de add-on die { -brand-short-name } verwachtte."
  - Current: `{ -brand-short-name }`
- `addon-local-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — addon-install-error-incorrect-hash, addon-local-install-error-incorrect-hash — addonNotifications.ftl — relative clause collapsed. Current: "…niet overeenkomt met de verwachte add-on { -brand-short-name }." → Suggest: "…niet overeenkomt met de add-on die { -brand-short-name } verwachtte."
  - Current: `{ -brand-short-name }`
- `smart-window-switched-tab-summary` — `browser/browser/aiWindowContent.ftl` — smart-window-switched-tab-label, smart-window-switched-tab-summary — aiWindowContent.ftl — "switched to" is not "swapped". Current: "Omgewisselde tabbladen" / "Omgewisseld naar ‘{ $title }’." → Suggest: "Van tabblad gewisseld" / "Overgeschakeld naar ‘{ $title }’."
  - Current: `{ $title }`
- `profiler-popup-presets-ml-description` — `browser/browser/appmenu.ftl` — perftools-presets-ml-description2, profiler-popup-presets-ml-description — client/perftools.ftl, browser/browser/appmenu.ftl — "machine learning" became "machine translation". Suggest: "…bugs in machinaal leren…"
- `other-backup-files-founds` — `browser/browser/backupSettings.ftl` — en-US "Note:". Current: "<b>Noot:</b>" → Suggest: "<b>Opmerking:</b>"
  - en-US: `<b>`
- `enable-devtools-popup-description2` — `browser/browser/browser.ftl` — en-US "Browser Tools menu"; nl points at the "Extra" menu. Suggest: "…via het menu Browserhulpmiddelen…"
- `trustpanel-description-disabled` — `browser/browser/browser.ftl` — en-US "is off-duty", losing the contrast with trustpanel-header-enabled ("staat op wacht"). Current: "…heeft geen dienst." → Suggest: "…staat niet op wacht."
  - en-US: `"…staat niet op wacht."`
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — urlbar-result-action-search-actions, urlbar-placeholder-search-mode-other-actions (.aria-label) — browser.ftl — "Search" is a verb here. Current: "Zoekacties" → Suggest: "Acties doorzoeken" / "Zoeken in acties"
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — urlbar-result-action-search-actions, urlbar-placeholder-search-mode-other-actions (.aria-label) — browser.ftl — "Search" is a verb here. Current: "Zoekacties" → Suggest: "Acties doorzoeken" / "Zoeken in acties"
- `customkeys-conflict-unusable-body` — `browser/browser/customkeys.ftl` — customkeys-conflict-unusable-title, customkeys-conflict-unusable-body — customkeys.ftl — "key" is a keyboard key, not a cryptographic key. Current: "Sleutel kan niet worden gebruikt" / "Deze sleutel wordt al gebruikt door…" → Suggest: "Toets kan niet worden gebruikt" / "Deze toets wordt al gebruikt door…" (cf. customkeys-conflict-confirm, which correctly uses "toets")
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — customkeys-conflict-unusable-title, customkeys-conflict-unusable-body — customkeys.ftl — "key" is a keyboard key, not a cryptographic key. Current: "Sleutel kan niet worden gebruikt" / "Deze sleutel wordt al gebruikt door…" → Suggest: "Toets kan niet worden gebruikt" / "Deze toets wordt al gebruikt door…" (cf. customkeys-conflict-confirm, which correctly uses "toets")
- `windows-10-eos-sync-general-title-1` — `browser/browser/featureCallout.ftl` — en-US "the { -brand-short-name } you've made yours". Current: "…die u van u hebt gemaakt." → Suggest: "…die u zich eigen hebt gemaakt."
  - Current: `{ -brand-short-name }`
  - en-US: `"…die u zich eigen hebt gemaakt."`
- `firefoxview-closed-tabs-dismiss-tab` — `browser/browser/firefoxView.ftl` — firefoxview-closed-tabs-dismiss-tab (.title), fxviewtabrow-dismiss-tab-button (.title) — firefoxView.ftl, fxviewTabList.ftl — these dismiss an already-closed tab from the list; "sluiten" collides with the real close action (fxviewtabrow-close-tab-button). Current: "{ $tabTitle } sluiten" → Suggest: "{ $tabTitle } uit de lijst verwijderen"
  - Current: `{ $tabTitle }`
- `fxviewtabrow-dismiss-tab-button` — `browser/browser/fxviewTabList.ftl` — firefoxview-closed-tabs-dismiss-tab (.title), fxviewtabrow-dismiss-tab-button (.title) — firefoxView.ftl, fxviewTabList.ftl — these dismiss an already-closed tab from the list; "sluiten" collides with the real close action (fxviewtabrow-close-tab-button). Current: "{ $tabTitle } sluiten" → Suggest: "{ $tabTitle } uit de lijst verwijderen"
  - Current: `{ $tabTitle }`
- `genai-prompts-summarize` — `browser/browser/genai.ftl` — "concise" became "descriptive", nearly reversing the instruction. Current: "…in exacte en beschrijvende woorden." → Suggest: "…in precieze en beknopte woorden."
  - en-US: `"…in precieze en beknopte woorden."`
- `cfr-doorhanger-bookmark-fxa-body` — `browser/browser/newtab/asrouter.ftl` — "this bookmark" generalised. Suggest: "…dat u niet zonder deze bladwijzer zit…" (cf. -body-2)
- `firefoxview-cfr-body-v2` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
- `fxa-menu-message-sync-devices-secondary-text` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
- `fxa-menu-message-sync-devices-secondary-text2` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
- `set-default-menu-message-row-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
- `windows-10-eos-sync-callout-privacy-screen-2-subtitle` — `browser/browser/newtab/asrouter.ftl` — "data and privacy settings" became "data settings and privacy settings". Suggest: "…om uw gegevens en privacyinstellingen mee te nemen."
- `home-prefs-highlights-option-most-recent-download-srd` — `browser/browser/newtab/newtab.ftl` — home-prefs-highlights-option-most-recent-download, home-prefs-highlights-option-most-recent-download-srd — preferences/preferences.ftl, newtab/newtab.ftl — noun phrase rendered as a participle. Current: "Meest recent gedownload" → Suggest: "Meest recente download"
  - en-US: `"Meest recente download"`
- `newtab-section-following-button` — `browser/browser/newtab/newtab.ftl` — newtab-section-following-button, newtab-section-unfollow-button-label (.aria-label) — newtab/newtab.ftl — "Volgend" means next. Current: "Volgend" → Suggest: "Gevolgd" (matches newtab-section-mangage-topics-followed-topics)
- `newtab-section-unfollow-button-label` — `browser/browser/newtab/newtab.ftl` — newtab-section-following-button, newtab-section-unfollow-button-label (.aria-label) — newtab/newtab.ftl — "Volgend" means next. Current: "Volgend" → Suggest: "Gevolgd" (matches newtab-section-mangage-topics-followed-topics)
- `newtab-weather-see-forecast` — `browser/browser/newtab/newtab.ftl` — newtab-weather-see-forecast (.title), newtab-weather-see-forecast-description (.title) — newtab/newtab.ftl — $provider is the weather service. Current: "…bekijken voor { $provider }" → Suggest: "…bekijken in { $provider }"
  - Current: `{ $provider }`
- `newtab-weather-see-forecast-description` — `browser/browser/newtab/newtab.ftl` — newtab-weather-see-forecast (.title), newtab-weather-see-forecast-description (.title) — newtab/newtab.ftl — $provider is the weather service. Current: "…bekijken voor { $provider }" → Suggest: "…bekijken in { $provider }"
  - Current: `{ $provider }`
- `newtab-widget-message-copy` — `browser/browser/newtab/newtab.ftl` — "stretch breaks" became "long breaks". Suggest: "…tot pauzes om te bewegen"
- `newtab-widget-timer-label-play` — `browser/browser/newtab/newtab.ftl` — timer control, not media playback. Current: "Afspelen" → Suggest: "Starten"
  - en-US: `"Starten"`
- `create-backup-screen-2-easy-label` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-label, mr2022-onboarding-import-header — newtab/onboarding.ftl — "setup" is configuration, not software installation. Current: "Eenvoudige instellingen" / "Razendsnelle installatie" → Suggest: "Eenvoudig instellen" / "Razendsnel instellen"
- `mr2022-onboarding-import-header` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-label, mr2022-onboarding-import-header — newtab/onboarding.ftl — "setup" is configuration, not software installation. Current: "Eenvoudige instellingen" / "Razendsnelle installatie" → Suggest: "Eenvoudig instellen" / "Razendsnel instellen"
- `onboarding-sign-up-description` — `browser/browser/newtab/onboarding.ftl` — "any device" weakened to "a device". Suggest: "…op een willekeurig apparaat…"
- `restored-from-backup-success-title` — `browser/browser/newtab/onboarding.ftl` — possessive dropped. Suggest: "We zijn terug! Uw { -brand-short-name }-gegevens zijn hersteld."
- `policy-DisableRemoteImprovements` — `browser/browser/policies/policies-descriptions.ftl` — "changes" dropped. Suggest: "…wijzigingen aan prestaties, stabiliteit en functies toepast…"
- `policy-DisableSecurityBypass` — `browser/browser/policies/policies-descriptions.ftl` — "security warnings" became "security settings". Suggest: "…bepaalde beveiligingswaarschuwingen omzeilt."
- `policy-GoToIntranetSiteForSingleWordEntryInAddressBar` — `browser/browser/policies/policies-descriptions.ftl` — "single word entries" read as "a few words". Suggest: "…bij invoer van één woord in de adresbalk."
- `containers-icon-briefcase` — `browser/browser/preferences/containers.ftl` — "Briefcase" is the depicted object. Current: "Werkmap" → Suggest: "Aktetas" (and align briefcase-avatar/briefcase-avatar-alt in profiles.ftl, which also say "Werkmap" while briefcase-avatar-tooltip says "Aktetas")
- `permissions-searchbox` — `browser/browser/preferences/permissions.ftl` — the box filters the website list. Current: "Website doorzoeken" → Suggest: "Websites zoeken"
  - en-US: `"Websites zoeken"`
- `appearance-group2` — `browser/browser/preferences/preferences.ftl` — appearance-group2 (.label), preferences-web-appearance-header, web-appearance-group (.aria-label) — preferences/preferences.ftl — definite singular implies one specific site. Current: "Uiterlijk van de website" → Suggest: "Uiterlijk van websites"
  - en-US: `"Uiterlijk van websites"`
- `appearance-window-density-touch` — `browser/browser/preferences/preferences.ftl` — "and" became "such as". Current: "Grotere vensterelementen zoals klikdoelen" → Suggest: "Grotere vensterelementen en klikdoelen"
  - en-US: `"Grotere vensterelementen en klikdoelen"`
- `home-prefs-highlights-option-most-recent-download` — `browser/browser/preferences/preferences.ftl` — home-prefs-highlights-option-most-recent-download, home-prefs-highlights-option-most-recent-download-srd — preferences/preferences.ftl, newtab/newtab.ftl — noun phrase rendered as a participle. Current: "Meest recent gedownload" → Suggest: "Meest recente download"
  - en-US: `"Meest recente download"`
- `pane-experimental-description4` — `browser/browser/preferences/preferences.ftl` — "evolving" became "in de groei"; the parallel -description3 uses "worden steeds beter".
- `permissions-header3` — `browser/browser/preferences/preferences.ftl` — en-US "Manage what websites can access…". Current: "Beheren welke websites kunnen benaderen, aansturen of starten." → Suggest: "Beheren wat websites kunnen benaderen, aansturen of starten."
  - en-US: `"Beheren wat websites kunnen benaderen, aansturen of starten."`
- `preferences-etp-advanced-settings-group` — `browser/browser/preferences/preferences.ftl` — en-US "blocking most trackers automatically"; the qualifier is dropped. Suggest: "…waarbij de meeste trackers automatisch worden geblokkeerd"
  - en-US: `.description`
- `preferences-etp-level-standard` — `browser/browser/preferences/preferences.ftl` — the word is repeated, so the parenthesis conveys nothing. Current: "Standaard (standaard)" → Suggest: "Standaard (standaardinstelling)"
  - en-US: `"Standaard`
- `preferences-web-appearance-header` — `browser/browser/preferences/preferences.ftl` — appearance-group2 (.label), preferences-web-appearance-header, web-appearance-group (.aria-label) — preferences/preferences.ftl — definite singular implies one specific site. Current: "Uiterlijk van de website" → Suggest: "Uiterlijk van websites"
  - en-US: `"Uiterlijk van websites"`
- `web-appearance-group` — `browser/browser/preferences/preferences.ftl` — appearance-group2 (.label), preferences-web-appearance-header, web-appearance-group (.aria-label) — preferences/preferences.ftl — definite singular implies one specific site. Current: "Uiterlijk van de website" → Suggest: "Uiterlijk van websites"
  - en-US: `"Uiterlijk van websites"`
- `report-broken-site-panel-reason-adblocker-moz-box-button` — `browser/browser/reportBrokenSite.ftl` — report-broken-site-panel-reason-adblocker2 (.label), report-broken-site-panel-reason-adblocker-moz-box-button (.label) — reportBrokenSite.ftl — missing determiner. Current: "Website vroeg om adblocker uit te schakelen" → Suggest: "…om de adblocker uit te schakelen"
  - en-US: `"…om de adblocker uit te schakelen"`
- `report-broken-site-panel-reason-adblocker2` — `browser/browser/reportBrokenSite.ftl` — report-broken-site-panel-reason-adblocker2 (.label), report-broken-site-panel-reason-adblocker-moz-box-button (.label) — reportBrokenSite.ftl — missing determiner. Current: "Website vroeg om adblocker uit te schakelen" → Suggest: "…om de adblocker uit te schakelen"
  - en-US: `"…om de adblocker uit te schakelen"`
- `safeb-blocked-malware-page-error-desc-no-override-sumo` — `browser/browser/safebrowsing/blockedSite.ftl` — safeb-blocked-malware-page-short-desc, safeb-blocked-malware-page-error-desc-override-sumo, safeb-blocked-malware-page-error-desc-no-override-sumo — safebrowsing/blockedSite.ftl — kwaadwillend describes persons with ill intent, not software. Current: "kwaadwillende software" → Suggest: "kwaadaardige software"
  - en-US: `"kwaadaardige software"`
- `safeb-blocked-malware-page-error-desc-override-sumo` — `browser/browser/safebrowsing/blockedSite.ftl` — safeb-blocked-malware-page-short-desc, safeb-blocked-malware-page-error-desc-override-sumo, safeb-blocked-malware-page-error-desc-no-override-sumo — safebrowsing/blockedSite.ftl — kwaadwillend describes persons with ill intent, not software. Current: "kwaadwillende software" → Suggest: "kwaadaardige software"
  - en-US: `"kwaadaardige software"`
- `safeb-blocked-malware-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — safeb-blocked-malware-page-short-desc, safeb-blocked-malware-page-error-desc-override-sumo, safeb-blocked-malware-page-error-desc-no-override-sumo — safebrowsing/blockedSite.ftl — kwaadwillend describes persons with ill intent, not software. Current: "kwaadwillende software" → Suggest: "kwaadaardige software"
  - en-US: `"kwaadaardige software"`
- `set-background-fill` — `browser/browser/setDesktopBackground.ftl` — uitvullen is the typographic term for justify. Current: "Uitvullen" → Suggest: "Vullen"
  - en-US: `"Vullen"`
- `duplicate-tab2` — `browser/browser/tabContextMenu.ftl` — duplicate-tab2 (.label), duplicate-tabs2 (.label) — tabContextMenu.ftl — noun instead of the menu verb. Current: "Duplicaat" → Suggest: "Dupliceren"
  - en-US: `"Dupliceren"`
- `duplicate-tabs2` — `browser/browser/tabContextMenu.ftl` — duplicate-tab2 (.label), duplicate-tabs2 (.label) — tabContextMenu.ftl — noun instead of the menu verb. Current: "Duplicaat" → Suggest: "Dupliceren"
  - en-US: `"Dupliceren"`
- `existing-user-privacy-notice-update-message` — `browser/browser/termsofuse.ftl` — "to reflect" lost. Current: "…bijgewerkt naar de nieuwste functies in { -brand-short-name }." → Suggest: "…bijgewerkt om de nieuwste functies in { -brand-short-name } te weerspiegelen."
  - Current: `{ -brand-short-name }`
- `webrtc-sharing-menu` — `browser/browser/webrtcIndicator.ftl` — subject and object swapped. en-US "Tabs sharing devices". Current: "Apparaten die tabbladen delen" → Suggest: "Tabbladen die apparaten delen"
  - en-US: `"Tabbladen die apparaten delen"`
- `accessibility-best-practices` — `devtools/client/accessibility.ftl` — Current: "Goede voorbeelden" → Suggest: "Best practices"
  - en-US: `"Best practices"`
- `accessibility-text-label-issue-heading` — `devtools/client/accessibility.ftl` — accessibility-text-label-issue-heading, -heading-content — client/accessibility.ftl — HTML headings are koppen, not kopteksten. Suggest: "Koppen moeten worden gelabeld."
  - en-US: `-heading-content`
- `session-history-entry-info-button-title` — `devtools/client/application.ftl` — "data" dropped. Suggest: "Sessiegeschiedenisgegevens tonen"
  - en-US: `.title`
- _…and 75 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — "in de klassieke en Slimme Vensters" mixes a lone adjective with a plural brand term; en-US "in Classic and Smart Windows". Worth rewording.
  - en-US: `.label`
- `aiwindow-ai-chat-grid-list-view` — `browser/browser/aiWindow.ftl` — "Modus wisselen: Lijstweergave" → lowercase (cf. -grid-view)
  - en-US: `-grid-view`
- `toolbar-switcher-customizable-label` — `browser/browser/aiWindow.ftl` — toolbar-switcher-customizable-label (.tooltiptext) — aiWindow.ftl; smartwindow-switcher-callout — newtab/onboarding.ftl — mid-sentence "Slimme" capitalised in one half of a coordination only.
  - en-US: `.tooltiptext`
- `aiwindow-manage-memories` — `browser/browser/aiWindowContent.ftl` — no hyphen between these two Dutch nouns. Current: "Herinnering-instellingen" → Suggest: "Herinneringsinstellingen"
  - en-US: `"Herinneringsinstellingen"`
- `smart-window-opened-tabs-summary-group` — `browser/browser/aiWindowContent.ftl` — subjectless finite verb; the parallel smart-window-grouped-tabs-summary is correct. Current: "Heeft de groep ‘{ $label }’ gemaakt…" → Suggest: "Groep ‘{ $label }’ gemaakt…"
  - Current: `{ $label }`
- `smart-window-ungroup-success-summary` — `browser/browser/aiWindowContent.ftl` — smart-window-ungroup-success-summary, smart-window-ungrouped-row-label — aiWindowContent.ftl — "degroeperen" is not a Dutch verb. Current: "gedegroepeerd" → Suggest: "Groepering van { $count } tabbladen opgeheven" (cf. smart-window-grouped-and-ungrouped-label, which correctly uses "Groepering … ongedaan gemaakt")
  - en-US: `{ $count }`
- `smart-window-ungrouped-row-label` — `browser/browser/aiWindowContent.ftl` — smart-window-ungroup-success-summary, smart-window-ungrouped-row-label — aiWindowContent.ftl — "degroeperen" is not a Dutch verb. Current: "gedegroepeerd" → Suggest: "Groepering van { $count } tabbladen opgeheven" (cf. smart-window-grouped-and-ungrouped-label, which correctly uses "Groepering … ongedaan gemaakt")
  - en-US: `{ $count }`
- `fxa-menu-sync-status-off` — `browser/browser/appmenu.ftl` — fxa-menu-sync-status-on, fxa-menu-sync-status-off — appmenu.ftl — "Synchronisatie is Aan" / "is Uit" → lowercase
  - en-US: `lowercase`
- `fxa-menu-sync-status-on` — `browser/browser/appmenu.ftl` — fxa-menu-sync-status-on, fxa-menu-sync-status-off — appmenu.ftl — "Synchronisatie is Aan" / "is Uit" → lowercase
  - en-US: `lowercase`
- `onboarding-aw-finish-setup-button` — `browser/browser/browser.ftl` — Current: "Instellen { -brand-short-name } voltooien" → Suggest: "Instellen van { -brand-short-name } voltooien" (as in onboarding-checklist-title)
  - Current: `{ -brand-short-name }`
- `urlbar-result-explanation-last-visited-relative` — `browser/browser/browser.ftl` — $date is relative ("vandaag"). Current: "Uw laatste bezoek was op { $date }" → Suggest: drop "op" (keep it in …-last-visited-absolute)
  - Current: `{ $date }`
  - en-US: `…-last-visited-absolute`
- `main-context-menu-link-send-to-mobile` — `browser/browser/browserContext.ftl` — main-context-menu-send-to-mobile-2, main-context-menu-link-send-to-mobile — browserContext.ftl; fxviewtabrow-send-to-mobile — fxviewTabList.ftl; tab-context-send-to-mobile ([1] variant) — tabContextMenu.ftl — "Naar Mobiel verzenden" → "Naar mobiel verzenden"; note tab-context-send-to-mobile is inconsistent within itself (only the [1] variant capitalises).
- `main-context-menu-send-to-mobile-2` — `browser/browser/browserContext.ftl` — main-context-menu-send-to-mobile-2, main-context-menu-link-send-to-mobile — browserContext.ftl; fxviewtabrow-send-to-mobile — fxviewTabList.ftl; tab-context-send-to-mobile ([1] variant) — tabContextMenu.ftl — "Naar Mobiel verzenden" → "Naar mobiel verzenden"; note tab-context-send-to-mobile is inconsistent within itself (only the [1] variant capitalises).
- `contextual-manager-passwords-no-passwords-message` — `browser/browser/contextual-manager.ftl` — calque of "watch out for". Suggest: "…en we letten op datalekken en waarschuwen u als u wordt getroffen."
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — defaultBrowserNotification.ftl — step sentences inconsistently capitalised after the colon, both between and within the two variants.
- `webext-quarantine-confirmation-line-2` — `browser/browser/extensionsUI.ftl` — missing second "te" in a coordinated infinitive. Suggest: "…te lezen en te wijzigen."
- `fxviewtabrow-move-tab-end` — `browser/browser/fxviewTabList.ftl` — fxviewtabrow-move-tab-start, fxviewtabrow-move-tab-end — fxviewTabList.ftl — "Verplaatsen naar Start" / "naar Einde" → "naar begin" / "naar einde" (cf. move-to-start / move-to-end in tabContextMenu.ftl, and fxviewtabrow-move-tab-window)
- `fxviewtabrow-move-tab-start` — `browser/browser/fxviewTabList.ftl` — fxviewtabrow-move-tab-start, fxviewtabrow-move-tab-end — fxviewTabList.ftl — "Verplaatsen naar Start" / "naar Einde" → "naar begin" / "naar einde" (cf. move-to-start / move-to-end in tabContextMenu.ftl, and fxviewtabrow-move-tab-window)
- `genai-settings-chat-claude-links` — `browser/browser/genai.ftl` — "gebruiksbeleid" lowercased while the two other document names in the same sentence are capitalised.
- `menu-tools-extensions-and-themes` — `browser/browser/menubar.ftl` — "Extensies en Thema's" → "Extensies en thema's". (See also S-2.)
  - en-US: `"Extensies en thema's".`
- `launch-on-login-infobar-final-message` — `browser/browser/newtab/asrouter.ftl` — launch-on-login-infobar-message, launch-on-login-infobar-final-message — newtab/asrouter.ftl — "telkens dat" is not standard Dutch. Suggest: "telkens wanneer" (as in launch-options-spotlight-title-launch-on-login)
- `launch-on-login-infobar-message` — `browser/browser/newtab/asrouter.ftl` — launch-on-login-infobar-message, launch-on-login-infobar-final-message — newtab/asrouter.ftl — "telkens dat" is not standard Dutch. Suggest: "telkens wanneer" (as in launch-options-spotlight-title-launch-on-login)
- `newtab-privacy-message-daily-cap` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-info-5, newtab-privacy-message-daily-cap — newtab/newtab.ftl — plural subject with singular verb. Current: "…betekent…" → Suggest: "…betekenen…" (and -info-5: "across sites" → "op verschillende websites")
  - en-US: `-info-5`
- `newtab-privacy-message-info-5` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-info-5, newtab-privacy-message-daily-cap — newtab/newtab.ftl — plural subject with singular verb. Current: "…betekent…" → Suggest: "…betekenen…" (and -info-5: "across sites" → "op verschillende websites")
  - en-US: `-info-5`
- `newtab-privacy-message-promo-vpn-1` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-promo-vpn-1, -vpn-2 — newtab/newtab.ftl — missing article. Suggest: "Schakel de ingebouwde VPN in…" (cf. -vpn-3)
  - en-US: `-vpn-2`
- `newtab-privacy-message-streak` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-streak ([one]) — newtab/newtab.ftl — "in a row" dropped, "inmiddels" added. Suggest: "U bent { $count } dag op rij beschermd."
  - en-US: `[one]`
- `newtab-privacy-trackers-blocked-today` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-trackers-blocked-today ([one]) — newtab/newtab.ftl — the singular variant uses the plural noun, so the distinction is lost. Current: "Trackers vandaag geblokkeerd" → Suggest: "Tracker vandaag geblokkeerd"
  - en-US: `"Tracker vandaag geblokkeerd"`
- `newtab-search-box-handoff-input` — `browser/browser/newtab/newtab.ftl` — newtab/newtab.ftl — infinitive and imperative coordinated. Current: "Met { $engine } zoeken of voer adres in" → Suggest: "Zoek met { $engine } of voer adres in"
  - Current: `{ $engine }`
- `newtab-search-box-handoff-text` — `browser/browser/newtab/newtab.ftl` — newtab/newtab.ftl — infinitive and imperative coordinated. Current: "Met { $engine } zoeken of voer adres in" → Suggest: "Zoek met { $engine } of voer adres in"
  - Current: `{ $engine }`
- `newtab-section-unblock-topic` — `browser/browser/newtab/newtab.ftl` — missing preposition. Current: "Blokkering { $topic } opheffen" → Suggest: "Blokkering van { $topic } opheffen"
  - Current: `{ $topic }`
- `newtab-stocks-widget-menu-button` — `browser/browser/newtab/newtab.ftl` — newtab/newtab.ftl — "Opties voor Aandelenwidget" → lowercase
  - en-US: `lowercase`
- `newtab-wallpaper-suspension-bridge` — `browser/browser/newtab/newtab.ftl` — plural noun for a single image, and "full-suspension" mistranslated. Suggest: "Foto van een grijze hangbrug bij daglicht"
- `mr2022-onboarding-welcome-pin-subtitle` — `browser/browser/newtab/onboarding.ftl` — adverb wedged between verb and object. Current: "Start overal { -brand-short-name } met een enkele klik." → Suggest: "Start { -brand-short-name } overal met een enkele klik."
  - Current: `{ -brand-short-name }`
- `places-forward-button` — `browser/browser/places.ftl` — Current: "Vooruit gaan" → Suggest: "Vooruitgaan" (cf. sibling "Teruggaan")
  - en-US: `"Vooruitgaan"`
- `places-view-sortby-name` — `browser/browser/places.ftl` — places-view-sortby-name, -url, -date, -visit-count, -date-added, -last-modified — places.ftl — "Sorteren op Naam / Locatie / Meest recente bezoek / Bezoekteller / Toegevoegd / Laatst gewijzigd" → lowercase after "op" (cf. places-sortby-name)
- `policy-SkipTermsOfUse2` — `browser/browser/policies/policies-descriptions.ftl` — "(Ge)bruiksvoorwaarden" capitalised differently in its two sentences.
- `connection-proxy-option-wpad` — `browser/browser/preferences/connection.ftl` — "…voor Automatische detectie van webproxy…" → lowercase "automatische"
  - en-US: `lowercase "automatische"`
- `address-capture-save-doorhanger-description` — `browser/browser/preferences/formAutofill.ftl` — address-capture-save-doorhanger-description, passport-capture-save-doorhanger-description — browser/browser/preferences/formAutofill.ftl — anglicism "save to". Current: "Sla gegevens op naar { -brand-short-name }" → Suggest: "…op in { -brand-short-name }"
  - Current: `{ -brand-short-name }`
- `passport-capture-save-doorhanger-description` — `browser/browser/preferences/formAutofill.ftl` — address-capture-save-doorhanger-description, passport-capture-save-doorhanger-description — browser/browser/preferences/formAutofill.ftl — anglicism "save to". Current: "Sla gegevens op naar { -brand-short-name }" → Suggest: "…op in { -brand-short-name }"
  - Current: `{ -brand-short-name }`
- `browsing-media-control` — `browser/browser/preferences/preferences.ftl` — browsing-use-full-keyboard-navigation (.label), browsing-media-control (.label) — browser/browser/preferences/preferences.ftl — imperative among infinitive checkbox labels. Suggest: "De tab-toets gebruiken om…" / "Media beheren via toetsenbord…"
  - en-US: `.label`
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — browsing-use-full-keyboard-navigation (.label), browsing-media-control (.label) — browser/browser/preferences/preferences.ftl — imperative among infinitive checkbox labels. Suggest: "De tab-toets gebruiken om…" / "Media beheren via toetsenbord…"
  - en-US: `.label`
- `content-blocking-all-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
- `content-blocking-cross-site-cookies-in-all-windows2` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
- `content-blocking-isolate-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
- `preferences-default-zoom` — `browser/browser/preferences/preferences.ftl` — preferences-default-zoom-label, preferences-default-zoom, preferences-default-zoom-select (.aria-label) — preferences/preferences.ftl — Current: "Standaard zoom" → Suggest: "Standaardzoom" (the warning strings already write it closed)
  - en-US: `"Standaardzoom"`
- `preferences-default-zoom-label` — `browser/browser/preferences/preferences.ftl` — preferences-default-zoom-label, preferences-default-zoom, preferences-default-zoom-select (.aria-label) — preferences/preferences.ftl — Current: "Standaard zoom" → Suggest: "Standaardzoom" (the warning strings already write it closed)
  - en-US: `"Standaardzoom"`
- `preferences-default-zoom-select` — `browser/browser/preferences/preferences.ftl` — preferences-default-zoom-label, preferences-default-zoom, preferences-default-zoom-select (.aria-label) — preferences/preferences.ftl — Current: "Standaard zoom" → Suggest: "Standaardzoom" (the warning strings already write it closed)
  - en-US: `"Standaardzoom"`
- `preferences-doh-overview-default` — `browser/browser/preferences/preferences.ftl` — preferences-doh-setting-default (.label), preferences-doh-overview-default (.label) — preferences/preferences.ftl — Current: "Standaard bescherming" → Suggest: "Standaardbescherming"
  - en-US: `"Standaardbescherming"`
- `preferences-doh-setting-default` — `browser/browser/preferences/preferences.ftl` — preferences-doh-setting-default (.label), preferences-doh-overview-default (.label) — preferences/preferences.ftl — Current: "Standaard bescherming" → Suggest: "Standaardbescherming"
  - en-US: `"Standaardbescherming"`
- `preferences-text-zoom-override-warning2` — `browser/browser/preferences/preferences.ftl` — the verb must close the subordinate clause. Current: "…en uw standaardzoom is niet 100%, geven…" → Suggest: "…en uw standaardzoom niet 100% is, geven…" (the older -warning is correct)
  - en-US: `-warning`
- `sitedata-heading` — `browser/browser/preferences/preferences.ftl` — doubled conjunction. Suggest: "Uw cookies, geschiedenis, buffer, websitegegevens en meer beheren."
  - en-US: `.description`
- `sitedata-option-block-cross-site-cookies2` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
- `sitedata-option-block-cross-site-trackers` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
- `sitedata-option-block-cross-site-tracking-cookies` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
- `preonboarding-manage-and-read-header-v2` — `browser/browser/preonboarding.ftl` — "Gebruiksvoorwaarden en privacyverklaring" — "Privacyverklaring" is capitalised as a document title everywhere else in the file.
- `present-avatar-alt` — `browser/browser/profiles.ftl` — nonstandard spelling. Current: "Kado" → Suggest: "Cadeau" (also check cadeau-avatar siblings for consistency)
- `recently-closed-window-panel-tooltip` — `browser/browser/recentlyClosed.ftl` — the value renders as date and time, so "om" (which only introduces a clock time) is wrong. Suggest: "…, gesloten op { DATETIME(…) })"
- `add-engine-suggest-url` — `browser/browser/search.ftl` — missing articles; add-engine-url2 in the same file has them. Suggest: "…met %s op de plaats van de zoekterm (optioneel)"
- `protections-not-blocking-cookies-all` — `browser/browser/siteProtections.ftl` — protections-not-blocking-cookies-third-party (.title), protections-not-blocking-cookies-all (.title) — siteProtections.ftl — active phrasing where all "not blocking" siblings use the passive. Current: "Blokkeert cookies van derden niet" → Suggest: "Cookies van derden worden niet geblokkeerd" (cf. protections-not-blocking-fingerprinters, -cryptominers, -tracking-content, -social-media-trackers)
- `protections-not-blocking-cookies-third-party` — `browser/browser/siteProtections.ftl` — protections-not-blocking-cookies-third-party (.title), protections-not-blocking-cookies-all (.title) — siteProtections.ftl — active phrasing where all "not blocking" siblings use the passive. Current: "Blokkeert cookies van derden niet" → Suggest: "Cookies van derden worden niet geblokkeerd" (cf. protections-not-blocking-fingerprinters, -cryptominers, -tracking-content, -social-media-trackers)
- _…and 41 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `about-logins-import-report-no-change2` — `browser/browser/aboutLogins.ftl` — about-logins-import-report-row-description-no-change2, -modified2, about-logins-import-report-no-change2 — aboutLogins.ftl — "entry" rendered three ways in one file: "invoer" (= data input, wrong), "vermelding", "item".
  - en-US: `-modified2`
- `about-logins-import-report-row-description-no-change2` — `browser/browser/aboutLogins.ftl` — about-logins-import-report-row-description-no-change2, -modified2, about-logins-import-report-no-change2 — aboutLogins.ftl — "entry" rendered three ways in one file: "invoer" (= data input, wrong), "vermelding", "item".
  - en-US: `-modified2`
- `turn-on-scheduled-backups-error-default-dir-denied` — `browser/browser/backupSettings.ftl` — "back-upmap" while the file otherwise uses "reservekopie".
- `urlbar-result-action-switch-to-tabgroup` — `browser/browser/browser.ftl` — urlbar-result-action-switch-to-tabgroup, mr2022-onboarding-live-language-switch-to, firefoxview-opentabs-pinned-tab (.title) — "Switch to" rendered as "Omschakelen", "Overschakelen" and "Wisselen".
- `customkeys-dev-inspector` — `browser/browser/customkeys.ftl` — "DOM- en stijlcontrole" loses the tool name; cf. customkeys-dev-storage "Opslag-inspector".
- `firefoxview-opentabs-pinned-tab` — `browser/browser/firefoxView.ftl` — urlbar-result-action-switch-to-tabgroup, mr2022-onboarding-live-language-switch-to, firefoxview-opentabs-pinned-tab (.title) — "Switch to" rendered as "Omschakelen", "Overschakelen" and "Wisselen".
- `link-preview-first-time-setup-message` — `browser/browser/genai.ftl` — "belangrijkste punten" while link-preview-key-points-header, link-preview-setup-faster-next-time, link-preview-settings-key-points use "hoofdpunten".
- `ipprotection-summer-promo-offramp-default-browser-incentive-description` — `browser/browser/ipProtection.ftl` — "plaatsen" while the file uses "locaties".
- `menu-application-show-all` — `browser/browser/menubar.ftl` — "Toon alles" while pocket-panel-button-show-all and about-config-show-all use "Alles tonen".
  - en-US: `.label`
- `menu-view-enter-full-screen` — `browser/browser/menubar.ftl` — "Schermvullende weergave" while its siblings menu-view-exit-full-screen / menu-view-full-screen use "Volledig scherm".
- `newtab-custom-pocket-subtitle` — `browser/browser/newtab/newtab.ftl` — "samengesteld" vs "verzameld" in home-prefs-stories-header2.description, newtab-custom-stories-toggle.description.
- `newtab-custom-web-notifications-toggle` — `browser/browser/newtab/newtab.ftl` — newtab-custom-web-notifications-toggle (.description), newtab-topsites-hover-card-header — newtab/newtab.ftl — "Meldingen" vs "notificaties" in the same feature's own label.
  - en-US: `.description`
- `newtab-menu-section-unfollow-topic` — `browser/browser/newtab/newtab.ftl` — newtab-menu-section-unfollow-topic, newtab-section-unfollow-button — newtab/newtab.ftl — "Ontvolgen" (a non-standard neologism) vs "niet meer volgen" in newtab-menu-section-unfollow, newtab-section-unfollow-topic, newtab-section-toast-unfollow.
- `newtab-picture-header` — `browser/browser/newtab/newtab.ftl` — newtab-picture-header, newtab-picture-menu-hide-photo, newtab-picture-image-alt — newtab/newtab.ftl — "Afbeelding van de dag" vs "Foto van de dag" in newtab-picture-header-main, home-prefs-picture-header, newtab-custom-widget-picture-toggle, newtab-picture-menu-show-photo, newtab-picture-widget-menu-button — both shown side by side in the same widget.
- `newtab-picture-image-alt` — `browser/browser/newtab/newtab.ftl` — newtab-picture-header, newtab-picture-menu-hide-photo, newtab-picture-image-alt — newtab/newtab.ftl — "Afbeelding van de dag" vs "Foto van de dag" in newtab-picture-header-main, home-prefs-picture-header, newtab-custom-widget-picture-toggle, newtab-picture-menu-show-photo, newtab-picture-widget-menu-button — both shown side by side in the same widget.
- `newtab-picture-menu-hide-photo` — `browser/browser/newtab/newtab.ftl` — newtab-picture-header, newtab-picture-menu-hide-photo, newtab-picture-image-alt — newtab/newtab.ftl — "Afbeelding van de dag" vs "Foto van de dag" in newtab-picture-header-main, home-prefs-picture-header, newtab-custom-widget-picture-toggle, newtab-picture-menu-show-photo, newtab-picture-widget-menu-button — both shown side by side in the same widget.
- `newtab-section-unfollow-button` — `browser/browser/newtab/newtab.ftl` — newtab-menu-section-unfollow-topic, newtab-section-unfollow-button — newtab/newtab.ftl — "Ontvolgen" (a non-standard neologism) vs "niet meer volgen" in newtab-menu-section-unfollow, newtab-section-unfollow-topic, newtab-section-toast-unfollow.
- `newtab-sports-widget-match-aria-label-upcoming-suspended` — `browser/browser/newtab/newtab.ftl` — newtab-sports-widget-suspended vs newtab-sports-widget-match-aria-label-upcoming-suspended (.aria-label) — "Onderbroken" vs "opgeschort".
- `newtab-sports-widget-suspended` — `browser/browser/newtab/newtab.ftl` — newtab-sports-widget-suspended vs newtab-sports-widget-match-aria-label-upcoming-suspended (.aria-label) — "Onderbroken" vs "opgeschort".
- `newtab-topsites-hover-card-header` — `browser/browser/newtab/newtab.ftl` — newtab-custom-web-notifications-toggle (.description), newtab-topsites-hover-card-header — newtab/newtab.ftl — "Meldingen" vs "notificaties" in the same feature's own label.
  - en-US: `.description`
- `newtab-weather-opt-in-headline` — `browser/browser/newtab/newtab.ftl` — newtab-weather-opt-in-headline, newtab-widget-message-focus-forecasts-title, -body — newtab/newtab.ftl — "weersvoorspelling" vs "weersverwachting" elsewhere.
- `newtab-widget-message-focus-forecasts-title` — `browser/browser/newtab/newtab.ftl` — newtab-weather-opt-in-headline, newtab-widget-message-focus-forecasts-title, -body — newtab/newtab.ftl — "weersvoorspelling" vs "weersverwachting" elsewhere.
- `newtab-widget-timer-decrease-min` — `browser/browser/newtab/newtab.ftl` — newtab/newtab.ftl — mismatched verb pair ("verminderen" / "verlengen"). Suggest: "verkorten" / "verlengen".
- `create-backup-screen-2-all-list-2` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-list-2, create-backup-screen-2-all-list-2, fx-backup-confirmation-screen-easy-setup-item-text-3 — "betaalmethoden" vs "betalingsmethoden" in fxa-adoption-credit-cards-backup-title/-subtitle, policy-AutofillCreditCardEnabled.
- `create-backup-screen-2-easy-list-2` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-list-2, create-backup-screen-2-all-list-2, fx-backup-confirmation-screen-easy-setup-item-text-3 — "betaalmethoden" vs "betalingsmethoden" in fxa-adoption-credit-cards-backup-title/-subtitle, policy-AutofillCreditCardEnabled.
- `fx-backup-confirmation-screen-easy-setup-item-text-3` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-list-2, create-backup-screen-2-all-list-2, fx-backup-confirmation-screen-easy-setup-item-text-3 — "betaalmethoden" vs "betalingsmethoden" in fxa-adoption-credit-cards-backup-title/-subtitle, policy-AutofillCreditCardEnabled.
- `mr2-onboarding-start-browsing-button-label` — `browser/browser/newtab/onboarding.ftl` — mr2-onboarding-start-browsing-button-label, onboarding-genai-sidebar-secondary-button — "Beginnen met surfen" vs "Beginnen met browsen" elsewhere.
- `mr2022-onboarding-live-language-switch-to` — `browser/browser/newtab/onboarding.ftl` — urlbar-result-action-switch-to-tabgroup, mr2022-onboarding-live-language-switch-to, firefoxview-opentabs-pinned-tab (.title) — "Switch to" rendered as "Omschakelen", "Overschakelen" and "Wisselen".
- `onboarding-genai-sidebar-secondary-button` — `browser/browser/newtab/onboarding.ftl` — mr2-onboarding-start-browsing-button-label, onboarding-genai-sidebar-secondary-button — "Beginnen met surfen" vs "Beginnen met browsen" elsewhere.
- `restored-from-backup-success-no-checklist-subtitle` — `browser/browser/newtab/onboarding.ftl` — "back-ups" while the file otherwise uses "reservekopie".
- `origin-controls-toolbar-button-permission-needed` — `browser/browser/originControls.ftl` — "Machtiging benodigd" vs origin-controls-state-when-clicked "Toestemming nodig". (See also S-3.)
  - en-US: `.tooltiptext`
- `places-untag-bookmark` — `browser/browser/places.ftl` — "Tag verwijderen" while places-view-sort-col-tags, places-view-sortby-tags use "Labels".
- `policy-AllowedDomainsForApps` — `browser/browser/policies/policies-descriptions.ftl` — policy-AllowedDomainsForApps, policy-AutoLaunchProtocolsFromOrigins — imperative "Definieer …" while all other ~130 entries in the file use the infinitive.
- `policy-AutoLaunchProtocolsFromOrigins` — `browser/browser/policies/policies-descriptions.ftl` — policy-AllowedDomainsForApps, policy-AutoLaunchProtocolsFromOrigins — imperative "Definieer …" while all other ~130 entries in the file use the infinitive.
- `policy-DisableBuiltinPDFViewer` — `browser/browser/policies/policies-descriptions.ftl` — policy-DisableBuiltinPDFViewer vs policy-PDFjs — "PDF-viewer" vs "PDF-lezer" in adjacent policies.
- `policy-PDFjs` — `browser/browser/policies/policies-descriptions.ftl` — policy-DisableBuiltinPDFViewer vs policy-PDFjs — "PDF-viewer" vs "PDF-lezer" in adjacent policies.
- `permissions-exceptions-popup-window2` — `browser/browser/preferences/permissions.ftl` — permissions-exceptions-popup-window3 (.title) vs permissions-exceptions-popup-window2 — preferences/permissions.ftl — "Allowed Websites" as "Toegestane websites" vs "Websites met toestemming"; and -window3 uses "doorleidingen" where the whole tree otherwise uses "omleidingen" for third-party redirects (site-permissions-unblock-redirect, browser.ftl pop-up strings).
  - en-US: `.title`
- `permissions-exceptions-popup-window3` — `browser/browser/preferences/permissions.ftl` — permissions-exceptions-popup-window3 (.title) vs permissions-exceptions-popup-window2 — preferences/permissions.ftl — "Allowed Websites" as "Toegestane websites" vs "Websites met toestemming"; and -window3 uses "doorleidingen" where the whole tree otherwise uses "omleidingen" for third-party redirects (site-permissions-unblock-redirect, browser.ftl pop-up strings).
  - en-US: `.title`
- `content-blocking-and-isolating-etp-warning-description-4` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-warning-message (.message), content-blocking-and-isolating-etp-warning-description-4 — preferences/preferences.ftl — the quoted "Fix site issues" reference appears in three forms and matches neither real label (content-blocking-baseline-exceptions-3 "Grote problemen met de website verhelpen", content-blocking-convenience-exceptions-3 "Kleine problemen met de website oplossen…
  - en-US: `.message`
- `pane-experimental-search-results-header` — `browser/browser/preferences/preferences.ftl` — "Proceed with Caution" rendered differently from pane-experimental-subtitle ("Ga voorzichtig verder").
- `preferences-doh-enabled-detailed-desc-1` — `browser/browser/preferences/preferences.ftl` — "aanbieder" where all sibling DoH strings use "provider".
- `preferences-doh-overview-custom` — `browser/browser/preferences/preferences.ftl` — preferences-doh-overview-default, preferences-doh-overview-custom, preferences-doh-radio-default (.description), preferences-doh-radio-custom — preferences/preferences.ftl — "secure DNS" as "Veilige DNS" while preferences-doh-default-desc, -strict-desc, permissions-exceptions-manage-doh-desc, preferences-doh-fallback-label and preferences-doh-default-detailed-desc-1 use "Beveiligde DNS".
- `preferences-doh-overview-default` — `browser/browser/preferences/preferences.ftl` — preferences-doh-overview-default, preferences-doh-overview-custom, preferences-doh-radio-default (.description), preferences-doh-radio-custom — preferences/preferences.ftl — "secure DNS" as "Veilige DNS" while preferences-doh-default-desc, -strict-desc, permissions-exceptions-manage-doh-desc, preferences-doh-fallback-label and preferences-doh-default-detailed-desc-1 use "Beveiligde DNS".
- `preferences-doh-radio-custom` — `browser/browser/preferences/preferences.ftl` — preferences-doh-overview-default, preferences-doh-overview-custom, preferences-doh-radio-default (.description), preferences-doh-radio-custom — preferences/preferences.ftl — "secure DNS" as "Veilige DNS" while preferences-doh-default-desc, -strict-desc, permissions-exceptions-manage-doh-desc, preferences-doh-fallback-label and preferences-doh-default-detailed-desc-1 use "Beveiligde DNS".
- `preferences-doh-radio-default` — `browser/browser/preferences/preferences.ftl` — preferences-doh-overview-default, preferences-doh-overview-custom, preferences-doh-radio-default (.description), preferences-doh-radio-custom — preferences/preferences.ftl — "secure DNS" as "Veilige DNS" while preferences-doh-default-desc, -strict-desc, permissions-exceptions-manage-doh-desc, preferences-doh-fallback-label and preferences-doh-default-detailed-desc-1 use "Beveiligde DNS".
- `preferences-etp-custom-control-group` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-custom (.description) vs preferences-etp-custom-control-group (.description) — "beschermingsmaatregelen" vs "beschermingsinstellingen" for the same en-US string.
  - en-US: `.description`
- `preferences-etp-level-custom` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-custom (.description) vs preferences-etp-custom-control-group (.description) — "beschermingsmaatregelen" vs "beschermingsinstellingen" for the same en-US string.
  - en-US: `.description`
- `preferences-etp-level-warning-message` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-warning-message (.message), content-blocking-and-isolating-etp-warning-description-4 — preferences/preferences.ftl — the quoted "Fix site issues" reference appears in three forms and matches neither real label (content-blocking-baseline-exceptions-3 "Grote problemen met de website verhelpen", content-blocking-convenience-exceptions-3 "Kleine problemen met de website oplossen…
  - en-US: `.message`
- `preferences-text-zoom-override-warning` — `browser/browser/preferences/preferences.ftl` — preferences-text-zoom-override-warning, -warning2 (.message) — preferences/preferences.ftl — quote the option as "‘Alleen tekst zoomen’" but the actual checkbox preferences-zoom-text-only is "Alleen tekst inzoomen".
  - en-US: `-warning2`
- `related-settings-tabs-browsing-link` — `browser/browser/preferences/preferences.ftl` — points at a setting named "Browserindeling" (browser-layout-header2) but says "Browseropmaak aanpassen".
  - en-US: `.label`
- `security-privacy-issue-warning-safe-browsing` — `browser/browser/preferences/preferences.ftl` — English "scams" left untranslated; security-safe-browsing-warning uses "oplichting".
  - en-US: `.description`
- `barbell-avatar-tooltip` — `browser/browser/profiles.ftl` — briefcase-avatar-tooltip, craft-avatar-tooltip, barbell-avatar-tooltip, video-game-controller-avatar-tooltip (.tooltiptext) — profiles.ftl — each tooltip names the avatar differently from its own -avatar / -avatar-alt pair ("Aktetas" vs "Werkmap", "Handwerk" vs "Knutselen", "Barbell" vs "Halter", "Gamecontroller" vs "Videogamecontroller").
- `briefcase-avatar-tooltip` — `browser/browser/profiles.ftl` — briefcase-avatar-tooltip, craft-avatar-tooltip, barbell-avatar-tooltip, video-game-controller-avatar-tooltip (.tooltiptext) — profiles.ftl — each tooltip names the avatar differently from its own -avatar / -avatar-alt pair ("Aktetas" vs "Werkmap", "Handwerk" vs "Knutselen", "Barbell" vs "Halter", "Gamecontroller" vs "Videogamecontroller").
- `craft-avatar-tooltip` — `browser/browser/profiles.ftl` — briefcase-avatar-tooltip, craft-avatar-tooltip, barbell-avatar-tooltip, video-game-controller-avatar-tooltip (.tooltiptext) — profiles.ftl — each tooltip names the avatar differently from its own -avatar / -avatar-alt pair ("Aktetas" vs "Werkmap", "Handwerk" vs "Knutselen", "Barbell" vs "Halter", "Gamecontroller" vs "Videogamecontroller").
- `video-game-controller-avatar-tooltip` — `browser/browser/profiles.ftl` — briefcase-avatar-tooltip, craft-avatar-tooltip, barbell-avatar-tooltip, video-game-controller-avatar-tooltip (.tooltiptext) — profiles.ftl — each tooltip names the avatar differently from its own -avatar / -avatar-alt pair ("Aktetas" vs "Werkmap", "Handwerk" vs "Knutselen", "Barbell" vs "Halter", "Gamecontroller" vs "Videogamecontroller").
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — "advertentiebureaus" (ad agencies) where the identical paragraph cookie-tab-content in protections.ftl says "adverteerders".
- `select-translations-panel-unsupported-language-message-known` — `browser/browser/translations.ftl` — select-translations-panel-unsupported-language-message-known vs translations-panel-error-unsupported-hint-known — translations.ftl — the same en-US sentence is rendered "Sorry, we ondersteunen nog geen { $language }." and "Sorry, we ondersteunen het { $language } nog niet." Pick one (the article form is the more standard Dutch construction with language names).
- `translations-panel-error-unsupported-hint-known` — `browser/browser/translations.ftl` — select-translations-panel-unsupported-language-message-known vs translations-panel-error-unsupported-hint-known — translations.ftl — the same en-US sentence is rendered "Sorry, we ondersteunen nog geen { $language }." and "Sorry, we ondersteunen het { $language } nog niet." Pick one (the article form is the more standard Dutch construction with language names).
- `unified-extensions-mb-blocklist-warning-single` — `browser/browser/unifiedExtensions.ftl` — unifiedExtensions.ftl — "risicovol" vs "riskant" in -single2 / -multiple2 and unified-extensions-item-messagebar-softblocked.
  - en-US: `-single2`
- `about-debugging-setup-usb-disabled` — `devtools/client/aboutdebugging.ftl` — about-debugging-setup-usb-disabled, about-debugging-setup-usb-step-enable-debug2, about-debugging-sidebar — "debugging" vs "foutopsporing" for the same concept in one file.
- _…and 49 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `popup-trigger-redirect-menuitem` — `browser/browser/browser.ftl` — uses ‘…’ while its sibling popup-show-popup-menuitem and en-US both use “…”.
  - en-US: `.label`
- `ip-protection-vpn-upgrade-link-1` — `browser/browser/ipProtection.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — lost the trailing … that marks the item as opening a further page (en-US "Share Ideas and Feedback…").
- `july-jam-body` — `browser/browser/newtab/asrouter.ftl` — july-jam-body vs spotlight-peace-mind-body — newtab/asrouter.ftl — the same figure written "3.000" and "3000".
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — july-jam-body vs spotlight-peace-mind-body — newtab/asrouter.ftl — the same figure written "3.000" and "3000".
- `newtab-custom-weather-toggle` — `browser/browser/newtab/newtab.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `fx100-thank-you-subtitle` — `browser/browser/newtab/onboarding.ftl` — fx100-thank-you-subtitle vs fx100-upgrade-thank-you-body — newtab/onboarding.ftl — the same ordinal written "100ste" and "100e".
- `fx100-upgrade-thank-you-body` — `browser/browser/newtab/onboarding.ftl` — fx100-thank-you-subtitle vs fx100-upgrade-thank-you-body — newtab/onboarding.ftl — the same ordinal written "100ste" and "100e".
- `mr2022-onboarding-no-mobile-download-cta-text` — `browser/browser/newtab/onboarding.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `policy-DisableThirdPartyModuleBlocking` — `browser/browser/policies/policies-descriptions.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `policy-LegacyProfiles` — `browser/browser/policies/policies-descriptions.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `content-blocking-cross-site-tracking-cookies-plus-isolate` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-cookies (.label), content-blocking-cross-site-tracking-cookies-plus-isolate — preferences/preferences.ftl — same stray comma before "en".
  - en-US: `.label`
- `home-prefs-weather-description` — `browser/browser/preferences/preferences.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
- `preferences-doh-radio-default` — `browser/browser/preferences/preferences.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
- `preferences-doh-radio-off` — `browser/browser/preferences/preferences.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
- `sitedata-option-block-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-cookies (.label), content-blocking-cross-site-tracking-cookies-plus-isolate — preferences/preferences.ftl — same stray comma before "en".
  - en-US: `.label`
- `inactive-css-first-letter-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `inactive-css-first-line-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `pippki-reset-password-confirmation-message` — `security/manager/security/pippki/pippki.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `crashreporter-checkbox-send-report` — `toolkit/crashreporter/crashreporter.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
  - en-US: `.message`
- `about-httpsonly-explanation-continue` — `toolkit/toolkit/about/aboutHttpsOnlyError.ftl` — stray space before the final period.
- `about-processes-total-memory-size-changed` — `toolkit/toolkit/about/aboutProcesses.ftl` — a space between the number and its unit in two of the three, none in the third. (The space is correct Dutch; the third should match.)
- `about-processes-total-memory-size-no-change` — `toolkit/toolkit/about/aboutProcesses.ftl` — a space between the number and its unit in two of the three, none in the third. (The space is correct Dutch; the third should match.)
- `download-utils-time-pair` — `toolkit/toolkit/downloads/downloadUtils.ftl` — a space between the number and its unit in two of the three, none in the third. (The space is correct Dutch; the third should match.)
- `fp-certerror-not-yet-valid-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — stray space before the final period.

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (115)

- `about-logins-import-dialog-error-title` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-10
- `about-logins-import-report-page-title` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-10
- `breach-alert-text` — `browser/browser/aboutLogins.ftl` — fixed 2026-08-10
- `about-unloads-intro` — `browser/browser/aboutUnloads.ftl` — fixed 2026-08-10
- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — fixed 2026-08-10
- `smart-window-switched-tab-label` — `browser/browser/aiWindowContent.ftl` — fixed 2026-08-10
- `extension-firefox-alpenglow-description` — `browser/browser/appExtensionFields.ftl` — fixed 2026-08-10
- `appmenu-update-other-instance` — `browser/browser/appMenuNotifications.ftl` — fixed 2026-08-10
- `bookmarks-mobile-bookmarks-menu` — `browser/browser/browser.ftl` — fixed 2026-08-10
- `quickactions-cmd-manageai` — `browser/browser/browser.ftl` — fixed 2026-08-10
- `restore-session-startup-suggestion-button` — `browser/browser/browser.ftl` — fixed 2026-08-10
- `search-one-offs-context-open-new-tab` — `browser/browser/browser.ftl` — fixed 2026-08-10
- `main-context-menu-frame-add-bookmark` — `browser/browser/browserContext.ftl` — fixed 2026-08-10
- `main-context-menu-send-to-mobile-enable-sync2` — `browser/browser/browserContext.ftl` — fixed 2026-08-10
- `clear-data-for-site-cookies` — `browser/browser/clearDataForSite.ftl` — fixed 2026-08-10
- `sidebar-callout-survey-neutral` — `browser/browser/featureCallout.ftl` — fixed 2026-08-10
- `ipprotection-feature-introduction-description-private-browsing` — `browser/browser/ipProtection.ftl` — fixed 2026-08-10
- `fxa-adoption-addresses-backup-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-10
- `relay-50-masks-announcement-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-10
- `windows-10-eos-challenger-callout-title` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-10
- `windows-10-eos-feature-toast-subtitle` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-10
- `newtab-custom-wallpaper-title` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-10
- `newtab-privacy-message-info-2` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-10
- `newtab-privacy-message-promo-monitor-1` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-10
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-10
- `newtab-wallpaper-abstract-purple-green` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-10
- `newtab-wallpaper-reset` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-10
- `create-backup-screen-1-backup-body` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-10
- `mr2022-onboarding-colorway-description-playmaker` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-10
- `mr2022-onboarding-get-started-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-10
- `onboarding-live-language-installing` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-10
- `onboarding-live-language-waiting-button` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-10
- `onboarding-refresh-sync-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-10
- `smartwindow-sidebar-auto-open-callout-accepted-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-10
- `panic-button-thankyou-msg2` — `browser/browser/panelUI.ftl` — fixed 2026-08-10
- `policy-DisableDefaultBrowserAgent` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-10
- `policy-DisabledCiphers` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-10
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-10
- `policy-HttpAllowlist` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-10
- `policy-HttpsOnlyMode` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-10

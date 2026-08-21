# Firefox l10n QA — nl

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `f2e9b7fce093` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `37560db2354a` |
| **Previous run** | 2026-08-21 @ `a9b9a116b725` |
| **Mode** | incremental |
| **Strings reviewed this run** | 8 of 18,156 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

Also for nl: [android](android.md)

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
| Strings | 18,156 |
| Missing strings | 17 |
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
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

**17 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 3
- `browser/browser/aboutPrivateBrowsing.ftl` — 2
- `browser/browser/appmenu.ftl` — 2
- `browser/browser/menubar.ftl` — 2
- `browser/browser/preferences/preferences.ftl` — 2
- `browser/browser/aboutDialog.ftl` — 1
- `browser/browser/preferences/formAutofill.ftl` — 1
- `dom/chrome/accessibility/AccessFu.properties` — 1
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
| register | `formal` 3091 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (377)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 23 |
| 2 | Wrong content (says something other than the English) | 126 |
| 3 | Degraded language (grammar, spelling, terminology) | 198 |
| 4 | Cosmetic (typography, spacing) | 30 |

### A. Functional, markup, variables & plurals

- `about-logins-copy-password-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — about-logins-edit-login-os-auth-dialog-message-macosx, about-logins-reveal-password-os-auth-dialog-message-macosx, about-logins-copy-password-os-auth-dialog-message-macosx — browser/browser/aboutLogins.ftl — the comment says to supply only the reason, which macOS prefixes with "Firefox is trying to …". These are imperatives, so the resulting sentence breaks. Current: "bewerk de opgeslagen aanmeld…
    - Source: `copy the saved password`
    - Suggest: `…message2-macosx`
- `about-logins-edit-login-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — about-logins-edit-login-os-auth-dialog-message-macosx, about-logins-reveal-password-os-auth-dialog-message-macosx, about-logins-copy-password-os-auth-dialog-message-macosx — browser/browser/aboutLogins.ftl — the comment says to supply only the reason, which macOS prefixes with "Firefox is trying to …". These are imperatives, so the resulting sentence breaks. Current: "bewerk de opgeslagen aanmeld…
    - Source: `edit the saved login`
    - Suggest: `…message2-macosx`
- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — same defect in both plural variants: <span data-l10n-name="meta">(niet geïmporteerd)</span > → Suggest: </span>
    - Source: `{$count ->} [other] <span>Duplicate entries found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
- `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl` — double space before the second link (… of <a data-l10n-name="import-file-link">).
    - Source: `Select the plus sign button above to add a password now. You can also <a data-l10n-name="import-browser-link">import passwords from another browser</a> or <a data-l10n-name="import-file-link">from a file</a>.`
- `about-logins-reveal-password-os-auth-dialog-message-macosx` — `browser/browser/aboutLogins.ftl` — about-logins-edit-login-os-auth-dialog-message-macosx, about-logins-reveal-password-os-auth-dialog-message-macosx, about-logins-copy-password-os-auth-dialog-message-macosx — browser/browser/aboutLogins.ftl — the comment says to supply only the reason, which macOS prefixes with "Firefox is trying to …". These are imperatives, so the resulting sentence breaks. Current: "bewerk de opgeslagen aanmeld…
    - Source: `reveal the saved password`
    - Suggest: `…message2-macosx`
- `xpinstall-prompt-never-allow-and-report` — `browser/browser/addonNotifications.ftl` — Access key `m` of `xpinstall-prompt-never-allow-and-report` is not present in its label
    - Current: `m`
    - Source: `accesskey: R label: Report Suspicious Site`
    - The label is “Verdachte website rapporteren”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `contextual-manager-passwords-copy-password-os-auth-dialog-message-macosx` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-reveal-password-os-auth-dialog-message-macosx, contextual-manager-passwords-copy-password-os-auth-dialog-message-macosx — browser/browser/contextual-manager.ftl — same defect; …edit-password-os-auth-dialog-message-macosx in the same file is correct.
    - Source: `copy the saved password`
- `contextual-manager-passwords-reveal-password-os-auth-dialog-message-macosx` — `browser/browser/contextual-manager.ftl` — contextual-manager-passwords-reveal-password-os-auth-dialog-message-macosx, contextual-manager-passwords-copy-password-os-auth-dialog-message-macosx — browser/browser/contextual-manager.ftl — same defect; …edit-password-os-auth-dialog-message-macosx in the same file is correct.
    - Source: `reveal the saved password`
- `tab-groups-2026-onboarding-cta-button` — `browser/browser/featureCallout.ftl` — the comment asks for "under ~15 characters so it fits in the callout UI"; "Een groep starten" is 17. Soft limit, worth a shorter form (e.g. "Groep starten").
    - Source: `Start a group`
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — malformed closing tag </a > (space inside the tag), so the second link will not render. Current: …generatieve AI</a > en de… → Suggest: …generatieve AI</a> en de…
    - Source: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
- `cfr-doorhanger-milestone-heading2` — `browser/browser/newtab/asrouter.ftl` — cfr-doorhanger-milestone-heading2 ([one] variant) — browser/browser/newtab/asrouter.ftl — the opening <b> is corrupted to b>, and "over" is dropped. Current: … b>{ $blockedCount }</b> tracker geblokkeerd! → Suggest: … meer dan <b>{ $blockedCount }</b> tracker geblokkeerd!
    - Source: `{$blockedCount ->} [other] { -brand-short-name } blocked over <b>{ $blockedCount }</b> trackers since { $date }!`
- `return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — double space around <img data-l10n-name="icon"/>.
    - Source: `Now let’s get you <img data-l10n-name="icon"/> <b>{ $addon-name }</b>.`
- `settings-translations-subpage-never-translate-sites-description` — `browser/browser/preferences/preferences.ftl` — double space after <img data-l10n-name="translations-icon"/>.
    - Source: `To add a site, open the <img data-l10n-name="translations-icon"/> translation panel, select <img data-l10n-name="settings-icon"/> translation settings, then choose “Never translate this site”`
- `protections-vpn-header-content-subscribed` — `browser/browser/protections.ftl` — stray space inside the link text, producing a trailing underlined space. Current: <a data-l10n-name="appstore-link">Apple App Store </a> → Suggest: …Apple App Store</a>
    - Source: `{$count ->} [other] Using the { -mozilla-vpn-brand-name } encrypts all your traffic and hides your location — on up to { $count } devices. Get the most from your subscription — add it from the <a data-l10n-name="playsto…`
- `inactive-css-not-grid-or-flex-container-or-multicol-container-fix` — `devtools/client/tooltips.ftl` — the CSS keyword inside <strong> is misspelled, so the suggested fix is wrong code. Current: <strong>colums:2</strong> → Suggest: <strong>columns:2</strong>
    - Source: `Try adding either <strong>display:grid</strong>, <strong>display:flex</strong>, or <strong>columns:2</strong>. { learn-more }`
- `inactive-css-not-grid-or-flex-container-or-multicol-container-fix` — `devtools/client/tooltips.ftl` — Also in this bucket: the CSS keyword items already listed in section A (inactive-css-not-grid-or-flex-container-or-multicol-container-fix, inactive-css-ruby-element-fix, webconsole-commands-usage-block).
    - Source: `Try adding either <strong>display:grid</strong>, <strong>display:flex</strong>, or <strong>columns:2</strong>. { learn-more }`
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — inactive-css-ruby-element-fix, inactive-css-ruby-element-fix-1 — devtools/client/tooltips.ftl — the CSS property name inside <strong> was translated, against the section's developer comment. Current: <strong>lettergrootte</strong> → Suggest: <strong>font-size</strong>
    - Source: `Try changing the <strong>font-size</strong> of the ruby text. { learn-more }`
- `inactive-css-ruby-element-fix` — `devtools/client/tooltips.ftl` — Also in this bucket: the CSS keyword items already listed in section A (inactive-css-not-grid-or-flex-container-or-multicol-container-fix, inactive-css-ruby-element-fix, webconsole-commands-usage-block).
    - Source: `Try changing the <strong>font-size</strong> of the ruby text. { learn-more }`
- `inactive-css-ruby-element-fix-1` — `devtools/client/tooltips.ftl` — inactive-css-ruby-element-fix, inactive-css-ruby-element-fix-1 — devtools/client/tooltips.ftl — the CSS property name inside <strong> was translated, against the section's developer comment. Current: <strong>lettergrootte</strong> → Suggest: <strong>font-size</strong>
    - Source: `Try changing the <strong>font-size</strong> of the ruby text.`
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — Also in this bucket: the CSS keyword items already listed in section A (inactive-css-not-grid-or-flex-container-or-multicol-container-fix, inactive-css-ruby-element-fix, webconsole-commands-usage-block).
    - Source: `:block URL_STRING  Start blocking network requests    It accepts only one URL_STRING argument, an unquoted string which will be used to block all requests whose URL includes this string.   Use :unblock or the Network Mo…`
- `addon-badge-line3` — `toolkit/toolkit/about/aboutAddons.ftl` — addon-badge-line3 (.title), addon-badge-line4 (.title) — toolkit/toolkit/about/aboutAddons.ftl — the dev comment states that "Mozilla" is hard-coded on purpose "because … we don't want forks to display 'by Fork'". nl adds "Firefox". Current: "Officiële door Mozilla Firefox gebouwde extensie." → Suggest: "Officiële door Mozilla gebouwde extensie."
    - Source: `aria-label: { addon-badge-line3.title } title: Official extension built by Mozilla. Meets security and performance standards`
    - Suggest: `"Officiële door Mozilla gebouwde extensie."`
- `addon-badge-line4` — `toolkit/toolkit/about/aboutAddons.ftl` — addon-badge-line3 (.title), addon-badge-line4 (.title) — toolkit/toolkit/about/aboutAddons.ftl — the dev comment states that "Mozilla" is hard-coded on purpose "because … we don't want forks to display 'by Fork'". nl adds "Firefox". Current: "Officiële door Mozilla Firefox gebouwde extensie." → Suggest: "Officiële door Mozilla gebouwde extensie."
    - Source: `title: Official extension built by Mozilla. Meets security and performance standards`
    - Suggest: `"Officiële door Mozilla gebouwde extensie."`
- `about-glean-profiler-explanation` — `toolkit/toolkit/about/aboutGlean.ftl` — both <q> items are literal Profiler UI labels; "Marker Chart" was kept but "Telemetry" was translated. Suggest: <q>Telemetry</q>
    - Current: `<q>`
    - Source: `To see a full view of all recorded metrics, you can use the { -profiler-brand-name }. First you must <a data-l10n-name="firefox-profiler-link">capture a performance profile</a>. Once you capture the profile, select <q>M…`
- `btp-warning-tracker-purged` — `toolkit/toolkit/global/antiTracking.ftl` — the dev comment says not to translate "bounce tracker"; nl closes it into one word here but keeps two in btp-warning-tracker-classified. Suggest: "bounce tracker" in both.
    - Source: `The state of “{ $siteHost }” was recently purged because it was detected as a bounce tracker.`

### B. Mistranslation, reversed meaning, wrong names & brand

- `profiler-popup-presets-ml-description` — `browser/browser/appmenu.ftl` — perftools-presets-ml-description2, profiler-popup-presets-ml-description — client/perftools.ftl, browser/browser/appmenu.ftl — "machine learning" became "machine translation". Suggest: "…bugs in machinaal leren…"
    - Source: `Preset for investigating machine learning bugs in { -brand-shorter-name }.`
- `other-backup-files-founds` — `browser/browser/backupSettings.ftl` — en-US "Note:". Current: "<b>Noot:</b>" → Suggest: "<b>Opmerking:</b>"
    - Source: `{$numberOfOtherBackupsFound ->} [one] <b>Note:</b> { $numberOfOtherBackupsFound } other backup file found [other] <b>Note:</b> { $numberOfOtherBackupsFound } other backup files found`
    - Suggest: `<b>`
- `enable-devtools-popup-description2` — `browser/browser/browser.ftl` — en-US "Browser Tools menu"; nl points at the "Extra" menu. Suggest: "…via het menu Browserhulpmiddelen…"
    - Source: `To use the F12 shortcut, first open DevTools via the Browser Tools menu.`
- `trustpanel-description-disabled` — `browser/browser/browser.ftl` — en-US "is off-duty", losing the contrast with trustpanel-header-enabled ("staat op wacht"). Current: "…heeft geen dienst." → Suggest: "…staat niet op wacht."
    - Source: `{ -brand-product-name } is off-duty. We suggest turning protections back on.`
    - Suggest: `"…staat niet op wacht."`
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — urlbar-result-action-search-actions, urlbar-placeholder-search-mode-other-actions (.aria-label) — browser.ftl — "Search" is a verb here. Current: "Zoekacties" → Suggest: "Acties doorzoeken" / "Zoeken in acties"
    - Source: `aria-label: Search actions placeholder: Enter search terms`
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — urlbar-result-action-search-actions, urlbar-placeholder-search-mode-other-actions (.aria-label) — browser.ftl — "Search" is a verb here. Current: "Zoekacties" → Suggest: "Acties doorzoeken" / "Zoeken in acties"
    - Source: `Search Actions`
- `customkeys-conflict-unusable-body` — `browser/browser/customkeys.ftl` — customkeys-conflict-unusable-title, customkeys-conflict-unusable-body — customkeys.ftl — "key" is a keyboard key, not a cryptographic key. Current: "Sleutel kan niet worden gebruikt" / "Deze sleutel wordt al gebruikt door…" → Suggest: "Toets kan niet worden gebruikt" / "Deze toets wordt al gebruikt door…" (cf. customkeys-conflict-confirm, which correctly uses "toets")
    - Source: `This key is already used by “{ $conflict }” and cannot be used.`
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — customkeys-conflict-unusable-title, customkeys-conflict-unusable-body — customkeys.ftl — "key" is a keyboard key, not a cryptographic key. Current: "Sleutel kan niet worden gebruikt" / "Deze sleutel wordt al gebruikt door…" → Suggest: "Toets kan niet worden gebruikt" / "Deze toets wordt al gebruikt door…" (cf. customkeys-conflict-confirm, which correctly uses "toets")
    - Source: `Key cannot be used`
- `windows-10-eos-sync-general-title-1` — `browser/browser/featureCallout.ftl` — en-US "the { -brand-short-name } you've made yours". Current: "…die u van u hebt gemaakt." → Suggest: "…die u zich eigen hebt gemaakt."
    - Current: `{ -brand-short-name }`
    - Source: `Protect the { -brand-short-name } you’ve made yours.`
    - Suggest: `"…die u zich eigen hebt gemaakt."`
- `genai-prompts-summarize` — `browser/browser/genai.ftl` — "concise" became "descriptive", nearly reversing the instruction. Current: "…in exacte en beschrijvende woorden." → Suggest: "…in precieze en beknopte woorden."
    - Source: `label: Summarize value: Please summarize the selection using precise and concise language. Use headers and bulleted lists in the summary, to make it scannable. Maintain the meaning and factual accuracy.`
    - Suggest: `"…in precieze en beknopte woorden."`
- `cfr-doorhanger-bookmark-fxa-body` — `browser/browser/newtab/asrouter.ftl` — "this bookmark" generalised. Suggest: "…dat u niet zonder deze bladwijzer zit…" (cf. -body-2)
    - Source: `Great find! Now don’t be left without this bookmark on your mobile devices. Get Started with a { -fxaccount-brand-name }.`
- `firefoxview-cfr-body-v2` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
    - Source: `Get recently closed tabs back, plus seamlessly hop between devices with { -firefoxview-brand-name }.`
- `fxa-menu-message-sync-devices-secondary-text` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
    - Source: `Instantly get your info — like bookmarks and passwords — everywhere you use { -brand-short-name }.`
- `fxa-menu-message-sync-devices-secondary-text2` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
    - Source: `Instantly get your bookmarks, passwords, and more — everywhere you’re signed in to { -brand-short-name }.`
- `set-default-menu-message-row-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
    - Source: `Get speed, safety and privacy every time you browse.`
- `set-default-menu-message-split-layout-subtitle` — `browser/browser/newtab/asrouter.ftl` — firefoxview-cfr-body-v2, set-default-menu-message-row-layout-subtitle, set-default-menu-message-split-layout-subtitle ([other]), fxa-menu-message-sync-devices-secondary-text, fxa-menu-message-sync-devices-secondary-text2 — newtab/asrouter.ftl — "Get" rendered as "Ontvang" (= receive), not idiomatic for these objects. Suggest: "Haal … terug", "Geniet van …", "Surf sneller met …", "Beschik direct o…
    - Source: `{$sel_1 ->} [macos] Make it your default and keep it in your Dock. [other] Get faster browsing and automatic privacy protection.`
- `windows-10-eos-sync-callout-privacy-screen-2-subtitle` — `browser/browser/newtab/asrouter.ftl` — "data and privacy settings" became "data settings and privacy settings". Suggest: "…om uw gegevens en privacyinstellingen mee te nemen."
    - Source: `Backing up { -brand-shorter-name } makes it easy to bring your data and privacy settings with you.`
- `home-prefs-highlights-option-most-recent-download-srd` — `browser/browser/newtab/newtab.ftl` — home-prefs-highlights-option-most-recent-download, home-prefs-highlights-option-most-recent-download-srd — preferences/preferences.ftl, newtab/newtab.ftl — noun phrase rendered as a participle. Current: "Meest recent gedownload" → Suggest: "Meest recente download"
    - Source: `label: Most recent download`
    - Suggest: `"Meest recente download"`
- `newtab-section-following-button` — `browser/browser/newtab/newtab.ftl` — newtab-section-following-button, newtab-section-unfollow-button-label (.aria-label) — newtab/newtab.ftl — "Volgend" means next. Current: "Volgend" → Suggest: "Gevolgd" (matches newtab-section-mangage-topics-followed-topics)
    - Source: `Following`
- `newtab-section-unfollow-button-label` — `browser/browser/newtab/newtab.ftl` — newtab-section-following-button, newtab-section-unfollow-button-label (.aria-label) — newtab/newtab.ftl — "Volgend" means next. Current: "Volgend" → Suggest: "Gevolgd" (matches newtab-section-mangage-topics-followed-topics)
    - Source: `aria-label: Following: Unfollow { $topic }`
- `newtab-widget-message-copy` — `browser/browser/newtab/newtab.ftl` — "stretch breaks" became "long breaks". Suggest: "…tot pauzes om te bewegen"
    - Source: `From quick reminders to daily to-dos, focus sessions to stretch breaks — stay on task and on time.`
- `newtab-widget-timer-label-play` — `browser/browser/newtab/newtab.ftl` — timer control, not media playback. Current: "Afspelen" → Suggest: "Starten"
    - Source: `label: Play`
    - Suggest: `"Starten"`
- `create-backup-screen-2-easy-label` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-label, mr2022-onboarding-import-header — newtab/onboarding.ftl — "setup" is configuration, not software installation. Current: "Eenvoudige instellingen" / "Razendsnelle installatie" → Suggest: "Eenvoudig instellen" / "Razendsnel instellen"
    - Source: `Easy setup`
- `mr2022-onboarding-import-header` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-label, mr2022-onboarding-import-header — newtab/onboarding.ftl — "setup" is configuration, not software installation. Current: "Eenvoudige instellingen" / "Razendsnelle installatie" → Suggest: "Eenvoudig instellen" / "Razendsnel instellen"
    - Source: `Lightning-fast setup`
- `onboarding-sign-up-description` — `browser/browser/newtab/onboarding.ftl` — "any device" weakened to "a device". Suggest: "…op een willekeurig apparaat…"
    - Source: `Sign up for an account and all of your important info — passwords, bookmarks, and more — will be securely stored and available when you sign in to any device.`
- `restored-from-backup-success-title` — `browser/browser/newtab/onboarding.ftl` — possessive dropped. Suggest: "We zijn terug! Uw { -brand-short-name }-gegevens zijn hersteld."
    - Source: `We’re back! Your { -brand-short-name } data has been restored.`
- `policy-DisableRemoteImprovements` — `browser/browser/policies/policies-descriptions.ftl` — "changes" dropped. Suggest: "…wijzigingen aan prestaties, stabiliteit en functies toepast…"
    - Source: `Prevent { -brand-short-name } from applying performance, stability, and feature changes between updates.`
- `policy-DisableSecurityBypass` — `browser/browser/policies/policies-descriptions.ftl` — "security warnings" became "security settings". Suggest: "…bepaalde beveiligingswaarschuwingen omzeilt."
    - Source: `Prevent the user from bypassing certain security warnings.`
- `policy-GoToIntranetSiteForSingleWordEntryInAddressBar` — `browser/browser/policies/policies-descriptions.ftl` — "single word entries" read as "a few words". Suggest: "…bij invoer van één woord in de adresbalk."
    - Source: `Force direct intranet site navigation instead of searching when typing single word entries in the address bar.`
- `containers-icon-briefcase` — `browser/browser/preferences/containers.ftl` — "Briefcase" is the depicted object. Current: "Werkmap" → Suggest: "Aktetas" (and align briefcase-avatar/briefcase-avatar-alt in profiles.ftl, which also say "Werkmap" while briefcase-avatar-tooltip says "Aktetas")
    - Source: `label: Briefcase`
- `permissions-searchbox` — `browser/browser/preferences/permissions.ftl` — the box filters the website list. Current: "Website doorzoeken" → Suggest: "Websites zoeken"
    - Source: `placeholder: Search Website`
    - Suggest: `"Websites zoeken"`
- `appearance-group2` — `browser/browser/preferences/preferences.ftl` — appearance-group2 (.label), preferences-web-appearance-header, web-appearance-group (.aria-label) — preferences/preferences.ftl — definite singular implies one specific site. Current: "Uiterlijk van de website" → Suggest: "Uiterlijk van websites"
    - Source: `description: Some websites change their colors to match your preferences. Choose your color scheme. label: Website appearance`
    - Suggest: `"Uiterlijk van websites"`
- `appearance-window-density-touch` — `browser/browser/preferences/preferences.ftl` — "and" became "such as". Current: "Grotere vensterelementen zoals klikdoelen" → Suggest: "Grotere vensterelementen en klikdoelen"
    - Source: `description: Larger window elements and click targets, optimized for touch screens label: Touch`
    - Suggest: `"Grotere vensterelementen en klikdoelen"`
- `home-prefs-highlights-option-most-recent-download` — `browser/browser/preferences/preferences.ftl` — home-prefs-highlights-option-most-recent-download, home-prefs-highlights-option-most-recent-download-srd — preferences/preferences.ftl, newtab/newtab.ftl — noun phrase rendered as a participle. Current: "Meest recent gedownload" → Suggest: "Meest recente download"
    - Source: `label: Most recent download`
    - Suggest: `"Meest recente download"`
- `pane-experimental-description4` — `browser/browser/preferences/preferences.ftl` — "evolving" became "in de groei"; the parallel -description3 uses "worden steeds beter".
    - Source: `Give our experimental features a try! They’re in development and evolving, which could impact how { -brand-short-name } works. We only receive data about your use of these features if you have <a data-l10n-name="data-co…`
- `permissions-header3` — `browser/browser/preferences/preferences.ftl` — en-US "Manage what websites can access…". Current: "Beheren welke websites kunnen benaderen, aansturen of starten." → Suggest: "Beheren wat websites kunnen benaderen, aansturen of starten."
    - Source: `description: Manage what websites can access, control, or trigger. label: Permissions`
    - Suggest: `"Beheren wat websites kunnen benaderen, aansturen of starten."`
- `preferences-etp-advanced-settings-group` — `browser/browser/preferences/preferences.ftl` — en-US "blocking most trackers automatically"; the qualifier is dropped. Suggest: "…waarbij de meeste trackers automatisch worden geblokkeerd"
    - Source: `description: Sites use trackers to follow you online and show creepy ads. { -brand-short-name } shields you as you browse, blocking most trackers automatically so you’re in control of your digital trail. label: Advanced…`
    - Suggest: `.description`
- `preferences-etp-level-standard` — `browser/browser/preferences/preferences.ftl` — the word is repeated, so the parenthesis conveys nothing. Current: "Standaard (standaard)" → Suggest: "Standaard (standaardinstelling)"
    - Source: `description: Strong, reliable protections that work smoothly with most websites. label: Standard (default)`
    - Suggest: `"Standaard`
- `preferences-web-appearance-header` — `browser/browser/preferences/preferences.ftl` — appearance-group2 (.label), preferences-web-appearance-header, web-appearance-group (.aria-label) — preferences/preferences.ftl — definite singular implies one specific site. Current: "Uiterlijk van de website" → Suggest: "Uiterlijk van websites"
    - Source: `Website appearance`
    - Suggest: `"Uiterlijk van websites"`
- `web-appearance-group` — `browser/browser/preferences/preferences.ftl` — appearance-group2 (.label), preferences-web-appearance-header, web-appearance-group (.aria-label) — preferences/preferences.ftl — definite singular implies one specific site. Current: "Uiterlijk van de website" → Suggest: "Uiterlijk van websites"
    - Source: `aria-label: Website appearance`
    - Suggest: `"Uiterlijk van websites"`
- `report-broken-site-panel-reason-adblocker-moz-box-button` — `browser/browser/reportBrokenSite.ftl` — report-broken-site-panel-reason-adblocker2 (.label), report-broken-site-panel-reason-adblocker-moz-box-button (.label) — reportBrokenSite.ftl — missing determiner. Current: "Website vroeg om adblocker uit te schakelen" → Suggest: "…om de adblocker uit te schakelen"
    - Source: `label: Site asked to turn off ad blocker`
    - Suggest: `"…om de adblocker uit te schakelen"`
- `report-broken-site-panel-reason-adblocker2` — `browser/browser/reportBrokenSite.ftl` — report-broken-site-panel-reason-adblocker2 (.label), report-broken-site-panel-reason-adblocker-moz-box-button (.label) — reportBrokenSite.ftl — missing determiner. Current: "Website vroeg om adblocker uit te schakelen" → Suggest: "…om de adblocker uit te schakelen"
    - Source: `label: Site asked to turn off ad blocker`
    - Suggest: `"…om de adblocker uit te schakelen"`
- `safeb-blocked-malware-page-error-desc-no-override-sumo` — `browser/browser/safebrowsing/blockedSite.ftl` — safeb-blocked-malware-page-short-desc, safeb-blocked-malware-page-error-desc-override-sumo, safeb-blocked-malware-page-error-desc-no-override-sumo — safebrowsing/blockedSite.ftl — kwaadwillend describes persons with ill intent, not software. Current: "kwaadwillende software" → Suggest: "kwaadaardige software"
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing malicious software</a>.`
    - Suggest: `"kwaadaardige software"`
- `safeb-blocked-malware-page-error-desc-override-sumo` — `browser/browser/safebrowsing/blockedSite.ftl` — safeb-blocked-malware-page-short-desc, safeb-blocked-malware-page-error-desc-override-sumo, safeb-blocked-malware-page-error-desc-no-override-sumo — safebrowsing/blockedSite.ftl — kwaadwillend describes persons with ill intent, not software. Current: "kwaadwillende software" → Suggest: "kwaadaardige software"
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing malicious software</a>. You can <a data-l10n-name='ignore_warning_link'>ignore the risk</a> and go…`
    - Suggest: `"kwaadaardige software"`
- `safeb-blocked-malware-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — safeb-blocked-malware-page-short-desc, safeb-blocked-malware-page-error-desc-override-sumo, safeb-blocked-malware-page-error-desc-no-override-sumo — safebrowsing/blockedSite.ftl — kwaadwillend describes persons with ill intent, not software. Current: "kwaadwillende software" → Suggest: "kwaadaardige software"
    - Source: `{ -brand-short-name } blocked this page because it might attempt to install malicious software that may steal or delete personal information on your computer.`
    - Suggest: `"kwaadaardige software"`
- `set-background-fill` — `browser/browser/setDesktopBackground.ftl` — uitvullen is the typographic term for justify. Current: "Uitvullen" → Suggest: "Vullen"
    - Source: `label: Fill`
    - Suggest: `"Vullen"`
- `duplicate-tab2` — `browser/browser/tabContextMenu.ftl` — duplicate-tab2 (.label), duplicate-tabs2 (.label) — tabContextMenu.ftl — noun instead of the menu verb. Current: "Duplicaat" → Suggest: "Dupliceren"
    - Source: `accesskey: D label: Duplicate`
    - Suggest: `"Dupliceren"`
- `duplicate-tabs2` — `browser/browser/tabContextMenu.ftl` — duplicate-tab2 (.label), duplicate-tabs2 (.label) — tabContextMenu.ftl — noun instead of the menu verb. Current: "Duplicaat" → Suggest: "Dupliceren"
    - Source: `accesskey: D label: Duplicate`
    - Suggest: `"Dupliceren"`
- `webrtc-sharing-menu` — `browser/browser/webrtcIndicator.ftl` — subject and object swapped. en-US "Tabs sharing devices". Current: "Apparaten die tabbladen delen" → Suggest: "Tabbladen die apparaten delen"
    - Source: `accesskey: d label: Tabs sharing devices`
    - Suggest: `"Tabbladen die apparaten delen"`
- `accessibility-best-practices` — `devtools/client/accessibility.ftl` — Current: "Goede voorbeelden" → Suggest: "Best practices"
    - Source: `alt: Best Practices`
    - Suggest: `"Best practices"`
- `accessibility-text-label-issue-heading` — `devtools/client/accessibility.ftl` — accessibility-text-label-issue-heading, -heading-content — client/accessibility.ftl — HTML headings are koppen, not kopteksten. Suggest: "Koppen moeten worden gelabeld."
    - Source: `Headings must be labeled. <a>Learn more</a>`
    - Suggest: `-heading-content`
- `session-history-entry-info-button-title` — `devtools/client/application.ftl` — "data" dropped. Suggest: "Sessiegeschiedenisgegevens tonen"
    - Source: `title: Show session history data`
    - Suggest: `.title`
- `perftools-presets-ml-description2` — `devtools/client/perftools.ftl` — perftools-presets-ml-description2, profiler-popup-presets-ml-description — client/perftools.ftl, browser/browser/appmenu.ftl — "machine learning" became "machine translation". Suggest: "…bugs in machinaal leren…"
    - Source: `Preset for investigating machine learning bugs in { -brand-shorter-name }.`
- `perftools-thread-compositor` — `devtools/client/perftools.ftl` — English word left mid-sentence. Current: "verschillende painted elementen" → Suggest: "verschillende getekende elementen"
    - Source: `title: Composites together different painted elements on the page`
    - Suggest: `"verschillende getekende elementen"`
- `perftools-thread-img-decoder` — `devtools/client/perftools.ftl` — decoding as decryption. Current: "Afbeeldingsontsleutelingsthreads" → Suggest: "Afbeeldingsdecoderingsthreads"
    - Source: `title: Image decoding threads`
    - Suggest: `"Afbeeldingsdecoderingsthreads"`
- `perftools-thread-timer` — `devtools/client/perftools.ftl` — subject/object swapped. en-US "The thread handling timers". Current: "De timers voor het afhandelen van threads…" → Suggest: "De thread die timers afhandelt…"
    - Source: `title: The thread handling timers (setTimeout, setInterval, nsITimer)`
    - Suggest: `"De thread die timers afhandelt…"`
- `styleeditor-pretty-print-button` — `devtools/client/styleeditor.ftl` — English left as an inverted noun phrase. Current: "Stylesheet Pretty Print" → Suggest: "Stijlblad opmaken"
    - Source: `title: Pretty print style sheet`
    - Suggest: `"Stijlblad opmaken"`
- `styleeditor-pretty-print-button-disabled` — `devtools/client/styleeditor.ftl` — styleeditor-pretty-print-button-disabled, -disabled-read-only — client/styleeditor.ftl — "pretty print" as mooi afdrukken (print nicely on paper). Suggest: "Kan alleen CSS-bestanden opmaken" / "Kan een alleen-lezen-stijlblad niet opmaken."
    - Source: `title: Can only pretty print CSS files`
    - Suggest: `-disabled-read-only`
- `options-enable-custom-formatters-label` — `devtools/client/toolbox-options.ftl` — options-enable-custom-formatters-label, options-enable-custom-formatters-tooltip — client/toolbox-options.ftl — formatters are functions, not elements. Current: "Aangepaste opmaakelementen" → Suggest: "Aangepaste formatters"
    - Source: `Enable custom formatters`
    - Suggest: `"Aangepaste formatters"`
- `options-enable-custom-formatters-tooltip` — `devtools/client/toolbox-options.ftl` — options-enable-custom-formatters-label, options-enable-custom-formatters-tooltip — client/toolbox-options.ftl — formatters are functions, not elements. Current: "Aangepaste opmaakelementen" → Suggest: "Aangepaste formatters"
    - Source: `title: Turning this option on will allow sites to define custom formatters for DOM objects`
    - Suggest: `"Aangepaste formatters"`
- _…and 65 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — "in de klassieke en Slimme Vensters" mixes a lone adjective with a plural brand term; en-US "in Classic and Smart Windows". Worth rewording.
    - Source: `label: Learn from browsing in Classic and { -smart-window-brand-name }`
    - Suggest: `.label`
- `aiwindow-ai-chat-grid-list-view` — `browser/browser/aiWindow.ftl` — "Modus wisselen: Lijstweergave" → lowercase (cf. -grid-view)
    - Source: `aria-label: Switch mode: List View tooltiptext: List View`
    - Suggest: `-grid-view`
- `toolbar-switcher-customizable-label` — `browser/browser/aiWindow.ftl` — toolbar-switcher-customizable-label (.tooltiptext) — aiWindow.ftl; smartwindow-switcher-callout — newtab/onboarding.ftl — mid-sentence "Slimme" capitalised in one half of a coordination only.
    - Source: `label: { -smart-window-brand-name } switcher tooltiptext: Switch between Smart and Classic windows.`
    - Suggest: `.tooltiptext`
- `aiwindow-manage-memories` — `browser/browser/aiWindowContent.ftl` — no hyphen between these two Dutch nouns. Current: "Herinnering-instellingen" → Suggest: "Herinneringsinstellingen"
    - Source: `label: Memory settings`
    - Suggest: `"Herinneringsinstellingen"`
- `smart-window-ungroup-success-summary` — `browser/browser/aiWindowContent.ftl` — smart-window-ungroup-success-summary, smart-window-ungrouped-row-label — aiWindowContent.ftl — "degroeperen" is not a Dutch verb. Current: "gedegroepeerd" → Suggest: "Groepering van { $count } tabbladen opgeheven" (cf. smart-window-grouped-and-ungrouped-label, which correctly uses "Groepering … ongedaan gemaakt")
    - Source: `{$count ->} [one] { $count } tab grouped, then ungrouped. [other] { $count } tabs grouped, then ungrouped.`
    - Suggest: `{ $count }`
- `smart-window-ungrouped-row-label` — `browser/browser/aiWindowContent.ftl` — smart-window-ungroup-success-summary, smart-window-ungrouped-row-label — aiWindowContent.ftl — "degroeperen" is not a Dutch verb. Current: "gedegroepeerd" → Suggest: "Groepering van { $count } tabbladen opgeheven" (cf. smart-window-grouped-and-ungrouped-label, which correctly uses "Groepering … ongedaan gemaakt")
    - Source: `{$count ->} [one] Ungrouped { $count } tab [other] Ungrouped { $count } tabs`
    - Suggest: `{ $count }`
- `fxa-menu-sync-status-off` — `browser/browser/appmenu.ftl` — fxa-menu-sync-status-on, fxa-menu-sync-status-off — appmenu.ftl — "Synchronisatie is Aan" / "is Uit" → lowercase
    - Source: `Sync is Off`
    - Suggest: `lowercase`
- `fxa-menu-sync-status-on` — `browser/browser/appmenu.ftl` — fxa-menu-sync-status-on, fxa-menu-sync-status-off — appmenu.ftl — "Synchronisatie is Aan" / "is Uit" → lowercase
    - Source: `Sync is On`
    - Suggest: `lowercase`
- `urlbar-result-explanation-last-visited-relative` — `browser/browser/browser.ftl` — $date is relative ("vandaag"). Current: "Uw laatste bezoek was op { $date }" → Suggest: drop "op" (keep it in …-last-visited-absolute)
    - Current: `{ $date }`
    - Source: `You last visited { $date }`
    - Suggest: `…-last-visited-absolute`
- `main-context-menu-link-send-to-mobile` — `browser/browser/browserContext.ftl` — main-context-menu-send-to-mobile-2, main-context-menu-link-send-to-mobile — browserContext.ftl; fxviewtabrow-send-to-mobile — fxviewTabList.ftl; tab-context-send-to-mobile ([1] variant) — tabContextMenu.ftl — "Naar Mobiel verzenden" → "Naar mobiel verzenden"; note tab-context-send-to-mobile is inconsistent within itself (only the [1] variant capitalises).
    - Source: `accesskey: n label: Send Link to Mobile`
- `main-context-menu-send-to-mobile-2` — `browser/browser/browserContext.ftl` — main-context-menu-send-to-mobile-2, main-context-menu-link-send-to-mobile — browserContext.ftl; fxviewtabrow-send-to-mobile — fxviewTabList.ftl; tab-context-send-to-mobile ([1] variant) — tabContextMenu.ftl — "Naar Mobiel verzenden" → "Naar mobiel verzenden"; note tab-context-send-to-mobile is inconsistent within itself (only the [1] variant capitalises).
    - Source: `accesskey: n label: Send to Mobile`
- `contextual-manager-passwords-no-passwords-message` — `browser/browser/contextual-manager.ftl` — calque of "watch out for". Suggest: "…en we letten op datalekken en waarschuwen u als u wordt getroffen."
    - Source: `All passwords are encrypted and we’ll watch out for breaches and alerts if you’re affected.`
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — defaultBrowserNotification.ftl — step sentences inconsistently capitalised after the colon, both between and within the two variants.
    - Source: `Step 1: Go to Settings > Default apps Step 2: Scroll down to “Web browser” Step 3: Select and choose { -brand-short-name }`
- `webext-quarantine-confirmation-line-2` — `browser/browser/extensionsUI.ftl` — missing second "te" in a coordinated infinitive. Suggest: "…te lezen en te wijzigen."
    - Source: `Allow this extension if you trust it to read and change your data on sites restricted by { -vendor-short-name }.`
- `fxviewtabrow-move-tab-end` — `browser/browser/fxviewTabList.ftl` — fxviewtabrow-move-tab-start, fxviewtabrow-move-tab-end — fxviewTabList.ftl — "Verplaatsen naar Start" / "naar Einde" → "naar begin" / "naar einde" (cf. move-to-start / move-to-end in tabContextMenu.ftl, and fxviewtabrow-move-tab-window)
    - Source: `(value): Move to End accesskey: E`
- `fxviewtabrow-move-tab-start` — `browser/browser/fxviewTabList.ftl` — fxviewtabrow-move-tab-start, fxviewtabrow-move-tab-end — fxviewTabList.ftl — "Verplaatsen naar Start" / "naar Einde" → "naar begin" / "naar einde" (cf. move-to-start / move-to-end in tabContextMenu.ftl, and fxviewtabrow-move-tab-window)
    - Source: `(value): Move to Start accesskey: S`
- `genai-settings-chat-claude-links` — `browser/browser/genai.ftl` — "gebruiksbeleid" lowercased while the two other document names in the same sentence are capitalised.
    - Source: `By choosing Anthropic Claude, you agree to the Anthropic <a data-l10n-name="link1">Consumer Terms of Service</a>, <a data-l10n-name="link2">Usage Policy</a>, and <a data-l10n-name="link3">Privacy Policy</a>.`
- `menu-tools-extensions-and-themes` — `browser/browser/menubar.ftl` — "Extensies en Thema's" → "Extensies en thema's". (See also S-2.)
    - Source: `accesskey: E label: Extensions and Themes`
    - Suggest: `"Extensies en thema's".`
- `launch-on-login-infobar-final-message` — `browser/browser/newtab/asrouter.ftl` — launch-on-login-infobar-message, launch-on-login-infobar-final-message — newtab/asrouter.ftl — "telkens dat" is not standard Dutch. Suggest: "telkens wanneer" (as in launch-options-spotlight-title-launch-on-login)
    - Source: `<strong>Open { -brand-short-name } every time you restart your computer?</strong> To manage your Startup preferences, search “startup” in settings.`
- `launch-on-login-infobar-message` — `browser/browser/newtab/asrouter.ftl` — launch-on-login-infobar-message, launch-on-login-infobar-final-message — newtab/asrouter.ftl — "telkens dat" is not standard Dutch. Suggest: "telkens wanneer" (as in launch-options-spotlight-title-launch-on-login)
    - Source: `<strong>Open { -brand-short-name } every time you restart your computer?</strong> Now you can set { -brand-short-name } to open automatically when you restart your device.`
- `newtab-privacy-message-daily-cap` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-info-5, newtab-privacy-message-daily-cap — newtab/newtab.ftl — plural subject with singular verb. Current: "…betekent…" → Suggest: "…betekenen…" (and -info-5: "across sites" → "op verschillende websites")
    - Source: `(100+ trackers blocked today.) Fewer trackers means more privacy.`
    - Suggest: `-info-5`
- `newtab-privacy-message-info-5` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-info-5, newtab-privacy-message-daily-cap — newtab/newtab.ftl — plural subject with singular verb. Current: "…betekent…" → Suggest: "…betekenen…" (and -info-5: "across sites" → "op verschillende websites")
    - Source: `Blocked trackers means fewer companies can follow you across sites.`
    - Suggest: `-info-5`
- `newtab-privacy-message-promo-vpn-1` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-promo-vpn-1, -vpn-2 — newtab/newtab.ftl — missing article. Suggest: "Schakel de ingebouwde VPN in…" (cf. -vpn-3)
    - Source: `Shopping on public Wi-Fi? Turn on built-in VPN for extra protection.`
    - Suggest: `-vpn-2`
- `newtab-privacy-message-streak` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-message-streak ([one]) — newtab/newtab.ftl — "in a row" dropped, "inmiddels" added. Suggest: "U bent { $count } dag op rij beschermd."
    - Source: `{$count ->} [one] You’ve been protected { $count } day in a row. [other] You’ve been protected { $count } days in a row.`
    - Suggest: `[one]`
- `newtab-privacy-trackers-blocked-today` — `browser/browser/newtab/newtab.ftl` — newtab-privacy-trackers-blocked-today ([one]) — newtab/newtab.ftl — the singular variant uses the plural noun, so the distinction is lost. Current: "Trackers vandaag geblokkeerd" → Suggest: "Tracker vandaag geblokkeerd"
    - Source: `{$count ->} [one] Tracker blocked today [other] Trackers blocked today`
    - Suggest: `"Tracker vandaag geblokkeerd"`
- `newtab-stocks-widget-menu-button` — `browser/browser/newtab/newtab.ftl` — newtab/newtab.ftl — "Opties voor Aandelenwidget" → lowercase
    - Source: `aria-label: Stocks widget options title: Stocks widget options`
    - Suggest: `lowercase`
- `newtab-wallpaper-suspension-bridge` — `browser/browser/newtab/newtab.ftl` — plural noun for a single image, and "full-suspension" mistranslated. Suggest: "Foto van een grijze hangbrug bij daglicht"
    - Source: `Grey full-suspension bridge photography during daytime`
- `places-forward-button` — `browser/browser/places.ftl` — Current: "Vooruit gaan" → Suggest: "Vooruitgaan" (cf. sibling "Teruggaan")
    - Source: `tooltiptext: Go forward`
    - Suggest: `"Vooruitgaan"`
- `places-view-sortby-name` — `browser/browser/places.ftl` — places-view-sortby-name, -url, -date, -visit-count, -date-added, -last-modified — places.ftl — "Sorteren op Naam / Locatie / Meest recente bezoek / Bezoekteller / Toegevoegd / Laatst gewijzigd" → lowercase after "op" (cf. places-sortby-name)
    - Source: `accesskey: N label: Sort by Name`
- `policy-SkipTermsOfUse2` — `browser/browser/policies/policies-descriptions.ftl` — "(Ge)bruiksvoorwaarden" capitalised differently in its two sentences.
    - Source: `Do not display the Terms of Use and Privacy Notice upon startup. You represent that you accept and have the authority to accept the Terms of Use on behalf of all individuals to whom you provide access to this browser.`
- `connection-proxy-option-wpad` — `browser/browser/preferences/connection.ftl` — "…voor Automatische detectie van webproxy…" → lowercase "automatische"
    - Source: `accesskey: g label: Use system Web Proxy Auto-Discovery setting`
    - Suggest: `lowercase "automatische"`
- `browsing-media-control` — `browser/browser/preferences/preferences.ftl` — browsing-use-full-keyboard-navigation (.label), browsing-media-control (.label) — browser/browser/preferences/preferences.ftl — imperative among infinitive checkbox labels. Suggest: "De tab-toets gebruiken om…" / "Media beheren via toetsenbord…"
    - Source: `accesskey: v label: Control media via keyboard, headset, or virtual interface`
    - Suggest: `.label`
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — browsing-use-full-keyboard-navigation (.label), browsing-media-control (.label) — browser/browser/preferences/preferences.ftl — imperative among infinitive checkbox labels. Suggest: "De tab-toets gebruiken om…" / "Media beheren via toetsenbord…"
    - Source: `accesskey: t label: Use the tab key to move focus between form controls and links`
    - Suggest: `.label`
- `content-blocking-all-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
    - Source: `All cross-site cookies`
- `content-blocking-cross-site-cookies-in-all-windows2` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
    - Source: `Cross-site cookies in all windows`
- `content-blocking-isolate-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
    - Source: `Isolate cross-site cookies`
- `preferences-default-zoom` — `browser/browser/preferences/preferences.ftl` — preferences-default-zoom-label, preferences-default-zoom, preferences-default-zoom-select (.aria-label) — preferences/preferences.ftl — Current: "Standaard zoom" → Suggest: "Standaardzoom" (the warning strings already write it closed)
    - Source: `(value): Default zoom accesskey: z`
    - Suggest: `"Standaardzoom"`
- `preferences-default-zoom-label` — `browser/browser/preferences/preferences.ftl` — preferences-default-zoom-label, preferences-default-zoom, preferences-default-zoom-select (.aria-label) — preferences/preferences.ftl — Current: "Standaard zoom" → Suggest: "Standaardzoom" (the warning strings already write it closed)
    - Source: `accesskey: z label: Default zoom`
    - Suggest: `"Standaardzoom"`
- `preferences-default-zoom-select` — `browser/browser/preferences/preferences.ftl` — preferences-default-zoom-label, preferences-default-zoom, preferences-default-zoom-select (.aria-label) — preferences/preferences.ftl — Current: "Standaard zoom" → Suggest: "Standaardzoom" (the warning strings already write it closed)
    - Source: `aria-label: Default zoom`
    - Suggest: `"Standaardzoom"`
- `preferences-doh-overview-default` — `browser/browser/preferences/preferences.ftl` — preferences-doh-setting-default (.label), preferences-doh-overview-default (.label) — preferences/preferences.ftl — Current: "Standaard bescherming" → Suggest: "Standaardbescherming"
    - Source: `description: Use secure DNS in regions where it’s available. label: Default protection`
    - Suggest: `"Standaardbescherming"`
- `preferences-doh-setting-default` — `browser/browser/preferences/preferences.ftl` — preferences-doh-setting-default (.label), preferences-doh-overview-default (.label) — preferences/preferences.ftl — Current: "Standaard bescherming" → Suggest: "Standaardbescherming"
    - Source: `accesskey: D label: Default Protection`
    - Suggest: `"Standaardbescherming"`
- `preferences-text-zoom-override-warning2` — `browser/browser/preferences/preferences.ftl` — the verb must close the subordinate clause. Current: "…en uw standaardzoom is niet 100%, geven…" → Suggest: "…en uw standaardzoom niet 100% is, geven…" (the older -warning is correct)
    - Source: `message: If “Zoom text only” is on and your default zoom isn’t 100%, some sites might not display content correctly.`
    - Suggest: `-warning`
- `sitedata-heading` — `browser/browser/preferences/preferences.ftl` — doubled conjunction. Suggest: "Uw cookies, geschiedenis, buffer, websitegegevens en meer beheren."
    - Source: `description: Manage your cookies, history, cache, website data, and more. label: Browsing data`
    - Suggest: `.description`
- `sitedata-option-block-cross-site-cookies2` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
    - Source: `label: Isolate cross-site cookies`
- `sitedata-option-block-cross-site-trackers` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
    - Source: `label: Cross-site trackers`
- `sitedata-option-block-cross-site-tracking-cookies` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-trackers, sitedata-option-block-cross-site-tracking-cookies, content-blocking-cross-site-cookies-in-all-windows2 vs sitedata-option-block-cross-site-cookies2, content-blocking-isolate-cross-site-cookies, content-blocking-all-cross-site-cookies — preferences/preferences.ftl — the same compound is hyphenated three different ways ("Cross-site-cookies", "Cross-site-tr…
    - Source: `label: Cross-site tracking cookies`
- `preonboarding-manage-and-read-header-v2` — `browser/browser/preonboarding.ftl` — "Gebruiksvoorwaarden en privacyverklaring" — "Privacyverklaring" is capitalised as a document title everywhere else in the file.
    - Source: `Read Terms of Use and Privacy Notice. Manage additional settings.`
- `present-avatar-alt` — `browser/browser/profiles.ftl` — nonstandard spelling. Current: "Kado" → Suggest: "Cadeau" (also check cadeau-avatar siblings for consistency)
    - Source: `alt: Present`
- `recently-closed-window-panel-tooltip` — `browser/browser/recentlyClosed.ftl` — the value renders as date and time, so "om" (which only introduces a clock time) is wrong. Suggest: "…, gesloten op { DATETIME(…) })"
    - Source: `{$tabCount ->} [0] { $winTitle } [one] { $winTitle } ({ $tabCount } tab, closed at { $closedAt }) [other] { $winTitle } ({ $tabCount } tabs, closed at { $closedAt })`
- `add-engine-suggest-url` — `browser/browser/search.ftl` — missing articles; add-engine-url2 in the same file has them. Suggest: "…met %s op de plaats van de zoekterm (optioneel)"
    - Source: `Suggestions URL with %s in place of search term (optional)`
- `protections-not-blocking-cookies-all` — `browser/browser/siteProtections.ftl` — protections-not-blocking-cookies-third-party (.title), protections-not-blocking-cookies-all (.title) — siteProtections.ftl — active phrasing where all "not blocking" siblings use the passive. Current: "Blokkeert cookies van derden niet" → Suggest: "Cookies van derden worden niet geblokkeerd" (cf. protections-not-blocking-fingerprinters, -cryptominers, -tracking-content, -social-media-trackers)
    - Source: `title: Not Blocking Cookies`
- `protections-not-blocking-cookies-third-party` — `browser/browser/siteProtections.ftl` — protections-not-blocking-cookies-third-party (.title), protections-not-blocking-cookies-all (.title) — siteProtections.ftl — active phrasing where all "not blocking" siblings use the passive. Current: "Blokkeert cookies van derden niet" → Suggest: "Cookies van derden worden niet geblokkeerd" (cf. protections-not-blocking-fingerprinters, -cryptominers, -tracking-content, -social-media-trackers)
    - Source: `title: Not Blocking Third-Party Cookies`
- `tab-context-separate-split-view` — `browser/browser/tabbrowser.ftl` — two verbs for the same "Separate" action in one file. Current: "Gesplitste weergave afzonderen" → Suggest: "Gesplitste weergave scheiden" (cf. split-view-menuitem-separate-tabs)
    - Source: `accesskey: t label: Separate Split View`
- `select-translations-panel-from-label` — `browser/browser/translations.ftl` — its pair select-translations-panel-to-label is "Naar het", which carries the article the following language name needs. Current: "Van" → Suggest: "Van het" (cf. translations-panel-from-label / -to-label)
    - Source: `From`
- `unified-extensions-mb-blocklist-warning-single` — `browser/browser/unifiedExtensions.ftl` — unified-extensions-mb-blocklist-warning-single (.message), -single2 (.message) — browser/browser/unifiedExtensions.ftl — masculine pronoun for "extensie". Current: "U kunt hem inschakelen…" → Suggest: "U kunt deze inschakelen…" (the plural variants correctly use "ze")
    - Source: `heading: { $extensionName } disabled message: This extension violates Mozilla’s policies and has been disabled. You can enable it in settings, but this may be risky.`
    - Suggest: `"U kunt deze inschakelen…"`
- `about-debugging-setup-usb-step-enable-file-transfer` — `devtools/client/aboutdebugging.ftl` — about-debugging-setup-usb-step-enable-file-transfer, about-debugging-setup-usb-step-plug-device — devtools/client/aboutdebugging.ftl — two of five step instructions switch to the imperative. Suggest: align with -enable-dev-menu2, -enable-debug2, -enable-debug-firefox2 (infinitive).
    - Source: `Enable file transfer and ensure that your device is not in charging-only mode.`
- `about-debugging-setup-usb-step-plug-device` — `devtools/client/aboutdebugging.ftl` — about-debugging-setup-usb-step-enable-file-transfer, about-debugging-setup-usb-step-plug-device — devtools/client/aboutdebugging.ftl — two of five step instructions switch to the imperative. Suggest: align with -enable-dev-menu2, -enable-debug2, -enable-debug-firefox2 (infinitive).
    - Source: `Connect the Android device to your computer.`
- `styleeditor-go-to-line` — `devtools/client/styleeditor.ftl` — imperative among infinitive menu labels. Current: "Spring naar regel…" → Suggest: "Naar regel springen…"
    - Source: `accesskey: J label: Jump to Line…`
    - Suggest: `"Naar regel springen…"`
- `whypaused-get-watchpoint` — `devtools/shared/debugger-paused-reasons.ftl` — devtools/shared/debugger-paused-reasons.ftl — the get/set pair is broken: one translated, one keeps the English keyword. Suggest: "Gepauzeerd bij property get" / "Gepauzeerd bij property set"
    - Source: `Paused on property get`
- `whypaused-set-watchpoint` — `devtools/shared/debugger-paused-reasons.ftl` — devtools/shared/debugger-paused-reasons.ftl — the get/set pair is broken: one translated, one keeps the English keyword. Suggest: "Gepauzeerd bij property get" / "Gepauzeerd bij property set"
    - Source: `Paused on property set`
- _…and 29 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `about-logins-import-report-no-change2` — `browser/browser/aboutLogins.ftl` — about-logins-import-report-row-description-no-change2, -modified2, about-logins-import-report-no-change2 — aboutLogins.ftl — "entry" rendered three ways in one file: "invoer" (= data input, wrong), "vermelding", "item".
    - Source: `{$count ->} [other] <div data-l10n-name="count">{ $count }</div> <div data-l10n-name="details">Duplicate entries</div> <div data-l10n-name="not-imported">(not imported)</div>`
    - Suggest: `-modified2`
- `about-logins-import-report-row-description-no-change2` — `browser/browser/aboutLogins.ftl` — about-logins-import-report-row-description-no-change2, -modified2, about-logins-import-report-no-change2 — aboutLogins.ftl — "entry" rendered three ways in one file: "invoer" (= data input, wrong), "vermelding", "item".
    - Source: `Duplicate: Exact match of existing entry`
    - Suggest: `-modified2`
- `turn-on-scheduled-backups-error-default-dir-denied` — `browser/browser/backupSettings.ftl` — "back-upmap" while the file otherwise uses "reservekopie".
    - Source: `We couldn’t access your backup folder. Try picking a new location.`
- `urlbar-result-action-switch-to-tabgroup` — `browser/browser/browser.ftl` — urlbar-result-action-switch-to-tabgroup, mr2022-onboarding-live-language-switch-to, firefoxview-opentabs-pinned-tab (.title) — "Switch to" rendered as "Omschakelen", "Overschakelen" and "Wisselen".
    - Source: `Switch to { $group }`
- `customkeys-dev-inspector` — `browser/browser/customkeys.ftl` — "DOM- en stijlcontrole" loses the tool name; cf. customkeys-dev-storage "Opslag-inspector".
    - Source: `DOM and Style Inspector`
- `firefoxview-opentabs-pinned-tab` — `browser/browser/firefoxView.ftl` — urlbar-result-action-switch-to-tabgroup, mr2022-onboarding-live-language-switch-to, firefoxview-opentabs-pinned-tab (.title) — "Switch to" rendered as "Omschakelen", "Overschakelen" and "Wisselen".
    - Source: `title: Switch to { $tabTitle }`
- `link-preview-first-time-setup-message` — `browser/browser/genai.ftl` — "belangrijkste punten" while link-preview-key-points-header, link-preview-setup-faster-next-time, link-preview-settings-key-points use "hoofdpunten".
    - Source: `This may take a moment. You’ll see key points more quickly next time.`
- `ipprotection-summer-promo-offramp-default-browser-incentive-description` — `browser/browser/ipProtection.ftl` — "plaatsen" while the file uses "locaties".
    - Source: `Make { -brand-product-name } your go-to browser and get more than 20 extra places to browse from after August 31.`
- `menu-application-show-all` — `browser/browser/menubar.ftl` — "Toon alles" while pocket-panel-button-show-all and about-config-show-all use "Alles tonen".
    - Source: `label: Show All`
    - Suggest: `.label`
- `menu-view-enter-full-screen` — `browser/browser/menubar.ftl` — "Schermvullende weergave" while its siblings menu-view-exit-full-screen / menu-view-full-screen use "Volledig scherm".
    - Source: `accesskey: F label: Enter Full Screen`
- `newtab-custom-pocket-subtitle` — `browser/browser/newtab/newtab.ftl` — "samengesteld" vs "verzameld" in home-prefs-stories-header2.description, newtab-custom-stories-toggle.description.
    - Source: `Exceptional content curated by { -pocket-brand-name }, part of the { -brand-product-name } family`
- `newtab-custom-web-notifications-toggle` — `browser/browser/newtab/newtab.ftl` — newtab-custom-web-notifications-toggle (.description), newtab-topsites-hover-card-header — newtab/newtab.ftl — "Meldingen" vs "notificaties" in the same feature's own label.
    - Source: `description: Show notifications from your sites on their shortcuts label: Web notifications`
    - Suggest: `.description`
- `newtab-menu-section-unfollow-topic` — `browser/browser/newtab/newtab.ftl` — newtab-menu-section-unfollow-topic, newtab-section-unfollow-button — newtab/newtab.ftl — "Ontvolgen" (a non-standard neologism) vs "niet meer volgen" in newtab-menu-section-unfollow, newtab-section-unfollow-topic, newtab-section-toast-unfollow.
    - Source: `Unfollow`
- `newtab-picture-header` — `browser/browser/newtab/newtab.ftl` — newtab-picture-header, newtab-picture-menu-hide-photo, newtab-picture-image-alt — newtab/newtab.ftl — "Afbeelding van de dag" vs "Foto van de dag" in newtab-picture-header-main, home-prefs-picture-header, newtab-custom-widget-picture-toggle, newtab-picture-menu-show-photo, newtab-picture-widget-menu-button — both shown side by side in the same widget.
    - Source: `Picture of the day · Wikimedia Commons`
- `newtab-picture-image-alt` — `browser/browser/newtab/newtab.ftl` — newtab-picture-header, newtab-picture-menu-hide-photo, newtab-picture-image-alt — newtab/newtab.ftl — "Afbeelding van de dag" vs "Foto van de dag" in newtab-picture-header-main, home-prefs-picture-header, newtab-custom-widget-picture-toggle, newtab-picture-menu-show-photo, newtab-picture-widget-menu-button — both shown side by side in the same widget.
    - Source: `Wikimedia Commons picture of the day`
- `newtab-picture-menu-hide-photo` — `browser/browser/newtab/newtab.ftl` — newtab-picture-header, newtab-picture-menu-hide-photo, newtab-picture-image-alt — newtab/newtab.ftl — "Afbeelding van de dag" vs "Foto van de dag" in newtab-picture-header-main, home-prefs-picture-header, newtab-custom-widget-picture-toggle, newtab-picture-menu-show-photo, newtab-picture-widget-menu-button — both shown side by side in the same widget.
    - Source: `Hide today’s picture`
- `newtab-section-unfollow-button` — `browser/browser/newtab/newtab.ftl` — newtab-menu-section-unfollow-topic, newtab-section-unfollow-button — newtab/newtab.ftl — "Ontvolgen" (a non-standard neologism) vs "niet meer volgen" in newtab-menu-section-unfollow, newtab-section-unfollow-topic, newtab-section-toast-unfollow.
    - Source: `Unfollow`
- `newtab-sports-widget-match-aria-label-upcoming-suspended` — `browser/browser/newtab/newtab.ftl` — newtab-sports-widget-suspended vs newtab-sports-widget-match-aria-label-upcoming-suspended (.aria-label) — "Onderbroken" vs "opgeschort".
    - Source: `aria-label: { $homeTeam } vs. { $awayTeam }, suspended`
- `newtab-sports-widget-suspended` — `browser/browser/newtab/newtab.ftl` — newtab-sports-widget-suspended vs newtab-sports-widget-match-aria-label-upcoming-suspended (.aria-label) — "Onderbroken" vs "opgeschort".
    - Source: `Suspended`
- `newtab-topsites-hover-card-header` — `browser/browser/newtab/newtab.ftl` — newtab-custom-web-notifications-toggle (.description), newtab-topsites-hover-card-header — newtab/newtab.ftl — "Meldingen" vs "notificaties" in the same feature's own label.
    - Source: `Notifications from { $site }`
    - Suggest: `.description`
- `newtab-weather-opt-in-headline` — `browser/browser/newtab/newtab.ftl` — newtab-weather-opt-in-headline, newtab-widget-message-focus-forecasts-title, -body — newtab/newtab.ftl — "weersvoorspelling" vs "weersverwachting" elsewhere.
    - Source: `Get your local weather forecast`
- `newtab-widget-message-focus-forecasts-title` — `browser/browser/newtab/newtab.ftl` — newtab-weather-opt-in-headline, newtab-widget-message-focus-forecasts-title, -body — newtab/newtab.ftl — "weersvoorspelling" vs "weersverwachting" elsewhere.
    - Source: `One spot for focus, forecasts, and more`
- `newtab-widget-timer-decrease-min` — `browser/browser/newtab/newtab.ftl` — newtab/newtab.ftl — mismatched verb pair ("verminderen" / "verlengen"). Suggest: "verkorten" / "verlengen".
    - Source: `title: Decrease 1 minute`
- `create-backup-screen-2-all-list-2` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-list-2, create-backup-screen-2-all-list-2, fx-backup-confirmation-screen-easy-setup-item-text-3 — "betaalmethoden" vs "betalingsmethoden" in fxa-adoption-credit-cards-backup-title/-subtitle, policy-AutofillCreditCardEnabled.
    - Source: `Includes passwords and payments`
- `create-backup-screen-2-easy-list-2` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-list-2, create-backup-screen-2-all-list-2, fx-backup-confirmation-screen-easy-setup-item-text-3 — "betaalmethoden" vs "betalingsmethoden" in fxa-adoption-credit-cards-backup-title/-subtitle, policy-AutofillCreditCardEnabled.
    - Source: `Doesn’t include passwords and payments`
- `fx-backup-confirmation-screen-easy-setup-item-text-3` — `browser/browser/newtab/onboarding.ftl` — create-backup-screen-2-easy-list-2, create-backup-screen-2-all-list-2, fx-backup-confirmation-screen-easy-setup-item-text-3 — "betaalmethoden" vs "betalingsmethoden" in fxa-adoption-credit-cards-backup-title/-subtitle, policy-AutofillCreditCardEnabled.
    - Source: `Passwords and payments not included`
- `mr2-onboarding-start-browsing-button-label` — `browser/browser/newtab/onboarding.ftl` — mr2-onboarding-start-browsing-button-label, onboarding-genai-sidebar-secondary-button — "Beginnen met surfen" vs "Beginnen met browsen" elsewhere.
    - Source: `Start browsing`
- `mr2022-onboarding-live-language-switch-to` — `browser/browser/newtab/onboarding.ftl` — urlbar-result-action-switch-to-tabgroup, mr2022-onboarding-live-language-switch-to, firefoxview-opentabs-pinned-tab (.title) — "Switch to" rendered as "Omschakelen", "Overschakelen" and "Wisselen".
    - Source: `Switch to { $negotiatedLanguage }`
- `onboarding-genai-sidebar-secondary-button` — `browser/browser/newtab/onboarding.ftl` — mr2-onboarding-start-browsing-button-label, onboarding-genai-sidebar-secondary-button — "Beginnen met surfen" vs "Beginnen met browsen" elsewhere.
    - Source: `Start browsing`
- `restored-from-backup-success-no-checklist-subtitle` — `browser/browser/newtab/onboarding.ftl` — "back-ups" while the file otherwise uses "reservekopie".
    - Source: `You can turn backup on for this device in <a data-l10n-name="settings">Settings</a>.`
- `origin-controls-toolbar-button-permission-needed` — `browser/browser/originControls.ftl` — "Machtiging benodigd" vs origin-controls-state-when-clicked "Toestemming nodig". (See also S-3.)
    - Source: `label: { $extensionTitle } tooltiptext: { $extensionTitle } Permission needed`
    - Suggest: `.tooltiptext`
- `places-untag-bookmark` — `browser/browser/places.ftl` — "Tag verwijderen" while places-view-sort-col-tags, places-view-sortby-tags use "Labels".
    - Source: `accesskey: R label: Remove Tag`
- `policy-AllowedDomainsForApps` — `browser/browser/policies/policies-descriptions.ftl` — policy-AllowedDomainsForApps, policy-AutoLaunchProtocolsFromOrigins — imperative "Definieer …" while all other ~130 entries in the file use the infinitive.
    - Source: `Define domains allowed to access Google Workspace.`
- `policy-AutoLaunchProtocolsFromOrigins` — `browser/browser/policies/policies-descriptions.ftl` — policy-AllowedDomainsForApps, policy-AutoLaunchProtocolsFromOrigins — imperative "Definieer …" while all other ~130 entries in the file use the infinitive.
    - Source: `Define a list of external protocols that can be used from listed origins without prompting the user.`
- `policy-DisableBuiltinPDFViewer` — `browser/browser/policies/policies-descriptions.ftl` — policy-DisableBuiltinPDFViewer vs policy-PDFjs — "PDF-viewer" vs "PDF-lezer" in adjacent policies.
    - Source: `Disable PDF.js, the built-in PDF viewer in { -brand-short-name }.`
- `policy-PDFjs` — `browser/browser/policies/policies-descriptions.ftl` — policy-DisableBuiltinPDFViewer vs policy-PDFjs — "PDF-viewer" vs "PDF-lezer" in adjacent policies.
    - Source: `Disable or configure PDF.js, the built-in PDF viewer in { -brand-short-name }.`
- `permissions-exceptions-popup-window2` — `browser/browser/preferences/permissions.ftl` — permissions-exceptions-popup-window3 (.title) vs permissions-exceptions-popup-window2 — preferences/permissions.ftl — "Allowed Websites" as "Toegestane websites" vs "Websites met toestemming"; and -window3 uses "doorleidingen" where the whole tree otherwise uses "omleidingen" for third-party redirects (site-permissions-unblock-redirect, browser.ftl pop-up strings).
    - Source: `style: { permissions-window2.style } title: Allowed Websites - Pop-ups`
    - Suggest: `.title`
- `permissions-exceptions-popup-window3` — `browser/browser/preferences/permissions.ftl` — permissions-exceptions-popup-window3 (.title) vs permissions-exceptions-popup-window2 — preferences/permissions.ftl — "Allowed Websites" as "Toegestane websites" vs "Websites met toestemming"; and -window3 uses "doorleidingen" where the whole tree otherwise uses "omleidingen" for third-party redirects (site-permissions-unblock-redirect, browser.ftl pop-up strings).
    - Source: `style: { permissions-window2.style } title: Allowed Websites - Pop-ups and Third-Party Redirects`
    - Suggest: `.title`
- `content-blocking-and-isolating-etp-warning-description-4` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-warning-message (.message), content-blocking-and-isolating-etp-warning-description-4 — preferences/preferences.ftl — the quoted "Fix site issues" reference appears in three forms and matches neither real label (content-blocking-baseline-exceptions-3 "Grote problemen met de website verhelpen", content-blocking-convenience-exceptions-3 "Kleine problemen met de website oplossen…
    - Source: `{ -brand-short-name } recommends using the “Fix site issues” settings to reduce broken site features and content. If a site seems broken, try turning off tracking protection for that site to load all content.`
    - Suggest: `.message`
- `pane-experimental-search-results-header` — `browser/browser/preferences/preferences.ftl` — "Proceed with Caution" rendered differently from pane-experimental-subtitle ("Ga voorzichtig verder").
    - Source: `{ -brand-short-name } Experiments: Proceed with Caution`
- `preferences-doh-enabled-detailed-desc-1` — `browser/browser/preferences/preferences.ftl` — "aanbieder" where all sibling DoH strings use "provider".
    - Source: `Use the provider you select`
- `preferences-doh-overview-custom` — `browser/browser/preferences/preferences.ftl` — preferences-doh-overview-default, preferences-doh-overview-custom, preferences-doh-radio-default (.description), preferences-doh-radio-custom — preferences/preferences.ftl — "secure DNS" as "Veilige DNS" while preferences-doh-default-desc, -strict-desc, permissions-exceptions-manage-doh-desc, preferences-doh-fallback-label and preferences-doh-default-detailed-desc-1 use "Beveiligde DNS".
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior. label: Custom`
- `preferences-doh-overview-default` — `browser/browser/preferences/preferences.ftl` — preferences-doh-overview-default, preferences-doh-overview-custom, preferences-doh-radio-default (.description), preferences-doh-radio-custom — preferences/preferences.ftl — "secure DNS" as "Veilige DNS" while preferences-doh-default-desc, -strict-desc, permissions-exceptions-manage-doh-desc, preferences-doh-fallback-label and preferences-doh-default-detailed-desc-1 use "Beveiligde DNS".
    - Source: `description: Use secure DNS in regions where it’s available. label: Default protection`
- `preferences-doh-radio-custom` — `browser/browser/preferences/preferences.ftl` — preferences-doh-overview-default, preferences-doh-overview-custom, preferences-doh-radio-default (.description), preferences-doh-radio-custom — preferences/preferences.ftl — "secure DNS" as "Veilige DNS" while preferences-doh-default-desc, -strict-desc, permissions-exceptions-manage-doh-desc, preferences-doh-fallback-label and preferences-doh-default-detailed-desc-1 use "Beveiligde DNS".
    - Source: `description: Always use secure DNS with control over your provider and fallback behavior label: Custom`
- `preferences-doh-radio-default` — `browser/browser/preferences/preferences.ftl` — preferences-doh-overview-default, preferences-doh-overview-custom, preferences-doh-radio-default (.description), preferences-doh-radio-custom — preferences/preferences.ftl — "secure DNS" as "Veilige DNS" while preferences-doh-default-desc, -strict-desc, permissions-exceptions-manage-doh-desc, preferences-doh-fallback-label and preferences-doh-default-detailed-desc-1 use "Beveiligde DNS".
    - Source: `description: Use secure DNS in regions where it’s available label: Default`
- `preferences-etp-custom-control-group` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-custom (.description) vs preferences-etp-custom-control-group (.description) — "beschermingsmaatregelen" vs "beschermingsinstellingen" for the same en-US string.
    - Source: `description: Choose which protections to turn on or off. label: Tracking protection`
    - Suggest: `.description`
- `preferences-etp-level-custom` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-custom (.description) vs preferences-etp-custom-control-group (.description) — "beschermingsmaatregelen" vs "beschermingsinstellingen" for the same en-US string.
    - Source: `description: Choose which protections to turn on or off. label: Custom`
    - Suggest: `.description`
- `preferences-etp-level-warning-message` — `browser/browser/preferences/preferences.ftl` — preferences-etp-level-warning-message (.message), content-blocking-and-isolating-etp-warning-description-4 — preferences/preferences.ftl — the quoted "Fix site issues" reference appears in three forms and matches neither real label (content-blocking-baseline-exceptions-3 "Grote problemen met de website verhelpen", content-blocking-convenience-exceptions-3 "Kleine problemen met de website oplossen…
    - Source: `heading: Heads up! Some sites may not work as expected. message: Some sites build trackers into their features or content. When { -brand-short-name } blocks them, the site looks broken. Try using “Fix site issue” or tur…`
    - Suggest: `.message`
- `preferences-text-zoom-override-warning` — `browser/browser/preferences/preferences.ftl` — preferences-text-zoom-override-warning, -warning2 (.message) — preferences/preferences.ftl — quote the option as "‘Alleen tekst zoomen’" but the actual checkbox preferences-zoom-text-only is "Alleen tekst inzoomen".
    - Source: `message: Warning: If you select “Zoom text only” and your default zoom is not set to 100%, it may cause some sites or content to break.`
    - Suggest: `-warning2`
- `related-settings-tabs-browsing-link` — `browser/browser/preferences/preferences.ftl` — points at a setting named "Browserindeling" (browser-layout-header2) but says "Browseropmaak aanpassen".
    - Source: `label: Customize browser layout`
    - Suggest: `.label`
- `security-privacy-issue-warning-safe-browsing` — `browser/browser/preferences/preferences.ftl` — English "scams" left untranslated; security-safe-browsing-warning uses "oplichting".
    - Source: `description: Your exposure to scams and malware from websites is increased. label: Dangerous and deceptive content is not blocked`
    - Suggest: `.description`
- `barbell-avatar-tooltip` — `browser/browser/profiles.ftl` — briefcase-avatar-tooltip, craft-avatar-tooltip, barbell-avatar-tooltip, video-game-controller-avatar-tooltip (.tooltiptext) — profiles.ftl — each tooltip names the avatar differently from its own -avatar / -avatar-alt pair ("Aktetas" vs "Werkmap", "Handwerk" vs "Knutselen", "Barbell" vs "Halter", "Gamecontroller" vs "Videogamecontroller").
    - Source: `tooltiptext: Apply barbell avatar`
- `briefcase-avatar-tooltip` — `browser/browser/profiles.ftl` — briefcase-avatar-tooltip, craft-avatar-tooltip, barbell-avatar-tooltip, video-game-controller-avatar-tooltip (.tooltiptext) — profiles.ftl — each tooltip names the avatar differently from its own -avatar / -avatar-alt pair ("Aktetas" vs "Werkmap", "Handwerk" vs "Knutselen", "Barbell" vs "Halter", "Gamecontroller" vs "Videogamecontroller").
    - Source: `tooltiptext: Apply briefcase avatar`
- `craft-avatar-tooltip` — `browser/browser/profiles.ftl` — briefcase-avatar-tooltip, craft-avatar-tooltip, barbell-avatar-tooltip, video-game-controller-avatar-tooltip (.tooltiptext) — profiles.ftl — each tooltip names the avatar differently from its own -avatar / -avatar-alt pair ("Aktetas" vs "Werkmap", "Handwerk" vs "Knutselen", "Barbell" vs "Halter", "Gamecontroller" vs "Videogamecontroller").
    - Source: `tooltiptext: Apply craft avatar`
- `video-game-controller-avatar-tooltip` — `browser/browser/profiles.ftl` — briefcase-avatar-tooltip, craft-avatar-tooltip, barbell-avatar-tooltip, video-game-controller-avatar-tooltip (.tooltiptext) — profiles.ftl — each tooltip names the avatar differently from its own -avatar / -avatar-alt pair ("Aktetas" vs "Werkmap", "Handwerk" vs "Knutselen", "Barbell" vs "Halter", "Gamecontroller" vs "Videogamecontroller").
    - Source: `tooltiptext: Apply video game controller avatar`
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — "advertentiebureaus" (ad agencies) where the identical paragraph cookie-tab-content in protections.ftl says "adverteerders".
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
- `select-translations-panel-unsupported-language-message-known` — `browser/browser/translations.ftl` — select-translations-panel-unsupported-language-message-known vs translations-panel-error-unsupported-hint-known — translations.ftl — the same en-US sentence is rendered "Sorry, we ondersteunen nog geen { $language }." and "Sorry, we ondersteunen het { $language } nog niet." Pick one (the article form is the more standard Dutch construction with language names).
    - Source: `message: Sorry, we don’t support { $language } yet.`
- `translations-panel-error-unsupported-hint-known` — `browser/browser/translations.ftl` — select-translations-panel-unsupported-language-message-known vs translations-panel-error-unsupported-hint-known — translations.ftl — the same en-US sentence is rendered "Sorry, we ondersteunen nog geen { $language }." and "Sorry, we ondersteunen het { $language } nog niet." Pick one (the article form is the more standard Dutch construction with language names).
    - Source: `Sorry, we don’t support { $language } yet.`
- `unified-extensions-mb-blocklist-warning-single` — `browser/browser/unifiedExtensions.ftl` — unifiedExtensions.ftl — "risicovol" vs "riskant" in -single2 / -multiple2 and unified-extensions-item-messagebar-softblocked.
    - Source: `heading: { $extensionName } disabled message: This extension violates Mozilla’s policies and has been disabled. You can enable it in settings, but this may be risky.`
    - Suggest: `-single2`
- `about-debugging-setup-usb-disabled` — `devtools/client/aboutdebugging.ftl` — about-debugging-setup-usb-disabled, about-debugging-setup-usb-step-enable-debug2, about-debugging-sidebar — "debugging" vs "foutopsporing" for the same concept in one file.
    - Source: `Enabling this will download and add the required Android USB debugging components to { -brand-shorter-name }.`
- _…and 49 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `popup-trigger-redirect-menuitem` — `browser/browser/browser.ftl` — uses ‘…’ while its sibling popup-show-popup-menuitem and en-US both use “…”.
    - Source: `label: Show “{ $redirectURI }”`
    - Suggest: `.label`
- `ip-protection-vpn-upgrade-link-1` — `browser/browser/ipProtection.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
    - Source: `description: Choose from 300+ locations and protect all your apps on up to 5 devices. label: Take protection further with { -mozilla-vpn-brand-name }`
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
    - Source: `heading: Take protection further with { -mozilla-vpn-brand-name } message: Choose from 300+ locations and protect all your apps on up to 5 devices.`
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `heading: Take protection further with { -mozilla-vpn-brand-name } message: Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `.message`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `heading: Getting close to your VPN limit message: You have { $usageLeft } GB of { $maxUsage } GB left this month.`
    - Suggest: `.message`
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — lost the trailing … that marks the item as opening a further page (en-US "Share Ideas and Feedback…").
    - Source: `accesskey: S label: Share Ideas and Feedback…`
- `july-jam-body` — `browser/browser/newtab/asrouter.ftl` — july-jam-body vs spotlight-peace-mind-body — newtab/asrouter.ftl — the same figure written "3.000" and "3000".
    - Source: `Every month, { -brand-short-name } blocks an average of 3,000+ trackers per user, giving you safe, speedy access to the good internet.`
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — july-jam-body vs spotlight-peace-mind-body — newtab/asrouter.ftl — the same figure written "3.000" and "3000".
    - Source: `Every month, { -brand-short-name } blocks an average of over 3,000 trackers per user. Because nothing, especially privacy nuisances like trackers, should stand between you and the good internet.`
- `newtab-custom-weather-toggle` — `browser/browser/newtab/newtab.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
    - Source: `description: Today’s forecast at a glance label: Weather`
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `Upgrading to Windows 11? Let’s back up your { -brand-product-name } data.`
    - Suggest: `.message`
- `fx100-thank-you-subtitle` — `browser/browser/newtab/onboarding.ftl` — fx100-thank-you-subtitle vs fx100-upgrade-thank-you-body — newtab/onboarding.ftl — the same ordinal written "100ste" and "100e".
    - Source: `It’s our 100th release! Thanks for helping us build a better, healthier internet.`
- `fx100-upgrade-thank-you-body` — `browser/browser/newtab/onboarding.ftl` — fx100-thank-you-subtitle vs fx100-upgrade-thank-you-body — newtab/onboarding.ftl — the same ordinal written "100ste" and "100e".
    - Source: `It’s our 100th release of { -brand-short-name }. Thank <em>you</em> for helping us build a better, healthier internet.`
- `mr2022-onboarding-no-mobile-download-cta-text` — `browser/browser/newtab/onboarding.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `Scan the QR code to get { -brand-product-name } for mobile.`
    - Suggest: `.message`
- `policy-DisableThirdPartyModuleBlocking` — `browser/browser/policies/policies-descriptions.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `Prevent the user from blocking third-party modules that get injected into the { -brand-short-name } process.`
    - Suggest: `.message`
- `policy-Handlers` — `browser/browser/policies/policies-descriptions.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `Configure default application handlers.`
    - Suggest: `.message`
- `policy-LegacyProfiles` — `browser/browser/policies/policies-descriptions.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `Disable the feature enforcing a separate profile for each installation.`
    - Suggest: `.message`
- `content-blocking-cross-site-tracking-cookies-plus-isolate` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-cookies (.label), content-blocking-cross-site-tracking-cookies-plus-isolate — preferences/preferences.ftl — same stray comma before "en".
    - Source: `Cross-site tracking cookies, and isolate remaining cookies`
    - Suggest: `.label`
- `home-prefs-weather-description` — `browser/browser/preferences/preferences.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
    - Source: `Today’s forecast at a glance`
- `preferences-doh-radio-default` — `browser/browser/preferences/preferences.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
    - Source: `description: Use secure DNS in regions where it’s available label: Default`
- `preferences-doh-radio-off` — `browser/browser/preferences/preferences.ftl` — Superfluous sentence-final period (absent in en-US and in the sibling strings): home-prefs-weather-description (preferences/preferences.ftl; newtab-custom-weather-toggle.description has none), preferences-doh-radio-default (.description), preferences-doh-radio-off (.description), ip-protection-vpn-upgrade-link-1 (.description) vs ipprotection-locations-subview-promo.
    - Source: `description: Use your default DNS resolver label: Off`
- `sitedata-option-block-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — sitedata-option-block-cross-site-cookies (.label), content-blocking-cross-site-tracking-cookies-plus-isolate — preferences/preferences.ftl — same stray comma before "en".
    - Source: `label: Cross-site tracking cookies, and isolate other cross-site cookies`
    - Suggest: `.label`
- `inactive-css-first-letter-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `<strong>{ $property }</strong> is not supported on ::first-letter pseudo-elements.`
    - Suggest: `.message`
- `inactive-css-first-line-pseudo-element-not-supported` — `devtools/client/tooltips.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `<strong>{ $property }</strong> is not supported on ::first-line pseudo-elements.`
    - Suggest: `.message`
- `pippki-reset-password-confirmation-message` — `security/manager/security/pippki/pippki.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `Your Primary Password has been reset.`
    - Suggest: `.message`
- `crashreporter-checkbox-send-report` — `toolkit/crashreporter/crashreporter.ftl` — Missing sentence-final period (present in en-US and in the sibling strings): ipprotection-message-bandwidth-warning (.message), ipprotection-locations-subview-promo (.message), inactive-css-first-line-pseudo-element-not-supported, inactive-css-first-letter-pseudo-element-not-supported, pippki-reset-password-confirmation-message, crashreporter-checkbox-send-report, policy-LegacyProfiles, policy-Di…
    - Source: `Tell { -vendor-short-name } about this crash so they can fix it.`
    - Suggest: `.message`
- `about-httpsonly-explanation-continue` — `toolkit/toolkit/about/aboutHttpsOnlyError.ftl` — stray space before the final period.
    - Source: `If you continue, HTTPS-Only Mode will be turned off temporarily for this site.`
- `about-processes-total-memory-size-changed` — `toolkit/toolkit/about/aboutProcesses.ftl` — a space between the number and its unit in two of the three, none in the third. (The space is correct Dutch; the third should match.)
    - Source: `(value): { $total }{ $totalUnit } title: Evolution: { $deltaSign }{ $delta }{ $deltaUnit }`
- `about-processes-total-memory-size-no-change` — `toolkit/toolkit/about/aboutProcesses.ftl` — a space between the number and its unit in two of the three, none in the third. (The space is correct Dutch; the third should match.)
    - Source: `{ $total }{ $totalUnit }`
- `download-utils-time-pair` — `toolkit/toolkit/downloads/downloadUtils.ftl` — a space between the number and its unit in two of the three, none in the third. (The space is correct Dutch; the third should match.)
    - Source: `{ $time }{ $unit }`
- `fp-certerror-not-yet-valid-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — stray space before the final period.
    - Source: `Sites use certificates issued by a certificate authority to prove they’re really who they say they are. { -brand-short-name } doesn’t trust this site because it looks like the certificate will not be valid until { $date…`

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/nl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (23)

- `addon-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `addon-local-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `smart-window-opened-tabs-summary-group` — `browser/browser/aiWindowContent.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `smart-window-switched-tab-summary` — `browser/browser/aiWindowContent.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `onboarding-aw-finish-setup-button` — `browser/browser/browser.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `firefoxview-closed-tabs-dismiss-tab` — `browser/browser/firefoxView.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `fxviewtabrow-dismiss-tab-button` — `browser/browser/fxviewTabList.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `newtab-search-box-handoff-input` — `browser/browser/newtab/newtab.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `newtab-search-box-handoff-text` — `browser/browser/newtab/newtab.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `newtab-section-unblock-topic` — `browser/browser/newtab/newtab.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `newtab-weather-see-forecast` — `browser/browser/newtab/newtab.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `newtab-weather-see-forecast-description` — `browser/browser/newtab/newtab.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `mr2022-onboarding-welcome-pin-subtitle` — `browser/browser/newtab/onboarding.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `address-capture-save-doorhanger-description` — `browser/browser/preferences/formAutofill.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `passport-capture-save-doorhanger-description` — `browser/browser/preferences/formAutofill.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `tabbrowser-unmute-tab-audio-background-tooltip` — `browser/browser/tabbrowser.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `tabbrowser-unmute-tab-audio-tooltip` — `browser/browser/tabbrowser.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `existing-user-privacy-notice-update-message` — `browser/browser/termsofuse.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `accessibility-progress-progressbar` — `devtools/client/accessibility.ftl` — raised by `legacy`, withdrawn 2026-08-20
- `about-pdf-title` — `toolkit/toolkit/about/aboutPDF.ftl` — raised by `legacy`, withdrawn 2026-08-20

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

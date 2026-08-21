# Firefox l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `5cbe42651962` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `60f24d17564f` |
| **Previous run** | 2026-08-21 @ `f2e9b7fce093` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,161 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-GB: [android](android.md)

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
| Strings | 18,161 |
| Missing strings | 19 |
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
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 2 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 41 |

### Completeness

**19 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 7
- `browser/browser/appmenu.ftl` — 2
- `browser/browser/menubar.ftl` — 2
- `browser/browser/sharePanel.ftl` — 2
- `browser/browser/preferences/preferences.ftl` — 2
- `browser/browser/aboutDialog.ftl` — 1
- `browser/browser/preferences/formAutofill.ftl` — 1
- `dom/chrome/accessibility/AccessFu.properties` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 597, `curly-single` 101, `straight-double` 58 | **curly-double** |
| apostrophe | `typographic` 1121, `straight` 56 | **typographic** |
| ellipsis | `char` 461, `ascii` 1 | **char** |
| dash | `em` 108, `en` 4 | **em** |
| nbsp | `total` 5, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

- **typography — 41 strings** — 41 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `BlockMixedActiveContent`, `BlockMixedDisplayContent`, `CSPROViolation`, `CSPROViolationWithURI`, `CSPViolation`, `CSPViolationWithURI`, `DontAskAgain`, `FullscreenDeniedContainerNotAllowed`, `ImageMapCircleNegativeRadius`, `ImageMapCircleWrongNumberOfCoords`, `ImageMapPolyOddNumberOfCoords`, `ImageMapPolyWrongNumberOfCoords` …and 25 more

---

## 3. Open findings (32)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 8 |
| 2 | Wrong content (says something other than the English) | 11 |
| 3 | Degraded language (grammar, spelling, terminology) | 11 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `mr2022-onboarding-colorway-description-dreamer` — `browser/browser/newtab/onboarding.ftl` — American spelling "favors" left unadapted; en-GB requires "favours".
    - Current: `fortune favors the bold`
    - Source: `<b>You are a Dreamer.</b> You believe that fortune favors the bold and inspire others to be brave.`
    - Suggest: `fortune favours the bold`
    - This is the only occurrence of American -or in "favour"/"favours" as an ordinary word anywhere in the en-GB tree; the locale otherwise uses "favourite", "favourites", "favour" consistently (e.g. newtab.ftl newtab-shortcuts-highlight-title "Your favourites at your fingertips", asrouter.ftl fox-doodle-pin-body "your favourite indie browser"). Remaining "favor" hits are en-US developer comments or t…
- `SEC_ERROR_LIBPKIX_INTERNAL` — `security/manager/chrome/pipnss/nsserrors.properties` — "occured" is a misspelling of "occurred", which the locale uses everywhere else.
    - Current: `Libpkix internal error occured during certificate validation.`
    - Source: `Libpkix internal error occurred during cert validation.`
    - Suggest: `Libpkix internal error occurred during certificate validation.`
    - en-US reads "occurred"; en-GB also spells it "occurred" in every other string in this partition (e.g. SEC_ERROR_IO "An I/O error occurred during security authorisation.", SSLConnectionErrorPrefix2, PERR_FAILURE). "occured" is not a British variant, just a typo introduced in the localisation.

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — The two plural variants of the same message render "Sync" differently: the [1] variant says "synchronised devices" while the [other] variant says "synced devices".
    - Current: `on all your synced devices`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices. This will also remove any breach alerts that appear here. You cannot undo this action. [other] This will remove al…`
    - Suggest: `on all your synchronised devices`
    - Within a single message the same phrase must be rendered the same way; the [1] variant of this very message, and the parallel message contextual-manager-passwords-remove-all-message-sync in browser/browser/contextual-manager.ftl (both variants), use "synchronised devices".
- `appmenu-remote-tabs-sign-into-sync` — `browser/browser/appmenu.ftl` — "Sign in to sync…" keeps the en-US short form while the identical phrase is expanded to "Sign in to synchronise" twice elsewhere in the same file.
    - Current: `Sign in to sync…`
    - Source: `label: Sign in to sync…`
    - Suggest: `Sign in to synchronise…`
    - fxa-menu-sync-off-signin-description and appmenu-fxa-sign-in-promo-heading in this same file both render the phrase as "Sign in to synchronise", as do syncedTabs.ftl, sync.ftl and aboutLogins.ftl.
- `appmenu-remote-tabs-turn-on-sync` — `browser/browser/appmenu.ftl` — "Turn on sync…" keeps the en-US short form while the same phrase is expanded to "Turn on synchronisation" elsewhere in the same file.
    - Current: `Turn on sync…`
    - Source: `label: Turn on sync…`
    - Suggest: `Turn on synchronisation…`
    - appmenu-sync-promo-turnonsync-cta in this same file reads "Turn on synchronisation", matching syncedTabs.ftl, firefoxView.ftl and preferences.ftl, which all expand this phrase.
- `backup-file-moz-browser-restore-step-1` — `browser/browser/backupSettings.ftl` — The instruction points the user to "Settings > Synchronisation", but the settings pane is labelled "Sync" in this locale, so the referenced item does not exist.
    - Current: `go to Settings > Synchronisation`
    - Source: `Open the application menu ☰ and go to Settings > Sync`
    - Suggest: `go to Settings > Sync`
    - pane-sync-title3 in browser/browser/preferences/preferences.ftl is localised as "Sync", and login-intro-instructions-fxa-settings in browser/browser/aboutLogins.ftl already refers to the pane as "Settings > Sync"; a literal UI path must match the label it points at.
- `backup-file-other-browser-restore-step-2` — `browser/browser/backupSettings.ftl` — Same broken UI-path reference: "Settings > Synchronisation" does not match the "Sync" settings pane label used in this locale.
    - Current: `open the application menu ☰ and go to Settings > Synchronisation`
    - Source: `Start { -brand-short-name }, open the application menu ☰ and go to Settings > Sync`
    - Suggest: `open the application menu ☰ and go to Settings > Sync`
    - pane-sync-title3 in browser/browser/preferences/preferences.ftl is localised as "Sync"; the quoted navigation path must reproduce the label the user will actually see.
- `urlbar-popup-blocked2` — `browser/browser/browser.ftl` — "website" is used here although this file writes "web site" as two words everywhere else, including in the near-identical sibling string urlbar-popup-blocked.
    - Current: `for this website.`
    - Source: `tooltiptext: You have blocked pop-ups and third-party redirects for this website.`
    - Suggest: `for this web site.`
    - browser.ftl contains 22 visible-string occurrences of "web site"/"web sites" and this is the only visible-string occurrence of "website"; the adjacent urlbar-popup-blocked, which differs only by the redirect clause, reads "You have blocked pop-ups for this web site."
- `customkeys-nav-forward` — `browser/browser/customkeys.ftl` — The Forward navigation action is labelled "Forwards" while its paired Back action on the preceding line is left as "Back", so the pair is inconsistent.
    - Current: `Forwards`
    - Source: `Forward`
    - Suggest: `Forward`
    - customkeys-nav-back immediately above reads "Back", not "Backwards"; the two shortcut labels appear side by side in the same list and must use the same form (browser/browser/browserContext.ftl adapts both members of the pair together, as "Backwards"/"Forwards").
- `fxa-menu-message-backup-sync-secondary-text` — `browser/browser/newtab/asrouter.ftl` — "Sync" left untranslated while every sibling string in the same block renders it "Synchronise".
    - Current: `Sync backs up most of your data`
    - Source: `Sync backs up most of your data so you can access it everywhere you use { -brand-short-name }.`
    - Suggest: `Synchronise backs up most of your data`
    - In this same FxA Menu Message block en-GB renders en-US "Sync"/"syncing" as "Synchronise"/"synchronising" in every other string (fxa-menu-message-sync-button, -sync-devices-primary-text, -sync-devices-collapsed-text, -backup-sync-primary-text "safe and synchronised", -backup-sync-collapsed-text "Synchronise and back up data", -mobile-secondary-text, -mobile-collapsed-text). Only this one keeps th…
- `policy-AllowFileSelectionDialogs` — `browser/browser/policies/policies-descriptions.ftl` — UI term "dialog" spelled "dialogues" here, against the tree's dominant "dialog".
    - Current: `Allow file selection dialogues.`
    - Source: `Allow file selection dialogs.`
    - Suggest: `Allow file selection dialogs.`
    - The en-GB tree uses "dialog" for the UI-window sense about 388 times against 22 "dialogue" (e.g. toolkit/toolkit/global/handlerDialog.ftl, browser/browser/sanitize.ftl, browser/browser/tabbrowser.ftl). "Dialogue" is the conversation sense in British English and is not the established term here.
- `policy-UseSystemPrintDialog` — `browser/browser/policies/policies-descriptions.ftl` — "print dialogue" conflicts with "print dialog" used in the locale's printing files.
    - Current: `Print using the system print dialogue.`
    - Source: `Print using the system print dialog.`
    - Suggest: `Print using the system print dialog.`
    - toolkit/toolkit/printing/printUI.ftl and toolkit/chrome/global/printdialog.properties in this same tree use "print dialog" for the identical concept, so this string diverges from the locale's own printing terminology.
- `shopping-avatar-tooltip` — `browser/browser/profiles.ftl` — The same shopping icon is called a "basket" in its label and alt text but a "trolley" in its tooltip.
    - Current: `Apply shopping trolley avatar`
    - Source: `tooltiptext: Apply shopping cart avatar`
    - Suggest: `Apply shopping basket avatar`
    - In the same file, shopping-avatar and shopping-avatar-alt both render en-US "Shopping cart" as "Shopping basket", and the locale uses "shopping baskets" for "shopping carts" in browser/browser/sanitize.ftl (item-cookies-site-data-description) and browser/browser/protectionsPanel.ftl (protections-panel-cookie-banner-view-cookie-clear-warning). "Trolley" is an isolated departure describing the same…
- `check` — `dom/chrome/accessibility/unix/accessible.properties` — The checkbox action is adapted to "Tick"/"Untick" in the parallel mac file but left as "Check"/"Uncheck" here.
    - Current: `check = Check`
    - Source: `Check`
    - Suggest: `check = Tick`
    - For the identical string IDs, dom/chrome/accessibility/mac/accessible.properties uses "Tick"/"Untick", and the locale uses "tick" for checkbox actions elsewhere (AccessFu.properties "tick button", "tick menu item"; dom.properties "Please tick this box"). The unix/win platform files are the odd ones out for the same UI action.
- `check` — `dom/chrome/accessibility/win/accessible.properties` — The checkbox action is adapted to "Tick"/"Untick" in the parallel mac file but left as "Check"/"Uncheck" here.
    - Current: `check = Check`
    - Source: `Check`
    - Suggest: `check = Tick`
    - Same inconsistency as the unix file: mac/accessible.properties renders these very IDs as "Tick"/"Untick", and AccessFu.properties uses "tick button"/"tick menu item", so the win file diverges from the locale's own choice for the same action.
- `back` — `toolkit/chrome/global/narrate.properties` — Skip-back/skip-forward controls named both "Backwards/Forwards" and "Back/Forward" in the same file.
    - Current: `back = Backwards`
    - Source: `Back`
    - Suggest: `back = Back`
    - `back` and `previous-label` label the same Narrate control, as do `forward` and `next-label`. The first pair was changed to "Backwards"/"Forwards" while the second pair kept "Back (%S)"/"Forward (%S)", so one control carries two names. The en-US source for `back` is "Back" (not "Backward"), so no en-GB adverb adaptation was required here.
- `fp-certerror-revoked-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — "any more" here versus "anymore" in four sibling strings carrying the identical clause.
    - Current: `isn’t trusted any more.`
    - Source: `{ -brand-short-name } is warning you about this site because the certificate provided for { $hostname } has been revoked and isn’t trusted anymore.`
    - Suggest: `isn’t trusted anymore.`
    - certError.ftl uses "isn’t trusted anymore" at lines 94, 157, 167 and 171; only line 81 splits it. Both forms are current in British English, so this is reported purely as a departure from what the file and the wider tree (7 occurrences of "anymore") do consistently, not as a preference.

### C. Grammar, agreement & spelling

- `autofill-address-postal-code` — `browser/browser/preferences/formAutofill.ftl` — “Post Code” is not the British form of the term; en-GB writes “Postcode” as one word.
    - Current: `Post Code`
    - Source: `Postal Code`
    - Suggest: `Postcode`
    - The locale deliberately adapted en-US “Postal Code”, but the UK term (Royal Mail, and the locale's own bundled en-GB dictionary, which lists only “postcode”) is the single word “Postcode”; “Post Code” is neither the en-US source form nor the en-GB convention.
- `prefs-syncing-off` — `browser/browser/preferences/preferences.ftl` — `prefs-syncing-off` still uses the en-US form “syncing”
    - Current: `Syncing: OFF`
    - Suggest: `synchronising`
    - This locale writes “synchronising” for “syncing” in 22 other strings and keeps “syncing” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `prefs-syncing-on` — `browser/browser/preferences/preferences.ftl` — `prefs-syncing-on` still uses the en-US form “syncing”
    - Current: `Syncing: ON`
    - Suggest: `synchronising`
    - This locale writes “synchronising” for “syncing” in 22 other strings and keeps “syncing” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `safeb-palm-accept-label` — `browser/browser/safebrowsing/blockedSite.ftl` — Button label reads "Go backwards" where the locale consistently labels this action "Go back"
    - Current: `Go backwards`
    - Source: `Go back`
    - Suggest: `Go back`
    - Every other standalone back-button label in the en-GB tree uses "Go back" (toolkit/toolkit/global/mozPageHeader.ftl, toolkit/toolkit/about/abuseReports.ftl:32, toolkit/toolkit/about/aboutAddons.ftl:265, toolkit/toolkit/neterror/certError.ftl:75, browser/browser/places.ftl:241). "Go backwards" as a button label is unidiomatic in en-GB and inconsistent with the locale's own usage; the adverbial "ba…
- `tabHistory.goBack` — `browser/chrome/browser/browser.properties` — "Go backwards to this page" is unidiomatic; en-GB uses "Go back to" with a destination
    - Current: `Go backwards to this page`
    - Source: `Go back to this page`
    - Suggest: `Go back to this page`
    - In en-GB "backwards" is a directional adverb ("Go backwards one page", browserContext.ftl:17) but takes "back" before a destination phrase: the locale writes "Go back to aggregates" (devtools/client/memory.properties:53) and "Go back" for the Back tooltip in places.ftl:241. "Go backwards to this page" mixes the two patterns.
- `discopane-intro` — `toolkit/toolkit/about/aboutAddons.ftl` — "software programmes" uses the broadcast/schedule sense; British English spells computer programs "programs".
    - Current: `These small software programmes are`
    - Source: `Extensions and themes are like apps for your browser, and they let you protect passwords, download videos, find deals, block annoying ads, change how your browser looks, and much more. These small software programs are…`
    - Suggest: `These small software programs are`
    - In en-GB, "programme" means a broadcast or plan; a computer program is spelled "program". The rest of this locale follows that rule (toolkit/toolkit/global/extensions.ftl "Another program on your computer…", toolkit/toolkit/neterror/certError.ftl "if an antivirus program…", toolkit/toolkit/neterror/nsserrors.ftl "enabled in this program").
- `discopane-intro3` — `toolkit/toolkit/about/aboutAddons.ftl` — "software programmes" uses the broadcast/schedule sense; British English spells computer programs "programs".
    - Current: `so much more. These small software programmes are often developed by a third party.`
    - Source: `Extensions and themes let you customize { -brand-product-name }. They can boost privacy, enhance productivity, improve media, change the way { -brand-product-name } looks, and so much more. These small software programs…`
    - Suggest: `so much more. These small software programs are often developed by a third party.`
    - Same as discopane-intro: en-GB uses "program" for computer software, and this locale does so consistently elsewhere in toolkit (extensions.ftl, certError.ftl, nsserrors.ftl).
- `region-name-fk` — `toolkit/toolkit/intl/regionNames.ftl` — US-only "(Islas Malvinas)" gloss retained on the Falkland Islands entry.
    - Current: `Falkland Islands (Islas Malvinas)`
    - Suggest: `Falkland Islands`
    - The parenthetical Argentine name is a US State Department naming convention. British English usage, including UK government and UK-facing software, uses the bare "Falkland Islands"; presenting the disputed name as an alternative title is a variant-specific defect rather than a faithful mirror of a neutral source.

### D. Terminology, register & consistency

- `genai-chatbot-summarize-sidebar-generic-subtitle` — `browser/browser/genai.ftl` — `genai-chatbot-summarize-sidebar-generic-subtitle` quotes “Summarise Page” but the string it names, `genai-chatbot-summarize-button`, reads “Summarise page”
    - Current: `Right-click the sparkles button in the sidebar and choose “Summarise Page”. The first time, you’ll also choose an AI chatbot.`
    - Source: `Right-click the sparkles button in the sidebar and choose “Summarize Page”. The first time, you’ll also choose an AI chatbot.`
    - Suggest: `Summarise page`
    - In the source this string quotes “Summarize Page”, which is exactly the value of `genai-chatbot-summarize-button` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `genai-chatbot-summarize-sidebar-provider-subtitle` — `browser/browser/genai.ftl` — `genai-chatbot-summarize-sidebar-provider-subtitle` quotes “Summarise Page” but the string it names, `genai-chatbot-summarize-button`, reads “Summarise page”
    - Current: `Right-click on your AI chatbot in the sidebar and choose “Summarise Page”.`
    - Source: `Right-click on your AI chatbot in the sidebar and choose “Summarize Page”.`
    - Suggest: `Summarise page`
    - In the source this string quotes “Summarize Page”, which is exactly the value of `genai-chatbot-summarize-button` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `permissions-exceptions-https-only-desc` — `browser/browser/preferences/permissions.ftl` — "websites" was changed to "web sites", which is inconsistent with the source and the locale's usual single-word form.
    - Current: `for specific web sites`
    - Source: `You can turn off HTTPS-Only Mode for specific websites. { -brand-short-name } won’t attempt to upgrade the connection to secure HTTPS for those sites. Exceptions do not apply to private windows.`
    - Suggest: `for specific websites`
    - en-GB does not require splitting "websites"; the same string later uses "sites" and the rest of the tree uses "websites". This is an unnecessary, inconsistent alteration.
- `recommended-theme-1` — `toolkit/toolkit/about/aboutAddons.ftl` — Product name "Firefox Color" was spelling-adapted to "Firefox Colour", against the explicit developer comment.
    - Current: `Build your own theme with Firefox Colour.`
    - Source: `Feeling creative? <a data-l10n-name="link">Build your own theme with Firefox Color.</a>`
    - Suggest: `Build your own theme with Firefox Color.`
    - The developer comment above this string states the "Firefox Color" name itself should not be translated; it is the name of a Mozilla product.
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — The proper name of the licence document, "Mozilla Public License", was respelled as "Mozilla Public Licence" (twice in the string).
    - Current: `Mozilla Public Licence`
    - Source: `{ -brand-short-name } is made available to you under the terms of the <a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>. This means you may use, copy and distribute { -brand-short-name } to othe…`
    - Suggest: `Mozilla Public License`
    - "Mozilla Public License" is the official title of a specific legal instrument (as reproduced verbatim in every file header of this same tree) and is not subject to the licence/license noun rule. Note the generic noun uses elsewhere in this partition ("Licence information") are correct and should stay.

### E. Typography, punctuation & spacing

- `migration-wizard-import-browser-no-browsers` — `browser/browser/migrationWizard.ftl` — "programs" over-corrected to "programmes", which in British English means broadcasts/schedules, not software.
    - Current: `couldn’t find any programmes that contain bookmark, history or password data`
    - Source: `{ -brand-short-name } couldn’t find any programs that contain bookmark, history or password data.`
    - Suggest: `couldn’t find any programs that contain bookmark, history or password data`
    - British English retains the spelling "program" for computer software and reserves "programme" for broadcasts, events and plans. The locale itself follows this everywhere else, including the equivalent legacy string no-migration-sources in browser/browser/migration.ftl ("No programs that contain bookmarks, history or password data could be found.") and toolkit/toolkit/global/extensionPermissions.f…
- `PINotInProlog` — `dom/chrome/layout/xul.properties` — "prolog" (the XML technical term) was over-corrected to "prologue", and the sibling string keeps "prolog".
    - Current: `does not have any effect outside the prologue any longer`
    - Source: `<?%1$S?> processing instruction does not have any effect outside the prolog anymore (see bug 360119).`
    - Suggest: `does not have any effect outside the prolog any longer`
    - "prolog" here is the XML specification term (the XML prolog), not the ordinary word; the immediately following string PINotInProlog2 in the same file correctly keeps "outside the prolog", so the file contradicts itself.

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

### Resolved to date (6)

- `permissions-exceptions-https-only-desc` — `browser/browser/preferences/permissions.ftl` — fixed 2026-08-21
- `preferences-data-migration-description` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-21
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-08-20
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-08-20
- `abuse-report-messagebar-aborted` — `toolkit/toolkit/about/abuseReports.ftl` — fixed 2026-08-20
- `abuse-report-messagebar-aborted` — `toolkit/toolkit/about/abuseReports.ftl` — fixed 2026-08-20

# Firefox l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b95608d528c8` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | _none — this is the baseline_ @ `—` |
| **Mode** | baseline |
| **Strings reviewed this run** | 18,161 of 18,161 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (35)

- `prefs-syncing-on` — `browser/browser/preferences/preferences.ftl` — `prefs-syncing-on` still uses the en-US form “syncing”
  - Current: `Syncing: ON`
  - en-US: `synchronising`
  - This locale writes “synchronising” for “syncing” in 22 other strings and keeps “syncing” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `prefs-syncing-off` — `browser/browser/preferences/preferences.ftl` — `prefs-syncing-off` still uses the en-US form “syncing”
  - Current: `Syncing: OFF`
  - en-US: `synchronising`
  - This locale writes “synchronising” for “syncing” in 22 other strings and keeps “syncing” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — `rights-webservices-term-6` still uses the en-US form “canceled”
  - Current: `{ -vendor-short-name } may update these terms as necessary from time to time. These terms may not be modified or canceled without { -vendor-short-name }’s written agreement.`
  - en-US: `cancelled`
  - This locale writes “cancelled” for “canceled” in 20 other strings and keeps “canceled” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `abuse-report-messagebar-aborted` — `toolkit/toolkit/about/abuseReports.ftl` — `abuse-report-messagebar-aborted` still uses the en-US form “canceled”
  - Current: `Report for <span data-l10n-name="addon-name">{ $addon-name }</span> canceled.`
  - en-US: `cancelled`
  - This locale writes “cancelled” for “canceled” in 20 other strings and keeps “canceled” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `permissions-exceptions-https-only-desc` — `browser/browser/preferences/permissions.ftl` — Uses en-US “websites” where this locale consistently writes “web sites”.
  - Current: `for specific websites.`
  - en-US: `for specific web sites.`
  - en-GB writes “web site(s)” throughout the tree (251 occurrences across 45 files, including the immediately following string permissions-exceptions-https-only-desc2, which renders the same sentence as “for specific web sites”). This is the only user-visible “websites” left in the preferences partition.
- `preferences-data-migration-description` — `browser/browser/preferences/preferences.ftl` — “auto-fill” hyphenated here but spelled “autofill” everywhere else in the locale.
  - Current: `auto-fill data`
  - en-US: `autofill data`
  - This is the only occurrence of “auto-fill” in the whole en-GB tree; the sibling string preferences-data-migration-group in the same file says “autofill data”, and formAutofill.ftl/preferences.ftl use “autofill” consistently (180+ occurrences).
- `autofill-address-postal-code` — `browser/browser/preferences/formAutofill.ftl` — “Post Code” is not the British form of the term; en-GB writes “Postcode” as one word.
  - Current: `Post Code`
  - en-US: `Postcode`
  - The locale deliberately adapted en-US “Postal Code”, but the UK term (Royal Mail, and the locale's own bundled en-GB dictionary, which lists only “postcode”) is the single word “Postcode”; “Post Code” is neither the en-US source form nor the en-GB convention.
- `mr2022-onboarding-colorway-description-dreamer` — `browser/browser/newtab/onboarding.ftl` — American spelling "favors" left unadapted; en-GB requires "favours".
  - Current: `fortune favors the bold`
  - en-US: `fortune favours the bold`
  - This is the only occurrence of American -or in "favour"/"favours" as an ordinary word anywhere in the en-GB tree; the locale otherwise uses "favourite", "favourites", "favour" consistently (e.g. newtab.ftl newtab-shortcuts-highlight-title "Your favourites at your fingertips", asrouter.ftl fox-doodle-pin-body "your favourite indie browser"). Remaining "favor" hits are en-US developer comments or t…
- `fxa-menu-message-backup-sync-secondary-text` — `browser/browser/newtab/asrouter.ftl` — "Sync" left untranslated while every sibling string in the same block renders it "Synchronise".
  - Current: `Sync backs up most of your data`
  - en-US: `Synchronise backs up most of your data`
  - In this same FxA Menu Message block en-GB renders en-US "Sync"/"syncing" as "Synchronise"/"synchronising" in every other string (fxa-menu-message-sync-button, -sync-devices-primary-text, -sync-devices-collapsed-text, -backup-sync-primary-text "safe and synchronised", -backup-sync-collapsed-text "Synchronise and back up data", -mobile-secondary-text, -mobile-collapsed-text). Only this one keeps th…
- `policy-AllowFileSelectionDialogs` — `browser/browser/policies/policies-descriptions.ftl` — UI term "dialog" spelled "dialogues" here, against the tree's dominant "dialog".
  - Current: `Allow file selection dialogues.`
  - en-US: `Allow file selection dialogs.`
  - The en-GB tree uses "dialog" for the UI-window sense about 388 times against 22 "dialogue" (e.g. toolkit/toolkit/global/handlerDialog.ftl, browser/browser/sanitize.ftl, browser/browser/tabbrowser.ftl). "Dialogue" is the conversation sense in British English and is not the established term here.
- `policy-UseSystemPrintDialog` — `browser/browser/policies/policies-descriptions.ftl` — "print dialogue" conflicts with "print dialog" used in the locale's printing files.
  - Current: `Print using the system print dialogue.`
  - en-US: `Print using the system print dialog.`
  - toolkit/toolkit/printing/printUI.ftl and toolkit/chrome/global/printdialog.properties in this same tree use "print dialog" for the identical concept, so this string diverges from the locale's own printing terminology.
- `migration-wizard-import-browser-no-browsers` — `browser/browser/migrationWizard.ftl` — "programs" over-corrected to "programmes", which in British English means broadcasts/schedules, not software.
  - Current: `couldn’t find any programmes that contain bookmark, history or password data`
  - en-US: `couldn’t find any programs that contain bookmark, history or password data`
  - British English retains the spelling "program" for computer software and reserves "programme" for broadcasts, events and plans. The locale itself follows this everywhere else, including the equivalent legacy string no-migration-sources in browser/browser/migration.ftl ("No programs that contain bookmarks, history or password data could be found.") and toolkit/toolkit/global/extensionPermissions.f…
- `shopping-avatar-tooltip` — `browser/browser/profiles.ftl` — The same shopping icon is called a "basket" in its label and alt text but a "trolley" in its tooltip.
  - Current: `Apply shopping trolley avatar`
  - en-US: `Apply shopping basket avatar`
  - In the same file, shopping-avatar and shopping-avatar-alt both render en-US "Shopping cart" as "Shopping basket", and the locale uses "shopping baskets" for "shopping carts" in browser/browser/sanitize.ftl (item-cookies-site-data-description) and browser/browser/protectionsPanel.ftl (protections-panel-cookie-banner-view-cookie-clear-warning). "Trolley" is an isolated departure describing the same…
- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — The two plural variants of the same message render "Sync" differently: the [1] variant says "synchronised devices" while the [other] variant says "synced devices".
  - Current: `on all your synced devices`
  - en-US: `on all your synchronised devices`
  - Within a single message the same phrase must be rendered the same way; the [1] variant of this very message, and the parallel message contextual-manager-passwords-remove-all-message-sync in browser/browser/contextual-manager.ftl (both variants), use "synchronised devices".
- `urlbar-popup-blocked2` — `browser/browser/browser.ftl` — "website" is used here although this file writes "web site" as two words everywhere else, including in the near-identical sibling string urlbar-popup-blocked.
  - Current: `for this website.`
  - en-US: `for this web site.`
  - browser.ftl contains 22 visible-string occurrences of "web site"/"web sites" and this is the only visible-string occurrence of "website"; the adjacent urlbar-popup-blocked, which differs only by the redirect clause, reads "You have blocked pop-ups for this web site."
- `backup-file-moz-browser-restore-step-1` — `browser/browser/backupSettings.ftl` — The instruction points the user to "Settings > Synchronisation", but the settings pane is labelled "Sync" in this locale, so the referenced item does not exist.
  - Current: `go to Settings > Synchronisation`
  - en-US: `go to Settings > Sync`
  - pane-sync-title3 in browser/browser/preferences/preferences.ftl is localised as "Sync", and login-intro-instructions-fxa-settings in browser/browser/aboutLogins.ftl already refers to the pane as "Settings > Sync"; a literal UI path must match the label it points at.
- `backup-file-other-browser-restore-step-2` — `browser/browser/backupSettings.ftl` — Same broken UI-path reference: "Settings > Synchronisation" does not match the "Sync" settings pane label used in this locale.
  - Current: `open the application menu ☰ and go to Settings > Synchronisation`
  - en-US: `open the application menu ☰ and go to Settings > Sync`
  - pane-sync-title3 in browser/browser/preferences/preferences.ftl is localised as "Sync"; the quoted navigation path must reproduce the label the user will actually see.
- `customkeys-nav-forward` — `browser/browser/customkeys.ftl` — The Forward navigation action is labelled "Forwards" while its paired Back action on the preceding line is left as "Back", so the pair is inconsistent.
  - Current: `Forwards`
  - en-US: `Forward`
  - customkeys-nav-back immediately above reads "Back", not "Backwards"; the two shortcut labels appear side by side in the same list and must use the same form (browser/browser/browserContext.ftl adapts both members of the pair together, as "Backwards"/"Forwards").
- `appmenu-remote-tabs-sign-into-sync` — `browser/browser/appmenu.ftl` — "Sign in to sync…" keeps the en-US short form while the identical phrase is expanded to "Sign in to synchronise" twice elsewhere in the same file.
  - Current: `Sign in to sync…`
  - en-US: `Sign in to synchronise…`
  - fxa-menu-sync-off-signin-description and appmenu-fxa-sign-in-promo-heading in this same file both render the phrase as "Sign in to synchronise", as do syncedTabs.ftl, sync.ftl and aboutLogins.ftl.
- `appmenu-remote-tabs-turn-on-sync` — `browser/browser/appmenu.ftl` — "Turn on sync…" keeps the en-US short form while the same phrase is expanded to "Turn on synchronisation" elsewhere in the same file.
  - Current: `Turn on sync…`
  - en-US: `Turn on synchronisation…`
  - appmenu-sync-promo-turnonsync-cta in this same file reads "Turn on synchronisation", matching syncedTabs.ftl, firefoxView.ftl and preferences.ftl, which all expand this phrase.
- `recommended-theme-1` — `toolkit/toolkit/about/aboutAddons.ftl` — Product name "Firefox Color" was spelling-adapted to "Firefox Colour", against the explicit developer comment.
  - Current: `Build your own theme with Firefox Colour.`
  - en-US: `Build your own theme with Firefox Color.`
  - The developer comment above this string states the "Firefox Color" name itself should not be translated; it is the name of a Mozilla product.
- `discopane-intro` — `toolkit/toolkit/about/aboutAddons.ftl` — "software programmes" uses the broadcast/schedule sense; British English spells computer programs "programs".
  - Current: `These small software programmes are`
  - en-US: `These small software programs are`
  - In en-GB, "programme" means a broadcast or plan; a computer program is spelled "program". The rest of this locale follows that rule (toolkit/toolkit/global/extensions.ftl "Another program on your computer…", toolkit/toolkit/neterror/certError.ftl "if an antivirus program…", toolkit/toolkit/neterror/nsserrors.ftl "enabled in this program").
- `discopane-intro3` — `toolkit/toolkit/about/aboutAddons.ftl` — "software programmes" uses the broadcast/schedule sense; British English spells computer programs "programs".
  - Current: `so much more. These small software programmes are often developed by a third party.`
  - en-US: `so much more. These small software programs are often developed by a third party.`
  - Same as discopane-intro: en-GB uses "program" for computer software, and this locale does so consistently elsewhere in toolkit (extensions.ftl, certError.ftl, nsserrors.ftl).
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — The proper name of the licence document, "Mozilla Public License", was respelled as "Mozilla Public Licence" (twice in the string).
  - Current: `Mozilla Public Licence`
  - en-US: `Mozilla Public License`
  - "Mozilla Public License" is the official title of a specific legal instrument (as reproduced verbatim in every file header of this same tree) and is not subject to the licence/license noun rule. Note the generic noun uses elsewhere in this partition ("Licence information") are correct and should stay.
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — "canceled" keeps the en-US single-l spelling where this locale consistently writes "cancelled".
  - Current: `modified or canceled without`
  - en-US: `modified or cancelled without`
  - The locale uses "cancelled" everywhere else (toolkit/toolkit/downloads/downloadUI.ftl ×6, toolkit/toolkit/about/aboutWebauthn.ftl, toolkit/toolkit/neterror/netError.ftl, browser/browser/downloads.ftl, browser/chrome/browser/downloads/downloads.properties). Only two strings in the tree retain "canceled".
- `abuse-report-messagebar-aborted` — `toolkit/toolkit/about/abuseReports.ftl` — "canceled" keeps the en-US single-l spelling where this locale consistently writes "cancelled".
  - Current: `</span> canceled.`
  - en-US: `</span> cancelled.`
  - en-GB doubles the l before -ed here, and the locale does so consistently (downloadUI.ftl, aboutWebauthn.ftl, netError.ftl, downloads.ftl, newtab.ftl). This string and rights-webservices-term-6 are the only two holdouts.
- `safeb-palm-accept-label` — `browser/browser/safebrowsing/blockedSite.ftl` — Button label reads "Go backwards" where the locale consistently labels this action "Go back"
  - Current: `Go backwards`
  - en-US: `Go back`
  - Every other standalone back-button label in the en-GB tree uses "Go back" (toolkit/toolkit/global/mozPageHeader.ftl, toolkit/toolkit/about/abuseReports.ftl:32, toolkit/toolkit/about/aboutAddons.ftl:265, toolkit/toolkit/neterror/certError.ftl:75, browser/browser/places.ftl:241). "Go backwards" as a button label is unidiomatic in en-GB and inconsistent with the locale's own usage; the adverbial "ba…
- `tabHistory.goBack` — `browser/chrome/browser/browser.properties` — "Go backwards to this page" is unidiomatic; en-GB uses "Go back to" with a destination
  - Current: `Go backwards to this page`
  - en-US: `Go back to this page`
  - In en-GB "backwards" is a directional adverb ("Go backwards one page", browserContext.ftl:17) but takes "back" before a destination phrase: the locale writes "Go back to aggregates" (devtools/client/memory.properties:53) and "Go back" for the Back tooltip in places.ftl:241. "Go backwards to this page" mixes the two patterns.
- `region-name-fk` — `toolkit/toolkit/intl/regionNames.ftl` — US-only "(Islas Malvinas)" gloss retained on the Falkland Islands entry.
  - Current: `Falkland Islands (Islas Malvinas)`
  - en-US: `Falkland Islands`
  - The parenthetical Argentine name is a US State Department naming convention. British English usage, including UK government and UK-facing software, uses the bare "Falkland Islands"; presenting the disputed name as an alternative title is a variant-specific defect rather than a faithful mirror of a neutral source.
- `fp-certerror-revoked-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — "any more" here versus "anymore" in four sibling strings carrying the identical clause.
  - Current: `isn’t trusted any more.`
  - en-US: `isn’t trusted anymore.`
  - certError.ftl uses "isn’t trusted anymore" at lines 94, 157, 167 and 171; only line 81 splits it. Both forms are current in British English, so this is reported purely as a departure from what the file and the wider tree (7 occurrences of "anymore") do consistently, not as a preference.
- `back` — `toolkit/chrome/global/narrate.properties` — Skip-back/skip-forward controls named both "Backwards/Forwards" and "Back/Forward" in the same file.
  - Current: `back = Backwards`
  - en-US: `back = Back`
  - `back` and `previous-label` label the same Narrate control, as do `forward` and `next-label`. The first pair was changed to "Backwards"/"Forwards" while the second pair kept "Back (%S)"/"Forward (%S)", so one control carries two names. The en-US source for `back` is "Back" (not "Backward"), so no en-GB adverb adaptation was required here.
- `SEC_ERROR_LIBPKIX_INTERNAL` — `security/manager/chrome/pipnss/nsserrors.properties` — "occured" is a misspelling of "occurred", which the locale uses everywhere else.
  - Current: `Libpkix internal error occured during certificate validation.`
  - en-US: `Libpkix internal error occurred during certificate validation.`
  - en-US reads "occurred"; en-GB also spells it "occurred" in every other string in this partition (e.g. SEC_ERROR_IO "An I/O error occurred during security authorisation.", SSLConnectionErrorPrefix2, PERR_FAILURE). "occured" is not a British variant, just a typo introduced in the localisation.
- `PINotInProlog` — `dom/chrome/layout/xul.properties` — "prolog" (the XML technical term) was over-corrected to "prologue", and the sibling string keeps "prolog".
  - Current: `does not have any effect outside the prologue any longer`
  - en-US: `does not have any effect outside the prolog any longer`
  - "prolog" here is the XML specification term (the XML prolog), not the ordinary word; the immediately following string PINotInProlog2 in the same file correctly keeps "outside the prolog", so the file contradicts itself.
- `check` — `dom/chrome/accessibility/unix/accessible.properties` — The checkbox action is adapted to "Tick"/"Untick" in the parallel mac file but left as "Check"/"Uncheck" here.
  - Current: `check = Check`
  - en-US: `check = Tick`
  - For the identical string IDs, dom/chrome/accessibility/mac/accessible.properties uses "Tick"/"Untick", and the locale uses "tick" for checkbox actions elsewhere (AccessFu.properties "tick button", "tick menu item"; dom.properties "Please tick this box"). The unix/win platform files are the odd ones out for the same UI action.
- `check` — `dom/chrome/accessibility/win/accessible.properties` — The checkbox action is adapted to "Tick"/"Untick" in the parallel mac file but left as "Check"/"Uncheck" here.
  - Current: `check = Check`
  - en-US: `check = Tick`
  - Same inconsistency as the unix file: mac/accessible.properties renders these very IDs as "Tick"/"Untick", and AccessFu.properties uses "tick button"/"tick menu item", so the win file diverges from the locale's own choice for the same action.

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
| Missing strings | 2 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Source-language spellings left unchanged | 4 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 41 |

### Completeness

**2 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 1
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

## 3. Open findings (35)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 8 |
| 2 | Wrong content (says something other than the English) | 13 |
| 3 | Degraded language (grammar, spelling, terminology) | 12 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `mr2022-onboarding-colorway-description-dreamer` — `browser/browser/newtab/onboarding.ftl` — American spelling "favors" left unadapted; en-GB requires "favours".
  - Current: `fortune favors the bold`
  - en-US: `fortune favours the bold`
  - This is the only occurrence of American -or in "favour"/"favours" as an ordinary word anywhere in the en-GB tree; the locale otherwise uses "favourite", "favourites", "favour" consistently (e.g. newtab.ftl newtab-shortcuts-highlight-title "Your favourites at your fingertips", asrouter.ftl fox-doodle-pin-body "your favourite indie browser"). Remaining "favor" hits are en-US developer comments or t…
- `SEC_ERROR_LIBPKIX_INTERNAL` — `security/manager/chrome/pipnss/nsserrors.properties` — "occured" is a misspelling of "occurred", which the locale uses everywhere else.
  - Current: `Libpkix internal error occured during certificate validation.`
  - en-US: `Libpkix internal error occurred during certificate validation.`
  - en-US reads "occurred"; en-GB also spells it "occurred" in every other string in this partition (e.g. SEC_ERROR_IO "An I/O error occurred during security authorisation.", SSLConnectionErrorPrefix2, PERR_FAILURE). "occured" is not a British variant, just a typo introduced in the localisation.
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — "canceled" keeps the en-US single-l spelling where this locale consistently writes "cancelled".
  - Current: `modified or canceled without`
  - en-US: `modified or cancelled without`
  - The locale uses "cancelled" everywhere else (toolkit/toolkit/downloads/downloadUI.ftl ×6, toolkit/toolkit/about/aboutWebauthn.ftl, toolkit/toolkit/neterror/netError.ftl, browser/browser/downloads.ftl, browser/chrome/browser/downloads/downloads.properties). Only two strings in the tree retain "canceled".
- `abuse-report-messagebar-aborted` — `toolkit/toolkit/about/abuseReports.ftl` — "canceled" keeps the en-US single-l spelling where this locale consistently writes "cancelled".
  - Current: `</span> canceled.`
  - en-US: `</span> cancelled.`
  - en-GB doubles the l before -ed here, and the locale does so consistently (downloadUI.ftl, aboutWebauthn.ftl, netError.ftl, downloads.ftl, newtab.ftl). This string and rights-webservices-term-6 are the only two holdouts.

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — The two plural variants of the same message render "Sync" differently: the [1] variant says "synchronised devices" while the [other] variant says "synced devices".
  - Current: `on all your synced devices`
  - en-US: `on all your synchronised devices`
  - Within a single message the same phrase must be rendered the same way; the [1] variant of this very message, and the parallel message contextual-manager-passwords-remove-all-message-sync in browser/browser/contextual-manager.ftl (both variants), use "synchronised devices".
- `appmenu-remote-tabs-sign-into-sync` — `browser/browser/appmenu.ftl` — "Sign in to sync…" keeps the en-US short form while the identical phrase is expanded to "Sign in to synchronise" twice elsewhere in the same file.
  - Current: `Sign in to sync…`
  - en-US: `Sign in to synchronise…`
  - fxa-menu-sync-off-signin-description and appmenu-fxa-sign-in-promo-heading in this same file both render the phrase as "Sign in to synchronise", as do syncedTabs.ftl, sync.ftl and aboutLogins.ftl.
- `appmenu-remote-tabs-turn-on-sync` — `browser/browser/appmenu.ftl` — "Turn on sync…" keeps the en-US short form while the same phrase is expanded to "Turn on synchronisation" elsewhere in the same file.
  - Current: `Turn on sync…`
  - en-US: `Turn on synchronisation…`
  - appmenu-sync-promo-turnonsync-cta in this same file reads "Turn on synchronisation", matching syncedTabs.ftl, firefoxView.ftl and preferences.ftl, which all expand this phrase.
- `backup-file-moz-browser-restore-step-1` — `browser/browser/backupSettings.ftl` — The instruction points the user to "Settings > Synchronisation", but the settings pane is labelled "Sync" in this locale, so the referenced item does not exist.
  - Current: `go to Settings > Synchronisation`
  - en-US: `go to Settings > Sync`
  - pane-sync-title3 in browser/browser/preferences/preferences.ftl is localised as "Sync", and login-intro-instructions-fxa-settings in browser/browser/aboutLogins.ftl already refers to the pane as "Settings > Sync"; a literal UI path must match the label it points at.
- `backup-file-other-browser-restore-step-2` — `browser/browser/backupSettings.ftl` — Same broken UI-path reference: "Settings > Synchronisation" does not match the "Sync" settings pane label used in this locale.
  - Current: `open the application menu ☰ and go to Settings > Synchronisation`
  - en-US: `open the application menu ☰ and go to Settings > Sync`
  - pane-sync-title3 in browser/browser/preferences/preferences.ftl is localised as "Sync"; the quoted navigation path must reproduce the label the user will actually see.
- `urlbar-popup-blocked2` — `browser/browser/browser.ftl` — "website" is used here although this file writes "web site" as two words everywhere else, including in the near-identical sibling string urlbar-popup-blocked.
  - Current: `for this website.`
  - en-US: `for this web site.`
  - browser.ftl contains 22 visible-string occurrences of "web site"/"web sites" and this is the only visible-string occurrence of "website"; the adjacent urlbar-popup-blocked, which differs only by the redirect clause, reads "You have blocked pop-ups for this web site."
- `customkeys-nav-forward` — `browser/browser/customkeys.ftl` — The Forward navigation action is labelled "Forwards" while its paired Back action on the preceding line is left as "Back", so the pair is inconsistent.
  - Current: `Forwards`
  - en-US: `Forward`
  - customkeys-nav-back immediately above reads "Back", not "Backwards"; the two shortcut labels appear side by side in the same list and must use the same form (browser/browser/browserContext.ftl adapts both members of the pair together, as "Backwards"/"Forwards").
- `fxa-menu-message-backup-sync-secondary-text` — `browser/browser/newtab/asrouter.ftl` — "Sync" left untranslated while every sibling string in the same block renders it "Synchronise".
  - Current: `Sync backs up most of your data`
  - en-US: `Synchronise backs up most of your data`
  - In this same FxA Menu Message block en-GB renders en-US "Sync"/"syncing" as "Synchronise"/"synchronising" in every other string (fxa-menu-message-sync-button, -sync-devices-primary-text, -sync-devices-collapsed-text, -backup-sync-primary-text "safe and synchronised", -backup-sync-collapsed-text "Synchronise and back up data", -mobile-secondary-text, -mobile-collapsed-text). Only this one keeps th…
- `policy-AllowFileSelectionDialogs` — `browser/browser/policies/policies-descriptions.ftl` — UI term "dialog" spelled "dialogues" here, against the tree's dominant "dialog".
  - Current: `Allow file selection dialogues.`
  - en-US: `Allow file selection dialogs.`
  - The en-GB tree uses "dialog" for the UI-window sense about 388 times against 22 "dialogue" (e.g. toolkit/toolkit/global/handlerDialog.ftl, browser/browser/sanitize.ftl, browser/browser/tabbrowser.ftl). "Dialogue" is the conversation sense in British English and is not the established term here.
- `policy-UseSystemPrintDialog` — `browser/browser/policies/policies-descriptions.ftl` — "print dialogue" conflicts with "print dialog" used in the locale's printing files.
  - Current: `Print using the system print dialogue.`
  - en-US: `Print using the system print dialog.`
  - toolkit/toolkit/printing/printUI.ftl and toolkit/chrome/global/printdialog.properties in this same tree use "print dialog" for the identical concept, so this string diverges from the locale's own printing terminology.
- `permissions-exceptions-https-only-desc` — `browser/browser/preferences/permissions.ftl` — Uses en-US “websites” where this locale consistently writes “web sites”.
  - Current: `for specific websites.`
  - en-US: `for specific web sites.`
  - en-GB writes “web site(s)” throughout the tree (251 occurrences across 45 files, including the immediately following string permissions-exceptions-https-only-desc2, which renders the same sentence as “for specific web sites”). This is the only user-visible “websites” left in the preferences partition.
- `preferences-data-migration-description` — `browser/browser/preferences/preferences.ftl` — “auto-fill” hyphenated here but spelled “autofill” everywhere else in the locale.
  - Current: `auto-fill data`
  - en-US: `autofill data`
  - This is the only occurrence of “auto-fill” in the whole en-GB tree; the sibling string preferences-data-migration-group in the same file says “autofill data”, and formAutofill.ftl/preferences.ftl use “autofill” consistently (180+ occurrences).
- `shopping-avatar-tooltip` — `browser/browser/profiles.ftl` — The same shopping icon is called a "basket" in its label and alt text but a "trolley" in its tooltip.
  - Current: `Apply shopping trolley avatar`
  - en-US: `Apply shopping basket avatar`
  - In the same file, shopping-avatar and shopping-avatar-alt both render en-US "Shopping cart" as "Shopping basket", and the locale uses "shopping baskets" for "shopping carts" in browser/browser/sanitize.ftl (item-cookies-site-data-description) and browser/browser/protectionsPanel.ftl (protections-panel-cookie-banner-view-cookie-clear-warning). "Trolley" is an isolated departure describing the same…
- `check` — `dom/chrome/accessibility/unix/accessible.properties` — The checkbox action is adapted to "Tick"/"Untick" in the parallel mac file but left as "Check"/"Uncheck" here.
  - Current: `check = Check`
  - en-US: `check = Tick`
  - For the identical string IDs, dom/chrome/accessibility/mac/accessible.properties uses "Tick"/"Untick", and the locale uses "tick" for checkbox actions elsewhere (AccessFu.properties "tick button", "tick menu item"; dom.properties "Please tick this box"). The unix/win platform files are the odd ones out for the same UI action.
- `check` — `dom/chrome/accessibility/win/accessible.properties` — The checkbox action is adapted to "Tick"/"Untick" in the parallel mac file but left as "Check"/"Uncheck" here.
  - Current: `check = Check`
  - en-US: `check = Tick`
  - Same inconsistency as the unix file: mac/accessible.properties renders these very IDs as "Tick"/"Untick", and AccessFu.properties uses "tick button"/"tick menu item", so the win file diverges from the locale's own choice for the same action.
- `back` — `toolkit/chrome/global/narrate.properties` — Skip-back/skip-forward controls named both "Backwards/Forwards" and "Back/Forward" in the same file.
  - Current: `back = Backwards`
  - en-US: `back = Back`
  - `back` and `previous-label` label the same Narrate control, as do `forward` and `next-label`. The first pair was changed to "Backwards"/"Forwards" while the second pair kept "Back (%S)"/"Forward (%S)", so one control carries two names. The en-US source for `back` is "Back" (not "Backward"), so no en-GB adverb adaptation was required here.
- `fp-certerror-revoked-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — "any more" here versus "anymore" in four sibling strings carrying the identical clause.
  - Current: `isn’t trusted any more.`
  - en-US: `isn’t trusted anymore.`
  - certError.ftl uses "isn’t trusted anymore" at lines 94, 157, 167 and 171; only line 81 splits it. Both forms are current in British English, so this is reported purely as a departure from what the file and the wider tree (7 occurrences of "anymore") do consistently, not as a preference.

### C. Grammar, agreement & spelling

- `autofill-address-postal-code` — `browser/browser/preferences/formAutofill.ftl` — “Post Code” is not the British form of the term; en-GB writes “Postcode” as one word.
  - Current: `Post Code`
  - en-US: `Postcode`
  - The locale deliberately adapted en-US “Postal Code”, but the UK term (Royal Mail, and the locale's own bundled en-GB dictionary, which lists only “postcode”) is the single word “Postcode”; “Post Code” is neither the en-US source form nor the en-GB convention.
- `prefs-syncing-off` — `browser/browser/preferences/preferences.ftl` — `prefs-syncing-off` still uses the en-US form “syncing”
  - Current: `Syncing: OFF`
  - en-US: `synchronising`
  - This locale writes “synchronising” for “syncing” in 22 other strings and keeps “syncing” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `prefs-syncing-on` — `browser/browser/preferences/preferences.ftl` — `prefs-syncing-on` still uses the en-US form “syncing”
  - Current: `Syncing: ON`
  - en-US: `synchronising`
  - This locale writes “synchronising” for “syncing” in 22 other strings and keeps “syncing” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `safeb-palm-accept-label` — `browser/browser/safebrowsing/blockedSite.ftl` — Button label reads "Go backwards" where the locale consistently labels this action "Go back"
  - Current: `Go backwards`
  - en-US: `Go back`
  - Every other standalone back-button label in the en-GB tree uses "Go back" (toolkit/toolkit/global/mozPageHeader.ftl, toolkit/toolkit/about/abuseReports.ftl:32, toolkit/toolkit/about/aboutAddons.ftl:265, toolkit/toolkit/neterror/certError.ftl:75, browser/browser/places.ftl:241). "Go backwards" as a button label is unidiomatic in en-GB and inconsistent with the locale's own usage; the adverbial "ba…
- `tabHistory.goBack` — `browser/chrome/browser/browser.properties` — "Go backwards to this page" is unidiomatic; en-GB uses "Go back to" with a destination
  - Current: `Go backwards to this page`
  - en-US: `Go back to this page`
  - In en-GB "backwards" is a directional adverb ("Go backwards one page", browserContext.ftl:17) but takes "back" before a destination phrase: the locale writes "Go back to aggregates" (devtools/client/memory.properties:53) and "Go back" for the Back tooltip in places.ftl:241. "Go backwards to this page" mixes the two patterns.
- `discopane-intro` — `toolkit/toolkit/about/aboutAddons.ftl` — "software programmes" uses the broadcast/schedule sense; British English spells computer programs "programs".
  - Current: `These small software programmes are`
  - en-US: `These small software programs are`
  - In en-GB, "programme" means a broadcast or plan; a computer program is spelled "program". The rest of this locale follows that rule (toolkit/toolkit/global/extensions.ftl "Another program on your computer…", toolkit/toolkit/neterror/certError.ftl "if an antivirus program…", toolkit/toolkit/neterror/nsserrors.ftl "enabled in this program").
- `discopane-intro3` — `toolkit/toolkit/about/aboutAddons.ftl` — "software programmes" uses the broadcast/schedule sense; British English spells computer programs "programs".
  - Current: `so much more. These small software programmes are often developed by a third party.`
  - en-US: `so much more. These small software programs are often developed by a third party.`
  - Same as discopane-intro: en-GB uses "program" for computer software, and this locale does so consistently elsewhere in toolkit (extensions.ftl, certError.ftl, nsserrors.ftl).
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — `rights-webservices-term-6` still uses the en-US form “canceled”
  - Current: `{ -vendor-short-name } may update these terms as necessary from time to time. These terms may not be modified or canceled without { -vendor-short-name }’s written agreement.`
  - en-US: `cancelled`
  - This locale writes “cancelled” for “canceled” in 20 other strings and keeps “canceled” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `abuse-report-messagebar-aborted` — `toolkit/toolkit/about/abuseReports.ftl` — `abuse-report-messagebar-aborted` still uses the en-US form “canceled”
  - Current: `Report for <span data-l10n-name="addon-name">{ $addon-name }</span> canceled.`
  - en-US: `cancelled`
  - This locale writes “cancelled” for “canceled” in 20 other strings and keeps “canceled” in 2. This string is byte-identical to en-US, so the substitution looks simply to have been missed.
- `region-name-fk` — `toolkit/toolkit/intl/regionNames.ftl` — US-only "(Islas Malvinas)" gloss retained on the Falkland Islands entry.
  - Current: `Falkland Islands (Islas Malvinas)`
  - en-US: `Falkland Islands`
  - The parenthetical Argentine name is a US State Department naming convention. British English usage, including UK government and UK-facing software, uses the bare "Falkland Islands"; presenting the disputed name as an alternative title is a variant-specific defect rather than a faithful mirror of a neutral source.

### D. Terminology, register & consistency

- `recommended-theme-1` — `toolkit/toolkit/about/aboutAddons.ftl` — Product name "Firefox Color" was spelling-adapted to "Firefox Colour", against the explicit developer comment.
  - Current: `Build your own theme with Firefox Colour.`
  - en-US: `Build your own theme with Firefox Color.`
  - The developer comment above this string states the "Firefox Color" name itself should not be translated; it is the name of a Mozilla product.
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — The proper name of the licence document, "Mozilla Public License", was respelled as "Mozilla Public Licence" (twice in the string).
  - Current: `Mozilla Public Licence`
  - en-US: `Mozilla Public License`
  - "Mozilla Public License" is the official title of a specific legal instrument (as reproduced verbatim in every file header of this same tree) and is not subject to the licence/license noun rule. Note the generic noun uses elsewhere in this partition ("Licence information") are correct and should stay.

### E. Typography, punctuation & spacing

- `migration-wizard-import-browser-no-browsers` — `browser/browser/migrationWizard.ftl` — "programs" over-corrected to "programmes", which in British English means broadcasts/schedules, not software.
  - Current: `couldn’t find any programmes that contain bookmark, history or password data`
  - en-US: `couldn’t find any programs that contain bookmark, history or password data`
  - British English retains the spelling "program" for computer software and reserves "programme" for broadcasts, events and plans. The locale itself follows this everywhere else, including the equivalent legacy string no-migration-sources in browser/browser/migration.ftl ("No programs that contain bookmarks, history or password data could be found.") and toolkit/toolkit/global/extensionPermissions.f…
- `PINotInProlog` — `dom/chrome/layout/xul.properties` — "prolog" (the XML technical term) was over-corrected to "prologue", and the sibling string keeps "prolog".
  - Current: `does not have any effect outside the prologue any longer`
  - en-US: `does not have any effect outside the prolog any longer`
  - "prolog" here is the XML specification term (the XML prolog), not the ordinary word; the immediately following string PINotInProlog2 in the same file correctly keeps "outside the prolog", so the file contradicts itself.

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._

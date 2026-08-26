# Firefox l10n QA — en-GB

| | |
|---|---|
| **Generated** | 2026-08-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b82b7a344c63` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcb4650bbefb` |
| **Previous run** | 2026-08-25 @ `ad52f2a75880` |
| **Mode** | incremental |
| **Strings reviewed this run** | 41 of 18,210 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for en-GB: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (2)

- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — The proper name "Mozilla Public License" has been altered to "Mozilla Public Licence".
    - Current: `<a data-l10n-name="mozilla-public-license-link">Mozilla Public Licence</a>`
    - Source: `{ -brand-short-name } is made available to you under the terms of the <a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>. This means you may use, copy and distribute { -brand-short-name } to othe…`
    - Suggest: `<a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>`
    - "Mozilla Public License" is the official name of a legal document and must not be respelled, even though "licence" is the British noun spelling.
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — Second occurrence of the proper name "Mozilla Public License" respelled as "Licence".
    - Current: `The Mozilla Public Licence also gives you the right`
    - Source: `{ -brand-short-name } is made available to you under the terms of the <a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>. This means you may use, copy and distribute { -brand-short-name } to othe…`
    - Suggest: `The Mozilla Public License also gives you the right`
    - The official licence name is a proper noun and should retain its US spelling as in the source.

### ✅ Fixed since the last run (5)

- `urlbar-popup-blocked2` — `browser/browser/browser.ftl` — "website" is used here although this file writes "web site" as two words everywhere else, including in the near-identical sibling string urlbar-popup-blocked.
    - Current: `for this website.`
    - Source: `tooltiptext: You have blocked pop-ups and third-party redirects for this website.`
    - Suggest: `for this web site.`
    - browser.ftl contains 22 visible-string occurrences of "web site"/"web sites" and this is the only visible-string occurrence of "website"; the adjacent urlbar-popup-blocked, which differs only by the redirect clause, reads "You have blocked pop-ups for this web site."
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
- `fp-certerror-revoked-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — "any more" here versus "anymore" in four sibling strings carrying the identical clause.
    - Current: `isn’t trusted any more.`
    - Source: `{ -brand-short-name } is warning you about this site because the certificate provided for { $hostname } has been revoked and isn’t trusted anymore.`
    - Suggest: `isn’t trusted anymore.`
    - certError.ftl uses "isn’t trusted anymore" at lines 94, 157, 167 and 171; only line 81 splits it. Both forms are current in British English, so this is reported purely as a departure from what the file and the wider tree (7 occurrences of "anymore") do consistently, not as a preference.
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — The proper name of the licence document, "Mozilla Public License", was respelled as "Mozilla Public Licence" (twice in the string).
    - Current: `Mozilla Public Licence`
    - Source: `{ -brand-short-name } is made available to you under the terms of the <a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>. This means you may use, copy and distribute { -brand-short-name } to othe…`
    - Suggest: `Mozilla Public License`
    - "Mozilla Public License" is the official title of a specific legal instrument (as reproduced verbatim in every file header of this same tree) and is not subject to the licence/license noun rule. Note the generic noun uses elsewhere in this partition ("Licence information") are correct and should stay.

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
| Files | 362 |
| Strings | 18,210 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 2 |
| Source-language spellings left unchanged | 2 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 41 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 597, `curly-single` 101, `straight-double` 58 | **curly-double** |
| apostrophe | `typographic` 1123, `straight` 56 | **typographic** |
| ellipsis | `char` 461, `ascii` 1 | **char** |
| dash | `em` 108, `en` 4 | **em** |
| nbsp | `total` 5, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

- **typography — 41 strings** — 41 strings. These deviate from the convention the rest of the tree follows. Whether to normalize them is one decision.
    - Affected: `BlockMixedActiveContent`, `BlockMixedDisplayContent`, `CSPROViolation`, `CSPROViolationWithURI`, `CSPViolation`, `CSPViolationWithURI`, `DontAskAgain`, `FullscreenDeniedContainerNotAllowed`, `ImageMapCircleNegativeRadius`, `ImageMapCircleWrongNumberOfCoords`, `ImageMapPolyOddNumberOfCoords`, `ImageMapPolyWrongNumberOfCoords` …and 25 more

---

## 3. Open findings (19)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 4 |
| 2 | Wrong content (says something other than the English) | 9 |
| 3 | Degraded language (grammar, spelling, terminology) | 5 |
| 4 | Cosmetic (typography, spacing) | 1 |

### A. Functional, markup, variables & plurals

- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — The [1] singular variant uses plural "passwords" instead of the singular "the password" of the source.
    - Current: `[1] This will remove the passwords saved to`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices. This will also remove any breach alerts that appear here. You cannot undo this action. [other] This will remove al…`
    - Suggest: `[1] This will remove the password saved to`
    - The en-US [1] case reads "This will remove the password saved to…"; the singular plural form must stay singular in the count=1 variant.

### B. Mistranslation, reversed meaning, wrong names & brand

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
- `statePartiallyChecked` — `dom/chrome/accessibility/AccessFu.properties` — Accessibility state name "checked" wrongly changed to "ticked".
    - Current: `partially ticked`
    - Source: `partially checked`
    - Suggest: `partially checked`
    - "Checked" is the standard ARIA/accessibility state term (aria-checked) reported by screen readers and is identical in en-GB; substituting "ticked" changes established terminology and breaks consistency with other checkbox state strings.
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
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — The proper name "Mozilla Public License" has been altered to "Mozilla Public Licence".
    - Current: `<a data-l10n-name="mozilla-public-license-link">Mozilla Public Licence</a>`
    - Source: `{ -brand-short-name } is made available to you under the terms of the <a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>. This means you may use, copy and distribute { -brand-short-name } to othe…`
    - Suggest: `<a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>`
    - "Mozilla Public License" is the official name of a legal document and must not be respelled, even though "licence" is the British noun spelling.
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — Second occurrence of the proper name "Mozilla Public License" respelled as "Licence".
    - Current: `The Mozilla Public Licence also gives you the right`
    - Source: `{ -brand-short-name } is made available to you under the terms of the <a data-l10n-name="mozilla-public-license-link">Mozilla Public License</a>. This means you may use, copy and distribute { -brand-short-name } to othe…`
    - Suggest: `The Mozilla Public License also gives you the right`
    - The official licence name is a proper noun and should retain its US spelling as in the source.

### C. Grammar, agreement & spelling

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
- `recommended-theme-1` — `toolkit/toolkit/about/aboutAddons.ftl` — Product name "Firefox Color" was spelling-adapted to "Firefox Colour", against the explicit developer comment.
    - Current: `Build your own theme with Firefox Colour.`
    - Source: `Feeling creative? <a data-l10n-name="link">Build your own theme with Firefox Color.</a>`
    - Suggest: `Build your own theme with Firefox Color.`
    - The developer comment above this string states the "Firefox Color" name itself should not be translated; it is the name of a Mozilla product.

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

### Suppressed as false positives (12)

- **`en-GB-backwards-forwards`** (4) — "Backwards" and "Forwards" are the en-GB house forms for the en-US "Back" and "Forward", in navigation labels and accessibility descriptions alike. See conventions.md.
    - `customkeys-nav-forward`, `safeb-palm-accept-label`, `tabHistory.goBack`, `back`
- **`en-GB-post-code`** (1) — "Post Code" is the deliberate en-GB rendering of the en-US "Postal Code"; "Postcode" must not be suggested in its place. See conventions.md.
    - `autofill-address-postal-code`
- **`en-GB-sync-short-form-accepted`** (4) — The mirror image: the short "sync" is equally accepted, so the short and spelled-out forms sitting side by side is not an inconsistency to report. Scoped to category B so a genuine mistranslation of a string that happens to mention sync still reports. See conventions.md.
    - `about-logins-confirm-remove-all-sync-dialog-message3`, `appmenu-remote-tabs-sign-into-sync`, `appmenu-remote-tabs-turn-on-sync`, `fxa-menu-message-backup-sync-secondary-text`
- **`en-GB-sync-variant-spelling`** (2) — `variant_spelling` counts the tree and reports the minority form, so it reads the strings that kept "syncing" as a missed substitution. Both forms are accepted here, so the split is not a defect. See conventions.md.
    - `prefs-syncing-off`, `prefs-syncing-on`
- **`en-GB-web-site-two-words`** (1) — "web site" / "web sites" is the en-GB house form; a suggestion to close it up to the en-US "website" must never be accepted. See conventions.md.
    - `permissions-exceptions-https-only-desc`

_Suppressions live in `locales/en-GB/suppressions.yaml`. Removing a rule brings its findings back._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (12)

- `urlbar-popup-blocked2` — `browser/browser/browser.ftl` — fixed 2026-08-26
- `mr2022-onboarding-colorway-description-dreamer` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-26
- `SEC_ERROR_LIBPKIX_INTERNAL` — `security/manager/chrome/pipnss/nsserrors.properties` — fixed 2026-08-26
- `rights-intro-point-1` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-08-26
- `fp-certerror-revoked-why-dangerous-body` — `toolkit/toolkit/neterror/certError.ftl` — fixed 2026-08-26
- `helpus-referrals2` — `browser/browser/aboutDialog.ftl` — fixed 2026-08-24
- `permissions-exceptions-https-only-desc` — `browser/browser/preferences/permissions.ftl` — fixed 2026-08-21
- `preferences-data-migration-description` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-21
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-08-20
- `rights-webservices-term-6` — `toolkit/toolkit/about/aboutRights.ftl` — fixed 2026-08-20
- `abuse-report-messagebar-aborted` — `toolkit/toolkit/about/abuseReports.ftl` — fixed 2026-08-20
- `abuse-report-messagebar-aborted` — `toolkit/toolkit/about/abuseReports.ftl` — fixed 2026-08-20

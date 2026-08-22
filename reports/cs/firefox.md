# Firefox l10n QA — cs

| | |
|---|---|
| **Generated** | 2026-08-22 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `9441127ed8c4` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `60f24d17564f` |
| **Previous run** | 2026-08-21 @ `bd0ff4b2f741` |
| **Mode** | incremental |
| **Strings reviewed this run** | 8 of 18,169 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for cs: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Strings | 18,169 |
| Missing strings | 11 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 7 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 6 |
| Term parameter mismatches | 3 |
| Plural variants (dead or missing forms) | 77 |
| Text quoting a UI label that no longer matches | 6 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 4 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 4 |

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
| quotes | `german-double` 526, `curly-double` 231, `curly-single` 60, `straight-double` 46, `polish-double` 3 | _mixed_ |
| apostrophe | `typographic` 74, `straight` 11 | **typographic** |
| ellipsis | `char` 451, `ascii` 4 | **char** |
| dash | `em` 101, `en` 30 | **em** |
| nbsp | `total` 13, `before-punctuation` 3, `space-before-punctuation` 8 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

- **plurals — 77 strings** — 77 strings. The locale's plural variants differ from what the rest of its tree does. At this scale it is a convention to settle once, not a defect per string.
    - Affected: `about-logins-confirm-remove-all-dialog-title`, `about-logins-confirm-remove-all-sync-dialog-title`, `about-processes-active-threads`, `about-processes-inactive-threads`, `about-processes-profile-process`, `about-reader-estimated-read-time`, `about-telemetry-histogram-stats`, `about-webrtc-channels`, `about-webrtc-frames`, `about-webrtc-lost-label`, `about-webrtc-received-label`, `about-webrtc-sent-label` …and 65 more

---

## 3. Open findings (258)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 54 |
| 2 | Wrong content (says something other than the English) | 120 |
| 3 | Degraded language (grammar, spelling, terminology) | 56 |
| 4 | Cosmetic (typography, spacing) | 23 |

### A. Functional, markup, variables & plurals

- `about-private-browsing-nova-info-subheader2` — `browser/browser/aboutPrivateBrowsing.ftl` — “like blocking trackers” became “like trackers”, so the sentence says trackers are a protection that is on.
    - Current: `jako třeba sledovací prvky, jsou zapnuté`
    - Source: `We’ll erase every search and sign-in when you close all your Private Windows. { -brand-short-name }’s built-in protections are on here too, like blocking trackers.`
    - Suggest: `jako třeba blokování sledovacích prvků, jsou zapnuté`
    - en-US: “…built-in protections are on here too, like blocking trackers.” The sibling string about-private-browsing-nova-info-subheader renders it correctly as “blokování sledovacích prvků”.
- `appmenuitem-new-ai-window` — `browser/browser/aiWindow.ftl` — `appmenuitem-new-ai-window` (`.value`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
    - Current: `Nové { -smart-window-brand-name }`
    - Source: `label: New { -smart-window-brand-name } value: New { -smart-window-brand-name }`
    - The term falls back to its catch-all variant, so the intended form is never selected.
- `menu-file-new-ai-window` — `browser/browser/aiWindow.ftl` — `menu-file-new-ai-window` (`.label`) calls `-smart-window-brand-name` with ['capitalization'], but that term selects on ['case', 'plural-form']
    - Current: `Nové { -smart-window-brand-name }`
    - Source: `label: New { -smart-window-brand-name }`
    - The term falls back to its catch-all variant, so the intended form is never selected.
- `action-log-searched-web-with-exa` — `browser/browser/aiWindowContent.ftl` — The completed-action label is identical to the in-progress one, losing the past tense.
    - Current: `Vyhledávání na webu pomocí <a data-l10n-name="exa-link">Exa</a>`
    - Source: `Searched the web with <a data-l10n-name="exa-link">Exa</a>`
    - Suggest: `Vyhledáno na webu pomocí <a data-l10n-name="exa-link">Exa</a>`
    - en-US distinguishes “Searching the web with Exa” from “Searched the web with Exa”; the file keeps that distinction elsewhere (action-log-searching-web / action-log-searched-web).
- `smart-window-confirm-group-tab` — `browser/browser/aiWindowContent.ftl` — Button label translated as the noun “group” although the developer comment states “Group” is a verb.
    - Current: `Skupina`
    - Source: `Group`
    - Suggest: `Seskupit`
    - Comment: '# Button label - "Group" is a verb (action to group tabs)'. The same problem affects smart-window-confirm-group-tabs (“Skupina { $count } panelů”), which reads as a label, not an action.
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — “which ones (tabs)” rendered as “záložky” (bookmarks) instead of “panely” (tabs).
    - Current: `vyberte, které záložky chcete seskupit`
    - Source: `If you still want to group tabs, choose <strong>Retry</strong> and select which ones in the card that opens.`
    - Suggest: `vyberte, které panely chcete seskupit`
    - en-US: “…select which ones in the card that opens”, referring to tabs; the same sentence already uses “panely” for tabs, so “záložky” names the wrong object.
- `appmenu-help-not-deceptive` — `browser/browser/appmenu.ftl` — Access key `l` of `appmenu-help-not-deceptive` is not present in its label
    - Current: `l`
    - Source: `accesskey: d label: This isn’t a deceptive site…`
    - The label is “Tato stránka není podvodná…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `urlbar-result-action-calculator-result-decimal` — `browser/browser/browser.ftl` — The calculator result is printed twice, producing output like “0.3330.333”.
    - Current: `= { NUMBER($result, maximumSignificantDigits: 9) }{ NUMBER($result, maximumSignificantDigits: 9) }`
    - Source: `= { $result }`
    - Suggest: `= { NUMBER($result, maximumSignificantDigits: 9) }`
    - en-US has a single NUMBER() call; the duplicated call concatenates the number with itself in the address bar result.
- `main-context-menu-reveal-password` — `browser/browser/browserContext.ftl` — Access key `v` of `main-context-menu-reveal-password` is not present in its label
    - Current: `v`
    - Source: `accesskey: v label: Reveal Password`
    - The label is “Zobrazit heslo”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `login-status-advisory-title` — `browser/browser/featureCallout.ftl` — Negation added: en-US says the user IS signed out, Czech says they are NOT signed out.
    - Current: `Nejste odhlášeni. Pro přihlášení klepněte na ikonu účtu.`
    - Source: `You’re signed out. Click the account icon to sign in.`
    - Suggest: `Jste odhlášeni. Pro přihlášení klepněte na ikonu účtu.`
    - en-US: “You’re signed out. Click the account icon to sign in.” The Czech reverses the state, contradicting the call to action in the same sentence.
- `taskbar-tabs-media-callout-subtitle` — `browser/browser/featureCallout.ftl` — The no-cases variant is a copy of the e-mail callout and talks about webmail instead of streaming sites.
    - Current: `*[no-cases] Spusťte webmail jako aplikaci v jednoduchém okně chráněném aplikací { -brand-short-name }.`
    - Source: `Launch your streaming sites like an app in a streamlined window protected by { -brand-short-name }.`
    - Suggest: `*[no-cases] Spouštějte své streamovací stránky jako aplikaci v jednoduchém okně chráněném aplikací { -brand-short-name }.`
    - en-US: “Launch your streaming sites like an app…”. The with-cases variant of the same message is correct, so only this branch is wrong.
- `menu-help-not-deceptive` — `browser/browser/menubar.ftl` — Access key `l` of `menu-help-not-deceptive` is not present in its label
    - Current: `l`
    - Source: `accesskey: D label: This Isn’t a Deceptive Site…`
    - The label is “Tato stránka není podvodná…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `browser-data-cookies-checkbox` — `browser/browser/migration.ftl` — `browser-data-cookies-checkbox` (`.label`) switches on ['browser'], which en-US does not pass (it provides nothing)
    - Current: `{$browser ->} [firefox] Cookies [chrome] Soubory cookie [edge] Soubory cookie [safari] Cookies [other] Cookies`
    - Source: `label: Cookies`
    - Suggest: `Cookies`
    - Selecting on a variable the code does not pass makes every variant unreachable and the number render blank.
- `browser-data-cookies-label` — `browser/browser/migration.ftl` — `browser-data-cookies-label` (`.value`) switches on ['browser'], which en-US does not pass (it provides nothing)
    - Current: `{$browser ->} [firefox] Cookies [chrome] Soubory cookie [edge] Soubory cookie [safari] Cookies [other] Cookies`
    - Source: `value: Cookies`
    - Suggest: `Cookies`
    - Selecting on a variable the code does not pass makes every variant unreachable and the number render blank.
- `browser-data-formdata-checkbox` — `browser/browser/migration.ftl` — `browser-data-formdata-checkbox` (`.label`) switches on ['browser'], which en-US does not pass (it provides nothing)
    - Current: `{$browser ->} [firefox] Uložená historie formulářů [chrome] Uložená historie formulářů [edge] Vyplňování formulářů [safari] Vyplňování formulářů [other] Uložená historie formulářů`
    - Source: `label: Saved Form History`
    - Suggest: `Saved Form History`
    - Selecting on a variable the code does not pass makes every variant unreachable and the number render blank.
- `browser-data-formdata-label` — `browser/browser/migration.ftl` — `browser-data-formdata-label` (`.value`) switches on ['browser'], which en-US does not pass (it provides nothing)
    - Current: `{$browser ->} [firefox] Uložená historie formulářů [chrome] Uložená historie formulářů [edge] Vyplňování formulářů [safari] Vyplňování formulářů [other] Uložená historie formulářů`
    - Source: `value: Saved Form History`
    - Suggest: `Saved Form History`
    - Selecting on a variable the code does not pass makes every variant unreachable and the number render blank.
- `browser-data-passwords-checkbox` — `browser/browser/migration.ftl` — `browser-data-passwords-checkbox` (`.label`) switches on ['browser'], which en-US does not pass (it provides nothing)
    - Current: `{$browser ->} [firefox] Uložená uživatelská jména a hesla [chrome] Uložená hesla [edge] Uložená hesla [safari] Hesla [other] Uložená uživatelská jména a hesla`
    - Source: `label: Saved Logins and Passwords`
    - Suggest: `Saved Logins and Passwords`
    - Selecting on a variable the code does not pass makes every variant unreachable and the number render blank.
- `browser-data-passwords-label` — `browser/browser/migration.ftl` — `browser-data-passwords-label` (`.value`) switches on ['browser'], which en-US does not pass (it provides nothing)
    - Current: `{$browser ->} [firefox] Uložená uživatelská jména a hesla [chrome] Uložená hesla [edge] Uložená hesla [safari] Hesla [other] Uložená uživatelská jména a hesla`
    - Source: `value: Saved Logins and Passwords`
    - Suggest: `Saved Logins and Passwords`
    - Selecting on a variable the code does not pass makes every variant unreachable and the number render blank.
- `migration-wizard-progress-extensions-addons-link` — `browser/browser/migrationWizard.ftl` — "Browse extensions" rendered as "Prohledávat" (search through) instead of "Procházet" (browse).
    - Current: `Prohledávat rozšíření pro`
    - Source: `Browse extensions for { -brand-short-name }`
    - Suggest: `Procházet rozšíření pro`
    - The link opens the add-ons catalogue for browsing, not a search function.
- `fxa-adoption-addresses-backup-subtitle` — `browser/browser/newtab/asrouter.ftl` — Talks about protecting passwords, while the message and its title are about saved addresses.
    - Current: `Chraňte svá hesla synchronizací se zařízeními pomocí šifrování.`
    - Source: `Protect your saved addresses by syncing them to your devices with encryption.`
    - Suggest: `Chraňte své uložené adresy tím, že je synchronizujete se svými zařízeními pomocí šifrování.`
    - en-US: "Protect your saved addresses by syncing them to your devices with encryption." The sibling strings (credit cards, bookmarks) correctly name their own data type; only this one names the wrong one.
- `fxa-menu-message-sign-up-button` — `browser/browser/newtab/asrouter.ftl` — "Sign up" rendered as "Přihlásit se", identical to the "Sign in" button.
    - Current: `Přihlásit se`
    - Source: `Sign up`
    - Suggest: `Zaregistrovat se`
    - en-US distinguishes fxa-menu-message-sign-up-button ("Sign up") from fxa-menu-message-sign-in-button ("Sign in"); both are "Přihlásit se" in Czech, so the account-creation action is mislabelled. The locale uses "Zaregistrovat se" for Sign up in fxa-adoption-primary-button-label in the same file.
- `home-homepage-new-tabs` — `browser/browser/newtab/newtab.ftl` — "New tabs" rendered as "In a new tab", breaking the parallel with "Nová okna".
    - Current: `V novém panelu`
    - Source: `label: New tabs`
    - Suggest: `Nové panely`
    - en-US label is the plural noun phrase "New tabs", matching "New windows" ("Nová okna") in the row above; the Czech turns it into a prepositional phrase and makes it singular.
- `newtab-sports-widget-world-cup-champions` — `browser/browser/newtab/newtab.ftl` — "2026 World Cup Champions" rendered as just the tournament name, dropping "Champions".
    - Current: `Mistrovství světa ve fotbale 2026`
    - Source: `2026 World Cup Champions`
    - Suggest: `Mistři světa 2026`
    - The label is shown over the winning team on the result card; as translated it names the tournament rather than the champions, unlike the short variant newtab-sports-widget-world-cup-champions-short ("Mistři pro rok 2026").
- `mr2022-upgrade-onboarding-pin-private-window-subtitle` — `browser/browser/newtab/onboarding.ftl` — The whole sentence is duplicated in two slightly different wordings, with no space between them.
    - Current: `Žádné uložené cookies ani historie, přímo z vaší plochy. Prohlížejte, jako když se nikdo nedívá.Žádné uložené soubory cookies ani historie, přímo z vaší plochy. Prohlížejte, jako by se nikdo nedíval.`
    - Source: `No saved cookies or history, right from your desktop. Browse like no one’s watching.`
    - Suggest: `Žádné uložené soubory cookies ani historie, přímo z vaší plochy. Prohlížejte, jako by se nikdo nedíval.`
    - en-US contains a single sentence pair; the Czech leftover duplicate is displayed to the user.
- `onboarding-new-user-survey-time-based-option-3` — `browser/browser/newtab/onboarding.ftl` — "More than 1 month" translated as "Less than 1 month", duplicating the previous survey option.
    - Current: `Méně než 1 měsíc, pravidelně`
    - Source: `More than 1 month, regularly`
    - Suggest: `Více než 1 měsíc, pravidelně`
    - en-US is "More than 1 month, regularly"; the Czech says "Less than", so options 2, 3 and 4 all read "Méně než 1 měsíc" and the survey answers become indistinguishable.
- `onboarding-new-user-survey-time-based-option-4` — `browser/browser/newtab/onboarding.ftl` — "More than 1 month" translated as "Less than 1 month".
    - Current: `Méně než 1 měsíc, příležitostně`
    - Source: `More than 1 month, occasionally`
    - Suggest: `Více než 1 měsíc, příležitostně`
    - en-US is "More than 1 month, occasionally"; reversed comparison.
- `policy-PrivateBrowsingModeAvailability` — `browser/browser/policies/policies-descriptions.ftl` — Says "set availability in private browsing mode" instead of "set availability of private browsing mode".
    - Current: `Nastaví dostupnost v režimu anonymního prohlížení.`
    - Source: `Set availability of private browsing mode.`
    - Suggest: `Nastaví dostupnost režimu anonymního prohlížení.`
    - en-US: "Set availability of private browsing mode." The policy controls whether the mode itself is available, not something inside it; the extra "v" inverts what an administrator would expect.
- `autofill-address-name` — `browser/browser/preferences/formAutofill.ftl` — The person's "Name" field is labelled "Název" (name of a thing).
    - Current: `Název`
    - Source: `Name`
    - Suggest: `Jméno`
    - This is the full-name field of an address record; Czech uses "Jméno" for people (as in autofill-passport-name), while "Název" denotes a title of an object.
- `autofill-address-state` — `browser/browser/preferences/formAutofill.ftl` — "State" is translated as "Země" (country), the same word used for the Country field.
    - Current: `Země`
    - Source: `State`
    - Suggest: `Stát`
    - autofill-address-country-only is also "Země"; labelling the state/province level as "country" is a reversed level in the address hierarchy and collides with the actual country field.
- `autofill-address-townland` — `browser/browser/preferences/formAutofill.ftl` — Irish "Townland" is translated as "Město" (city), identical to the City field.
    - Current: `Město`
    - Source: `Townland`
    - Suggest: `Townland (katastrální osada)`
    - A townland is a rural land division below the locality level; using "Město" duplicates autofill-address-city and mislabels the sublocality field for Irish addresses.
- `preferences-etp-level-strict` — `browser/browser/preferences/preferences.ftl` — "may cause some sites to break" translated as damaging websites.
    - Current: `mohou způsobit poškození některých webových stránek`
    - Source: `description: Stronger protections that block more trackers, but may cause some sites to break. label: Strict`
    - Suggest: `mohou omezit fungování některých webových stránek`
    - "Poškození webových stránek" says the browser damages the sites themselves; elsewhere in the file the same source idea is correctly rendered as "může omezit fungování některých stránek".
- `website-advertising-private-attribution` — `browser/browser/preferences/preferences.ftl` — "privacy-preserving ad measurement" is rendered as allowing "tracking advertising".
    - Current: `Umožnit webům použití sledující reklamy, která je šetrná k soukromí`
    - Source: `accesskey: a label: Allow websites to perform privacy-preserving ad measurement`
    - Suggest: `Umožnit webům měření výkonu reklamy šetrné k soukromí`
    - The checkbox permits measurement of ad performance, not the use of tracking ads; the description below correctly speaks about measuring how ads perform, so the label misstates what the user is enabling.
- `preonboarding-checklist-interaction-data-description` — `browser/browser/preonboarding.ftl` — "for users everywhere" translated as "pro běžné uživatele" (for ordinary users).
    - Current: `pro běžné uživatele`
    - Source: `Data about your device, hardware configuration, and how you use { -brand-product-name } helps improve features, performance, and stability for users everywhere.`
    - Suggest: `pro uživatele na celém světě`
    - en-US says the data improves things for users everywhere, not for "ordinary" users as opposed to advanced ones.
- `present-avatar-tooltip` — `browser/browser/profiles.ftl` — "Present" (gift box) translated as "současný" (current), the meaning the developer comment explicitly rules out.
    - Current: `Použít současný avatar`
    - Source: `tooltiptext: Apply present avatar`
    - Suggest: `Použít avatar dárku`
    - The comment says "Present refers to a gift box, not the current time period"; the alt text for the same icon is correctly "Dárek".
- `protections-panel-cookie-banner-blocker-view-turn-on-for-site` — `browser/browser/protectionsPanel.ftl` — `protections-panel-cookie-banner-blocker-view-turn-on-for-site` references ['host'], which en-US does not pass
    - Current: `Zapnout blokování lišť cookie pro { $host }?`
    - Source: `Turn on Cookie Banner Blocker for this site?`
    - Suggest: `Turn on Cookie Banner Blocker for this site?`
    - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.
- `safeb-palm-notdeceptive` — `browser/browser/safebrowsing/blockedSite.ftl` — Access key `l` of `safeb-palm-notdeceptive` is not present in its label
    - Current: `l`
    - Source: `accesskey: d label: This isn’t a deceptive site…`
    - The label is “Tato stránka není podvodná…”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `fxa-avatar-sign-up` — `browser/browser/sync.ftl` — "Sign up" (create an account) rendered as "Přihlásit se" (sign in), identical to fxa-avatar-sign-in.
    - Current: `Přihlásit se`
    - Source: `Sign up`
    - Suggest: `Vytvořit účet`
    - en-US distinguishes fxa-avatar-sign-in = "Sign in" from fxa-avatar-sign-up = "Sign up"; the Czech collapses the two.
- `close-tabs-to-the-start-vertical` — `browser/browser/tabContextMenu.ftl` — Singular "panel" where the action closes all tabs above; the three sibling strings use the plural.
    - Current: `Zavřít panel výše`
    - Source: `accesskey: l label: Close Tabs Above`
    - Suggest: `Zavřít panely výše`
    - en-US "Close Tabs Above"; close-tabs-to-the-end-vertical is correctly "Zavřít panely níže".
- `midi.shareWithSite` — `browser/chrome/browser/browser.properties` — MIDI permission prompt asks about contacts instead of MIDI devices, and drops "allow".
    - Current: `Chcete %S přístup k vašim kontaktům?`
    - Source: `Allow %S to access your MIDI devices?`
    - Suggest: `Chcete serveru %S povolit přístup k vašim MIDI zařízením?`
    - en-US is "Allow %S to access your MIDI devices?"; the Czech says "your contacts" (kontaktům), naming a completely different permission, and omits the verb "povolit". The sibling string midi.shareSysexWithSite correctly uses "přístup k vašim MIDI zařízením".
- `edit-controls.tooltiptext2` — `browser/chrome/browser/customizableui/customizableWidgets.properties` — Noun phrase "Edit controls" translated as the verb phrase "will edit the controls".
    - Current: `Upraví ovládání`
    - Source: `Edit controls`
    - Suggest: `Ovládání úprav`
    - "Edit controls" names the cut/copy/paste widget group (cf. edit-controls.label = "Úpravy"), matching "Zoom controls" which is correctly rendered as the noun phrase "Ovládání přiblížení stránky". "Upraví ovládání" states that the button edits the controls.
- `errorReportFalseDeceptiveMessage` — `browser/chrome/browser/safebrowsing/safebrowsing.properties` — Extra negation reverses the meaning: "cannot not report".
    - Current: `Tuto chybu teď nelze nehlásit.`
    - Source: `It’s not possible to report this error at this time.`
    - Suggest: `Tuto chybu teď nelze nahlásit.`
    - en-US: "It’s not possible to report this error at this time." The Czech has both "nelze" and "nehlásit", a double negation that inverts/garbles the sentence; it should be "nelze nahlásit".
- `UN_SURVEY_CHECKBOX_LABEL` — `browser/installer/custom.properties` — Uninstall survey label says "why you installed" instead of "why you uninstalled".
    - Current: `Řekněte Mozille, proč jste si aplikaci $BrandShortName nainstalovali`
    - Source: `Tell Mozilla why you uninstalled $BrandShortName`
    - Suggest: `Řekněte Mozille, proč jste si aplikaci $BrandShortName odinstalovali`
    - en-US: "Tell Mozilla why you uninstalled $BrandShortName". The string appears in the uninstaller, so the Czech asks the opposite question.
- `FileError` — `browser/installer/override.properties` — The third button option is described as "Cancel to stop the installation" instead of "Ignore to skip this file".
    - Current: `nebo na Storno pro ukončení instalace.`
    - Source: `Error opening file for writing:   $0  Click Abort to stop the installation, Retry to try again, or Ignore to skip this file.`
    - Suggest: `nebo na Ignorovat pro přeskočení tohoto souboru.`
    - en-US: "Click Abort to stop the installation, Retry to try again, or Ignore to skip this file." The Czech repeats the abort meaning and never explains the Ignore button; it also duplicates the FileError_NoIgnore wording.
- `document_properties_page_size_name_legal` — `browser/pdfviewer/viewer.properties` — Paper-format name "Legal" translated as "legal document".
    - Current: `Právní dokument`
    - Source: `Legal`
    - Suggest: `Legal`
    - "Legal" here is the paper size (8.5×14 in) in the page-size list alongside A3/A4/Letter, not a description of the document’s content; "Právní dokument" names the wrong thing and would render as e.g. "216 × 356 mm (Právní dokument, na výšku)".
- `document_properties_page_size_name_letter` — `browser/pdfviewer/viewer.properties` — Paper-format name "Letter" translated as the word for a mail letter.
    - Current: `Dopis`
    - Source: `Letter`
    - Suggest: `Letter`
    - This is the name of the North American paper size (Letter, 8.5×11 in) shown as a page-size name, not the word "letter" in the correspondence sense; "Dopis" names the wrong thing. Neighbouring size names A3/A4 are left as-is.
- `document_properties_title` — `browser/pdfviewer/viewer.properties` — PDF document "Title" metadata field labelled as page title.
    - Current: `Název stránky:`
    - Source: `Title:`
    - Suggest: `Název:`
    - In the Document Properties dialog this field is the PDF’s document Title metadata, not a page title; the dialog also has a separate "Velikost stránky" (Page Size) entry, so "Název stránky" misidentifies the field.
- `editor_ink_opacity` — `browser/pdfviewer/viewer.properties` — "Opacity" rendered as "transparency", the inverse property.
    - Current: `Průhlednost`
    - Source: `Opacity`
    - Suggest: `Neprůhlednost`
    - The control sets opacity (higher value = more opaque); "Průhlednost" means transparency, the inverse scale, so the slider label describes the opposite of what the value does.
- `player.runningOnCompositorTooltip` — `devtools/client/animationinspector.properties` — "compositor thread" translated as "composer's (musical) thread"
    - Current: `Tato animace běží na skladatelském vlákně`
    - Source: `This animation is running on compositor thread`
    - Suggest: `Tato animace běží na vlákně kompozitoru`
    - "skladatelský" in Czech relates to a music composer; the graphics compositor thread is "kompozitor"/"vlákno kompozitoru". The current wording is meaningless in the graphics context.
- `boxmodel.offsetParent.title` — `devtools/client/boxmodel.properties` — "Offset parent of the selected element" loses "parent"
    - Current: `Offset vybraného prvku`
    - Source: `Offset parent of the selected element`
    - Suggest: `Offsetový rodič vybraného prvku`
    - The tooltip labels the previewed DOM node that is the offset *parent*; as translated it reads as the offset value of the selected element.
- `pauseOnDebuggerStatement` — `devtools/client/debugger.properties` — "debugger statement" translated as generic "debugging"
    - Current: `Pozastavit při odlaďování`
    - Source: `Pause on debugger statement`
    - Suggest: `Pozastavit na příkazu debugger`
    - en-US "Pause on debugger statement" refers to the JavaScript `debugger;` statement, not to debugging in general; as translated the checkbox reads "Pause during debugging", which does not describe what it toggles.
- `dropShadowPlaceholder` — `devtools/client/filterwidget.properties` — drop-shadow parameter list mistranslated ("radius color" → "color of the radius")
    - Current: `x y barva radiusu`
    - Source: `x y radius color`
    - Suggest: `x y poloměr barva`
    - en-US lists four values "x y radius color"; the Czech merges the last two into "color of the radius", so the placeholder no longer documents the expected syntax.
- `fontinspector.fontVendor` — `devtools/client/font-inspector.properties` — Font "Vendor" translated as "Author"
    - Current: `Autor:`
    - Source: `Vendor:`
    - Suggest: `Dodavatel:`
    - "Vendor" is the distributor/foundry field; "Autor" conflates it with the designer, which is a separate field already translated as "Designér".
- `inspector-color-scheme-emulation-light` — `devtools/client/inspector.ftl` — "light" dropped, making the light and dark tooltips indistinguishable
    - Current: `Přepnutí emulace barevného schématu stránky`
    - Source: `title: Toggle light color scheme emulation for the page`
    - Suggest: `Přepnutí emulace světlého barevného schématu pro tuto stránku`
    - en-US is "Toggle light color scheme emulation for the page"; the paired dark string keeps "tmavého", so omitting "světlého" leaves the two buttons with tooltips that no longer differentiate them.
- `inspector.noProperties` — `devtools/client/inspector.properties` — "CSS properties" translated as "CSS rules"
    - Current: `Žádná pravidla CSS nebyla nalezena.`
    - Source: `No CSS properties found.`
    - Suggest: `Nebyly nalezeny žádné vlastnosti CSS.`
    - en-US is "No CSS properties found." and the message is shown in the computed-properties list; rules and properties are distinct concepts in the Inspector UI.
- `inspectorShowAccessibilityProperties.label` — `devtools/client/inspector.properties` — "Accessibility Properties" translated as accessibility "settings"
    - Current: `Zobrazit nastavení přístupnosti`
    - Source: `Show Accessibility Properties`
    - Suggest: `Zobrazit vlastnosti přístupnosti`
    - The item opens the accessibility properties of the node, not any settings; the sibling item inspectorShowDOMProperties.label correctly uses "vlastnosti".
- `flexbox.noFlexboxeOnThisPage` — `devtools/client/layout.properties` — Drops "Flex container" as a selectable option
    - Current: `Pro pokračování vyberte položku Flex kontejneru.`
    - Source: `Select a Flex container or item to continue.`
    - Suggest: `Pro pokračování vyberte flex kontejner nebo položku.`
    - en-US is "Select a Flex container or item to continue."; the Czech tells the user to select an item of a flex container only, hiding the container option.
- `dominatortree.field.label` — `devtools/client/memory.properties` — Column header "Dominator" translated as "Label"
    - Current: `Označení`
    - Source: `Dominator`
    - Suggest: `Dominátor`
    - The en-US value is "Dominator" (the id merely still says .label); the dominator-tree column shows the dominating object, and "Označení" duplicates the generic "label" wording used elsewhere.
- `certmgr.certificateTransparency.label` — `devtools/client/netmonitor.properties` — Certificate Transparency rendered as physical "transparency"
    - Current: `Průhlednost:`
    - Source: `Transparency:`
    - Suggest: `Transparentnost certifikátů:`
    - The label heads the Certificate Transparency (SCT) fields in the Security tab; "Průhlednost" means see-through transparency and is also the term used for colour opacity elsewhere in DevTools, so it misidentifies the field.
- `responsive.changeDevicePixelRatio` — `devtools/client/responsive.properties` — "of the viewport" turned into "or the viewport"
    - Current: `Změní poměr pixelů zařízení nebo výřez`
    - Source: `Change device pixel ratio of the viewport`
    - Suggest: `Změní poměr pixelů zařízení pro výřez`
    - en-US is "Change device pixel ratio of the viewport"; the Czech claims the control also changes the viewport itself, which it does not.
- `storage-table-type-cache-hint` — `devtools/client/storage.ftl` — "delete the cache storage entries" translated as "edit"
    - Current: `Pro zobrazení a úpravu položek úložiště mezipaměti vyberte úložiště.`
    - Source: `View and delete the cache storage entries by selecting a storage. <a data-l10n-name="learn-more-link">Learn more</a>`
    - Suggest: `Pro zobrazení a smazání položek úložiště mezipaměti vyberte úložiště.`
    - en-US is "View and delete the cache storage entries…"; cache entries can only be deleted, not edited.
- _…and 51 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `appearance-browser-icon-pride` — `browser/browser/preferences/browserIcon.ftl` — The Pride icon name is translated as the common noun "Hrdost".
    - Current: `Hrdost`
    - Source: `label: Pride`
    - Suggest: `Pride`
    - "Pride" here names the LGBTQ+ Pride icon variant, used untranslated in Czech; "Hrdost" reads as the abstract quality and loses the reference, unlike the neighbouring untranslated names Retro 2004, Kit, Momo.
- `experimental-features-cookie-samesite-none-requires-secure2-description` — `toolkit/toolkit/featuregates/features.ftl` — Dependency names the wrong SameSite value: en-US says the feature requires "Cookies: SameSite=Lax by default", Czech says SameSite=None.
    - Current: `Tato funkce vyžaduje „Cookies: SameSite=None by default“.`
    - Source: `Cookies with “SameSite=None” attribute require the secure attribute. This feature requires “Cookies: SameSite=Lax by default”.`
    - Suggest: `Tato funkce vyžaduje „Cookies: SameSite=Lax by default“.`
    - The developer comment says do not translate 'SameSite', 'Lax' and 'None'; the keyword was also swapped, so the string describes a non-existent dependency. (The missing space after 'secure.' in the same string should be fixed too.)
- `btp-warning-tracker-purged` — `toolkit/toolkit/global/antiTracking.ftl` — "bounce tracker" translated as "sledovač" despite the do-not-translate note.
    - Current: `protože byl rozpoznán jako sledovač`
    - Source: `The state of “{ $siteHost }” was recently purged because it was detected as a bounce tracker.`
    - Suggest: `protože byl rozpoznán jako bounce tracker`
    - The developer comment says do not translate "bounce tracker", and the sibling string btp-warning-tracker-classified keeps the English term, so the two messages use different names for the same classification.
- `ssl-error-missing-extended-master-secret` — `toolkit/toolkit/neterror/nsserrors.ftl` — English word left in place and the extension name is truncated.
    - Current: `bez correct extended_master_secre rozšíření`
    - Source: `The peer tried to resume without a correct extended_master_secret extension.`
    - Suggest: `bez správného rozšíření extended_master_secret`
    - en-US: "without a correct extended_master_secret extension"; "correct" is untranslated and the identifier lost its final letter.
- `pdfjs-digital-signature-properties-certificate-untrusted-self-signed` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "Self-signed" left in English although the tree translates the term elsewhere.
    - Current: `Certifikát: Self-signed ({ $issuer })`
    - Source: `Certificate: Self-signed ({ $issuer })`
    - Suggest: `Certifikát: Podepsán sám sebou ({ $issuer })`
    - certError.ftl renders self-signed as "podepsán sám sebou"; the surrounding rows in this same panel are all translated.

### C. Grammar, agreement & spelling

- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — The quoted option prefix does not match the labels of the settings it refers to.
    - Current: `zrušte zaškrtnutí u možnosti „Učit se od…“`
    - Source: `Existing memories will be deleted. If you don’t want any new memories created, uncheck the options to “Learn from…” in { -smart-window-brand-name } settings.`
    - Suggest: `zrušte zaškrtnutí u možností „Učit se z…“`
    - The developer comment says the quoted text refers to ai-window-learn-from-chat-activity and ai-window-learn-from-browsing-activity, which are localized as “Učit se z chatu…” and “Učit se z prohlížení…”, so users will not find an option starting with “Učit se od”.
- `default-browser-prompt-button-primary-set` — `browser/browser/defaultBrowserNotification.ftl` — “primary browser” rendered as “výchozí prohlížeč” here but as “hlavní prohlížeč” in the rest of the same prompt.
    - Current: `Nastavit jako výchozí prohlížeč`
    - Source: `Set as primary browser`
    - Suggest: `Nastavit jako hlavní prohlížeč`
    - en-US “Set as primary browser”; the prompt title and default-browser-prompt-button-primary-pin use “hlavní prohlížeč”, while default-browser-prompt-button-primary-alt (“Set as default browser”) already uses “výchozí prohlížeč”, so the two distinct actions become identical.
- `colorways-cfr-primarybutton` — `browser/browser/newtab/asrouter.ftl` — "baletu" (ballet) instead of "paletu" (palette).
    - Current: `Zvolit baletu barev`
    - Source: `(value): Choose colorway accesskey: C`
    - Suggest: `Zvolit paletu barev`
    - Typo; the neighbouring colorways-cfr-header-* strings all use "Paleta barev".
- `home-custom-homepage-replace-with-prompt` — `browser/browser/newtab/newtab.ftl` — "Nahradit s" is a calque of "Replace with"; Czech "nahradit" takes the instrumental without "s".
    - Current: `Nahradit s`
    - Source: `label: Replace with`
    - Suggest: `Nahradit čím:`
    - "Nahradit s" is ungrammatical in Czech; the verb requires a bare instrumental object.
- `newtab-clock-widget-menu-switch-to-24h` — `browser/browser/newtab/newtab.ftl` — "24-hodinový" is hyphenated, unlike "12hodinový" in the adjacent string.
    - Current: `Přepnout na 24-hodinový formát`
    - Source: `Switch to 24-hour format`
    - Suggest: `Přepnout na 24hodinový formát`
    - Czech joins a numeral to the adjective without a hyphen; newtab-clock-widget-menu-switch-to-12h correctly writes "12hodinový".
- `newtab-label-sponsored` — `browser/browser/newtab/newtab.ftl` — "sponzrováno" is misspelled.
    - Current: `{ $sponsorOrSource } · sponzrováno`
    - Source: `{ $sponsorOrSource } · Sponsored`
    - Suggest: `{ $sponsorOrSource } · Sponzorováno`
    - Missing "o"; the parallel labels newtab-topsite-sponsored and newtab-label-sponsored-fixed use "Sponzorováno".
- `newtab-pocket-new-topics-title` — `browser/browser/newtab/newtab.ftl` — Adjective does not agree with the neuter plural noun "témata".
    - Current: `Podívejte se na oblíbené témata`
    - Source: `Want even more stories? See these popular topics from { -pocket-brand-name }`
    - Suggest: `Podívejte se na oblíbená témata`
    - "téma" is neuter; the accusative plural requires "oblíbená témata".
- `newtab-sports-widget-message-wallpapers-semifinals-title` — `browser/browser/newtab/newtab.ftl` — "semi-finále" is written with a hyphen.
    - Current: `Získejte novou tapetu pro semi-finále`
    - Source: `Get a new wallpaper for the semi-finals`
    - Suggest: `Získejte novou tapetu pro semifinále`
    - Czech spells it "semifinále" as one word; the same file already uses "Semifinále" in newtab-sports-widget-semi-finals.
- `newtab-wallpaper-suspension-bridge` — `browser/browser/newtab/newtab.ftl` — The wallpaper description is grammatically broken and does not parse as Czech.
    - Current: `Šedivé fotografování celé visuté můstky během dne`
    - Source: `Grey full-suspension bridge photography during daytime`
    - Suggest: `Fotografie šedého visutého mostu za denního světla`
    - en-US: "Grey full-suspension bridge photography during daytime". "celé visuté můstky" has no agreement with anything in the sentence and "můstky" (small footbridges, plural) does not match "bridge".
- `newtab-widget-section-minimize` — `browser/browser/newtab/newtab.ftl` — "wigety" is a typo for "widgety".
    - Current: `Minimalizovat wigety`
    - Source: `aria-label: Collapse all widgets to compact size title: Minimize widgets`
    - Suggest: `Minimalizovat widgety`
    - Every other widget string in the file spells it "widgety".
- `mr2022-onboarding-import-header` — `browser/browser/newtab/onboarding.ftl` — "nastaveni" is missing its accent.
    - Current: `Bleskové nastaveni`
    - Source: `Lightning-fast setup`
    - Suggest: `Bleskové nastavení`
    - Czech spelling requires "nastavení".
- `onboarding-infrequent-import-title` — `browser/browser/newtab/onboarding.ftl` — "Buďte se" is ungrammatical — a stray reflexive pronoun.
    - Current: `Buďte se jako doma`
    - Source: `Make yourself at home`
    - Suggest: `Buďte jako doma`
    - The verb "být" is not reflexive; either "Buďte jako doma" or "Ciťte se jako doma" is correct.
- `onboarding-personalization-subtitle` — `browser/browser/newtab/onboarding.ftl` — "odporučíme" is not a Czech word; should be "doporučíme".
    - Current: `my vám odporučíme funkce a rozšíření`
    - Source: `Answer a few questions and we’ll recommend features and extensions to enhance your use of { -brand-short-name }.`
    - Suggest: `my vám doporučíme funkce a rozšíření`
    - Spelling error in both the with-cases and no-cases variants of the string.
- `onboarding-sign-up-secondary-button` — `browser/browser/newtab/onboarding.ftl` — "pohlížet" instead of "prohlížet".
    - Current: `Začít pohlížet`
    - Source: `Start browsing`
    - Suggest: `Začít prohlížet`
    - Typo; every other "Start browsing" button in the file is "Začít prohlížet".
- `fonts-langgroup-canadian` — `browser/browser/preferences/fonts.ftl` — "Unified Canadian Syllabary" is translated as "Kannadština" (Kannada), the same label already used for fonts-langgroup-kannada.
    - Current: `Kannadština`
    - Source: `label: Unified Canadian Syllabary`
    - Suggest: `Sjednocené kanadské slabičné písmo`
    - The Canadian Aboriginal syllabics script is named as the Kannada language; the font-group list then shows two identical "Kannadština" entries, so the user cannot pick fonts for either script correctly.
- `fonts-langgroup-odia` — `browser/browser/preferences/fonts.ftl` — "Odia" is rendered as "Udijština", which names the Udi language of the Caucasus.
    - Current: `Udijština`
    - Source: `label: Odia`
    - Suggest: `Urijština`
    - The Indic language Odia/Oriya is "urijština" (or "odijština") in Czech; "udijština" is a different, unrelated language.
- `preonboarding-terms-of-use-header-button-title-b-v2` — `browser/browser/preonboarding.ftl` — "Terms of Use" appears as "Podmínky použití" here but as "Podmínky používání" everywhere else on the same screen.
    - Current: `Podmínky použití`
    - Source: `Terms of Use`
    - Suggest: `Podmínky používání`
    - preonboarding-subtitle, -manage-and-read-header and -terms-of-use-header-button-title all use "Podmínky používání" for the same legal document.
- `paw-print-avatar-tooltip` — `browser/browser/profiles.ftl` — "potisk" (printed pattern on fabric) used for paw print instead of "otisk" as elsewhere.
    - Current: `Použít avatar s potiskem tlapky`
    - Source: `tooltiptext: Apply paw print avatar`
    - Suggest: `Použít avatar otisku tlapky`
    - paw-print-avatar and paw-print-avatar-alt in the same file use "Otisk tlapky".
- `sidebar-history-sort-option-date-and-site` — `browser/browser/sidebar.ftl` — "site" rendered as "název" (name) although the adjacent sort option renders the same term as "Server".
    - Current: `Datum a název`
    - Source: `label: Date and site`
    - Suggest: `Datum a server`
    - sidebar-history-sort-option-site = "Server" for en-US "Site" in the same dropdown; "název" refers to something else.
- `autofillReauthCheckboxMac` — `browser/extensions/formautofill/formautofill.properties` — Apple OS brand name miscapitalized as "MacOS".
    - Current: `ověření od systému MacOS`
    - Source: `Require macOS authentication to autofill, view, or edit stored credit cards.`
    - Suggest: `ověření od systému macOS`
    - The en-US source and Apple’s branding use "macOS"; "MacOS" is not a correct form of the product name.
- `WARN_DISK_SPACE_QUIT2` — `browser/installer/nsisstrings.properties` — Wrong case after "na": "na instalace" should be "na instalaci".
    - Current: `dostatek úložného prostoru na instalace aplikace $BrandShortName`
    - Source: `It looks like you don’t have enough storage on your device to install $BrandShortName.`
    - Suggest: `dostatek úložného prostoru na instalaci aplikace $BrandShortName`
    - "na" with this meaning takes the accusative singular "instalaci".
- `CopyDetails` — `browser/installer/override.properties` — Wrong case: "podrobnosti" should be genitive plural "podrobností".
    - Current: `Zkopírování podrobnosti do schránky`
    - Source: `Copy Details To Clipboard`
    - Suggest: `Zkopírování podrobností do schránky`
    - The verbal noun "zkopírování" governs the genitive.
- `CSSContainerRuleSingleConditionWarning` — `dom/chrome/dom/dom.properties` — Do-not-translate API name CSSContainerRule.conditions rendered as CSSContainerRule.currents.
    - Current: `CSSContainerRule.currents`
    - Source: `CSSContainerRule.containerName and CSSContainerRule.containerQuery don’t support multiple conditions. Use CSSContainerRule.conditions instead.`
    - Suggest: `CSSContainerRule.conditions`
    - The developer comment says not to translate CSSContainerRule.conditions; the localized identifier does not exist in the API.
- `DrawWindowCanvasRenderingContext2DWarning` — `dom/chrome/dom/dom.properties` — Interface name CanvasRenderingContext2D split by a space.
    - Current: `CanvasRenderingContext 2D`
    - Source: `Use of drawWindow method from CanvasRenderingContext2D is deprecated. Use tabs.captureTab extensions API instead https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/tabs/captureTab`
    - Suggest: `CanvasRenderingContext2D`
    - Developer comment says do not translate CanvasRenderingContext2D; the space breaks the identifier (the first occurrence in the same file is correct).
- `EditContextCharacterBoundsWarning` — `dom/chrome/dom/dom.properties` — Do-not-translate event name characterboundsupdate is mangled.
    - Current: `charakteruboundsupdate`
    - Source: `EditContext.updateCharacterBounds() was not called synchronously in characterboundsupdate event listener. IME interface may move around unexpectedly for some users. More information: https://developer.mozilla.org/docs/W…`
    - Suggest: `characterboundsupdate`
    - The developer comment explicitly says not to translate “characterboundsupdate”; the partial Czech spelling breaks the identifier.
- `IDBIndexMozGetAllKeysWarning` — `dom/chrome/dom/dom.properties` — API name IDBIndex.getAllKeys() misspelled with a doubled i.
    - Current: `IDBIindex.getAllKeys()`
    - Source: `IDBIndex.mozGetAllKeys() is deprecated. Use IDBIndex.getAllKeys() instead.`
    - Suggest: `IDBIndex.getAllKeys()`
    - Developer comment says do not translate “IDBIndex.getAllKeys()”.
- `IDBIndexMozGetAllWarning` — `dom/chrome/dom/dom.properties` — API name IDBIndex.getAll() misspelled with a doubled i.
    - Current: `IDBIindex.getAll()`
    - Source: `IDBIndex.mozGetAll() is deprecated. Use IDBIndex.getAll() instead.`
    - Suggest: `IDBIndex.getAll()`
    - Developer comment says do not translate “IDBIndex.getAll()”; the typo makes the suggested replacement invalid.
- `PushMessageBadEncodingHeader` — `dom/chrome/dom/dom.properties` — HTTP header name Content-Encoding written as Content-Encryption.
    - Current: `Hlavička ‘Content-Encryption’ je povolena pouze s ‘aesgcm‘`
    - Source: `The ServiceWorker for scope ‘%1$S’ failed to decrypt a push message. The ‘Content-Encoding‘ header must be ‘aesgcm‘. ‘aesgcm128‘ is allowed, but deprecated and will soon be removed. See https://tools.ietf.org/html/draft…`
    - Suggest: `Hlavička ‘Content-Encoding‘ musí být ‘aesgcm‘`
    - en-US and the developer comment name the “Content-Encoding” header; “Content-Encryption” is a non-existent header.
- `crashreporter-submit-failure` — `toolkit/crashreporter/crashreporter.ftl` — Spelling: "Pří" instead of "Při".
    - Current: `Pří odesílání hlášení o pádu nastala chyba.`
    - Source: `There was a problem submitting your report.`
    - Suggest: `Při odesílání hlášení o pádu nastala chyba.`
    - "Pří" is not a Czech word; the preposition is "při".
- `private-browsing-description2` — `toolkit/toolkit/about/aboutAddons.ftl` — Comma incorrectly separates the subject from its predicate
    - Current: `Žádné nově nainstalované rozšíření, nebude ve výchozím nastavení v anonymních oknech fungovat`
    - Source: `{ -brand-short-name } is changing how extensions work in private browsing. Any new extensions you add to { -brand-short-name } won’t run by default in Private Windows. Unless you allow it in settings, the extension won’…`
    - Suggest: `Žádné nově nainstalované rozšíření nebude ve výchozím nastavení v anonymních oknech fungovat`
    - Czech punctuation does not allow a comma between the subject phrase and the verb here; it is a plain typo.
- `about-reader-estimated-read-time` — `toolkit/toolkit/about/aboutReader.ftl` — Singular plural variant uses the genitive-plural form "minut"
    - Current: `[one] { $range } minut`
    - Source: `{$rangePlural ->} [one] { $range } minute [other] { $range } minutes`
    - Suggest: `[one] { $range } minuta`
    - The [one] category is selected for ranges like "~1", where Czech requires the nominative singular "1 minuta"; "1 minut" is ungrammatical. The [few] and [other] variants are correct.
- `rights-locationawarebrowsing-term-2` — `toolkit/toolkit/about/aboutRights.ftl` — Ungrammatical instruction "Zadejte hledat"
    - Current: `a potvrďte varování. Zadejte hledat „geo.enabled“`
    - Source: `Type geo.enabled`
    - Suggest: `a potvrďte varování. Vyhledejte „geo.enabled“`
    - "Zadejte hledat" chains two verbs with no valid construction in Czech; the step is meant to say "search for geo.enabled".
- `experimental-features-devtools-serviceworker-debugger-support-description` — `toolkit/toolkit/featuregates/features.ftl` — Spelling: "laděni" instead of "ladění".
    - Current: `v panelu laděni`
    - Source: `Enables experimental support for Service Workers in the Debugger panel. This feature may slow the Developer Tools down and increase memory consumption.`
    - Suggest: `v panelu ladění`
    - Missing length mark; "laděni" is not the correct form here.
- `webext-perms-update-list-intro-with-data-collection` — `toolkit/toolkit/global/extensions.ftl` — Broken parallel structure: an infinitive is coordinated with a bare accusative noun.
    - Current: `Zrušit pro zachování aktuální verze a nastavení, nebo aktualizaci pro získání nové verze a schválení změn.`
    - Source: `Cancel to keep your current version and settings, or update to get the new version and approve the changes.`
    - Suggest: `Zrušte pro zachování aktuální verze a nastavení, nebo aktualizujte pro získání nové verze a schválení změn.`
    - en-US uses two parallel imperatives ("Cancel to keep…, or update to get…"); "nebo aktualizaci" leaves the second clause without a verb.
- `moz-box-item-reorder-handle` — `toolkit/toolkit/global/mozBoxBase.ftl` — Spelling: "Šipka dolu" instead of "Šipka dolů".
    - Current: `Ctrl+Shift+Šipka dolu`
    - Source: `aria-label: Reorder item using Ctrl+Shift+ArrowUp or Ctrl+Shift+ArrowDown`
    - Suggest: `Ctrl+Shift+Šipka dolů`
    - The adverb is "dolů"; "dolu" is the genitive of "důl" (mine). The same error appears in moz-box-item-reorder-handle-named.
- `refresh-profile-dialog-title` — `toolkit/toolkit/global/resetProfile.ftl` — Duplicated word: "výchozí nastavení nastavení".
    - Current: `výchozí nastavení nastavení`
    - Source: `Refresh { -brand-short-name } to its default settings?`
    - Suggest: `výchozí nastavení`
    - The word "nastavení" is repeated in both variants of the dialog title.
- `sec-error-revoked-certificate-ocsp` — `toolkit/toolkit/neterror/nsserrors.ftl` — Subject is in the accusative: "Respondenta OCSP vydavatele nahlásil".
    - Current: `Respondenta OCSP vydavatele nahlásil`
    - Source: `Issuer’s OCSP responder reports certificate is revoked.`
    - Suggest: `Respondent OCSP vydavatele nahlásil`
    - The subject of "nahlásil" must be nominative ("respondent").
- `ssl-error-unsupported-hash-algorithm` — `toolkit/toolkit/neterror/nsserrors.ftl` — Agreement error ("neplatná … algoritmus") plus "unsupported" rendered as "invalid".
    - Current: `Partner TLS použil neplatná hashovací algoritmus.`
    - Source: `Unsupported hash algorithm used by TLS peer.`
    - Suggest: `Partner TLS použil nepodporovaný hashovací algoritmus.`
    - en-US: "Unsupported hash algorithm used by TLS peer." "algoritmus" is masculine, so "neplatná" is ungrammatical, and unsupported ≠ invalid.
- `primary-password-admin` — `toolkit/toolkit/preferences/preferences.ftl` — Ungrammatical case after the preposition "před": "před ukládání hesel".
    - Current: `před ukládání hesel`
    - Source: `Your administrator requires that you have a Primary Password set in order to save logins and passwords.`
    - Suggest: `před ukládáním přihlašovacích údajů a hesel`
    - "před" requires the instrumental ("ukládáním"); the accusative form is incorrect.
- `webauthn-pin-required-prompt` — `toolkit/toolkit/webauthnDialog.ftl` — Typo: "Zajdete" instead of "Zadejte" in the PIN prompt.
    - Current: `Zajdete prosím PIN pro vaše zařízení.`
    - Source: `Please enter the PIN for your device.`
    - Suggest: `Zadejte prosím PIN pro vaše zařízení.`
    - "Zajdete" is not a valid imperative here; the intended verb is "zadejte" (enter).

### D. Terminology, register & consistency

- `about-logins-confirm-remove-all-dialog-message2` — `browser/browser/aboutLogins.ftl` — Wrong case after the preposition “v”: “v aplikace” instead of “v aplikaci”.
    - Current: `Tímto odstraníte hesla uložená v aplikace { -brand-short-name }`
    - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } and any breach alerts. You cannot undo this action. [other] This will remove the passwords saved to { -brand-short-name } and any breach alert…`
    - Suggest: `Tímto odstraníte hesla uložená v aplikaci { -brand-short-name }`
    - “v” requires the locative “aplikaci”; every other no-cases variant in this file uses “v aplikaci”.
- `about-logins-import-dialog-items-modified2` — `browser/browser/aboutLogins.ftl` — Adjective does not agree with neuter plural “hesla” in the [few]/[many] branches.
    - Current: `[few] <span>Aktualizované hesla:</span>`
    - Source: `{$count ->} [other] <span>Existing entries updated:</span> <span data-l10n-name="count">{ $count }</span>`
    - Suggest: `[few] <span>Aktualizovaná hesla:</span>`
    - “heslo” is neuter; the nominative plural adjective is “aktualizovaná”. The [many] branch additionally needs a genitive phrasing (“Aktualizovaných hesel”).
- `about-logins-import-report-added2` — `browser/browser/aboutLogins.ftl` — Adjective agreement error in the [few] branch: “nové přidané hesla”.
    - Current: `[few] <div data-l10n-name="count">{ $count }</div><div data-l10n-name="details">nové přidané hesla</div>`
    - Source: `{$count ->} [other] <div data-l10n-name="count">{ $count }</div> <div data-l10n-name="details">New passwords added</div>`
    - Suggest: `[few] <div data-l10n-name="count">{ $count }</div><div data-l10n-name="details">nová přidaná hesla</div>`
    - Neuter plural “hesla” requires “nová přidaná”.
- `about-logins-import-report-modified2` — `browser/browser/aboutLogins.ftl` — Number mismatch in the [few] branch: plural adjective with singular noun.
    - Current: `[few] <div data-l10n-name="count">{ $count }</div><div data-l10n-name="details">aktualizované položka</div>`
    - Source: `{$count ->} [other] <div data-l10n-name="count">{ $count }</div> <div data-l10n-name="details">Existing entries updated</div>`
    - Suggest: `[few] <div data-l10n-name="count">{ $count }</div><div data-l10n-name="details">aktualizované položky</div>`
    - For counts 2–4 the noun must be nominative plural “položky”; the singular “položka” is left over from the [one] branch.
- `about-private-browsing-hide-activity-1` — `browser/browser/aboutPrivateBrowsing.ftl` — Wrong case after “o”: instrumental “prohlížením” instead of locative “prohlížení”.
    - Current: `Skryjte informace o svém prohlížením s { -mozilla-vpn-brand-name(case: "ins") }.`
    - Source: `Hide browsing activity and location with { -mozilla-vpn-brand-name }. One click creates a secure connection, even on public Wi-Fi.`
    - Suggest: `Skryjte informace o svém prohlížení s { -mozilla-vpn-brand-name(case: "ins") }.`
    - The preposition “o” with the meaning “about” governs the locative case.
- `addon-confirm-install-some-unsigned-message` — `browser/browser/addonNotifications.ftl` — Typo “nověřený” instead of “neověřený” (unverified) in the [one] branch.
    - Current: `nainstalovat nověřený doplněk`
    - Source: `{$addonCount ->} [other] Caution: This site would like to install { $addonCount } add-ons in { -brand-short-name }, some of which are unverified. Proceed at your own risk.`
    - Suggest: `nainstalovat neověřený doplněk`
    - Both branches of the [one] variant misspell the word; the same term is spelled “neověřený” everywhere else in the file.
- `aiwindow-memories-callout-description` — `browser/browser/aiWindowContent.ftl` — Past-participle agreement: inanimate feminine plural requires “pomohly”, not “pomohli”.
    - Current: `Vzpomínky pomohli přizpůsobit tuto odpověď.`
    - Source: `Memories helped personalize this response.`
    - Suggest: `Vzpomínky pomohly přizpůsobit tuto odpověď.`
    - “vzpomínky” is feminine inanimate plural, so the participle ends in -y.
- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — `backup-file-moz-browser-restore-step-2-1` quotes “Obnovit data” but the string it names, `restore-from-backup-header`, reads “Obnovení vašich dat”
    - Current: `Klepněte na “Obnovit data” a vyberte tento soubor`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Obnovení vašich dat`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — `backup-file-other-browser-restore-step-3-1` quotes “Obnovit data” but the string it names, `restore-from-backup-header`, reads “Obnovení vašich dat”
    - Current: `Klepněte na “Obnovit data” a vyberte tento soubor`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Obnovení vašich dat`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `identity-etsi` — `browser/browser/browser.ftl` — Slovak abbreviation “EÚ” used instead of Czech “EU”.
    - Current: `Klasifikovaný podle nařízení (EÚ) 2024/1183.`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Kvalifikovaný podle nařízení (EU) 2024/1183.`
    - Czech spells the European Union as EU; EÚ is Slovak. (“Qualified” here also refers to a qualified certificate, i.e. “kvalifikovaný”, not “klasifikovaný”.)
- `trustpanel-list-label-tracking-cookies` — `browser/browser/browser.ftl` — Singular branch reads “třetí stran”, mixing singular and plural.
    - Current: `[one] { $count } sledovací cookie třetí stran`
    - Source: `{$count ->} [one] { $count } Cross-site tracking cookie [other] { $count } Cross-site tracking cookies`
    - Suggest: `[one] { $count } sledovací cookie třetí strany`
    - Later strings in the same panel (trustpanel-tracking-cookies-blocking-tab-header) correctly use “sledovací cookie třetí strany”.
- `requested-crash-reports-message-new` — `browser/browser/contentCrash.ftl` — The [few]/[many] branches keep the singular “toto hlášení bude ignorováno”.
    - Current: `[few] Máte { $reportCount } neodeslaná hlášení o pádech týkající se pádu, který řešíme. Jejich odeslání nám pomůže { -brand-product-name } zlepšit. Zavřením tohoto oznámení bude toto hlášení ignorováno.`
    - Source: `{$reportCount ->} [one] You have an unsent crash report related to crashes being investigated, sending it will help us improve { -brand-product-name }. Closing this notification will ignore this report. [other] You have…`
    - Suggest: `[few] Máte { $reportCount } neodeslaná hlášení o pádech týkající se pádu, který řešíme. Jejich odeslání nám pomůže { -brand-product-name } zlepšit. Zavřením tohoto oznámení budou tato hlášení ignorována.`
    - en-US plural: “Closing this notification will ignore these reports.” The parallel string requested-crash-reports-message handles the plural branches correctly.
- `contextual-manager-passwords-import-success-message-2` — `browser/browser/contextual-manager.ftl` — Typo “aktualizováné” instead of “aktualizované”.
    - Current: `aktualizováné: { $modified }`
    - Source: `New: { $added }, Updated: { $modified }, Duplicates: { $no_change }, Errors: { $error }`
    - Suggest: `aktualizované: { $modified }`
    - The v1 string contextual-manager-passwords-import-success-message spells it correctly as “aktualizované”.
- `pin-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — Pronoun does not agree with masculine “panel”.
    - Current: `Chcete-li připnout libovolný panel, přetáhněte ji na začátek lišty panelů.`
    - Source: `To pin any tab, drag it to the start of the tab strip. Or right-click and choose Pin Tab.`
    - Suggest: `Chcete-li připnout libovolný panel, přetáhněte jej na začátek lišty panelů.`
    - “panel” is masculine inanimate, so the accusative pronoun is “jej/ho”, not the feminine “ji”.
- `windows-10-eos-sync-urgency-title-1` — `browser/browser/featureCallout.ftl` — Misspelled imperative “Nepřijďe” and a trailing comma instead of a period.
    - Current: `Nepřijďe při přechodu na Windows 11 o vše, co jste si uložili,`
    - Source: `Don’t lose everything you’ve saved when you move to Windows 11.`
    - Suggest: `Nepřijďte při přechodu na Windows 11 o vše, co jste si uložili.`
    - The 2nd person plural imperative is “nepřijďte”; “nepřijďe” is not a Czech word form, and the sentence ends with a stray comma.
- `firefoxview-dont-remember-history-empty-description-2` — `browser/browser/firefoxView.ftl` — Gender agreement: “Tuto nastavení” instead of “Toto nastavení”.
    - Current: `Tuto nastavení můžete kdykoli změnit`
    - Source: `{ -brand-short-name } isn’t saving your history right now. Change that any time in <a data-l10n-name="history-settings-url-two">settings</a>.`
    - Suggest: `Toto nastavení můžete kdykoli změnit`
    - “nastavení” is neuter, so the demonstrative must be “toto”.
- `identity-credential-policy-description` — `browser/browser/identityCredentialNotification.ftl` — “podléhá” takes the dative, but the objects are in the instrumental case.
    - Current: `podléhá jejich <label data-l10n-name="privacy-url">Zásadami ochrany osobních údajů</label> a <label data-l10n-name="tos-url">Podmínkami poskytování služby</label>`
    - Source: `Logging in to { $host } with a { $provider } account is subject to their <label data-l10n-name="privacy-url">Privacy Policy</label> and <label data-l10n-name="tos-url">Terms of Service</label>.`
    - Suggest: `podléhá jejich <label data-l10n-name="privacy-url">Zásadám ochrany osobních údajů</label> a <label data-l10n-name="tos-url">Podmínkám poskytování služby</label>`
    - “podléhat něčemu” requires the dative (Zásadám, Podmínkám); the current forms are instrumental.
- `ipp-activator-breakage-sign-in-warning` — `browser/browser/ipProtection.ftl` — Gender agreement error: “Tento stránka” instead of “Tato stránka”.
    - Current: `<strong>Tento stránka nemusí fungovat s VPN.</strong>`
    - Source: `<strong>This website may not work with a VPN.</strong> Try signing in or turning VPN off while you use this website.`
    - Suggest: `<strong>Tato stránka nemusí fungovat s VPN.</strong>`
    - “stránka” is feminine; the parallel string ipp-activator-breakage-turn-off-warning correctly uses “Tato stránka”.
- `ipprotection-feature-introduction-description-summer-promo` — `browser/browser/ipProtection.ftl` — Case mismatch: “vestavěnou služby VPN” (accusative adjective + genitive noun).
    - Current: `Využijte vestavěnou služby VPN`
    - Source: `Go farther with { -brand-product-name }’s built-in VPN: more locations, unlimited bandwidth. Now until August 31.`
    - Suggest: `Využijte vestavěnou službu VPN`
    - “využijte” governs the accusative; the adjective and noun must agree (“vestavěnou službu”). Both branches of the message contain the error.
- `migration-no-permissions-instructions` — `browser/browser/migrationWizard.ftl` — Fallback variant uses nominative "aplikace" where the dative "aplikaci" is required.
    - Current: `udělte aplikace { -brand-short-name } přístup`
    - Source: `To continue importing data from another browser, grant { -brand-short-name } access to its profile folder.`
    - Suggest: `udělte aplikaci { -brand-short-name } přístup`
    - "udělit" requires the dative object; all parallel no-cases fallbacks in the tree write "aplikaci".
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Synchronizovat s mobilním telefonem” but the string it names, `sync-to-mobile-button-label`, reads “Synchronizace s mobilem”
    - Current: `{$sel_1 ->} [with-cases] Naskenujte QR kód a stáhněte si { -brand-product-name } pro mobily. Po instalaci vyberte možnost "Synchronizovat s mobilním telefonem" a získejte přístup ke svým heslům, záložkám a dalším údajům…`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Synchronizace s mobilem`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `security-visits-number` — `browser/browser/pageInfo.ftl` — "krát" written as a separate word after a numeral; Czech orthography joins it to the number.
    - Current: `Ano, { $visits } krát`
    - Source: `{$visits ->} [0] No [one] Yes, once [other] Yes, { $visits } times`
    - Suggest: `Ano, { $visits }krát`
    - Numeral + krát is written as one word in Czech (e.g. "5krát").
- `appearance-browser-icon-pin-button` — `browser/browser/preferences/browserIcon.ftl` — The Windows taskbar is called "lišta" here but "hlavní panel" in the same feature.
    - Current: `Připnout na lištu`
    - Source: `label: Pin to taskbar`
    - Suggest: `Připnout na hlavní panel`
    - appearance-browser-icon-entry-group uses the official Windows term "hlavní panel" for taskbar; "lišta" in the button on the same page names a different UI element.
- `addressbar-locbar-suggest-all-option-2` — `browser/browser/preferences/preferences.ftl` — Case/agreement error: "z webu souvisejícím".
    - Current: `Získat návrhy z webu souvisejícím s vaším vyhledáváním.`
    - Source: `description: Get suggestions from the web related to your search. label: Suggestions from { -brand-short-name }`
    - Suggest: `Získat návrhy z webu související s vaším vyhledáváním.`
    - The participle is meant to modify "návrhy" (accusative plural) but is inflected as instrumental singular, agreeing with nothing in the sentence. Same text in addressbar-locbar-suggest-nonsponsored-desc.
- `certs-devices2` — `browser/browser/preferences/preferences.ftl` — "bezpečností" should be the adjective "bezpečnostní".
    - Current: `Spravovat bezpečností zařízení`
    - Source: `accesskey: D label: Manage security devices`
    - Suggest: `Spravovat bezpečnostní zařízení`
    - "bezpečností" is the instrumental of the noun "bezpečnost"; the phrase needs the adjective, as used correctly in certs-devices ("Bezpečnostní zařízení…").
- `content-blocking-cross-site-cookies-in-all-windows2` — `browser/browser/preferences/preferences.ftl` — "Cross-site cookies" rendered as "Cookies třetích stran" (third-party cookies) while neighbouring items keep "cross-site cookies".
    - Current: `Cookies třetích stran ve všech oknech`
    - Source: `Cross-site cookies in all windows`
    - Suggest: `Cross-site cookies ve všech oknech`
    - In the same blocked-items list content-blocking-all-cross-site-cookies uses "cross-site cookies"; third-party and cross-site are distinct concepts, so one of the two renderings is wrong on the same surface.
- `home-custom-homepage-header` — `browser/browser/preferences/preferences.ftl` — Heading uses the accusative "Vlastní domovskou stránku" instead of the nominative.
    - Current: `Vlastní domovskou stránku`
    - Source: `Custom Homepage`
    - Suggest: `Vlastní domovská stránka`
    - "Custom Homepage" is a page title, which in Czech takes the nominative; the accusative reads as a sentence fragment. The same string is used for home-custom-homepage-subpage.
- `home-custom-homepage-replace-with-prompt` — `browser/browser/preferences/preferences.ftl` — "Nahradit s" uses the wrong preposition/case for "Replace with".
    - Current: `Nahradit s`
    - Source: `label: Replace with`
    - Suggest: `Nahradit:`
    - In Czech "nahradit" takes a bare instrumental (nahradit něčím); "nahradit s" is a calque from English and is ungrammatical before the buttons that follow.
- `home-homepage-new-tabs` — `browser/browser/preferences/preferences.ftl` — Label "V novém panelu" (prepositional phrase, singular) does not match its sibling "Nová okna".
    - Current: `V novém panelu`
    - Source: `label: New tabs`
    - Suggest: `Nové panely`
    - home-homepage-new-windows/new-tabs are a parallel pair of field labels ("New windows"/"New tabs"); one is a plural noun phrase and the other a locative phrase copied from the dropdown label home-newtabs-mode-label.
- `preferences-doh-enabled-detailed-desc-2` — `browser/browser/preferences/preferences.ftl` — Verb form "se použijte" (imperative) instead of "se použije" (3rd person singular).
    - Current: `Výchozí překladač DNS se použijte jen v případě problému se zabezpečeným DNS`
    - Source: `Only use your default DNS resolver if there is a problem with secure DNS`
    - Suggest: `Výchozí překladač DNS se použije jen v případě problému se zabezpečeným DNS`
    - The subject is "překladač DNS", so the verb must be 3rd person singular; the imperative makes the descriptive bullet ungrammatical.
- `search-suggestions-cant-show-2` — `browser/browser/preferences/preferences.ftl` — Missing preposition "v" before "adresním řádku".
    - Current: `se nebudou adresním řádku zobrazovat`
    - Source: `message: Search suggestions will not be shown in location bar results because you have configured { -brand-short-name } to never remember history.`
    - Suggest: `se nebudou v adresním řádku zobrazovat`
    - "adresním řádku" is locative and requires "v"; without it the sentence is ungrammatical. The same defect is in search-suggestions-cant-show.
- `security-privacy-issue-warning-third-party-cookies` — `browser/browser/preferences/preferences.ftl` — Verb "sledovali" (masculine animate) does not agree with the subject "cookies".
    - Current: `aby vás sledovali na různých webových stránkách`
    - Source: `description: Third-party cookies are used to track you across websites. label: Third-party cookies are enabled`
    - Suggest: `aby vás sledovaly na různých webových stránkách`
    - The subject of the subordinate clause is "cookies třetích stran"; the participle must be inanimate plural "sledovaly".
- `hammer-avatar-tooltip` — `browser/browser/profiles.ftl` — Wrong case: "Použít avataru" instead of "Použít avatar".
    - Current: `Použít avataru s kladívkem`
    - Source: `tooltiptext: Apply hammer avatar`
    - Suggest: `Použít avatar kladiva`
    - "Použít" takes the accusative; all sibling tooltips use "Použít avatar …".
- `monitor-breaches-tooltip` — `browser/browser/protections.ftl` — Missing diacritic: "uniky" instead of "úniky".
    - Current: `Zobrazit uniky dat známé`
    - Source: `title: View known data breaches on { -monitor-brand-short-name }`
    - Suggest: `Zobrazit úniky dat známé`
    - Every other occurrence in the file uses "úniky dat".
- `protections-panel-cookie-banner-blocker-view-turn-off-for-site` — `browser/browser/protectionsPanel.ftl` — Wrong genitive plural "lišť" for "lišta"; correct form is "lišt" (also used in the same panel).
    - Current: `Vypnout blokování lišť cookie`
    - Source: `Turn off Cookie Banner Blocker for { $host }?`
    - Suggest: `Vypnout blokování lišt cookie`
    - protections-panel-cookie-banner-blocker-header uses the correct "Blokování lišt cookie"; the same error is in the turn-on-for-site string.
- `protections-panel-site-not-working-view-issue-list-fonts` — `browser/browser/protectionsPanel.ftl` — List item not in the instrumental case required by the introducing header, unlike all other items.
    - Current: `Písma`
    - Source: `Fonts`
    - Suggest: `písmy`
    - The header reads "…pokud pozorujete problémy s:" and the other items are "přihlášením", "platbami", "psaním komentářů"; "Písma" does not agree.
- `safeb-blocked-phishing-page-learn-more` — `browser/browser/safebrowsing/blockedSite.ftl` — Missing preposition "o" before "ochraně".
    - Current: `Zjistěte více ochraně proti phishingu a malwaru`
    - Source: `Learn more about deceptive sites and phishing at <a data-l10n-name='learn_more_link'>www.antiphishing.org</a>. Learn more about { -brand-short-name }’s Phishing and Malware Protection at <a data-l10n-name='firefox_suppo…`
    - Suggest: `Zjistěte více o ochraně proti phishingu a malwaru`
    - "Zjistit více" requires the preposition "o" with the locative ("o ochraně"). The parallel string safeb-blocked-malware-page-learn-more-sumo in the same file correctly reads "Zjistěte více o ochraně proti phishingu a malwaru", confirming this is an omission, not a variant. Affects both the with-cases and no-cases variants.
- `safeb-blocked-unwanted-page-learn-more` — `browser/browser/safebrowsing/blockedSite.ftl` — Missing preposition "o" before "ochraně".
    - Current: `Zjistěte více ochraně proti phishingu a malwaru`
    - Source: `Learn more about harmful and unwanted software at <a data-l10n-name='learn_more_link'>Unwanted Software Policy</a>. Learn more about { -brand-short-name }’s Phishing and Malware Protection at <a data-l10n-name='firefox_…`
    - Suggest: `Zjistěte více o ochraně proti phishingu a malwaru`
    - Same omission as in safeb-blocked-phishing-page-learn-more; "Zjistěte více" needs "o" + locative. Both the with-cases and no-cases variants are affected.
- `screenshots-request-error-details` — `browser/browser/screenshots.ftl` — "vás snímek" should be the possessive "váš snímek".
    - Current: `nemohli jsme vás snímek uložit`
    - Source: `Sorry! We couldn’t save your shot. Please try again later.`
    - Suggest: `nemohli jsme váš snímek uložit`
    - en-US: "We couldn’t save your shot."; "vás" is the pronoun accusative, not the possessive.
- `add-engine-no-url` — `browser/browser/search.ftl` — Slovak verb form "Zadajte" instead of Czech "Zadejte".
    - Current: `Zadajte adresu URL.`
    - Source: `Please enter a URL.`
    - Suggest: `Zadejte adresu URL.`
    - "Zadajte" is Slovak; the neighbouring string add-engine-no-name uses the Czech "Zadejte".
- `sidebar-resize-splitter` — `browser/browser/sidebar.ftl` — Wrong case/number: "velikosti" instead of accusative singular "velikost".
    - Current: `Změnit velikosti postranní lišty`
    - Source: `aria-label: Resize sidebar`
    - Suggest: `Změnit velikost postranní lišty`
    - en-US "Resize sidebar" is singular; tabbrowser.ftl uses "Změnit velikost panelů".
- `protections-blocking-cryptominers` — `browser/browser/siteProtections.ftl` — Misspelling "kryproměn" instead of "kryptoměn".
    - Current: `Blokována těžba kryproměn`
    - Source: `title: Cryptominers Blocked`
    - Suggest: `Blokována těžba kryptoměn`
    - Everywhere else in the same surface the term is "těžba kryptoměn".
- `protections-not-blocking-cookies-third-party` — `browser/browser/siteProtections.ftl` — Misspelling "stan" instead of "stran".
    - Current: `Cookies třetích stan neblokovány`
    - Source: `title: Not Blocking Third-Party Cookies`
    - Suggest: `Cookies třetích stran neblokovány`
    - Same file uses the correct "Cookies třetích stran" in the blocking variant.
- `tab-group-editor-color-selector2-gray` — `browser/browser/tabbrowser.ftl` — Gray is given in masculine form while all other colour names in the list are feminine.
    - Current: `Šedivý`
    - Source: `(value): Gray title: Gray`
    - Suggest: `Šedá`
    - The surrounding colour labels are Modrá, Fialová, Azurová, Oranžová, Žlutá, Růžová, Zelená, Červená; profiles.ftl also uses "Šedá".
- `toolbar-drop-on-home-msg` — `browser/browser/toolbarDropHandler.ftl` — Misspelling "stánku" instead of "stránku".
    - Current: `novou domovskou stánku`
    - Source: `Do you want this document to be your new home page?`
    - Suggest: `novou domovskou stránku`
    - The plural variant in the same file correctly uses "domovské stránky".
- `webauthn-pin-required-prompt` — `browser/browser/webauthnDialog.ftl` — "Zajdete" is a typo for "Zadejte", producing nonsense ("you will drop by the PIN").
    - Current: `Zajdete prosím PIN pro vaše zařízení.`
    - Source: `Please enter the PIN for your device.`
    - Suggest: `Zadejte prosím PIN pro vaše zařízení.`
    - en-US is "Please enter the PIN for your device."
- `webrtc-allow-share-camera-and-microphone` — `browser/browser/webrtcIndicator.ftl` — "vaší webkameru" uses the genitive/dative pronoun where the accusative "vaši" is required.
    - Current: `používat vaší webkameru a mikrofon`
    - Source: `Allow { $origin } to use your camera and microphone?`
    - Suggest: `používat vaši webkameru a mikrofon`
    - Neighbouring strings correctly write "používat vaši kameru"; the same error recurs in the -audio-capture and -unsafe-delegation variants.
- `droponhomemsg` — `browser/chrome/browser/browser.properties` — Misspelling "stánku" instead of "stránku".
    - Current: `jako novou domovskou stánku?`
    - Source: `Do you want this document to be your new home page?`
    - Suggest: `jako novou domovskou stránku?`
    - "stánku" (a stall/booth) instead of "stránku" (page); droponhomemsgMultiple on the next line spells "stránky" correctly.
- `protections.blocking.cryptominers.title` — `browser/chrome/browser/browser.properties` — Misspelling "kryproměn" instead of "kryptoměn".
    - Current: `Blokována těžba kryproměn`
    - Source: `Cryptominers Blocked`
    - Suggest: `Blokována těžba kryptoměn`
    - "kryptoměna" (cryptocurrency) is misspelled; protections.notBlocking.cryptominers.title in the same file spells it correctly as "Těžba kryptoměn neblokována".
- `protections.notBlocking.cookies.3rdParty.title` — `browser/chrome/browser/browser.properties` — Misspelling "stan" instead of "stran".
    - Current: `Cookies třetích stan neblokovány`
    - Source: `Not Blocking Third-Party Cookies`
    - Suggest: `Cookies třetích stran neblokovány`
    - "třetích stran" (third parties) is misspelled as "třetích stan" (of third tents); the same phrase is spelled correctly elsewhere in the file (e.g. contentBlocking.cookies.blocking3rdParty2.label).
- `dom.filterDOMPanel` — `devtools/client/dom.properties` — Untinflected noun stack "Filtr DOM Panel"
    - Current: `Filtr DOM Panel`
    - Source: `Filter DOM Panel`
    - Suggest: `Filtrovat DOM panel`
    - Three nominatives in a row is not valid Czech; other filter placeholders in the same surface use either a verb ("Filtrovat styly") or a genitive ("Filtr vlastností").
- `har.requestBodyNotIncluded` — `devtools/client/har.properties` — Participle does not agree with neuter plural "těla"
    - Current: `Těla požadavků nejsou zahrnuty.`
    - Source: `Request bodies are not included.`
    - Suggest: `Těla požadavků nejsou zahrnuta.`
    - Same agreement error as har.responseBodyNotIncluded: neuter plural subject requires "zahrnuta".
- `har.responseBodyNotIncluded` — `devtools/client/har.properties` — Participle does not agree with neuter plural "těla"
    - Current: `Těla odpovědí nejsou zahrnuty.`
    - Source: `Response bodies are not included.`
    - Suggest: `Těla odpovědí nejsou zahrnuta.`
    - "tělo/těla" is neuter, so the passive participle must be "zahrnuta", not the feminine/masculine-inanimate "zahrnuty".
- `flexbox.togglesFlexboxHighlighter2` — `devtools/client/layout.properties` — Ungrammatical tooltip: adjective used where the noun "zvýrazňovač" is needed
    - Current: `Přepnout zvýrazněný Flexboxu`
    - Source: `Toggle Flexbox Highlighter`
    - Suggest: `Přepnout zvýrazňovač flexboxu`
    - "zvýrazněný Flexboxu" is not a valid Czech phrase (adjective + genitive noun with no head noun); the parallel string layout.toggleGridHighlighter correctly uses "Přepnout zvýrazňovač mřížky".
- `heapview.none-match` — `devtools/client/memory.properties` — Number/gender disagreement in "Žádná shody"
    - Current: `Žádná shody.`
    - Source: `No matches.`
    - Suggest: `Žádné shody.`
    - "shody" is nominative plural feminine, so the determiner must be "žádné"; "žádná" is singular.
- `styleeditor-stylesheet-all-filtered` — `devtools/client/styleeditor.ftl` — Determiner/adjective disagreement in the no-results message
    - Current: `Nebyly nalezeny žádná odpovídající kaskádové styly.`
    - Source: `No matching style sheet has been found.`
    - Suggest: `Nebyly nalezeny žádné odpovídající kaskádové styly.`
    - "styly" is masculine inanimate plural, requiring "žádné"; "žádná" does not agree with the rest of the sentence.
- `options-netmonitor-body-limit-set` — `devtools/client/toolbox-options.ftl` — Verbal noun used with an accusative object
    - Current: `Nastavení aktuální vstupní hodnotu jako maximální velikost těla požadavku/odpovědi.`
    - Source: `title: Set the current input value as maximum request/response body size.`
    - Suggest: `Nastaví aktuální vstupní hodnotu jako maximální velikost těla požadavku/odpovědi.`
    - "Nastavení" (a noun) cannot govern the accusative "hodnotu"; the neighbouring tooltips use finite verbs ("Upravit", "Obnovit").
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “lokálního režimu” but the string it names, `options-local-mode-label`, reads “Lokální režim”
    - Current: `Tento dokument lze také načíst z adresy „{ $url }“ pomocí „lokálního režimu“ v Nástrojích pro vývojáře, který lze aktivovat v panelu nastavení.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Lokální režim`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `toolbox.frames.disabled.tooltip` — `devtools/client/toolbox.properties` — Missing space produces the non-word "nastánkách"
    - Current: `jen nastánkách s několika iframy`
    - Source: `This button is only available on pages with several iframes`
    - Suggest: `jen na stránkách s několika iframy`
    - "na stránkách" was run together and mistyped; "nastánkách" is not a Czech word.
- `accessibility.text.label.issue.form.visible` — `devtools/shared/accessibility.properties` — Animate verb ending used with inanimate subject "prvky"
    - Current: `Prvky formuláře by měli mít viditelný textový štítek.`
    - Source: `Form elements should have a visible text label.`
    - Suggest: `Prvky formuláře by měly mít viditelný textový popisek.`
    - "prvky" is masculine inanimate, so the conditional participle is "měly"; the parallel Fluent string accessibility-text-label-issue-form-visible uses "by měly mít".
- _…and 11 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `smart-window-opened-tabs-summary-group` — `browser/browser/aiWindowContent.ftl` — English quotation marks around the group label, unlike the parallel string in the same file.
    - Current: `Byla vytvořena skupina “{ $label }” a otevřen { $count } panel.`
    - Source: `{$count ->} [other] Created the group “{ $label }” and opened { $count } tabs.`
    - Suggest: `Byla vytvořena skupina „{ $label }“ a otevřen { $count } panel.`
    - smart-window-grouped-tabs-summary in the same file uses „{ $label }“; smart-window-switched-tab-summary has the same problem.
- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — English quotation marks around a UI label that is also quoted differently from the actual button text.
    - Current: `Klepněte na “Obnovit data” a vyberte tento soubor`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Klepněte na „Obnovení vašich dat“ a vyberte tento soubor`
    - Czech quotes are „…“ in this tree, and the quoted control is localized as “Obnovení vašich dat” (restore-from-backup-header), so the instruction does not match the UI. Same issue in backup-file-other-browser-restore-step-3-1.
- `popup-trigger-redirect-menuitem` — `browser/browser/browser.ftl` — English quotation marks used where the file otherwise uses Czech quotes.
    - Current: `Zobrazit “{ $redirectURI }”`
    - Source: `label: Show “{ $redirectURI }”`
    - Suggest: `Zobrazit „{ $redirectURI }“`
    - The directly preceding, parallel string popup-show-popup-menuitem uses „{ $popupURI }“, as do other quoted strings in browser.ftl.
- `urlbar-result-explanation-last-visited-months` — `browser/browser/browser.ftl` — Missing space between the number placeholder and the noun in the [one] branch.
    - Current: `[one] Naposledy navštívena před { $monthsAgo }měsícem`
    - Source: `{$monthsAgo ->} [one] You last visited { $monthsAgo } month ago [other] You last visited { $monthsAgo } months ago`
    - Suggest: `[one] Naposledy navštívena před { $monthsAgo } měsícem`
    - All sibling branches and the -2 variant of the same message include the space, so this renders as “před 1měsícem”.
- `main-context-menu-audio-save-as` — `browser/browser/browserContext.ftl` — Doubled ellipsis at the end of the menu label.
    - Current: `Uložit audio jako……`
    - Source: `accesskey: v label: Save Audio As…`
    - Suggest: `Uložit audio jako…`
    - en-US has a single ellipsis, as do all neighbouring “Uložit … jako…” items in this file.
- `customkeys-conflict-unusable-body` — `browser/browser/customkeys.ftl` — English quotation marks where the sibling dialog string uses Czech quotes.
    - Current: `Tato klávesa je již použita pro akci “{ $conflict }” a není možné ji použít.`
    - Source: `This key is already used by “{ $conflict }” and cannot be used.`
    - Suggest: `Tato klávesa je již použita pro akci „{ $conflict }“ a není možné ji použít.`
    - customkeys-conflict-confirm-body, shown in the same dialog family, uses „{ $conflict }“.
- `ipprotection-feature-introduction-link-text-privacy-2` — `browser/browser/ipProtection.ftl` — Missing space before the brand placeholder, rendering “VPNFirefoxu”.
    - Current: `Integrovaná služba VPN{ -brand-product-name(case: "gen") }`
    - Source: `<a data-l10n-name="learn-more-vpn">{ -brand-product-name }’s built-in VPN</a> helps protect your browsing. Choose from multiple locations to keep where you browse more private.`
    - Suggest: `Integrovaná služba VPN { -brand-product-name(case: "gen") }`
    - The no-cases branch of the same message has the space; without it the brand name is glued to “VPN”.
- `launch-on-login-infobar-final-message` — `browser/browser/newtab/asrouter.ftl` — Uses ASCII straight quotes where the file otherwise uses Czech quotation marks.
    - Current: `vyhledejte v nastavení položku "spuštění"`
    - Source: `<strong>Open { -brand-short-name } every time you restart your computer?</strong> To manage your Startup preferences, search “startup” in settings.`
    - Suggest: `vyhledejte v nastavení položku „spuštění“`
    - set-default-pdf-handler-headline in the same file correctly uses „PDF“; straight ASCII quotes are not Czech typography.
- `windows-10-eos-global-infobar-title` — `browser/browser/newtab/asrouter.ftl` — Missing space after the closing </strong> tag, so two sentences run together.
    - Current: `systém Windows 10.</strong>Zálohujte si svá data`
    - Source: `<strong>Microsoft is no longer supporting Windows 10.</strong> Back up your info to get { -brand-product-name } ready for Windows 11.`
    - Suggest: `systém Windows 10.</strong> Zálohujte si svá data`
    - en-US has a space after </strong>; without it the rendered text reads "…Windows 10.Zálohujte…".
- `newtab-privacy-message-info-13` — `browser/browser/newtab/newtab.ftl` — Trackers rendered as "sledovací soubory" (tracking files) instead of the established "sledovací prvky".
    - Current: `{ -brand-short-name } blokuje sledovací soubory, čímž uvolňuje šířku pásma pro plynulejší streamování.`
    - Source: `{ -brand-short-name } blocks trackers, freeing up bandwidth for smoother streaming.`
    - Suggest: `{ -brand-short-name } blokuje sledovací prvky, čímž uvolňuje šířku pásma pro plynulejší streamování.`
    - Every other message in the Privacy widget group renders "trackers" as "sledovací prvky"; "sledovací soubory" additionally misstates what a tracker is (it is not a file).
- `newtab-stocks-search-no-results` — `browser/browser/newtab/newtab.ftl` — Wrong quotation marks: English opening curly quotes used instead of Czech quotes.
    - Current: `Žádné výsledky pro “{ $query }”`
    - Source: `No results for “{ $query }”`
    - Suggest: `Žádné výsledky pro „{ $query }“`
    - Czech uses German-style double quotes („ “); the string copies the English “ ” pair, and the opening mark is a closing-style quote in Czech typography.
- `newtab-weather-sponsored` — `browser/browser/newtab/newtab.ftl` — Missing space after the separator character.
    - Current: `{ $provider } ∙Sponzorované`
    - Source: `{ $provider } ∙ Sponsored`
    - Suggest: `{ $provider } ∙ Sponzorované`
    - en-US has spaces on both sides of "∙"; the same defect is repeated in newtab-weather-see-forecast-description.
- `more-from-moz-mozilla-monitor-card` — `browser/browser/preferences/moreFromMozilla.ftl` — "Internetu" is capitalized, contrary to the rest of the file.
    - Current: `kde na Internetu došlo k úniku`
    - Source: `description: Find out where your personal info has been exposed online with a free scan. label: { -mozmonitor-brand-name }`
    - Suggest: `kde na internetu došlo k úniku`
    - Czech orthography and the same file (more-from-moz-subtitle: "zdravý internet") write "internet" in lower case.
- `content-blocking-rfp-incompatibility-warning` — `browser/browser/preferences/preferences.ftl` — Stray space before the sentence-final period.
    - Current: `otisku prohlížeče . To může`
    - Source: `You’re using Resist Fingerprinting (RFP), which replaces some of { -brand-short-name }’s fingerprinting protection settings. This might cause some sites to break.`
    - Suggest: `otisku prohlížeče. To může`
    - A space separates the last word from the period. The identical defect appears in preferences-etp-rfp-warning-message.
- `sync-button-switch-profile` — `browser/browser/sync.ftl` — Mismatched quotation marks: the closing mark is a left double quote.
    - Current: `Přepnout na profil “{ $profileName }“`
    - Source: `Switch to “{ $profileName }”`
    - Suggest: `Přepnout na profil „{ $profileName }“`
    - The pair opens with “ and closes with “ instead of a proper closing mark; the file's other strings use matched pairs.
- `serviceworker-empty-suggestions2` — `devtools/client/application.ftl` — Missing space before the <a> link, rendering "vKonzoli"
    - Current: `případné jeho chyby najdete v<a>Konzoli</a>`
    - Source: `If the current page should have a service worker, you could look for errors in the <a>Console</a> or step through your service worker registration in the <span>Debugger</span>.`
    - Suggest: `případné jeho chyby najdete v <a>Konzoli</a>`
    - The preposition "v" is glued to the link text because there is no space before the markup, so the UI shows "vKonzoli".
- `netmonitor.context.perfTools` — `devtools/client/netmonitor.properties` — `netmonitor.context.perfTools` uses three dots where this locale uses …
    - Current: `Zahájit analýzu výkonu...`
    - Source: `Start Performance Analysis…`
    - The tree uses … 451 times against 4 ASCII runs.
- `styleeditor-stylesheet-rule-count` — `devtools/client/styleeditor.ftl` — Doubled period in the [few] plural variant
    - Current: `{ $ruleCount } pravidla..`
    - Source: `{$ruleCount ->} [one] { $ruleCount } rule. [other] { $ruleCount } rules.`
    - Suggest: `{ $ruleCount } pravidla.`
    - The other variants end with a single period; the extra dot is a typo.
- `ruleCount.label` — `devtools/client/styleeditor.properties` — Doubled period in the second plural form
    - Current: `#1 pravidla..`
    - Source: `#1 rule.;#1 rules.`
    - Suggest: `#1 pravidla.`
    - Same typo as in styleeditor.ftl; the other two plural forms end with one period.
- `crashreporter-submit-waiting-hardware-tests` — `toolkit/crashreporter/crashreporter.ftl` — `crashreporter-submit-waiting-hardware-tests` uses three dots where this locale uses …
    - Current: `Probíhá kontrola problémů s hardwarem a konfigurací...`
    - Source: `Checking for hardware and configuration problems…`
    - The tree uses … 451 times against 4 ASCII runs.
- `about-networking-dns-https-rr-lookup-table-column` — `toolkit/toolkit/about/aboutNetworking.ftl` — Adjacent RR column headers use opposite word order
    - Current: `RR HTTP`
    - Source: `HTTP RRs`
    - Suggest: `HTTP RR`
    - The neighbouring column about-networking-dns-https-rrs-lookup-table-column is "HTTPS RR"; reversing the order to "RR HTTP" for the paired column makes the two headers read inconsistently in the same table.
- `rights-safebrowsing-term-3` — `toolkit/toolkit/about/aboutRights.ftl` — Straight ASCII quotes instead of the Czech quotation marks used throughout the tree
    - Current: `Zrušte výběr možnosti "{ enableSafeBrowsing-label }"`
    - Source: `Uncheck the option to “{ enableSafeBrowsing-label }”`
    - Suggest: `Zrušte výběr možnosti „{ enableSafeBrowsing-label }“`
    - Every other quoted string in this partition (about:config, about:logging, aboutProfiles, aboutTelemetry, aboutHttpsOnlyError) uses „…“; this string is the only one with straight double quotes.
- `gpu-vendor-id` — `toolkit/toolkit/about/aboutSupport.ftl` — "Vendor" rendered as "prodejce" (seller), inconsistent with the rest of the page
    - Current: `ID prodejce`
    - Source: `Vendor ID`
    - Suggest: `ID výrobce`
    - The same page uses "Výrobce" for media-device-vendor and "Autor ovladače" for gpu-driver-vendor; a GPU vendor ID identifies the hardware manufacturer, not a seller.
- `webgl2-renderer` — `toolkit/toolkit/about/aboutSupport.ftl` — WebGL 2 renderer row drops "Driver" and diverges from the WebGL 1 row
    - Current: `Zobrazování WebGL2`
    - Source: `WebGL 2 Driver Renderer`
    - Suggest: `Ovladač pro zobrazování WebGL 2`
    - en-US "WebGL 2 Driver Renderer" mirrors "WebGL 1 Driver Renderer", which is translated "Ovladač pro zobrazování WebGL 1"; the WebGL 2 row also drops the space in "WebGL 2" used by every other row in the block.
- `about-telemetry-keyed-scalar-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — "Keyed" rendered as "key/important" here but as "s klíčem" for histograms
    - Current: `Klíčové skaláry`
    - Source: `Keyed Scalars`
    - Suggest: `Skaláry s klíčem`
    - "Klíčové" means "key/crucial", not "keyed"; the sibling section about-telemetry-keyed-histogram-section correctly uses "Histogramy s klíčem" on the same page.
- `about-webrtc-ice-pair-bytes-received` — `toolkit/toolkit/about/aboutWebrtc.ftl` — "Bytes received" rendered as "bytes downloaded", inconsistent with the paired sent label
    - Current: `Staženo bajtů:`
    - Source: `Bytes received:`
    - Suggest: `Přijato bajtů:`
    - The paired label uses "Odesláno bajtů"; "staženo" (downloaded) is not the counterpart of "odesláno" and misdescribes ICE pair statistics, where the locale elsewhere uses "přijato".
- `contentanalysis-block-dialog-body-download-file` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — Straight ASCII quotes around the filename while the parallel upload string uses „…“.
    - Current: `"{ $filename }"`
    - Source: `Under your organization’s data protection policies, you’re not permitted to download the file “{ $filename }”. Contact your administrator for more info.`
    - Suggest: `„{ $filename }“`
    - contentanalysis-block-dialog-body-upload-file and contentanalysis-error-message-upload-file in the same file use „…“.
- `contentanalysis-slow-agent-notification` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — Mismatched quotation marks: „ closed with ”.
    - Current: `„{ $content }”`
    - Source: `The Content Analysis tool is taking a long time to respond for resource “{ $content }”`
    - Suggest: `„{ $content }“`
    - Czech pairs „…“; the closing mark here is the English right double quote.
- `neterror-search-cta-hint-search-query` — `toolkit/toolkit/neterror/netError.ftl` — Mismatched quotation marks: Czech opening quote closed with an ASCII double quote.
    - Current: `„{ $query }"`
    - Source: `Search the web for <strong>“{ $query }”</strong>`
    - Suggest: `„{ $query }“`
    - The tree consistently uses the paired „…“ quotes; here the closing mark is a straight ASCII ".
- `pdfjs-editor-alt-text-settings-downloading-model-button` — `toolkit/toolkit/pdfviewer/viewer.ftl` — `pdfjs-editor-alt-text-settings-downloading-model-button` uses three dots where this locale uses …
    - Current: `Probíhá stahování...`
    - Source: `Downloading…`
    - The tree uses … 451 times against 4 ASCII runs.
- `pdfjs-free-text2` — `toolkit/toolkit/pdfviewer/viewer.ftl` — `pdfjs-free-text2` uses three dots where this locale uses …
    - Current: `Začněte psát...`
    - Source: `aria-label: Text Editor default-content: Start typing…`
    - The tree uses … 451 times against 4 ASCII runs.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/cs/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

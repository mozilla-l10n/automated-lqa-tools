# Firefox l10n QA — fy-NL

| | |
|---|---|
| **Generated** | 2026-11-09 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `f82b652e600a` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcf134b6aeea` |
| **Previous run** | 2026-11-09 @ `f278b81a68aa` |
| **Mode** | incremental |
| **Strings reviewed this run** | 23 of 16,875 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fy-NL: [Firefox for Android](android.md) · [Focus for Android](focus_android.md)

---

## Changes in this run

### 🆕 New findings (5)

- `preferences-etp-status-header` — `browser/browser/preferences/preferences.ftl` — Translation says 'most trackers' are blocked, where the source just says trackers are blocked automatically.
    - Current: `wêrby’t de measte trackers automatysk blokkearre wurde`
    - Source: `description: Sites use trackers to follow you online and show creepy ads. { -brand-short-name } shields you as you browse, blocking trackers automatically so you’re in control of your digital trail. label: Enhanced Trac…`
    - Suggest: `wêrby’t trackers automatysk blokkearre wurde`
    - en-US 'blocking trackers automatically' has no quantifier, but the Frisian adds 'de measte' (most).
- `preferences-etp-status-header` — `browser/browser/preferences/preferences.ftl` — 'wylst it sneupen' is ungrammatical because the conjunction 'wylst' needs a clause.
    - Current: `wylst it sneupen`
    - Source: `description: Sites use trackers to follow you online and show creepy ads. { -brand-short-name } shields you as you browse, blocking trackers automatically so you’re in control of your digital trail. label: Enhanced Trac…`
    - Suggest: `wylst jo sneupe`
    - 'wylst' (while) introduces a subordinate clause with a finite verb. It can't be followed by a nominalised infinitive.
- `elevation-finished-background-page` — `toolkit/toolkit/updates/elevation.ftl` — Wrong past participle: 'download' instead of 'downloade'.
    - Current: `is krekt download`
    - Source: `A security and stability update for { -brand-short-name } has been downloaded and is ready to be installed.`
    - Suggest: `is downloade`
    - The Frisian past participle of 'downloade' is 'downloade'. The translation also adds 'krekt' (just), which the source doesn't have.
- `SEC_ERROR_CRL_INVALID_VERSION` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo in 'Sertifikaateerroppingslist'.
    - Current: `Sertifikaateerroppingslist`
    - Source: `Issuer’s Certificate Revocation List has an unknown version number.`
    - Suggest: `Sertifikaatwerroppingslist`
    - The word should be 'werroppingslist'. The same string in nsserrors.ftl spells it correctly.
- `options-stylesheet-autocompletion-tooltip` — `devtools/client/toolbox-options.ftl` — Wrong verb form 'type' instead of 'typje'.
    - Current: `wylst jo type`
    - Source: `title: Autocomplete CSS properties, values and selectors in Style Editor as you type`
    - Suggest: `wylst jo typje`
    - The Frisian verb is 'typje', and its form with 'jo' is 'typje'.

### ✅ Fixed since the last run (21)

- `restart-required-single-instance-answer-2` — `browser/browser/aboutRestartRequired.ftl` — 'working normally' has been reduced to 'normal', so the sentence now says restarting keeps the browser 'safe and normal'.
    - Current: `feilich en normaal.`
    - Source: `This can happen during a long browsing session, or when your operating system updates { -brand-short-name }. Restarting keeps { -brand-short-name } secure and working normally.`
    - Suggest: `feilich en normaal wurkjend.`
    - en-US says restarting keeps the browser 'secure and working normally'. The Frisian drops the verb 'working', which changes the meaning and reads oddly.
- `contextual-manager-passwords-delete-all-passwords-checkbox` — `browser/browser/contextual-manager.ftl` — Typo: 'wachturd' should be 'wachtwurd'.
    - Current: `Ja, wachturd fuortsmite`
    - Source: `{$total ->} [1] Yes, delete password [other] Yes, delete passwords`
    - Suggest: `Ja, wachtwurd fuortsmite`
    - The Frisian word for password is 'wachtwurd', as spelled in the other variant and the surrounding strings.
- `genai-more-actions-all-off-notice` — `browser/browser/genai.ftl` — The settings path leaves out 'Tabs' and turns 'browsing' into the verb 'browse', and 'it' (the menu) has become 'the page'.
    - Current: `<span data-l10n-name="chevron"></span> en blêdzje om de side opnij te toanen.`
    - Source: `You won’t see this menu when you select text. Visit Settings <span data-l10n-name="chevron"></span> Tabs and browsing to show it again.`
    - Suggest: `<span data-l10n-name="chevron"></span> Ljepblêden en navigaasje om it menu opnij te toanen.`
    - en-US says 'Settings > Tabs and browsing' (a settings section name) and that this shows the menu again. The Frisian reads 'Visit Settings > and browse to show the page again', so the user gets the wrong path and the wrong object.
- `newtab-wallpaper-palm-trees` — `browser/browser/newtab/newtab.ftl` — 'wylst' is a conjunction and cannot govern the noun phrase 'gouden oere'.
    - Current: `wylst gouden oere`
    - Source: `Silhouette of coconut palm trees during golden hour`
    - Suggest: `yn it gouden oere`
    - 'during golden hour' needs a preposition (yn/tidens) plus article; 'wylst gouden oere' is ungrammatical.
- `hnt-card-extensions-body` — `browser/browser/newtab/onboarding.ftl` — 'meast leafste' is a double superlative; 'most loved' should be 'meast leafde'.
    - Current: `meast leafste`
    - Source: `Customize your browsing with our most loved extensions.`
    - Suggest: `meast leafde`
    - 'leafste' is already superlative; combining with 'meast' is ungrammatical. The source means 'most loved'.
- `hnt-card-pin-body` — `browser/browser/newtab/onboarding.ftl` — Nominal infinitive should be 'navigearjen', not the bare verb 'navigearje'.
    - Current: `beskerme navigearje fan`
    - Source: `{$sel_1 ->} [macos] Jump back in to protected browsing from your dock. [other] Jump back in to protected browsing from your taskbar.`
    - Suggest: `beskerme navigearjen fan`
    - Used as a noun after 'nei', Frisian requires the -en form, as the locale itself uses in 'Begjin mei navigearjen'.
- `tab-groups-onboarding-auto-saved-title` — `browser/browser/newtab/onboarding.ftl` — 'Tabgroepen' is a Dutch-style term inconsistent with the locale's 'ljepblêd' and 'groep'.
    - Current: `Tabgroepen`
    - Source: `Tab groups are auto-saved. Find them here.`
    - Suggest: `Ljepblêdgroepen`
    - The locale translates 'tab' as 'ljepblêd' and 'group' as 'groep' (e.g. 'Ljepblêden oan groep tafoegje'); 'Tabgroepen' mixes English and Dutch forms.
- `policy-DisableThirdPartyModuleBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — Stray 'oer' ('about') inserted before the about:third-party reference, garbling the feature name.
    - Current: `eksterne module-ynformaasje oer (about:third-party)`
    - Source: `Prevent the user from using Third-party Module Information (about:third-party) to block third-party modules injected into the { -brand-short-name } process.`
    - Suggest: `eksterne module-ynformaasje (about:third-party)`
    - The source names the page 'Third-party Module Information (about:third-party)'; the added 'oer' makes it read 'information about (about:third-party)'.
- `policy-OfferToSaveLoginsDefault` — `browser/browser/policies/policies-descriptions.ftl` — Infinitive clause uses 'mei' instead of 'om' after 'oanbiede'.
    - Current: `oanbiede mei bewarre oanmeldingen en wachtwurden te ûnthâlden`
    - Source: `Set the default value for allowing { -brand-short-name } to offer to remember saved logins and passwords. Both true and false values are accepted.`
    - Suggest: `oanbiede om bewarre oanmeldingen en wachtwurden te ûnthâlden`
    - 'offer to remember' requires 'om … te' in Frisian; 'mei … te ûnthâlden' is a grammatical slip.
- `sync-engine-payment-methods3` — `browser/browser/preferences/preferences.ftl` — Tooltip uses the Dutch spelling 'Betellingsmethoden', inconsistent with the label's Frisian 'Betellingsmetoaden'.
    - Current: `Betellingsmethoden`
    - Source: `accesskey: n label: Payment methods tooltiptext: Payment methods you’ve saved`
    - Suggest: `Betellingsmetoaden`
    - Frisian spelling is 'metoaden', as in the label of the same message.
- `sync-engine-tabs2` — `browser/browser/preferences/preferences.ftl` — Tooltip uses the imperative verb 'Iepenje' (open!) instead of the adjective 'iepen' (open tabs).
    - Current: `Iepenje ljepblêden`
    - Source: `accesskey: t label: Open tabs tooltiptext: Open tabs from your other devices`
    - Suggest: `Iepen ljepblêden`
    - The developer comment states 'Open tabs' is a modified noun (tabs that are open), not an instruction.
- `sync-engine-tabs2` — `browser/browser/preferences/preferences.ftl` — Misspelling of 'ljepblêden' (missing b) in the label.
    - Current: `Iepen ljeplêden`
    - Source: `accesskey: t label: Open tabs tooltiptext: Open tabs from your other devices`
    - Suggest: `Iepen ljepblêden`
    - The locale's word for tabs is 'ljepblêden', as used in the tooltip and elsewhere.
- `tab-context-close-duplicate-tabs-alt` — `browser/browser/tabContextMenu.ftl` — Typo: 'jepblêden' is missing the initial 'l' of 'ljepblêden'.
    - Current: `Dûbele jepblêden`
    - Source: `accesskey: x label: Duplicate Tabs`
    - Suggest: `Dûbele ljepblêden`
    - The locale's word for tabs is 'ljepblêden', used consistently elsewhere in the tab context menu.
- `options-stylesheet-autocompletion-tooltip` — `devtools/client/toolbox-options.ftl` — Wrong verb form 'type' instead of 'typje'.
    - Current: `wylst jo type`
    - Source: `title: Autocomplete CSS properties, values and selectors in Style Editor as you type`
    - Suggest: `wylst jo typje`
    - The Frisian verb is 'typje', and its form with 'jo' is 'typje'.
- `about-processes-collapse-all-sites` — `toolkit/toolkit/about/aboutProcesses.ftl` — "Alle ynklappe" uses the plural adjective form instead of the pronoun "Alles", which the sibling string "Alles útklappe" uses.
    - Current: `Alle ynklappe`
    - Source: `title: Collapse all`
    - Suggest: `Alles ynklappe`
    - "Collapse all" needs the standalone pronoun "alles"; "alle" needs a following noun. This is also inconsistent with "Alles útklappe".
- `sec-error-baggage-not-created` — `toolkit/toolkit/neterror/nsserrors.ftl` — Ungrammatical construction: the conjunction 'wylst' is followed by a noun phrase.
    - Current: `flater wylst it meitsjen fan bagageobjekt`
    - Source: `error while creating baggage object`
    - Suggest: `flater by it meitsjen fan bagageobjekt`
    - 'wylst' is a conjunction that needs a clause; 'error while creating' should be 'flater by it meitsjen fan'.
- `sec-error-crl-invalid-version` — `toolkit/toolkit/neterror/nsserrors.ftl` — 'unknown version number' translated as 'invalid version number'.
    - Current: `hat in ûnjildich ferzjenûmer`
    - Source: `Issuer’s Certificate Revocation List has an unknown version number.`
    - Suggest: `hat in ûnbekend ferzjenûmer`
    - Source says 'unknown', not 'invalid'; 'ûnjildich' means invalid.
- `ssl-error-cipher-disallowed-for-version` — `toolkit/toolkit/neterror/nsserrors.ftl` — Preposition 'yn' (in) used instead of the indefinite article 'in' (a).
    - Current: `selektearre yn net tastiene`
    - Source: `SSL peer selected a cipher suite disallowed for the selected protocol version.`
    - Suggest: `selektearre in net tastiene`
    - Source 'selected a cipher suite' needs the article 'in'; 'yn' means 'in/into'.
- `elevation-finished-background-page` — `toolkit/toolkit/updates/elevation.ftl` — Wrong past participle: 'download' instead of 'downloade'.
    - Current: `is krekt download`
    - Source: `A security and stability update for { -brand-short-name } has been downloaded and is ready to be installed.`
    - Suggest: `is downloade`
    - The Frisian past participle of 'downloade' is 'downloade'. The translation also adds 'krekt' (just), which the source doesn't have.
- `options-stylesheet-autocompletion-tooltip` — `devtools/client/toolbox-options.ftl` — Wrong verb form 'type' instead of 'typje'.
    - Current: `wylst jo type`
    - Source: `title: Autocomplete CSS properties, values and selectors in Style Editor as you type`
    - Suggest: `wylst jo typje`
    - The Frisian verb is 'typje', and its form with 'jo' is 'typje'.
- `elevation-finished-background-page` — `toolkit/toolkit/updates/elevation.ftl` — Wrong past participle: 'download' instead of 'downloade'.
    - Current: `is krekt download`
    - Source: `A security and stability update for { -brand-short-name } has been downloaded and is ready to be installed.`
    - Suggest: `is downloade`
    - The Frisian past participle of 'downloade' is 'downloade'. The translation also adds 'krekt' (just), which the source doesn't have.

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
| Files | 331 |
| Strings | 16,875 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 1 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-single` 815, `straight-double` 26, `curly-double` 16 | **curly-single** |
| apostrophe | `typographic` 1537 | **typographic** |
| ellipsis | `char` 403 | **char** |
| dash | `em` 12, `en` 86 | **en** |
| nbsp | `total` 4, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (175)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 4 |
| 2 | Wrong content (says something other than the English) | 62 |
| 3 | Degraded language (grammar, spelling, terminology) | 80 |
| 4 | Cosmetic (typography, spacing) | 29 |

### A. Functional, markup, variables & plurals

- `error-try-again` — `browser/browser/aboutRobots.ftl` — .label2 left in English while the value is translated
    - Source: `(value): Try Again label2: Please do not press this button again.`
- `styleeditor-pretty-print-button` — `devtools/client/styleeditor.ftl` — Left in English ("Stylesheet Pretty Print") while both siblings are translated
    - Source: `title: Pretty print style sheet`
- `styleeditor-save-button` — `devtools/client/styleeditor.ftl` — Access key `s` of `styleeditor-save-button` is not present in its label
    - Current: `s`
    - Source: `(value): Save accesskey: S tooltiptext: Save this style sheet to a file`
    - The label is “Bewarje”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `url-classifier-content-classifier-loading-url` — `toolkit/toolkit/about/url-classifier.ftl` — URL lade (imperative) → Ladende URL (noun label, per comment)
    - Current: `URL lade`
    - Source: `Loading URL`
    - Suggest: `Ladende URL`
- `url-classifier-content-classifier-loading-url-enabled` — `toolkit/toolkit/about/url-classifier.ftl` — Laden fan URL ynskeakelje → Ladende URL ynskeakelje
    - Current: `Laden fan URL ynskeakelje`
    - Source: `Enable loading URL`
    - Suggest: `Ladende URL ynskeakelje`

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-logins-import-report-page-title` — `browser/browser/aboutLogins.ftl` — Gearfettend rapport ymportearje → Rapport ymportgearfetting
    - Current: `Gearfettend rapport ymportearje`
    - Source: `Import Summary Report`
    - Suggest: `Rapport ymportgearfetting`
- `browser-window-restore-down-button` — `browser/browser/browser.ftl` — Omleech opnij ynstelle → Ferlytsje
    - Current: `Omleech opnij ynstelle`
    - Source: `tooltiptext: Restore Down`
    - Suggest: `Ferlytsje`
- `identity-https-only-info-no-upgrade` — `browser/browser/browser.ftl` — HTTP-ferbining net fernije → ferbining net opwurdearje fan HTTP
    - Current: `HTTP-ferbining net fernije`
    - Source: `Unable to upgrade connection from HTTP.`
    - Suggest: `ferbining net opwurdearje fan HTTP`
- `urlbar-placeholder-search-mode-other-actions` — `browser/browser/browser.ftl` — Sykaksjes → Sykje yn aksjes / Aksjes trochsykje ("Search" is a verb)
    - Current: `Sykaksjes`
    - Source: `aria-label: Search actions placeholder: Enter search terms`
    - Suggest: `Sykje yn aksjes`
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — Sykaksjes → Sykje yn aksjes / Aksjes trochsykje ("Search" is a verb)
    - Current: `Sykaksjes`
    - Source: `Search Actions`
    - Suggest: `Sykje yn aksjes`
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
- `genai-menu-ask-smart-window` — `browser/browser/genai.ftl` — Fragen… → Freegje…
    - Current: `Fragen…`
    - Source: `accesskey: z label: Ask…`
    - Suggest: `Freegje…`
- `genai-page-warning` — `browser/browser/genai.ftl` — is dit foar in part de gearfetting → is dit in dielgearfetting
    - Current: `is dit foar in part de gearfetting`
    - Source: `message: Since the page is long, this is a partial summary.`
    - Suggest: `is dit in dielgearfetting`
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
- `newtab-wallpaper-your-images-folder` — `browser/browser/newtab/newtab.ftl` — The accessible name changes "Your images, wallpapers that you have saved" into "Your saved images and wallpapers", turning an appositive description into two separate categories.
    - Current: `Jo bewarre ôfbyldingen en eftergrûnen`
    - Source: `aria-label: Your images, wallpapers that you have saved`
    - Suggest: `Jo ôfbyldingen, eftergrûnen dy’t jo bewarre hawwe`
    - The en-US names one thing — the "Your images" folder — and explains it as wallpapers the user saved; the Frisian lists images and wallpapers as two things, losing the link to the "Jo ôfbyldingen" label.
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — The word “major” is missing, so the Frisian says Firefox is the only browser of any kind backed by a non-profit.
    - Current: `de iennige browser dy’t stipe wurdt`
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
    - Suggest: `de iennige grutte browser dy’t stipe wurdt`
    - The en-US says “the only major browser backed by a non-profit”. Without “major” (grutte), the Frisian makes a broader factual claim than the source.
- `onboarding-refresh-tou-pin-unchecked` — `browser/browser/newtab/onboarding.ftl` — "a click away" is rendered as "ien klik fuort", which in Frisian/Dutch idiom says the browser is one click *away/gone* rather than within one click's reach.
    - Current: `Hâld de iennige grutte ûnôfhinklike browser ien klik fuort`
    - Source: `Keep the only major independent browser a click away`
    - Suggest: `Hâld de iennige grutte ûnôfhinklike browser op ien klik ôfstân`
    - The en-US means keeping the browser easily reachable (one click away); "ien klik fuort" reads as removing/keeping it away.
- `preferences-etp-advanced-settings-group` — `browser/browser/preferences/preferences.ftl` — The quantifier "most" is missing, so the text claims trackers are blocked without the source's limit.
    - Current: `wêrby’t trackers automatysk blokkearre wurde`
    - Source: `description: Sites use trackers to follow you online and show creepy ads. { -brand-short-name } shields you as you browse, blocking most trackers automatically so you’re in control of your digital trail. label: Advanced…`
    - Suggest: `wêrby’t de measte trackers automatysk blokkearre wurde`
    - The en-US says "blocking most trackers automatically". The Frisian is copied from the ETP status header, which has no "most", so this text no longer says the protection is partial.
- `preferences-etp-status-header` — `browser/browser/preferences/preferences.ftl` — Translation says 'most trackers' are blocked, where the source just says trackers are blocked automatically.
    - Current: `wêrby’t de measte trackers automatysk blokkearre wurde`
    - Source: `description: Sites use trackers to follow you online and show creepy ads. { -brand-short-name } shields you as you browse, blocking trackers automatically so you’re in control of your digital trail. label: Enhanced Trac…`
    - Suggest: `wêrby’t trackers automatysk blokkearre wurde`
    - en-US 'blocking trackers automatically' has no quantifier, but the Frisian adds 'de measte' (most).
- `profiles-pink-theme-title` — `browser/browser/profiles.ftl` — Rôze → Rôs (its own label is Rôs)
    - Current: `Rôze`
    - Source: `title: Apply pink theme`
    - Suggest: `Rôs`
- `item-offline-apps` — `browser/browser/sanitize.ftl` — Bewarre websitegegevens → Offline websitegegevens
    - Current: `Bewarre websitegegevens`
    - Source: `accesskey: O label: Offline website data`
    - Suggest: `Offline websitegegevens`
- `sanitize-button-clearing` — `browser/browser/sanitize.ftl` — Wiskje (identical to sanitize-button-ok2) → Dwaande mei wiskjen…
    - Source: `label: Clearing`
    - Suggest: `Dwaande mei wiskjen…`
- `tab-context-close-multiple-tabs` — `browser/browser/tabContextMenu.ftl` — Mear ljepblêden slute → Meardere ljepblêden slute
    - Current: `Mear ljepblêden slute`
    - Source: `accesskey: M label: Close Multiple Tabs`
    - Suggest: `Meardere ljepblêden slute`
- `network-menu-summary-finish` — `devtools/client/netmonitor.ftl` — Foltôgje: (imperative) → Klear: (noun label)
    - Current: `Foltôgje:`
    - Source: `Finish: { $formattedTime }`
    - Suggest: `Klear:`
- `jsonlScopeName` — `devtools/client/netmonitor.properties` — "JSON Lines" is a format name that should not be translated.
    - Current: `JSON-regels`
    - Source: `JSON Lines`
    - Suggest: `JSON Lines`
    - The developer comment explains this is the JSON Lines (JSONL/NDJSON) format name displayed as the payload type; it is a format identifier, not descriptive text.
- `perftools-heading-features-default` — `devtools/client/perftools.ftl` — (standert oan oanrekommandearre) — two words collide; → (oanrekommandearre, standert oan)
    - Current: `(standert oan oanrekommandearre)`
    - Source: `Features (Recommended on by default)`
    - Suggest: `(oanrekommandearre, standert oan)`
- `styleeditor-import-button` — `devtools/client/styleeditor.ftl` — Says "apply to an existing style sheet"; en-US: "Import and append an existing style sheet to the document"
    - Source: `accesskey: I tooltiptext: Import and append an existing style sheet to the document`
- `inactive-css-at-position-try-not-supported` — `devtools/client/tooltips.ftl` — Translation inserts 'yn de folgjende browsers' (in the following browsers), which the source does not contain.
    - Current: `wurdt net stipe yn de folgjende browsers <strong>@position-try</strong>-regels.`
    - Source: `<strong>{ $property }</strong> is not supported in <strong>@position-try</strong> rules.`
    - Suggest: `wurdt net stipe yn <strong>@position-try</strong>-regels.`
    - The source says the property is not supported in @position-try rules. The Frisian says 'not supported in the following browsers @position-try rules', which is wrong and garbled.
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — Argument name written 'URLSTRING' in the explanation, which doesn't match 'URL_STRING' in the usage line.
    - Current: `argumint URLSTRING`
    - Source: `:block URL_STRING  Start blocking network requests    It accepts only one URL_STRING argument, an unquoted string which will be used to block all requests whose URL includes this string.   Use :unblock or the Network Mo…`
    - Suggest: `argumint URL_STRING`
    - The usage line and the source both name the argument URL_STRING. The explanation should refer to it the same way.
- `config-pref-reset-button` — `mobile/android/mobile/android/aboutConfig.ftl` — Werinisjalisearje → Weromsette (established rendering of "Reset")
    - Current: `Werinisjalisearje`
    - Source: `Reset`
    - Suggest: `Weromsette`
- `pippki-failed-pw-change` — `security/manager/security/pippki/pippki.ftl` — All five add "haad-" (Primary); these are the security-device password dialogs, not the Primary Password. pippki-incorrect-pw also drops "current".
    - Source: `Unable to change password.`
- `pippki-incorrect-pw` — `security/manager/security/pippki/pippki.ftl` — All five add "haad-" (Primary); these are the security-device password dialogs, not the Primary Password. pippki-incorrect-pw also drops "current".
    - Source: `You did not enter the correct current password. Please try again.`
- `pippki-pw-change2empty-in-fips-mode` — `security/manager/security/pippki/pippki.ftl` — All five add "haad-" (Primary); these are the security-device password dialogs, not the Primary Password. pippki-incorrect-pw also drops "current".
    - Source: `You are currently in FIPS mode. FIPS requires a non-empty password.`
- `pippki-pw-erased-ok` — `security/manager/security/pippki/pippki.ftl` — All five add "haad-" (Primary); these are the security-device password dialogs, not the Primary Password. pippki-incorrect-pw also drops "current".
    - Source: `You have deleted your password. { pippki-pw-empty-warning }`
- `pippki-pw-not-wanted` — `security/manager/security/pippki/pippki.ftl` — All five add "haad-" (Primary); these are the security-device password dialogs, not the Primary Password. pippki-incorrect-pw also drops "current".
    - Source: `Warning! You have decided not to use a password. { pippki-pw-empty-warning }`
- `about-about-note` — `toolkit/toolkit/about/aboutAbout.ftl` — se wearden nedich hawwe → se querystrings fereaskje
    - Current: `se wearden nedich hawwe`
    - Source: `This is a list of “about” pages for your convenience.<br/> Some of them might be confusing. Some are for diagnostic purposes only.<br/> And some are omitted because they require query strings.`
    - Suggest: `se querystrings fereaskje`
- `addon-badge-line4` — `toolkit/toolkit/about/aboutAddons.ftl` — 'Firefox' added after 'Mozilla', though the developer comment says only 'Mozilla' is fixed so that forks don't show a different maker.
    - Current: `troch Mozilla Firefox boude`
    - Source: `title: Official extension built by Mozilla. Meets security and performance standards`
    - Suggest: `troch Mozilla boude`
    - The source says 'built by Mozilla'. The developer comment explains that 'Mozilla' is fixed text so forks don't display their own name. Adding 'Firefox' brings in a product brand the source deliberately left out.
- `about-glean-about-data-list-item-dictionary` — `toolkit/toolkit/about/aboutGlean.ftl` — { -glean-brand-name }-biblioteek → { -glean-brand-name } Dictionary
    - Current: `{ -glean-brand-name }-biblioteek`
    - Source: `To browse the list of data collected by { -glean-brand-name } per application, please consult the <a data-l10n-name="glean-dictionary-link">{ -glean-brand-name } Dictionary</a>.`
    - Suggest: `{ -glean-brand-name } Dictionary`
- `about-glean-metrics-table-settings-hide-empty-value-rows` — `toolkit/toolkit/about/aboutGlean.ftl` — Regels (rules) → Rigen (table rows)
    - Current: `Regels`
    - Source: `Hide empty value rows`
    - Suggest: `Rigen`
- `about-networking-dns-lookup-button` — `toolkit/toolkit/about/aboutNetworking.ftl` — Omsette (convert/translate) → Opsykje (en-US: "Resolve")
    - Current: `Omsette`
    - Source: `Resolve`
    - Suggest: `Opsykje`
- `about-processes-inference-process` — `toolkit/toolkit/about/aboutProcesses.ftl` — Konklúzje → Inference (ML inference process)
    - Current: `Konklúzje`
    - Source: `Inference ({ $pid })`
    - Suggest: `Inference`
- `about-reader-font-weight-light` — `toolkit/toolkit/about/aboutReader.ftl` — Ljocht (brightness) → Tin (font weight)
    - Current: `Ljocht`
    - Source: `Light`
    - Suggest: `Tin`
- `media-device-rate` — `toolkit/toolkit/about/aboutSupport.ftl` — Wurdearrring → Frekwinsje (device sample rate)
    - Current: `Wurdearrring`
    - Source: `Rate`
    - Suggest: `Frekwinsje`
- `place-database-stats-size-kib` — `toolkit/toolkit/about/aboutSupport.ftl` — Grutte (KB) → Grutte (KiB)
    - Current: `Grutte (KB)`
    - Source: `Size (KiB)`
    - Suggest: `Grutte (KiB)`
- `reset-on-next-restart` — `toolkit/toolkit/about/aboutSupport.ftl` — Opnij ynstelle nij werstart → … by de folgjende werstart
    - Current: `Opnij ynstelle nij werstart`
    - Source: `Reset on Next Restart`
    - Suggest: `… by de folgjende werstart`
- `roundtrip-latency` — `toolkit/toolkit/about/aboutSupport.ftl` — Retinsjelatinsje (retention) → Retoerlatinsje
    - Current: `Retinsjelatinsje`
    - Source: `Roundtrip latency (standard deviation)`
    - Suggest: `Retoerlatinsje`
- `sample-rate` — `toolkit/toolkit/about/aboutSupport.ftl` — foarbyldfrekwinsje → samplefrekwinsje
    - Current: `foarbyldfrekwinsje`
    - Source: `Preferred Sample Rate`
    - Suggest: `samplefrekwinsje`
- `about-telemetry-current-store` — `toolkit/toolkit/about/aboutTelemetry.ftl` — Aktuele winkel: → Aktuele opslach:
    - Current: `Aktuele winkel:`
    - Source: `Current Store:`
    - Suggest: `Aktuele opslach:`
- `about-telemetry-events-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — Eveneminten (social events) → Barrens
    - Current: `Eveneminten`
    - Source: `Events`
    - Suggest: `Barrens`
- `about-telemetry-histogram-stats` — `toolkit/toolkit/about/aboutTelemetry.ftl` — foarbyld/foarbylden → stekproef/stekproeven
    - Source: `{$sampleCount ->} [one] { $sampleCount } sample, average = { $prettyAverage }, sum = { $sum } [other] { $sampleCount } samples, average = { $prettyAverage }, sum = { $sum }`
- `about-telemetry-late-writes-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — Lêste add-ons → Lette skriuwaksjes
    - Current: `Lêste add-ons`
    - Source: `Late Writes`
    - Suggest: `Lette skriuwaksjes`
- `about-telemetry-memory-map-title` — `toolkit/toolkit/about/aboutTelemetry.ftl` — Unthâldtawizing: (allocation) → Unthâldkaart:
    - Current: `Unthâldtawizing:`
    - Source: `Memory map:`
    - Suggest: `Unthâldkaart:`
- `about-telemetry-no-search-results-all` — `toolkit/toolkit/about/aboutTelemetry.ftl` — yn watfoar seksje reads interrogative → yn gjin inkelde seksje
    - Current: `yn watfoar seksje`
    - Source: `Sorry! There are no results in any sections for “{ $searchTerms }”`
    - Suggest: `yn gjin inkelde seksje`
- `third-party-intro` — `toolkit/toolkit/about/aboutThirdParty.ftl` — ynboud → ynjektearre (contradicts the next sentence)
    - Current: `ynboud`
    - Source: `This page shows the third-party modules which were injected into your { -brand-short-name }. Any module that is not signed by Microsoft or { -vendor-short-name } is considered to be a third-party module.`
    - Suggest: `ynjektearre`
- `about-webrtc-dropped-frames-label` — `toolkit/toolkit/about/aboutWebrtc.ftl` — Ferlerne frames: collides with about-webrtc-lost-label → Fallen litten frames:
    - Source: `Dropped frames:`
    - Suggest: `Fallen litten frames:`
- `about-webrtc-ice-restart-count-label` — `toolkit/toolkit/about/aboutWebrtc.ftl` — ICE start opnij: (status) → ICE-werstarts: (counter label)
    - Current: `ICE start opnij:`
    - Source: `ICE restarts:`
    - Suggest: `ICE-werstarts:`
- `about-webrtc-max-padding-bytes-sec` — `toolkit/toolkit/about/aboutWebrtc.ftl` — opfolling (succession) → padding
    - Current: `opfolling`
    - Source: `Maximum Padding (bytes/sec)`
    - Suggest: `padding`
- `certificate-viewer-extended-key-usages` — `toolkit/toolkit/about/certviewer.ftl` — Wiidweidige brûksmooglikheden → Utwreide kaaibrûksmooglikheden
    - Current: `Wiidweidige brûksmooglikheden`
    - Source: `Extended Key Usages`
    - Suggest: `Utwreide kaaibrûksmooglikheden`
- `certificate-viewer-key-usages` — `toolkit/toolkit/about/certviewer.ftl` — Wichtichste brûksmooglikheden → Kaaibrûksmooglikheden (cryptographic key)
    - Current: `Wichtichste brûksmooglikheden`
    - Source: `Key Usages`
    - Suggest: `Kaaibrûksmooglikheden`
- `certificate-viewer-tab-ca` — `toolkit/toolkit/about/certviewer.ftl` — Organisaasjes → Autoriteiten (this tab lists CAs)
    - Current: `Organisaasjes`
    - Source: `Authorities`
    - Suggest: `Autoriteiten`
- _…and 4 more; see `state/` for the full list._

### C. Grammar, agreement & spelling

- `about-logins-confirm-delete-all-sync-dialog-message` — `browser/browser/aboutLogins.ftl` — The particle is missing from the separable verb, so "smyt it fan" does not mean "deletes it from".
    - Current: `Dit smyt it fan`
    - Source: `{$count ->} [1] This deletes it from { -brand-short-name } on every device that syncs your passwords. You can’t undo this. [other] This deletes them from { -brand-short-name } on every device that syncs your passwords.…`
    - Suggest: `Dit smyt it út`
    - Without "út" or "fuort", "smite" does not mean "delete". The parallel string about-logins-confirm-delete-dialog-message correctly uses "smyt it út". The same fix applies to the plural form ("smyt se út").
- `about-unloads-column-sortweight` — `browser/browser/aboutUnloads.ftl` — ôflaad → ôflaat
    - Current: `ôflaad`
    - Source: `(value): Secondary Weight title: If available, tabs are sorted by this value after being sorted by the base weight. The value derives from tab’s memory usage and the count of processes.`
    - Suggest: `ôflaat`
- `about-unloads-column-weight` — `browser/browser/aboutUnloads.ftl` — alteart → allearst; ôflaad → ôflaat
    - Current: `alteart`
    - Source: `(value): Base Weight title: Tabs are first sorted by this value, which derives from some special attributes such as playing a sound, WebRTC, etc.`
    - Suggest: `allearst`
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — Dangling hokker ljepblêden at the end
    - Source: `If you still want to group tabs, choose <strong>Retry</strong> and select which ones in the card that opens.`
- `onboarding-aw-finish-setup-button` — `browser/browser/browser.ftl` — Ynstellen { -brand-short-name } → Ynstellen fan { -brand-short-name }
    - Current: `Ynstellen { -brand-short-name }`
    - Source: `label: Finish setup tooltiptext: Finish setting up { -brand-short-name }`
    - Suggest: `Ynstellen fan { -brand-short-name }`
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
- `downloads-unblock-insecure` — `browser/browser/downloads.ftl` — 'wylst' is a conjunction and can't come before a noun phrase; a preposition such as 'tidens' is needed here.
    - Current: `wylst it downloadproses`
    - Source: `The download is offered over HTTP even though the current document was delivered over a secure HTTPS connection. If you proceed, the download may be corrupted or tampered with during the download process.`
    - Suggest: `tidens it downloadproses`
    - The en-US says 'during the download process'. That needs a preposition in Frisian, but 'wylst' ('while') has to introduce a clause, so this is ungrammatical.
- `vertical-tabs-callout-2-subtitle` — `browser/browser/featureCallout.ftl` — list mei ljeppers → list mei ljepblêden
    - Current: `list mei ljeppers`
    - Source: `This layout makes it easy to quickly scan your list of tabs. Plus, you can adjust the width to see more or less of your tab titles.`
    - Suggest: `list mei ljepblêden`
- `genai-prompts-proofread` — `browser/browser/genai.ftl` — krekten → krektens
    - Current: `krekten`
    - Source: `label: Proofread value: Please proofread the selection for spelling and grammar errors. Identify any mistakes and provide a corrected version of the text. Maintain the meaning and factual accuracy and output the list of…`
    - Suggest: `krektens`
- `menu-application-hide-other` — `browser/browser/menubar.ftl` — Oare ferstopje → Oaren ferstopje
    - Current: `Oare ferstopje`
    - Source: `label: Hide Others`
    - Suggest: `Oaren ferstopje`
- `migration-list-autofill-label` — `browser/browser/migrationWizard.ftl` — gegevens automatysk ynfolje → gegevens foar automatysk ynfoljen
    - Current: `gegevens automatysk ynfolje`
    - Source: `autofill data`
    - Suggest: `gegevens foar automatysk ynfoljen`
- `taskbar-tabs-spotlight-subtitle` — `browser/browser/newtab/asrouter.ftl` — The adjective has the wrong ending: 'finster' is a neuter noun, so after 'in' the adjective takes no -e.
    - Current: `in ferienfâldige finster`
    - Source: `One click launches your most used sites in a streamlined window with all of { -brand-short-name }’s protections.`
    - Suggest: `in ferienfâldich finster`
    - In Frisian, 'finster' takes the article 'it', which makes it neuter. When a neuter noun follows the indefinite article 'in', the adjective before it has no -e ending (for example 'in grut finster'). So 'ferienfâldige' should be 'ferienfâldich'.
- `newtab-picture-widget-open-menu-button` — `browser/browser/newtab/newtab.ftl` — Mistranslated/misparsed compound: "Ofbylding fan it dei-menu" means "the day menu's picture" instead of "picture of the day menu"; also missing diacritic on "Ôfbylding".
    - Current: `aria-label: Ofbylding fan it dei-menu iepenje`
    - Source: `aria-label: Open picture of the day menu title: Open picture of the day menu`
    - Suggest: `aria-label: Menu Ôfbylding fan de dei iepenje`
    - Source means the menu of the "picture of the day" widget; the Frisian attaches "menu" to "dei", and the Frisian word is spelled "Ôfbylding".
- `newtab-section-unblock-topic` — `browser/browser/newtab/newtab.ftl` — Blokkearring { $topic } opheffe → Blokkearring fan { $topic } opheffe
    - Current: `Blokkearring { $topic } opheffe`
    - Source: `aria-label: Unblock { $topic }`
    - Suggest: `Blokkearring fan { $topic } opheffe`
- `newtab-wallpaper-abstract-purple-green` — `browser/browser/newtab/newtab.ftl` — Pears en griene → Pearze en griene
    - Current: `Pears en griene`
    - Source: `Purple and green light gradient`
    - Suggest: `Pearze en griene`
- `page-info-page` — `browser/browser/pageInfo.ftl` — 'Sydeynfo' uses 'syd' (side) instead of 'side' (page) for Page Info.
    - Current: `Sydeynfo`
    - Source: `title: Page Info — { $website }`
    - Suggest: `Side-ynfo`
    - In Frisian, 'page' is 'side', while 'syd' means side, as in 'sydbalke' (sidebar). 'Sydeynfo' is a misspelling of Page Info.
- `policy-ManagedBookmarks` — `browser/browser/policies/policies-descriptions.ftl` — wizige wurde kin → wizige wurde kinne
    - Current: `wizige wurde kin`
    - Source: `Configures a list of bookmarks managed by an administrator that cannot be changed by the user.`
    - Suggest: `wizige wurde kinne`
- `connection-proxy-autologin-checkbox` — `browser/browser/preferences/connection.ftl` — automatisysk → automatysk; derfaor → derfoar
    - Current: `automatisysk`
    - Source: `accesskey: i label: Do not prompt for authentication if password is saved tooltiptext: This option silently authenticates you to proxies when you have saved credentials for them. You will be prompted if authentication f…`
    - Suggest: `automatysk`
- `browsing-use-full-keyboard-navigation` — `browser/browser/preferences/preferences.ftl` — formulierbesjoeringseleminten → formulierbestjoeringseleminten
    - Current: `formulierbesjoeringseleminten`
    - Source: `accesskey: t label: Use the tab key to move focus between form controls and links`
    - Suggest: `formulierbestjoeringseleminten`
- `data-collection-usage-ping` — `browser/browser/preferences/preferences.ftl` — ferstjoerd → ferstjoere
    - Current: `ferstjoerd`
    - Source: `accesskey: u description: This helps { -vendor-short-name } to estimate active users. label: Send daily usage ping to { -vendor-short-name }`
    - Suggest: `ferstjoere`
- `download-private-browsing-delete2` — `browser/browser/preferences/preferences.ftl` — Stray út: fan priveefinsters út by sluten → fan priveefinsters by sluten
    - Current: `fan priveefinsters út by sluten`
    - Source: `accesskey: D label: Delete private window downloads on close`
    - Suggest: `fan priveefinsters by sluten`
- `preferences-doh-manage-exceptions` — `browser/browser/preferences/preferences.ftl` — Utsûndering → Utsûnderingen
    - Current: `Utsûndering`
    - Source: `accesskey: x label: Manage Exceptions…`
    - Suggest: `Utsûnderingen`
- `preferences-etp-status-header` — `browser/browser/preferences/preferences.ftl` — 'wylst it sneupen' is ungrammatical because the conjunction 'wylst' needs a clause.
    - Current: `wylst it sneupen`
    - Source: `description: Sites use trackers to follow you online and show creepy ads. { -brand-short-name } shields you as you browse, blocking trackers automatically so you’re in control of your digital trail. label: Enhanced Trac…`
    - Suggest: `wylst jo sneupe`
    - 'wylst' (while) introduces a subordinate clause with a finite verb. It can't be followed by a nominalised infinitive.
- `search-suggestions-cant-show-2` — `browser/browser/preferences/preferences.ftl` — lokaasjebalkresultaten → lokaasjebalkeresultaten
    - Current: `lokaasjebalkresultaten`
    - Source: `message: Search suggestions will not be shown in location bar results because you have configured { -brand-short-name } to never remember history.`
    - Suggest: `lokaasjebalkeresultaten`
- `sitedata-cookies-exceptions3` — `browser/browser/preferences/preferences.ftl` — hoe → hoe’t
    - Current: `hoe`
    - Source: `accesskey: x description: Choose how specific sites handle cookies and site data. label: Manage exceptions`
    - Suggest: `hoe’t`
- `spellcheck-promo` — `browser/browser/preferences/preferences.ftl` — staveringhifkjen → staveringshifkjen
    - Current: `staveringhifkjen`
    - Source: `heading: How to use spell checking message: Right-click a text field to turn spell check on or off or to change the language. Not all fields support spell check.`
    - Suggest: `staveringshifkjen`
- `sync-signedin-login-failure` — `browser/browser/preferences/preferences.ftl` — om wer te ferbinen { $email } → om { $email } wer te ferbinen
    - Current: `om wer te ferbinen { $email }`
    - Source: `Please sign in to reconnect { $email }`
    - Suggest: `om { $email } wer te ferbinen`
- `tracking-manage-exceptions` — `browser/browser/preferences/preferences.ftl` — Utsûndering → Utsûnderingen
    - Current: `Utsûndering`
    - Source: `accesskey: x label: Manage Exceptions…`
    - Suggest: `Utsûnderingen`
- `delete-profile-autofill` — `browser/browser/profiles.ftl` — Same; also betelmetoaden vs Betellingsmetoaden elsewhere
    - Current: `betelmetoaden`
    - Source: `Autofill data (addresses, payment methods)`
    - Suggest: `Betellingsmetoaden`
- `item-cached-content-with-size` — `browser/browser/sanitize.ftl` — Tydlik buffere → Tydlike buffere
    - Current: `Tydlik buffere`
    - Source: `accesskey: f label: Temporary cached files and pages ({ $amount } { $unit })`
    - Suggest: `Tydlike buffere`
- `tab-context-close-n-tabs` — `browser/browser/tabContextMenu.ftl` — sluten (participle) → slute
    - Current: `sluten`
    - Source: `accesskey: C label: {$tabCount ->} [1] Close Tab [other] Close { $tabCount } Tabs`
    - Suggest: `slute`
- `tab-group-preview-closed-description` — `browser/browser/tabbrowser.ftl` — Ljepblêdelist → Ljepblêdlist
    - Current: `Ljepblêdelist`
    - Source: `Tabs list closed`
    - Suggest: `Ljepblêdlist`
- `tab-group-preview-open-description` — `browser/browser/tabbrowser.ftl` — Ljepblêdelist → Ljepblêdlist
    - Current: `Ljepblêdelist`
    - Source: `Tabs list open`
    - Suggest: `Ljepblêdlist`
- `tabbrowser-context-unmute-selected-tabs` — `browser/browser/tabbrowser.ftl` — Ljepblêd dempe/dôvje opheffe (verb on verb) → Dempen fan ljepblêd opheffe
    - Source: `accesskey: m label: Unmute Tabs`
    - Suggest: `Dempen fan ljepblêd opheffe`
- `tabbrowser-context-unmute-tab` — `browser/browser/tabbrowser.ftl` — Ljepblêd dempe/dôvje opheffe (verb on verb) → Dempen fan ljepblêd opheffe
    - Source: `accesskey: m label: Unmute Tab`
    - Suggest: `Dempen fan ljepblêd opheffe`
- `tabbrowser-manager-unmute-tab` — `browser/browser/tabbrowser.ftl` — Ljepblêd dempe/dôvje opheffe (verb on verb) → Dempen fan ljepblêd opheffe
    - Source: `tooltiptext: Unmute tab`
    - Suggest: `Dempen fan ljepblêd opheffe`
- `tabbrowser-tab-audio-playing-description` — `browser/browser/tabbrowser.ftl` — Lûd ôfspylje (imperative) → Lûd wurdt ôfspile
    - Current: `Lûd ôfspylje`
    - Source: `Playing audio`
    - Suggest: `Lûd wurdt ôfspile`
- `tabbrowser-unmute-tab-audio-aria-label` — `browser/browser/tabbrowser.ftl` — Ljepblêd dempe/dôvje opheffe (verb on verb) → Dempen fan ljepblêd opheffe
    - Source: `aria-label: Unmute tab`
    - Suggest: `Dempen fan ljepblêd opheffe`
- `taskbar-tab-audio-unmute` — `browser/browser/taskbartabs.ftl` — Ljepblêd dempe/dôvje opheffe (verb on verb) → Dempen fan ljepblêd opheffe
    - Source: `tooltiptext: Unmute Tab`
    - Suggest: `Dempen fan ljepblêd opheffe`
- `manifest-json-link-data-url` — `devtools/client/application.ftl` — ynbed → ynbêde
    - Current: `ynbed`
    - Source: `The manifest is embedded in a Data URL.`
    - Suggest: `ynbêde`
- `styleeditor-new-button` — `devtools/client/styleeditor.ftl` — in nije stylblêd → in nij stylblêd
    - Current: `in nije stylblêd`
    - Source: `accesskey: N tooltiptext: Create and append a new style sheet to the document`
    - Suggest: `in nij stylblêd`
- `toolbox-mode-parent-process-container` — `devtools/client/toolbox.ftl` — Allinne → Allinnich
    - Current: `Allinne`
    - Source: `title: Only focus on resources from the parent process.`
    - Suggest: `Allinnich`
- `dom-manifest-scope-not-same-origin` — `dom/dom/manifest.ftl` — 'deselfe' is misspelled; the Frisian form is 'deselde'.
    - Current: `deselfe`
    - Source: `The scope URL must be same origin as document.`
    - Suggest: `deselde`
    - 'Deselde' is the correct Frisian word. The neighbouring strings use it, so 'deselfe' reads as a mix of Dutch and Frisian.
- `SEC_ERROR_CRL_INVALID_VERSION` — `security/manager/chrome/pipnss/nsserrors.properties` — Typo in 'Sertifikaateerroppingslist'.
    - Current: `Sertifikaateerroppingslist`
    - Source: `Issuer’s Certificate Revocation List has an unknown version number.`
    - Suggest: `Sertifikaatwerroppingslist`
    - The word should be 'werroppingslist'. The same string in nsserrors.ftl spells it correctly.
- `delete-user-cert-impact` — `security/manager/security/certificates/certManager.ftl` — ydentifisearjen → identifisearjen
    - Current: `ydentifisearjen`
    - Source: `If you delete one of your own certificates, you can no longer use it to identify yourself.`
    - Suggest: `identifisearjen`
- `set-password-message` — `security/manager/security/pippki/pippki.ftl` — Typo 'reserverkopybestân' instead of 'reservekopybestân'.
    - Current: `reserverkopybestân`
    - Source: `The certificate backup password you set here protects the backup file that you are about to create. You must set this password to proceed with the backup.`
    - Suggest: `reservekopybestân`
    - The word for backup is 'reservekopy', which is spelled correctly earlier in the same string. The extra 'r' is a spelling error.
- `detail-show-preferences` — `toolkit/toolkit/about/aboutAddons.ftl` — fan dizze add-ons → fan dizze add-on (plural for a single add-on; both platform variants)
    - Current: `fan dizze add-ons`
    - Source: `accesskey: {$sel_1 ->} [windows] O [other] P label: {$sel_1 ->} [windows] Options [other] Preferences tooltiptext: {$sel_1 ->} [windows] Change this add-on’s options [other] Change this add-on’s preferences`
    - Suggest: `fan dizze add-on`
- `about-glean-about-data-list-item-debug-ping-viewer` — `toolkit/toolkit/about/aboutGlean.ftl` — live-barresstream → live-barrensstream
    - Source: `To browse debug tags, see full pings, see a live event stream, or view metric visualizations, please consult the <a data-l10n-name="glean-debug-ping-viewer">{ glean-debug-ping-viewer-brand-name }</a>.`
- `about-pdf-dropzone-error-generic` — `toolkit/toolkit/about/aboutPDF.ftl` — De oplaad → It opladen
    - Current: `De oplaad`
    - Source: `The upload didn’t go through. Try again later.`
    - Suggest: `It opladen`
- `about-reader-load-error` — `toolkit/toolkit/about/aboutReader.ftl` — Artikel fan side laden is mislearre → Laden fan artikel fan side is mislearre
    - Current: `Artikel fan side laden is mislearre`
    - Source: `Failed to load article from page`
    - Suggest: `Laden fan artikel fan side is mislearre`
- `about-translations-feature-blocked-info-message` — `toolkit/toolkit/about/aboutTranslations.ftl` — om dizze brûken te gean → om dizze te brûken
    - Current: `om dizze brûken te gean`
    - Source: `heading: To translate text, unblock this feature message: It looks like you updated AI controls to block this feature. Unblock any time to start using it.`
    - Suggest: `om dizze te brûken`
- `about-webauthn-auth-info-preferred-platform-uv-attempts` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Mis-bracketed compound
    - Source: `Preferred platform user verification attempts`
- `about-webauthn-confirm-deletion-label` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Jo geane fuortsmite: → Jo steane op it punt om te fuortsmiten:
    - Current: `Jo geane fuortsmite:`
    - Source: `You are about to delete:`
    - Suggest: `Jo steane op it punt om te fuortsmiten:`
- `download-ui-confirm-quit-cancel-downloads` — `toolkit/toolkit/downloads/downloadUI.ftl` — Singular verb+noun in the plural branch
    - Source: `{$downloadsCount ->} [1] If you exit now, 1 download will be canceled. Are you sure you want to exit? [other] If you exit now, { $downloadsCount } downloads will be canceled. Are you sure you want to exit?`
- `cert-error-inadequate-cert-type` — `toolkit/toolkit/neterror/certError.ftl` — Verb cluster garbled
    - Source: `{ -brand-short-name } blocked your visit to this site because the certificate provided for { $hostname } isn’t allowed to be used by a web server.`
- `cert-error-trust-expired-issuer` — `toolkit/toolkit/neterror/certError.ftl` — útjousertifikaat → útjouwerssertifikaat
    - Current: `útjousertifikaat`
    - Source: `The certificate is not trusted because the issuer certificate has expired.`
    - Suggest: `útjouwerssertifikaat`
- `cert-error-trust-untrusted-issuer` — `toolkit/toolkit/neterror/certError.ftl` — útjousertifikaat → útjouwerssertifikaat
    - Current: `útjousertifikaat`
    - Source: `The certificate is not trusted because the issuer certificate is not trusted.`
    - Suggest: `útjouwerssertifikaat`
- `sec-error-not-a-recipient` — `toolkit/toolkit/neterror/nsserrors.ftl` — privekaai → priveekaai
    - Current: `privekaai`
    - Source: `Cannot decrypt: you are not a recipient, or matching certificate and private key not found.`
    - Suggest: `priveekaai`
- _…and 3 more; see `state/` for the full list._

### D. Terminology, register & consistency

- `navbar-home` — `browser/browser/browser.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `label: Home tooltiptext: { -brand-short-name } Home Page`
    - Suggest: `Begjinside`
- `newtab-stocks-watchlist-full` — `browser/browser/newtab/newtab.ftl` — "Remove" is translated as "Ferwiderje" here while the sibling watchlist strings use "fuortsmite".
    - Current: `Ferwiderje ien om in oare ta te foegjen.`
    - Source: `{$limit ->} [one] You can add up to { $limit } stock. Remove one to add another. [other] You can add up to { $limit } stocks. Remove one to add another.`
    - Suggest: `Smyt ien fuort om in oare ta te foegjen.`
    - Same surface (stocks watchlist) uses "fuortsmite" for Remove in newtab-stocks-remove-from-watchlist and -removed-from-watchlist; "Ferwiderje" is inconsistent and not the Frisian standard term.
- `home-homepage-title` — `browser/browser/preferences/preferences.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `label: Homepage`
    - Suggest: `Begjinside`
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
- `security-privacy-issue-warning-doh` — `browser/browser/preferences/preferences.ftl` — Network provider — netwurkbehearder (administrator) vs ynternetoanbieder: security-privacy-issue-warning-doh, security-privacy-issue-warning-ech (vs their -doh2/-ech2 variants).
    - Current: `netwurkbehearder`
    - Source: `description: DNS over HTTPS hides what sites you visit from your network provider. label: DNS over HTTPS is disabled`
    - Suggest: `ynternetoanbieder`
- `security-privacy-issue-warning-ech` — `browser/browser/preferences/preferences.ftl` — Network provider — netwurkbehearder (administrator) vs ynternetoanbieder: security-privacy-issue-warning-doh, security-privacy-issue-warning-ech (vs their -doh2/-ech2 variants).
    - Current: `netwurkbehearder`
    - Source: `description: Encrypted Client Hello hides what sites you visit from your network provider. label: Encrypted Client Hello is disabled`
    - Suggest: `ynternetoanbieder`
- `PermissionsPolicyUnsupportedFeatureName` — `dom/chrome/security/security.properties` — "Permissions Policy" is rendered as "Machtigingenbelied" here but as "machtigingsbelied" in dom.properties, an inconsistent term for the same spec name.
    - Current: `Machtigingenbelied`
    - Source: `Permissions Policy: Skipping unsupported feature name “%S”.`
    - Suggest: `Machtigingsbelied`
    - Same en-US term "Permissions Policy" rendered two different ways across related console messages.
- `addon-detail-homepage-label` — `toolkit/toolkit/about/aboutAddons.ftl` — Homepage — Startside vs Begjinside: home-homepage-title.label, detail-home.label, addon-detail-homepage-label, navbar-home (label vs tooltiptext), toolbar-drop-on-home-msg vs -multiple.
    - Current: `Startside`
    - Source: `Homepage`
    - Suggest: `Begjinside`

### E. Typography, punctuation & spacing

- `about-logins-import-report-description2` — `browser/browser/aboutLogins.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `Passwords imported to { -brand-short-name }.`
- `about-logins-import-report-error` — `browser/browser/aboutLogins.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `{$count ->} [other] <div data-l10n-name="count">{ $count }</div> <div data-l10n-name="details">Errors</div> <div data-l10n-name="not-imported">(not imported)</div>`
- `popup-show-popup-menuitem` — `browser/browser/browser.ftl` — rights-webservices-term-4 ("as-is") · protections-vpn-banner-content (TechRadar quote in "…") · popup-show-popup-menuitem.label (uses “…” where the adjacent popup-trigger-redirect-menuitem uses ‘…’).
    - Source: `label: Show “{ $popupURI }”`
    - Suggest: `"as-is"`
- `redirect-warning-with-popup-message` — `browser/browser/browser.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `{$popupCount ->} [0] { -brand-short-name } prevented this site from redirecting. [1] { -brand-short-name } prevented this site from opening a pop-up window and redirecting. [other] { -brand-short-name } prevented this s…`
- `main-context-menu-bookmark-page` — `browser/browser/browserContext.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
    - Source: `accesskey: m aria-label: Bookmark Page… tooltiptext: Bookmark page`
- `main-context-menu-bookmark-page-2` — `browser/browser/browserContext.ftl` — Tooltip text has an ellipsis that the source does not have.
    - Current: `tooltiptext: Blêdwizer foar side meitsje…`
    - Source: `aria-label: Bookmark Page… tooltiptext: Bookmark page`
    - Suggest: `tooltiptext: Blêdwizer foar side meitsje`
    - en-US tooltiptext is "Bookmark page" without ellipsis; only the aria-label has one.
- `main-context-menu-edit-bookmark` — `browser/browser/browserContext.ftl` — Added where en-US has none: add-engine-button (both search.ftl and preferences/addEngine.ftl) · quickactions-plugins · main-context-menu-bookmark-page.tooltiptext · main-context-menu-edit-bookmark.tooltiptext.
    - Source: `accesskey: m aria-label: Edit Bookmark… tooltiptext: Edit bookmark`
- `main-context-menu-edit-bookmark-2` — `browser/browser/browserContext.ftl` — Tooltip adds an ellipsis that the source does not have.
    - Current: `tooltiptext: Blêdwizer bewurkje…`
    - Source: `aria-label: Edit Bookmark… tooltiptext: Edit bookmark`
    - Suggest: `tooltiptext: Blêdwizer bewurkje`
    - The en-US tooltiptext is "Edit bookmark" without ellipsis (only the aria-label has one).
- `sidebar-customization-callout-1-subtitle` — `browser/browser/featureCallout.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `The { -brand-product-name } sidebar gives you quick access to your browsing history, tabs from other devices, and an AI chatbot — all without leaving your main view.`
- `splitview-onboarding-callout-subtitle-2` — `browser/browser/featureCallout.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `No extra windows. No tab flipping. Right-click this tab and choose “Add Split View.”`
- `ipprotection-locations-subview-promo` — `browser/browser/ipProtection.ftl` — ipprotection-locations-subview-promo.message (mear as300) · support-remote-experiments-see-about-studies (missing space before the placeable) · about-logging-unknown-error (bard :) · download-ui-confirm-quit-cancel-downloads-mac (stopje ,) · about-httpsonly-explanation-continue (útskeakele .) · experimental-features-custom-wallpaper-description (Nij-ljepblêdside .) · plus the 47 doubled-space str…
    - Source: `heading: Take protection further with { -mozilla-vpn-brand-name } message: Choose from 300+ locations and protect all your apps on up to 5 devices.`
    - Suggest: `mear as300`
- `ipprotection-message-bandwidth-warning` — `browser/browser/ipProtection.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `heading: Getting close to your VPN limit message: You have { $usageLeft } GB of { $maxUsage } GB left this month.`
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `accesskey: S label: Share Ideas and Feedback…`
- `migration-chrome-windows-password-import-step1` — `browser/browser/migrationWizard.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Open the main menu <img data-l10n-name="chrome-icon-3dots"/> and go to Passwords and Autofill > Google Password Manager.`
- `migration-safari-password-import-step2` — `browser/browser/migrationWizard.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Select the <img data-l10n-name="safari-icon-3dots"/> button and choose “Export All Passwords”`
- `newtab-label-source-read-time` — `browser/browser/newtab/newtab.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `{ $source } · { $timeToRead } min`
- `no-page-title` — `browser/browser/pageInfo.ftl` — Dropped: no-page-title.value.
    - Source: `value: Untitled Page:`
- `choose-language-description` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `Choose your preferred language for displaying pages`
- `download-always-ask-where2` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `accesskey: A label: Ask where to save files before downloading`
- `extension-controlled-enable` — `browser/browser/preferences/preferences.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `To enable the extension go to <img data-l10n-name="addons-icon"/> Add-ons in the <img data-l10n-name="menu-icon"/> menu.`
- `forms-master-pw-change` — `browser/browser/preferences/preferences.ftl` — Dropped where en-US has one: menu-help-share-ideas.label · home-mode-choice-custom.label · home-mode-choice-custom-srd.label · forms-master-pw-change.label.
    - Source: `accesskey: M label: Change Master Password…`
- `preferences-doh-status-item-not-active` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `message: DNS over HTTPS is not working because we encountered an error ({ $reason }) while trying to use the provider { $name }`
- `preferences-doh-status-item-not-active-local` — `browser/browser/preferences/preferences.ftl` — appmenuitem-monitor-description2 · bookmark-overlay-tags-empty-description.placeholder · choose-language-description · confirm-browser-language-change-description · download-always-ask-where2.label · home-prefs-weather-description · forms-master-pw-fips-desc · preferences-doh-status-item-not-active.message · preferences-doh-status-item-not-active-local.message · onboarding-refresh-import-title ·…
    - Source: `message: DNS over HTTPS is not working because we encountered an error ({ $reason }) while trying to use the local provider { $name }`
- `sync-mobile-promo` — `browser/browser/preferences/preferences.ftl` — about-logins-intro-import3, ipprotection-feature-introduction-link-text-privacy-3, ipprotection-site-settings-callout-subtitle, migration-chrome-windows-password-import-step1, migration-safari-password-import-step2, onboarding-gratitude-security-and-privacy-subtitle, onboarding-refresh-gratitude-subtitle, fxa-qrcode-pair-step2-signin, extension-controlled-enable, settings-translations-subpage-nev…
    - Source: `Download Firefox for <img data-l10n-name="android-icon"/> <a data-l10n-name="android-link">Android</a> or <img data-l10n-name="ios-icon"/> <a data-l10n-name="ios-link">iOS</a> to sync with your mobile device.`
- `tab-group-menu-closed-tab-group` — `browser/browser/tabbrowser.ftl` — page-info-page, page-info-frame, tabbrowser-container-tab-title use - where the locale's house dash is – · tab-group-menu-closed-tab-group uses — while sibling tab-group strings use – · aboutdialog-update-downloading uses – while settings-update-downloading uses —.
    - Source: `label: { $tabGroupName } title: { $tabGroupName } — Closed`
- `third-party-tag-background` — `toolkit/toolkit/about/aboutThirdParty.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `(value): Background title: This module did not block the application because it was loaded in the background.`
- `download-ui-confirm-quit-title` — `toolkit/toolkit/downloads/downloadUI.ftl` — There is a double space before the brand name in the [other 1] variant.
    - Current: `stopje en  { -brand-short-name }`
    - Source: `{$sel_1, downloadsCount ->} [windows 1] Stop 1 download and exit { -brand-short-name }? [windows other] Stop { $downloadsCount } downloads and exit { -brand-short-name }? [other 1] Stop 1 download and quit { -brand-shor…`
    - Suggest: `stopje en { -brand-short-name }`
    - The extra space appears in the dialog title that users see; the other variants use a single space.
- `fp-neterror-offline-intro-2` — `toolkit/toolkit/neterror/netError.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `{ -brand-short-name } can’t connect to the server at <strong>{ $hostname }</strong>.`
- `sec-error-no-key` — `toolkit/toolkit/neterror/nsserrors.ftl` — pippki-reset-password-confirmation-message · add-exception-invalid-header · monitor-header-content-signed-in · profiler-popup-presets-networking-with-logs-description · perftools-presets-networking-with-logs-description · spotlight-focus-promo-subtitle · firefoxview-tabpickup-description · redirect-warning-with-popup-message · ipprotection-locations-subview-promo.message · ipprotection-message-ba…
    - Source: `The private key for this certificate cannot be found in key database`

---

## 4. Appendix

### Dismissed by hand (26)

- `about-glean-metrics-table-settings-histograms-left-padding` — `toolkit/toolkit/about/aboutGlean.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `about-networking-ssl-tokens-restored` — `toolkit/toolkit/about/aboutNetworking.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The finding was likely wrong: this tree uses "ûnthâld" for "storage" (e.g. "Lokale ûnthâld" for Local Storage), so the original was already acceptable.
- `data-collection-run-studies` — `browser/browser/preferences/preferences.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `decoder-doctor-decode-error-message` — `browser/browser/browser.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `decoder-doctor-decode-warning-message` — `browser/browser/browser.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `expand-sidebar-on-hover` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `fxa-menu-sync-status-off` — `browser/browser/appmenu.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; likely reason (inferred): The original was probably already fine: the capitalised "Ut" follows the title-case "Off" in the source, and this tree writes capital Ú without its accent elsewhere ("Utwreidingen"), so lowercasing it to "út" wasn't wanted.
- `ipprotection-button-turn-vpn-off-1` — `browser/browser/ipProtection.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): Likely deliberate: strings in this batch consistently leave the accent off a capital first letter (Utskeakelje, Ofbylding, Unbetroubere, Untdek), so adding Ú breaks that pattern.
- `ipprotection-connection-status-blocked-error-description-1` — `browser/browser/ipProtection.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `newtab-picture-header-date` — `browser/browser/newtab/newtab.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): Likely deliberate: strings in this batch consistently leave the accent off a capital first letter (Ofbylding, Utskeakelje, Unbetroubere, Untdek), so adding Ô breaks that pattern.
- `newtab-picture-menu-show-photo2` — `browser/browser/newtab/newtab.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): Likely deliberate: strings in this batch consistently leave the accent off a capital first letter (Ofbylding, Utskeakelje, Unbetroubere, Untdek), so adding Ô breaks that pattern.
- `newtab-picture-show-button2` — `browser/browser/newtab/newtab.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): Likely deliberate: strings in this batch consistently leave the accent off a capital first letter (Ofbylding, Utskeakelje, Unbetroubere, Untdek), so adding Ô breaks that pattern.
- `newtab-privacy-message-promo-monitor-1` — `browser/browser/newtab/newtab.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `newtab-shortcuts-highlight-title` — `browser/browser/newtab/newtab.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `onboarding-new-tabs-subtitle` — `browser/browser/newtab/onboarding.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `policy-DisableMacOSUserPolicies` — `browser/browser/policies/policies-descriptions.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `profiles-delete-profile-failed-message` — `toolkit/toolkit/about/aboutProfiles.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `protections-panel-not-found-label` — `browser/browser/protectionsPanel.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `protections-vpn-banner-content` — `browser/browser/protections.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `restart-required-unsaved-work-answer` — `browser/browser/aboutRestartRequired.ftl` — pontoon-rejected (2026-11-05): rejected in Pontoon without comment; reason unclear
- `security-technical-broken-encryption` — `browser/browser/pageInfo.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; likely reason (inferred): Likely deliberate: strings in this batch consistently leave the accent off a capital first letter (Unbetroubere, Utskeakelje, Ofbylding, Untdek), so adding Û breaks that pattern.
- `sidebar-context-menu-unpin-extension` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `sidebar-open-tools-from-sidebar` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `sidebar-resize-splitter` — `browser/browser/sidebar.ftl` — Sidebar — sydbalke vs sidebalke: sidebar-resize-splitter, sidebar-open-tools-from-sidebar, expand-sidebar-on-hover, sidebar-context-menu-unpin-extension (sidebar.ftl); sidebar-customization-callout-callout-button, -dismiss-button, sidebar-callout-survey- (featureCallout.ftl); genai-onboarding-description (genai.ftl); pdfjs-views-manager-sidebar (viewer.ftl)
- `spotlight-public-wifi-vpn-body` — `browser/browser/newtab/asrouter.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear
- `storage-tree-labels-local-storage` — `devtools/client/storage.ftl` — pontoon-rejected (2026-11-08): rejected in Pontoon without comment; reason unclear

_One line each in `locales/fy-NL/dismissed.txt`. Delete the line and the finding returns._

### Closed by the fixer (13)

- `aboutdialog-update-downloading` — `browser/browser/aboutDialog.ftl` — auto-suggest (2026-11-05, string 6e268c55): The translation uses the en dash (–), which is the measured fy-NL house dash (en 95 vs em 26).
- `add-exception-valid-long` — `security/manager/security/certificates/certManager.ftl` — auto-suggest (2026-11-05, string 0a1083c4): The double space between sentences is also present in the en-US source.
- `autofill-delete-payment-method-os-prompt-windows` — `toolkit/toolkit/formautofill/formAutofill.ftl` — auto-suggest (2026-11-05, string 6c642735): "bewarre betellingsgegevens" is an adequate rendering of "stored payment method information"; no meaning is changed.
- `console-timer-start` — `mobile/android/mobile/android/geckoViewConsole.ftl` — auto-suggest (2026-11-06, string 26e481e9): For 'starte' the Frisian past participle is 'start', so 'timer start' already means 'timer started'.
- `content-analysis-title` — `toolkit/toolkit/about/aboutSupport.ftl` — auto-suggest (2026-11-06, string c8afba9e): Standard Frisian spelling is 'analyze' (cf. 'analyzearje'), so 'Ynhâldsanalyze' is correct.
- `more-from-moz-solo-description` — `browser/browser/preferences/moreFromMozilla.ftl` — auto-suggest (2026-11-05, string 3e6a30cb): Here 'fergees' is used adverbially ('keppelje fergees'), where the uninflected form is correct; 'fergese' is the attributive inflected form.
- `opensearch-error-duplicate-desc` — `browser/browser/search.ftl` — auto-suggest (2026-11-05, string dbbbf446): The source itself says 'an engine', which 'in masine' renders faithfully.
- `opensearch-error-format-title` — `browser/browser/search.ftl` — auto-suggest (2026-11-05, string 4c1557cc): 'Net falide formaat' correctly means 'invalid format'; the suggestion is just a synonym.
- `permissions-block-popups-exceptions-button4` — `browser/browser/preferences/preferences.ftl` — auto-suggest (2026-11-05, string 354df7bf): This string already uses 'trochliedingen', which is the suggested term.
- `popup-trigger-redirect-menuitem` — `browser/browser/browser.ftl` — auto-suggest (2026-11-05, string e97aa29e): Curly single quotes are the measured fy-NL quote convention (875 uses).
- `speech-recognition-model-download-complete-message` — `browser/browser/permissions.ftl` — auto-suggest (2026-11-06, string 09282b37): In Frisian, 'downloade' is a class-1 weak verb, so its past participle is 'download' (like 'hearre' → 'heard'); the translation already states completion.
- `statePartiallyChecked` — `dom/chrome/accessibility/AccessFu.properties` — auto-suggest (2026-11-06, string 630b9c94): 'oanfinkt' is the past participle of the Frisian verb 'oanfinkje', so it is correct as a state description.
- `url-classifier-search-result-list` — `toolkit/toolkit/about/url-classifier.ftl` — auto-suggest (2026-11-06, string c29d7f23): 'List fan tabellen' is the normal Frisian rendering of 'List of tables'; 'fan' is correct here.

_The Pontoon suggestions workflow's model judged these wrong, or could not confirm them (`unreliable finding`); no person has decided. Each lapses when its string changes, and deleting its line in `locales/fy-NL/dismissed.txt` brings the finding back now._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (61)

- `addon-confirm-install-some-unsigned-message` — `browser/browser/addonNotifications.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `downloads-files-not-downloaded` — `browser/browser/downloads.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `genai-shortcuts-selected-warning-generic` — `browser/browser/genai.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `firefoxview-spotlight-promo-primarybutton` — `browser/browser/newtab/asrouter.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `fxa-menu-message-sync-devices-secondary-text2` — `browser/browser/newtab/asrouter.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `mr2022-onboarding-pin-image-alt` — `browser/browser/newtab/onboarding.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `return-to-amo-addon-title` — `browser/browser/newtab/onboarding.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `places-locked-prompt` — `browser/browser/places.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `security-browsing-protection` — `browser/browser/preferences/preferences.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `safeb-blocked-addon-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `safeb-blocked-unwanted-page-title` — `browser/browser/safebrowsing/blockedSite.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `screenshots-generic-error-title` — `browser/browser/screenshots.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `tabbrowser-confirm-caretbrowsing-message` — `browser/browser/tabbrowser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `tabbrowser-empty-private-tab-title` — `browser/browser/tabbrowser.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `about-debugging-setup-intro` — `devtools/client/aboutdebugging.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `css-compatibility-default-message` — `devtools/client/tooltips.ftl` — raised by `legacy`, withdrawn 2026-09-03
- `inactive-css-not-grid-or-flex-container-or-multicol-container` — `devtools/client/tooltips.ftl` — raised by `legacy`, withdrawn 2026-09-03

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (592)

- `restart-required-single-instance-answer-2` — `browser/browser/aboutRestartRequired.ftl` — fixed 2026-11-09
- `contextual-manager-passwords-delete-all-passwords-checkbox` — `browser/browser/contextual-manager.ftl` — fixed 2026-11-09
- `genai-more-actions-all-off-notice` — `browser/browser/genai.ftl` — fixed 2026-11-09
- `newtab-wallpaper-palm-trees` — `browser/browser/newtab/newtab.ftl` — fixed 2026-11-09
- `hnt-card-extensions-body` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `hnt-card-pin-body` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `tab-groups-onboarding-auto-saved-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-11-09
- `policy-DisableThirdPartyModuleBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-09
- `policy-OfferToSaveLoginsDefault` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-11-09
- `sync-engine-payment-methods3` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-09
- `sync-engine-tabs2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-09
- `sync-engine-tabs2` — `browser/browser/preferences/preferences.ftl` — fixed 2026-11-09
- `tab-context-close-duplicate-tabs-alt` — `browser/browser/tabContextMenu.ftl` — fixed 2026-11-09
- `options-stylesheet-autocompletion-tooltip` — `devtools/client/toolbox-options.ftl` — fixed 2026-11-09
- `about-processes-collapse-all-sites` — `toolkit/toolkit/about/aboutProcesses.ftl` — fixed 2026-11-09
- `sec-error-baggage-not-created` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-11-09
- `sec-error-crl-invalid-version` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-11-09
- `ssl-error-cipher-disallowed-for-version` — `toolkit/toolkit/neterror/nsserrors.ftl` — fixed 2026-11-09
- `elevation-finished-background-page` — `toolkit/toolkit/updates/elevation.ftl` — fixed 2026-11-09
- `settings-update-unsupported` — `browser/browser/aboutDialog.ftl` — fixed 2026-11-08
- `update-unsupported` — `browser/browser/aboutDialog.ftl` — fixed 2026-11-08
- `login-list-intro-description` — `browser/browser/aboutLogins.ftl` — fixed 2026-11-08
- `about-private-browsing-nova-info-subheader2` — `browser/browser/aboutPrivateBrowsing.ftl` — fixed 2026-11-08
- `restart-required-multiple-instances-answer` — `browser/browser/aboutRestartRequired.ftl` — fixed 2026-11-08
- `restart-required-multiple-instances-question` — `browser/browser/aboutRestartRequired.ftl` — fixed 2026-11-08
- `restart-required-single-instance-answer-2` — `browser/browser/aboutRestartRequired.ftl` — fixed 2026-11-08
- `restore-page-list-header` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-11-08
- `restore-page-window-label` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-11-08
- `welcome-back-restore-some-label` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-11-08
- `addon-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — fixed 2026-11-08
- `addon-install-full-screen-blocked` — `browser/browser/addonNotifications.ftl` — fixed 2026-11-08
- `addon-local-install-error-incorrect-hash` — `browser/browser/addonNotifications.ftl` — fixed 2026-11-08
- `aiwindow-starter-browsing-compare` — `browser/browser/aiWindow.ftl` — fixed 2026-11-08
- `smartbar-placeholder` — `browser/browser/aiWindow.ftl` — fixed 2026-11-08
- `smart-window-opened-tabs-row-label` — `browser/browser/aiWindowContent.ftl` — fixed 2026-11-08
- `appmenu-remote-tabs-tabsnotsyncing` — `browser/browser/appmenu.ftl` — fixed 2026-11-08
- `profiler-popup-presets-ml-description` — `browser/browser/appmenu.ftl` — fixed 2026-11-08
- `smartwindow-group-tabs-all-sorted` — `browser/browser/autoTabGrouping.ftl` — fixed 2026-11-08
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — fixed 2026-11-08
- `backup-file-how-to-restore-header` — `browser/browser/backupSettings.ftl` — fixed 2026-11-08

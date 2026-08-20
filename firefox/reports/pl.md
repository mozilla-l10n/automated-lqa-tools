# Firefox l10n QA — pl

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `443328fa7930` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `443328fa7930` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,836 |

Findings are keyed by string id, never by line number. The locale is assessed against en-US only.

---

## Changes in this run

### 🆕 New findings (2)

- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
  - Current: `Zdarzenie klawisza jest niedostępne dla GTK2: key="%S" modifiers="%S" id="%S"`
  - The locale's quote convention is `polish-double` (1552 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
  - Current: `Zdarzenie klawisza jest niedostępne przy niektórych układach klawiatury: key="%S" modifiers="%S" id="%S"`
  - The locale's quote convention is `polish-double` (1552 occurrences).

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
| Files | 357 |
| Strings | 17,836 |
| Missing strings | 327 |
| Obsolete strings | 0 |
| Files absent from the locale | 3 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 2 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

**327 strings** are not translated yet, concentrated in:

- `browser/browser/aiWindow.ftl` — 159
- `browser/browser/aiWindowContent.ftl` — 80
- `browser/browser/aiFeatures.ftl` — 43
- `browser/browser/newtab/newtab.ftl` — 15
- `browser/browser/newtab/onboarding.ftl` — 13
- `browser/browser/preferences/containers.ftl` — 7
- `browser/browser/preferences/preferences.ftl` — 4
- `browser/browser/aboutPrivateBrowsing.ftl` — 3
- `toolkit/toolkit/about/aboutProcesses.ftl` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1
- `toolkit/toolkit/global/processTypes.ftl` — 1

**Files absent from the locale:**

- `browser/browser/aiFeatures.ftl`
- `browser/browser/aiWindow.ftl`
- `browser/browser/aiWindowContent.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 1552, `straight-double` 36, `german-double` 7, `curly-double` 2 | **polish-double** |
| apostrophe | `straight` 1 | **straight** |
| ellipsis | `char` 459 | **char** |
| dash | `em` 170, `en` 12 | **em** |
| nbsp | `total` 5383, `narrow` 3, `before-punctuation` 49, `space-before-punctuation` 21 | **total** |
| register | `informal` 79 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (81)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 12 |
| 2 | Wrong content (says something other than the English) | 33 |
| 3 | Degraded language (grammar, spelling, terminology) | 32 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

- `popup-warning-exceeded-message` — `browser/browser/browser.ftl` — A8. The [one] variant drops "more than": "…uniemożliwił tej witrynie otwarcie wyskakującego okna." → Suggest: "…otwarcie więcej niż { $popupCount } wyskakującego okna." (the [few]/[many] variants keep it).
  - Current: `[one]`
  - en-US: `[few]`
- `popup-warning-exceeded-with-redirect-message` — `browser/browser/browser.ftl` — A8. The [one] variant drops "more than": "…uniemożliwił tej witrynie otwarcie wyskakującego okna." → Suggest: "…otwarcie więcej niż { $popupCount } wyskakującego okna." (the [few]/[many] variants keep it).
  - Current: `[one]`
  - en-US: `[few]`
- `mr2022-onboarding-live-language-continue-in` — `browser/browser/newtab/onboarding.ftl` — `mr2022-onboarding-live-language-continue-in` drops ['appLanguage'], which en-US passes
  - Current: `Nie przełączaj języka`
  - en-US: `Continue in { $appLanguage }`
  - The string renders, but the value en-US shows the user -- a count, a name, a size -- never appears.
- `monitor-partial-breaches-title` — `browser/browser/protections.ftl` — A4. Selector changed from $numBreaches to $numBreachesResolved. That is defensible for Polish agreement, but the [one] variant then also drops the z { $numBreaches } part that both other variants and the source have. Current [one]: "{ $numBreachesResolved } wyciek jest oznaczony jako rozwiązany" → Suggest: "{ $numBreachesResolved } z { $numBreaches } wycieków jest oznaczony jako rozwiązany".
  - Current: `[one]`
  - en-US: `"{ $numBreachesResolved } z { $numBreaches } wycieków jest oznaczony jako rozwiązany".`
- `protections-panel-cookie-banner-blocker-view-turn-on-for-site` — `browser/browser/protectionsPanel.ftl` — `protections-panel-cookie-banner-blocker-view-turn-on-for-site` references ['host'], which en-US does not pass
  - Current: `Włączyć blokowanie informacji o ciasteczkach na witrynie { $host }?`
  - en-US: `Turn on Cookie Banner Blocker for this site?`
  - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.
- `tab-group-editor-action-copy-links` — `browser/browser/tabbrowser.ftl` — A3, functional. The plural select keys on $tabCount, but the source (and the calling code) passes $linkCount. $tabCount is never supplied, so the selector cannot match and the message always falls through to [many] (and Fluent logs a resolver error). Current: { $tabCount -> [one] … [few] … [many] … } → Suggest: { $linkCount -> … }.
  - Current: `[many]`
  - en-US: `→ Suggest:`
- `state-dd-enabled` — `toolkit/toolkit/about/aboutPlugins.ftl` — A9, markup. Colon is inside the span and outside it, so the page renders "Stan:: włączony". Current: <span data-l10n-name="state">Stan:</span>: włączony → Suggest: <span data-l10n-name="state">Stan</span>: włączony (matching the three sibling state-dd- strings).
- `download-ui-cancel-downloads-ok` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
  - Current: `[1]`
  - en-US: `[other]`
- `download-ui-confirm-leave-private-browsing-windows-cancel-downloads` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
  - Current: `[1]`
  - en-US: `[other]`
- `download-ui-confirm-offline-cancel-downloads` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
  - Current: `[1]`
  - en-US: `[other]`
- `download-ui-confirm-quit-cancel-downloads` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
  - Current: `[1]`
  - en-US: `[other]`
- `download-ui-confirm-quit-cancel-downloads-mac` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
  - Current: `[1]`
  - en-US: `[other]`

### B. Mistranslation, reversed meaning, wrong names & brand

- `backup-file-intro` — `browser/browser/backupSettings.ftl` — lists the wrong data category: "zakładki, hasła i pozostałe dane" for "bookmarks, history, and other data". settings-data-backup-header2 in the same file has it right. → "zakładki, historię i pozostałe dane".
  - en-US: `"zakładki, historię i pozostałe dane".`
- `main-context-menu-link-send-to-device` — `browser/browser/browserContext.ftl` — dangling preposition: "Wyślij stronę do" / "Wyślij odnośnik do". → "Wyślij stronę na urządzenie" / "Wyślij odnośnik na urządzenie" (cf. main-context-menu-send-to-device-2).
- `main-context-menu-send-to-device` — `browser/browser/browserContext.ftl` — dangling preposition: "Wyślij stronę do" / "Wyślij odnośnik do". → "Wyślij stronę na urządzenie" / "Wyślij odnośnik na urządzenie" (cf. main-context-menu-send-to-device-2).
- `genai-settings-chat-lechat-links` — `browser/browser/genai.ftl` — "Mistral AI" is a company name and should not be translated. Current: "…zasady ochrony prywatności</a> sztucznej inteligencji Mistral." → Suggest: "…zasady ochrony prywatności</a> Mistral AI." (the sibling strings correctly keep OpenAI, Microsoft, Anthropic).
- `newtab-wallpaper-dark-green` — `browser/browser/newtab/newtab.ftl` — "Ciemnoniebieski" (= dark blue), duplicating newtab-wallpaper-dark-blue. → "Ciemnozielony".
  - en-US: `"Ciemnozielony".`
- `policy-ShowHomeButton` — `browser/browser/policies/policies-descriptions.ftl` — "przycisku strony domowej"; the product uses strona startowa everywhere else (including policy-Homepage in the same file). "Strona domowa" is reserved for add-on homepages in aboutAddons.ftl. → "przycisku strony startowej".
  - en-US: `"przycisku strony startowej".`
- `fxa-qrcode-pair-step1` — `browser/browser/preferences/fxaPairDevice.ftl` — narrows "mobile device" to "telefon", contradicting the dialog title (fxa-qrcode-pair-title = "…na telefonie lub tablecie"). → "…na urządzeniu mobilnym."
  - en-US: `"…na urządzeniu mobilnym."`
- `more-from-moz-solo-title` — `browser/browser/preferences/moreFromMozilla.ftl` — drops the "AI" qualifier present in en-US ("{ -solo-ai-brand-name } AI") and in the sibling more-from-moz-solo-title-2 ("Kreator SI stron internetowych…").
- `inactive-css-property-because-of-display` — `devtools/client/tooltips.ftl` — "ponieważ wyświetla { $display }" for "since it has a display of…". → "ponieważ jego własność display ma wartość { $display }".
  - Current: `{ $display }`
  - en-US: `display`
- `whypaused-assert` — `devtools/shared/debugger-paused-reasons.ftl` — "Wstrzymane na warunku" for "Paused on assertion"; warunek is a different debugger concept already used by whypaused-breakpoint-condition-thrown. → "Wstrzymane na asercji".
  - en-US: `"Wstrzymane na asercji".`
- `xslt-load-recursion` — `dom/dom/xslt.ftl` — the source ends with a colon because the offending stylesheet URI is appended; pl ends with a period, so the URI will follow a sentence-final dot. Siblings xslt-network-error, xslt-wrong-mime-type keep the colon. → end with ":".
  - en-US: `end with ":".`
- `config-new-pref-value-integer` — `mobile/android/mobile/android/aboutConfig.ftl` — "Liczba" for the specific Integer pref type; also collides with config-new-pref-number ("Wprowadź liczbę"). → "Liczba całkowita".
  - en-US: `"Liczba całkowita".`
- `network-connection-status-looked-up` — `netwerk/netwerk/necko.ftl` — breaks the Looking up / Looked up pair (rendered "Ustalanie adresu serwera" / "Odnaleziono"). → "Ustalono adres serwera { $host }…".
  - en-US: `"Ustalono adres serwera { $host }…".`
- `about-networking-networkid-status-known` — `toolkit/toolkit/about/aboutNetworking.ftl` — meaning reversed. "Stan łącza jest nieznany" for "Link status is known". It sits next to about-networking-networkid-is-up = "Łącze jest aktywne"; both are meant to be positive. → "Stan łącza jest znany".
  - en-US: `"Stan łącza jest znany".`
- `rights-webservices-term-5` — `toolkit/toolkit/about/aboutRights.ftl` — the damages enumeration lists "wyjątkowe" twice and includes the unfinished-looking "będące skutkiem czegoś" for "indirect, special, incidental, consequential, punitive, or exemplary". Needs a rewrite of the list.
- `media-audio-robustness` — `toolkit/toolkit/about/aboutSupport.ftl` — "Siła wideo" / "Siła dźwięku". EME robustness is the CDM security level. → "Poziom zabezpieczeń wideo" / "Poziom zabezpieczeń dźwięku".
- `media-video-robustness` — `toolkit/toolkit/about/aboutSupport.ftl` — "Siła wideo" / "Siła dźwięku". EME robustness is the CDM security level. → "Poziom zabezpieczeń wideo" / "Poziom zabezpieczeń dźwięku".
- `third-party-message-no-duration` — `toolkit/toolkit/about/aboutThirdParty.ftl` — "Nie nagrano" (audio/video sense) for "Not recorded". → "Nie zarejestrowano".
  - en-US: `"Nie zarejestrowano".`
- `about-webrtc-aec-logging-msg-label` — `toolkit/toolkit/about/aboutWebrtc.ftl` — the group comment says "AEC is an abbreviation for Acoustic Echo Cancellation", but pl renders it as redukcja szumów otoczenia (ambient-noise reduction), a different feature. about-webrtc-aec-logging-unavailable-sandbox in the same file already keeps "AEC", so the file is internally inconsistent. → "…usuwania echa akustycznego (AEC)".
  - en-US: `"…usuwania echa akustycznego`
- `abuse-report-unwanted-reason-v2` — `toolkit/toolkit/about/abuseReports.ftl` — "Samo się zainstalowało i nie wiem, jak je usunąć" for "I never wanted it and don't know how to get rid of it"; the self-installation claim duplicates abuse-report-unwanted-example. → "Nigdy tego nie chciałem(-am) i nie wiem, jak to usunąć".
  - en-US: `"Nigdy tego nie chciałem`
- `certificate-viewer-inc-locality` — `toolkit/toolkit/about/certviewer.ftl` — "Region" / "Region założenia" for X.509 L= (city/town), which also blurs the line with certificate-viewer-state-province = "Województwo". → "Miejscowość" / "Miejscowość założenia".
- `certificate-viewer-locality` — `toolkit/toolkit/about/certviewer.ftl` — "Region" / "Region założenia" for X.509 L= (city/town), which also blurs the line with certificate-viewer-state-province = "Województwo". → "Miejscowość" / "Miejscowość założenia".
- `experimental-features-cookie-samesite-none-requires-secure2` — `toolkit/toolkit/featuregates/features.ftl` — "wymaga atrybutu bezpieczeństwa"; the source means the literal Secure cookie attribute. → "wymaga atrybutu Secure".
  - Current: `Secure`
  - en-US: `"wymaga atrybutu Secure".`
- `user-context-color-purple` — `toolkit/toolkit/global/contextual-identity.ftl` — "Fioletowy", identical to user-context-color-violet; two container swatches become indistinguishable, notably for screen-reader users. → purple = "Purpurowy", keep violet = "Fioletowy".
  - en-US: `purple`
- `csp-error-illegal-host-wildcard` — `toolkit/toolkit/global/cspErrors.ftl` — "nieogólną domenę" for "non-generic sub-domain"; the sub-domain level is the whole point (.example.com vs .com). → "nieogólną poddomenę".
  - Current: `.com`
  - en-US: `"nieogólną poddomenę".`
- `language-name-ii` — `toolkit/toolkit/intl/languageNames.ftl` — "Syczuański" alone denotes Sichuanese Mandarin, a different language; the Yi/Nuosu qualifier identifies this entry. → "Yi syczuański".
  - en-US: `"Yi syczuański".`
- `language-name-meh` — `toolkit/toolkit/intl/languageNames.ftl` — the same Mesoamerican family term is handled three ways ("Południowo-zachodni Tlaxiaco Mixtec" / "Mixtepec Mixtec" / "Zapotecki Miahuatlán"): Mixtec is left in English in two entries while Zapotec is polonised in the third, and English modifier-noun order is kept. → one pattern, e.g. "Mikstecki z południowo-zachodniego Tlaxiaco" / "Mikstecki z Mixtepec" / "Zapotecki z Miahuatlán".
- `language-name-mix` — `toolkit/toolkit/intl/languageNames.ftl` — the same Mesoamerican family term is handled three ways ("Południowo-zachodni Tlaxiaco Mixtec" / "Mixtepec Mixtec" / "Zapotecki Miahuatlán"): Mixtec is left in English in two entries while Zapotec is polonised in the third, and English modifier-noun order is kept. → one pattern, e.g. "Mikstecki z południowo-zachodniego Tlaxiaco" / "Mikstecki z Mixtepec" / "Zapotecki z Miahuatlán".
- `language-name-zam` — `toolkit/toolkit/intl/languageNames.ftl` — the same Mesoamerican family term is handled three ways ("Południowo-zachodni Tlaxiaco Mixtec" / "Mixtepec Mixtec" / "Zapotecki Miahuatlán"): Mixtec is left in English in two entries while Zapotec is polonised in the third, and English modifier-noun order is kept. → one pattern, e.g. "Mikstecki z południowo-zachodniego Tlaxiaco" / "Mikstecki z Mixtepec" / "Zapotecki z Miahuatlán".
- `region-name-bq-2018` — `toolkit/toolkit/intl/regionNames.ftl` — judgment call. "Holandia" / "Holandia Karaibska"; the official Polish names per KSNG are "Niderlandy" / "Niderlandy Karaibskie". "Holandia" remains the dominant colloquial form, so this is a policy decision rather than an outright error.
- `region-name-nl` — `toolkit/toolkit/intl/regionNames.ftl` — judgment call. "Holandia" / "Holandia Karaibska"; the official Polish names per KSNG are "Niderlandy" / "Niderlandy Karaibskie". "Holandia" remains the dominant colloquial form, so this is a policy decision rather than an outright error.
- `netReset-title` — `toolkit/toolkit/neterror/certError.ftl` — "Przerwane połączenie", identical to netInterrupt-title; "connection was reset" and "connection was interrupted" collapse into one message. → "Połączenie zostało zresetowane".
  - en-US: `"Połączenie zostało zresetowane".`
- `pictureinpicture-unpip-btn` — `toolkit/toolkit/pictureinpicture/pictureinpicture.ftl` — "Wyłącz „Obraz w obrazie”" for Send back to tab / Back to tab; the button returns the video to its tab, it does not turn the feature off. The two distinct source values are also collapsed. → .aria-label = Odeślij z powrotem do karty, .tooltip = Z powrotem do karty.
  - en-US: `.aria-label = Odeślij z powrotem do karty`

### C. Grammar, agreement & spelling

- `refresh-blocked-redirect-label` — `browser/browser/browser.ftl` — "uniemożliwić" takes a noun phrase, not an infinitive. Current: "…uniemożliwił tej stronie automatycznie odświeżyć stronę." / "…automatycznie przekierować…" → Suggest: "…uniemożliwił automatyczne odświeżenie tej strony." / "…uniemożliwił tej stronie automatyczne przekierowanie do innej strony."
- `refresh-blocked-refresh-label` — `browser/browser/browser.ftl` — "uniemożliwić" takes a noun phrase, not an infinitive. Current: "…uniemożliwił tej stronie automatycznie odświeżyć stronę." / "…automatycznie przekierować…" → Suggest: "…uniemożliwił automatyczne odświeżenie tej strony." / "…uniemożliwił tej stronie automatyczne przekierowanie do innej strony."
- `cfr-doorhanger-extension-total-users` — `browser/browser/newtab/asrouter.ftl` — [few] = "{ $total } użytkowników"; 2/3/4 take the nominative plural. → [few] = "{ $total } użytkownicy" (the adjacent cfr-doorhanger-extension-rating handles this correctly).
  - Current: `[few]`
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — trailing space at the end of the first line of the multiline value ("Aktualizujesz system do Windows 11? "); Fluent preserves it. Same in psmerr-hostreusedissuerandserial (toolkit/toolkit/neterror/nsserrors.ftl), where en-US has no trailing space.
- `collection-usage-ping` — `browser/browser/preferences/preferences.ftl` — .label = "Wysyłaj dzienny sygnału o użyciu…" (adjective/noun case clash). The newer duplicate data-collection-usage-ping already has "dzienny sygnał". → "Wysyłaj dzienny sygnał o użyciu do…".
  - en-US: `"Wysyłaj dzienny sygnał o użyciu do…".`
- `safeb-blocked-unwanted-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — "ponieważ może one próbować" with a feminine singular subject ("ta strona"); the parallel malware/harmful strings use "może ona". → "ponieważ może ona próbować".
  - en-US: `"ponieważ może ona próbować".`
- `tab-group-label-tooltip-collapsed` — `browser/browser/tabbrowser.ftl` — the adjective refers to grupa (fem.): "— zamknięte", "— zwinięte", "— rozwinięte". The parallel tabbrowser-manager-closed-tab-group correctly uses "— zamknięta". → "— zamknięta", "— zwinięta", "— rozwinięta".
  - en-US: `"— zamknięta", "— zwinięta", "— rozwinięta".`
- `tab-group-label-tooltip-expanded` — `browser/browser/tabbrowser.ftl` — the adjective refers to grupa (fem.): "— zamknięte", "— zwinięte", "— rozwinięte". The parallel tabbrowser-manager-closed-tab-group correctly uses "— zamknięta". → "— zamknięta", "— zwinięta", "— rozwinięta".
  - en-US: `"— zamknięta", "— zwinięta", "— rozwinięta".`
- `tab-group-menu-closed-tab-group` — `browser/browser/tabbrowser.ftl` — the adjective refers to grupa (fem.): "— zamknięte", "— zwinięte", "— rozwinięte". The parallel tabbrowser-manager-closed-tab-group correctly uses "— zamknięta". → "— zamknięta", "— zwinięta", "— rozwinięta".
  - en-US: `"— zamknięta", "— zwinięta", "— rozwinięta".`
- `inactive-css-not-display-block-on-floated` — `devtools/client/tooltips.ftl` — "element to floated" is a word-for-word calque and not grammatical Polish ("floated" is an English adjective here, not a CSS keyword). → "…ponieważ element jest przestawiony (float)."
  - Current: `floated`
  - en-US: `float`
- `certmgr-begins-label` — `security/manager/security/certificates/certManager.ftl` — stray trailing colon on a tree column header: .label = "Ważny od dnia:"; the paired certmgr-expires-label has none. → "Ważny od dnia".
  - en-US: `"Ważny od dnia".`
- `permanent-override` — `security/manager/security/certificates/certManager.ftl` — the two values of one column mix an adverbial phrase and an adjective: "Na stałe" / "Tymczasowy". → "Stały" / "Tymczasowy" (both agreeing with wyjątek).
- `temporary-override` — `security/manager/security/certificates/certManager.ftl` — the two values of one column mix an adverbial phrase and an adjective: "Na stałe" / "Tymczasowy". → "Stały" / "Tymczasowy" (both agreeing with wyjątek).
- `protected-auth-alert` — `security/manager/security/pippki/pippki.ftl` — "uwierzytelnić się" governs "w" + locative. Current: "Proszę uwierzytelnić się do urządzenia zabezpieczającego…" / "…do tokenu „{ $tokenName }”." → Suggest: "…w urządzeniu zabezpieczającym ({ $tokenName })." / "…w tokenie „{ $tokenName }”."
  - en-US: `"…w urządzeniu zabezpieczającym`
- `protected-auth-prompt` — `security/manager/security/pippki/pippki.ftl` — "uwierzytelnić się" governs "w" + locative. Current: "Proszę uwierzytelnić się do urządzenia zabezpieczającego…" / "…do tokenu „{ $tokenName }”." → Suggest: "…w urządzeniu zabezpieczającym ({ $tokenName })." / "…w tokenie „{ $tokenName }”."
  - en-US: `"…w urządzeniu zabezpieczającym`
- `no-config-label` — `toolkit/crashreporter/aboutcrashes.ftl` — missing sentence-final period after <code>breakpad.reportURL</code>.
- `autofill-insecure-field-warning-description` — `toolkit/toolkit/formautofill/formAutofill.ftl` — missing sentence-final period after "…wypełnianie formularzy".
- `webext-perms-header-unsigned` — `toolkit/toolkit/global/extensions.ftl` — "Dodaj rozszerzanie jedynie…" (= expanding). Same typo in webext-perms-header-unsigned-with-perms, webext-perms-list-intro-unsigned and webext-site-perms-header-unsigned-with-perms. → "rozszerzenie".
  - en-US: `"rozszerzenie".`

### D. Terminology, register & consistency

- `newtab-sports-widget-round-16` — `browser/browser/newtab/newtab.ftl` — "Pierwsza runda" / "Druga runda" for "Round of 32" / "Round of 16"; Polish football usage names these by fraction, and the current wording is ambiguous against the preceding group stage. → "1/16 finału" / "1/8 finału".
- `newtab-sports-widget-round-32` — `browser/browser/newtab/newtab.ftl` — "Pierwsza runda" / "Druga runda" for "Round of 32" / "Round of 16"; Polish football usage names these by fraction, and the current wording is ambiguous against the preceding group stage. → "1/16 finału" / "1/8 finału".
- `media-count` — `browser/browser/pageInfo.ftl` — .label = "Ilość" for a count of discrete items; the locale uses "Liczba" elsewhere (processes-count, place-database-stats-count, "Liczba wizyt" in places.ftl). → "Liczba".
  - en-US: `"Liczba".`
- `storage-add-button` — `devtools/client/storage.ftl` — "Item" is "obiekt" here and in storage-context-menu-add-item / storage-refresh-button, but "element" in storage-search-box; "obiekt" also collides with the JS sense of object.
- `pkcs12-info-no-smartcard-backup` — `security/manager/security/certificates/certManager.ftl` — "inteligentna karta"; the established Polish term is "karta inteligentna".
- `pkcs12-unknown-err-backup` — `security/manager/security/certificates/certManager.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
  - en-US: `standardize on "kopia zapasowa".`
- `pkcs12-unknown-err-restore` — `security/manager/security/certificates/certManager.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
  - en-US: `standardize on "kopia zapasowa".`
- `unable-to-toggle-fips` — `security/manager/security/certificates/deviceManager.ftl` — the only occurrence of "urządzenie bezpieczeństwa" in the locale; everything else, including fips-nonempty-primary-password-required two entries above, says "urządzenie zabezpieczające".
- `set-password-backup-pw` — `security/manager/security/pippki/pippki.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
  - en-US: `standardize on "kopia zapasowa".`
- `set-password-repeat-backup-pw` — `security/manager/security/pippki/pippki.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
  - en-US: `standardize on "kopia zapasowa".`
- `set-password-window` — `security/manager/security/pippki/pippki.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
  - en-US: `standardize on "kopia zapasowa".`
- `enableSafeBrowsing-label` — `toolkit/toolkit/about/aboutRights.ftl` — quotes a preferences label verbatim, but with different wording: "Blokowanie niebezpiecznych i podejrzanych treści." vs the actual security-enable-safe-browsing = "Blokuj niebezpieczne i podejrzane treści."
- `about-telemetry-keyed-scalar-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — left in English ("Keyed scalars") while about-telemetry-scalar-section = "Skalary" and about-telemetry-keyed-histogram-section = "Indeksowane histogramy". → "Indeksowane skalary".
  - en-US: `"Indeksowane skalary".`
- `tabmodalprompt-username` — `toolkit/toolkit/global/tabprompts.ftl` — .value = "Użytkownik:"; the identical field in common-dialog-username is "Nazwa użytkownika". → "Nazwa użytkownika:".
  - en-US: `"Nazwa użytkownika:".`

### E. Typography, punctuation & spacing

- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
  - Current: `Zdarzenie klawisza jest niedostępne dla GTK2: key="%S" modifiers="%S" id="%S"`
  - The locale's quote convention is `polish-double` (1552 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
  - Current: `Zdarzenie klawisza jest niedostępne przy niektórych układach klawiatury: key="%S" modifiers="%S" id="%S"`
  - The locale's quote convention is `polish-double` (1552 occurrences).
- `plugins-openh264-description` — `toolkit/toolkit/about/aboutAddons.ftl` — stale URL "http://www.openh264.org"; the source uses "https://www.openh264.org/".
- `password-manager-update-password-message` — `toolkit/toolkit/passwordmgr/passwordmgr.ftl` — "hasło dla { $host }?" without quotes, while the sibling password-manager-save-password-message in the same doorhanger uses „{ $host }”.

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Resolved to date (126)

- `about-private-browsing-felt-privacy-v1-info-link` — `browser/browser/aboutPrivateBrowsing.ftl` — fixed 2026-08-06
- `about-private-browsing-nova-info-link` — `browser/browser/aboutPrivateBrowsing.ftl` — fixed 2026-08-06
- `error-long-desc1` — `browser/browser/aboutRobots.ftl` — fixed 2026-08-06
- `restore-page-try-this` — `browser/browser/aboutSessionRestore.ftl` — fixed 2026-08-06
- `crashed-include-URL-2` — `browser/browser/aboutTabCrashed.ftl` — fixed 2026-08-06
- `crashed-send-report-2` — `browser/browser/aboutTabCrashed.ftl` — fixed 2026-08-06
- `about-unloads-intro` — `browser/browser/aboutUnloads.ftl` — fixed 2026-08-06
- `appmenuitem-fxa-sync-off-description` — `browser/browser/appmenu.ftl` — fixed 2026-08-06
- `bookmarks-menu-button` — `browser/browser/browser.ftl` — fixed 2026-08-06
- `eme-notifications-drm-content-playing` — `browser/browser/browser.ftl` — fixed 2026-08-06
- `qrcode-copy-success` — `browser/browser/browser.ftl` — fixed 2026-08-06
- `toolbar-button-email-link` — `browser/browser/browser.ftl` — fixed 2026-08-06
- `toolbar-button-logins` — `browser/browser/browser.ftl` — fixed 2026-08-06
- `toolbar-button-save-page` — `browser/browser/browser.ftl` — fixed 2026-08-06
- `urlbar-serial-notification-anchor` — `browser/browser/browser.ftl` — fixed 2026-08-06
- `main-context-menu-bookmark-page-with-shortcut` — `browser/browser/browserContext.ftl` — fixed 2026-08-06
- `window-minimize-command` — `browser/browser/browserSets.ftl` — fixed 2026-08-06
- `content-sharing-modal-description-2` — `browser/browser/contentSharing.ftl` — fixed 2026-08-06
- `content-sharing-modal-description-signed-in` — `browser/browser/contentSharing.ftl` — fixed 2026-08-06
- `default-browser-guidance-notification-title` — `browser/browser/defaultBrowserNotification.ftl` — fixed 2026-08-06
- `default-browser-guidance-notification-v2-title` — `browser/browser/defaultBrowserNotification.ftl` — fixed 2026-08-06
- `default-browser-guidance-notification-v2-title-only` — `browser/browser/defaultBrowserNotification.ftl` — fixed 2026-08-06
- `firefoxview-recentlyclosed-empty-header` — `browser/browser/firefoxView.ftl` — fixed 2026-08-06
- `genai-shortcuts-selected-warning` — `browser/browser/genai.ftl` — fixed 2026-08-06
- `genai-shortcuts-selected-warning-generic` — `browser/browser/genai.ftl` — fixed 2026-08-06
- `identity-credential-policy-title` — `browser/browser/identityCredentialNotification.ftl` — fixed 2026-08-06
- `ipprotection-feature-introduction-link-text-privacy-1` — `browser/browser/ipProtection.ftl` — fixed 2026-08-06
- `windows-10-eos-feature-toast-whats-new-button` — `browser/browser/newtab/asrouter.ftl` — fixed 2026-08-06
- `newtab-privacy-modal-paragraph-2` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-06
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-06
- `newtab-sports-widget-pagination-dot` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-06
- `newtab-topic-selection-privacy-link` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-06
- `newtab-widget-lists-empty-cta` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-06
- `newtab-widget-timer-reset` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-06
- `create-backup-screen-1-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-06
- `mr2022-onboarding-colorway-description-activist` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-06
- `mr2022-onboarding-existing-pin-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-06
- `mr2022-onboarding-gratitude-primary-button-label` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-06
- `mr2022-onboarding-welcome-pin-subtitle` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-06
- `restore-from-backup-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-06

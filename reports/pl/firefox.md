# Firefox l10n QA — pl

| | |
|---|---|
| **Generated** | 2026-08-21 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `bd0ff4b2f741` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `60f24d17564f` |
| **Previous run** | 2026-08-21 @ `5cbe42651962` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 17,866 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for pl: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 357 |
| Strings | 17,866 |
| Missing strings | 314 |
| Obsolete strings | 0 |
| Files absent from the locale | 3 |
| Fluent / properties syntax errors | 0 |
| Variable & placeholder mismatches | 2 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| Strings marked untranslatable in the source | 0 |
| printf placeholder mismatches | 0 |
| Plural / select selector mismatches | 0 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 1 |
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

**314 strings** are not translated yet, concentrated in:

- `browser/browser/aiWindow.ftl` — 159
- `browser/browser/aiWindowContent.ftl` — 80
- `browser/browser/aiFeatures.ftl` — 43
- `browser/browser/newtab/onboarding.ftl` — 13
- `browser/browser/newtab/newtab.ftl` — 7
- `browser/browser/appmenu.ftl` — 2
- `browser/browser/menubar.ftl` — 2
- `browser/browser/sharePanel.ftl` — 2
- `browser/browser/preferences/preferences.ftl` — 2
- `browser/browser/aboutDialog.ftl` — 1
- `browser/browser/preferences/formAutofill.ftl` — 1
- `dom/chrome/accessibility/AccessFu.properties` — 1

**Files absent from the locale:**

- `browser/browser/aiFeatures.ftl`
- `browser/browser/aiWindow.ftl`
- `browser/browser/aiWindowContent.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 1560, `straight-double` 36, `german-double` 7, `curly-double` 2 | **polish-double** |
| apostrophe | `straight` 1 | **straight** |
| ellipsis | `char` 460 | **char** |
| dash | `em` 170, `en` 12 | **em** |
| nbsp | `total` 5389, `narrow` 3, `before-punctuation` 49, `space-before-punctuation` 21 | **total** |
| register | `informal` 79 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (83)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 13 |
| 2 | Wrong content (says something other than the English) | 37 |
| 3 | Degraded language (grammar, spelling, terminology) | 29 |
| 4 | Cosmetic (typography, spacing) | 4 |

### A. Functional, markup, variables & plurals

- `popup-warning-exceeded-message` — `browser/browser/browser.ftl` — A8. The [one] variant drops "more than": "…uniemożliwił tej witrynie otwarcie wyskakującego okna." → Suggest: "…otwarcie więcej niż { $popupCount } wyskakującego okna." (the [few]/[many] variants keep it).
    - Current: `[one]`
    - Source: `{$popupCount ->} [other] { -brand-short-name } prevented this site from opening more than { $popupCount } pop-up windows.`
    - Suggest: `[few]`
- `popup-warning-exceeded-with-redirect-message` — `browser/browser/browser.ftl` — A8. The [one] variant drops "more than": "…uniemożliwił tej witrynie otwarcie wyskakującego okna." → Suggest: "…otwarcie więcej niż { $popupCount } wyskakującego okna." (the [few]/[many] variants keep it).
    - Current: `[one]`
    - Source: `{$popupCount ->} [other] { -brand-short-name } prevented this site from opening more than { $popupCount } pop-up windows and redirecting.`
    - Suggest: `[few]`
- `mr2022-onboarding-live-language-continue-in` — `browser/browser/newtab/onboarding.ftl` — `mr2022-onboarding-live-language-continue-in` drops ['appLanguage'], which en-US passes
    - Current: `Nie przełączaj języka`
    - Source: `Continue in { $appLanguage }`
    - Suggest: `Continue in { $appLanguage }`
    - The string renders, but the value en-US shows the user -- a count, a name, a size -- never appears.
- `monitor-partial-breaches-title` — `browser/browser/protections.ftl` — A4. Selector changed from $numBreaches to $numBreachesResolved. That is defensible for Polish agreement, but the [one] variant then also drops the z { $numBreaches } part that both other variants and the source have. Current [one]: "{ $numBreachesResolved } wyciek jest oznaczony jako rozwiązany" → Suggest: "{ $numBreachesResolved } z { $numBreaches } wycieków jest oznaczony jako rozwiązany".
    - Current: `[one]`
    - Source: `{$numBreaches ->} [other] { $numBreachesResolved } out of { $numBreaches } breaches marked as resolved`
    - Suggest: `"{ $numBreachesResolved } z { $numBreaches } wycieków jest oznaczony jako rozwiązany".`
- `protections-panel-cookie-banner-blocker-view-turn-on-for-site` — `browser/browser/protectionsPanel.ftl` — `protections-panel-cookie-banner-blocker-view-turn-on-for-site` references ['host'], which en-US does not pass
    - Current: `Włączyć blokowanie informacji o ciasteczkach na witrynie { $host }?`
    - Source: `Turn on Cookie Banner Blocker for this site?`
    - Suggest: `Turn on Cookie Banner Blocker for this site?`
    - A variable the code does not pass renders as an empty string, so the sentence loses the value it was built around.
- `tab-group-editor-action-copy-links` — `browser/browser/tabbrowser.ftl` — A3, functional. The plural select keys on $tabCount, but the source (and the calling code) passes $linkCount. $tabCount is never supplied, so the selector cannot match and the message always falls through to [many] (and Fluent logs a resolver error). Current: { $tabCount -> [one] … [few] … [many] … } → Suggest: { $linkCount -> … }.
    - Current: `[many]`
    - Source: `label: {$linkCount ->} [1] Copy link in group [other] Copy { $linkCount } links in group`
    - Suggest: `→ Suggest:`
- `state-dd-enabled` — `toolkit/toolkit/about/aboutPlugins.ftl` — A9, markup. Colon is inside the span and outside it, so the page renders "Stan:: włączony". Current: <span data-l10n-name="state">Stan:</span>: włączony → Suggest: <span data-l10n-name="state">Stan</span>: włączony (matching the three sibling state-dd- strings).
    - Source: `<span data-l10n-name="state">State:</span> Enabled`
- `download-ui-cancel-downloads-ok` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
    - Current: `[1]`
    - Source: `{$downloadsCount ->} [1] Cancel 1 Download [other] Cancel { $downloadsCount } Downloads`
    - Suggest: `[other]`
- `download-ui-confirm-leave-private-browsing-windows-cancel-downloads` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
    - Current: `[1]`
    - Source: `{$downloadsCount ->} [1] If you close all Private Browsing windows now, 1 download will be canceled. Are you sure you want to leave Private Browsing? [other] If you close all Private Browsing windows now, { $downloadsCo…`
    - Suggest: `[other]`
- `download-ui-confirm-offline-cancel-downloads` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
    - Current: `[1]`
    - Source: `{$downloadsCount ->} [1] If you go offline now, 1 download will be canceled. Are you sure you want to go offline? [other] If you go offline now, { $downloadsCount } downloads will be canceled. Are you sure you want to g…`
    - Suggest: `[other]`
- `download-ui-confirm-quit-cancel-downloads` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
    - Current: `[1]`
    - Source: `{$downloadsCount ->} [1] If you exit now, 1 download will be canceled. Are you sure you want to exit? [other] If you exit now, { $downloadsCount } downloads will be canceled. Are you sure you want to exit?`
    - Suggest: `[other]`
- `download-ui-confirm-quit-cancel-downloads-mac` — `toolkit/toolkit/downloads/downloadUI.ftl` — A6, plural. All five use only [1] + [other] with "{ $downloadsCount } plików", so 2/3/4 render as "2 plików" instead of "2 pliki". Add a [few] variant to each.
    - Current: `[1]`
    - Source: `{$downloadsCount ->} [1] If you quit now, 1 download will be canceled. Are you sure you want to quit? [other] If you quit now, { $downloadsCount } downloads will be canceled. Are you sure you want to quit?`
    - Suggest: `[other]`
- `pdfjs-editor-comments-sidebar-title` — `toolkit/toolkit/pdfviewer/viewer.ftl` — `pdfjs-editor-comments-sidebar-title` is missing the ['few', 'many'] plural forms
    - Current: `{$count ->} [one] Komentarz [other] Komentarze`
    - Source: `{$count ->} [one] Comment [other] Comments`
    - Suggest: `{$count ->} [one] Comment [other] Comments`
    - This locale uses ['few', 'many', 'one'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.

### B. Mistranslation, reversed meaning, wrong names & brand

- `about-private-browsing-relay-promo-title` — `browser/browser/aboutPrivateBrowsing.ftl` — "when you sign up" mistranslated as "gdy się logujesz" (when you log in).
    - Current: `gdy się logujesz`
    - Source: `Hide your real address with an email mask when you sign up, shop, or share it online.`
    - Suggest: `gdy się rejestrujesz`
    - en-US "sign up" means creating an account (rejestracja), not signing in (logowanie).
- `backup-file-intro` — `browser/browser/backupSettings.ftl` — lists the wrong data category: "zakładki, hasła i pozostałe dane" for "bookmarks, history, and other data". settings-data-backup-header2 in the same file has it right. → "zakładki, historię i pozostałe dane".
    - Source: `Get back to browsing and recover all your bookmarks, history, and other data. <a data-l10n-name="backup-file-support-link">Learn more</a>`
    - Suggest: `"zakładki, historię i pozostałe dane".`
- `main-context-menu-link-send-to-device` — `browser/browser/browserContext.ftl` — dangling preposition: "Wyślij stronę do" / "Wyślij odnośnik do". → "Wyślij stronę na urządzenie" / "Wyślij odnośnik na urządzenie" (cf. main-context-menu-send-to-device-2).
    - Source: `accesskey: n label: Send Link to Device`
- `main-context-menu-send-to-device` — `browser/browser/browserContext.ftl` — dangling preposition: "Wyślij stronę do" / "Wyślij odnośnik do". → "Wyślij stronę na urządzenie" / "Wyślij odnośnik na urządzenie" (cf. main-context-menu-send-to-device-2).
    - Source: `accesskey: n label: Send Page to Device`
- `genai-settings-chat-lechat-links` — `browser/browser/genai.ftl` — "Mistral AI" is a company name and should not be translated. Current: "…zasady ochrony prywatności</a> sztucznej inteligencji Mistral." → Suggest: "…zasady ochrony prywatności</a> Mistral AI." (the sibling strings correctly keep OpenAI, Microsoft, Anthropic).
    - Source: `By choosing Le Chat Mistral, you agree to the Mistral AI <a data-l10n-name="link1">Terms of Service</a> and <a data-l10n-name="link2">Privacy Policy</a>.`
- `newtab-wallpaper-dark-green` — `browser/browser/newtab/newtab.ftl` — "Ciemnoniebieski" (= dark blue), duplicating newtab-wallpaper-dark-blue. → "Ciemnozielony".
    - Source: `Dark green`
    - Suggest: `"Ciemnozielony".`
- `policy-ShowHomeButton` — `browser/browser/policies/policies-descriptions.ftl` — "przycisku strony domowej"; the product uses strona startowa everywhere else (including policy-Homepage in the same file). "Strona domowa" is reserved for add-on homepages in aboutAddons.ftl. → "przycisku strony startowej".
    - Source: `Show the home button on the toolbar.`
    - Suggest: `"przycisku strony startowej".`
- `fxa-qrcode-pair-step1` — `browser/browser/preferences/fxaPairDevice.ftl` — narrows "mobile device" to "telefon", contradicting the dialog title (fxa-qrcode-pair-title = "…na telefonie lub tablecie"). → "…na urządzeniu mobilnym."
    - Source: `1. Open { -brand-product-name } on your mobile device.`
    - Suggest: `"…na urządzeniu mobilnym."`
- `more-from-moz-solo-title` — `browser/browser/preferences/moreFromMozilla.ftl` — drops the "AI" qualifier present in en-US ("{ -solo-ai-brand-name } AI") and in the sibling more-from-moz-solo-title-2 ("Kreator SI stron internetowych…").
    - Source: `{ -solo-ai-brand-name } AI`
- `inactive-css-property-because-of-display` — `devtools/client/tooltips.ftl` — "ponieważ wyświetla { $display }" for "since it has a display of…". → "ponieważ jego własność display ma wartość { $display }".
    - Current: `{ $display }`
    - Source: `<strong>{ $property }</strong> has no effect on this element since it has a display of <strong>{ $display }</strong>.`
    - Suggest: `display`
- `whypaused-assert` — `devtools/shared/debugger-paused-reasons.ftl` — "Wstrzymane na warunku" for "Paused on assertion"; warunek is a different debugger concept already used by whypaused-breakpoint-condition-thrown. → "Wstrzymane na asercji".
    - Source: `Paused on assertion`
    - Suggest: `"Wstrzymane na asercji".`
- `xslt-load-recursion` — `dom/dom/xslt.ftl` — the source ends with a colon because the offending stylesheet URI is appended; pl ends with a period, so the URI will follow a sentence-final dot. Siblings xslt-network-error, xslt-wrong-mime-type keep the colon. → end with ":".
    - Source: `An XSLT stylesheet directly or indirectly imports or includes itself:`
    - Suggest: `end with ":".`
- `config-new-pref-value-integer` — `mobile/android/mobile/android/aboutConfig.ftl` — "Liczba" for the specific Integer pref type; also collides with config-new-pref-number ("Wprowadź liczbę"). → "Liczba całkowita".
    - Source: `Integer`
    - Suggest: `"Liczba całkowita".`
- `network-connection-status-looked-up` — `netwerk/netwerk/necko.ftl` — breaks the Looking up / Looked up pair (rendered "Ustalanie adresu serwera" / "Odnaleziono"). → "Ustalono adres serwera { $host }…".
    - Source: `Looked up { $host }…`
    - Suggest: `"Ustalono adres serwera { $host }…".`
- `about-networking-networkid-status-known` — `toolkit/toolkit/about/aboutNetworking.ftl` — meaning reversed. "Stan łącza jest nieznany" for "Link status is known". It sits next to about-networking-networkid-is-up = "Łącze jest aktywne"; both are meant to be positive. → "Stan łącza jest znany".
    - Source: `Link status is known`
    - Suggest: `"Stan łącza jest znany".`
- `rights-webservices-term-5` — `toolkit/toolkit/about/aboutRights.ftl` — the damages enumeration lists "wyjątkowe" twice and includes the unfinished-looking "będące skutkiem czegoś" for "indirect, special, incidental, consequential, punitive, or exemplary". Needs a rewrite of the list.
    - Source: `<strong>Except as required by law, { -vendor-short-name }, its contributors, licensors, and distributors will not be liable for any indirect, special, incidental, consequential, punitive, or exemplary damages arising ou…`
- `media-audio-robustness` — `toolkit/toolkit/about/aboutSupport.ftl` — "Siła wideo" / "Siła dźwięku". EME robustness is the CDM security level. → "Poziom zabezpieczeń wideo" / "Poziom zabezpieczeń dźwięku".
    - Source: `Audio Robustness`
- `media-video-robustness` — `toolkit/toolkit/about/aboutSupport.ftl` — "Siła wideo" / "Siła dźwięku". EME robustness is the CDM security level. → "Poziom zabezpieczeń wideo" / "Poziom zabezpieczeń dźwięku".
    - Source: `Video Robustness`
- `third-party-message-no-duration` — `toolkit/toolkit/about/aboutThirdParty.ftl` — "Nie nagrano" (audio/video sense) for "Not recorded". → "Nie zarejestrowano".
    - Source: `Not recorded`
    - Suggest: `"Nie zarejestrowano".`
- `about-webrtc-aec-logging-msg-label` — `toolkit/toolkit/about/aboutWebrtc.ftl` — the group comment says "AEC is an abbreviation for Acoustic Echo Cancellation", but pl renders it as redukcja szumów otoczenia (ambient-noise reduction), a different feature. about-webrtc-aec-logging-unavailable-sandbox in the same file already keeps "AEC", so the file is internally inconsistent. → "…usuwania echa akustycznego (AEC)".
    - Source: `AEC Logging`
    - Suggest: `"…usuwania echa akustycznego`
- `abuse-report-unwanted-reason-v2` — `toolkit/toolkit/about/abuseReports.ftl` — "Samo się zainstalowało i nie wiem, jak je usunąć" for "I never wanted it and don't know how to get rid of it"; the self-installation claim duplicates abuse-report-unwanted-example. → "Nigdy tego nie chciałem(-am) i nie wiem, jak to usunąć".
    - Source: `I never wanted it and don’t know how to get rid of it`
    - Suggest: `"Nigdy tego nie chciałem`
- `certificate-viewer-inc-locality` — `toolkit/toolkit/about/certviewer.ftl` — "Region" / "Region założenia" for X.509 L= (city/town), which also blurs the line with certificate-viewer-state-province = "Województwo". → "Miejscowość" / "Miejscowość założenia".
    - Source: `Inc. Locality`
- `certificate-viewer-locality` — `toolkit/toolkit/about/certviewer.ftl` — "Region" / "Region założenia" for X.509 L= (city/town), which also blurs the line with certificate-viewer-state-province = "Województwo". → "Miejscowość" / "Miejscowość założenia".
    - Source: `Locality`
- `experimental-features-cookie-samesite-none-requires-secure2` — `toolkit/toolkit/featuregates/features.ftl` — "wymaga atrybutu bezpieczeństwa"; the source means the literal Secure cookie attribute. → "wymaga atrybutu Secure".
    - Current: `Secure`
    - Source: `label: Cookies: SameSite=None requires secure attribute`
    - Suggest: `"wymaga atrybutu Secure".`
- `user-context-color-purple` — `toolkit/toolkit/global/contextual-identity.ftl` — "Fioletowy", identical to user-context-color-violet; two container swatches become indistinguishable, notably for screen-reader users. → purple = "Purpurowy", keep violet = "Fioletowy".
    - Source: `label: Purple`
    - Suggest: `purple`
- `csp-error-illegal-host-wildcard` — `toolkit/toolkit/global/cspErrors.ftl` — "nieogólną domenę" for "non-generic sub-domain"; the sub-domain level is the whole point (.example.com vs .com). → "nieogólną poddomenę".
    - Current: `.com`
    - Source: `{ $scheme }: wildcard sources in ‘{ $directive }’ directives must include at least one non-generic sub-domain (e.g., *.example.com rather than *.com)`
    - Suggest: `"nieogólną poddomenę".`
- `language-name-ii` — `toolkit/toolkit/intl/languageNames.ftl` — "Syczuański" alone denotes Sichuanese Mandarin, a different language; the Yi/Nuosu qualifier identifies this entry. → "Yi syczuański".
    - Source: `Sichuan Yi`
    - Suggest: `"Yi syczuański".`
- `language-name-meh` — `toolkit/toolkit/intl/languageNames.ftl` — the same Mesoamerican family term is handled three ways ("Południowo-zachodni Tlaxiaco Mixtec" / "Mixtepec Mixtec" / "Zapotecki Miahuatlán"): Mixtec is left in English in two entries while Zapotec is polonised in the third, and English modifier-noun order is kept. → one pattern, e.g. "Mikstecki z południowo-zachodniego Tlaxiaco" / "Mikstecki z Mixtepec" / "Zapotecki z Miahuatlán".
    - Source: `Southwestern Tlaxiaco Mixtec`
- `language-name-mix` — `toolkit/toolkit/intl/languageNames.ftl` — the same Mesoamerican family term is handled three ways ("Południowo-zachodni Tlaxiaco Mixtec" / "Mixtepec Mixtec" / "Zapotecki Miahuatlán"): Mixtec is left in English in two entries while Zapotec is polonised in the third, and English modifier-noun order is kept. → one pattern, e.g. "Mikstecki z południowo-zachodniego Tlaxiaco" / "Mikstecki z Mixtepec" / "Zapotecki z Miahuatlán".
    - Source: `Mixtepec Mixtec`
- `language-name-zam` — `toolkit/toolkit/intl/languageNames.ftl` — the same Mesoamerican family term is handled three ways ("Południowo-zachodni Tlaxiaco Mixtec" / "Mixtepec Mixtec" / "Zapotecki Miahuatlán"): Mixtec is left in English in two entries while Zapotec is polonised in the third, and English modifier-noun order is kept. → one pattern, e.g. "Mikstecki z południowo-zachodniego Tlaxiaco" / "Mikstecki z Mixtepec" / "Zapotecki z Miahuatlán".
    - Source: `Miahuatlán Zapotec`
- `region-name-bq-2018` — `toolkit/toolkit/intl/regionNames.ftl` — judgment call. "Holandia" / "Holandia Karaibska"; the official Polish names per KSNG are "Niderlandy" / "Niderlandy Karaibskie". "Holandia" remains the dominant colloquial form, so this is a policy decision rather than an outright error.
    - Source: `Caribbean Netherlands`
- `region-name-nl` — `toolkit/toolkit/intl/regionNames.ftl` — judgment call. "Holandia" / "Holandia Karaibska"; the official Polish names per KSNG are "Niderlandy" / "Niderlandy Karaibskie". "Holandia" remains the dominant colloquial form, so this is a policy decision rather than an outright error.
    - Source: `Netherlands`
- `netReset-title` — `toolkit/toolkit/neterror/certError.ftl` — "Przerwane połączenie", identical to netInterrupt-title; "connection was reset" and "connection was interrupted" collapse into one message. → "Połączenie zostało zresetowane".
    - Source: `The connection was reset`
    - Suggest: `"Połączenie zostało zresetowane".`
- `pictureinpicture-unpip-btn` — `toolkit/toolkit/pictureinpicture/pictureinpicture.ftl` — "Wyłącz „Obraz w obrazie”" for Send back to tab / Back to tab; the button returns the video to its tab, it does not turn the feature off. The two distinct source values are also collapsed. → .aria-label = Odeślij z powrotem do karty, .tooltip = Z powrotem do karty.
    - Source: `aria-label: Send back to tab tooltip: Back to tab`
    - Suggest: `.aria-label = Odeślij z powrotem do karty`

### C. Grammar, agreement & spelling

- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — trailing space at the end of the first line of the multiline value ("Aktualizujesz system do Windows 11? "); Fluent preserves it. Same in psmerr-hostreusedissuerandserial (toolkit/toolkit/neterror/nsserrors.ftl), where en-US has no trailing space.
    - Source: `Upgrading to Windows 11? Let’s back up your { -brand-product-name } data.`
- `collection-usage-ping` — `browser/browser/preferences/preferences.ftl` — .label = "Wysyłaj dzienny sygnału o użyciu…" (adjective/noun case clash). The newer duplicate data-collection-usage-ping already has "dzienny sygnał". → "Wysyłaj dzienny sygnał o użyciu do…".
    - Source: `accesskey: u label: Send daily usage ping to { -vendor-short-name }`
    - Suggest: `"Wysyłaj dzienny sygnał o użyciu do…".`
- `safeb-blocked-unwanted-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — "ponieważ może one próbować" with a feminine singular subject ("ta strona"); the parallel malware/harmful strings use "może ona". → "ponieważ może ona próbować".
    - Source: `{ -brand-short-name } blocked this page because it might try to trick you into installing programs that harm your browsing experience (for example, by changing your homepage or showing extra ads on sites you visit).`
    - Suggest: `"ponieważ może ona próbować".`
- `tab-group-label-tooltip-collapsed` — `browser/browser/tabbrowser.ftl` — the adjective refers to grupa (fem.): "— zamknięte", "— zwinięte", "— rozwinięte". The parallel tabbrowser-manager-closed-tab-group correctly uses "— zamknięta". → "— zamknięta", "— zwinięta", "— rozwinięta".
    - Source: `{ $tabGroupName } — Collapsed`
    - Suggest: `"— zamknięta", "— zwinięta", "— rozwinięta".`
- `tab-group-label-tooltip-expanded` — `browser/browser/tabbrowser.ftl` — the adjective refers to grupa (fem.): "— zamknięte", "— zwinięte", "— rozwinięte". The parallel tabbrowser-manager-closed-tab-group correctly uses "— zamknięta". → "— zamknięta", "— zwinięta", "— rozwinięta".
    - Source: `{ $tabGroupName } — Expanded`
    - Suggest: `"— zamknięta", "— zwinięta", "— rozwinięta".`
- `tab-group-menu-closed-tab-group` — `browser/browser/tabbrowser.ftl` — the adjective refers to grupa (fem.): "— zamknięte", "— zwinięte", "— rozwinięte". The parallel tabbrowser-manager-closed-tab-group correctly uses "— zamknięta". → "— zamknięta", "— zwinięta", "— rozwinięta".
    - Source: `label: { $tabGroupName } title: { $tabGroupName } — Closed`
    - Suggest: `"— zamknięta", "— zwinięta", "— rozwinięta".`
- `inactive-css-not-display-block-on-floated` — `devtools/client/tooltips.ftl` — "element to floated" is a word-for-word calque and not grammatical Polish ("floated" is an English adjective here, not a CSS keyword). → "…ponieważ element jest przestawiony (float)."
    - Current: `floated`
    - Source: `The <strong>display</strong> value has been changed by the engine to <strong>block</strong> because the element is <strong>floated</strong>.`
    - Suggest: `float`
- `certmgr-begins-label` — `security/manager/security/certificates/certManager.ftl` — stray trailing colon on a tree column header: .label = "Ważny od dnia:"; the paired certmgr-expires-label has none. → "Ważny od dnia".
    - Source: `label: Begins On`
    - Suggest: `"Ważny od dnia".`
- `permanent-override` — `security/manager/security/certificates/certManager.ftl` — the two values of one column mix an adverbial phrase and an adjective: "Na stałe" / "Tymczasowy". → "Stały" / "Tymczasowy" (both agreeing with wyjątek).
    - Source: `Permanent`
- `temporary-override` — `security/manager/security/certificates/certManager.ftl` — the two values of one column mix an adverbial phrase and an adjective: "Na stałe" / "Tymczasowy". → "Stały" / "Tymczasowy" (both agreeing with wyjątek).
    - Source: `Temporary`
- `protected-auth-alert` — `security/manager/security/pippki/pippki.ftl` — "uwierzytelnić się" governs "w" + locative. Current: "Proszę uwierzytelnić się do urządzenia zabezpieczającego…" / "…do tokenu „{ $tokenName }”." → Suggest: "…w urządzeniu zabezpieczającym ({ $tokenName })." / "…w tokenie „{ $tokenName }”."
    - Source: `Please authenticate to the token “{ $tokenName }”. How to do so depends on the token (for example, using a fingerprint reader or entering a code with a keypad).`
    - Suggest: `"…w urządzeniu zabezpieczającym`
- `protected-auth-prompt` — `security/manager/security/pippki/pippki.ftl` — "uwierzytelnić się" governs "w" + locative. Current: "Proszę uwierzytelnić się do urządzenia zabezpieczającego…" / "…do tokenu „{ $tokenName }”." → Suggest: "…w urządzeniu zabezpieczającym ({ $tokenName })." / "…w tokenie „{ $tokenName }”."
    - Source: `Please authenticate to the security device ({ $tokenName }). How to do so depends on the device (for example, using a fingerprint reader or entering a code with a keypad).`
    - Suggest: `"…w urządzeniu zabezpieczającym`
- `no-config-label` — `toolkit/crashreporter/aboutcrashes.ftl` — missing sentence-final period after <code>breakpad.reportURL</code>.
    - Source: `This application has not been configured to display crash reports. The preference <code>breakpad.reportURL</code> must be set.`
- `autofill-insecure-field-warning-description` — `toolkit/toolkit/formautofill/formAutofill.ftl` — missing sentence-final period after "…wypełnianie formularzy".
    - Source: `{ -brand-short-name } has detected an insecure site. Form Autofill is temporarily disabled.`
- `webext-perms-header-unsigned` — `toolkit/toolkit/global/extensions.ftl` — "Dodaj rozszerzanie jedynie…" (= expanding). Same typo in webext-perms-header-unsigned-with-perms, webext-perms-list-intro-unsigned and webext-site-perms-header-unsigned-with-perms. → "rozszerzenie".
    - Source: `Add { $extension }? This extension is unverified. Malicious extensions can steal your private information or compromise your computer. Only add it if you trust the source.`
    - Suggest: `"rozszerzenie".`

### D. Terminology, register & consistency

- `backup-file-moz-browser-restore-step-2-1` — `browser/browser/backupSettings.ftl` — `backup-file-moz-browser-restore-step-2-1` quotes “Przywróć dane” but the string it names, `restore-from-backup-header`, reads “Przywracanie danych”
    - Current: `Kliknij „Przywróć dane” i wybierz ten plik`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Przywracanie danych`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `backup-file-other-browser-restore-step-3-1` — `browser/browser/backupSettings.ftl` — `backup-file-other-browser-restore-step-3-1` quotes “Przywróć dane” but the string it names, `restore-from-backup-header`, reads “Przywracanie danych”
    - Current: `Kliknij „Przywróć dane” i wybierz ten plik`
    - Source: `Click “Restore your data” and select this file`
    - Suggest: `Przywracanie danych`
    - In the source this string quotes “Restore your data”, which is exactly the value of `restore-from-backup-header` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `newtab-sports-widget-round-16` — `browser/browser/newtab/newtab.ftl` — "Pierwsza runda" / "Druga runda" for "Round of 32" / "Round of 16"; Polish football usage names these by fraction, and the current wording is ambiguous against the preceding group stage. → "1/16 finału" / "1/8 finału".
    - Source: `Round of 16`
- `newtab-sports-widget-round-32` — `browser/browser/newtab/newtab.ftl` — "Pierwsza runda" / "Druga runda" for "Round of 32" / "Round of 16"; Polish football usage names these by fraction, and the current wording is ambiguous against the preceding group stage. → "1/16 finału" / "1/8 finału".
    - Source: `Round of 32`
- `media-count` — `browser/browser/pageInfo.ftl` — .label = "Ilość" for a count of discrete items; the locale uses "Liczba" elsewhere (processes-count, place-database-stats-count, "Liczba wizyt" in places.ftl). → "Liczba".
    - Source: `label: Count`
    - Suggest: `"Liczba".`
- `storage-add-button` — `devtools/client/storage.ftl` — "Item" is "obiekt" here and in storage-context-menu-add-item / storage-refresh-button, but "element" in storage-search-box; "obiekt" also collides with the JS sense of object.
    - Source: `title: Add Item`
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “trybu lokalnego” but the string it names, `options-local-mode-label`, reads “Tryb lokalny”
    - Current: `Ten dokument można także wczytać z „{ $url }” za pomocą „trybu lokalnego” narzędzi dla programistów, który można włączyć w panelu ustawień.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Tryb lokalny`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `pkcs12-info-no-smartcard-backup` — `security/manager/security/certificates/certManager.ftl` — "inteligentna karta"; the established Polish term is "karta inteligentna".
    - Source: `It is not possible to back up certificates from a hardware security device such as a smart card.`
- `pkcs12-unknown-err-backup` — `security/manager/security/certificates/certManager.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
    - Source: `Failed to create the PKCS #12 backup file for unknown reasons.`
    - Suggest: `standardize on "kopia zapasowa".`
- `pkcs12-unknown-err-restore` — `security/manager/security/certificates/certManager.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
    - Source: `Failed to restore the PKCS #12 file for unknown reasons.`
    - Suggest: `standardize on "kopia zapasowa".`
- `unable-to-toggle-fips` — `security/manager/security/certificates/deviceManager.ftl` — the only occurrence of "urządzenie bezpieczeństwa" in the locale; everything else, including fips-nonempty-primary-password-required two entries above, says "urządzenie zabezpieczające".
    - Source: `Unable to change the FIPS mode for the security device. It is recommended that you exit and restart this application.`
- `set-password-backup-pw` — `security/manager/security/pippki/pippki.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
    - Source: `value: Certificate backup password:`
    - Suggest: `standardize on "kopia zapasowa".`
- `set-password-repeat-backup-pw` — `security/manager/security/pippki/pippki.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
    - Source: `value: Certificate backup password (again):`
    - Suggest: `standardize on "kopia zapasowa".`
- `set-password-window` — `security/manager/security/pippki/pippki.ftl` — "kopia bezpieczeństwa" (6 occurrences, all here) vs "kopia zapasowa" (79 elsewhere, including certmgr-backup in the same dialog). → standardize on "kopia zapasowa".
    - Source: `title: Choose a Certificate Backup Password`
    - Suggest: `standardize on "kopia zapasowa".`
- `enableSafeBrowsing-label` — `toolkit/toolkit/about/aboutRights.ftl` — quotes a preferences label verbatim, but with different wording: "Blokowanie niebezpiecznych i podejrzanych treści." vs the actual security-enable-safe-browsing = "Blokuj niebezpieczne i podejrzane treści."
    - Source: `Block dangerous and deceptive content`
- `about-telemetry-keyed-scalar-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — left in English ("Keyed scalars") while about-telemetry-scalar-section = "Skalary" and about-telemetry-keyed-histogram-section = "Indeksowane histogramy". → "Indeksowane skalary".
    - Source: `Keyed Scalars`
    - Suggest: `"Indeksowane skalary".`
- `tabmodalprompt-username` — `toolkit/toolkit/global/tabprompts.ftl` — .value = "Użytkownik:"; the identical field in common-dialog-username is "Nazwa użytkownika". → "Nazwa użytkownika:".
    - Source: `value: User Name:`
    - Suggest: `"Nazwa użytkownika:".`

### E. Typography, punctuation & spacing

- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
    - Current: `Zdarzenie klawisza jest niedostępne dla GTK2: key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `polish-double` (1560 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
    - Current: `Zdarzenie klawisza jest niedostępne przy niektórych układach klawiatury: key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `polish-double` (1560 occurrences).
- `plugins-openh264-description` — `toolkit/toolkit/about/aboutAddons.ftl` — stale URL "http://www.openh264.org"; the source uses "https://www.openh264.org/".
    - Source: `This plugin is automatically installed by Mozilla to comply with the WebRTC specification and to enable WebRTC calls with devices that require the H.264 video codec. Visit https://www.openh264.org/ to view the codec sou…`
- `password-manager-update-password-message` — `toolkit/toolkit/passwordmgr/passwordmgr.ftl` — "hasło dla { $host }?" without quotes, while the sibling password-manager-save-password-message in the same doorhanger uses „{ $host }”.
    - Source: `Update password for { $host }?`

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/pl/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (1)

- `cfr-doorhanger-extension-total-users` — `browser/browser/newtab/asrouter.ftl` — raised by `legacy`, withdrawn 2026-08-20

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (127)

- `refresh-blocked-redirect-label` — `browser/browser/browser.ftl` — fixed 2026-08-21
- `refresh-blocked-refresh-label` — `browser/browser/browser.ftl` — fixed 2026-08-21
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

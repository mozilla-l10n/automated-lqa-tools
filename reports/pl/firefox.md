# Firefox l10n QA — pl

| | |
|---|---|
| **Generated** | 2026-08-26 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `b82b7a344c63` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `bcb4650bbefb` |
| **Previous run** | 2026-08-25 @ `ad52f2a75880` |
| **Mode** | incremental |
| **Strings reviewed this run** | 2 of 18,112 |

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
| Files | 360 |
| Strings | 18,112 |
| Missing strings | 98 |
| Obsolete strings | 0 |
| Files absent from the locale | 2 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Variable & placeholder mismatches | 2 |
| Term parameter mismatches | 0 |
| Plural variants (dead or missing forms) | 3 |
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 2 |

### Completeness

**98 strings** are not translated yet, concentrated in:

- `browser/browser/aiWindow.ftl` — 63
- `toolkit/services/aboutSyncLog.ftl` — 26
- `browser/browser/newtab/newtab.ftl` — 6
- `toolkit/toolkit/pdfviewer/embedFallback.ftl` — 2
- `browser/browser/newtab/onboarding.ftl` — 1

**Files absent from the locale:**

- `toolkit/services/aboutSyncLog.ftl`
- `toolkit/toolkit/pdfviewer/embedFallback.ftl`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 1571, `straight-double` 36, `german-double` 7, `curly-double` 2 | **polish-double** |
| apostrophe | `straight` 1 | **straight** |
| ellipsis | `char` 468 | **char** |
| dash | `em` 170, `en` 14 | **em** |
| nbsp | `total` 5459, `narrow` 3, `before-punctuation` 49, `space-before-punctuation` 21 | **total** |
| register | `informal` 79 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (65)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 11 |
| 2 | Wrong content (says something other than the English) | 36 |
| 3 | Degraded language (grammar, spelling, terminology) | 16 |
| 4 | Cosmetic (typography, spacing) | 2 |

### A. Functional, markup, variables & plurals

- `smart-window-closed-tabs-summary` — `browser/browser/aiWindowContent.ftl` — `smart-window-closed-tabs-summary` is missing the ['few', 'many'] plural forms
    - Current: `{$count ->} [one] Gotowe! Zamknięto kartę. [other] Gotowe! Zamknięto karty.`
    - Source: `{$count ->} [one] Done! Tab closed. [other] Done! Tabs closed.`
    - This locale uses ['few', 'many', 'one'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
- `smart-window-restore-success-summary` — `browser/browser/aiWindowContent.ftl` — `smart-window-restore-success-summary` is missing the ['few', 'many'] plural forms
    - Current: `{$count ->} [one] Zamknięto kartę, a następnie ją przywrócono. [other] Zamknięto karty, a następnie je przywrócono.`
    - Source: `{$count ->} [one] Tab closed, then restored. [other] Tabs closed, then restored.`
    - This locale uses ['few', 'many', 'one'] in most of its plurals, and en-US pluralizes this string. The catch-all variant will be shown instead, giving the wrong grammatical form.
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
- `ai-window-is-default-window` — `browser/browser/aiFeatures.ftl` — The "restarts" case is dropped from the description.
    - Current: `Otwieraj { -smart-window-brand-name } po uruchomieniu { -brand-short-name } i po kliknięciu odnośników w innych aplikacjach.`
    - Source: `description: Open { -smart-window-brand-name } when { -brand-short-name } starts, restarts, or opens links from other apps. label: Use { -smart-window-brand-name } by default`
    - Suggest: `Otwieraj { -smart-window-brand-name } po uruchomieniu lub ponownym uruchomieniu { -brand-short-name } oraz po otwarciu odnośników z innych aplikacji.`
    - The en-US lists three triggers: when Firefox starts, restarts, or opens links from other apps; the Polish omits "restarts".
- `action-log-checked-memories` — `browser/browser/aiWindowContent.ftl` — "Checked memories" translated as "searched remembered content".
    - Current: `Przeszukano zapamiętane treści`
    - Source: `Checked memories`
    - Suggest: `Sprawdzono zapamiętane treści`
    - en-US says "Checked" (sprawdzono), not "Searched".
- `action-log-checked-world-cup-live` — `browser/browser/aiWindowContent.ftl` — "Checked live World Cup matches" rendered with "Przeszukano" (searched) instead of checked.
    - Current: `Przeszukano trwające mecze mistrzostw świata`
    - Source: `Checked live World Cup matches`
    - Suggest: `Sprawdzono trwające mecze mistrzostw świata`
    - en-US says "Checked", not "Searched".
- `action-log-checking-memories` — `browser/browser/aiWindowContent.ftl` — "Checking memories" translated as "searching remembered content", changing the verb from check to search.
    - Current: `Przeszukiwanie zapamiętanych treści`
    - Source: `Checking memories`
    - Suggest: `Sprawdzanie zapamiętanych treści`
    - en-US uses "Checking" (sprawdzanie), not "Searching"; the pl string also blurs the distinction with the neighbouring "Searching…" strings.
- `action-log-checking-world-cup-live` — `browser/browser/aiWindowContent.ftl` — "Checking live World Cup matches" rendered with "Przeszukiwanie" (searching) instead of checking.
    - Current: `Przeszukiwanie trwających meczów mistrzostw świata`
    - Source: `Checking live World Cup matches`
    - Suggest: `Sprawdzanie trwających meczów mistrzostw świata`
    - en-US distinguishes "Checking" from "Searching"; the pl text uses the same verb for both.
- `smart-window-grouped-and-ungrouped-label` — `browser/browser/aiWindowContent.ftl` — "Tabs ungrouped" rendered as "Rozgrupowane karty" while the corresponding row label uses the verb form; label describes an action result.
    - Current: `Rozgrupowane karty`
    - Source: `Tabs ungrouped`
    - Suggest: `Karty rozgrupowane`
    - Per the developer comment this is an action result label ("Tabs ungrouped"), parallel to "Closed and restored tabs"; the adjective-first form loses the result sense.
- `smartwindow-assistant-error-budget-body` — `browser/browser/aiWindowContent.ftl` — "once your daily limit resets" rendered as "po przywróceniu dziennego ograniczenia" (after the daily limit is restored/reinstated), reversing the meaning.
    - Current: `po przywróceniu dziennego ograniczenia`
    - Source: `You can still browse in this window. Chat will be available again once your daily limit resets.`
    - Suggest: `po wyzerowaniu dziennego limitu`
    - en-US means the limit counter resets (is cleared), making chat available again; "przywrócenie ograniczenia" says the restriction is reinstated, which contradicts the sentence.
- `smartwindow-assistant-error-budget-header` — `browser/browser/aiWindowContent.ftl` — "Reached today's chat limit" translated as "exceeded today's limit of the conversation", changing meaning from a daily chat quota to a single conversation.
    - Current: `Przekroczono dzisiejsze ograniczenie rozmowy.`
    - Source: `You’ve reached today’s chat limit.`
    - Suggest: `Osiągnięto dzisiejszy limit rozmów.`
    - en-US says the user reached today's chat limit (a daily quota on chats); the Polish singular genitive "ograniczenie rozmowy" says the limit of the (one) conversation, and "przekroczono" says it was exceeded rather than reached.
- `smartwindow-assistant-error-capacity-header` — `browser/browser/aiWindowContent.ftl` — "is at capacity" rendered as "jest teraz zbyt zajęte" (is too busy), an inaccurate rendering of reaching capacity.
    - Current: `jest teraz zbyt zajęte`
    - Source: `{ -smart-window-brand-name } is at capacity right now. Please try again later.`
    - Suggest: `jest w tej chwili przeciążone`
    - en-US states the service has reached its capacity; "zbyt zajęte" (too busy) is not the same statement and reads oddly.
- `smartwindow-assistant-error-max-length-header` — `browser/browser/aiWindowContent.ftl` — "reached its length limit" translated as "przekroczyła" (exceeded) instead of reached.
    - Current: `Ta przekroczyła ograniczenie długości.`
    - Source: `It’s time to start a new chat. This one’s reached its length limit.`
    - Suggest: `Ta osiągnęła limit długości.`
    - en-US says the chat has reached its length limit, not that it exceeded it.
- `smartwindow-messages-document-title` — `browser/browser/aiWindowContent.ftl` — "chat messages" reduced to just "Wiadomości", dropping "chat".
    - Current: `Wiadomości { -smart-window-brand-name }`
    - Source: `{ -smart-window-brand-name } chat messages`
    - Suggest: `Wiadomości rozmowy { -smart-window-brand-name }`
    - The en-US document title specifies chat messages; the Polish omits the "chat" qualifier present in the source.
- `smartwindow-nl-retry-group-tabs-message` — `browser/browser/aiWindowContent.ftl` — "in the card that opens" mistranslated as "na karcie" (browser tab) in a string that also talks about tabs.
    - Current: `kliknij <strong>Ponów</strong> i dokonaj wyboru na karcie, która się otworzy`
    - Source: `If you still want to group tabs, choose <strong>Retry</strong> and select which ones in the card that opens.`
    - Suggest: `wybierz <strong>Ponów</strong> i dokonaj wyboru w wyświetlonym oknie`
    - Same as the sibling string: "card" is a UI card, not a browser tab, so "na karcie" conflicts with "karty" used for tabs earlier in the sentence.
- `smartwindow-nl-retry-message` — `browser/browser/aiWindowContent.ftl` — "in the card that opens" refers to a UI card, but the Polish uses "karta" in the sense of a browser tab, and "choose" became "kliknij".
    - Current: `kliknij <strong>Ponów</strong> i dokonaj wyboru na karcie, która się otworzy`
    - Source: `If you still want to close tabs, choose <strong>Retry</strong> and make your selection in the card that opens.`
    - Suggest: `wybierz <strong>Ponów</strong> i dokonaj wyboru w wyświetlonym oknie`
    - The message is about closing tabs (karty); rendering "card" as "karta" makes the sentence ambiguous/wrong — the user is told to make a selection "on the tab that opens" rather than in the card UI that appears.
- `main-context-menu-link-send-to-device` — `browser/browser/browserContext.ftl` — dangling preposition: "Wyślij stronę do" / "Wyślij odnośnik do". → "Wyślij stronę na urządzenie" / "Wyślij odnośnik na urządzenie" (cf. main-context-menu-send-to-device-2).
    - Source: `accesskey: n label: Send Link to Device`
- `main-context-menu-send-to-device` — `browser/browser/browserContext.ftl` — dangling preposition: "Wyślij stronę do" / "Wyślij odnośnik do". → "Wyślij stronę na urządzenie" / "Wyślij odnośnik na urządzenie" (cf. main-context-menu-send-to-device-2).
    - Source: `accesskey: n label: Send Page to Device`
- `genai-settings-chat-lechat-links` — `browser/browser/genai.ftl` — "Mistral AI" is a company name and should not be translated. Current: "…zasady ochrony prywatności</a> sztucznej inteligencji Mistral." → Suggest: "…zasady ochrony prywatności</a> Mistral AI." (the sibling strings correctly keep OpenAI, Microsoft, Anthropic).
    - Source: `By choosing Le Chat Mistral, you agree to the Mistral AI <a data-l10n-name="link1">Terms of Service</a> and <a data-l10n-name="link2">Privacy Policy</a>.`
- `smartwindow-sidebar-auto-open-callout-title` — `browser/browser/newtab/onboarding.ftl` — "Want to keep the assistant closed?" loses "keep", becoming "Do you want the assistant to be closed?"
    - Current: `Czy chcesz, aby asystent był zamknięty?`
    - Source: `Want to keep the assistant closed?`
    - Suggest: `Czy chcesz, aby asystent pozostał zamknięty?`
    - en-US asks about keeping the assistant closed (continuing state); the pl drops that nuance.
- `fxa-qrcode-pair-step1` — `browser/browser/preferences/fxaPairDevice.ftl` — narrows "mobile device" to "telefon", contradicting the dialog title (fxa-qrcode-pair-title = "…na telefonie lub tablecie"). → "…na urządzeniu mobilnym."
    - Source: `1. Open { -brand-product-name } on your mobile device.`
    - Suggest: `"…na urządzeniu mobilnym."`
- `more-from-moz-solo-title` — `browser/browser/preferences/moreFromMozilla.ftl` — drops the "AI" qualifier present in en-US ("{ -solo-ai-brand-name } AI") and in the sibling more-from-moz-solo-title-2 ("Kreator SI stron internetowych…").
    - Source: `{ -solo-ai-brand-name } AI`
- `whypaused-assert` — `devtools/shared/debugger-paused-reasons.ftl` — "Wstrzymane na warunku" for "Paused on assertion"; warunek is a different debugger concept already used by whypaused-breakpoint-condition-thrown. → "Wstrzymane na asercji".
    - Source: `Paused on assertion`
    - Suggest: `"Wstrzymane na asercji".`
- `config-new-pref-value-integer` — `mobile/android/mobile/android/aboutConfig.ftl` — "Liczba" for the specific Integer pref type; also collides with config-new-pref-number ("Wprowadź liczbę"). → "Liczba całkowita".
    - Source: `Integer`
    - Suggest: `"Liczba całkowita".`
- `network-connection-status-looked-up` — `netwerk/netwerk/necko.ftl` — breaks the Looking up / Looked up pair (rendered "Ustalanie adresu serwera" / "Odnaleziono"). → "Ustalono adres serwera { $host }…".
    - Source: `Looked up { $host }…`
    - Suggest: `"Ustalono adres serwera { $host }…".`
- `MOZILLA_PKIX_ERROR_INVALID_INTEGER_ENCODING` — `security/manager/chrome/pipnss/nsserrors.properties` — "encodings that are longer than necessary" mistranslated as "niepotrzebne już kodowania" (encodings no longer needed).
    - Current: `i niepotrzebne już kodowania`
    - Source: `The server presented a certificate that contains an invalid encoding of an integer. Common causes include negative serial numbers, negative RSA moduli, and encodings that are longer than necessary.`
    - Suggest: `i kodowania dłuższe niż to konieczne`
    - The source describes encodings longer than necessary, not obsolete encodings.
- `rights-webservices-term-5` — `toolkit/toolkit/about/aboutRights.ftl` — the damages enumeration lists "wyjątkowe" twice and includes the unfinished-looking "będące skutkiem czegoś" for "indirect, special, incidental, consequential, punitive, or exemplary". Needs a rewrite of the list.
    - Source: `<strong>Except as required by law, { -vendor-short-name }, its contributors, licensors, and distributors will not be liable for any indirect, special, incidental, consequential, punitive, or exemplary damages arising ou…`
- `abuse-report-unwanted-reason-v2` — `toolkit/toolkit/about/abuseReports.ftl` — "Samo się zainstalowało i nie wiem, jak je usunąć" for "I never wanted it and don't know how to get rid of it"; the self-installation claim duplicates abuse-report-unwanted-example. → "Nigdy tego nie chciałem(-am) i nie wiem, jak to usunąć".
    - Source: `I never wanted it and don’t know how to get rid of it`
    - Suggest: `"Nigdy tego nie chciałem`
- `certificate-viewer-inc-locality` — `toolkit/toolkit/about/certviewer.ftl` — "Region" / "Region założenia" for X.509 L= (city/town), which also blurs the line with certificate-viewer-state-province = "Województwo". → "Miejscowość" / "Miejscowość założenia".
    - Source: `Inc. Locality`
- `certificate-viewer-locality` — `toolkit/toolkit/about/certviewer.ftl` — "Region" / "Region założenia" for X.509 L= (city/town), which also blurs the line with certificate-viewer-state-province = "Województwo". → "Miejscowość" / "Miejscowość założenia".
    - Source: `Locality`
- `user-context-color-purple` — `toolkit/toolkit/global/contextual-identity.ftl` — "Fioletowy", identical to user-context-color-violet; two container swatches become indistinguishable, notably for screen-reader users. → purple = "Purpurowy", keep violet = "Fioletowy".
    - Source: `label: Purple`
    - Suggest: `purple`
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
- `cert-error-invalid-integer-encoding` — `toolkit/toolkit/neterror/certError.ftl` — "encodings that are longer than necessary" mistranslated as "niepotrzebne już kodowania" (encodings that are no longer needed).
    - Current: `i niepotrzebne już kodowania`
    - Source: `{ -brand-short-name } blocked your visit to this site because the certificate provided for { $hostname } contains an invalid encoding of an integer. Common causes include negative serial numbers, negative RSA moduli, an…`
    - Suggest: `i kodowania dłuższe niż to konieczne`
    - The en-US says the encodings are longer than necessary, not that they are obsolete/no longer needed.
- `mozilla-pkix-error-invalid-integer-encoding` — `toolkit/toolkit/neterror/nsserrors.ftl` — "encodings that are longer than necessary" mistranslated as "niepotrzebne już kodowania" (encodings no longer needed).
    - Current: `i niepotrzebne już kodowania`
    - Source: `The server presented a certificate that contains an invalid encoding of an integer. Common causes include negative serial numbers, negative RSA moduli, and encodings that are longer than necessary.`
    - Suggest: `i kodowania dłuższe niż to konieczne`
    - The source describes encodings longer than necessary, not obsolete encodings.
- `pictureinpicture-unpip-btn` — `toolkit/toolkit/pictureinpicture/pictureinpicture.ftl` — "Wyłącz „Obraz w obrazie”" for Send back to tab / Back to tab; the button returns the video to its tab, it does not turn the feature off. The two distinct source values are also collapsed. → .aria-label = Odeślij z powrotem do karty, .tooltip = Z powrotem do karty.
    - Source: `aria-label: Send back to tab tooltip: Back to tab`
    - Suggest: `.aria-label = Odeślij z powrotem do karty`

### C. Grammar, agreement & spelling

- `ai-window-learn-from-browsing-activity` — `browser/browser/aiFeatures.ftl` — "Learn from browsing in Classic and { -smart-window-brand-name }" is rendered with a dangling plural adjective "klasycznych" that has no noun.
    - Current: `Ucz się z przeglądania w klasycznych i { -smart-window-brand-name }`
    - Source: `label: Learn from browsing in Classic and { -smart-window-brand-name }`
    - Suggest: `Ucz się z przeglądania w oknach klasycznych i { -smart-window-brand-name }`
    - "Classic" here names the Classic window mode; the Polish leaves a plural adjective with no noun, which is ungrammatical and unintelligible.
- `inactive-css-not-display-block-on-floated` — `devtools/client/tooltips.ftl` — "element to floated" is a word-for-word calque and not grammatical Polish ("floated" is an English adjective here, not a CSS keyword). → "…ponieważ element jest przestawiony (float)."
    - Current: `floated`
    - Source: `The <strong>display</strong> value has been changed by the engine to <strong>block</strong> because the element is <strong>floated</strong>.`
    - Suggest: `float`
- `temporary-override` — `security/manager/security/certificates/certManager.ftl` — the two values of one column mix an adverbial phrase and an adjective: "Na stałe" / "Tymczasowy". → "Stały" / "Tymczasowy" (both agreeing with wyjątek).
    - Source: `Temporary`

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
- `toolbox-local-mode-notice` — `devtools/client/toolbox.ftl` — `toolbox-local-mode-notice` quotes “trybu lokalnego” but the string it names, `options-local-mode-label`, reads “Tryb lokalny”
    - Current: `Ten dokument można także wczytać z „{ $url }” za pomocą „trybu lokalnego” narzędzi dla programistów, który można włączyć w panelu ustawień.`
    - Source: `This document could also be loaded from “{ $url }” using DevTools “Local Mode”, which can be enabled in the settings panel.`
    - Suggest: `Tryb lokalny`
    - In the source this string quotes “Local Mode”, which is exactly the value of `options-local-mode-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `pkcs12-info-no-smartcard-backup` — `security/manager/security/certificates/certManager.ftl` — "inteligentna karta"; the established Polish term is "karta inteligentna".
    - Source: `It is not possible to back up certificates from a hardware security device such as a smart card.`
- `enableSafeBrowsing-label` — `toolkit/toolkit/about/aboutRights.ftl` — quotes a preferences label verbatim, but with different wording: "Blokowanie niebezpiecznych i podejrzanych treści." vs the actual security-enable-safe-browsing = "Blokuj niebezpieczne i podejrzane treści."
    - Source: `Block dangerous and deceptive content`
- `certificate-viewer-modulus` — `toolkit/toolkit/about/certviewer.ftl` — Mathematical term "Modulus" rendered as "Moduł" (module) instead of "Moduł" in the RSA sense; ambiguous with software module.
    - Current: `Moduł`
    - Source: `Modulus`
    - Suggest: `Modulus`
    - In the certificate viewer this is the RSA modulus; Polish cryptographic terminology uses "modulus", while "Moduł" reads as a software module.
- `tabmodalprompt-username` — `toolkit/toolkit/global/tabprompts.ftl` — .value = "Użytkownik:"; the identical field in common-dialog-username is "Nazwa użytkownika". → "Nazwa użytkownika:".
    - Source: `value: User Name:`
    - Suggest: `"Nazwa użytkownika:".`

### E. Typography, punctuation & spacing

- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
    - Current: `Zdarzenie klawisza jest niedostępne dla GTK2: key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `polish-double` (1571 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
    - Current: `Zdarzenie klawisza jest niedostępne przy niektórych układach klawiatury: key="%S" modifiers="%S" id="%S"`
    - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
    - The locale's quote convention is `polish-double` (1571 occurrences).

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

### Fixed to date (166)

- `backup-file-intro` — `browser/browser/backupSettings.ftl` — fixed 2026-08-24
- `newtab-wallpaper-dark-green` — `browser/browser/newtab/newtab.ftl` — fixed 2026-08-24
- `create-backup-screen-1-title` — `browser/browser/newtab/onboarding.ftl` — fixed 2026-08-24
- `policy-ShowHomeButton` — `browser/browser/policies/policies-descriptions.ftl` — fixed 2026-08-24
- `collection-usage-ping` — `browser/browser/preferences/preferences.ftl` — fixed 2026-08-24
- `safeb-blocked-unwanted-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — fixed 2026-08-24
- `tab-group-editor-action-copy-links` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `tab-group-label-tooltip-collapsed` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `tab-group-label-tooltip-expanded` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `tab-group-menu-closed-tab-group` — `browser/browser/tabbrowser.ftl` — fixed 2026-08-24
- `storage-add-button` — `devtools/client/storage.ftl` — fixed 2026-08-24
- `inactive-css-property-because-of-display` — `devtools/client/tooltips.ftl` — fixed 2026-08-24
- `xslt-load-recursion` — `dom/dom/xslt.ftl` — fixed 2026-08-24
- `certmgr-begins-label` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `permanent-override` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `pkcs12-unknown-err-backup` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `pkcs12-unknown-err-restore` — `security/manager/security/certificates/certManager.ftl` — fixed 2026-08-24
- `unable-to-toggle-fips` — `security/manager/security/certificates/deviceManager.ftl` — fixed 2026-08-24
- `protected-auth-alert` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `protected-auth-prompt` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `set-password-backup-pw` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `set-password-repeat-backup-pw` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `set-password-window` — `security/manager/security/pippki/pippki.ftl` — fixed 2026-08-24
- `no-config-label` — `toolkit/crashreporter/aboutcrashes.ftl` — fixed 2026-08-24
- `plugins-openh264-description` — `toolkit/toolkit/about/aboutAddons.ftl` — fixed 2026-08-24
- `about-networking-networkid-status-known` — `toolkit/toolkit/about/aboutNetworking.ftl` — fixed 2026-08-24
- `state-dd-enabled` — `toolkit/toolkit/about/aboutPlugins.ftl` — fixed 2026-08-24
- `media-audio-robustness` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-08-24
- `media-video-robustness` — `toolkit/toolkit/about/aboutSupport.ftl` — fixed 2026-08-24
- `about-telemetry-keyed-scalar-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — fixed 2026-08-24
- `third-party-message-no-duration` — `toolkit/toolkit/about/aboutThirdParty.ftl` — fixed 2026-08-24
- `about-webrtc-aec-logging-msg-label` — `toolkit/toolkit/about/aboutWebrtc.ftl` — fixed 2026-08-24
- `experimental-features-cookie-samesite-none-requires-secure2` — `toolkit/toolkit/featuregates/features.ftl` — fixed 2026-08-24
- `autofill-insecure-field-warning-description` — `toolkit/toolkit/formautofill/formAutofill.ftl` — fixed 2026-08-24
- `csp-error-illegal-host-wildcard` — `toolkit/toolkit/global/cspErrors.ftl` — fixed 2026-08-24
- `webext-perms-header-unsigned` — `toolkit/toolkit/global/extensions.ftl` — fixed 2026-08-24
- `language-name-ii` — `toolkit/toolkit/intl/languageNames.ftl` — fixed 2026-08-24
- `netReset-title` — `toolkit/toolkit/neterror/certError.ftl` — fixed 2026-08-24
- `password-manager-update-password-message` — `toolkit/toolkit/passwordmgr/passwordmgr.ftl` — fixed 2026-08-24
- `refresh-blocked-redirect-label` — `browser/browser/browser.ftl` — fixed 2026-08-21

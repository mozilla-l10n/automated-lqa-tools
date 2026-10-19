# Firefox l10n QA — sv-SE

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `9ea69c4843c5` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `2d5e7eb1f225` |
| **Previous run** | 2026-10-19 @ `ba8eba5819d0` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 16,520 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for sv-SE: [android](android.md) · [firefox_ios](firefox_ios.md)

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
| Files | 328 |
| Strings | 16,520 |
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
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 0 |
| Markup & `data-l10n-name` defects | 4 |
| Typography deviations from this locale's own norm | 18 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `straight-double` 305, `curly-double` 221, `curly-single` 122 | _mixed_ |
| apostrophe | `typographic` 126, `straight` 42 | **typographic** |
| ellipsis | `char` 385, `ascii` 16 | **char** |
| dash | `em` 67, `en` 9 | **em** |
| nbsp | `total` 9, `before-punctuation` 2, `space-before-punctuation` 7 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (329)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 212 |
| 2 | Wrong content (says something other than the English) | 96 |
| 3 | Degraded language (grammar, spelling, terminology) | 2 |
| 4 | Cosmetic (typography, spacing) | 19 |

### A. Functional, markup, variables & plurals

- `about-logins-import-dialog-items-no-change2` — `browser/browser/aboutLogins.ftl` — Malformed closing tag `</span >` in `about-logins-import-dialog-items-no-change2`
    - Current: `{$count ->} [one] <span>Duplicerad post hittad:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(ej importerad)</span > [other] <span>Duplicerade poster hittades:</span> <span data-l10n…`
    - Source: `{$count ->} [other] <span>Duplicate entries found:</span> <span data-l10n-name="count">{ $count }</span> <span data-l10n-name="meta">(not imported)</span>`
    - Whitespace inside a closing tag makes it render as literal text.
- `restart-required-multiple-instances-question` — `browser/browser/aboutRestartRequired.ftl` — "Why can this happen" is rendered as "Hur kan detta inträffa" (how can this happen).
    - Current: `Hur kan detta inträffa med flera profiler`
    - Source: `Why can this happen with multiple profiles or { -brand-short-name } instances?`
    - Suggest: `Varför kan detta inträffa med flera profiler`
    - The FAQ answer explains the reason, not the mechanism; the neighbouring question uses "Varför" correctly.
- `addon-mlmodel-removal-body` — `browser/browser/addonNotifications.ftl` — The Swedish says the features/extensions will be re-added, while the developer comment states "it" refers to the local AI model.
    - Current: `kommer de att läggas till igen`
    - Source: `If you use the features or extensions that use this model, it will be re-added.`
    - Suggest: `kommer den att läggas till igen`
    - Comment: '"it" refers to the local AI model that is paired to the AI feature'. Plural "de" makes the sentence claim the add-ons/features are re-added, not the model.
- `action-log-read-page` — `browser/browser/aiWindowContent.ftl` — Completed-action log entry is rendered as an imperative/present "Läs" instead of past tense.
    - Current: `Läs sidans innehåll`
    - Source: `Read page content`
    - Suggest: `Läste sidans innehåll`
    - Comment: 'Read is past tense, to indicate that the action has been completed.' Neighbouring completed entries use past tense (Sökte, Kontrollerade), so this row reads as an instruction rather than a finished step.
- `action-log-searching-history` — `browser/browser/aiWindowContent.ftl` — In-progress label "Searching history" is rendered as the compound noun "Sökhistorik" (search history).
    - Current: `Sökhistorik`
    - Source: `Searching history`
    - Suggest: `Söker i historik`
    - The string is the in-progress counterpart of action-log-searched-history ("Sökte i historik"); "Sökhistorik" names the user's search history instead of the ongoing action.
- `action-log-searching-web-with-exa` — `browser/browser/aiWindowContent.ftl` — In-progress label uses the imperative "Sök" instead of the progressive form used by the sibling strings.
    - Current: `Sök på webben med <a data-l10n-name="exa-link">Exa</a>`
    - Source: `Searching the web with <a data-l10n-name="exa-link">Exa</a>`
    - Suggest: `Söker på webben med <a data-l10n-name="exa-link">Exa</a>`
    - action-log-searching-web is "Söker på webben"; here the same "Searching" state is rendered as a command, making the progress row inconsistent with the rest of the log.
- `appmenu-search-history` — `browser/browser/appmenu.ftl` — Menu command for searching history is rendered as the noun "Sökhistorik" (search history).
    - Current: `Sökhistorik`
    - Source: `label: Search History`
    - Suggest: `Sök i historik`
    - Comment: 'This allows to search through the browser’s history.' "Sökhistorik" names a list of past searches rather than the search action.
- `profiler-popup-presets-web-developer-description` — `browser/browser/appmenu.ftl` — "low overhead" is rendered as "lite pålägg" (little markup/cold cuts) instead of the term used by the other presets.
    - Current: `med lite pålägg`
    - Source: `Recommended preset for most web app debugging, with low overhead.`
    - Suggest: `med låg omkostnad`
    - The sibling preset descriptions use "låg omkostnad"/"Hög omkostnad" for overhead; "pålägg" means price markup or sandwich topping and does not convey performance overhead.
- `smartwindow-group-tabs-duplicates-list` — `browser/browser/autoTabGrouping.ftl` — "Duplicate tabs" is rendered with the verb "Duplicera" (duplicate), exactly what the developer comment warns against.
    - Current: `Duplicera flikar att stänga`
    - Source: `aria-label: Duplicate tabs to close`
    - Suggest: `Duplicerade flikar att stänga`
    - The comment says: '"Duplicate tabs" refers to tabs that are copies of each other; it is not a verb telling the user to duplicate anything.' The accessible name now reads as a command to duplicate tabs.
- `main-context-menu-preview-link` — `browser/browser/browserContext.ftl` — The action "Preview Link" is rendered as a compound noun "Förhandsgranskningslänk" (preview link).
    - Current: `Förhandsgranskningslänk`
    - Source: `accesskey: J label: Preview Link`
    - Suggest: `Förhandsgranska länk`
    - Every other item in this context menu is a verb phrase; as written the entry names an object instead of the action it performs.
- `confirmation-hint-pin-tab-description` — `browser/browser/confirmationHints.ftl` — "Right-click the tab to unpin it" is rendered as "to remove it".
    - Current: `Högerklicka på fliken för att ta bort den.`
    - Source: `Right-click the tab to unpin it.`
    - Suggest: `Högerklicka på fliken för att lossa den.`
    - "ta bort den" tells the user the action deletes/closes the tab, whereas the action only unpins it.
- `contextual-manager-passwords-add-password-success-button` — `browser/browser/contextual-manager.ftl` — The button label "View" is translated as the noun "Vy" (a view/layout) instead of the verb.
    - Current: `Vy`
    - Source: `View`
    - Suggest: `Visa`
    - This is an action button that opens the newly added password; "Vy" is the noun for a display layout and is not an action in Swedish UI.
- `customkeys-search-input` — `browser/browser/customkeys.ftl` — "Search shortcuts" is rendered as a compound noun meaning "search shortcuts" (shortcuts for searching), not the search action.
    - Current: `Sökgenvägar`
    - Source: `aria-label: Search shortcuts placeholder: Search shortcuts`
    - Suggest: `Sök genvägar`
    - Comment: 'Search is a verb, as in "search through shortcuts".' The compound reads as a category of shortcuts rather than the placeholder prompting a search.
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Malformed closing tag `</a >` in `genai-settings-chat-gemini-links`
    - Current: `Genom att välja Google Gemini godkänner du <a data-l10n-name="link1">Googles användarvillkor</a>, <a data-l10n-name="link2">policyn för förbjuden användning av generativ AI</a > och <a data-l10n-name="link3">sekretessme…`
    - Source: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
    - Whitespace inside a closing tag makes it render as literal text.
- `cfr-doorhanger-extension-heading` — `browser/browser/newtab/asrouter.ftl` — Singular heading "Recommended Extension" rendered in the plural.
    - Current: `Rekommenderade tillägg`
    - Source: `Recommended Extension`
    - Suggest: `Rekommenderat tillägg`
    - The doorhanger heads a single add-on recommendation; the parallel string cfr-doorhanger-feature-heading is correctly singular ("Rekommenderad funktion").
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — "Loading more matches" rendered with "matchningar" (matchings/pairings) instead of football matches.
    - Current: `Laddar fler matchningar…`
    - Source: `Loading more matches…`
    - Suggest: `Laddar fler matcher…`
    - The developer comment says this is shown when more matches are being fetched. "Matchningar" means matchings/correspondences, not sports matches, which the rest of the widget calls "matcher".
- `newtab-sports-widget-team-name-label-eng` — `browser/browser/newtab/newtab.ftl` — The FIFA team name "England" is rendered as "Storbritannien" (Great Britain), naming a different entity.
    - Current: `Storbritannien`
    - Source: `label: England`
    - Suggest: `England`
    - The group comment says these are FIFA country codes; ENG is England, which competes separately from Scotland (sco, correctly "Skottland"). "Storbritannien" is the United Kingdom/Great Britain, not the England team.
- `newtab-sports-widget-view-matches` — `browser/browser/newtab/newtab.ftl` — "View matches" (football matches) rendered as "Visa träffar" (view hits/search results).
    - Current: `Visa träffar`
    - Source: `label: View matches`
    - Suggest: `Visa matcher`
    - In the sports widget "matches" are football matches, translated elsewhere in the same file as "matcher" (e.g. newtab-sports-widget-no-upcoming-matches). "Träffar" means hits/search results.
- `newtab-topic-label-food` — `browser/browser/newtab/newtab.ftl` — The story topic "Food" is rendered as "Livsmedel" (foodstuffs/groceries).
    - Current: `Livsmedel`
    - Source: `Food`
    - Suggest: `Mat`
    - This is a content topic for food-related articles; "Livsmedel" is the commodity/industry term for groceries, not the subject area.
- `onboarding-new-user-survey-legal-link-label` — `browser/browser/newtab/onboarding.ftl` — Malformed closing tag `</a >` in `onboarding-new-user-survey-legal-link-label`
    - Current: `Genom att välja "{ onboarding-new-user-survey-next-button-label }" godkänner du { -brand-product-name }:s <a data-l10n-name="privacy_notice">sekretesspolicy</a >`
    - Source: `By selecting “{ onboarding-new-user-survey-next-button-label },” you agree to { -brand-product-name }’s <a data-l10n-name="privacy_notice">Privacy Notice</a>`
    - Whitespace inside a closing tag makes it render as literal text.
- `security-view-privacy-history-value` — `browser/browser/pageInfo.ftl` — "prior to today" rendered as the ungrammatical "tidigare dagar".
    - Current: `Har jag besökt den här webbplatsen tidigare dagar?`
    - Source: `Have I visited this website prior to today?`
    - Suggest: `Har jag besökt den här webbplatsen före idag?`
    - en-US asks whether the site was visited before today; "tidigare dagar" ("earlier days") is not a grammatical adverbial here and loses the reference to today.
- `places-history-search` — `browser/browser/places.ftl` — "Search history" (verb) rendered as the noun "Sökhistorik" (history of searches).
    - Current: `Sökhistorik`
    - Source: `placeholder: Search history`
    - Suggest: `Sök i historik`
    - The en-US placeholder is the imperative "Search history"; "Sökhistorik" is a compound noun meaning the user's search history. The parallel string places-search-history in the same file correctly uses "Sök i historik".
- `policy-DisableDefaultBrowserAgent` — `browser/browser/policies/policies-descriptions.ftl` — "Prevent the default browser agent from taking any actions" became "prevent the default browser from acting" — the agent is dropped from the subject.
    - Current: `Förhindra att standardwebbläsaren agerar.`
    - Source: `Prevent the default browser agent from taking any actions. Only applicable to Windows; other platforms don’t have the agent.`
    - Suggest: `Förhindra att agenten för standardwebbläsaren utför några åtgärder.`
    - The policy disables the default-browser agent, not the default browser; the sibling string policy-DisableDefaultBrowserAgent2 renders the same English correctly as "agenten för standardwebbläsaren". The following sentence in this very string still refers to "agenten", so the first sentence contradicts it.
- `policy-RelaunchRequired` — `browser/browser/policies/policies-descriptions.ftl` — The second occurrence of "relaunch" is rendered as "nylansering" (a new product launch).
    - Current: `den kommande nylanseringen`
    - Source: `Require { -brand-short-name } to be relaunched within a given period and notify the user of the upcoming relaunch.`
    - Suggest: `den kommande omstarten`
    - The same English word is correctly rendered as "återstartas" earlier in the sentence; "nylansering" means launching a product anew, not restarting the browser.
- `policy-RequestedLocales` — `browser/browser/policies/policies-descriptions.ftl` — "in order of preference" rendered as "efter ordning i inställningar" (by order in settings).
    - Current: `efter ordning i inställningar`
    - Source: `Set the list of requested locales for the application in order of preference.`
    - Suggest: `i prioritetsordning`
    - The policy takes an ordered list whose order expresses preference; the translation instead refers to an ordering found in settings, which the English does not say.
- `appearance-browser-icon-pixelated` — `browser/browser/preferences/browserIcon.ftl` — "Pixelated" rendered with the prefix av- (pixelated-out/censored)
    - Current: `Avpixlad`
    - Source: `label: Pixelated`
    - Suggest: `Pixelerad`
    - The icon name describes a pixel-art style; Swedish "avpixlad" is used for censoring something by pixelation (and the av- prefix suggests removal), whereas "pixelerad" is the plain rendering of "pixelated".
- `connection-proxy-option-wpad` — `browser/browser/preferences/connection.ftl` — Drops "system" from "system Web Proxy Auto-Discovery setting"
    - Current: `Använd inställningen för automatisk upptäckt av webbproxy`
    - Source: `accesskey: g label: Use system Web Proxy Auto-Discovery setting`
    - Suggest: `Använd systemets inställning för automatisk upptäckt av webbproxy (WPAD)`
    - The option refers specifically to the operating system's WPAD setting; without "systemets" it is indistinguishable from the adjacent "Auto-detect proxy settings" option.
- `autofill-address-area` — `browser/browser/preferences/formAutofill.ftl` — "Area" rendered as surface area instead of an administrative area
    - Current: `Yta`
    - Source: `Area`
    - Suggest: `Område`
    - The comment says this is Hong Kong's primary administrative level below the country; "Yta" means surface/square measure, not a geographic area, so the address field label names the wrong concept.
- `permissions-site-camera-desc` — `browser/browser/preferences/permissions.ftl` — Reversed subject: says the sites asked that *you* access your camera
    - Current: `Följande webbplatser har begärt att du ska komma åt din kamera.`
    - Source: `The following websites have requested to access your camera. You can specify which websites are allowed to access your camera. You can also block new requests asking to access your camera.`
    - Suggest: `Följande webbplatser har begärt att få komma åt din kamera.`
    - The en-US says the websites requested to access your camera; the Swedish says they requested that you access your camera, reversing who gets the access.
- `permissions-site-microphone-desc` — `browser/browser/preferences/permissions.ftl` — Reversed subject: says the sites asked that *you* access your microphone
    - Current: `Följande webbplatser har begärt att du ska komma åt din mikrofon.`
    - Source: `The following websites have requested to access your microphone. You can specify which websites are allowed to access your microphone. You can also block new requests asking to access your microphone.`
    - Suggest: `Följande webbplatser har begärt att få komma åt din mikrofon.`
    - The en-US says the websites requested to access your microphone; the Swedish reverses the actor, as in the parallel camera string.
- `report-broken-site-panel-reason-adblocker-moz-box-button` — `browser/browser/reportBrokenSite.ftl` — Agent reversed: the Swedish says the site is being asked to turn off the ad blocker.
    - Current: `Webbplatsen ombeds att stänga av annonsblockeraren`
    - Source: `label: Site asked to turn off ad blocker`
    - Suggest: `Webbplatsen bad mig stänga av annonsblockeraren`
    - en-US "Site asked to turn off ad blocker" means the site asked the user; the passive "Webbplatsen ombeds" makes the site the one being asked, which inverts who does what in this breakage reason.
- `split-view-menuitem-separate-tabs` — `browser/browser/tabbrowser.ftl` — Verb "Separate" rendered as the adjective "Separata" despite the developer comment.
    - Current: `Separata flikar`
    - Source: `label: Separate Tabs`
    - Suggest: `Separera flikar`
    - The comment states "Separate" is a verb (separate the split view tabs). "Separata flikar" reads as "separate tabs" (adjective), not an action; tab-context-separate-split-view in the same file correctly uses "Separera".
- `search-popover` — `browser/browser/touchbar/touchbar.ftl` — A noun phrase ("Search shortcuts" = shortcuts for search) is rendered as a verb phrase "search for shortcuts".
    - Current: `Sök genvägar`
    - Source: `Search shortcuts`
    - Suggest: `Sökgenvägar`
    - The developer comment states the string describes shortcuts for search; the split form reads as the imperative "search shortcuts" on the Touch Bar button.
- `translations-panel-settings-never-translate-site` — `browser/browser/translations.ftl` — "this site" narrowed to "den här sidan" (this page).
    - Current: `Översätt aldrig den här sidan`
    - Source: `label: Never translate this site`
    - Suggest: `Översätt aldrig den här webbplatsen`
    - The setting applies to the whole site, and translations-settings-never-translate-sites-description uses "webbplatser"; "den här sidan" is also what translations-panel-header uses for a single page, so the two scopes become indistinguishable.
- `unified-extensions-mb-blocklist-warning-multiple2` — `browser/browser/unifiedExtensions.ftl` — The .message repeats the count heading instead of the warning text, dropping the risk notice.
    - Current: `{ $extensionsCount } tillägg inaktiverade`
    - Source: `heading: {$extensionsCount ->} [other] { $extensionsCount } extensions disabled message: Some of your extensions are restricted and have been disabled. You can enable them in settings, but this may be risky.`
    - Suggest: `Vissa av dina tillägg är begränsade och har inaktiverats. Du kan aktivera dem i inställningarna, men det kan vara riskabelt.`
    - en-US message is "Some of your extensions are restricted and have been disabled. You can enable them in settings, but this may be risky." The Swedish message body only restates the number of disabled extensions, so the user never learns they can re-enable them or that doing so is risky.
- `unblockTypeMalware` — `browser/chrome/browser/downloads/downloads.properties` — "will harm your computer" weakened to "can harm"
    - Current: `annat farligt program som kan skada din dator`
    - Source: `This file contains a virus or other malware that will harm your computer.`
    - Suggest: `annat farligt program som kommer att skada din dator`
    - The en-US states the malware will harm the computer; the Swedish only says it may, and the sibling string blockedPotentiallyUnwanted ("may harm") already uses "kan skada", collapsing the severity distinction the comment describes.
- `inadequateSecurityError` — `browser/chrome/overrides/appstrings.properties` — Negation dropped: "inadequate level of security" rendered as an adequate level
    - Current: `Webbplatsen försökte förhandla fram en lämplig nivå av säkerhet.`
    - Source: `The website tried to negotiate an inadequate level of security.`
    - Suggest: `Webbplatsen försökte förhandla fram en otillräcklig säkerhetsnivå.`
    - en-US says the site tried to negotiate an *inadequate* level of security; "lämplig" means suitable/adequate, reversing the reason for the error page.
- `accessibility-text-label-issue-figure` — `devtools/client/accessibility.ftl` — HTML <figure> elements rendered as "Siffror" (digits/numbers).
    - Current: `Siffror med valfria bildtexter ska märkas med namn.`
    - Source: `Figures with optional captions should be labeled. <a>Learn more</a>`
    - Suggest: `Figurer med valfria bildtexter ska märkas med namn.`
    - en-US "Figures with optional captions" refers to <figure> elements; "Siffror" means numerals, so the accessibility check text names the wrong thing entirely.
- `player.animationOverallEasingLabel` — `devtools/client/animationinspector.properties` — "Overall easing" rendered as "Total lättnad" (relief).
    - Current: `Total lättnad:`
    - Source: `Overall easing:`
    - Suggest: `Total easing:`
    - "Easing" is the animation timing curve; "lättnad" means relief/alleviation and conveys nothing about animation easing.
- `manifest-item-presentation` — `devtools/client/application.ftl` — Manifest section "Presentation" rendered as "Orientering" (orientation).
    - Current: `Orientering`
    - Source: `Presentation`
    - Suggest: `Presentation`
    - The section covers presentation-related manifest members, not only orientation; the heading names a different thing than en-US.
- `compatibility-issue-occurrences` — `devtools/client/compatibility.ftl` — "occurrences" rendered as "händelser" (events).
    - Current: `[one] { $number } händelse`
    - Source: `{$number ->} [one] { $number } occurrence [other] { $number } occurrences`
    - Suggest: `[one] { $number } förekomst`
    - The developer comment says this is the number of nodes where the issue occurred; "händelse" means event, which is a different concept in a devtools surface that also talks about events.
- `copyToClipboard.label` — `devtools/client/debugger.properties` — Context-menu command "Copy to clipboard" rendered as the past-tense statement "Kopierad till urklipp".
    - Current: `Kopierad till urklipp`
    - Source: `Copy to clipboard`
    - Suggest: `Kopiera till urklipp`
    - The string labels an action the user can take; the Swedish states that copying already happened.
- `framework.disableGrouping` — `devtools/client/debugger.properties` — "framework grouping" rendered as "ramgruppering" (frame grouping).
    - Current: `Inaktivera ramgruppering`
    - Source: `Disable framework grouping`
    - Suggest: `Inaktivera ramverksgruppering`
    - "ram" is the word used for stack frames elsewhere in this file; a framework is "ramverk", so the menu item reads as frame grouping.
- `scopes.block` — `devtools/client/debugger.properties` — The noun "Block" (code block) rendered as the verb "Blockera" (to block).
    - Current: `Blockera`
    - Source: `Block`
    - Suggest: `Block`
    - The developer comment states it refers to a block of code in the Scopes pane; "Blockera" tells the user to block something.
- `dropShadowPlaceholder` — `devtools/client/filterwidget.properties` — Placeholder "x y radius color" collapsed into the nonsense compound "färgradie".
    - Current: `x y färgradie`
    - Source: `x y radius color`
    - Suggest: `x y radie färg`
    - The placeholder tells the user which four values to enter; merging "radius" and "color" into one invented word loses one parameter.
- `eventsTooltip.Capturing` — `devtools/client/inspector.properties` — The DOM event phase "Capturing" rendered as "Lagrar" (storing).
    - Current: `Lagrar`
    - Source: `Capturing`
    - Suggest: `Capturing`
    - Capturing is the event propagation phase shown next to Bubbling; "Lagrar" says the listener stores something.
- `eventsTooltip.unknownLocationExplanation` — `devtools/client/inspector.properties` — "the code is transpiled by a utility such as Babel" rendered as the code having been translated incorrectly.
    - Current: `Kanske har koden översatts fel med ett verktyg som Babel.`
    - Source: `The original location of this listener cannot be detected. Maybe the code is transpiled by a utility such as Babel.`
    - Suggest: `Kanske har koden transpilerats av ett verktyg som Babel.`
    - en-US states a neutral fact about transpilation; "översatts fel" asserts the build tool made an error.
- `markupView.scrollableBadge.tooltip` — `devtools/client/inspector.properties` — "scrollable overflow" rendered as "rullbar övergång" (transition).
    - Current: `Detta element har rullbar övergång.`
    - Source: `This element has scrollable overflow.`
    - Suggest: `Detta element har rullningsbart överflöde.`
    - "övergång" means transition; the interactive variant of the same tooltip correctly uses "överflöden".
- `layout.gridDisplaySettings` — `devtools/client/layout.properties` — "Grid Display Settings" rendered as monitor/screen settings.
    - Current: `Bildskärmsinställningar för rutnät`
    - Source: `Grid Display Settings`
    - Suggest: `Visningsinställningar för rutnät`
    - "Display" here means how the grid is displayed; "bildskärm" means the physical monitor.
- `snapshot.io.save.window` — `devtools/client/memory.properties` — "Save Snapshot" dialog title rendered as saving a screenshot.
    - Current: `Spara skärmbild`
    - Source: `Save Snapshot`
    - Suggest: `Spara ögonblicksbild`
    - Same snapshot/screenshot confusion in the file picker title.
- `snapshot.state.saving` — `devtools/client/memory.properties` — The same en-US string "Saving snapshot…" is rendered "skärmbild" here and "ögonblicksbild" in snapshot.state.saving.full.
    - Current: `Sparar skärmbild…`
    - Source: `Saving snapshot…`
    - Suggest: `Sparar ögonblicksbild…`
    - Two renderings of one source string in the same tool, one of which means screenshot.
- `take-snapshot` — `devtools/client/memory.properties` — Heap "snapshot" rendered as "skärmbild" (screenshot).
    - Current: `Ta skärmbild`
    - Source: `Take snapshot`
    - Suggest: `Ta ögonblicksbild`
    - A heap snapshot is not a screenshot; the same file uses the correct "ögonblicksbild" in snapshot.state.*.full, so the panel mixes both.
- `toolbar.view.treemap.tooltip` — `devtools/client/memory.properties` — "larger blocks account for" rendered as the nonsense compound "blockkonto".
    - Current: `större blockkonto för en större procent av minnesanvändning`
    - Source: `Visualize memory usage: larger blocks account for a larger percent of memory usage`
    - Suggest: `större block motsvarar en större andel av minnesanvändningen`
    - "account for" was taken as the noun "account"; the sentence no longer states what the tree map shows.
- `charts.cacheDisabled` — `devtools/client/netmonitor.properties` — "Empty cache" rendered as "Inaktiverad cache" (disabled cache).
    - Current: `Inaktiverad cache`
    - Source: `Empty cache`
    - Suggest: `Tom cache`
    - The performance chart compares a primed cache with an empty one; it says nothing about the cache being disabled.
- `netmonitor.cache.fetchCount` — `devtools/client/netmonitor.properties` — The column label "Fetch Count" rendered as the command "Hämta antal" (fetch the count).
    - Current: `Hämta antal`
    - Source: `Fetch Count`
    - Suggest: `Antal hämtningar`
    - It is a tree-view label for how many times the cached object was fetched, not an action.
- `netmonitor.custom.postData` — `devtools/client/netmonitor.properties` — The label "Request Body" misparsed as the command "Begär innehåll" (request content).
    - Current: `Begär innehåll`
    - Source: `Request Body`
    - Suggest: `Begärans innehåll`
    - It labels the request body field in the custom request form; the Swedish reads as an imperative verb.
- `netmonitor.ws.context.controlFrames` — `devtools/client/netmonitor.properties` — The WebSocket filter "Control" (control frames) rendered as the verb "Kontrollera".
    - Current: `Kontrollera`
    - Source: `Control`
    - Suggest: `Kontrollramar`
    - The item filters control frames; "Kontrollera" reads as a command to check something.
- `networkMenu.sortedAsc` — `devtools/client/netmonitor.properties` — "Sorted ascending" rendered as descending.
    - Current: `Fallande ordning`
    - Source: `Sorted ascending`
    - Suggest: `Stigande ordning`
    - The tooltip is shown on ascending-sorted columns; it states the opposite sort direction.
- `networkMenu.sortedDesc` — `devtools/client/netmonitor.properties` — "Sorted descending" rendered as ascending.
    - Current: `Stigande ordning`
    - Source: `Sorted descending`
    - Suggest: `Fallande ordning`
    - Mirror of the sortedAsc swap; the two tooltips are reversed.
- `paramsFilterText` — `devtools/client/netmonitor.properties` — "Filter Request Parameters" misparsed as "parameters for the filter request".
    - Current: `Parametrar för filterbegäran`
    - Source: `Filter Request Parameters`
    - Suggest: `Filtrera förfrågningsparametrar`
    - The string is the filter input placeholder in the request tab; the Swedish turns "filter" into part of a noun phrase and loses the action.
- _…and 69 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `genai-settings-chat-claude-links` — `browser/browser/genai.ftl` — The brand name Anthropic is misspelled twice as "Antropic"/"Antropics".
    - Current: `Genom att välja Antropic Claude, godkänner du`
    - Source: `By choosing Anthropic Claude, you agree to the Anthropic <a data-l10n-name="link1">Consumer Terms of Service</a>, <a data-l10n-name="link2">Usage Policy</a>, and <a data-l10n-name="link3">Privacy Policy</a>.`
    - Suggest: `Genom att välja Anthropic Claude godkänner du`
    - The same brand is spelled correctly in genai-onboarding-claude-tooltip ("Anthropic Claude"); brand names must not be altered.
- `autofill-address-department` — `browser/browser/preferences/formAutofill.ftl` — Administrative "Department" rendered as an organizational division
    - Current: `Avdelning`
    - Source: `Department`
    - Suggest: `Departement`
    - The comment marks this as the primary administrative subdivision in Nicaragua and Colombia; Swedish "Avdelning" means a department of a company or store, while the administrative unit is "departement".
- `permission.register-protocol-handler.label` — `browser/chrome/browser/sitePermissions.properties` — "Fråga för att öppna" means "ask in order to open", not "ask to open" (the site may ask whether to open app links).
    - Current: `Fråga för att öppna applänkar`
    - Source: `Ask to open app links`
    - Suggest: `Fråga om att öppna applänkar`
    - The comment says this permission controls whether the site may ask to open app links. "för att" expresses purpose, which changes the meaning. It is also inconsistent with "fråga om att öppna applänkar" in preferences.ftl.
- `language-name-se` — `toolkit/toolkit/intl/languageNames.ftl` — "Northern Sami" rendered as the name of the whole Sami language group.
    - Current: `Samiska`
    - Source: `Northern Sami`
    - Suggest: `Nordsamiska`
    - en-US language-name-se is "Northern Sami"; "samiska" names the family, not this specific language.
- `region-name-sz-2019` — `toolkit/toolkit/intl/regionNames.ftl` — Country named by its former name Swaziland instead of Eswatini.
    - Current: `Swaziland`
    - Source: `Eswatini`
    - Suggest: `Eswatini`
    - en-US region-name-sz-2019 is "Eswatini"; the id's 2019 suffix marks the rename.

### C. Grammar, agreement & spelling

- `about-logins-import-report-title` — `browser/browser/aboutLogins.ftl` — "Import Summary" is rendered as the imperative verb plus noun ("Importera sammanfattning" = import a summary).
    - Current: `Importera sammanfattning`
    - Source: `Import Summary`
    - Suggest: `Importsammanfattning`
    - The page heading names a report about the import; as written it instructs the user to import a summary. Compare about-logins-import-dialog-title, which correctly uses the noun form "Import slutförd".
- `addon-confirm-install-some-unsigned-message` — `browser/browser/addonNotifications.ftl` — Singular "varav någon är overifierad" where the source says some of several add-ons are unverified.
    - Current: `varav någon är overifierad`
    - Source: `{$addonCount ->} [other] Caution: This site would like to install { $addonCount } add-ons in { -brand-short-name }, some of which are unverified. Proceed at your own risk.`
    - Suggest: `varav några är overifierade`
    - The message is only shown for at least two add-ons (per the developer comment), so the singular agreement is wrong.
- `webext-perms-sideload-menu-item` — `browser/browser/addonNotifications.ftl` — Missing preposition after "lagts till", leaving "har lagts till Firefox".
    - Current: `har lagts till { -brand-short-name }`
    - Source: `{ $addonName } added to { -brand-short-name }`
    - Suggest: `har lagts till i { -brand-short-name }`
    - In Swedish "lägga till" requires "i" before the target; without it the phrase is ungrammatical.
- `ai-window-no-memories-learning-off` — `browser/browser/aiFeatures.ftl` — Agreement error: "är avstängd" with an infinitive-clause subject requires the neuter "avstängt".
    - Current: `Att lära från aktivitet är avstängd`
    - Source: `description: Learning from activity is off, so { -smart-window-brand-name } isn’t creating memories. label: No memories to show`
    - Suggest: `Att lära från aktivitet är avstängt`
    - The subject is a clause (neuter), so the predicative adjective must be "avstängt".
- `aiwindow-feedback-include-page-content` — `browser/browser/aiWindow.ftl` — "chat" left in the English spelling instead of Swedish "chatt".
    - Current: `i denna chat`
    - Source: `Share the pages referenced in this chat`
    - Suggest: `i den här chatten`
    - The rest of the file consistently uses "chatt"/"chattar"; "chat" is a misspelling in Swedish.
- `appmenuitem-fxa-sync-off-description` — `browser/browser/appmenu.ftl` — Mixed verb forms: imperative "Skydda" coordinated with the infinitive "komma åt".
    - Current: `Skydda och komma åt dina bokmärken`
    - Source: `Protect and access your bookmarks, passwords, and more anywhere.`
    - Suggest: `Skydda och kom åt dina bokmärken`
    - Both verbs render the same imperative in en-US ("Protect and access"); the coordination is ungrammatical as written.
- `identity-permissions-storage-access-hint` — `browser/browser/browser.ftl` — Missing plural agreement: "global kakor" instead of "globala kakor".
    - Current: `kan använda global kakor`
    - Source: `These parties can use cross-site cookies and site data while you are on this site.`
    - Suggest: `kan använda globala kakor`
    - The panel header in the same surface uses "Globala kakor"; the adjective must agree with the plural noun.
- `trustpanel-connection-label-secure` — `browser/browser/browser.ftl` — Missing verb: "Anslutningen säker" is not a grammatical Swedish clause.
    - Current: `Anslutningen säker`
    - Source: `Connection secure`
    - Suggest: `Anslutningen är säker`
    - The paired string trustpanel-connection-label-insecure reads "Anslutningen är inte säker", and identity-connection-secure reads "Anslutningen är säker".
- `webext-default-search-description` — `browser/browser/extensionsUI.ftl` — The sentence is garbled: "vill du ändra" turns the statement into a question mid-sentence.
    - Current: `{ $addonName } vill du ändra din förvalda sökmotor från { $currentEngine } till { $newEngine }.`
    - Source: `{ $addonName } would like to change your default search engine from { $currentEngine } to { $newEngine }. Is that OK?`
    - Suggest: `{ $addonName } vill ändra din förvalda sökmotor från { $currentEngine } till { $newEngine }.`
    - The en-US is a statement ("would like to change"); the Swedish reads "AddonName, do you want to change…" followed by a period and then "Är det OK?", which is ungrammatical.
- `callout-firefox-view-tab-pickup-subtitle` — `browser/browser/featureCallout.ftl` — Wrong pronoun form: "öppna de här" instead of the object form "öppna dem här".
    - Current: `öppna de här`
    - Source: `Quickly grab open tabs from your phone and open them here for maximum flow.`
    - Suggest: `öppna dem här`
    - "de" is the subject form; as written the phrase reads "open these" rather than "open them here".
- `firefoxview-syncedtabs-synctabs-header-2` — `browser/browser/firefoxView.ftl` — Misspelled compound "Flikarsynkronisering".
    - Current: `Flikarsynkronisering är avstängd`
    - Source: `Tab syncing is off`
    - Suggest: `Fliksynkronisering är avstängd`
    - The same term is spelled "Fliksynkronisering" in firefoxview-tabpickup-fxa-admin-disabled-header-2; "Flikar-" is not a valid compound form.
- `ipprotection-connection-status-paused-title-2` — `browser/browser/ipProtection.ftl` — Gender agreement: "pausad" instead of neuter "pausat" for VPN.
    - Current: `VPN är pausad`
    - Source: `(value): VPN is paused aria-label: VPN is paused`
    - Suggest: `VPN är pausat`
    - The file treats VPN as a neuter noun elsewhere ("VPN är avstängt", "VPN är inte tillgängligt"), so the participle must be neuter.
- `ipprotection-site-settings-callout-title` — `browser/browser/ipProtection.ftl` — "vart" (to where, motion) used where static "var" (where) is required.
    - Current: `Välj vart du använder VPN`
    - Source: `Choose where you use VPN`
    - Suggest: `Välj var du använder VPN`
    - No motion is involved; the equivalent settings strings use "var" (e.g. "dölja var du surfar").
- `speech-recognition-model-download-message` — `browser/browser/permissions.ftl` — Missing "att" after "så", giving subordinate word order in a main clause.
    - Current: `så ljudet aldrig lämnar din enhet`
    - Source: `{ -brand-short-name } runs speech recognition locally, so the audio never leaves your device. To set this up, a ~{ $sizeMB } MB download will start when you continue.`
    - Suggest: `så att ljudet aldrig lämnar din enhet`
    - With coordinating "så" the order must be "lämnar aldrig"; with the subordinate order used here the conjunction must be "så att".
- `appearance-browser-icon-momo` — `browser/browser/preferences/browserIcon.ftl` — Social-media handle altered although the comment says it must be kept verbatim
    - Current: `Skapad av @heyheymomomodraws`
    - Source: `description: Created by @heyheymomodraws label: Momo`
    - Suggest: `Skapad av @heyheymomodraws`
    - The developer comment states "@heyheymomodraws is the social-media handle of the icon's author and must be kept verbatim"; the Swedish has an extra "mo" (@heyheymomomodraws), crediting a non-existent account.
- `permissions-site-notification-desc` — `browser/browser/preferences/permissions.ftl` — "notifications" rendered as both "aviseringar" and "meddelanden" in one string
    - Current: `Följande webbplatser har begärt att skicka meddelanden. Du kan ange vilka webbplatser som får skicka aviseringar. Du kan också blockera nya förfrågningar om att tillåta meddelanden.`
    - Source: `The following websites have requested to send you notifications. You can specify which websites are allowed to send you notifications. You can also block new requests asking to allow notifications.`
    - Suggest: `Följande webbplatser har begärt att få skicka aviseringar. Du kan ange vilka webbplatser som får skicka aviseringar. Du kan också blockera nya förfrågningar om att tillåta aviseringar.`
    - The same en-US term "notifications" is rendered two different ways within one paragraph, and the dialog title uses "aviseringar"; "meddelanden" (messages) is the inconsistent one.
- `permissions-site-xr-window2` — `browser/browser/preferences/permissions.ftl` — "Permissions" rendered as "Rättigheter" where the sibling dialogs use "Behörigheter"
    - Current: `Rättigheter för virtuell verklighet`
    - Source: `style: { permissions-window2.style } title: Settings - Virtual Reality Permissions`
    - Suggest: `Behörigheter för virtuell verklighet`
    - All other "Settings - … Permissions" titles in this file use "Behörigheter" (notifications, location, camera, microphone); "Rättigheter" (rights) is the odd one out in the same surface.
- `lockwise-scanned-text-breached-logins` — `browser/browser/protections.ftl` — Plural participle with a singular subject in the [one] variant.
    - Current: `1 lösenord kan ha blivit exponerade vid ett dataintrång.`
    - Source: `{$count ->} [one] 1 password may have been exposed in a data breach. [other] { $count } passwords may have been exposed in a data breach.`
    - Suggest: `1 lösenord kan ha blivit exponerat vid ett dataintrång.`
    - "1 lösenord" is singular neuter and requires "exponerat"; "exponerade" is the plural form.
- `protection-report-settings-link` — `browser/browser/protections.ftl` — Missing hyphen in the coordinated compound "integritets- och säkerhetsinställningar".
    - Current: `Hantera dina integritets och säkerhetsinställningar`
    - Source: `Manage your privacy and security settings`
    - Suggest: `Hantera dina integritets- och säkerhetsinställningar`
    - Swedish requires a hanging hyphen when the first element of a compound is coordinated; without it "integritets" is a stray fragment.
- `protections-panel-cookie-banner-blocker-header` — `browser/browser/protectionsPanel.ftl` — Missing preposition in "Blockering kakbanners".
    - Current: `Blockering kakbanners`
    - Source: `Cookie Banner Blocker`
    - Suggest: `Blockering av kakbanners`
    - Swedish needs "av" between the deverbal noun and its object; the same file writes "blockering av kakbanners" in protections-panel-cookie-banner-blocker-view-turn-off-for-site.
- `protections-panel-cookie-banner-view-cookie-clear-warning` — `browser/browser/protectionsPanel.ftl` — Bare infinitive used as subject without "Att".
    - Current: `Rensa alla kakor kan logga ut dig eller tömma kundvagnar.`
    - Source: `{ -brand-short-name } will clear this site’s cookies and refresh the page. Clearing all cookies may sign you out or empty shopping carts.`
    - Suggest: `Att rensa alla kakor kan logga ut dig eller tömma kundvagnar.`
    - As written the sentence starts as an imperative and then takes a modal verb, which is ungrammatical; the subject infinitive needs "Att".
- `tab-context-move-tabs2` — `browser/browser/tabContextMenu.ftl` — Spelling error "flikat" for "flikar" in the plural variant.
    - Current: `Flytta { $tabCount } flikat till`
    - Source: `accesskey: v label: {$tabCount ->} [1] Move Tab to [other] Move { $tabCount } Tabs to`
    - Suggest: `Flytta { $tabCount } flikar till`
    - "flikat" is not a word; the plural of "flik" is "flikar", as used in every other plural variant in this file.
- `tabbrowser-allow-dialogs-to-get-focus` — `browser/browser/tabbrowser.ftl` — Ungrammatical sentence; the infinitive clause "to take you to their tab" is rendered as a finite verb.
    - Current: `Tillåt liknande meddelanden från { $domain } leder dig till deras flik`
    - Source: `label: Allow notifications like this from { $domain } to take you to their tab`
    - Suggest: `Tillåt liknande meddelanden från { $domain } att ta dig till deras flik`
    - "Tillåt … leder dig" is not a possible Swedish construction; the checkbox label is broken and its meaning (allowing the notification to switch tabs) is obscured.
- `webrtc-allow-share-speaker-with-file` — `browser/browser/webrtcIndicator.ftl` — Indicative "Tillåter" instead of the imperative/question form used by every sibling prompt.
    - Current: `Tillåter den här lokala filen att använda andra högtalare?`
    - Source: `Allow this local file to use other speakers?`
    - Suggest: `Tillåt den här lokala filen att använda andra ljudenheter?`
    - en-US "Allow this local file to use other speakers?" is a permission request; "Tillåter …?" reads as a question about whether the file permits something, inverting the prompt.
- `sslv3Used` — `browser/chrome/overrides/appstrings.properties` — Product name replaced with a generic "Denna applikation"
    - Current: `Denna applikation kan inte garantera säkerheten för dina data på %S`
    - Source: `Firefox cannot guarantee the safety of your data on %S because it uses SSLv3, a broken security protocol.`
    - Suggest: `Firefox kan inte garantera säkerheten för dina data på %S`
    - The en-US names Firefox, as this file does throughout (and the Swedish keeps "Firefox" in every other string); replacing it with "this application" drops the product attribution.
- `accessibility-text-label-issue-document-title` — `devtools/client/accessibility.ftl` — The code-marked attribute name "title" was translated.
    - Current: `Dokument måste ha en <code>titel</code>.`
    - Source: `Documents must have a <code>title</code>. <a>Learn more</a>`
    - Suggest: `Dokument måste ha en <code>title</code>.`
    - The <code> wrapper marks it as the literal HTML title element/attribute, which must not be localized.
- `accessibility-text-label-issue-optgroup-label2` — `devtools/client/accessibility.ftl` — The HTML element name "optgroup" was translated to "optgrupp".
    - Current: `<span>optgrupp</span>`
    - Source: `Use a <code>label</code> attribute to label an <span>optgroup</span>. <a>Learn more</a>`
    - Suggest: `<span>optgroup</span>`
    - The element name inside the markup span is a code identifier (the shared string keeps "optgroup"); "optgrupp" is not a valid HTML element.
- `screenshotFileManual` — `devtools/shared/screenshot.properties` — The literal parameter value "True" was translated to "Sant".
    - Current: `Sant om skärmdumpen ska spara filen`
    - Source: `True if the screenshot should save the file even when other options are enabled (eg. clipboard).`
    - Suggest: `True om skärmdumpen ska spara filen`
    - The value the user must type is the boolean literal true; screenshotClipboardManual correctly keeps "True".
- `webconsole-commands-usage-block` — `devtools/shared/webconsole-commands.ftl` — The parameter token URL_STRING was altered to URLSTRING.
    - Current: `Den accepterar endast ett URLSTRING-argument`
    - Source: `:block URL_STRING  Start blocking network requests    It accepts only one URL_STRING argument, an unquoted string which will be used to block all requests whose URL includes this string.   Use :unblock or the Network Mo…`
    - Suggest: `Den accepterar endast ett URL_STRING-argument`
    - The usage text names the command's literal argument, shown as URL_STRING on the line above; dropping the underscore mismatches the identifier.
- `webconsole.group.csp` — `devtools/shared/webconsole.properties` — The header name Content-Security-Policy was translated despite the do-not-translate comment.
    - Current: `Varningar för innehåll-säkerhet-policy`
    - Source: `Content-Security-Policy warnings`
    - Suggest: `Content-Security-Policy-varningar`
    - The developer comment explicitly says not to translate 'Content-Security-Policy' as it is the header name.
- `MediaStreamAudioSourceNodeCrossOrigin` — `dom/chrome/dom/dom.properties` — Wrong API name: string names createMediaElementSource instead of createMediaStreamSource.
    - Current: `MediaStream skickad till createMediaElementSource`
    - Source: `The MediaStream passed to createMediaStreamSource has a cross-origin resource, the node will output silence.`
    - Suggest: `MediaStream skickad till createMediaStreamSource`
    - The developer comment says do not translate MediaStream and createMediaStreamSource; the Swedish copied the function name from the preceding string.
- `RequestStorageAccessNullPrincipal` — `dom/chrome/dom/dom.properties` — Wrong sandbox token: en-US says allow-same-origin, Swedish says allow-storage-access-by-user-activation.
    - Current: `i en sandlådad iframe utan allow-storage-access-by-user-activation i sandbox-attributet`
    - Source: `document.requestStorageAccess() may not be called on a document with an opaque origin, such as a sandboxed iframe without allow-same-origin in its sandbox attribute.`
    - Suggest: `till exempel en sandlådad iframe utan allow-same-origin i sandbox-attributet`
    - The comment lists allow-same-origin as the do-not-translate token for this string; the token from the next string was used instead, and “such as” was dropped.
- `RewriteYouTubeEmbed` — `dom/chrome/dom/dom.properties` — Brand name miscapitalized as “Youtube”.
    - Current: `Omskrivning av gammal Youtube Flash-inbäddad`
    - Source: `Rewriting old-style YouTube Flash embed (%S) to iframe embed (%S). Please update page to use iframe instead of embed/object, if possible.`
    - Suggest: `Omskrivning av gammal YouTube Flash-inbäddning`
    - The developer comment says do not translate 'YouTube'; the capital T is part of the trademark. Same in RewriteYouTubeEmbedPathParams.
- `TooLargeDashedRadius` — `dom/chrome/layout/css.properties` — The CSS keyword values ‘dashed’/‘dotted’ were translated.
    - Current: `för ‘streckad’ stil`
    - Source: `Border radius is too large for ‘dashed’ style (the limit is 100000px). Rendering as solid.`
    - Suggest: `för stilen ‘dashed’`
    - The quoted tokens are CSS keyword values a developer must type; translating them makes the console message unusable for lookup. Same in TooLargeDottedRadius.
- `BlockFileScriptWithWrongMimeType` — `dom/chrome/security/security.properties` — The do-not-translate scheme “file: URI” was translated to “fil: URI”.
    - Current: `Laddar skript från fil: URI`
    - Source: `Loading script from file: URI (“%1$S”) was blocked because its MIME type (“%2$S”) is not a valid JavaScript MIME type.`
    - Suggest: `Laddar skript från file: URI`
    - The developer comment says do not translate "file: URI"; “fil:” is not a valid scheme.
- `SSL_ERROR_MISSING_EXTENDED_MASTER_SECRET` — `security/manager/chrome/pipnss/nsserrors.properties` — Technical identifier mangled: extended_master_secre.
    - Current: `extended_master_secre utökning`
    - Source: `The peer tried to resume without a correct extended_master_secret extension.`
    - Suggest: `extended_master_secret-utökning`
    - The TLS extension name is an identifier and must be spelled exactly, as it is in the neighbouring SSL_ERROR_UNEXPECTED_EXTENDED_MASTER_SECRET.
- `addon-badge-line4` — `toolkit/toolkit/about/aboutAddons.ftl` — Hard-coded vendor name expanded to “Mozilla Firefox”
    - Current: `Officiellt tillägg byggt av Mozilla Firefox.`
    - Source: `title: Official extension built by Mozilla. Meets security and performance standards`
    - Suggest: `Officiellt tillägg byggt av Mozilla.`
    - The en-US hard-codes only “Mozilla” with the comment explaining the extensions are built by Mozilla; adding “Firefox” attributes the build to a different entity than the source states.
- `about-glean-label-for-ping-names` — `toolkit/toolkit/about/aboutGlean.ftl` — Code identifier `event` changed to `events` and “metrics” dropped
    - Current: `Annars är standardvärdena för <code>events</code>`
    - Source: `Select from the preceding list the ping your instrumentation is in. If it’s in a <a data-l10n-name="custom-ping-link">custom ping</a>, choose that one. Otherwise, the default for <code>event</code> metrics is the <code>…`
    - Suggest: `Annars är standardvärdet för <code>event</code>-mätvärden`
    - The en-US distinguishes `event` metrics (the metric type) from the `events` ping; the comment marks <code> content as untranslatable. The Swedish names the wrong identifier and loses “metrics”.
- `glean-debug-ping-viewer-brand-name` — `toolkit/toolkit/about/aboutGlean.ftl` — Tool name partly translated as an imperative verb
    - Current: `{ -glean-brand-name } Felsök Ping Viewer`
    - Source: `{ -glean-brand-name } Debug Ping Viewer`
    - Suggest: `{ -glean-brand-name } Debug Ping Viewer`
    - “Glean Debug Ping Viewer” is the name of the external tool the link points to; translating only “Debug” to the imperative “Felsök” yields a half-translated product name.
- `about-webauthn-auth-info-true` — `toolkit/toolkit/about/aboutWebauthn.ftl` — Boolean value translated despite do-not-translate comment
    - Current: `Sant`
    - Source: `True`
    - Suggest: `True`
    - The developer comment says “True should not be translated”; the parallel option fields (about-webauthn-auth-option-true/false) correctly keep “True”/“False”. The same applies to about-webauthn-auth-info-false (“Falskt”).
- `url-classifier-content-classifier-col-important` — `toolkit/toolkit/about/url-classifier.ftl` — Syntax keyword “Important” translated despite do-not-translate comment
    - Current: `Viktigt`
    - Source: `Important`
    - Suggest: `Important`
    - The developer comment states “‘Important’ should not be translated as it refers to technical syntax” (the filter-list `important` option).
- `-mdn-brand-name` — `toolkit/toolkit/branding/brandings.ftl` — The brand "MDN Web Docs" is partly translated.
    - Current: `MDN webbdokument`
    - Source: `MDN Web Docs`
    - Suggest: `MDN Web Docs`
    - The file header states these feature names must be treated as brands and neither transliterated nor translated; sibling entries keep their English names.
- `experimental-features-link-previews-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — The macOS key name Option is translated as "Alternativ" in one variant and kept as "Option" in the parallel string.
    - Current: `tryck på Shift (⇧) plus Alternativ (⌥) eller Alt`
    - Source: `{$sel_1 ->} [macos] To learn more about a webpage before you click, hover over a link and press Shift (⇧) plus Option (⌥) or Alt. Previews can include details like title and reading time. For some webpages, AI can also…`
    - Suggest: `tryck på Shift (⇧) plus Option (⌥) eller Alt`
    - Keyboard key names are shown as printed on the keyboard; experimental-features-link-previews-description-no-ai keeps "Option (⌥)".
- `region-name-cc` — `toolkit/toolkit/intl/regionNames.ftl` — Territory name left in English although every neighbouring island group is translated.
    - Current: `Cocos (Keeling) Islands`
    - Suggest: `Kokosöarna`
    - The file consistently translates island-group names (Caymanöarna, Cooköarna, Falklandsöarna); this entry is the lone English string.

### D. Terminology, register & consistency

- `default-browser-notification-privacy-body-text` — `browser/browser/backgroundtasks/defaultagent.ftl` — Missing verb makes the sentence ungrammatical
    - Current: `Din standardwebbläsare ändrad.`
    - Source: `Your default changed. Come back to { -brand-short-name } for built-in privacy and protection.`
    - Suggest: `Din standardwebbläsare har ändrats.`
    - "Your default changed" needs a finite verb in Swedish; "Din standardwebbläsare ändrad" is not a sentence.
- `customkeys-conflict-confirm-body` — `browser/browser/customkeys.ftl` — A keyboard key is called "nyckel" (key for a lock) instead of "tangent".
    - Current: `Den här nyckeln används redan av`
    - Source: `This key is already used by “{ $conflict }”.`
    - Suggest: `Den här tangenten används redan av`
    - customkeys-conflict-confirm in the same file uses "Den här tangenten"; "nyckel" is the wrong sense of "key" in a keyboard-shortcut dialog.
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — A keyboard key is called "Nyckeln" (key for a lock) instead of "Tangenten".
    - Current: `Nyckeln kan inte användas`
    - Source: `Key cannot be used`
    - Suggest: `Tangenten kan inte användas`
    - Same surface uses "tangent" elsewhere (customkeys-conflict-confirm, customkeys-new-key); "nyckel" is the wrong sense of "key".
- `bookmark-overlay-tags-caption-label` — `browser/browser/editBookmarkOverlay.ftl` — The caption calls the field "taggar" while the field label in the same dialog is "Etiketter".
    - Current: `Använd taggar för att ordna`
    - Source: `Use tags to organize and search for bookmarks from the address bar`
    - Suggest: `Använd etiketter för att ordna`
    - bookmark-overlay-tags-2 and bookmark-overlay-tags-expander2 both use "etiketter" for "tags", so the caption refers to a control by a name the UI does not use.
- `newtab-privacy-message-milestone-week` — `browser/browser/newtab/newtab.ftl` — Missing space between the brand placeholder and the following word in the plural variant.
    - Current: `{ -brand-short-name }skyddar dig ifrån`
    - Source: `{$count ->} [one] { $count } tracker blocked this week. See what { -brand-short-name } is keeping out of your way [other] { $count } trackers blocked this week. See what { -brand-short-name } is keeping out of your way`
    - Suggest: `{ -brand-short-name } skyddar dig ifrån`
    - The [one] variant has the space; the [other] variant renders as "Firefoxskyddar dig ifrån" for users.
- `newtab-topsites-image-url-label` — `browser/browser/newtab/newtab.ftl` — The field label "Custom Image URL" is translated with the verb "Anpassa" (customize) instead of the adjective.
    - Current: `Anpassa bild-URL`
    - Source: `Custom Image URL`
    - Suggest: `Anpassad bild-URL`
    - This is a label for a text field, not a button; "Anpassa bild-URL" reads as the command "Customize image URL".
- `newtab-wallpaper-suspension-bridge` — `browser/browser/newtab/newtab.ftl` — "Photography" (the photograph) rendered as "fotografering" (the act of photographing).
    - Current: `Grå fotografering av helhängbro under dagtid`
    - Source: `Grey full-suspension bridge photography during daytime`
    - Suggest: `Grått fotografi av helhängbro under dagtid`
    - The string describes an image for screen readers; "fotografering" denotes the activity, not the picture.
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Synkronisera till mobil” but the string it names, `sync-to-mobile-button-label`, reads “Synka till mobil”
    - Current: `Skanna QR-koden för att ladda ner { -brand-product-name } för mobil. När du har installerat den, välj "Synkronisera till mobil" för att komma åt dina lösenord, bokmärken och mer när du är på språng.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Synka till mobil`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `onboarding-existing-horizontal-tabs-label` — `browser/browser/newtab/onboarding.ftl` — Spelling error: "Beåll" instead of "Behåll".
    - Current: `Beåll horisontella flikar`
    - Source: `Keep horizontal tabs`
    - Suggest: `Behåll horisontella flikar`
    - Missing letter h in the verb "behåll"; the label is visible text under the tab-layout image.
- `onboarding-genai-sidebar-title` — `browser/browser/newtab/onboarding.ftl` — Compound written as two words: "AI chatbot" instead of a hyphenated Swedish compound.
    - Current: `Testa en AI chatbot i sidofältet`
    - Source: `Try an AI chatbot in the sidebar`
    - Suggest: `Testa en AI-chattbot i sidofältet`
    - Swedish compounds an abbreviation with a following noun using a hyphen; the locale does this elsewhere ("AI-kontroller", "AI-funktioner" in policies-descriptions.ftl).
- `smartwindow-onboarding-subtitle` — `browser/browser/newtab/onboarding.ftl` — Verb form mismatch: an infinitive "jämföra" in a list of imperatives.
    - Current: `Sammanfatta, jämföra och ställ frågor utan problem.`
    - Source: `Summarize, compare, and ask questions without missing a beat.`
    - Suggest: `Sammanfatta, jämför och ställ frågor utan problem.`
    - The English is a list of imperatives (Summarize, compare, and ask); "jämföra" is the infinitive and does not agree with "Sammanfatta" and "ställ".
- `media-animated-image-type` — `browser/browser/pageInfo.ftl` — Animation "frames" translated as "ramar" (borders/frames of a picture).
    - Current: `animerad, { $frames } ramar`
    - Source: `value: {$frames ->} [one] { $type } Image (animated, { $frames } frame) [other] { $type } Image (animated, { $frames } frames)`
    - Suggest: `animerad, { $frames } bildrutor`
    - In the context of an animated image, "frame" is "bildruta" in Swedish; "ram" means a border/frame, which is also how media-border-img is translated in the same file.
- `policy-IPProtectionAvailable` — `browser/browser/policies/policies-descriptions.ftl` — Doubled construction "Förhindra att … från att" makes the sentence ungrammatical.
    - Current: `Förhindra att inbyggt VPN från att vara tillgängligt för användarna.`
    - Source: `Prevent the built-in VPN from being available to users.`
    - Suggest: `Förhindra att inbyggt VPN är tillgängligt för användarna.`
    - Either "Förhindra att X är …" or "Förhindra X från att vara …" is correct; combining both leaves a stray subordinate clause.
- `policy-LocalNetworkAccess` — `browser/browser/policies/policies-descriptions.ftl` — Adjective agreement error: "lokala nätverksåtkomst".
    - Current: `kontroller av lokala nätverksåtkomst`
    - Source: `Enable or disable local network access checks.`
    - Suggest: `kontroller av lokal nätverksåtkomst`
    - "Nätverksåtkomst" is an indefinite singular common-gender noun, so the attributive adjective must be "lokal", not the definite/plural "lokala".
- `policy-PopupBlocking2` — `browser/browser/policies/policies-descriptions.ftl` — Missing infinitive marker "att" after "Tillåt vissa webbplatser".
    - Current: `Tillåt vissa webbplatser visa popup-fönster`
    - Source: `Allow certain websites to display popups and be redirected by third-party frames.`
    - Suggest: `Tillåt vissa webbplatser att visa popup-fönster`
    - Swedish requires "att" here; compare policy-InstallAddonsPermission "Tillåt vissa webbplatser att installera tillägg" in the same file.
- `permissions-site-notification-disable-desc` — `browser/browser/preferences/permissions.ftl` — Ungrammatical mix of "förhindra att …" and "… från att"
    - Current: `Detta kommer att förhindra att webbplatser som inte listas ovan från att begära tillstånd att skicka meddelanden.`
    - Source: `This will prevent any websites not listed above from requesting permission to send notifications. Blocking notifications may break some website features.`
    - Suggest: `Detta kommer att förhindra att webbplatser som inte listas ovan begär tillstånd att skicka meddelanden.`
    - Two competing constructions are combined ("förhindra att X" + "förhindra X från att"), leaving the clause without a finite verb; the same error recurs in the location, camera and microphone disable-desc strings.
- `site-data-clear-all-prompt-title` — `browser/browser/preferences/siteDataSettings.ftl` — Missing plural agreement on "all"
    - Current: `Rensa all kakor och webbplatsdata`
    - Source: `Clear all cookies and site data`
    - Suggest: `Rensa alla kakor och webbplatsdata`
    - "kakor" is plural, so the determiner must be "alla", not "all".
- `site-data-settings-description` — `browser/browser/preferences/siteDataSettings.ftl` — Verb not conjugated and adjective/noun agreement error
    - Current: `{ -brand-short-name } spara data från webbplatser med beständig lagring tills du raderar det och raderar data från webbplatser med icke-beständig lagringsutrymme, eftersom det behövs utrymme.`
    - Source: `The following websites store cookies and site data on your computer. { -brand-short-name } keeps data from websites with persistent storage until you delete it, and deletes data from websites with non-persistent storage…`
    - Suggest: `{ -brand-short-name } sparar data från webbplatser med beständig lagring tills du raderar dem och raderar data från webbplatser med icke-beständigt lagringsutrymme allt eftersom utrymme behövs.`
    - "spara" is the infinitive where the present "sparar" is required; "icke-beständig lagringsutrymme" lacks neuter agreement ("icke-beständigt"); "eftersom det behövs utrymme" means "because space is needed" rather than "as space is needed".
- `safeb-blocked-harmful-page-error-desc-override` — `browser/browser/safebrowsing/blockedSite.ftl` — Double definiteness error "denna osäkra webbplatsen"
    - Current: `gå till denna osäkra webbplatsen`
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing a potentially harmful application</a>. You can <a data-l10n-name='ignore_warning_link'>ignore the…`
    - Suggest: `gå till denna osäkra webbplats`
    - With the determiner "denna" the noun must be indefinite: "denna osäkra webbplats".
- `safeb-blocked-harmful-page-short-desc` — `browser/browser/safebrowsing/blockedSite.ftl` — Pronoun gender mismatch: "det" referring to "sidan"
    - Current: `eftersom det kan försöka installera farliga appar`
    - Source: `{ -brand-short-name } blocked this page because it might try to install dangerous apps that steal or delete your information (for example, photos, passwords, messages and credit cards).`
    - Suggest: `eftersom den kan försöka installera farliga appar`
    - The antecedent is "den här sidan" (common gender), so the pronoun must be "den"; the three sibling short-desc strings all use "den".
- `safeb-blocked-phishing-page-error-desc-override` — `browser/browser/safebrowsing/blockedSite.ftl` — Double definiteness error "denna osäkra webbplatsen"
    - Current: `gå till denna osäkra webbplatsen`
    - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as a deceptive site</a>. You can <a data-l10n-name='report_detection'>report a detection problem</a> or <a data-…`
    - Suggest: `gå till denna osäkra webbplats`
    - With the determiner "denna" the noun stays indefinite in standard Swedish; the malware and unwanted variants in the same file write it correctly ("den osäkra webbplatsen" / "den här osäkra webbplatsen").
- `sidebar-history-sort-option-date-and-site` — `browser/browser/sidebar.ftl` — "site" rendered as "plats" in one sort option while the adjacent option uses "Webbplats".
    - Current: `Datum och plats`
    - Source: `label: Date and site`
    - Suggest: `Datum och webbplats`
    - In the same sort menu, sidebar-history-sort-option-site is "Webbplats"; "plats" means location and does not name the same grouping.
- `tab-context-open-in-new-container-tab2` — `browser/browser/tabContextMenu.ftl` — "Container tab" rendered as "behållarflik" where the tree consistently uses "innehållsflik".
    - Current: `Öppna i en ny behållarflik`
    - Source: `accesskey: e label: Open in a New Container Tab`
    - Suggest: `Öppna i en ny innehållsflik`
    - tab-context-open-in-new-container-tab in the same file, plus places.ftl, menubar.ftl, sidebar.ftl and syncedTabs.ftl, all use "innehållsflik"; this variant label for the same feature uses a different term.
- `existing-user-privacy-notice-update-message` — `browser/browser/termsofuse.ftl` — "Privacy Notice" rendered as "sekretesspolicy" instead of the established "sekretessmeddelande".
    - Current: `sekretesspolicy`
    - Source: `We’ve updated our <a data-l10n-name="privacy-notice-link">Privacy Notice</a> to reflect the latest features in { -brand-short-name }.`
    - Suggest: `sekretessmeddelande`
    - The two neighbouring strings in the same file (and preonboarding.ftl) translate the same link label "Privacy Notice" as "sekretessmeddelande"; "sekretesspolicy" names a different document (Privacy Policy).
- `decoder.decodeError.message` — `browser/chrome/browser/browser.properties` — Missing preposition after "avkodning"
    - Current: `Ett fel uppstod vid avkodning en mediaresurs.`
    - Source: `An error occurred while decoding a media resource.`
    - Suggest: `Ett fel uppstod vid avkodning av en mediaresurs.`
    - The noun "avkodning" requires "av" before its object in Swedish.
- `decoder.decodeWarning.message` — `browser/chrome/browser/browser.properties` — Missing preposition after "avkodning"
    - Current: `Ett återhämtningsbart fel uppstod vid avkodning en mediaresurs.`
    - Source: `A recoverable error occurred while decoding a media resource.`
    - Suggest: `Ett återhämtningsbart fel uppstod vid avkodning av en mediaresurs.`
    - The noun "avkodning" requires "av" before its object in Swedish.
- `decoder.noPulseAudio.message` — `browser/chrome/browser/browser.properties` — Missing "För" in the purpose clause, plus split compound "PulseAudio programvara"
    - Current: `Att spela upp ljud, kan du behöva installera PulseAudio programvara som krävs.`
    - Source: `To play audio, you may need to install the required PulseAudio software.`
    - Suggest: `För att spela upp ljud kan du behöva installera den PulseAudio-programvara som krävs.`
    - "Att spela upp ljud, kan du…" is ungrammatical; the parallel strings decoder.noCodecsLinux and decoder.noHWAcceleration both begin with "För att…". "PulseAudio programvara" is a missing-hyphen compound.
- `permissions.fullscreen.fullScreenCanceled` — `browser/chrome/browser/browser.properties` — Spelling error "Avlutade"
    - Current: `Avlutade DOM-helskärm`
    - Source: `Exited DOM fullscreen: permission requests should not be issued while in DOM fullscreen.`
    - Suggest: `Avslutade DOM-helskärm`
    - "Avlutade" is not a word; the intended verb is "avslutade" (exited).
- `safebrowsing.reportedAttackSite` — `browser/chrome/browser/browser.properties` — Gender agreement error and inconsistent term for "attack site"
    - Current: `Rapporterat skadlig plats!`
    - Source: `Reported Attack Site!`
    - Suggest: `Rapporterad angreppswebbplats!`
    - "plats" is common gender, so the participle must be "Rapporterad"; the adjacent button string renders "attack site" as "angreppswebbplats", while here it becomes the unrelated "skadlig plats".
- `unsignedAddonsDisabled.message` — `browser/chrome/browser/browser.properties` — Word order error: negation placed before the verb in a main clause
    - Current: `Ett eller flera installerade tillägg inte kan verifieras och har inaktiverats.`
    - Source: `One or more installed add-ons cannot be verified and have been disabled.`
    - Suggest: `Ett eller flera installerade tillägg kan inte verifieras och har inaktiverats.`
    - In a Swedish main clause the negation follows the finite verb; "tillägg inte kan verifieras" is subordinate-clause order and reads as broken Swedish.
- `unblockHeaderUnblock` — `browser/chrome/browser/downloads/downloads.properties` — Missing "på" after "säker"
    - Current: `Är du säker att du vill tillåta denna hämtning?`
    - Source: `Are you sure you want to allow this download?`
    - Suggest: `Är du säker på att du vill tillåta denna hämtning?`
    - Swedish requires "säker på att"; the neighbouring unblockHeaderOpen gets it right.
- `clearSiteDataPromptTitle` — `browser/chrome/browser/siteData.properties` — Agreement error: "all" with a plural noun
    - Current: `Rensa all kakor och webbplatsdata`
    - Source: `Clear all cookies and site data`
    - Suggest: `Rensa alla kakor och webbplatsdata`
    - "kakor" is plural, so the quantifier must be "alla"; the body text of the same dialog already uses "alla kakor".
- `about-debugging-browser-version-too-old` — `devtools/client/aboutdebugging.ftl` — Ungrammatical clause: "Det här är inställningen stöds inte".
    - Current: `Det här är inställningen stöds inte och kan göra att DevTools misslyckas.`
    - Source: `The connected browser has an old version ({ $runtimeVersion }). The minimum supported version is ({ $minVersion }). This is an unsupported setup and may cause DevTools to fail. Please update the connected browser. <a>Tr…`
    - Suggest: `Den här konfigurationen stöds inte och kan göra att DevTools misslyckas.`
    - en-US "This is an unsupported setup"; the Swedish merges two clauses and is not parsable Swedish.
- `about-debugging-browser-version-too-recent` — `devtools/client/aboutdebugging.ftl` — Gender agreement: "Det här konfigurationen" should be "Den här konfigurationen".
    - Current: `Det här konfigurationen stöds inte`
    - Source: `The connected browser is more recent ({ $runtimeVersion }, buildID { $runtimeID }) than your { -brand-shorter-name } ({ $localVersion }, buildID { $localID }). This is an unsupported setup and may cause DevTools to fail…`
    - Suggest: `Den här konfigurationen stöds inte`
    - "konfiguration" is an en-word and requires "den".
- `accessibility-keyboard-issue-mouse-only` — `devtools/client/accessibility.ftl` — Spelling: "Klickabara" should be "Klickbara".
    - Current: `Klickabara element måste vara fokuserbara`
    - Source: `Clickable elements must be focusable and should have interactive semantics. <a>Learn more</a>`
    - Suggest: `Klickbara element måste vara fokuserbara`
    - Simple misspelling of "klickbara".
- `accessibility-progress-progressbar` — `devtools/client/accessibility.ftl` — Singular variant uses the imperative/infinitive "Kontrollera" instead of present tense.
    - Current: `[one] Kontrollera { $nodeCount } nod`
    - Source: `{$nodeCount ->} [one] Checking { $nodeCount } node [other] Checking { $nodeCount } nodes`
    - Suggest: `[one] Kontrollerar { $nodeCount } nod`
    - The plural variant correctly reads "Kontrollerar" (is checking); the singular reads as a command.
- `editor.continueToHere.label` — `devtools/client/debugger.properties` — Ungrammatical "Fortsätt till hit".
    - Current: `Fortsätt till hit`
    - Source: `Continue to here`
    - Suggest: `Fortsätt hit`
    - "hit" already means "to here"; the preposition makes the phrase ungrammatical.
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “Avbryt vid…” but the string it names, `watchpoints.submenu`, reads “Bryt vid…”
    - Current: `Högerklicka på ett element i inspektören och välj "Avbryt vid…" för att lägga till en brytpunkt`
    - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
    - Suggest: `Bryt vid…`
    - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `network-menu-summary-requests-count` — `devtools/client/netmonitor.ftl` — Plural variant uses the singular noun "begäran".
    - Current: `*[other] { $requestCount } begäran`
    - Source: `{$requestCount ->} [0] No requests [one] { $requestCount } request [other] { $requestCount } requests`
    - Suggest: `*[other] { $requestCount } förfrågningar`
    - The plural of "begäran" is "begäranden"; "5 begäran" is ungrammatical.
- `certmgr.certificateTransparency.status.ok` — `devtools/client/netmonitor.properties` — The acronym SCT is misspelled "STC".
    - Current: `Giltiga STC-poster`
    - Source: `Valid SCT records`
    - Suggest: `Giltiga SCT-poster`
    - The neighbouring strings correctly use "SCT:er" for signed certificate timestamps.
- `netmonitor.search.status.labels.matchingLines` — `devtools/client/netmonitor.properties` — Plural form uses the passive "Hittades" where the singular uses "Hittade".
    - Current: `Hittades #1 matchande rader`
    - Source: `Found #1 matching line;Found #1 matching lines`
    - Suggest: `Hittade #1 matchande rader`
    - Inconsistent verb form between the two plural variants of the same message; the plural reads "was found".
- `pref-thread-stream-trans` — `devtools/client/perftools.ftl` — Spelling: "Nätvärksströmstransport".
    - Current: `Nätvärksströmstransport`
    - Source: `title: Network stream transport`
    - Suggest: `Nätverksströmstransport`
    - "Nätvärks-" is a misspelling of "Nätverks-".
- `responsive.remoteOnly` — `devtools/client/responsive.properties` — Agreement: "designläge … är endast tillgänglig" should be "tillgängligt".
    - Current: `Följsamt designläge är endast tillgänglig för fjärrwebbläsarflikar`
    - Source: `Responsive Design Mode is only available for remote browser tabs, such as those used for web content in multi-process Firefox.`
    - Suggest: `Följsamt designläge är endast tillgängligt för fjärrwebbläsarflikar`
    - "läge" is a neuter noun and requires the -t form of the predicative adjective.
- `application.panelLabel` — `devtools/client/startup.properties` — Compound written as two words: "Applikations panel".
    - Current: `Applikations panel`
    - Source: `Application Panel`
    - Suggest: `Applikationspanel`
    - Swedish compounds are written together; the same file writes "Nätverkspanel", "Minnespanel" correctly.
- `toolbox.buttons.measure` — `devtools/client/startup.properties` — Double article: "en del av en sidan".
    - Current: `Mät en del av en sidan`
    - Source: `Measure a portion of the page`
    - Suggest: `Mät en del av sidan`
    - "en sidan" combines indefinite article with definite noun.
- `constructedStyleSheet` — `devtools/client/styleeditor.properties` — Adjective in definite form: "konstruerade stilmall".
    - Current: `<konstruerade stilmall #%S>`
    - Source: `<constructed style sheet #%S>`
    - Suggest: `<konstruerad stilmall #%S>`
    - An indefinite singular noun requires "konstruerad".
- `options-inspector-rules-focus-next-on-enter-label` — `devtools/client/toolbox-options.ftl` — Spelling: "Focusera" should be "Fokusera".
    - Current: `Focusera nästa inmatning på <kbd>Enter</kbd>`
    - Source: `Focus next input on <kbd>Enter</kbd>`
    - Suggest: `Fokusera nästa inmatning på <kbd>Enter</kbd>`
    - Swedish spells the verb with k; the rest of the tree uses "fokus"/"fokusera".
- `accessibility.keyboard.issue.mouse.only` — `devtools/shared/accessibility.properties` — Spelling: "Klickabara" should be "Klickbara".
    - Current: `Klickabara element måste vara fokuserbara`
    - Source: `Clickable elements must be focusable and should have interactive semantics.`
    - Suggest: `Klickbara element måste vara fokuserbara`
    - Same misspelling as in accessibility.ftl.
- `remoteIncomingPromptHeader` — `devtools/shared/debugger.properties` — Two grammar errors in the remote-debugging security prompt.
    - Current: `Ett inkommande begäran att tillåta anslutning för fjärrfelsökning har upptäcktes.`
    - Source: `An incoming request to permit remote debugging connection was detected. A remote client can take complete control over your browser!`
    - Suggest: `En inkommande begäran om att tillåta anslutning för fjärrfelsökning har upptäckts.`
    - "begäran" is an en-word ("En inkommande begäran") and the perfect tense is "har upptäckts", not "har upptäcktes".
- `serverReceiveOOBBody` — `devtools/shared/debugger.properties` — "token value" rendered as "symboliskt värde" with broken agreement ("det symboliskt värde").
    - Current: `Ange det symboliskt värde här`
    - Source: `The client should be displaying a token value.  Enter that token value here to complete authentication with this client.`
    - Suggest: `Ange tokenvärdet här`
    - "symboliskt värde" means symbolic value rather than an authentication token, and the definite construction is ungrammatical.
- `screenshotDPRDecreasedWarning` — `devtools/shared/screenshot.properties` — Compound split: "Enhets pixelförhållande".
    - Current: `Enhets pixelförhållande reducerades till 1`
    - Source: `The device pixel ratio was reduced to 1 as the resulting image was too large`
    - Suggest: `Enhetspixelförhållandet reducerades till 1`
    - The same file writes "Enhetspixelförhållande" as one word in screenshotDPRDesc.
- `close-fence` — `dom/chrome/accessibility/AccessFu.properties` — Misspelling “parantes”.
    - Current: `close-fence = högerparantes`
    - Source: `closing fence`
    - Suggest: `close-fence = högerparentes`
    - Correct Swedish is “parentes”, as used in open-fence (“vänsterparentes”).
- `outlineitem` — `dom/chrome/accessibility/AccessFu.properties` — Compound written as two words.
    - Current: `outlineitem = kontur objekt`
    - Source: `outline item`
    - Suggest: `outlineitem = konturobjekt`
    - Swedish compounds are written as one word; “listitem” is correctly rendered “listobjekt” in the same file.
- `FullscreenDeniedContainerNotAllowed` — `dom/chrome/dom/dom.properties` — Garbled clause: “at least one of the document’s containing elements” became agrammatical.
    - Current: `åtminstone en av det dokument som innehåller elementen`
    - Source: `Request for fullscreen was denied because at least one of the document’s containing elements is not an iframe or does not have an “allowfullscreen” attribute.`
    - Suggest: `åtminstone ett av dokumentets omslutande element`
    - Number and head noun are swapped, so the sentence no longer says which element lacks allowfullscreen.
- `ImageBitmapRenderingContext_TransferImageBitmapWarning` — `dom/chrome/dom/dom.properties` — Typo “Använa” for “Använd”.
    - Current: `Använa ImageBitmapRenderingContext.transferFromImageBitmap`
    - Source: `ImageBitmapRenderingContext.transferImageBitmap is deprecated and will be removed soon. Use ImageBitmapRenderingContext.transferFromImageBitmap instead.`
    - Suggest: `Använd ImageBitmapRenderingContext.transferFromImageBitmap`
    - Missing d in the imperative verb.
- `KillAddonScriptGlobalMessage` — `dom/chrome/dom/dom.properties` — Ungrammatical ending “tills det nästa omladdning”.
    - Current: `tills det nästa omladdning`
    - Source: `Prevent the extension script from running on this page until it next reloads`
    - Suggest: `till nästa omladdning`
    - Stray pronoun “det” and missing article leave the phrase agrammatical.
- `RewriteYouTubeEmbedPathParams` — `dom/chrome/dom/dom.properties` — Typo “inta” for “inte”.
    - Current: `Parametrar stöds inta av iframe-inbäddad`
    - Source: `Rewriting old-style YouTube Flash embed (%S) to iframe embed (%S). Params were unsupported by iframe embeds and converted. Please update page to use iframe instead of embed/object, if possible.`
    - Suggest: `Parametrar stöds inte av iframe-inbäddning`
    - Simple misspelling of the negation.
- `PEBadSelectorKeyframeRuleIgnored` — `dom/chrome/layout/css.properties` — Redundant “pga. av”.
    - Current: `ignorerades pga. av ogiltig selektor`
    - Source: `Keyframe rule ignored due to bad selector.`
    - Suggest: `ignorerades pga. ogiltig selektor`
    - “pga.” already contains “av”; the sibling PEBadSelectorRSIgnored is correct.
- `errEndTagSeenWithoutDoctype` — `dom/chrome/layout/htmlparser.properties` — Typo “föregåenden”.
    - Current: `utan föregåenden doctype`
    - Source: `End tag seen without seeing a doctype first. Expected “<!DOCTYPE html>”.`
    - Suggest: `utan föregående doctype`
    - The parallel errStartTagWithoutDoctype spells it “föregående”.
- `CompositorAnimationWarningContentTooLargeArea` — `dom/chrome/layout/layout_errors.properties` — Agreement error: “området … är för stor”.
    - Current: `eftersom området för ramen (%1$S) är för stor`
    - Source: `Animation cannot be run on the compositor because the area of the frame (%1$S) is too large relative to the viewport (larger than %2$S)`
    - Suggest: `eftersom området för ramen (%1$S) är för stort`
    - “område” is neuter and requires “stort”.
- _…and 45 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `error-long-desc2` — `browser/browser/aboutRobots.ftl` — `error-long-desc2` uses a straight apostrophe
    - Current: `Robots have seen things you people wouldn't believe.`
    - Source: `Robots have seen things you people wouldn’t believe.`
    - The tree uses ’ 126 times against 42 straight.
- `error-long-desc3` — `browser/browser/aboutRobots.ftl` — `error-long-desc3` uses a straight apostrophe
    - Current: `Robots are Your Plastic Pal Who's Fun To Be With.`
    - Source: `Robots are Your Plastic Pal Who’s Fun To Be With.`
    - The tree uses ’ 126 times against 42 straight.
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — `ai-window-delete-all-memories-message` uses three dots where this locale uses …
    - Current: `Befintliga minnen raderas. Om du inte vill skapa några nya minnen, avmarkera alternativen för "Lär dig av..." i inställningarna för { -smart-window-brand-name }.`
    - Source: `Existing memories will be deleted. If you don’t want any new memories created, uncheck the options to “Learn from…” in { -smart-window-brand-name } settings.`
    - The tree uses … 385 times against 16 ASCII runs.
- `smart-window-grouped-tabs-summary` — `browser/browser/aiWindowContent.ftl` — Missing space between "till" and the count in the singular variant, producing e.g. "la till1 flik".
    - Current: `och la till{ $count } flik.`
    - Source: `{$count ->} [one] Created the group “{ $label }” and added { $count } tab. [other] Created the group “{ $label }” and added { $count } tabs.`
    - Suggest: `och lade till { $count } flik.`
    - The plural variant has the space ("lade till { $count } flikar"); the singular renders the number glued to the verb in the visible text.
- `appmenu-help-share-ideas` — `browser/browser/appmenu.ftl` — `appmenu-help-share-ideas` uses three dots where this locale uses …
    - Current: `Dela idéer och feedback...`
    - Source: `accesskey: S label: Share Ideas and Feedback…`
    - The tree uses … 385 times against 16 ASCII runs.
- `edit-popup-settings2` — `browser/browser/browser.ftl` — `edit-popup-settings2` uses three dots where this locale uses …
    - Current: `Hantera popup-inställningar och omdirigeringsinställningar för tredje part...`
    - Source: `accesskey: M label: Manage pop-up and third-party redirect settings…`
    - The tree uses … 385 times against 16 ASCII runs.
- `menu-share-mac-picker-multiple` — `browser/browser/browser.ftl` — `menu-share-mac-picker-multiple` uses three dots where this locale uses …
    - Current: `Meddelanden, Mail och mer...`
    - Source: `accesskey: M label: Messages, Mail, and More…`
    - The tree uses … 385 times against 16 ASCII runs.
- `restore-session-startup-suggestion-message` — `browser/browser/browser.ftl` — Missing space after the bold question, so the two sentences run together in the visible text.
    - Current: `</strong>Du kan återställa`
    - Source: `<strong>Open previous tabs?</strong> You can restore your previous session from the { -brand-short-name } application menu <img data-l10n-name="icon"/>, under History.`
    - Suggest: `</strong> Du kan återställa`
    - The en-US has a space after </strong>; without it the infobar renders "Öppna tidigare flikar?Du kan återställa…".
- `menu-help-share-ideas` — `browser/browser/menubar.ftl` — `menu-help-share-ideas` uses three dots where this locale uses …
    - Current: `Dela idéer och feedback...`
    - Source: `accesskey: S label: Share Ideas and Feedback…`
    - The tree uses … 385 times against 16 ASCII runs.
- `migration-chrome-windows-password-import-step1` — `browser/browser/migrationWizard.ftl` — Missing space before the ">" separator in the menu path.
    - Current: `Lösenord och autofyll> Googles lösenordshantering.`
    - Source: `Open the main menu <img data-l10n-name="chrome-icon-3dots"/> and go to Passwords and Autofill > Google Password Manager.`
    - Suggest: `Lösenord och autofyll > Googles lösenordshantering.`
    - The en-US has "Passwords and Autofill > Google Password Manager"; the missing space runs the menu name into the separator in text the user reads.
- `cfr-doorhanger-bookmark-fxa-link-text` — `browser/browser/newtab/asrouter.ftl` — `cfr-doorhanger-bookmark-fxa-link-text` uses three dots where this locale uses …
    - Current: `Synkronisera bokmärken nu...`
    - Source: `Sync bookmarks now…`
    - The tree uses … 385 times against 16 ASCII runs.
- `restore-session-startup-suggestion-message` — `browser/browser/newtab/asrouter.ftl` — Missing space between the bold heading and the following sentence.
    - Current: `flikar?</strong>Du`
    - Source: `<strong>Open previous tabs?</strong> You can restore your previous session from the { -brand-short-name } application menu <img data-l10n-name="icon"/>, under History.`
    - Suggest: `flikar?</strong> Du`
    - The en-US has a space after </strong>. Without it the rendered text reads "flikar?Du kan…" with the two sentences run together.
- `home-mode-choice-custom-srd` — `browser/browser/newtab/newtab.ftl` — `home-mode-choice-custom-srd` uses three dots where this locale uses …
    - Current: `Anpassade webbadresser...`
    - Source: `label: Custom URLs…`
    - The tree uses … 385 times against 16 ASCII runs.
- `newtab-widget-section-minimize` — `browser/browser/newtab/newtab.ftl` — The English plural "widgets" is left untranslated in the tooltip while the rest of the surface uses "widgetar".
    - Current: `Minimera widgets`
    - Source: `aria-label: Collapse all widgets to compact size title: Minimize widgets`
    - Suggest: `Minimera widgetar`
    - Adjacent strings (newtab-widget-section-hide-all-button, -maximize, -show-widgets, -menu-manage) all use "widgetar"; only this tooltip keeps the English plural.
- `places-edit-folder2` — `browser/browser/places.ftl` — `places-edit-folder2` uses three dots where this locale uses …
    - Current: `Redigera mapp...`
    - Source: `accesskey: E label: Edit Folder…`
    - The tree uses … 385 times against 16 ASCII runs.
- `browser-languages-search` — `browser/browser/preferences/languages.ftl` — `browser-languages-search` uses three dots where this locale uses …
    - Current: `Sök efter fler språk...'`
    - Source: `Search for more languages…`
    - The tree uses … 385 times against 16 ASCII runs.
- `browser-languages-search` — `browser/browser/preferences/languages.ftl` — Stray apostrophe at end of the string
    - Current: `Sök efter fler språk...'`
    - Source: `Search for more languages…`
    - Suggest: `Sök efter fler språk…`
    - A stray straight apostrophe is appended to visible UI text; the en-US also uses a true ellipsis character, as the neighbouring Swedish strings in this file do.
- `browser-languages-searching` — `browser/browser/preferences/languages.ftl` — `browser-languages-searching` uses three dots where this locale uses …
    - Current: `Söker efter språk...`
    - Source: `label: Searching for languages…`
    - The tree uses … 385 times against 16 ASCII runs.
- `home-mode-choice-custom` — `browser/browser/preferences/preferences.ftl` — `home-mode-choice-custom` uses three dots where this locale uses …
    - Current: `Anpassade webbadresser...`
    - Source: `label: Custom URLs…`
    - The tree uses … 385 times against 16 ASCII runs.
- `sync-syncing-across-devices-empty-state2` — `browser/browser/preferences/preferences.ftl` — `sync-syncing-across-devices-empty-state2` uses three dots where this locale uses …
    - Current: `Du synkroniserar ingenting ... ännu. Börja synkronisera för att få all din data på alla dina enheter.`
    - Source: `description: You aren’t syncing anything… yet. Start syncing to get all of your data on all your devices. label: Manage synced data`
    - The tree uses … 385 times against 16 ASCII runs.
- `safeb-blocked-malware-page-learn-more-sumo` — `browser/browser/safebrowsing/blockedSite.ftl` — English genitive apostrophe used on the brand term
    - Current: `{ -brand-short-name }’s skydd mot nätfiske och skadlig programvara`
    - Source: `Learn more about { -brand-short-name }’s Phishing and Malware Protection at <a data-l10n-name='firefox_support'>support.mozilla.org</a>.`
    - Suggest: `{ -brand-short-name }:s skydd mot nätfiske och skadlig programvara`
    - Swedish forms the genitive of such names with ":s"; the same file uses "{ -brand-short-name }:s" in safeb-blocked-addon-page-learn-more3, and the other learn-more strings avoid the genitive entirely.
- `fxa-menu-send-to-device` — `browser/browser/sync.ftl` — Plural variant of the menu label starts with a lowercase letter.
    - Current: `skicka { $tabCount } flikar till enhet`
    - Source: `label: {$tabCount ->} [1] Send to device [other] Send { $tabCount } tabs to device`
    - Suggest: `Skicka { $tabCount } flikar till enhet`
    - The singular variant and the parallel fxa-menu-send-to-mobile variants all start with a capital "S"; this label would display lowercase in the menu.
- `synced-tabs-sidebar-title` — `browser/browser/syncedTabs.ftl` — English title-casing of the second word ("Flikar").
    - Current: `Synkade Flikar`
    - Source: `Synced Tabs`
    - Suggest: `Synkade flikar`
    - Swedish does not capitalize non-initial words; every other occurrence in the tree (menubar.ftl, sidebarMenu.ftl) writes "Synkade flikar".
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — Stray ">" character after the privacy notice link.
    - Current: `sekretessmeddelande</a> >.`
    - Source: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
    - Suggest: `sekretessmeddelande</a>.`
    - The en-US has no such character; the user sees a visible " >." after the link text.
- `open-sidebar` — `browser/browser/touchbar/touchbar.ftl` — "Sidebars" rendered as the obsolete "Sidrad" instead of the term used elsewhere in the product.
    - Current: `Sidrad`
    - Source: `Sidebars`
    - Suggest: `Sidofält`
    - The locale renders "sidebar" as "sidofält" elsewhere (e.g. onboarding-vertical-tabs-tooltip, onboarding-new-tabs-subtitle); "Sidrad" is a legacy term no longer used in the UI.
- `corruptedContentErrorv2` — `browser/chrome/overrides/appstrings.properties` — "network protocol violation" rendered as "kränkning", inconsistent with networkProtocolError
    - Current: `har upplevt en kränkning av nätverksprotokollet`
    - Source: `The site at %S has experienced a network protocol violation that cannot be repaired.`
    - Suggest: `har upplevt en överträdelse av nätverksprotokollet`
    - networkProtocolError in the same file translates the identical phrase as "överträdelse av nätverksprotokoll"; "kränkning" means violation of a person or their rights and is wrong for a protocol.
- `STUB_BLURB_THIRD2` — `browser/installer/nsisstrings.properties` — Uses the plural/formal address "ni" where the locale consistently addresses the user with "du".
    - Current: `Tack för att ni skapar en bättre webb tillsammans med oss`
    - Source: `Thanks for building a better web with us`
    - Suggest: `Tack för att du skapar en bättre webb tillsammans med oss`
    - Every other string in these installer files and in the sibling STUB_BLURB_THIRD2_DEVEDITION uses "du"/"dig"; "ni" breaks the established form of address.
- `about-debugging-sidebar-runtime-item-waiting-for-browser` — `devtools/client/aboutdebugging.ftl` — `about-debugging-sidebar-runtime-item-waiting-for-browser` uses three dots where this locale uses …
    - Current: `Väntar på webbläsare...`
    - Source: `Waiting for browser…`
    - The tree uses … 385 times against 16 ASCII runs.
- `manifest-loading` — `devtools/client/application.ftl` — `manifest-loading` uses three dots where this locale uses …
    - Current: `Laddar manifest...`
    - Source: `Loading manifest…`
    - The tree uses … 385 times against 16 ASCII runs.
- `collapseSources` — `devtools/client/debugger.properties` — The Sources pane is called "resurs" here but "Källor" everywhere else in the debugger.
    - Current: `Fäll ihop resurs och konturpanel`
    - Source: `Collapse Sources and Outline panes`
    - Suggest: `Fäll ihop panelerna Källor och Kontur`
    - sources.header is "Källor" and outline.header is "Kontur"; naming the same pane "resurs" makes the tooltip point at a pane that does not exist in the UI (expandSources has the same problem).
- `ignoreContextItem.ignoreLines` — `devtools/client/debugger.properties` — Editor lines called "linjer" here but "rad" in the adjacent singular item.
    - Current: `Ignorera linjer`
    - Source: `Ignore lines`
    - Suggest: `Ignorera rader`
    - ignoreContextItem.ignoreLine uses "rad"; "linjer" are geometric lines, so the same menu pair uses two different terms, one of them wrong.
- `settings.autoPrettyPrint.label` — `devtools/client/debugger.properties` — "pretty printing" rendered as "snygg utskrift" (nice printout) instead of the file's own "kodformatera".
    - Current: `Automatisk snygg utskrift`
    - Source: `Automatic pretty printing`
    - Suggest: `Automatisk kodformatering`
    - sourceFooter.prettyPrint.* consistently use "kodformatera"; "utskrift" suggests printing on paper.
- `sourceSearch.search` — `devtools/client/debugger.properties` — `sourceSearch.search` uses three dots where this locale uses …
    - Current: `Sök...`
    - Source: `Search sources…`
    - The tree uses … 385 times against 16 ASCII runs.
- `inspectorBreakpointSubmenu.label` — `devtools/client/inspector.properties` — "Break on…" rendered as "Avbryt vid…" (cancel at…), while the debugger uses "Bryt vid…".
    - Current: `Avbryt vid…`
    - Source: `Break on…`
    - Suggest: `Bryt vid…`
    - watchpoints.submenu in debugger.properties renders the same en-US string as "Bryt vid…"; "Avbryt" normally means cancel/abort.
- `jsonViewer.responseHeaders` — `devtools/client/jsonview.properties` — HTTP headers called "rubriker" in one label and "huvuden" in the sibling label of the same panel.
    - Current: `Svarsrubriker`
    - Source: `Response Headers`
    - Suggest: `Svarshuvuden`
    - jsonViewer.requestHeaders uses "Begäranhuvuden"; the two header group labels sit next to each other in the Headers panel and must use one term.
- `perftools-presets-web-developer-description` — `devtools/client/perftools.ftl` — "overhead" rendered as "pålägg" (topping/markup) instead of the file's "omkostnad".
    - Current: `med lite pålägg`
    - Source: `Recommended preset for most web app debugging, with low overhead.`
    - Suggest: `med låg omkostnad`
    - The other presets render "overhead" as "omkostnad"; "pålägg" does not mean processing overhead.
- `styleeditor-visibility-toggle-system` — `devtools/client/styleeditor.ftl` — Style sheets called "formatmallar" here, "stilmallar" everywhere else in the file.
    - Current: `Systemformatmallar kan inte inaktiveras`
    - Source: `tooltiptext: System style sheets can’t be disabled`
    - Suggest: `Systemstilmallar kan inte inaktiveras`
    - Every other string in the Style Editor uses "stilmall"; the tooltip introduces a second term for the same object.
- `gridtype-dual` — `devtools/shared/highlighters.ftl` — Half-translated label: "Rutnätsbehållare/Item".
    - Current: `Rutnätsbehållare/Item`
    - Source: `Grid Container/Item`
    - Suggest: `Rutnätsbehållare/Rutnätsobjekt`
    - gridtype-item is translated as "Rutnätsobjekt", so the dual label leaves the second half in English (flextype-dual has the same issue).
- `rule.colorSwatch.tooltip` — `devtools/shared/styleinspector.properties` — Stray space before the comma in visible tooltip text.
    - Current: `färgväljaren , skift + klicka`
    - Source: `Click to open the color picker, Shift+click to change the color format`
    - Suggest: `färgväljaren, skift + klicka`
    - A space precedes the comma in text the user reads.
- `pageTitle` — `toolkit/chrome/global/aboutStudies.properties` — Page title says "Undersökningar" (surveys) while every other string on the page says "studier".
    - Current: `Undersökningar`
    - Source: `Studies`
    - Suggest: `Studier`
    - en-US "Studies"; activeStudiesList, completedStudiesList and noStudies all render it "studier".
- `uninstall.confirmation.message` — `toolkit/chrome/global/extensions.properties` — "extension" rendered "Utökningen" while the same file uses "tillägg" elsewhere.
    - Current: `Utökningen “%S” begär att avinstalleras.`
    - Source: `The extension “%S” is requesting to be uninstalled. What would you like to do?`
    - Suggest: `Tillägget “%S” begär att avinstalleras.`
    - newTabControlled.message2 and tabHideControlled.message in this very file use "Ett tillägg" for the same en-US word.
- `context_goToLine_label` — `toolkit/chrome/global/viewSource.properties` — A text line is called "linje" here but "rad" in every other string of the same dialog.
    - Current: `Gå till linje…`
    - Source: `Go to Line…`
    - Suggest: `Gå till rad…`
    - goToLineTitle/goToLineText/outOfRangeText all use "rad"; "linje" is a geometric line, not a line of text.
- `about-reader-loading` — `toolkit/toolkit/about/aboutReader.ftl` — `about-reader-loading` uses three dots where this locale uses …
    - Current: `Laddar...`
    - Source: `Loading…`
    - The tree uses … 385 times against 16 ASCII runs.
- `about-reader-loading` — `toolkit/toolkit/about/aboutReader.ftl` — Three periods instead of an ellipsis character
    - Current: `Laddar...`
    - Source: `Loading…`
    - Suggest: `Laddar…`
    - Every other truncation in the partition uses the ellipsis character (“Laddar…”, “Väntar…”, “Tar bort…”), matching the en-US.
- `process-type-extension` — `toolkit/toolkit/global/processTypes.ftl` — "Extension" rendered "Utökning" where the tree uses "Tillägg".
    - Current: `Utökning`
    - Source: `Extension`
    - Suggest: `Tillägg`
    - browser-utils.ftl, extensions.ftl and extensions.properties all use "tillägg" for extension/add-on.
- `pdfjs-document-properties-page-size-orientation-landscape` — `toolkit/toolkit/pdfviewer/viewer.ftl` — Page orientation called "landskap" instead of the term used throughout printing UI.
    - Current: `landskap`
    - Source: `landscape`
    - Suggest: `liggande`
    - printUI.ftl, printDialogs.ftl and printPreview.ftl all render landscape orientation as "Liggande"; "landskap" is the scenery sense.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/sv-SE/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

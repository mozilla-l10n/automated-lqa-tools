# Firefox l10n QA — hu

| | |
|---|---|
| **Generated** | 2026-08-20 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `fef20cd7efc2` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `9277403f174f` |
| **Previous run** | 2026-08-20 @ `b95608d528c8` |
| **Mode** | incremental |
| **Strings reviewed this run** | 0 of 18,116 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.



---

## Changes in this run

### 🆕 New findings (3)

- `splitview-onboarding-callout-subtitle-1` — `browser/browser/featureCallout.ftl` — `splitview-onboarding-callout-subtitle-1` quotes “Hozzáadás osztott nézethez” but the string it names, `customkeys-view-add-split-view`, reads “Osztott nézet hozzáadása”
  - Current: `Kattintson jobb gombbal erre a lapra, és válassza a „Hozzáadás osztott nézethez” lehetőséget, hogy egyszerre két lapot lásson.`
  - Source: `Right-click this tab and choose “Add Split View” to see two tabs at once.`
  - Suggest: `Osztott nézet hozzáadása`
  - In the source this string quotes “Add Split View”, which is exactly the value of `customkeys-view-add-split-view` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “Töréspont…” but the string it names, `watchpoints.submenu`, reads “Szüneteltetés…”
  - Current: `Kattintson a jobb gombbal egy elemre a Vizsgálóban, és válassza a „Töréspont…” lehetőséget`
  - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
  - Suggest: `Szüneteltetés…`
  - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `noDomMutationBreakpoints` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints` quotes “Töréspont…” but the string it names, `watchpoints.submenu`, reads “Szüneteltetés…”
  - Current: `Kattintson a jobb gombbal egy elemre itt: %S, és válassza a „Töréspont…” lehetőséget`
  - Source: `Right click an element in the %S and select “Break on…” to add a breakpoint`
  - Suggest: `Szüneteltetés…`
  - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.

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
| Strings | 18,116 |
| Missing strings | 47 |
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
| Text quoting a UI label that no longer matches | 3 |
| Source-language spellings left unchanged | 0 |
| Access keys not in their label | 1 |
| Markup & `data-l10n-name` defects | 3 |
| Typography deviations from this locale's own norm | 11 |

### Completeness

**47 strings** are not translated yet, concentrated in:

- `browser/browser/newtab/newtab.ftl` — 15
- `browser/browser/preferences/containers.ftl` — 7
- `toolkit/toolkit/neterror/netError.ftl` — 7
- `browser/browser/preferences/preferences.ftl` — 4
- `devtools/client/inspector.ftl` — 4
- `browser/browser/aboutPrivateBrowsing.ftl` — 3
- `toolkit/toolkit/global/theme-picker.ftl` — 2
- `browser/browser/firefoxView.ftl` — 1
- `toolkit/toolkit/about/aboutNetworking.ftl` — 1
- `toolkit/toolkit/about/aboutProcesses.ftl` — 1
- `toolkit/toolkit/global/mozBoxBase.ftl` — 1
- `toolkit/toolkit/global/processTypes.ftl` — 1

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `polish-double` 874, `straight-double` 33, `german-double` 2, `curly-single` 1 | **polish-double** |
| apostrophe | `typographic` 1, `straight` 1 | _mixed_ |
| ellipsis | `char` 459, `ascii` 7 | **char** |
| dash | `em` 2, `en` 164 | **en** |
| nbsp | `total` 6, `before-punctuation` 2, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (273)

| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 34 |
| 2 | Wrong content (says something other than the English) | 119 |
| 3 | Degraded language (grammar, spelling, terminology) | 86 |
| 4 | Cosmetic (typography, spacing) | 29 |

### A. Functional, markup, variables & plurals

- `about-logins-confirm-remove-all-sync-dialog-message3` — `browser/browser/aboutLogins.ftl` — The singular branches say “passwords” instead of “password”.
  - Current: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszavakat az összes szinkronizált eszközéről.`
  - Source: `{$count ->} [1] This will remove the password saved to { -brand-short-name } on all your synced devices. This will also remove any breach alerts that appear here. You cannot undo this action. [other] This will remove al…`
  - Suggest: `[1] Ez eltávolítja a { -brand-short-name }ba mentett jelszót az összes szinkronizált eszközéről.`
  - en-US [1] reads “This will remove the password saved to …”; the plural noun makes the one-item case wrong and indistinguishable from the *[other] branch.
- `pocket-panel-signup-signup-firefox` — `browser/browser/aboutPocket.ftl` — “Sign up with Firefox” is rendered as “Firefox login”, reversing sign-up into sign-in.
  - Current: `{ -brand-product-name } bejelentkezés`
  - Source: `Sign up with { -brand-product-name }`
  - Suggest: `Regisztráció a { -brand-product-name }kal`
  - en-US is “Sign up with { -brand-product-name }”; the sibling string pocket-panel-signup-signup-email correctly uses “Regisztráció”, while “bejelentkezés” means log in.
- `smartbar-mentions-list-recent-tabs-label` — `browser/browser/aiWindow.ftl` — “Recent tabs” is translated as “Recent tags”.
  - Current: `Legújabb címkék`
  - Source: `Recent tabs`
  - Suggest: `Legutóbbi lapok`
  - en-US “Recent tabs” labels the list of recently used tabs; “címkék” means tags, a different concept already used for tag chips.
- `action-log-searching-history` — `browser/browser/aiWindowContent.ftl` — “Searching history” (verb) is rendered as the noun phrase “search history”.
  - Current: `Keresés előzményei`
  - Source: `Searching history`
  - Suggest: `Előzmények keresése`
  - The action log describes an ongoing action; the completed counterpart action-log-searched-history correctly uses “Előzmények keresve”.
- `smart-window-opened-tabs-summary-group` — `browser/browser/aiWindowContent.ftl` — The action is attributed to the user rather than reported as completed by the assistant.
  - Current: `Létrehozta a(z) „{ $label }” csoportot, és megnyitott { $count } lapot.`
  - Source: `{$count ->} [other] Created the group “{ $label }” and opened { $count } tabs.`
  - Suggest: `A(z) „{ $label }” csoport létrehozva és { $count } lap megnyitva.`
  - en-US “Created the group … and opened … tabs.” reports what the assistant did; the Hungarian second-person-formal reading says the user did it, and it contradicts the parallel smart-window-grouped-tabs-summary which uses the passive.
- `smart-window-restore-success-summary` — `browser/browser/aiWindowContent.ftl` — The plural variant is worded in the singular.
  - Current: `*[other] Lap bezárva, majd helyreállítva.`
  - Source: `{$count ->} [one] Tab closed, then restored. [other] Tabs closed, then restored.`
  - Suggest: `*[other] Lapok bezárva, majd helyreállítva.`
  - en-US distinguishes “Tab closed, then restored.” from “Tabs closed, then restored.”; the Hungarian plural branch keeps the singular noun.
- `appmenu-update-available2` — `browser/browser/appMenuNotifications.ftl` — Access key `D` of `appmenu-update-available2` is not present in its label
  - Current: `D`
  - Source: `buttonaccesskey: D buttonlabel: Download label: Update available secondarybuttonaccesskey: m secondarybuttonlabel: Dismiss`
  - The label is “Letöltés”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `appmenu-search-history` — `browser/browser/appmenu.ftl` — “Search history” (verb + object) is rendered as the noun “search history”.
  - Current: `Keresés előzményei`
  - Source: `label: Search history`
  - Suggest: `Előzmények keresése`
  - The developer comment says “This allows to search through the browser's history”, i.e. Search is a verb here.
- `fxa-menu-device-recent-tabs-panel` — `browser/browser/appmenu.ftl` — The synced-device panel title “Recent tabs” is translated as “Recent tags”.
  - Current: `Legújabb címkék`
  - Source: `title: Recent tabs`
  - Suggest: `Legutóbbi lapok`
  - The developer comment states this is the panel of recent tabs on a synced device; “címkék” (tags) names the wrong thing.
- `default-browser-notification-privacy-body-text` — `browser/browser/backgroundtasks/defaultagent.ftl` — “built-in privacy and protection” shortened to “built-in privacy”.
  - Current: `Térjen vissza a { -brand-short-name }hoz a beépített adatvédelemhez.`
  - Source: `Your default changed. Come back to { -brand-short-name } for built-in privacy and protection.`
  - Suggest: `Térjen vissza a { -brand-short-name }hoz a beépített adatvédelemért és védelemért.`
  - The second benefit named by en-US (protection) is dropped from the notification body.
- `urlbar-result-action-search-actions` — `browser/browser/browser.ftl` — “Search Actions” rendered as the noun phrase “search actions”.
  - Current: `Keresési műveletek`
  - Source: `Search Actions`
  - Suggest: `Műveletek keresése`
  - The group comment states “In these actions ‘Search’ is a verb, followed by where the search is performed”; the neighbouring entries use “Könyvjelzők keresése”, “Előzmények keresése”, “Lapok keresése”.
- `customkeys-shortcut-unassigned` — `browser/browser/customkeys.ftl` — “Add shortcut” is translated as “Add launcher icon”.
  - Current: `Indítóikon hozzáadása`
  - Source: `placeholder: Add shortcut`
  - Suggest: `Gyorsbillentyű hozzáadása`
  - In this file “shortcut” means a keyboard shortcut (“gyorsbillentyű”), not a desktop/launcher icon.
- `taskbar-tabs-email-callout-subtitle-v3` — `browser/browser/featureCallout.ftl` — The email taskbar-tab callout says “chat sites” instead of “email sites”.
  - Current: `Indítsa el csevegőoldalait alkalmazásként`
  - Source: `Launch your email sites like an app in a streamlined window protected by { -brand-short-name }.`
  - Suggest: `Indítsa el e-mail-oldalait alkalmazásként`
  - en-US reads “Launch your email sites like an app”; the Hungarian duplicates the chat variant’s wording, so the message contradicts its own title about the inbox.
- `firefoxview-search-text-box-history` — `browser/browser/firefoxView.ftl` — Search placeholder rendered as the noun “search history” instead of “search the history”.
  - Current: `Keresés előzményei`
  - Source: `placeholder: Search history`
  - Suggest: `Előzmények keresése`
  - The developer comment marks “search” as a verb, and all sibling placeholders in the same file use the “X keresése” pattern.
- `genai-settings-chat-gemini-links` — `browser/browser/genai.ftl` — Malformed closing tag `</a >` in `genai-settings-chat-gemini-links`
  - Current: `A Google Gemini választásával elfogadja a <a data-l10n-name="link1">Google szolgáltatási feltételeit</a>, a <a data-l10n-name="link2">Generatív MI tiltott használatára vonatkozó irányelveket</a > és a <a data-l10n-name=…`
  - Source: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
  - Suggest: `By choosing Google Gemini, you agree to the <a data-l10n-name="link1">Google Terms of Service</a>, <a data-l10n-name="link2">Generative AI Prohibited Use Policy</a>, and <a data-l10n-name="link3">Gemini Apps Privacy Not…`
  - Whitespace inside a closing tag makes it render as literal text.
- `menu-help-exit-troubleshoot-mode` — `browser/browser/menubar.ftl` — Reversed meaning: the item that turns Troubleshoot Mode off is labelled as turning it on.
  - Current: `Hibakeresési mód bekapcsolása`
  - Source: `accesskey: M label: Turn Troubleshoot Mode Off`
  - Suggest: `Hibaelhárítási mód kikapcsolása`
  - en-US is “Turn Troubleshoot Mode Off”; the Hungarian says “Turn … Mode On”. It also uses “Hibakeresési” where the sibling string menu-help-enter-troubleshoot-mode2 and safeMode.ftl use “Hibaelhárítási”.
- `menu-history-search` — `browser/browser/menubar.ftl` — “Search History” rendered as the noun phrase “history of searches” instead of the action “search in history”.
  - Current: `Keresés előzményei`
  - Source: `label: Search History`
  - Suggest: `Előzmények keresése`
  - The developer comment states “Search” is a verb, as in “Search in History”. Compare menu-bookmarks-search, correctly rendered “Könyvjelzők keresése”.
- `annotations-make-default-pdf-handler-title` — `browser/browser/newtab/asrouter.ftl` — "Default PDF editor" translated as default PDF viewer.
  - Current: `alapértelmezett PDF-megjelenítője`
  - Source: `Make { -brand-short-name } your default PDF editor?`
  - Suggest: `alapértelmezett PDF-szerkesztője`
  - The message is about editing/signing PDFs; "megjelenítő" is the term used for the PDF viewer (policy-PDFjs), so it understates and confuses the two features.
- `fxa-menu-message-mobile-primary-text` — `browser/browser/newtab/asrouter.ftl` — Imperative CTA "Send tabs to your phone" turned into a third-person statement.
  - Current: `Lapokat küld a telefonjára`
  - Source: `Send tabs to your phone`
  - Suggest: `Küldjön lapokat a telefonjára`
  - "Lapokat küld" reads as "it sends tabs"; the neighbouring primary texts in the same group use imperatives ("Szinkronizálja…", "Készítsen…", "Tartsa…").
- `newtab-privacy-message-info-11` — `browser/browser/newtab/newtab.ftl` — "more private" rendered as "more securely".
  - Current: `hogyan segíti elő, hogy biztonságosabban böngésszen`
  - Source: `Find out how { -brand-short-name } helps keep your browsing more private.`
  - Suggest: `hogyan segít abban, hogy bizalmasabban böngésszen`
  - The source is about privacy, not security; the same widget renders "more private" as "bizalmasabban" (newtab-privacy-message-promo-vpn-3, promo-private-window-1).
- `newtab-section-following-button` — `browser/browser/newtab/newtab.ftl` — "Following" (state) rendered identically to "Follow" (action).
  - Current: `Követés`
  - Source: `Following`
  - Suggest: `Követve`
  - newtab-section-follow-button is also "Követés", so the followed state is indistinguishable from the follow action; the state label should be "Követve" (cf. newtab-section-blocked-button = "Blokkolva").
- `newtab-sports-widget-loading-more` — `browser/browser/newtab/newtab.ftl` — "Loading more matches" translated as loading more search results.
  - Current: `További találatok betöltése…`
  - Source: `Loading more matches…`
  - Suggest: `További mérkőzések betöltése…`
  - "matches" here means sports matches ("mérkőzés"), which is the term used throughout the sports widget; "találat" means a search hit.
- `newtab-sports-widget-watch` — `browser/browser/newtab/newtab.ftl` — "Watch" (view a live stream) translated as "Follow", colliding with the widget's follow-teams action.
  - Current: `Követés`
  - Source: `label: Watch title: Watch live`
  - Suggest: `Megtekintés`
  - The dev comment says "Watch is a verb (as in watch matches online)". "Követés" is the term the same widget uses for following teams (newtab-sports-widget-follow-teams), so the button now reads as a different, existing action.
- `newtab-topsites-add-shortcut-header` — `browser/browser/newtab/newtab.ftl` — "Shortcut" translated as "quick search" instead of the term used everywhere else.
  - Current: `Új gyorskereső`
  - Source: `New Shortcut`
  - Suggest: `Új indítóikon`
  - Top Sites shortcuts are rendered "indítóikon" throughout the file (newtab-topsites-add-shortcut-label, newtab-custom-shortcuts-title); "gyorskereső" means quick-search and misdescribes the dialog.
- `newtab-topsites-edit-shortcut-header` — `browser/browser/newtab/newtab.ftl` — "Edit Shortcut" translated as editing a quick search.
  - Current: `Gyorskereső szerkesztése`
  - Source: `Edit Shortcut`
  - Suggest: `Indítóikon szerkesztése`
  - Same inconsistency as newtab-topsites-add-shortcut-header; the rest of the file uses "indítóikon" for shortcut.
- `newtab-wallpaper-category-title-celestial` — `browser/browser/newtab/newtab.ftl` — "Celestial" rendered with the religious sense the developer comment explicitly warns against.
  - Current: `Mennyei`
  - Source: `Celestial`
  - Suggest: `Égi`
  - The comment says the word means astronomical/sky-related and is "Not to be confused with religious definition of the word." Hungarian "mennyei" means heavenly/divine (and colloquially 'delicious'); the astronomy sense is "égi".
- `mr2022-onboarding-colorway-tooltip-innovator2` — `browser/browser/newtab/onboarding.ftl` — Colorway name rendered differently in the tooltip than in its own label and description.
  - Current: `Innovátor (narancs)`
  - Source: `title: Innovator (orange)`
  - Suggest: `Újító (narancs)`
  - mr2022-onboarding-colorway-label-innovator and -description-innovator both use "újító", so the tooltip names a different colorway than the swatch it describes.
- `onboarding-new-user-survey-legal-link-label` — `browser/browser/newtab/onboarding.ftl` — Malformed closing tag `</a >` in `onboarding-new-user-survey-legal-link-label`
  - Current: `A „{ onboarding-new-user-survey-next-button-label }” kiválasztásával elfogadja a { -brand-product-name } <a data-l10n-name="privacy_notice">Adatvédelmi nyilatkozatát</a >`
  - Source: `By selecting “{ onboarding-new-user-survey-next-button-label },” you agree to { -brand-product-name }’s <a data-l10n-name="privacy_notice">Privacy Notice</a>`
  - Suggest: `By selecting “{ onboarding-new-user-survey-next-button-label },” you agree to { -brand-product-name }’s <a data-l10n-name="privacy_notice">Privacy Notice</a>`
  - Whitespace inside a closing tag makes it render as literal text.
- `blocklist-treehead-list` — `browser/browser/preferences/blocklists.ftl` — Column header "List" rendered as the action noun "Listing".
  - Current: `Listázás`
  - Source: `label: List`
  - Suggest: `Lista`
  - This is a tree column header naming the block list, a noun; "Listázás" means the act of listing.
- `appearance-browser-icon-requirement` — `browser/browser/preferences/browserIcon.ftl` — "Complete" rendered as "fill out (a form)".
  - Current: `Töltse ki, és oldjon fel további rókás ikonokat`
  - Source: `message: Complete and unlock bonus fox icons to personalize { -brand-short-name }.`
  - Suggest: `Teljesítse a feltételeket, és oldjon fel további rókás ikonokat`
  - en-US: "Complete and unlock bonus fox icons" refers to completing the requirements (default browser + pinned to taskbar). "Töltse ki" means filling in a form and makes the sentence unintelligible in context.
- `cookie-banner-blocker-description` — `browser/browser/preferences/preferences.ftl` — "refuses for you" rendered as "rejects you".
  - Current: `a { -brand-short-name } automatikusan elutasítja Önt`
  - Source: `When a site asks if they can use cookies in private browsing mode, { -brand-short-name } automatically refuses for you. Only on supported sites.`
  - Suggest: `a { -brand-short-name } automatikusan elutasítja Ön helyett`
  - en-US: "{ -brand-short-name } automatically refuses for you". The Hungarian says the browser rejects the user, not that it declines the cookie request on the user's behalf.
- `open-external-link-next-to-active-tab` — `browser/browser/preferences/preferences.ftl` — Modifier attached to the wrong noun, changing the meaning.
  - Current: `Hivatkozások megnyitása az aktív lap melletti alkalmazásokból`
  - Source: `label: Open links from apps next to your active tab`
  - Suggest: `Alkalmazásokból származó hivatkozások megnyitása az aktív lap mellett`
  - en-US: "Open links from apps next to your active tab" — the links open next to the active tab. The Hungarian reads "open links from the apps that are next to the active tab", which is not what the preference does.
- `sitedata-option-block-cross-site-cookies` — `browser/browser/preferences/preferences.ftl` — Blocking of tracking cookies turned into isolation.
  - Current: `Webhelyek közötti követő és egyéb webhelyek közötti sütik elkülönítése`
  - Source: `label: Cross-site tracking cookies, and isolate other cross-site cookies`
  - Suggest: `Webhelyek közötti nyomkövető sütik, és a többi webhelyek közötti süti elkülönítése`
  - en-US: "Cross-site tracking cookies, and isolate other cross-site cookies" — the first item is blocked (this is the "Type blocked" dropdown), only the rest are isolated. The Hungarian applies isolation to both.
- `sidebar-history-sort-option-date-and-site` — `browser/browser/sidebar.ftl` — Sort option says “Date and time” instead of “Date and site”.
  - Current: `Dátum és idő`
  - Source: `label: Date and site`
  - Suggest: `Dátum és webhely`
  - en-US is “Date and site”; the adjacent option sidebar-history-sort-option-site is correctly “Webhely”, so the sort criterion is misnamed.
- `tab-context-separate-split-view` — `browser/browser/tabbrowser.ftl` — Verb “Separate” rendered as the adverb “apart”, so the menu item reads as a state, not an action.
  - Current: `Külön osztott nézet`
  - Source: `accesskey: t label: Separate Split View`
  - Suggest: `Osztott nézet szétválasztása`
  - The developer comment says “Separate” is a verb; split-view-menuitem-separate-tabs correctly uses “Lapok szétválasztása”.
- `tabbrowser-confirm-close-tabs-with-key-checkbox` — `browser/browser/tabbrowser.ftl` — Case suffix turns “quitting with <key>” into “quitting from <key>”.
  - Current: `Megerősítés a { $quitKey }ból történő kilépés előtt`
  - Source: `Confirm before quitting with { $quitKey }`
  - Suggest: `Megerősítés a { $quitKey } billentyűvel történő kilépés előtt`
  - en-US “Confirm before quitting with { $quitKey }”. The -ból ablative reads as quitting out of the key; the parallel string tabbrowser-ask-close-tabs-with-key-checkbox uses the correct “billentyűvel”.
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — Malformed closing tag `</a >` in `tou-existing-user-spotlight-body`
  - Current: `Bevezettük a <a data-l10n-name="terms-of-use">Használati feltételeket</a> és frissítettük az <a data-l10n-name="privacy-notice">Adatvédelmi nyilatkozatunkat</a >.<br><br> Szánjon egy percet az ellenőrzésére és elfogadás…`
  - Source: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
  - Suggest: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
  - Whitespace inside a closing tag makes it render as literal text.
- `text-recognition-modal-searching-title` — `browser/browser/textRecognition.ftl` — Subject and object are swapped: says “searching for an image by text” instead of “searching the image for text”.
  - Current: `Kép keresése szöveg alapján…`
  - Source: `Searching image for text…`
  - Suggest: `Szöveg keresése a képen…`
  - en-US “Searching image for text…” means scanning the image to find text; the Hungarian states the opposite relationship.
- `webrtc-allow-share-screen-and-microphone-unsafe-delegation` — `browser/browser/webrtcIndicator.ftl` — Permission prompt names the camera instead of the microphone.
  - Current: `hozzáférjen a kamerájához és lássa a képernyőjét?`
  - Source: `Allow { $origin } to give { $thirdParty } access to your microphone and see your screen?`
  - Suggest: `hozzáférjen a mikrofonjához, és lássa a képernyőjét?`
  - en-US: “give { $thirdParty } access to your microphone and see your screen?”. The prompt grants microphone + screen access, so naming the camera misinforms the user about what is being granted.
- `webauthn.selectSignResultPrompt` — `browser/chrome/browser/browser.properties` — “or cancel” rendered as “or delete”.
  - Current: `Válassza ki, hogy melyiket szeretné használni vagy törölni.`
  - Source: `Multiple accounts found for %S. Select which to use or cancel.`
  - Suggest: `Válassza ki, melyiket szeretné használni, vagy szakítsa meg a műveletet.`
  - en-US “Select which to use or cancel” offers cancelling the operation; “törölni” tells the user they can delete an account, an action the dialog does not offer.
- `edit-controls.tooltiptext2` — `browser/chrome/browser/customizableui/customizableWidgets.properties` — The noun phrase “Edit controls” is rendered as the command “Edit the controls”.
  - Current: `Vezérlőelemek szerkesztése`
  - Source: `Edit controls`
  - Suggest: `Szerkesztésvezérlők`
  - This tooltip names the cut/copy/paste widget group, as the sibling label edit-controls.label correctly renders it (“Szerkesztésvezérlők”); the tooltip instead promises that the controls themselves can be edited.
- `dialogTitleEditBookmarkFolder` — `browser/chrome/browser/places/bookmarkProperties.properties` — “Edit bookmark folder” translated as “Add bookmark folder”.
  - Current: `Könyvjelző mappa hozzáadása`
  - Source: `Edit bookmark folder`
  - Suggest: `Könyvjelző mappa szerkesztése`
  - The dialog title for editing is identical to dialogTitleAddBookmarkFolder; en-US is “Edit bookmark folder” and the parallel string dialogTitleEditBookmarksFolder correctly uses “szerkesztése”.
- `clientSocketMisconfiguration` — `browser/chrome/overrides/appstrings.properties` — “doesn’t know how to communicate” rendered as “doesn’t know whether to communicate”.
  - Current: `A Firefox nem tudja, hogy kommunikáljon a kiszolgálóval.`
  - Source: `Firefox doesn’t know how to communicate with the server.`
  - Suggest: `A Firefox nem tudja, hogyan kommunikáljon a kiszolgálóval.`
  - Without “hogyan”, the clause reads as uncertainty about whether to communicate, not about the manner; the manner is what en-US states.
- `unknownSocketType` — `browser/chrome/overrides/appstrings.properties` — “doesn’t know how to communicate” rendered as “doesn’t know whether to communicate”.
  - Current: `A Firefox nem tudja, hogy kommunikáljon a kiszolgálóval.`
  - Source: `Firefox doesn’t know how to communicate with the server.`
  - Suggest: `A Firefox nem tudja, hogyan kommunikáljon a kiszolgálóval.`
  - Same as clientSocketMisconfiguration: the missing “hogyan” changes the meaning of the error message.
- `autofillReauthCheckboxLin` — `browser/extensions/formautofill/formautofill.properties` — “stored credit cards” translated as “stored authentication data”.
  - Current: `Linux-hitelesítés megkövetelése a tárolt hitelesítési adatok automatikus kitöltéséhez, megtekintéséhez vagy szerkesztéséhez.`
  - Source: `Require Linux authentication to autofill, view, or edit stored credit cards.`
  - Suggest: `Linux-hitelesítés megkövetelése a tárolt bankkártyaadatok automatikus kitöltéséhez, megtekintéséhez vagy szerkesztéséhez.`
  - en-US: “Require Linux authentication to autofill, view, or edit stored credit cards.” The Hungarian names authentication data instead of credit cards.
- `autofillReauthCheckboxMac` — `browser/extensions/formautofill/formautofill.properties` — “stored credit cards” translated as “stored authentication data”.
  - Current: `MacOS-hitelesítés megkövetelése a tárolt hitelesítési adatok automatikus kitöltéséhez, megtekintéséhez vagy szerkesztéséhez.`
  - Source: `Require macOS authentication to autofill, view, or edit stored credit cards.`
  - Suggest: `macOS-hitelesítés megkövetelése a tárolt bankkártyaadatok automatikus kitöltéséhez, megtekintéséhez vagy szerkesztéséhez.`
  - en-US says “autofill, view, or edit stored credit cards”; the Hungarian says the setting protects stored authentication data, describing a different feature. Also “MacOS” should be “macOS” as elsewhere in the file (useCreditCardPasswordPrompt notes, en-US spelling).
- `autofillReauthCheckboxWin` — `browser/extensions/formautofill/formautofill.properties` — “stored credit cards” translated as “stored authentication data”.
  - Current: `Windows-hitelesítés megkövetelése a tárolt hitelesítési adatok automatikus kitöltéséhez, megtekintéséhez vagy szerkesztéséhez.`
  - Source: `Require Windows authentication to autofill, view, or edit stored credit cards.`
  - Suggest: `Windows-hitelesítés megkövetelése a tárolt bankkártyaadatok automatikus kitöltéséhez, megtekintéséhez vagy szerkesztéséhez.`
  - en-US: “Require Windows authentication to autofill, view, or edit stored credit cards.” The Hungarian names authentication data instead of credit cards, describing the wrong protected object.
- `STUB_BLURB_SECOND1` — `browser/installer/nsisstrings.properties` — "Faster page loading and tab switching" became "faster page loading, without tab switching".
  - Current: `Gyorsabb oldalbetöltés, lapváltás nélkül`
  - Source: `Faster page loading and tab switching`
  - Suggest: `Gyorsabb oldalbetöltés és lapváltás`
  - The English lists two things that are faster; the Hungarian negates the second one ("nélkül" = without), stating the opposite of the source.
- `LicenseTextRB` — `browser/installer/override.properties` — "select the first option below" became "choose from the options below".
  - Current: `válasszon az alábbi lehetőségek közül`
  - Source: `Please review the license agreement before installing $BrandFullNameDA. If you accept all terms of the agreement, select the first option below. $_CLICK`
  - Suggest: `válassza az alábbi első lehetőséget`
  - The English tells the user which specific radio button to pick; the Hungarian drops "first", so the instruction no longer identifies the accept option.
- `attachments_label` — `browser/pdfviewer/viewer.properties` — Sidebar button label “Attachments” rendered as the sentence “There is an attachment”.
  - Current: `Van melléklet`
  - Source: `Attachments`
  - Suggest: `Mellékletek`
  - This is the alt text/label of the attachments panel button, a noun; all neighbouring labels (Rétegek, Bélyegképek) are plain nouns. “Van melléklet” asserts that an attachment exists.
- `document_outline.title` — `browser/pdfviewer/viewer.properties` — “Show Document Outline” rendered as “show document online”.
  - Current: `Dokumentum megjelenítése online (dupla kattintás minden elem kinyitásához/összecsukásához)`
  - Source: `Show Document Outline (double-click to expand/collapse all items)`
  - Suggest: `Dokumentumvázlat megjelenítése (dupla kattintás minden elem kinyitásához/összecsukásához)`
  - “outline” was read as “online”. The sibling label document_outline_label correctly uses “Dokumentumvázlat”, so the tooltip contradicts the button it describes.
- `document_properties_page_size_name_legal` — `browser/pdfviewer/viewer.properties` — The paper size name “Legal” is translated as “Legal information”.
  - Current: `Jogi információk`
  - Source: `Legal`
  - Suggest: `Legal`
  - This string is a paper format name in the list with A3, A4 and Letter (all left untranslated). “Jogi információk” means “legal information” and names the wrong thing entirely.
- `about-debugging-browser-version-too-recent` — `devtools/client/aboutdebugging.ftl` — An extra sentence was added: the message tells the user twice to update, once about the wrong browser.
  - Current: `Frissítse a csatlakoztatott böngészőt. Frissítse a Firefoxot.`
  - Source: `The connected browser is more recent ({ $runtimeVersion }, buildID { $runtimeID }) than your { -brand-shorter-name } ({ $localVersion }, buildID { $localID }). This is an unsupported setup and may cause DevTools to fail…`
  - Suggest: `Frissítse a Firefoxot.`
  - en-US has only "Please update Firefox." here; instructing the user to update the connected (remote) browser contradicts the message, which says the connected browser is newer.
- `about-debugging-runtime-profile-button2` — `devtools/client/aboutdebugging.ftl` — "Profile performance" (verb phrase) rendered as the noun phrase "Performance of the profile".
  - Current: `about-debugging-runtime-profile-button2 = Profil teljesítménye`
  - Source: `Profile performance`
  - Suggest: `about-debugging-runtime-profile-button2 = Teljesítmény profilozása`
  - The comment says this is the button that opens the performance profiler panel; "Profil teljesítménye" states a property of a profile instead of the action.
- `about-debugging-worker-fetch-not-listening` — `devtools/client/aboutdebugging.ftl` — Negation dropped: the "not listening for fetch events" state is translated identically to the "listening" state.
  - Current: `.value = Fetch események figyelése`
  - Source: `label: Fetch value: Not listening for fetch events`
  - Suggest: `.value = Nem figyeli a Fetch eseményeket`
  - en-US: "Not listening for fetch events" vs. the sibling string "Listening for fetch events"; the Hungarian value is identical for both keys, so the UI reports the opposite state.
- `accessibility-text-label-issue-optgroup-label2` — `devtools/client/accessibility.ftl` — "label attribute" rendered as "label element".
  - Current: `Használja a <code>label</code> elemet, hogy címkét adjon a <span>optgroup</span> elemnek.`
  - Source: `Use a <code>label</code> attribute to label an <span>optgroup</span>. <a>Learn more</a>`
  - Suggest: `Használja a <code>label</code> attribútumot, hogy címkét adjon az <span>optgroup</span> elemnek.`
  - en-US says "Use a label attribute"; an optgroup is labelled by its label attribute, not by a label element, and the parallel key in devtools/shared/accessibility.properties says "attribútumot".
- `manifest-item-identity` — `devtools/client/application.ftl` — Manifest "Identity" section header translated as "User".
  - Current: `manifest-item-identity = Felhasználó`
  - Source: `Identity`
  - Suggest: `manifest-item-identity = Azonosság`
  - The section shows the web app manifest's identity fields (name, short_name); "Felhasználó" means "user" and names the wrong thing.
- `boxmodel.offsetParent.title` — `devtools/client/boxmodel.properties` — "Offset parent of the selected element" turned into "Offset of the selected element's parent".
  - Current: `boxmodel.offsetParent.title = A kiválasztott elem szülőjének eltolása`
  - Source: `Offset parent of the selected element`
  - Suggest: `boxmodel.offsetParent.title = A kiválasztott elem eltolási szülője`
  - The comment says the previewed DOM node is the offset parent of the positioned element; the Hungarian describes an offset belonging to the parent instead.
- `callStack.group.collapseTooltip` — `devtools/client/debugger.properties` — Call-stack "frames" translated as "képkockák" (video frames).
  - Current: `callStack.group.collapseTooltip = %S képkockák összecsukása`
  - Source: `Collapse %S frames`
  - Suggest: `callStack.group.collapseTooltip = %S keretek összecsukása`
  - Same defect as callStack.group.expandTooltip; "keret" is used for stack frames elsewhere in this file (restartFrame, callStack.group.collapseTooltipWithSelectedFrame).
- `callStack.group.expandTooltip` — `devtools/client/debugger.properties` — Call-stack "frames" translated as "képkockák" (video frames).
  - Current: `callStack.group.expandTooltip = %S képkockák megjelenítése`
  - Source: `Show %S frames`
  - Suggest: `callStack.group.expandTooltip = %S keretek megjelenítése`
  - These are stack frames in the Call Stack pane; the neighbouring string callStack.group.collapseTooltipWithSelectedFrame correctly uses "keret".
- _…and 56 more; see `state/` for the full list._

### B. Mistranslation, reversed meaning, wrong names & brand

- `genai-onboarding-copilot-learn` — `browser/browser/genai.ftl` — The product name Copilot is misspelled as “Coplit”.
  - Current: `Tudjon meg többet a Coplitról`
  - Source: `Learn more about Copilot`
  - Suggest: `Tudjon meg többet a Copilotról`
  - Copilot is a brand name and must be spelled correctly; the same file spells it correctly elsewhere.
- `autofill-address-department` — `browser/browser/preferences/formAutofill.ftl` — Administrative division rendered as an organizational "department".
  - Current: `Részleg`
  - Source: `Department`
  - Suggest: `Megye (departamento)`
  - The developer comment states this is the primary administrative division used in Nicaragua and Colombia. "Részleg" means a section/unit of a company or institution, not a territorial division.
- `autofill-address-parish` — `browser/browser/preferences/formAutofill.ftl` — Civil division rendered with the religious term.
  - Current: `Egyházközség`
  - Source: `Parish`
  - Suggest: `Kerület (parish)`
  - The comment states this is primary address information (1 level below the country) in Barbados and Jamaica; "egyházközség" denotes a church congregation, not a civil administrative unit.
- `autofill-address-post-town` — `browser/browser/preferences/formAutofill.ftl` — "Post town" rendered as "post station".
  - Current: `Postaállomás`
  - Source: `Post town`
  - Suggest: `Postaváros`
  - The comment marks this as secondary address information for GB/NO/SE — the town used for postal routing, not a postal facility ("postaállomás").
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — “Beta” translated as “Béta” although the developer comment forbids translating it.
  - Current: `Próbálja ki a privát fordításokat a { -brand-shorter-name }ban – Béta`
  - Source: `tooltiptext: Try private translations in { -brand-shorter-name } - Beta`
  - Suggest: `Próbálja ki a privát fordításokat a { -brand-shorter-name }ban – Beta`
  - The comment immediately above the string says “Beta” should not be translated because it mirrors the un-localized BETA icon.
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — “Beta” translated as “Béta” although the developer comment forbids translating it.
  - Current: `Oldal lefordítása – Béta`
  - Source: `tooltiptext: Translate this page - Beta`
  - Suggest: `Oldal lefordítása – Beta`
  - The comment states: “Note that here "Beta" should not be translated, as it is a reflection of the un-localized BETA icon that is in the panel.”
- `serviceworker-empty-suggestions2` — `devtools/client/application.ftl` — "service worker" misspelled as "server worker" twice in the same string.
  - Current: `server workernek`
  - Source: `If the current page should have a service worker, you could look for errors in the <a>Console</a> or step through your service worker registration in the <span>Debugger</span>.`
  - Suggest: `service workernek`
  - The technology name is "service worker" and is spelled correctly everywhere else in this file (serviceworker-empty-intro2, serviceworker-worker-debug).
- `inactive-css-not-display-block-on-floated` — `devtools/client/tooltips.ftl` — The CSS keyword value <strong>block</strong> was translated as "blokkolásra" ("to blocking").
  - Current: `A <strong>display</strong> értéket <strong>blokkolásra</strong> változtatta a motor`
  - Source: `The <strong>display</strong> value has been changed by the engine to <strong>block</strong> because the element is <strong>floated</strong>.`
  - Suggest: `A <strong>display</strong> értéket <strong>block</strong> értékre változtatta a motor`
  - The section comment says CSS properties and values in <strong> tags should not be translated; "blokkolásra" also means "blocking", not the display value.
- `btp-warning-tracker-classified` — `toolkit/toolkit/global/antiTracking.ftl` — "bounce tracker" was translated although the developer comment forbids it.
  - Current: `visszapattanás-követőnek lett besorolva`
  - Source: `{$gracePeriodSeconds ->} [other] “{ $siteHost }” has been classified as a bounce tracker. If it does not receive user activation within the next { $gracePeriodSeconds } seconds it will have its state purged.`
  - Suggest: `„bounce tracker”-nek lett besorolva`
  - The comment directly above the string states: 'Do not translate "bounce tracker".'
- `btp-warning-tracker-purged` — `toolkit/toolkit/global/antiTracking.ftl` — "bounce tracker" was translated although the developer comment forbids it.
  - Current: `visszapattanás-követőként észlelték`
  - Source: `The state of “{ $siteHost }” was recently purged because it was detected as a bounce tracker.`
  - Suggest: `„bounce tracker”-ként észlelték`
  - The comment directly above the string states: 'Do not translate "bounce tracker".'

### C. Grammar, agreement & spelling

- `about-private-browsing-cookie-banners-promo-body` — `browser/browser/aboutPrivateBrowsing.ftl` — Wrong case on the quantifier: “kevesebbet nyomkövetést”.
  - Current: `így kevesebbet nyomkövetést kap`
  - Source: `We now automatically refuse many cookie banners so you can get tracked less and go back to distraction-free browsing.`
  - Suggest: `így kevesebb nyomkövetést kap`
  - “kevesebb” must be uninflected when modifying the accusative noun; “kevesebbet nyomkövetést” doubles the accusative marking.
- `ai-window-delete-all-memories-message` — `browser/browser/aiFeatures.ftl` — A leftover verb makes the sentence ungrammatical.
  - Current: `akkor vegye kapcsolja ki a „Tanulás…” lehetőségeket`
  - Source: `Existing memories will be deleted. If you don’t want any new memories created, uncheck the options to “Learn from…” in { -smart-window-brand-name } settings.`
  - Suggest: `akkor kapcsolja ki a „Tanulás…” lehetőségeket`
  - “vegye” is stray editing residue before “kapcsolja ki”; two conflicting imperatives cannot stand together.
- `smartbar-placeholder-hint-1` — `browser/browser/aiWindow.ftl` — Indefinite verb form used with a definite object.
  - Current: `A @ használatával említhet meg a legutóbbi lapokat…`
  - Source: `Use @ to mention recent tabs…`
  - Suggest: `A @ használatával említheti meg a legutóbbi lapokat…`
  - “a legutóbbi lapokat” is a definite object, requiring the definite conjugation “említheti”.
- `identity-etsi` — `browser/browser/browser.ftl` — Misspelling of “rendeletben”.
  - Current: `Az (EU) 2024/1183 rendeleteben meghatározottak szerint.`
  - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
  - Suggest: `Az (EU) 2024/1183 rendeletben meghatározottak szerint.`
  - The inessive of “rendelet” is “rendeletben”; “rendeleteben” is not a valid form.
- `urlbar-result-dismissal-acknowledgment-market` — `browser/browser/browser.ftl` — Wrong definite article before a consonant-initial word.
  - Current: `Többé nem fogja látni az pénzpiaci javaslatokat.`
  - Source: `Thanks for your feedback. You won’t see market suggestions anymore.`
  - Suggest: `Többé nem fogja látni a pénzpiaci javaslatokat.`
  - “az” is only used before vowel-initial words; “pénzpiaci” begins with a consonant.
- `content-sharing-modal-no-shareable-links` — `browser/browser/contentSharing.ftl` — The heading is ungrammatical and does not convey “No shareable links included”.
  - Current: `Nincs tartalmaz megosztható hivatkozásokat`
  - Source: `heading: No shareable links included message: Only links to web content can be shared.`
  - Suggest: `Nem tartalmaz megosztható hivatkozásokat`
  - “Nincs tartalmaz” combines a negative existential with a finite verb and is not a valid Hungarian clause.
- `customize-mode-touchbar-cmd` — `browser/browser/customizeMode.ftl` — “Touch Bar” is misspelled as “Érintősár”.
  - Current: `Érintősár testreszabása…`
  - Source: `label: Customize Touch Bar…`
  - Suggest: `Érintősáv testreszabása…`
  - The intended word is “Érintősáv” (Touch Bar); “Érintősár” is a typo with no meaning.
- `genai-prompts-explain` — `browser/browser/genai.ftl` — Wrong verbal prefix in the prompt body: “Magyarázza le”.
  - Current: `Magyarázza le a kulcsfogalmakat a kijelölésben`
  - Source: `label: Explain this value: Please explain the key concepts in this selection, using simple words. Also, use examples.`
  - Suggest: `Magyarázza el a kulcsfogalmakat a kijelölésben`
  - “megmagyarázni/elmagyarázni” is the correct form; the label of the same message correctly uses “Magyarázza el”.
- `genai-settings-chat-claude-links` — `browser/browser/genai.ftl` — Last item of the enumeration is not in the accusative required by “elfogadja”.
  - Current: `és az <a data-l10n-name="link3">Adatvédelmi irányelvek</a>`
  - Source: `By choosing Anthropic Claude, you agree to the Anthropic <a data-l10n-name="link1">Consumer Terms of Service</a>, <a data-l10n-name="link2">Usage Policy</a>, and <a data-l10n-name="link3">Privacy Policy</a>.`
  - Suggest: `és az <a data-l10n-name="link3">Adatvédelmi irányelveit</a>`
  - The other two coordinated objects are accusative (“feltételeit”, “irányelveket”); the third one is left in the nominative.
- `ipprotection-feature-introduction-link-text-privacy-1` — `browser/browser/ipProtection.ftl` — The definite article is duplicated before the link text.
  - Current: `A <a data-l10n-name="learn-more-vpn">A { -brand-product-name } beépített VPN-je</a>`
  - Source: `<a data-l10n-name="learn-more-vpn">{ -brand-product-name }’s built-in VPN</a> helps protect your browsing. Choose from several locations to keep where you browse more private.`
  - Suggest: `<a data-l10n-name="learn-more-vpn">A { -brand-product-name } beépített VPN-je</a>`
  - The article appears both outside and inside the link, producing “A A Firefox beépített VPN-je”; the -2 variant of the same string has it only once.
- `mr1-onboarding-theme-label-alpenglow` — `browser/browser/newtab/onboarding.ftl` — Theme name "Alpenglow" was translated although the developer comment forbids it.
  - Current: `Alpesi fény`
  - Source: `Alpenglow`
  - Suggest: `Alpenglow`
  - The dev comment states: "'Alpenglow' here is the name of the theme, and should be kept in English." The Hungarian renders it as a common noun, breaking the product name.
- `general-url` — `browser/browser/pageInfo.ftl` — “Address” and “Title” are both rendered “Cím:”, making two adjacent fields in the same panel indistinguishable.
  - Current: `Cím:`
  - Source: `value: Address:`
  - Suggest: `Webcím:`
  - general-title (“Title:”) is also “Cím:”. Elsewhere in the tree “URL/Address” is consistently “Webcím” (e.g. placesPrompts.ftl, reportBrokenSite.ftl), so the address row should use “Webcím:”.
- `tou-existing-user-spotlight-body` — `browser/browser/termsofuse.ftl` — “Terms of Use” rendered “Használati feltételek” here but “Felhasználási feltételek” in the sibling strings of the same feature.
  - Current: `Használati feltételeket`
  - Source: `We’ve introduced a <a data-l10n-name="terms-of-use">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice">Privacy Notice</a>.<br><br> Please take a moment to review and accept. <a data-l10n-name="learn-mor…`
  - Suggest: `Felhasználási feltételeket`
  - existing-user-tou-message and preonboarding.ftl consistently use “Felhasználási feltételek” for the same legal document, so the differing term in this Spotlight body is an inconsistency.
- `maxTimersExceeded` — `devtools/client/webconsole.properties` — console.time() timers called "óra" (clock) while every neighbouring string uses "időzítő".
  - Current: `maxTimersExceeded = Ezen az oldalon nem indítható el több óra.`
  - Source: `The maximum allowed number of timers in this page was exceeded.`
  - Suggest: `maxTimersExceeded = Ezen az oldalon nem indítható el több időzítő.`
  - timerAlreadyExists/timerDoesntExist/timerJSError all render "timer" as "időzítő"; "óra" (clock/hour) is wrong in this surface.
- `maxTimersExceeded` — `devtools/shared/webconsole.properties` — console.time() timers called "óra" (clock) while every neighbouring string uses "időzítő".
  - Current: `maxTimersExceeded = Ezen az oldalon nem indítható el több óra.`
  - Source: `The maximum allowed number of timers in this page was exceeded.`
  - Suggest: `maxTimersExceeded = Ezen az oldalon nem indítható el több időzítő.`
  - Same defect as the client copy: the surrounding timer strings use "időzítő".
- `CSSContainerRuleSingleConditionWarning` — `dom/chrome/dom/dom.properties` — The do-not-translate identifier CSSContainerRule is misspelled as CSSSContainerRule twice.
  - Current: `A CSSSContainerRule.containerName és a CSSContainerRule.containerQuery nem támogat több feltételt. Használja helyette a CSSSContainerRule.conditions mezőt.`
  - Source: `CSSContainerRule.containerName and CSSContainerRule.containerQuery don’t support multiple conditions. Use CSSContainerRule.conditions instead.`
  - Suggest: `A CSSContainerRule.containerName és a CSSContainerRule.containerQuery nem támogat több feltételt. Használja helyette a CSSContainerRule.conditions mezőt.`
  - The comment says do not translate CSSContainerRule.containerName / .containerQuery / .conditions; a triple S makes the suggested API name non-existent for developers copying it.
- `MathML_DeprecatedStyleAttributeWarning` — `dom/chrome/dom/dom.properties` — The MathML attribute name fontstyle is misspelled as “fonststlye”.
  - Current: `„fonststlye”`
  - Source: `MathML attributes “background”, “color”, “fontfamily”, “fontsize”, “fontstyle” and “fontweight” are deprecated and will be removed at a future date.`
  - Suggest: `„fontstyle”`
  - en-US lists “fontstyle” and the note says do not translate it; the garbled token names a nonexistent attribute.
- `MediaStreamTrackAudioSourceNodeCrossOrigin` — `dom/chrome/dom/dom.properties` — The API name MediaStreamTrack was replaced by MediaStream, although the developer comment says not to translate it.
  - Current: `A createMediaStreamTrackSource-nak átadott MediaStream egy cross-origin erőforrás`
  - Source: `The MediaStreamTrack passed to createMediaStreamTrackSource is a cross-origin resource, the node will output silence.`
  - Suggest: `A createMediaStreamTrackSource-nak átadott MediaStreamTrack egy cross-origin erőforrás`
  - en-US: “The MediaStreamTrack passed to createMediaStreamTrackSource is a cross-origin resource”. The note says “Do not translate MediaStreamTrack and createMediaStreamTrackSource”; the message now names a different interface than the one the error is about.
- `UseSendBeaconDuringUnloadAndPagehideWarning` — `dom/chrome/dom/dom.properties` — The do-not-translate event name “unload” is written as “unlode”, with a wrong article.
  - Current: `a unlode és pagehide folyamatokban`
  - Source: `Use of navigator.sendBeacon instead of synchronous XMLHttpRequest during unload and pagehide improves user experience.`
  - Suggest: `az unload és a pagehide folyamatokban`
  - The comment says do not translate unload or pagehide; “unlode” is not the event name, and Hungarian requires “az” before a vowel-initial word.
- `CSPEvalScriptViolation` — `dom/chrome/security/csp.properties` — The single quotes that are part of the CSP keyword 'unsafe-eval' were replaced by Hungarian quotation marks.
  - Current: `(hiányzó „unsafe-eval”)`
  - Source: `The page’s settings blocked a JavaScript eval (%2$S) from being executed because it violates the following directive: “%1$S” (Missing 'unsafe-eval')`
  - Suggest: `(hiányzó 'unsafe-eval')`
  - The comment says “Don't translate/change "'unsafe-eval'", including the single quote”; the quotes are part of the source-expression syntax the developer must type. Same change in CSPROEvalScriptViolation and the Wasm variants.
- `BlockFileScriptWithWrongMimeType` — `dom/chrome/security/security.properties` — The “file:” scheme is dropped and the quotation mark is placed inside the parenthesis.
  - Current: `Parancsfájl betöltése: az URI „(%1$S”) blokkolva lett`
  - Source: `Loading script from file: URI (“%1$S”) was blocked because its MIME type (“%2$S”) is not a valid JavaScript MIME type.`
  - Suggest: `A file: URI-ról („%1$S”) történő parancsfájl-betöltés blokkolva lett`
  - en-US: “Loading script from file: URI (“%1$S”) was blocked…”, with the note “Do not translate "file: URI"”. The scheme is missing and the quote/paren order is inverted.
- `BlockRedirectToDataURI` — `dom/chrome/security/security.properties` — The “data:” URI scheme was translated into “az adatokhoz:”, although the comment forbids translating it.
  - Current: `Átirányítás az adatokhoz: az URI-hoz navigálás nem engedélyezett`
  - Source: `Redirecting to data: URI not allowed (Blocked loading of: “%1$S”)`
  - Suggest: `Átirányítás a data: URI-ra nem engedélyezett`
  - en-US: “Redirecting to data: URI not allowed”, with the note “Do not translate "data: URI"”. The scheme name is lost and the sentence no longer parses.
- `CookieRejectedNonRequiresSecure2` — `netwerk/necko.properties` — The do-not-localize token SameSite=None is written with a lowercase “none”.
  - Current: `a „SameSite=none” attribútum lett megadva`
  - Source: `Cookie “%1$S” rejected because it has the “SameSite=None” attribute but is missing the “secure” attribute.`
  - Suggest: `a „SameSite=None” attribútum lett megadva`
  - The comment says do not localize “SameSite=None”; CookieSameSiteValueInvalid2 in the same file keeps the capitalised “None”.
- `SaveVideoTitle` — `toolkit/chrome/global/contentAreaCommands.properties` — "Videó" spelled without its accent.
  - Current: `SaveVideoTitle = Video mentése`
  - Source: `Save Video`
  - Suggest: `SaveVideoTitle = Videó mentése`
  - The standalone Hungarian noun is "videó" (cf. "Videó kipattintása" in videocontrols.ftl); the unaccented form only occurs as a compound prefix.
- `url-classifier-content-classifier-col-important` — `toolkit/toolkit/about/url-classifier.ftl` — "Important" is translated although the developer comment forbids translating it.
  - Current: `Fontos`
  - Source: `Important`
  - Suggest: `Important`
  - Developer comment: "'Important' should not be translated as it refers to technical syntax." It names the `important` filter-syntax option, so the localized "Fontos" no longer matches the syntax keyword it labels.
- `autofill-clear-form-label` — `toolkit/toolkit/formautofill/formAutofill.ftl` — Adjective used where an adverb is required.
  - Current: `Automatikus kitöltött űrlap ürítése`
  - Source: `Clear Autofill Form`
  - Suggest: `Automatikusan kitöltött űrlap ürítése`
  - "Automatikus" cannot modify the participle "kitöltött"; the adverbial "automatikusan" is required.
- `wallet-custom-scheme-warning-heading` — `toolkit/toolkit/global/handlerDialog.ftl` — The heading has no verb, so it does not say what the site is being allowed to do.
  - Current: `Engedélyezi az oldal számára a digitális tárcáját?`
  - Source: `heading: Allow this site to open your digital wallet?`
  - Suggest: `Engedélyezi az oldal számára, hogy megnyissa a digitális tárcáját?`
  - en-US: "Allow this site to open your digital wallet?" All sibling permission-dialog strings in this file use the "…számára, hogy megnyissa…" pattern; here the verb is missing and the sentence is ungrammatical.
- `profiledowngrade-nosync` — `toolkit/toolkit/global/profileDowngrade.ftl` — Missing accusative ending on the object of "hozzon létre".
  - Current: `hozzon létre egy új profil a { -brand-short-name } ezen telepítéséhez`
  - Source: `Using an older version of { -brand-product-name } can corrupt bookmarks and browsing history already saved to an existing { -brand-product-name } profile. To protect your information, create a new profile for this insta…`
  - Suggest: `hozzon létre egy új profilt a { -brand-short-name } ezen telepítéséhez`
  - "létrehoz" takes a direct object; "profil" must be "profilt".
- `profiledowngrade-sync` — `toolkit/toolkit/global/profileDowngrade.ftl` — Missing accusative ending on the object of "hozzon létre".
  - Current: `hozzon létre egy új profil a { -brand-short-name } ezen telepítéséhez`
  - Source: `Using an older version of { -brand-product-name } can corrupt bookmarks and browsing history already saved to an existing { -brand-product-name } profile. To protect your information, create a new profile for this insta…`
  - Suggest: `hozzon létre egy új profilt a { -brand-short-name } ezen telepítéséhez`
  - "létrehoz" takes a direct object; "profil" must be "profilt".
- `profiledowngrade-sync2` — `toolkit/toolkit/global/profileDowngrade.ftl` — Missing accusative ending on the object of "hozzon létre".
  - Current: `hozzon létre egy új profil a { -brand-short-name } ezen telepítéséhez`
  - Source: `Using an older version of { -brand-product-name } can corrupt bookmarks and browsing history already saved to an existing { -brand-product-name } profile. To protect your information, create a new profile for this insta…`
  - Suggest: `hozzon létre egy új profilt a { -brand-short-name } ezen telepítéséhez`
  - "létrehoz" takes a direct object; "profil" must be "profilt".
- `rosetta-translated-message` — `toolkit/toolkit/global/rosettaNotification.ftl` — A stray "s" left in the sentence.
  - Current: `A { -brand-short-name } s Rosettával fut`
  - Source: `{ -brand-short-name } is running using Rosetta, which can reduce performance and battery life.`
  - Suggest: `A { -brand-short-name } a Rosettával fut`
  - en-US: "{ -brand-short-name } is running using Rosetta". The isolated "s" is a typo and makes the sentence ungrammatical.
- `region-name-nr` — `toolkit/toolkit/intl/regionNames.ftl` — Country name written in lowercase.
  - Current: `region-name-nr = nauru`
  - Source: `Nauru`
  - Suggest: `region-name-nr = Nauru`
  - Every other region name in the file is capitalized, and Hungarian orthography capitalizes country names.
- `region-name-re` — `toolkit/toolkit/intl/regionNames.ftl` — Réunion is missing its accent.
  - Current: `region-name-re = Reunion`
  - Source: `Réunion`
  - Suggest: `region-name-re = Réunion`
  - en-US is "Réunion"; the Hungarian form also carries the accent, and other entries in the file keep diacritics (Curaçao, Saint Barthélemy).
- `region-name-ss` — `toolkit/toolkit/intl/regionNames.ftl` — "Dél-Szudán" is missing its hyphen.
  - Current: `region-name-ss = Dél Szudán`
  - Source: `South Sudan`
  - Suggest: `region-name-ss = Dél-Szudán`
  - Hungarian spells this compound country name with a hyphen, as the file itself does in "Dél-Afrikai Köztársaság" and "Dél-Korea".
- `region-name-st` — `toolkit/toolkit/intl/regionNames.ftl` — São Tomé és Príncipe is written without any of its diacritics.
  - Current: `region-name-st = Sao Tome és Principe`
  - Source: `São Tomé and Príncipe`
  - Suggest: `region-name-st = São Tomé és Príncipe`
  - en-US: "São Tomé and Príncipe"; other entries in the same file preserve diacritics.
- `sec-error-bad-nickname` — `toolkit/toolkit/neterror/nsserrors.ftl` — The article "A" was typed as the conjunction "Ha", turning the sentence into a dangling conditional.
  - Current: `Ha tanúsítvány neve már használatban van.`
  - Source: `Certificate nickname already in use.`
  - Suggest: `A tanúsítvány neve már használatban van.`
  - en-US: "Certificate nickname already in use." There is no conditional in the source and the clause has no main clause.
- `sec-error-old-krl` — `toolkit/toolkit/neterror/nsserrors.ftl` — Wrong definite article before a consonant and missing comma before "mint".
  - Current: `Az KRL régebbi mint a jelenlegi.`
  - Source: `New KRL is not later than the current one.`
  - Suggest: `Az új KRL nem újabb, mint a jelenlegi.`
  - "KRL" is pronounced with a consonant, so it takes "a", not "az"; Hungarian also requires a comma before "mint". en-US: "New KRL is not later than the current one."
- `ssl-error-bad-cert-status-response-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — Misspelling of "partner".
  - Current: `Az SSL-patner nem kapott OCSP-választ a tanúsítványára.`
  - Source: `SSL peer was unable to get an OCSP response for its certificate.`
  - Suggest: `Az SSL-partner nem kapott OCSP-választ a tanúsítványára.`
  - Every neighbouring string spells it "SSL-partner".
- `ssl-error-internal-error-alert` — `toolkit/toolkit/neterror/nsserrors.ftl` — Verb typo: "jelet" instead of "jelez".
  - Current: `A partner saját belső hibát jelet.`
  - Source: `Peer reports it experienced an internal error.`
  - Suggest: `A partner saját belső hibát jelez.`
  - en-US: "Peer reports it experienced an internal error." "jelet" is the accusative of the noun "jel", leaving the sentence verbless.
- `ssl-error-ssl2-disabled` — `toolkit/toolkit/neterror/nsserrors.ftl` — Subject carries an accusative ending, making the sentence ungrammatical.
  - Current: `A partnert csak az SSL 2-es verzióját támogatja`
  - Source: `Peer only supports SSL version 2, which is locally disabled.`
  - Suggest: `A partner csak az SSL 2-es verzióját támogatja`
  - en-US: "Peer only supports SSL version 2, which is locally disabled." "A partnert" is the object form of the subject.

### D. Terminology, register & consistency

- `aiwindow-applied-memories-list` — `browser/browser/aiWindowContent.ftl` — “Memories” is translated as “Emlékek” here while the rest of the feature uses “Memóriák”.
  - Current: `Emlékek`
  - Source: `aria-label: Memories`
  - Suggest: `Memóriák`
  - Every other Memories string in aiWindow.ftl, aiWindowContent.ftl and aiFeatures.ftl uses “Memóriák”, including the sibling popover label in the same block.
- `confirmation-hint-pin-tab-description` — `browser/browser/confirmationHints.ftl` — “tab” rendered as “fül” although the tree consistently uses “lap”.
  - Current: `kattintson a fülre jobb egérgombbal`
  - Source: `Right-click the tab to unpin it.`
  - Suggest: `kattintson a lapra jobb egérgombbal`
  - Every other tab-related string in this partition uses “lap”; “fül” is an isolated inconsistency in the same UI surface.
- `customkeys-conflict-unusable-title` — `browser/browser/customkeys.ftl` — Keyboard “key” is translated as “kulcs” (cryptographic/lock key) instead of “billentyű”.
  - Current: `A kulcs nem használható`
  - Source: `Key cannot be used`
  - Suggest: `A billentyű nem használható`
  - The whole file is about keyboard shortcuts and elsewhere uses “billentyű” (customkeys-new-key: “Nyomja meg az új billentyűt”); “kulcs” names the wrong object.
- `splitview-onboarding-callout-subtitle-1` — `browser/browser/featureCallout.ftl` — `splitview-onboarding-callout-subtitle-1` quotes “Hozzáadás osztott nézethez” but the string it names, `customkeys-view-add-split-view`, reads “Osztott nézet hozzáadása”
  - Current: `Kattintson jobb gombbal erre a lapra, és válassza a „Hozzáadás osztott nézethez” lehetőséget, hogy egyszerre két lapot lásson.`
  - Source: `Right-click this tab and choose “Add Split View” to see two tabs at once.`
  - Suggest: `Osztott nézet hozzáadása`
  - In the source this string quotes “Add Split View”, which is exactly the value of `customkeys-view-add-split-view` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `menu-application-hide-other` — `browser/browser/menubar.ftl` — “A több elrejtése” is not grammatical; the pronoun for “others” is “a többi”.
  - Current: `A több elrejtése`
  - Source: `label: Hide Others`
  - Suggest: `A többi elrejtése`
  - en-US “Hide Others”. “több” means “more”; the correct pronoun is “többi”.
- `menu-application-touch-bar` — `browser/browser/menubar.ftl` — Typo: “Érintősár” instead of “Érintősáv” (Touch Bar).
  - Current: `Érintősár testreszabása…`
  - Source: `label: Customize Touch Bar…`
  - Suggest: `Érintősáv testreszabása…`
  - “sár” means mud; the intended word is “sáv” (bar).
- `migration-chrome-windows-password-import-step1` — `browser/browser/migrationWizard.ftl` — Wrong definite article before a vowel-initial word.
  - Current: `és ugorjon a Automatikus kitöltés és jelszavak`
  - Source: `Open the main menu <img data-l10n-name="chrome-icon-3dots"/> and go to Passwords and Autofill > Google Password Manager.`
  - Suggest: `és ugorjon az Automatikus kitöltés és jelszavak`
  - “a” must become “az” before a word starting with a vowel.
- `spotlight-peace-mind-body` — `browser/browser/newtab/asrouter.ftl` — Thousands written with a period, which is the decimal separator in Hungarian.
  - Current: `átlagosan 3.000 nyomkövetőt`
  - Source: `Every month, { -brand-short-name } blocks an average of over 3,000 trackers per user. Because nothing, especially privacy nuisances like trackers, should stand between you and the good internet.`
  - Suggest: `átlagosan 3000 nyomkövetőt`
  - Hungarian uses no separator for four-digit numbers (or a space), and the period marks decimals, so "3.000" reads as three; july-jam-body in the same file correctly writes "3000".
- `home-prefs-mission-message-learn-more-link-srd` — `browser/browser/newtab/newtab.ftl` — Missing comma before the subordinate clause.
  - Current: `Tudja meg hogyan`
  - Source: `Find out how`
  - Suggest: `Tudja meg, hogyan`
  - Hungarian requires a comma before a subordinating conjunction; the same file writes "Tudja meg, hogyan működik…" (newtab-privacy-modal-link).
- `newtab-stocks-menu-search` — `browser/browser/newtab/newtab.ftl` — Wrong case ending makes the menu item ungrammatical.
  - Current: `Részvénykódok keresésére`
  - Source: `Search ticker symbols`
  - Suggest: `Részvénykódok keresése`
  - The sublative -re turns the label into a dangling "for the searching of…"; other menu items in the widget use the plain nominal form.
- `newtab-widget-section-feedback` — `browser/browser/newtab/newtab.ftl` — Missing comma before the subordinate clause.
  - Current: `Mondja el nekünk mit gondol`
  - Source: `Tell us what you think`
  - Suggest: `Mondja el nekünk, mit gondol`
  - A comma is obligatory before the embedded question "mit gondol".
- `fx-backup-opt-in-filepath-label` — `browser/browser/newtab/onboarding.ftl` — Wrong vowel-harmony suffix on "OneDrive".
  - Current: `például a OneDrive-re`
  - Source: `Pick a place you plan to transfer to a new device, like OneDrive.`
  - Suggest: `például a OneDrive-ra`
  - "Drive" is pronounced with a back vowel in Hungarian, so it takes -ra; create-backup-screen-1-backup-body in the same file correctly writes "OneDrive-ra".
- `onboarding-genai-sidebar-subtitle` — `browser/browser/newtab/onboarding.ftl` — Ungrammatical, garbled rendering of "draft messages".
  - Current: `írjon összes piszkozatokat`
  - Source: `Summarize web content, brainstorm ideas, draft messages — all as you browse. Choose from multiple providers. Switch anytime. <a data-l10n-name="learn-more">Learn more</a>`
  - Suggest: `írjon üzenetpiszkozatokat`
  - "összes piszkozatokat" is not grammatical Hungarian (mismatched quantifier and plural accusative) and does not convey "draft messages".
- `onboarding-sign-up-description` — `browser/browser/newtab/onboarding.ftl` — Misspelling of "egyebek".
  - Current: `egyeket`
  - Source: `Sign up for an account and all of your important info — passwords, bookmarks, and more — will be securely stored and available when you sign in to any device.`
  - Suggest: `egyebek`
  - "egyeket" is not a word; the intended form in the list "jelszavak, könyvjelzők és egyebek" is "egyebek".
- `managed-bookmarks` — `browser/browser/places.ftl` — Verb stem used instead of the participle: “Menedzsel könyvjelzők”.
  - Current: `Menedzsel könyvjelzők`
  - Source: `label: Managed bookmarks`
  - Suggest: `Felügyelt könyvjelzők`
  - en-US “Managed bookmarks”; “menedzsel” is a finite verb form and cannot modify a noun. A participle (e.g. “felügyelt” / “menedzselt”) is required.
- `policy-DisablePasswordReveal` — `browser/browser/policies/policies-descriptions.ftl` — Misspelling: "mentet" instead of "mentett".
  - Current: `a mentet bejelentkezésekben`
  - Source: `Do not allow passwords to be revealed in saved logins.`
  - Suggest: `a mentett bejelentkezésekben`
  - Past participle of "ment" is "mentett" with a double t; "mentet" is a different (causative) form.
- `policy-EnableTrackingProtection` — `browser/browser/policies/policies-descriptions.ftl` — Misspelling: "válaszható" instead of "választható".
  - Current: `válaszható módon`
  - Source: `Enable or disable Content Blocking and optionally lock it.`
  - Suggest: `választható módon`
  - The word for "optionally" is "választható" (from választ); "válaszható" is a typo, cf. policy-Homepage which spells it correctly.
- `policy-EncryptedMediaExtensions` — `browser/browser/policies/policies-descriptions.ftl` — Misspelling: "válaszható" instead of "választható".
  - Current: `válaszható módon`
  - Source: `Enable or disable Encrypted Media Extensions and optionally lock it.`
  - Suggest: `választható módon`
  - Same typo as in policy-EnableTrackingProtection; policy-Homepage spells it "választható".
- `policy-OverrideFirstRunPage` — `browser/browser/policies/policies-descriptions.ftl` — Duplicated article "a az".
  - Current: `ha le akarja tiltani a az első indítás oldalt`
  - Source: `Override the first run page. Set this policy to blank if you want to disable the first run page.`
  - Suggest: `ha le akarja tiltani az első indítás oldalt`
  - Two stacked definite articles; only "az" belongs before "első".
- `policy-OverridePostUpdatePage` — `browser/browser/policies/policies-descriptions.ftl` — Missing case suffix makes the sentence ungrammatical.
  - Current: `Állítsa üres ezt a házirendet`
  - Source: `Override the post-update “What’s New” page. Set this policy to blank if you want to disable the post-update page.`
  - Suggest: `Állítsa üresre ezt a házirendet`
  - "Állít" requires the sublative -re on the resulting state; cf. the parallel policy-OverrideFirstRunPage which uses "Állítsa üres értékre".
- `fxa-qrcode-pair-step2-signin` — `browser/browser/preferences/fxaPairDevice.ftl` — Wrong definite article before a vowel-initial word.
  - Current: `koppintson a <strong>Adatok szinkronizálása és mentése</strong> elemre`
  - Source: `2. Go to the menu (<img data-l10n-name="ios-menu-icon"/> on iOS or <img data-l10n-name="android-menu-icon"/> on Android) and tap <strong>Sync and save data</strong>`
  - Suggest: `koppintson az <strong>Adatok szinkronizálása és mentése</strong> elemre`
  - "Adatok" begins with a vowel, so the article must be "az".
- `browser-language-heading` — `browser/browser/preferences/preferences.ftl` — Misspelling "menüijeinek".
  - Current: `menüijeinek`
  - Source: `description: Choose the language used to display menus, messages, and notifications from { -brand-short-name }. label: Browser language`
  - Suggest: `menüinek`
  - The possessive plural of "menü" is "menüinek"; "menüijeinek" is not a word.
- `forms-generate-passwords` — `browser/browser/preferences/preferences.ftl` — Garbled coordination: "javaslata az előállítása".
  - Current: `Erős jelszavak javaslata az előállítása`
  - Source: `accesskey: u label: Suggest and generate strong passwords`
  - Suggest: `Erős jelszavak javaslata és előállítása`
  - en-US: "Suggest and generate strong passwords". The conjunction "és" was replaced by the article "az", leaving an ungrammatical string.
- `preferences-data-migration-group` — `browser/browser/preferences/preferences.ftl` — Verb misspelled: "Hozzá át" instead of "Hozza át".
  - Current: `Hozzá át a könyvjelzőit`
  - Source: `description: Bring your bookmarks, passwords, history, extensions, and autofill data from another browser. label: Import browser data`
  - Suggest: `Hozza át a könyvjelzőit`
  - "Hozzá" is not an imperative form; the imperative of "hoz" is "hozza". Visible in the Import browser data group description.
- `preferences-doh-description` — `browser/browser/preferences/preferences.ftl` — "lássak" (1sg) should be "lássák" (3pl).
  - Current: `hogy lássak, hogy melyik weboldalakat éri el`
  - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, creating a secure DNS and making it harder for others to see which website you’re about to access.`
  - Suggest: `hogy lássák, hogy mely weboldalakat éri el`
  - Same conjugation error as in preferences-doh-description2: the subject "mások" requires "lássák".
- `preferences-doh-description2` — `browser/browser/preferences/preferences.ftl` — "lássak" (1sg) should be "lássák" (3pl).
  - Current: `hogy lássak, hogy melyik weboldalakat éri el`
  - Source: `Domain Name System (DNS) over HTTPS sends your request for a domain name through an encrypted connection, providing a secure DNS and making it harder for others to see which website you’re about to access.`
  - Suggest: `hogy lássák, hogy mely weboldalakat éri el`
  - The subject is "mások" (others), so the verb must be third person plural "lássák".
- `privacy-segmentation-section-description` — `browser/browser/preferences/preferences.ftl` — Number agreement: plural subject with singular verb.
  - Current: `amelyek az Ön adatait használja`
  - Source: `When we offer features that use your data to give you a more personal experience:`
  - Suggest: `amelyek az Ön adatait használják`
  - The relative pronoun "amelyek" is plural (referring to "funkciókat"), so the verb must be "használják".
- `search-results-empty-message2` — `browser/browser/preferences/preferences.ftl` — "Elnézését" should be "Elnézést".
  - Current: `Elnézését, nincs találat`
  - Source: `Sorry! There are no results in Settings for “<span data-l10n-name="query"></span>”.`
  - Suggest: `Elnézést, nincs találat`
  - The fixed apologetic phrase is "Elnézést"; "Elnézését" (a possessive accusative) is ungrammatical here.
- `security-privacy-status-update-needed-description` — `browser/browser/preferences/preferences.ftl` — Typo "sebességbelii".
  - Current: `sebességbelii`
  - Source: `Update for the latest speed, stability, and security updates.`
  - Suggest: `sebességbeli`
  - Doubled final "i"; the correct adjective is "sebességbeli".
- `settings-tabs-show-image-in-preview` — `browser/browser/preferences/preferences.ftl` — "fülé" should be "fölé" (over/above).
  - Current: `ha az egérmutatót egy lap fülé húzza`
  - Source: `accessKey: h label: Show an image preview when you hover on a tab`
  - Suggest: `ha az egérmutatót egy lap fölé húzza`
  - en-US: "when you hover on a tab". "fülé" means "to his/her ear"; the postposition meaning "over" is "fölé".
- `sitedata-delete-on-close-private-browsing4` — `browser/browser/preferences/preferences.ftl` — Wrong definite article "az" before a consonant-initial word.
  - Current: `törli a sütiket és az webhelyadatokat`
  - Source: `heading: History won’t be saved. message: { -brand-short-name } clears cookies and site data from your session when you close the browser.`
  - Suggest: `törli a sütiket és a webhelyadatokat`
  - "webhelyadatokat" starts with a consonant, so the article must be "a", not "az".
- `update-setting-write-failure-message2` — `browser/browser/preferences/preferences.ftl` — "szükségesen" should be the predicate "szükséges".
  - Current: `írási engedély szükségesen a lenti fájlon`
  - Source: `{ -brand-short-name } encountered an error and didn’t save this change. Note that changing this update setting requires permission to write to the file below. You or a system administrator may be able to resolve the err…`
  - Suggest: `írási engedély szükséges a lenti fájlra`
  - en-US: "requires permission to write to the file below". "szükségesen" is an adverb and makes the clause ungrammatical.
- `site-data-settings-description` — `browser/browser/preferences/siteDataSettings.ftl` — Missing accusative ending on "oldaladatok".
  - Current: `tárolnak sütiket és oldaladatok a számítógépén`
  - Source: `The following websites store cookies and site data on your computer. { -brand-short-name } keeps data from websites with persistent storage until you delete it, and deletes data from websites with non-persistent storage…`
  - Suggest: `tárolnak sütiket és oldaladatokat a számítógépén`
  - The object of "tárolnak" must be accusative: "oldaladatokat", matching the preceding "sütiket".
- `preonboarding-manage-and-read-header` — `browser/browser/preonboarding.ftl` — Case mismatch between the two coordinated objects of “elolvasása”.
  - Current: `a felhasználási feltételeinket és az adatvédelmi nyilatkozat elolvasása`
  - Source: `Manage data collection settings and read our Terms of Use and Privacy Notice`
  - Suggest: `a felhasználási feltételeink és az adatvédelmi nyilatkozat elolvasása`
  - With the possessive noun phrase “… elolvasása”, both coordinated members must be nominative; “feltételeinket” is accusative and does not agree with “nyilatkozat”.
- `preonboarding-privacy-notice-header-button-title` — `browser/browser/preonboarding.ftl` — “felolvasása” means “reading aloud”, not “reading”.
  - Current: `Adatvédelmi nyilatkozat felolvasása`
  - Source: `Read our Privacy Notice`
  - Suggest: `Adatvédelmi nyilatkozat elolvasása`
  - en-US “Read our Privacy Notice”; the parallel button preonboarding-terms-of-use-header-button-title correctly uses “elolvasása”.
- `fingerprinter-tab-content` — `browser/browser/protections.ftl` — Wrong definite article (“A” before a vowel) and missing accusative on “Ön”.
  - Current: `A ujjlenyomat-készítők beállításokat gyűjtenek a böngészőjéből és számítógépéből, hogy profilt hozzanak létre Önről. A digitális ujjlenyomat használatával követhetik Ön a különböző webhelyek között.`
  - Source: `Fingerprinters collect settings from your browser and computer to create a profile of you. Using this digital fingerprint, they can track you across different websites. <a data-l10n-name="learn-more-link">Learn more</a>`
  - Suggest: `Az ujjlenyomat-készítők beállításokat gyűjtenek a böngészőjéből és számítógépéből, hogy profilt hozzanak létre Önről. A digitális ujjlenyomat használatával követhetik Önt a különböző webhelyek között.`
  - “A” must be “az” before a vowel-initial word, and the object of “követhetik” requires the accusative “Önt”.
- `graph-week-summary-private-window` — `browser/browser/protections.ftl` — Relative pronoun does not agree in number with the plural antecedent.
  - Current: `Követők, melyet a { -brand-short-name } blokkolt a héten`
  - Source: `Trackers { -brand-short-name } blocked this week`
  - Suggest: `Követők, amelyeket a { -brand-short-name } blokkolt a héten`
  - “Követők” is plural, so the accusative relative pronoun must be “amelyeket/melyeket”.
- `monitor-partial-breaches-motivation-description` — `browser/browser/protections.ftl` — Sentence ends with a bare brand term missing its case suffix, so it is ungrammatical.
  - Current: `Oldja meg a többi adatvédelmi incidenst a { -monitor-brand-short-name }.`
  - Source: `Resolve the rest of your breaches on { -monitor-brand-short-name }.`
  - Suggest: `Oldja meg a többi adatvédelmi incidenst a { -monitor-brand-short-name }on.`
  - en-US “Resolve the rest of your breaches on { -monitor-brand-short-name }.”; every other string in this file attaches “on” to the brand term (e.g. monitor-resolve-breaches-link tooltip).
- `protections-panel-cross-site-tracking-cookies` — `browser/browser/protectionsPanel.ftl` — Missing accusative: “követik Ön” instead of “követik Önt”.
  - Current: `Ezek a sütik követik Ön oldalról oldalra`
  - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies.`
  - Suggest: `Ezek a sütik követik Önt oldalról oldalra`
  - The direct object of “követik” must be in the accusative.
- `protections-panel-fingerprinters` — `browser/browser/protectionsPanel.ftl` — Wrong definite article (“A” before a vowel) and missing accusative on “Ön”.
  - Current: `A ujjlenyomat-készítők beállításokat gyűjtenek a böngészőjéből és számítógépéből, hogy profilt hozzanak létre Önről. A digitális ujjlenyomat használatával követhetik Ön a különböző webhelyek között.`
  - Source: `Fingerprinters collect settings from your browser and computer to create a profile of you. Using this digital fingerprint, they can track you across different websites.`
  - Suggest: `Az ujjlenyomat-készítők beállításokat gyűjtenek a böngészőjéből és számítógépéből, hogy profilt hozzanak létre Önről. A digitális ujjlenyomat használatával követhetik Önt a különböző webhelyek között.`
  - Same two errors as in protections.ftl: “az” is required before a vowel, and “követhetik” takes the accusative “Önt”.
- `report-broken-site-panel-description2` — `browser/browser/reportBrokenSite.ftl` — Indefinite conjugation used with a definite object: “Adjon meg a lépéseket”.
  - Current: `Adjon meg a lépéseket a probléma reprodukálásához.`
  - Source: `placeholder: What happened? What did you expect to happen? Please provide steps to reproduce the issue.`
  - Suggest: `Adja meg a lépéseket a probléma reprodukálásához.`
  - “a lépéseket” is a definite object, so the verb must take the definite conjugation “adja meg”.
- `safeb-blocked-harmful-page-error-desc-no-override` — `browser/browser/safebrowsing/blockedSite.ftl` — Missing accusative ending (and missing space) before the link: “oldal” should be “oldalt”.
  - Current: `oldal<a data-l10n-name='error_desc_link'>ártalmas szoftvert tartalmazóként jelentették</a>`
  - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing a potentially harmful application</a>.`
  - Suggest: `oldalt <a data-l10n-name='error_desc_link'>ártalmas szoftvert tartalmazóként jelentették</a>`
  - Same defect as the -override variant: “jelentették” requires the accusative “oldalt”, and the noun is glued to the opening link tag.
- `safeb-blocked-harmful-page-error-desc-override` — `browser/browser/safebrowsing/blockedSite.ftl` — Missing accusative ending (and missing space) before the link: “oldal” should be “oldalt”.
  - Current: `oldal<a data-l10n-name='error_desc_link'>ártalmas szoftvert tartalmazóként jelentették</a>`
  - Source: `<span data-l10n-name='sitename'>{ $sitename }</span> has been <a data-l10n-name='error_desc_link'>reported as containing a potentially harmful application</a>. You can <a data-l10n-name='ignore_warning_link'>ignore the…`
  - Suggest: `oldalt <a data-l10n-name='error_desc_link'>ártalmas szoftvert tartalmazóként jelentették</a>`
  - “jelentették” takes an accusative object, so it must be “oldalt”, as in the parallel phishing strings (“A(z) … oldalt … megtévesztő oldalként jelentették”). The word also runs into the link with no space.
- `screenshots-private-window-error-title` — `browser/browser/screenshots.ftl` — Plural verb with a singular brand-name subject.
  - Current: `A { -screenshots-brand-name } le vannak tiltva Privát böngészésben`
  - Source: `{ -screenshots-brand-name } is disabled in Private Browsing Mode`
  - Suggest: `A { -screenshots-brand-name } le van tiltva a privát böngészésben`
  - en-US “{ -screenshots-brand-name } is disabled…”; the brand term is singular, so “vannak” does not agree.
- `protections-not-blocking-fingerprinters` — `browser/browser/siteProtections.ftl` — Compound misspelled with a plural first member: “ujjlenyomatok-készítőket”.
  - Current: `Nem blokkolja az ujjlenyomatok-készítőket`
  - Source: `title: Not Blocking Fingerprinters`
  - Suggest: `Nem blokkolja az ujjlenyomat-készítőket`
  - Everywhere else in this file and in protections.ftl the term is “ujjlenyomat-készítő”; the first element of the compound must be singular.
- `tab-groups-list-empty-description` — `browser/browser/tabbrowser.ftl` — Missing accusative ending on the object of “Húzzon”.
  - Current: `Húzzon egy lap egy másikra`
  - Source: `Drag one tab onto another or right-click a tab to start organizing. We’ll save your groups here so they’re easy to find later.`
  - Suggest: `Húzzon egy lapot egy másikra`
  - en-US “Drag one tab onto another”; the object requires the accusative “lapot”.
- `existing-user-tou-message` — `browser/browser/termsofuse.ftl` — Object of “frissítettük” is left in the nominative instead of the accusative.
  - Current: `frissítettük az <a data-l10n-name="privacy-notice-link">Adatvédelmi nyilatkozat</a>`
  - Source: `<strong>Update</strong> We’ve introduced a { -brand-short-name } <a data-l10n-name="terms-of-use-link">Terms of Use</a> and updated our <a data-l10n-name="privacy-notice-link">Privacy Notice</a>. Please take a moment to…`
  - Suggest: `frissítettük az <a data-l10n-name="privacy-notice-link">Adatvédelmi nyilatkozatot</a>`
  - The sibling string existing-user-privacy-notice-update-message correctly uses the accusative “Adatvédelmi nyilatkozatot”.
- `protections.notBlocking.fingerprinters.title` — `browser/chrome/browser/browser.properties` — Misspelled compound: “ujjlenyomatok-készítőket” instead of “ujjlenyomat-készítőket”.
  - Current: `Nem blokkolja az ujjlenyomatok-készítőket`
  - Source: `Not Blocking Fingerprinters`
  - Suggest: `Nem blokkolja az ujjlenyomat-készítőket`
  - The term is consistently “ujjlenyomat-készítők” elsewhere in the same file (protections.blocking.fingerprinters.title, trackingProtection.icon.activeTooltip2); the plural first member is not valid in this compound.
- `unblockInsecure2` — `browser/chrome/browser/downloads/downloads.properties` — Case-agreement error: accusative subject with a passive predicate.
  - Current: `annak ellenére, hogy az aktuális dokumentumot biztonságos HTTPS-kapcsolaton keresztül lett kézbesítve`
  - Source: `The download is offered over HTTP even though the current document was delivered over a secure HTTPS connection. If you proceed, the download may be corrupted or tampered with during the download process.`
  - Suggest: `annak ellenére, hogy az aktuális dokumentum biztonságos HTTPS-kapcsolaton keresztül lett kézbesítve`
  - “az aktuális dokumentumot” is accusative but “lett kézbesítve” requires a nominative subject; the clause is ungrammatical.
- `CONTEXT_OPTIONS` — `browser/installer/custom.properties` — "Options" rendered as a verbal noun "setting it up" instead of the settings noun.
  - Current: `$BrandShortName &beállítása`
  - Source: `$BrandShortName &Options`
  - Suggest: `$BrandShortName &beállításai`
  - This is a shortcut context-menu entry naming the Options/Settings screen; "beállítása" reads as the act of configuring it, while the UI item is "beállításai".
- `accessibility-text-label-issue-dialog` — `devtools/client/accessibility.ftl` — Spelling error: "párbeszablakokat" instead of "párbeszédablakokat".
  - Current: `A párbeszablakokat címkézni kell.`
  - Source: `Dialogs should be labeled. <a>Learn more</a>`
  - Suggest: `A párbeszédablakokat címkézni kell.`
  - The same message in devtools/shared/accessibility.properties (accessibility.text.label.issue.dialog) is spelled "párbeszédablakokat".
- `accessibility.enable.disabledTitle` — `devtools/client/accessibility.properties` — Truncated word: "akadálymentesít szolgáltatások" is missing its ending.
  - Current: `az akadálymentesít szolgáltatások adatvédelmi beállításán keresztül`
  - Source: `Accessibility service can not be turned on. It is turned off via accessibility services privacy preference.`
  - Suggest: `az akadálymentesítési szolgáltatások adatvédelmi beállításán keresztül`
  - "akadálymentesít" is a verb form; the noun modifier used consistently elsewhere in this file is "akadálymentesítési".
- `timeline.pausedButtonTooltip` — `devtools/client/animationinspector.properties` — Missing space between the two words: "Animációkfolytatása".
  - Current: `timeline.pausedButtonTooltip = Animációkfolytatása`
  - Source: `Resume the animations`
  - Suggest: `timeline.pausedButtonTooltip = Animációk folytatása`
  - Two words are run together; the parallel strings (timeline.resumedButtonTooltip, timeline.rewindButtonTooltip) are correctly spaced.
- `noDomMutationBreakpoints` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints` quotes “Töréspont…” but the string it names, `watchpoints.submenu`, reads “Szüneteltetés…”
  - Current: `Kattintson a jobb gombbal egy elemre itt: %S, és válassza a „Töréspont…” lehetőséget`
  - Source: `Right click an element in the %S and select “Break on…” to add a breakpoint`
  - Suggest: `Szüneteltetés…`
  - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `noDomMutationBreakpoints.notice` — `devtools/client/debugger.properties` — `noDomMutationBreakpoints.notice` quotes “Töréspont…” but the string it names, `watchpoints.submenu`, reads “Szüneteltetés…”
  - Current: `Kattintson a jobb gombbal egy elemre a Vizsgálóban, és válassza a „Töréspont…” lehetőséget`
  - Source: `Right click an element in the Inspector and select “Break on…” to add a breakpoint`
  - Suggest: `Szüneteltetés…`
  - In the source this string quotes “Break on…”, which is exactly the value of `watchpoints.submenu` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `emptyPresetList` — `devtools/client/filterwidget.properties` — Typo: "előbeállítáokat" is missing an "s".
  - Current: `Tárolhat szűrő-előbeállítáokat`
  - Source: `You don’t have any saved presets. You can store filter presets by choosing a name and saving them. Presets are quickly accessible and you can reuse them with ease.`
  - Suggest: `Tárolhat szűrő-előbeállításokat`
  - The correct accusative plural is "előbeállításokat", as used in presetsToggleButton/newPresetPlaceholder.
- `markupView.scrollableBadge.interactive.tooltip` — `devtools/client/inspector.properties` — Case agreement error: "azokat az elemek" instead of "azokat az elemeket".
  - Current: `hogy felfedje azokat az elemek, melyek a túlcsordulást okozzák`
  - Source: `This element has scrollable overflow. Click to reveal elements that are causing the overflow.`
  - Suggest: `hogy felfedje azokat az elemeket, amelyek a túlcsordulást okozzák`
  - The object of "felfedje" must be accusative; the demonstrative is accusative but the noun is not.
- `responsive.reloadConditions.userAgent` — `devtools/client/responsive.properties` — Missing adjectival suffix: "felhasználó ügynök" instead of "felhasználói ügynök".
  - Current: `responsive.reloadConditions.userAgent = Újratöltés, ha a felhasználó ügynök megváltozik`
  - Source: `Reload when user agent is changed`
  - Suggest: `responsive.reloadConditions.userAgent = Újratöltés, ha a felhasználói ügynök megváltozik`
  - The rest of the file uses "felhasználói ügynök" (responsive.customUserAgent, responsive.userAgentList); "felhasználó ügynök" is ungrammatical.
- `inactive-css-border-image` — `devtools/client/tooltips.ftl` — The sentence ends with a dangling, uninflected "szülő táblázatelem", losing the "on the parent table element" relation.
  - Current: `<strong>collapse</strong> értékre van állítva szülő táblázatelem.`
  - Source: `<strong>{ $property }</strong> has no effect on this element since it cannot be applied to internal table elements where <strong>border-collapse</strong> is set to <strong>collapse</strong> on the parent table element.`
  - Suggest: `<strong>collapse</strong> értékre van állítva a szülő táblázatelemen.`
  - en-US: "…where border-collapse is set to collapse on the parent table element"; the Hungarian leaves the noun phrase unattached and unmarked.
- `inactive-text-overflow-when-no-overflow` — `devtools/client/tooltips.ftl` — Ungrammatical clause: "mivel nem megadva az overflow:hidden".
  - Current: `mivel nem megadva az <strong>overflow:hidden</strong>`
  - Source: `<strong>{ $property }</strong> has no effect on this element since <strong>overflow:hidden</strong> is not set.`
  - Suggest: `mivel nincs megadva az <strong>overflow:hidden</strong>`
  - "nem megadva" is not a valid predicate here; the negated existential form is "nincs megadva".
- _…and 23 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `about-logins-intro-import2` — `browser/browser/aboutLogins.ftl` — A stray message identifier is concatenated to the end of the translated string and will be displayed to users.
  - Current: `egy fájlból</a>create-new-login-button =`
  - Source: `If your logins are saved outside of { -brand-product-name }, you can <a data-l10n-name="import-browser-link">import them from another browser</a> or <a data-l10n-name="import-file-link">from a file</a>`
  - Suggest: `egy fájlból</a>`
  - The text `create-new-login-button =` is leftover editing debris pasted into the value; the en-US string ends after the link.
- `newtab-sports-widget-message-wallpapers-semifinals-body` — `browser/browser/newtab/newtab.ftl` — Informal second-person imperative in a file that consistently uses the formal address.
  - Current: `Készítsd elő a színteret a világbajnokság legnagyobb mérkőzéseire!`
  - Source: `Set the stage for the World Cup’s biggest matches.`
  - Suggest: `Készítse elő a színteret a világbajnokság legnagyobb mérkőzéseire.`
  - Every other imperative in this file uses the formal Ön form (e.g. "Válassza", "Kövesse", "Vigyen"); "Készítsd" is the informal te form.
- `fonts-langgroup-latin` — `browser/browser/preferences/fonts.ftl` — Script name lowercased while every other entry in the list is capitalized.
  - Current: `latin`
  - Source: `label: Latin`
  - Suggest: `Latin`
  - All sibling labels in the same dropdown (Arab, Örmény, Cirill, Görög…) start with a capital letter; only this one does not.
- `permissions-site-local-network-window` — `browser/browser/preferences/permissions.ftl` — Missing space after the en dash in the window title.
  - Current: `Beállítások –Helyi hálózati eszközök`
  - Source: `style: { permissions-window2.style } title: Settings - Local Network Devices`
  - Suggest: `Beállítások – Helyi hálózati eszközök`
  - Every other title in this file uses "Beállítások – X" with spaces on both sides of the dash.
- `privacy-segmentation-radio-off` — `browser/browser/preferences/preferences.ftl` — Missing space between the article and the brand placeholder.
  - Current: `A{ -brand-product-name } javaslatainak használata`
  - Source: `label: Use { -brand-product-name } recommendations`
  - Suggest: `A { -brand-product-name } javaslatainak használata`
  - Renders as "AFirefox javaslatainak használata"; every other string in the file separates the article from the term with a space.
- `keywordURIFixup.goTo` — `browser/chrome/browser/browser.properties` — Informal second-person address in a UI button, breaking the locale's formal register.
  - Current: `Igen, vigyél ide: %S`
  - Source: `Yes, take me to %S`
  - Suggest: `Igen, vigyen ide: %S`
  - Everything else in this file and the tree addresses the user formally (Ön / “Engedélyezi…”, “Válasszon…”). “vigyél” is the informal imperative addressed to the browser/user in tegező form, inconsistent with the established formal address.
- `Strings.InfoText` — `browser/updater/updater.ini` — `Strings.InfoText` uses three dots where this locale uses …
  - Current: `A %MOZ_APP_DISPLAYNAME% telepíti a frissítéseket, és pár pillanat múlva elindul...`
  - Source: `%MOZ_APP_DISPLAYNAME% is installing your updates and will start in a few moments…`
  - The tree uses … 459 times against 7 ASCII runs.
- `heading` — `dom/chrome/accessibility/AccessFu.properties` — “heading” is translated as “fejléc”, the same word used for “header”, collapsing two distinct roles.
  - Current: `heading = fejléc`
  - Source: `heading`
  - Suggest: `heading = címsor`
  - The same file already has “header = fejléc”, and dom/chrome/accessibility/mac/accessible.properties translates the ARIA heading role as “címsor”; a screen reader would announce headers and headings identically.
- `GTK2Conflict2` — `dom/chrome/dom/dom.properties` — `GTK2Conflict2` uses straight double quotes
  - Current: `A billentyűesemény nem érhető el GTK2 alatt: key="%S" modifiers="%S" id="%S"`
  - Source: `Key event not available on GTK2: key=“%S” modifiers=“%S” id=“%S”`
  - The locale's quote convention is `polish-double` (874 occurrences).
- `WinConflict2` — `dom/chrome/dom/dom.properties` — `WinConflict2` uses straight double quotes
  - Current: `A billentyűesemény nem érhető el egyes billentyűzetkiosztások esetén: key="%S" modifiers="%S" id="%S"`
  - Source: `Key event not available on some keyboard layouts: key=“%S” modifiers=“%S” id=“%S”`
  - The locale's quote convention is `polish-double` (874 occurrences).
- `TooLargeDashedRadius` — `dom/chrome/layout/css.properties` — `TooLargeDashedRadius` uses straight double quotes
  - Current: `A szegélysugár túl nagy a "dashed" stílushoz (a korlát 100000px). Megjelenítés tömörként.`
  - Source: `Border radius is too large for ‘dashed’ style (the limit is 100000px). Rendering as solid.`
  - The locale's quote convention is `polish-double` (874 occurrences).
- `TooLargeDottedRadius` — `dom/chrome/layout/css.properties` — `TooLargeDottedRadius` uses straight double quotes
  - Current: `A szegélysugár túl nagy a "dotted" stílushoz (a korlát 100000px). Megjelenítés tömörként.`
  - Source: `Border radius is too large for ‘dotted’ style (the limit is 100000px). Rendering as solid.`
  - The locale's quote convention is `polish-double` (874 occurrences).
- `crashreporter-button-details` — `toolkit/crashreporter/crashreporter.ftl` — `crashreporter-button-details` uses three dots where this locale uses …
  - Current: `Részletek...`
  - Source: `Details…`
  - The tree uses … 459 times against 7 ASCII runs.
- `crashreporter-resubmit-status` — `toolkit/crashreporter/crashreporter.ftl` — `crashreporter-resubmit-status` uses three dots where this locale uses …
  - Current: `A korábban sikertelenül elküldött bejelentések újraküldése...`
  - Source: `Resending reports that previously failed to send…`
  - The tree uses … 459 times against 7 ASCII runs.
- `crashreporter-submit-in-progress` — `toolkit/crashreporter/crashreporter.ftl` — `crashreporter-submit-in-progress` uses three dots where this locale uses …
  - Current: `Bejelentés elküldése...`
  - Source: `Submitting your report…`
  - The tree uses … 459 times against 7 ASCII runs.
- `Strings.Details` — `toolkit/crashreporter/crashreporter.ini` — `Strings.Details` uses three dots where this locale uses …
  - Current: `Részletek...`
  - Source: `Details…`
  - The tree uses … 459 times against 7 ASCII runs.
- `Strings.ReportDuringSubmit2` — `toolkit/crashreporter/crashreporter.ini` — `Strings.ReportDuringSubmit2` uses three dots where this locale uses …
  - Current: `Bejelentés elküldése...`
  - Source: `Submitting your report…`
  - The tree uses … 459 times against 7 ASCII runs.
- `Strings.ReportResubmit` — `toolkit/crashreporter/crashreporter.ini` — `Strings.ReportResubmit` uses three dots where this locale uses …
  - Current: `A korábban sikertelenül elküldött bejelentések újraküldése...`
  - Source: `Resending reports that previously failed to send…`
  - The tree uses … 459 times against 7 ASCII runs.
- `about-webrtc-consecutive-frames` — `toolkit/toolkit/about/aboutWebrtc.ftl` — Video "frames" rendered as "keretek" (borders) instead of "képkockák" used elsewhere in the file.
  - Current: `Egymást követő keretek`
  - Source: `Consecutive Frames`
  - Suggest: `Egymást követő képkockák`
  - This is in the video frame statistics block, where the same file consistently uses "képkocka" (about-webrtc-dropped-frames-label, about-webrtc-frames, about-webrtc-first-frame-timestamp). "keret" means a frame/border, not a video frame.
- `abuse-report-learnmore` — `toolkit/toolkit/about/abuseReports.ftl` — "extensions" rendered as "bővítmények" (the locale's word for plugins) instead of "kiegészítők".
  - Current: `További információk a bővítmények és témák jelentéséről`
  - Source: `Unsure what issue to select? <a data-l10n-name="learnmore-link">Learn more about reporting extensions and themes</a>`
  - Suggest: `További információk a kiegészítők és témák jelentéséről`
  - Throughout this file and the surrounding about:addons surface "extension" is "kiegészítő" (abuse-report-title-extension, abuse-report-messagebar-removed-extension), while "bővítmény" is reserved for plugins (aboutPlugins.ftl, addon-category-plugin). Using it here points the user at the wrong add-on type.
- `neterror-dns-not-found-offline-hint-reconnect` — `toolkit/toolkit/neterror/netError.ftl` — "Wi-Fi" written with an en dash instead of a hyphen.
  - Current: `kapcsolódjon újra a Wi–Fi-hez`
  - Source: `Disconnect and reconnect to Wi-Fi.`
  - Suggest: `kapcsolódjon újra a Wi-Fi-hez`
  - fp-neterror-offline-what-can-you-do-body in the same file writes "Wi-Fi" with a plain hyphen, as does the en-US source.
- `backgroundupdate-task-description` — `toolkit/toolkit/updates/backgroundupdate.ftl` — Stray space before a comma.
  - Current: `frissítéseit , ha`
  - Source: `The Background Update task checks for updates to { -brand-short-name } when { -brand-short-name } is not running. This task is installed automatically by { -brand-short-name }, and is reinstalled when { -brand-short-nam…`
  - Suggest: `frissítéseit, ha`
  - A space must not precede a comma in Hungarian; the en-US source has no such gap.

---

## 4. Appendix

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Resolved to date (0)

_Nothing resolved yet._

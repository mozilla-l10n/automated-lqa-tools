# Firefox l10n QA — fi

| | |
|---|---|
| **Generated** | 2026-10-19 |
| **Locale tree** | `https://github.com/mozilla-l10n/firefox-l10n` @ `ba8eba5819d0` |
| **en-US reference** | `https://github.com/mozilla-l10n/firefox-l10n-source` @ `2d5e7eb1f225` |
| **Previous run** | 2026-10-16 @ `db2cfca9d18c` |
| **Mode** | incremental |
| **Strings reviewed this run** | 78 of 16,036 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.


Also for fi: [android](android.md) · [firefox_ios](firefox_ios.md)

---

## Changes in this run

### 🆕 New findings (1)

- `migration-no-permissions-instructions-step2-2` — `browser/browser/migrationWizard.ftl` — The macOS variant uses straight double quotes but the other variant of the same message uses curly quotes.
    - Current: `"Avaa"`
    - Source: `{$sel_1 ->} [macos] In the file picker, choose “Open” [other] In the file picker, navigate to <code>{ $permissionsPath }</code> and choose “Select”`
    - Suggest: `“Avaa”`
    - The en-US uses curly quotes in both variants, and so does the Finnish 'other' variant (“Valitse”). The macOS variant switches to straight quotes, so the two variants of one message don't match.

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
| Strings | 16,036 |
| Missing strings | 484 |
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
| Access keys not in their label | 4 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 9 |

### Completeness

**484 strings** are not translated yet, concentrated in:

- `dom/chrome/dom/dom.properties` — 71
- `toolkit/toolkit/about/aboutGlean.ftl` — 62
- `browser/browser/ipProtection.ftl` — 41
- `toolkit/toolkit/about/aboutLogging.ftl` — 40
- `dom/chrome/security/csp.properties` — 34
- `dom/chrome/security/security.properties` — 28
- `toolkit/toolkit/about/aboutWebauthn.ftl` — 22
- `toolkit/toolkit/about/url-classifier.ftl` — 21
- `toolkit/toolkit/about/aboutProcesses.ftl` — 17
- `browser/browser/newtab/newtab.ftl` — 16
- `toolkit/toolkit/about/aboutSupport.ftl` — 15
- `browser/browser/aboutPrivateBrowsing.ftl` — 13

**Files present but identical to en-US:**

- `devtools/client/aboutdebugging.ftl`
- `devtools/client/accessibility.ftl`
- `devtools/client/accessibility.properties`
- `devtools/client/animationinspector.properties`
- `devtools/client/boxmodel.properties`
- `devtools/client/changes.properties`
- `devtools/client/compatibility.ftl`
- `devtools/client/components.properties`
- `devtools/client/device.properties`
- `devtools/client/inspector.ftl`
- `devtools/client/jsonview.properties`
- `devtools/client/layout.properties`
- `devtools/client/memory.properties`
- `devtools/client/perftools.ftl`
- `devtools/client/responsive.properties`
- `devtools/client/shared.properties`
- `devtools/client/sourceeditor.properties`
- `devtools/client/startup.properties`
- `devtools/client/tooltips.ftl`
- `devtools/shared/debugger.properties`

_Completeness is reported, never raised as a finding: a missing string needs translating, not fixing._

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 309, `straight-double` 116, `curly-single` 70 | _mixed_ |
| apostrophe | `typographic` 148, `straight` 33 | **typographic** |
| ellipsis | `char` 399, `ascii` 1 | **char** |
| dash | `em` 42, `en` 29 | _mixed_ |
| nbsp | `total` 11, `before-punctuation` 3, `space-before-punctuation` 6 | _mixed_ |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (155)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 108 |
| 2 | Wrong content (says something other than the English) | 37 |
| 3 | Degraded language (grammar, spelling, terminology) | 0 |
| 4 | Cosmetic (typography, spacing) | 10 |

### A. Functional, markup, variables & plurals

- `xpinstall-prompt-never-allow-and-report` — `browser/browser/addonNotifications.ftl` — Access key `R` of `xpinstall-prompt-never-allow-and-report` is not present in its label
    - Current: `R`
    - Source: `accesskey: R label: Report Suspicious Site`
    - The label is “Ilmoita epäilyttävästä sivustosta”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `firefox-relay-opt-in-confirmation-enable-button` — `browser/browser/firefoxRelay.ftl` — Access key `U` of `firefox-relay-opt-in-confirmation-enable-button` is not present in its label
    - Current: `U`
    - Source: `accesskey: U label: Use email mask`
    - The label is “Käytä sähköpostimaskia”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `link-preview-optin-title` — `browser/browser/genai.ftl` — "See more with AI?" rendered as "More eyesight with AI?"
    - Current: `Enemmän näköä tekoälyn avulla?`
    - Source: `See more with AI?`
    - Suggest: `Näe enemmän tekoälyn avulla?`
    - "näkö" means eyesight; "enemmän näköä" does not convey the source's "see more" (get more information) and reads as a different claim about vision.
- `set-default-menu-message-row-layout-title` — `browser/browser/newtab/asrouter.ftl` — "primary browser" rendered as "oletusselaimeksi" (default browser), making it identical to the -variant string.
    - Current: `set-default-menu-message-row-layout-title = Aseta { -brand-short-name } oletusselaimeksi`
    - Source: `Make { -brand-short-name } your primary browser`
    - Suggest: `Aseta { -brand-short-name } ensisijaiseksi selaimeksi`
    - The en-US pair deliberately contrasts "primary browser" and "default browser" as A/B variants; both Finnish strings now read the same. The file elsewhere renders "primary" as "ensisijainen" (set-default-menu-message-primary-button-variant).
- `newtab-sports-widget-follow-teams-title` — `browser/browser/newtab/newtab.ftl` — "Follow up to { $number } teams" rendered as "Follow { $number } teams" — the "up to" limit is dropped.
    - Current: `Seuraa { $number } joukkuetta`
    - Source: `{$number ->} [other] Follow up to { $number } teams`
    - Suggest: `Seuraa enintään { $number } joukkuetta`
    - The source states a maximum the user may pick; the Finnish reads as an instruction to follow exactly that many teams.
- `onboarding-refresh-gratitude-subtitle` — `browser/browser/newtab/onboarding.ftl` — "the only major browser backed by a non-profit" is rendered as "the only browser backed by a non-profit" — the qualifier "major" is dropped, making the exclusivity claim absolute.
    - Current: `ainoaa selainta, jota tukee voittoa tavoittelematon järjestö`
    - Source: `Thank you for using { -brand-short-name }, the only major browser backed by a non-profit. With your support, we’re working to make the internet safer and more accessible for everyone.`
    - Suggest: `ainoaa merkittävää selainta, jota tukee voittoa tavoittelematon järjestö`
    - Without "merkittävä", the product claims to be the only non-profit-backed browser at all, which the en-US does not say. The sibling string onboarding-refresh-tou-pin-unchecked in the same file does keep "merkittävä".
- `connection-proxy-option-auto` — `browser/browser/preferences/connection.ftl` — “Auto-detect proxy settings for this network” rendered as generic “Automatic proxy settings”.
    - Current: `Automaattiset välityspalvelinasetukset`
    - Source: `accesskey: w label: Auto-detect proxy settings for this network`
    - Suggest: `Tunnista tämän verkon välityspalvelinasetukset automaattisesti`
    - The option is specifically auto-detection for the current network; the Finnish label states only “automatic proxy settings”, which overlaps with the separate automatic-configuration-URL option and loses the network scoping.
- `autofill-address-parish` — `browser/browser/preferences/formAutofill.ftl` — “Parish” (administrative division in Barbados/Jamaica) rendered as “church village”.
    - Current: `Kirkonkylä`
    - Source: `Parish`
    - Suggest: `Kirkkopitäjä`
    - The developer comment states this is primary address information one level below the country for BB and JM, i.e. an administrative division. “Kirkonkylä” means the village centre around a church, not an administrative region.
- `autofill-address-village-township` — `browser/browser/preferences/formAutofill.ftl` — “Township” rendered as “kaupunki” (city), colliding with the City field label.
    - Current: `Kylä tai kaupunki`
    - Source: `Village or Township`
    - Suggest: `Kylä tai kunta`
    - The comment marks this as a sublocality below a locality in Malaysia; translating “Township” as “kaupunki” both misnames the unit and duplicates autofill-address-city (“Kaupunki”) in the same address form.
- `autofill-card-number-2` — `browser/browser/preferences/formAutofill.ftl` — Field label “Card number” rendered as “Credit card”.
    - Current: `Luottokortti`
    - Source: `label: Card number`
    - Suggest: `Kortin numero`
    - en-US “Card number” labels the input for the card number; “Luottokortti” means “credit card” and drops the “number” part, mislabeling the field (the adjacent error string correctly says “luottokortin numero”).
- `addressbar-locbar-quickactions-option` — `browser/browser/preferences/preferences.ftl` — Access key `Q` of `addressbar-locbar-quickactions-option` is not present in its label
    - Current: `Q`
    - Source: `accesskey: Q label: Quick actions`
    - The label is “Pikatoiminnot”. An access key not in the label cannot be underlined and is unreachable by keyboard.
- `home-prefs-highlights-option-most-recent-download` — `browser/browser/preferences/preferences.ftl` — Singular “Most recent download” rendered as plural “most recent downloads”.
    - Current: `Viimeisimmät lataukset`
    - Source: `label: Most recent download`
    - Suggest: `Viimeisin lataus`
    - en-US refers to a single most recent download item shown on the home page; the Finnish plural states that several downloads are shown.
- `search-keyword-warning-engine` — `browser/browser/preferences/preferences.ftl` — Warning about a keyword already used by a search engine says it is used by a bookmark.
    - Current: `Annettu pikakomento on jo kirjanmerkillä ”{ $name }”.`
    - Source: `You have chosen a keyword that is currently in use by “{ $name }”. Please select another.`
    - Suggest: `Annettu pikakomento on jo hakukoneella ”{ $name }”.`
    - en-US: “You have chosen a keyword that is currently in use by “{ $name }””, where $name is a search engine name (per the Variables comment). The Finnish calls it a bookmark, which duplicates the separate string search-keyword-warning-bookmark and misinforms the user about what owns the keyword.
- `cookie-tab-content` — `browser/browser/protections.ftl` — The final sentence about blocking cross-site tracking cookies reducing follow-you ads is missing.
    - Current: `Ne on asetettu kolmansien osapuolten, kuten mainostajien ja analytiikkayhtiöiden, toimesta.`
    - Source: `These cookies follow you from site to site to gather data about what you do online. They are set by third parties such as advertisers and analytics companies. Blocking cross-site tracking cookies reduces the number of a…`
    - Suggest: `Ne on asetettu kolmansien osapuolten, kuten mainostajien ja analytiikkayhtiöiden, toimesta. Sivustorajat ylittävien seurainevästeiden estäminen vähentää sinua seuraavien mainosten määrää.`
    - en-US ends with "Blocking cross-site tracking cookies reduces the number of ads that follow you around." — a whole factual sentence present in the source has no counterpart in the Finnish string.
- `smartblock-placeholder-desc` — `browser/browser/protectionsPanel.ftl` — "being used for ads" rendered as the content "using ads" — the agent of the action is reversed.
    - Current: `tai käyttämästä mainoksia`
    - Source: `Your { -brand-short-name } settings blocked this content from tracking you across sites or being used for ads.`
    - Suggest: `tai sen käyttämisen mainoksiin`
    - en-US: "blocked this content from tracking you across sites or being used for ads". The Finnish verb chain makes the blocked content the user of ads ("from using ads") instead of the thing that is used for ads; the passive sense is lost and the sentence states something the source does not.
- `back` — `browser/browser/touchbar/touchbar.ftl` — The Back and Forward Touch Bar buttons are swapped: "back" is translated as "Eteen" (forward).
    - Current: `back = Eteen`
    - Source: `Back`
    - Suggest: `back = Takaisin`
    - Finnish "eteen" means forward/ahead, so the Back button is labelled Forward. Paired with the "forward = Taakse" defect, both navigation buttons carry the opposite label.
- `forward` — `browser/browser/touchbar/touchbar.ftl` — "forward" is translated as "Taakse" (backward).
    - Current: `forward = Taakse`
    - Source: `Forward`
    - Suggest: `forward = Eteenpäin`
    - "Taakse" means backward/behind; the Forward button therefore reads as Back. Reversed meaning of a navigation control.
- `unified-extensions-mb-blocklist-error-multiple` — `browser/browser/unifiedExtensions.ftl` — The .message body repeats the count instead of giving the reason (policy violation).
    - Current: `{ $extensionsCount } laajennusta poistettu käytöstä`
    - Source: `heading: {$extensionsCount ->} [other] { $extensionsCount } extensions disabled message: Some of your extensions have been disabled for violating Mozilla’s policies.`
    - Suggest: `Jotkin laajennuksistasi on poistettu käytöstä, koska ne rikkovat Mozillan käytäntöjä.`
    - en-US .message: "Some of your extensions have been disabled for violating Mozilla’s policies." The Finnish states only a count, losing the reason that the single-extension variant (unified-extensions-mb-blocklist-error-single) does convey.
- `unified-extensions-mb-blocklist-warning-multiple2` — `browser/browser/unifiedExtensions.ftl` — The .message body repeats the count instead of saying the extensions are restricted and can be re-enabled at some risk.
    - Current: `{ $extensionsCount } laajennusta poistettu käytöstä`
    - Source: `heading: {$extensionsCount ->} [other] { $extensionsCount } extensions disabled message: Some of your extensions are restricted and have been disabled. You can enable them in settings, but this may be risky.`
    - Suggest: `Jotkin laajennuksistasi on rajoitettu ja poistettu käytöstä. Voit ottaa ne käyttöön asetuksista, mutta se voi olla riskialtista.`
    - en-US .message: "Some of your extensions are restricted and have been disabled. You can enable them in settings, but this may be risky." The Finnish message drops both the reason (restricted) and the statement that the user can re-enable them with risk, duplicating the heading instead.
- `developer-button.tooltiptext2` — `browser/chrome/browser/customizableui/customizableWidgets.properties` — Tooltip adds a claim that the developer tools are in English.
    - Current: `Avaa web-työkalut (englanninkielisiä) (%S)`
    - Source: `Open Web developer tools (%S)`
    - Suggest: `Avaa web-kehittäjän työkalut (%S)`
    - The en-US says only "Open Web developer tools"; the added "(englanninkielisiä)" asserts the tools are English-only, which the fi tree contradicts since devtools strings are localized.
- `dialogTitleEdit` — `browser/chrome/browser/places/bookmarkProperties.properties` — Generic "Properties for “%S”" is rendered as properties of a *folder*, adding a type the source does not state.
    - Current: `Muokkaa kansion ”%S” ominaisuuksia`
    - Source: `Properties for “%S”`
    - Suggest: `Kohteen ”%S” ominaisuuksia`
    - The en-US title is type-neutral and this dialog title is also used for bookmark items, not only folders, so the Finnish asserts the edited item is a folder when it may not be.
- `FileError_NoIgnore` — `browser/installer/override.properties` — Instructs the user to click "Hylkää" (Abort) where the dialog's button is Cancel ("Peruuta").
    - Current: `lopeta asennus valitsemalla Hylkää`
    - Source: `Error opening file for writing:   $0  Click Retry to try again, or Cancel to stop the installation.`
    - Suggest: `lopeta asennus valitsemalla Peruuta`
    - The en-US says "Cancel to stop the installation" and CancelBtn in the same file is "Peruuta"; "Hylkää" is this file's rendering of Abort, used in the FileError variant. The user is told to press a button that is not on this dialog.
- `icon-warning` — `devtools/client/application.ftl` — The .title attribute of icon-warning contains corrupted, duplicated content ("Warning", a stray "titleWarning" token, a blank line, then "Warning" again) instead of the single word the source defines.
    - Current: `titleWarning`
    - Source: `alt: Warning icon title: Warning`
    - Suggest: `.title = Warning`
    - en-US has `icon-warning .title = Warning`. The fi file instead renders a multi-line value containing "Warning", the stray literal "titleWarning", a blank line and a second "Warning", so the warning icon's tooltip shows garbled text including an internal attribute-name fragment that was never meant to be user-visible. This is content, not file formatting: the extra words appear in the tooltip the…
- `comboboxoption` — `dom/chrome/accessibility/AccessFu.properties` — "combo box option" is rendered as "combo box settings".
    - Current: `comboboxoption = monivalintakohdan asetukset`
    - Source: `combo box option`
    - Suggest: `comboboxoption = valintalistan vaihtoehto`
    - "asetukset" means settings/preferences, not a single selectable option; the role describes one option inside a combo box (cf. listboxoption = valinta).
- `main` — `dom/chrome/accessibility/AccessFu.properties` — The ARIA "main" landmark is announced as "main menu" instead of the main content region.
    - Current: `main = päävalikko`
    - Source: `main`
    - Suggest: `main = pääsisältö`
    - The en-US "main" (under the "# Landmark announcements" comment) is the main content landmark, not a menu. "päävalikko" means "main menu", so a screen-reader user is told they are in a menu when they are in the page's main content.
- `mathmlfractionwithoutbar` — `dom/chrome/accessibility/AccessFu.properties` — "fraction without bar" is rendered as "fraction without a divisor".
    - Current: `mathmlfractionwithoutbar = murtoluku ilman jakajaa`
    - Source: `fraction without bar`
    - Suggest: `mathmlfractionwithoutbar = murtoluku ilman murtoviivaa`
    - "bar" is the fraction line, not the divisor; the file already translates denominator as "nimittäjä", so "ilman jakajaa" wrongly says the fraction has no divisor.
- `mathmlscripted` — `dom/chrome/accessibility/AccessFu.properties` — MathML "scripted" is translated as "command sequence/batch".
    - Current: `mathmlscripted = komentojono`
    - Source: `scripted`
    - Suggest: `mathmlscripted = indeksoitu`
    - In MathML, "scripted" refers to an element carrying sub/superscripts (cf. subscript/superscript in the same file), not to a computer script; "komentojono" means a batch of commands.
- `menubar` — `dom/chrome/accessibility/AccessFu.properties` — The "menu bar" role is announced simply as "menu".
    - Current: `menubar = valikko`
    - Source: `menu bar`
    - Suggest: `menubar = valikkopalkki`
    - en-US distinguishes "menu bar" from "menu popup" (ponnahdusvalikko); rendering menubar as plain "valikko" loses the role distinction that screen readers rely on.
- `main` — `dom/chrome/accessibility/mac/accessible.properties` — The "main" landmark role is rendered as "centre/hub".
    - Current: `main = keskus`
    - Source: `main`
    - Suggest: `main = pääsisältö`
    - The comment marks these as WAI-ARIA landmark role descriptions; "keskus" (centre, hub) does not name the main content region.
- `cspBlocked` — `dom/chrome/appstrings.properties` — "content security policy" is translated as a privacy policy ("tietosuojakäytäntö").
    - Current: `Tällä sivulla on sisällön tietosuojakäytäntö`
    - Source: `This page has a content security policy that prevents it from being loaded in this way.`
    - Suggest: `Tällä sivulla on sisällön turvallisuuskäytäntö`
    - CSP is a security mechanism; "tietosuoja" means data protection/privacy. The error page tells the user the page has a privacy policy blocking framing, which is not what the en-US says and misnames a well-known security feature.
- `5` — `dom/chrome/layout/xmlparser.properties` — The parser error "unclosed token" is rendered with "poletti" (a physical token/coin).
    - Current: `5 = sulkematon poletti`
    - Source: `unclosed token`
    - Suggest: `5 = sulkematon lekseemi`
    - In this Expat error list "token" is a lexical unit of the XML document; "poletti" denotes a physical token (as used for PKCS#11 hardware tokens elsewhere) and does not name anything in a parse error shown on the XML error page.
- `hostNameMightBeKeyword` — `dom/chrome/security/csp.properties` — CSP "keyword" is translated as "search term".
    - Current: `Tulkitaan %1$S palvelimen nimeksi, ei hakusanaksi. Jos halusit kirjoittaa hakusanan`
    - Source: `Interpreting %1$S as a hostname, not a keyword. If you intended this to be a keyword, use ‘%2$S’ (wrapped in single quotes).`
    - Suggest: `Tulkitaan %1$S palvelimen nimeksi, ei avainsanaksi. Jos halusit kirjoittaa avainsanan`
    - A CSP keyword (e.g. 'self') is an "avainsana", as the same file translates it in strictDynamicButNoHashOrNonce; "hakusana" means a search term and misidentifies the construct the developer must fix.
- `WeakCipherSuiteWarning` — `dom/chrome/security/security.properties` — "uses the cipher RC4 for encryption" becomes "is protected with an RC4 encryption key".
    - Current: `Tämä sivusto on suojattu RC4-salausavaimella`
    - Source: `This site uses the cipher RC4 for encryption, which is deprecated and insecure.`
    - Suggest: `Tämä sivusto käyttää salaukseen RC4-salausmenetelmää`
    - RC4 is a cipher, not a key, and the en-US warning says the site uses it, not that the site is protected by it; "on suojattu" asserts protection where the source reports a weakness.
- `SEC_ERROR_PKCS11_DEVICE_ERROR` — `security/manager/chrome/pipnss/nsserrors.properties` — "token" is rendered as "vuoromerkki" (queue ticket) instead of the term used elsewhere in the file.
    - Current: `virheestä vuoromerkissä tai paikassa`
    - Source: `A PKCS #11 module returned CKR_DEVICE_ERROR, indicating that a problem has occurred with the token or slot.`
    - Suggest: `virheestä poletissa tai paikassa`
    - en-US: "a problem has occurred with the token or slot". Every other string in this file translates the PKCS#11 token as "poletti" (e.g. SEC_ERROR_TOKEN_NOT_LOGGED_IN); "vuoromerkki" means a queue number and names nothing in this context.
- `SSL_ERROR_DECRYPTION_FAILURE` — `security/manager/chrome/pipnss/nsserrors.properties` — Decryption failure is described as an encryption failure, identical to SSL_ERROR_ENCRYPTION_FAILURE.
    - Current: `SSL_ERROR_DECRYPTION_FAILURE = Valitun salaajan datan salausalgoritmi kohtasi virheen.`
    - Source: `Bulk data decryption algorithm failed in selected cipher suite.`
    - Suggest: `SSL_ERROR_DECRYPTION_FAILURE = Valitun salaajan datan salauksenpurkualgoritmi kohtasi virheen.`
    - en-US: "Bulk data decryption algorithm failed…" versus "Bulk data encryption algorithm failed…" for the previous key. The Finnish text is byte-identical for both, so the decryption error names the wrong operation.
- `SSL_ERROR_RX_UNEXPECTED_UNCOMPRESSED_RECORD` — `security/manager/chrome/pipnss/nsserrors.properties` — "uncompressed record" is rendered as "compressed record", reversing the condition.
    - Current: `SSL vastaanotti odottamattoman tiivistetyn paketin.`
    - Source: `SSL received an unexpected uncompressed record.`
    - Suggest: `SSL vastaanotti odottamattoman tiivistämättömän paketin.`
    - en-US: "SSL received an unexpected uncompressed record." The negation in "un-compressed" is dropped, making this identical in meaning to SSL_ERROR_DECOMPRESSION_FAILURE (line 114), which correctly uses "tiivistetyn" for a compressed record.
- `newCAMessage1` — `security/manager/chrome/pippki/pippki.properties` — A question asking the user whether to trust a CA is rendered as a statement that it is trusted.
    - Current: `Varmentajaan %S luotetaan seuraavissa toimissa:`
    - Source: `Do you want to trust “%S” for the following purposes?`
    - Suggest: `Luotetaanko varmentajaan %S seuraavissa toimissa?`
    - en-US: "Do you want to trust “%S” for the following purposes?" The Finnish asserts that the certificate authority is trusted rather than asking for the user's decision in a dialog whose purpose is to obtain that decision.
- `edit-trust-ca` — `security/manager/security/certificates/certManager.ftl` — "represents a Certificate Authority" is rendered as "authenticates the certificate authority".
    - Current: `Varmenne { $certName } todentaa varmentajan.`
    - Source: `The certificate “{ $certName }” represents a Certificate Authority.`
    - Suggest: `Varmenne { $certName } on varmentajan varmenne.`
    - en-US states that the certificate itself is a CA certificate; the Finnish instead claims the certificate verifies/authenticates some CA, which is a different statement about what the certificate does.
- `devinfo-label` — `security/manager/security/certificates/deviceManager.ftl` — The token "Label" column is translated as "Form name".
    - Current: `Lomakkeen nimi`
    - Source: `label: Label`
    - Suggest: `Nimike`
    - en-US "Label" is the PKCS#11 token's label shown in the Device Manager details list. "Lomake" means an HTML/paper form, which has nothing to do with this field.
- `crashreporter-comment-prompt` — `toolkit/crashreporter/crashreporter.ftl` — The Finnish instructs the user to write the comment in English, an instruction the en-US does not give.
    - Current: `Lisää kommenttisi englanniksi`
    - Source: `Add a comment (comments are publicly visible)`
    - Suggest: `Lisää kommentti`
    - en-US is "Add a comment (comments are publicly visible)"; the added "englanniksi" imposes a language requirement on the user that the source does not state.
- `push-end-point-result` — `toolkit/toolkit/about/aboutServiceWorkers.ftl` — “Push Endpoint” rendered as “Tulosteen päätepiste” (printout/output endpoint).
    - Current: `<strong>Tulosteen päätepiste:</strong>`
    - Source: `<strong>Push Endpoint:</strong> { $name }`
    - Suggest: `<strong>Push-päätepiste:</strong>`
    - “Push” refers to the Web Push endpoint, not to output/printing; “tuloste” means printout/output, naming a different thing. The same error appears in push-end-point-waiting.
- `drag-enabled` — `toolkit/toolkit/about/aboutSupport.ftl` — “scrollbar drag” rendered as “vierityspalkin vastus” (scrollbar resistance).
    - Current: `vierityspalkin vastus käytössä`
    - Source: `scrollbar drag enabled`
    - Suggest: `vierityspalkin raahaus käytössä`
    - “Drag” here is the act of dragging the scrollbar; “vastus” means resistance/drag force, a different concept, so the APZ capability listed is misnamed.
- `pdfjs-open-attachments-inline` — `toolkit/toolkit/about/aboutSupport.ftl` — “Inline” rendered as “sisennettynä” (indented).
    - Current: `Avaa PDF-liitteet sisennettynä`
    - Source: `Open PDF Attachments Inline`
    - Suggest: `Avaa PDF-liitteet samassa näkymässä`
    - “Open PDF Attachments Inline” means opening attachments within the viewer, not indenting them; “sisennettynä” means “indented” and says something the source never said.
- `about-telemetry-keyed-histogram-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — “Keyed Histograms” rendered as “Histogrammit merkinnöistä” (histograms of entries).
    - Current: `Histogrammit merkinnöistä`
    - Source: `Keyed Histograms`
    - Suggest: `Avaimelliset histogrammit`
    - “Keyed” is rendered “Avaimelliset” in the adjacent about-telemetry-keyed-scalar-section; “merkinnöistä” says the histograms are about entries, which is a different statement about the section's content.
- `third-party-message-no-duration` — `toolkit/toolkit/about/aboutThirdParty.ftl` — “Not recorded” rendered as “Ei nauhoitettu” (not audio/video-recorded).
    - Current: `Ei nauhoitettu`
    - Source: `Not recorded`
    - Suggest: `Ei tallennettu`
    - Here “recorded” means the blocking time was not measured/logged; “nauhoittaa” specifically means to record audio or video, which is not what the field reports.
- `url-classifier-content-classifier-loading-url` — `toolkit/toolkit/about/url-classifier.ftl` — Noun label “Loading URL” turned into a sentence “the URL is being loaded”.
    - Current: `URL-osoitetta ladataan`
    - Source: `Loading URL`
    - Suggest: `Lataava URL-osoite`
    - The developer comment states this is the URL that loads the URL being tested (“hence Loading URL”), i.e. a field label for a URL. The Finnish reads as a progress message about a URL being loaded, which is a different meaning.
- `url-classifier-content-classifier-loading-url-enabled` — `toolkit/toolkit/about/url-classifier.ftl` — Checkbox described as enabling URL loading instead of enabling the Loading-URL field.
    - Current: `Ota URL-osoitteen lataus käyttöön`
    - Source: `Enable loading URL`
    - Suggest: `Ota lataava URL-osoite käyttöön`
    - The comment says the checkbox lets the developer type a “Loading URL”; it does not enable the loading of a URL. The Finnish states the checkbox turns on URL loading, a different action.
- `contentanalysis-slow-agent-dialog-body-clipboard` — `toolkit/toolkit/contentanalysis/contentanalysis.ftl` — The Finnish says the agent is reviewing what you pasted "in violation of" the organisation's data policies, instead of reviewing it "against" (i.e. comparing it to) those policies.
    - Current: `organisaatiosi datakäytäntöjen vastaisesti`
    - Source: `{ $agent } is reviewing what you pasted against your organization’s data policies. This may take a moment.`
    - Suggest: `organisaatiosi datakäytäntöjä vasten`
    - en-US "reviewing what you pasted against your organization's data policies" means checking the content against the policies; "vastaisesti" means "contrary to / in breach of", so the dialog tells the user the product has already concluded their paste broke company policy while the scan is still in progress. The sibling string for files (contentanalysis-slow-agent-dialog-body-file) correctly uses "…
- `region-name-cz-2019` — `toolkit/toolkit/intl/regionNames.ftl` — Czechia is given as the long formal name "Tšekin tasavalta" rather than the short country name.
    - Current: `Tšekin tasavalta`
    - Source: `Czechia`
    - Suggest: `Tšekki`
    - The -2019 message id exists precisely to carry the short form "Czechia" instead of "Czech Republic"; the established Finnish short name is "Tšekki", and every other entry in this list uses the short country name.
- `ssl-error-decryption-failure` — `toolkit/toolkit/neterror/nsserrors.ftl` — The decryption-failure message says "encryption algorithm", making it identical to the encryption-failure message.
    - Current: `Valitun salaajan datan salausalgoritmi kohtasi virheen.`
    - Source: `Bulk data decryption algorithm failed in selected cipher suite.`
    - Suggest: `Valitun salaajan datan salauksenpurkualgoritmi kohtasi virheen.`
    - en-US distinguishes "Bulk data encryption algorithm failed" (ssl-error-encryption-failure) from "Bulk data decryption algorithm failed" (ssl-error-decryption-failure); the Finnish renders both with "salausalgoritmi" (encryption algorithm), losing the distinction between the two error codes.
- `pdfjs-editor-add-signature-save-warning-message` — `toolkit/toolkit/pdfviewer/viewer.ftl` — "to save more" (store more signatures) is rendered with "säästää" (to economise), not "tallentaa".
    - Current: `Poista yksi säästääksesi lisää.`
    - Source: `You’ve reached the limit of 5 saved signatures. Remove one to save more.`
    - Suggest: `Poista yksi tallentaaksesi lisää.`
    - The en-US "save" here means storing a signature, as in the same file's pdfjs-editor-add-signature-save-checkbox ("Tallenna allekirjoitus"); "säästääksesi" means to save money/economise and makes the sentence nonsensical.
- `remove-primary-password-warning2` — `toolkit/toolkit/preferences/preferences.ftl` — The condition "if your computer is compromised" is dropped, turning a conditional risk into an unconditional statement.
    - Current: `Jos poistat pääsalasanan, tietosi eivät enää ole suojattuina.`
    - Source: `If you remove your Primary Password your information will not be protected if your computer is compromised.`
    - Suggest: `Jos poistat pääsalasanan, tietosi eivät ole suojattuja, jos tietokoneesi vaarantuu.`
    - en-US: "If you remove your Primary Password your information will not be protected if your computer is compromised." The Finnish states flatly that the data is no longer protected, omitting the circumstance that scopes the warning.
- `webauthn-block` — `toolkit/toolkit/webauthnDialog.ftl` — Access key `B` of `webauthn-block` is not present in its label
    - Current: `B`
    - Source: `(value): Block accesskey: B`
    - The label is “Estä”. An access key not in the label cannot be underlined and is unreachable by keyboard.

### B. Mistranslation, reversed meaning, wrong names & brand

- `set-default-menu-message-row-layout-subtitle-variant` — `browser/browser/newtab/asrouter.ftl` — macOS "Dock" is translated as "telakka", while every other string keeps "Dock".
    - Current: `kiinnitä se telakkaan`
    - Source: `{$sel_1 ->} [macos] Keep { -brand-short-name } at your fingertips — make it your default and keep it in your Dock. [other] Keep { -brand-short-name } at your fingertips — make it your default and keep it in your taskbar.`
    - Suggest: `kiinnitä se Dockiin`
    - The Dock is a macOS product-name UI element kept untranslated throughout this file and the tree ("Pidä { -brand-short-name } Dockissa", "Aseta oletukseksi ja pidä Dockissa").
- `urlbar-translations-button-intro` — `browser/browser/translations.ftl` — "Beta" translated as "Beeta" although the developer comment forbids translating it.
    - Current: `Kokeile yksityisiä käännöksiä { -brand-shorter-name }issa - Beeta`
    - Source: `tooltiptext: Try private translations in { -brand-shorter-name } - Beta`
    - Suggest: `Kokeile yksityisiä käännöksiä { -brand-shorter-name }issa - Beta`
    - The comment states: "here 'Beta' should not be translated, as it is a reflection of the un-localized BETA icon that is in the panel".
- `urlbar-translations-button2` — `browser/browser/translations.ftl` — "Beta" translated as "Beeta" although the developer comment forbids translating it.
    - Current: `Käännä tämä sivu - Beeta`
    - Source: `tooltiptext: Translate this page - Beta`
    - Suggest: `Käännä tämä sivu - Beta`
    - The comment states: "here 'Beta' should not be translated, as it is a reflection of the un-localized BETA icon that is in the panel". The localized form no longer matches the untranslated BETA icon shown in the panel.
- `certificate-viewer-state-province` — `toolkit/toolkit/about/certviewer.ftl` — “State/Province” rendered as “Paikkakunta” (municipality/town).
    - Current: `certificate-viewer-state-province = Paikkakunta`
    - Source: `State/Province`
    - Suggest: `Osavaltio/maakunta`
    - “Paikkakunta” names a locality, a different administrative level than state/province; it also collides with the neighbouring Locality field, so two distinct certificate fields are mislabelled. The same applies to certificate-viewer-inc-state-province (“Perustuspaikkakunta”).

### C. Grammar, agreement & spelling

- `cfr-doorhanger-doh-body` — `browser/browser/newtab/asrouter.ftl` — Wrong person on the purpose clause: "suojellaksesi sinua" says the user protects the user, not that Firefox protects them.
    - Current: `kumppanipalveluun suojellaksesi sinua, kun selaat verkkoa`
    - Source: `Your privacy matters. { -brand-short-name } now securely routes your DNS requests whenever possible to a partner service to protect you while you browse.`
    - Suggest: `kumppanipalveluun suojellakseen sinua, kun selaat verkkoa`
    - The subject of the purpose clause is { -brand-short-name }, so the 3rd-person possessive suffix ("suojellakseen") is required; the 2nd-person form attributes the action to the reader.
- `set-default-pdf-handler-headline` — `browser/browser/newtab/asrouter.ftl` — Misspelling: "Muuttaksesi" instead of "Muuttaaksesi".
    - Current: `Muuttaksesi toimintaa, etsi asetuksista “PDF”.`
    - Source: `<strong>Your PDFs now open in { -brand-short-name }.</strong> Edit or sign forms directly in your browser. To change, search “PDF” in settings.`
    - Suggest: `Muuttaaksesi toimintaa, etsi asetuksista “PDF”.`
    - The first infinitive + translative form of "muuttaa" is "muuttaaksesi"; a vowel is missing.
- `fx100-upgrade-thank-you-body` — `browser/browser/newtab/onboarding.ftl` — Misspelling: "terveellisemän" instead of "terveellisemmän".
    - Current: `paremman ja terveellisemän internetin`
    - Source: `It’s our 100th release of { -brand-short-name }. Thank <em>you</em> for helping us build a better, healthier internet.`
    - Suggest: `paremman ja terveellisemmän internetin`
    - The comparative genitive requires a double m; fx100-thank-you-subtitle in the same file spells it correctly.
- `onboarding-minimal-tabs-tooltip` — `browser/browser/newtab/onboarding.ftl` — Misspelling: "pienennettyssä" instead of "pienennetyssä".
    - Current: `pienennettyssä sivupaneelissa`
    - Source: `title: A browser window displaying tabs as small icons along the side of the screen, in a minimized sidebar.`
    - Suggest: `pienennetyssä sivupaneelissa`
    - The inessive of "pienennetty" is "pienennetyssä"; the paired string onboarding-minimal-tabs-description spells it correctly.
- `onboarding-new-user-survey-legal-link-label` — `browser/browser/newtab/onboarding.ftl` — Missing space before the privacy-notice link, so two words run together in the rendered text.
    - Current: `{ -brand-product-name }in<a data-l10n-name="privacy_notice">tietosuojakäytännön</a>`
    - Source: `By selecting “{ onboarding-new-user-survey-next-button-label },” you agree to { -brand-product-name }’s <a data-l10n-name="privacy_notice">Privacy Notice</a>`
    - Suggest: `{ -brand-product-name }in <a data-l10n-name="privacy_notice">tietosuojakäytännön</a>`
    - The rendered legal line reads "Firefoxintietosuojakäytännön" with no word break (there is also a stray double space earlier in the sentence). This is missing spacing in the text the user reads, not file indentation.
- `onboarding-personalization-use-case-title` — `browser/browser/newtab/onboarding.ftl` — Misspelling: "ensijaisesti" instead of "ensisijaisesti".
    - Current: `Mihin aiot käyttää { -brand-short-name }ia ensijaisesti?`
    - Source: `What will you use { -brand-short-name } for?`
    - Suggest: `Mihin aiot käyttää { -brand-short-name }ia ensisijaisesti?`
    - A syllable is missing from "ensisijaisesti"; the correct form appears elsewhere in the tree (e.g. "Aseta ensisijaiseksi selaimeksi").
- `policy-IPProtectionAvailable` — `browser/browser/policies/policies-descriptions.ftl` — Ungrammatical verb government: "Estä … VPN:n olevan saatavilla".
    - Current: `Estä sisäänrakennetun VPN:n olevan saatavilla käyttäjille.`
    - Source: `Prevent the built-in VPN from being available to users.`
    - Suggest: `Estä sisäänrakennettua VPN:ää olemasta saatavilla käyttäjille.`
    - Finnish "estää" takes a partitive object plus a 3rd infinitive in the elative ("estää jotakin olemasta"), not genitive + participle.
- `policy-RelaunchRequired` — `browser/browser/policies/policies-descriptions.ftl` — Duplicated word: "käynnistetään uudelleen uudelleen".
    - Current: `käynnistetään uudelleen uudelleen tietyn ajan kuluessa`
    - Source: `Require { -brand-short-name } to be relaunched within a given period and notify the user of the upcoming relaunch.`
    - Suggest: `käynnistetään uudelleen tietyn ajan kuluessa`
    - "uudelleen" appears twice in a row; the en-US has a single "relaunched".
- `policy-SkipTermsOfUse2` — `browser/browser/policies/policies-descriptions.ftl` — Misspelling: "tietosuojakäytöntöä" instead of "tietosuojakäytäntöä".
    - Current: `käyttöehtoja ja tietosuojakäytöntöä`
    - Source: `Do not display the Terms of Use and Privacy Notice upon startup. You represent that you accept and have the authority to accept the Terms of Use on behalf of all individuals to whom you provide access to this browser.`
    - Suggest: `käyttöehtoja ja tietosuojakäytäntöä`
    - Vowel error in a standard term; everywhere else in the tree it is "tietosuojakäytäntö".
- `ERROR_CREATE_DIRECTORY_PREFIX` — `browser/installer/custom.properties` — Garbled word in installer error message: "kans1iota" contains a stray digit.
    - Current: `Virhe luotaessa kans1iota:`
    - Source: `Error creating directory:`
    - Suggest: `Virhe luotaessa kansiota:`
    - "kans1iota" is not a Finnish word; the correct form is "kansiota". The typo is visible in the installer's error dialog.
- `support-user-namespaces-unavailable` — `toolkit/toolkit/about/aboutSupport.ftl` — Brand name given the appositive “-palvelu” (service).
    - Current: `{ -brand-short-name } -palvelun suojausominaisuuksia`
    - Source: `{ $status } — This feature is not allowed by your system. This can restrict security features of { -brand-short-name }.`
    - Suggest: `{ -brand-short-name }in suojausominaisuuksia`
    - The source says “security features of { -brand-short-name }”; calling the browser a “palvelu” (service) mischaracterizes the product and is not how the brand term is inflected elsewhere in the file.
- `-mdn-brand-name` — `toolkit/toolkit/branding/brandings.ftl` — The brand name "MDN Web Docs" is translated although the section comment forbids translating these names.
    - Current: `MDN-verkkodokumentit`
    - Source: `MDN Web Docs`
    - Suggest: `MDN Web Docs`
    - The group comment above this block states the feature names "cannot be: Transliterated. Translated." Other entries in the same block (Firefox Monitor, Mozilla VPN, Firefox Labs) are left in English, and the entries that may be partly localised carry an explicit per-string comment saying so; -mdn-brand-name has no such comment.

### D. Terminology, register & consistency

- `about-logins-intro-import3` — `browser/browser/aboutLogins.ftl` — Stray " a>" fragment appears as visible text at the end of the sentence.
    - Current: `tiedostosta</a> a>.`
    - Source: `Select the plus sign button above to add a password now. You can also <a data-l10n-name="import-browser-link">import passwords from another browser</a> or <a data-l10n-name="import-file-link">from a file</a>.`
    - Suggest: `tiedostosta</a>.`
    - A leftover closing-tag fragment is rendered as literal text after the link, so the user sees "…tiedostosta a>." The en-US ends the sentence right after the link.
- `about-logins-vulnerable-alert-text2` — `browser/browser/aboutLogins.ftl` — Misspelled verb form "vuosivat" instead of "vuotivat".
    - Current: `jonka tiedot todennäköisesti vuosivat`
    - Source: `This password has been used on another account that was likely in a data breach. Reusing credentials puts all your accounts at risk. Change this password.`
    - Suggest: `jonka tiedot todennäköisesti vuotivat`
    - "vuosivat" is not a Finnish word; the past tense of "vuotaa" is "vuotivat".
- `about-unloads-no-unloadable-tab` — `browser/browser/aboutUnloads.ftl` — Relative clause is ungrammatical: "joiden lataus purkaa".
    - Current: `Ei välilehtiä, joiden lataus purkaa.`
    - Source: `There are no unloadable tabs.`
    - Suggest: `Ei välilehtiä, joiden lataus voidaan purkaa.`
    - en-US "There are no unloadable tabs." The Finnish clause has "lataus" as subject of the transitive "purkaa", so it literally says the loading unloads something; a passive or potential form is required.
- `xpinstall-disabled` — `browser/browser/addonNotifications.ftl` — Compound written as two words: "saman nimistä".
    - Current: `napsauttamalla saman nimistä painiketta`
    - Source: `Software installation is currently disabled. Click Enable and try again.`
    - Suggest: `napsauttamalla samannimistä painiketta`
    - In standard Finnish the compound is written as one word, "samannimistä".
- `ai-window-manage-memories-header` — `browser/browser/aiFeatures.ftl` — Missing space before the brand placeable, so two words run together.
    - Current: `kun{ -smart-window-brand-name } on käytössä`
    - Source: `description: Memories are stored locally on this device to help protect your privacy. They refresh a few times a day while you use { -smart-window-brand-name }, so recent activity may take time to be reflected. heading:…`
    - Suggest: `kun { -smart-window-brand-name } on käytössä`
    - The rendered text reads "kunSmart Window" because the space between "kun" and the brand name is missing in the user-visible text.
- `aiwindow-firstrun-memories-title` — `browser/browser/aiWindow.ftl` — Double comparative "Enemmän hyödyllisempiä".
    - Current: `Enemmän hyödyllisempiä vastauksia`
    - Source: `More helpful answers, on your terms`
    - Suggest: `Hyödyllisempiä vastauksia`
    - "hyödyllisempiä" is already a comparative, so prefixing "enemmän" produces an ungrammatical double comparative for "More helpful answers".
- `fxa-signout-dialog-body-aiwindow` — `browser/browser/aiWindow.ftl` — Subject–verb disagreement and wrong verb: plural subject with singular transitive "vaihtaa".
    - Current: `Avoimet { -smart-window-brand-name } vaihtaa perinteisiin ikkunoihin.`
    - Source: `Synced data will remain in your account. Open { -smart-window-brand-name } will switch to Classic Windows.`
    - Suggest: `Avoimet { -smart-window-brand-name } vaihtuvat perinteisiksi ikkunoiksi.`
    - en-US says open Smart Windows will switch to Classic Windows; the Finnish uses a singular transitive verb with a plural subject, which is ungrammatical.
- `profiler-popup-presets-web-developer-description` — `browser/browser/appmenu.ftl` — Case disagreement between "suurimpaan osaan" and "vianjäljityksessä".
    - Current: `Suositeltu esiasetus suurimpaan osaan verkkosovellusten vianjäljityksessä.`
    - Source: `Recommended preset for most web app debugging, with low overhead.`
    - Suggest: `Suositeltu esiasetus suurimpaan osaan verkkosovellusten vianjäljityksestä.`
    - "osaan" governs the elative ("osaan jostakin"), so the inessive "vianjäljityksessä" does not agree.
- `default-browser-agent-task-description` — `browser/browser/backgroundtasks/defaultagent.ftl` — Misspelling "automattisesti" for "automaattisesti".
    - Current: `automattisesti`
    - Source: `The Default Browser Agent task checks when the default changes from { -brand-short-name } to another browser. If the change happens under suspicious circumstances, it will prompt users to change back to { -brand-short-n…`
    - Suggest: `automaattisesti`
    - Plain spelling error: the Finnish word is "automaattisesti" with a long "aa".
- `password-rules-email-description` — `browser/browser/backupSettings.ftl` — Missing possessive suffix in "Ei sinun sähköpostiosoite".
    - Current: `Ei sinun sähköpostiosoite`
    - Source: `Not your email address`
    - Suggest: `Ei sinun sähköpostiosoitteesi`
    - With the genitive pronoun "sinun" the noun needs the possessive suffix; the variant password-rules-email-description2 avoids the problem entirely.
- `browser-import-button2` — `browser/browser/browser.ftl` — Typo "selaimsta" in the tooltip.
    - Current: `toisesta selaimsta`
    - Source: `label: Import bookmarks… tooltiptext: Import bookmarks from another browser to { -brand-short-name }.`
    - Suggest: `toisesta selaimesta`
    - Missing vowel: the elative of "selain" is "selaimesta".
- `identity-description-active-loaded` — `browser/browser/browser.ftl` — Double negation: "eikä … ei ole".
    - Current: `eikä yhteytesi sivustoon ei ole yksityinen`
    - Source: `This website contains content that is not secure (such as scripts) and your connection to it is not private.`
    - Suggest: `eikä yhteytesi sivustoon ole yksityinen`
    - The conjunction "eikä" already carries the negation, so the extra "ei" is ungrammatical.
- `sharing-warning-window` — `browser/browser/browser.ftl` — Typo "parhailleen" instead of "parhaillaan".
    - Current: `Jaat parhailleen`
    - Source: `You are sharing { -brand-short-name }. Other people can see when you switch to a new tab.`
    - Suggest: `Jaat parhaillaan`
    - The adjacent string sharing-warning-screen uses the correct form "parhaillaan".
- `toolbar-settings-button` — `browser/browser/browser.ftl` — Typo "asetuket" in the non-macOS tooltip.
    - Current: `Avaa asetuket`
    - Source: `label: Settings tooltiptext: {$sel_1 ->} [macos] Open settings ({ $shortcut }) [other] Open settings`
    - Suggest: `Avaa asetukset`
    - "asetuket" is a misspelling of "asetukset"; the macOS variant in the same message spells it correctly.
- `urlbar-result-menu-trending-dont-show` — `browser/browser/browser.ftl` — Typo "suositujja" instead of "suosittuja".
    - Current: `Älä näytä suositujja hakuja`
    - Source: `accesskey: D label: Don’t show trending searches`
    - Suggest: `Älä näytä suosittuja hakuja`
    - Same misspelling as in urlbar-result-menu-trending-dont-show2; the correct partitive plural is "suosittuja".
- `urlbar-result-menu-trending-dont-show2` — `browser/browser/browser.ftl` — Typo "suositujja" instead of "suosittuja".
    - Current: `Älä näytä suositujja hakuja`
    - Source: `(value): Don’t show trending searches accesskey: D`
    - Suggest: `Älä näytä suosittuja hakuja`
    - "suositujja" is not a word; the partitive plural of "suosittu" is "suosittuja", as used correctly in urlbar-trending-dismissal-acknowledgment.
- `default-browser-guidance-notification-body-instruction-win10` — `browser/browser/defaultBrowserNotification.ftl` — `default-browser-guidance-notification-body-instruction-win10` quotes “Selain” but the string it names, `desktop-entry-generic-name`, reads “Verkkoselain”
    - Current: `Vaihe 1: Siirry kohtaan Asetukset > Oletussovellukset Vaihe 2: Vieritä alas kohtaan "Selain" Vaihe 3: Valitse { -brand-short-name }`
    - Source: `Step 1: Go to Settings > Default apps Step 2: Scroll down to “Web browser” Step 3: Select and choose { -brand-short-name }`
    - Suggest: `Verkkoselain`
    - In the source this string quotes “Web browser”, which is exactly the value of `desktop-entry-generic-name` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `site-rules-status-heading` — `browser/browser/ipProtection.ftl` — Missing possessive suffix in "Sinun sääntö".
    - Current: `Sinun sääntö`
    - Source: `Your rule`
    - Suggest: `Sääntösi`
    - Finnish requires the possessive suffix with the genitive pronoun: "sinun sääntösi" or simply "sääntösi".
- `vpn-error-alert-body` — `browser/browser/ipProtection.ftl` — Infinitive "Yrittää" used instead of the imperative "Yritä".
    - Current: `Yrittää myöhemmin uudelleen.`
    - Source: `Try again later.`
    - Suggest: `Yritä myöhemmin uudelleen.`
    - en-US "Try again later." is an imperative; every comparable string in the file uses "Yritä". "Yrittää" is a bare infinitive and reads as broken Finnish.
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — `desktop-to-mobile-subtitle` quotes “Synkronoi matkapuhelimeen” but the string it names, `sync-to-mobile-button-label`, reads “Synkronoi mobiililaitteeseen”
    - Current: `Skannaa QR-koodi ladataksesi { -brand-product-name }in mobiililaitteelle. Kun olet asentanut sen, valitse "Synkronoi matkapuhelimeen" käyttääksesi salasanoja, kirjanmerkkejä ja muuta liikkeellä ollessasi.`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `Synkronoi mobiililaitteeseen`
    - In the source this string quotes “Sync to mobile”, which is exactly the value of `sync-to-mobile-button-label` -- it is naming a piece of UI. The two have been translated differently, so the message points at a label the user cannot see. Fixing either string resolves this, and the check is re-derived every run.
- `connection-dns-over-https-url-custom` — `browser/browser/preferences/connection.ftl` — Misspelling: “ensijainen” instead of “ensisijainen”.
    - Current: `Kirjoita ensijainen osoite DNS-kyselyjen selvittämiseen HTTPS:n välityksellä`
    - Source: `accesskey: C label: Custom tooltiptext: Enter your preferred URL for resolving DNS over HTTPS`
    - Suggest: `Kirjoita ensisijainen osoite DNS-kyselyjen selvittämiseen HTTPS:n välityksellä`
    - “ensijainen” is not a Finnish word; the correct form is “ensisijainen”.
- `fonts-langgroup-khmer` — `browser/browser/preferences/fonts.ftl` — Malformed derivation “Khmerlainen” for the Khmer script.
    - Current: `Khmerlainen`
    - Source: `label: Khmer`
    - Suggest: `Khmeriläinen`
    - Finnish forms this adjective with -läinen after a front-vowel stem and requires a linking vowel: “khmeriläinen”; “Khmerlainen” is neither well formed nor vowel-harmonic.
- `more-from-moz-firefox-relay-description` — `browser/browser/preferences/moreFromMozilla.ftl` — Misspelling: “henkilöytesi” instead of “henkilöllisyytesi”.
    - Current: `Suojaa postilaatikkosi ja henkilöytesi ilmaisella sähköpostimaskilla.`
    - Source: `Protect your inbox and your identity with free email masking.`
    - Suggest: `Suojaa postilaatikkosi ja henkilöllisyytesi ilmaisella sähköpostimaskilla.`
    - “henkilöytesi” is not a Finnish word; “identity” is “henkilöllisyys”.
- `more-from-moz-mdn-card` — `browser/browser/preferences/moreFromMozilla.ftl` — Misspelling: “sovelluskehiystä” instead of “sovelluskehitystä”.
    - Current: `Opi web-sovelluskehiystä ilmaisten ohjeiden ja viitteiden avulla.`
    - Source: `description: Learn web development with free guides and references. label: { -mdn-brand-name }`
    - Suggest: `Opi web-sovelluskehitystä ilmaisten ohjeiden ja viitteiden avulla.`
    - Letter transposition in “kehitystä”.
- `permissions-site-speaker-desc` — `browser/browser/preferences/permissions.ftl` — Misspelling: “äänentoistolaiteen” instead of “äänentoistolaitteen”.
    - Current: `Seuraavat sivustot ovat pyytäneet oikeutta valita äänentoistolaiteen.`
    - Source: `The following websites have requested to select an audio output device. You can specify which websites are allowed to select an audio output device.`
    - Suggest: `Seuraavat sivustot ovat pyytäneet oikeutta valita äänentoistolaitteen.`
    - The genitive of “laite” is “laitteen”; the same string's next sentence spells it correctly.
- `browsing-protection-group2` — `browser/browser/preferences/preferences.ftl` — Misspelling: “riskalttiista” instead of “riskialttiista”.
    - Current: `varoittaa sinua riskalttiista tai ei-halutuista ohjelmistoista`
    - Source: `description: Dangerous sites and downloads can put your data and device at risk. { -brand-short-name } automatically blocks them, and warns you about risky or unwanted software. label: Deceptive content and dangerous so…`
    - Suggest: `varoittaa sinua riskialttiista tai ei-halutuista ohjelmistoista`
    - The compound is “riskialtis” → “riskialttiista”; a letter is missing.
- `containers-card-header2` — `browser/browser/preferences/preferences.ftl` — Misspelling: “käytttää” with a triple t.
    - Current: `niin voit käytttää eri käyttäjätilejä samalla sivustolla`
    - Source: `description: Separate cookies by container so you can use different accounts on the same site and limit cross-site tracking. label: Containers`
    - Suggest: `niin voit käyttää eri käyttäjätilejä samalla sivustolla`
    - Typo in “käyttää”.
- `dns-over-https-group2` — `browser/browser/preferences/preferences.ftl` — Misspelling: “nimipalvelujärjestlemä” instead of “nimipalvelujärjestelmä”.
    - Current: `Domain Name System (nimipalvelujärjestlemä) HTTPS:n kautta (DoH)`
    - Source: `description: Domain Name System over HTTPS (DoH) encrypts site lookups so it’s harder for your internet provider or others to see what websites you’re about to visit. label: DNS over HTTPS`
    - Suggest: `Domain Name System (nimipalvelujärjestelmä) HTTPS:n kautta (DoH)`
    - Letter transposition in “järjestelmä”.
- `history-remember-option-never2` — `browser/browser/preferences/preferences.ftl` — Ungrammatical clause for “When on, extensions need to be allowed.”
    - Current: `Kun käytössä, laajennukset tulee olla sallittu.`
    - Source: `description: Every window acts like a private window. When on, extensions need to be allowed. label: Never remember history`
    - Suggest: `Kun asetus on käytössä, laajennukset on erikseen sallittava.`
    - “laajennukset tulee olla sallittu” has no valid subject/agreement in Finnish (nominative plural with “tulee olla” plus singular participle).
- `preferences-ai-controls-description` — `browser/browser/preferences/preferences.ftl` — Doubled comma in the visible text.
    - Current: `Sinulla on aina vaihtoehtoja { -brand-short-name }issa,, mukaan lukien`
    - Source: `You always have a choice in { -brand-short-name }, including whether to use features enhanced with AI. More controls coming soon.`
    - Suggest: `Sinulla on aina vaihtoehtoja { -brand-short-name }issa, mukaan lukien`
    - Two consecutive commas appear in the user-visible sentence.
- `preferences-doh-advanced-section` — `browser/browser/preferences/preferences.ftl` — Same misspelling “nimipalvelujärjestlemä” in the advanced DoH section description.
    - Current: `Domain Name System (nimipalvelujärjestlemä) HTTPS:n kautta (DoH) salaa sivustojen etsinnän`
    - Source: `description: Domain Name System over HTTPS (DoH) encrypts site lookups so it’s harder for your internet provider or others to see what websites you’re about to visit. label: Advanced settings`
    - Suggest: `Domain Name System (nimipalvelujärjestelmä) HTTPS:n kautta (DoH) salaa sivustojen etsinnän`
    - Letter transposition in “järjestelmä”, duplicated from the other DoH description string.
- `preferences-etp-level-warning-message` — `browser/browser/preferences/preferences.ftl` — Redundant/ungrammatical “poista … pois käytöstä”.
    - Current: `poista seurannan suojaus pois käytöstä kyseisellä sivustolla`
    - Source: `heading: Heads up! Some sites may not work as expected. message: Some sites build trackers into their features or content. When { -brand-short-name } blocks them, the site looks broken. Try using “Fix site issue” or tur…`
    - Suggest: `poista seurannan suojaus käytöstä kyseisellä sivustolla`
    - “poistaa pois käytöstä” doubles the particle; the correct form is “poistaa käytöstä” (or “ottaa pois käytöstä”).
- `sitedata-cookies-exceptions2` — `browser/browser/preferences/preferences.ftl` — Agreement error in “voivat aina tai ei koskaan käyttää”.
    - Current: `mitkä verkkosivustot voivat aina tai ei koskaan käyttää evästeitä ja sivustotietoa`
    - Source: `accesskey: x description: You can specify which websites are always or never allowed to use cookies and site data. label: Manage exceptions`
    - Suggest: `mitkä verkkosivustot saavat aina käyttää evästeitä ja sivustotietoa ja mitkä eivät koskaan`
    - The negative verb must agree with the plural subject (“eivät koskaan”), and it cannot share the positive auxiliary “voivat” as written.
- `graph-week-summary` — `browser/browser/protections.ftl` — Doubled space between "esti" and the count in the singular variant.
    - Current: `{ -brand-short-name } esti  { $count } seuraimen viime viikon aikana`
    - Source: `{$count ->} [one] { -brand-short-name } blocked { $count } tracker over the past week [other] { -brand-short-name } blocked { $count } trackers over the past week`
    - Suggest: `{ -brand-short-name } esti { $count } seuraimen viime viikon aikana`
    - Two spaces appear between two words of the rendered sentence; the plural variant of the same message has a single space.
- `tabbrowser-allow-dialogs-to-get-focus` — `browser/browser/tabbrowser.ftl` — Possessive construction is ungrammatical: "heidän välilehteen" lacks the possessive suffix and uses a human pronoun for a site.
    - Current: `vievät sinut heidän välilehteen`
    - Source: `label: Allow notifications like this from { $domain } to take you to their tab`
    - Suggest: `vievät sinut kyseisen sivuston välilehdelle`
    - Finnish requires the possessive suffix ("välilehteensä") or an explicit genitive noun; "heidän välilehteen" is not grammatical, and "heidän" refers to people rather than to the site named by $domain.
- `webrtc-allow-share-screen-and-microphone-with-file` — `browser/browser/webrtcIndicator.ftl` — Case agreement error: "näyttöäsi sisällön" mixes partitive and genitive.
    - Current: `nähdä näyttöäsi sisällön`
    - Source: `Allow this local file to use your microphone and see your screen?`
    - Suggest: `nähdä näyttösi sisällön`
    - The parallel strings (webrtc-allow-share-screen-with-file, webrtc-allow-share-screen-and-audio-capture-with-file) correctly read "nähdä näyttösi sisällön"; here the possessed noun is in the wrong case for the following genitive-governed "sisällön".
- `unknownProtocolFound` — `browser/chrome/overrides/appstrings.properties` — Ungrammatical clause "ei ole sallittu käyttää tässä tavalla".
    - Current: `tai ei ole sallittu käyttää tässä tavalla`
    - Source: `Firefox doesn’t know how to open this address, because one of the following protocols (%S) isn’t associated with any program or is not allowed in this context.`
    - Suggest: `tai sitä ei ole sallittua käyttää tässä yhteydessä`
    - "tässä tavalla" mixes two expressions ("tällä tavalla" / "tässä yhteydessä") and the passive "ei ole sallittu käyttää" lacks its object, leaving the sentence broken; en-US reads "is not allowed in this context".
- `math` — `dom/chrome/accessibility/mac/accessible.properties` — Misspelling of "matematiikka".
    - Current: `math = matemaatiikka`
    - Source: `math`
    - Suggest: `math = matematiikka`
    - "matemaatiikka" has a doubled vowel; the correct Finnish spelling is "matematiikka". This role description is spoken by screen readers.
- `FormValidationNumberRangeUnderflow` — `dom/chrome/dom/dom.properties` — Missing verb makes the sentence ungrammatical.
    - Current: `Valitse arvo, joka vähintään %S.`
    - Source: `Please select a value that is no less than %S.`
    - Suggest: `Valitse arvo, joka on vähintään %S.`
    - The relative clause has no predicate; compare FormValidationNumberRangeOverflow ("joka on enintään %S"). This message is shown to end users in form validation bubbles.
- `PERR_ABORT` — `dom/chrome/layout/printing.properties` — Misspelling of "keskeytettiin".
    - Current: `Tulostustyö keskeytettin tai peruutettiin.`
    - Source: `The print job was aborted, or canceled.`
    - Suggest: `Tulostustyö keskeytettiin tai peruutettiin.`
    - "keskeytettin" is missing an "i"; the passive past form is "keskeytettiin", as the parallel verb "peruutettiin" in the same sentence shows.
- `PERR_GFX_PRINTER_DOC_IS_BUSY_PP` — `dom/chrome/layout/printing.properties` — Misspelling of "koska".
    - Current: `ksoka sivua ladataan vielä`
    - Source: `Cannot print-preview this document yet, it is still being loaded.`
    - Suggest: `koska sivua ladataan vielä`
    - Transposed letters: "ksoka" should be "koska" (as in PERR_GFX_PRINTER_DOC_IS_BUSY).
- `32` — `dom/chrome/layout/xmlparser.properties` — Misspelling of "tunnisteessa" (triple "e").
    - Current: `julkisessa tunnisteeessa on kiellettyjä merkkejä`
    - Source: `illegal character(s) in public id`
    - Suggest: `julkisessa tunnisteessa on kiellettyjä merkkejä`
    - The inessive of "tunniste" is "tunnisteessa" with two e's, not three.
- `SDAccessErrorCardReadOnly` — `dom/chrome/nsWebBrowserPersist.properties` — Wrong case on the subject "SD-kortti".
    - Current: `Ei voitu ladata tiedostoa, koska SD-korttia on käytössä.`
    - Source: `Cannot download file because the SD card is in use.`
    - Suggest: `Ei voitu ladata tiedostoa, koska SD-kortti on käytössä.`
    - The subject of "on käytössä" must be nominative; the partitive "SD-korttia" is ungrammatical (the parallel SDAccessErrorCardMissing correctly uses the partitive only with "ei löydy").
- `LoadingMixedActiveContent2` — `dom/chrome/security/security.properties` — Case disagreement between adjective and noun.
    - Current: `Ladataan osittain suojaamaton interaktiivista sisältöä`
    - Source: `Loading mixed (insecure) active content “%1$S” on a secure page`
    - Suggest: `Ladataan osittain suojaamatonta interaktiivista sisältöä`
    - The object is in the partitive ("sisältöä"), so the modifier must be "suojaamatonta"; the neighbouring LoadingMixedDisplayContent2 gets this right.
- `CookieRejectedInvalidCharName` — `netwerk/necko.properties` — Wrong case on the subject "Eväste".
    - Current: `Evästeä “%1$S” on hylätty`
    - Source: `Cookie “%1$S” has been rejected for invalid characters in the name.`
    - Suggest: `Eväste “%1$S” on hylätty`
    - With the passive perfect "on hylätty" the subject is nominative; every neighbouring string uses "Eväste … on hylätty".
- `SEC_ERROR_REUSED_ISSUER_AND_SERIAL` — `security/manager/chrome/pipnss/nsserrors.properties` — Misspelling of "kuitenkin".
    - Current: `mutta tuotava varmenne on kuitenkiin uusi varmenne`
    - Source: `You are attempting to import a cert with the same issuer/serial as an existing cert, but that is not the same cert.`
    - Suggest: `mutta tuotava varmenne on kuitenkin uusi varmenne`
    - "kuitenkiin" is not a Finnish word; the correct form is "kuitenkin".
- `SSL_ERROR_WEAK_SERVER_EPHEMERAL_DH_KEY` — `security/manager/chrome/pipnss/nsserrors.properties` — Stray hyphen joins "SSL" to the verb.
    - Current: `SSL-vastaanotti heikon ephemeral Diffie-Hellman -avaimen`
    - Source: `SSL received a weak ephemeral Diffie-Hellman key in Server Key Exchange handshake message.`
    - Suggest: `SSL vastaanotti heikon ephemeral Diffie-Hellman -avaimen`
    - Every other string in the file reads "SSL vastaanotti…"; here (and in SSL_ERROR_NEXT_PROTOCOL_DATA_INVALID) the subject is hyphenated to the finite verb, which is ungrammatical.
- `certErrorMitM2` — `security/manager/chrome/pipnss/pipnss.properties` — Case disagreement between modifier and "Mozilla".
    - Current: `%Sin tukena on voittoa tavoittelemattoman Mozilla`
    - Source: `%S is backed by the non-profit Mozilla, which administers a completely open certificate authority (CA) store. The CA store helps ensure that certificate authorities are following best practices for user security.`
    - Suggest: `%Sin tukena on voittoa tavoittelematon Mozilla`
    - "Mozilla" is the nominative subject complement, so the modifier must be "tavoittelematon"; the genitive "tavoittelemattoman" leaves the phrase ungrammatical on a certificate error page.
- `add-exception-domain-mismatch-long` — `security/manager/security/certificates/certManager.ftl` — Doubled verb "voi olla tarkoittaa".
    - Current: `Tämä voi olla tarkoittaa, että joku yrittää tekeytyä sivustoksi.`
    - Source: `The certificate belongs to a different site, which could mean that someone is trying to impersonate this site.`
    - Suggest: `Tämä voi tarkoittaa, että joku yrittää tekeytyä sivustoksi.`
    - "voi olla tarkoittaa" stacks two verbs; the grammatical form is "voi tarkoittaa".
- `delete-ssl-override-impact` — `security/manager/security/certificates/certManager.ftl` — Misspelling of "varmennetta".
    - Current: `vaadit sen käyttävän kelvollista varmentetta`
    - Source: `If you delete a server exception, you restore the usual security checks for that server and require it uses a valid certificate.`
    - Suggest: `vaadit sen käyttävän kelvollista varmennetta`
    - The partitive of "varmenne" is "varmennetta"; "varmentetta" is a typo found nowhere else in the file.
- `addon-badge-private-browsing-allowed3` — `toolkit/toolkit/about/aboutAddons.ftl` — Misspelling of “ikkunoissa”.
    - Current: `Sallittu yksityisissä ikkunnoissa`
    - Source: `title: Allowed in private windows`
    - Suggest: `Sallittu yksityisissä ikkunoissa`
    - “ikkunnoissa” has a doubled n; the correct inessive plural of “ikkuna” is “ikkunoissa”, as used elsewhere in the same file (e.g. detail-private-disallowed-label).
- `addon-badge-verified4` — `toolkit/toolkit/about/aboutAddons.ftl` — Misspelling of “laajennus”.
    - Current: `Tämä laajennnus on katselmoitu`
    - Source: `title: This extension has been reviewed to meet standards for security and performance`
    - Suggest: `Tämä laajennus on katselmoitu`
    - “laajennnus” contains three n's; the word is “laajennus”, spelled correctly everywhere else in the file.
- `colorway-removal-notice-message` — `toolkit/toolkit/about/aboutAddons.ftl` — “lisalta” is a typo for “listalta” (from the list).
    - Current: `“Tallennetut teemat”-lisalta`
    - Source: `heading: Your colorway theme(s) were removed. message: { -brand-product-name } updated its colorways collection. We removed the old version(s) from your “Saved Themes” list. Get new versions on the add-ons site.`
    - Suggest: `“Tallennetut teemat” -listalta`
    - The source says “from your ‘Saved Themes’ list”; “lisalta” is not a Finnish word — the ablative of “lista” is “listalta”.
- `mlmodel-addon-detail-used-by-label` — `toolkit/toolkit/about/aboutAddons.ftl` — “Used by” rendered as an active past participle “Käyttänyt” (has used).
    - Current: `Käyttänyt`
    - Source: `Used by`
    - Suggest: `Käyttökohteet`
    - The comment says this label introduces the extensions or features that use the model; “Käyttänyt” is the active participle “has used” and does not work as a section label for what uses the model.
- `about-httpsonly-title-site-not-available` — `toolkit/toolkit/about/aboutHttpsOnlyError.ftl` — Missing verb/case agreement in the error page title.
    - Current: `Suojattu sivusto ei saatavilla`
    - Source: `Secure Site Not Available`
    - Suggest: `Suojattua sivustoa ei ole saatavilla`
    - A Finnish negative existential clause requires the negated verb “ei ole” and a partitive subject; “Suojattu sivusto ei saatavilla” is ungrammatical as written.
- `about-reader-color-sepia-theme` — `toolkit/toolkit/about/aboutReader.ftl` — Compound-word error: “Seepia teema” written as two words.
    - Current: `Seepia teema`
    - Source: `(value): Sepia title: Sepia theme`
    - Suggest: `Seepiateema`
    - “Seepia” is a noun, so Finnish requires the compound “Seepiateema”, exactly as the sibling string renders “Contrast theme” as “Kontrastiteema”. The adjective cases (“Vaalea teema”, “Harmaa teema”) are correctly separate.
- `about-telemetry-scalar-section` — `toolkit/toolkit/about/aboutTelemetry.ftl` — “Skaalariarvot” misspells “skalaari” (scalar).
    - Current: `Skaalariarvot`
    - Source: `Scalars`
    - Suggest: `Skalaariarvot`
    - The Finnish term for “scalar” is “skalaari”, as spelled correctly in the very next string (about-telemetry-keyed-scalar-section = “Avaimelliset skalaariarvot”). “Skaalari” would derive from “skaala” (scale).
- `experimental-features-js-warp-description` — `toolkit/toolkit/firefoxlabs/features.ftl` — "JavaScript" is written with a lowercase j ("javaScript").
    - Current: `javaScript-kielen`
    - Source: `Enable Warp, a project to improve JavaScript performance and memory usage.`
    - Suggest: `JavaScript-kielen`
    - JavaScript is a product name and is capitalised everywhere else in the tree, including the label of this very message (experimental-features-js-warp = JavaScript JIT: Warp).
- `profile-creation-explanation-1` — `toolkit/toolkit/global/createProfileWizard.ftl` — Case agreement error: the noun does not take the illative case required by the preceding adjective.
    - Current: `henkilökohtaiseen profiilisi`
    - Source: `{ -brand-short-name } stores information about your settings and preferences in your personal profile.`
    - Suggest: `henkilökohtaiseen profiiliisi`
    - "tallentaa … henkilökohtaiseen profiili-" requires the illative (profiiliisi) to agree with the illative adjective "henkilökohtaiseen"; "profiilisi" is nominative with a possessive suffix and does not agree.
- `webext-perms-description-data-short-personalCommunications` — `toolkit/toolkit/global/extensionPermissions.ftl` — This list item is in the genitive case while every other short-form item in the list is nominative.
    - Current: `henkilökohtaisen yhteydenpidon`
    - Source: `personal communications`
    - Suggest: `henkilökohtainen yhteydenpito`
    - These short forms are joined with Intl.ListFormat into one list (see the section comment and webext-perms-description-data-some); mixing a genitive item into a list of nominatives produces an ungrammatical enumeration.
- _…and 1 more; see `state/` for the full list._

### E. Typography, punctuation & spacing

- `smartwindow-nl-retry-tool-button` — `browser/browser/aiWindowContent.ftl` — Retry button label does not match the wording the instruction text tells the user to look for.
    - Current: `Yritä uudestaan`
    - Source: `label: Retry`
    - Suggest: `Yritä uudelleen`
    - smartwindow-nl-retry-message and smartwindow-nl-retry-group-tabs-message instruct the user to choose "Yritä uudelleen", but this button is labelled "Yritä uudestaan" on the same surface.
- `migration-no-permissions-instructions-step2-2` — `browser/browser/migrationWizard.ftl` — The macOS variant uses straight double quotes but the other variant of the same message uses curly quotes.
    - Current: `"Avaa"`
    - Source: `{$sel_1 ->} [macos] In the file picker, choose “Open” [other] In the file picker, navigate to <code>{ $permissionsPath }</code> and choose “Select”`
    - Suggest: `“Avaa”`
    - The en-US uses curly quotes in both variants, and so does the Finnish 'other' variant (“Valitse”). The macOS variant switches to straight quotes, so the two variants of one message don't match.
- `home-prefs-widgets-header` — `browser/browser/newtab/newtab.ftl` — "Widgets" is left as "Widgetit" here while the whole surface uses "Pienoisohjelmat".
    - Current: `home-prefs-widgets-header =     .label = Widgetit`
    - Source: `label: Widgets`
    - Suggest: `.label = Pienoisohjelmat`
    - Every other occurrence in this file (newtab-spaces-tab-widgets, newtab-custom-widget-section-title, newtab-widget-manage-title, home-prefs-manage-widgets-link "Hallitse pienoisohjelmia") translates Widgets as "Pienoisohjelmat"; this settings header is the lone English-derived outlier, directly above its own "Hallitse pienoisohjelmia" link.
- `newtab-topsites-add-shortcut-label` — `browser/browser/newtab/newtab.ftl` — "Shortcut" rendered as "pikavalinta" while the surrounding Top Sites strings use "oikotie".
    - Current: `newtab-topsites-add-shortcut-label = Lisää pikavalinta`
    - Source: `Add Shortcut`
    - Suggest: `Lisää oikotie`
    - The adjacent headers and menu items all use "oikotie" (newtab-topsites-add-shortcut-header "Uusi oikotie", newtab-topsites-edit-shortcut-header, newtab-menu-add-topsite "Lisää uusi oikotie", home-prefs-shortcuts-header-srd "Oikotiet"), so the add button names the same object differently.
- `desktop-to-mobile-subtitle` — `browser/browser/newtab/onboarding.ftl` — The quoted UI label does not match the button it refers to ("Synkronoi matkapuhelimeen" vs "Synkronoi mobiililaitteeseen").
    - Current: `valitse "Synkronoi matkapuhelimeen"`
    - Source: `Scan the QR code to download { -brand-product-name } for mobile. Once installed, select “Sync to mobile” to access your passwords, bookmarks, and more on the go.`
    - Suggest: `valitse "Synkronoi mobiililaitteeseen"`
    - The string quotes the "Sync to mobile" control, which is localized as "Synkronoi mobiililaitteeseen" in sync-to-mobile-button-label in the same file; the user is told to look for a label that does not exist.
- `places-open-all-in-tabs` — `browser/browser/places.ftl` — "Open All in Tabs" drops "all", unlike the parallel Synced Tabs string.
    - Current: `Avaa välilehtiin`
    - Source: `accesskey: O label: Open All in Tabs`
    - Suggest: `Avaa kaikki välilehtiin`
    - syncedTabs.ftl's synced-tabs-context-open-all-in-tabs (whose comment says it must match the places.ftl bookmarks-manager wording) reads "Avaa kaikki välilehtiin"; the places entry omits "kaikki", so the two menus that are required to match differ.
- `safeb-blocked-unwanted-page-title` — `browser/browser/safebrowsing/blockedSite.ftl` — "harmful programs" rendered as "haittaohjelmia" (malware), duplicating the malware title and conflicting with the body strings.
    - Current: `Edessä olevalla sivustolla voi olla haittaohjelmia`
    - Source: `The site ahead may contain harmful programs`
    - Suggest: `Edessä olevalla sivustolla voi olla haitallisia ohjelmia`
    - en-US distinguishes "harmful programs" (unwanted) from "malware" (harmful); the Finnish uses "haittaohjelmia" for both titles, and the matching body strings for this category correctly say "haitallisia ohjelmia".
- `sidebar-widget-expand-sidebar2` — `browser/browser/sidebar.ftl` — "sidebar" rendered as "sivupalkki" in the toolbar widget tooltips while the whole surface otherwise uses "sivupaneeli".
    - Current: `Laajenna sivupalkki ({ $shortcut })`
    - Source: `label: Sidebars tooltiptext: Expand sidebar ({ $shortcut })`
    - Suggest: `Laajenna sivupaneeli ({ $shortcut })`
    - Everywhere else in this file (including this widget's own .label "Sivupaneelit", sidebar-resize-splitter, sidebar-context-menu-hide-sidebar) "sidebar" is "sivupaneeli"; only the four sidebar-widget-* tooltips (expand/collapse/show/hide) say "sivupalkki", so the same control uses two terms at once.
- `searchWithHeader` — `browser/chrome/browser/search.properties` — "Search with:" uses "palvelulla" while the paired string uses "hakukoneella", against the developer comment.
    - Current: `Hae palvelulla:`
    - Source: `Search with:`
    - Suggest: `Hae hakukoneella:`
    - The comment says the wording should be as close as possible to searchForSomethingWith2, which renders the same "with" as "hakukoneella"; the two headers appear in the same panel.
- `cspBlocked` — `browser/chrome/overrides/appstrings.properties` — "content security policy" rendered as "sisällön tietosuojakäytäntö" (privacy policy) instead of a security policy.
    - Current: `sisällön tietosuojakäytäntö`
    - Source: `This page has a content security policy that prevents it from being loaded in this way.`
    - Suggest: `sisällön turvallisuuskäytäntö`
    - "tietosuoja" means data protection/privacy, not security; CSP is a security mechanism, and the neighbouring strings in the same file use "turvallisuus-" for security concepts.
- `PRIVATE_BROWSING_SHORTCUT_TITLE` — `browser/installer/custom.properties` — Does not match the required browser.ftl string: lowercase "yksityinen selaus" vs "Yksityinen selaus".
    - Current: `$BrandShortName - yksityinen selaus`
    - Source: `$BrandShortName Private Browsing`
    - Suggest: `$BrandShortName - Yksityinen selaus`
    - The developer comment states the non-variable portion MUST match private-browsing-shortcut-text-2 in browser.ftl, which reads "{ -brand-shortcut-name } - Yksityinen selaus".
- `styleeditor-no-stylesheet-tip` — `devtools/client/styleeditor.ftl` — `styleeditor-no-stylesheet-tip` uses a straight apostrophe
    - Current: `Perhaps you'd like to <a data-l10n-name="append-new-stylesheet">append a new style sheet</a>?`
    - Source: `Perhaps you’d like to <a data-l10n-name="append-new-stylesheet">append a new style sheet</a>?`
    - The tree uses ’ 148 times against 33 straight.
- `FullscreenDeniedContainerNotAllowed` — `dom/chrome/dom/dom.properties` — `FullscreenDeniedContainerNotAllowed` uses a straight apostrophe
    - Current: `Request for fullscreen was denied because at least one of the document's containing elements is not an iframe or does not have an "allowfullscreen" attribute.`
    - Source: `Request for fullscreen was denied because at least one of the document’s containing elements is not an iframe or does not have an “allowfullscreen” attribute.`
    - The tree uses ’ 148 times against 33 straight.
- `ManifestInvalidType` — `dom/chrome/dom/dom.properties` — `ManifestInvalidType` uses a straight apostrophe
    - Current: `Expected the %1$S's %2$S member to be a %3$S.`
    - Source: `Expected the %1$S’s %2$S member to be a %3$S.`
    - The tree uses ’ 148 times against 33 straight.
- `ResponseTypeSyncXHRWarning` — `dom/chrome/dom/dom.properties` — `ResponseTypeSyncXHRWarning` uses a straight apostrophe
    - Current: `Use of XMLHttpRequest's responseType attribute is no longer supported in the synchronous mode in window context.`
    - Source: `Use of XMLHttpRequest’s responseType attribute is no longer supported in the synchronous mode in window context.`
    - The tree uses ’ 148 times against 33 straight.
- `TargetPrincipalDoesNotMatch` — `dom/chrome/dom/dom.properties` — `TargetPrincipalDoesNotMatch` uses a straight apostrophe
    - Current: `Failed to execute 'postMessage' on 'DOMWindow': The target origin provided ('%S') does not match the recipient window's origin ('%S').`
    - Source: `Failed to execute ‘postMessage’ on ‘DOMWindow’: The target origin provided (‘%S’) does not match the recipient window’s origin (‘%S’).`
    - The tree uses ’ 148 times against 33 straight.
- `TimeoutSyncXHRWarning` — `dom/chrome/dom/dom.properties` — `TimeoutSyncXHRWarning` uses a straight apostrophe
    - Current: `Use of XMLHttpRequest's timeout attribute is not supported in the synchronous mode in window context.`
    - Source: `Use of XMLHttpRequest’s timeout attribute is not supported in the synchronous mode in window context.`
    - The tree uses ’ 148 times against 33 straight.
- `IneligibleResource` — `dom/chrome/security/security.properties` — `IneligibleResource` uses a straight apostrophe
    - Current: `"%1$S" is not eligible for integrity checks since it's neither CORS-enabled nor same-origin.`
    - Source: `“%1$S” is not eligible for integrity checks since it’s neither CORS-enabled nor same-origin.`
    - The tree uses ’ 148 times against 33 straight.
- `headerFooterCustom` — `toolkit/chrome/global/printdialog.properties` — `headerFooterCustom` uses three dots where this locale uses …
    - Current: `Oma...`
    - Source: `Custom…`
    - The tree uses … 399 times against 1 ASCII runs.
- `addon-category-dictionary` — `toolkit/toolkit/about/aboutAddons.ftl` — “Dictionaries” rendered as “Oikoluvut” while the rest of the page uses “sanastot”.
    - Current: `Oikoluvut`
    - Source: `Dictionaries`
    - Suggest: `Sanastot`
    - The same add-on type is called “sanastot” in list-empty-get-dictionaries-message and dictionary-heading (“Sanastojen hallinta”); “Oikoluvut” means “spell checks”, so the sidebar category and the page heading it opens do not match.
- `about-webrtc-dropped-frames-label` — `toolkit/toolkit/about/aboutWebrtc.ftl` — Video frames called “kehykset” here but “ruudut” elsewhere on the same page.
    - Current: `Pudotetut kehykset:`
    - Source: `Dropped frames:`
    - Suggest: `Pudotetut ruudut:`
    - The same page renders “frames” as “ruutu(a)” in about-webrtc-frames, about-webrtc-consecutive-frames and the frame-timestamp labels; “kehys” means a border/frame and is used for subframes elsewhere in the tree, so it is the wrong member of the pair here.
- `user-context-color-purple` — `toolkit/toolkit/global/contextual-identity.ftl` — "Purple" and "Violet" are both labelled "Violetti", so two selectable colour swatches have identical names.
    - Current: `Violetti`
    - Source: `label: Purple`
    - Suggest: `Purppura`
    - user-context-color-purple and user-context-color-violet are distinct swatches in the container colour picker; giving both the label "Violetti" makes them indistinguishable to users and to screen readers.
- `region-name-bv` — `toolkit/toolkit/intl/regionNames.ftl` — `region-name-bv` uses a straight apostrophe
    - Current: `Bouvet'nsaari`
    - Source: `Bouvet Island`
    - The tree uses ’ 148 times against 33 straight.
- `cert-error-unknown-critical-extension` — `toolkit/toolkit/neterror/certError.ftl` — A certificate "extension" is rendered as "pääte" (suffix/file extension) instead of "laajennus".
    - Current: `ei-tuetun kriittisen päätteen`
    - Source: `{ -brand-short-name } blocked your visit to this site because the certificate provided for { $hostname } contains an unsupported critical extension.`
    - Suggest: `ei-tuetun kriittisen laajennuksen`
    - The immediately following string cert-error-extension-value-invalid translates the same en-US term "extension" as "laajennus"; "pääte" means a suffix or terminal and is wrong for an X.509 certificate extension.
- `certerror-mitm-what-can-you-do-about-it-attack` — `toolkit/toolkit/neterror/netError.ftl` — "attack" is rendered as "huijaus" (a scam/hoax) here, while the parallel -sts string uses "hyökkäys".
    - Current: `kyseessä voi olla huijaus`
    - Source: `If you are not familiar with <b>{ $mitm }</b>, then this could be an attack and you should not continue to the site.`
    - Suggest: `kyseessä voi olla hyökkäys`
    - The en-US of both strings says "this could be an attack"; certerror-mitm-what-can-you-do-about-it-attack-sts correctly uses "hyökkäys", so the same warning on the same page names two different things.

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/fi/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

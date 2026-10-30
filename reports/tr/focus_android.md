# Focus for Android l10n QA — tr

| | |
|---|---|
| **Generated** | 2026-10-30 |
| **Locale tree** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **en-US reference** | `https://github.com/mozilla-l10n/android-l10n` @ `f1e4f5447b8d` |
| **Previous run** | 2026-10-26 @ `f1e4f5447b8d` |
| **Mode** | checks-only |
| **Strings reviewed this run** | 0 of 250 |

Findings are keyed by string id, never by line number. The locale is assessed against its source only.

> **The reviewer did not run for this report.** Only the deterministic checks were applied; no string was read. The absence of a finding here means nothing has looked, not that there is nothing to find.

Also for tr: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| Files | 1 |
| Strings | 250 |
| Missing strings | 0 |
| Obsolete strings | 0 |
| Files absent from the locale | 0 |
| Files with no en-US counterpart | 0 |
| Fluent / properties syntax errors | 0 |
| Reference files that did not parse | 0 |
| Android escaping (apostrophes, quotes, ampersands) | 0 |
| printf placeholder mismatches | 0 |
| Text quoting a UI label that no longer matches | 0 |
| Source-language spellings left unchanged | 0 |
| Markup & `data-l10n-name` defects | 0 |
| Typography deviations from this locale's own norm | 0 |

### Completeness

The locale is complete against the en-US source.

### Conventions detected in this locale

Counted over the whole tree. Checks flag deviations from the locale's **own** majority, so a convention that reads _mixed_ produces no findings at all.

The count includes Firefox for Android's strings for this locale, which the same team translates, so both projects infer the same conventions. Nothing there is checked here.

| Convention | Counts | Inferred |
|---|---|---|
| quotes | `curly-double` 14, `straight-double` 2 | **curly-double** |
| apostrophe | `typographic` 153, `straight` 1 | **typographic** |
| ellipsis | `char` 21 | **char** |
| register | `informal` 2, `formal` 18 | **formal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (17)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 8 |
| 3 | Degraded language (grammar, spelling, terminology) | 9 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `menu_custom_tab_branding` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — The "Powered by" wording is dropped, leaving only the app name placeholder.
    - Current: `%1$s`
    - Source: `Powered by %1$s`
    - Suggest: `%1$s tarafından destekleniyor`
    - Source "Powered by %1$s" conveys branding attribution; the translation omits the entire phrase.
- `menu_open_with_a_browser2` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Open in…" translated as "Birlikte aç…" (Open with…), inconsistent with menu_open_with_default_browser2 phrasing.
    - Current: `Birlikte aç…`
    - Source: `Open in…`
    - Suggest: `Şununla aç…`
    - "Birlikte aç" is ungrammatical on its own (it means "open together"); the sibling string uses "%1$s ile aç", so the generic form should be "Şununla aç…".
- `menu_remove_from_shortcuts` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Menu action label translated as a past-tense statement ("Removed from shortcuts") instead of the imperative action "Remove from Shortcuts".
    - Current: `Kısayollardan kaldırıldı`
    - Source: `Remove from Shortcuts`
    - Suggest: `Kısayollardan kaldır`
    - Source is a menu item action "Remove from Shortcuts"; the Turkish reads "was removed from shortcuts", a status message, and is inconsistent with the paired "Kısayollara ekle".
- `preference_default_browser2` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Translation adds the possessive "my" not present in the source ("default browser" becomes "varsayılan tarayıcım").
    - Current: `varsayılan tarayıcım yap`
    - Source: `Make %1$s default browser`
    - Suggest: `varsayılan tarayıcı yap`
    - The source is "Make %1$s default browser", with no first-person possessive.
- `preference_mozilla_telemetry_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — The translation drops "to provide" and "for everyone" from the source sentence.
    - Current: `Mozilla, yalnızca %1$s’u daha da geliştirmek için ihtiyaç duyduğumuz verileri toplar.`
    - Source: `Mozilla strives to collect only what we need to provide and improve %1$s for everyone.`
    - Suggest: `Mozilla, %1$s uygulamasını herkese sunmak ve geliştirmek için yalnızca ihtiyaç duyduğumuz verileri toplamaya çalışır.`
    - Source: "Mozilla strives to collect only what we need to provide and improve %1$s for everyone." The Turkish omits "provide" and "for everyone" and turns "strives to collect" into a flat "collects".
- `preference_privacy_block_ads_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Meaning shifted: source says ads track site visits, translation says ads track the sites you visit.
    - Current: `Bazı reklamlar, siz onlara tıklamasanız bile ziyaret ettiğiniz siteleri takip eder`
    - Source: `Some ads track site visits, even if you don’t click the ads`
    - Suggest: `Bazı reklamlar, siz onlara tıklamasanız bile site ziyaretlerinizi takip eder`
    - "track site visits" refers to the visits themselves, not to the sites; the current wording changes the object of tracking.
- `preference_privacy_block_analytics_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "collect" rendered as "kaydetmek" (record) instead of "toplamak" (collect).
    - Current: `kaydetmek, çözümlemek ve ölçmek`
    - Source: `Used to collect, analyze and measure activities like tapping and scrolling`
    - Suggest: `toplamak, çözümlemek ve ölçmek`
    - Source says "collect, analyze and measure"; "kaydetmek" means "to record/save", not "to collect".
- `preference_privacy_block_social_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — The social tracker summary is mistranslated and reverses the meaning of the source.
    - Current: `Sosyal medyada paylaşım düğmeleri, ziyaret ettiğiniz siteleri de takip eder`
    - Source: `Embedded on sites to track your visits and to display functionality like share buttons`
    - Suggest: `Ziyaretlerinizi izlemek ve paylaşım düğmeleri gibi işlevler sunmak için sitelere yerleştirilir`
    - The source says these trackers are embedded on sites to track your visits and to display functionality like share buttons; the Turkish instead claims that share buttons on social media also track the sites you visit.
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Source says the browser cannot restore "this tab" (singular); the translation generalizes it to "your tabs" plural.
    - Current: `sekmelerinizi asla kaydetmediğimiz için geri getirmemiz de mümkün değil`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `bu sekmeyi asla kaydetmediğimiz için geri getirmemiz de mümkün değil`
    - en-US: "we never save and cannot restore this tab" refers to the specific crashed tab, not all tabs.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_security_bad_cert_techInfo` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Typo: "doğu" instead of "doğru".
    - Current: `sunucu doğu ara sertifikaları göndermiyor`
    - Source: `{ <label> }Someone could be trying to impersonate the site and continuing could be risky.{ </label> } { <br> }{ <br> } { <label> }%1$s does not trust { <b> }%2$s{ </b> } because its certificate issuer is unknown, the ce…`
    - Suggest: `sunucu doğru ara sertifikaları göndermiyor`
    - "correct intermediate certificates" should be "doğru ara sertifikalar"; "doğu" means "east" and is a misspelling.
- `preference_show_search_suggestions_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Mixed person: informal "yazdıklarını" with formal "arama motorunuza" in the same sentence.
    - Current: `%1$s, adres çubuğuna yazdıklarını arama motorunuza gönderecektir`
    - Source: `%1$s will send what you type in the address bar to your search engine`
    - Suggest: `%1$s, adres çubuğuna yazdıklarınızı arama motorunuza gönderecektir`
    - Source is "what you type"; the Turkish switches between informal and formal second person within one string, which is inconsistent and ungrammatical in agreement.
- `tool_tip_message` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — Wrong case suffix: "ihtiyaçlarınızı göre" should be "ihtiyaçlarınıza göre".
    - Current: `ihtiyaçlarınızı göre`
    - Source: `These default settings offer strong protection. But it’s easy to tweak the settings to meet your specific needs.`
    - Suggest: `ihtiyaçlarınıza göre`
    - The postposition "göre" requires the dative case (-a/-e), not the accusative; "ihtiyaçlarınızı göre" is ungrammatical.

### D. Terminology, register & consistency

- `preference_autocomplete_menu_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Remove" is translated as "Sil" (delete) instead of "Kaldır".
    - Current: `Sil`
    - Source: `Remove`
    - Suggest: `Kaldır`
    - The source distinguishes Remove from Delete; Turkish standard for "Remove" is "Kaldır", and "Sil" means "Delete".
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — "Remove custom URLs" rendered with "sil" (delete) instead of "kaldır".
    - Current: `Özel adresleri sil`
    - Source: `Remove custom URLs`
    - Suggest: `Özel adresleri kaldır`
    - Source says "Remove"; Turkish equivalent is "kaldır", while "sil" corresponds to "delete".
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — First-person possessive "parmak izimi" breaks the formal second-person register used elsewhere.
    - Current: `Uygulama kilidini açmak için parmak izimi kullan`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `Uygulama kilidini açmak için parmak izini kullan`
    - The source is a neutral setting title ("Use fingerprint to unlock app"); the locale convention is formal address, not first-person "my fingerprint".
- `preference_security_biometric_summary2` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — First-person "eklediysem" contradicts the second-person source and the formal register.
    - Current: `Kısayollar eklediysem veya %s tarayıcısında bir web sitesi açıksa kilidi parmak iziyle aç.`
    - Source: `Unlock using fingerprint if you’ve added Shortcuts or when a website is already open in %s.`
    - Suggest: `Kısayollar eklediyseniz veya %s tarayıcısında bir web sitesi açıksa kilidi parmak iziyle açın.`
    - The source uses second person ("if you’ve added Shortcuts"); the tr tree convention is formal second-person address.
- `preference_switch_autocomplete_user_list` — `mozilla-mobile/focus-android/app/src/main/res/values-tr/strings.xml` — First-person "Eklediğim" instead of second-person address used in the source.
    - Current: `Eklediğim sitelerde`
    - Source: `For sites you add`
    - Suggest: `Eklediğiniz sitelerde`
    - Source is "For sites you add"; the locale convention is formal second-person address, not first person.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/tr/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

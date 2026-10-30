# Focus for Android l10n QA — es-AR

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

Also for es-AR: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `curly-double` 15 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| inverted marks | `open-question` 107, `open-exclamation` 26 | **open-question** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (13)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 3 |
| 3 | Degraded language (grammar, spelling, terminology) | 10 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `cfr_for_toolbar_shield_icon2` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "site" is translated as "página web" (web page) while the rest of the file uses "sitio web", and "any time" is dropped.
    - Current: `Evitamos que esta página web te espíe. Presioná el escudo para ver lo que estamos bloqueando.`
    - Source: `Got ‘em! We stopped this site from spying on you. Tap the shield any time to see what we’re blocking.`
    - Suggest: `Evitamos que este sitio web te espíe. Presioná el escudo en cualquier momento para ver lo que estamos bloqueando.`
    - The source says "this site" (elsewhere rendered "sitio web", e.g. content_description_reload) and "Tap the shield any time"; the time qualifier is omitted.
- `preference_autocomplete_title_remove` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Plural "custom URLs" rendered as singular.
    - Current: `Borrar URL personalizada`
    - Source: `Remove custom URLs`
    - Suggest: `Borrar URL personalizadas`
    - The source is "Remove custom URLs" (plural, screen for removing multiple URLs), but the target reads as a single URL, identical in form to the singular add-title string.
- `preference_category_switching_apps` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Switching Apps" (changing between apps) is rendered as "Intercambio de aplicaciones" (exchange of apps).
    - Current: `Intercambio de aplicaciones`
    - Source: `Switching Apps`
    - Suggest: `Cambio entre aplicaciones`
    - The developer comment says the category covers stealth settings while switching between apps, not exchanging apps.
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Regulation (EU)" is rendered as "Regulación (EU)" instead of the official Spanish name "Reglamento (UE)".
    - Current: `la Regulación (EU) 2024/1183`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `el Reglamento (UE) 2024/1183`
    - The EU legal instrument "Regulation" is officially "Reglamento" in Spanish and the country code is "UE", not "EU"; the current text names the instrument incorrectly.

### C. Grammar, agreement & spelling

- `mozac_browser_errorpages_security_bad_cert_message` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Ésto" is misspelled; the neuter demonstrative "esto" never takes an accent.
    - Current: `Ésto podría ser un problema`
    - Source: `This could be a problem with the server’s configuration, or it could be someone trying to impersonate the server. { <br/> }{ <br/> } If you’ve connected to this server successfully in the past, the error may be temporar…`
    - Suggest: `Esto podría ser un problema`
    - Per RAE, the neuter demonstrative pronoun "esto" is never accented.
- `preference_security_biometric` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Extra preposition "de" makes the phrase ungrammatical.
    - Current: `Usar la huella digital de para desbloquear la aplicación`
    - Source: `Use fingerprint to unlock app`
    - Suggest: `Usar la huella digital para desbloquear la aplicación`
    - Source is "Use fingerprint to unlock app"; the stray "de" before "para" is a typo.

### D. Terminology, register & consistency

- `placeholder_rename_top_site` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Shortcut" is rendered as "atajo" here but as "acceso directo" in menu_remove_from_shortcuts on the same surface.
    - Current: `Nombre del atajo`
    - Source: `Shortcut name`
    - Suggest: `Nombre del acceso directo`
    - Inconsistent terminology for the same source term "Shortcut" within the same app/feature (shortcuts on the home screen).
- `preference_autocomplete_add_error` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses "usted" form while the surrounding autocomplete strings use the "vos/tú" informal form required for es-AR.
    - Current: `Verifique la URL que escribió.`
    - Source: `Double-check the URL you entered.`
    - Suggest: `Verificá la URL que escribiste.`
    - Neighboring strings (preference_autocomplete_explanation_text "Tu lista", preference_autocomplete_user_list_summary2 "tus URLs") use informal address; this string switches to formal register, an inconsistency on the same surface.
- `preference_autocomplete_add_hint` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Formal "usted" imperative conflicts with the informal register used in the same settings screen.
    - Current: `Pegue o escriba una URL`
    - Source: `Paste or enter URL`
    - Suggest: `Pegá o escribí una URL`
    - The same autocomplete screen addresses the user informally ("Tu lista de autocompletado", "tus URLs favoritas"); this hint uses the formal form.
- `preference_category_tracking_protection3` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Enhanced Tracking Protection" uses a non-standard rendering instead of the established Mozilla term.
    - Current: `Protección de rastreo aumentada`
    - Source: `Enhanced Tracking Protection`
    - Suggest: `Protección contra el rastreo mejorada`
    - Mozilla's established es-AR term for Enhanced Tracking Protection is "Protección contra el rastreo mejorada"; "aumentada" is inconsistent terminology.
- `preference_switch_autocomplete_user_list` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses "usted" verb form instead of the voseo/tuteo register used elsewhere in es-AR.
    - Current: `Para los sitios que agrega`
    - Source: `For sites you add`
    - Suggest: `Para los sitios que agregás`
    - The es-AR locale addresses the user with voseo (e.g. "Te dejaremos con tu navegación privada... podés" in promote_search_widget_dialog_subtitle); "agrega" is the usted form and breaks the established form of address.
- `shortcut_erase_and_open_short_label` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — "Erase" is translated as "Eliminar" here while the parallel erase shortcut strings use "Borrar".
    - Current: `Eliminar y abrir`
    - Source: `Erase & open`
    - Suggest: `Borrar y abrir`
    - shortcut_erase_short_label renders "Erase" as "Borrar"; using "Eliminar" for the same source term in the same shortcut group is inconsistent.
- `tab_crash_report_headline` — `mozilla-mobile/focus-android/app/src/main/res/values-es-rAR/strings.xml` — Uses the formal "usted" imperative "Disculpe" while the locale's established address form is voseo/tuteo (used elsewhere in this batch: "Conseguí", "tus necesidades", "¡Estás protegido!").
    - Current: `Disculpe.`
    - Source: `Sorry. We’re having a problem with this tab.`
    - Suggest: `Disculpá.`
    - Register inconsistency: es-AR Focus strings address the user informally (voseo), e.g. "Conseguí acceso…", "¡Estás protegido!"; this string switches to formal usted.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/es-AR/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (0)

_Nothing fixed yet._

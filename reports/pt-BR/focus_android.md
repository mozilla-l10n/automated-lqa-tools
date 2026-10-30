# Focus for Android l10n QA — pt-BR

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

Also for pt-BR: [Firefox for Android](android.md) · [Firefox](firefox.md) · [Firefox iOS](firefox_ios.md)

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
| quotes | `curly-double` 14 | **curly-double** |
| ellipsis | `char` 21 | **char** |
| register | `informal` 229 | **informal** |

---

## 2. Systemic items (decisions, not line items)

_Nothing reported._

---

## 3. Open findings (11)


| Impact | Meaning | Count |
|---|---|---|
| 1 | Broken output (blank value, broken markup, wrong variable) | 0 |
| 2 | Wrong content (says something other than the English) | 7 |
| 3 | Degraded language (grammar, spelling, terminology) | 4 |
| 4 | Cosmetic (typography, spacing) | 0 |

### A. Functional, markup, variables & plurals

_Nothing in this category._

### B. Mistranslation, reversed meaning, wrong names & brand

- `exit_fullscreen_with_back_button_short` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — Translation exceeds the 68-character limit stated in the developer comment and adds text not in the source.
    - Current: `Deslize do topo para baixo e toque em Voltar para sair de tela inteira`
    - Source: `Drag from top & press back to exit`
    - Suggest: `Deslize do topo e toque em Voltar para sair`
    - The developer comment says the text should be as short as possible, max 68 chars; the current string is 70 characters and adds "de tela inteira", which is not in the source "Drag from top & press back to exit".
- `menu_add_to_home_screen` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — "Add to Home screen" is rendered as "Adicionar à tela do dispositivo", losing the "home screen" reference and conflicting with the same term elsewhere.
    - Current: `Adicionar à tela do dispositivo`
    - Source: `Add to Home screen`
    - Suggest: `Adicionar à tela inicial`
    - The source and developer comment refer to the device's home screen (launcher); firstrun_shortcut_text already translates "Add to Home screen" as "Adicionar à tela inicial", so this is both inaccurate and inconsistent.
- `preference_https_only_summary3` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — The adverb "automatically" was moved so it modifies "using" instead of "attempts to connect".
    - Current: `Tenta se conectar com sites usando automaticamente o protocolo de criptografia HTTPS`
    - Source: `Automatically attempts to connect to sites using the HTTPS encryption protocol for increased security.`
    - Suggest: `Tenta se conectar automaticamente com sites usando o protocolo de criptografia HTTPS`
    - In the source, "Automatically attempts to connect" — the automation applies to the connection attempt, not to the use of the protocol.
- `preference_phone_feature_media_key_system_access` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — "DRM-controlled content" is rendered as "conteúdo controlado por direitos autorais", dropping the DRM term and saying "copyright-controlled" instead.
    - Current: `Conteúdo controlado por direitos autorais`
    - Source: `DRM-controlled content`
    - Suggest: `Conteúdo controlado por DRM`
    - The source refers specifically to DRM (digital rights management) content, not to copyright control; the established Mozilla term is "controlado por DRM".
- `preference_privacy_block_content` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — "other content trackers" loses "content" in the translation.
    - Current: `Bloquear outros rastreadores`
    - Source: `Block other content trackers`
    - Suggest: `Bloquear outros rastreadores de conteúdo`
    - The source specifies content trackers, distinguishing this option from the ad, analytics and social tracker settings.
- `preference_show_search_suggestions_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — Translation adds a conditional clause and "escolhido" not present in the source.
    - Current: `Se ativar, o %1$s envia o que você escreve na barra de endereços para o mecanismo de pesquisa escolhido.`
    - Source: `%1$s will send what you type in the address bar to your search engine`
    - Suggest: `O %1$s envia o que você digitar na barra de endereços para seu mecanismo de pesquisa`
    - Source states "%1$s will send what you type in the address bar to your search engine" with no "if enabled" condition and no "chosen" qualifier.
- `search_add_error_empty_search` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — "Search string" is rendered as "código de pesquisa" (search code), which is wrong and inconsistent with other strings that use "termo de pesquisa".
    - Current: `Digite um código de pesquisa`
    - Source: `Enter search string`
    - Suggest: `Digite o termo de pesquisa`
    - The source says "search string", not "search code"; the related string search_add_manually_string translates it as "Termo de pesquisa".
- `tab_crash_report_description` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — First-person plural "we never save" was changed to third person "ele nunca salva", shifting the subject.
    - Current: `Sendo um navegador privativo, ele nunca salva e não pode restaurar esta aba.`
    - Source: `As a private browser, we never save and cannot restore this tab.`
    - Suggest: `Por ser um navegador privativo, nunca salvamos e não podemos restaurar esta aba.`
    - The source says "we never save and cannot restore this tab"; the translation attributes the action to the browser instead of to us.

### C. Grammar, agreement & spelling

- `preference_safe_browsing_summary` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — Redundant/incorrect wording "com contendo" in the safe browsing summary.
    - Current: `sites com contendo software indesejado`
    - Source: `Block reported deceptive and attack sites, malware sites, and unwanted software sites.`
    - Suggest: `sites com software indesejado`
    - "com contendo" is ungrammatical; the source reads "unwanted software sites".
- `qualified_text` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — The EU abbreviation is written "EU" instead of the Portuguese "UE" in the regulation reference.
    - Current: `Regulamento (EU) 2024/1183`
    - Source: `Qualified as specified in Regulation (EU) 2024/1183.`
    - Suggest: `Regulamento (UE) 2024/1183`
    - In Portuguese the European Union regulation designation is "(UE)"; "EU" is the English abbreviation and in pt means "I".

### D. Terminology, register & consistency

- `search_add_error_format` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — "search string" translated as "código de pesquisa", inconsistent with "termo de pesquisa" used elsewhere.
    - Current: `código de pesquisa`
    - Source: `Check that search string matches Example format`
    - Suggest: `termo de pesquisa`
    - Same source term "search string" is rendered as "termo de pesquisa" in search_add_manually_string; "código" (code) is not the meaning.

### E. Typography, punctuation & spacing

_Nothing in this category._

---

## 4. Appendix

### Dismissed by hand (0)

_Nothing dismissed._

_One line each in `locales/pt-BR/dismissed.txt`. Delete the line and the finding returns._

### Suppressed as false positives (0)

_No suppression rules have matched._

### Withdrawn to date (0)

_Nothing withdrawn._

_A finding is withdrawn when a check stops raising it while the string itself never changed: the check was wrong, not the translation. Kept separate from fixes so the fixed count stays honest._

### Fixed to date (1)

- `search_add_manually_example` — `mozilla-mobile/focus-android/app/src/main/res/values-pt-rBR/strings.xml` — fixed 2026-10-18

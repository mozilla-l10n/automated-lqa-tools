# Firefox for iOS — l10n QA

- **Generated:** 2026-09-10
- **Locales tracked:** 20 (20 with recorded state)
- **Findings:** 1,325 raised, 38 fixed (2%), 1,220 open
- **Closed by a person:** 14 dismissed, 52 suppressed by rule

Counts come from `state/`, not from the rendered reports, so they always reflect what the pipeline recorded.

## Read these first

### Reads as a deliberate edit (2)

The translation makes the product assert something the en-US never said. Nothing here says the change was intended — that cannot be read off the text, which is exactly the problem, because a user cannot read it off either.

- **`hi-IN`** `NSMicrophoneUsageDescription` — `Client/en-US.lproj/InfoPlist.strings`
    - Microphone permission description translated as taking and uploading videos, omitting Firefox and the microphone/audio recording purpose.
    - Current: `यह आपको वीडियो लेने और अपलोड करने देता है।`
    - Suggest: `Firefox ऑडियो रिकॉर्ड करने और अपलोड करने के लिए आपके माइक्रोफ़ोन का उपयोग करता है।`
- **`hi-IN`** `Oops! Firefox crashed` — `Shared/en-US.lproj/Localizable.strings`
    - "crashed" is rendered as "नष्ट हो गया" (was destroyed), which is not the software sense of crashing.
    - Current: `उफ़! Firefox नष्ट हो गया`
    - Suggest: `उफ़! Firefox क्रैश हो गया`

### Broken output — impact 1 (0)

_Nothing open at impact 1._

### Wrong content — impact 2 (677)

Too many to list here; the per-locale counts are in the table below and every one of them is in `reports/<locale>/firefox_ios.md`.

| Locale | Last run | Mode | Commit | Strings | Missing | Open | Impact 1–2 | Fixed | Dismissed | Suppressed |
|---|---|---|---|---|---|---|---|---|---|---|
| [cs](cs/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **65** | 42 | 0 | 0 | 0 |
| [de](de/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **74** | 31 | 2 | 0 | 0 |
| [en-CA](en-CA/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,912 | 10 | **0** | 0 | 16 | 0 | 0 |
| [en-GB](en-GB/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **0** | 0 | 3 | 0 | 50 |
| [es-AR](es-AR/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **85** | 36 | 0 | 0 | 0 |
| [es-ES](es-ES/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **51** | 27 | 0 | 0 | 0 |
| [es-MX](es-MX/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,884 | 38 | **114** | 64 | 1 | 0 | 0 |
| [fr](fr/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,920 | 2 | **45** | 30 | 0 | 0 | 0 |
| [hi-IN](hi-IN/firefox_ios.md) | 2026-09-10 | baseline | `4e8024d2` | 602 | 1,320 | **79** | 33 | 0 | 0 | 0 |
| [hu](hu/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,916 | 6 | **80** | 40 | 0 | 0 | 0 |
| [id](id/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **91** | 40 | 0 | 0 | 0 |
| [it](it/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **0** | 0 | 16 | 14 | 2 |
| [ja](ja/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **116** | 77 | 0 | 0 | 0 |
| [nl](nl/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,918 | 4 | **43** | 25 | 0 | 0 | 0 |
| [pl](pl/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **45** | 32 | 0 | 0 | 0 |
| [pt-BR](pt-BR/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,916 | 6 | **46** | 31 | 0 | 0 | 0 |
| [ru](ru/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **76** | 47 | 0 | 0 | 0 |
| [sl](sl/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,917 | 5 | **74** | 40 | 0 | 0 | 0 |
| [tr](tr/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,922 | 0 | **78** | 45 | 0 | 0 | 0 |
| [zh-CN](zh-CN/firefox_ios.md) | 2026-09-07 | incremental | `386c3ca4` | 1,839 | 83 | **58** | 37 | 0 | 0 | 0 |

**Impact 1–2** is the queue that matters: broken output and wrong content. Impact 3–4 is language polish and typography.

## Adding a locale

Add its code to `firefox_ios/config.yaml` and run the workflow. The first run has no stored state, so it takes the from-scratch baseline path over the whole tree; every run after that reviews only what changed.

## Flagging a false positive

Write a rule in `firefox_ios/locales/<code>/suppressions.yaml`, or better, a sentence in `firefox_ios/locales/<code>/conventions.md`. Both are re-applied to the entire backlog on the next run, so a rule added today retires findings raised months ago. See `docs/suppressions.md`.

# Firefox l10n review & fix — the manual runbook

> **This document is history and reference, not the operating procedure.**
>
> It is the hand-driven process that the fourteen locale reviews of July and
> August 2026 followed, and that `firefox/tools/` now automates. It is kept
> because it explains *why* the automation is shaped the way it is: which
> checks matter, which are worthless, how a locale's typographic conventions
> have to be measured rather than assumed, and how findings should be
> reported.
>
> Where the two disagree, the code is authoritative. In particular the
> automation fixes three bugs this runbook's own scripts had:
>
> * `vars_of()` here subtracts `msg.declarations`, which removes the
>   selector variable and both hides real selector mismatches and invents
>   phantom ones — see `_vars()` and `check_selectors()` in `tools/checks.py`;
> * the `<\w+>` reading of markup treats angle-bracket *text* like
>   `<anonymous>` in the legacy `.properties` files as an unclosed tag — see
>   `KNOWN_TAGS` in `tools/checks.py`;
> * "fixed" was decided by "did the string change at all", which a Pontoon
>   sync satisfies for unrelated reasons — see `resolve()` in
>   `tools/findings.py`.
>
> Sections 1 and 2 map onto `tools/checks.py` and the two `tools/llm_*.py`
> reviewers; section 3 onto `tools/report.py`. Section 4 (applying fixes) is
> deliberately **not** automated: this system reports, it does not edit
> locale files.

---

## 0. Inputs & setup

You need two directory trees with **matching relative paths**:

- **`L10N`** — the locale's Fluent tree (e.g. `.../firefox-l10n/<locale>`).
- **`REF`** — the **en-US reference** with the same layout. In the `firefox-l10n` world this is the *source-strings* repo (the "quarantine"/source export), NOT en-US inside the l10n repo.

```bash
export L10N=~/mozilla/git/firefox-l10n/<locale>       # e.g. .../de, .../es-MX
export REF=~/mozilla/git/firefox-quarantine           # en-US source, same relative paths
```

**Different repo / project?** The only hard requirement is that `REF` mirrors `L10N`'s relative `.ftl` paths.
- From `firefox-l10n`: `REF` = the source repo (mozilla-l10n/firefox-l10n *source*). Locales are top-level dirs; pull it first (`git pull`) so you review current strings.
- From `mozilla-central`/gecko: en-US lives split across `browser/locales/en-US/…`, `toolkit/locales/en-US/…`, etc. Assemble a `REF` whose layout matches the locale tree (or use a `l10n.toml` with `compare-locales`). If paths can't be aligned, the ID-diff and per-file steps below still work file-by-file; only the bulk tools need aligned paths.

**Tooling — `moz.l10n`** (provides `l10n-lint`, `l10n-compare`, `l10n-fix`, and the `moz.l10n.resource` parser used by the scripts here):
```bash
python3 -m venv /tmp/mozl10n && /tmp/mozl10n/bin/pip install moz.l10n
export PY=/tmp/mozl10n/bin/python           # or an existing venv that has moz.l10n
```
(`compare-locales` is an alternative for the missing/obsolete step if you have a `l10n.toml`.)

---

## 1. Phase 1 — Automated health check

### 1a. Completeness (missing / obsolete strings) + files entirely missing
```bash
cd "$L10N"
miss=0; obs=0
while IFS= read -r f; do
  rel="${f#./}"; src="$REF/$rel"; [ -f "$src" ] || { echo "LOCALE-ONLY: $rel"; continue; }
  s=$(grep -oE '^-?[a-zA-Z][a-zA-Z0-9_-]* *=' "$src" | sed 's/ *=//' | sort -u)
  l=$(grep -oE '^-?[a-zA-Z][a-zA-Z0-9_-]* *=' "$f"   | sed 's/ *=//' | sort -u)
  m=$(comm -23 <(echo "$s") <(echo "$l") | grep -c .); o=$(comm -13 <(echo "$s") <(echo "$l") | grep -c .)
  [ "$m" -gt 0 ] && echo "$rel  MISSING $m"; [ "$o" -gt 0 ] && echo "$rel  OBSOLETE $o"
  miss=$((miss+m)); obs=$((obs+o))
done < <(find . -name '*.ftl')
echo "TOTAL missing=$miss obsolete=$obs"
# files present in REF but absent in the locale (fully untranslated):
( cd "$REF" && find . -name '*.ftl' | while read f; do rel="${f#./}"; [ -f "$L10N/$rel" ] || echo "MISSING FILE: $rel"; done )
```
A large `miss` = locale is behind (sync lag). Completeness is **not** something you "fix" — it needs translation; report it, don't invent strings.

### 1b. Syntax
```bash
cd "$L10N" && "${PY%/*}/l10n-lint" .        # non-.ftl "unsupported" lines are fine; look for parse errors
```

### 1c. Variables/placeholders + access keys (parser-based) — save as `/tmp/checks.py`
```python
import os, re
from moz.l10n.resource import parse_resource
from moz.l10n.model import PatternMessage, SelectMessage, Expression, VariableRef, Markup
L10N=os.environ["L10N"]; REF=os.environ["REF"]

def vars_of(msg):
    vs=set(); decls=set()
    def wp(p):
        for x in p:
            if isinstance(x,Expression):
                if isinstance(x.arg,VariableRef): vs.add(x.arg.name)
                for o in x.options.values():
                    if isinstance(o,VariableRef): vs.add(o.name)
            elif isinstance(x,Markup):
                for o in list(x.options.values())+list(x.attributes.values()):
                    if isinstance(o,VariableRef): vs.add(o.name)
    if isinstance(msg,PatternMessage): decls|=set(msg.declarations); wp(msg.pattern)
    elif isinstance(msg,SelectMessage):
        decls|=set(msg.declarations)
        for s in msg.selectors:
            if isinstance(s,VariableRef): vs.add(s.name)
        for v in msg.variants.values(): wp(v)
    return vs-decls

def plain(msg):
    out=[]
    def wp(p):
        for x in p:
            if isinstance(x,str): out.append(x)
            elif isinstance(x,Expression) and isinstance(x.arg,str): out.append("{REF:"+x.arg+"}")
    if isinstance(msg,PatternMessage): wp(msg.pattern)
    elif isinstance(msg,SelectMessage):
        for v in msg.variants.values(): wp(v); break
    return "".join(out)

def emap(p):
    d={}
    for s in parse_resource(p).sections:
        for e in s.entries:
            if hasattr(e,'id'): d[".".join(e.id)]=e
    return d

terms={}; msgs={}                     # for accesskey expansion of { -brand } / { msg } refs
for root,_,fs in os.walk(L10N):
    for fn in fs:
        if fn.endswith('.ftl'):
            try: res=parse_resource(os.path.join(root,fn))
            except: continue
            for s in res.sections:
                for e in s.entries:
                    if hasattr(e,'id'):
                        k=".".join(e.id); (terms if k.startswith('-') else msgs)[k]=plain(e.value)
def expand(t,d=0):
    if d>3: return t
    return re.sub(r'\{REF:([^}]+)\}', lambda m: expand(terms.get(m.group(1),msgs.get(m.group(1),"")),d+1), t)

var_issues=[]; ak_issues=[]
for root,_,fs in os.walk(L10N):
    for fn in fs:
        if not fn.endswith('.ftl'): continue
        p=os.path.join(root,fn); rel=os.path.relpath(p,L10N); sp=os.path.join(REF,rel)
        if not os.path.exists(sp): continue
        try: le=emap(p); se=emap(sp)
        except: continue
        for key,e in le.items():
            props={'':e.value}; props.update(e.properties or {})
            se_e=se.get(key)
            if se_e is not None:
                sp_=({'':se_e.value}); sp_.update(se_e.properties or {})
                for pk,m in props.items():
                    if pk in sp_ and vars_of(m)!=vars_of(sp_[pk]):
                        var_issues.append(f"{rel} [{key}.{pk}] REF={sorted(vars_of(sp_[pk]))} LOC={sorted(vars_of(m))}")
            for pk,m in props.items():
                if pk.endswith('accesskey'):
                    ak=plain(m).strip()
                    if len(ak)!=1: continue
                    base=pk[:-9]
                    lbl=next((props[c] for c in [base+'label',base+'value',base+'title',base+'aria-label',
                              base+'placeholder',base+'tooltiptext',base+'toolbarname','','label','value',
                              'aria-label','placeholder','tooltiptext','toolbarname'] if c in props and c!=pk), None)
                    if lbl is not None and ak.lower() not in expand(plain(lbl)).lower():
                        ak_issues.append(f"{rel} [{key}] accesskey '{ak}' not in label")
print("VARIABLE/PLACEHOLDER MISMATCHES:", len(var_issues)); [print(" ",x) for x in var_issues]
print("ACCESSKEY NOT IN LABEL:", len(ak_issues)); [print(" ",x) for x in ak_issues[:200]]
```
```bash
"$PY" /tmp/checks.py
```
- **Variable mismatches** are the only truly *functional* class here — an undefined `$var` renders blank. Verify each against the source (some are safe: the var is passed for a sibling attribute).
- **Access keys**: a big count usually means the locale kept English accesskeys without re-mapping to translated labels — treat as **one systemic decision**, not N line items. Confirm against `REF` (if en-US's key matches its own label but the locale's doesn't, it's unadapted). `inspect`→Q etc. are inherited from en-US, not defects.

### 1d. Typography — **detect the locale's convention first, then flag deviations**
Don't assume. Count, then check. Examples seen so far:
| Locale | Quotes | Apostrophe | Punctuation spacing | Address register |
|---|---|---|---|---|
| it | `'`/`"` (typographic) | `’` (U+2019) | — | — |
| fr | `« »` | `’` | **NBSP U+00A0** before `? ! ; :` | — |
| de | `„…"` (U+201E/U+201C) | `’` | — | formal **Sie** (flag "du") |
| es-MX | curly `"…"` (or straight) | — | `¿`/`¡` open marks required | informal **tú** (flag "usted") |

Detect convention (adapt chars per language):
```bash
cd "$L10N"
grep -rohP "„" --include='*.ftl' . | wc -l      # German open quote count, etc.
grep -rhoP "\x{00a0}[?!;:]" --include='*.ftl' . | wc -l   # French NBSP-before-punct count
```
Then flag deviations with the parser (operate on message **values**, strip `<tags>`; **ignore**: `#` comments, `.style` CSS, `data-l10n-name='…'` attrs, code/URLs, `::1`/`::first-line`, `&lt;` entities). Language-specific value checks worth scripting:
- fr: regular space (U+0020) before `? ! : ;` where the locale uses NBSP.
- es: a `?`-terminated value with no leading `¿` (Spanish opens with `¿`/`¡`).
- de/es: capitalization of nominalized verbs/nouns (de) / title-case vs sentence-case (es).
- any: straight `"` pairs / straight `'` in-word where the locale uses typographic.

### 1e. Cross-file consistency (same en-US string → divergent translations)
Parse both trees, key by en-US value, report where the locale rendered the same source string differently (`marque page`/`marque-page`, `Chariot`/`Charriot`, synonym drift). Many are legitimate context differences — surface, don't force. (Script: group `REF` messages by normalized value; for each group with >1 distinct locale rendering, print them.)

---

## 2. Phase 2 — Qualitative review (fan-out)

Automated checks miss meaning. Fan out **per-directory reviewer agents** (parallel), each comparing the locale file to `REF` at the same path, using the `#` developer comments as context. Partition to keep file sets disjoint. A balanced 8-way split that worked:
1. `browser/browser/preferences/`
2. `browser/browser/*.ftl` a–l (top-level only)
3. `browser/browser/*.ftl` m–z (top-level only)
4. `browser/browser/newtab/` + `touchbar/` + `policies/` + `branding/` + `langpack-metadata.ftl`
5. `toolkit/toolkit/about/`
6. `toolkit/**` except `about/` (+ `intl/languageNames|regionNames`, neterror, pdfviewer, formautofill, global…)
7. `devtools/`
8. `dom/` + `security/` + `netwerk/` + `mobile/`

**Reviewer instructions (each agent):** report ONLY high-confidence concrete defects (never subjective/style); read both the locale file and `REF/<same path>`; skip untranslated/English strings (that's the completeness gap); categories = mistranslation, dev-comment not followed (do-not-translate, char limits), terminology inconsistency, grammar/agreement/spelling/accents, **locale register** (du/Sie, tú/usted), typography specific to the language, markup defects. **Do NOT** report missing/obsolete strings, syntax, variable/placeholder, or accesskey (handled in Phase 1). Output one bullet per finding: `STRING-ID — path — [category] desc. Current "…" → Suggest "…" (why)`.

**Gotchas with fan-out agents:**
- Some agents try to "coordinate" and return a non-answer like *"waiting for group X"*. **Re-query** them ("there is no group X; you did the work yourself; output your findings now").
- Language names in `intl/languageNames.ftl` are a rich defect source (country/adherent instead of the language, e.g. `Judío` for Yiddish). `regionNames.ftl` too.
- CSS keywords inside `<strong>` in `devtools/tooltips.ftl` must stay English (dev comment) — watch for translated/garbled ones.
- `enterprise/` + `FELT` files may be locale-only and legitimate (not in `REF`).

---

## 3. Phase 3 — The report

Write `~/Desktop/firefox-<locale>-l10n-review.md`. Conventions that were requested and worth keeping:
- **Key every finding by its string ID, not line numbers** (line numbers drift between locale and REF and across syncs). If you have line numbers, resolve them with the parser (see `resolve_ids` pattern: for each `(file,line)`, the enclosing entry whose `linepos.start ≤ line ≤ end`).
- **No cross-language comparisons** in the report — assess the locale on its own terms vs en-US only.
- Header: date, locale repo path + **commit hash**, REF path.
- **Health check** table (syntax / variables / accesskeys / completeness).
- **Systemic bucket** — things reported as *decisions*, not enumerated line-by-line: accesskey remapping, quote convention, register normalization, title-case capitalization, and any pervasive accent/ellipsis pattern (list the affected IDs).
- **Enumerated sections by category** (A functional/markup, B mistranslation, C wrong names, D brand/do-not-translate, E gender/number, F verb/mood/prep, G spelling/accents, H terminology, I typography). Each item: `` `string-id` (`file`) — Current → Suggest (why) ``.
- A **findings-by-area count** table.
- For huge locales, enumerate the concrete unambiguous defects and **summarize pervasive patterns** with representative examples + counts (don't list 200 identical accents).
- Note upstream issues that are **not** the locale's fault (e.g. an ID typo like `cclear-…` present in en-US too).
- Ask the user whether they want a subjective-conclusions paragraph; some prefer it omitted.

---

## 4. Phase 4 — Applying fixes

1. **Pull** the repo first (review current strings), then branch:
   ```bash
   cd <repo-root> && git pull --ff-only && git checkout -b <locale>-l10n-fixes
   ```
2. **Scope** with the user. "Fix all errors but section H" meant: apply the enumerated concrete defects in report sections A–G and I plus the clearly-mechanical systemic buckets (interrogative accents, ellipsis), and **skip** H (terminology) and the judgment-call systemic buckets (register, quotes, accesskey remapping, title-case) — those are large normalization decisions, not mechanical fixes. Completeness is always out of scope.
3. **Fan out fixer agents by the same area partition**, each driven by the report on disk. Give each: its file scope, the exact inclusion (which report sections/buckets) and **strict exclusions**; method = locate by **string ID**, read current value, if it no longer matches (already fixed by a sync) **skip + note**, else apply the **minimal** edit preserving variables `{ $x }`, terms `{ -x }`, markup/attributes, Fluent structure; for "meaning reversed" items read `REF` and match the English meaning; keep the locale's existing register/quote style except the specific fix; change nothing else; **do not commit**. Disjoint file scopes → safe in parallel on one branch.
4. Also fix **identical-typo siblings** the agents flag even if the report enumerated only one instance.
5. **Verify**:
   ```bash
   cd "$L10N" && "${PY%/*}/l10n-lint" .            # syntax clean
   "$PY" /tmp/checks.py                            # variable mismatches must NOT increase; accesskeys unchanged
   cd <repo-root> && git diff --stat main -- <locale>/
   ```
   Spot-check the risky edits: plural-variant swaps, `<strong>`/markup restorations, reworded mistranslations, language names.
6. **Do not commit or push unless asked.** Offer a commit (`<locale>: fix localization errors from QA review`) and/or PR, and offer the skipped normalization passes (register / capitalization / accesskeys) as separate commits.

---

## 5. Lessons / gotchas checklist

- Detect typographic conventions by counting; never assume per language.
- Access-key and straight-quote counts are usually **systemic decisions**, not N bugs.
- en-US line numbers ≠ locale line numbers; key on **string IDs**.
- Report files written to `~/Desktop` in a sandboxed run may end up in `~/.Trash`; check there if a file "vanishes".
- Re-query fan-out agents that return "waiting for group X".
- Ignore for typography: `#` comments, `.style` CSS, `data-l10n-name='…'`, code/URLs, IPv6 `::1`, CSS `::first-line`, `&lt;`-entities, `min-width:`.
- Some ID typos / double spaces exist in en-US too — verify before blaming the locale.
- Memory: this workflow and per-locale outcomes are recorded under the project memory (`l10n-qa-tooling`, `firefox-<locale>-locale-review-*`).

#!/usr/bin/env python3
"""Self-test against real locale trees.

The deterministic checks are only worth anything if they agree with the
fourteen hand-written reviews: they must find the defects those reviews
found by hand, and stay silent on the conventions those reviews established
as correct. Both directions matter, and the second one more -- a checker
that cries wolf on correct Japanese ellipsis or Polish case declension is
worse than no checker.

Needs local clones; it reads them and writes nothing.

    python firefox/tools/selftest.py \\
        --l10n-dir ~/mozilla/git/firefox-l10n \\
        --source-dir ~/mozilla/git/firefox-quarantine
"""

from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(_HERE)), "lib"))

import checks  # noqa: E402
import config  # noqa: E402
import layout  # noqa: E402
import conventions  # noqa: E402
import findings as findings_mod  # noqa: E402
import parse  # noqa: E402
import suppress  # noqa: E402

# Defects the manual reviews found by hand. Each must still be caught.
# Anything the locale team has since fixed is listed under FIXED_UPSTREAM
# instead of being quietly deleted -- the difference between "the check
# broke" and "the defect is gone" is the whole point of the system.
MUST_FIND = [
    ("tr", "term_params", "fxa-signout-dialog-body-aiwindow"),
    # Polish needs one/few/many; with only one/other, five comments render
    # the `few` form. en-US selects on the `one` *category* here, so this is
    # real grammatical agreement rather than a one-versus-many choice.
    ("pl", "plurals", "pdfjs-editor-comments-sidebar-title"),
    ("sl", "term_params", "firefox-relay-must-login-to-fxa"),
    ("de", "markup", "about-logins-import-dialog-items-no-change2"),
]

FIXED_UPSTREAM = [
    # Repaired by the Italian team in a Pontoon sync on 2026-08-20, between
    # two runs of this suite -- which is the tracking working, not a
    # regression in the check.
    ("it", "markup", "about-glean-about-data-list-item-dictionary"),
    # The Turkish string no longer passes `plural-form` to the brand term.
    ("tr", "term_params", "ai-window-learn-from-browsing-activity"),
    # The Dutch team repaired all three malformed closing tags the nl review
    # reported; nl markup findings are now legitimately zero.
    ("nl", "markup", "genai-settings-chat-gemini-links"),
    ("nl", "markup", "about-logins-import-dialog-items-no-change2"),
    ("nl", "markup", "cfr-doorhanger-milestone-heading2"),
]

# Correct localization that earlier versions of these checks misread. Each
# one is a false positive that was actually reported, kept here so it cannot
# come back.
NOT_A_DEFECT = [
    # Fluent passes arguments per message, not per attribute: en-US uses
    # $extensionsCount in .heading, so .message may use it too. Comparing
    # attribute-to-attribute called this an undefined variable.
    ("es-MX", "variables", "unified-extensions-mb-blocklist-warning-multiple"),
    ("es-MX", "variables", "unified-extensions-mb-blocklist-error-multiple"),
    # The locale adding [one] where en-US has only [other] is what
    # localizing a plural *is*, and must never be flagged.
    ("es-MX", "plurals", "unified-extensions-mb-blocklist-warning-multiple2"),
    # en-US keys on the exact number 1 ("Remove" / "Remove All"): a
    # one-versus-many choice, not agreement. Mirroring it is correct, and
    # demanding few/many here flagged most of Polish and Russian.
    ("pl", "plurals", "about-logins-confirm-remove-all-dialog-confirm-button-label"),
    ("sl", "plurals", "places-delete-page"),
    ("ru", "plurals", "places-delete-page"),
    ("es-MX", "plurals", "download-ui-cancel-downloads-ok"),
]

# Conventions the reviews established as correct. These checks must be
# silent, or explicitly skipped for the locale.
MUST_BE_SILENT = [
    ("ja", "typography", "Japanese uses ASCII ellipsis, not …"),
    ("ja", "accesskey", "Japanese access keys are deliberately English"),
    ("zh-CN", "accesskey", "access keys are meaningless in Chinese"),
    ("nl", "typography", "the en dash is the Dutch house dash"),
    ("pl", "accesskey", "Polish access keys are correctly remapped"),
    ("tr", "accesskey", "Turkish access keys are correctly remapped"),
    ("it", "accesskey", "Italian access keys are correctly remapped"),
    ("it", "variables", "Italian has no variable mismatches"),
    ("it", "selectors", "Italian has no selector mismatches"),
    ("sl", "variables", "Slovenian sklon case params are not mismatches"),
    ("sl", "selectors", "Slovenian sklon case params are not mismatches"),
    ("it", "variant_spelling", "the variant check is silent for a translation"),
    ("it", "plurals", "Italian mirrors en-US plurals correctly"),
    ("nl", "plurals", "Dutch mirrors en-US plurals correctly"),
    ("es-MX", "plurals", "Mexican Spanish plurals are correct"),
    ("ru", "plurals", "Russian plurals are correct"),
    ("sl", "plurals", "Slovenian plurals are correct"),
]

# Health numbers that should stay in the right neighbourhood. Completeness
# drifts with every upstream sync, so these are bounds, not equalities.
HEALTH_BOUNDS = [
    ("it", "missing", 0, 50),
    ("nl", "missing", 0, 200),
    ("ja", "syntax", 0, 0),
    ("it", "syntax", 0, 0),
]


def run(l10n_dir, source_dir, project) -> int:
    src = parse.parse_tree(source_dir, project.extensions, project.exclude)
    print(f"en-US reference: {len(src):,} strings\n")


    needed = sorted(
        {loc for loc, *_ in MUST_FIND + MUST_BE_SILENT + FIXED_UPSTREAM + NOT_A_DEFECT}
        | {loc for loc, *_ in HEALTH_BOUNDS}
        | {loc for loc in ("en-GB", "en-CA") if loc in project.locales}
    )
    results = {}
    trees = {}
    for locale in needed:
        loaded = layout.load(project, locale, l10n_dir, source_dir)
        counts = conventions.detect(locale, loaded.l10n)
        health, found = checks.run_all(project, locale, loaded, counts)
        results[locale] = (health, found, counts)
        trees[locale] = loaded.l10n

    passed = failed = 0

    def check(ok, label):
        nonlocal passed, failed
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if ok:
            passed += 1
        else:
            failed += 1

    print("Defects the manual reviews found — must still be caught")
    for locale, kind, string_id in MUST_FIND:
        _, found, _ = results[locale]
        hit = any(f.check == kind and f.string_id == string_id for f in found)
        check(hit, f"{locale}: {kind} on {string_id}")

    print("\nDefects since fixed upstream — must NOT be reported any more")
    for locale, kind, string_id in FIXED_UPSTREAM:
        _, found, _ = results[locale]
        hit = any(f.check == kind and f.string_id == string_id for f in found)
        check(not hit, f"{locale}: {kind} on {string_id} is gone")

    print("\nCorrect localization that must not be flagged")
    for locale, kind, string_id in NOT_A_DEFECT:
        _, found, _ = results[locale]
        hit = any(f.check == kind and f.string_id == string_id for f in found)
        check(not hit, f"{locale}: {kind} on {string_id}")

    print("\nConventions established as correct — must stay silent")
    for locale, kind, why in MUST_BE_SILENT:
        health, _, _ = results[locale]
        silent = kind in health.skipped or health.counts.get(kind, 0) == 0
        state = "skipped" if kind in health.skipped else health.counts.get(kind, 0)
        check(silent, f"{locale}: {kind} = {state} ({why})")

    print("\nHealth numbers in range")
    for locale, metric, low, high in HEALTH_BOUNDS:
        health, _, _ = results[locale]
        value = len(health.syntax_errors) if metric == "syntax" else health.missing
        check(low <= value <= high, f"{locale}: {metric} = {value} (expected {low}–{high})")

    print("\nFinding lifecycle")
    from findings import Finding
    f = Finding(locale="xx", file="a.ftl", string_id="s", category="A",
                summary="malformed tag", current="text</a >here")
    check(f.status == "open", "a new finding starts open")
    check(findings_mod.still_present("text</a >here", "text</a >here more"),
          "an unchanged defect is detected as still present")
    check(not findings_mod.still_present("text</a >here", "text</a>here more"),
          "a punctuation-only repair is detected as fixed")
    check(f.identity() == Finding(**{**f.__dict__, "fid": ""}).identity(),
          "identity is stable across reconstruction")

    print("\nLanguage variants")
    import llm_incremental as _li
    import variants as _v
    src_tree = src
    for loc in ("en-GB", "en-CA"):
        if loc not in project.locales:
            continue
        health, found, _ = results[loc]
        check(project.is_variant(loc), f"{loc} is configured as a variant")
        check(not health.untranslated_files,
              f"{loc}: files identical to the source are not reported")
        spelling = [f for f in found if f.check == "variant_spelling"]
        check(bool(spelling), f"{loc}: unadapted source spellings are found ({len(spelling)})")
        prompt = _li.system_prompt(project, loc)
        check("variant of" in prompt, f"{loc}: the variant prompt is selected")
    check(not project.is_variant("it"), "an ordinary locale is not a variant")
    check("variant of" not in _li.system_prompt(project, "it"),
          "an ordinary locale gets the ordinary prompt")

    if "en-GB" in project.locales:
        gb = trees["en-GB"]
        rules = _v.learn(gb, src_tree)
        check(rules.get("color", ("",))[0] == "colour",
              "the colour rule is learned from the corpus, not hardcoded")
        check("forward" not in rules,
              "a contextual swap (forward/forwards) is not treated as a rule")
        check(_v.in_code_token("color", "Animations of \u2018background-color\u2019 cannot"),
              "a word inside a hyphenated identifier is left alone")
        check(_v.in_code_token("color", 'MathML attributes \u201cbackground\u201d, \u201ccolor\u201d'),
              "a word quoted as a literal is left alone")
        check(not _v.in_code_token("colour", "Choose a colour for the theme"),
              "a word used as prose is not mistaken for code")

    print("\nFixed versus withdrawn")

    class _Msg:
        def __init__(self, text, digest):
            self._t, self._h = text, digest

        def text(self):
            return self._t

        def hash(self):
            return self._h

    def _resolve(store, digest):
        found = [store]
        findings_mod.resolve(
            found, {("a.ftl", "s"): _Msg("text", digest)}, {("a.ftl", "s")},
            "2026-01-01", rerunnable={"markup"}, still_raised=set(),
        )
        return store.status

    from findings import Finding as _F
    moved = _F(locale="xx", file="a.ftl", string_id="s", category="A",
               check="markup", summary="bad tag", string_hash="oldhash")
    check(_resolve(moved, "newhash") == "fixed",
          "a check finding whose string changed is fixed")
    stayed = _F(locale="xx", file="a.ftl", string_id="s", category="A",
                check="markup", summary="bad tag", string_hash="samehash")
    check(_resolve(stayed, "samehash") == "withdrawn",
          "a check finding dropped while the string never moved is withdrawn, not fixed")

    print("\nPlural categories")
    import plurals
    check(plurals.categories_for("ja") == frozenset({"other"}),
          "Japanese has only the `other` category")
    check("few" in (plurals.categories_for("pl") or set()),
          "Polish has a `few` category")
    check(plurals.categories_for("not-a-locale-xyz") is None,
          "an unresolvable locale disables the check rather than guessing")
    check(plurals.covered_categories("es-MX", {"1", "other"}) == frozenset({"one", "other"}),
          "the exact key [1] covers the `one` category in Spanish")
    check(plurals.covered_categories("ja", {"1", "other"}) == frozenset({"other"}),
          "the exact key [1] covers `other` in Japanese")
    check(plurals.is_numeric_key("1") and not plurals.is_numeric_key("one"),
          "numeric keys are told apart from category keys")

    print("\nFix detection")
    check(not findings_mod.still_present("INDIRIZZO", "Indirizzo"),
          "a capitalisation fix is detected (case is not folded away)")
    check(findings_mod.still_present("Traduzione", "Traduzione"),
          "an unchanged string still reads as unfixed")

    class _M:
        def __init__(self, t): self.t = t
        def text(self): return self.t
        def hash(self): return "now"

    check(findings_mod.verdict("Traduzione", "Traduzione") == "unchanged",
          "a string still exactly as flagged reads as unchanged")
    check(findings_mod.verdict("Traduzione", "Traduzione in corso") == "unclear",
          "a fragment surviving an addition is unclear, not still-present")
    check(findings_mod.verdict("vecchio", "nuovo testo") == "gone",
          "text that has gone reads as gone")

    f_moved = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                      summary="x", current="Traduzione", string_hash="then")
    findings_mod.resolve([f_moved], {("a.ftl", "s"): _M("Traduzione in corso")},
                         set(), "2026-01-01")
    check(f_moved.status == "needs-recheck",
          "a surviving substring after an edit asks for a re-read, not a verdict")

    f_same = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                     summary="x", current="Traduzione", string_hash="then")
    findings_mod.resolve([f_same], {("a.ftl", "s"): _M("Traduzione")},
                         set(), "2026-01-01")
    check(f_same.status == "open",
          "an unchanged string keeps its finding open, not re-queued")

    f_stale = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                      summary="x", current="vecchio", string_hash="now")
    findings_mod.resolve([f_stale], {("a.ftl", "s"): _M("nuovo testo")},
                         set(), "2026-01-01", recheck=True)
    check(f_stale.status == "fixed",
          "--recheck closes a defect whose text has gone, whatever the delta says")

    f_quiet = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                      summary="x", current="Trad", string_hash="now")
    findings_mod.resolve([f_quiet], {("a.ftl", "s"): _M("Traduzione")},
                         set(), "2026-01-01", recheck=True)
    check(f_quiet.status == "open",
          "--recheck leaves alone a finding whose string shows no sign of moving")

    f_open = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                     summary="x", current="Traduzione", string_hash="now")
    findings_mod.close_reviewed([f_open], {("a.ftl", "s")}, set(),
                                {("a.ftl", "s")}, "2026-01-01")
    check(f_open.status == "fixed",
          "a finding the reviewer re-read and did not repeat is closed")

    f_quiet2 = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                       summary="x", current="Traduzione", string_hash="now")
    findings_mod.close_reviewed([f_quiet2], {("a.ftl", "s")}, set(),
                                set(), "2026-01-01")
    check(f_quiet2.status == "open",
          "silence about an unchanged string closes nothing")

    print("\nDismissing one finding by hand")
    import dismiss as _d
    parsed = _d.load.__wrapped__ if hasattr(_d.load, "__wrapped__") else None
    import tempfile, os as _os
    tmp = tempfile.mkdtemp()
    _os.makedirs(_os.path.join(tmp, "locales", "it"), exist_ok=True)
    with open(_os.path.join(tmp, "locales", "it", "dismissed.txt"), "w") as fh:
        fh.write("# a comment\n\nmy_string — looked at it, it is fine\n"
                 "other_string @ some/path — fine here only\n")

    class _P:
        def locale_dir(self, loc): return _os.path.join(tmp, "locales", loc)

    entries = _d.load(_P(), "it")
    check(entries.get(("my_string", None)) == "looked at it, it is fine",
          "a plain line parses, with its reason")
    check(("other_string", "some/path") in entries,
          "a line can be qualified by file")
    check(len(entries) == 2, "comments and blank lines are ignored")

    a = Finding(locale="it", file="x/y.ftl", string_id="my_string",
                category="B", summary="s")
    b = Finding(locale="it", file="x/y.ftl", string_id="untouched",
                category="B", summary="s")
    c = Finding(locale="it", file="other/place.ftl", string_id="other_string",
                category="B", summary="s")
    _d.apply(entries, [a, b, c])
    check(a.status == "dismissed" and a.dismissed_because.startswith("looked at"),
          "the named finding is dismissed, with its reason kept")
    check(b.status == "open", "other findings are untouched")
    check(c.status == "open", "a file-qualified line does not match another file")
    _d.apply({}, [a, b, c])
    check(a.status == "open" and not a.dismissed_because,
          "removing the line brings the finding back")

    print("\nA maintainer's dismissal must survive")
    from suppress import Rule as _R
    revived = Finding(locale="it", file="a.ftl", string_id="s", category="D",
                      summary="x", status="suppressed",
                      suppressed_by="legacy-dismissed")
    suppress.apply([], [revived])
    check(revived.status == "open",
          "a suppression whose rule no longer exists is correctly restored")
    kept = Finding(locale="it", file="a.ftl", string_id="s", category="D",
                   summary="x", status="dismissed",
                   dismissed_because="maintainer said so")
    suppress.apply([], [kept])
    check(kept.status == "dismissed",
          "which is why an imported dismissal must be `dismissed`, not a "
          "`suppressed` pointing at a rule id no file defines")

    print("\nReporting a run honestly")
    # The bug this pins: resolve() marked a finding fixed, the reviewer
    # raised it again in the same run so merge() reopened it, and the
    # report still counted it under "fixed since the last run".
    was_fixed = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                        summary="x", current="old", status="fixed")
    bucket = [was_fixed]
    findings_mod.merge([was_fixed],
                       [Finding(locale="it", file="a.ftl", string_id="s",
                                category="B", summary="x", current="old")],
                       "2026-01-01")
    check(was_fixed.status == "open",
          "re-raising a fixed finding reopens it")
    check([f for f in bucket if f.status == "fixed"] == [],
          "and it must then be dropped from the run's fixed list")

    import summary as _summary
    for locale in ("it",):
        counted = findings_mod.load(project, locale)
        rendered = _summary.render(project)
        n_fixed = sum(1 for f in counted if f.status == "fixed")
        check(f"| {n_fixed} |" in rendered or str(n_fixed) in rendered,
              f"the cross-locale page reports {locale}'s {n_fixed} fixed")

    listed = [line.split("[", 1)[1].split("]", 1)[0]
              for line in _summary.render(project).splitlines()
              if line.startswith("| [")]
    check(listed == sorted(listed),
          "the cross-locale table is ordered by locale code, so a locale "
          "stays put between runs")

    # Detail lines are nested under their finding with four spaces: the
    # published site renders with Python-Markdown, which flattens a
    # two-space indent and turned every report into one undifferentiated
    # list of bullets.
    import report as report_mod
    nested = report_mod._item(
        Finding(locale="it", file="a.ftl", string_id="s", category="B",
                summary="wrong content", current="testo", rationale="why"))
    check(all(line.startswith("    - ") for line in nested.splitlines()[1:]),
          "a finding's Current/Source/Suggest/rationale hang under it at a "
          "full indent level")
    try:
        import markdown
    except ImportError:
        markdown = None
    if markdown is not None:
        html = markdown.markdown(nested, extensions=["tables", "sane_lists"],
                                 output_format="html5")
        check(html.count("<ul>") == 2,
              "and the site's renderer really does nest them")

    # The site escapes the source and the renderer escapes the `&` of every
    # entity again inside a code span. One round is undone so the reviewer
    # reads the markup the string actually contains -- but only one, and the
    # text must stay text.
    import importlib.util
    import tempfile
    _root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    spec = importlib.util.spec_from_file_location(
        "site_build", os.path.join(_root, "site", "build.py"))
    site_build = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(site_build)
    with tempfile.TemporaryDirectory() as tmp:
        sample = os.path.join(tmp, "x.md")
        with open(sample, "w", encoding="utf-8") as fh:
            fh.write("- Current: `<span data-l10n-name=\"a\">x</span >`\n"
                     "\nA <b>bold</b> claim outside a code span.\n")
        out = site_build.render(sample, "it")
    check("<code>&lt;span data-l10n-name=&quot;a&quot;&gt;x&lt;/span &gt;</code>" in out,
          "a quoted string shows its markup as markup, not as `&amp;lt;`")
    check("<b>" not in out and "&lt;b&gt;bold" in out,
          "and markup outside a code span is still inert text")

    # The bug this pins: nineteen Android locales were run with --no-llm and
    # every report called the result a completed baseline. The deterministic
    # checks had run; nothing had read a string.
    import run as run_mod
    check(run_mod.pick_mode("auto", {}) == "baseline",
          "a locale with no state gets a baseline")
    check(run_mod.pick_mode("auto", {"mode": "incremental"}) == "incremental",
          "a reviewed locale gets an incremental run")
    check(run_mod.pick_mode("auto", {"mode": "checks-only"}) == "baseline",
          "a locale whose only run skipped the model is still owed its "
          "baseline, state or no state")
    check(run_mod.pick_mode("incremental", {}) == "incremental",
          "an explicit --mode is never second-guessed")
    check(report_mod._reviewer_warning({"mode": "checks-only"}).startswith(">"),
          "and its report says outright that the reviewer did not run")
    check(report_mod._reviewer_warning({"mode": "baseline"}) == "",
          "while a real baseline says nothing of the sort")

    # fy-NL lost twenty-seven completed batches when one item in a tool call
    # came back as a bare string instead of an object.
    import llm_incremental as _llm

    class _Block:
        type = "tool_use"

        def __init__(self, payload):
            self.input = payload

    real = {"string_id": "s", "file": "a.ftl", "category": "B", "impact": 2,
            "summary": "wrong", "current": "vecchio", "suggest": "nuovo",
            "rationale": "r", "confidence": "high"}

    class _Msg:
        file, id, comment = "a.ftl", "s", ""

        def text(self):
            return "vecchio"

        def hash(self):
            return "h"

    tree = {("a.ftl", "s"): _Msg()}
    got, bad = _llm.collect(
        [_Block({"findings": ["not a finding", real]})], "it", tree)
    check(len(got) == 1 and bad == 1,
          "a malformed item is dropped and counted, and the rest of the "
          "batch survives it")
    got, bad = _llm.collect([_Block({"findings": "everything is fine"})],
                            "it", tree)
    check(got == [] and bad == 1, "so is a findings list that is not a list")

    # A batch that fails after its retries used to discard every batch
    # before it. It ends the pass now, but what was read is kept -- and,
    # just as importantly, only what was read counts as reviewed.
    calls = {"n": 0}

    class _Response:
        content = [_Block({"findings": [real]})]

        class usage:
            input_tokens = output_tokens = 1

    def _flaky(*a, **kw):
        calls["n"] += 1
        if calls["n"] > 2:
            raise RuntimeError("LLM call failed after 4 attempts: timeout")
        return _Response()

    saved_call, saved_key = _llm._call, os.environ.get("ANTHROPIC_API_KEY")
    saved_llm = dict(project.data.get("llm", {}))
    _llm._call = _flaky
    os.environ["ANTHROPIC_API_KEY"] = "test"
    try:
        keys = [("a.ftl", "s")] * 0 + [(f"f{i}.ftl", f"s{i}") for i in range(5)]
        fake_tree = {k: _Msg() for k in keys}
        fake_tree[("a.ftl", "s")] = _Msg()  # what the fake response reports
        project.data["llm"] = dict(project.data.get("llm", {}), batch_size=1)
        found, usage, prog = _llm.review(
            project, "it", keys, fake_tree, {}, log=lambda *a: None)
    finally:
        _llm._call = saved_call
        project.data["llm"] = saved_llm
        if saved_key is None:
            os.environ.pop("ANTHROPIC_API_KEY", None)
        else:
            os.environ["ANTHROPIC_API_KEY"] = saved_key

    check(len(found) == 2, "the findings from before the failure are kept")
    check(prog.reviewed == set(keys[:2]),
          "and only the strings actually read count as reviewed, so the "
          "snapshot cannot mark the rest as seen")
    check("batch 3 of 5" in prog.stopped,
          "the run records where it stopped, not just that it did")

    print("\nSuppression rules")
    from suppress import Rule
    rule = Rule({"id": "r", "reason": "because", "match": {"check": "typography",
                                                           "string_id": "felt-*"}}, 0)
    g = Finding(locale="xx", file="a.ftl", string_id="felt-error-x", category="E",
                check="typography", summary="straight apostrophe")
    h = Finding(locale="xx", file="a.ftl", string_id="other-x", category="E",
                check="typography", summary="straight apostrophe")
    check(rule.applies(g), "a prefix rule matches its string")
    check(not rule.applies(h), "a prefix rule does not over-match")
    suppress.apply([rule], [g, h])
    check(g.status == "suppressed" and g.suppressed_by == "r", "matching finding is suppressed")
    check(h.status == "open", "non-matching finding stays open")
    suppress.apply([], [g, h])
    check(g.status == "open" and not g.suppressed_by, "removing the rule restores the finding")

    rule_suggest = Rule({"id": "s", "reason": "r",
                         "match": {"suggest": r"re:\battivat[aoie]\b"}}, 0)
    yes = Finding(locale="it", file="a.ftl", string_id="x", category="D",
                  summary="s", current="Attivo", suggest="Attivato")
    no = Finding(locale="it", file="a.ftl", string_id="x", category="D",
                 summary="s", current="Disattiva", suggest="Disattivato")
    check(rule_suggest.applies(yes), "a rule can match the proposed replacement")
    check(not rule_suggest.applies(no),
          "a word-anchored regex spares disattivato, which contains attivat")

    for bad, why in (
        ({"id": "x", "match": {"check": "typography"}}, "a rule with no reason"),
        ({"id": "x", "reason": "r"}, "a rule that matches nothing"),
        ({"id": "x", "reason": "r", "match": {"nope": 1}}, "an unknown match field"),
    ):
        try:
            Rule(bad, 0)
            check(False, f"{why} is rejected")
        except ValueError:
            check(True, f"{why} is rejected")

    print(f"\n{passed} passed, {failed} failed")
    return 1 if failed else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="firefox")
    ap.add_argument("--l10n-dir", default="~/mozilla/git/firefox-l10n")
    ap.add_argument("--source-dir", default="~/mozilla/git/firefox-quarantine")
    args = ap.parse_args(argv)
    return run(
        os.path.expanduser(args.l10n_dir),
        os.path.expanduser(args.source_dir),
        config.load(args.project),
    )


if __name__ == "__main__":
    raise SystemExit(main())

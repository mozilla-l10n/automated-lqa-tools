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
import selftest_lib  # noqa: E402
import findings as findings_mod  # noqa: E402
import parse  # noqa: E402
import suppress  # noqa: E402

# Defects the manual reviews found by hand. Each must still be caught.
# Anything the locale team has since fixed is listed under FIXED_UPSTREAM
# instead of being quietly deleted -- the difference between "the check
# broke" and "the defect is gone" is the whole point of the system.
MUST_FIND = [
    # Polish needs one/few/many; with only one/other, five comments render
    # the `few` form. en-US selects on the `one` *category* here, so this is
    # real grammatical agreement rather than a one-versus-many choice.
    ("pl", "plurals", "pdfjs-editor-comments-sidebar-title"),
    ("sl", "term_params", "firefox-relay-must-login-to-fxa"),
]

FIXED_UPSTREAM = [
    # The Turkish call now passes the parameter its term selects on.
    ("tr", "term_params", "fxa-signout-dialog-body-aiwindow"),
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
    # The German team closed the `</span >` in both plural variants; the run
    # of 2026-08-25 reported it fixed.
    ("de", "markup", "about-logins-import-dialog-items-no-change2"),
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
    results = selftest_lib.load_results(
        project, checks, l10n_dir, source_dir, needed
    )
    trees = {loc: r[2] for loc, r in results.items()}

    suite = selftest_lib.Suite()
    check = suite.check

    selftest_lib.must_find(suite, results, MUST_FIND)
    selftest_lib.fixed_upstream(suite, results, FIXED_UPSTREAM)
    selftest_lib.not_a_defect(suite, results, NOT_A_DEFECT)
    selftest_lib.must_be_silent(suite, results, MUST_BE_SILENT)

    suite.section("Health numbers in range")
    for locale, metric, low, high in HEALTH_BOUNDS:
        health, _, _ = results[locale]
        value = len(health.syntax_errors) if metric == "syntax" else health.missing
        check(low <= value <= high, f"{locale}: {metric} = {value} (expected {low}–{high})")

    suite.section("Finding lifecycle")
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

    suite.section("Language variants")
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
        gb = trees["en-GB"].l10n
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

    suite.section("Fixed versus withdrawn")

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

    suite.section("Plural categories")
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

    suite.section("Fix detection")
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

    # `string_hash="then"` against a mock hashing to "now": the string moved,
    # the delta simply does not know it. That is what "whatever the delta
    # says" means here. It used to read `string_hash="now"` -- a string that
    # had *not* moved since the finding was raised -- which is a state where
    # the quoted text cannot have been fixed, only mis-quoted.
    f_stale = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                      summary="x", current="vecchio", string_hash="then")
    findings_mod.resolve([f_stale], {("a.ftl", "s"): _M("nuovo testo")},
                         set(), "2026-01-01", recheck=True)
    check(f_stale.status == "fixed",
          "--recheck closes a defect whose text has gone, whatever the delta says")

    f_unmoved = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                        summary="x", current="vecchio", string_hash="now")
    findings_mod.resolve([f_unmoved], {("a.ftl", "s"): _M("nuovo testo")},
                         set(), "2026-01-01", recheck=True)
    check(f_unmoved.status == "open",
          "but a fragment absent from a string that never moved is an "
          "unusable quote, not a fix, and closes nothing")

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

    suite.section("Dismissing one finding by hand")
    import os as _os
    import tempfile

    import dismiss as _d
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

    suite.section("A maintainer's dismissal must survive")
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

    suite.section("Reporting a run honestly")
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
                summary="wrong content", current="testo", rationale="why"),
        report_mod.Ctx())
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
    check(run_mod.pick_mode("auto", False) == "baseline",
          "a locale with no state gets a baseline")
    check(run_mod.pick_mode("auto", True) == "incremental",
          "a reviewed locale gets an incremental run")
    check(run_mod.pick_mode("auto", False) == "baseline",
          "a locale whose only run skipped the model is still owed its "
          "baseline")
    check(run_mod.pick_mode("incremental", False) == "incremental",
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

        def __init__(self, text="vecchio"):
            self._text = text

        def text(self):
            return self._text

        def hash(self):
            return "h"

        def context_hash(self):
            return ""

    tree = {("a.ftl", "s"): _Msg()}
    got, bad, _ok = _llm.collect(
        [_Block({"findings": ["not a finding", real]})], "it", tree)
    check(len(got) == 1 and bad == 1,
          "a malformed item is dropped and counted, and the rest of the "
          "batch survives it")
    got, bad, _ok = _llm.collect([_Block({"findings": "everything is fine"})],
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
        fake_src = {k: _Msg("old") for k in keys}
        project.data["llm"] = dict(project.data.get("llm", {}), batch_size=1)
        found, usage, prog = _llm.review(
            project, "it", keys, fake_tree, fake_src, log=lambda *a: None)
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

    suite.section("A string with no en-US counterpart is not reviewable")

    # Eleven German findings were raised against the ten `enterprise/` files,
    # which are synced from a separate repository and have no en-US side in
    # this one. The reviewer was handed the translation and the words "no
    # source string", inferred the English from the string id, and reported
    # the translation against its own guess -- including that "Guten Morgen"
    # should be an update title.
    lone = ("browser/browser/enterprise/felt.ftl", "felt-updates-title")
    paired = ("browser/browser/appmenu.ftl", "appmenu-new-tab")
    lone_tree = {lone: _Msg("Guten Morgen"), paired: _Msg("Neuer Tab")}
    lone_src = {paired: _Msg("New tab")}
    body = _llm.render_batch([lone, paired], lone_tree, lone_src)
    check("Guten Morgen" not in body,
          "a string with no source is not put in front of the model")
    check("Neuer Tab" in body, "while its neighbour with a source still is")

    import snapshot as _snap
    snap = _snap.build(lone_tree, lone_src)
    check(lone[0] not in snap,
          "and it is not in the snapshot, so no delta ever offers it")
    check(snap.get(paired[0], {}).get(paired[1]),
          "a string with a source is snapshotted as before")

    # Not counted as reviewed either: the empty-batch shortcut means "every
    # string here is identical to its source", which is an answer. "There
    # was nothing to compare against" is not.
    saved_call, saved_key = _llm._call, os.environ.get("ANTHROPIC_API_KEY")
    _llm._call = lambda *a, **kw: (_ for _ in ()).throw(
        AssertionError("the model must not be called at all"))
    os.environ["ANTHROPIC_API_KEY"] = "test"
    try:
        _found, _usage, prog = _llm.review(
            project, "de", [lone], lone_tree, lone_src, log=lambda *a: None)
    finally:
        _llm._call = saved_call
        if saved_key is None:
            os.environ.pop("ANTHROPIC_API_KEY", None)
        else:
            os.environ["ANTHROPIC_API_KEY"] = saved_key
    check(not prog.reviewed and not prog.trusted,
          "an unreviewable string is not recorded as read, so reviewer "
          "silence about it closes nothing")

    suite.section("Locale-only files are reported, not reviewed")
    de_health, de_found, de_trees = results["de"]
    only = de_trees.l10n_files - de_trees.source_files
    check(bool(only), f"de has files with no en-US counterpart ({len(only)})")
    check(set(de_health.locale_only_files) == only,
          "the health check names them rather than silently dropping them")
    check(de_health.locale_only > 0,
          f"and counts their strings ({de_health.locale_only})")
    check("Files with no en-US counterpart" in report_mod._health_table(de_health),
          "the report says how many there are")
    # `obsolete` means en-US dropped a string the locale still has. A file
    # en-US never had at all is a different thing and must not inflate it.
    lone_strings = sum(1 for k in de_trees.l10n
                       if k not in de_trees.source and k[0] in only)
    check(de_health.obsolete + lone_strings
          == sum(1 for k in de_trees.l10n if k not in de_trees.source)
          and de_health.obsolete < lone_strings,
          "they are counted apart from obsolete strings, not as them")

    import llm_baseline as _bl
    reviewable, dropped = _bl.comparable_files(de_trees)
    check(set(dropped) == only and not (set(reviewable) & only),
          "and the baseline hands the agent no file it cannot compare")
    buckets = _bl.partition_files(de_trees.root, tuple(project.extensions),
                                  files=reviewable)
    check(not (set(sum(buckets.values(), [])) & only),
          "so no partition claims one either")

    # Rewording a check's own message used to retire its real findings.
    # The fid folds in the summary, so the stored finding looked
    # un-re-raised and was withdrawn; `merge` then matched the new one
    # loosely, refreshed the withdrawn record in place, and the defect left
    # the backlog without anyone deciding it had.
    class _H:
        def __init__(self, h="same"):
            self._h = h

        def hash(self):
            return self._h

        def text(self):
            return "testo"

    was = Finding(locale="cs", file="a.xml", string_id="s", category="A",
                  check="placeholders", summary="has placeholders %d",
                  string_hash="same")
    now = Finding(locale="cs", file="a.xml", string_id="s", category="A",
                  check="placeholders", summary="has placeholders %1$d",
                  string_hash="same")
    check(was.fid != now.fid, "rewording the message does give it a new fid")
    check(was.rekey == now.rekey,
          "but the same check on the same string is the same complaint")
    buckets = findings_mod.resolve(
        [was], {("a.xml", "s"): _H()}, set(), "2026-08-23",
        rerunnable={"placeholders"}, still_raised={now.fid},
        still_raised_loose={now.rekey},
    )
    check(was.status == "open" and not buckets["withdrawn"],
          "so a reworded finding stays open instead of being withdrawn")

    gone = Finding(locale="cs", file="a.xml", string_id="t", category="A",
                   check="placeholders", summary="x", string_hash="same")
    buckets = findings_mod.resolve(
        [gone], {("a.xml", "t"): _H()}, set(), "2026-08-23",
        rerunnable={"placeholders"}, still_raised=set(), still_raised_loose=set(),
    )
    check(gone.status == "withdrawn",
          "while a check that really did stop raising it still withdraws it")

    suite.section("A finding raised against no source has a route out")

    # The eleven German findings already in the backlog have to have a route
    # out, and it is `withdrawn`: the reviewer will never be offered those
    # strings again, so it can neither repeat nor retract itself, and the
    # string never moved. Not `fixed` -- nobody fixed anything.
    invented = Finding(locale="de", file=lone[0], string_id=lone[1],
                       category="B", check="llm", summary="not an update title",
                       current="Guten Morgen", string_hash="same")
    inherited = Finding(locale="de", file=lone[0], string_id=lone[1],
                        category="E", check="typography",
                        summary="three dots", string_hash="same")
    imported = Finding(locale="de", file=lone[0], string_id=lone[1],
                       category="B", check="legacy", summary="from the review",
                       string_hash="same")
    buckets = findings_mod.resolve(
        [invented, inherited, imported], {lone: _H()}, set(), "2026-08-25",
        rerunnable={"typography"}, still_raised={inherited.fid},
        still_raised_loose={inherited.rekey}, unreviewable={lone},
    )
    check(invented.status == "withdrawn" and buckets["withdrawn"] == [invented],
          "a model finding on a string with no en-US counterpart is withdrawn")
    check(invented.status != "fixed", "and never counted as fixed")
    check(inherited.status == "open",
          "a deterministic finding on the same string is left alone -- that "
          "check ran and speaks for itself")
    check(imported.status == "open",
          "so is an imported one: a person may have read an English this "
          "tree does not carry")

    selftest_lib.deliberate_flag_wiring(suite, project)

    # The reviewer's flag is the only way a finding reaches the top of the
    # pull request body, so it has to survive the parser and it has to be
    # refused where it could not mean anything.
    import summary as summary_mod

    abusive = dict(real, reads_as_deliberate=True,
                   summary="says the browser lies", current="vecchio")
    got, _, _ok = _llm.collect([_Block({"findings": [abusive]})], "it", tree)
    check(got and got[0].reads_as_deliberate,
          "a B/2 finding the reviewer flagged keeps the flag")
    cosmetic = dict(abusive, category="E", impact=4)
    got, _, _ok = _llm.collect([_Block({"findings": [cosmetic]})], "it", tree)
    check(got and not got[0].reads_as_deliberate,
          "the same flag on a typography finding is dropped: spacing cannot "
          "put words in the product's mouth")
    plain, _, _ok = _llm.collect([_Block({"findings": [real]})], "it", tree)
    check(plain and not plain[0].reads_as_deliberate,
          "and an ordinary mistranslation is not flagged by default")

    flagged = Finding(locale="it", file="a.ftl", string_id="x", category="B",
                      impact=2, summary="s", reads_as_deliberate=True)
    quiet = Finding(locale="it", file="a.ftl", string_id="y", category="B",
                    impact=2, summary="s")
    broke = Finding(locale="it", file="a.ftl", string_id="z", category="A",
                    impact=1, summary="s")
    check(findings_mod.deliberate([flagged, quiet, broke]) == [flagged],
          "the escalation list is the flag, not the impact")
    check(findings_mod.broken([flagged, quiet, broke]) == [broke],
          "and impact 1 is its own axis, not a slice of the flagged ones")
    closed = Finding(locale="it", file="a.ftl", string_id="w", category="B",
                     impact=2, summary="s", reads_as_deliberate=True,
                     status="fixed")
    check(findings_mod.deliberate([closed]) == [],
          "a flagged finding that was fixed does not stay at the top")

    # Adding the flag must not re-key anything: a backlog of thousands would
    # otherwise reappear as new findings the first time one was set.
    check(flagged.identity() == Finding(
              locale="it", file="a.ftl", string_id="x", category="B",
              impact=2, summary="s").identity(),
          "the flag is outside the finding's identity")

    # The body quotes real UI text, which contains real backticks.
    check(summary_mod._code("a `code` b").startswith("``"),
          "an inline quote is fenced longer than the backticks inside it")
    check("…" in summary_mod._code("x" * 400),
          "and a long string is cut with a visible ellipsis")

    many = [(loc, quiet) for loc in ("aa", "bb") for _ in range(5)]
    listed = summary_mod._listing(many, cap=8, per_locale=2)
    check(listed.count("**`aa`**") == 2 and listed.count("**`bb`**") == 2,
          "the impact-1 sample gives every locale a turn instead of "
          "spending its whole budget on the first one alphabetically")
    check("and 6 more" in listed,
          "and says how many it left out, so a capped list is not read as "
          "the whole of it")

    suite.section("Suppression rules")
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

    suite.section("Baseline partitioning")
    # The partition patterns are written against the paths a message key uses.
    # Rooted at the localization *repository* instead of the locale tree,
    # every path gains a locale prefix, nothing matches, and all 45,440 files
    # of all 230 locales land in `other` -- the eight-way split silently
    # stops existing, which nothing else notices.
    import llm_baseline
    it = trees["it"]
    buckets = llm_baseline.partition_files(
        it.root, tuple(project.extensions), files=sorted(it.l10n_files)
    )
    check(len(buckets) > 1,
          f"the tree splits into {len(buckets)} partitions, not one bucket")
    check(sum(len(v) for v in buckets.values()) == len(it.l10n_files),
          "and every file in the tree is assigned to exactly one of them")
    catchall = len(buckets.get(llm_baseline.CATCHALL, []))
    check(catchall < len(it.l10n_files) // 4,
          f"the catch-all holds {catchall} of {len(it.l10n_files)} files, "
          "not the whole tree")
    # What comes back as `covered` becomes `reviewed_keys`, so it has to be
    # in the same path space as a message key.
    covered = set().union(*buckets.values())
    check(covered >= {k[0] for k in it.l10n},
          "the partitioned paths are the ones messages are keyed by, so a "
          "baseline can say which strings it reviewed")

    # Everything that needs no clone lives in one place, so CI can run it on
    # a bare checkout. Run it here too: a suite nobody invokes locally rots.
    import selftest_unit
    selftest_unit.run(suite)

    return suite.report()


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

#!/usr/bin/env python3
"""Regression tests that need no clone of anything.

The three project suites pin real defects against real repositories, which
is what makes them worth having and also what stops them running anywhere a
1.6 GB checkout is not already on disk. Everything here is pure logic --
finding identity, the lifecycle, suppression, the model-response parser, the
snapshot delta, and the markdown the site publishes -- so it runs in CI on a
bare checkout, and each of these is a bug that actually shipped.

    python lib/selftest_unit.py
"""

from __future__ import annotations

import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import findings as fm  # noqa: E402
import llm_baseline  # noqa: E402
import llm_incremental as llm  # noqa: E402
import report  # noqa: E402
import run as runner  # noqa: E402
import selftest_lib  # noqa: E402
import snapshot  # noqa: E402
import suppress  # noqa: E402
from findings import Finding  # noqa: E402
from parse import Msg  # noqa: E402


def _f(**kw):
    base = dict(locale="it", file="a.ftl", string_id="s", category="A",
                check="markup", summary="x", current="v")
    base.update(kw)
    return Finding(**base)


class _Block:
    type = "tool_use"

    def __init__(self, payload):
        self.input = payload


def _pattern_with_option(form):
    """A one-placeable Fluent pattern, optionally parameterized."""
    from moz.l10n.model import Expression, PatternMessage

    options = {"form": form} if form is not None else {}
    return PatternMessage(
        ["dans une ", Expression("-brand", function="message", options=options)]
    )


def run(suite) -> None:
    check = suite.check

    # --- the content hash sees placeable options --------------------------
    suite.section("A term parameter is part of the string, so it is part of the hash")
    # `_flatten` renders a term reference as its name and drops the
    # arguments, so these two flatten identically. They are different words
    # on screen, and fr changed one to the other as a fix: hashing them
    # alike made the fix invisible, the finding uncloseable, and kept the
    # string out of every subsequent delta.
    plural = Msg(file="a.ftl", id="s", props={"": "dans une { -brand }"},
                 raw={"": _pattern_with_option("lower-plural")})
    singular = Msg(file="a.ftl", id="s", props={"": "dans une { -brand }"},
                   raw={"": _pattern_with_option("lower-singular")})
    check(plural.text() == singular.text(),
          "the flattened text is deliberately identical -- reports stay readable")
    check(plural.hash() != singular.hash(),
          "but the hash separates them, so changing the form reads as movement")
    bare = Msg(file="a.ftl", id="s", props={"": "dans une { -brand }"},
               raw={"": _pattern_with_option(None)})
    check(bare.hash() == Msg(file="a.ftl", id="s",
                             props={"": "dans une { -brand }"}).hash(),
          "a message with no options hashes exactly as before, so correcting "
          "this does not invalidate every stored anchor")

    # --- finding identity -------------------------------------------------
    suite.section("Two complaints about one string are two findings")
    stored, raised = fm.merge(
        [], [_f(summary="Malformed closing tag"), _f(summary="data-l10n-name mismatch")], "D"
    )
    check(len(stored) == 2 and len(raised) == 2,
          "two distinct markup defects on one string are stored separately")
    stored, raised = fm.merge(
        [], [_f(check="variables", summary="references x"),
             _f(check="selectors", summary="switches on x")], "D")
    check(len(stored) == 2, "so are two different checks reporting category A")
    stored = [_f(check="typography", category="E", summary="straight apostrophe")]
    stored, _ = fm.merge(stored, [_f(check="llm", category="E", summary="odd wording")], "D")
    check(len(stored) == 2,
          "and a model finding never overwrites a check finding on the same string")

    suite.section("A check adopts the import it re-derives")
    # 4,346 stored findings came from the hand-written reviews and carry
    # `legacy` rather than a check name -- and a `fid` computed by the
    # importer, which the current identity() does not reproduce. So they can
    # never match by fid, and the loose fallback is the only thing that ever
    # reunited them with the check that now derives the same defect. Adding
    # `check` to that key forked every one of them into a duplicate, which is
    # how this rule earned its own test.
    same = "drops ['appLanguage'], which en-US passes"
    imported = _f(check="legacy", summary=same, status="open", fid="stale00legacy")
    imported.first_seen = "2026-07-01"
    stored, raised = fm.merge([imported], [_f(check="variables", summary=same)], "D")
    check(len(stored) == 1 and not raised, "the import is adopted, not duplicated")
    check(stored[0].check == "variables",
          "and now names the check, so the next run can resolve it authoritatively")
    check(stored[0].first_seen == "2026-07-01", "keeping the date it was first raised")

    two = [_f(check="legacy", summary="one", fid="stale01"),
           _f(check="legacy", summary="two", fid="stale02")]
    stored, _ = fm.merge(two, [_f(check="variables", summary="three")], "D")
    check(len(stored) == 3,
          "but two imports on one string are ambiguous, so neither is adopted")

    model = _f(check="llm", category="E", summary="odd wording", fid="stale03")
    stored, _ = fm.merge([model], [_f(check="typography", category="E",
                                      summary="straight apostrophe")], "D")
    check(len(stored) == 2,
          "and a model finding is never adopted: two observers, two records")

    suite.section("But a reworded complaint is still the same complaint")
    was = _f(summary="Malformed closing tag")
    was.first_seen = "2026-01-01"
    stored, raised = fm.merge([was], [_f(summary="Malformed closing tag `</a >`")], "D")
    check(len(stored) == 1 and not raised, "rewording does not duplicate the finding")
    check(stored[0].first_seen == "2026-01-01", "and does not reset its history")
    check(stored[0].summary.endswith("`</a >`"), "while the wording is refreshed")

    # --- lifecycle --------------------------------------------------------
    suite.section("Silence from the reviewer closes nothing a check answers for")
    key = {("a.ftl", "s")}

    def closed(check_name, rerunnable):
        f = _f(check=check_name, category="E", string_hash="old", status="open")
        fm.close_reviewed([f], key, set(), key, "D", rerunnable)
        return f.status

    check(closed("typography", {"typography"}) == "open",
          "a check finding stays open when its check ran and re-raised it")
    check(closed("typography", {"markup"}) == "fixed",
          "a check skipped this run falls back to the reviewer")
    check(closed("llm", {"typography"}) == "fixed",
          "and a model finding the reviewer re-read in silence still closes")

    suite.section("A quoted fragment is compared in the shape the parser keeps")
    # The reviewer quotes the file; the snapshot holds `parse.flatten` output.
    # Each of these was a real finding whose `current` could never match, so
    # `verdict` called it "gone" and it was one unrelated edit from closing
    # itself as fixed.
    for label, quoted, stored_text, sid in (
        ("the whole source line", "check = Check", "Check", "check"),
        ("an attribute line", "user-context-color-purple =\n    .label = Violeta",
         "label: Violeta", "user-context-color-purple"),
        ("one variant of a select", "*[no-cases] Spusťte webmail",
         "[with-cases] Spouštějte stránky [no-cases] Spusťte webmail", "s"),
        ("a term with arguments", 'Skryjte s { -vpn-name(case: "ins") }.',
         "Skryjte s { -vpn-name }.", "s"),
        ("a NUMBER() call", "= { NUMBER($result, maximumSignificantDigits: 9) }",
         "= { $result }", "s"),
    ):
        check(fm.still_present(quoted, stored_text, sid),
              f"a fragment quoting {label} is found in the parsed message")

    check(not fm.still_present("x = Wrong", "Right", "x"),
          "while a fragment that really is gone still reads as gone")
    check(fm.as_parsed("x = a = b", "x") == "a = b",
          "only the message's own id is stripped, never an `=` inside the value")
    check(fm.as_parsed("[Anlage: { $type }]", "s") == "[Anlage: { $type }]",
          "and bracketed prose is not mistaken for a variant key")
    check(fm.verdict("</a >", "</a>", True) == "gone"
          and fm.verdict("INDIRIZZO", "Indirizzo", True) == "gone",
          "comparison stays literal: punctuation and case are still real fixes")

    # Canonical equivalence is not a fold: these are the same characters,
    # written two ways. The reviewer quotes \u0921 + nukta where the file
    # holds \u095c, and ten Hindi findings across Android and iOS read as
    # absent from strings they are verbatim in.
    decomposed = "\u0906\u092a\u0915\u0947 \u0926\u094d\u0935\u093e\u0930\u093e \u091c\u094b\u0921\u093c\u0947"
    composed = "\u0906\u092a\u0915\u0947 \u0926\u094d\u0935\u093e\u0930\u093e \u091c\u094b\u095c\u0947 \u0938\u093e\u0907\u091f\u094b\u0902"
    check(decomposed not in composed, "the two spellings are not the same bytes")
    check(fm.still_present(decomposed, composed, "s"),
          "but a quote differing only in Unicode composition is found")
    check(fm.verdict(decomposed, composed, True) == "unclear",
          "so it is not read as a fix the moment the string is edited")

    suite.section("A string that never moved cannot have been fixed")
    check(fm.verdict("uncomparable quote", "some other text", False) == "unclear",
          "an absent fragment on an unmoved string means the quote is unusable")
    check(fm.verdict("uncomparable quote", "some other text", True) == "gone",
          "the same fragment on a string that did move is a fix")
    check(fm.verdict("uncomparable quote", "some other text", None) == "gone",
          "and with nothing recorded either way the old reading stands")

    suite.section("Parking a finding does not eat the evidence that parked it")
    # "unclear": the string moved, but the quoted text survives inside it, so
    # matching cannot say whether the edit was the fix.
    msg = Msg(file="a.ftl", id="s", props={"": "a quoted fragment, now in context"})
    f = _f(check="llm", current="a quoted fragment", string_hash="raised@")
    got = fm.resolve([f], {("a.ftl", "s"): msg}, {("a.ftl", "s")}, "D")
    check(f.status == "needs-recheck" and len(got["recheck"]) == 1,
          "an unresolvable finding on a changed string is parked")
    check(f.string_hash == "raised@",
          "and keeps the hash from when it was raised -- re-anchoring here is "
          "what closed every route back out of the bucket")
    got = fm.resolve([f], {("a.ftl", "s"): msg}, {("a.ftl", "s")}, "E")
    check(f.status == "needs-recheck" and not got["recheck"],
          "a second run leaves it parked without re-announcing it")

    # --- suppression ------------------------------------------------------
    suite.section("Suppression stays reversible")
    rule = suppress.Rule({"id": "r", "reason": "why", "match": {"check": "markup"}}, 0)
    f = _f()
    suppress.apply([rule], [f])
    check(f.status == "suppressed", "a matching rule suppresses")
    narrowed = suppress.Rule({"id": "r", "reason": "why", "match": {"check": "plurals"}}, 0)
    suppress.apply([narrowed], [f])
    check(f.status == "open" and not f.suppressed_by,
          "narrowing a rule while keeping its id brings the finding back")
    hand = _f(status="dismissed", dismissed_because="read it, it is fine")
    suppress.apply([rule], [hand])
    check(hand.status == "dismissed" and hand.dismissed_because == "read it, it is fine",
          "a class rule does not overwrite a hand dismissal or its reason")

    # --- the model response parser ----------------------------------------
    suite.section("A malformed model reply loses the item, never the batch")
    tree = {("a.ftl", "s"): Msg(file="a.ftl", id="s", props={"": "v"})}
    good = dict(string_id="s", file="a.ftl", category="B", impact=2, summary="x")
    for label, payload, want_ok in (
        ("a bare string in the findings list", ["oops"], True),
        ("a non-integer impact", [dict(good, impact="high")], True),
        ("an out-of-range impact", [dict(good, impact=9)], True),
        ("an unknown category", [dict(good, category="Z")], True),
        ("a findings field that is not a list", "everything is fine", False),
    ):
        found, malformed, ok = llm.collect([_Block({"findings": payload})], "it", tree)
        check(ok is want_ok, f"{label}: response usable = {ok}")
    found, _, _ = llm.collect([_Block({"findings": [dict(good, impact="high")]})], "it", tree)
    check(found and found[0].impact in fm.IMPACT,
          "a nonsense impact falls back to the category default instead of raising")
    found, _, _ = llm.collect([_Block({"findings": [dict(good, category="Z")]})], "it", tree)
    check(found and found[0].category in fm.CATEGORIES,
          "an unknown category is forced into one the report actually renders")
    check(not llm.collect([_Block({"findings": [dict(good, summary="  ")]})], "it", tree)[0],
          "a finding with nothing to say is dropped")
    check(llm.collect([], "it", tree)[2] is False,
          "a reply with no tool call at all is not evidence of a clean review")

    suite.section("A finding is filed against the string it quotes")
    # The model carried a neighbour's id across a batch: a hi-IN typo was
    # filed on the addons permission dialog while quoting the address
    # prompt. The id existed, so nothing rejected it, the hash came from the
    # wrong message, and `resolve` -- which asks whether *that* string moved
    # -- could never close it. The typo was fixed the same day.
    two = {("a.ftl", "s"): Msg(file="a.ftl", id="s", props={"": "the addons dialog"}),
           ("a.ftl", "t"): Msg(file="a.ftl", id="t", props={"": "update the address?"})}
    misfiled = dict(string_id="s", file="a.ftl", category="B", impact=2,
                    summary="typo", current="update the address?")
    found, _, _ = llm.collect([_Block({"findings": [misfiled]})], "it", two)
    check(found and found[0].string_id == "t",
          "the quote decides: the finding is re-filed on the string it is about")
    check(found and found[0].string_hash == two[("a.ftl", "t")].hash(),
          "and anchored to that string, so a later fix to it can be seen")

    nowhere = dict(misfiled, current="text that is in no string at all")
    check(not llm.collect([_Block({"findings": [nowhere]})], "it", two)[0],
          "a quote in no single string leaves an anchor nobody can trust: dropped")

    ambiguous = dict(two)
    ambiguous[("a.ftl", "u")] = Msg(file="a.ftl", id="u",
                                    props={"": "update the address?"})
    check(not llm.collect([_Block({"findings": [misfiled]})], "it", ambiguous)[0],
          "and two strings carrying the quote are no better than none: the "
          "same value is duplicated across apps all the time")

    short = {("a.ftl", "s"): Msg(file="a.ftl", id="s", props={"": "\u5c0f\u7d2b"})}
    kept = dict(misfiled, current="\u5c0f\u7d2b")
    check(llm.collect([_Block({"findings": [kept]})], "it", short)[0],
          "a quote too short to weigh is left alone, not thrown away")

    # --- baseline coverage ------------------------------------------------
    suite.section("A partition that failed was not reviewed")
    ok = llm_baseline.Outcome("p", True, findings=[])
    bad = llm_baseline.Outcome("p", False, reason="timed out")
    check(ok.ok and not bad.ok, "clean and failed are distinguishable outcomes")
    check(bad.reason, "and a failure carries why, for the report to repeat")
    for payload in ([], {}, {"findings": "clean"}):
        items, _ = llm_baseline._finding_items(payload)
        check(items is None, f"malformed baseline findings are rejected ({payload!r})")
    items, error = llm_baseline._finding_items({"findings": []})
    check(items == [] and error is None, "an explicit empty findings list is clean")
    tree = {("a.ftl", "s"): Msg(file="a.ftl", id="s", props={"": "v"})}

    class _UnexpectedFailure(dict):
        def get(self, *_args, **_kwargs):
            raise RuntimeError("unexpected conversion failure")

    converted, malformed = llm_baseline._convert_findings(
        [good, "bad", dict(good, summary=3), _UnexpectedFailure()], "it", tree
    )
    check(len(converted) == 1 and malformed == 3,
          "malformed baseline items do not discard valid siblings")

    suite.section("Checks-only state preserves completed review history")
    check(runner.pick_mode("auto", False) == "baseline",
          "a new checks-only locale still needs its baseline")
    check(runner.pick_mode("auto", True) == "incremental",
          "an established locale resumes incrementally after a checks-only run")
    check(runner.pick_mode("auto", False) == "baseline",
          "a missing review snapshot always requires a baseline")

    suite.section("Each project loads its own check registry")
    firefox_checks = runner.load_checks(config.load("firefox")).CHECKS
    android_checks = runner.load_checks(config.load("android")).CHECKS
    check("term_params" in firefox_checks and "term_params" not in android_checks,
          "Firefox-only checks do not leak into Android")
    check("escaping" in android_checks and "escaping" not in firefox_checks,
          "Android-only checks do not leak into Firefox")
    focus_checks = runner.load_checks(config.load("focus_android")).CHECKS
    check(focus_checks["escaping"] is android_checks["escaping"],
          "the two Android projects share one escaping check, not two copies")

    suite.section("Context strings are looked up, never checked")
    import common_checks as _cc

    def _m(file, ident, text):
        return Msg(file=file, id=ident, props={"": text})

    # Focus quotes an Android Components button. Focus does not own that
    # string, so it arrives as context: a candidate the label can name,
    # never a string a finding is raised on.
    ac = "ac/values/strings.xml"
    own = "focus/values/strings.xml"
    src = {(own, "tip"): _m(own, "tip", "Select \u201cTry Again\u201d to retry")}
    loc = {(own, "tip"): _m(own, "tip", "Seleziona \u201cRiprova\u201d per riprovare")}
    ctx_src = {(ac, "retry"): _m(ac, "retry", "Try Again")}
    ctx_loc = {(ac, "retry"): _m(ac, "retry", "Riprovare")}
    found = _cc.check_ui_references("it", loc, src, ctx_loc, ctx_src)
    check([f.string_id for f in found] == ["tip"],
          "a label quoting a context string is checked against it")
    check(not _cc.check_ui_references("it", loc, src),
          "without the context there is nothing to point at, and nothing is said")
    found = _cc.check_ui_references("it", ctx_loc, ctx_src, loc, src)
    check(not found, "a context string is never the one a finding is raised on")

    from layout import Trees
    t = Trees(l10n={(own, "a"): _m(own, "a", "uno")},
              context_conventions={(ac, "b"): _m(ac, "b", "due")})
    check(set(t.measured()) == {(own, "a"), (ac, "b")} and set(t.l10n) == {(own, "a")},
          "conventions count the context, and the checked tree does not grow")
    missing = type("Project", (), {
        "tools_dir": "/definitely-not-a-project/tools", "name": "missing"
    })()
    try:
        runner.load_checks(missing)
    except RuntimeError as exc:
        check("does not exist" in str(exc), "a missing checks module fails clearly")
    else:
        check(False, "a missing checks module fails clearly")

    suite.section("The health table never prints a check that did not run")
    import common_checks as cc
    h = cc.Health(ran=["typography"], counts={"typography": 3})
    table = report._health_table(h)
    check("Typography deviations" in table, "a check that ran is listed with its count")
    check("Plural / select selector" not in table,
          "one the project does not run is left out, not printed as zero -- a "
          "zero says we looked")
    h = cc.Health(ran=["typography"], counts={"typography": 0}, skipped=["accesskey"])
    check("_skipped for this locale_" in report._health_table(h),
          "and a locale-level skip still says so")

    # --- the snapshot delta -----------------------------------------------
    suite.section("A changed en-US comment re-queues the string")
    def tree_of(value, comment):
        return {("f", "s"): Msg(file="f", id="s", props={"": value}, comment=comment)}

    loc = tree_of("trad", "")
    before = snapshot.build(loc, tree_of("src", "Count of open tabs"))
    after = snapshot.build(loc, tree_of("src", "Count of CLOSED tabs"))
    check(snapshot.diff(before, after).to_review == [("f", "s")],
          "a comment-only change to the source queues the translation")
    legacy = {"f": {"s": " ".join(before["f"]["s"].split(" ")[:2])}}
    check(snapshot.diff(legacy, after).to_review == [],
          "but a snapshot written before comments were tracked re-reviews nothing")

    # --- what the site publishes -----------------------------------------
    suite.section("A finding's details nest under it on the published page")
    # Python-Markdown flattens a two-space nested list, so the quoted string
    # and the suggestion came out as siblings of the finding rather than
    # under it. Pinned for both renderers: the per-locale report was fixed
    # for this first and the cross-locale summary kept its own indent.
    import summary as summary_mod
    f = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                summary="wrong word", current="valore", suggest="corretto")
    for label, text in (("locale report", report._item(f, report.Ctx())),
                        ("summary and PR body", summary_mod._one(f, "it"))):
        rendered = _render(text)
        check(rendered.count("<ul>") == 2,
              f"the details are one list inside the finding's own ({label})")

    suite.section("A translation cannot inject active content")
    payload = 'x` [click](javascript:alert(1)) ![p](https://evil.example/t.png)'
    for value in ("a`b", "``x``", "`lead", "trail`"):
        rendered = _render(f"- Current: {report.fence(value)}")
        inside = re.findall(r"<code>(.*?)</code>", rendered)
        check(inside and html.unescape(inside[0]).strip() == value,
              f"a value containing backticks survives whole inside one code "
              f"span ({value!r})")
    for field in ("current", "suggest", "summary", "rationale"):
        kw = dict(locale="it", file="a.ftl", string_id="s", category="B",
                  summary="ok", current="v")
        kw[field] = payload
        body = _render(report._item(Finding(**kw), report.Ctx()))
        live_href = re.findall(r'(?<!blocked-)href="([^"]*)"', body)
        live_src = re.findall(r'(?<!blocked-)src="([^"]*)"', body)
        check(not live_href and not live_src,
              f"a payload in `{field}` reaches the page as text, with no live "
              f"href or src")
    check(_safe("#/it/firefox") and _safe("android.md") and _safe("../x.html"),
          "while the links the reports really use are kept")
    check(not _safe("javascript:alert(1)") and not _safe("data:text/html,x")
          and not _safe("&#106;avascript:x"),
          "and obfuscated script URLs are refused")
    check(
        all(not _site()._safe_url(url, "src")
            for url in ("//evil.example/pixel.png", "\\\\evil.example/pixel.png")),
        "protocol-relative remote images are refused too",
    )

    # --- the QA digest -----------------------------------------------------
    suite.section("The digest merges only what needs no person")
    import digest
    ok = [{"__typename": "CheckRun", "name": "checks", "status": "COMPLETED",
           "conclusion": "SUCCESS"},
          {"__typename": "CheckRun", "name": "semgrep", "status": "COMPLETED",
           "conclusion": "SKIPPED"}]
    check(digest.check_problems(ok) == [], "green checks allow a merge")
    check(digest.check_problems([]),
          "no checks at all is not a pass: `checks` is required")
    waiting = [dict(ok[0], conclusion="ACTION_REQUIRED")]
    check(any("approve" in p for p in digest.check_problems(waiting)),
          "a run waiting for approval says so, rather than 'failed'")
    check(digest.check_problems([dict(ok[0], status="IN_PROGRESS",
                                      conclusion=None)]),
          "a check still running blocks the merge")
    check(digest.check_problems(ok + [{"__typename": "StatusContext",
                                       "context": "x", "state": "FAILURE"}]),
          "and so does any other failing status, not only `checks`")

    suite.section("The suggestions workflow merges only a green, unmoved head")
    green = {"number": 9, "state": "OPEN", "headRefOid": "abc", "statusCheckRollup": ok}
    pending = dict(green, statusCheckRollup=[dict(ok[0], status="IN_PROGRESS",
                                                  conclusion=None)])
    merged = []
    real_merge = digest.merge
    digest.merge = lambda out: merged.append(out.pr["number"])
    try:
        views = iter([dict(green, statusCheckRollup=[]), pending, green])
        why = digest.wait_and_merge("b", "abc", view=lambda: next(views),
                                    sleep=lambda s: None)
        check(why == "" and merged == [9],
              "it waits through checks not yet started or running, then merges")
        merged.clear()
        why = digest.wait_and_merge("b", "abc", view=lambda: dict(
            green, statusCheckRollup=waiting), sleep=lambda s: None)
        check(not merged and "approve" in why,
              "a run waiting for approval is not waited on, and not merged")
        why = digest.wait_and_merge("b", "abc", view=lambda: dict(green, headRefOid="def"),
                                    sleep=lambda s: None)
        check(not merged and "moved" in why, "a branch that moved is not merged")
        clock = iter([0, 0, 10_000])
        why = digest.wait_and_merge("b", "abc", timeout=60, view=lambda: pending,
                                    sleep=lambda s: None, now=lambda: next(clock))
        check(not merged and "timed out" in why, "and the wait has an end")

        # 2026-11-09: four projects' pull requests merged within a second of
        # each other and GitHub refused android's with this; it sat open.
        refusal = ("merging failed: GraphQL: Base branch was modified. Review "
                   "and try the merge again. (mergePullRequest)")
        attempts = []

        def racing(out):
            attempts.append(out.pr["number"])
            if len(attempts) == 1:
                out.reasons.append(refusal)
        digest.merge = racing
        why = digest.wait_and_merge("b", "abc", view=lambda: green,
                                    sleep=lambda s: None)
        check(why == "" and attempts == [9, 9],
              "a merge refused because another landed at once is retried")
        attempts.clear()
        views = iter([green, dict(green, headRefOid="def")])
        why = digest.wait_and_merge("b", "abc", view=lambda: next(views),
                                    sleep=lambda s: None)
        check(attempts == [9] and "moved" in why,
              "and the retry still refuses a branch that moved meanwhile")

        def refused(out):
            out.reasons.append(refusal)
        digest.merge = refused
        clock = iter([0, 0, 10_000])
        why = digest.wait_and_merge("b", "abc", timeout=60, view=lambda: green,
                                    sleep=lambda s: None, now=lambda: next(clock))
        check("Base branch was modified" in why,
              "a refusal past the deadline is reported as GitHub gave it")

        digest.merge = lambda out: out.reasons.append("merging failed: other")
        why = digest.wait_and_merge("b", "abc", view=lambda: green,
                                    sleep=lambda s: None)
        check(why == "merging failed: other", "any other merge failure is final")
    finally:
        digest.merge = real_merge

    suite.section("The fixer closes what it cannot stand behind, and only that")
    # fy-NL, 2026-11-05: "'Ljepblêd oanpasse' may be the localized name for
    # custom tabs" came back as `skip`, which records nothing, and group B
    # never ran again -- so a finding the fixer doubted stayed open for good.
    import autosuggest
    import json as _json
    v = lambda verdict, reason="r": {"verdict": verdict, "reason": reason}  # noqa: E731
    reason, why = autosuggest.closing({"a": v("unreliable", "may be the usual term")}, 0)
    check(reason == "unreliable finding: may be the usual term" and why is None,
          "a doubted finding is closed, and its reason says it was doubted, not disproved")
    reason, _ = autosuggest.closing({"a": v("false_positive", "en-US has it too"),
                                     "b": v("unreliable", "stylistic")}, 0)
    check(reason == "en-US has it too; unreliable finding: stylistic",
          "a string whose findings are all doubted or wrong is closed with every reason")
    check(autosuggest.closing({"a": v("skip")}, 0) == (None, None),
          "a real defect too big for a small edit stays open")
    check(autosuggest.closing({"a": v("unreliable"), "b": v("skip")}, 0) == (None, None)
          and autosuggest.closing({"a": v("unreliable"), "b": v("fix")}, 0) == (None, None),
          "and keeps its string open: a dismissal covers the whole string")
    reason, why = autosuggest.closing({"a": v("unreliable")}, 2)
    check(reason is None and "2 other open finding(s)" in why,
          "so does an open finding outside this run's groups, and the log says so")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "prompts", "fix_schema.json"), encoding="utf-8") as fh:
        enum = (_json.load(fh)["input_schema"]["properties"]["strings"]["items"]
                ["properties"]["findings"]["items"]["properties"]["verdict"]["enum"])
    check(set(autosuggest.CLOSING) | {"fix", "skip"} == set(enum),
          "every verdict the model may give is handled, and nothing else")

    suite.section("A group picks the strings, and each string brings all its findings")
    # fy-NL `page-info-page`: a group-E run fixed its E finding and sent
    # that, and its C finding ('syd' for 'side') was never in front of the
    # model. 31 of 1029 suggestions left another group's finding behind.
    import autosuggest as _as
    e1 = _f(string_id="s1", category="E", fid="e1")
    c1 = _f(string_id="s1", category="C", fid="c1")
    c2 = _f(string_id="s2", category="C", fid="c2")
    asked = _f(string_id="s1", category="B", fid="b1")
    gone = _f(string_id="s3", category="E", fid="e3")
    recs = [{"file": "a.ftl", "string_id": "s1", "fids": ["b1"], "status": "rejected",
             "original": "o", "text": "t"}]
    got, held, added = _as.select([e1, c1, c2, asked, gone], ["E"], recs, {("s3", None): "fine"})
    check([f.fid for f in got] == ["e1", "c1"],
          "an E run takes the string with an E finding, and its C finding with it")
    check(added == 1 and held == 1,
          "and says how many came from other groups and how many were held back")
    check("b1" not in [f.fid for f in got],
          "a finding already asked about on that string stays out")
    got, _, _ = _as.select([c1, c2], ["E"], [], {})
    check(got == [], "a string with nothing in the group is not touched")
    pending = [dict(recs[0], status="pending")]
    got, held, _ = _as.select([e1, c1], ["E"], pending, {})
    check(got == [] and held == 1, "nor is one with a suggestion still pending")

    suite.section("A fix to an attribute is seen as a fix, and a string can be suggested again")
    # fy-NL, 2026-11-05: `.label = Fragen…` → `Freegje…` was compared as
    # `F` → `F` (the access key, all Pontoon's simple rendering shows), and
    # dropped as "Pontoon already has this translation" -- 27 fixes for one
    # locale. And `set-password-message`, suggested once for one finding,
    # could never be suggested for its typo.
    import tempfile as _tf

    import pontoon_review as _pr
    import suggest as _sg
    import tracker as _tr
    from moz.l10n.formats import Format as _Fmt
    with _tf.TemporaryDirectory() as tmp:
        ftl = os.path.join(tmp, "genai.ftl")
        with open(ftl, "w", encoding="utf-8") as fh:
            fh.write("ask =\n    .label = Fragen…\n    .accesskey = F\n"
                     "fixed =\n    .label = Freegje…\n    .accesskey = F\n"
                     "plain = Iepenje\n")
        _, entries = _sg._entries(ftl)
    ask, fixed, plain = entries[("ask",)], entries[("fixed",)], entries[("plain",)]
    check(_sg.pontoon_preview(_Fmt.fluent, ask) == _sg.pontoon_preview(_Fmt.fluent, fixed) == "F",
          "Pontoon's simple rendering of the two is the same access key")
    check(_sg.full_preview(_Fmt.fluent, ask) == ".accesskey = F\n.label = Fragen…"
          and _sg.full_preview(_Fmt.fluent, fixed) != _sg.full_preview(_Fmt.fluent, ask),
          "the full rendering shows the label, and tells the fix from the original")
    check(_sg.full_preview(_Fmt.fluent, plain) == _sg.pontoon_preview(_Fmt.fluent, plain),
          "and for a message with no attributes it is just the preview")
    change = {"old": "F", "new": "F"}
    check(_sg.check_against_pontoon(change, "F") == "",
          "a change Pontoon's rendering cannot show is sent, not taken as already there")
    check("moved on" in _sg.check_against_pontoon(change, "G"),
          "but Pontoon having moved in the part it does show still stops it")
    seen = {"old": "Fragen", "new": "Freegje"}
    check(_sg.check_against_pontoon(seen, "Freegje") == "Pontoon already has this translation"
          and "moved on" in _sg.check_against_pontoon(seen, "Oars")
          and _sg.check_against_pontoon(seen, "Fragen") == "",
          "a change it can show is checked exactly as before")
    row = {"format": "fluent", "preview": "F", "value": [],
           "properties": {"label": ["Freegje…"], "accesskey": ["F"]}}
    check(_sg.full_preview_of_feed(row) == _sg.full_preview(_Fmt.fluent, fixed)
          and _sg.full_preview_of_feed({"format": "fluent", "properties": None}) is None,
          "the feed's whole message renders the same as the clone's")

    rec = lambda **kw: dict({"file": "a.ftl", "string_id": "s", "fids": ["f1"],  # noqa: E731
                             "status": "rejected", "original": "Fragen", "text": "Freegje"}, **kw)
    key = ("a.ftl", "s")
    check("waiting" in _tr.blocked([rec(status="pending")], key, ["f2"]),
          "a string waiting on a reviewer is not suggested again")
    check("same finding" in _tr.blocked([rec()], key, ["f1"]),
          "nor for a finding that was already asked about")
    check(_tr.blocked([rec()], key, ["f2"]) == ""
          and _tr.blocked([rec(status="approved")], key, ["f2"], now=("Freegje", "Freegje")) == "",
          "but a different finding on it can be")
    check("not reached" in _tr.blocked([rec(status="approved")], key, ["f2"],
                                       now=("Fragen", "Fragen")),
          "unless an approved fix has not reached the repository, which it would undo")
    check("exact text" in _tr.blocked([rec()], key, ["f2"], new=("Freegje", "Freegje")),
          "and never with a text that was rejected before, which would un-reject it")
    check(_tr.blocked([rec()], ("a.ftl", "other"), ["f1"]) == "",
          "another string is not affected")
    full = _tr.entry(date="d", group="C", file="a.ftl", string_id="s", server="x", slug="p",
                     resource="a.ftl", key=["s"], fids=["f1"], findings=[], source="",
                     original="F", text="F", full_original=".accesskey = F\n.label = Fragen…",
                     full_text=".accesskey = F\n.label = Freegje…")
    bare = _tr.entry(date="d", group="C", file="a.ftl", string_id="s", server="x", slug="p",
                     resource="a.ftl", key=["s"], fids=["f1"], findings=[], source="",
                     original="Fragen", text="Freegje", full_original="Fragen",
                     full_text="Freegje")
    check("full_text" in full and "full_text" not in bare,
          "a record keeps the full form only where it says more than the preview")
    full["pontoon"] = {"project": "p", "resource": "a.ftl", "key": ["s"]}
    other = dict(row, project="p", resource="a.ftl", entity="s", status="rejected",
                 properties={"label": ["Iets oars"], "accesskey": ["F"]}, date="2026-11-01")
    mine = dict(row, project="p", resource="a.ftl", entity="s", status="rejected",
                date="2026-11-02", translation_pk=7, rejected_date="2026-11-03")
    check(_pr.match(full, [other, mine]) is mine and _pr.match(full, [other]) is None,
          "the review tells two attribute suggestions apart by the whole message")
    got = _pr.decide(full, mine, full["full_original"], {"f1"})
    check(got["outcome"] == "dismissed",
          "and a rejection with the label unchanged is a rejection, not an adoption")
    check(_pr.decide(full, mine, full["full_text"], {"f1"})["outcome"] == "adopted",
          "while the label reaching the repository anyway is an adoption")

    suite.section("The fixer's dismissal lapses with the text it judged, and is not a person's")
    # A dismissal is keyed by string id. Written by the fixer about one text,
    # it went on hiding every finding raised on that string afterwards, on
    # any text, for good.
    import tempfile

    import dismiss as dz
    import summary as sm

    class _M:
        def __init__(self, h):
            self.h = h

        def hash(self):
            return self.h

    with tempfile.TemporaryDirectory() as tmp:
        dpath = os.path.join(tmp, "dismissed.txt")
        kept_person = "p @ a.xml — fine, I read it\n"
        kept_old = "o @ a.xml — auto-suggest (2026-11-02): no anchor, so never withdrawn\n"
        kept_same = dz.line("s", "a.xml", dz.FIXER_TAG, "2026-11-09", "r", "aaaa1111") + "\n"
        moved = dz.line("m", "a.xml", dz.FIXER_TAG, "2026-11-09", "r", "bbbb2222") + "\n"
        gone_str = dz.line("g", "a.xml", dz.FIXER_TAG, "2026-11-09", "r", "cccc3333") + "\n"
        rejected = "m @ a.xml — pontoon-rejected (2026-11-05): rejected in Pontoon: no\n"
        with open(dpath, "w", encoding="utf-8") as fh:
            fh.writelines([kept_person, kept_old, kept_same, moved, gone_str, rejected])
        msgs = {("a.xml", "p"): _M("x"), ("a.xml", "o"): _M("x"),
                ("a.xml", "s"): _M("aaaa1111"), ("a.xml", "m"): _M("dddd4444")}
        check(dz.withdraw_moved(dpath, msgs, write=False) == [moved.strip()]
              and moved in open(dpath, encoding="utf-8").read(),
              "a dry run names the lapsed line and leaves the file alone")
        out = dz.withdraw_moved(dpath, msgs)
        after = open(dpath, encoding="utf-8").read()
        check(out == [moved.strip()] and moved not in after,
              "the fixer's line goes once its string's text changes")
        check(all(x in after for x in (kept_person, kept_old, kept_same, gone_str, rejected)),
              "a person's line, a Pontoon rejection, an unanchored or unchanged one, "
              "and one whose string has left the tree all stay")
    check(dz.by_fixer("auto-suggest (2026-11-09, string ab12): unreliable finding: x")
          and dz.by_fixer("auto-suggest (2026-11-02): x")
          and not dz.by_fixer("pontoon-rejected (2026-11-05): rejected in Pontoon: no")
          and not dz.by_fixer("fine, I read it"),
          "the fixer's lines are told from a person's and from a Pontoon reviewer's")
    closed = {k: t for k, _, t in sm._CLOSED}
    mine = _f(status="dismissed", dismissed_because="auto-suggest (2026-11-09): x")
    theirs = _f(status="dismissed", dismissed_because="pontoon-rejected (2026-11-05): no")
    check(closed["fixer"](mine) and not closed["person"](mine)
          and closed["person"](theirs) and not closed["fixer"](theirs),
          "so the pull request counts the fixer's closures apart from people's")
    check(sum(1 for _, _, t in sm._CLOSED
              for f in (mine, theirs, _f(status="suppressed"), _f(status="fixed"))
              if t(f)) == 4,
          "and every closed finding lands in exactly one bucket")

    suite.section("A locale read-only in Pontoon is never worked on")
    check(config.load("firefox").pontoon_readonly("it"),
          "Italian is read-only for Firefox in Pontoon")
    check(not config.load("firefox_ios").pontoon_readonly("it"),
          "but not for iOS, where its suggestions were stored")

    suite.section("The digest email cannot be injected into either")
    fx = config.load("firefox")
    bad = Finding(locale="it", file="a.ftl", string_id="s", category="B",
                  impact=1, summary="ok",
                  current='<img src="https://evil.example/t.png"><script>x</script>')
    empty = {k: [] for k in ("first_run", "new", "reopened", "recheck", "gone",
                             "fixed", "withdrawn", "person", "fixer", "obsolete")}
    held = digest.Outcome(fx, pr={"number": 1, "url": "https://example/1"},
                          reasons=["it changes locale instructions"],
                          delta=dict(empty, locales={}))
    done = digest.Outcome(fx, pr={"number": 2, "url": "https://example/2"},
                          delta=dict(empty, locales={"it": {"new": 1, "net": 1}},
                                     new=[("it", bad)]), merged=True)
    subject, body = digest.compose([held, done], dry_run=False, today="x")
    check("not merged" in subject and body.index("Needs a person")
          < body.index("merged [#2]"),
          "a pull request left open leads the email and the subject")
    page = digest.to_html(body)
    check("<img" not in page and "<script" not in page and "&lt;img" in page,
          "a quoted translation reaches the HTML part as text")

    header = ("diff --git a/x/locales/it/dismissed.txt b/x/locales/it/dismissed.txt\n"
              "--- a/x/locales/it/dismissed.txt\n+++ b/x/locales/it/dismissed.txt\n"
              "@@ -5,0 +6 @@\n")
    tagged = "s @ a.xml — pontoon-rejected (2026-10-20): rejected in Pontoon: no"
    check(digest.only_tool_dismissals(header + "+" + tagged),
          "appended Pontoon dismissals do not hold the pull request")
    check(not digest.only_tool_dismissals(header + "+" + tagged + "\n+t — fine"),
          "but a person's own line alongside them does")
    check(not digest.only_tool_dismissals(
        header.replace("dismissed.txt", "conventions.md") + "+" + tagged),
          "and so does any other file under locales/")
    fixer = "s @ a.xml — auto-suggest (2026-11-09, string 59767936): unreliable finding: x"
    check(digest.only_tool_dismissals(header.replace("+6", "+5,0") + "-" + fixer),
          "a run withdrawing the fixer's line for a changed string does not hold it")
    check(not digest.only_tool_dismissals(header + "+" + fixer),
          "but the fixer's line being added in a QA pull request does")

    # --- Pontoon review outcomes ---------------------------------------------
    suite.section("A Pontoon review moves a suggestion on only as far as it shows")
    import datetime
    import tempfile

    import dismiss as dismiss_mod
    import pontoon_review as pr
    import suggest
    rec = {"file": "a.xml", "string_id": "s", "fids": ["f1"], "status": "pending",
           "original": "vecchio", "text": "nuovo",
           "pontoon": {"server": "https://p", "project": "fx", "resource": "a.xml",
                       "key": ["s"]}}

    # The feed's shape since mozilla/pontoon#4639: `preview` is Pontoon's
    # simple preview, `value`/`properties` the message in moz-l10n's model.
    def res(status, preview="nuovo", comments=(), entity="s"):
        return {"translation_pk": 1, "preview": preview, "value": [preview],
                "properties": None, "format": "android", "status": status,
                "date": "2026-10-10T00:00:00Z", "approved_date": None,
                "rejected_date": "2026-10-20T00:00:00Z" if status == "rejected" else None,
                "entity": entity, "resource": "a.xml", "project": "fx",
                "locale": "it", "url": "https://p/x", "comments": list(comments)}

    check(pr.decide(rec, None, "vecchio", {"f1"}) is None,
          "no answer from Pontoon leaves the record pending")
    check(pr.decide(rec, res("unreviewed"), "vecchio", {"f1"}) is None,
          "and so does an unreviewed suggestion")
    check(pr.match(rec, [res("rejected", preview="altro")]) is None,
          "a different suggestion on the same string is not this one")
    # Real cs answers from 2026-10-13: approved in Pontoon, read as pending.
    held = dict(rec, text="Smazáno „%1$s“ <b>teď</b>")
    mf2 = "Smazáno „{$arg1 :string @source=|%1$s|}“ {|<b>| :html}teď{|</b>| :html}"
    check(pr.match(held, [res("approved", preview="Smazáno „%1$s“ <b>teď</b>")]),
          "the feed's preview matches the text that was sent")
    check(pr.match(held, [res("approved", preview="Smazáno „%2$s“ <b>teď</b>")]) is None,
          "but a different placeholder in it does not")
    check(suggest.preview_of_api(mf2) == held["text"]
          and suggest.preview_of_api(mf2.replace("%1$s", "%2$s")) != held["text"],
          "the action log's raw MF2 reads back into the same form")
    # An upload whose text Pontoon already had: pt-BR, 2026-10-12. Pontoon
    # revived the older translation rather than storing one by the bot, and
    # the reviewer rejected that.
    def act(kind, pk, string, user=31119, implicit=False, when="2026-10-12T08:00:00Z",
            key=("s",), locale="it"):
        return {"type": f"translation:{kind}", "is_implicit_action": implicit,
                "date": when, "user": {"pk": user}, "locale": {"code": locale},
                "entity": {"key": list(key)}, "resource": {"path": "a.xml"},
                "translation": {"pk": pk, "string": string}}
    own = [dict(res("unreviewed"), translation_pk=9, entity="other")]
    anchor = act("created", 9, "x", key=("other",))
    revival = act("unrejected", 5, "nuovo")
    review = act("rejected", 5, "nuovo", user=377, when="2026-10-12T09:00:00Z")
    got = pr.revived(rec, "it", own, [anchor, revival], [anchor, revival, review])
    check(got and got["status"] == "rejected" and got["translation_pk"] == 5,
          "a revived translation's review is the suggestion's answer")
    check(pr.decide(rec, got, "vecchio", {"f1"})["outcome"] == "dismissed",
          "and is decided like any other rejection")
    check(pr.revived(rec, "it", own, [anchor, revival], [anchor, revival]) is None,
          "a revival nobody has reviewed yet stays pending")
    check(pr.revived(rec, "it", own, [anchor, revival],
                     [anchor, revival, dict(review, is_implicit_action=True)]) is None,
          "and an implicit rejection -- another translation approved -- is not an answer")
    check(pr.revived(rec, "it", own, [anchor, act("unrejected", 5, "nuovo", user=8)],
                     [anchor, review]) is None,
          "someone else reviving the same text is not the bot's suggestion")
    check(pr.revived(rec, "it", [], [revival], [revival, review]) is None,
          "with nothing of its own in the feed the bot cannot be told apart: pending")
    check(pr.revived(rec, "it", own, [anchor, act("unrejected", 5, "altro")],
                     [anchor, review]) is None,
          "a revival of different text is not this suggestion")
    check(pr.revived(rec, "it", own + [res("unreviewed")], [anchor, revival],
                     [anchor, revival, review]) is None,
          "and a string the bot's own feed has a row for is left to match()")
    ios = dict(rec, pontoon=dict(rec["pontoon"], key=["Shared/x.strings", "s"]))
    check(pr.match(ios, [res("rejected", entity="s • Shared/x.strings")]),
          "a two-part key matches Pontoon's innermost-first entity")
    approved = pr.decide(rec, dict(res("approved"), approved_date="2026-10-21T0"),
                         "vecchio", {"f1"})
    check(approved["outcome"] == "approved" and not approved["dismiss"],
          "an approval is recorded and closes nothing")
    check(pr.decide(rec, res("rejected"), "nuovo", {"f1"})["outcome"] == "adopted",
          "rejected, but the repository has the text anyway: not dismissed")
    moved = pr.decide(rec, res("rejected"), "diverso", {"f1"})
    check(moved["outcome"] == "moved" and not moved["dismiss"],
          "rejected after the string moved: the finding stays open")
    check(pr.decide(rec, res("rejected"), None, {"f1"})["outcome"] == "obsolete",
          "rejected, string gone: left to the lifecycle")
    kept = pr.decide(rec, res("rejected"), "vecchio", {"f1", "f2"})
    check(kept["outcome"] == "kept" and not kept["dismiss"],
          "another open finding on the string blocks the dismissal")
    check(pr.decide(dict(rec, fids=[]), res("rejected"), "vecchio", set())["outcome"]
          == "kept", "a suggestion sent without a finding dismisses nothing")
    plain = pr.decide(rec, res("rejected"), "vecchio", {"f1"})
    check(plain["dismiss"] and plain["needs_reason"] and plain["status_date"] == "2026-10-20",
          "rejected, unchanged, no comment: dismissed, and a reason is wanted")
    said = pr.decide(rec, res("rejected", comments=[
        {"author": {"username": "rev"}, "content": "keep  it"}]), "vecchio", {"f1"})
    check(said["dismiss"] and not said["needs_reason"]
          and pr.reason_for(said, None) == "rejected in Pontoon: rev: keep it",
          "with a comment, the comment is the reason")
    check("(inferred)" in pr.reason_for(plain, "too formal")
          and "reason unclear" in pr.reason_for(plain, "Unclear.")
          and "reason unclear" in pr.reason_for(plain, None),
          "an inferred reason says so, and 'unclear' is never dressed up")
    check(pr.decide(dict(rec, status="rejected", outcome="dismissed"),
                    res("rejected"), "vecchio", {"f1"}) is None,
          "an outcome already recorded is not decided again")

    span = pr.windows(datetime.date(2026, 8, 1), datetime.date(2026, 10, 30))
    check(len(span) == 3 and all((b - a).days <= pr.MAX_DAYS for a, b in span)
          and span[0][0] == datetime.date(2026, 8, 1)
          and span[-1][1] == datetime.date(2026, 10, 30),
          "a long range is read in windows Pontoon accepts, end to end")
    pages = {"1": {"results": [res("approved")], "next": "2"},
             "2": {"results": [dict(res("rejected"), translation_pk=2)], "next": None}}
    seen = pr.fetch("https://p", "bot", "fx", "it", datetime.date(2026, 10, 1),
                    datetime.date(2026, 10, 10), "t",
                    get=lambda url, tok: pages["2" if url == "2" else "1"])
    check(len(seen) == 2, "every page of the answer is read")

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "dismissed.txt")
        dismiss_mod.append(path, ["s @ a.xml — pontoon-rejected (2026-10-20): x"])
        with open(path, "a", encoding="utf-8") as fh:
            fh.write("s — a person's own line\n")
        dismiss_mod.remove(path, [pr._prefix(rec)])
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        check("pontoon-rejected" not in text and "a person's own line" in text,
              "withdrawing a Pontoon dismissal leaves a person's line alone")

    suite.section("A work copy's round trip is not a changed placeholder")
    # moz.l10n writes Fluent named arguments sorted, so an edited string read
    # back from its work copy has its options in a different order from the
    # clone. Compared positionally, fy-NL's whole Firefox upload was refused
    # over about-unloads-last-updated.
    from moz.l10n.resource import serialize_resource
    with tempfile.TemporaryDirectory() as tmp:
        clone = os.path.join(tmp, "clone.ftl")
        work = os.path.join(tmp, "work.ftl")
        with open(clone, "w", encoding="utf-8") as fh:
            fh.write('x = A { DATETIME($date, year: "numeric", month: "numeric", '
                     'hour12: "false") } <b>b</b>\n')
        res, _ = suggest._entries(clone)
        with open(work, "w", encoding="utf-8") as fh:
            fh.write("".join(serialize_resource(res)))
        (_, before), = suggest._entries(clone)[1].items()
        (_, after), = suggest._entries(work)[1].items()
        check(suggest._placeables(before) == suggest._placeables(after),
              "options written in another order are the same placeholder")
        with open(work, "w", encoding="utf-8") as fh:
            fh.write('x = A { DATETIME($date, year: "2-digit", month: "numeric", '
                     'hour12: "false") } <b>b</b>\n')
        (_, changed), = suggest._entries(work)[1].items()
        check(suggest._placeables(before) != suggest._placeables(changed),
              "but a changed option value still is a changed placeholder")

    suite.section("Local secrets fill gaps and never override the environment")
    import local_secrets
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "secrets.env")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("# c\nexport _LQA_A='from file'\n_LQA_B=from file\n"
                     "_LQA_C=\n_LQA_D=unasked\n")
        saved = {k: os.environ.pop(k, None) for k in ("_LQA_A", "_LQA_B", "_LQA_C", "_LQA_D")}
        os.environ["_LQA_B"] = "from env"
        try:
            local_secrets.load("_LQA_A", "_LQA_B", "_LQA_C", path=path)
            check(os.environ.get("_LQA_A") == "from file",
                  "an unset name is read from the file, quotes and `export` dropped")
            check(os.environ["_LQA_B"] == "from env",
                  "a name already in the environment wins, as in CI")
            check("_LQA_C" not in os.environ, "an empty value sets nothing")
            check("_LQA_D" not in os.environ,
                  "a name the script did not ask for stays out of its environment")
        finally:
            for k, v in saved.items():
                os.environ.pop(k, None)
                if v is not None:
                    os.environ[k] = v

    # --- convention proposals ------------------------------------------------
    suite.section("Recurring dismissals are proposed as a convention, never applied")
    # fy-NL, 2026-11: the reviewer kept asking for Û/Ú/Ô on capitalised
    # initials. Every rejection retired one string, and nothing carried the
    # rule to the next one.
    import proposals as prop
    text = "\n".join([
        "# a comment",
        "a — fine, I checked",
        "b @ x.ftl — a person's line, with no tag",
        "c @ x.ftl — pontoon-rejected (2026-11-05): rejected in Pontoon without "
        "comment; reason unclear",
        "d @ x.ftl — pontoon-rejected (2026-11-05): rejected in Pontoon without "
        "comment; likely reason (inferred): capital initials take no accent",
        "e @ x.ftl — pontoon-rejected (2026-11-05): rejected in Pontoon: Ut is right",
        "f @ y.xml — auto-suggest (2026-11-06): capital U drops the circumflex",
        "g @ y.xml — auto-suggest (2026-11-06, string 0a1b2c3d): capital O drops the circumflex",
    ])
    items = prop.parse(text, "firefox")
    check([e["string_id"] for e in items] == ["d", "e", "f", "g"],
          "only tool-written lines with a reason are evidence; a person's and an unclear one are not")
    check([e["kind"] for e in items[:2]] == ["rejected, reason inferred",
                                             "rejected, reviewer's comment"]
          and items[0]["reason"] == "capital initials take no accent",
          "an inferred reason stays labelled as one, without the boilerplate")
    model_only, human = items[2:], items[1:]
    check(not prop.eligible(model_only + [dict(model_only[0], string_id="h")]),
          "agreement among auto-suggest lines alone proposes nothing")
    check(prop.eligible(human) and not prop.eligible(human[:2]),
          f"{prop.MIN_STRINGS} distinct strings with a rejection among them are needed")
    check(not prop.eligible([items[1], items[2], dict(items[2])]),
          "the same string twice counts once")
    got = prop.validate([{"rule": " capital  initials\ttake no accent ", "refs": [1, 2, 3, 99]},
                         {"rule": "too thin", "refs": [2, 3]},
                         {"rule": "", "refs": [0, 1, 2]}], items)
    check(len(got) == 1 and got[0]["rule"] == "capital initials take no accent"
          and [e["string_id"] for e in got[0]["support"]] == ["e", "f", "g"],
          "a ref outside the evidence is dropped, and a proposal it leaves too thin goes with it")

    class _Resp:
        def __init__(self, payload):
            b = _Block(payload)
            b.name = "report_proposals"
            self.content = [b]

    class _Client:
        def __init__(self, payload):
            self.calls, self.payload = 0, payload
            self.messages = self

        def create(self, **kw):
            self.calls += 1
            return _Resp(self.payload)

    with tempfile.TemporaryDirectory() as tmp:
        class _Proj:
            name, llm, conv = "firefox", {"model": "m"}, "nothing yet"

            def state_dir(self, locale):
                return os.path.join(tmp, locale)

            def conventions(self, locale):
                return self.conv

        proj = _Proj()
        client = _Client({"proposals": [{"rule": "capital initials take no accent",
                                         "refs": [0, 1, 2, 3]}]})
        quiet = dict(write=True, log=lambda *_: None)
        first = prop.refresh(proj, "fy-NL", client, items=items, **quiet)
        again = prop.refresh(proj, "fy-NL", client, items=items, **quiet)
        check(client.calls == 1 and first == again and len(first) == 1,
              "an unchanged input is not asked twice")
        proj.conv = "capital initials take no accent"
        client.payload = {"proposals": []}
        check(prop.refresh(proj, "fy-NL", client, items=items, **quiet) == []
              and client.calls == 2 and prop.load(proj, "fy-NL") == [],
              "editing conventions.md re-asks, and an empty answer replaces the old one")
        prop.refresh(proj, "fy-NL", client, items=items, **quiet)
        check(client.calls == 2, "and an empty answer is recorded, so it is not re-asked either")
        prop.refresh(proj, "fy-NL", client, items=model_only, **quiet)
        check(client.calls == 2, "evidence that cannot support a proposal makes no request")
        check(not os.path.exists(prop.path(proj, "it"))
              and prop.refresh(proj, "it", client, items=[], **quiet) == []
              and not os.path.exists(prop.path(proj, "it")),
              "and a locale with nothing to propose gets no file")

    was = [{"rule": "r", "support": [items[1], items[2]]}]
    reworded = [{"rule": "r, said differently", "support": [items[1], items[2]]}]
    grown = [{"rule": "r", "support": [items[1], items[2], items[3]]}]
    check(prop.new_since(was, reworded) == [] and prop.new_since(was, grown) == grown,
          "the pull request repeats a proposal only when new evidence is behind it")
    md = prop.render([{"rule": "Keep <b>bold</b>",
                       "support": [dict(items[1], reason="<img src=x onerror=alert(1)>"),
                                   dict(items[2], project="android")]}], "firefox", "fy-NL")
    check("not applied" in md and "`firefox/locales/fy-NL/conventions.md`" in md
          and "(android)" in md and "(firefox)" not in md,
          "a proposal says it is not applied, where it would go, and which project each string is in")
    short = prop.render([{"rule": "r", "support": items[2:] + items[:2]}],
                        "firefox", "fy-NL", cap=2)
    check(short.index("`d`") < short.index("`e`") and "`f`" not in short
          and "2 more" in short and "4 dismissals, 2 of them rejected" in short,
          "a capped list leads with the rejections and says how many it left out")
    page = _render(md)
    check("<img" not in page and "&lt;img" in page and "<li>" in page,
          "quoted reasons are shown as text on the site, and the evidence nests under the rule")


def _site():
    import importlib.util

    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "site", "build.py")
    spec = importlib.util.spec_from_file_location("_site_build", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _render(markdown_text: str) -> str:
    """Put one finding through exactly what the published site does to it."""
    import markdown as md

    build = _site()
    body = md.markdown(html.escape(markdown_text), extensions=["tables", "sane_lists"],
                       output_format="html5")
    body = build._CODE.sub(
        lambda m: f"<code>{build._DOUBLED.sub(r'&\1;', m.group(1))}</code>", body
    )
    return build.sanitize_urls(body)


def _safe(url: str) -> bool:
    return _site()._safe_url(url)


def main(argv=None) -> int:
    suite = selftest_lib.Suite()
    run(suite)
    return suite.report()


if __name__ == "__main__":
    raise SystemExit(main())

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

import findings as fm  # noqa: E402
import llm_baseline  # noqa: E402
import llm_incremental as llm  # noqa: E402
import report  # noqa: E402
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


def run(suite) -> None:
    check = suite.check

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

    # --- baseline coverage ------------------------------------------------
    suite.section("A partition that failed was not reviewed")
    ok = llm_baseline.Outcome("p", True, findings=[])
    bad = llm_baseline.Outcome("p", False, reason="timed out")
    check(ok.ok and not bad.ok, "clean and failed are distinguishable outcomes")
    check(bad.reason, "and a failure carries why, for the report to repeat")

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

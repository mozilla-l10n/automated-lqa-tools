"""Scaffolding shared by the three projects' self-test suites.

What a suite asserts is per project and must stay that way -- a defect is
pinned against a string that really exists in one repository, and the
project-specific checks are the part worth reading. What every suite does
*around* those assertions was three copies of the same code: a pass/fail
tally, a warm-up that loads each locale it is going to talk about, and the
four table-driven loops over MUST_FIND / FIXED_UPSTREAM / NOT_A_DEFECT /
MUST_BE_SILENT.

Keeping one copy matters most for the loops, because their semantics are the
point rather than an implementation detail. ``FIXED_UPSTREAM`` in particular
exists so that "the check broke" and "the defect is gone" stay
distinguishable, and three separate versions of it is three chances for one
of them to quietly start meaning something else.
"""

from __future__ import annotations

import conventions
import layout


class Suite:
    """A running pass/fail tally that prints as it goes."""

    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, ok, label: str) -> bool:
        ok = bool(ok)
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if ok:
            self.passed += 1
        else:
            self.failed += 1
        return ok

    __call__ = check

    def section(self, title: str) -> None:
        print(f"\n{title}")

    def report(self) -> int:
        print(f"\n{self.passed} passed, {self.failed} failed")
        return 1 if self.failed else 0


def load_results(project, checks, l10n_dir, source_dir, locales) -> dict:
    """Run every check over each locale once: ``{locale: (health, found, trees)}``.

    The suites ask several questions of the same locale, and parsing a tree
    is the expensive part, so it happens once per locale rather than once per
    assertion.
    """
    results = {}
    for locale in sorted(set(locales)):
        trees = layout.load(project, locale, l10n_dir, source_dir)
        counts = conventions.detect(locale, trees.l10n)
        health, found = checks.run_all(project, locale, trees, counts)
        results[locale] = (health, found, trees)
    return results


def _raised(results, locale, kind, string_id) -> bool:
    _health, found, _trees = results[locale]
    return any(f.check == kind and f.string_id == string_id for f in found)


def must_find(suite, results, table) -> None:
    """Defects that are really in the repository and must still be caught."""
    suite.section("Defects that are really there — must still be caught")
    for locale, kind, string_id in table:
        suite.check(_raised(results, locale, kind, string_id),
                    f"{locale}: {kind} on {string_id}")


def fixed_upstream(suite, results, table) -> None:
    """Defects a locale team has since fixed.

    Listed rather than deleted, so a check that breaks and a defect that is
    genuinely gone cannot be mistaken for each other.
    """
    suite.section("Defects since fixed upstream — must NOT be reported any more")
    for locale, kind, string_id in table:
        suite.check(not _raised(results, locale, kind, string_id),
                    f"{locale}: {kind} on {string_id} is gone")


def not_a_defect(suite, results, table) -> None:
    """False positives these checks really produced once. Each must stay dead."""
    suite.section("Correct localization that must not be flagged")
    for locale, kind, string_id in table:
        suite.check(not _raised(results, locale, kind, string_id),
                    f"{locale}: {kind} on {string_id}")


def must_be_silent(suite, results, table) -> None:
    """Checks that must report nothing for a locale, or be skipped for it."""
    suite.section("Conventions established as correct — must stay silent")
    for locale, kind, why in table:
        health = results[locale][0]
        silent = kind in health.skipped or health.counts.get(kind, 0) == 0
        state = "skipped" if kind in health.skipped else health.counts.get(kind, 0)
        suite.check(silent, f"{locale}: {kind} = {state} ({why})")


def deliberate_flag_wiring(suite, project) -> None:
    """The reviewer must be asked, and told what the answer means.

    The pull request body leads with findings flagged as reading like a
    deliberate edit, so nothing can lead it if the field never reaches the
    model. The schema and the prompts are per project, so each one is pinned
    against its own files.
    """
    import json

    suite.section("Escalation to the pull request")
    schema = json.loads(project.prompt("finding_schema.json"))
    props = schema["input_schema"]["properties"]["findings"]["items"]
    suite.check("reads_as_deliberate" in props["required"],
                "the reviewer is asked, on every finding, whether it reads as "
                "a deliberate edit")
    names = ["incremental_review.md"]
    if project.data.get("variants"):
        names.append("variant_review.md")
    for name in names:
        suite.check("reads_as_deliberate" in project.prompt(name),
                    f"{name} tells it what that means")

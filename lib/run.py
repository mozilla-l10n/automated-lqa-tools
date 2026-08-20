#!/usr/bin/env python3
"""Orchestrator. This is the only entry point CI calls.

    run.py --locale it
    run.py --all --dry-run
    run.py --locale cs --mode baseline

Per locale: refresh the repositories, parse both trees, diff against the
stored snapshot, run the deterministic checks over everything and the model
over the delta, fold the results into the backlog, apply suppressions,
re-render the report, and write the new state.

Everything is non-interactive: stdin is closed for every subprocess, there
are no prompts, and a locale that fails is logged and skipped rather than
aborting the run.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import layout  # noqa: E402
import conventions  # noqa: E402
import findings as findings_mod  # noqa: E402
import parse  # noqa: E402
import report  # noqa: E402
import repos  # noqa: E402
import snapshot  # noqa: E402
import suppress  # noqa: E402


def load_checks(project):
    """Import the project's own checks module.

    Each project composes the shared checks in `lib/common_checks.py` with
    whatever its file format needs, so the module lives next to the project
    rather than here.
    """
    if project.tools_dir not in sys.path:
        sys.path.insert(0, project.tools_dir)
    import importlib

    return importlib.import_module("checks")


def today() -> str:
    return datetime.date.today().isoformat()


class Log:
    def __init__(self, quiet: bool = False):
        self.quiet = quiet

    def __call__(self, message: str = "") -> None:
        if not self.quiet:
            print(message, flush=True)


def load_meta(project, locale: str) -> dict:
    path = os.path.join(project.state_dir(locale), "meta.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_meta(project, locale: str, meta: dict) -> None:
    path = os.path.join(project.state_dir(locale), "meta.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=1, sort_keys=True)
        fh.write("\n")


def build_systemic(project, locale, fresh, health):
    """Collapse a check that fired on very many strings into one decision.

    The manual reviews learned this the hard way: 142 unadapted access keys
    is one choice the locale team makes once, not 142 bugs, and listing them
    individually buries the handful of real defects.
    """
    threshold = project.systemic_threshold
    by_check: dict[str, list] = {}
    for f in fresh:
        by_check.setdefault(f.check, []).append(f)

    systemic, remaining = [], []
    notes = {
        "accesskey": (
            "The locale kept en-US access keys rather than remapping them to its "
            "own labels. Remapping is a single decision for the locale team; it is "
            "not tracked as individual defects."
        ),
        "typography": (
            "These deviate from the convention the rest of the tree follows. "
            "Whether to normalize them is one decision."
        ),
        "plurals": (
            "The locale's plural variants differ from what the rest of its "
            "tree does. At this scale it is a convention to settle once, not "
            "a defect per string."
        ),
    }
    for check, group in by_check.items():
        if len(group) >= threshold and check in notes:
            systemic.append({
                "title": f"{check.replace('_', ' ')} — {len(group)} strings",
                "count": len(group),
                "note": notes[check],
                "ids": sorted({f.string_id for f in group}),
                "check": check,
            })
        else:
            remaining.extend(group)
    return systemic, remaining


def process(project, locale, l10n_root, source_root, args, log) -> dict:
    log(f"\n=== {locale}")
    meta = load_meta(project, locale)
    is_new = not meta
    mode = args.mode
    if mode == "auto":
        mode = "baseline" if is_new else "incremental"

    trees = layout.load(project, locale, l10n_root, source_root)
    l10n, source = trees.l10n, trees.source
    if not l10n:
        raise RuntimeError(f"no strings parsed for {locale} under {l10n_root}")
    log(f"  parsed {len(l10n):,} strings from {len(trees.l10n_files)} files, mode={mode}")

    counts_conv = conventions.detect(locale, l10n)
    current = snapshot.build(l10n, source)
    previous = snapshot.load(os.path.join(project.state_dir(locale), "strings.json"))
    delta = snapshot.diff(previous, current)
    log(f"  delta: {delta.summary()}")

    # --- deterministic layer: always over the whole tree ------------------
    checks = load_checks(project)
    health, check_findings = checks.run_all(project, locale, trees, counts_conv)
    log(f"  checks: {health.counts}")

    # --- model layer ------------------------------------------------------
    llm_findings: list = []
    reviewed = 0
    if args.no_llm:
        log("  model review skipped (--no-llm)")
    elif mode == "baseline" and project.baseline_strategy == "batched":
        import llm_incremental
        keys = sorted(l10n)
        if args.limit:
            keys = keys[: args.limit]
            log(f"  limited to {len(keys)} strings (--limit)")
        log(f"  baseline review of all {len(keys):,} strings, in batches")
        llm_findings, usage = llm_incremental.review(
            project, locale, keys, l10n, source, log=log
        )
        log(f"  model usage: {usage}")
        reviewed = len(keys)
    elif mode == "baseline":
        import llm_baseline
        log("  baseline review of the whole tree")
        llm_findings, empty = llm_baseline.review(
            project, locale, l10n_root, source_root, l10n, trees,
            only=args.partitions, log=log,
        )
        reviewed = len(l10n)
        if empty:
            log(f"  partitions returning nothing: {', '.join(sorted(empty))}")
    else:
        keys = delta.to_review
        if args.limit:
            keys = keys[: args.limit]
            log(f"  limited to {len(keys)} strings (--limit)")
        if keys:
            import llm_incremental
            log(f"  reviewing {len(keys):,} changed strings")
            llm_findings, usage = llm_incremental.review(
                project, locale, keys, l10n, source, log=log
            )
            log(f"  model usage: {usage}")
            reviewed = len(keys)
        else:
            log("  nothing changed since the last run; no model call")

    # --- fold into the backlog -------------------------------------------
    stored = findings_mod.load(project, locale)
    delta_keys = set(delta.to_review)
    # Deterministic checks just ran over the whole tree, so their output is
    # the ground truth for their own findings. Captured before the systemic
    # collapse below, which removes findings from `fresh` without meaning
    # they stopped being true.
    rerunnable = {c for c in checks.CHECKS if c not in health.skipped}
    still_raised = {f.fid for f in check_findings}
    resolved = findings_mod.resolve(
        stored, l10n, delta_keys, today(), rerunnable, still_raised
    )

    fresh = check_findings + llm_findings
    systemic, fresh = build_systemic(project, locale, fresh, health)
    stored, raised = findings_mod.merge(stored, fresh, today())

    rules = suppress.load(project, locale)
    hits = suppress.apply(rules, stored)
    if hits:
        log(f"  suppressed: {hits}")
    raised = [f for f in raised if f.status != "suppressed"]

    open_now = [f for f in stored if f.is_open]
    log(
        f"  findings: {len(raised)} new, {len(resolved['fixed'])} fixed, "
        f"{len(resolved['withdrawn'])} withdrawn, "
        f"{len(resolved['obsolete'])} retired, {len(open_now)} open"
    )

    new_meta = {
        "locale": locale,
        "mode": mode,
        "last_run": today(),
        "previous_run": meta.get("last_run", ""),
        "previous_sha": meta.get("l10n_sha", ""),
        "l10n_repo": project.data["repos"]["l10n"]["url"],
        "l10n_sha": repos.head_sha(args.l10n_dir or l10n_root),
        "source_repo": project.data["repos"]["source"]["url"],
        "source_sha": repos.head_sha(source_root),
        "reviewed": reviewed,
        "strings": len(l10n),
        "missing": health.missing,
        "open": len(open_now),
        "fixed_total": sum(1 for f in stored if f.status == "fixed"),
        "withdrawn_total": sum(1 for f in stored if f.status == "withdrawn"),
        "suppressed": sum(1 for f in stored if f.status == "suppressed"),
    }

    report.use_paths(trees.locale_paths)
    text = report.render(
        locale, new_meta, health, health.counts, stored, systemic,
        {
            "new": raised,
            "fixed": resolved["fixed"],
            "withdrawn": resolved["withdrawn"],
            "recheck": resolved["recheck"],
            "obsolete": resolved["obsolete"],
        },
        counts_conv, rules,
    )

    if args.dry_run:
        log("  --dry-run: nothing written")
        log(f"  report would be {len(text.splitlines())} lines")
    else:
        changed = report.write(project, locale, text)
        log(f"  report {'updated' if changed else 'unchanged'}")
        findings_mod.save(project, locale, stored)
        snapshot.save(os.path.join(project.state_dir(locale), "strings.json"), current)
        conventions.save(project, locale, counts_conv)
        save_meta(project, locale, new_meta)
        _ensure_locale_files(project, locale, counts_conv, log)

    return {
        "locale": locale, "mode": mode, "new": len(raised),
        "fixed": len(resolved["fixed"]),
        "withdrawn": len(resolved["withdrawn"]), "open": len(open_now),
        "missing": health.missing, "reviewed": reviewed,
    }


def _ensure_locale_files(project, locale, counts_conv, log) -> None:
    """Create the editable per-locale files on first run, never overwrite."""
    directory = project.locale_dir(locale)
    os.makedirs(directory, exist_ok=True)
    conv_path = os.path.join(directory, "conventions.md")
    if not os.path.exists(conv_path):
        with open(conv_path, "w", encoding="utf-8") as fh:
            fh.write(conventions.draft(locale, counts_conv, today()))
        log(f"  wrote a draft {conv_path} — review it before the next run")
    sup_path = suppress.path(project, locale)
    if not os.path.exists(sup_path):
        with open(sup_path, "w", encoding="utf-8") as fh:
            fh.write(suppress.TEMPLATE.format(locale=locale))


def resolve_trees(project, args, log):
    """Point at local clones, or make shallow ones."""
    work = os.path.join(config.REPO_ROOT, "work")
    if args.source_dir:
        source_root = repos.ensure_local(args.source_dir)
    else:
        cfg = project.data["repos"]["source"]
        log(f"cloning {cfg['url']}")
        source_root = repos.ensure_clone(
            cfg["url"], cfg["branch"], os.path.join(work, "source"), None
        )
    if args.l10n_dir:
        l10n_root = repos.ensure_local(args.l10n_dir)
    else:
        cfg = project.data["repos"]["l10n"]
        locales = args.locales or project.locales
        log(f"cloning {cfg['url']} (sparse: {len(locales)} locales)")
        l10n_root = repos.ensure_clone(
            cfg["url"], cfg["branch"], os.path.join(work, "l10n"),
            [f"/{loc}/" for loc in locales],
        )
    return l10n_root, source_root


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", default="firefox",
                    help="the project directory to run: firefox, android, ...")
    ap.add_argument("--locale", dest="locales", action="append",
                    help="repeatable; defaults to every locale in config.yaml")
    ap.add_argument("--all", action="store_true", help="explicitly run every locale")
    ap.add_argument("--mode", choices=("auto", "incremental", "baseline"), default="auto")
    ap.add_argument("--partitions", action="append",
                    help="baseline only: run just these partitions")
    ap.add_argument("--baseline-strategy", choices=("agent", "batched"),
                    help="override how a from-scratch review runs: `agent` "
                         "hands whole files to the claude CLI, `batched` sends "
                         "strings through the API")
    ap.add_argument("--limit", type=int, default=0,
                    help="review at most this many changed strings (for testing)")
    ap.add_argument("--no-llm", action="store_true",
                    help="deterministic checks only; no API calls")
    ap.add_argument("--dry-run", action="store_true", help="write nothing")
    ap.add_argument("--l10n-dir", help="use an existing localization clone")
    ap.add_argument("--source-dir", help="use an existing en-US source clone")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    log = Log(args.quiet)
    project = config.load(args.project)
    if args.baseline_strategy:
        project._baseline_override = args.baseline_strategy
    locales = args.locales or project.locales
    unknown = [loc for loc in locales if loc not in project.locales]
    if unknown:
        log(f"error: not in {args.project}/config.yaml: {', '.join(unknown)}")
        return 2

    # Only the incremental reviewer talks to the API directly; the baseline
    # shells out to the `claude` CLI, which carries its own credentials. So
    # a from-scratch run works without an API key in the environment, and
    # the incremental path reports the problem itself, per locale, rather
    # than aborting a whole run that might not need a key at all.
    if (
        not args.no_llm
        and args.mode != "baseline"
        and not os.environ.get("ANTHROPIC_API_KEY")
    ):
        log("note: ANTHROPIC_API_KEY is not set — any locale needing the")
        log("      incremental reviewer will fail. Baseline runs are fine.")

    l10n_root, source_root = resolve_trees(project, args, log)
    log(f"locale tree      {l10n_root}")
    log(f"                 {repos.describe(l10n_root)}")
    log(f"source reference {source_root}")
    log(f"                 {repos.describe(source_root)}")
    if args.l10n_dir or args.source_dir:
        # A local checkout is used exactly as it is on disk. Saying so
        # matters: an unpulled tree quietly produces an empty delta and a
        # run that looks like "nothing changed".
        log("                 (local checkout, used as-is -- pull it yourself)")

    results, failed = [], []
    for locale in locales:
        try:
            results.append(
                process(project, locale, l10n_root, source_root, args, log)
            )
        except Exception:  # noqa: BLE001 - one locale must not sink the run
            log(f"  FAILED:\n{traceback.format_exc()}")
            failed.append(locale)

    log("\n" + "=" * 62)
    log(f"{'locale':8} {'mode':12} {'reviewed':>9} {'new':>5} {'fixed':>6} "
        f"{'withdrn':>8} {'open':>6}")
    for r in results:
        log(f"{r['locale']:8} {r['mode']:12} {r['reviewed']:9,} {r['new']:5} "
            f"{r['fixed']:6} {r['withdrawn']:8} {r['open']:6}")
    if failed:
        log(f"\nfailed: {', '.join(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

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
import dismiss  # noqa: E402
import layout  # noqa: E402
import conventions  # noqa: E402
import findings as findings_mod  # noqa: E402
import report  # noqa: E402
import repos  # noqa: E402
import snapshot  # noqa: E402
import summary  # noqa: E402
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


def build_systemic(project, fresh):
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


# A run where the model never read a string is not the mode it was asked
# for. Recorded as itself so no report can claim a locale was reviewed from
# scratch when only the deterministic checks ran over it.
CHECKS_ONLY = config.CHECKS_ONLY


def pick_mode(requested: str, meta: dict) -> str:
    """The path this run takes, resolving `auto` against what came before.

    A locale whose only run skipped the model has not been reviewed, whatever
    it has in `state/`: its snapshot is empty and its findings are the check
    layer's alone. So `auto` still owes it a baseline -- which for an agent
    project is a different path entirely from replaying the whole tree
    through the incremental reviewer.
    """
    if requested != "auto":
        return requested
    if not meta or meta.get("mode") == CHECKS_ONLY:
        return "baseline"
    return "incremental"


def process(project, locale, l10n_root, source_root, args, log) -> dict:
    log(f"\n=== {locale}")
    meta = load_meta(project, locale)
    mode = pick_mode(args.mode, meta)

    trees = layout.load(project, locale, l10n_root, source_root)
    l10n, source = trees.l10n, trees.source
    if not l10n:
        raise RuntimeError(f"no strings parsed for {locale} under {l10n_root}")
    if not source:
        # Every check and every prompt is a comparison against en-US. With no
        # source at all they all still "run", quietly: the model sees strings
        # with no reference, the source hashes vanish from the snapshot so
        # nothing looks stale again, and the health table reports a complete
        # locale. A wrong --source-dir must not look like a clean run.
        raise RuntimeError(
            f"no source strings parsed under {source_root}; every check and "
            "every review compares against en-US, so there is nothing to "
            "review. Check --source-dir."
        )
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

    stored = findings_mod.load(project, locale)

    # --- model layer ------------------------------------------------------
    llm_findings: list = []
    reviewed = 0
    reviewed_keys: set = set()
    # Strings whose review came back well formed. Only these may be read as
    # reviewer silence; `reviewed_keys` merely advances the snapshot.
    trusted_keys: set = set()
    incomplete = ""
    if args.no_llm:
        log("  model review skipped (--no-llm)")
    elif mode == "baseline" and project.baseline_strategy == "batched":
        import llm_incremental
        keys = sorted(l10n)
        if args.limit:
            keys = keys[: args.limit]
            log(f"  limited to {len(keys)} strings (--limit)")
        log(f"  baseline review of all {len(keys):,} strings, in batches")
        llm_findings, usage, progress = llm_incremental.review(
            project, locale, keys, l10n, source, log=log
        )
        log(f"  model usage: {usage}")
        reviewed_keys = progress.reviewed
        trusted_keys = progress.trusted
        reviewed = len(reviewed_keys)
        incomplete = progress.stopped
    elif mode == "baseline":
        import llm_baseline
        log("  baseline review of the whole tree")
        # trees.root, not l10n_root: partitions are written against the
        # paths a message key uses, which are relative to the locale tree.
        pass_ = llm_baseline.review(
            project, locale, trees.root, source_root, l10n, trees,
            only=args.partitions, log=log,
        )
        llm_findings = pass_.findings
        # Only the partitions that actually succeeded count as reviewed. No
        # fallback to the whole tree: `covered` being empty means every
        # partition failed, and reading that as "all of it was reviewed" is
        # how a locale used to be marked complete without a string being read.
        reviewed_keys = {k for k in l10n if k[0] in pass_.covered}
        trusted_keys = reviewed_keys
        reviewed = len(reviewed_keys)
        if pass_.clean:
            log(f"  partitions returning nothing: {', '.join(sorted(pass_.clean))}")
        if pass_.failed:
            names = ", ".join(sorted(n for n, _ in pass_.failed))
            incomplete = (
                f"did not review {len(pass_.failed)} of {pass_.attempted} "
                f"partition(s): {names}. Re-run with --partitions {names}"
            )
    else:
        keys = delta.to_review
        # `needs-recheck` is the pipeline saying, in its own words, that text
        # matching cannot answer this one and a reader has to. So a normal run
        # owes it a read: nothing else can ever close it, and 456 of the 589
        # Firefox findings in the bucket quote nothing at all, so no amount of
        # matching would have. The set drains as the reviewer answers, and it
        # is bounded by the backlog rather than by the tree.
        parked = [
            f.key for f in stored
            if f.status == "needs-recheck" and f.key in l10n
        ]
        pending = [k for k in dict.fromkeys(parked) if k not in set(keys)]
        if pending:
            log(f"  re-reading {len(pending)} string(s) parked as needs-recheck")
        keys = list(keys) + pending
        if args.recheck:
            # Substring matching cannot close a finding whose quoted text
            # survives an edit that fixed it -- "Traduzione" is still inside
            # "Traduzione in corso". Those need reading, so re-queue every
            # string that still carries an open finding.
            moved = [
                f.key for f in stored
                if f.is_open and f.key in l10n
                and f.string_hash and f.string_hash != l10n[f.key].hash()
            ]
            extra = [k for k in dict.fromkeys(moved) if k not in set(keys)]
            if extra:
                log(f"  --recheck: re-queueing {len(extra)} string(s) with open findings")
            keys = list(keys) + extra
        if args.limit:
            keys = keys[: args.limit]
            log(f"  limited to {len(keys)} strings (--limit)")
        if keys:
            import llm_incremental
            log(f"  reviewing {len(keys):,} changed strings")
            llm_findings, usage, progress = llm_incremental.review(
                project, locale, keys, l10n, source, log=log
            )
            log(f"  model usage: {usage}")
            reviewed_keys = progress.reviewed
            trusted_keys = progress.trusted
            reviewed = len(reviewed_keys)
            incomplete = progress.stopped
        else:
            log("  nothing changed since the last run; no model call")

    # --- fold into the backlog -------------------------------------------
    delta_keys = set(delta.to_review)
    # Deterministic checks just ran over the whole tree, so their output is
    # the ground truth for their own findings. Captured before the systemic
    # collapse below, which removes findings from `fresh` without meaning
    # they stopped being true.
    noop = findings_mod.drop_noop(stored, today())
    if noop:
        log(f"  retired {len(noop)} finding(s) that proposed no change")

    # What actually ran, reported by the runner rather than reconstructed
    # from the registry: `checks.CHECKS` is every check the module can offer,
    # and a project runs the subset its config lists. Resolving against the
    # registry withdrew or "fixed" findings from checks that never executed.
    rerunnable = set(health.ran)
    still_raised = {f.fid for f in check_findings}
    resolved = findings_mod.resolve(
        stored, l10n, delta_keys, today(), rerunnable, still_raised,
        recheck=args.recheck,
        still_raised_loose={f.rekey for f in check_findings},
    )
    if args.recheck:
        log(f"  re-read {sum(1 for f in stored if f.is_open) + len(resolved['fixed'])} "
            f"open findings against the current tree")

    fresh = check_findings + llm_findings
    systemic, fresh = build_systemic(project, fresh)
    llm_fids = {f.fid for f in llm_findings}
    stored, raised = findings_mod.merge(stored, fresh, today())

    # A model finding the reviewer re-read and did not repeat is resolved;
    # otherwise a needs-recheck item could never close.
    # Silence from the reviewer only means something for a string that has
    # actually moved. --recheck widens what gets *re-read*, never what a
    # quiet answer is allowed to conclude.
    # A `needs-recheck` finding is only in that bucket because its string had
    # already moved when it was parked, so reviewer silence about it means
    # something -- the invariant is about strings that never moved, not about
    # strings whose movement was established on an earlier run.
    trusted = set(delta.to_review) | {
        f.key for f in stored
        if f.key in l10n and (
            f.status == "needs-recheck"
            or (f.string_hash and f.string_hash != l10n[f.key].hash())
        )
    }
    reclosed = findings_mod.close_reviewed(
        stored, trusted_keys, llm_fids, trusted, today(), rerunnable
    )
    if reclosed:
        log(f"  closed {len(reclosed)} finding(s) the reviewer did not repeat")
    resolved["fixed"].extend(reclosed)

    # Narrowest mechanism first, as `docs/suppressions.md` orders them: a
    # dismissal is about one string somebody read, and `suppress.apply`
    # leaves those alone, so a class rule can no longer overwrite one and
    # lose the reason with it. Running dismissals first also means a finding
    # whose dismissal line was deleted is available to a class rule in the
    # same run rather than the next one.
    dismissals = dismiss.load(project, locale)
    dropped = dismiss.apply(dismissals, stored)
    if dropped:
        log(f"  dismissed by hand: {sum(dropped.values())}")

    rules = suppress.load(project, locale)
    hits = suppress.apply(rules, stored)
    if hits:
        log(f"  suppressed: {hits}")
    raised = [f for f in raised if f.status not in ("suppressed", "dismissed")]

    # The buckets were filled before suppressions, dismissals and merge had
    # their say, and any of those can move a finding afterwards -- a defect
    # resolved earlier in the run and then raised again by the reviewer ends
    # up open, but was still sitting in the "fixed" list. Report what each
    # finding actually ended up as.
    _final = {
        "fixed": "fixed", "withdrawn": "withdrawn",
        "obsolete": "obsolete", "recheck": "needs-recheck",
    }
    for bucket, status in _final.items():
        resolved[bucket] = [f for f in resolved[bucket] if f.status == status]

    open_now = [f for f in stored if f.is_open]
    log(
        f"  findings: {len(raised)} new, {len(resolved['fixed'])} fixed, "
        f"{len(resolved['withdrawn'])} withdrawn, "
        f"{len(resolved['obsolete'])} retired, {len(open_now)} open"
    )

    new_meta = {
        "project": project.name,
        "display_name": f"{project.display_name} l10n",
        "locale": locale,
        "mode": CHECKS_ONLY if args.no_llm else mode,
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
        "dismissed": sum(1 for f in stored if f.status == "dismissed"),
    }
    if incomplete:
        # Only present when it happened, so it does not add a line to every
        # meta.json in the tree. The next run overwrites meta wholesale, so
        # a locale that completes drops the key again.
        new_meta["incomplete"] = incomplete

    text = report.render(
        locale, new_meta, health, stored, systemic,
        {
            "new": raised,
            "fixed": resolved["fixed"],
            "withdrawn": resolved["withdrawn"] + noop,
            "recheck": resolved["recheck"],
            "obsolete": resolved["obsolete"],
        },
        counts_conv, rules,
        report.Ctx(paths=trees.locale_paths, source=source),
    )

    if args.dry_run:
        log("  --dry-run: nothing written")
        log(f"  report would be {len(text.splitlines())} lines")
    else:
        changed = report.write(project, locale, text)
        log(f"  report {'updated' if changed else 'unchanged'}")
        findings_mod.save(project, locale, stored)
        snapshot.save(
            os.path.join(project.state_dir(locale), "strings.json"),
            snapshot.merge(previous, current, reviewed_keys),
        )
        conventions.save(project, locale, counts_conv)
        save_meta(project, locale, new_meta)
        _ensure_locale_files(project, locale, counts_conv, log)

    return {
        "locale": locale, "mode": new_meta["mode"], "new": len(raised),
        "fixed": len(resolved["fixed"]),
        "withdrawn": len(resolved["withdrawn"]), "open": len(open_now),
        "missing": health.missing, "reviewed": reviewed,
        "incomplete": incomplete,
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
    dis_path = dismiss.path(project, locale)
    if not os.path.exists(dis_path):
        with open(dis_path, "w", encoding="utf-8") as fh:
            fh.write(dismiss.TEMPLATE)


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
    ap.add_argument("--recheck", action="store_true",
                    help="re-verify every open finding against the tree as it "
                         "stands: close the ones whose quoted text has gone, "
                         "and send the rest back to the reviewer even if the "
                         "delta says nothing changed")
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
        if args.baseline_strategy == "agent" and not project.supports_agent_baseline:
            log(f"error: --baseline-strategy agent is not available for "
                f"{project.name}: a locale is a single file that no partition "
                f"can make small enough for one agent to read.")
            return 2
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

    if results and not args.dry_run:
        # Otherwise the cross-locale page keeps yesterday's numbers until
        # somebody remembers to run summary.py by hand.
        log(f"\nrefreshed {os.path.relpath(summary.write(project), config.REPO_ROOT)}")

    log("\n" + "=" * 62)
    log(f"{'locale':8} {'mode':12} {'reviewed':>9} {'new':>5} {'fixed':>6} "
        f"{'withdrn':>8} {'open':>6}")
    for r in results:
        log(f"{r['locale']:8} {r['mode']:12} {r['reviewed']:9,} {r['new']:5} "
            f"{r['fixed']:6} {r['withdrawn']:8} {r['open']:6}"
            + ("  (incomplete)" if r.get("incomplete") else ""))
    if failed:
        log(f"\nfailed: {', '.join(failed)}")
    # Kept apart from `failed`: the work these locales did do is real and
    # was written. They are not finished, though, and nothing else says so
    # once the batch log has scrolled past.
    partial = [r for r in results if r.get("incomplete")]
    for r in partial:
        log(f"\nincomplete: {r['locale']} — {r['incomplete']}")
        log(f"            {r['reviewed']:,} string(s) reviewed and kept; "
            "re-run the same command to resume")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

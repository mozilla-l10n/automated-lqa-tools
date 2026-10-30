#!/usr/bin/env python3
"""Merge the weekly QA pull requests and email what they changed.

One pull request per project, on `l10n-qa/<project>`. Each is merged only
when nothing about it needs a person:

- every check on its head commit passed -- `checks` is required on `main`,
  but the merging token belongs to an admin, who bypasses the ruleset, so
  this is tested here rather than left to GitHub;
- its project's QA workflow is not still running, which would push to the
  branch after the decision was made;
- it touches nothing under `<project>/locales/`. Those files are written by
  people, and a run only adds there on the first sight of a locale -- a
  draft `conventions.md` that would go straight into the reviewer's prompt.
  The one exception is `dismissed.txt` lines tagged `pontoon-rejected`:
  those record a Pontoon reviewer's rejection, already a person's answer.

Anything left open is named at the top of the email with the reason, so a
skipped pull request cannot pass for a quiet week.

The digest is computed before merging, from the pull request's head against
the base, with the same `summary.delta` the pull request body uses. It is
code, not a model: the email reaches people outside this repository, and a
summary that can misstate a finding is worse than none. It leads with
findings that read as a deliberate edit and with broken output; the rest is
counted and linked.

Mail goes through `smtplib`, as `mozl10n-linter` sends its failure emails --
no third-party action. The HTML part is rendered by the site's own renderer,
which escapes every quoted translation before rendering it.

    python lib/digest.py                  # decide and print; merge and send nothing
    python lib/digest.py --merge --send   # what .github/workflows/qa-digest.yml runs
"""

from __future__ import annotations

import argparse
import datetime
import glob
import importlib.util
import json
import os
import re
import smtplib
import subprocess
import sys
from dataclasses import dataclass, field
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import summary  # noqa: E402
import tracker  # noqa: E402

# Must match `pontoon_review.PONTOON_TAG`; not imported, because that module
# pulls in the whole parsing stack and this one needs none of it.
PONTOON_TAG = "pontoon-rejected"
_TAGGED = re.compile(rf"^.+ @ .+ — {re.escape(PONTOON_TAG)} \(\d{{4}}-\d{{2}}-\d{{2}}\): ")

RECIPIENTS = ["flodolo+l10nqa@mozilla.com"]
SITE = "https://mozilla-l10n.github.io/automated-lqa-tools/"
BASE = "main"

# Conclusions that do not stand in the way of a merge.
_PASSING = {"SUCCESS", "NEUTRAL", "SKIPPED"}


@dataclass
class Outcome:
    project: object
    pr: dict | None = None
    reasons: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    delta: dict | None = None
    pontoon: list = field(default_factory=list)
    merged: bool = False

    @property
    def ready(self) -> bool:
        return self.pr is not None and not self.reasons


def _run(*cmd: str) -> str:
    return subprocess.run(cmd, cwd=config.REPO_ROOT, capture_output=True,
                          text=True, check=True).stdout


def _gh_json(*args: str):
    return json.loads(_run("gh", *args))


def projects() -> list:
    paths = sorted(glob.glob(os.path.join(config.REPO_ROOT, "*", "config.yaml")))
    return [config.load(os.path.basename(os.path.dirname(p))) for p in paths]


def branch(project) -> str:
    return f"l10n-qa/{project.name}"


def check_problems(rollup: list) -> list[str]:
    """Why the head commit's checks do not allow a merge; empty if they do."""
    problems, seen_required = [], False
    for item in rollup or []:
        if item.get("__typename") == "StatusContext":
            name, state = item.get("context", "?"), item.get("state", "")
            if state != "SUCCESS":
                problems.append(f"`{name}` is {state.lower() or 'unknown'}")
            continue
        name = item.get("name", "?")
        seen_required |= name == "checks"
        if item.get("status") != "COMPLETED":
            problems.append(f"`{name}` has not finished")
        elif item.get("conclusion") == "ACTION_REQUIRED":
            # What a pull request opened with GITHUB_TOKEN looks like: its
            # checks wait for a person to approve them. See the QA workflows.
            problems.append(f"`{name}` is waiting for someone to approve the run")
        elif item.get("conclusion") not in _PASSING:
            problems.append(f"`{name}` ended {str(item.get('conclusion')).lower()}")
    if not seen_required:
        problems.append("the required `checks` job has not run on it")
    return list(dict.fromkeys(problems))


def _qa_runs(project) -> tuple[bool, dict | None]:
    """Is the project's QA workflow running, and its latest finished run."""
    runs = _gh_json("run", "list", "--workflow", f"{project.name}-qa.yml",
                    "--limit", "10",
                    "--json", "status,conclusion,url,createdAt,event")
    active = any(r["status"] != "completed" for r in runs)
    done = next((r for r in runs if r["status"] == "completed"), None)
    return active, done


def assess(project) -> Outcome:
    out = Outcome(project)
    active, last = _qa_runs(project)
    if last and last["conclusion"] not in ("success", "skipped"):
        out.notes.append(
            f"The last QA run ({last['createdAt'][:10]}) ended "
            f"{last['conclusion']}; locales whose job failed are missing. "
            f"[Run]({last['url']})"
        )

    prs = _gh_json("pr", "list", "--head", branch(project), "--base", BASE,
                   "--state", "open",
                   "--json", "number,url,title,headRefOid,statusCheckRollup")
    if active:
        out.reasons.append("its QA workflow is still running")
    if not prs:
        return out
    out.pr = pr = prs[0]

    _run("git", "fetch", "--quiet", "--no-tags", "origin",
         f"+refs/heads/{BASE}:refs/remotes/origin/{BASE}",
         f"+refs/heads/{branch(project)}:refs/remotes/origin/{branch(project)}")
    head = _run("git", "rev-parse", f"origin/{branch(project)}").strip()
    if head != pr["headRefOid"]:
        out.reasons.append("its branch moved while this was deciding")

    out.reasons += check_problems(pr.get("statusCheckRollup"))

    locales = os.path.relpath(project.root, config.REPO_ROOT) + "/locales/"
    touched = [p for p in _run("git", "diff", "--name-only",
                               f"origin/{BASE}...{head}", "--", locales).split()
               if not only_pontoon_dismissals(
                   _run("git", "diff", "-U0", f"origin/{BASE}...{head}", "--", p))]
    if touched:
        shown = ", ".join(f"`{p}`" for p in touched[:5])
        more = f" and {len(touched) - 5} more" if len(touched) > 5 else ""
        out.reasons.append(
            f"it changes locale instructions, which a person has to read: "
            f"{shown}{more}"
        )

    out.delta = summary.delta(project, summary.rows_at(project, head),
                              f"origin/{BASE}")
    out.pontoon = tracker.changes(project, f"origin/{BASE}", head)
    return out


def only_pontoon_dismissals(diff: str) -> bool:
    """Whether a `git diff -U0` of a locale file is nothing a person must read.

    True for a `dismissed.txt` change made only of lines `pontoon_review`
    writes and withdraws -- a Pontoon reviewer's rejection, already a
    person's decision -- plus the comment header a new file starts with.
    Anything else under `locales/` reaches the reviewer's prompt or is a
    person's own dismissal, and holds the pull request.
    """
    lines = diff.splitlines()
    if not lines or not any(x.startswith("+++ ") and x.endswith("/dismissed.txt")
                            for x in lines):
        return False
    for x in lines:
        if x.startswith(("diff ", "index ", "--- ", "+++ ", "@@", "new file mode")):
            continue
        body = x[1:]
        if x.startswith("+") and (not body.strip() or body.startswith("#")
                                  or _TAGGED.match(body)):
            continue
        if x.startswith("-") and _TAGGED.match(body):
            continue
        return False
    return True


def merge(out: Outcome) -> None:
    try:
        _run("gh", "pr", "merge", str(out.pr["number"]), "--squash",
             "--match-head-commit", out.pr["headRefOid"])
        out.merged = True
    except subprocess.CalledProcessError as err:
        last = (err.stderr or err.stdout or "").strip().splitlines()
        out.reasons.append(f"merging failed: {last[-1] if last else 'no output'}")


# --- the email --------------------------------------------------------------

def _counts(d: dict) -> str:
    raised = d["new"] + d["reopened"]
    bits = [
        f"{len(raised)} new or reopened "
        f"({sum(1 for _, f in raised if f.reads_as_deliberate)} read as a "
        f"deliberate edit, {sum(1 for _, f in raised if f.impact == 1)} "
        "broken output)"
    ]
    for key, label in (("fixed", "fixed"), ("withdrawn", "withdrawn"),
                       ("person", "dismissed or suppressed"),
                       ("obsolete", "retired"), ("recheck", "need re-reading")):
        if d[key]:
            bits.append(f"{len(d[key])} {label}")
    return " · ".join(bits)


def _pr_link(out: Outcome) -> str:
    return f"[#{out.pr['number']}]({out.pr['url']})"


def _section(out: Outcome, dry_run: bool) -> list[str]:
    project, d = out.project, out.delta
    verb = "ready to merge (dry run)" if dry_run else "merged"
    lines = [f"## {project.display_name} — {verb} {_pr_link(out)}", ""]
    lines += [f"_{note}_" for note in out.notes]
    if out.notes:
        lines.append("")
    if d["first_run"]:
        lines += ["First run for " + ", ".join(f"`{x}`" for x in d["first_run"])
                  + ": the whole backlog counts as new.", ""]
    lines += [_counts(d), "", summary.delta_table(d), ""]

    loud = [p for p in d["new"] + d["reopened"]
            if p[1].reads_as_deliberate or p[1].impact == 1]
    if loud:
        lines += [f"### Read as a deliberate edit, or broken output ({len(loud)})",
                  "", summary._listing(summary._escalation_order(loud), 30,
                                       per_locale=5), ""]
    if out.pontoon:
        lines += [summary.pontoon_section(out.pontoon, heading="###")]
    lines += [
        f"Everything else is in the pull request {_pr_link(out)} and in the "
        f"[{project.display_name} report]({SITE}#/all/{project.name}).",
        "",
    ]
    return lines


def compose(outcomes: list[Outcome], dry_run: bool,
            today: str | None = None) -> tuple[str, str]:
    """The subject and the markdown body; the body is also the text part."""
    today = today or datetime.date.today().isoformat()
    done = [o for o in outcomes if o.ready or o.merged]
    held = [o for o in outcomes if o.reasons and not o.merged]
    noted = [o for o in outcomes if o.notes and o.pr is None and not o.reasons]
    quiet = [o for o in outcomes if o.pr is None and not o.reasons and not o.notes]

    subject = f"Localization QA — {today}"
    if held:
        subject += f" ({len(held)} pull request{'s' if len(held) > 1 else ''} "
        subject += "not merged)"

    lines = [f"# Localization QA — {today}", ""]
    if dry_run:
        lines += ["_Dry run: nothing was merged and nothing was sent._", ""]
    if held or noted:
        lines += ["## ⚠️ Needs a person", ""]
        for o in held:
            what = (f"{_pr_link(o)} was not merged" if o.pr
                    else "no pull request yet")
            lines.append(f"- **{o.project.display_name}** — {what}: "
                         + "; ".join(o.reasons) + ".")
            if o.delta:
                lines.append(f"{summary.report.SUB}Waiting in it: "
                             f"{_counts(o.delta)}.")
            lines += [f"{summary.report.SUB}{n}" for n in o.notes]
        for o in noted:
            lines.append(f"- **{o.project.display_name}** — no pull request. "
                         + " ".join(o.notes))
        lines.append("")
    for o in done:
        lines += _section(o, dry_run)
    if quiet:
        lines += ["No pull request open for "
                  + ", ".join(o.project.display_name for o in quiet)
                  + ": nothing changed.", ""]
    return subject, "\n".join(lines)


def _site():
    path = os.path.join(config.REPO_ROOT, "site", "build.py")
    spec = importlib.util.spec_from_file_location("_site_build", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def to_html(body: str) -> str:
    """The site's own escape-then-render, so a quoted string stays text."""
    fragment = _site().render_text(body, toc=False)
    style = ("body{font-family:sans-serif;line-height:1.4}"
             "table{border-collapse:collapse}"
             "th,td{border:1px solid #ccc;padding:2px 6px;text-align:right}"
             "th:first-child,td:first-child{text-align:left}"
             "code{background:#f3f3f3;padding:0 2px}")
    return (f'<!doctype html><html><head><meta charset="utf-8">'
            f"<style>{style}</style></head><body>{fragment}</body></html>")


def send(subject: str, body: str) -> None:
    user = os.environ["SMTP_USER"]
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"L10n Automation <{user}>"
    msg["To"] = ", ".join(RECIPIENTS)
    msg.attach(MIMEText(body, "plain", "utf-8"))
    msg.attach(MIMEText(to_html(body), "html", "utf-8"))
    server = smtplib.SMTP_SSL(os.environ.get("SMTP_SERVER", "smtp.gmail.com"),
                              int(os.environ.get("SMTP_PORT", "465")))
    server.login(user, os.environ["SMTP_PASSWORD"])
    server.sendmail(user, RECIPIENTS, msg.as_string())
    server.quit()


def _github_output(key: str, value: str) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(f"{key}={value}\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--merge", action="store_true",
                    help="merge every pull request that needs no person")
    ap.add_argument("--send", action="store_true",
                    help=f"email the digest to {', '.join(RECIPIENTS)}")
    args = ap.parse_args(argv)

    outcomes = [assess(p) for p in projects()]
    if args.merge:
        for o in outcomes:
            if o.ready:
                merge(o)
    subject, body = compose(outcomes, dry_run=not args.merge)

    print(f"Subject: {subject}\n\n{body}")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(body + "\n")
    _github_output("merged", str(any(o.merged for o in outcomes)).lower())

    if all(o.pr is None and not o.reasons and not o.notes for o in outcomes):
        print("nothing to report; no email sent")
    elif args.send:
        send(subject, body)
        print(f"sent to {len(RECIPIENTS)} recipient(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

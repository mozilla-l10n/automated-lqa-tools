#!/usr/bin/env python3
"""Record what Pontoon's reviewers did with the suggestions we sent.

Every suggestion Pontoon stored is listed in
``<project>/pontoon_suggestions/<locale>.json`` as ``pending``. This reads
the submitting account's translations back from Pontoon
(``/api/v2/users/<user>/translations/``) and moves each record on:

``approved``
    Recorded, and nothing else. The finding closes as **fixed** through the
    normal lifecycle once the sync changes the string in the repository:
    Pontoon approving it is not the repository changing, and closing it
    early would credit a fix nobody can see yet.

``rejected``
    What happens next depends on the string in the clone, rendered the way
    Pontoon renders it (``suggest.pontoon_preview``) and compared literally
    with what it said when the suggestion was sent:

    - it now reads as the suggestion: adopted through another submission,
      and the lifecycle records the fix;
    - it has moved to something else: the reviewer fixed it their own way or
      changed it for another reason. The finding stays open, and the next
      incremental review reads the new text and raises whatever is wrong
      with it on its own;
    - it has not moved: the reviewer said no. The string is dismissed in
      ``dismissed.txt`` with the reviewer's comment as the reason or, with
      no comment, a reason the model infers and is labelled as inferred.
      As in ``autosuggest``, a dismissal covers the whole string, so this
      only happens when every open finding on it is one the suggestion was
      for.

A dismissal written here carries the ``pontoon-rejected`` tag and is this
tool's to withdraw: if the outcome later changes, or the string moves after
all, the line is removed and the finding comes back. A line a person wrote
is never touched.

An upload whose text Pontoon already has on that string -- an older
translation by someone else, rejected or approved -- is not stored as a new
translation by the submitting account: Pontoon revives the existing one
(``translation:unrejected``), and the reviewer answers on *that*. The
account's own feed then has nothing on the string at all, so for a record
in that state the project's action log for the day it was sent is read
(``/api/v2/user-actions/<date>/project/<slug>/``), and the revived
translation's last explicit approval or rejection in range is its answer.
See `revived`.

A suggestion Pontoon has not answered -- unreviewed, or simply absent from
the window that was read -- stays ``pending``. Not hearing back is not an
answer, the same rule as for the reviewer model.

The QA workflows run this for the last two weeks before each review, so the
dismissals take effect in the same run. ``--since`` reaches further back;
ranges longer than Pontoon's limit are read in windows.

    python lib/pontoon_review.py --project android --locale it \\
        --l10n-dir ~/github/android-l10n            # show; writes nothing
    ... --write                                     # record it
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import urllib.error
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import local_secrets  # noqa: E402
import dismiss  # noqa: E402
import findings as findings_mod  # noqa: E402
import layout  # noqa: E402
import suggest  # noqa: E402
import tracker  # noqa: E402
from llm_incremental import _call, _close, language_of  # noqa: E402

PONTOON_TAG = "pontoon-rejected"
DEFAULT_USER = "l10n-qa-bot"
DEFAULT_DAYS = 14
# Pontoon refuses a range spanning more than this many days.
MAX_DAYS = 30
ANSWERED = ("approved", "rejected")


# --- reading Pontoon -----------------------------------------------------------

def entity_of(key: list) -> str:
    """The ``entity`` the API returns for Pontoon key ``key``: innermost first."""
    return " • ".join(reversed(key))


def windows(start: datetime.date, end: datetime.date) -> list[tuple]:
    """``[start, end]`` cut into inclusive ranges Pontoon accepts."""
    out = []
    while start <= end:
        stop = min(end, start + datetime.timedelta(days=MAX_DAYS))
        out.append((start, stop))
        start = stop + datetime.timedelta(days=1)
    return out


def fetch(server: str, user: str, slug: str, locale: str, start, end,
          token: str, get=suggest._get_json) -> list[dict]:
    """Every translation by ``user`` created, approved or rejected in range."""
    seen = {}
    for a, b in windows(start, end):
        query = urllib.parse.urlencode({
            "project": slug, "locale": locale,
            "start_date": a.isoformat(), "end_date": b.isoformat(),
        })
        url = (f"{server}/api/v2/users/{urllib.parse.quote(user)}/translations/"
               f"?{query}")
        while url:
            data = get(url, token)
            for row in data.get("results", []):
                seen[row["translation_pk"]] = row
            url = data.get("next")
    return list(seen.values())


def match(record: dict, results: list[dict]) -> dict | None:
    """The Pontoon translation that is this suggestion, or None.

    The text has to be equal as well as the entity: a later suggestion with
    different text on the same string is a different suggestion. Equal once
    Pontoon's MF2 is read back into the form the record holds: compared
    raw, every string with a placeholder or a tag in it stayed pending
    forever, whatever its reviewer had done.
    """
    p = record["pontoon"]
    entity = entity_of(p["key"])
    found = [r for r in results
             if r["project"] == p["project"] and r["resource"] == p["resource"]
             and r["entity"] == entity
             and record["text"] in (r["string"], suggest.preview_of_api(r["string"]))]
    if not found:
        return None
    return max(found, key=lambda r: max(filter(None, (
        r.get("date"), r.get("approved_date"), r.get("rejected_date")))))


REVIEWS = {"translation:approved": "approved", "translation:rejected": "rejected"}
_actions_cache: dict[tuple, list] = {}


def fetch_actions(server: str, slug: str, day: datetime.date, token: str,
                  get=suggest._get_json) -> list[dict]:
    """Every translation action on project ``slug`` on ``day``, any locale.

    Per project, not per locale, so it is cached across the locales of a run.
    """
    key = (server, slug, day, get)
    if key not in _actions_cache:
        url = f"{server}/api/v2/user-actions/{day.isoformat()}/project/{slug}/"
        _actions_cache[key] = get(url, token).get("actions", [])
    return _actions_cache[key]


def bot_pks(results: list[dict], actions: list[dict]) -> set:
    """The submitting account's user pk(s), as the action log names it.

    The log identifies users by pk and display name only. Anchored on the
    translations the account's own feed returned, so a display name -- which
    anybody can share -- never decides whose action an entry was.
    """
    ours = {r["translation_pk"] for r in results}
    return {a["user"]["pk"] for a in actions
            if a.get("translation", {}).get("pk") in ours and a.get("user")}


def in_feed(record: dict, results: list[dict]) -> bool:
    """Has the account's own feed any translation at all on this string?"""
    p = record["pontoon"]
    entity = entity_of(p["key"])
    return any(r["entity"] == entity and r["resource"] == p["resource"]
               and r["project"] == p["project"] for r in results)


def revived(record: dict, locale: str, results: list[dict], sent_actions: list[dict],
            later_actions: list[dict]) -> dict | None:
    """The answer to a suggestion Pontoon stored as an existing translation.

    ``sent_actions`` are the project's actions around the day it was sent,
    ``later_actions`` every action from then until the end of the range.
    Only for a record the account's feed has no row for on this string at
    all: anything there is the account's own translation, and `match`
    decides it. The revival has to be the account's, on this string, with
    exactly the text that was sent; the answer has to be an explicit review
    of that same translation. Anything short of that is None -- pending.

    Returns a result shaped like a feed row, so `decide` reads it as one.
    """
    p = record["pontoon"]
    entity = entity_of(p["key"])
    if in_feed(record, results):
        return None
    bots = bot_pks(results, sent_actions)

    def same_string(a) -> bool:
        return ((a.get("locale") or {}).get("code") == locale
                and (a.get("entity") or {}).get("key") == p["key"]
                and (a.get("resource") or {}).get("path") == p["resource"])

    revivals = [a for a in sent_actions
                if a["type"] == "translation:unrejected" and same_string(a)
                and (a.get("user") or {}).get("pk") in bots
                and record["text"] in (a["translation"]["string"],
                                       suggest.preview_of_api(a["translation"]["string"]))]
    if not revivals:
        return None
    pk = revivals[-1]["translation"]["pk"]
    reviews = sorted((a for a in later_actions
                      if a["type"] in REVIEWS and not a.get("is_implicit_action")
                      and a["translation"]["pk"] == pk and same_string(a)),
                     key=lambda a: a["date"])
    if not reviews:
        return None
    last = reviews[-1]
    status = REVIEWS[last["type"]]
    return {"translation_pk": pk, "string": last["translation"]["string"],
            "status": status, "date": revivals[-1]["date"],
            "approved_date": last["date"] if status == "approved" else None,
            "rejected_date": last["date"] if status == "rejected" else None,
            "entity": entity, "resource": p["resource"], "project": p["project"],
            "locale": locale, "url": "", "comments": [], "revived": True}


# --- deciding --------------------------------------------------------------------

def comment_text(result: dict) -> str:
    return "; ".join(
        f"{(c.get('author') or {}).get('username') or 'deleted user'}: "
        f"{' '.join(c['content'].split())}"
        for c in result.get("comments") or [] if c.get("content", "").strip()
    )


def decide(record: dict, result: dict | None, current: str | None,
           open_fids: set[str]) -> dict | None:
    """The fields that change on ``record``, or None if nothing does.

    ``current`` is the string in the clone in Pontoon's rendering, None if
    the clone no longer has it; ``open_fids`` are the open findings on the
    same string, whatever raised them. Pure, so the tests can pin it.
    ``needs_reason`` asks the caller for an inferred reason; ``dismiss``
    says whether a dismissal is wanted.
    """
    if result is None or result["status"] not in ANSWERED:
        return None
    status = result["status"]
    if status == record.get("status") and record.get("outcome"):
        return None
    when = (result.get(f"{status}_date") or result["date"])[:10]
    out = {"status": status, "status_date": when,
           "pontoon_pk": result["translation_pk"],
           "pontoon_url": result.get("url", ""),
           "comment": comment_text(result), "dismiss": False,
           "needs_reason": False}
    if status == "approved":
        return dict(out, outcome="approved", note=(
            "approved in Pontoon; the finding closes as fixed when the "
            "repository has the new text"))
    if current is None:
        return dict(out, outcome="obsolete",
                    note="rejected; the string is no longer in the repository")
    if current == record["text"]:
        return dict(out, outcome="adopted", note=(
            "rejected, but the repository now has this text, through another "
            "submission"))
    if current != record["original"]:
        return dict(out, outcome="moved", note=(
            "rejected, and the translation has changed since the suggestion; "
            "the finding stays open for the next review"))
    fids = set(record.get("fids") or [])
    if not fids:
        return dict(out, outcome="kept", note=(
            "rejected; sent without a finding, so there is nothing to dismiss"))
    if not open_fids & fids:
        return dict(out, outcome="kept",
                    note="rejected; its findings were already closed")
    others = open_fids - fids
    if others:
        return dict(out, outcome="kept", note=(
            f"rejected, but the string has {len(others)} other open finding(s), "
            "and a dismissal would cover them too; not dismissed"))
    return dict(out, outcome="dismissed", dismiss=True,
                needs_reason=not out["comment"],
                note="rejected with the translation unchanged; dismissed")


def reason_for(change: dict, inferred: str | None) -> str:
    if change["comment"]:
        return f"rejected in Pontoon: {change['comment']}"
    if inferred and inferred.strip().lower().rstrip(".") != "unclear":
        return ("rejected in Pontoon without comment; likely reason "
                f"(inferred): {inferred.strip()}")
    return "rejected in Pontoon without comment; reason unclear"


def _prefix(record: dict) -> str:
    """How every line this tool writes for ``record``'s string starts."""
    return f"{record['string_id']} @ {record['file']} — {PONTOON_TAG} ("


# --- the inferred reason -------------------------------------------------------

def _tool() -> dict:
    tool = {
        "name": "report_reasons",
        "description": "One likely rejection reason per string, or `unclear`.",
        "input_schema": {
            "type": "object",
            "properties": {"reasons": {"type": "array", "items": {
                "type": "object",
                "properties": {"ref": {"type": "integer"},
                               "reason": {"type": "string"}},
                "required": ["ref", "reason"],
            }}},
            "required": ["reasons"],
        },
    }
    _close(tool["input_schema"])
    return {**tool, "strict": True}


def infer_reasons(client, project, locale: str, items: list[dict]) -> dict[int, str]:
    """``{ref: reason}`` from one plain API request; no tools, no files."""
    with open(os.path.join(os.path.dirname(__file__), "prompts",
                           "rejection_reason.md"), encoding="utf-8") as fh:
        system = fh.read().format(
            language=language_of(locale), locale=locale,
            conventions=project.conventions(locale).strip()
            or "_No conventions recorded yet for this locale._")
    batch = json.dumps([{
        "ref": i, "string_id": r["string_id"], "source": r["source"],
        "original": r["original"], "rejected_suggestion": r["text"],
        "findings": r["findings"],
    } for i, r in enumerate(items)], ensure_ascii=False, indent=1)
    cfg = project.llm
    response = _call(client, cfg["model"], system, batch, _tool(), 4000,
                     effort=cfg.get("effort"))
    for block in response.content:
        if getattr(block, "type", "") == "tool_use" and block.name == "report_reasons":
            return {r["ref"]: r["reason"] for r in block.input.get("reasons", [])
                    if isinstance(r.get("ref"), int)}
    return {}


# --- one locale ------------------------------------------------------------------

def _current_reader(project, locale: str, l10n_dir: str, source_dir: str):
    trees = layout.load(project, locale, l10n_dir, source_dir)
    localized_of = suggest._localized_resolver(project, trees, l10n_dir)
    cache = {}

    def current(record: dict) -> str | None:
        path = os.path.join(l10n_dir, localized_of(record["file"]))
        if path not in cache:
            cache[path] = suggest._entries(path) if os.path.exists(path) else None
        if cache[path] is None:
            return None
        res, entries = cache[path]
        entry = entries.get(tuple(record["pontoon"]["key"]))
        return None if entry is None else suggest.pontoon_preview(res.format, entry)

    return current


def reconcile(project, locale: str, *, l10n_dir: str, source_dir: str,
              start, end, token: str, user: str = DEFAULT_USER,
              client=None, write: bool = False, log=print, get=suggest._get_json,
              current=None) -> dict:
    """Bring one locale's records up to date with Pontoon. Returns counts."""
    tpath, data = tracker.open_for(project, locale)
    records = data["suggestions"]
    counts: dict[str, int] = {}
    if not records:
        return counts
    current = current or _current_reader(project, locale, l10n_dir, source_dir)
    open_by_string: dict[tuple, set] = {}
    for f in findings_mod.load(project, locale):
        if f.status in findings_mod.OPEN_STATUSES:
            open_by_string.setdefault(f.key, set()).add(f.fid)

    results = {}
    for server, slug in sorted({(r["pontoon"]["server"], r["pontoon"]["project"])
                                for r in records}):
        results[(server, slug)] = fetch(server, user, slug, locale, start, end,
                                        token, get=get)

    def actions(server, slug, first, last):
        out, day = [], first
        while day <= last:
            out += fetch_actions(server, slug, day, token, get=get)
            day += datetime.timedelta(days=1)
        return out

    decided = []
    for record in records:
        server, slug = record["pontoon"]["server"], record["pontoon"]["project"]
        found = match(record, results[(server, slug)])
        sent = datetime.date.fromisoformat(record["date"])
        if (found is None and record.get("status") == "pending"
                and start <= sent <= end and not in_feed(record, results[(server, slug)])):
            # The day after too: the record's date is the runner's, the
            # log's is UTC.
            around = min(end, sent + datetime.timedelta(days=1))
            found = revived(record, locale, results[(server, slug)],
                            actions(server, slug, sent, around),
                            actions(server, slug, sent, end))
        now = current(record)
        change = decide(record, found, now,
                        open_by_string.get((record["file"], record["string_id"]), set()))
        if change is None and record.get("outcome") == "dismissed" \
                and now is not None and now != record["original"]:
            # Dismissed because the reviewer kept the old text, which has now
            # moved after all: the dismissal no longer describes the string.
            change = {"outcome": "moved", "dismiss": False, "needs_reason": False,
                      "note": "rejected, then the translation changed; the "
                              "dismissal was withdrawn and the finding reopened"}
        if change is not None and found and found.get("revived"):
            change["note"] += (" (Pontoon revived an existing translation with "
                               "this text rather than storing a new one)")
        if change is not None:
            decided.append((record, change))

    wanting = [r for r, c in decided if c["needs_reason"]]
    inferred: dict[int, str] = {}
    if wanting and client is not None:
        try:
            inferred = infer_reasons(client, project, locale, wanting)
        except Exception as exc:  # noqa: BLE001 - a missing reason is not fatal
            log(f"  could not infer rejection reasons: {exc}")
    by_id = {id(r): i for i, r in enumerate(wanting)}

    path = dismiss.path(project, locale)
    to_remove = []
    for record, change in decided:
        if record.get("outcome") == "dismissed" and change["outcome"] != "dismissed":
            to_remove.append(_prefix(record))
            record.pop("dismissal", None)
        if change["dismiss"]:
            reason = reason_for(change, inferred.get(by_id.get(id(record))))
            record["dismissal"] = dismiss.line(
                record["string_id"], record["file"], PONTOON_TAG,
                change["status_date"], reason)
        for key in ("status", "status_date", "comment", "pontoon_pk",
                    "pontoon_url", "outcome", "note"):
            if key in change:
                record[key] = change[key]
        counts[record["outcome"]] = counts.get(record["outcome"], 0) + 1
        log(f"  {record['outcome'].upper():9} {record['string_id']}: {record['note']}")
        if record.get("dismissal"):
            log(f"            {record['dismissal']}")
    # Every run, not only on a change: a merge that let the base's copy of
    # dismissed.txt win would otherwise lose a line for good.
    to_add = [r["dismissal"] for r in records
              if r.get("outcome") == "dismissed" and r.get("dismissal")]

    if write:
        removed = dismiss.remove(path, to_remove)
        added = dismiss.append(path, to_add)
        if decided:
            tracker.save(tpath, data)
        if removed or added:
            log(f"  {os.path.relpath(path, config.REPO_ROOT)}: "
                f"+{added} -{removed}")
    return counts


def main(argv=None) -> int:
    local_secrets.load("ANTHROPIC_API_KEY", "PONTOON_TOKEN")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", required=True)
    ap.add_argument("--locale", action="append", required=True,
                    help="repeatable, or `all` for every locale with records")
    ap.add_argument("--l10n-dir", required=True)
    ap.add_argument("--source-dir", help="defaults to --l10n-dir")
    today = datetime.date.today()
    ap.add_argument("--since", type=datetime.date.fromisoformat,
                    default=today - datetime.timedelta(days=DEFAULT_DAYS))
    ap.add_argument("--until", type=datetime.date.fromisoformat, default=today)
    ap.add_argument("--user", default=DEFAULT_USER)
    ap.add_argument("--no-llm", action="store_true",
                    help="never infer a reason; an uncommented rejection "
                         "reads 'reason unclear'")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args(argv)

    project = config.load(args.project)
    locales = args.locale
    if "all" in locales:
        locales = [loc for loc in project.locales
                   if os.path.exists(tracker.path(project, loc))]
    locales = [loc for loc in locales
               if tracker.load(tracker.path(project, loc))["suggestions"]]
    if not locales:
        print("no suggestions recorded; nothing to reconcile")
        return 0
    token = os.environ.get("PONTOON_TOKEN")
    if not token:
        print("::warning::PONTOON_TOKEN is not set; Pontoon review outcomes "
              "were not read")
        return 0
    client = None
    if not args.no_llm and os.environ.get("ANTHROPIC_API_KEY"):
        import anthropic
        client = anthropic.Anthropic()

    for locale in locales:
        print(f"== {project.name} {locale} ({args.since} → {args.until})")
        try:
            counts = reconcile(
                project, locale, l10n_dir=args.l10n_dir,
                source_dir=args.source_dir or args.l10n_dir,
                start=args.since, end=args.until, token=token, user=args.user,
                client=client, write=args.write)
        except (urllib.error.URLError, KeyError, ValueError) as exc:
            # A failure here must not stop the review that follows it.
            print(f"::warning::{locale}: could not read Pontoon: {exc}")
            continue
        print("  " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
                      or "no change"))
    if not args.write:
        print("\ndry run: pass --write to record this")
    # Zero even when every locale failed: the QA review runs straight after
    # this, and must not be stopped by Pontoon being unreachable.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

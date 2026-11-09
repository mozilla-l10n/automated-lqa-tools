#!/usr/bin/env python3
"""Propose locale conventions from the dismissals tools have recorded.

A dismissal covers one string. When the reviewer keeps raising the same
mistaken finding -- fy-NL's "Ut should be Út", when Frisian never writes a
diacritic on a capitalised initial -- each rejection retires one string and
the next new string gets the same finding. The rule that would stop it
belongs in ``locales/<code>/conventions.md``, which is injected into every
review prompt, and only a person may write there: the reasons behind most
tool-written dismissals are a model's inference, and a wrong one promoted to
a convention would hide a whole class of real defects with nobody having
decided it should.

So this proposes and never applies. It reads the ``pontoon-rejected`` and
``auto-suggest`` lines in the locale's ``dismissed.txt`` -- across every
project, since a rule of the language holds in all of them -- asks the model
in one plain request (no tools, no files) which reasons recur, and records
the answer in ``state/<locale>/convention_proposals.json``. The locale report
and the pull request body show each proposal with the dismissals behind it,
labelled as not applied. Adding it to ``conventions.md`` is the human step.

What the code enforces rather than asks for:

- A proposal needs ``MIN_STRINGS`` distinct strings behind it, at least one
  of them a Pontoon rejection. ``auto-suggest`` lines are a model declining
  to fix what another model raised; without a person having said no to
  something, the agreement is the model's with itself.
- A rejection whose reason is "unclear" says nothing about *why*, and is not
  evidence for any rule.
- The request is made only when its input changed: the evidence, the
  project's ``conventions.md``, the prompt or the model. Adding the proposed
  rule to ``conventions.md`` therefore re-asks, and the model is told to
  leave out what the conventions already say.

    python lib/proposals.py --project firefox --locale fy-NL    # show
    ... --write                                                  # record
"""

from __future__ import annotations

import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import dismiss  # noqa: E402
import local_secrets  # noqa: E402

HUMAN_TAG = "pontoon-rejected"   # must match pontoon_review.PONTOON_TAG
MODEL_TAG = "auto-suggest"       # must match autosuggest.DISMISS_TAG
MIN_STRINGS = 3

_LINE = re.compile(
    rf"^(?P<sid>\S+) @ (?P<file>.+?) — (?P<tag>{HUMAN_TAG}|{MODEL_TAG}) "
    r"\((?P<date>\d{4}-\d{2}-\d{2})(?:, string [0-9a-f]+)?\): (?P<reason>.+)$")
_UNCLEAR = "rejected in Pontoon without comment; reason unclear"
_INFERRED = "rejected in Pontoon without comment; likely reason (inferred): "
_COMMENT = "rejected in Pontoon: "
PROMPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts",
                      "convention_proposal.md")


def path(project, locale: str) -> str:
    return os.path.join(project.state_dir(locale), "convention_proposals.json")


def load(project, locale: str) -> list[dict]:
    """The recorded proposals for ``locale``; empty when there are none."""
    try:
        with open(path(project, locale), encoding="utf-8") as fh:
            return json.load(fh).get("proposals", [])
    except (OSError, ValueError):
        return []


def parse(text: str, project_name: str) -> list[dict]:
    """The tool-written dismissals in a ``dismissed.txt`` that carry a reason.

    Lines a person wrote are not read: they are already a person's decision,
    and nothing here should be suggesting what they meant.
    """
    out = []
    for raw in text.splitlines():
        m = _LINE.match(raw.strip())
        if not m:
            continue
        reason, kind = m["reason"].strip(), "model"
        if m["tag"] == HUMAN_TAG:
            if reason.startswith(_UNCLEAR):
                continue
            if reason.startswith(_INFERRED):
                reason, kind = reason[len(_INFERRED):], "rejected, reason inferred"
            elif reason.startswith(_COMMENT):
                reason, kind = reason[len(_COMMENT):], "rejected, reviewer's comment"
            else:
                kind = "rejected"
        out.append({"project": project_name, "string_id": m["sid"], "file": m["file"],
                    "tag": m["tag"], "kind": kind, "date": m["date"], "reason": reason})
    return out


def _projects() -> list[str]:
    return sorted(os.path.basename(os.path.dirname(p)) for p in
                  glob.glob(os.path.join(config.REPO_ROOT, "*", "config.yaml")))


def evidence(locale: str, projects: list[str] | None = None) -> list[dict]:
    """Every reasoned tool dismissal for ``locale``, in every project."""
    out = []
    for name in projects if projects is not None else _projects():
        p = dismiss.path(config.load(name), locale)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                out += parse(fh.read(), name)
    out.sort(key=lambda e: (e["project"], e["file"], e["string_id"]))
    return out


def _key(e: dict) -> tuple:
    return (e["project"], e["file"], e["string_id"])


def eligible(items: list[dict]) -> bool:
    """Whether ``items`` could support a proposal at all."""
    return (len({_key(e) for e in items}) >= MIN_STRINGS
            and any(e["tag"] == HUMAN_TAG for e in items))


def validate(raw: list, items: list[dict]) -> list[dict]:
    """Keep the model's proposals the evidence actually carries."""
    out = []
    for p in raw:
        rule = " ".join(str(p.get("rule", "")).split())
        refs = sorted({r for r in p.get("refs", [])
                       if isinstance(r, int) and 0 <= r < len(items)})
        support = list({_key(items[r]): items[r] for r in refs}.values())
        if rule and eligible(support):
            out.append({"rule": rule, "support": support})
    return out


def _fingerprint(items, conventions_text, prompt, model) -> str:
    h = hashlib.sha256()
    for part in (json.dumps(items, sort_keys=True, ensure_ascii=False),
                 conventions_text, prompt, model):
        h.update(part.encode("utf-8"))
        h.update(b"\0")
    return h.hexdigest()


def _tool() -> dict:
    from llm_incremental import _close
    tool = {
        "name": "report_proposals",
        "description": "Conventions the dismissals support; usually none.",
        "input_schema": {
            "type": "object",
            "properties": {"proposals": {"type": "array", "items": {
                "type": "object",
                "properties": {"rule": {"type": "string"},
                               "refs": {"type": "array", "items": {"type": "integer"}}},
                "required": ["rule", "refs"],
            }}},
            "required": ["proposals"],
        },
    }
    _close(tool["input_schema"])
    return {**tool, "strict": True}


def ask(client, project, locale: str, items: list[dict], prompt: str) -> list:
    """The model's raw proposals, from one plain API request."""
    from llm_incremental import _call, language_of
    system = prompt.format(
        language=language_of(locale), locale=locale, min_strings=MIN_STRINGS,
        conventions=project.conventions(locale).strip()
        or "_No conventions recorded yet for this locale._")
    batch = json.dumps([{"ref": i, "project": e["project"], "string_id": e["string_id"],
                         "kind": e["kind"], "reason": e["reason"]}
                        for i, e in enumerate(items)], ensure_ascii=False, indent=1)
    cfg = project.llm
    response = _call(client, cfg["model"], system, batch, _tool(), 4000,
                     effort=cfg.get("effort"))
    for block in response.content:
        if getattr(block, "type", "") == "tool_use" and block.name == "report_proposals":
            return block.input.get("proposals", [])
    return []


def refresh(project, locale: str, client, *, write: bool = False, log=print,
            items: list[dict] | None = None) -> list[dict]:
    """Bring ``locale``'s proposals up to date; returns them.

    Asks only when the input changed since the recorded answer. With too
    little evidence for any proposal, records none without asking.
    """
    items = evidence(locale) if items is None else items
    with open(PROMPT, encoding="utf-8") as fh:
        prompt = fh.read()
    model = project.llm["model"]
    fingerprint = _fingerprint(items, project.conventions(locale), prompt, model)
    p = path(project, locale)
    try:
        with open(p, encoding="utf-8") as fh:
            stored = json.load(fh)
    except (OSError, ValueError):
        stored = {}
    if stored.get("input") == fingerprint:
        return stored.get("proposals", [])
    asked = eligible(items)
    if not asked:
        proposals = []
    elif client is None:
        return stored.get("proposals", [])
    else:
        proposals = validate(ask(client, project, locale, items, prompt), items)
    for prop in proposals:
        log(f"  PROPOSED  {prop['rule']}")
        for e in prop["support"]:
            log(f"            {e['project']} {e['string_id']} ({e['kind']}): {e['reason']}")
    # Recorded when asked, so an answer of "nothing" is not re-asked every
    # run; with nothing asked, only to clear an earlier answer.
    if write and (asked or stored):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            json.dump({"input": fingerprint, "date": datetime.date.today().isoformat(),
                       "proposals": proposals}, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    return proposals


def new_since(before: list[dict], after: list[dict]) -> list[dict]:
    """Proposals in ``after`` whose evidence ``before`` had not already shown.

    Keyed on the supporting strings rather than the wording, which the model
    is free to vary from one request to the next: a proposal is news when
    some string behind it was behind no earlier proposal.
    """
    seen = {_key(e) for prop in before for e in prop.get("support", [])}
    return [prop for prop in after
            if any(_key(e) not in seen for e in prop.get("support", []))]


def render(proposals: list[dict], project_name: str, locale: str,
           title: str = "### Proposed conventions — not applied",
           cap: int | None = None, sub: str = "    ") -> str:
    """Markdown for a report or, with ``cap`` on the evidence, a PR body."""
    if not proposals:
        return ""
    out = [f"{title} ({len(proposals)})", "",
           f"Recurring reasons in this locale's tool-written dismissals. Nothing "
           f"here reaches the reviewer until a person adds it to "
           f"`{project_name}/locales/{locale}/conventions.md`; an inferred reason "
           f"is a model's guess at why a Pontoon reviewer said no.", ""]
    for prop in proposals:
        support = prop["support"]
        rejected = sum(1 for e in support if e["tag"] == HUMAN_TAG)
        out += [f"- {prop['rule']}",
                f"{sub}_Behind it: {len(support)} dismissals, {rejected} of them "
                f"rejected in Pontoon._", ""]
        # Rejections first: they are what makes the proposal more than a
        # model agreeing with itself.
        ordered = sorted(support, key=lambda e: e["tag"] != HUMAN_TAG)
        shown = ordered if cap is None else ordered[:cap]
        for e in shown:
            where = "" if e["project"] == project_name else f" ({e['project']})"
            out.append(f"{sub}- `{e['string_id']}`{where} — _{e['kind']}_: {e['reason']}")
        if len(shown) < len(ordered):
            out.append(f"{sub}- …and {len(ordered) - len(shown)} more in the locale report")
        out.append("")
    return "\n".join(out)


def main(argv=None) -> int:
    local_secrets.load("ANTHROPIC_API_KEY")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--project", required=True)
    ap.add_argument("--locale", required=True)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args(argv)
    project = config.load(args.project)
    client = None
    if os.environ.get("ANTHROPIC_API_KEY"):
        import anthropic
        client = anthropic.Anthropic()
    proposals = refresh(project, args.locale, client, write=args.write)
    if not proposals:
        print("no proposals")
    if not args.write:
        print("\ndry run: pass --write to record this")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

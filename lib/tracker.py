"""The record of suggestions submitted to Pontoon.

One file per locale, ``<project>/pontoon_suggestions/<locale>.json``, written
by every path that submits: ``suggest.py upload --submit`` (a person's
edits), ``autosuggest.py run --submit`` (the model's) and
``suggest.py backfill`` (submissions made before this file existed). A
string listed here, in any status, is never suggested again: ``pending`` is
waiting on a reviewer, ``approved`` is done, and ``rejected`` was a person's
answer.

Only suggestions Pontoon actually stored are recorded, each with its review
``status`` (``pending`` until somebody updates it), the ``status_date`` it
last changed and an optional ``comment``, typically why it was rejected.
"""

from __future__ import annotations

import json
import os

TRACKER_DIR = "pontoon_suggestions"
STATUSES = ("pending", "approved", "rejected")


def path(project, locale: str) -> str:
    return os.path.join(project.root, TRACKER_DIR, f"{locale}.json")


def load(file: str) -> dict:
    if not os.path.exists(file):
        return {"suggestions": []}
    with open(file, encoding="utf-8") as fh:
        return json.load(fh)


def save(file: str, data: dict) -> None:
    data["suggestions"].sort(key=lambda s: (s["date"], s["file"], s["string_id"]))
    data = {"project": data.get("project"), "locale": data.get("locale"),
            **{k: v for k, v in data.items() if k not in ("project", "locale")}}
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


def identity(entry: dict) -> tuple:
    return (entry["file"], entry["string_id"], entry["text"])


def strings(*trackers: dict) -> set[tuple[str, str]]:
    """``(file, string_id)`` of every string with a suggestion recorded."""
    return {(s["file"], s["string_id"]) for t in trackers for s in t["suggestions"]}


def entry(*, date: str, group: str, file: str, string_id: str, server: str,
          slug: str, resource: str, key: list, fids: list[str],
          findings: list[str], source: str, original: str, text: str) -> dict:
    return {
        "date": date,
        "group": group,
        "file": file,
        "string_id": string_id,
        "pontoon": {"server": server, "project": slug, "resource": resource,
                    "key": list(key)},
        "fids": fids,
        "findings": findings,
        "source": source,
        "original": original,
        "text": text,
        "status": "pending",
        "status_date": date,
        "comment": "",
    }


def add(data: dict, new: dict) -> bool:
    """Append ``new`` unless the same text is already recorded for its string."""
    if identity(new) in {identity(s) for s in data["suggestions"]}:
        return False
    data["suggestions"].append(new)
    return True


def open_for(project, locale: str) -> tuple[str, dict]:
    """``(path, data)`` for a locale, with its header filled in."""
    file = path(project, locale)
    data = load(file)
    data.setdefault("project", project.name)
    data.setdefault("locale", locale)
    return file, data

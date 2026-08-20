"""Per-locale content snapshots and the run-to-run delta.

The snapshot is the whole basis for incremental review. For every string it
stores two short hashes -- the localized text and the en-US source text --
so a run can tell, without any repository history:

* the translation changed              -> re-review
* the English changed under it         -> re-review (a stale translation)
* the string is new                    -> review
* the string is gone                   -> retire its findings

On disk it is grouped by file, one string per line::

    {
     "browser/browser/appmenu.ftl": {
      "appmenu-menu-button-closed2": "3f9c1a2b 88ad0e14",
      "appmenu-new-tab": "0c4e77aa"
     }
    }

The value is ``"<locale-hash> <source-hash>"``; the source hash is omitted
for strings with no en-US counterpart. Grouping by file keeps the payload
around 1 MB per locale and makes git diffs read as "these strings moved".
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field

Key = tuple[str, str]


@dataclass
class Delta:
    new: list[Key] = field(default_factory=list)
    changed: list[Key] = field(default_factory=list)
    source_changed: list[Key] = field(default_factory=list)
    removed: list[Key] = field(default_factory=list)
    unchanged: int = 0

    @property
    def to_review(self) -> list[Key]:
        """Strings an LLM pass should look at, de-duplicated, order-stable."""
        seen: dict[Key, None] = {}
        for k in self.new + self.changed + self.source_changed:
            seen[k] = None
        return list(seen)

    def is_empty(self) -> bool:
        return not (self.new or self.changed or self.source_changed or self.removed)

    def summary(self) -> str:
        return (
            f"new={len(self.new)} changed={len(self.changed)} "
            f"source-changed={len(self.source_changed)} "
            f"removed={len(self.removed)} unchanged={self.unchanged}"
        )


def build(l10n: dict, source: dict) -> dict[str, dict[str, str]]:
    """Snapshot of the current trees, keyed file -> id -> hashes."""
    snap: dict[str, dict[str, str]] = {}
    for (file, mid), msg in l10n.items():
        src = source.get((file, mid))
        value = msg.hash()
        if src is not None:
            value = f"{value} {src.hash()}"
        snap.setdefault(file, {})[mid] = value
    return snap


def _split(value: str) -> tuple[str, str | None]:
    loc, _, src = value.partition(" ")
    return loc, (src or None)


def diff(previous: dict, current: dict) -> Delta:
    d = Delta()
    for file, ids in current.items():
        prev_ids = previous.get(file, {})
        for mid, value in ids.items():
            prev = prev_ids.get(mid)
            if prev is None:
                d.new.append((file, mid))
                continue
            cur_l, cur_s = _split(value)
            prev_l, prev_s = _split(prev)
            if cur_l != prev_l:
                d.changed.append((file, mid))
            elif cur_s != prev_s:
                d.source_changed.append((file, mid))
            else:
                d.unchanged += 1
    for file, ids in previous.items():
        cur_ids = current.get(file, {})
        for mid in ids:
            if mid not in cur_ids:
                d.removed.append((file, mid))
    return d


def merge(previous: dict, current: dict, reviewed: set) -> dict:
    """Advance the snapshot only for strings the model actually reviewed.

    The snapshot means "content the reviewer has already seen", so a partial
    run must not claim more than it did. Running one partition of a
    baseline, or capping the batch with --limit, or skipping the model
    entirely with --no-llm, all used to write a complete snapshot -- which
    silently marked everything unreviewed as seen, and the skipped strings
    would never be looked at again.

    A string is recorded at its current hash if it was reviewed, or if it
    has not changed since the last snapshot. Otherwise it keeps its old hash
    -- so it still reads as changed next time -- or is left out entirely if
    it is new, so it reads as new.
    """
    out: dict[str, dict[str, str]] = {}
    for file, ids in current.items():
        prev_ids = previous.get(file, {})
        for mid, value in ids.items():
            if (file, mid) in reviewed or prev_ids.get(mid) == value:
                out.setdefault(file, {})[mid] = value
            elif mid in prev_ids:
                out.setdefault(file, {})[mid] = prev_ids[mid]
    return out


def load(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save(path: str, snap: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    j = lambda v: json.dumps(v, ensure_ascii=False)  # noqa: E731
    blocks = []
    for file in sorted(snap):
        rows = ",\n".join(f"  {j(mid)}: {j(snap[file][mid])}" for mid in sorted(snap[file]))
        blocks.append(f" {j(file)}: {{\n{rows}\n }}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("{\n" + ",\n".join(blocks) + "\n}\n")

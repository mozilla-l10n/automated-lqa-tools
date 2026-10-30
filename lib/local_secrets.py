"""Secrets for local runs, from `secrets.env` at the repository root.

So a local run does not need a round of `export` first. The file is
git-ignored; `secrets.env-dist` lists every name the scripts read.

A variable already set in the environment wins, which is how CI works: the
workflows set them from repository secrets and have no file. Each script
asks only for the names it uses, so a review run -- which hands its
environment to the baseline agent -- never carries the Pontoon token or the
SMTP password just because they are in the file.
"""

from __future__ import annotations

import os

PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "secrets.env")


def read(path: str = PATH) -> dict[str, str]:
    """``NAME=value`` lines; blanks and ``#`` comments skipped, quotes dropped."""
    if not os.path.exists(path):
        return {}
    out = {}
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            name, _, value = line.partition("=")
            name = name.strip().removeprefix("export ").strip()
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
                value = value[1:-1]
            if value:
                out[name] = value
    return out


def load(*names: str, path: str = PATH) -> None:
    """Put each of ``names`` from the file into the environment, if unset."""
    found = read(path)
    for name in names:
        if not os.environ.get(name) and name in found:
            os.environ[name] = found[name]

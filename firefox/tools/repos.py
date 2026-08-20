"""Cloning and refreshing the two upstream repositories.

``firefox-l10n`` is ~1.6 GB with 380k commits, so it is never cloned in
full. A blobless, depth-1, sparse clone of the locales actually being
checked is enough: the delta engine compares content hashes it stored
itself, so no history is required.

A local clone can be pointed at instead (``--l10n-dir`` / ``--source-dir``),
which is how the system is developed and how the legacy import runs.
"""

from __future__ import annotations

import os
import subprocess


def run(cmd: list[str], cwd: str | None = None) -> str:
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"command failed: {' '.join(cmd)}\n{proc.stdout}\n{proc.stderr}"
        )
    return proc.stdout.strip()


def head_sha(path: str) -> str:
    try:
        return run(["git", "-C", path, "rev-parse", "HEAD"])[:12]
    except Exception:
        return "unknown"


def head_date(path: str) -> str:
    try:
        return run(["git", "-C", path, "log", "-1", "--format=%cs"])
    except Exception:
        return ""


def current_branch(path: str) -> str:
    try:
        return run(["git", "-C", path, "rev-parse", "--abbrev-ref", "HEAD"])
    except Exception:
        return ""


def describe(path: str) -> str:
    """`<sha> on <branch>, <date>` -- enough to spot a stale checkout."""
    sha, br, date = head_sha(path), current_branch(path), head_date(path)
    bits = [b for b in (sha, f"on {br}" if br and br != "HEAD" else "", date) if b]
    return ", ".join(bits) or "not a git checkout"


def ensure_clone(url: str, branch: str, dest: str, sparse: list[str] | None) -> str:
    """Clone if absent, otherwise fast-forward. Returns ``dest``."""
    if not os.path.exists(os.path.join(dest, ".git")):
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
        cmd = [
            "git",
            "clone",
            "--filter=blob:none",
            "--depth",
            "1",
            "--branch",
            branch,
        ]
        if sparse:
            cmd += ["--sparse"]
        cmd += [url, dest]
        run(cmd)
    else:
        run(["git", "-C", dest, "fetch", "--depth", "1", "origin", branch])
        run(["git", "-C", dest, "reset", "--hard", f"origin/{branch}"])
    if sparse:
        run(["git", "-C", dest, "sparse-checkout", "set", "--no-cone", *sparse])
    return dest


def ensure_local(path: str) -> str:
    path = os.path.expanduser(path)
    if not os.path.isdir(path):
        raise RuntimeError(f"not a directory: {path}")
    return path

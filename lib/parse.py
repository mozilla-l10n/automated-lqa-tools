"""Parsing and canonical serialization of localization resources.

Everything downstream (snapshots, checks, prompts, reports) works on the
``Msg`` records produced here, never on raw file text. The parser is
``moz.l10n`` -- the same one the manual reviews used -- so results stay
comparable with the legacy reports.
"""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass, field
from fnmatch import fnmatch

from moz.l10n.model import (
    CatchallKey,
    Expression,
    Markup,
    PatternMessage,
    SelectMessage,
    VariableRef,
)
from moz.l10n.resource import parse_resource

# Placeholders are rendered back in native Fluent syntax rather than an
# invented marker: it is what the strings actually look like, so reports read
# naturally and the model sees the syntax it knows.
REF = "{ %s }"
VAR = "{ $%s }"


@dataclass
class Msg:
    """One localizable message: its value plus every attribute."""

    file: str  # path relative to the locale tree
    id: str  # Fluent message/term id, or .properties key
    comment: str = ""
    # property name ("" = the message value itself) -> flattened text
    props: dict[str, str] = field(default_factory=dict)
    # property name -> the raw moz.l10n message object
    raw: dict[str, object] = field(default_factory=dict)
    line: int = 0

    @property
    def key(self) -> tuple[str, str]:
        return (self.file, self.id)

    @property
    def value(self) -> str:
        return self.props.get("", "")

    def text(self) -> str:
        """Everything a human reviewer needs to read, as one string."""
        if list(self.props) == [""]:
            return self.value
        return "\n".join(
            f"{k or '(value)'}: {v}"
            for k, v in sorted(self.props.items())
            if v or k
        )

    def hash(self) -> str:
        """Content hash: the message's own text, and nothing else.

        Deliberately not the comment. This is what a finding records as the
        string it was raised against, so a comment edit must not make an
        untouched translation read as fixed.
        """
        h = hashlib.sha1()
        for k in sorted(self.props):
            h.update(k.encode())
            h.update(b"\x00")
            h.update(self.props[k].encode())
            h.update(b"\x01")
        return h.hexdigest()[:8]

    def context_hash(self) -> str:
        """Hash of the developer comment.

        Used only on the source side, only to decide whether a translation is
        worth re-reviewing. The comment goes into the review prompt and is
        often the only thing that says what a string means, so a corrected
        en-US comment can turn a plausible translation into a wrong one --
        and with the text unchanged, nothing else would ever notice.
        """
        if not self.comment:
            return ""
        return hashlib.sha1(self.comment.encode()).hexdigest()[:8]


def _flatten(pattern) -> str:
    out: list[str] = []
    for part in pattern:
        if isinstance(part, str):
            out.append(part)
        elif isinstance(part, Expression):
            # Android keeps the original printf spec on the expression, so a
            # placeholder renders as `%1$s` rather than an invented
            # `{ $arg1 }`. Reports read like the file, and the reviewer sees
            # the syntax it will be asked about. Fluent has no `source`
            # attribute, so nothing changes there.
            literal = (part.attributes or {}).get("source")
            if isinstance(literal, str) and literal:
                out.append(literal)
            elif isinstance(part.arg, VariableRef):
                out.append(VAR % part.arg.name)
            elif isinstance(part.arg, str):
                out.append(REF % part.arg)
        elif isinstance(part, Markup):
            name = part.name
            if part.kind == "close":
                out.append(f"</{name}>")
            else:
                attrs = "".join(
                    f" {k}" for k in list(part.options) + list(part.attributes)
                )
                out.append(f"<{name}{attrs}{'/' if part.kind == 'standalone' else ''}>")
    return "".join(out)


def _variant_key(key) -> str:
    parts = []
    for k in key:
        parts.append(k.value if isinstance(k, CatchallKey) else str(k))
    return " ".join(parts)


def flatten(msg) -> str:
    """Flatten a message to a single readable string.

    SelectMessage keeps every variant, tagged by key, because a defect can
    live in one variant only (reversed plurals, an undefined ``$var`` in
    ``[one]``).
    """
    if isinstance(msg, PatternMessage):
        return _flatten(msg.pattern)
    if isinstance(msg, SelectMessage):
        sel = ", ".join(
            s.name if isinstance(s, VariableRef) else str(s) for s in msg.selectors
        )
        body = " ".join(
            f"[{_variant_key(k)}] {_flatten(v)}" for k, v in msg.variants.items()
        )
        return f"{{${sel} ->}} {body}"
    return str(msg)


def is_excluded(rel: str, patterns: list[str]) -> bool:
    return any(fnmatch(rel, p) for p in patterns)


def parse_tree(root: str, extensions: list[str], exclude: list[str],
               errors: dict | None = None) -> dict:
    """Parse a whole locale (or reference) tree.

    Returns ``{(relpath, id): Msg}``. A file that fails to parse is skipped so
    one broken file cannot abort a run; pass ``errors`` to collect what went
    wrong, which is what the health check's syntax row reports.
    """
    out: dict[tuple[str, str], Msg] = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", ".hg")]
        for fn in sorted(filenames):
            if not any(fn.endswith(e) for e in extensions):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, root)
            if is_excluded(rel, exclude):
                continue
            for msg in parse_file(path, rel, errors):
                out[msg.key] = msg
    return out


def parse_file(path: str, rel: str, errors: dict | None = None) -> list[Msg]:
    """Parse one resource file into ``Msg`` records.

    A file that does not parse yields nothing rather than raising, so one
    broken file cannot abort a run. Pass ``errors`` to be told which files
    those were and why: the syntax check used to answer that by parsing the
    whole tree a second time, and for a layout where many keys resolve to one
    large file it parsed that file once per key.
    """
    try:
        res = parse_resource(path)
    except Exception as exc:  # noqa: BLE001 - the message is the finding
        if errors is not None:
            errors[rel] = str(exc)
        return []
    msgs: list[Msg] = []
    for section in res.sections:
        prefix = list(section.id or ())
        for entry in section.entries:
            if not hasattr(entry, "id"):
                continue
            mid = ".".join(prefix + list(entry.id))
            props = {"": flatten(entry.value)}
            raw: dict[str, object] = {"": entry.value}
            for pname, pval in (entry.properties or {}).items():
                props[pname] = flatten(pval)
                raw[pname] = pval
            msgs.append(
                Msg(
                    file=rel,
                    id=mid,
                    comment=(entry.comment or "").strip(),
                    props=props,
                    raw=raw,
                    line=getattr(getattr(entry, "linepos", None), "start", 0) or 0,
                )
            )
    return msgs


def list_files(root: str, extensions: list[str], exclude: list[str]) -> set[str]:
    """Relative paths of every parseable resource file under ``root``."""
    found: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", ".hg")]
        for fn in filenames:
            if not any(fn.endswith(e) for e in extensions):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), root)
            if not is_excluded(rel, exclude):
                found.add(rel)
    return found

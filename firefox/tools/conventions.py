"""Detect a locale's typographic and register conventions by counting.

The single most productive rule from the manual reviews: *never assume what
is correct for a language -- count what the locale actually does, then flag
deviations from its own majority.* Assuming produced real false positives:

* ``ja`` writes ellipsis as three ASCII dots (367) not ``…`` (6)
* ``nl``'s house dash is the en dash ``–`` (100) not ``—`` (42)
* ``pl`` uses ``„…”``; ``fr`` uses ``« »`` with U+00A0; ``tr`` uses ``“…”``
* ``ja``/``zh-CN`` keep English access keys on purpose

So every check that could be locale-dependent asks this module first, and
the numbers are printed in the report so a human can audit the inference.
"""

from __future__ import annotations

import json
import os
import re

# Text that is never prose and must not feed convention counts: CSS in
# .style attributes, HTML attribute values, URLs, code-ish tokens.
_SKIP_PROPS = {"style", "accesskey"}
_URL = re.compile(r"https?://\S+|chrome://\S+|about:[a-z-]+")
_PLACEHOLDER = re.compile(r"\{\s*[$-][^}]*\}")
_TAG = re.compile(r"</?[a-zA-Z][^>]*>")
_VARIANT_TAG = re.compile(r"\[[a-zA-Z0-9_*-]+\]|\{\$[^}]*->\}")

QUOTE_PAIRS = {
    "curly-double": ("“", "”"),  # “ ”
    "german-double": ("„", "“"),  # „ “
    "polish-double": ("„", "”"),  # „ ”
    "guillemet": ("«", "»"),  # « »
    "curly-single": ("‘", "’"),  # ‘ ’
    "straight-double": ('"', '"'),
    "corner": ("「", "」"),  # 「 」
}

# Register markers: second-person pronouns that reveal formal/informal
# address. Counted as whole words, case-insensitively.
REGISTER = {
    "de": {"informal": ["du", "dein", "deine", "deinen", "dir", "dich"],
           "formal": ["sie", "ihr", "ihre", "ihren", "ihnen"]},
    "fr": {"informal": ["tu", "ton", "ta", "tes", "toi"],
           "formal": ["vous", "votre", "vos"]},
    "es-ES": {"informal": ["tu", "tus", "tú", "contigo"],
              "formal": ["usted", "su", "sus"]},
    "es-MX": {"informal": ["tu", "tus", "tú", "contigo"],
              "formal": ["usted", "su", "sus"]},
    "it": {"informal": ["tuo", "tua", "tuoi", "tue"],
           "formal": ["suo", "sua", "vostro"]},
    "nl": {"informal": ["je", "jouw", "jij"], "formal": ["u", "uw"]},
    "pt-BR": {"informal": ["você", "seu", "sua"], "formal": ["vós"]},
    "ru": {"informal": ["ты", "твой", "твоя"], "formal": ["вы", "ваш", "ваша"]},
    "tr": {"informal": ["sen", "senin"], "formal": ["siz", "sizin"]},
    "zh-CN": {"informal": ["你"], "formal": ["您"]},
    "sl": {"informal": ["tvoj", "ti"], "formal": ["vaš", "vi"]},
    "pl": {"informal": ["twój", "twoje", "ty"], "formal": ["państwa", "wasz"]},
}


def _count_quotes(texts: list[str]) -> dict[str, int]:
    """Count quote *pairs*, not lone characters.

    Several families share an opening character -- German ``„…“`` and Polish
    ``„…”`` both open with U+201E -- so counting the opener alone reports a
    tie. Matching the closing character too resolves them. The pattern is
    non-greedy and bounded so an unbalanced quote cannot swallow a whole
    string.
    """
    quotes: dict[str, int] = {}
    for name, (open_ch, close_ch) in QUOTE_PAIRS.items():
        if name == "straight-double":
            continue
        pattern = re.compile(
            f"{re.escape(open_ch)}[^{re.escape(open_ch)}{re.escape(close_ch)}]{{0,300}}?"
            f"{re.escape(close_ch)}"
        )
        total = sum(len(pattern.findall(t)) for t in texts)
        if total:
            quotes[name] = total
    straight = re.compile(r'"[^"]{0,300}?"')
    total = sum(len(straight.findall(t)) for t in texts)
    if total:
        quotes["straight-double"] = total
    return dict(sorted(quotes.items(), key=lambda kv: -kv[1]))


def clean(text: str) -> str:
    """Strip everything that is not human-readable prose."""
    text = _PLACEHOLDER.sub(" ", text)
    text = _VARIANT_TAG.sub(" ", text)
    text = _URL.sub(" ", text)
    text = _TAG.sub(" ", text)
    return text


def _prose(messages: dict) -> list[str]:
    out = []
    for msg in messages.values():
        for pname, value in msg.props.items():
            if pname in _SKIP_PROPS or not value:
                continue
            out.append(clean(value))
    return out


def detect(locale: str, messages: dict) -> dict:
    """Count the locale's conventions over its whole tree."""
    texts = _prose(messages)
    blob = "\n".join(texts)
    counts: dict[str, object] = {}

    counts["quotes"] = _count_quotes(texts)

    counts["apostrophe"] = {
        "typographic": blob.count("’"),
        "straight": len(re.findall(r"(?<=\w)'(?=\w)|(?<=\w)'(?=\s|$)", blob)),
    }
    counts["ellipsis"] = {
        "char": blob.count("…"),
        "ascii": len(re.findall(r"(?<!\.)\.\.\.(?!\.)", blob)),
    }
    counts["dash"] = {
        "em": blob.count("—"),
        "en": blob.count("–"),
    }
    counts["nbsp"] = {
        "total": blob.count(" "),
        "narrow": blob.count(" "),
        "before-punctuation": len(re.findall("[  ][?!;:%]", blob)),
        "space-before-punctuation": len(re.findall(r"(?<=\w) [?!;:](?=\s|$)", blob)),
    }
    counts["inverted_marks"] = {
        "open-question": blob.count("¿"),
        "open-exclamation": blob.count("¡"),
    }
    counts["fullwidth"] = {
        "punctuation": len(re.findall("[，。？！：；]", blob)),
    }

    markers = REGISTER.get(locale)
    if markers:
        register = {}
        for kind, words in markers.items():
            total = 0
            for w in words:
                pattern = re.escape(w)
                if w.isascii():
                    pattern = rf"\b{pattern}\b"
                total += len(re.findall(pattern, blob, re.IGNORECASE))
            register[kind] = total
        counts["register"] = register

    counts["_meta"] = {"locale": locale, "strings": len(messages), "prose_chunks": len(texts)}
    return counts


def preferred(counts: dict, group: str, minimum_ratio: float = 3.0) -> str | None:
    """The dominant option in a counted group, or None if it is a real mix.

    ``minimum_ratio`` is deliberately high: a 2:1 split is a locale that has
    not settled, and flagging the minority there would produce noise rather
    than defects.
    """
    values = counts.get(group) or {}
    ranked = sorted(((v, k) for k, v in values.items() if isinstance(v, int)), reverse=True)
    ranked = [(v, k) for v, k in ranked if v > 0]
    if not ranked:
        return None
    if len(ranked) == 1:
        return ranked[0][1]
    top, second = ranked[0], ranked[1]
    return top[1] if top[0] >= second[0] * minimum_ratio else None


def render(counts: dict) -> str:
    """Markdown table for the report's health-check section."""
    rows = ["| Convention | Counts | Inferred |", "|---|---|---|"]
    for group in ("quotes", "apostrophe", "ellipsis", "dash", "nbsp",
                  "inverted_marks", "fullwidth", "register"):
        values = counts.get(group)
        if not values:
            continue
        shown = ", ".join(f"`{k}` {v}" for k, v in values.items() if v)
        if not shown:
            continue
        pref = preferred(counts, group)
        rows.append(f"| {group.replace('_', ' ')} | {shown} | {f'**{pref}**' if pref else '_mixed_'} |")
    return "\n".join(rows)


def path(project, locale: str) -> str:
    return os.path.join(project.state_dir(locale), "conventions.json")


def save(project, locale: str, counts: dict) -> None:
    p = path(project, locale)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(counts, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")


def load(project, locale: str) -> dict:
    p = path(project, locale)
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


DRAFT_HEADER = """# {locale} — conventions and review instructions

_Counted over the whole {locale} tree on {date}. Review this, correct
anything the counting got wrong, and add prose instructions for the reviewer
below. This file is injected verbatim into every review prompt, so anything
written here is what the model is told to treat as correct._

## Detected conventions

{table}

## Instructions for the reviewer

<!-- Add rules here, e.g.:
- Access keys are intentionally left as English letters; never flag them.
- The en dash is the house dash; do not suggest an em dash.
- "Primary Password" is deliberately translated with the legacy term.
-->
"""


def draft(locale: str, counts: dict, date: str) -> str:
    return DRAFT_HEADER.format(locale=locale, date=date, table=render(counts))

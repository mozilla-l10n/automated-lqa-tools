"""Support for locales that are variants of the source language.

`en-GB` and `en-CA` break the assumption the rest of the pipeline rests on.
For an ordinary locale a string identical to en-US is untranslated, and
skipping it is right. Here 93% of `en-GB` and 97% of `en-CA` are identical
to en-US *and correct*, while the most valuable question is the opposite
one: **is this string identical when it should not be?** A missed
`colour`, a `Syncing:` label that should read `Synchronising:`.

So for a variant the pipeline flips: identical strings are the interesting
population rather than the discarded one, "file is identical to en-US" stops
being a signal at all, and the defect classes are spelling, vocabulary and
date or unit conventions rather than mistranslation.

The spelling map is **learned from the locale**, not hardcoded. Every string
that does differ from en-US is a worked example of what this variant
changes; aligning the two word by word yields `color -> colour`,
`organization -> organisation`, `syncing -> synchronising` and so on, with
no list to maintain and no assumption about which variant of English -- or
which pair of languages -- is involved. The same machinery would work for
`pt-PT` against `pt-BR`.

Only near-universal substitutions are used. `forward -> forwards` and
`cert -> certificate` show up in the alignment too, but the locale keeps the
original form far more often than it changes it, so they are contextual
choices rather than rules, and applying them everywhere would be wrong.
"""

from __future__ import annotations

import difflib
import re
from collections import Counter

WORD = re.compile(r"[A-Za-z]+")

# A substitution must be seen this many times, and the locale must keep the
# source form no more than (1 - CONSISTENCY) of the time, before it counts
# as a rule rather than a one-off wording choice.
MIN_APPLIED = 3
CONSISTENCY = 0.9

# Contexts where an English word is a code token rather than prose: CSS
# properties and values, MathML and HTML attribute names, identifiers. These
# are the only false positives the check produced on en-GB and en-CA, and
# they all look the same -- the word is part of a hyphenated token.
_CODEY = re.compile(
    r"(?:[A-Za-z]+-{word}|{word}-[A-Za-z]+)",
)

# A word quoted on its own is being named, not used: MathML's list of
# attributes -- "background", "color", "fontfamily" -- must stay verbatim.
_QUOTED = re.compile(
    r"[\u201c\u2018\"\'`]{word}[\u201d\u2019\"\'`]",
)


def learn(l10n: dict, source: dict) -> dict[str, tuple[str, int, int]]:
    """Derive the variant's word substitutions from its own divergences.

    Returns ``{source_word: (variant_word, times_applied, times_retained)}``
    for substitutions consistent enough to treat as rules.
    """
    applied: Counter = Counter()
    retained: Counter = Counter()

    for key, msg in l10n.items():
        src = source.get(key)
        if src is None:
            continue
        src_text, loc_text = src.text(), msg.text()
        src_words = WORD.findall(src_text)
        loc_words = WORD.findall(loc_text)

        if src_text.strip() != loc_text.strip():
            matcher = difflib.SequenceMatcher(None, src_words, loc_words, autojunk=False)
            for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                # Only equal-length replacements: a clean word-for-word swap.
                # Insertions and deletions are rewording, not spelling.
                if tag != "replace" or (i2 - i1) != (j2 - j1):
                    continue
                for before, after in zip(src_words[i1:i2], loc_words[j1:j2]):
                    before, after = before.lower(), after.lower()
                    if before != after and len(before) > 2 and len(after) > 2:
                        applied[(before, after)] += 1

        lowered = {w.lower() for w in loc_words}
        for word in {w.lower() for w in src_words}:
            if word in lowered:
                retained[word] += 1

    rules: dict[str, tuple[str, int, int]] = {}
    for (before, after), count in applied.items():
        if count < MIN_APPLIED:
            continue
        kept = retained.get(before, 0)
        if count / (count + kept) < CONSISTENCY:
            continue
        # Two different targets for one source word: not a rule.
        existing = rules.get(before)
        if existing is not None and existing[1] >= count:
            continue
        rules[before] = (after, count, kept)
    return rules


def in_code_token(word: str, text: str) -> bool:
    """Is every occurrence of the word a code token rather than prose?

    Two shapes cover every false positive this produced on en-GB and en-CA:
    the word inside a hyphenated identifier (`background-color`,
    `color-scheme`), and the word quoted as a literal being named rather
    than used (MathML's list of attributes). A word that also appears
    plainly somewhere in the same string is still worth reporting.
    """
    escaped = re.escape(word)
    codey = len(re.findall(_CODEY.pattern.format(word=escaped), text, re.IGNORECASE))
    codey += len(re.findall(_QUOTED.pattern.format(word=escaped), text, re.IGNORECASE))
    total = len(re.findall(rf"\b{escaped}\b", text, re.IGNORECASE))
    return total > 0 and codey >= total


def unapplied(l10n: dict, source: dict, rules: dict) -> list[tuple[tuple, str, str]]:
    """Strings identical to the source that still contain a source-only form.

    Returns ``(key, source_word, variant_word)``.
    """
    out = []
    for key, msg in l10n.items():
        src = source.get(key)
        if src is None:
            continue
        text = msg.text()
        if src.text().strip() != text.strip():
            continue  # already localized; the model reviews those
        seen: set[str] = set()
        for raw in WORD.findall(text):
            word = raw.lower()
            if word in seen or word not in rules:
                continue
            seen.add(word)
            if in_code_token(word, text):
                continue
            out.append((key, word, rules[word][0]))
    return out

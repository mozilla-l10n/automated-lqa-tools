#!/usr/bin/env python3
"""Build the static site published to GitHub Pages.

Turns `reports/` into `_site/`: one pre-rendered HTML fragment per report,
a manifest saying which locale-and-project pairs exist, and the three static
files that make up the page itself.

Two decisions are worth knowing about.

**Markdown is rendered here, not in the browser.** The page then needs no
parser, no CDN and no third-party JavaScript, and a report opens as fast as
the network can hand over one fragment.

**The source is HTML-escaped before it is rendered.** Reports quote the
strings they are complaining about, and those strings routinely contain
markup: `Current: <span data-l10n-name="state">Stan:</span>` and 58 more
like it across the tree, some inside code spans and some not. Rendering with
HTML passthrough would let a translation inject markup into the page; a
sanitiser that stripped unknown tags would delete the very text the finding
is about. Escaping first shows it as text, which is what a reviewer needs to
read. Escaping leaves markdown's own syntax characters alone, so tables and
headings still work. One round of it is undone again inside code spans, where
the renderer escapes the same characters a second time -- see `_DOUBLED`.

    python site/build.py [--out _site]
"""

from __future__ import annotations

import argparse
import datetime
import glob
import html
import json
import os
import re
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, os.path.join(_ROOT, "lib"))

import config  # noqa: E402

STATIC = ("index.html", "app.js", "style.css")

# `[ru](ru/firefox.md)` in a summary, `[android](android.md)` in a locale
# report. Both have to become in-page routes or they would leave the site.
_LINK = re.compile(r'href="(?:\.\./)?(?:([A-Za-z0-9_-]+)/)?([A-Za-z0-9_]+)\.md"')

# The source is escaped once here and a second time by the renderer, which
# escapes the `&` of an entity inside a code span. Two rounds show the
# reviewer `&lt;/span &gt;` where the string says `</span >`, so one round is
# undone -- inside code spans only, where the doubling happens, and never on
# the tags themselves. The result is still entities, so nothing becomes
# markup: `&amp;lt;` -> `&lt;` -> the browser draws `<`.
_CODE = re.compile(r"(?s)<code>(.*?)</code>")
_DOUBLED = re.compile(r"&amp;(lt|gt|quot|amp|#x27|#39);")

# Escaping the source blocks literal HTML but not *markdown*: a report quotes
# real translations, and a translation containing a backtick can close the
# code span the renderer put it in, after which `[x](javascript:...)` is read
# as a link and `![x](http://...)` as an automatic request. The report side
# fences the values it quotes, but a finding's summary and rationale embed
# translated fragments as prose, so the target of every link and image the
# renderer produced is checked here too. Only in-page and plain http(s)
# targets survive; anything else keeps its text and loses its destination.
_ATTR = re.compile(r"""(?i)\s(href|src)\s*=\s*("|')(.*?)\2""")
_SAFE_SCHEME = re.compile(r"(?i)^(?:https?:|mailto:)")


def _safe_url(value: str, attr: str = "href") -> bool:
    """Is this a target the page may keep?

    An allowlist, because the dangerous set is open-ended: `javascript:`,
    `data:`, `vbscript:`, and any of them obfuscated with entities, embedded
    newlines or control characters. Relative and in-page links are what the
    reports actually use, so nothing legitimate is lost by refusing the rest.

    ``src`` is held to a stricter rule than ``href``: a link is inert until
    somebody clicks it, but an image is fetched the moment the page renders,
    which hands the reader's address to whoever chose the URL. Reports have
    no legitimate remote images, so only local ones are kept.
    """
    raw = html.unescape(value or "")
    raw = "".join(c for c in raw if c.isprintable()).strip()
    if not raw:
        return False
    if raw.startswith(("#", "/", "./", "../")):
        return True
    if ":" not in raw.split("/")[0]:
        return True  # no scheme at all: a relative path
    if attr == "src":
        return False
    return bool(_SAFE_SCHEME.match(raw))


def sanitize_urls(body: str) -> str:
    """Drop every href/src the allowlist does not accept, keeping the text."""
    def one(match):
        attr, quote, value = match.group(1), match.group(2), match.group(3)
        if _safe_url(value, attr.lower()):
            return match.group(0)
        return f" data-blocked-{attr.lower()}={quote}{html.escape(value)}{quote}"

    return _ATTR.sub(one, body)


def discover_projects() -> list:
    """Every sibling directory that is a project.

    `lib/config.py` has no registry -- it loads one project by name -- so
    the set is whatever has a config.yaml next to the pipeline.
    """
    found = []
    for path in sorted(glob.glob(os.path.join(_ROOT, "*", "config.yaml"))):
        found.append(config.load(os.path.basename(os.path.dirname(path))))
    return found


def render(path: str, locale: str | None) -> str:
    """One report as an HTML fragment, safe to inject."""
    import markdown

    with open(path, encoding="utf-8") as fh:
        source = fh.read()

    body = markdown.markdown(
        html.escape(source),
        extensions=["tables", "sane_lists"],
        output_format="html5",
    )

    body = _CODE.sub(
        lambda m: f"<code>{_DOUBLED.sub(r'&\1;', m.group(1))}</code>", body
    )
    body = sanitize_urls(body)

    def route(match: re.Match) -> str:
        where, project = match.group(1), match.group(2)
        # A bare `android.md` inside reports/it/ means this same locale.
        return f'href="#/{where or locale or "all"}/{project}"'

    return _LINK.sub(route, body)


# Written into every directory this script generates. Its presence is what
# makes a later `rmtree` safe: the target is something this script made, not
# something it was pointed at by mistake.
MARKER = ".site-build"


def _clear(out: str) -> None:
    """Empty the output directory, refusing anything we did not create.

    `--out` went straight to `shutil.rmtree`. A typo -- `--out .`, `--out
    site`, the repository root -- would recursively delete real work before
    writing the replacement, and the reports and state directories are not
    reconstructible from the site.
    """
    target = os.path.realpath(out)
    if target == os.path.realpath(_ROOT) or os.path.dirname(target) == target:
        raise SystemExit(f"refusing to build into {target}: that is the repository root")
    if os.path.commonpath([target, os.path.realpath(_HERE)]) == os.path.realpath(_HERE):
        raise SystemExit(f"refusing to build into {target}: that is the site source")
    if not os.path.isdir(target):
        return
    # The marker, or the artifacts a previous version of this script left --
    # so an `_site` built before the marker existed is still recognised as
    # ours rather than refused.
    ours = os.path.exists(os.path.join(target, MARKER)) or all(
        os.path.exists(os.path.join(target, name))
        for name in (".nojekyll", "index.json", "index.html")
    )
    if not ours:
        if os.listdir(target):
            raise SystemExit(
                f"refusing to delete {target}: it is not empty and was not "
                f"built by this script (no {MARKER}). Remove it yourself, or "
                "point --out somewhere else."
            )
        return
    shutil.rmtree(target)


def build(out: str) -> dict:
    projects = discover_projects()
    if not projects:
        raise SystemExit("no projects found: expected <name>/config.yaml")

    _clear(out)
    os.makedirs(os.path.join(out, "r"), exist_ok=True)

    manifest = {
        "generated": datetime.date.today().isoformat(),
        "projects": {p.name: p.display_name for p in projects},
        "summaries": [],
        "locales": {},
    }

    written = 0
    for project in projects:
        if os.path.exists(project.summary_path):
            target = os.path.join(out, "r", f"{project.name}.html")
            with open(target, "w", encoding="utf-8") as fh:
                fh.write(render(project.summary_path, None))
            manifest["summaries"].append(project.name)
            written += 1

        for locale in project.locales:
            source = project.report_path(locale)
            # Listed in config but never run: leave it out rather than
            # offering a choice that 404s.
            if not os.path.exists(source):
                continue
            os.makedirs(os.path.join(out, "r", locale), exist_ok=True)
            target = os.path.join(out, "r", locale, f"{project.name}.html")
            with open(target, "w", encoding="utf-8") as fh:
                fh.write(render(source, locale))
            manifest["locales"].setdefault(locale, []).append(project.name)
            written += 1

    manifest["summaries"].sort()
    manifest["locales"] = {k: sorted(v) for k, v in sorted(manifest["locales"].items())}

    with open(os.path.join(out, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")

    for name in STATIC:
        shutil.copy(os.path.join(_HERE, name), os.path.join(out, name))

    # Pages would otherwise hand the tree to Jekyll, which ignores anything
    # starting with an underscore and would rather we did not.
    open(os.path.join(out, ".nojekyll"), "w").close()
    open(os.path.join(out, MARKER), "w").close()

    manifest["_written"] = written
    return manifest


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=os.path.join(_ROOT, "_site"))
    args = ap.parse_args(argv)

    manifest = build(args.out)
    locales = manifest["locales"]
    print(f"{manifest['_written']} reports -> {os.path.relpath(args.out, _ROOT)}")
    print(f"  projects : {', '.join(manifest['projects'])}")
    print(f"  summaries: {', '.join(manifest['summaries'])}")
    print(f"  locales  : {len(locales)}")
    ragged = {loc: p for loc, p in locales.items() if len(p) != len(manifest["projects"])}
    if ragged:
        print("  not every project covers every locale, which the page reflects:")
        for loc, ps in list(ragged.items())[:4]:
            print(f"      {loc}: {', '.join(ps)}")
        if len(ragged) > 4:
            print(f"      …and {len(ragged) - 4} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""How a project's localized files relate to its source files.

Two shapes so far, and they are genuinely different.

**mirrored** -- Firefox. Two repositories with identical relative paths:
``firefox-l10n/<locale>/browser/browser/appmenu.ftl`` against
``firefox-l10n-source/browser/browser/appmenu.ftl``. Walking both trees and
matching on the relative path is enough.

**xliff** -- firefoxios-l10n. One file per locale, and each trans-unit
carries the English and the translation together, so there is no second
tree to walk: one parse fills both sides. The `<file original="...">` group
is part of the key, because a trans-unit id is only unique within its group.

**android** -- android-l10n. One repository in which the source and every
locale sit side by side, ``res/values/strings.xml`` next to
``res/values-it/strings.xml``, with the mapping declared in compare-locales
TOML files. The locale segment also uses Android's own codes, where
``pt-BR`` becomes ``pt-rBR``. ``moz.l10n.paths`` already reads those configs
and does that conversion, so this module delegates rather than reimplements.

A project may also read part of a neighbouring project as **context**:
strings that are measured or looked up but never checked, reviewed or
reported, because another project owns them. Focus and Firefox for Android
are translated by the same team in the same repository, so conventions are
counted over both -- Focus alone has too few strings for a majority to mean
anything -- and Focus quotes Android Components labels, which Firefox for
Android owns. Only the android layout has a neighbour so far.

Everything downstream is written against :class:`Trees`, so a new project
adds a loader here instead of touching the pipeline. A message is keyed by
``(file, id)`` where ``file`` is the **reference** path relative to the
repository root -- the one identifier that is the same for every locale,
which is what lets stored state and findings survive.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

import parse


@dataclass
class Trees:
    # Directory the `file` keys and `locale_paths` are relative to.
    root: str = ""
    l10n: dict = field(default_factory=dict)
    source: dict = field(default_factory=dict)
    l10n_files: set = field(default_factory=set)
    source_files: set = field(default_factory=set)
    # Reference path -> the actual localized file, for reports and for the
    # baseline reviewer, which hands real paths to an agent.
    locale_paths: dict = field(default_factory=dict)
    # Same, for the reference side. Kept apart because they mean different
    # things: a localized file that will not parse is the locale's defect, a
    # reference file that will not parse invalidates every comparison made
    # against it and is this pipeline's problem, not the team's.
    source_errors: dict = field(default_factory=dict)
    # Reference path -> the parser's complaint, for files that did not parse.
    # Collected while loading, because parsing the tree a second time just to
    # ask this doubled every run -- and for the XLIFF layout, where many keys
    # resolve to one large file, it re-read that file once per key.
    syntax_errors: dict = field(default_factory=dict)
    # Strings another project owns, counted towards this locale's
    # conventions -- typography and a variant's spelling -- and nothing else.
    # See the module docstring.
    context_conventions: dict = field(default_factory=dict)
    context_conventions_source: dict = field(default_factory=dict)
    # Strings another project owns that a quoted UI label may name. Both
    # sides, because `ui_references` compares the two.
    context_l10n: dict = field(default_factory=dict)
    context_source: dict = field(default_factory=dict)

    def measured(self) -> dict:
        """What the locale's conventions are counted over."""
        return {**self.context_conventions, **self.l10n}

    def measured_source(self) -> dict:
        """The source side of :meth:`measured`."""
        return {**self.context_conventions_source, **self.source}


def load(project, locale: str, l10n_root: str, source_root: str) -> Trees:
    kind = project.data.get("layout", "mirrored")
    if kind == "mirrored":
        return _mirrored(project, locale, l10n_root, source_root)
    if kind == "android":
        return _android(project, locale, l10n_root)
    if kind == "xliff":
        return _xliff(project, locale, l10n_root)
    raise RuntimeError(f"unknown layout {kind!r} in {project.name}/config.yaml")


def _mirrored(project, locale, l10n_root, source_root) -> Trees:
    tree = os.path.join(l10n_root, project.locale_subpath(locale))
    errors: dict = {}
    source_errors: dict = {}
    return Trees(
        root=tree,
        l10n=parse.parse_tree(tree, project.extensions, project.exclude, errors),
        source=parse.parse_tree(
            source_root, project.extensions, project.exclude, source_errors
        ),
        l10n_files=parse.list_files(tree, project.extensions, project.exclude),
        source_files=parse.list_files(source_root, project.extensions, project.exclude),
        locale_paths={},
        syntax_errors=errors,
        source_errors=source_errors,
    )


def _config_paths(project, root: str, names):
    from moz.l10n.paths import L10nConfigPaths

    for name in names:
        path = os.path.join(root, name)
        if not os.path.exists(path):
            raise RuntimeError(f"missing path config: {path}")
        yield L10nConfigPaths(path)


def _android_configs(project, locale, root, names, trees: Trees, paths=None):
    """Load the files the named configs map, optionally only under `paths`."""
    for config in _config_paths(project, root, names):
        for (ref, target), locales in config.all().items():
            if locales and locale not in locales:
                continue
            rel = os.path.relpath(ref, root)
            if project.exclude and parse.is_excluded(rel, project.exclude):
                continue
            if paths is not None and not any(rel.startswith(p) for p in paths):
                continue
            if os.path.exists(ref):
                trees.source_files.add(rel)
                for msg in parse.parse_file(ref, rel, trees.source_errors):
                    trees.source[msg.key] = msg
            localized = config.format_target_path(target, locale)
            if os.path.exists(localized):
                trees.l10n_files.add(rel)
                trees.locale_paths[rel] = os.path.relpath(localized, root)
                for msg in parse.parse_file(localized, rel, trees.syntax_errors):
                    trees.l10n[msg.key] = msg


def _android(project, locale, root) -> Trees:
    trees = Trees(root=root)
    _android_configs(project, locale, root, project.data.get("configs", []), trees)

    context = project.data.get("context") or {}
    names = context.get("conventions") or []
    if names:
        other = Trees(root=root)
        _android_configs(project, locale, root, names, other)
        trees.context_conventions = {
            k: v for k, v in other.l10n.items() if k not in trees.l10n
        }
        trees.context_conventions_source = {
            k: v for k, v in other.source.items() if k not in trees.source
        }
    refs = context.get("references") or {}
    if refs.get("configs"):
        other = Trees(root=root)
        _android_configs(
            project, locale, root, refs["configs"], other, refs.get("paths") or None
        )
        own = set(trees.source) | set(trees.l10n)
        trees.context_source = {k: v for k, v in other.source.items() if k not in own}
        trees.context_l10n = {k: v for k, v in other.l10n.items() if k not in own}
    return trees


def _xliff_messages(path: str):
    """Yield ``(group, id, target_msg, source_text)`` from one XLIFF file.

    moz.l10n gives the ``<target>`` as the entry value and puts the
    ``<source>`` in the entry's metadata. An untranslated unit comes back
    with an empty pattern rather than being absent, so the caller has to
    look at the pattern to tell the two apart.
    """
    from moz.l10n.resource import parse_resource

    resource = parse_resource(path)
    for section in resource.sections:
        group = "/".join(section.id) if section.id else os.path.basename(path)
        for entry in section.entries:
            if not hasattr(entry, "id"):
                continue
            meta = {m.key: m.value for m in (entry.meta or [])}
            yield group, ".".join(entry.id), entry, meta.get("source")


def _xliff(project, locale, root) -> Trees:
    """One file per locale, source and target side by side inside it.

    The reference is the dedicated reference locale (``en-US``) rather than
    the ``<source>`` sitting next to each target. Upstream only rewrites a
    locale's ``<source>`` in one of its three matching modes, so it can lag
    behind the English; taking the reference from its own file is what lets
    the snapshot notice that the source moved under a translation nobody
    updated. Where a unit is missing from the reference -- an id the
    reference has since dropped -- the in-file ``<source>`` is used instead.
    """
    from parse import Msg

    trees = Trees(root=root)
    template = project.data.get("locale_file", "{locale}/firefox-ios.xliff")
    reference = project.data.get("reference_locale", "en-US")

    # Keep the reference's *parsed* message, not just its text: the
    # placeholder check reads the literal spec off each expression, so
    # handing it the target's own message would compare a string with
    # itself and report nothing, however wrong the translation was.
    ref_path = os.path.join(root, template.format(locale=reference))
    ref_msgs: dict[tuple[str, str], object] = {}
    if os.path.exists(ref_path):
        for group, mid, entry, _src in _xliff_messages(ref_path):
            if getattr(entry.value, "pattern", None):
                ref_msgs[(group, mid)] = entry.value

    path = os.path.join(root, template.format(locale=locale))
    if not os.path.exists(path):
        return trees

    rel = os.path.relpath(path, root)
    try:
        units = list(_xliff_messages(path))
    except Exception as exc:  # noqa: BLE001 - the message is what gets reported
        # One unparseable file is the whole locale here, so it has to be
        # reported rather than raised: the health check says so and the run
        # carries on to the next locale.
        trees.syntax_errors[rel] = str(exc)
        return trees

    for group, mid, entry, in_file_source in units:
        key = (group, mid)
        trees.source_files.add(group)
        ref_value = ref_msgs.get(key)
        source_text = (
            parse.flatten(ref_value) if ref_value is not None else (in_file_source or "")
        )
        if source_text:
            source_msg = Msg(
                file=group, id=mid, comment=(entry.comment or "").strip(),
                props={"": source_text},
            )
            # Only expose a parsed message where it really is the source's.
            # Without one the placeholder check skips the unit, which is the
            # right outcome for an id the reference no longer carries.
            if ref_value is not None:
                source_msg.raw = {"": ref_value}
            trees.source[key] = source_msg
        # An empty pattern is an untranslated unit: leave it out so
        # completeness counts it as missing rather than as an empty string.
        if not getattr(entry.value, "pattern", None):
            continue
        trees.l10n_files.add(group)
        trees.locale_paths[group] = os.path.relpath(path, root)
        trees.l10n[key] = Msg(
            file=group, id=mid, comment=(entry.comment or "").strip(),
            props={"": parse.flatten(entry.value)}, raw={"": entry.value},
            line=getattr(getattr(entry, "linepos", None), "start", 0) or 0,
        )
    return trees

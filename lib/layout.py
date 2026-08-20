"""How a project's localized files relate to its source files.

Two shapes so far, and they are genuinely different.

**mirrored** -- Firefox. Two repositories with identical relative paths:
``firefox-l10n/<locale>/browser/browser/appmenu.ftl`` against
``firefox-l10n-source/browser/browser/appmenu.ftl``. Walking both trees and
matching on the relative path is enough.

**android** -- android-l10n. One repository in which the source and every
locale sit side by side, ``res/values/strings.xml`` next to
``res/values-it/strings.xml``, with the mapping declared in compare-locales
TOML files. The locale segment also uses Android's own codes, where
``pt-BR`` becomes ``pt-rBR``. ``moz.l10n.paths`` already reads those configs
and does that conversion, so this module delegates rather than reimplements.

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


def load(project, locale: str, l10n_root: str, source_root: str) -> Trees:
    kind = project.data.get("layout", "mirrored")
    if kind == "mirrored":
        return _mirrored(project, locale, l10n_root, source_root)
    if kind == "android":
        return _android(project, locale, l10n_root)
    raise RuntimeError(f"unknown layout {kind!r} in {project.name}/config.yaml")


def _mirrored(project, locale, l10n_root, source_root) -> Trees:
    tree = os.path.join(l10n_root, project.locale_subpath(locale))
    return Trees(
        root=tree,
        l10n=parse.parse_tree(tree, project.extensions, project.exclude),
        source=parse.parse_tree(source_root, project.extensions, project.exclude),
        l10n_files=parse.list_files(tree, project.extensions, project.exclude),
        source_files=parse.list_files(source_root, project.extensions, project.exclude),
        locale_paths={},
    )


def _config_paths(project, root: str):
    from moz.l10n.paths import L10nConfigPaths

    for name in project.data.get("configs", []):
        path = os.path.join(root, name)
        if not os.path.exists(path):
            raise RuntimeError(f"missing path config: {path}")
        yield L10nConfigPaths(path)


def _android(project, locale, root) -> Trees:
    trees = Trees(root=root)
    for paths in _config_paths(project, root):
        for (ref, target), locales in paths.all().items():
            if locales and locale not in locales:
                continue
            rel = os.path.relpath(ref, root)
            if project.exclude and parse.is_excluded(rel, project.exclude):
                continue
            if os.path.exists(ref):
                trees.source_files.add(rel)
                for msg in parse.parse_file(ref, rel):
                    trees.source[msg.key] = msg
            localized = paths.format_target_path(target, locale)
            if os.path.exists(localized):
                trees.l10n_files.add(rel)
                trees.locale_paths[rel] = os.path.relpath(localized, root)
                for msg in parse.parse_file(localized, rel):
                    trees.l10n[msg.key] = msg
    return trees


def locale_file(trees: Trees, rel: str) -> str:
    """The localized file for a reference path, for display."""
    return trees.locale_paths.get(rel, rel)

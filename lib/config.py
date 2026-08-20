"""Configuration and path helpers.

One project = one directory next to this repo's root (``firefox/``), holding
its own config, prompts, locale instructions, state and reports. Adding a
second project means adding a sibling directory, not touching this module.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from fnmatch import fnmatch

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@dataclass
class Project:
    """One automation: its config, prompts, locale instructions and state.

    Everything format-agnostic lives in ``lib/``; a project directory holds
    only what differs -- its configuration, its prompts, and the checks that
    are specific to its file format.
    """

    name: str
    root: str
    data: dict

    # --- config accessors -------------------------------------------------
    @property
    def locales(self) -> list[str]:
        return list(self.data.get("locales", []))

    @property
    def extensions(self) -> list[str]:
        return list(self.data.get("extensions", [".ftl"]))

    @property
    def exclude(self) -> list[str]:
        return list(self.data.get("exclude", []))

    @property
    def llm(self) -> dict:
        return dict(self.data.get("llm", {}))

    def locale_subpath(self, locale: str) -> str:
        return self.data["repos"]["l10n"]["locale_path"].format(locale=locale)

    def variant_of(self, locale: str) -> str | None:
        """The source locale this one is a variant of, if any."""
        return (self.data.get("variants") or {}).get(locale)

    def is_variant(self, locale: str) -> bool:
        return self.variant_of(locale) is not None

    def check_skipped(self, check: str, locale: str) -> bool:
        ov = self.data.get("check_overrides", {}).get(check, {})
        return locale in ov.get("skip_locales", [])

    def check_skips_path(self, check: str, rel: str) -> bool:
        ov = self.data.get("check_overrides", {}).get(check, {})
        return any(fnmatch(rel, pat) for pat in ov.get("skip_paths", []))

    @property
    def systemic_threshold(self) -> int:
        return int(self.data.get("systemic_threshold", 25))

    # --- paths ------------------------------------------------------------
    def state_dir(self, locale: str) -> str:
        return os.path.join(self.root, "state", locale)

    def locale_dir(self, locale: str) -> str:
        return os.path.join(self.root, "locales", locale)

    def report_path(self, locale: str) -> str:
        return os.path.join(self.root, "reports", f"{locale}.md")

    @property
    def tools_dir(self) -> str:
        return os.path.join(self.root, "tools")

    @property
    def checks(self) -> list[str]:
        """Checks this project runs, in report order."""
        return list(self.data.get("checks", []))

    def prompt(self, name: str) -> str:
        with open(os.path.join(self.root, "prompts", name), encoding="utf-8") as fh:
            return fh.read()

    def conventions(self, locale: str) -> str:
        path = os.path.join(self.locale_dir(locale), "conventions.md")
        if not os.path.exists(path):
            return ""
        with open(path, encoding="utf-8") as fh:
            return fh.read()


def load(project: str = "firefox", root: str | None = None) -> Project:
    root = root or os.path.join(REPO_ROOT, project)
    with open(os.path.join(root, "config.yaml"), encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return Project(name=project, root=root, data=data)

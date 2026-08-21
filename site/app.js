/* The whole front-end. No framework, no dependencies.
 *
 * Reports are pre-rendered to HTML fragments at build time, so this only
 * has to decide which one to show and fetch it. The one piece of real
 * logic is the project dropdown: coverage is ragged -- iOS currently only
 * has Italian -- so the options depend on the locale chosen, and switching
 * to a locale that lacks the current project has to fall back rather than
 * ask for a report that does not exist.
 */
"use strict";

const ALL = "all";
const els = {
  locale: document.getElementById("locale"),
  project: document.getElementById("project"),
  report: document.getElementById("report"),
  status: document.getElementById("status"),
  generated: document.getElementById("generated"),
};

let manifest = null;
const cache = new Map();

/** Projects available for a locale; for "all", those with a summary. */
function projectsFor(locale) {
  if (!manifest) return [];
  return locale === ALL ? manifest.summaries : manifest.locales[locale] || [];
}

function option(value, label) {
  const o = document.createElement("option");
  o.value = value;
  o.textContent = label;
  return o;
}

function fillLocales() {
  els.locale.replaceChildren(
    option(ALL, "All locales"),
    ...Object.keys(manifest.locales).map((l) => option(l, l))
  );
}

/** Rebuild the project list, keeping the current choice where it still exists. */
function fillProjects(locale, preferred) {
  const available = projectsFor(locale);
  els.project.replaceChildren(
    ...available.map((p) => option(p, manifest.projects[p] || p))
  );
  const keep = available.includes(preferred) ? preferred : available[0];
  if (keep) els.project.value = keep;
  els.project.disabled = available.length <= 1;
  return keep;
}

function href(locale, project) {
  return locale === ALL ? `r/${project}.html` : `r/${locale}/${project}.html`;
}

async function show(locale, project) {
  const url = href(locale, project);
  if (cache.has(url)) {
    els.report.innerHTML = cache.get(url);
    return;
  }
  els.status.textContent = "Loading…";
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`${res.status}`);
    const body = await res.text();
    cache.set(url, body);
    els.report.innerHTML = body;
  } catch (err) {
    els.report.innerHTML =
      `<p class="placeholder">No report for <code>${locale}</code> / ` +
      `<code>${project}</code>. It may not have been run yet.</p>`;
  } finally {
    els.status.textContent = "";
  }
}

/** #/<locale>/<project> -- so a report can be linked to and the back button works. */
function readHash() {
  const m = location.hash.match(/^#\/([^/]+)\/([^/]+)$/);
  return m ? { locale: decodeURIComponent(m[1]), project: decodeURIComponent(m[2]) } : null;
}

function apply(route, { push = true } = {}) {
  let locale = route && (route.locale === ALL || manifest.locales[route.locale])
    ? route.locale
    : ALL;
  els.locale.value = locale;
  const project = fillProjects(locale, route && route.project);
  if (!project) {
    els.report.innerHTML = `<p class="placeholder">Nothing to show for ${locale}.</p>`;
    return;
  }
  const target = `#/${locale}/${project}`;
  if (push && location.hash !== target) {
    history.pushState(null, "", target);
  } else if (!push && location.hash !== target) {
    history.replaceState(null, "", target);
  }
  document.title = `${locale === ALL ? "All locales" : locale} · ` +
    `${manifest.projects[project] || project} · Localization QA`;
  show(locale, project);
}

function onSelect() {
  apply({ locale: els.locale.value, project: els.project.value });
}

async function start() {
  try {
    manifest = await (await fetch("index.json")).json();
  } catch (err) {
    els.report.innerHTML =
      '<p class="placeholder">Could not load <code>index.json</code>. ' +
      "If you are previewing locally, run <code>python site/build.py</code> first.</p>";
    return;
  }
  els.generated.textContent = `Last built ${manifest.generated}.`;
  fillLocales();
  els.locale.addEventListener("change", onSelect);
  els.project.addEventListener("change", onSelect);
  // A link inside a report (a summary row, or "Also for it:") just changes
  // the hash; treat that as navigation and keep the dropdowns in step.
  window.addEventListener("hashchange", () => apply(readHash(), { push: false }));
  apply(readHash(), { push: false });
}

start();

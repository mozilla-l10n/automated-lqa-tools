/* The whole front-end. No framework, no dependencies.
 *
 * Reports are pre-rendered to HTML fragments at build time, so this only
 * has to decide which one to show and fetch it. The one piece of real
 * logic is the project dropdown: coverage is ragged -- iOS currently only
 * has Italian -- so the options depend on the locale chosen, and switching
 * to a locale that lacks the current project has to fall back rather than
 * ask for a report that does not exist.
 *
 * The landing page, `#/bot`, is the Pontoon suggestion bot's statistics:
 * one more pre-rendered fragment, outside the locale/project grid.
 */
"use strict";

const ALL = "all";
const BOT = "#/bot";
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

// Which selection the user is actually on. Every fetch was independent and
// unconditional, so changing locale twice quickly could let the first, slower
// response land last and paint a report the dropdowns, the URL and the title
// all disagree with. A response is only allowed to paint if its request is
// still the current one.
let latestRequest = 0;

async function show(locale, project) {
  return load(href(locale, project),
    `No report for <code>${locale}</code> / <code>${project}</code>. ` +
    "It may not have been run yet.");
}

async function load(url, missing) {
  const token = ++latestRequest;
  if (cache.has(url)) {
    els.report.innerHTML = cache.get(url);
    return true;
  }
  els.status.textContent = "Loading…";
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`${res.status}`);
    const body = await res.text();
    cache.set(url, body);
    if (token !== latestRequest) return false;
    els.report.innerHTML = body;
    return true;
  } catch (err) {
    if (token !== latestRequest) return;
    els.report.innerHTML = `<p class="placeholder">${missing}</p>`;
    return false;
  } finally {
    if (token === latestRequest) els.status.textContent = "";
  }
}

/** Parse the stable #/<locale>/<project> route used by links and browser history. */
function readHash() {
  const m = location.hash.match(/^#\/([^/]+)\/([^/]+)$/);
  if (!m) return null;
  try {
    return { locale: decodeURIComponent(m[1]), project: decodeURIComponent(m[2]) };
  } catch {
    return null;
  }
}

// Chart.js is only needed by the landing page, so it is fetched the first
// time that page is shown rather than with every report.
let chartScripts = null;

function script(src) {
  return new Promise((resolve, reject) => {
    const el = document.createElement("script");
    el.src = src;
    el.onload = resolve;
    el.onerror = reject;
    document.head.appendChild(el);
  });
}

function drawCharts() {
  chartScripts ||= script("vendor/chart.umd.min.js").then(() => script("charts.js"));
  chartScripts
    .then(() => window.drawBotCharts())
    .catch(() => {
      chartScripts = null; // let the next visit try again
    });
}

/** The landing page. The dropdowns offer a way into the reports from here,
 * so the project list gets a placeholder: otherwise its first entry would
 * already be selected and choosing it would fire no change. */
function showBot({ push = true } = {}) {
  els.locale.value = ALL;
  fillProjects(ALL);
  els.project.prepend(option("", "Choose a report…"));
  els.project.value = "";
  els.project.disabled = false;
  if (location.hash !== BOT) {
    (push ? history.pushState : history.replaceState).call(history, null, "", BOT);
  }
  document.title = "Pontoon suggestion bot · Localization QA";
  load("r/bot.html", "The suggestion statistics have not been built.")
    .then((painted) => { if (painted) drawCharts(); });
}

function apply(route, { push = true } = {}) {
  if (!route) return showBot({ push });
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

// In-page links -- the table of contents and "↑ Contents" -- name an id, not
// a route. Left to the browser they would change the hash, and the router
// would read `#sec-…` as a bad route and fall back to the default page.
function onReportClick(event) {
  const link = event.target.closest && event.target.closest("a[href^='#']");
  if (!link) return;
  const id = link.getAttribute("href").slice(1);
  if (id.startsWith("/")) return; // a route: hashchange handles it
  const target = document.getElementById(id);
  if (!target || !els.report.contains(target)) return;
  event.preventDefault();
  target.scrollIntoView({ block: "start" });
  // Move focus too, so the next Tab continues from the section the reader
  // jumped to rather than from the link they clicked.
  if (!target.hasAttribute("tabindex")) target.setAttribute("tabindex", "-1");
  target.focus({ preventScroll: true });
}

function onSelect() {
  apply({ locale: els.locale.value, project: els.project.value });
}

async function start() {
  try {
    const response = await fetch("index.json");
    if (!response.ok) throw new Error(`${response.status}`);
    manifest = await response.json();
    if (!manifest || !manifest.projects || !manifest.locales || !manifest.summaries) {
      throw new Error("invalid manifest");
    }
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
  els.report.addEventListener("click", onReportClick);
  // A link inside a report (a summary row, or "Also for it:") just changes
  // the hash; treat that as navigation and keep the dropdowns in step.
  window.addEventListener("hashchange", () => apply(readHash(), { push: false }));
  apply(readHash(), { push: false });
}

start();

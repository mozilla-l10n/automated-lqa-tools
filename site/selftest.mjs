// Exercise app.js against a minimal DOM.
//
// The build script is Python and is checked by running it; this covers the
// part of the site that is not: the dropdown logic. Coverage is ragged --
// not every project reviews every locale -- so the project list depends on
// the locale, and moving to a locale that lacks the current project must
// fall back instead of requesting a report that does not exist. That is easy
// to get wrong and invisible until someone clicks it.
//
// Reads _site/ off disk rather than over HTTP, so it needs no server:
//
//     python site/build.py && node site/selftest.mjs
import fs from 'node:fs';
const src = fs.readFileSync(new URL('app.js', import.meta.url), 'utf8');

const BASE = new URL('../_site/', import.meta.url).pathname;
// Without this the missing build surfaces as a TypeError thrown from inside
// app.js on a manifest that was never fetched, which reads as a bug in the
// page rather than a step that did not run.
if (!fs.existsSync(BASE + 'index.json')) {
  console.error(`No build at ${BASE} -- run: python site/build.py`);
  process.exit(1);
}
const mk = (tag) => ({tag, children:[], value:'', textContent:'', disabled:false,
  replaceChildren(...c){this.children=c;}, appendChild(c){this.children.push(c);},
  addEventListener(n,f){(this.on ||= {})[n]=f;}, get options(){return this.children;}});
const els = {locale:mk('select'), project:mk('select'), report:mk('main'),
             status:mk('span'), generated:mk('span')};
globalThis.document = {
  getElementById:(id)=>({locale:els.locale,project:els.project,report:els.report,
                         status:els.status,generated:els.generated}[id]),
  createElement:(t)=>mk(t), title:'',
};
globalThis.location = {hash:''};
globalThis.history = {pushState:(a,b,h)=>{location.hash=h;}, replaceState:(a,b,h)=>{location.hash=h;}};
const listeners={};
globalThis.window = {addEventListener:(n,f)=>{listeners[n]=f;}};
globalThis.fetch = async (u) => {
  const p = BASE + u;
  if (!fs.existsSync(p)) return { ok: false, status: 404, text: async () => '', json: async () => ({}) };
  const body = fs.readFileSync(p, 'utf8');
  return { ok: true, status: 200, text: async () => body, json: async () => JSON.parse(body) };
};
eval(src);
await new Promise(r=>setTimeout(r,600));

const opts = (s)=>s.children.map(o=>o.value);
let fail=0;
const check=(ok,label)=>{console.log(`  ${ok?'PASS':'FAIL'}  ${label}`); if(!ok)fail++;};

// Which locale is the ragged one moves as coverage fills in -- iOS gained
// eighteen locales in one run and the case that used to be cs became fy-NL.
// So read the shape out of the manifest the page itself is driven by rather
// than pinning locale codes here: what is being tested is the fallback, not
// who happens to need it today.
const manifest = JSON.parse(fs.readFileSync(BASE + 'index.json', 'utf8'));
const PROJECTS = Object.keys(manifest.projects).sort();
const covered = Object.entries(manifest.locales);
const [FULL] = covered.find(([, p]) => p.length === PROJECTS.length) || [];
const [PARTIAL, PARTIAL_HAS] = covered.find(([, p]) => p.length < PROJECTS.length) || [];
const MISSING = PARTIAL && PROJECTS.find((p) => !PARTIAL_HAS.includes(p));

console.log('The page, driven through app.js\n');
console.log('Initial state');
check(opts(els.locale)[0]==='all', 'locale dropdown leads with "all"');
check(opts(els.locale).length===covered.length+1,
      `${covered.length} locales plus All (${opts(els.locale).length})`);
check(location.hash===`#/all/${PROJECTS[0]}`, `defaults to a summary (${location.hash})`);

console.log('\nRagged coverage');
if (!FULL || !PARTIAL) {
  // Not a pass: with coverage this shape the fallback cannot be reached, and
  // counting it as green would read as tested when it is only unexercised.
  console.log(`  SKIP  every locale covers ${PROJECTS.length} projects, `
              + 'so there is no fallback to exercise');
} else {
  els.locale.value=FULL; await els.locale.on.change(); await new Promise(r=>setTimeout(r,200));
  check(opts(els.project).length===PROJECTS.length,
        `${FULL} offers all ${PROJECTS.length} (${opts(els.project).join(',')})`);
  els.project.value=MISSING; await els.project.on.change(); await new Promise(r=>setTimeout(r,200));
  check(location.hash===`#/${FULL}/${MISSING}`, `selected ${MISSING} (${location.hash})`);
  els.locale.value=PARTIAL; await els.locale.on.change(); await new Promise(r=>setTimeout(r,300));
  check(opts(els.project).length===PARTIAL_HAS.length,
        `${PARTIAL} offers ${PARTIAL_HAS.length} (${opts(els.project).join(',')})`);
  check(!location.hash.includes(MISSING), `fell back instead of 404ing (${location.hash})`);
  check(!els.report.innerHTML.includes('No report'), 'and rendered a real report');
}

console.log('\nKeeping the project across locales');
const KEPT = PARTIAL_HAS ? PARTIAL_HAS[0] : PROJECTS[0];
const OTHER = covered.find(([loc, p]) => loc !== PARTIAL && p.includes(KEPT))[0];
els.project.value=KEPT; await els.project.on.change(); await new Promise(r=>setTimeout(r,200));
els.locale.value=OTHER; await els.locale.on.change(); await new Promise(r=>setTimeout(r,300));
check(els.project.value===KEPT, `${KEPT} stays selected moving to ${OTHER}`);

console.log('\nHash navigation from a link inside a report');
// Somewhere other than where the dropdowns already are, so following the
// hash is what moves them.
const [LINKED, LINKED_HAS] = covered.find(([loc]) => loc !== OTHER && loc !== PARTIAL);
const LINKED_PROJECT = LINKED_HAS[0];
location.hash=`#/${LINKED}/${LINKED_PROJECT}`;
await listeners.hashchange(); await new Promise(r=>setTimeout(r,400));
check(els.locale.value===LINKED && els.project.value===LINKED_PROJECT,
      'dropdowns follow the hash');
check(els.report.innerHTML.includes('<h1>'), 'and the report is rendered');

console.log('\nBad input');
location.hash=`#/nope/${PROJECTS[0]}`; await listeners.hashchange(); await new Promise(r=>setTimeout(r,300));
check(els.locale.value==='all', 'an unknown locale falls back to All rather than erroring');
location.hash='#/%E0%A4%A/firefox'; await listeners.hashchange(); await new Promise(r=>setTimeout(r,300));
check(els.locale.value==='all', 'a malformed encoded hash falls back rather than breaking navigation');
console.log(`\n${fail} failed`);
process.exit(fail?1:0);

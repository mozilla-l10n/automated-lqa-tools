// Exercise app.js against a minimal DOM.
//
// The build script is Python and is checked by running it; this covers the
// part of the site that is not: the dropdown logic. Coverage is ragged --
// iOS has only Italian -- so the project list depends on the locale, and
// moving to a locale that lacks the current project must fall back instead
// of requesting a report that does not exist. That is easy to get wrong and
// invisible until someone clicks it.
//
// Reads _site/ off disk rather than over HTTP, so it needs no server:
//
//     python site/build.py && node site/selftest.mjs
import fs from 'node:fs';
const src = fs.readFileSync(new URL('app.js', import.meta.url), 'utf8');

const BASE = new URL('../_site/', import.meta.url).pathname;
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

console.log('The page, driven through app.js\n');
console.log('Initial state');
check(opts(els.locale)[0]==='all', 'locale dropdown leads with "all"');
check(opts(els.locale).length===21, `20 locales plus All (${opts(els.locale).length})`);
check(location.hash==='#/all/android', `defaults to a summary (${location.hash})`);

console.log('\nRagged coverage');
els.locale.value='it'; await els.locale.on.change(); await new Promise(r=>setTimeout(r,200));
check(opts(els.project).length===3, `it offers all three (${opts(els.project).join(',')})`);
els.project.value='firefox_ios'; await els.project.on.change(); await new Promise(r=>setTimeout(r,200));
check(location.hash==='#/it/firefox_ios', `selected iOS (${location.hash})`);
els.locale.value='cs'; await els.locale.on.change(); await new Promise(r=>setTimeout(r,300));
check(opts(els.project).length===2, `cs offers two (${opts(els.project).join(',')})`);
check(!location.hash.includes('firefox_ios'), `fell back instead of 404ing (${location.hash})`);
check(!els.report.innerHTML.includes('No report'), 'and rendered a real report');

console.log('\nKeeping the project across locales');
els.project.value='firefox'; await els.project.on.change(); await new Promise(r=>setTimeout(r,200));
els.locale.value='de'; await els.locale.on.change(); await new Promise(r=>setTimeout(r,300));
check(els.project.value==='firefox', 'firefox stays selected moving cs -> de');

console.log('\nHash navigation from a link inside a report');
location.hash='#/ru/firefox'; await listeners.hashchange(); await new Promise(r=>setTimeout(r,400));
check(els.locale.value==='ru' && els.project.value==='firefox', 'dropdowns follow the hash');
check(els.report.innerHTML.includes('<h1>'), 'and the report is rendered');

console.log('\nBad input');
location.hash='#/nope/firefox'; await listeners.hashchange(); await new Promise(r=>setTimeout(r,300));
check(els.locale.value==='all', 'an unknown locale falls back to All rather than erroring');
console.log(`\n${fail} failed`);
process.exit(fail?1:0);

// Scrambles from JTuu's DR subset generator, https://jtuu.be/subsets.html, taken from the page itself.
//
// usage: node subsets_page.mjs gen CORNER_SUBSET N [EDGES]     N scrambles, one JSON line each
//        node subsets_page.mjs classify < SCRAMBLES            one scramble per line -> what the page's library says
//
// The page is opened in headless Chrome and used as a visitor would: one corner subset checked (a name on the page:
// 0c0 2c3 2c4 4b2 4c3 ...), the edge subsets as the page comes (2e 4e 6e; EDGES like 2e,4e,6e to change), U/D as the
// only axis, no DR trigger, images off, "How many?" set to N, Generate clicked.  Each scramble is then given to
// the page's own cube library (pkg/cubelab.js) for its corner subset (which tells 4a3 from 4b3; the page offers the
// two together as 4c3) and whether it is a DR on U/D.
import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const URL = 'https://jtuu.be/subsets.html';
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function withPage(work) {
    const dir = mkdtempSync(join(process.env.SUBSETS_TMP || tmpdir(), 'subsets-chrome-'));
    const chrome = spawn('google-chrome', ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${dir}`,
        '--no-first-run', '--no-default-browser-check', '--disable-gpu', '--disable-background-networking',
        '--disable-component-update', '--disable-sync', '--disable-default-apps', '--mute-audio', 'about:blank'],
        { stdio: ['ignore', 'ignore', 'pipe'] });
    try {
        const ws = await new Promise((ok, bad) => {
            let err = '';
            const t = setTimeout(() => bad(new Error('Chrome did not start: ' + err.slice(-400))), 30000);
            chrome.stderr.on('data', d => {
                err += d;
                const m = err.match(/DevTools listening on (ws:\/\/\S+)/);
                if (m) { clearTimeout(t); ok(m[1]); }
            });
            chrome.on('exit', c => bad(new Error(`Chrome exited (${c}): ${err.slice(-400)}`)));
        });
        const sock = new WebSocket(ws);
        await new Promise((ok, bad) => { sock.onopen = ok; sock.onerror = () => bad(new Error('no DevTools connection')); });
        let id = 0;
        const waiting = new Map(), events = [];
        sock.onmessage = e => {
            const m = JSON.parse(e.data);
            if (m.id && waiting.has(m.id)) {
                const [ok, bad] = waiting.get(m.id);
                waiting.delete(m.id);
                m.error ? bad(new Error(JSON.stringify(m.error))) : ok(m.result);
            } else if (m.method) {
                events.push(m);
            }
        };
        const send = (method, params = {}, sessionId) => new Promise((ok, bad) => {
            waiting.set(++id, [ok, bad]);
            sock.send(JSON.stringify({ id, method, params, sessionId }));
        });
        const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
        const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
        await send('Page.enable', {}, sessionId);
        await send('Runtime.enable', {}, sessionId);
        await send('Page.navigate', { url: URL }, sessionId);
        for (let i = 0; !events.some(m => m.method === 'Page.loadEventFired'); i++) {
            if (i > 300) throw new Error('the page did not load');
            await sleep(100);
        }
        const evaluate = async (fn, ...args) => {
            const expression = `(${fn})(...${JSON.stringify(args)})`;
            const r = await send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true }, sessionId);
            if (r.exceptionDetails) throw new Error('in the page: ' + JSON.stringify(r.exceptionDetails).slice(0, 600));
            return r.result.value;
        };
        // the page's own script is ready once its library is (it sets up the buttons right after)
        await evaluate(async () => { const m = await import('/pkg/cubelab.js'); await m.default(); });
        await sleep(1000);
        return await work(evaluate);
    } finally {
        chrome.kill();
        await sleep(300);
        rmSync(dir, { recursive: true, force: true, maxRetries: 5 });
    }
}

// in the page: what its library says about a scramble
const CLASSIFY = async scrambles => {
    const m = await import('/pkg/cubelab.js');
    await m.default();
    return scrambles.map(s => {
        const c = m.ArrayCube.from_alg(s);
        return { scramble: s, lib_subset: m.CornerSubset[c.get_htr_subset_slow()].slice(1), dr_ud: c.is_dr(m.Axis.UD) };
    });
};

// in the page: set the form, press Generate, read the list
const GENERATE = async (subset, n, edges) => {
    const set = (name, values) => {
        const boxes = [...document.querySelectorAll(`input[name=${name}]`)];
        if (values.some(v => !boxes.some(b => b.value === v))) throw new Error(`the page has no ${name} ${values}`);
        for (const b of boxes) if (b.checked !== values.includes(b.value)) b.click();
        return boxes.filter(b => b.checked).map(b => b.value);
    };
    const form = { corner: set('c_subset', [subset]), edges: edges ? set('e_subset', edges) : [...document.querySelectorAll('input[name=e_subset]:checked')].map(b => b.value),
        axis: set('axis', ['U/D']), normal_trigger: set('normal_trigger', []), inverse_trigger: set('inverse_trigger', []) };
    const img = document.getElementById('image_toggle');
    if (img.checked) img.click();
    document.getElementById('clear_button').click();
    document.getElementById('n_scrams_field').value = String(n);
    document.getElementById('generate_button').click();
    const items = [...document.querySelectorAll('#scrams li')].map(li => ({ subset: li.title, scramble: li.querySelector('p').innerText.split('\n')[0].trim() }));
    return { form, items };
};

const [mode, ...args] = process.argv.slice(2);
if (mode === 'gen') {
    const [subset, n, edges] = args;
    const out = await withPage(async evaluate => {
        let got;
        for (let i = 0; i < 20; i++) {             // until the page's buttons answer
            got = await evaluate(GENERATE, subset, Number(n), edges ? edges.split(',') : null);
            if (got.items.length) break;
            await sleep(500);
        }
        if (got.items.length !== Number(n)) throw new Error(`asked for ${n} scrambles, the page listed ${got.items.length}`);
        const cls = await evaluate(CLASSIFY, got.items.map(t => t.scramble));
        return { form: got.form, items: got.items.map((t, i) => ({ ...t, edges: got.form.edges, ...cls[i] })) };
    });
    console.error('form:', JSON.stringify(out.form));
    for (const t of out.items) console.log(JSON.stringify(t));
} else if (mode === 'classify') {
    const scrambles = readFileSync(0, 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
    for (const t of await withPage(evaluate => evaluate(CLASSIFY, scrambles))) console.log(JSON.stringify(t));
} else {
    console.error('usage: node subsets_page.mjs gen CORNER_SUBSET N [EDGES] | classify < SCRAMBLES');
    process.exit(2);
}
process.exit(0);

// Runs the simulator (WebAssembly) off the page's thread.
//
// Messages in:  {type: 'init'}  then  {type: 'simulate', id, request: {scramble, settings}}
// Messages out: {type: 'defaults', defaults}, {type: 'progress', value}, {type: 'ready', cached},
//               {type: 'result', id, report, ms}, {type: 'error', id, message}
//
// The finish table (56 MB) takes a few seconds to build; it is kept in the browser (IndexedDB) so that the next
// visit only reloads it.  If the browser keeps nothing, it is simply built again.

import init, { Simulator } from './pkg/attempt_sim_wasm.js';

const DB = 'attempt-sim';
const STORE = 'tables';
let sim = null;

function openDb() {
  return new Promise((resolve, reject) => {
    const r = indexedDB.open(DB, 1);
    r.onupgradeneeded = () => r.result.createObjectStore(STORE);
    r.onsuccess = () => resolve(r.result);
    r.onerror = () => reject(r.error);
  });
}

async function cacheGet(key) {
  try {
    const db = await openDb();
    return await new Promise((resolve) => {
      const q = db.transaction(STORE, 'readonly').objectStore(STORE).get(key);
      q.onsuccess = () => resolve(q.result || null);
      q.onerror = () => resolve(null);
    });
  } catch {
    return null;
  }
}

async function cachePut(key, value) {
  try {
    const db = await openDb();
    await new Promise((resolve) => {
      const tx = db.transaction(STORE, 'readwrite');
      const store = tx.objectStore(STORE);
      store.clear(); // an older table is of no use
      store.put(value, key);
      tx.oncomplete = tx.onerror = tx.onabort = () => resolve();
    });
  } catch {
    // private window or storage blocked: the table is built again next time
  }
}

async function start() {
  await init();
  sim = new Simulator();
  postMessage({ type: 'defaults', defaults: JSON.parse(Simulator.defaults()) });
  const key = Simulator.table_version();
  let cached = false;
  const kept = await cacheGet(key);
  if (kept) {
    postMessage({ type: 'progress', value: 0.99, loading: true });
    cached = sim.load_table(kept);
  }
  if (!cached) {
    let p = 0;
    let last = 0;
    while (p < 1) {
      p = sim.build_step(32);
      const now = performance.now();
      if (now - last > 50 || p >= 1) {
        postMessage({ type: 'progress', value: p });
        last = now;
      }
    }
    cachePut(key, sim.table_bytes());
  }
  postMessage({ type: 'ready', cached });
}

self.onmessage = async (ev) => {
  const msg = ev.data;
  if (msg.type === 'init') {
    try {
      await start();
    } catch (e) {
      postMessage({ type: 'fatal', message: String((e && e.message) || e) });
    }
  } else if (msg.type === 'simulate') {
    try {
      const t0 = performance.now();
      const text = sim.simulate(JSON.stringify(msg.request));
      postMessage({ type: 'result', id: msg.id, report: JSON.parse(text), ms: performance.now() - t0 });
    } catch (e) {
      postMessage({ type: 'error', id: msg.id, message: String((e && e.message) || e) });
    }
  }
};

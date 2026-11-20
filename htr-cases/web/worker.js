// Runs the case index (WebAssembly) off the page's thread.  Messages: {id, op, args} -> {id, ok, value | error}.
import init, { Index } from './pkg/htr_cases_wasm.js';

let index = null;
const ready = init().then(() => {
  index = new Index();
});

const ops = {
  cases: () => index.cases(),
  prepare: () => (index.prepare(), 'null'),
  solutions: (number, turned, maxLen) => index.solutions(number, turned, maxLen),
  find: (text, maxLen) => index.find(text, maxLen),
};

self.onmessage = async (e) => {
  const { id, op, args } = e.data;
  try {
    await ready;
    self.postMessage({ id, ok: true, value: JSON.parse(ops[op](...args)) });
  } catch (err) {
    self.postMessage({ id, ok: false, error: String(err && err.message ? err.message : err) });
  }
};

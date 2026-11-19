// A small 3D drawing of the cube on a canvas: every piece a box, the highlighted ones solid, the others glass, so that
// pieces at the back show through.  Pieces are named by their faces ("UFR", "DB", "U"); x is R, y is U, z is F.

const FACE = { U: [0, 1, 0], D: [0, -1, 0], R: [1, 0, 0], L: [-1, 0, 0], F: [0, 0, 1], B: [0, 0, -1] };
const LETTER_OF = new Map(Object.entries(FACE).map(([k, v]) => [v.join(), k]));

export const DEFAULT_VIEW = { yaw: -0.6, pitch: 0.5 };
const HALF = 0.42; // half the side of a piece (1 = spacing)
const DISTANCE = 9; // camera distance, in pieces

function placeOf(name) {
  const p = [0, 0, 0];
  for (const ch of name) FACE[ch].forEach((v, i) => (p[i] += v));
  return p;
}

const PIECES = [];
for (let x = -1; x <= 1; x++)
  for (let y = -1; y <= 1; y++)
    for (let z = -1; z <= 1; z++) if (x || y || z) PIECES.push([x, y, z]);

const FACE_DIRS = Object.values(FACE);
const AXES = [[0, 1, 2], [1, 2, 0], [2, 0, 1]];

function colors() {
  const css = getComputedStyle(document.documentElement);
  const v = (name) => css.getPropertyValue(name).trim();
  return { bad: v('--bad-piece'), ghost: v('--ghost'), line: v('--ghost-line'),
    solidLine: v('--solid-line'), label: v('--muted') };
}

// Mix a #rrggbb colour with white (amount > 0) or black (amount < 0).
function shade(hex, amount) {
  const n = parseInt(hex.slice(1), 16);
  const ch = [n >> 16, (n >> 8) & 255, n & 255].map((c) => Math.round(amount > 0 ? c + (255 - c) * amount : c * (1 + amount)));
  return `rgb(${ch.join(',')})`;
}

export class CubeView {
  constructor(canvas, { interactive = false } = {}) {
    this.canvas = canvas;
    this.view = { ...DEFAULT_VIEW };
    this.model = { corners: [], edges: [] };
    if (interactive) this.listen();
  }

  set(model) {
    this.model = model;
    this.draw();
  }

  reset() {
    this.view = { ...DEFAULT_VIEW };
    this.draw();
  }

  listen() {
    const c = this.canvas;
    let last = null;
    c.style.touchAction = 'none';
    c.addEventListener('pointerdown', (e) => { last = [e.clientX, e.clientY]; c.setPointerCapture(e.pointerId); });
    c.addEventListener('pointermove', (e) => {
      if (!last) return;
      this.view.yaw += (e.clientX - last[0]) * 0.012;
      this.view.pitch = Math.max(-1.45, Math.min(1.45, this.view.pitch + (e.clientY - last[1]) * 0.012));
      last = [e.clientX, e.clientY];
      this.draw();
    });
    const stop = () => (last = null);
    c.addEventListener('pointerup', stop);
    c.addEventListener('pointercancel', stop);
    c.addEventListener('dblclick', () => this.reset());
  }

  draw() {
    const canvas = this.canvas;
    const ratio = window.devicePixelRatio || 1;
    const size = canvas.clientWidth;
    if (!size) return;
    if (canvas.width !== Math.round(size * ratio)) {
      canvas.width = canvas.height = Math.round(size * ratio);
    }
    const ctx = canvas.getContext('2d');
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
    ctx.clearRect(0, 0, size, size);
    const col = colors();

    const { yaw, pitch } = this.view;
    const [cy, sy, cp, sp] = [Math.cos(yaw), Math.sin(yaw), Math.cos(pitch), Math.sin(pitch)];
    const rotate = ([x, y, z]) => {
      const x1 = x * cy + z * sy, z1 = -x * sy + z * cy;
      return [x1, y * cp - z1 * sp, y * sp + z1 * cp];
    };
    const scale = size * 1.75; // the cube about fills the canvas
    const project = ([x, y, z]) => {
      const s = scale / (DISTANCE - z);
      return [size / 2 + x * s, size / 2 - y * s];
    };

    const solid = new Map();
    for (const n of [...this.model.corners, ...this.model.edges]) solid.set(placeOf(n).join(), col.bad);
    const light = [-0.35, 0.8, 0.5];

    // every face facing the camera, drawn far to near
    const faces = [];
    for (const p of PIECES) {
      const fill = solid.get(p.join());
      for (const d of FACE_DIRS) {
        const outer = d.some((v, i) => v !== 0 && v === p[i]);
        if (!fill && !outer) continue; // glass pieces: only their outside
        const n = rotate(d);
        const centre = rotate(p.map((v, i) => v + d[i] * HALF));
        if (n[0] * -centre[0] + n[1] * -centre[1] + n[2] * (DISTANCE - centre[2]) <= 0) continue;
        const k = d.findIndex((v) => v !== 0);
        const [, a, b] = AXES[k];
        const corners = [[-1, -1], [1, -1], [1, 1], [-1, 1]].map(([u, v]) => {
          const q = p.map((c, i) => c + d[i] * HALF);
          q[a] += u * HALF;
          q[b] += v * HALF;
          return project(rotate(q));
        });
        const brightness = n[0] * light[0] + n[1] * light[1] + n[2] * light[2];
        const centreLabel = p.filter((v) => v !== 0).length === 1 && outer ? LETTER_OF.get(d.join()) : null;
        faces.push({ depth: centre[2], corners, fill, brightness, label: centreLabel, at: project(centre) });
      }
    }
    faces.sort((f, g) => f.depth - g.depth);
    ctx.lineJoin = 'round';
    for (const f of faces) {
      ctx.beginPath();
      f.corners.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)));
      ctx.closePath();
      if (f.fill) {
        ctx.fillStyle = shade(f.fill, f.brightness * 0.35);
        ctx.fill();
        ctx.strokeStyle = col.solidLine;
        ctx.lineWidth = Math.max(0.6, size / 220);
      } else {
        ctx.fillStyle = col.ghost;
        ctx.fill();
        ctx.strokeStyle = col.line;
        ctx.lineWidth = Math.max(0.5, size / 300);
      }
      ctx.stroke();
      if (f.label && size >= 90) {
        ctx.fillStyle = col.label;
        ctx.font = `600 ${Math.round(size / 13)}px system-ui, sans-serif`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(f.label, f.at[0], f.at[1]);
      }
    }
  }
}

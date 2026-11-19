#!/usr/bin/env python3
"""The mazes and the flow chart, as inline SVG that follows the site's light and dark colours.

Everything drawn is computed from the tables: the transitions between the six corner types, between the shapes
of the out corners, between the pictures of the D-colour corners, and the cases within two quarter turns of HTR.
Writes research/out/figures.json (name -> svg) and research/out/figdata.json (the numbers behind them).

usage: figures.py
"""
import json
import os
from collections import Counter, defaultdict

import numpy as np

import c3
from core import N, T, shape_names, kinds_text, scramble, descend, A_FREE, B_PLACES, LETTER

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
QUARTER = [0, 2, 3, 5, 6, 8]


# ---------- drawing ----------

class Svg:
    def __init__(self, w, h, title):
        self.w, self.h, self.title, self.parts = w, h, title, []

    def box(self, x, y, w, h, lines, bold=False, soft=True):
        fill = "var(--soft)" if soft else "none"
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" '
                          f'stroke="currentColor" stroke-width="1.2"/>')
        n = len(lines)
        for i, line in enumerate(lines):
            ty = y + h / 2 + (i - (n - 1) / 2) * 15 + 4.5
            weight = ' font-weight="650"' if bold and i == 0 else ""
            self.parts.append(f'<text x="{x + w / 2}" y="{ty:.1f}" text-anchor="middle"{weight}>{esc(line)}</text>')

    def line(self, x1, y1, x2, y2, label=None, arrow=False, dash=False, lx=None, ly=None):
        extra = ' marker-end="url(#arr)"' if arrow else ""
        extra += ' stroke-dasharray="5 4"' if dash else ""
        self.parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="currentColor" '
                          f'stroke-width="1.2"{extra}/>')
        if label:
            mx = (x1 + x2) / 2 if lx is None else lx
            my = (y1 + y2) / 2 if ly is None else ly
            self.text(mx, my, label, small=True, halo=True)

    def loop(self, x, y, label):
        """A turn that stays in the same node: a small loop above (x, y)."""
        self.parts.append(f'<path d="M {x - 14} {y} C {x - 30} {y - 34}, {x + 30} {y - 34}, {x + 14} {y}" fill="none" '
                          f'stroke="currentColor" stroke-width="1.2"/>')
        self.text(x, y - 30, label, small=True, halo=True)

    def text(self, x, y, s, small=False, halo=False, anchor="middle", bold=False):
        size = ' font-size="12"' if small else ""
        weight = ' font-weight="650"' if bold else ""
        if halo:
            self.parts.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}"{size} stroke="var(--bg)" '
                              f'stroke-width="5" stroke-linejoin="round" fill="var(--bg)">{esc(s)}</text>')
        self.parts.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}"{size}{weight}>{esc(s)}</text>')

    def render(self):
        return (f'<svg viewBox="0 0 {self.w} {self.h}" width="{self.w}" role="img" aria-label="{esc(self.title)}" '
                f'style="max-width:100%;height:auto;color:var(--fg);font:14px system-ui,sans-serif" fill="currentColor">'
                f'<title>{esc(self.title)}</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" '
                f'markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" '
                f'fill="currentColor"/></marker></defs>' + "".join(self.parts) + "</svg>")


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def share(x):
    """A share of the quarter turns as a fraction with a small denominator when it is one."""
    for den in (1, 2, 3, 6, 12):
        if abs(x * den - round(x * den)) < 1e-9:
            num = round(x * den)
            return "all" if num == den else f"{num} in {den}"
    return f"{100 * x:.0f}%"


# ---------- data ----------

def type_transitions(t):
    """What a quarter turn about each axis does to each of the six types, the twisted ones named by the face
    their U/D sticker is on.  Checked on every state and quarter turn; must not depend on anything else."""
    k = t.kinds
    # the axis the U/D sticker of a twisted corner faces
    names = np.empty((N, 7), dtype="U8")
    for p in range(7):
        cw = [1, 2, 0] if c3.TETRAD[p] else [1, 0, 2]
        face = np.array(cw)[t.O[:, p]]
        col = np.where(k[:, p] == 0, "good", np.where(k[:, p] >= 3, np.char.add("out-", np.array(list("ruf"))[np.clip(k[:, p] - 3, 0, 2)]),
                                                      np.where(face == 2, "tw-FB", "tw-RL")))
        names[:, p] = col
    rule = {}
    for m in QUARTER:
        axis = m // 3
        on = c3.ON[axis]
        nxt = t.mv[m]
        # where each place of the face goes
        s0 = c3.apply(t.mv, 0, [m])
        dest = {int(p): int(np.where(t.P[s0] == p)[0][0]) for p in on}
        for p in on:
            before = names[:, p]
            after = names[nxt, dest[int(p)]]
            pairs = np.unique(np.char.add(np.char.add(before, ">"), after))
            for pr in pairs:
                a, b = pr.split(">")
                key = ("RUF"[axis], a)
                assert rule.setdefault(key, b) == b, (key, b, rule[key])
        # corners off the face keep their type
        for p in range(7):
            if p not in on:
                assert (names[:, p] == names[nxt, p]).all()
    return rule


def shape_maze(t, shape):
    tr = defaultdict(Counter)
    for m in QUARTER:
        u, c = np.unique(np.char.add(np.char.add(shape, ">"), shape[t.mv[m]]), return_counts=True)
        for k_, v in zip(u, c):
            a, b = k_.split(">")
            tr[a][b] += int(v)
    qtet = c3.u8("qt_tet")
    out = {}
    for a in ("0c", "2c", "4a", "4b", "6c"):
        tot = sum(tr[a].values())
        m = shape == a
        out[a] = dict(to={b: v / tot for b, v in sorted(tr[a].items())}, states=int(m.sum()), share=float(m.mean()),
                      qt=int(qtet[m].max()), moves=sorted(set(t.dtet[m].tolist())))
    return out


def colour_maze(t):
    col = t.col[:, 1].astype(np.int64)
    lab = col.copy()
    changed = True
    while changed:
        changed = False
        for m in (1, 4, 7):
            new = np.minimum(lab, lab[t.mv[m]])
            if (new != lab).any():
                lab, changed = new, True
    six = set(np.unique(col[t.d == 0]).tolist())
    names = {}
    for o in np.unique(lab):
        mem = sorted(set(col[lab == o].tolist()))
        in_a = sum(1 for p in range(7) if mem[0] >> p & 1 and c3.TETRAD[p]) + 1
        nm = {2: "4a" if mem[0] in six else "4b", 3: "4c (3-1)", 1: "4c (1-3)", 4: "4d"}[in_a]
        names[int(o)] = (nm, len(mem))
    cname = np.array([names[int(x)][0] for x in lab])
    tr = defaultdict(Counter)
    for m in QUARTER:
        u, c = np.unique(np.char.add(np.char.add(cname, ">"), cname[t.mv[m]]), return_counts=True)
        for k_, v in zip(u, c):
            a, b = k_.split(">")
            tr[a][b] += int(v)
    # floor: turns from each picture to one of the six, in the 35-picture graph
    pics = sorted(set(col.tolist()))
    first = {p: int(np.where(col == p)[0][0]) for p in pics}
    nxt = {p: [int(col[t.mv[m][first[p]]]) for m in range(9)] for p in pics}
    dist = {p: (0 if p in six else 99) for p in pics}
    frontier = [p for p in pics if p in six]
    while frontier:
        new = []
        for p in frontier:
            for r in nxt[p]:
                if dist[r] > dist[p] + 1:
                    dist[r] = dist[p] + 1
                    new.append(r)
        frontier = new
    floor = np.array([dist[int(x)] for x in col])
    assert (floor <= t.d).all()
    out = {}
    for o, (nm, size) in names.items():
        tot = sum(tr[nm].values())
        m = cname == nm
        out[nm] = dict(pictures=size, to={b: v / tot for b, v in sorted(tr[nm].items())}, share=float(m.mean()),
                       floor=int(floor[m].max()))
    return out, float(floor.mean())


def low_cases(t, shape):
    """The type patterns (up to half turns and the six symmetries) that can be within two quarter turns of HTR."""
    q = t.q
    cls = t.cls
    # symmetry classes of half-turn classes: smallest class label over the six images
    best = cls.copy()
    for k in range(1, 6):
        best = np.minimum(best, cls[t.sym[k]])
    # close under the relation (two half-turn classes with a common symmetric image are one case)
    sizes = Counter(cls.tolist())
    cases = []
    for c in np.unique(best):
        m = best == c
        if t.qg[m].min() > 2:
            continue
        idx = np.where(m)[0]
        members = np.unique(cls[idx])
        # per half-turn class: 6 cosets; how many at each q
        one = np.where(cls == members[0])[0]
        sig = np.bincount(q[one], minlength=9) * 6 // len(one)
        k = t.kinds[idx[0]]
        wit = {}
        for qq in range(3):
            sel = idx[q[idx] == qq]
            if len(sel):
                w = int(sel[np.lexsort((sel, t.d[sel], t.dsolved[sel]))[0]])
                wit[qq] = dict(scramble=scramble(t, w), kinds=kinds_text(t.kinds[w]), d=int(t.d[w]),
                               solution=c3.show(descend(t, w, t.d)))
        cases.append(dict(floor=int(t.qg[idx].min()), classes=len(members), patterns=int(sum(sizes[int(x)] for x in members) // 144),
                          cosets=[int(x) for x in sig], twisted=int(t.nT[idx[0]]), out=sorted(t.xa[idx[0]].tolist(), reverse=True),
                          a="".join(sorted(LETTER[k[p]] for p in A_FREE)), b="".join(sorted(LETTER[k[p]] for p in B_PLACES)),
                          shape=str(shape[idx[0]]), witness=wit))
    cases.sort(key=lambda c_: (c_["floor"], c_["twisted"], c_["patterns"]))
    return cases


# ---------- figures ----------

def fig_types(rule):
    s = Svg(720, 330, "What a quarter turn does to a corner: the six types")
    left = [("good", ["good", "3 stickers oriented"]), ("tw-FB", ["twisted", "U/D sticker on F/B"]),
            ("tw-RL", ["twisted", "U/D sticker on R/L"])]
    right = [("out-u", ["out", "only U/D oriented"]), ("out-r", ["out", "only R/L oriented"]),
             ("out-f", ["out", "only F/B oriented"])]
    pos = {}
    for i, (name, lines) in enumerate(left):
        s.box(20, 30 + i * 105, 180, 60, lines, bold=True)
        pos[name] = (200, 60 + i * 105)
    for i, (name, lines) in enumerate(right):
        s.box(520, 30 + i * 105, 180, 60, lines, bold=True)
        pos[name] = (520, 60 + i * 105)
    done = set()
    for (face, a), b in sorted(rule.items()):
        if (b, a, face) in done:
            continue
        done.add((a, b, face))
        l, r = (a, b) if a in dict(left) else (b, a)
        x1, y1 = pos[l]
        x2, y2 = pos[r]
        # put the label a quarter of the way along, nearer the left end, so the nine labels do not collide
        f = {"good": 0.2, "tw-FB": 0.33, "tw-RL": 0.2}[l]
        s.line(x1, y1, x2, y2, label=face, lx=x1 + f * (x2 - x1), ly=y1 + f * (y2 - y1) + 4)
    s.text(360, 322, "A line marked R is a quarter turn of R (either way) on a corner of the R face; U and F alike.", small=True)
    return s.render()


def fig_shape(data):
    s = Svg(720, 330, "The out corners: shapes, and where a quarter turn can take them")
    pos = {"0c": (40, 130), "4a": (200, 130), "4b": (380, 130), "2c": (560, 60), "6c": (560, 210)}
    w, h = 120, 64
    desc = {"0c": "no corner out", "4a": "4 out, like a face", "4b": "4 out, bars", "2c": "2 out", "6c": "6 out"}
    for name, (x, y) in pos.items():
        d = data[name]
        s.box(x, y, w, h, [name, desc[name], f"at least {d['qt']} qt" if d["qt"] else "0 qt"], bold=True)

    def edge(a, b, dy=0):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        if abs(y1 - y2) < 5:
            xa, xb = (x1 + w, x2) if x1 < x2 else (x1, x2 + w)
            s.line(xa, y1 + h / 2 + dy, xb, y2 + h / 2 + dy)
        else:
            s.line(x1 + w if x1 < x2 else x1 + w / 2, y1 + (h / 2 if x1 < x2 else (h if y1 < y2 else 0)),
                   x2 if x1 < x2 else x2 + w / 2, y2 + (h / 2 if x1 < x2 else (0 if y1 < y2 else h)))

    edge("0c", "4a")
    edge("4a", "4b")
    edge("4b", "2c")
    edge("4b", "6c")
    edge("2c", "6c")
    s.loop(pos["4a"][0] + w / 2, pos["4a"][1], "can stay")
    s.loop(pos["2c"][0] + w / 2, pos["2c"][1], "can stay")
    s.text(360, 300, "One line = one quarter turn of R, U or F. Half turns never change the shape.", small=True)
    s.text(360, 318, "4a: on one face, or on one after half turns. 0c and 4b always change. 6 out is 2c seen from the other side.", small=True)
    return s.render()


def fig_colour(data):
    s = Svg(720, 300, "The D-colour corners: pictures, and where a quarter turn can take them")
    pos = {"4d": (30, 110), "4a": (200, 110), "4b": (380, 110), "4c": (560, 110)}
    w, h = 130, 64
    desc = {"4a": ["4a", "2 and 2, HTR-like", "0 qt"], "4b": ["4b", "2 and 2, bars", "at least 1 qt"],
            "4c": ["4c", "3 and 1", "at least 2 qt"], "4d": ["4d", "4 and 0", "at least 1 qt"]}
    for name, (x, y) in pos.items():
        s.box(x, y, w, h, desc[name], bold=True)
    for a, b in (("4d", "4a"), ("4a", "4b"), ("4b", "4c")):
        s.line(pos[a][0] + w, pos[a][1] + h / 2, pos[b][0], pos[b][1] + h / 2)
    s.loop(pos["4a"][0] + w / 2, pos["4a"][1], "can stay")
    s.loop(pos["4c"][0] + w / 2, pos["4c"][1], "can stay")
    s.text(360, 235, "Count the four corners that carry the D colour (DBL is one) by tetrad: 2 and 2, 3 and 1, or 4 and 0.", small=True)
    s.text(360, 253, "4a: the two pairs sit on the same face or on opposite faces. One line = one quarter turn of R, U or F.", small=True)
    s.text(360, 271, "These are rodneykinney's UD labels with the same 0, 1, 2, 1 quarter turns: nothing changes off the DR axis.", small=True)
    del data
    return s.render()


def case_label(c):
    tw = c["twisted"]
    out = [x for x in c["out"] if x]
    parts = []
    if out:
        parts.append(" + ".join(str(x) for x in out) + " out")
    if tw:
        parts.append(f"{tw} twisted")
    return ", ".join(parts) or "all good"


def fig_funnel(cases):
    s = Svg(720, 500, "Every kind of corner pattern within two quarter turns of HTR")
    cols = {2: 20, 1: 300, 0: 560}
    for qq, x in cols.items():
        s.text(x + (110 if qq == 2 else 80), 22, ["HTR", "1 quarter turn", "2 quarter turns"][qq], bold=True)
    two = [c for c in cases if c["cosets"][2]]
    one = [c for c in cases if c["cosets"][1]]
    ys = {}
    for i, c in enumerate(two):
        y = 40 + i * 84
        name = case_label(c) + (f" ({c['shape']})" if c["shape"] in ("4a", "4b") and not c["twisted"] else "")
        s.box(cols[2], y, 230, 70, [name, c["witness"]["2"]["scramble"] if "2" in c["witness"] else c["witness"][2]["scramble"],
                                    f"really 2 qt: {c['cosets'][2]} of 6"], bold=True)
        ys[i] = y + 35
    y1 = 40 + (len(two) - 1) * 42
    for c in one:
        s.box(cols[1], y1, 200, 70, [case_label(c) + " (4a)", c["witness"][1]["scramble"], f"really 1 qt: {c['cosets'][1]} of 6"], bold=True)
    s.box(cols[0], y1, 140, 70, ["all good", "really HTR:", "1 of 6"], bold=True)
    for i in ys:
        s.line(cols[2] + 230, ys[i], cols[1], y1 + 35)
    s.line(cols[1] + 200, y1 + 35, cols[0], y1 + 35)
    s.text(360, 478, "Each box: what you count, a scramble that makes it, and how many of the six states that look", small=True)
    s.text(360, 494, "alike are that close. One line = one quarter turn, after half turns to set it up.", small=True)
    return s.render()


def fig_flow():
    s = Svg(720, 560, "Flow chart: reading the corners for a floor and for the next turn")
    x, w, h = 20, 330, 64
    steps = [
        (["1. Type every corner", "3 oriented stickers: good. 1: out. 0: twisted."], 20),
        (["2. Are they all good?"], 130),
        (["3. Count twisted, and out per axis", "The count table gives a floor."], 240),
        (["4. Can you see how to make them", "all good in 4 turns or less?"], 350),
        (["5. Further out", "The types don't tell the closer turn.", "Cut with the floors, then search."], 460),
    ]
    for lines, y in steps:
        s.box(x, y, w, h + (14 if len(lines) == 3 else 0), lines, bold=True)
    for (_, y1), (_, y2) in zip(steps, steps[1:]):
        s.line(x + w / 2, y1 + h, x + w / 2, y2, arrow=True)
    s.text(x + w / 2 + 10, 222, "no", small=True, anchor="start")
    s.text(x + w / 2 + 10, 442, "no", small=True, anchor="start")
    # to the right: what "yes" leads to
    rx, rw = 420, 280
    s.box(rx, 110, rw, 104, ["D-colour corners in a 4a picture,", "and parity even?", "Yes: HTR.", "No: fake HTR, exactly 9 moves away."], soft=False)
    s.line(x + w, 162, rx, 162, arrow=True)
    s.text(x + w + 34, 154, "yes", small=True)
    s.box(rx, 330, rw, 104, ["That is the shortest way to all good.", "It ends in HTR for 1 state in 6", "that look like yours: check the end", "the way step 2 does."], soft=False)
    s.line(x + w, 382, rx, 382, arrow=True)
    s.text(x + w + 34, 374, "yes", small=True)
    return s.render()


def main():
    t = T.load()
    shape = shape_names(t)
    rule = type_transitions(t)
    sm = shape_maze(t, shape)
    cm, cmean = colour_maze(t)
    cases = low_cases(t, shape)
    figs = dict(types=fig_types(rule), shape=fig_shape(sm), colour=fig_colour(cm), funnel=fig_funnel(cases),
                flow=fig_flow())
    data = dict(rule={f"{k[0]} {k[1]}": v for k, v in sorted(rule.items())}, shape=sm, colour=cm,
                colour_floor_mean=cmean, cases=cases)
    with open(os.path.join(OUT, "figures.json"), "w") as fh:
        json.dump(figs, fh)
    with open(os.path.join(OUT, "figdata.json"), "w") as fh:
        json.dump(data, fh, indent=1)
    os.makedirs(os.path.join(OUT, "figures"), exist_ok=True)
    for name, svg in figs.items():
        with open(os.path.join(OUT, "figures", name + ".svg"), "w") as fh:
            fh.write(svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" '))
    print(json.dumps(data["rule"], indent=0))
    print("cases within two quarter turns:", len(cases))
    for c in cases:
        print(c["floor"], case_label(c), c["shape"], "|", c["a"], c["b"], "| patterns", c["patterns"], "cosets", c["cosets"][:6], "|",
              {k: (v["scramble"], v["kinds"]) for k, v in c["witness"].items()})


if __name__ == "__main__":
    main()

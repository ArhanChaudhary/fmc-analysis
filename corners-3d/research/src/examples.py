#!/usr/bin/env python3
"""The data of the examples page: research/out/examples.json.

    catalogue   every type pattern within 3 moves of all good, one per symmetry class
    random      200 uniformly random states, with everything a reader checks against
    dr          DR corner cases by subset, with the DR-only and the all-turn optimal

usage: examples.py
"""
import json
import os
from collections import Counter

import numpy as np

import c3
from core import N, T, kinds_text, scramble, descend, all_shortest, shape_names, quarters

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
SEED = 20261119


def colour_class(t):
    """rodneykinney's label of the D-colour picture of every state: 4a, 4b, 4c or 4d."""
    col = t.col[:, 1].astype(np.int64)
    six = set(np.unique(col[t.d == 0]).tolist())
    names = {}
    for bits in np.unique(col):
        in_a = sum(1 for p in range(7) if bits >> p & 1 and c3.TETRAD[p]) + 1
        names[int(bits)] = {2: "4a" if int(bits) in six else "4b", 3: "4c", 1: "4c", 4: "4d"}[in_a]
    return np.array([names[int(x)] for x in col])


def facts(t, s, shape, cclass, dn, cf):
    """Everything printed about one state."""
    k = t.kinds[s]
    sol = descend(t, s, t.d)
    return dict(
        scramble=scramble(t, s), kinds=kinds_text(k), twisted=int(t.nT[s]),
        out=[int(x) for x in t.xa[s]], shape=str(shape[s]), colour=str(cclass[s]), parity="odd" if t.par[s] else "even",
        floor_count=int(cf[0][s]), floor_count_q=int(cf[1][s]), floor_types=int(t.dg[s]), floor_par=int(t.de[s]),
        floor_types_q=int(t.qg[s]), subset=int(t.qp[s]), d=int(t.d[s]), q=int(t.q[s]), niss=int(dn[s]),
        closer=[c3.MOVES[m] for m in range(9) if t.closer[s, m]], solution=c3.show(sol), solution_q=quarters(sol),
        n_solutions=len(all_shortest(t, s, t.d, limit=99)),
        types_solution=c3.show(descend(t, s, t.dg)),
        types_solution_ends=int(t.d[c3.apply(t.mv, s, descend(t, s, t.dg))]),
    )


def main():
    t = T.load()
    shape = shape_names(t)
    cclass = colour_class(t)
    dn = np.load(os.path.join(c3.BIG, "d_niss.npy"))
    count_key = t.nT * 1000 + t.xs[:, 0] * 100 + t.xs[:, 1] * 10 + t.xs[:, 2]
    cf = []
    for y in (t.d, t.q):
        u, iv = np.unique(count_key, return_inverse=True)
        mn = np.full(len(u), 99, dtype=np.int64)
        np.minimum.at(mn, iv, y)
        cf.append(mn[iv])
    E = {}

    # --- catalogue: patterns with a types floor of 3 or less, up to the six symmetries
    pid = t.pid.astype(np.int64)
    canon = pid.copy()
    for k in range(1, 6):
        canon = np.minimum(canon, pid[t.sym[k]])
    rows = []
    near = np.where(t.dg <= 3)[0]
    seen = {}
    for s in near:
        c = int(canon[s])
        if c not in seen:
            seen[c] = []
        if int(pid[s]) not in [x[0] for x in seen[c]]:
            seen[c].append((int(pid[s]), int(s)))
    patterns_total = len({int(pid[s]) for s in near})
    for c, members in seen.items():
        # the member whose state is closest to solved, to get a short scramble; among the 144 states of a pattern
        # take the one that really is that close to HTR
        best = None
        for p_, _ in members:
            cand = np.where(pid == p_)[0]
            cand = cand[t.d[cand] == t.dg[cand]]
            w = int(cand[np.lexsort((cand, t.dsolved[cand]))[0]])
            if best is None or (t.dsolved[w], w) < (t.dsolved[best], best):
                best = w
        sols = all_shortest(t, best, t.dg, limit=50)
        rows.append(dict(floor=int(t.dg[best]), patterns=len(members), kinds=kinds_text(t.kinds[best]),
                         twisted=int(t.nT[best]), out=sorted([int(x) for x in t.xa[best]], reverse=True),
                         shape=str(shape[best]), scramble=scramble(t, best), ways=[c3.show(x) for x in sols[:4]],
                         n_ways=len(sols), quarter=min(quarters(x) for x in sols)))
    rows.sort(key=lambda r: (r["floor"], r["quarter"], r["twisted"], r["out"], r["kinds"]))
    E["catalogue"] = rows
    E["catalogue_patterns"] = patterns_total
    E["catalogue_by_floor"] = [int(x) for x in np.bincount([r["floor"] for r in rows], minlength=4)]
    E["patterns_by_floor"] = [int(x) for x in np.bincount(t.dg[np.unique(pid, return_index=True)[1]], minlength=10)]

    # --- 200 uniformly random states
    rng = np.random.default_rng(SEED)
    picks = rng.integers(0, N, size=200)
    E["random"] = [facts(t, int(s), shape, cclass, dn, cf) for s in picks]
    E["random_summary"] = dict(
        d=dict(sorted(Counter(int(t.d[s]) for s in picks).items())), q=dict(sorted(Counter(int(t.q[s]) for s in picks).items())),
        types_exact=int(sum(t.dg[s] == t.d[s] for s in picks)), par_exact=int(sum(t.de[s] == t.d[s] for s in picks)),
        types_way_htr=int(sum(1 for e in E["random"] if e["types_solution_ends"] == 0)))

    # --- DR corner cases (oriented on U/D): one or two per subset, the ones leaving DR helps most first
    dr = np.where(t.dco[:, 1] == 0)[0]
    by = {}
    for s in dr:
        name = shape[s].replace("6c", "2c") + str(int(t.qdr[s, 1]))
        by.setdefault(name, []).append(int(s))
    rows = []
    for name in sorted(by):
        states = np.array(by[name])
        save = t.ddr[states, 1].astype(int) - t.d[states]
        order = np.lexsort((states, t.dsolved[states], -save))
        chosen = [int(states[order[0]])]
        # a second one where nothing is saved, if the subset has both kinds
        zero = states[save == 0]
        if save.max() > 0 and len(zero):
            chosen.append(int(zero[np.lexsort((zero, t.dsolved[zero]))[0]]))
        for s in chosen:
            drsol = descend_moves(t, s, t.ddr[:, 1], (3, 4, 5, 1, 7))
            rows.append(dict(subset=name, scramble=scramble_dr(t, s), kinds=kinds_text(t.kinds[s]),
                             dr_only=int(t.ddr[s, 1]), dr_solution=c3.show(drsol), all=int(t.d[s]),
                             solution=c3.show(descend(t, s, t.d)), niss=int(dn[s]), q=int(t.q[s])))
    E["dr"] = rows

    with open(os.path.join(OUT, "examples.json"), "w") as fh:
        json.dump(E, fh, indent=1)
    print("catalogue:", len(E["catalogue"]), "classes for", patterns_total, "patterns", E["catalogue_by_floor"])
    print("random:", E["random_summary"])
    print("dr rows:", len(rows))


def descend_moves(t, s, table, moves):
    out = []
    while table[s] > 0:
        for m in moves:
            n = int(t.mv[m][s])
            if table[n] < table[s]:
                out.append(m)
                s = n
                break
        else:
            raise ValueError("no way down")
    return out


_DRS = {}


def scramble_dr(t, s):
    """A shortest scramble of a DR state that uses DR turns only (U, R2, F2), so it reads as a DR case."""
    if "d" not in _DRS:
        dist = np.full(N, 99, dtype=np.int16)
        dist[0] = 0
        level = 0
        while True:
            S = np.where(dist == level)[0]
            if len(S) == 0:
                break
            for m in (3, 4, 5, 1, 7):
                nb = t.mv[m][S]
                dist[nb] = np.minimum(dist[nb], level + 1)
            level += 1
        _DRS["d"] = dist
    return c3.show(c3.invert(descend_moves(t, s, _DRS["d"], (3, 4, 5, 1, 7))))


if __name__ == "__main__":
    main()

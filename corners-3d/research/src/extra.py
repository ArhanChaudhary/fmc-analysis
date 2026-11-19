#!/usr/bin/env python3
"""Numbers that need more than the main tables: NISS (turns on both sides), the server's claims, and the
eight-corner checks.  Writes research/out/extra.json.

usage: extra.py
"""
import json
import os
from collections import Counter, deque

import numpy as np

import c3
import fullcorners as fc
from core import N, T, kinds_text, scramble, shape_names

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")


def hist(a, size=0):
    return [int(x) for x in np.bincount(np.asarray(a).astype(np.int64), minlength=size)]


def niss(t, table, moves=range(9)):
    """Fewest turns with turns allowed on both sides: min over X of |X| + table(inverse of s X), and the same
    with nothing on the inverse."""
    D = np.minimum(table[t.inverse].astype(np.int64), table.astype(np.int64))
    for level in range(0, 14):
        S = np.where(D == level)[0]
        for m in moves:
            nb = t.mv[m][S]
            D[nb] = np.minimum(D[nb], level + 1)
    return D


_DR = {}


def scramble_dr_turns(t, s):
    """A shortest scramble of a DR state in U, R2, F2 turns."""
    if "d" not in _DR:
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
        _DR["d"] = dist
    dist = _DR["d"]
    out = []
    while dist[s] > 0:
        for m in (3, 4, 5, 1, 7):
            nb = int(t.mv[m][s])
            if dist[nb] < dist[s]:
                out.append(m)
                s = nb
                break
    return c3.show(c3.invert(out))


def inv_seq(s):
    return " ".join(m[0] + {"": "'", "2": "2", "'": ""}[m[1:]] for m in reversed(s.split()))


def main():
    t = T.load()
    d = t.d.astype(np.int64)
    q = t.q.astype(np.int64)
    E = {}

    # --- NISS
    dN = niss(t, d)
    dgN = niss(t, t.dg)
    deN = niss(t, t.de)
    np.save(os.path.join(c3.BIG, "d_niss.npy"), dN.astype(np.int8))
    np.save(os.path.join(c3.BIG, "dg_niss.npy"), dgN.astype(np.int8))
    np.save(os.path.join(c3.BIG, "de_niss.npy"), deN.astype(np.int8))
    count_key = t.nT * 1000 + t.xs[:, 0] * 100 + t.xs[:, 1] * 10 + t.xs[:, 2]
    count_floor = {}
    for k in np.unique(count_key):
        m = count_key == k
        i = np.where(m)[0]
        w = i[np.lexsort((i, t.dsolved[i], dN[i]))[0]]
        count_floor[int(k)] = dict(floor=int(dN[i].min()), mean=float(dN[i].mean()), witness=scramble(t, int(w)))
    cf = np.zeros(N, dtype=np.int64)
    for k, v in count_floor.items():
        cf[count_key == k] = v["floor"]

    def row(name, f):
        gap = dN - f
        assert gap.min() >= 0, name
        return dict(name=name, mean=float(f.mean()), exact=float((gap == 0).mean()),
                    within1=float((gap <= 1).mean()), maxgap=int(gap.max()))

    E["niss"] = dict(
        hist=hist(dN), mean=float(dN.mean()), saves=hist(d - dN), inverse_diff=hist(np.abs(d[t.inverse] - d)),
        linear_types_floor_broken=float((t.dg > dN).mean()), linear_types_floor_excess=int((t.dg - dN).max()),
        min_by_q=[int(dN[q == k].min()) for k in range(9)], max_by_q=[int(dN[q == k].max()) for k in range(9)],
        mean_by_q=[float(dN[q == k].mean()) for k in range(9)],
        floors=[row("quarter turns", q), row("count table", cf), row("types on both sides", dgN),
                row("types on both sides + parity", deN)],
        count_floor=count_floor,
    )
    # a state where the one-sided types floor is beaten by NISS, with the turns
    bad = np.where(t.dg - dN == (t.dg - dN).max())[0]
    w = int(bad[np.argmin(d[bad])])
    E["niss"]["witness_broken"] = dict(scramble=scramble(t, w), types_floor=int(t.dg[w]), linear=int(d[w]),
                                       niss=int(dN[w]), kinds=kinds_text(t.kinds[w]))
    # which turn (on either side) gets closer, by NISS distance
    succ = [t.mv[m] for m in range(9)] + [t.inverse[t.mv[m][t.inverse]] for m in range(9)]
    closer = np.stack([dN[s] < dN for s in succ], 1)

    def grade(f):
        fn = np.stack([f[s] for s in succ], 1)
        tie = fn == fn.min(1, keepdims=True)
        return (tie & closer).sum(1) / tie.sum(1)

    g_types, g_par = grade(dgN), grade(deN)
    rows = []
    for dd in range(1, int(dN.max()) + 1):
        m = dN == dd
        rows.append(dict(d=dd, states=int(m.sum()), share=float(m.mean()), closer=float(closer[m].sum(1).mean()),
                         random=float((closer[m].sum(1) / 18).mean()), types=float(g_types[m].mean()),
                         types_par=float(g_par[m].mean())))
    E["niss"]["moves"] = rows

    # --- DR corners with DBL fixed: NISS with DR turns only, by subset
    shape = shape_names(t)
    dr = np.where(t.dco[:, 1] == 0)[0]
    ddr = t.ddr[:, 1].astype(np.int64)
    D = np.where(ddr < 99, np.minimum(ddr, ddr[t.inverse]), 99)
    for level in range(0, 13):
        S = np.where(D == level)[0]
        for m in (3, 4, 5, 1, 7):
            nb = t.mv[m][S]
            D[nb] = np.minimum(D[nb], level + 1)
    sub = {}
    for s in dr:
        name = shape[s].replace("6c", "2c") + str(int(t.qdr[s, 1]))
        e = sub.setdefault(name, dict(states=0, lin=[], niss=[], all=[], allniss=[]))
        e["states"] += 1
        e["lin"].append(int(ddr[s]))
        e["niss"].append(int(D[s]))
        e["all"].append(int(d[s]))
        e["allniss"].append(int(dN[s]))
    E["dr_subsets"] = {k: dict(states=v["states"], cases=v["states"] // 24,
                               lin_min=min(v["lin"]), lin_max=max(v["lin"]), lin_mean=float(np.mean(v["lin"])),
                               niss_min=min(v["niss"]), niss_max=max(v["niss"]), niss_mean=float(np.mean(v["niss"])),
                               all_min=min(v["all"]), all_max=max(v["all"]), all_mean=float(np.mean(v["all"])),
                               allniss_min=min(v["allniss"]), allniss_max=max(v["allniss"]),
                               allniss_mean=float(np.mean(v["allniss"])),
                               saved=hist(np.array(v["lin"]) - np.array(v["all"]), 3))
                       for k, v in sorted(sub.items())}
    E["dr_niss_min_by_q"] = [int(D[dr][t.qdr[dr, 1] == k].min()) for k in range(6)]
    E["dr_lin_min_by_q"] = [int(ddr[dr][t.qdr[dr, 1] == k].min()) for k in range(6)]

    # --- claims on the placement's quarter-turn count
    qp = t.qp.astype(np.int64)
    # what a trigger does to it
    trig = {}
    for seq in ("R", "R U2 R'", "R U R'", "R U' R'", "R' U2 R", "R U R", "R U2 R"):
        s = np.arange(N)
        for m in c3.parse(seq):
            s = t.mv[m][s]
        trig[seq] = {int(k): int(v) for k, v in sorted(Counter((qp[s] - qp).tolist()).items())}
    E["trigger_change"] = trig
    # cycle type of the placement (7 free corners) against the count
    P = t.P[::729]
    types = []
    for row_ in P:
        seen, lens = set(), []
        for i in range(7):
            if i not in seen:
                n, j = 0, i
                while j not in seen:
                    seen.add(j)
                    j = int(row_[j])
                    n += 1
                if n > 1:
                    lens.append(n)
        types.append(" ".join(f"{n}c" for n in sorted(lens, reverse=True)) or "solved")
    by = {}
    for ct, v in zip(types, qp[::729]):
        by.setdefault(ct, Counter())[int(v)] += 1
    E["cycle_type"] = {k: {str(a): b for a, b in sorted(v.items())} for k, v in sorted(by.items())}

    # torchlight's Klein-4 rule on the 144 all-good states: the two tetrad placements compared
    good = np.where(t.dg == 0)[0]
    A, B = [1, 2, 3], [0, 4, 5, 6]
    # label opposite corners alike: UFL~DBR? opposite of UFL (-1,1,1) is (1,-1,-1) = DBR, and so on
    opp = {int(p): int(np.where((c3.XYZ == -c3.XYZ[p]).all(1))[0][0]) for p in A}   # A place -> opposite B place
    klein = Counter()
    for s in good:
        perm = t.P[s]
        # tetrad B as a permutation of its four places; tetrad A as a permutation of {DBL} + 3, written on the
        # opposite places so both act on the same four labels (DBL's opposite is UFR)
        pb = {b: int(perm[b]) for b in B}
        pa = {0: 0}
        for a in A:
            pa[opp[a]] = opp[int(perm[a])]
        # the quotient pb^-1 o pa
        inv_b = {v: k for k, v in pb.items()}
        quo = {x: inv_b[pa[x]] for x in B}
        seen, lens = set(), []
        for i in B:
            if i not in seen:
                n, j = 0, i
                while j not in seen:
                    seen.add(j)
                    j = quo[j]
                    n += 1
                lens.append(n)
        klein[(tuple(sorted(lens, reverse=True)), int(q[s]))] += 1
    E["klein"] = {f"{k[0]} q{k[1]}": v for k, v in sorted(klein.items())}

    # FakeMMAP's lemma: all good, the D colour on the whole D face, even -> the four states he lists
    whole_d = (1 << 3) | (1 << 5) | (1 << 6)          # DFR, DFL, DBR
    lem = np.where((t.dg == 0) & (t.col[:, 1] == whole_d) & (t.par == 0))[0]
    want = sorted(c3.apply(t.mv, 0, s) for s in ("", "U2", "R2 F2 R2", "R2 F2 R2 U2"))
    E["lemma1"] = dict(states=len(lem), match=sorted(lem.tolist()) == want, all_htr=bool((d[lem] == 0).all()),
                       without_parity=int(((t.dg == 0) & (t.col[:, 1] == whole_d)).sum()))

    # rodneykinney's six paths
    start = c3.apply(t.mv, 0, "R2 U R2 U' R2 U F2 U")
    paths = ["U' F2 U' R2 U R2 U", "U F2 U R2 U' F2 U", "F2 U R2 U F2 U' R2 U", "F2 U' R2 U' R2 U F2 U",
             "R2 U R2 U F2 U R2 U2 F2 U", "R2 U' F2 U' F2 U R2 U2 F2 U"]
    E["six_paths"] = dict(q=int(q[start]), qdr=int(t.qdr[start, 1]), d=int(d[start]), ddr=int(t.ddr[start, 1]),
                          ok=[bool(d[c3.apply(t.mv, start, p)] == 0) for p in paths],
                          quarters=[sum(1 for m in c3.parse(p) if m % 3 != 1) for p in paths],
                          shape=str(shape[start]))

    # which quarter turn (after free half turns) lowers the quarter-turn count: per class of states up to half turns
    lab = np.arange(N)
    changed = True
    while changed:
        changed = False
        for m in (1, 4, 7):
            new = np.minimum(lab, lab[t.mv[m]])
            if (new != lab).any():
                lab, changed = new, True
    u, orb = np.unique(lab, return_inverse=True)
    no = len(u)
    qmoves = [0, 2, 3, 5, 6, 8]

    def qgrade(f):
        best = np.full(no, 10 ** 9, dtype=np.int64)
        for m in qmoves:
            np.minimum.at(best, orb, f[t.mv[m]])
        ties = np.zeros(no)
        good = np.zeros(no)
        for m in qmoves:
            tie = f[t.mv[m]] == best[orb]
            np.add.at(ties, orb, tie)
            np.add.at(good, orb, tie & (q[t.mv[m]] < q))
        return good / ties

    tot = np.zeros(no)
    down = np.zeros(no)
    for m in qmoves:
        np.add.at(tot, orb, 1)
        np.add.at(down, orb, q[t.mv[m]] < q)
    qo = np.zeros(no, dtype=np.int64)
    qo[orb] = q
    L, Le = t.qg.astype(np.int64), t.qe.astype(np.int64)
    g = dict(random=down / tot, types=qgrade(L), types_par=qgrade(Le), subset=qgrade(qp),
             all=qgrade(np.maximum(Le, qp)))
    rows = []
    for k in list(range(1, 9)) + [0]:
        m = qo > 0 if k == 0 else qo == k
        rows.append(dict(q=k, cases=int(m.sum()), **{name: float(v[m].mean()) for name, v in g.items()}))
    E["qt_moves"] = rows
    E["cases_up_to_half_turns"] = no

    # examples for the errata: a trigger that leaves the placement's count alone
    def example(seq, change):
        s2 = np.arange(N)
        for m in c3.parse(seq):
            s2 = t.mv[m][s2]
        ok = np.where((qp[s2] - qp == change) & (t.dco[:, 1] == 0))[0]      # start from a DR state, as he does
        first = c3.parse(seq)[0] // 3
        best = None
        for s_ in ok[np.argsort(t.dsolved[ok], kind="stable")]:
            scr = scramble_dr_turns(t, int(s_))
            if scr and c3.parse(scr)[-1] // 3 != first:
                best = (int(s_), scr)
                break
        best, scr = best
        return dict(scramble=scr, before=int(qp[best]), after=int(qp[s2[best]]), trigger=seq)

    # the same, the way it happens in an attempt: the state after the trigger is a DR (corners oriented on U/D)
    drs = np.where(t.dco[:, 1] == 0)[0]
    td = {}
    for seq in ("R", "R U2 R'", "R U R'", "R U' R'"):
        before = drs.copy()
        for m in c3.invert(c3.parse(seq)):
            before = t.mv[m][before]
        td[seq] = {int(k): int(v) for k, v in sorted(Counter((qp[drs] - qp[before]).tolist()).items())}
    E["trigger_change_dr"] = td
    E["trigger_examples"] = [example("R U2 R'", 0), example("R U R'", 1), example("R U R'", -1)]

    # --- eight corners, DR turns
    ds, dh, half = fc.dr_corner_search()
    names = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"]
    maps = []
    for n in names:
        s = fc.turn(fc.solved(), n)
        maps.append({p: s[p][0] for p in fc.PLACES})

    def step(pl, m):
        return tuple(m[a] for a in pl)

    def solve(pl, dist, allowed=names):
        out = []
        while dist[pl] > 0:
            for n, m in zip(names, maps):
                if n in allowed and dist[step(pl, m)] < dist[pl]:
                    out.append(n)
                    pl = step(pl, m)
                    break
            else:
                return None
        return " ".join(out)

    qd = {h: 0 for h in half}
    dq = deque(half)
    while dq:
        p = dq.popleft()
        for n, m in zip(names, maps):
            c = 0 if "2" in n else 1
            x = step(p, m)
            if qd.get(x, 99) > qd[p] + c:
                qd[x] = qd[p] + c
                (dq.appendleft if c == 0 else dq.append)(x)

    def bad(pl):
        return sum(1 for home, at in zip(fc.PLACES, pl) if home[0] * home[1] * home[2] != at[0] * at[1] * at[2])

    wen = "R2 U2 F2 U' R2 U R2 U2 F2 U' R2 U R2"
    st = fc.apply(inv_seq(wen))
    pl = fc.placement(st)
    sol = solve(pl, ds, ["U", "U2", "U'", "R2", "F2"]) or solve(pl, ds)
    assert fc.key(fc.apply(sol, st)) == fc.key(fc.solved())
    ant = [p for p, v in ds.items() if v == max(ds.values())]
    p13 = sorted(ant)[0]
    s13 = solve(p13, ds)
    assert fc.key(fc.apply(s13, fc.apply(inv_seq(s13)))) == fc.key(fc.solved())
    longest = {}
    longest_h = {}
    for p, v in ds.items():
        k = f"{min(bad(p), 8 - bad(p))} bad, {qd[p]} qt"
        longest[k] = max(longest.get(k, 0), v)
        longest_h[k] = max(longest_h.get(k, 0), dh[p])
    E["eight"] = dict(
        placements=len(ds), half=len(half), hist_solved=hist(list(ds.values())), hist_htr=hist(list(dh.values())),
        hist_q=hist(list(qd.values())), max_solved=max(ds.values()), max_htr=max(dh.values()),
        wen_case=inv_seq(wen), wen_alg=wen, wen_len=len(wen.split()), wen_true=int(ds[pl]), wen_sol=sol,
        wen_bad=bad(pl), wen_q=int(qd[pl]),
        wen_second_ok=fc.key(fc.apply("U' F2 U R2 U2 F2 U R2 U2 F2 U' F2 U2", st)) == fc.key(fc.solved()),
        torchlight_11_ok=fc.key(fc.apply("D2 F2 U' F' D F' R2 B U' B' D'", st)) == fc.key(fc.solved()),
        antipodes=len(ant), antipode_classes=dict(Counter(f"{bad(p)} bad, {qd[p]} qt" for p in ant)),
        thirteen_scramble=inv_seq(s13), thirteen_sol=s13, longest=dict(sorted(longest.items())),
        longest_htr=dict(sorted(longest_h.items())),
        r_like=fc.placement(fc.apply("R")) == fc.placement(fc.apply("D2 L2 U' L2 D2")),
        l_like=fc.placement(fc.apply("L")) == fc.placement(fc.apply("U2 L2 U' L2 U2")),
        u_like=[fc.placement(fc.apply("U")) == fc.placement(fc.apply(x)) for x in ("R2 U2 R' U2 R2", "F2 U2 F' U2 F2")],
        trangium=fc.placement(fc.apply("R2 U D L2 F B")) in half,
        # ... and it leaves every corner's U/D sticker on an R/L face
        trangium_twists=all(v[1][1][0] != 0 for v in fc.apply("R2 U D L2 F B").values()),
    )
    with open(os.path.join(OUT, "extra.json"), "w") as fh:
        json.dump(E, fh, indent=1)
    print("extra.json written")


if __name__ == "__main__":
    main()

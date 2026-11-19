#!/usr/bin/env python3
"""Every number of the write-up, from the exact tables, into research/out/numbers.json.

usage: analysis.py
"""
import json
import os
from collections import Counter

import numpy as np

import c3
import derive
from core import N, T, SHOW, kinds_text, scramble, descend, shape_names, colour_text, quarters

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")


def hist(a, size=None):
    h = np.bincount(np.asarray(a).astype(np.int64), minlength=size or 0)
    return [int(x) for x in h]


def floor_row(key, name, read, level, f, truth):
    gap = truth.astype(np.int64) - f.astype(np.int64)
    assert gap.min() >= 0, name
    return dict(key=key, name=name, read=read, level=level, mean=float(f.mean()), exact=float((gap == 0).mean()),
                within1=float((gap <= 1).mean()), meangap=float(gap.mean()), maxgap=int(gap.max()),
                gaps=hist(gap))


def class_min(lab, y):
    """For each state, the smallest y among the states with the same label."""
    u, iv = np.unique(lab, return_inverse=True)
    mn = np.full(len(u), 99, dtype=np.int64)
    np.minimum.at(mn, iv, y)
    return mn[iv], len(u)


def grade(t, f, nz):
    """How often the turn that makes f smallest gets closer to HTR; ties share the credit evenly."""
    fn = np.stack([f[t.mv[m]] for m in range(9)], 1)
    tie = fn == fn.min(1, keepdims=True)
    return (tie & t.closer).sum(1) / tie.sum(1)


def ceiling(t, lab, sel):
    """An upper bound for any rule that sees only `lab`, at one distance taken on its own: per label, among the
    states selected, the single turn that is closer most often.  (A rule that reached it would have to know the
    distance as well.)"""
    u, iv = np.unique(lab[sel], return_inverse=True)
    tab = np.zeros((len(u), 9))
    for m in range(9):
        tab[:, m] = np.bincount(iv, weights=t.closer[sel, m], minlength=len(u))
    return float(tab.max(1).sum() / sel.sum())


def one_table(t, lab, nz):
    """The best rule that is one table on `lab`: per label, the single turn that is closer for the most states
    (all distances together).  Returns, per state, whether that turn gets closer."""
    u, iv = np.unique(lab, return_inverse=True)
    tab = np.zeros((len(u), 9))
    for m in range(9):
        tab[:, m] = np.bincount(iv, weights=(t.closer[:, m] & nz), minlength=len(u))
    best = tab.argmax(1)[iv]
    return t.closer[np.arange(N), best]


def walk(t, f, tiebreak):
    """Follow `f` down from every state (smallest f next, ties by `tiebreak`, then by turn order) until f is 0.
    Returns the share of states that end in HTR."""
    key = f.astype(np.float64) + 1e-3 * tiebreak
    fn = np.stack([key[t.mv[m]] for m in range(9)], 1)
    nxt = t.mv[fn.argmin(1), np.arange(N)]
    cur = np.arange(N)
    for _ in range(12):
        cur = np.where(f[cur] == 0, cur, nxt[cur])
    assert (f[cur] == 0).all()
    return float((t.d[cur] == 0).mean())


def main():
    t = T.load()
    R = {"N": N}
    d, q = t.d, t.q
    nz = d > 0

    # 1. distances
    R["hist_d"] = hist(d)
    R["hist_q"] = hist(q)
    R["hist_qtm"] = hist(t.qtm)
    R["mean_d"] = float(d.mean())
    R["mean_q"] = float(q.mean())
    joint = np.zeros((int(q.max()) + 1, int(d.max()) + 1), dtype=np.int64)
    np.add.at(joint, (q, d), 1)
    R["joint_q_d"] = joint.tolist()
    R["hist_dsolved"] = hist(t.dsolved)
    R["d_minus_dsolved"] = hist(t.dsolved.astype(int) - d)

    # 2. all good
    good = t.dg == 0
    fake = good & nz
    R["allgood"] = dict(n=int(good.sum()), htr=int((good & ~nz).sum()), fake=int(fake.sum()),
                        fake_d=hist(d[fake]), fake_q=hist(q[fake]),
                        fake_odd=int((fake & (t.par == 1)).sum()), fake_even=int((fake & (t.par == 0)).sum()))

    # 3. types, classes
    pid = t.pid.astype(np.int64)
    R["patterns"] = int(len(np.unique(pid)))
    R["classes"] = int(len(np.unique(t.cls)))
    key = t.cls.astype(np.int64) * 16 + q
    uk, ck = np.unique(key, return_counts=True)
    sig = {}
    for k_, c_ in zip(uk, ck):
        sig.setdefault(int(k_ // 16), []).append((int(k_ % 16), int(c_)))
    sizes = Counter(t.cls.tolist())
    sigs = Counter(tuple((v, 6 * n // sizes[c]) for v, n in rows) for c, rows in sig.items())
    R["signatures"] = len(sigs)
    R["cases"] = N // 24

    # 4. floors
    shape = shape_names(t)
    six = np.unique(t.col[~nz, 1])
    goal48 = np.where(good & np.isin(t.col[:, 1], six))[0]
    assert len(goal48) == 48
    dtc = derive.distance(t.mv, goal48, np.zeros(48, dtype=np.int16), range(9)).astype(np.int64)
    np.save(os.path.join(c3.BIG, "d_goodcol.npy"), dtc.astype(np.int8))
    count_key = t.nT * 1000 + t.xs[:, 0] * 100 + t.xs[:, 1] * 10 + t.xs[:, 2]
    cf_d, n_count = class_min(count_key, d)
    cf_q, _ = class_min(count_key, q)
    wq = np.ceil(t.W / 4).astype(np.int64)
    R["floors_htm"] = [
        floor_row("tet", "corners back in their tetrads", "which corners are out", 1, t.dtet, d),
        floor_row("co1", "corners oriented on one axis (U/D)", "the U/D stickers", 4, t.dco[:, 1], d),
        floor_row("co3", "the same, best of the three axes", "all stickers, by axis", 4, t.dco.max(1), d),
        floor_row("count", "count table", "how many twisted, how many out per axis", 1, cf_d, d),
        floor_row("perm", "placement alone", "the pieces, twists ignored", 4, t.dp, d),
        floor_row("types", "types floor", "the type of every corner", 4, t.dg, d),
        floor_row("types_par", "types + parity", "types, and the parity", 4, t.de, d),
        floor_row("types_col", "types + D-colour corners", "types, and where the D-colour corners sit", 4, dtc, d),
        floor_row("both", "the larger of the last two", "types, parity, D-colour corners", 4,
                  np.maximum(t.de, dtc), d),
    ]
    R["floors_qt"] = [
        floor_row("weight", "weight / 4", "how many out, how many twisted", 1, wq, q),
        floor_row("count", "count table", "how many twisted, how many out per axis", 1, cf_q, q),
        floor_row("perm", "twist flat, read the subset", "an HTR subset read", 3, t.qp, q),
        floor_row("types", "types floor", "the type of every corner", 4, t.qg, q),
        floor_row("types_par", "types + parity", "types, and the parity", 4, t.qe, q),
        floor_row("types_perm", "types + parity, and the subset read", "all of the above", 4,
                  np.maximum(t.qe, t.qp), q),
    ]

    # 5. count table with witnesses
    rows = []
    for key_ in np.unique(count_key):
        m = count_key == key_
        idx = np.where(m)[0]
        # a state that meets the move floor (and one that meets the quarter-turn floor), with the shortest scramble
        w = idx[np.lexsort((idx, t.dsolved[idx], d[idx]))[0]]
        wq_ = idx[np.lexsort((idx, t.dsolved[idx], q[idx]))[0]]
        sol = descend(t, int(w), d)
        rows.append(dict(twisted=int(key_ // 1000), out=[int(key_ // 100 % 10), int(key_ // 10 % 10), int(key_ % 10)],
                         states=int(m.sum()), share=float(m.mean()), floor_d=int(d[idx].min()),
                         floor_q=int(q[idx].min()), mean_d=float(d[idx].mean()), mean_q=float(q[idx].mean()),
                         max_d=int(d[idx].max()), witness=scramble(t, int(w)), witness_kinds=kinds_text(t.kinds[w]),
                         witness_sol=c3.show(sol), witness_q=scramble(t, int(wq_)),
                         witness_q_sol=c3.show(descend(t, int(wq_), q_table(t)))))
    R["count_table"] = rows
    R["count_classes"] = n_count

    # 6. which turn gets closer, by distance
    def ahead(f, depth):
        """The smallest f within `depth` turns: what a solver sees who looks that far for the best weight."""
        best = f.astype(np.int16)
        for _ in range(depth - 1):
            best = np.minimum(best, np.stack([best[t.mv[m]] for m in range(9)], 0).min(0))
        return best

    look2 = ahead(t.W, 2)
    look3 = ahead(t.W, 3)
    g = dict(types=grade(t, t.dg, nz), types_par=grade(t, t.de, nz), types_col=grade(t, dtc, nz),
             look2=grade(t, look2, nz), look3=grade(t, look3, nz),
             both=grade(t, np.maximum(t.de, dtc), nz), weight=grade(t, t.W, nz), perm=grade(t, t.dp, nz),
             co3=grade(t, t.dco.min(1), nz), staged=grade(t, t.staged.min(1), nz))
    labs = dict(c_types=pid, c_types_par=pid * 2 + t.par, c_types_col=pid * 128 + t.col[:, 1],
                c_count=count_key.astype(np.int64))
    tables = {k_: one_table(t, lab, nz) for k_, lab in labs.items()}
    ncl = t.closer.sum(1)
    moves = []
    for dd in list(range(1, int(d.max()) + 1)) + [0]:
        sel = nz if dd == 0 else d == dd
        row = dict(d=dd, states=int(sel.sum()), share=float(sel.mean()), closer=float(ncl[sel].mean()),
                   random=float((ncl[sel] / 9).mean()))
        for k_, v in g.items():
            row[k_] = float(v[sel].mean())
        for k_, lab in labs.items():
            row["t" + k_[1:]] = float(tables[k_][sel].mean())
            if dd:
                row[k_] = ceiling(t, lab, sel)
        moves.append(row)
    # the bound for all states: each distance on its own, then weighted (the last row is "all states")
    for k_ in labs:
        moves[-1][k_] = sum(r[k_] * r["states"] for r in moves[:-1]) / moves[-1]["states"]
    R["moves"] = moves
    R["closer_hist"] = hist(ncl[nz])

    # 7. where a rule ends that follows a floor down
    tb = np.zeros(N)       # ties by turn order only: the rule sees nothing but its reads
    R["walk"] = dict(types=walk(t, t.dg, tb), types_par=walk(t, t.de, tb), types_col=walk(t, dtc, tb))

    # 8. the colour read
    col_classes = {}
    for bits in np.unique(t.col[:, 1]):
        col_classes[int(bits)] = colour_text(int(bits))
    R["colour"] = dict(pictures=len(col_classes), six=[colour_text(int(b)) for b in six],
                       types_col_par=int(len(np.unique((pid * 128 + t.col[:, 1]) * 2 + t.par))),
                       types_two=int(len(np.unique((pid * 128 + t.col[:, 1]) * 128 + t.col[:, 2]))),
                       good_six=int((good & np.isin(t.col[:, 1], six)).sum()),
                       good_six_even=int((good & np.isin(t.col[:, 1], six) & (t.par == 0)).sum()))
    # does (types, D colours, parity) fix d and q?  and (types, parity) alone, (types) alone: how often
    for name, lab in (("types", pid), ("types_par", pid * 2 + t.par),
                      ("types_col", pid * 128 + t.col[:, 1]),
                      ("types_col_par", (pid * 128 + t.col[:, 1]) * 2 + t.par)):
        u, iv = np.unique(lab, return_inverse=True)
        for tn, y in (("d", d), ("q", q)):
            tab = np.zeros((len(u), int(y.max()) + 1), dtype=np.int64)
            np.add.at(tab, (iv, y), 1)
            R[f"fix_{name}_{tn}"] = dict(classes=len(u), mode=float(tab.max(1).sum() / N),
                                         fixed=float(tab.sum(1)[tab.max(1) == tab.sum(1)].sum() / N))
    R["baseline"] = dict(d_mode=int(np.argmax(R["hist_d"])), d_share=max(R["hist_d"]) / N,
                         q_mode=int(np.argmax(R["hist_q"])), q_share=max(R["hist_q"]) / N)

    # 9. DR corners inside 3D (U/D axis)
    dr = np.where(t.dco[:, 1] == 0)[0]
    ddr = t.ddr[dr, 1].astype(int)
    qdr = t.qdr[dr, 1].astype(int)
    assert (qdr == q[dr]).all()
    sub = {}
    for s_, a_, b_, c_ in zip(dr, ddr, qdr, d[dr]):
        name = shape[s_].replace("6c", "2c") + str(b_)
        e = sub.setdefault(name, dict(states=0, dr=Counter(), all=Counter(), save=Counter()))
        e["states"] += 1
        e["dr"][int(a_)] += 1
        e["all"][int(c_)] += 1
        e["save"][int(a_ - c_)] += 1
    R["dr"] = dict(states=len(dr), hist_ddr=hist(ddr), hist_d=hist(d[dr]), hist_q=hist(qdr),
                   save=hist(ddr - d[dr]), qt_same=bool((qdr == q[dr]).all()),
                   subsets={k_: dict(states=v["states"], dr_min=min(v["dr"]), dr_max=max(v["dr"]),
                                     all_min=min(v["all"]), all_max=max(v["all"]),
                                     dr_mean=sum(a * b for a, b in v["dr"].items()) / v["states"],
                                     all_mean=sum(a * b for a, b in v["all"].items()) / v["states"],
                                     save=[v["save"].get(i, 0) for i in range(3)]) for k_, v in sorted(sub.items())})
    # when leaving DR is shorter: how many more quarter turns the shortest solutions use than the subset number
    qopt = c3.u8("qopt_htr")[dr].astype(int)
    shorter = (ddr - d[dr]) > 0
    R["dr"]["shorter_states"] = int(shorter.sum())
    R["dr"]["shorter_extra_q"] = hist((qopt - q[dr])[shorter], 5)
    # a DR case where leaving DR saves 2
    w = dr[np.argmax(ddr - d[dr])]
    R["dr"]["witness_save2"] = dict(scramble=scramble(t, int(w)), dr_only=int(t.ddr[w, 1]), all=int(d[w]),
                                    sol=c3.show(descend(t, int(w), d)), kinds=kinds_text(t.kinds[w]))
    # the three axes give the same subset number for a placement
    same3 = True
    for a in range(3):
        s_ = np.where(t.dco[:, a] == 0)[0]
        same3 &= bool((t.qdr[s_, a] == t.qp[s_]).all()) and len(np.unique(s_ // 729)) == 5040
    R["perm"] = dict(same_on_three_axes=same3, hist_q=hist(t.qp[::729]), hist_d=hist(t.dp[::729]),
                     surcharge=hist(q.astype(int) - t.qp), surcharge_d=hist(d.astype(int) - t.dp))
    sur = q.astype(int) - t.qp
    R["perm"]["surcharge_by_twisted"] = {int(k_): hist(sur[t.nT == k_], 9) for k_ in range(8)}
    R["perm"]["surcharge_mean_by_twisted"] = {int(k_): float(sur[t.nT == k_].mean()) for k_ in range(8)}

    # 10. the staged route: optimal orientation on an axis, then the best DR-only finish
    st = t.staged.astype(int)
    R["staged"] = dict(fixed=hist(st[:, 1] - d), best=hist(st.min(1) - d), mean_fixed=float(st[:, 1].mean()),
                       mean_best=float(st.min(1).mean()))
    amin = t.dco.argmin(1)
    pick = st[np.arange(N), amin]
    R["staged"]["shortest_co"] = hist(pick - d)
    R["staged"]["mean_shortest_co"] = float(pick.mean())

    # 11. corner orientation on one axis
    mis = ((t.kinds != 0) & (t.kinds != 4)).sum(1)       # misoriented for U/D
    R["co"] = dict(hist=hist(t.dco[:, 1]), mean=float(t.dco[:, 1].mean()),
                   best3=hist(t.dco.min(1)), mean_best3=float(t.dco.min(1).mean()),
                   by_mis={int(k_): hist(t.dco[mis == k_, 1], 7) for k_ in np.unique(mis)})

    # 12. by tetrad shape and by twisted count
    by_shape = {}
    for name in ("0c", "2c", "4a", "4b", "6c"):
        m = shape == name
        by_shape[name] = dict(states=int(m.sum()), share=float(m.mean()), min_d=int(d[m].min()), mean_d=float(d[m].mean()),
                              min_q=int(q[m].min()), mean_q=float(q[m].mean()), hist_q=hist(q[m], 9), hist_d=hist(d[m], 11),
                              tet=int(t.dtet[m].max()))
    R["by_shape"] = by_shape
    R["by_twisted"] = {int(k_): dict(states=int((t.nT == k_).sum()), min_d=int(d[t.nT == k_].min()),
                                     mean_d=float(d[t.nT == k_].mean()), min_q=int(q[t.nT == k_].min()),
                                     mean_q=float(q[t.nT == k_].mean())) for k_ in range(8)}
    # twisted corners only (no out corner)
    only_tw = {}
    for k_ in range(1, 8):
        m = (t.nT == k_) & (t.nX == 0)
        if m.any():
            i = np.where(m)[0]
            w = i[np.lexsort((i, t.dsolved[i], d[i]))[0]]
            only_tw[k_] = dict(states=int(m.sum()), min_d=int(d[i].min()), min_q=int(q[i].min()),
                               mean_d=float(d[i].mean()), mean_q=float(q[i].mean()), max_d=int(d[i].max()),
                               witness=scramble(t, int(w)), sol=c3.show(descend(t, int(w), d)))
    R["only_twisted"] = only_tw
    # four twisted corners and nothing out: the best quarter-turn count of each type pattern
    m4 = (t.nT == 4) & (t.nX == 0)
    _, first4 = np.unique(pid[m4], return_index=True)
    R["twisted4_patterns_by_q"] = hist(t.qg[m4][first4], 7)

    # 13. the quarter-turn count against the types floor
    R["q_minus_types"] = hist(q.astype(int) - t.qg)
    R["d_minus_types"] = hist(d.astype(int) - t.dg)
    R["q_types_hist"] = hist(t.qg)
    R["d_types_hist"] = hist(t.dg)
    R["types_q_classes"] = hist([int(t.qg[np.where(t.cls == c)[0][0]]) for c in np.unique(t.cls)])
    R["types_d_patterns"] = hist(t.dg[np.unique(pid, return_index=True)[1]])

    # 14. moves against quarter turns
    R["mean_d_by_q"] = [float(d[q == k_].mean()) for k_ in range(int(q.max()) + 1)]
    R["min_d_by_q"] = [int(d[q == k_].min()) for k_ in range(int(q.max()) + 1)]
    R["max_d_by_q"] = [int(d[q == k_].max()) for k_ in range(int(q.max()) + 1)]

    with open(os.path.join(OUT, "numbers.json"), "w") as fh:
        json.dump(R, fh, indent=1)
    print("numbers.json written:", len(R), "entries")


_Q = {}


def q_table(t):
    """A table that goes down by one along a solution with the fewest quarter turns: 16 x quarter turns to HTR
    plus the half turns still needed inside that level."""
    if "t" not in _Q:
        # inside a level of q, count the half turns to the nearest state with a quarter turn down
        q = t.q.astype(np.int64)
        inner = np.full(N, 99, dtype=np.int64)
        inner[q == 0] = 0
        down = np.zeros(N, dtype=bool)
        for m in range(9):
            if m % 3 != 1:
                down |= q[t.mv[m]] < q
        inner[down] = 0
        changed = True
        while changed:
            changed = False
            for m in (1, 4, 7):
                nb = t.mv[m]
                cand = np.where(q[nb] == q, inner[nb] + 1, 99)
                better = cand < inner
                if better.any():
                    inner[better] = cand[better]
                    changed = True
        # a quarter turn down costs 1, each half turn inside a level 1: the table falls by 1 along the way
        _Q["t"] = q * 16 + inner + (q > 0)
    return _Q["t"]


if __name__ == "__main__":
    main()

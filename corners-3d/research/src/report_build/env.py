"""Names the write-up sources can use in {= expression =} and {{ table() }} placeholders.  Every number comes
from research/out/numbers.json, extra.json, figdata.json and examples.json (written by analysis.py, extra.py,
figures.py and examples.py); nothing is typed by hand."""
import json
import os

B = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(B, "..", "..", "out")


def load(name):
    with open(os.path.join(OUT, name + ".json")) as fh:
        return json.load(fh)


R = load("numbers")
X = load("extra")
F = load("figdata")
E = load("examples")
FIG = load("figures")
N = R["N"]


def n(x):
    return f"{x:,}"


def pc(x, digits=1):
    """A share as a percentage, rounded once from full precision."""
    return f"{100 * x:.{digits}f}%"


def f2(x, digits=2):
    return f"{x:.{digits}f}"


def share(count, total=None, digits=1):
    return pc(count / (total or N), digits)


def fig(name, caption):
    return f'<figure>\n{FIG[name]}\n<figcaption>{caption}</figcaption>\n</figure>'


def table(head, rows, align=None):
    align = align or ["---"] + ["---:"] * (len(head) - 1)
    out = ["| " + " | ".join(head) + " |", "|" + "|".join(align) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def code(s):
    return f"`{s}`" if s else "(nothing)"


# ---------- section 3: distances ----------

def t_moves():
    hd, hn = R["hist_d"], X["niss"]["hist"]
    rows = []
    cum = cumn = 0
    for d in range(len(hd)):
        cum += hd[d]
        nn = hn[d] if d < len(hn) else 0
        cumn += nn
        rows.append([d, n(hd[d]), share(hd[d], digits=2), share(cum, digits=2), n(nn), share(nn, digits=2), share(cumn, digits=2)])
    return table(["Moves to HTR", "States, one side", "Share", "This or fewer", "States, with NISS", "Share", "This or fewer"], rows)


def t_quarters():
    hq = R["hist_q"]
    rows = []
    for q in range(len(hq)):
        rows.append([q, n(hq[q]), share(hq[q], digits=2), R["min_d_by_q"][q], f2(R["mean_d_by_q"][q]), R["max_d_by_q"][q],
                     f2(X["niss"]["mean_by_q"][q])])
    return table(["Quarter turns to HTR", "States", "Share", "Fewest moves", "Mean moves", "Most moves", "Mean moves with NISS"], rows)


# ---------- section 4: types ----------

def t_rule():
    r = F["rule"]
    rows = []
    for face, axis in (("R", "R/L"), ("U", "U/D"), ("F", "F/B")):
        rows.append([f"{face} or {face}'", f"out, only {axis} oriented",
                     "out, " + {"out-r": "only R/L", "out-u": "only U/D", "out-f": "only F/B"}[r[f"{face} tw-FB"]] + " oriented",
                     "out, " + {"out-r": "only R/L", "out-u": "only U/D", "out-f": "only F/B"}[r[f"{face} tw-RL"]] + " oriented"])
    return table(["Quarter turn", "A good corner becomes", "Twisted, U/D sticker on F/B, becomes", "Twisted, U/D sticker on R/L, becomes"],
                 rows, ["---", "---", "---", "---"])


# ---------- section 5: the three reads ----------

def t_reads():
    rows = [
        ["the types", n(R["fix_types_d"]["classes"]), 144, "1 in 6", pc(R["fix_types_d"]["fixed"]), pc(R["fix_types_q"]["fixed"])],
        ["types + parity", n(R["fix_types_par_d"]["classes"]), 72, "1 in 3 at best", pc(R["fix_types_par_d"]["fixed"]), pc(R["fix_types_par_q"]["fixed"])],
        ["types + D-colour corners", n(R["fix_types_col_d"]["classes"]), 8, "1 in 2 at best", pc(R["fix_types_col_d"]["fixed"]), pc(R["fix_types_col_q"]["fixed"])],
        ["types + D-colour corners + parity", n(R["fix_types_col_par_d"]["classes"]), 4, "always", pc(R["fix_types_col_par_d"]["fixed"]), pc(R["fix_types_col_par_q"]["fixed"])],
    ]
    return table(["What you read", "Different things you can see", "States that show the same", "In HTR once every corner is good",
                  "States whose moves to HTR it determines", "States whose quarter turns it determines"], rows)


def t_fake():
    a = R["allgood"]
    rows = [["HTR", a["htr"], "even", 0, 0],
            ["fake HTR, a swap away", a["fake_odd"], "odd", 3, 9],
            ["fake HTR, a 3-cycle away", a["fake_even"], "even", 4, 9]]
    return table(["All corners good, and", "States", "Parity", "Quarter turns to HTR", "Moves to HTR"], rows)


# ---------- section 6: floors ----------

LEVEL = {1: "at a glance", 2: "tracing", 3: "a subset read", 4: "table or search"}


def floor_by_key(key, qt=False):
    return next(r for r in R["floors_qt" if qt else "floors_htm"] if r["key"] == key)


def t_floors():
    order = ["tet", "count", "co1", "co3", "perm", "types", "types_par", "types_col", "both"]
    how = {"tet": "at a glance", "count": "at a glance", "co1": "table", "co3": "table", "perm": "table",
           "types": "table, or a search", "types_par": "table, or a search", "types_col": "table, or a search",
           "both": "table, or a search"}
    rows = []
    for k in order:
        r = floor_by_key(k)
        rows.append([r["name"], r["read"], how[k], f2(r["mean"]), pc(r["exact"]), pc(r["within1"]), r["maxgap"]])
    rows.append(["the true distance", "everything", "computer", f2(R["mean_d"]), "100.0%", "100.0%", 0])
    return table(["Floor", "What it reads", "How you get it", "Mean floor (moves)", "States where it is exact", "Exact or 1 short", "Most it is short by"],
                 rows, ["---", "---", "---", "---:", "---:", "---:", "---:"])


def t_floors_qt():
    order = ["weight", "count", "perm", "types", "types_par", "types_perm"]
    how = {"weight": "at a glance", "count": "at a glance", "perm": "a subset read", "types": "table, or a search",
           "types_par": "table, or a search", "types_perm": "table, or a search"}
    rows = []
    for k in order:
        r = floor_by_key(k, True)
        rows.append([r["name"], how[k], f2(r["mean"]), pc(r["exact"]), pc(r["within1"]), r["maxgap"]])
    rows.append(["the true count", "computer", f2(R["mean_q"]), "100.0%", "100.0%", 0])
    return table(["Floor", "How you get it", "Mean floor (quarter turns)", "States where it is exact", "Exact or 1 short", "Most it is short by"],
                 rows, ["---", "---", "---:", "---:", "---:", "---:"])


def t_floors_niss():
    rows = []
    for r in X["niss"]["floors"]:
        rows.append([r["name"], f2(r["mean"]), pc(r["exact"]), pc(r["within1"]), r["maxgap"]])
    rows.append(["the true distance with NISS", f2(X["niss"]["mean"]), "100.0%", "100.0%", 0])
    return table(["Floor that holds with NISS", "Mean floor (moves)", "States where it is exact", "Exact or 1 short", "Most it is short by"], rows)


def out_text(o):
    o = [x for x in o if x]
    return " + ".join(str(x) for x in o) if o else "0"


def t_count():
    rows = []
    for r in R["count_table"]:
        key = str(r["twisted"] * 1000 + r["out"][0] * 100 + r["out"][1] * 10 + r["out"][2])
        nf = X["niss"]["count_floor"][key]
        rows.append([r["twisted"], out_text(r["out"]), pc(r["share"], 2), r["floor_d"], nf["floor"], r["floor_q"],
                     code(r["witness"])])
    return table(["Twisted", "Out, by axis", "Share of states", "Floor, moves", "Floor, moves with NISS", "Floor, quarter turns",
                  "A scramble that meets the move floor"], rows, ["---:", "---", "---:", "---:", "---:", "---:", "---"])


def t_only_twisted():
    rows = []
    for k, r in sorted(R["only_twisted"].items(), key=lambda kv: int(kv[0])):
        rows.append([k, n(r["states"]), r["min_d"], f2(r["mean_d"]), r["max_d"], r["min_q"], code(r["witness"]), code(r["sol"])])
    return table(["Twisted corners, nothing out", "States", "Fewest moves", "Mean moves", "Most moves", "Fewest quarter turns",
                  "A scramble at the fewest", "Its solution to HTR"], rows, ["---:"] * 6 + ["---", "---"])


def binom_tail(k, n_, p):
    """The chance of k or more successes in n_ tries."""
    from math import comb
    return sum(comb(n_, i) * p ** i * (1 - p) ** (n_ - i) for i in range(k, n_ + 1))


def crow(twisted, out):
    """A row of the count table."""
    return next(r for r in R["count_table"] if r["twisted"] == twisted and r["out"] == out)


def lean_text():
    path = os.path.join(B, "lean.md")
    return open(path).read().strip() if os.path.exists(path) else "(the Lean summary goes here)"


# ---------- section 7: which turn ----------

def moves_row(d):
    return next(r for r in R["moves"] if r["d"] == d)


def t_moves_rules():
    rows = []
    for r in R["moves"]:
        name = "all states" if r["d"] == 0 else r["d"]
        rows.append([name, pc(r["share"], 2), f2(r["closer"]), pc(r["random"]), pc(r["types"]), pc(r["types_par"]),
                     pc(r["types_col"]), pc(r["both"])])
    return table(["Moves to HTR", "Share of states", "Turns that get closer (of 9)", "A random turn", "Follow the types floor",
                  "Types + parity floor", "Types + D-colour floor", "The larger of those two"], rows)


def t_thumb():
    rows = []
    for r in R["moves"]:
        name = "all states" if r["d"] == 0 else r["d"]
        rows.append([name, pc(r["random"]), pc(r["weight"]), pc(r["look2"]), pc(r["look3"]), pc(r["co3"])])
    return table(["Moves to HTR", "A random turn", "Lowest weight after the turn", "Lowest weight within 2 turns",
                  "Lowest weight within 3 turns", "Shortest CO on any axis after the turn"], rows)


def t_moves_table():
    rows = []
    for r in R["moves"]:
        name = "all states" if r["d"] == 0 else r["d"]
        rows.append([name, pc(r["t_count"]), pc(r["t_types"]), pc(r["t_types_par"]), pc(r["t_types_col"])])
    return table(["Moves to HTR", "Best table on the counts", "Best table on the types", "On types + parity",
                  "On types + D-colour corners"], rows)


def t_moves_ceil():
    rows = []
    for r in R["moves"]:
        name = "all states" if r["d"] == 0 else r["d"]
        rows.append([name, pc(r["c_count"]), pc(r["c_types"]), pc(r["c_types_par"]), pc(r["c_types_col"]), "100.0%"])
    return table(["Moves to HTR", "Bound on the counts", "Bound on the types", "On types + parity",
                  "On types + D-colour corners", "On all three"], rows)


def t_moves_niss():
    rows = []
    for r in X["niss"]["moves"]:
        rows.append([r["d"], pc(r["share"], 2), f2(r["closer"]), pc(r["random"]), pc(r["types"]), pc(r["types_par"])])
    return table(["Moves to HTR with NISS", "Share of states", "Turns that get closer (of 18)", "A random turn",
                  "Follow the types floor (both sides)", "Types + parity floor (both sides)"], rows)


# ---------- section 8: quarter turns ----------

def t_surcharge():
    s = R["perm"]["surcharge"]
    rows = [[k, n(s[k]), share(s[k], digits=2)] for k in range(0, len(s), 2)]
    return table(["Extra quarter turns the twist costs", "States", "Share"], rows)


def t_surcharge_tw():
    rows = []
    for k in range(8):
        h = R["perm"]["surcharge_by_twisted"][str(k)]
        tot = sum(h)
        rows.append([k, n(tot), pc(h[0] / tot), pc(h[2] / tot), pc(sum(h[4:]) / tot), f2(R["perm"]["surcharge_mean_by_twisted"][str(k)])])
    return table(["Twisted corners", "States", "Costs nothing", "Costs 2", "Costs 4 or more", "Mean cost (quarter turns)"], rows)


def t_subset_hist():
    h = R["perm"]["hist_q"]
    rows = [[k, n(h[k]), h[k] // 24, share(h[k], 5040)] for k in range(len(h))]
    return table(["Subset number", "Placements (of 5,040)", "In cases of 24", "Share"], rows)


def t_low():
    rows = []
    for c in F["cases"]:
        for q in ("1", "2"):
            if q in c["witness"]:
                w = c["witness"][q]
                name = out_text(c["out"]) + " out" + (f", {c['twisted']} twisted" if c["twisted"] else "") if any(c["out"]) else f"{c['twisted']} twisted"
                if c["shape"] in ("4a", "4b") and not c["twisted"]:
                    name += f" ({c['shape']})"
                rows.append([q, name, c["patterns"], f"{c['cosets'][int(q)]} of 6", code(w["scramble"]), f"`{w['kinds']}`", w["d"]])
    rows.sort(key=lambda r: (r[0], r[1]))
    return table(["Quarter turns", "What you count", "Type patterns", "Of 6 look-alikes, this close", "A scramble", "Its types", "Its moves to HTR"],
                 rows, ["---:", "---", "---:", "---:", "---", "---", "---:"])


# ---------- section 9: DR ----------

SUBSETS = ["0c0", "4a1", "4a2", "4b2", "0c3", "2c3", "4a3", "4b3", "0c4", "2c4", "4a4", "4b4", "2c5", "4b5"]


def t_dr():
    rows = []
    for name in SUBSETS:
        s = X["dr_subsets"][name]
        rows.append([name, s["cases"], s["lin_min"], s["lin_max"], s["all_min"], s["all_max"], s["saved"][1] // 24, s["saved"][2] // 24])
    return table(["Subset", "Cases (of 210)", "DR turns: fewest", "DR turns: most", "All turns: fewest", "All turns: most",
                  "Cases 1 shorter", "Cases 2 shorter"], rows)


def t_dr_niss():
    rows = []
    for name in SUBSETS:
        s = X["dr_subsets"][name]
        rows.append([name, s["niss_min"], s["niss_max"], f2(s["niss_mean"]), s["allniss_min"], s["allniss_max"], f2(s["allniss_mean"])])
    return table(["Subset", "DR turns + NISS: fewest", "Most", "Mean", "All turns + NISS: fewest", "Most", "Mean"], rows)


def t_staged():
    fx, bs = R["staged"]["fixed"], R["staged"]["best"]
    rows = []
    for k in range(max(len(fx), len(bs))):
        a = fx[k] if k < len(fx) else 0
        b = bs[k] if k < len(bs) else 0
        rows.append([k, share(a), share(b)])
    return table(["Moves longer than the optimal", "Orient on U/D first", "Orient on the best of the three axes first"], rows)


def t_co():
    by = R["co"]["by_mis"]
    rows = []
    for k in sorted(by, key=int):
        h = by[k]
        tot = sum(h)
        rows.append([k, share(tot)] + [pc(x / tot, 0) for x in h])
    return table(["Corners misoriented for the axis", "Share of states"] + [f"{i} moves" for i in range(7)], rows)


def t_co_hist():
    h, b = R["co"]["hist"], R["co"]["best3"]
    rows = [[k, h[k] // 5040, share(h[k]), share(b[k])] for k in range(len(h))]
    return table(["Moves to orient", "Twist cases (of 729)", "Share, one axis", "Share, best of three axes"], rows)


def t_shape():
    rows = []
    for name in ("0c", "4a", "4b", "2c", "6c"):
        s = R["by_shape"][name]
        rows.append([name, pc(s["share"], 2), F["shape"][name]["qt"], s["min_q"], f2(s["mean_q"]), s["min_d"], f2(s["mean_d"])])
    return table(["Out corners", "Share of states", "Quarter turns to put them back", "Fewest quarter turns to HTR",
                  "Mean quarter turns", "Fewest moves to HTR", "Mean moves"], rows)


def t_cycle():
    rows = []
    for k, v in X["cycle_type"].items():
        tot = sum(v.values())
        vals = sorted(int(a) for a in v)
        rows.append([k, tot] + [v.get(str(q), 0) for q in range(6)])
    rows.sort(key=lambda r: -r[1])
    return table(["Cycles of the placement", "Placements"] + [f"{q} qt" for q in range(6)], rows)


# ---------- examples page ----------

def t_catalogue():
    rows = []
    for r in E["catalogue"]:
        if r["floor"] == 0:
            continue
        cnt = (out_text(r["out"]) + " out" if any(r["out"]) else "") + (", " if any(r["out"]) and r["twisted"] else "") + \
              (f"{r['twisted']} twisted" if r["twisted"] else "")
        if r["shape"] in ("4a", "4b"):
            cnt += f" ({r['shape']})"
        rows.append([r["floor"], r["quarter"], f"`{r['kinds']}`", cnt, r["patterns"], code(r["scramble"]), code(r["ways"][0])])
    return table(["Moves to all good", "Quarter turns in them", "Types", "What you count", "Patterns alike by symmetry", "A scramble", "A way to all good"],
                 rows, ["---:", "---:", "---", "---", "---:", "---", "---"])


def random_blocks():
    out = []
    for i, e in enumerate(E["random"], 1):
        o = e["out"]
        counts = f"{e['twisted']} twisted, out {o[0]} on R/L, {o[1]} on U/D, {o[2]} on F/B"
        head = (f"**{i}.** `{e['scramble']}`\n\n"
                f"Types `{e['kinds']}`. {counts}. Out corners {e['shape']}, D-colour corners {e['colour']}, parity {e['parity']}.\n\n"
                f"Floors: count table {e['floor_count']} moves ({e['floor_count_q']} qt), types {e['floor_types']}, types + parity {e['floor_par']}. "
                f"Subset number of the placement: {e['subset']}.")
        closer = ", ".join(e["closer"])
        ends = "HTR" if e["types_solution_ends"] == 0 else f"a fake HTR, {e['types_solution_ends']} from HTR"
        ans = (f"{e['d']} moves, {e['q']} quarter turns ({e['niss']} moves with NISS). Closer turns: {closer}. "
               f"One of {e['n_solutions']}{'+' if e['n_solutions'] >= 99 else ''} shortest ways: `{e['solution']}`. "
               f"The first shortest way to all good, `{e['types_solution']}`, ends in {ends}.")
        out.append(head + f"\n\n<details><summary>Answer</summary>\n\n{ans}\n\n</details>")
    return "\n\n".join(out)


def t_dr_examples():
    rows = []
    for r in E["dr"]:
        if r["subset"] == "0c0":
            continue
        rows.append([r["subset"], code(r["scramble"]), r["dr_only"], code(r["dr_solution"]), r["all"], code(r["solution"]), r["niss"]])
    return table(["Subset", "Scramble", "DR turns", "A shortest way in DR turns", "All turns", "A shortest way", "With NISS"],
                 rows, ["---", "---", "---:", "---", "---:", "---", "---:"])


# ---------- single states, for the worked examples ----------

import sys  # noqa: E402

sys.path.insert(0, os.path.join(B, ".."))
import numpy as np  # noqa: E402
import c3  # noqa: E402
from core import T, kinds_text, descend, all_shortest, quarters  # noqa: E402

from examples import colour_class  # noqa: E402

_T = T.load()
_DN = np.load(os.path.join(c3.BIG, "d_niss.npy"))
_CC = colour_class(_T)


def S(scr):
    """Facts about the state a scramble (R, U, F turns) makes."""
    t = _T
    s = c3.apply(t.mv, 0, scr)
    sol = descend(t, s, t.d)
    tsol = descend(t, s, t.dg)
    return dict(kinds=kinds_text(t.kinds[s]), d=int(t.d[s]), q=int(t.q[s]), niss=int(_DN[s]), types=int(t.dg[s]),
                types_q=int(t.qg[s]), par=int(t.de[s]), subset=int(t.qp[s]), parity="odd" if t.par[s] else "even",
                twisted=int(t.nT[s]), out=[int(x) for x in t.xa[s]], closer=", ".join(c3.MOVES[m] for m in range(9) if t.closer[s, m]),
                sol=c3.show(sol), sol_q=quarters(sol), tsol=c3.show(tsol), tsol_ends=int(t.d[c3.apply(t.mv, s, tsol)]),
                n_sol=len(all_shortest(t, s, t.d, limit=99)), ddr=int(t.ddr[s, 1]), state=s, colour=str(_CC[s]))


def after(scr, seq):
    """Moves to HTR after doing `seq` on the state `scr` makes."""
    return int(_T.d[c3.apply(_T.mv, c3.apply(_T.mv, 0, scr), seq)])


def far(which):
    """The scramble of a state at the largest number of quarter turns ('q'), of moves ('d'), or of moves with NISS
    ('niss'): the one with the shortest scramble."""
    t = _T
    table = {"q": t.q, "d": t.d, "niss": _DN}[which]
    idx = np.where(table == table.max())[0]
    from core import scramble
    return scramble(t, int(idx[np.lexsort((idx, t.dsolved[idx]))[0]]))


def quarters_of(seq):
    """How many of the turns of a sequence are quarter turns."""
    return sum(1 for m in seq.split() if not m.endswith("2"))


def rnd(i):
    return E["random"][i]


def first_random(**want):
    """The first of the 200 random states with the given values, e.g. first_random(d=5)."""
    return next(e for e in E["random"] if all(e[k] == v for k, v in want.items()))


def dr_row(subset, which=0):
    return [r for r in E["dr"] if r["subset"] == subset][which]


def is_htr(seq):
    return bool(_T.d[c3.apply(_T.mv, 0, seq)] == 0)


# The claims table says "Confirmed" in words: refuse to build if a check behind one of them is not true.
assert X["eight"]["r_like"] and X["eight"]["l_like"] and all(X["eight"]["u_like"])
assert X["eight"]["trangium"] and X["eight"]["trangium_twists"]
assert X["eight"]["max_htr"] == 11 and len(R["dr"]["hist_ddr"]) - 1 == 11
assert X["eight"]["wen_second_ok"] and X["eight"]["torchlight_11_ok"] and X["eight"]["wen_true"] == 12
assert all(X["six_paths"]["ok"]) and set(X["six_paths"]["quarters"]) == {4} and X["six_paths"]["q"] == 4
assert X["lemma1"]["match"] and X["lemma1"]["all_htr"] and X["lemma1"]["states"] == 4
assert R["perm"]["same_on_three_axes"] and R["dr"]["qt_same"]
assert R["hist_q"] == [24, 432, 6768, 86184, 780048, 1708416, 1049856, 42048, 384]           # Jules Porteners
assert R["perm"]["hist_q"] == [24, 144, 720, 1416, 1776, 960]                               # FakeMMAP
assert [X["dr_subsets"][k]["cases"] for k in ("0c0", "0c3", "0c4", "4a1", "4a2", "4a3", "4a4", "4b2", "4b3", "4b4", "4b5",
                                              "2c3", "2c4", "2c5")] == [1, 3, 2, 6, 6, 12, 12, 24, 12, 12, 24, 32, 48, 16]  # Shota
assert X["dr_niss_min_by_q"][1:] == [1, 2, 4, 6, 8] and X["dr_subsets"]["0c3"]["niss_min"] == 6   # Joba, Zagros
assert R["allgood"]["fake_d"][9] == R["allgood"]["fake"] == 120 and R["walk"]["types"] == 1 / 6
assert set(X["klein"]) == {"(1, 1, 1, 1) q0", "(2, 2) q0", "(3, 1) q4", "(2, 1, 1) q3", "(4,) q3"}   # torchlight

ENV = {k: v for k, v in globals().items() if not k.startswith("_")}

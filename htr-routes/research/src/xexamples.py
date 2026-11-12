#!/usr/bin/env python3
"""report/EXAMPLES.md: 200 uniformly random DR states (the 10 first sampled states of each of the 20 most common
subset x edges), each with the subset's route checklist graded on it, one optimal finish for every class that works,
and the shortest DR-bounding reductions to 1q and 2q that lead to an optimal finish.  Answers folded away.

Every move sequence printed is replayed on the sticker model (sticker.py, built on is-dr-xs-worth-it's cube.py)
before the page is written; the page states how many checks and fails on any mismatch.

Inputs: out/checks/dist48.tsv (exact subset sizes), out/big/run1/states_<subset>.tsv and routes_<subset>.bin
(the main sample: which classes the route enumeration found per state, used as a cross-check), route_keys.tsv,
out/q2_checklist_budget.tsv (the checklists), out/big/bound.tsv (shortest reductions, cross-check), and two
`htrtools trace` runs (every optimal finish of each state with every NISS reading; then the finish used to write the
scramble).  usage: xexamples.py"""
import csv, os, sys, json, random, subprocess, hashlib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sticker
from sticker import do, SOLVED, inv_seq, QT, label

AMOUNT = {'': 1, '2': 2, "'": 3}
AXIS = {'U': 0, 'D': 0, 'R': 1, 'L': 1, 'F': 2, 'B': 2}
def simplify(seq):
    """Printed scrambles: each run of moves on one axis merged (`U2 D2 U` -> `U' D2`, `L2 R2 L2` -> `R2`), faces of an
    axis in the order U D, R L, F B, repeated until nothing changes."""
    toks = seq.split()
    while True:
        out, i = [], 0
        while i < len(toks):
            j = i
            while j < len(toks) and AXIS[toks[j][0]] == AXIS[toks[i][0]]:
                j += 1
            tot = collections.Counter()
            for m in toks[i:j]:
                tot[m[0]] += AMOUNT[m[1:]]
            for f in 'UDRLFB':
                a = tot[f] % 4
                if f in tot and a:
                    out.append(f + {1: '', 2: '2', 3: "'"}[a])
            i = j
        if out == toks:
            return ' '.join(out)
        toks = out
import common
from common import level_of, Routes, keys

R = common.R
OUT = common.OUT + '/'
PAGE = os.path.normpath(os.path.join(R, '..', 'report', 'EXAMPLES.md'))
TOOL = f'{R}/htrtools/target/release/htrtools'
EXACT = '/data/fmc/judging-a-dr/research/data/lean_exact_table.u8'
CAP = ['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=4G']
CACHE = '/data/fmc/tmp/htr_examples_cache'
ORDER = ['0c0', '2c5', '2c4', '0c3', '4a2', '4a1', '2c3', '0c4', '4c3', '4c4', '4b2', '4b5']
NPER, NSUB, NCLS, BUDGET = 10, 20, 5, 2
DRM = sticker.DRM
REPLAYED = [0]
MISMATCH = []


def check(ok, what):
    REPLAYED[0] += 1
    if not ok:
        MISMATCH.append(what)


def trace(lines, cap):
    os.makedirs(CACHE, exist_ok=True)
    h = hashlib.sha1(('\n'.join(lines) + str(cap)).encode()).hexdigest()[:16]
    p = f'{CACHE}/{h}.jsonl'
    if not os.path.exists(p):
        r = subprocess.run(CAP + [TOOL, 'trace', EXACT, str(cap)], input='\n'.join(lines) + '\n',
                           capture_output=True, text=True, check=True)
        open(p, 'w').write(r.stdout)
    return [json.loads(l) for l in open(p) if l.strip()]


def cls_txt(c):
    c = c[:-5] if c.endswith(' | ht') else c
    return f'`{c}`'


def nq(seq):
    return sum(1 for m in seq if m in QT)


# ------------------------------------------------------------------------------------- the states
size = collections.Counter()
for r in csv.DictReader(open(OUT + 'checks/dist48.tsv'), delimiter='\t'):
    size[r['subset']] += int(r['states'])
TOTAL = sum(size.values())
top = [s for s, _ in size.most_common(NSUB)]
top.sort(key=lambda s: (ORDER.index(s.split()[0]), int(s.split()[1][:-1])))

checklist = collections.defaultdict(list)
for r in csv.DictReader(open(OUT + 'q2_checklist_budget.tsv'), delimiter='\t'):
    if r['level'] == 'C' and r['target'] == 'opt' and r['budget'] == str(BUDGET) and int(r['step']) <= NCLS:
        checklist[r['group']].append((r['class'], float(r['cumulative'])))

bound = {}
for r in csv.DictReader(open(OUT + 'big/bound.tsv'), delimiter='\t'):
    if r['subset'] in top and int(r['idx']) < NPER:
        r1 = [int(c.split(':')[2]) for c in r['cells'].split(';') if c and c.split(':')[0] == '0']
        bound[(r['subset'], int(r['idx']))] = ((r['c'], r['e'], r['s']), min(r1) if r1 else 99)

states = []
for sub in top:
    rows = list(csv.DictReader(open(f"{common.RUN}/states_{common.fname(sub)}.tsv"), delimiter='\t'))[:NPER]
    rt = Routes(sub)
    K = keys()
    for r in rows:
        i = int(r['idx'])
        a, b = rt.ptr[i], rt.ptr[i + 1]
        niss = int(r['htrNiss'])
        found = {'b': set(), 'n': set()}
        for rid, htr, dl in zip(rt.rid[a:b], rt.htr[a:b], rt.delta[a:b]):
            k = K[int(rid)]
            if k[0] != 'H' or dl:
                continue
            c = level_of(k, 'C')
            found['n'].add(c)
            if htr <= niss + BUDGET:
                found['b'].add(c)
        r['_bin'] = found
        r['_sub'] = sub
        states.append(r)
    del rt

# ------------------------------------------------------------------------------------- trace: every optimal finish
t1 = trace([f"#{r['c']},{r['e']},{r['s']}" for r in states], 10 ** 7)
assert len(t1) == len(states)
rng = random.Random(20261112)


def rand_w():
    n = rng.randint(8, 10); w = []
    while len(w) < n:
        m = rng.choice(DRM)
        if w and (w[-1][0] == m[0] or (len(w) > 1 and AXIS[w[-1][0]] == AXIS[m[0]] == AXIS[w[-2][0]])):
            continue
        w.append(m)
    return w


Ws = [rand_w() for _ in states]
t2 = trace([' '.join(inv_seq(w) + inv_seq(t['all'][0])) for w, t in zip(Ws, t1)], 0)

# ------------------------------------------------------------------------------------- per state
blocks = collections.defaultdict(list)
tally = collections.Counter()        # (subset-free) checklist position -> states found by the first k classes
tally_n = collections.Counter()
red_agree = [0, 0]
for j, (r, t, w, t2r) in enumerate(zip(states, t1, Ws, t2)):
    sub = r['_sub']
    d = int(r['d']); niss = int(r['htrNiss'])
    check(t['d'] == d, (sub, r['idx'], 'optimum'))
    fins = [f['moves'].split() for f in t['finishes']]
    check(len(fins) == len(t['all']), (sub, r['idx'], 'all finishes read'))
    target = do(SOLVED, inv_seq(fins[0]))
    F = t2r['all'][0].split()
    Z = simplify(' '.join(w + inv_seq(F)))
    X = do(SOLVED, Z)
    check(X == target, (sub, r['idx'], 'scramble gives the state'))
    check(label(X) == r['lab_n'], (sub, r['idx'], 'label normal', label(X), r['lab_n']))
    check(label(do(SOLVED, inv_seq(Z))) == r['lab_i'], (sub, r['idx'], 'label inverse'))
    Zl = Z.split()
    # classes from the trace (Rust) readings
    best = {}                                      # class -> (htr, finish index, k, side)
    for fi, f in enumerate(t['finishes']):
        for rd in f['readings']:
            c = level_of(rd['h'], 'C'); h = rd['htr']
            key = (h, rd['side'] == 'I', fi)
            if c not in best or key < best[c][0]:
                best[c] = (key, fi, rd['k'], rd['side'])
    found_b = {c for c, v in best.items() if v[0][0] <= niss + BUDGET}
    found_n = set(best)
    # cross-check against the main run's route sets (same state, independent pass)
    for c, _ in checklist[sub]:
        check((c in found_b) == (c in r['_bin']['b']) and (c in found_n) == (c in r['_bin']['n']),
              (sub, r['idx'], 'class vs main run', c))
    lines_cl = ['| # | Class | Cumulative share (sample) | Finds an optimal here (HTR within 2 / any HTR) |', '|---:|---|---:|---|']
    worked = []
    first_b = first_n = None
    for pos, (c, cum) in enumerate(checklist[sub], 1):
        yb, yn = c in found_b, c in found_n
        if yb and first_b is None: first_b = pos
        if yn and first_n is None: first_n = pos
        lines_cl.append(f"| {pos} | {cls_txt(c)} | {cum * 100:.1f}% | {'yes' if yb else 'no'} / {'yes' if yn else 'no'} |")
        if yn:
            (h, invf, fi), fi, k, side = best[c]
            mv = fins[fi]
            hk, fk, hl = sticker.reading(Zl, mv, k, side == 'I')
            check(level_of(hk, 'C') == c and hl == h, (sub, r['idx'], 'reading', c, hk, hl, h))
            check(do(X, mv) == SOLVED and len(mv) == d, (sub, r['idx'], 'finish solves'))
            A, B = mv[:k], inv_seq(mv[k:])
            nrm, inv = ' '.join(A), ' '.join(B)
            if not A:
                txt = f"linear on the inverse: `({inv})`"
            elif not B:
                txt = f"linear on normal: `{nrm}`"
            elif side == 'I':
                txt = f"inverse first: `({inv})`, then on normal `{nrm}`"
            else:
                txt = f"normal first: `{nrm}`, then on inverse `({inv})`"
            within = 'within the budget' if h <= niss + BUDGET else f'{h - niss} over the shortest NISS HTR'
            worked.append(f"- Class {pos}: {txt}. HTR after {h} moves ({within}); the whole finish, as read on normal: `{' '.join(mv)}`.")
    for k in range(1, len(checklist[sub]) + 1):
        tally[k] += first_b is not None and first_b <= k
        tally_n[k] += first_n is not None and first_n <= k
    # bounding: the shortest reduction to 1q and to 2q over every optimal finish
    red = {}
    for fi, mv in enumerate(fins):
        qpos = [i for i, m in enumerate(mv) if m in QT]
        n = len(mv)
        for q in (1, 2):
            for t0 in range(0, len(qpos) - q + 1):
                start = 0 if t0 == 0 else qpos[t0 - 1] + 1
                end = qpos[t0 + q] if t0 + q < len(qpos) else n
                rlen = start + (n - end)
                if q not in red or rlen < red[q][0]:
                    red[q] = (rlen, mv[:start], mv[start:end], mv[end:])
    red_lines = []
    for q in (1, 2):
        if q not in red:
            red_lines.append(f'- No optimal finish has a stretch with exactly {q} quarter turn{"s" if q > 1 else ""} and half turns around it.')
            continue
        rlen, P, Q, T = red[q]
        Y = do(SOLVED, T + Zl + P)                  # the reduced state: T, then the scramble, then P
        lab = label(Y)
        ok = do(Y, Q) == SOLVED and nq(Q) == q and (not P or P[-1] in QT) and (not T or T[0] in QT)
        ok &= lab == '4a1 4e' if q == 1 else lab.split()[0] in ('4a2', '4b2', '0c0')
        check(ok, (sub, r['idx'], 'reduction', q, lab))
        Ti = inv_seq(T)
        shown = ' '.join(P) + (' ' if P and Ti else '') + (f"({' '.join(Ti)})" if Ti else '')
        what = 'to 1q (4a1 4e)' if q == 1 else f'to 2q ({lab} here)'
        red_lines.append(f"- Shortest reduction {what} on an optimal path: {rlen} move{'s' if rlen != 1 else ''}"
                         + (f", `{shown}`" if rlen else ' (the DR is already there)')
                         + f"; the reduced state is then solved by `{' '.join(Q)}` ({len(Q)} moves, {q} quarter turn{'s' if q > 1 else ''}).")
    (bc, br) = bound[(sub, int(r['idx']))]
    if bc == (r['c'], r['e'], r['s']):
        red_agree[0] += 1; red_agree[1] += br == red.get(1, (99,))[0]
        check(br == red.get(1, (99,))[0], (sub, r['idx'], 'reduction vs bounding run', br, red.get(1)))
    j_in = sum(1 for s in states[:j + 1] if s['_sub'] == sub)
    lab_n, lab_i = r['lab_n'], r['lab_i']
    head = (f"**{sub}, example {j_in}.** `{Z}`\n\n"
            f"Read as {lab_n} on normal, {lab_i} on inverse. Shortest HTR: {r['htrN']} on normal, {r['htrI']} on inverse, "
            f"{niss} with NISS.")
    body = ['<details><summary>Optimal finish, checklist and bounding</summary>', '',
            f"Optimal: {d} moves ({len(fins)} optimal finish{'es' if len(fins) != 1 else ''}, counting both orders of commuting moves).", '',
            *lines_cl, '']
    body += (worked or ['- None of these classes finds an optimal finish on this DR.']) + ['']
    body += red_lines + ['', '</details>', '']
    blocks[sub].append(head + '\n\n' + '\n'.join(body))

# ------------------------------------------------------------------------------------- page
n = len(states)
summ = '\n'.join(f"| {k} | {tally[k]} ({tally[k] / n * 100:.0f}%) | {tally_n[k]} |" for k in range(1, NCLS + 1))
parts = []
for g in ORDER:
    subs = [s for s in top if s.split()[0] == g]
    if not subs:
        continue
    parts.append(f'## {g}\n')
    for s in subs:
        parts.append(f'### {s}\n\n{size[s] / TOTAL * 100:.2f}% of all DR states.\n')
        parts += blocks[s]
head = f"""# Worked examples: which HTR routes to try from a DR

Examples to play along with the write-up ([WRITEUP.md](WRITEUP.md)). Find the finish yourself, then open the answer.

These are {n} DR states, the first {NPER} of the study's uniform sample in each of the {NSUB} most common subsets with their edge counts (together {sum(size[s] for s in top) / TOTAL * 100:.0f}% of all DR states). Nothing is hand-picked, so they're as hard or as easy as real DRs of that subset. Each scramble is a random DR followed by DR moves to the state, so it doesn't give the finish away.

**How to read it.** Finishes stay in DR (U, D, R2, L2, F2, B2); optimal means the shortest such finish, E slice solved. A route class like `4b2 > 2c3 > (4b2 > 4a1 > 0c0)` is the corner subset at the start and after each quarter turn until HTR, in the first study's names (4a3 and 4b3 by side: they swap on inverse); the part in brackets is done on the other side after a NISS switch. A class ending in `| qt` has a quarter turn after HTR (an HTR-breaking finish); every other class finishes in half turns from HTR. The checklist of each subset is the one in the write-up (greedy order, HTR budget 2, target optimal), with the share of the subset's 25,000 sampled states it covers after each class. A class *finds an optimal here* if some optimal finish can be read in that class with an HTR at most 2 moves longer than this DR's shortest NISS HTR (first answer), or with any HTR (second). The HTR length counts the moves on both sides until HTR. NISS is written as usual, inverse moves in brackets; "normal first" says which side you start on:

```
R2 U (D F2)   // R2 U on normal, then D F2 on the inverse
```

 The finish "as read on normal" is the same finish written linearly.

The bounding lines give the shortest reduction that keeps an optimal finish: moves on normal and (on inverse), each empty or ending in a quarter turn, after which the DR is one quarter turn from HTR (4a1 4e) or two (4a2, 4b2, or a 0c0 with bad edges), and the rest of the optimal finish from there, with exactly that many quarter turns. This is the one-quarter-turn reading of the write-up's bounding section (what JTuu's simulation measured); the method as the bounding docs state it, finishing the reduced state optimally with any number of quarter turns, can occasionally do it with a shorter reduction.

**Replay check.** Every move sequence on this page was replayed on the sticker model before the page was written: {REPLAYED[0]:,} checks (each scramble gives the state and its labels on both sides, every optimal finish solves it in the stated length, each printed reading has the stated class and HTR length when re-simulated move by move, each reduction leads to a state of the stated kind that the rest solves; the classes found agree with the main run on every state, and the 1q reduction length with the bounding run's one-quarter-turn reading), {len(MISMATCH)} mismatches.

**In these {n}**, the subset's checklist finds an optimal finish after its first k classes on this many states:

| k | HTR within 2 | Any HTR |
|---|---|---|
{summ}

"""
page = head + '\n'.join(parts)
open(PAGE, 'w').write(page)
print(f'{PAGE}: {n} states; {REPLAYED[0]:,} sticker-model checks, {len(MISMATCH)} mismatches; '
      f'1q reduction vs bounding run: {red_agree[1]}/{red_agree[0]} equal (of {n} states)')
if MISMATCH:
    print(MISMATCH[:10]); sys.exit(1)

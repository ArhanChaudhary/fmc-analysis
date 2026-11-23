#!/usr/bin/env python
"""Annotated example solves with the skeleton/variant meta, in the layout of the "Advanced DR Bounding Examples" doc.

usage: annotate.py [options] ID [ID ...]        ID as in data/scrambles.jsonl (2c3-01, ...), or `all`
       --within K                               stop after the K-th within-goal finish (default 2; 0: no limit)
       --htrs K                                 stop after K HTRs, within goal or not (default 10; 0: no limit)
       --max-skeletons K                        at most K skeletons (a skeleton and its mirror on the other side
                                                count as one)
       --out DIR                                where ID.md goes (default out/)
       --doc FILE                               also write the examples document, every given scramble in it

What is printed, per scramble, is the meta of skeleton-variant-meta/report/WRITEUP.md applied by the solver
(`drvar metaannot`, see dr-variants/research/drvar/src/annot.rs):

  1-2  skeletons shortest first, a skeleton and the skeleton the inverse reads its solutions on together
       (normal first);
  3    per skeleton, every approach to 2qt with P <= 1 that the caps leave a variant on (P+S+T <= 5 and the goal with
       N = 0), no extra move first;
  3-5  per approach, the variants the meta finishes: P+S+T <= 5 and L+P+S+T+N <= G with N the corner-case-aware
       bound or the mirror floor, fewest P+S+T first, then (P, S, T, N).  Each one gets its line (setup, the
       NISS@1qt edges, +P+S+T(+N)) and its moves from 2qt on: the whole finish with its length when it is within
       goal, the moves up to HTR and "no good" when it is not.  An approach with no such variant gets the line of
       its best variant only, as the reason it is dropped.

Every within-goal solution is replayed on a sticker model (judging-a-dr's fmccube) from the doc's own scramble, and
every "no good" line is checked to end on a state whose U/D-layer stickers all sit on their own axis.  With
--reread the solver also reads each within-goal solution as a whole (`drvar metaread`).

Not printed, because the solver does not have it: fixable / unfixable and locked slices, reflected slices, the name
of an insertion (corner swap, slice, floppy swap), cs-parity, and a NISS in the middle of a skeleton."""
import sys, os, json, subprocess, argparse, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool')
import fmccube as fc

DRVAR = '/data/fmc/dr-variants/research/drvar/target-annot/release/drvar'
RULES = '/data/fmc/dr-variants/research/out/meta/rules_1123.tsv'
BOUND = 1                 # column of the corner-case-aware bound in the rules file (0 simple, 2 comprehensive)
PMAX, CAP = 1, 5          # the fixed part of the meta: P <= 1, P+S+T <= 5
QT = {'U', "U'", 'D', "D'"}
F_FIRST = {'F-D', 'F-V', 'D-D'}     # corner kinds whose F edges are named first, as in the doc


def scrambles():
    return {x['id']: x for x in map(json.loads, open(f'{HERE}/data/scrambles.jsonl'))}


def dump(x, outdir, fresh=False):
    """The solver's lines for one scramble (cached)."""
    path = f'{outdir}/{x["id"]}.jsonl'
    if fresh or not os.path.exists(path):
        cmd = [DRVAR, 'metaannot', RULES, x['dr_scramble']]
        if x['section'] == '0c0':
            cmd.append('2')         # a 0c0 DR is gone through as a 2qt one, goal 12
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            sys.exit(f'drvar failed on {x["id"]}: {r.stderr[-400:]}')
        open(path, 'w').write(r.stdout)
    return [json.loads(l) for l in open(path)]


class Variant:
    """One HTR, read against its own skeleton, and what the meta does with it."""

    def __init__(self, c, goal):
        q, e = c['q'], c['e']
        self.c, self.q, self.side = c, q, c['side']
        self.P, self.S, self.T = sum(e[:q - 2]), e[q - 2], e[q - 1]
        self.L, self.spare = c['L'], goal - c['L']
        self.N = c['nb'][BOUND]
        # the mirror floor (step 4): the smallest N this side has to cover
        mid = e[3] if q == 6 else 0
        self.floor = {2: self.S, 3: self.P, 4: self.P - self.T}.get(q, self.P - mid - self.S - self.T)
        pst = self.P + self.S + self.T
        fixed = 'members' in c and self.P <= PMAX and pst <= CAP
        self.listed = fixed and pst + max(0, self.floor) <= self.spare          # before the bound
        self.finished = fixed and pst + max(self.N, self.floor) <= self.spare   # steps 3-5
        self.within = c['total'] <= goal
        self.order = (pst, self.P, self.S, self.T, self.N)

    def tuple(self):
        head = f'+{self.P}' if self.q > 2 else ''
        return f'{head}+{self.S}+{self.T}(+{self.N})'

    def member(self):
        """The moves to print: the best finish when it is within goal, else a shortest way to this HTR."""
        ms = self.c['members']
        short = [m for m in ms if m['len'] == self.c['wl']]
        assert short and all(m['L'] == self.L and m['e'] == self.c['e'] for m in short), 'members read like their class'
        assert min(m['n'][BOUND] for m in short) == self.N and len({(m['fe'], m['re'], m['bf'], m['br'], m['fr']) for m in short}) == 1
        if self.within:
            m = min(ms, key=lambda m: (m['len'] + m['fin'], m['len'], dturns(m['w']), m['w']))
            assert m['len'] + m['fin'] == self.c['total'], 'the best finish starts with the approach as spelled'
            return m
        return min(short, key=lambda m: (m['fin'], dturns(m['w']), m['w']))


def dturns(w):
    return sum(t[0] == 'D' for t in w.split())


def split(m, a2):
    """approach, setup, the rest (from the first quarter turn of the trigger on)."""
    w = m['w'].split()
    rest = w[a2:]
    i = next(i for i, t in enumerate(rest) if t in QT)
    return w[:a2], rest[:i], rest[i:]


def edges(m):
    f = f"F{m['fe']} ({'bad' if m['bf'] else 'good'})"
    r = f"R{m['re']} ({'bad' if m['br'] else 'good'})"
    a, b = (f, r) if m['kind'] in F_FIRST else (r, f)
    # for DD corners the direction of the last quarter turn flips fr, and the bound does not use it
    return f'{a} and {b}' + (', fr=1' if m['fr'] and m['kind'] != 'D-D' else '')


def par(moves, side):
    s = moves if isinstance(moves, str) else ' '.join(moves)
    return f'({s})' if side == 'I' else s


# --- checks on the printed moves, on the sticker model -----------------------------------------------------------
AXIS = {'F': 'FB', 'B': 'FB', 'R': 'RL', 'L': 'RL', 'U': 'UD', 'D': 'UD'}
FACE_AXIS = {(1, 0, 0): 'RL', (-1, 0, 0): 'RL', (0, 1, 0): 'UD', (0, -1, 0): 'UD', (0, 0, 1): 'FB', (0, 0, -1): 'FB'}


def state(scramble, side, moves):
    start = fc.parse(scramble) if side == 'N' else fc.invert(fc.parse(scramble))
    return fc.apply(fc.solved(), start + fc.parse(moves if isinstance(moves, str) else ' '.join(moves)))


def ls_solved(st):
    sol = fc.solved()
    return all(st[k] == sol[k] for k in st if k[0][1] != 0)


def bad_edges(scramble):
    """U/D-layer edges whose side sticker is off its axis, counted on the sticker model (the doc's 8e, 6e, ...)."""
    st = fc.apply(fc.solved(), fc.parse(scramble))
    return sum(AXIS[st[k]] != FACE_AXIS[tuple(k[1])] for k in st
               if k[0][1] != 0 and k[1][1] == 0 and sum(v != 0 for v in k[0]) == 2)


def label(x, dr):
    """The DR as the doc names it: its section's corner case (the solver has 4a3 and 4b3 together as 4c3, and
    counts the bad edges of a DR with four bad corners up to a layer turn) and its bad edges."""
    corners = dr['subset'].split()[0]
    assert corners == x['section'] or (x['section'], corners) == ('4b3', '4c3'), (x['id'], dr['subset'])
    return f"{x['section']} {bad_edges(x['scramble'])}e"


def on_axis(st):
    """Every sticker of the U and D layers shows a colour of the axis of the face it is on (true of any HTR state)."""
    return all(AXIS[st[k]] == FACE_AXIS[tuple(k[1])] for k in st if k[0][1] != 0)


# --- one scramble ----------------------------------------------------------------------------------------------
def render(x, rows, max_within=2, max_htrs=10, max_skeletons=None, log=sys.stderr):
    dr = rows[0]
    goal = dr['goal']
    skel = {(r['side'], r['route']): r for r in rows if r['t'] == 'skel'}
    by_skel = collections.defaultdict(list)
    for c in rows:
        if c['t'] == 'cls':
            by_skel[(c['side'], c['route'])].append(Variant(c, goal))

    # a skeleton and its mirror: the skeleton the other side reads the same solutions on
    mirror = {}
    for k, vs in by_skel.items():
        ms = {v.c['mirror'] for v in vs}
        assert len(ms) == 1, 'one skeleton, one mirror'
        mirror[k] = ('NI'[k[0] == 'N'], ms.pop())
    for k, mk in mirror.items():
        assert mk not in mirror or mirror[mk] == k, 'mirrors pair up'
    groups = {}
    for k, vs in by_skel.items():
        if not any(v.listed for v in vs):
            continue
        n = k if k[0] == 'N' else mirror[k]
        groups.setdefault(n, {})[k[0]] = k
    def gkey(item):
        sides = item[1]
        k = sides.get('N') or sides['I']
        s = skel[k]
        assert all(skel[kk]['L'] == s['L'] for kk in sides.values()), 'a skeleton and its mirror have one length'
        return (s['L'], s['q'], s['shape'], k[1])
    ordered = sorted(groups.items(), key=gkey)

    out = []
    stats = collections.Counter(skeletons_listed=len(ordered))
    solved = []
    def done():
        return bool(max_within and stats['within'] >= max_within) or bool(max_htrs and stats['finished'] >= max_htrs)
    title = x['scramble'] + f"  // {label(x, dr)}, goal {goal}"
    out.append(title)
    out.append('')
    for gi, (_, sides) in enumerate(ordered):
        if max_skeletons is not None and gi >= max_skeletons:
            break
        stats['skeletons'] += 1
        for si, side in enumerate(s for s in 'NI' if s in sides):
            k = sides[side]
            s = skel[k]
            vs = [v for v in by_skel[k] if v.listed]
            kind = vs[0].c['kind'].replace('-', '')
            assert all(v.c['kind'] == vs[0].c['kind'] and v.L == s['L'] for v in by_skel[k])
            # approaches to 2qt, no extra move first
            apps = collections.defaultdict(list)
            for v in vs:
                apps[v.c['pre2']].append(v)
            for g in apps.values():
                assert len({v.c['approach'] for v in g}) == 1 and all(v.c['common'] for v in g), 'one spelling per approach'
                g.sort(key=lambda v: (v.order, v.c['key']))
            # no extra move first, and among those the approach whose variants keep the skeleton's own setup
            apps = sorted(apps.values(), key=lambda g: (g[0].P, min(v.S for v in g) if g[0].P == 0 else 0, g[0].order, g[0].c['approach']))
            # how the skeleton starts: its own moves up to 2qt (a 2qt skeleton: its setup)
            q = s['q']
            if q > 2:
                p0 = [g[0].c['approach'] for g in apps if g[0].P == 0]
                start = p0[0] if p0 else ' '.join(cut_form(s['form'], q - 2))
            else:
                s0 = [split(v.member(), 0)[1] for g in apps for v in g if v.S == 0]
                start = ' '.join(s0[0] if s0 else cut_form(s['form'], 0, setup=True)) or s['form'].split()[0]
            spare = goal - s['L']
            if si == 0:
                where = '' if side == 'N' else ' on inverse'
                out.append(f"Skeleton starting with {par(start, side)}{where} has {kind} corners, L={s['L']}, {spare} spare move{'s' * (spare != 1)}.")
            else:
                out.append(f'Check inverse. Skeleton starting with {par(start, side)} has {kind} corners.')
            out.append('')
            for g in apps:
                stats['approaches'] += 1
                ind = ''
                if q > 2:
                    out.append(f"- {par(g[0].c['approach'], side)}")
                    ind = '    '
                fin = [v for v in g if v.finished]
                nearest = min(g, key=lambda v: (sum(v.order[1:4]) + max(v.N, v.floor), v.order, v.c['key']))
                last = None
                for v in fin or [nearest]:
                    m = v.member()
                    _, setup, rest = split(m, v.c['a2'])
                    after = f'After {par(setup, side)}' if setup else 'With no setup'
                    note = ''
                    if not v.finished and sum(v.order[1:4]) + v.N <= v.spare:
                        note = f", left to {'the inverse' if side == 'N' else 'the normal scramble'}"
                    line = f'{ind}- {after}, 1qt edges will be {edges(m)}: {v.tuple()}{note}'
                    if line != last:          # variants with one setup, one edge case and one tuple share a line
                        out.append(line)
                    last = line
                    if not v.finished:
                        stats['approaches_dropped'] += 1
                        continue
                    stats['finished'] += 1
                    moves = setup + rest
                    if v.within:
                        full = m['w'].split() + m['finish'].split()
                        assert len(full) == v.c['total'] and ls_solved(state(x['scramble'], side, full)), ('not a leave-slice solution', x['id'], full)
                        moves = moves + m['finish'].split()
                        out.append(f'{ind}    - {par(moves, side)} // {len(full)}')
                        stats['within'] += 1
                        solved.append((side, full, v, m))
                    else:
                        assert on_axis(state(x['scramble'], side, m['w'])), ('not an HTR', x['id'], m['w'])
                        out.append(f'{ind}    - {par(moves, side)} // no good')
                    if done():
                        break
                if done():
                    break
            out.append('')
            if done():
                break
        if done():
            break
    stats['skeletons_left'] = len(ordered) - stats['skeletons']
    # how the example ends
    n, lens = stats['finished'], sorted(len(s[1]) for s in solved)
    htrs = f"{n} HTR{'s' * (n != 1)}"
    got = {0: 'nothing within goal', 1: f'one finish within goal ({lens[0]})' if lens else ''}.get(
        len(lens), f"{len(lens)} finishes within goal ({', '.join(map(str, lens))})")
    if max_within and len(lens) >= max_within:
        end = f'Stop: {got}, after {htrs}.'
    elif max_htrs and n >= max_htrs:
        end = f'Stop: {htrs} done, {got}.'
    else:
        end = f'Nothing else passes the meta: {htrs} done, {got}.'
    opt = dr['lsopt']
    end += f" This DR's optimal is {opt}" + (', over the goal.' if opt > goal else '.')
    out.append(end)
    info = dict(id=x['id'], section=x['section'], subset=label(x, dr), goal=goal, optimal=opt, htrs=n, lens=lens,
                dropped=stats['approaches_dropped'], skeletons=stats['skeletons'], listed=len(ordered),
                exhausted=not done())
    print(x['id'], dict(stats), 'optimal', opt, 'found', lens, file=log)
    return '\n'.join(out).rstrip() + '\n', info, solved


def reread(x, solved):
    """Each printed within-goal solution, read as a whole by the solver (`drvar metaread`): its skeleton's length
    and its extra moves must be the ones on its line, and add up to its length."""
    for side, full, v, m in solved:
        cmd = [DRVAR, 'metaread', x['dr_scramble'], ' '.join(full)] + (['inverse'] if side == 'I' else [])
        f = subprocess.run(cmd, capture_output=True, text=True).stdout.strip().split('\t')
        d = dict(zip(f[::2], f[1::2]))
        got = tuple(int(d[k]) for k in ('L', 'P', 'S', 'T', 'N', 'moves'))
        assert got[0] + sum(got[1:5]) == got[5] == len(full), (x['id'], full, got)
        if m['len'] == v.c['wl']:
            assert got[:4] == (v.L, v.P, v.S, v.T) and got[4] >= v.N, (x['id'], full, got, v.tuple())


SOURCE = 'https://docs.google.com/document/d/1xtvlA3Tg2zkl8H1D98XhLU66gITJ5S-oIPajsn68SOE'
BOUNDING = 'https://docs.google.com/document/d/13F8HonrKJyHjU9EwfiHDRyY4X77vPriYeaVSrh5guq0'
DATE = '23 Nov 2026'

INTRO = """# The skeleton/variant meta: example solves

{date}

The [skeleton/variant meta](WRITEUP.md), run by a solver on the {n} DRs of [*Advanced DR Bounding Examples*]({source}) and written out the way that doc writes its solves.
Every scramble is a DR on U/D. The goal is 12/13/14 moves from DR to a leave-slice finish for a 2qt/3qt/4qt DR; the 0c0 DRs are solved as 2qt ones, with goal 12.
The sections are the doc's; its 4b3 DRs fall under 4c3 in the write-up, which counts 4a3 and 4b3 together.

Each example goes through the skeletons in the meta's order and stops after {stop}.

## How to read an example

```
Skeleton starting with L2 U has FD corners, L=7, 6 spare moves.

- L2 U
    - After R2 B2, 1qt edges will be FH (bad) and RH (good), fr=1: +0+1+0(+5)
        - R2 B2 U B2 U // no good

Check inverse. Skeleton starting with (F2 U') has RD corners.
```

- **Skeleton line.** Skeletons come shortest first. A skeleton is named by how it starts (its moves up to 2qt; a 2qt skeleton by its setup), with the corners it leaves at NISS@1qt, its length L and the spare moves G−L.
- **Check inverse.** The skeleton the inverse scramble reads the same solutions on, with the same L. Moves in parentheses are on the inverse. Normal always goes first.
- **Approach to 2qt** (first-level bullet): the moves up to 2qt, with P ≤ 1. Approaches with no extra move come first. A 2qt skeleton has no approach, so its variants are the first level.
- **Variant line.** `After R2 B2` is the setup. The 1qt edges are the F and R edge cases at NISS@1qt as in [*Advanced DR Bounding*]({bounding}), each with whether that slice is bad for these corners, and `fr=1` when the F/R parity is odd. Then the extra moves `+P+S+T(+N)`, or `+S+T(+N)` on a 2qt skeleton, where N is the corner-case-aware bound.
- **Moves.** Under a variant, the moves from the setup on (put the approach in front for the whole solution). A finish within goal is written out with its length; anything else stops at HTR with `// no good`. Variants are in the meta's order: fewest P+S+T first, then (P, S, T, N).
- **A variant line with no moves under it.** No variant of that approach (on a 2qt skeleton: of that skeleton) passes the meta, and the line is the closest one, to show why. `left to the inverse` (or `the normal scramble`) means it is only dropped because it comes earlier on the other side (step 4).
- **Last line.** Why the example stops, what was found, and the DR's optimal to a leave-slice finish.

Left out, compared with the doc's own solves: fixable/unfixable, locked and reflected slices, the name of the insertion (a variant is given by its setup and its moves instead), cs parity, and a NISS in the middle of a skeleton.

## The examples at a glance

One row per example: what the meta finds before it stops, and how many HTRs it takes to reach its first finish within goal when nothing stops it. "Best found" is empty when nothing within goal was found, and the last column is empty when the DR has no finish within goal.

| Example | DR | Goal | DR optimal | HTRs done | Finishes within goal | Best found | HTRs to the first finish within goal |
|---|---|---|---|---|---|---|---|"""


def document(done, max_within, max_htrs):
    """The examples document: how to read an example, one row per example, then the examples by corner case."""
    n = len(done)
    stops = ([f"its {('first', 'second', 'third')[max_within - 1] if max_within <= 3 else f'{max_within}th'} finish within goal"] if max_within else []) \
        + ([f'after {max_htrs} HTRs'] if max_htrs else [])
    stop = {0: 'the last one', 1: stops[0] if stops else ''}.get(len(stops), ', or '.join(stops) + ', whichever comes first')
    o = [INTRO.format(date=DATE, n=n, source=SOURCE, bounding=BOUNDING, stop=stop)]
    num, counts = {}, collections.Counter()
    for x, info, _ in done:
        counts[x['section']] += 1
        num[x['id']] = counts[x['section']]
    for x, info, _ in done:
        k = num[x['id']]
        best = min(info['lens']) if info['lens'] else ''
        first = info['first'] or ('never' if info['optimal'] <= info['goal'] else '')
        o.append(f"| [{x['section']}, scramble {k}](#{x['section']}-scramble-{k}) | {info['subset']} | {info['goal']} | {info['optimal']} "
                 f"| {info['htrs']} | {len(info['lens'])} | {best} | {first} |")
    solvable = [i for _, i, _ in done if i['optimal'] <= i['goal']]
    hit = [i for i in solvable if i['lens']]
    opt = [i for i in hit if min(i['lens']) == i['optimal']]
    assert all(not i['lens'] for _, i, _ in done if i['optimal'] > i['goal'])
    reach = sorted(i['first'] for i in solvable if i['first'])
    assert all(i['first'] is None for _, i, _ in done if i['optimal'] > i['goal'])
    assert all(i['first'] <= max_htrs for i in hit) if max_htrs else True
    med = reach[len(reach) // 2] if len(reach) % 2 else (reach[len(reach) // 2 - 1] + reach[len(reach) // 2]) / 2
    o += ['', f"{len(solvable)} of the {n} DRs have a finish within goal. The meta finds one on {len(hit)} of them before it stops, "
              f"and on {len(opt)} of those it finds the DR's optimal. With nothing to stop it, it reaches a finish within goal on "
              f"{len(reach)} of the {len(solvable)}, after {reach[0]} to {reach[-1]} HTRs (median {med:g})."]
    for x, info, _ in done:
        if info.get('miss'):
            o += ['', f"The one it never solves within goal is {x['section']}, scramble {num[x['id']]}: {info['miss']}"]
    section = None
    for x, info, text in done:
        if x['section'] != section:
            section = x['section']
            o += ['', f'## {section}']
        head, body = text.split('\n', 1)
        scr, _ = head.split('  // ')
        assert scr == x['scramble']
        o += ['', f"### {section}, scramble {num[x['id']]}", '', f'`{scr}`', '', f"{info['subset']}, goal {info['goal']}.", body.rstrip('\n')]
    return '\n'.join(o) + '\n'


def missed(x, rows):
    """A DR with finishes within goal that the meta never reaches: how its within-goal HTRs read, and one of them
    written out and checked (the solver is run again with the caps opened just far enough to print it)."""
    goal = rows[0]['goal']
    vs = [Variant(c, goal) for c in rows if c['t'] == 'cls' and c['total'] <= goal]
    assert vs and not any(v.finished for v in vs)
    v = min(vs, key=lambda v: (v.order[0], v.P, v.side != 'N', v.c['key']))
    cmd = [DRVAR, 'metaannot', RULES, x['dr_scramble'], '2' if x['section'] == '0c0' else '-',
           str(max(v.P, PMAX)), str(max(v.order[0], CAP))]
    wide = [json.loads(l) for l in subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.splitlines()]
    c = next(c for c in wide if c['t'] == 'cls' and (c['side'], c['key']) == (v.side, v.c['key']))
    m = min(c['members'], key=lambda m: (m['len'] + m['fin'], m['len'], dturns(m['w']), m['w']))
    full = m['w'].split() + m['finish'].split()
    assert len(full) <= goal and ls_solved(state(x['scramble'], v.side, full)), (x['id'], full)
    cmd = [DRVAR, 'metaread', x['dr_scramble'], ' '.join(full)] + (['inverse'] if v.side == 'I' else [])
    f = subprocess.run(cmd, capture_output=True, text=True).stdout.strip().split('\t')
    d = dict(zip(f[::2], f[1::2]))
    L, P, S, T, N, n = (int(d[k]) for k in ('L', 'P', 'S', 'T', 'N', 'moves'))
    assert L + P + S + T + N == n == len(full) and P + S + T == v.order[0], (x['id'], full, d)
    if all(u.order[0] > CAP for u in vs):
        why = f"every one of them has P+S+T of {min(u.order[0] for u in vs)} or more"
    elif all(u.P > PMAX or u.order[0] > CAP for u in vs):
        why = f"every one of them has P > {PMAX} or P+S+T > {CAP}"
    else:
        why = 'the caps or the bound drop every one of them'
    kn, ki = (len({u.c['key'] for u in vs if u.side == sd}) for sd in 'NI')
    return (f"it has {kn} HTR{'s' * (kn != 1)} within goal on normal and {ki} on inverse, and {why}. For example `{par(full, v.side)}` ({n}) has a {L}-move skeleton "
            f"and reads (P, S, T, N) = ({P}, {S}, {T}, {N}).")


def cut_form(form, nq, setup=False):
    """The written skeleton up to its nq-th quarter turn; with `setup`, its first section only."""
    w = form.split()
    if setup:
        i = next(i for i, t in enumerate(w) if t in QT)
        return w[:i]
    seen = 0
    for i, t in enumerate(w):
        seen += t in QT
        if seen == nq:
            return w[:i + 1]
    return w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ids', nargs='+')
    ap.add_argument('--within', type=int, default=2)
    ap.add_argument('--htrs', type=int, default=10)
    ap.add_argument('--doc')
    ap.add_argument('--max-skeletons', type=int)
    ap.add_argument('--out', default=f'{HERE}/out')
    ap.add_argument('--fresh', action='store_true', help='rerun the solver even if its lines are cached')
    ap.add_argument('--reread', action='store_true', help='have the solver read every printed within-goal solution')
    a = ap.parse_args()
    sc = scrambles()
    ids = list(sc) if a.ids == ['all'] else a.ids
    done = []
    for i in ids:
        x = sc[i]
        text, info, solved = render(x, dump(x, a.out, a.fresh), a.within, a.htrs, a.max_skeletons)
        if a.reread:
            reread(x, solved)
        open(f'{a.out}/{i}.md', 'w').write(text)
        if a.doc:
            _, free, _ = render(x, dump(x, a.out), 1, 0, None, log=open(os.devnull, 'w'))
            info['first'] = free['htrs'] if free['lens'] else None
            if info['first'] is None and info['optimal'] <= info['goal']:
                info['miss'] = missed(x, dump(x, a.out))
        done.append((x, info, text))
    if a.doc:
        open(a.doc, 'w').write(document(done, a.within, a.htrs))


if __name__ == '__main__':
    main()

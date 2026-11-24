#!/usr/bin/env python
"""Annotated example solves with the skeleton/variant meta, in the layout of the "Advanced DR Bounding Examples" doc.

usage: annotate.py [options] ID [ID ...]        ID as in data/scrambles.jsonl and data/generated.jsonl (2c3-01,
                                                ...), or `all`
       --skeletons K                            skeletons gone through (default 8; a skeleton and its mirror on the
                                                other side count as one; 0: all)
       --spare K                                ... taken from the ones with at least K spare moves (default 2)
       --hard K                                 hard-to-find solutions shown from the other skeletons (default 3)
       --cap K                                  drop the variants with P+S+T > K, as the write-up does with 5
                                                (default: no cap)
       --hcap K                                 skip a variant whose HTR is more than G - K moves away (default 1,
                                                the write-up's cap; 0: no cap)
       --slack K                                the bound P+S+T+N has to stay K under the spare moves (default 0)
       --out DIR                                where the solver's lines are cached and ID.md goes (default out/)
       --doc FILE                               also write the examples document: the corner cases from 2c4 to 4a1
                                                (ORDER), the scrambles of each as given
       --unsolved K                             ... with at most K scrambles with no within-goal solution per
                                                corner case, at the end of its section (default 1; -1: all)
       --keep-order                             ... with the corner cases in the order of the scramble list
       --reread                                 have the solver read every printed within-goal solution again

What is printed, per scramble, is what the solver (`drvar metaannot`, dr-variants/research/drvar/src/annot.rs) finds
with the meta of skeleton-variant-meta/report/WRITEUP.md:

  - the skeletons in order of their moves to HTR, then most pairs after each quarter turn, a skeleton and the
    skeleton the inverse reads its solutions on together (normal first);
  - per skeleton side, every variant with P <= 1, L+P+S+T+N <= G and its HTR at most G-1 moves away, taken to
    HTR; N is the corner-case-aware bound or the mirror floor.  Shown are the solutions within goal and one variant
    that is no good, the one with the most pairs right after its last insertion;
  - a skeleton of 3 or more quarter turns that ends with its last one (HH corners) first with that quarter turn as
    a premove on the other side (`reduced`: the DR that is left, one move less to spend, no mirror floor), then
    linearly;
  - up to --hard solutions within goal from the skeletons that are not gone through.

A 0c0 DR is gone through as a 2qt one (goal 12).  A 4a1 DR has goal 12; its own skeleton has one quarter turn, no
approach and no setup to 2qt, so its variants read +T(+N) and have no mirror floor.

Each variant gets its line (setup, the NISS@1qt edges, +P+S+T(+N)) and its moves from 2qt on: the whole solution
with its length when it is within goal, the moves up to HTR and "no good" when it is not.

Moves are the solver's choice of U or D for each turn (annot.rs `human`), and a finish is leave-slice up to a turn
of both layers.  Every within-goal solution is replayed on a sticker model (judging-a-dr's fmccube) from the doc's
own scramble and read again as a whole by the solver; every "no good" line is checked to end on a state whose
U/D-layer stickers all sit on their own axis.  With --reread the solver's own command (`drvar metaread`) also reads
each within-goal solution with 2 or more quarter turns that ends with the centres in place and has no premove.

The scrambles: data/scrambles.jsonl (scrambles.py, from the Advanced DR Bounding Examples doc) and
data/generated.jsonl (add_generated.py, from the subset generator's page through subsets_page.mjs).

Not printed, because the solver does not have it: fixable / unfixable and locked slices, reflected slices, the name
of an insertion (corner swap, slice, floppy swap), cs-parity, and a NISS in the middle of a skeleton."""
import sys, os, json, subprocess, argparse, collections, random

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/data/fmc/judging-a-dr/research/tool')
import fmccube as fc

DRVAR = '/data/fmc/dr-variants/research/drvar/target-annot/release/drvar'
RULES = '/data/fmc/dr-variants/research/out/meta/rules_1123.tsv'
BOUND = 1                 # column of the corner-case-aware bound in the rules file (0 simple, 2 comprehensive)
PMAX = 1                  # approaches to 2qt with at most this many extra moves
# the write-up's meta also drops the variants with P+S+T > 5.  The examples keep them (None), to show every
# solution the bound lets through; 5 puts the cap back
CAP = None
OPEN = 99                 # what the solver is given for no cap
# a variant is checked when its lower bound P+S+T+N is at most the spare moves minus SLACK.  The write-up's meta has
# 0 (L+P+S+T+N <= G); 1 asks for a bound strictly under the spare moves
SLACK = 0
# the write-up's cap on the HTR itself: a variant is checked only when its HTR is at most G - HCAP moves away (after a
# premove: of the goal that is left, so the premove counts as a move to HTR).  The write-up has 1: at G moves there
# is no move left for a finish.  0: no cap
HCAP = 1
SKELETONS = 8             # skeletons gone through (a skeleton and its mirror on the other side count as one)
SPARE = 2                 # ... among the ones with at least this many spare moves
HARD = 3                  # finishes within goal shown from the skeletons that are not gone through
NOGOOD = 'side'           # of the variants that are no good, one is shown per skeleton side ('side') or per approach
# a skeleton of 3 or more quarter turns that ends with its last one (HH corners): 'premove' = the DR left after that
# quarter turn is made on the other side, in place of the skeleton; 'both' = that and then the skeleton in full;
# 'full' = the skeleton in full, no premove
HH = 'both'
# after a premove, a left-over skeleton of 3 or more quarter turns that again ends with its last one (the skeleton
# ends with two quarter turns in a row): gone through like any other left-over skeleton, or left out
PAIR_END = True
# the document: the corner cases in this order (the ones not named here after them, as they come), and per corner
# case at most UNSOLVED examples whose DR has no within-goal solution (optimal over the goal), after the others
# (None: all of them, where they stand)
ORDER = ['2c4', '2c3', '0c0', '4b3', '4b2', '4a2', '4a1']
REVERSE = True            # False: the corner cases in the order of the scramble lists
UNSOLVED = 1
# a section of the scramble lists under the name it has in the document: the "4b3" scrambles of the Advanced DR
# Bounding Examples doc are the subset generator's 4c3 (4a3 and 4b3 together)
NAME = {'4b3': '4c3'}
# a section whose DRs are not solved by their own quarter turns and the goal that goes with them (10 + quarter
# turns): (quarter turns, goal) as the solver takes them, `-` for its own.  A 0c0 DR is gone through as a 2qt one,
# goal 12; a 4a1 DR as the 1qt DR it is, with goal 12
SOLVE = {'0c0': ('2', '-'), '4a1': ('-', '12')}
QT = {'U', "U'", 'D', "D'"}
F_FIRST = {'F-D', 'F-V', 'D-D'}     # corner kinds whose F edges are named first, as in the doc


def scrambles():
    """The scrambles by id: the ones of the "Advanced DR Bounding Examples" doc (data/scrambles.jsonl, scrambles.py),
    then the ones generated since on the subset generator's page (data/generated.jsonl, add_generated.py)."""
    files = [f'{HERE}/data/scrambles.jsonl', f'{HERE}/data/generated.jsonl']
    return {x['id']: x for f in files if os.path.exists(f) for x in map(json.loads, open(f))}


def dump(x, outdir, fresh=False):
    """The solver's lines for one scramble (cached)."""
    path = f'{outdir}/{x["id"]}.jsonl'
    m, g = SOLVE.get(x['section'], ('-', '-'))
    if fresh or not os.path.exists(path):
        cmd = [DRVAR, 'metaannot', RULES, x['dr_scramble'], m, str(PMAX), str(CAP or OPEN), g]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            sys.exit(f'drvar failed on {x["id"]}: {r.stderr[-400:]}')
        open(path, 'w').write(r.stdout)
    rows = [json.loads(l) for l in open(path)]
    if rows[0]['pmax'] < PMAX or rows[0]['cap'] < (CAP or OPEN) or (g != '-' and rows[0]['goal'] != int(g)):
        sys.exit(f"{path} was made with P <= {rows[0]['pmax']}, P+S+T <= {rows[0]['cap']}, goal {rows[0]['goal']}: run again with --fresh")
    return rows


class Variant:
    """One HTR, read against its own skeleton, and what the meta does with it."""

    def __init__(self, c, goal, floor=True):
        q, e = c['q'], c['e']
        self.c, self.q, self.side = c, q, c['side']
        # a skeleton with one quarter turn (a 1qt DR's own) has no state with 2 quarter turns left: no approach and
        # no setup to a 2qt trigger, only the extra moves before its quarter turn, T
        self.P, self.S, self.T = (0, 0, e[0]) if q == 1 else (sum(e[:q - 2]), e[q - 2], e[q - 1])
        self.L, self.spare = c['L'], goal - c['L']
        self.N = c['nb'][BOUND]
        # the mirror floor (step 4): the smallest N this side has to cover
        mid = e[3] if q == 6 else 0
        self.floor = {1: 0, 2: self.S, 3: self.P, 4: self.P - self.T}.get(q, self.P - mid - self.S - self.T) if floor else 0
        pst = self.P + self.S + self.T
        fixed = self.P <= PMAX and (CAP is None or pst <= CAP)
        assert 'h' in c or not fixed, 'the solver wrote out every class the examples check'
        self.listed = fixed and pst + max(0, self.floor) <= self.spare          # before the bound
        self.bound_ok = fixed and pst + max(self.N, self.floor) <= self.spare - SLACK   # steps 3-5
        # ... and its HTR is near enough to leave a move for the finish
        self.finished = self.bound_ok and not (HCAP and c['wl'] > goal - HCAP)
        # the solver's `total` is the class's best finish with the centres in place, `htot` its best up to a turn of
        # both layers.  They differ when the best of the four HTR states a half turn of a layer apart is the one a
        # path with two quarter turns and no U2 does not end on; up to the turn it is one of the other three
        self.total = min(c['total'], c.get('htot', c['total']))
        self.within = self.total <= goal
        self.order = (pst, self.P, self.S, self.T, self.N)
        # true pairs in the U and D layers right after the last insertion: among the variants of one skeleton with
        # one (P, S, T, N), the ones with more pairs are taken first
        self.pairs, self.group, self.gsize = c['pairs'], self.order[1:], 1
        self.passno = 0           # 1, 2: the pass this variant is taken to HTR in; 0: it is not
        self.red = c.get('red')   # after a premove (a skeleton that ends with its last quarter turn): how it goes

    def tuple(self):
        if self.q == 1:
            return f'+{self.T}(+{self.N})'
        head = f'+{self.P}' if self.q > 2 else ''
        return f'{head}+{self.S}+{self.T}(+{self.N})'

    def approach(self):
        return ' '.join(self.c['h'].split()[:self.c['ha2']])

    def member(self):
        """The moves to print, as the solver wrote them (`h` of drvar metaannot: a member that reads like its
        class, each U/D turn on the face a solver turns, the finish up to a turn of both layers): the best finish
        when it is within goal, else a shortest way to this HTR.  With the NISS@1qt case of the HTR it lands on."""
        c = self.c
        assert c['hrot'] in (0, 2), 'a printed path ends on HTR with the centres in place'
        assert c['ha2'] == c['a2']
        n = len(c['h'].split())
        if self.within:
            assert c['htot'] == self.total, 'the printed moves are the best of their class'
        elif not self.red:
            assert n == c['wl'] and c['hL'] == self.L and c['he'] == c['e'] and c['htot'] == self.total
        if 'members' in c:
            short = [m for m in c['members'] if m['len'] == c['wl']]
            assert short and all(m['L'] == self.L and m['e'] == c['e'] for m in short), 'members read like their class'
            assert min(m['n'][BOUND] for m in short) == self.N and len({(m['fe'], m['re'], m['bf'], m['br'], m['fr']) for m in short}) == 1
            if not self.within:
                f = short[0]
                assert (c['hfe'], c['hre'], c['hbf'], c['hbr'], c['hfr']) == (f['fe'], f['re'], f['bf'], f['br'], f['fr'])
        return dict(w=c['h'], finish=c['hfin'], len=n, kind=c['hkind'], fe=c['hfe'], re=c['hre'], bf=c['hbf'], br=c['hbr'], fr=c['hfr'])


def group_sizes(vs):
    """How many of the variants the meta finishes on one skeleton side share each (P, S, T, N)."""
    size = collections.Counter(v.group for v in vs if v.finished)
    for v in vs:
        v.gsize = size[v.group]


def reduced(rows):
    """The premove route.  A skeleton of 3 or more quarter turns that ends with its last one (HH corners) is not gone
    through as it stands: that quarter turn is made first on the other side, and what is left on this side is a DR
    with one quarter turn fewer and one move less to spend (`rdr`, `rskel`, `rcls` of drvar metaannot).  The turn
    can go either way, so each HTR of what is left is listed twice (`dir`); here the two are put together: the
    reading is the one after the turn that leaves the shorter skeleton, the bound and the finish are the better of
    the two.  -> {(side, route of the HH skeleton): dict(classes, kind, q, pre)}; no classes when another HH skeleton
    with the same left-over came first, or, with PAIR_END off, when what is left ends with a quarter turn again
    (the skeleton ends with two in a row)."""
    rdr = {(r['side'], r['dir']): r for r in rows if r['t'] == 'rdr'}
    rsk = {(r['side'], r['dir'], r['route']): r for r in rows if r['t'] == 'rskel'}
    cls = collections.defaultdict(dict)
    for c in rows:
        if c['t'] == 'rcls':
            cls[(c['side'], c['key'])][c['dir']] = c
    r1to0 = {(side, ds[1]['route']): ds[0]['route'] for (side, _), ds in cls.items() if len(ds) == 2}

    def block(side, d, route):
        if d == 0:
            return (side, 0, route)
        return (side, 0, r1to0[(side, route)]) if (side, route) in r1to0 else (side, 1, route)

    blocks = collections.defaultdict(list)
    for (side, _), ds in cls.items():
        d = min(ds)
        blocks[block(side, d, ds[d]['route'])].append(ds)
    out, taken = {}, set()
    hh = sorted((r for r in rows if r['t'] == 'skel' and 'rroute' in r), key=lambda r: (r['L'], r['q'], r['shape'], r['route']))
    for sk in hh:
        side, k = sk['side'], (sk['side'], sk['route'])
        ids = [b for b in (block(side, d, sk['rroute'][d]) for d in (0, 1)) if b in blocks]
        out[k] = dict(classes=[], kind=None, q=sk['q'] - 1, pre=None, why='nothing in reach')
        if not ids:
            continue
        if ids[0] in taken:
            out[k]['why'] = 'same left-over as an earlier skeleton'
            continue
        taken.add(ids[0])
        items = blocks[ids[0]]
        L = {d: min(ds[d]['L'] for ds in items if d in ds) for d in (0, 1) if any(d in ds for ds in items)}
        # the premove is the skeleton's own last quarter turn (`rdir`), unless only the other way is in reach
        dstar = min(L, key=lambda d: (L[d], d != sk['rdir']))
        kinds = {ds[dstar]['kind'] for ds in items if dstar in ds}
        assert len(kinds) == 1 and all(ds[dstar]['L'] == L[dstar] and ds[dstar]['q'] == sk['q'] - 1 for ds in items if dstar in ds), 'one left-over skeleton'
        kind = kinds.pop()
        # the whole skeleton as it is turned after the premove: all but its last quarter turn, then that turn
        # the whole skeleton as it is gone through: what is left of it after the premove (one way to write that),
        # then the premove's quarter turn.  Quarter turns in a row are written on the two layers in turn.
        left = next(iter(ds[dstar]['route'] for ds in items if dstar in ds))
        body = rsk[(side, dstar, left)]['form'].split() if (side, dstar, left) in rsk else sk['rform'][dstar].split()
        full = body + [rdr[(side, dstar)]['last']]
        for i in range(len(full) - 2, -1, -1):
            if full[i] not in QT:
                break
            if full[i][0] == full[i + 1][0]:
                full[i] = 'UD'[full[i][0] == 'U'] + full[i][1:]
        full = ' '.join(full)
        out[k].update(kind=kind, pre=rdr[(side, dstar)]['pre'], L=L[dstar], why='', full=full)
        if kind == 'H-H' and sk['q'] - 1 >= 3 and not PAIR_END:
            out[k]['why'] = 'ends with two quarter turns in a row'
            continue
        goal = rdr[(side, dstar)]['goal']
        best = lambda x: min(x['total'], x.get('htot', x['total']))
        for ds in items:
            if dstar not in ds:
                continue
            c = dict(ds[dstar])
            c['nb'] = [min(x['wl'] + x['lc'] + x['nb'][i] for x in ds.values()) - c['wl'] - c['lc'] for i in range(len(c['nb']))]
            c['total'] = min(best(x) for x in ds.values())
            df = dstar
            if 'h' in c and c['total'] <= goal:
                # within goal: the finish of the way that is shorter
                df = min((d for d in ds if 'h' in ds[d]), key=lambda d: (ds[d]['htot'], d != dstar))
                for f in ('h', 'hfin', 'htot', 'hrot', 'hcut', 'ha2', 'hL', 'he', 'hread'):
                    c[f] = ds[df][f]
                assert c['htot'] == c['total']
            c['red'] = dict(pre=rdr[(side, dstar)]['pre'], last=rdr[(side, df)]['last'], lead=rdr[(side, dstar)]['last'], same=df == dstar)
            out[k]['classes'].append(c)
    return out


RING = ['F', 'R', 'B', 'L']


def image(moves):
    """A solution up to which of U and D is turned: every D turn written as the same U turn, the side moves after it
    renamed to match (U F2 and D R2 are the same two moves), and two side moves on one axis put in one order."""
    rot, out = 0, []
    for t in moves:
        f, suf = t[0], t[1:]
        if f in 'UD':
            if f == 'D':
                rot = (rot - {'': 1, '2': 2, "'": 3}[suf]) % 4
            out.append('U' + suf)
        else:
            out.append(RING[(RING.index(f) + rot) % 4] + suf)
    for i in range(len(out) - 1):
        a, b = out[i][0], out[i + 1][0]
        if a in RING and b in RING and RING.index(a) % 2 == RING.index(b) % 2 and a > b:
            out[i], out[i + 1] = out[i + 1], out[i]
    return tuple(out)


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


def ls_solved_turn(st):
    """Solved up to the E slice and up to a turn of both layers together: how many quarter turns off, or None."""
    for j in range(4):
        if ls_solved(st):
            return j
        st = fc.apply(st, fc.parse("U D'"))
    return None


def bad_edges(scramble):
    """U/D-layer edges whose side sticker is off its axis, counted on the sticker model (the doc's 8e, 6e, ...)."""
    st = fc.apply(fc.solved(), fc.parse(scramble))
    return sum(AXIS[st[k]] != FACE_AXIS[tuple(k[1])] for k in st
               if k[0][1] != 0 and k[1][1] == 0 and sum(v != 0 for v in k[0]) == 2)


def label(x, dr):
    """The DR as the document names it: its section's corner case (4a3 and 4b3 together are 4c3, for the solver and
    for the document; the solver counts the bad edges of a DR with four bad corners up to a layer turn) and its bad
    edges."""
    corners = dr['subset'].split()[0]
    assert corners == x['section'] or (x['section'], corners) == ('4b3', '4c3'), (x['id'], dr['subset'])
    return f"{NAME.get(x['section'], x['section'])} {bad_edges(x['scramble'])}e"


def on_axis(st):
    """Every sticker of the U and D layers shows a colour of the axis of the face it is on (true of any HTR state)."""
    return all(AXIS[st[k]] == FACE_AXIS[tuple(k[1])] for k in st if k[0][1] != 0)


# --- one scramble ----------------------------------------------------------------------------------------------
def skeleton_sides(rows):
    """Every skeleton side with the variants a solver goes through on it.  A skeleton of 3 or more quarter turns
    that ends with its last one (HH corners) is taken through the premove (`reduced`); every other one as it is.
    -> (skel lines by (side, route), variants by (side, route), the premove's info by (side, route), mirror)"""
    goal = rows[0]['goal']
    skel = {(r['side'], r['route']): r for r in rows if r['t'] == 'skel'}
    own = collections.defaultdict(list)
    for c in rows:
        if c['t'] == 'cls':
            own[(c['side'], c['route'])].append(Variant(c, goal))
    # a skeleton and its mirror: the skeleton the other side reads the same solutions on
    mirror = {}
    for k, vs in own.items():
        ms = {v.c['mirror'] for v in vs}
        assert len(ms) == 1, 'one skeleton, one mirror'
        mirror[k] = ('NI'[k[0] == 'N'], ms.pop())
    for k, mk in mirror.items():
        assert mk not in mirror or mirror[mk] == k, 'mirrors pair up'
    red = reduced(rows) if HH != 'full' else {}
    by = {}
    for k in set(own) | set(red):
        if k in red:
            assert skel[k]['shape'][-1] == 0 and skel[k]['q'] >= 3
            by[k] = [Variant(c, goal - 1, floor=False) for c in red[k]['classes']]
        else:
            assert HH == 'full' or k not in skel or skel[k]['shape'][-1] > 0 or skel[k]['q'] <= 2, 'an HH skeleton of 3 or more quarter turns goes through the premove'
            by[k] = own[k]
    return skel, by, red, mirror, own


def render(x, rows, max_skeletons=SKELETONS, min_spare=SPARE, hard=HARD, log=sys.stderr):
    dr = rows[0]
    goal = dr['goal']
    skel, by_skel, red, mirror, own = skeleton_sides(rows)
    # what is gone through on a skeleton side: the skeleton itself, or for an HH skeleton the DR left after the
    # premove (and, with HH = 'both', the skeleton itself after that)
    def parts(k):
        ps = [('premove' if k in red else None, by_skel[k])]
        if k in red and HH == 'both':
            ps.append(('full', own.get(k, [])))
        return [(mode, [v for v in vs if v.listed]) for mode, vs in ps if any(v.listed for v in vs)]
    groups = {}
    for k in by_skel:
        if not parts(k):
            continue
        n = k if k[0] == 'N' else mirror.get(k, k)
        groups.setdefault(n, {})[k[0]] = k
    def gkey(item):
        # fewest moves to HTR (on the side where the skeleton has more moves after its last quarter turn), then
        # most pairs after the first quarter turn, after the second, ...
        sides = item[1]
        assert len({skel[k]['L'] for k in sides.values()}) == 1, 'a skeleton and its mirror have one length'
        return min((skel[k]['L'] - skel[k]['shape'][-1], [-n for n in skel[k]['pq']], sd != 'N', k[1]) for sd, k in sides.items())
    ordered = sorted(groups.items(), key=gkey)
    spare_of = lambda item: goal - skel[next(iter(item[1].values()))]['L']
    tried = [g for g in ordered if spare_of(g) >= min_spare]
    if max_skeletons:
        tried = tried[:max_skeletons]
    rest = [g for g in ordered if not any(g is t for t in tried)]

    def blocks_of(group_list):
        out = []
        for gi, (_, sides) in enumerate(group_list):
            for si, side in enumerate(s for s in 'NI' if s in sides):
                k = sides[side]
                for pi, (mode, vs) in enumerate(parts(k)):
                    if mode == 'premove':
                        assert all(v.c['kind'] == red[k]['kind'] and v.L == red[k]['L'] for v in by_skel[k])
                    else:
                        assert all(v.c['kind'] == vs[0].c['kind'] and v.L == skel[k]['L'] for v in (own[k] if mode else by_skel[k]))
                    apps = collections.defaultdict(list)
                    for v in vs:
                        apps[v.c['pre2']].append(v)
                    for g in apps.values():
                        assert len({v.approach() for v in g}) == 1, 'one spelling per approach'
                        g.sort(key=lambda v: (v.order, -v.pairs, v.c['key']))
                    # no extra move first, and among those the approach whose variants keep the skeleton's own setup
                    apps = sorted(apps.values(), key=lambda g: (g[0].P, min(v.S for v in g) if g[0].P == 0 else 0, g[0].order, g[0].approach()))
                    run = sorted(((v.order, -v.pairs, ai, v.c['key'], v) for ai, g in enumerate(apps) for v in g if v.finished), key=lambda t: t[:4])
                    out.append(dict(gi=gi, si=si, side=side, k=k, mode=mode, again=pi > 0, apps=apps, run=[t[4] for t in run]))
        return out

    stats = collections.Counter(skeletons_listed=len(ordered), skeletons=len(tried))
    seen = set()
    start_of = fc.parse(x['scramble'])
    solved = []

    def head(b, alone):
        """The summary line of a skeleton side.  `alone`: a block shown on its own (hard to find), never as the
        second side of a pair."""
        side, k = b['side'], b['k']
        s = skel[k]
        pm = red[k] if b['mode'] == 'premove' else None
        kind = 'HH' if pm else b['apps'][0][0].c['kind'].replace('-', '')
        name = pm['full'] if pm else s['form']
        spare = goal - s['L']
        if b['again'] and not alone:
            line = 'Check linearly.' if side == 'N' else 'Check inverse linearly.'
        elif b['si'] == 0 or alone:
            where = '' if side == 'N' else ' on inverse'
            line = f"Skeleton {par(name, side)}{where} has {kind} corners, L={s['L']}, {spare} spare move{'s' * (spare != 1)}."
            if not pm:
                line += ' Check linearly.'
        else:
            line = f"Check inverse{'' if pm else ' linearly'}. Skeleton {par(name, side)} has {kind} corners."
        if pm:
            # the premove is made on the other side
            line += f" Apply {par(pm['pre'], 'NI'[side == 'N'])} and NISS: {pm['kind'].replace('-', '')} corners."
        return line

    def lines(b, show, note):
        """The approaches of a block with the variants in `show`: variant line, moves, and the checks of the moves.
        A finish that is already printed for this side (the same moves up to which of U and D is turned) is not
        printed again."""
        side, k = b['side'], b['k']
        q = skel[k]['q'] - (b['mode'] == 'premove')
        out = []
        for g in b['apps']:
            ind = '    ' if q > 2 else ''
            sub, last = [], None
            for v in (v for v in g if v in show):
                m = v.member()
                w = m['w'].split()
                _, setup, rest_ = split(m, v.c['ha2'])
                own_side = start_of if side == 'N' else fc.invert(start_of)
                if v.within:
                    # after a premove the solution ends with that quarter turn
                    full = w + m['finish'].split() + ([v.red['last']] if v.red else [])
                    assert len(full) == v.total + bool(v.red) <= goal and ls_solved_turn(state(x['scramble'], side, full)) is not None, ('not a leave-slice solution', x['id'], full)
                    read_check(x, v, m, w + m['finish'].split())
                    if v.red and not m['finish'] and full[-2] in QT:
                        # the premove follows a quarter turn directly: the two are one half turn, or nothing
                        full = full[:-2] + (['U2'] if full[-2][1:] == full[-1][1:] else [])
                        assert ls_solved_turn(state(x['scramble'], side, full)) is not None, ('not a leave-slice solution', x['id'], full)
                    if (side, image(full)) in seen:
                        stats['repeats'] += 1
                        continue
                    seen.add((side, image(full)))
                    move_line = f"{ind}    - **{par(full[v.c['ha2']:], side)} // {len(full)}**"
                    solved.append((side, full, v, m))
                else:
                    # the state the moves reach: after a premove, the premove's turn comes before the scramble
                    lead = fc.parse(v.red['lead']) if v.red else []
                    assert on_axis(fc.apply(fc.solved(), lead + own_side + fc.parse(' '.join(w)))), ('not an HTR', x['id'], m['w'])
                    move_line = f"{ind}    - {par(setup + rest_, side)} // {note[id(v)]}"
                after = f'After {par(setup, side)}' if setup else 'With no setup'
                # with one quarter turn the setup ends on the state the edges are read on
                line = f"{ind}- {after}, 1qt edges {'are' if v.q == 1 else 'will be'} {edges(m)}: {v.tuple()}"
                if line != last:          # variants with one setup, one edge case and one tuple share a line
                    sub.append(line)
                last = line
                sub.append(move_line)
            if sub:
                out += ([f"- {par(g[0].approach(), side)}"] if q > 2 else []) + sub
        return out

    out = [x['scramble'] + f"  // {label(x, dr)}, goal {goal}", '']
    # the skeletons gone through: every variant the meta lets through is taken to HTR; shown are the finishes within
    # goal and, per approach, the one that is no good with the most pairs right after its last insertion
    for b in blocks_of(tried):
        show, note = [], {}
        # NOGOOD: one no-good shown per approach to 2qt, or one for the whole skeleton side
        for part in ([[v for g in b['apps'] for v in g]] if NOGOOD == 'side' else b['apps']):
            taken = [v for v in part if v.finished]
            for v in taken:
                v.passno = 1
            stats['finished'] += len(taken)
            stats['premove'] += sum(bool(v.red) for v in taken)
            bad = [v for v in taken if not v.within]
            show += [v for v in taken if v.within]
            if bad:
                one = min(bad, key=lambda v: (-v.pairs, v.order, v.c['key']))
                show.append(one)
                note[id(one)] = 'no good'
        out.append(head(b, False))
        out.append('')
        body = lines(b, show, note)
        if not body:
            # nothing passes the bound, or (rarely) everything that does is a solution already printed
            stats['empty_repeat'] += bool(show)
            none = '- No variants have lower bound < spare moves.' if SLACK else '- All variants have lower bound > spare moves.'
            if any(v.bound_ok for g in b['apps'] for v in g):
                # the bound lets some through, and every one of those reaches HTR with no move left for a finish
                stats['empty_cap'] += 1
                none = '- All variants have lower bound > spare moves, or reach HTR with no move left.'
            body = ['- Only solutions already found above.' if show else none]
        out += body
        out.append('')
    found = len(solved)
    # hard to find: finishes within goal on the skeletons that are not gone through
    extra = []
    for b in blocks_of(rest):
        vs = [v for v in b['run'] if v.within][:hard - len(extra)]
        if vs:
            if not extra:
                out += ['Hard to find solutions:', '']
            extra += vs
            out.append(head(b, True))
            out.append('')
            out += lines(b, vs, {})
            out.append('')
        if len(extra) >= hard:
            break
    lens, hlens = sorted(len(t[1]) for t in solved[:found]), sorted(len(t[1]) for t in solved[found:])
    n, k = stats['finished'], len(tried)

    # the DR's optimal, the shortest solution on the skeletons gone through, and the shortest hard-to-find one
    # when it is shorter than that
    opt = dr['lsopt_turn']
    end = f"Optimal is {opt}. Found {min(lens) if lens else 'none'}."
    if hlens and (not lens or min(hlens) < min(lens)):
        end += f' Findable but hard {min(hlens)}.'
    out.append(end)
    info = dict(id=x['id'], section=x['section'], subset=label(x, dr), goal=goal, optimal=opt, htrs=n, lens=lens, hard=hlens,
                skeletons=k, listed=len(ordered), premove=stats['premove'], tried=[sorted(g[1].values()) for g in tried],
                half_turn=sum(v.c['hrot'] == 2 for _, _, v, _ in solved))
    print(x['id'], dict(stats), 'optimal', opt, 'found', lens, 'hard to find', hlens, file=log)
    return '\n'.join(out).rstrip() + '\n', info, solved


def read_check(x, v, m, full):
    """A printed within-goal solution as the solver reads it as a whole (`hread`: L, then the extra moves of every
    section): the skeleton's length and the extra moves must be the ones on its line, and add up to its length."""
    L, *ex = v.c['hread']
    q = len(ex) - 1
    got = (L, 0, 0, ex[0], ex[1]) if q == 1 else (L, sum(ex[:q - 2]), ex[q - 2], ex[q - 1], ex[q])
    assert L + sum(ex) == len(full), (x['id'], full, v.c['hread'])
    if m['len'] == v.c['wl'] and (not v.red or v.red['same']):
        # the line's N is the table's for the case the finish is read from, and the finish cannot beat it, but for
        # the table's one known error: the corner-case-aware table asks +5 for RD or FD corners with 1 bad slice and
        # cs/fr 1/1, where +4 is enough (the write-up's "Error in DR Bound").  The line keeps the table's +5
        known = (BOUND == 1 and m['kind'] in ('R-D', 'F-D') and m['bf'] + m['br'] == 1 and (v.c['hcsp'], m['fr']) == (1, 1)
                 and (v.N, got[4]) == (5, 4))
        assert got[:4] == (v.L, v.P, v.S, v.T) and (got[4] >= v.N or known), (x['id'], full, got, v.tuple())
    return got


def reread(x, solved):
    """Each printed within-goal solution read again by the solver's own command (`drvar metaread`), which takes a
    solution with 2 or more quarter turns that ends with the centres in place: the same reading as on its line."""
    for side, full, v, m in solved:
        if v.c['hrot'] or v.red or v.q == 1:       # `metaread` reads solutions with 2 or more quarter turns
            continue
        cmd = [DRVAR, 'metaread', x['dr_scramble'], ' '.join(full)] + (['inverse'] if side == 'I' else [])
        f = subprocess.run(cmd, capture_output=True, text=True).stdout.strip().split('\t')
        d = dict(zip(f[::2], f[1::2]))
        got = tuple(int(d[k]) for k in ('L', 'P', 'S', 'T', 'N'))
        assert got == read_check(x, v, m, full) and int(d['moves']) == len(full), (x['id'], full, got)


DATE = '24 Nov 2026'

# the block shown under "How to read an example": two blocks of one example, as they are printed (SAMPLE_ID)
SAMPLE_ID = '4b2-02'
SAMPLE = """Skeleton U R2 U R2 U F2 U has HH corners, L=7, 5 spare moves. Apply (U') and NISS: RD corners.

- U
    - After L2 B2 L2 F2, 1qt edges will be RD (good) and FH (good): +0+3+2(+0)
        - L2 B2 L2 F2 U' F2 R2 L2 D // no good

Check linearly.

- D B2 D
    - After L2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - L2 U B2 L2 B2 L2 U' // no good
    - After R2, 1qt edges will be RH (good) and FH (good): +0+0+3(+0)
        - **R2 U L2 B2 L2 B2 U L2 R2 // 12**
"""

INTRO = """# The skeleton/variant meta: example solves

{date}

Example solves using the [skeleton/variant meta](WRITEUP.md), generated using JTuu's [subset generator](https://jtuu.be/subsets.html).

Every scramble is a DR on U/D. The goal is 12/13/14 moves from DR to a leave-slice finish for a 2qt/3qt/4qt DR; the 0c0 DRs are solved as 2qt ones, with goal 12.{onequarter}

The solutions are found with an automated solver that implements the meta.

For each scramble:
 - Choose the {skeletons} skeletons with the fewest moves to HTR
 - Include extensions to extra qt (if they are among the top {skeletons})
   - Include extensions using null insertions such as U U'
   - These are treated like any other skeleton

Any solutions that use a different skeleton are listed as "hard to find"

For each skeleton:
 - Check all approaches to 2qt that use <= 1 extra move
 - Check all variants whose lower bound is {under} spare moves{capline}
 - Show any successes and some near-misses

## How to read an example

```
{sample}
```

**Skeleton ...** solves corners up to a possible corner swap. NISS after 1 qt is allowed on both sides
  - **... U**: the approach to 2qt (if any). Up to one extra move is allowed
    - **After ...** setup to a 2qt trigger and the full penalty's lower bound
      - **X2 U Y2 D ...** the within-goal full solution, or the near-miss approach to HTR"""


def document(done, max_skeletons=SKELETONS, min_spare=SPARE, hard=HARD):
    """The examples document: what is done per scramble, how to read an example, then the examples by corner case."""
    # the block of the reading guide is in the examples as it stands
    shown = [text for x, _, text in done if x['id'] == SAMPLE_ID]
    assert not shown or SAMPLE.strip('\n') in shown[0], 'the block under "How to read an example" is no longer in its example'
    # the 4a1 DRs, when there are any; their one-quarter-turn reading only when an example shows it
    onequarter = ''
    if any(x['section'] == '4a1' for x, _, _ in done):
        one = any(', 1qt edges are ' in text for x, _, text in done if x['section'] == '4a1')
        onequarter = ' The 4a1 DRs also have goal 12' + ('; a skeleton with one quarter turn has no 2qt trigger, so its variants read +T(+N).' if one else '.')
    o = [INTRO.format(date=DATE, skeletons=max_skeletons, sample=SAMPLE.rstrip('\n'), onequarter=onequarter, under='<' if SLACK else '<=',
                     capline='\n - Skip variants that reach HTR with no move left for a finish' if HCAP else '')]
    # the corner cases in the document's order (ORDER; as they come in with REVERSE off); in each, the examples with
    # a within-goal solution as they come, then the first UNSOLVED of the ones without (the others are left out)
    by = {}
    for item in done:
        by.setdefault(item[0]['section'], []).append(item)
    done = []
    for sec in ([s for s in ORDER if s in by] + [s for s in by if s not in ORDER] if REVERSE else by):
        none = [t for t in by[sec] if t[1]['optimal'] > t[1]['goal']]
        if UNSOLVED is None:
            done += by[sec]
        else:
            done += [t for t in by[sec] if t not in none] + none[:UNSOLVED]
    num, counts = {}, collections.Counter()
    for x, info, _ in done:
        counts[x['section']] += 1
        num[x['id']] = counts[x['section']]
    section = None
    for x, info, text in done:
        if x['section'] != section:
            section = x['section']
            o += ['', f'## {NAME.get(section, section)}']
        head, body = text.split('\n', 1)
        scr, _ = head.split('  // ')
        assert scr == x['scramble']
        o += ['', f"### {NAME.get(section, section)}, scramble {num[x['id']]}", '', f'`{scr}`', '', f"{info['subset']}, goal {info['goal']}.", body.rstrip('\n')]
    return '\n'.join(o) + '\n'


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
    global HH, PAIR_END, NOGOOD, CAP, UNSOLVED, REVERSE, SLACK, HCAP
    ap = argparse.ArgumentParser()
    ap.add_argument('ids', nargs='+')
    ap.add_argument('--skeletons', type=int, default=SKELETONS, help='skeletons gone through (0: all)')
    ap.add_argument('--spare', type=int, default=SPARE, help='fewest spare moves of a skeleton that is gone through')
    ap.add_argument('--hard', type=int, default=HARD, help='hard-to-find finishes shown from the other skeletons')
    ap.add_argument('--nogood', choices=['side', 'approach'], default=NOGOOD, help='one no-good variant shown per skeleton side, or per approach to 2qt')
    ap.add_argument('--hh', choices=['premove', 'both', 'full'], default=HH, help='HH skeletons of 3+ quarter turns: the premove in place of the skeleton, both, or the skeleton only')
    ap.add_argument('--cap', type=int, default=CAP or 0, help='drop the variants with P+S+T over this, as the write-up does with 5 (0: no cap)')
    ap.add_argument('--no-pair-end', action='store_true', help='leave out the HH skeletons that end with two quarter turns in a row')
    ap.add_argument('--doc')
    ap.add_argument('--hcap', type=int, default=HCAP, help='check a variant only when its HTR is at most G minus this many moves away (the write-up has 1; 0: no cap)')
    ap.add_argument('--slack', type=int, default=SLACK, help='moves the lower bound P+S+T+N has to stay under the spare moves by (0: the write-up\'s L+P+S+T+N <= G)')
    ap.add_argument('--unsolved', type=int, default=UNSOLVED, help='examples with no within-goal solution kept per corner case in the document, at the end of its section (-1: all, where they stand)')
    ap.add_argument('--keep-order', action='store_true', help='the corner cases in the order of the scramble list, not last to first')
    ap.add_argument('--out', default=f'{HERE}/out')
    ap.add_argument('--fresh', action='store_true', help='rerun the solver even if its lines are cached')
    ap.add_argument('--reread', action='store_true', help='have the solver read every printed within-goal solution')
    a = ap.parse_args()
    HH, PAIR_END, NOGOOD, CAP = a.hh, not a.no_pair_end, a.nogood, a.cap or None
    UNSOLVED, REVERSE, SLACK = (None if a.unsolved < 0 else a.unsolved), not a.keep_order, a.slack
    HCAP = a.hcap
    sc = scrambles()
    ids = list(sc) if a.ids == ['all'] else a.ids
    done = []
    for i in ids:
        x = sc[i]
        text, info, solved = render(x, dump(x, a.out, a.fresh), a.skeletons, a.spare, a.hard)
        if a.reread:
            reread(x, solved)
        open(f'{a.out}/{i}.md', 'w').write(text)
        done.append((x, info, text))
    if a.doc:
        open(a.doc, 'w').write(document(done, a.skeletons, a.spare, a.hard))


if __name__ == '__main__':
    main()

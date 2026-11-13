#!/usr/bin/env python3
"""The "100 scrambles" section of EXAMPLES.md: real scrambles, the DRs a solver could have on the page, what can be
read off each without solving, what the five-line prune list of the write-up says, and (folded away) the answers.

  scrambles   out/hand/attempt_scrambles.txt, drawn once: uniformly random states from the eo-to-dr study's
              `eodrtools mkscr N_RUN SCR_SEED` (adjacent turns of one face merged as in its canon.py), written the
              FMC way (R' U' F at both ends) with a two-phase solver (python package kociemba) so that nothing
              merges with the padding, and replayed to the same state.  The first N_PAGE are printed, all N_RUN
              are used for the closing tables.  An earlier version used nissy 2.0.8's `scramble`, which is not
              uniform (eo-to-dr README); those are kept in out/hand/attempt_scrambles_nissy.txt.
  DRs         cubelib-cli, steps "EO[niss=always] > DR[niss=before]": EO first with NISS anywhere, then DR without
              breaking it on either side, all three axes, every such DR up to CAP moves.  One DR per choice of
              direction of the last move on each side (written clockwise); the state is the one as written.
  reads       drtools read --quick on the DR state turned so that its axis is U/D (subset, true pairs, corner case
              on both sides, shortest HTR on both sides, optimal finish).
  solution    DR + optimal finish, where each last move may be turned the other way if that finishes shorter
              (the same thing as the finish's first or last move merging with it).
  the list    fillenv._dropped, the same function the write-up's guide is computed with.

Rewrites the region of EXAMPLES.md between the two markers, then re-reads every scramble, DR and answer printed
there from the page's text alone with the slow sticker simulator and the full `drtools read`, and prints the number
of mismatches; it has to be 0.

usage: source /data/fmc/env.sh; python3 many_examples.py [--rerun] | --verify-only
       (needs cubelib-cli, drtools built and the BFS tables; eodrtools and kociemba only to draw new scrambles;
        --rerun recomputes out/hand/attempt_run.csv, about ten minutes on four cores)"""
import csv, itertools, multiprocessing, os, random, re, subprocess, sys, importlib.machinery, importlib.util
R = '/data/fmc/judging-a-dr/research/'
for d in ('src', 'src/report_build', 'tool'): sys.path.insert(0, R + d)
import pv, fillenv, fmccube as fc
loader = importlib.machinery.SourceFileLoader('drread', R + 'tool/drread')
spec = importlib.util.spec_from_loader('drread', loader); dr = importlib.util.module_from_spec(spec); loader.exec_module(dr)

PAGE = '/data/fmc/judging-a-dr/report/EXAMPLES.md'
GUIDE = R + 'src/report_build/guide.md'
SCR = R + 'out/hand/attempt_scrambles.txt'
RUN = R + 'out/hand/attempt_run.csv'
START, END = '<!-- many-examples:start -->', '<!-- many-examples:end -->'
N_PAGE, N_RUN, CAP, SHOWN, SEED = 100, 500, 12, 8, 20261112
SCR_SEED = 20261112                            # eodrtools mkscr seed of the scrambles
MKSCR = '/data/fmc/eo-to-dr/research/eodrtools/target/release/eodrtools'
STEPS = f'EO[niss=always;max=8] > DR[niss=before;max={CAP}]'
QUICK = [R + 'drtools/target/release/drtools', 'read', '--quick', R + 'data/drbfs', R + 'data/ls_depth.u8']
PAD = "R' U' F"
AXIS = {'U': 0, 'D': 0, 'R': 1, 'L': 1, 'F': 2, 'B': 2}
SUF = {1: '', 2: '2', 3: "'"}
CLASSES = (9, 10, 11, 12)                      # DR length classes of the closing tables: 9 means 9 or less
TELL = {'8': '; back-face diagonals agree', '7': '; back-face diagonals differ'}

def text(moves): return ' '.join(b + SUF[t] for b, t in moves)
def niss(n, i): return ' '.join(x for x in (text(n), f'({text(i)})' if i else '') if x)

# ---- a fast sticker simulator (permutations of the 54 stickers), checked against fmccube in selfcheck()
KEYS = sorted(fc.solved()); IDX = {k: i for i, k in enumerate(KEYS)}; COL = [fc.solved()[k] for k in KEYS]
def _src(base, t):
    st = fc.turn({k: i for i, k in enumerate(KEYS)}, base, t)
    return [st[k] for k in KEYS]
SRC = {(b, t): _src(b, t) for b in 'UDRLFB' for t in (1, 2, 3)}
def perm(moves, p=None):
    """Sticker now at slot i came from slot p[i]; continue from state p if given."""
    p = list(range(54)) if p is None else p
    for m in moves:
        s = SRC[m]; p = [p[j] for j in s]
    return p
def as_dict(p): return {KEYS[i]: COL[p[i]] for i in range(54)}
def state(ps, n, i):
    """The cube after undoing the inverse-side moves i, the scramble (as perm ps) and the normal moves n."""
    pi = perm(fc.invert(i))
    return perm(n, [pi[j] for j in ps])

VIEW_ROT = {'U/D': None, 'F/B': fc.rot_r, 'R/L': fc.inv(fc.rot_f)}     # as in fmccube.find_dr
class View:
    def __init__(self, name):
        f = VIEW_ROT[name]; self.name = name
        fwd = (lambda v: v) if f is None else f
        back = (lambda v: v) if f is None else (lambda v: f(f(f(v))))
        self.relab = {c: fc.NORMAL_FACE[fwd(fc.FACE_NORMAL[c])] for c in 'UDRLFB'}
        self.face_back = {fc.NORMAL_FACE[fwd(fc.FACE_NORMAL[c])]: c for c in 'UDRLFB'}   # face in this view -> face on the cube
        self.groups = []
        for group in (fc.CORNERS, fc.UD_EDGES, fc.E_EDGES):
            homes = {fc.home_colours(pos): i for i, pos in enumerate(group)}; cub = []
            for pos in group:
                normals = [tuple((pos[i] if j == i else 0) for j in range(3)) for i in range(3) if pos[i]]
                chk = (0, pos[1], 0) if pos[1] != 0 else (0, 0, pos[2])
                cub.append(([IDX[(back(pos), back(n))] for n in normals], normals.index(chk), 'UD' if pos[1] != 0 else 'FB'))
            self.groups.append((homes, cub))
    def arrays(self, p):
        """(corners, U/D edges, E edges) of the state seen with this view's axis vertical, or None if it is no DR there."""
        out = []
        for homes, cub in self.groups:
            arr = []
            for srcs, ci, ok in cub:
                cols = [self.relab[COL[p[j]]] for j in srcs]
                if cols[ci] not in ok: return None
                h = homes.get(frozenset(cols))
                if h is None: return None
                arr.append(h)
            out.append(arr)
        return out
VIEWS = {name: View(name) for name in VIEW_ROT}

# ---- DRs of a scramble
def canon(mv):
    """One side's moves with the quarter turns among its last moves (those about one axis) written clockwise."""
    mv = list(mv); i = len(mv)
    while i > 0 and AXIS[mv[i - 1][0]] == AXIS[mv[-1][0]]: i -= 1
    return mv[:i] + [(b, 1 if t in (1, 3) else t) for b, t in mv[i:]]
def side_variants(mv, drax):
    """Every way the end of one side's moves can come out once a finish in DR moves is merged into it: a quarter turn
    of a side face may turn the other way, a half turn of a side face may go, and a turn about the DR axis may become
    any turn or go.  All of them are DR states again.  The moves as given come first."""
    mv = tuple(mv); out = [mv]; todo = [mv]
    while todo:
        cur = todo.pop(); i = len(cur)
        while i > 0 and AXIS[cur[i - 1][0]] == AXIS[cur[-1][0]]: i -= 1
        for j in range(i, len(cur)):
            b, t = cur[j]
            for t2 in ((1, 2, 3, 0) if AXIS[b] == drax else (1, 3) if t in (1, 3) else (2, 0)):
                new = cur[:j] + (((b, t2),) if t2 else ()) + cur[j + 1:]
                if new not in out: out.append(new); todo.append(new)
    return out
def variants(n, i, axis):
    """(normal moves, inverse moves) for the DR as written (first) and for every merged ending."""
    drax = AXIS[axis[0]]
    return [(list(a), list(b)) for a in side_variants(canon(n), drax) for b in side_variants(canon(i), drax)]

def cubelib(scramble, cap):
    """[(normal moves, inverse moves, axis)] for every EO-first DR up to cap moves, as cubelib-cli lists them."""
    out = subprocess.run(['cubelib-cli', '--no-check-update', 'solve', '-s', STEPS, '-q', '0', '-M', str(cap), '-f', 'detailed', scramble],
                         capture_output=True, text=True).stdout
    res = []
    for block in out.split('\n\n'):
        sol = re.search(r'^Solution \((\d+)\): ?(.*)$', block, re.M); ax = re.search(r'//\s*dr(ud|fb|lr)', block)
        if not sol or not ax: continue
        n, i = fc.split_niss(sol.group(2))
        assert len(n) + len(i) == int(sol.group(1)), block
        res.append((n, i, {'ud': 'U/D', 'fb': 'F/B', 'lr': 'R/L'}[ax.group(1)]))
    return res

def quick(states):
    out = subprocess.run(QUICK, input='\n'.join(' '.join(map(str, c + e + s)) for c, e, s in states) + '\n', capture_output=True, text=True).stdout
    res = [dict(l.split(': ', 1) for l in block.split('\n')) for block in out.strip().split('\n\n')] if states else []
    assert len(res) == len(states) and all('optimal' in kv for kv in res), 'drtools read --quick failed'
    return res

def drs_of(scramble, cap=CAP):
    """Every DR of the scramble up to cap moves, distinct as DR states, shortest first, with reads and answers."""
    ps = perm(fc.parse(scramble)); seen = {}; recs = []
    found = cubelib(scramble, cap)
    if not found:                               # no DR that short: take the shortest there is
        for c in range(cap + 1, 21):
            found = cubelib(scramble, c)
            if found: break
    for n, i, axis in sorted(found, key=lambda t: (len(t[0]) + len(t[1]), niss(canon(t[0]), canon(t[1])), t[2])):
        vs = variants(n, i, axis); V = VIEWS[axis]; sts = []
        for vn, vi in vs:
            a = V.arrays(state(ps, vn, vi))
            assert a is not None, (scramble, niss(vn, vi), axis)
            sts.append(a)
        key = (axis, tuple(map(tuple, sts[0])))
        if key in seen: continue
        seen[key] = 1
        recs.append(dict(n=vs[0][0], i=vs[0][1], axis=axis, length=len(n) + len(i), vs=vs, sts=sts))
    kvs = quick([s for r in recs for s in r['sts']]); k = 0
    for r in recs:
        mine = kvs[k:k + len(r['sts'])]; k += len(r['sts']); kv = mine[0]
        cs, e = kv['subset'].split(); a, b = kv['corner_case'].split(); hn, hi = map(int, kv['htr'].split())
        tot = [len(vn) + len(vi) + int(x['optimal']) for (vn, vi), x in zip(r['vs'], mine)]; j = tot.index(min(tot))
        r.update(cs=cs, e=int(e[0]), tp=int(kv['true_pairs']), a=a, b=b, hn=hn, hi=hi, opt=int(kv['optimal']), total=tot[j], best=r['vs'][j], best_st=r['sts'][j])
        r['drop'] = bool(fillenv._dropped(cs, r['e'], a, b, r['tp'], min(hn, hi), max(hn, hi)))
        del r['vs'], r['sts']
    return recs

def klass(length): return min(max(length, CLASSES[0]), CLASSES[-1])
def run_row(recs):
    """One line of attempt_run.csv: per DR length class, how many DRs, how many the list keeps, the best solution over all
    and over the kept ones, and how many reach the scramble's best solution (all, kept).  99 = none."""
    best = min(r['total'] for r in recs); row = [min(r['length'] for r in recs), best]
    for c in CLASSES:
        rs = [r for r in recs if klass(r['length']) == c]; ks = [r for r in rs if not r['drop']]
        row += [len(rs), len(ks), min([r['total'] for r in rs], default=99), min([r['total'] for r in ks], default=99),
                sum(r['total'] == best for r in rs), sum(r['total'] == best for r in ks)]
    return row
RUN_HEAD = ['scramble', 'shortest_dr', 'best'] + [f'{x}{c}' for c in CLASSES for x in ('n', 'kept', 'best', 'best_kept', 'reach', 'reach_kept')]

def work(job):
    idx, scramble, want_run = job
    recs = drs_of(scramble, CAP if want_run else 11)
    return idx, (run_row(recs) if want_run else None), ([r for r in recs if r['length'] <= 11] or recs) if idx < N_PAGE else None

# ---- scrambles
def facelets(st):
    """Sticker dict -> the 54-letter string of the kociemba package (faces U R F D L B, each row by row)."""
    order = [((0, 1, 0), lambda r, c: (c - 1, 1, r - 1)), ((1, 0, 0), lambda r, c: (1, 1 - r, 1 - c)), ((0, 0, 1), lambda r, c: (c - 1, 1 - r, 1)),
             ((0, -1, 0), lambda r, c: (c - 1, -1, 1 - r)), ((-1, 0, 0), lambda r, c: (-1, 1 - r, c - 1)), ((0, 0, -1), lambda r, c: (1 - c, 1 - r, -1))]
    return ''.join(st[(at(r, c), n)] for n, at in order for r in range(3) for c in range(3))
def rotations():
    """The 24 whole-cube rotations as maps face -> face."""
    out = []; seen = set()
    for a in range(4):
        for b in range(4):
            for c in range(4):
                def f(v, a=a, b=b, c=c):
                    for _ in range(a): v = fc.rot_u(v)
                    for _ in range(b): v = fc.rot_r(v)
                    for _ in range(c): v = fc.rot_u(v)
                    return v
                m = {x: fc.NORMAL_FACE[f(fc.FACE_NORMAL[x])] for x in 'UDRLFB'}
                if tuple(sorted(m.items())) not in seen: seen.add(tuple(sorted(m.items()))); out.append(m)
    assert len(out) == 24
    return out
def fmc_scramble(state_moves, rots):
    """R' U' F ... R' U' F for the state reached by state_moves (the state itself is not changed, only how it is written):
    the inner part is the inverse of a two-phase solution, looked for in several orientations and, if none of those can
    sit between the padding, with a fixed first or last move."""
    import kociemba
    target = fc.apply(fc.solved(), state_moves)
    unpad = fc.invert(fc.parse(PAD)); q = unpad + state_moves + unpad                 # the inner part has to reach this state
    free = [None] + [(b, t) for b in 'UDRL' for t in (1, 3, 2)]; last = [None] + [(b, t) for b in 'UDFB' for t in (1, 3, 2)]
    for first, end in sorted(itertools.product(free, last), key=lambda fe: (fe[0] is not None) + (fe[1] is not None)):
        mid = ([] if first is None else fc.invert([first])) + q + ([] if end is None else fc.invert([end]))
        for m in rots:                                                                # other ways to write the same state
            back = {v: k for k, v in m.items()}
            for inv in (False, True):
                seq = [(m[b], t) for b, t in (fc.invert(mid) if inv else mid)]
                z = fc.parse(kociemba.solve(facelets(fc.apply(fc.solved(), seq))))
                inner = ([] if first is None else [first]) + [(back[b], t) for b, t in (z if inv else fc.invert(z))] + ([] if end is None else [end])
                ax = [AXIS[b] for b, _ in inner]
                if (ax[0] != AXIS['F'] and ax[-1] != AXIS['R'] and all(x[0] != y[0] for x, y in zip(inner, inner[1:]))
                        and not any(ax[j] == ax[j + 1] == ax[j + 2] for j in range(len(ax) - 2))):
                    s = f'{PAD} {text(inner)} {PAD}'
                    assert fc.apply(fc.solved(), fc.parse(s)) == target
                    return s
    raise RuntimeError('no way to write it')
def scrambles():
    if not os.path.exists(SCR):
        sys.path.insert(0, '/data/fmc/eo-to-dr/research/src'); import canon
        raw = subprocess.run(['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=5G', MKSCR, 'mkscr', str(N_RUN), str(SCR_SEED)],
                             capture_output=True, text=True, check=True).stdout.strip().split('\n')
        assert len(raw) == N_RUN and len(set(raw)) == N_RUN
        rots = rotations()
        with open(SCR, 'w') as f:
            f.write(f"# {N_RUN} uniformly random states, drawn by the eo-to-dr study's `eodrtools mkscr {N_RUN} {SCR_SEED}` (adjacent turns of one face merged), "
                    f"each written with R' U' F at both ends (inner part: two-phase solver, python package kociemba) and replayed to the same state; "
                    f"the first {N_PAGE} are on the examples page. The earlier nissy 2.0.8 scrambles (not uniform) are in attempt_scrambles_nissy.txt\n")
            for r in raw:
                m = canon.simplify(r)
                assert canon.simplify(m) == m and fc.apply(fc.solved(), fc.parse(m)) == fc.apply(fc.solved(), fc.parse(r))
                w = fmc_scramble(fc.parse(m), rots)
                assert canon.simplify(w) == w and fc.apply(fc.solved(), fc.parse(w)) == fc.apply(fc.solved(), fc.parse(r))
                f.write(w + '\n')
        print(f'drew {N_RUN} scrambles into {SCR}')
    out = [l.strip() for l in open(SCR) if l.strip() and not l.startswith('#')]
    assert len(out) == N_RUN and len(set(out)) == N_RUN
    return out

def selfcheck(scr):
    """The fast simulator and DR reader against fmccube, on every DR up to 10 moves of the first three scrambles."""
    n = 0
    for s in scr[:3]:
        ps = perm(fc.parse(s))
        assert as_dict(ps) == fc.apply(fc.solved(), fc.parse(s))
        for nm, im, axis in cubelib(s, 10):
            p = state(ps, nm, im); st = fc.state_after(s, niss(nm, im))
            assert as_dict(p) == st
            for name, V in VIEWS.items():
                slow = fc.to_dr_arrays(st if VIEW_ROT[name] is None else fc.conj_rotation(st, VIEW_ROT[name]))
                fast = V.arrays(p)
                assert (slow is None and fast is None) or tuple(map(list, slow)) == tuple(fast), (s, niss(nm, im), name)
            assert VIEWS[axis].arrays(p) is not None
            n += 1
    print(f'selfcheck: fast simulator agrees with fmccube on {n} DRs (3 scrambles, 3 axes each)')

# ---- the page
def pick(recs, idx):
    """The rows of one scramble: up to four DRs of 10 moves or less (shortest first), then 11-movers, drawn at random."""
    rng = random.Random(SEED * 1000 + idx); recs = sorted(recs, key=lambda r: (r['length'], niss(r['n'], r['i']), r['axis']))
    short = [r for r in recs if r['length'] <= 10]; rest = [r for r in recs if r['length'] > 10]
    rng.shuffle(short); rng.shuffle(rest); short.sort(key=lambda r: r['length']); rest.sort(key=lambda r: r['length'])
    rows = short[:SHOWN // 2]; rows += rest[:SHOWN - len(rows)]; rows += short[SHOWN // 2:SHOWN // 2 + SHOWN - len(rows)]
    return sorted(rows, key=lambda r: r['length'])
def says(r): return 'look anyway' if r['length'] <= 10 else 'drop' if r['drop'] else 'keep'
def odds(r):
    h = pv.q(cs=r['cs'], e=r['e'], pairs=min(r['tp'], 5), both=({r['a']}, {r['b']}))
    assert sum(h) > 0 and h[r['opt']] > 0, r
    return pv.tri(h)
def judge(rows):
    """(best solution over the rows, its rows, best over what you'd still finish with the list, its rows)."""
    best = min(r['total'] for r in rows); left = [r for r in rows if says(r) != 'drop']
    bl = min((r['total'] for r in left), default=None)
    return best, [k for k, r in enumerate(rows) if r['total'] == best], bl, [k for k, r in enumerate(rows) if says(r) != 'drop' and r['total'] == bl]
def plural(n, word): return f'{n} {word}' if n == 1 else f'{n} {word}s'
def verdict_line(rows, solution):
    best, wb, bl, wl = judge(rows); long = [r for r in rows if r['length'] > 10]; nd = sum(r['drop'] for r in long)
    w = wl[0] if bl == best else wb[0]
    ties = [k for k in wb if k != w]
    names = [str(k + 1) for k in ties]
    tied = f" (DR {names[0] if len(names) == 1 else ', '.join(names[:-1]) + ' and ' + names[-1]} {'ties' if len(names) == 1 else 'tie'} it)" if ties else ''
    s = f"Best on the page: **{best} moves**, from DR {w + 1}{tied}: `{solution}`. "
    if not long: return s + 'No DR of 11 moves or more here, so the list has nothing to say.'
    s += f"The list drops {nd} of the {plural(len(long), 'DR')} of 11 moves or more"
    if bl == best:
        return s + (f", and the best one is {rows[w]['length']} moves long, so you'd finish it anyway." if rows[w]['length'] <= 10 else ', and keeps the best one.' if nd else ', so the best one stays.')
    if bl is None: return s + ', which is all there is on the page.'
    return s + f", the best one among them. What's left gives {bl} (DR {wl[0] + 1}), {plural(bl - best, 'move')} more."

def best_solution(scramble, r):
    """The solution behind r['total'], written out and checked on the sticker simulator."""
    V = VIEWS[r['axis']]; vn, vi = r['best']
    kv = dr.read_states([' '.join(map(str, r['best_st'][0] + r['best_st'][1] + r['best_st'][2]))])[0]
    finish = [(V.face_back[b], t) for b, t in fc.parse(kv['optimal_finish'])]
    sol = list(vn) + finish + fc.invert(vi)
    assert len(sol) == r['total'] and fc.apply(fc.solved(), fc.parse(scramble) + sol) == fc.solved(), (scramble, r)
    assert all(x[0] != y[0] for x, y in zip(sol, sol[1:]))
    return text(sol)

def guide_list():
    """The five lines of the prune list, as the write-up's guide has them."""
    g = open(GUIDE).read(); a = g.index('**The short version for an 11-move DR**'); b = g.index('What that does', a)
    lines = [l for l in g[a:b].split('\n') if l.startswith('- **')]
    assert len(lines) == 5 and '{=' not in ''.join(lines)
    return lines

HEAD = ['Each row is one DR you could have on the page:', '', '| DR | Moves to DR | Length, moves | Axis | Subset | True pairs |', '|---:|---|---:|---|---|---:|']
RHEAD = ['The same DRs: the corner case on each side, what the list says, and the share of DR states with the same reads that finish in 10, 11 and 12 or less:', '',
         '| DR | Corner case, normal | Corner case, inverse | The list says | Same reads: in 10 | Same reads: in 11 | Same reads: in 12 |', '|---:|---|---|---|---:|---:|---:|']
AHEAD = ['Each row is a DR from above, with its true shortest HTR on each side and its optimal finish and solution, in moves:', '',
         '| DR | Shortest HTR, normal | Shortest HTR, inverse | Optimal finish | Solution |', '|---:|---:|---:|---:|---:|']
def block(k, scramble, recs, rows, names, solution):
    cnt = {}
    for r in recs: cnt[r['length']] = cnt.get(r['length'], 0) + 1
    out = [f'#### Scramble {k + 1}', '', '```', f'{scramble} // scramble', '```', ''] + HEAD
    for j, r in enumerate(rows):
        out.append(f"| {j + 1} | `{niss(r['n'], r['i'])}` | {r['length']} | {r['axis']} | {r['cs']} {r['e']}e | {r['tp']} |")
    out += [''] + RHEAD
    for j, r in enumerate(rows):
        out.append(f"| {j + 1} | {names[r['a']]} | {names[r['b']]} | {says(r)} | {odds(r).replace(' / ', ' | ')} |")
    cap = max(cnt)
    out += ['', f"Shown: {len(rows)} of the {plural(len(recs), 'DR')} up to {cap} moves (" + '; '.join(f"{L} moves: {sum(r['length'] == L for r in rows)} of {cnt[L]}" for L in sorted(cnt)) + ').', '',
            '<details>', f'<summary>Answers for scramble {k + 1}</summary>', ''] + AHEAD
    for j, r in enumerate(rows):
        out.append(f"| {j + 1} | {r['hn']} | {r['hi']} | {r['opt']} | {r['total']} |")
    out += ['', verdict_line(rows, solution), '', '</details>', '']
    return out

def avg(xs): xs = list(xs); return sum(xs) / len(xs)
def tally_page(pages):
    """The table for the rows printed on the page."""
    rows = [r for _, _, rs in pages for r in rs]; long = [r for r in rows if r['length'] > 10]; J = [judge(rs) for _, _, rs in pages]
    lost = [(bl - b) for b, _, bl, _ in J if bl is not None and bl != b]; gone = sum(bl is None for _, _, bl, _ in J)
    t = ['| What | On the page |', '|---|---:|',
         f'| Scrambles | {len(pages)} |', f'| DRs shown | {len(rows)} |',
         f"| of 10 moves or less (you'd finish these anyway) | {len(rows) - len(long)} |",
         f'| of 11 moves or more | {len(long)} |',
         f"| of those, dropped by the list | {sum(r['drop'] for r in long)} ({pv.fmt(sum(r['drop'] for r in long), len(long))}) |",
         f'| DRs to finish per scramble, without the list | {avg(len(rs) for _, _, rs in pages):.1f} |',
         f"| DRs to finish per scramble, with the list | {avg(sum(says(r) != 'drop' for r in rs) for _, _, rs in pages):.1f} |",
         f'| Best solution on the page, average, finishing every DR shown | {avg(b for b, _, _, _ in J):.2f} |',
         f"| Best solution on the page, average, finishing what the list leaves | {avg(bl for _, _, bl, _ in J if bl is not None):.2f}{f' ({gone} scrambles left with nothing)' if gone else ''} |",
         f"| Scrambles where the list drops the page's best solution | {len(lost) + gone} of {len(pages)} |",
         f'| Moves lost on those, average | {avg(lost):.2f} |' if lost else '| Moves lost on those, average | none lost |']
    return t
def load_run():
    with open(RUN) as f:
        rd = csv.reader(l for l in f if not l.startswith('#')); head = next(rd)
        assert head == RUN_HEAD
        return [dict(zip(head, map(int, row))) for row in rd]
def tally_run(run):
    out = []; have = [x for x in run if x['n9'] + x['n10'] > 0]; n = len(have)
    pol = [('every DR of 10 moves or less', lambda x: (x['n9'] + x['n10'], min(x['best9'], x['best10']))),
           ('those, and the 11-movers the list keeps', lambda x: (x['n9'] + x['n10'] + x['kept11'], min(x['best9'], x['best10'], x['best_kept11']))),
           ('those, and every 11-mover', lambda x: (x['n9'] + x['n10'] + x['n11'], min(x['best9'], x['best10'], x['best11']))),
           ('every DR of 10 moves or less, and the 11- and 12-movers the list keeps', lambda x: (x['n9'] + x['n10'] + x['kept11'] + x['kept12'], min(x['best9'], x['best10'], x['best_kept11'], x['best_kept12']))),
           ('every DR up to 12 moves', lambda x: (x['n9'] + x['n10'] + x['n11'] + x['n12'], x['best']))]
    if n < len(run):
        out += [f"{len(run) - n} of the {len(run)} scrambles have no DR of 10 moves or less of this kind. This table leaves them out, so every row is about the same {n} scrambles. Each row is a set of DRs you finish, with how many that is and the best solution it gives.", '']
    out += ['| You finish | DRs to finish per scramble | Best solution, average moves | Scrambles where that is the best there is |', '|---|---:|---:|---:|']
    v = [[f(x) for x in have] for _, f in pol]
    for (name, _), col in zip(pol, v):
        assert all(b < 99 for _, b in col)
        out.append(f"| {name} | {avg(c for c, _ in col):,.0f} | {avg(b for _, b in col):.2f} | {pv.fmt(sum(b == x['best'] for (_, b), x in zip(col, have)), n)} |")
    c = [avg(c for c, _ in col) for col in v]; r = [avg(b for _, b in col) for col in v]
    out += ['', f"So the list on the 11-movers takes the DRs to finish from {c[2]:,.0f} to {c[1]:,.0f} per scramble and the average result from {r[2]:.2f} to {r[1]:.2f}. "
            f"On the 12-movers as well it takes {c[4]:,.0f} to {c[3]:,.0f}, and {r[4]:.2f} to {r[3]:.2f}.", '',
            'And by the length of the DR, over all ' + str(len(run)) + ' scrambles. "Reaches the best" means its solution is as short as the best one over all of that scramble\'s DRs up to 12 moves. '
            'The list is meant for 11 moves and up; the first two rows show what it would do if you used it on shorter DRs too. Each row is a DR length:', '',
            '| DR length | DRs per scramble | Scrambles where one of them reaches the best | The list drops | Kept DRs that reach the best | Dropped DRs that reach the best |', '|---|---:|---:|---:|---:|---:|']
    for cl in CLASSES:
        N = sum(x[f'n{cl}'] for x in run); K = sum(x[f'kept{cl}'] for x in run); Rr = sum(x[f'reach{cl}'] for x in run); Rk = sum(x[f'reach_kept{cl}'] for x in run)
        out.append(f"| {'9 or less' if cl == 9 else cl} | {N / len(run):,.1f} | {pv.fmt(sum(x[f'reach{cl}'] > 0 for x in run), len(run))} | {pv.fmt(N - K, N)} | {pv.fmt(Rk, K)} | {pv.fmt(Rr - Rk, N - K)} |")
    r11 = (sum(x['reach11'] for x in run), sum(x['reach_kept11'] for x in run)); r12 = (sum(x['reach12'] for x in run), sum(x['reach_kept12'] for x in run))
    out += ['', f"In counts: of the {r11[0]:,} 11-movers that reach their scramble's best solution the list keeps {r11[1]:,}, and of the {r12[0]:,} 12-movers it keeps {r12[1]:,}."]
    return out

def build(rerun):
    scr = scrambles(); selfcheck(scr); names = dr.corner_names(); CC = pv.corner_cases()
    have = os.path.exists(RUN) and not rerun
    jobs = [(k, s, not have) for k, s in enumerate(scr) if not have or k < N_PAGE]
    page = {}; runrows = {}
    with multiprocessing.Pool(4) as pool:
        for done, (k, row, recs) in enumerate(pool.imap_unordered(work, jobs, chunksize=2)):
            if row is not None: runrows[k] = row
            if recs is not None: page[k] = recs
            if (done + 1) % 50 == 0: print(f'  {done + 1} of {len(jobs)} scrambles', flush=True)
    if not have:
        with open(RUN, 'w') as f:
            f.write(f'# every EO-first DR up to {CAP} moves of each scramble in attempt_scrambles.txt (cubelib-cli steps "{STEPS}"), by DR length class\n'
                    f'# ({CLASSES[0]} = {CLASSES[0]} or less): how many, how many the prune list keeps, best solution over all / over the kept ones (99 = none),\n'
                    '# and how many reach the scramble\'s best solution (all / kept).  Written by many_examples.py --rerun.\n')
            w = csv.writer(f); w.writerow(RUN_HEAD)
            for k in range(N_RUN): w.writerow([k + 1] + runrows[k])
        print(f'wrote {RUN}')
    run = load_run(); assert len(run) == N_RUN
    pages = [(scr[k], page[k], pick(page[k], k)) for k in range(N_PAGE)]
    sols = []
    for s, recs, rows in pages:
        best, wb, bl, wl = judge(rows); sols.append(best_solution(s, rows[wl[0] if bl == best else wb[0]]))
    per11 = avg(x['n9'] + x['n10'] + x['n11'] for x in run)
    out = [START, '', '## 100 scrambles: which DRs would you finish?', '',
           f"A hundred random-state scrambles, written the way FMC scrambles are, and for each one some of the DRs you could have on your page. "
           "What you can read off each DR without solving is in the two tables. The answers are folded away under it: pick the DRs you'd finish, then open them.", '',
           f"**Where the DRs come from.** cubelib-cli (the solver behind Mallard) lists every DR that goes EO first (EOs of up to 5 moves; it doesn't list longer ones), with NISS, and then DR on normal or on inverse without breaking the EO, on all three axes. "
           f"A scramble has far more of those than anyone writes down: {per11:,.0f} up to 11 moves on average over the {N_RUN} scrambles of the tally at the end. "
           f"Each scramble shows at most {SHOWN} of them: up to {SHOWN // 2} of 10 moves or less, shortest first, then 11-movers, drawn at random where there are more. Nothing was picked by how it finishes.", '',
           "**What you're testing.** You finish a DR of 10 moves or less whatever it looks like. The 11-movers are where you need a quick way to say no, and that's what the short list in the write-up's guide is for. It needs no solving:", '']
    out += guide_list() + ['',
           '**The answers are the answer key**, not what a person finds in an hour: the true shortest HTR on each side, the optimal finish in DR moves, and the shortest solution through that DR.', '',
           '### How to read the tables', '',
           '- **Moves to DR**: brackets are moves on inverse. The last move on each side is written clockwise, and the row is about that DR exactly as written.',
           '- **Length**: the number of moves to DR. **Axis**: the axis the DR is on.',
           '- **Subset**: corner subset and number of bad edges, the way you already name it.',
           '- **True pairs**: a corner and an edge next to each other in one of the two layers of the DR axis, both touching stickers matching.',
           "- **Corner case, normal** and **inverse**: where the bad corners sit on each side, by the names in the table below (the same names as in the write-up's corner case appendix). Normal is the cube after the scramble and the unbracketed moves, with the bracketed ones as premoves the usual way. Inverse is the other side.",
           "- **The list says**: `keep` or `drop` for a DR of 11 moves or more. A DR of 10 moves or less says `look anyway`.",
           '- **Same reads: in 10, in 11, in 12**: of all DR states with that subset, that many true pairs (five or more count as one) and those two corner cases, the share whose optimal finish is 10 or less, 11 or less, 12 or less. 0 means none. An 11-move DR needs one of the first two.',
           '- **Shortest HTR, normal** and **inverse** (answers): the true shortest on each side.',
           '- **Optimal finish** (answers): the optimal finish in DR moves of the DR as written.',
           "- **Solution** (answers): the shortest solution through that DR, which is DR + finish less whatever cancels where the finish meets the DR. R then R2 is R', so a last move that is better turned the other way saves a move.", '',
           '### The corner cases', '',
           '"A qt takes it straight to" is the subset you are in after the right quarter turn of a layer, when one lowers the corner qt count with no setup. L is the range of optimal corner solutions. Each row is one corner case:', '',
           '| Corner case | Bad corners | L | A qt takes it straight to |', '|---|---|---|---|']
    for cs in pv.CS_ORDER:
        for k in sorted(pv.cases(cs), key=lambda k: int(names[k].split('-')[1])):
            c = CC[k]; sub = f" ({c['sub']})" if c['sub'] != cs else ''
            out.append(f"| {names[k]}{sub} | {c['layout']}{TELL.get(k, '')} | {c['lmin']}–{c['lmax']} | {c['straight'] or 'nothing, needs a setup'} |")
    out += ['', '### The scrambles', '']
    for k, ((s, recs, rows), sol) in enumerate(zip(pages, sols)): out += block(k, s, recs, rows, names, sol)
    out += ['### The tally', '',
            'First the rows printed above, with every DR finished optimally. Each row is one count over the 100 scrambles:', ''] + tally_page(pages) + ['',
            f'The page shows a handful of DRs per scramble. The same count over every DR up to {CAP} moves, for {N_RUN} scrambles (the 100 above are the first of them), '
            'says what there is to find and what the list does to it. Nobody finishes hundreds of DRs in an hour, so read the second column as the size of the haystack. '
            f'"The best there is" is the shortest solution over all of a scramble\'s DRs up to {CAP} moves, each finished optimally; the list is used on DRs of 11 moves and up only.', ''] + tally_run(run) + ['',
            f"Over all DR states the list drops {fillenv.PRUNE('drop')} and loses {fillenv.PRUNE('lose', 11)} of the finishes in 11 or less (write-up, guide). "
            'Every finish here is the optimal one: the answer key, not what you find by hand.', '', END]
    text_ = open(PAGE).read()
    assert text_.count(START) == 1 and text_.count(END) == 1, 'markers missing in EXAMPLES.md'
    a = text_.index(START); b = text_.index(END) + len(END)
    open(PAGE, 'w').write(text_[:a] + '\n'.join(out) + text_[b:])
    print(f'wrote {len(pages)} scrambles, {sum(len(rs) for _, _, rs in pages)} DRs to {PAGE}')

def verify():
    """Re-read everything printed in the section from the page's text alone: slow simulator, full drtools read."""
    names = dr.corner_names(); page = open(PAGE).read(); region = page[page.index(START):page.index(END)]
    blocks = re.split(r'^#### Scramble (\d+)$', region, flags=re.M)[1:]
    bad = 0; nrows = 0; nsol = 0; todo = []
    for num, body in zip(blocks[0::2], blocks[1::2]):
        scramble = re.search(r'^```\n(.+?) // scramble\n```$', body, re.M).group(1)
        look = re.findall(r"^\| (\d+) \| `([^`]+)` \| (\d+) \| (\S+) \| (\S+) (\d)e \| (\d+) \|$", body, re.M)
        reads = re.findall(r"^\| (\d+) \| (\S+) \| (\S+) \| (look anyway|keep|drop) \| (\S+) \| (\S+) \| (\S+) \|$", body, re.M)
        assert len(look) == len(reads) and all(a[0] == b[0] for a, b in zip(look, reads)), num
        rows = [a + b[1:4] + (' / '.join(b[4:]),) for a, b in zip(look, reads)]
        ans = re.findall(r'^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$', body, re.M)
        best = re.search(r'^Best on the page: \*\*(\d+) moves\*\*, from DR (\d+)(?: \([^)]*\))?: `([^`]+)`\.', body, re.M)
        assert rows and len(rows) == len(ans) and best, num
        assert scramble.startswith(PAD + ' ') and scramble.endswith(' ' + PAD)
        todo.append((num, scramble, rows, ans, best))
    # all states: each DR as written, and its merged endings
    states = []; index = []
    for num, scramble, rows, ans, best in todo:
        for row in rows:
            n, i = fc.split_niss(row[1]); axis = row[3]; f = VIEW_ROT[axis]; mine = []
            for vn, vi in variants(n, i, axis):
                st = fc.state_after(scramble, niss(vn, vi))
                arr = fc.to_dr_arrays(st if f is None else fc.conj_rotation(st, f))
                mine.append((len(vn) + len(vi), None if arr is None else len(states)))
                if arr is not None: states.append(' '.join(map(str, arr[0] + arr[1] + arr[2])))
            index.append(mine)
    kvs = dr.read_states(states); k = 0
    for num, scramble, rows, ans, best in todo:
        tots = []
        for row, an in zip(rows, ans):
            mine = index[k]; k += 1; nrows += 1
            j, seq, length, axis, cs, e, tp, cn, ci, say, od = row
            if any(x is None for _, x in mine):
                bad += 1; print('NOT A DR', num, row); tots.append(None); continue
            kv = kvs[mine[0][1]]; n, i = fc.split_niss(seq)
            kcs, ke = kv['subset'].split(); a, b = kv['corner_case'].split(); hn, hi = map(int, kv['htr'].split()); ktp = int(kv['true_pairs'].split()[0])
            total = min(L + int(kvs[x]['optimal']) for L, x in mine); tots.append(total)
            drop = bool(fillenv._dropped(kcs, int(ke[0]), a, b, ktp, min(hn, hi), max(hn, hi)))
            want = 'look anyway' if len(n) + len(i) <= 10 else 'drop' if drop else 'keep'
            h = pv.q(cs=kcs, e=int(ke[0]), pairs=min(ktp, 5), both=({a}, {b}))
            ok = (an[0] == j and niss(canon(n), canon(i)) == seq and len(n) + len(i) == int(length) and kcs == cs and ke[0] == e and ktp == int(tp) and names[a] == cn and names[b] == ci
                  and want == say and pv.tri(h) == od and (hn, hi) == (int(an[1]), int(an[2])) and int(kv['optimal']) == int(an[3]) and total == int(an[4]))
            if not ok:
                bad += 1; print('MISMATCH', num, row, an, kv)
        sol = fc.parse(best.group(3)); nsol += 1
        if not (fc.apply(fc.solved(), fc.parse(scramble) + sol) == fc.solved() and len(sol) == int(best.group(1)) == min(t for t in tots if t is not None) == tots[int(best.group(2)) - 1]):
            bad += 1; print('BAD SOLUTION', num, best.group(0))
    print(f're-read {len(todo)} scrambles from the page: {nrows} DRs (each a DR on its stated axis; subset, pairs, corner cases, list verdict, odds, HTR lengths, '
          f'optimal finish and solution recomputed) and {nsol} written-out solutions applied to their scrambles: {bad} mismatches')
    return bad

if __name__ == '__main__':
    if '--verify-only' not in sys.argv: build('--rerun' in sys.argv)
    sys.exit(1 if verify() else 0)

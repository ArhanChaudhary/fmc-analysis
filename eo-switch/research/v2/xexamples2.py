#!/usr/bin/env python3
"""report/EXAMPLES.md for the v2 cards (cards.py): about 200 real attempts (scramble, EO, RZP to a total of 5) from
the study's uniformly random scrambles (out/scrambles.txt), spread over the groups of the cards and random within a
group.  Each is turned so that its EO is F/B and its DR U/D, shows the bad pieces of the cube you are on in colours,
the reads the card of its DRM needs, and, folded away, the card's verdict next to the pairs rule's and an optimal
EO-kept DR on the other side.

The attempts come from `eoswtools att` (out/big/att_examples.tsv: every attempt of the first 40 scrambles).  Card
groups with too few attempts there are topped up from scrambles 40 to 1239 (out/examples_extra.tsv, written by this
script with the same sampler the first time it runs).

Every line is replayed on is-dr-xs-worth-it's sticker model (cube.py): the turned scramble is the same cube after a
rotation, EO + RZP gives the stated DRM with the EO solved, the switched case is the attempt's recorded case, every
read done on the side you are on (trace2.reads and the per-edge pair counts here) equals the feature of the inverse,
the card group is the one cards.py puts the case in, and the DR solves the other side to DR on U/D with the F/B EO
kept in the table's number of moves; nissy 2.0.8 (`solve drud-eofb`) gives the same length.  The page states the
number of checks; the script stops on any mismatch.   usage: xexamples2.py"""
import os, sys, csv, json, random, collections, subprocess, re, tempfile, shutil
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'src'))
from lib import F, d, N0, drm_mask
import cards as C
import trace2, geom
from geom import cube
from halfup import hu
OUT = os.path.join(HERE, '..', 'out'); PAGE = os.path.join(HERE, '..', '..', 'report', 'EXAMPLES.md')
RES = json.load(open(os.path.join(HERE, 'out', 'results.json')))
EXTRA = os.path.join(HERE, 'out', 'examples_extra.tsv')
CHECKS = [0]; BAD = []
def check(ok, what):
    CHECKS[0] += 1
    if not ok: BAD.append(what)
def pc(x): return f'{hu(x, 1, 100):.1f}%' if x >= 0.01 else f'{hu(x, 2, 100):.2f}%'
def pl(n, w): return f'{n} {w}' + ('' if n == 1 else 's')

# ---------------------------------------------------------------- card groups and the rules they are compared with
NAME = lambda drm: f'{drm[0]}c{drm[1]}e'
GID = {}
for drm, groups in C.CARDS.items():
    g_ = np.full(N0, -1, np.int32)
    for i, (label, g, v) in enumerate(groups): g_[g] = i
    GID[NAME(drm)] = g_
DRM_OF = {NAME(k): k for k in C.CARDS}
def fanti(drm):
    for key, nm, who, sw in C.BASE[drm]:
        if key.startswith('pairs+arm') and who == 'Fanti': return nm, sw
    return None
# how many examples of each card group (group index -> number)
QUOTA = {'4c4e': {0: 8, 1: 12, 2: 8, 3: 6, 4: 8, 5: 6, 6: 5, 7: 8, 8: 8, 9: 4, 10: 5, 11: 6, 12: 6},
         '4c2e': {0: 5, 1: 7, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3},
         '3c2e': {0: 6, 1: 8, 2: 6},
         '7c8e': {0: 4, 1: 7, 2: 5, 3: 3, 4: 4, 5: 3, 6: 1, 7: 3},
         '8c8e': {0: 1, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 7: 1},
         '2c2e': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
         '4c6e': {0: 1, 1: 1, 3: 1, 4: 1},
         '3c4e': {0: 1, 2: 1, 3: 1, 5: 1},
         '3c6e': {0: 1, 1: 1, 3: 1},
         '5c4e': {0: 1, 1: 1, 4: 1},
         '5c6e': {0: 1, 2: 1},
         '6c6e': {0: 1, 1: 1}}

# ---------------------------------------------------------------- candidates
def length5(path):
    for r in csv.DictReader(open(path), delimiter='\t'):
        if int(r['length']) == 5 and r['drm_normal'] in QUOTA: yield r
main_rows = list(length5(os.path.join(OUT, 'big', 'att_examples.tsv')))
cand = collections.defaultdict(list)
for r in main_rows:
    cand[(r['drm_normal'], int(GID[r['drm_normal']][int(r['ix_switched'])]))].append(r)
THIN = {(drm, g) for drm, q in QUOTA.items() for g, n in q.items() if len({r['scr'] for r in cand[(drm, g)]}) < n + 2}
def make_extra(first=40, last=1240, step=40):
    """The same sampler on scrambles first..last-1, kept only for the thin groups (length 5)."""
    binary = os.path.join(HERE, '..', 'eoswtools', 'target', 'release', 'eoswtools')
    tmp = tempfile.mkdtemp(dir='/data/fmc/tmp'); keep = []; header = None
    try:
        for a in range(first, last, step):
            pre = os.path.join(tmp, 'x')
            subprocess.run([binary, 'att', os.path.join(OUT, 'big', 'd.u8'), os.path.join(OUT, 'scrambles.txt'), str(a), str(step), pre, str(step)], check=True, capture_output=True)
            with open(pre + '_examples.tsv') as f:
                header = f.readline()
                for line in f:
                    p = line.rstrip('\n').split('\t')
                    if p[6] == '5' and p[7] in QUOTA and (p[7], int(GID[p[7]][int(p[9])])) in THIN: keep.append(line)
    finally:
        shutil.rmtree(tmp)
    with open(EXTRA, 'w') as f:
        f.write(header); f.writelines(keep)
if not os.path.exists(EXTRA): make_extra()
for r in length5(EXTRA):
    k = (r['drm_normal'], int(GID[r['drm_normal']][int(r['ix_switched'])]))
    if k in THIN: cand[k].append(r)

rng = random.Random(20261116)
chosen = []; SHORT = []
for drm, q in QUOTA.items():
    for g, n in q.items():
        c = cand[(drm, g)][:]; rng.shuffle(c)
        seen = set(); got = []
        for r in c:                                   # one attempt per scramble and group where there are enough
            if r['scr'] in seen: continue
            seen.add(r['scr']); got.append(r)
            if len(got) == n: break
        for r in c:                                   # rare groups: a second attempt from the same scramble, another case
            if len(got) == n: break
            if r not in got and not any(x['scr'] == r['scr'] and x['ix_switched'] == r['ix_switched'] for x in got): got.append(r)
        if len(got) < n: SHORT.append((drm, C.CARDS[DRM_OF[drm]][g][0], n, len(got)))
        chosen += [(drm, g, r) for r in got]

# ---------------------------------------------------------------- frames: rotations taking (EO axis, DR axis) to (F/B, U/D)
ROTS = ['', 'x', 'x2', "x'", 'y', 'y2', "y'", 'z', 'z2', "z'"] + [a + ' ' + b for a in ('x', 'x2', "x'") for b in ('y', 'y2', "y'", 'z', "z'")]
FACES = 'UDRLFB'; AX = {'U': 'UD', 'D': 'UD', 'R': 'RL', 'L': 'RL', 'F': 'FB', 'B': 'FB'}
def conj(rot):
    r = cube.do(cube.SOLVED, rot); ri = cube.do(cube.SOLVED, ' '.join(cube.inv_seq(rot))) if rot else cube.SOLVED
    return lambda s: cube.compose(cube.compose(ri, s), r)
def facemap(rot):
    cj = conj(rot); m = {}
    for f in FACES:
        img = cj(cube.do(cube.SOLVED, f))
        m[f] = [g for g in FACES if cube.do(cube.SOLVED, g) == img][0]
    return m
FRAME = {}
for rot in ROTS:
    m = facemap(rot)
    for eo in ('UD', 'RL', 'FB'):
        for dr in ('UD', 'RL', 'FB'):
            if eo != dr and AX[m[eo[0]]] == 'FB' and AX[m[dr[0]]] == 'UD': FRAME.setdefault((eo, dr), []).append((rot, m))
assert len(FRAME) == 6
def relabel(seq, m): return ' '.join(m[t[0]] + t[1:] for t in seq.split())

# ---------------------------------------------------------------- what you see, in colours (white top, green front)
COL = {'U': 'white', 'D': 'yellow', 'F': 'green', 'B': 'blue', 'R': 'red', 'L': 'orange'}
ORDER = 'UDFBRL'
def cname(cols): return '-'.join(COL[c] for c in sorted(cols, key=ORDER.index))
CASE = 'abcd'
READS = {'4c4e': ('pairs', 'fake', 'side', 'arm', 'case', 'cols', 'holes', 'clayer'), '4c2e': ('pairs', 'side', 'arm', 'case'), '3c2e': ('pairs', 'fake', 'split'),
         '7c8e': ('pairs', 'arm'), '8c8e': ('pairs', 'arm'), '2c2e': ('pairs', 'side', 'arm'), '4c6e': ('pairs', 'arm', 'elayer', 'clayer'),
         '3c4e': ('pairs', 'fake', 'side', 'arm', 'holes'), '3c6e': ('pairs', 'fake', 'arm'), '5c4e': ('pairs', 'fake', 'side', 'arm'), '5c6e': ('pairs', 'side', 'arm'),
         '6c6e': ('pairs', 'fake', 'clayer')}
def see(s, drm, ix):
    """The bad pieces of the cube you are on and the reads the card needs, as text; every read is checked against the
    feature of the inverse (ix = the switched case)."""
    cs = trace2.corners(s); es = trace2.ud_edges_in_E(s); hs = trace2.E_edges_out(s); rd = trace2.reads(s)
    for k, v in rd.items(): check(v == int(F[trace2.TRUTH[k]][ix]), f'read {k}')
    per = [(cname((ud, sd)), sum(1 for top, sides, _ in cs if sides == frozenset((ud, sd)))) for ud, sd in es]
    check(sum(n for _, n in per) == int(F['pairs'][ix]) and sum(1 for _, n in per if n) == int(F['edges_paired'][ix]), 'pairs per edge')
    pieces = ['U/D edges in the E slice: ' + (', '.join(cname(e) for e in es) or 'none'),
              'Misoriented corners: ' + (', '.join(f'{cname(sides | {top})} showing {COL[top]}' for top, sides, _ in cs) or 'none'),
              'E-slice edges out of the slice: ' + (', '.join(cname(h) for h in hs) or 'none')]
    out = []
    for k in READS[drm]:
        if k == 'pairs':
            n = rd['pairs']
            if n == 0: out.append('0 pairs')
            elif len(es) == 1: out.append(pl(n, 'pair') + (' (a bar)' if n == 2 else ''))
            elif n == 1: out.append(f'1 pair (on {[e for e, k_ in per if k_][0]})')
            elif len(es) == 2 and n == 2: out.append('2 pairs, ' + ('one on each edge' if rd['edges_paired'] == 2 else f'both on {[e for e, k_ in per if k_][0]} (a bar)'))
            else: out.append(pl(n, 'pair') + (f" on {pl(rd['edges_paired'], 'edge')}" if drm == '4c6e' else '') + ' (' + ', '.join(f'{e} {k_}' for e, k_ in per if k_) + ')')
        elif k == 'fake': out.append(pl(rd['fake'], 'fake pair'))
        elif k == 'side': out.append(pl(rd['side'], 'side pair'))
        elif k == 'split': out.append(pl(rd['split_pairs'], 'split pair'))
        elif k == 'arm': out.append(f"ARM {rd['carm']}{rd['earm']}")
        elif k == 'case':
            suffix = rd['carm'] if rd['cc'] == 0 else min(rd['carm'], 4 - rd['carm'])
            check(suffix == int(F['case_suffix'][ix]), 'corner case suffix')
            out.append(f"4{CASE[rd['cc']]}-{suffix} corners")
        elif k == 'holes':
            common = hs[0] & hs[1]
            out.append({0: f'holes on one R/L face (both edges out of the slice have {COL[next(iter(common))]})' if common else '', 1: 'holes diagonal (the edges out of the slice share no colour)',
                        2: f'holes on one F/B face (both edges out of the slice have {COL[next(iter(common))]})' if common else ''}[rd['hole_cfg']])
        elif k == 'cols':
            if rd['cc'] == 0: out.append('in two columns (two twins)' if rd['cols_bad'] == 2 else 'not in two columns')
        elif k == 'elayer':
            out.append(('both bad edges in one layer' if len(es) == 2 else 'the three bad edges in one layer') if rd['edges_same_layer'] else ('bad edges in different layers' if len(es) == 2 else 'bad edges in both layers'))
        elif k == 'clayer':
            nu = sum(1 for _, _, cud in cs if cud == 'U')
            out.append(f'corners {nu} white, {len(cs) - nu} yellow')
    return pieces, ', '.join(out), rd

# ---------------------------------------------------------------- per example
scr = open(os.path.join(OUT, 'scrambles.txt')).read().split('\n')
EX = []
for drm, g, r in chosen:
    S0 = scr[int(r['scr'])]; side = int(r['side'])
    for rot, m in FRAME[(r['eo_axis'], r['dr_axis'])]:      # the rotation that gives the study's own frame (the case index)
        S = relabel(S0, m); eo = relabel(r['eo'], m); rzp = relabel(r['rzp'], m)
        st = S if side == 0 else ' '.join(cube.inv_seq(S))
        if geom.ix_of_state(cube.do(cube.SOLVED, ' '.join(x for x in (st, eo, rzp) if x))) == int(r['ix_normal']): break
    check(conj(rot)(cube.do(cube.SOLVED, S0)) == cube.do(cube.SOLVED, S), 'turned scramble')
    start = S if side == 0 else ' '.join(cube.inv_seq(S))
    here = cube.do(cube.SOLVED, ' '.join(x for x in (start, eo, rzp) if x))            # the cube after EO + RZP, the side you are on
    check(geom.eo_fb_ok(here), 'EO solved')
    check(len(eo.split()) + len(rzp.split()) == 5, 'total 5')
    ixn = geom.ix_of_state(here)
    check(f"{int(F['drm_c'][ixn])}c{int(F['drm_e'][ixn])}e" == drm and ixn == int(r['ix_normal']), 'DRM on the side you are on')
    sw = cube.inverse(here); ix = geom.ix_of_state(sw)
    check(ix == int(r['ix_switched']), 'switched case')
    check(f"{int(F['drm_c'][ix])}c{int(F['drm_e'][ix])}e" == drm, 'DRM after the switch')
    check(int(GID[drm][ix]) == g and bool(C.CARDS[DRM_OF[drm]][g][1][ix]), 'card group')
    pieces, reads, rd = see(here, drm, ix)
    dr = ' '.join(geom.path_to_dr(ix, F['d']))
    t = cube.do(sw, dr)
    check(geom.is_dr_ud(t) and geom.eo_fb_ok(t) and len(dr.split()) == d[ix] == int(r['d_switched']), 'DR replayed')
    check(all(mv[0] not in 'FB' or mv.endswith('2') for mv in dr.split()), 'EO kept')
    swseq = ' '.join(cube.inv_seq(' '.join(x for x in (start, eo, rzp) if x)))            # the other side, as a sequence from solved (for nissy)
    check(cube.do(cube.SOLVED, swseq) == sw, 'switched sequence')
    label, _, verdict = C.CARDS[DRM_OF[drm]][g]
    base = C.BASE[DRM_OF[drm]][0]; fa = fanti(DRM_OF[drm])
    EX.append(dict(drm=drm, g=g, label=label, verdict=verdict, S=S, side=side, eo=eo, rzp=rzp, ix=int(ix), pieces=pieces, reads=reads, dr=dr, n=len(dr.split()),
                   swseq=swseq, pairs_rule=bool(base[3][ix]), fanti=(None if fa is None else bool(fa[1][ix])), scr=int(r['scr'])))
# nissy: the same optimal length
cmds = ''.join(f"solve drud-eofb {e['swseq']}\n" for e in EX)
res = subprocess.run(['nissy', '-b'], input=cmds, capture_output=True, text=True, check=True).stdout.splitlines()
lens = []
for i, l in enumerate(res):
    if l.startswith('>>> Executing command'):
        j = i + 1
        while res[j].startswith('>>>'): j += 1
        lens.append(int(re.search(r'\((\d+)\)\s*$', res[j]).group(1)))
assert len(lens) == len(EX), (len(lens), len(EX))
for e, n in zip(EX, lens): check(n == e['n'], 'nissy length')
assert not BAD, collections.Counter(BAD).most_common(8)

# ---------------------------------------------------------------- order: by DRM section, shuffled inside (so the place gives nothing away)
SECTIONS = [('4c4e', ['4c4e']), ('4c2e', ['4c2e']), ('3c2e', ['3c2e']), ('7c8e', ['7c8e']), ('8c8e', ['8c8e']), ('2c2e', ['2c2e']),
            ('The low DRMs (4c6e, 3c4e, 3c6e, 5c4e, 5c6e, 6c6e)', ['4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e'])]
ordered = []
for title, drms in SECTIONS:
    part = [e for e in EX if e['drm'] in drms]; rng.shuffle(part)
    ordered.append((title, part))
k = 0
for title, part in ordered:
    for e in part: k += 1; e['no'] = k
EX = [e for _, part in ordered for e in part]
json.dump([{k_: v for k_, v in e.items() if k_ not in ('swseq',)} for e in EX], open(os.path.join(HERE, 'out', 'examples.json'), 'w'), indent=1)

# ---------------------------------------------------------------- the page
VERDICT = {'switch': 'switch', 'time': 'if you have time', 'skip': 'skip'}
def cls(n): return 0 if n <= 4 else 1 if n == 5 else 2 if n == 6 else 3
def tally(sel):
    c = [0, 0, 0, 0]
    for e in EX:
        if sel(e): c[cls(e['n'])] += 1
    return c
rows = [('Card: switch', lambda e: e['verdict'] == 'switch'), ('Card: if you have time', lambda e: e['verdict'] == 'time'), ('Card: skip', lambda e: e['verdict'] == 'skip'),
        ('Pairs rule: switch', lambda e: e['pairs_rule']), ('Pairs rule: skip', lambda e: not e['pairs_rule'])]
TALLY = {name: tally(sel) for name, sel in rows}
nums = lambda sel: ', '.join(str(e['no']) for e in EX if sel(e)) or 'none'
DIS = {'card_switch_pairs_skip': [e['no'] for e in EX if e['verdict'] == 'switch' and not e['pairs_rule']],
       'card_time_pairs_switch': [e['no'] for e in EX if e['verdict'] == 'time' and e['pairs_rule']],
       'card_skip_pairs_switch': [e['no'] for e in EX if e['verdict'] == 'skip' and e['pairs_rule']]}
def good(ns): return sum(1 for e in EX if e['no'] in set(ns) and e['n'] <= 6)
out = ['# Worked examples: when to switch an EO', '',
       'Examples to play along with [the write-up](index.html). Do the EO and RZP, look at the bad pieces, do the reads, decide, then open the answer.', '',
       f"These are {len(EX)} real attempts from uniformly random scrambles: an EO and an RZP that reach the DRM at 5 moves total, so a good switch is a DR in 6 or less on the other side (sub-7). They're spread over the groups of the cards, 4c4e most, and random within a group. Nothing is hand-picked. A handful of examples per group is a small sample, so the tallies below wobble. The exact numbers of each group are in the answers.", '',
       '**How to read it.**', '',
       '- Every attempt is turned so the EO is on F/B and the DR on U/D, like in the write-up. The scramble printed is the generated one with the faces renamed, so it is the same scramble held another way.',
       '- An EO and RZP in brackets were found on the inverse scramble. The DR is then on the other side, as usual with NISS.',
       '- Colours are for white top, green front: the U/D colours are white and yellow, F/B green and blue, R/L red and orange.',
       '- *What you see* is the cube after the EO and RZP, before you switch: the U/D edges sitting in the E slice, the misoriented corners with the colour each one shows on the U/D face, and the E-slice edges that are out of the slice.',
       '- *Reads* are what the card of that DRM asks for, all counted on the side you are on, the way the write-up traces them:',
       '  - a *pair* is a misoriented corner whose two side stickers are the two colours of a U/D edge in the E slice, and two pairs on one edge are a *bar*;',
       '  - a *fake pair* is a corner with both of that edge\'s colours that shows the edge\'s side colour on U/D;',
       '  - a *side pair* is a corner with both colours of an E-slice edge that is out of the slice, showing green or blue on U/D;',
       '  - *ARM* is the corners showing red or orange on U/D, then the U/D edges in the E slice with green or blue;',
       '  - the *holes* are where the E-slice edges that are out of the slice belong: on one R/L face if the two share red or orange, on one F/B face if they share green or blue, diagonal if they share nothing;',
       '  - 4a corners are *in two columns* when they are two twins, each a white corner and a yellow corner with the same two other colours (Evan\'s stacked corners);',
       '  - *bad edges in one layer* (4c6e) means the U/D edges in the E slice are all white or all yellow, and the corner count is the misoriented corners by their white or yellow sticker;',
       '  - a *split pair* (3c2e) is wen\'s ([12 Feb 2026](https://discord.com/channels/1007840975726575667/1007841273111117924/1471458126539526323)), read in colours: a U/D edge in the E slice and a misoriented corner with the same white or yellow and without the edge\'s other colour, where the edge has green or blue and the corner shows red or orange on U/D, or the other way round.',
       '- The answer has the card\'s group and verdict (**switch**, **if you have time** or **skip**), how big that group is and how its cases split by DR length (exact, every case of the DRM once), what the pairs rule says, what Fanti\'s pairs + ARM list says where there is one, and one optimal DR on the other side with the EO kept.', '',
       'The rules the card is put next to, one row per DRM. The pairs rules are the NISS column of rodneykinney\'s [*DRM Subsets Meta*](https://docs.google.com/document/d/1Jnd1Qy_6b1W5dR5fZQScloMoMPR2LCAF7VPrgeTaRgg) where it has one, with plain 5+ pairs for 7c8e and rodneykinney\'s decision tree for 8c8e ([2 Sep 2025](https://discord.com/channels/1007840975726575667/1007841335434285126/1412510225906401403)). The pairs + ARM lists are Fanti\'s ([6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436034830046466069), and [6 Nov 2025](https://discord.com/channels/1007840975726575667/1007841273111117924/1436042954501390401) for 3c4e and 3c6e). [The write-up](index.html) has who said what, with the quotes.', '',
       '| DRM | Pairs rule | From | Pairs + ARM list (Fanti) |', '|---|---|---|---|']
for drm in QUOTA:
    b = C.BASE[DRM_OF[drm]][0]; fa = fanti(DRM_OF[drm])
    out.append(f"| {drm} | {b[1]} | {b[2].replace('DRM Subsets Meta', '*DRM Subsets Meta*')} | {fa[0] if fa else 'none'} |")
out += ['', f'**Replay check.** Every move sequence here was replayed on a sticker model of the cube before the page was written: {CHECKS[0]:,} checks, 0 mismatches. The turned scramble is the generated one after a rotation. EO + RZP solves the F/B EO in 5 moves and gives the stated DRM. Every read done on the side you are on equals the same count taken on the other side directly. The card group is the one the case falls in. The DR takes the other side to DR on U/D with the EO kept, in the optimal number of moves, and nissy 2.0.8 finds the same length for all {len(EX)}.', '',
        f'**How these {len(EX)} came out.** One row per verdict, the columns are the examples by the length of the optimal DR after the switch:', '',
        '| Verdict | Examples | DR in 4 or less | DR in 5 | DR in 6 | DR in 7 or more | DR in 6 or less, expected from the groups\' exact rates |', '|---|---|---|---|---|---|---|']
def expected(sel):
    return sum(next(g['rate'] for g in RES['drm'][e['drm']]['groups'] if g['label'] == e['label']) for e in EX if sel(e))
for name, sel in rows:
    c = TALLY[name]; out.append(f'| {name} | {sum(c)} | {c[0]} | {c[1]} | {c[2]} | {c[3]} | {expected(sel):.0f} |')
out += ['', 'The examples are spread over the groups, not drawn the way attempts come up, so read the rows as what each verdict looks like, not as how often you get it. The last column is how many of the row\'s examples would have a DR in 6 or less if every group came out at its exact rate. This draw is short on the *if you have time* row.', '',
        '**Where the card and the pairs rule disagree.**', '',
        f"- Card switches, pairs rule skips ({pl(len(DIS['card_switch_pairs_skip']), 'example')}, {good(DIS['card_switch_pairs_skip'])} with a DR in 6 or less): {', '.join(map(str, DIS['card_switch_pairs_skip'])) or 'none'}.",
        f"- Card says if you have time, pairs rule switches ({pl(len(DIS['card_time_pairs_switch']), 'example')}, {good(DIS['card_time_pairs_switch'])} with a DR in 6 or less): {', '.join(map(str, DIS['card_time_pairs_switch'])) or 'none'}.",
        f"- Card skips, pairs rule switches ({pl(len(DIS['card_skip_pairs_switch']), 'example')}, {good(DIS['card_skip_pairs_switch'])} with a DR in 6 or less): {', '.join(map(str, DIS['card_skip_pairs_switch'])) or 'none'}.", '']
GR = {drm: RES['drm'][drm]['groups'] for drm in QUOTA}
for title, part in ordered:
    out += [f"## {title}: examples {part[0]['no']}–{part[-1]['no']}", '']
    for drm in [x for x in QUOTA if x in {e['drm'] for e in part}]:
        X = RES['drm'][drm]
        out += [f"The {drm} card, one row per group, best first. *Sub-7* is the share of the group with a DR in 6 or less after the switch (exact, every case of {drm} once; {pc(X['sub7'])} for {drm} as a whole):", '',
                '| What you read | Verdict | Share of ' + drm + ' | Sub-7 |', '|---|---|---|---|']
        for g in X['groups']:
            out.append(f"| {g['label']} | {VERDICT[g['verdict']]} | {pc(g['share'])} | {pc(g['rate']) if 0 < g['rate'] < 1 else ('0%' if g['rate'] == 0 else '100%')} |")
        out.append('')
    for e in part:
        drm = e['drm']
        br = (lambda x: x) if e['side'] == 0 else (lambda x: f'({x})')
        moves = (f"EO `{br(e['eo'])}`, RZP `{br(e['rzp'])}`" if e['rzp'] else f"EO `{br(e['eo'])}`, no RZP needed") + ('' if e['side'] == 0 else ', on the inverse scramble')
        out += [f"**Example {e['no']} ({drm}).** `{e['S']}`", '', f"{moves}: {drm} in 5.", '', 'What you see:', ''] + ['- ' + p for p in e['pieces']] + ['', f"Reads: {e['reads']}.", '',
                '<details><summary>Verdict and the DR after the switch</summary>', '']
        g = GR[drm][e['g']]
        assert g['label'] == e['label'] and g['verdict'] == e['verdict']
        bad = g['d7'] + g['longer']; assert g['le4'] + g['d5'] + g['d6'] + bad == g['n']
        out += [f"Card: **{VERDICT[e['verdict']]}** (*{e['label']}*). That group is {pc(g['share'])} of {drm}, {g['n']:,} cases: {g['le4']:,} with a DR in 4 or less, {g['d5']:,} in 5, {g['d6']:,} in 6, {bad:,} in 7 or more.", '']
        line = f"Pairs rule, {C.BASE[DRM_OF[drm]][0][1]}: **{'switch' if e['pairs_rule'] else 'skip'}**."
        if e['fanti'] is not None: line += f" Fanti's pairs + ARM list: **{'switch' if e['fanti'] else 'skip'}**."
        er = ' '.join(x for x in (e['eo'], e['rzp']) if x)
        full = (f"`{er} ({e['dr']})`" if e['side'] == 0 else f"`({er}) {e['dr']}`")
        what = 'good' if e['n'] <= 6 else 'too long'
        out += [line, '', f"Optimal DR on the {'inverse' if e['side'] == 0 else 'normal side'}: `{e['dr']}` ({e['n']} moves, {what}). The whole attempt: {full}, {5 + e['n']} to DR.", '', '</details>', '']
open(PAGE, 'w').write('\n'.join(out))
by = collections.Counter(e['drm'] for e in EX); bv = collections.Counter(e['verdict'] for e in EX)
print(len(EX), 'examples,', CHECKS[0], 'checks, 0 mismatches ->', os.path.normpath(PAGE), os.path.getsize(PAGE), 'bytes')
print('per DRM', dict(by)); print('per verdict', dict(bv))
for name, _ in rows: print(name, TALLY[name])
print('disagree', {k_: (len(v), good(v)) for k_, v in DIS.items()})
print('short of the quota:', SHORT or 'none')
print('thin groups topped up from more scrambles:', sorted(THIN))

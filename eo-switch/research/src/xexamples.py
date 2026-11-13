#!/usr/bin/env python3
"""report/EXAMPLES.md: 200 real attempts (scramble, EO, RZP to a total of 5) from the study's uniform scrambles
(out/scrambles.txt; the example attempts of `eoswtools att`, out/big/att_examples.tsv), spread over the cells of the
switch cards.  Each is turned so that its EO is F/B and its DR U/D, shows what to trace on normal, the card's verdict,
the switched case's features, and an optimal EO-kept DR on the inverse written out.

Every line is replayed on is-dr-xs-worth-it's sticker model (cube.py): the turned scramble is the same cube seen
after a rotation (checked by conjugation), EO + RZP gives the stated DRM with the EO solved, the switched case is the
attempt's recorded case, each value traced on normal equals the feature of the inverse, and the DR solves the
inverse to DR on U/D with the F/B EO kept in the table's number of moves; nissy 2.0.8 (`solve drud-eofb`) gives the
same length.  The page states the count of checks and fails on any mismatch.  usage: xexamples.py"""
import os, sys, csv, random, collections, subprocess, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop, geom, features as fx
from halfup import hu
from geom import cube
import xtrace, niss_checks, rings, xtrace_rings, json
ZR = rings.load(); SIG = ZR['sigma'].astype(int); QSIG = ZR['qsig'].astype(int); HBAR = ZR['hbar'].astype(int)
RJ = json.load(open(os.path.join(HERE, '..', 'out', 'rings.json')))
F = pop.feat(); d = F['d'].astype(int)
OUT = os.path.join(HERE, '..', 'out'); PAGE = os.path.join(HERE, '..', '..', 'report', 'EXAMPLES.md')
CHECKS = [0]; BAD = []
def check(ok, what):
    CHECKS[0] += 1
    if not ok: BAD.append(what)
def pc(x): return f'{hu(x, 1, 100):.1f}%' if x >= 0.01 else f'{hu(x, 2, 100):.2f}%'

# ---------------------------------------------------------------- the card (same groups as xtables.RULES)
def card(ix):
    c, e = int(F['drm_c'][ix]), int(F['drm_e'][ix]); g = lambda k: int(F[k][ix])
    drm = f'{c}c{e}e'; ep, earm, carm, pairs, jzp, pph = g('edges_paired'), g('earm'), g('carm'), g('pairs'), g('jzp'), g('pairs_plus_half_side_x2')
    R = {'4c4e': [('switch', 'both bad U/D edges paired', ep == 2), ('your call', 'one paired, edge ARM 1', ep == 1 and earm == 1),
                  ('discard', 'one paired, edge ARM 0 or 2', ep == 1), ('discard', 'no bad edge paired', True)],
         '4c2e': [('switch', 'pairs + side pairs/2 is 1.5 or more', pph >= 3), ('your call', 'pairs + side pairs/2 is exactly 1', pph == 2), ('discard', 'pairs + side pairs/2 is 0 or 0.5', True)],
         '3c2e': [('switch', 'always', True)],
         '7c8e': [('switch', '5 or 6 pairs', pairs >= 5), ('your call', '4 pairs', pairs == 4), ('discard', '3 pairs or fewer', True)],
         '8c8e': [('your call', 'corner ARM 0, 4 or 8', carm in (0, 4, 8)), ('discard', 'corner ARM 2, 3, 5 or 6', True)],
         '2c2e': [('switch', 'a bad U/D edge with a pair', ep >= 1), ('your call', 'no pair, but JZP', jzp == 1), ('discard', 'no pair, not JZP', True)],
         '4c6e': [('switch', 'JZP', jzp == 1), ('your call', '4 pairs', pairs == 4), ('discard', 'anything else', True)],
         '3c4e': [('your call', '2 pairs', pairs == 2), ('discard', '0 or 1 pair', True)],
         '3c6e': [('discard', 'always', True)],
         '5c4e': [('your call', '3 pairs', pairs == 3), ('discard', '2 pairs or fewer', True)],
         '5c6e': [('your call', '4 pairs', pairs == 4), ('discard', '3 pairs or fewer', True)],
         '6c6e': [('your call', 'JZP, or 5 or 6 pairs', jzp == 1 or pairs >= 5), ('discard', 'anything else', True)]}
    for lab, txt, ok in R[drm]:
        if ok: return drm, lab, txt
# group rates (exact, uniform), for the verdict line
RATE = {}
rows = list(csv.DictReader(open(os.path.join(OUT, 'big', 'att_examples.tsv')), delimiter='\t'))
QUOTA = {('4c4e', 'switch'): 16, ('4c4e', 'your call'): 20, ('4c4e', 'discard'): 26,
         ('4c2e', 'switch'): 10, ('4c2e', 'your call'): 10, ('4c2e', 'discard'): 10,
         ('3c2e', 'switch'): 10, ('7c8e', 'switch'): 10, ('7c8e', 'your call'): 10, ('7c8e', 'discard'): 10,
         ('8c8e', 'your call'): 8, ('8c8e', 'discard'): 8, ('2c2e', 'switch'): 4, ('2c2e', 'discard'): 6,
         ('4c6e', 'switch'): 4, ('4c6e', 'your call'): 4, ('4c6e', 'discard'): 6, ('3c4e', 'your call'): 5, ('3c4e', 'discard'): 5,
         ('3c6e', 'discard'): 4, ('5c4e', 'your call'): 3, ('5c4e', 'discard'): 3, ('5c6e', 'your call'): 2, ('5c6e', 'discard'): 2,
         ('6c6e', 'your call'): 2, ('6c6e', 'discard'): 2}

rng = random.Random(20261112)
cand = collections.defaultdict(list)
for r in rows:
    if int(r['length']) != 5 or r['drm_normal'] not in {k[0] for k in QUOTA}: continue
    drm, lab, _ = card(int(r['ix_switched']))
    if drm == r['drm_normal'] and (drm, lab) in QUOTA: cand[(drm, lab)].append(r)
assert sum(QUOTA.values()) == 200, sum(QUOTA.values())
chosen = []
for k, q in QUOTA.items():
    c = cand[k][:]; rng.shuffle(c)
    seen = set(); got = []
    for r in c:                                   # one attempt per scramble and cell where there are enough
        if r['scr'] in seen: continue
        seen.add(r['scr']); got.append(r)
        if len(got) == q: break
    for r in c:                                   # rare cells: a second attempt from the same scramble
        if len(got) == q: break
        if r not in got and not any(x['scr'] == r['scr'] and x['ix_switched'] == r['ix_switched'] for x in got): got.append(r)
    assert len(got) == q, (k, len(got), len(c))
    chosen += [(k, r) for r in got]

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

# ---------------------------------------------------------------- per example
scr = open(os.path.join(OUT, 'scrambles.txt')).read().split('\n')
EX = []
for (drm, lab), r in chosen:
    S0 = scr[int(r['scr'])]; side = int(r['side'])
    for rot, m in FRAME[(r['eo_axis'], r['dr_axis'])]:      # the rotation that gives the study's own frame (the case index)
        S = relabel(S0, m); eo = relabel(r['eo'], m); rzp = relabel(r['rzp'], m)
        st = S if side == 0 else ' '.join(cube.inv_seq(S))
        if geom.ix_of_state(cube.do(cube.SOLVED, ' '.join(x for x in (st, eo, rzp) if x))) == int(r['ix_normal']): break
    check(conj(rot)(cube.do(cube.SOLVED, S0)) == cube.do(cube.SOLVED, S), 'turned scramble')
    start = S if side == 0 else ' '.join(cube.inv_seq(S))
    normal = cube.do(cube.SOLVED, ' '.join(x for x in (start, eo, rzp) if x))
    check(geom.eo_fb_ok(normal), 'EO solved')
    ixn = geom.ix_of_state(normal)
    check(f"{int(F['drm_c'][ixn])}c{int(F['drm_e'][ixn])}e" == drm and int(F['drm_c'][ixn]) * 0 == 0 and ixn == int(r['ix_normal']), 'DRM on normal')
    sw = cube.inverse(normal); ix = geom.ix_of_state(sw)
    check(ix == int(r['ix_switched']), 'switched case')
    tr = {'paired': xtrace.paired_edges_traced(normal), 'side': xtrace.side_traced(normal, 'fb'),
          'earm': sum(1 for ec in xtrace.bad_e_in_E(normal) if ec & set('FB')), 'carm': niss_checks.rl_on_ud(normal),
          'pairs': niss_checks.traced_pairs(normal, 'side')}
    for k, f in (('paired', 'edges_paired'), ('side', 'side'), ('earm', 'earm'), ('carm', 'carm'), ('pairs', 'pairs')):
        check(tr[k] == int(F[f][ix]), f'traced {k}')
    rg = xtrace_rings.read(normal)                      # the rings and holes of the switched case, read on normal
    check(rg == rings.rings_of(ix), 'traced rings')
    if drm == '4c4e': check(xtrace_rings.hbar_of(*rg) == int(HBAR[ix]), 'half turns from the traced rings')
    dr = ' '.join(geom.path_to_dr(ix, F['d']))
    t = cube.do(sw, dr)
    check(geom.is_dr_ud(t) and geom.eo_fb_ok(t) and len(dr.split()) == d[ix] == int(r['d_switched']), 'DR replayed')
    check(all(mv[0] not in 'FB' or mv.endswith('2') for mv in dr.split()), 'EO kept')
    # the switched cube as a sequence from solved (for nissy): inverse of (start, eo, rzp)
    swseq = ' '.join(cube.inv_seq(' '.join(x for x in (start, eo, rzp) if x)))
    check(cube.do(cube.SOLVED, swseq) == sw, 'switched sequence')
    EX.append(dict(drm=drm, lab=lab, txt=card(ix)[2], S=S, side=side, eo=eo, rzp=rzp, ix=ix, tr=tr, dr=dr, n=len(dr.split()), swseq=swseq, rot=rot, rg=rg))
# nissy: the same optimal length
cmds = ''.join(f"solve drud-eofb {e['swseq']}\n" for e in EX)
res = subprocess.run(['nissy', '-b'], input=cmds, capture_output=True, text=True, check=True).stdout.splitlines()
lens = []
for i, l in enumerate(res):
    if l.startswith('>>> Executing command'):
        j = i + 1
        while res[j].startswith('>>>'): j += 1
        lens.append(int(re.search(r'\((\d+)\)\s*$', res[j]).group(1)))
assert len(lens) == len(EX)
for e, n in zip(EX, lens): check(n == e['n'], 'nissy length')
assert not BAD, BAD[:5]
# group rates for the verdict lines (exact, every case once)
import numpy as np
_lab = {}
def grp_rate(drm, lab):
    c, e = int(drm[0]), int(drm[2]); idx = np.flatnonzero(pop.drm_mask(c, e))
    if drm not in _lab: _lab[drm] = np.array([card(i)[1] for i in idx])
    sel = idx[_lab[drm] == lab]
    return len(sel) / len(idx), float((d[sel] <= 6).mean())
for drm, lab in QUOTA: RATE[(drm, lab)] = grp_rate(drm, lab)

# ---------------------------------------------------------------- the page
CASE = 'abcd'
def pl(n, w):
    """'1 pair', '2 pairs'"""
    return f'{n} {w}' + ('' if n == 1 else 's')
out = ['# Worked examples: when to switch an EO', '',
       'Examples to play along with [the write-up](index.html). Do the EO and RZP, trace the inverse (pairs for the card, the rings for the half-turn count), decide, then open the answer.', '',
       f'These are {len(EX)} real attempts from the study\'s uniformly random scrambles: an EO and an RZP that reach the DRM at a total of 5 moves, so the target after the switch is a DR in 6 (sub-7). They\'re spread over the cells of the switch cards (more where the cards have more to say, 4c4e most) and picked at random within each cell. Nothing is hand-picked, so within each cell about as many reach a sub-7 as the cell\'s rate says.', '',
       '**How to read it.**', '',
       '- Every attempt is turned so that its EO is on F/B and its DR on U/D, the frame of the write-up: the scramble printed is the generated one with the faces renamed, which is the same scramble held in another orientation.',
       '- An EO and RZP in brackets were found on the inverse scramble; the DR is then done on the other side, as usual with NISS.',
       '- Colours are named by their home face (the *F/B colour* is the EO axis\'s colour, green or blue with green front).',
       '- *Traced before switching* is what section 7 of the write-up reads on the side where the EO and RZP were done, from the cube after them: how many of the U/D-coloured edges in the E slice find a misoriented corner showing their colours on its side stickers (paired edges on the inverse), how many of them have an F/B-colour sticker (edge ARM on the inverse), the R/L stickers on the U/D faces (corner ARM on the inverse), the pairs and the side pairs.',
       '- *Rings* are the two rings and the holes of the switched case as section 4.1 of the write-up writes them (clockwise from a corner: `>` and `<` bad corners pointing clockwise and counter-clockwise, `o` a good corner, `E` a bad edge place, `-` a good one), read on normal by colour as in section 7.',
       '- The answer gives the count of sections 4 and 5 (for 4c4e the half turns to two bars, for the other DRMs the side turns of the shortest setup, U and D turns not counted) with its sub-7 rate, then the card\'s verdict with the sub-7 rate of that group (both exact, every case once), the switched case, and one optimal DR on the inverse with the EO kept.', '',
       f'**Replay check.** Every move sequence on this page was replayed on the sticker model before the page was written: {CHECKS[0]:,} checks (the turned scramble is the generated one after a rotation; EO + RZP solves the F/B EO and gives the stated DRM; the switched case is the attempt\'s; every value traced on normal equals the feature of the inverse, the two rings and the holes included; the DR solves the inverse to DR on U/D with the EO kept, in the table\'s optimal number of moves, and nissy 2.0.8 finds the same length), 0 mismatches.', '']
hits = collections.Counter(); tot = collections.Counter()
for e in EX: tot[e['lab']] += 1; hits[e['lab']] += e['n'] <= 6
out.append('**In these ' + str(len(EX)) + '**, a DR in 6 or less exists after the switch in ' + ', '.join(f"{hits[k]} of the {tot[k]} *{k}*" for k in ('switch', 'your call')) + f" and {hits['discard']} of the {tot['discard']} *discard*" + ' attempts.')
def is_short(e): return SIG[e['ix']] <= 3 and QSIG[e['ix']] == (1 if e['drm'] == '4c4e' else 2)
hs = collections.Counter(); ht = collections.Counter()
for e in EX:
    if e['drm'] == '4c4e':
        k = '2 or fewer' if HBAR[e['ix']] <= 2 else '3' if HBAR[e['ix']] == 3 else '4 or 5'
        ht[k] += 1; hs[k] += e['n'] <= 6
out.append('By the half-turn count, the ' + str(sum(ht.values())) + ' 4c4e attempts: ' + ', '.join(f"{hs[k]} of the {ht[k]} with {k} half turns to two bars" for k in ('2 or fewer', '3', '4 or 5')) + ' have a DR in 6 or less.')
ss = collections.Counter(); st_ = collections.Counter()
for e in EX:
    if e['drm'] != '4c4e':
        k = 'short' if is_short(e) else 'not short'; st_[k] += 1; ss[k] += e['n'] <= 6
out.append('By side turns, the ' + str(sum(st_.values())) + ' attempts of the other DRMs: ' + ' and '.join(f"{ss[k]} of the {st_[k]} *{k}*" for k in ('short', 'not short')) + ' (short: 3 side turns or fewer, 2 of them quarter turns).')
out.append('')
order = ['4c4e', '4c2e', '3c2e', '7c8e', '8c8e', '2c2e', '4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e']
for drm in order:
    ex = [x for x in EX if x['drm'] == drm]
    out += [f'## DRM {drm}: examples 1–{len(ex)}', '']
    for k, e in enumerate(ex, 1):
        f = lambda kk: int(F[kk][e['ix']])
        br = (lambda x: x) if e['side'] == 0 else (lambda x: f'({x})')
        moves = (f"EO `{br(e['eo'])}`, RZP `{br(e['rzp'])}`" if e['rzp'] else f"EO `{br(e['eo'])}`, no RZP needed") + ('' if e['side'] == 0 else ', on the inverse scramble')
        tr = e['tr']
        out += [f"**{drm}, example {k}.** `{e['S']}`", '',
                f"{moves}: {drm} in 5. Traced before switching: {pl(tr['paired'], 'paired edge')}, edge ARM {tr['earm']}, corner ARM {tr['carm']} (R/L stickers on U/D), {pl(tr['pairs'], 'pair')}, {pl(tr['side'], 'side pair')}. Rings: U `{rings.nice(e['rg'][0])}`, D `{rings.nice(e['rg'][1])}`, holes {' '.join(nm for nm, x in zip(rings.SLOT_NAME, e['rg'][2]) if x) or 'none'}.", '',
                '<details><summary>Verdict and the DR after the switch</summary>', '']
        share, rate = RATE[(drm, e['lab'])]
        case = f", corners 4{CASE[f('corner_case')]}-{f('case_suffix')}" if f('drm_c') == 4 else ''
        er = ' '.join(x for x in (e['eo'], e['rzp']) if x)
        full = (f"`{er} ({e['dr']})`" if e['side'] == 0 else f"`({er}) {e['dr']}`")
        ix_ = e['ix']
        if drm == '4c4e':
            hh = int(HBAR[ix_]); hr = RJ['h'][str(hh)]
            cnt = f"Half turns to two bars: **{hh}** ({pc(hr['share'])} of 4c4e, {pc(hr['p6']) if hr['p6'] < 1 else '100%'} sub-7)."
        else:
            q_, h_ = int(QSIG[ix_]), int(SIG[ix_] - QSIG[ix_]); sh = is_short(e); g = RJ['short'][drm]['short' if sh else 'long']
            setup = f"{q_} qt" + (f" + {h_} half turn{'s' if h_ != 1 else ''}" if h_ else '')
            cnt = f"Shortest setup, U/D turns not counted: **{setup}**, {'short' if sh else 'not short'} ({pc(g['share'])} of {drm}, {pc(g['p6']) if g['p6'] < 1 else '100%'} sub-7)."
        out += [cnt, '', f"Card: **{e['lab']}** ({e['txt']}: {pc(share)} of {drm}, {pc(rate)} sub-7).", '',
                f"Switched case: {drm}, ARM {f('carm')}{f('earm')}, {pl(f('pairs'), 'pair')} on {pl(f('edges_paired'), 'edge')}, {f('fake')} fake, {pl(f('side'), 'side pair')}{case}{', JZP' if f('jzp') else ''}.", '',
                f"Optimal DR on the {'inverse' if e['side'] == 0 else 'normal side'}: `{e['dr']}` ({e['n']} moves, {'sub-7' if e['n'] <= 6 else 'not sub-7'}). The whole attempt: {full}, {5 + e['n']} moves to DR.", '',
                '</details>', '']
open(PAGE, 'w').write('\n'.join(out))
print(len(EX), 'examples,', CHECKS[0], 'checks, 0 mismatches ->', os.path.normpath(PAGE))

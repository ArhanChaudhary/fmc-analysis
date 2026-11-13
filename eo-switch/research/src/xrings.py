#!/usr/bin/env python3
"""Tables and numbers of the two-ring sections of the write-up, from out/big/rings.npz (rings.py), the features and
distances of out/big/feat.npz and the real attempts: report/data/ring_*.md, out/rings.json (numbers the text quotes)
and out/ring_examples.json (every example of those sections: a scramble in EO-kept moves from solved and an optimal
DR, replayed on the sticker model here).  usage: xrings.py"""
import os, sys, json, pickle, collections, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pop, geom, rings
from geom import cube, N0, NAMES, EOK, move_ix
from rings import rings_of, canon, sym_key, nice, ring_str, swap_rows, slot_type
OUT = os.path.normpath(os.path.join(HERE, '..', 'out')) + '/'
D = os.path.normpath(os.path.join(HERE, '..', '..', 'report', 'data')) + '/'
F = pop.feat(); d = F['d'].astype(int); P = pop.populations()
Z = rings.load(); sigma = Z['sigma'].astype(int); qsig = Z['qsig'].astype(int); hbar = Z['hbar'].astype(int)
swaps = Z['swaps'].astype(int); slot = Z['slot'].astype(int); Q = Z['Q']
CL = pickle.load(open(OUT + 'big/ring_classes.pkl', 'rb')); DIST = CL['dist']
hsig = sigma - qsig
f = lambda k: F[k].astype(int)
pairs, side, ep, earm, carm, jzp, pph = f('pairs'), f('side'), f('edges_paired'), f('earm'), f('carm'), f('jzp'), f('pairs_plus_half_side_x2')
DRMS = ['4c4e', '4c2e', '3c2e', '7c8e', '8c8e', '2c2e', '4c6e', '3c4e', '3c6e', '5c4e', '5c6e', '6c6e']
def M(drm): return pop.drm_mask(int(drm[0]), int(drm[2]))
def pc(x, dd=None):
    x = float(x) * 100
    if x == 0: return '0%'
    if 99.95 <= x and dd is None: return '100%' if x == 100 else '>99.9%'
    if dd is None: dd = 1 if x >= 1 else 2 if x >= 0.1 else 3
    return f'{x:.{dd}f}%'
def n_(x): return f'{int(x):,}'
def write(name, head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] + ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]
    open(D + name + '.md', 'w').write('\n'.join(out) + '\n')
def stats(base, sel):
    """sel within base (a DRM mask): states, share, DR <= 5/6/7 rates, share of the base's sub-7s, real attempts."""
    sel = sel & base; n = int(sel.sum())
    if n == 0: return None
    r = dict(n=n, share=n / base.sum(), p5=(d[sel] <= 5).mean(), p6=(d[sel] <= 6).mean(), p7=(d[sel] <= 7).mean(),
             hits=int((d[sel] <= 6).sum()), of_hits=(d[sel] <= 6).sum() / max(1, (d[base] <= 6).sum()))
    for L, k in ((4, 7), (5, 6), (6, 5)):
        w = P[f'P3_{L}'][sel]; r[f'a{L}'] = int(w.sum()); r[f'q{L}'] = float((w * (d[sel] <= k)).sum() / w.sum()) if w.sum() else float('nan')
    return r
def band(p): return 'switch' if p > 0.5 else 'discard' if p < 0.1 else 'your call'
R = {}                                            # numbers for the text
ALL = np.ones(N0, bool)
c44 = M('4c4e')

# ------------------------------------------------------------------------------------------------------------------
# 4c4e: half turns to two bars
rows, rows2 = [], []; R['h'] = {}
for h in range(6):
    s = stats(c44, hbar == h); R['h'][h] = s
    rows.append([h, n_(s['n']), pc(s['share']), pc(s['p6']), pc(s['of_hits']), pc(s['q5']), n_(s['a5'])])
    rows2.append([h, pc(s['p7']), pc(s['q4']), n_(s['a4']), pc(s['p5']), pc(s['q6']), n_(s['a6'])])
write('ring44_bands', ['Half turns to two bars', 'States', 'Share of 4c4e', 'Sub-7 rate, exact', "Share of 4c4e's sub-7s", 'Sub-7 rate, real attempts (RZP to 5)', 'Real attempts (RZP to 5)'], rows)
write('ring44_bands_rzp', ['Half turns to two bars', 'DR in 7 or fewer, exact (for a 4-move RZP)', 'DR in 7 or fewer, real attempts (RZP to 4)', 'Real attempts (RZP to 4)',
                           'DR in 5 or fewer, exact (for a 6-move RZP)', 'DR in 5 or fewer, real attempts (RZP to 6)', 'Real attempts (RZP to 6)'], rows2)
grp = {'le1': hbar <= 1, 'le2': hbar <= 2, 'eq2': hbar == 2, 'eq3': hbar == 3, 'ge3': hbar >= 3, 'ge4': hbar >= 4}
R['hg'] = {k: stats(c44, v) for k, v in grp.items()}
R['all44'] = stats(c44, ALL)
# against the published card
card = {'switch': ep == 2, 'your call': (ep == 1) & (earm == 1), 'discard': (ep == 0) | ((ep == 1) & (earm != 1))}
R['card'] = {k: stats(c44, v) for k, v in card.items()}
rows = []
for lab, txt, sel in (('this page', '2 half turns or fewer to two bars', hbar <= 2), ('this page', '3 half turns', hbar == 3), ('this page', '4 or 5 half turns', hbar >= 4),
                      ('the paired-edge card', 'both bad edges paired', card['switch']), ('the paired-edge card', 'one paired, edge ARM 1', card['your call']),
                      ('the paired-edge card', 'one paired with edge ARM 0 or 2, or none paired', card['discard'])):
    s = stats(c44, sel); rows.append([lab, txt, pc(s['share']), pc(s['p6']), pc(s['of_hits'])])
write('ring44_vs_card', ['Rule', 'Group (4c4e)', 'Share of 4c4e', 'Sub-7 rate', "Share of 4c4e's sub-7s"], rows)
# the card's groups, split by the half-turn count
rows = []; R['card_split'] = {}
for lab, sel in card.items():
    for txt, hs in (('2 or fewer', hbar <= 2), ('3', hbar == 3), ('4 or 5', hbar >= 4)):
        s = stats(c44, sel & hs)
        if s: rows.append([lab, txt, n_(s['n']), pc(s['share']), pc(s['p6'])]); R['card_split'][f'{lab}|{txt}'] = s
write('ring44_card_split', ["The paired-edge card's group", 'Half turns to two bars', 'States', 'Share of 4c4e', 'Sub-7 rate'], rows)
# ring swaps x slot type
SLOTN = {0: 'same R/L face', 1: 'diagonal', 2: 'same F/B face'}
rows = []; R['ss'] = {}
for a in range(6):
    for t in range(3):
        s = stats(c44, (swaps == a) & (slot == t)); R['ss'][f'{a}{t}'] = s
        rows.append([a, SLOTN[t], max(a, t), n_(s['n']), pc(s['share']), pc(s['p6'])])
write('ring44_swaps_slot', ['Row swaps to a bar in each layer', 'The two holes', 'Half turns to two bars', 'States', 'Share of 4c4e', 'Sub-7 rate'], rows)
R['classes'] = {str(k): v for k, v in sorted(collections.Counter(DIST.values()).items())}
R['classes_sym'] = {str(k): v for k, v in sorted(collections.Counter(DIST[c] for c in set(sym_key(k) for k in DIST)).items())}
# pairs x half turns
rows = []; R['ph'] = {}
for p in range(5):
    for txt, hs in (('1 or fewer', hbar <= 1), ('2', hbar == 2), ('3', hbar == 3), ('4 or 5', hbar >= 4)):
        s = stats(c44, (pairs == p) & hs)
        if s: rows.append([p, txt, n_(s['n']), pc(s['share']), pc(s['p6'])]); R['ph'][f'{p}|{txt}'] = s
    R['ph'][f'{p}|all'] = stats(c44, pairs == p); R['ph'][f'{p}|le2'] = stats(c44, (pairs == p) & (hbar <= 2)); R['ph'][f'{p}|ge3'] = stats(c44, (pairs == p) & (hbar >= 3))
write('ring44_pairs', ['Pairs', 'Half turns to two bars', 'States', 'Share of 4c4e', 'Sub-7 rate'], rows)
R['p2le2'] = stats(c44, (pairs >= 2) & (hbar <= 2)); R['p2ge3'] = stats(c44, (pairs >= 2) & (hbar >= 3)); R['p01'] = stats(c44, pairs <= 1)
R['p01le2'] = stats(c44, (pairs <= 1) & (hbar <= 2)); R['p01ge3'] = stats(c44, (pairs <= 1) & (hbar >= 3))
# what a hand reading gives: the count where it can be counted (2+ pairs), the paired-edge card for 0 or 1 pair
R['p0'] = stats(c44, pairs == 0); R['p1'] = stats(c44, pairs == 1)
R['p01_call'] = stats(c44, (pairs <= 1) & card['your call']); R['p01_disc'] = stats(c44, (pairs <= 1) & card['discard'])
R['p01_h45'] = stats(c44 & (hbar >= 4), pairs <= 1)
# alignment: U/D turns of the shortest finish with the fewest half turns and one quarter turn
u1 = np.full(N0, 99)
for h in range(6):
    m = c44 & (hbar == h); u1[m] = Q[1, h][m].astype(int) - h - 1
rows = []; R['u'] = {}
for h in range(6):
    for u in range(8):
        s = stats(c44, (hbar == h) & (u1 == u))
        if s: rows.append([h, u, h + u + 1, n_(s['n']), pc(s['n'] / (c44 & (hbar == h)).sum()), pc(s['p6'])]); R['u'][f'{h}{u}'] = s
write('ring44_align', ['Half turns to two bars', 'U/D turns of the shortest such setup', 'Length of that DR (moves)', 'States', 'Share of that half-turn count', 'Sub-7 rate'], rows)
rows = []
for h, cut in ((2, 3), (3, 2), (4, 1)):
    a = stats(c44, (hbar == h) & (u1 <= cut)); b = stats(c44, (hbar == h) & (u1 > cut))
    R[f'u_le_{h}'] = a; R[f'u_gt_{h}'] = b
    rows.append([h, f'{cut} or fewer', n_(a['n']), pc(a['n'] / (a['n'] + b['n'])), pc(a['p6'])])
    rows.append([h, f'{cut + 1} or more', n_(b['n']), pc(b['n'] / (a['n'] + b['n'])), pc(b['p6'])])
write('ring44_align_sum', ['Half turns to two bars', 'U/D turns that setup needs', 'States', 'Share of that half-turn count', 'Sub-7 rate'], rows)
# ARM, pairs, side pairs inside a half-turn count
rows = []; R['arm_in'] = {}
for h in (2, 3):
    for a in range(5):
        for b in range(3):
            s = stats(c44, (hbar == h) & (carm == a) & (earm == b))
            if s: rows.append([h, f'{a}{b}', n_(s['n']), pc(s['p6'])]); R['arm_in'][f'{h}|{a}{b}'] = s['p6']
write('ring44_arm', ['Half turns to two bars', 'ARM', 'States', 'Sub-7 rate'], rows)
def info(base, key):
    """share of the uncertainty about sub-7 inside base that the key removes (mutual information / entropy)"""
    y = (d[base] <= 6); k = key[base]
    H = lambda p: 0.0 if p in (0, 1) else float(-(p * np.log2(p) + (1 - p) * np.log2(1 - p)))
    h0 = H(y.mean()); h1 = sum((k == v).mean() * H(y[k == v].mean()) for v in np.unique(k))
    return (h0 - h1) / h0
def settled(base, key):
    y = (d[base] <= 6); k = key[base]; tot = 0
    for v in np.unique(k):
        p = y[k == v].mean()
        if p < 0.1 or p > 0.5: tot += (k == v).sum()
    return tot / base.sum()
arm = carm * 10 + earm
R['info'] = {'h': info(c44, hbar), 'pairs': info(c44, pairs), 'arm': info(c44, arm), 'pairs+arm': info(c44, pairs * 100 + arm), 'card': info(c44, ep * 10 + earm),
             'h+arm': info(c44, hbar * 100 + arm), 'h+pairs': info(c44, hbar * 10 + pairs), 'h+slot': info(c44, swaps * 10 + slot), 'h+side': info(c44, hbar * 10 + side),
             'h+pairs+side': info(c44, hbar * 100 + pairs * 10 + side), 'sigma': info(c44, sigma), 'h+sigma': info(c44, hbar * 10 + sigma)}
R['settled'] = {'h': settled(c44, hbar), 'h+side': settled(c44, hbar * 10 + np.minimum(side, 2)), 'h+pairs': settled(c44, hbar * 10 + pairs), 'h+arm': settled(c44, hbar * 100 + arm),
                'h+pairs+side': settled(c44, hbar * 100 + pairs * 10 + side), 'card': settled(c44, np.where(ep == 2, 0, np.where((ep == 1) & (earm == 1), 1, 2)))}
R['arm_align'] = {}
for h_, cut_ in ((2, 3), (3, 2)):          # does ARM say whether the setup lines up, once the count is known?
    m_ = c44 & (hbar == h_); okk = (u1[m_] <= cut_); a_ = arm[m_]
    Hb = lambda p: 0.0 if p in (0, 1) else float(-(p * np.log2(p) + (1 - p) * np.log2(1 - p)))
    R['arm_align'][h_] = (Hb(okk.mean()) - sum((a_ == v).mean() * Hb(okk[a_ == v].mean()) for v in np.unique(a_))) / Hb(okk.mean())
rows = []; R['in3'] = {}
for txt, sel in [(f"{p} pair{'s' if p != 1 else ''}", pairs == p) for p in range(4)] + [('0 side pairs', side == 0), ('1 side pair', side == 1), ('2 or more side pairs', side >= 2)] \
        + [('edge ARM 1', earm == 1), ('edge ARM 0 or 2', earm != 1)] + [('both bad edges paired', ep == 2), ('one bad edge paired', ep == 1), ('no bad edge paired', ep == 0)]:
    s = stats(c44, (hbar == 3) & sel); rows.append([txt, n_(s['n']), pc(s['share']), pc(s['p6']), pc(s['q5']), n_(s['a5'])]); R['in3'][txt] = s
write('ring44_inside3', ['Inside *3 half turns*', 'States', 'Share of 4c4e', 'Sub-7 rate, exact', 'Sub-7 rate, real attempts (RZP to 5)', 'Real attempts (RZP to 5)'], rows)
# routes: fewest quarter turns of an optimal DR among the sub-7 4c4e cases
qopt = np.full(N0, 9)
for q in range(Q.shape[0] - 1, -1, -1): qopt[(Q[q] == d[None, :]).any(axis=0)] = q
sub = c44 & (d <= 6); rows = []; R['qopt'] = {}
for q in range(1, 5):
    n = int((sub & (qopt == q)).sum()); R['qopt'][q] = n
    rows.append([q, n_(n), pc(n / sub.sum())])
write('ring44_routes', ['Fewest quarter turns in an optimal DR', 'Sub-7 states (4c4e)', "Share of 4c4e's sub-7s"], rows)
R['sigma44'] = {s: stats(c44, sigma == s) for s in range(1, 6)}
R['prof44'] = {f'{q}{h}': stats(c44, (qsig == q) & (hsig == h)) for q in range(1, 5) for h in range(5) if stats(c44, (qsig == q) & (hsig == h))}

# ------------------------------------------------------------------------------------------------------------------
# the ring pairs: patterns with at most 2 row swaps; the 3-pair rule
def rpairs(k):
    n = 0
    for e, h in k:
        for a in range(4):
            if e[a]: n += (h[(a - 1) % 4] == 1) + (h[a] == 2)
    return n
keys = CL['keys']; kid = {k: i for i, k in enumerate(keys)}; cls = Z['cls'].astype(int)
cls_n = np.bincount(cls[c44], minlength=len(keys)); cls_hit = np.bincount(cls[c44], weights=(d[c44] <= 6), minlength=len(keys))
symc = collections.defaultdict(list)
for k in keys: symc[sym_key(k)].append(k)
def layers(k):
    """the ring pair written with the layer holding more bad edges first, each ring from the corner before a bad edge"""
    a, b = k
    if (sum(b[0]), -sum(1 for x in b[1] if x)) > (sum(a[0]), -sum(1 for x in a[1] if x)): a, b = b, a
    return nice(a), nice(b)
rows = []; R['patterns'] = []
for c in sorted(symc, key=lambda c: (DIST[c], -rpairs(c), layers(c))):
    if DIST[c] > 2: continue
    n = sum(cls_n[kid[k]] for k in symc[c]); hit = sum(cls_hit[kid[k]] for k in symc[c]); a, b = layers(c)
    rows.append([f'`{a}`', f'`{b}`', DIST[c], rpairs(c), n_(n), pc(hit / n)])
    R['patterns'].append(dict(a=a, b=b, swaps=DIST[c], pairs=rpairs(c), n=int(n), p6=hit / n))
write('ring_patterns', ['One layer', 'The other layer', 'Row swaps to a bar in each layer', 'Pairs', 'States (4c4e)', 'Sub-7 rate'], rows)
R['patterns_n'] = {s: sum(1 for p in R['patterns'] if p['swaps'] == s) for s in (0, 1, 2)}
R['pairs_classes'] = {f'{p}{s}': v for (p, s), v in collections.Counter((rpairs(k), DIST[k]) for k in keys).items()}
R['pairs_swaps_states'] = {f'{p}{s}': int((c44 & (pairs == p) & (swaps == s)).sum()) for p in range(5) for s in range(6)}
dpair = collections.Counter()
for k in keys:
    for p in range(4):
        for q in range(4): dpair[rpairs(swap_rows(k[0], k[1], p, q)) - rpairs(k)] += 1
R['pair_change'] = {str(k): v for k, v in sorted(dpair.items())}
assert max(dpair) == 2 and all(DIST[k] >= -(-(4 - rpairs(k)) // 2) for k in keys)
def three(k):
    """3 pairs: (4th corner in the layer of the edge that lacks it, blocked, both edges in one layer and opposite)"""
    ne = [sum(k[0][0]), sum(k[1][0])]; lone = None; lack = None
    for ri, (e, h) in enumerate(k):
        for i in range(4):
            if h[i] == 1 and not e[(i + 1) % 4]: lone = (ri, i, 1)
            if h[i] == 2 and not e[i]: lone = (ri, i, 2)
        for a in range(4):
            if e[a] and not (h[(a - 1) % 4] == 1 and h[a] == 2): lack = ri
    ri, i, dr = lone; e, h = k[ri]
    blocked = bool(e[i] or h[(i - 1) % 4]) if dr == 1 else bool(e[(i + 1) % 4] or h[(i + 1) % 4])
    opp = 0
    if ne != [1, 1]:
        ee = k[0][0] if ne[0] == 2 else k[1][0]; opp = int(not any(ee[a] and ee[(a + 1) % 4] for a in range(4)))
    return int(lack == ri), int(blocked), opp
t3 = collections.defaultdict(lambda: [0, 0, set()])
for k in keys:
    if rpairs(k) != 3: continue
    same, blocked, opp = three(k); assert DIST[k] == 1 + same + blocked + opp, k
    t = t3[(same, blocked, opp)]; t[0] += cls_n[kid[k]]; t[1] += cls_hit[kid[k]]; t[2].add(DIST[k])
R['three_classes'] = sum(1 for k in keys if rpairs(k) == 3)
rows = []; R['three'] = {}
for (same, blocked, opp), (n, hit, ds) in sorted(t3.items(), key=lambda kv: (1 + sum(kv[0]), kv[0])):
    assert len(ds) == 1
    rows.append(['the layer of the edge that lacks it' if same else 'the other layer', 'yes' if blocked else 'no', 'yes' if opp else 'no', ds.pop(), n_(n), pc(hit / n)])
    R['three'][f'{same}{blocked}{opp}'] = dict(n=int(n), p6=hit / n)
write('ring44_3pairs', ['The unpaired corner is in', 'A bad piece in the two places behind it', 'Both bad edges in one layer, opposite each other', 'Row swaps', 'States (4c4e)', 'Sub-7 rate'], rows)

# is there a formula?  (a) single rings that behave alike against every partner ring; (b) a table over counts
def sig3(r): return (sum(r[0]), sum(1 for x in r[1] if x == 1), sum(1 for x in r[1] if x == 2))
single = sorted(set(k[0] for k in keys) | set(k[1] for k in keys))
rowof = {r: tuple(DIST.get((r, q)) if tuple(a + b for a, b in zip(sig3(r), sig3(q))) == (2, 2, 2) else None for q in single) for r in single}
assert all(DIST[(a, b)] == DIST[(b, a)] for a, b in keys)
R['ring_single'] = len(single); R['ring_eqv'] = len(set((sig3(r), rowof[r]) for r in single))
def count_features(k):
    """split of the two bad edges, pairs per edge, unpaired corners that the other layer needs (and how many of those
    are free), unpaired corners that are free"""
    ne = [sum(k[0][0]), sum(k[1][0])]
    if ne == [1, 1]: split = 0
    else:
        ee = k[0][0] if ne[0] == 2 else k[1][0]; split = 1 if any(ee[a] and ee[(a + 1) % 4] for a in range(4)) else 2
    def needs(r):
        e, h = r; t = hd = 0
        for a in range(4):
            if e[a]: t += h[(a - 1) % 4] != 1; hd += h[a] != 2
        return t, hd
    N = [needs(k[0]), needs(k[1])]; per = []; unh = []
    for ri, (e, h) in enumerate(k):
        for a in range(4):
            if e[a]: per.append((h[(a - 1) % 4] == 1) + (h[a] == 2))
        for i in range(4):
            if h[i] == 1 and not e[(i + 1) % 4]: unh.append((ri, 0, (not e[i]) and h[(i - 1) % 4] == 0))
            if h[i] == 2 and not e[i]: unh.append((ri, 1, (not e[(i + 1) % 4]) and h[(i + 1) % 4] == 0))
    far = [x for x in unh if N[1 - x[0]][x[1]] > 0]
    return (split, tuple(sorted(per)), len(far), sum(1 for x in far if x[2]), sum(1 for x in unh if x[2]))
tab = collections.defaultdict(collections.Counter)
for k in keys: tab[count_features(k)][min(max(DIST[k], 1), 4)] += int(cls_n[kid[k]])
R['count_table_cells'] = len(tab); R['count_table_acc'] = sum(max(v.values()) for v in tab.values()) / int(cls_n.sum())

# ------------------------------------------------------------------------------------------------------------------
# every DRM: side turns, and the (quarter turns, half turns) of the setups with the fewest side turns
def pname(q, h):
    return f"{q} qt" + (f" + {h} half turn{'s' if h != 1 else ''}" if h else '')
rows, rows2, rows3 = [], [], []; R['prof'] = {}; R['sig'] = {}
for drm in DRMS:
    m = M(drm); first = True; R['prof'][drm] = {}; R['sig'][drm] = {}
    for s in range(6):
        st = stats(m, sigma == s)
        if st: R['sig'][drm][s] = st; rows3.append([drm if not R['sig'][drm].keys() - {s} else '', s, n_(st['n']), pc(st['share']), pc(st['p6']), pc(st['of_hits'])])
    for s, q in sorted(set(zip(sigma[m].tolist(), qsig[m].tolist()))):
        st = stats(m, (sigma == s) & (qsig == q)); R['prof'][drm][f'{q}{s - q}'] = st
        rows.append([drm if first else '', pname(q, s - q), s, n_(st['n']), pc(st['share']), pc(st['p6']), pc(st['of_hits'])])
        rows2.append([drm if first else '', pname(q, s - q), pc(st['q5']), n_(st['a5']), pc(st['p7']), pc(st['p5'])]); first = False
write('ring_profiles', ['DRM', 'Shortest setup, U/D turns not counted', 'Side turns', 'States', 'Share of the DRM', 'Sub-7 rate, exact', "Share of the DRM's sub-7s"], rows)
write('ring_profiles_rzp', ['DRM', 'Shortest setup, U/D turns not counted', 'Sub-7 rate, real attempts (RZP to 5)', 'Real attempts (RZP to 5)', 'DR in 7 or fewer, exact (for a 4-move RZP)', 'DR in 5 or fewer, exact (for a 6-move RZP)'], rows2)
write('ring_sigma', ['DRM', 'Side turns', 'States', 'Share of the DRM', 'Sub-7 rate', "Share of the DRM's sub-7s"], rows3)
R['sig_all'] = {s: dict(n=int((sigma == s).sum()), p6=float((d[sigma == s] <= 6).mean()), hits=int((d[sigma == s] <= 6).sum())) for s in range(6)}
R['sig_max_d'] = {s: int(d[sigma == s].max()) for s in range(6)}; R['sig_min_d'] = {s: int(d[sigma == s].min()) for s in range(6)}
QANY = np.argmax(np.stack([(Q[q] < 99).any(axis=0) for q in range(Q.shape[0])]), axis=0)      # fewest quarter turns of any DR
R['qmin'] = {drm: sorted(set(int(x) for x in np.unique(QANY[M(drm)]))) for drm in DRMS}
m88 = M('8c8e'); tmaj = f('twist_major')
R['c88'] = {'n44': int((m88 & (tmaj == 4)).sum()), 'n71': int((m88 & (tmaj == 7)).sum()),
            'q44': sorted(set(int(x) for x in QANY[m88 & (tmaj == 4)])), 'q71': sorted(set(int(x) for x in QANY[m88 & (tmaj == 7)])),
            'p44': float((d[m88 & (tmaj == 4)] <= 6).mean()), 'p71': float((d[m88 & (tmaj == 7)] <= 6).mean())}
assert R['c88']['q44'] == [2] and R['c88']['q71'] == [3]
# the cards crossed with the short setups (side turns <= 3 with the fewest quarter turns the DRM allows)
CARD = {'4c4e': [('both bad edges paired', ep == 2), ('one paired, edge ARM 1', (ep == 1) & (earm == 1)), ('the rest', ALL)],
        '4c2e': [('pairs + side pairs/2 is 1.5 or more', pph >= 3), ('exactly 1', pph == 2), ('0 or 0.5', ALL)],
        '3c2e': [('any', ALL)],
        '7c8e': [('5 or 6 pairs', pairs >= 5), ('4 pairs', pairs == 4), ('3 pairs or fewer', ALL)],
        '8c8e': [('corner ARM 0, 4 or 8', np.isin(carm, [0, 4, 8])), ('corner ARM 2, 3, 5 or 6', ALL)],
        '2c2e': [('a bad edge with a pair', ep >= 1), ('no pair, JZP', jzp == 1), ('no pair, not JZP', ALL)],
        '4c6e': [('JZP', jzp == 1), ('4 pairs', pairs == 4), ('anything else', ALL)],
        '3c4e': [('2 pairs', pairs == 2), ('0 or 1 pair', ALL)], '3c6e': [('any', ALL)], '5c4e': [('3 pairs', pairs == 3), ('2 pairs or fewer', ALL)],
        '5c6e': [('4 pairs', pairs == 4), ('3 pairs or fewer', ALL)], '6c6e': [('JZP, or 5 or 6 pairs', (jzp == 1) | (pairs >= 5)), ('anything else', ALL)]}
rows = []; R['cross'] = {}; R['short'] = {}
for drm in DRMS:
    m = M(drm); qm = 1 if drm == '4c4e' else 2
    short = (sigma <= 3) & (qsig == qm); taken = np.zeros(N0, bool); first = True
    R['short'][drm] = {'short': stats(m, short), 'long': stats(m, ~short), 's2': stats(m, sigma <= 2), 's3': stats(m, short & (sigma == 3))}
    for txt, sel in CARD[drm]:
        g = sel & ~taken & m; taken |= g
        for lab, ss in (('short', short), ('not short', ~short)):
            st = stats(m, g & ss)
            if st:
                rows.append([drm if first else '', txt, lab, n_(st['n']), pc(st['share']), pc(st['p6']), pc(st['q5']), n_(st['a5'])]); first = False
                R['cross'][f'{drm}|{txt}|{lab}'] = st
write('ring_cross', ['DRM', "The card's group", 'Setup', 'States', 'Share of the DRM', 'Sub-7 rate, exact', 'Sub-7 rate, real attempts (RZP to 5)', 'Real attempts (RZP to 5)'], rows)
# where the half turn of a 2 qt + 1 half turn setup goes: before both quarter turns (one half turn from a case that two
# quarter turns solve), or between them (one quarter turn from a 4c4e that is one half turn from two bars)
RS = np.unpackbits(Z['R'], axis=1)[:, :N0].reshape(tuple(Z['Rshape'])).astype(bool)
hqq = rings.ud_closure(rings.image(RS[2, 0], rings.HTM_))
qhq = rings.ud_closure(rings.image(rings.ud_closure(rings.image(RS[1, 0], rings.HTM_)), rings.QTM))
assert ((hqq | qhq) == RS[2, 1]).all()
rows = []; R['hqq'] = {}
for drm in DRMS[1:]:
    m = M(drm); sel = m & (sigma == 3) & (qsig == 2); first = True; R['hqq'][drm] = {}
    for key, txt, ss in (('first', 'before both quarter turns', hqq), ('between', 'only between them', qhq & ~hqq)):
        st = stats(m, sel & ss); R['hqq'][drm][key] = st
        if st: rows.append([drm if first else '', txt, n_(st['n']), pc(st['share']), pc(st['p6'])]); first = False
write('ring_hqq', ['DRM', 'Where the half turn goes (2 qt + 1 half turn)', 'States', 'Share of the DRM', 'Sub-7 rate'], rows)
rows = [[s_, n_(R['sig_all'][s_]['n']), pc(R['sig_all'][s_]['n'] / N0) if R['sig_all'][s_]['n'] / N0 >= 5e-6 else '<0.001%', pc(R['sig_all'][s_]['p6']), R['sig_min_d'][s_], R['sig_max_d'][s_]] for s_ in range(6)]
write('ring_sigma_all', ['Side turns', 'States (all cases)', 'Share of all cases', 'Sub-7 rate', 'Shortest DR (moves)', 'Longest DR (moves)'], rows)
# the counts as switch rules, in the columns of the graded-rules table
def grade_row(drm, txt, sel):
    m = M(drm); st = stats(m, sel); al = stats(m, ALL)
    return [drm, txt, pc(st['share']), pc(st['p6']), pc(st['of_hits']), pc((al['hits'] - st['hits']) / al['n']), pc(st['q5'])]
rows = [grade_row('4c4e', '1 half turn or fewer to two bars', hbar <= 1), grade_row('4c4e', '2 half turns or fewer to two bars', hbar <= 2), grade_row('4c4e', '3 half turns or fewer to two bars', hbar <= 3)]
for drm in DRMS[1:]:
    if (M(drm) & (sigma <= 2)).any(): rows.append(grade_row(drm, '2 side turns or fewer', sigma <= 2))
    rows.append(grade_row(drm, 'short: 3 side turns or fewer, 2 of them quarter turns', (sigma <= 3) & (qsig == 2)))
last = None
for r in rows:
    if r[0] == last: r[0] = ''
    else: last = r[0]
write('ring_grades', ['DRM', 'Switch when', 'Switches (share of the DRM)', 'Sub-7 among switched', "Sub-7 states switched (share of the DRM's sub-7s)", 'Sub-7 states discarded (share of the DRM)', 'Real attempts: sub-7 among switched'], rows)
# the cases with at most two side turns, in ring notation
rows = []; R['trig'] = {}
for drm in DRMS:
    m = np.flatnonzero(M(drm) & (sigma <= 2)); cnt = collections.Counter()
    for ix in m:
        U, Dn, H = rings_of(ix); k = sym_key((canon(U), canon(Dn))); a, b = layers(k)
        cnt[(int(sigma[ix]), a, b, sum(H))] += 1
    R['trig'][drm] = len(m)
    for i, ((s, a, b, nh), n) in enumerate(sorted(cnt.items())):
        rows.append([drm if i == 0 else '', s, f'`{a}`', f'`{b}`', nh, n_(n)])
write('ring_triggers', ['DRM', 'Side turns', 'One layer', 'The other layer', 'Holes (U/D edges in the E slice)', 'States'], rows)

# ------------------------------------------------------------------------------------------------------------------
# examples: a scramble in EO-kept moves from solved (the inverse of an optimal DR) and that DR, replayed on stickers
def solve(ix, qh=None, length=None):
    """a DR of the given length (default: optimal) for case ix, optionally with exactly q quarter and h half turns on
    the side faces; canonical order, first found"""
    L = int(d[ix]) if length is None else length; out = []
    def rec(s, depth, seq, last):
        if out: return
        if depth == 0:
            if s == geom.SOLVED_IX:
                q = sum(1 for x in seq if x[0] in 'RL' and not x.endswith('2')); h = sum(1 for x in seq if x.endswith('2') and x[0] not in 'UD')
                if qh is None or (q, h) == qh: out.append(list(seq))
            return
        for mm in EOK:
            nm = NAMES[mm]
            if last and nm[0] == last[0]: continue
            if last and {nm[0], last[0]} in ({'U', 'D'}, {'R', 'L'}, {'F', 'B'}) and nm[0] < last[0]: continue
            j = int(move_ix(s, mm))
            if d[j] <= depth - 1:
                seq.append(nm); rec(j, depth - 1, seq, nm); seq.pop()
    rec(int(ix), L, [], None)
    return out[0] if out else None
EXS = {}
def example(name, sel, qh=None, note=''):
    idx = np.flatnonzero(sel); assert len(idx), name
    for ix in idx:
        sol = solve(int(ix), qh)
        if sol: break
    else: raise AssertionError(name)
    ix = int(ix); scr = cube.inv_seq(sol)
    s = cube.do(cube.SOLVED, ' '.join(scr)); assert geom.ix_of_state(s) == ix and geom.eo_fb_ok(s)
    t = cube.do(s, ' '.join(sol)); assert geom.is_dr_ud(t) and geom.eo_fb_ok(t) and len(sol) == d[ix]
    assert all(m[0] not in 'FB' or m.endswith('2') for m in sol)
    U, Dn, H = rings_of(ix)
    ex = dict(ix=ix, scramble=' '.join(scr), dr=' '.join(sol), d=int(d[ix]), drm=f"{int(F['drm_c'][ix])}c{int(F['drm_e'][ix])}e", U=ring_str(U), D=ring_str(Dn),
              Un=nice(U), Dn=nice(Dn),
              holes=[n for n, x in zip(rings.SLOT_NAME, H) if x], sigma=int(sigma[ix]), q=int(qsig[ix]), h=int(hsig[ix]), pairs=int(pairs[ix]),
              ep=int(ep[ix]), earm=int(earm[ix]), carm=int(carm[ix]), side=int(side[ix]), note=note, replayed=True)
    if c44[ix]: ex.update(hbar=int(hbar[ix]), swaps=int(swaps[ix]), slot=int(slot[ix]))
    EXS[name] = ex
    return ex
one = (Q[1].min(axis=0) == d)            # an optimal DR with a single quarter turn exists
example('h0', c44 & (hbar == 0) & (d == 3), (1, 0))
example('h0_slot2', c44 & (swaps == 0) & (slot == 2) & (d == 7))
example('h1_two_bars_one_layer', c44 & (hbar == 1) & (pairs == 4) & (slot == 0), (1, 1))
example('h1_three_pairs', c44 & (hbar == 1) & (pairs == 3) & (slot == 0) & (d == 5), (1, 1))
example('h1_trade', c44 & (hbar == 1) & (pairs == 2) & (slot == 0), (1, 1))
example('h2_sub7', c44 & (hbar == 2) & (d == 6) & (pairs == 2) & (ep == 2), (1, 2))
example('h2_not', c44 & (hbar == 2) & (d == 7), None)
example('h2_card_discard', c44 & (hbar == 2) & (ep == 0) & (d <= 6), (1, 2))
example('h3_card_switch', c44 & (hbar == 3) & (ep == 2) & (d == 8))
example('h3_sub7', c44 & (hbar == 3) & (d == 6), (1, 3))
example('h3_not', c44 & (hbar == 3) & (d == 8) & (pairs == 1))
example('h4', c44 & (hbar == 4) & (d == 8) & (pairs == 1))
example('h5', c44 & (hbar == 5))
for key, (same, blocked, opp) in (('three_1', (0, 0, 0)), ('three_2_blocked', (0, 1, 0)), ('three_2_same', (1, 0, 0)), ('three_2_opp', (0, 0, 1)), ('three_3', (1, 1, 0))):
    ks = [kid[k] for k in keys if rpairs(k) == 3 and three(k) == (same, blocked, opp)]
    example(key, c44 & np.isin(cls, ks) & (slot == 0) & one)
example('q2_route', c44 & (d == 6) & (qopt == 2) & (hbar == 3))
example('q3_route', c44 & (d == 6) & (qopt == 3) & (hbar == 3))
for drm in DRMS:
    m = M(drm); qm = 1 if drm == '4c4e' else 2
    if (m & (sigma <= 2)).any(): example(f'{drm}_s2', m & (sigma <= 2) & (d == d[m & (sigma <= 2)].max()))
    if drm != '4c4e':
        sel3 = m & (sigma == 3) & (qsig == qm)
        example(f'{drm}_s3', sel3 & (d <= 6), (qm, 3 - qm))
        if d[sel3].max() > 6: example(f'{drm}_s3_not', sel3 & (d == d[sel3].max()))
example('7c8e_5p_long', M('7c8e') & (pairs >= 5) & ~((sigma <= 3) & (qsig == 2)) & (d >= 7))
example('s4_any', (sigma == 4) & (d == 8) & M('4c2e'))
json.dump(EXS, open(OUT + 'ring_examples.json', 'w'), indent=1)
R['checks'] = [l.rstrip('\n').split('\t') for l in open(OUT + 'checks_rings.txt')]
R['n_examples'] = len(EXS)
json.dump(R, open(OUT + 'rings.json', 'w'), indent=1, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
print('ring tables written; examples replayed:', len(EXS))

# ------------------------------------------------------------------------------------------------------------------
# exact integer cells for the Lean certificate (lean/EOSwitch/gen_rings.py copies them into RingsRef.lean):
# every cell is [states, DR <= 5, DR <= 6, DR <= 7]
def cell(sel):
    return [int(sel.sum()), int((d[sel] <= 5).sum()), int((d[sel] <= 6).sum()), int((d[sel] <= 7).sum())]
REF = {}
REF['sigma_hist'] = [int((sigma == s).sum()) for s in range(6)]
REF['sigma_cells'] = [cell(sigma == s) for s in range(6)]
REF['h_bands'] = [cell(c44 & (hbar == h)) for h in range(6)]
REF['swaps_slot'] = [[a, t] + cell(c44 & (swaps == a) & (slot == t)) for a in range(6) for t in range(3)]
REF['ring_classes_hist'] = [R['classes'][str(k)] for k in range(6)]
HG = [('le1', hbar <= 1), ('2', hbar == 2), ('3', hbar == 3), ('ge4', hbar >= 4)]
REF['pairs_h'] = [[p, g] + cell(c44 & (pairs == p) & hs) for p in range(5) for g, (_, hs) in enumerate(HG) if (c44 & (pairs == p) & hs).any()]
HG3 = [hbar <= 2, hbar == 3, hbar >= 4]; CG = [card['switch'], card['your call'], card['discard']]
REF['card_split'] = [[ci, g] + cell(c44 & cs & hs) for ci, cs in enumerate(CG) for g, hs in enumerate(HG3) if (c44 & cs & hs).any()]
h3 = c44 & (hbar == 3)
REF['inside3'] = {'pairs': [cell(h3 & (pairs == p)) for p in range(4)], 'side': [cell(h3 & (side == 0)), cell(h3 & (side == 1)), cell(h3 & (side >= 2))],
                  'earm1': [cell(h3 & (earm == 1)), cell(h3 & (earm != 1))], 'edges_paired': [cell(h3 & (ep == e)) for e in range(3)]}
REF['three_rule'] = [[int(k[0]), int(k[1]), int(k[2]), 1 + int(k[0]) + int(k[1]) + int(k[2]), v['n'], int(round(v['p6'] * v['n']))] for k, v in sorted(R['three'].items())]
REF['patterns'] = [[p['a'], p['b'], p['swaps'], p['pairs'], p['n'], int(round(p['p6'] * p['n']))] for p in R['patterns']]
REF['pairs_swaps_classes'] = sorted([int(k[0]), int(k[1]), v] for k, v in R['pairs_classes'].items())
REF['pair_change'] = {k: v for k, v in R['pair_change'].items()}
REF['sigma_drm'] = {drm: [[s] + cell(M(drm) & (sigma == s)) for s in range(6) if (M(drm) & (sigma == s)).any()] for drm in DRMS}
REF['profiles'] = {drm: [[q, s - q] + cell(M(drm) & (sigma == s) & (qsig == q)) for s, q in sorted(set(zip(sigma[M(drm)].tolist(), qsig[M(drm)].tolist())))] for drm in DRMS}
REF['cross'] = {}
for drm in DRMS:
    m = M(drm); qm = 1 if drm == '4c4e' else 2; short = (sigma <= 3) & (qsig == qm); taken = np.zeros(N0, bool); out = []
    for gi, (txt, sel) in enumerate(CARD[drm]):
        g = sel & ~taken & m; taken |= g
        for si, ss in enumerate((short, ~short)):
            if (g & ss).any(): out.append([gi, si] + cell(g & ss))
    REF['cross'][drm] = out
REF['notes'] = 'cells are [states, DR<=5, DR<=6, DR<=7]; card groups in the order of xrings.CARD; short = side turns <= 3 with 1 quarter turn (4c4e) or 2 (other DRMs)'
json.dump(REF, open(OUT + 'rings_lean_ref.json', 'w'), indent=1)

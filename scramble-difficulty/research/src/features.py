"""Per-scramble features (state and text) for difficulty prediction.

usage: features.py in.tsv out.tsv [tnoodle]      in.tsv: id<TAB>scramble ; 'tnoodle' adds the scramble-text features
Feature names: suffix _UD/_FB/_RL = axis; for EO features the axis is the EO axis (edges flipped by that axis' quarter turns),
for corner/slice/DR features it is the DR axis.  _N / _I = normal / inverse scramble.
Groups (prefix of the name in the report): see FEATURE_GROUPS at the bottom."""
import sys, multiprocessing
import cube, coords, textfeat as tf

C = coords.load()
MV = coords.MV
AX = cube.AXES
OPP = {'U': 'D', 'D': 'U', 'R': 'L', 'L': 'R', 'F': 'B', 'B': 'F'}
ORDER = {'U': 0, 'D': 1, 'R': 2, 'L': 3, 'F': 4, 'B': 5}
TETRAD1 = {0, 2, 5, 7}   # URF ULB DLF DRB: one tetrad (corner orbit under half turns)

def canon_ok(last, m):
    if last is None: return True
    f, g = FACE_OF[last], m[0]
    if f == g: return False
    if OPP[f] == g and ORDER[g] < ORDER[f]: return False      # opposite faces in a fixed order
    return True
FACE_OF = coords.FACE_OF

def eo_solutions(eo0, e, co0, sl0, maxlen):
    """All canonical move sequences of length <= maxlen solving EO on axis e from eo-mask eo0 (pruned by exact
    distance). Yields (len, {a: (co, sl)}) for the two DR axes a != e."""
    T = C['eo'][e]; D = C['eo_dist'][e]
    others = [a for a in AX if a != e]
    TC = {a: C['co'][a] for a in others}; TS = {a: C['sl'][a] for a in others}
    out = []
    def rec(x, cos, sls, depth, last):
        if x == 0:
            # the same EO ending in X' instead of X (they differ by X2, which keeps EO, corner twist counts and slices)
            # is counted once, as nissy does
            if last is not None and MV[last].endswith("'"): return
            out.append((depth, dict((a, (cos[a], sls[a])) for a in others)))
            # a solved EO can be extended by more moves that keep it; those are not new EOs, stop here
            return
        if depth + D[x] > maxlen: return
        for k, m in enumerate(MV):
            if not canon_ok(last, m): continue
            y = T[x][k]
            if depth + 1 + D[y] > maxlen: continue
            rec(y, {a: TC[a][cos[a]][k] for a in others}, {a: TS[a][sls[a]][k] for a in others}, depth + 1, k)
    rec(eo0, co0, sl0, 0, None)
    return out

def tw(x):
    t = []
    for _ in range(8): t.append(x % 3); x //= 3
    return t

def nbad_c(cocoord): return sum(1 for t in tw(cocoord) if t)
def slice_in(slmask, a): return sum(1 for i in cube.SLICE[a] if slmask >> i & 1)

def pairs(st):
    """corner-edge pairs formed anywhere: a corner and an edge next to each other whose two shared stickers match."""
    fl = cube.facelets(st)
    n = 0
    for ci, cf in enumerate(cube.CF):
        cfaces = {cube.FACES[k // 9]: fl[k] for k in cf}
        for ei, ef in enumerate(cube.EF):
            efaces = [cube.FACES[k // 9] for k in ef]
            if all(f in cfaces for f in efaces):
                if all(fl[k] == cfaces[cube.FACES[k // 9]] for k in ef):
                    n += 1
    return n

def side_feats(st, tag, F):
    fl = cube.facelets(st)
    eo = {e: coords.f_eo(st, e) for e in AX}
    co = {a: coords.f_co(st, a) for a in AX}
    sl = {a: coords.f_sl(st, a) for a in AX}
    for a in AX:
        t = tw(co[a])
        F[f'cw_{a}_{tag}'] = sum(1 for x in t if x == 1)
        F[f'ccw_{a}_{tag}'] = sum(1 for x in t if x == 2)
        bad = [i for i in range(8) if t[i]]
        F[f'tetrad_split_{a}_{tag}'] = abs(sum(1 for i in bad if i in TETRAD1) - sum(1 for i in bad if i not in TETRAD1))
        # bad corners per a-layer (the two layers perpendicular to a)
        lay = {'UD': {0, 1, 2, 3}, 'FB': {0, 1, 4, 5}, 'RL': {0, 3, 4, 7}}[a]   # U layer / F layer / R layer positions
        F[f'clayer_diff_{a}_{tag}'] = abs(sum(1 for i in bad if i in lay) - sum(1 for i in bad if i not in lay))
        # where the a-coloured stickers of bad corners point: along which of the other axes
        for e in AX:
            if e == a: continue
            F[f'cface_{a}_{e}_{tag}'] = sum(1 for i in bad
                                           if cube.faxis(cube.FACES[[k for k in cube.CF[i] if cube.faxis(fl[k]) == a][0] // 9]) == e)
    for e in AX:
        bm = eo[e]
        for a in AX:   # bad edges (EO e) sitting in the a-slice positions
            F[f'be_in_slice_{e}_{a}_{tag}'] = sum(1 for i in cube.SLICE[a] if bm >> i & 1)
    # one-move lookahead: fewest bad edges / bad corners after one move on this side
    for e in AX:
        F[f'be_1mv_{e}_{tag}'] = min(bin(C['eo'][e][eo[e]][k]).count('1') for k in range(18))
    for a in AX:
        F[f'mc_1mv_{a}_{tag}'] = min(nbad_c(C['co'][a][co[a]][k]) for k in range(18))
    F[f'pairs_{tag}'] = pairs(st)
    # EO search on this side
    for e in AX:
        d = C['eo_dist'][e][eo[e]]
        F[f'eo_opt_{e}_{tag}'] = d
        sols = eo_solutions(eo[e], e, {a: co[a] for a in AX if a != e}, {a: sl[a] for a in AX if a != e}, max(5, d))
        F[f'n_eo4_{e}_{tag}'] = sum(1 for L, _ in sols if L <= 4)
        F[f'n_eo5_{e}_{tag}'] = sum(1 for L, _ in sols if L <= 5)
        for a in AX:
            if a == e: continue
            best_c = min((nbad_c(x[a][0]) for L, x in sols), default=8)
            best_ce = min((nbad_c(x[a][0]) + 2 * (4 - slice_in(x[a][1], a)) for L, x in sols), default=16)
            best_lc = min((L + nbad_c(x[a][0]) for L, x in sols), default=20)
            n_easy = sum(1 for L, x in sols if nbad_c(x[a][0]) <= 4 and 4 - slice_in(x[a][1], a) <= 2)
            F[f'post_eo_c_{e}_{a}_{tag}'] = best_c
            F[f'post_eo_ce_{e}_{a}_{tag}'] = best_ce
            F[f'post_eo_lc_{e}_{a}_{tag}'] = best_lc
            F[f'post_eo_neasy_{e}_{a}_{tag}'] = n_easy
    return eo, co, sl

def feats(scr, tnoodle=False):
    st = cube.seq(scr); sti = cube.inv(st)
    F = {}
    eo, co, sl = side_feats(st, 'N', F)
    eoi, coi, sli = side_feats(sti, 'I', F)
    for e in AX:
        F[f'be_{e}'] = bin(eo[e]).count('1')
        assert F[f'be_{e}'] == bin(eoi[e]).count('1')
    for a in AX:
        F[f'mc_{a}'] = nbad_c(co[a]); assert F[f'mc_{a}'] == nbad_c(coi[a])
        F[f'slin_{a}'] = slice_in(sl[a], a); assert F[f'slin_{a}'] == slice_in(sli[a], a)
    F['solved_c'] = sum(1 for i in range(8) if st[0][i] == i and st[1][i] == 0)
    F['solved_e'] = sum(1 for i in range(12) if st[2][i] == i and st[3][i] == 0)
    cp = st[0]; F['cparity'] = sum(1 for i in range(8) for j in range(i) if cp[j] > cp[i]) % 2
    if tnoodle:
        mid, padded = tf.strip(scr)
        assert padded
        F['t_len'] = len(mid)
        sp = tf.text_split(mid)
        for a in AX:
            F[f't_run_{a}'] = sp[a][1]
            F[f't_dr_{a}'] = len(mid) - sp[a][1]
        ax, x, h, y, drl = tf.text_dr(mid)
        F['t_axis'] = ax
        F['t_dr'] = drl
        F['t_short'] = min(x, y); F['t_long'] = max(x, y)
        F['t_p1_end'] = int(y > x)
        for a in AX:   # quarter turns of each axis in the middle
            F[f't_qt_{a}'] = sum(1 for m in mid if cube.faxis(m[0]) == a and not m.endswith('2'))
    return F

def work(job):
    k, scr, tn = job
    return k, feats(scr, tn)

if __name__ == '__main__':
    inp, out = sys.argv[1], sys.argv[2]; tn = len(sys.argv) > 3 and sys.argv[3] == 'tnoodle'
    W = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    jobs = [(*l.rstrip('\n').split('\t')[:2], tn) for l in open(inp) if l.strip()]
    keys = None
    with open(out, 'w') as f, multiprocessing.Pool(W) as pool:
        for i, (k, F) in enumerate(pool.imap(work, jobs, chunksize=8)):
            if keys is None:
                keys = list(F); f.write('id\t' + '\t'.join(keys) + '\n')
            f.write(k + '\t' + '\t'.join(str(F[x]) for x in keys) + '\n')
            if (i + 1) % 1000 == 0: print(i + 1, flush=True)

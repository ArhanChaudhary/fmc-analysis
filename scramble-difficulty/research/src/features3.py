"""Features the server proposed, per scramble and DR axis (tested in claims_extra.py):
  Zagros: bad edges on the two EO axes of a DR axis and how many they share  -> ov_<a> (bad on both), un_<a> (bad on either)
  Levi Gibson: for DR axis a with EO axes e1, e2: a-layer pieces and a-slice pieces bad on e1 only / e2 only / both
               -> lg_<a>_{L,S}{1,2,b}
  rodneykinney: DRM-style pairs already formed: an a-slice edge sitting in an a layer, next to a corner of that layer
               whose a-coloured sticker faces away from it (on the side face the edge does not touch)
               -> drmp_<a>_{N,I}
  Levi Gibson: corner QT: ignore corner twists, count the quarter turns the corner permutation needs to reach HTR with
               DR moves of axis a  -> cqt_<a>_{N,I}
usage: features3.py in.tsv out.tsv   |   features3.py selftest"""
import sys, itertools
from collections import deque
import cube

AX = cube.AXES
def third(a, b): return [x for x in AX if x not in (a, b)][0]

# ---- corner QT tables: perm (as tuple, position -> piece) -> min number of quarter turns of the a faces, half turns free
def cmove(name): return cube.MOVES[name][0]
def pmul(p, m): return tuple(p[m[i]] for i in range(8))
HALF = [cmove(f + '2') for f in 'URFDLB']
def qt_table(a):
    q = [cmove(f + s) for f in a for s in ('', "'")]
    start = {tuple(range(8))}; dq = deque(start)
    while dq:                                   # half-turn orbit of solved = corners in HTR
        p = dq.popleft()
        for m in HALF:
            x = pmul(p, m)
            if x not in start: start.add(x); dq.append(x)
    dist = {p: 0 for p in start}; layer = list(start); k = 0
    while layer:
        nxt = []
        for p in layer:                         # one quarter turn, then close under half turns
            for m in q:
                x = pmul(p, m)
                if x not in dist: dist[x] = k + 1; nxt.append(x)
        dq = deque(nxt)
        while dq:
            p = dq.popleft()
            for m in HALF:
                x = pmul(p, m)
                if x not in dist: dist[x] = k + 1; nxt.append(x); dq.append(x)
        layer = nxt; k += 1
    return dist, len(start)
_QT = {}
def QT(a):
    if a not in _QT: _QT[a] = qt_table(a)[0]
    return _QT[a]

def drm_pairs(st, a):
    fl = cube.facelets(st); n = 0
    for i in range(12):
        if i in cube.SLICE[a] or st[2][i] not in cube.SLICE[a]: continue
        ef = [cube.FACES[k // 9] for k in cube.EF[i]]
        side_axis = [cube.faxis(f) for f in ef if cube.faxis(f) != a][0]
        free = third(a, side_axis)
        for j in range(8):
            cf = [cube.FACES[k // 9] for k in cube.CF[j]]
            if not all(f in cf for f in ef): continue
            k = [k for k in cube.CF[j] if cube.faxis(fl[k]) == a][0]
            if cube.faxis(cube.FACES[k // 9]) == free: n += 1
    return n

def feats(scr):
    st = cube.seq(scr); sti = cube.inv(st); F = {}
    fl = cube.facelets(st)
    eo = {e: cube.eo_axis(fl, e) for e in AX}
    for a in AX:
        e1, e2 = [e for e in AX if e != a]
        F[f'ov_{a}'] = sum(1 for i in range(12) if eo[e1][i] and eo[e2][i])
        F[f'un_{a}'] = sum(1 for i in range(12) if eo[e1][i] or eo[e2][i])
        for tag, isslice in (('L', False), ('S', True)):
            idx = [i for i in range(12) if (st[2][i] in cube.SLICE[a]) == isslice]
            F[f'lg_{a}_{tag}1'] = sum(1 for i in idx if eo[e1][i] and not eo[e2][i])
            F[f'lg_{a}_{tag}2'] = sum(1 for i in idx if eo[e2][i] and not eo[e1][i])
            F[f'lg_{a}_{tag}b'] = sum(1 for i in idx if eo[e1][i] and eo[e2][i])
        F[f'drmp_{a}_N'] = drm_pairs(st, a); F[f'drmp_{a}_I'] = drm_pairs(sti, a)
        F[f'cqt_{a}_N'] = QT(a)[st[0]]; F[f'cqt_{a}_I'] = QT(a)[sti[0]]
    return F

def selftest():
    for a in AX:
        d, n0 = qt_table(a)
        from collections import Counter
        print(a, 'corner perms', len(d), 'in HTR', n0, 'QT histogram', sorted(Counter(d.values()).items()))
    # Levi Gibson: the QT count is the same on all three axes, for every corner permutation
    same = sum(1 for p in QT('UD') if QT('UD')[p] == QT('FB')[p] == QT('RL')[p])
    print('QT equal on the three axes for', same, 'of', len(QT('UD')), 'corner permutations')
    # and on the inverse permutation
    inv = lambda p: tuple(sorted(range(8), key=lambda i: p[i]))
    print('QT of the inverse permutation equal for', sum(1 for p in QT('UD') if QT('UD')[p] == QT('UD')[inv(p)]), 'of', len(QT('UD')))
    # pairs: R on a solved cube is 4c4e with 4 pairs (eo-switch test A3)
    print('R from solved: DRM pairs (U/D axis)', drm_pairs(cube.seq('R'), 'UD'), '; R U2 R:', drm_pairs(cube.seq("R U2 R"), 'UD'))

if __name__ == '__main__':
    if sys.argv[1] == 'selftest': selftest(); sys.exit()
    with open(sys.argv[2], 'w') as f:
        keys = None
        for l in open(sys.argv[1]):
            if not l.strip(): continue
            k, s = l.rstrip('\n').split('\t')[:2]
            D = feats(s)
            if keys is None: keys = list(D); f.write('id\t' + '\t'.join(keys) + '\n')
            f.write(k + '\t' + '\t'.join(str(D[x]) for x in keys) + '\n')

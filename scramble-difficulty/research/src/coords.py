"""Small coordinates with move tables, built from the cubie model (cube.py) by BFS:
  eo[e]  : 12-bit mask of bad edges for EO on axis e (positions)          2048 values
  co[a]  : twist of each corner position w.r.t. axis a, base-3 number       2187 values
  sl[a]  : 12-bit mask of positions holding the a-slice edges                495 values
Each table T[m][x] = coordinate after applying move m (state * m).  Checked on random states in selftest.
Distances: eo_dist[e][mask] = optimal EO length (HTM, 18 moves)."""
import pickle, os, random
from collections import deque
import cube

MV = list(cube.MOVES)                     # U U2 U' R R2 R' F ... (order of cube.MOVES)
FACE_OF = [m[0] for m in MV]
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, '..', 'out', 'coords.pkl')

def f_eo(st, e):
    return sum(b << i for i, b in enumerate(cube.eo_axis(cube.facelets(st), e)))
def f_co(st, a):
    t = cube.co_axis(cube.facelets(st), a)
    return sum(x * 3 ** i for i, x in enumerate(t))
def f_sl(st, a):
    S = cube.SLICE[a]
    return sum(1 << i for i in range(12) if st[2][i] in S)

def build_table(f):
    rep = {f(cube.SOLVED): cube.SOLVED}; q = deque([cube.SOLVED]); T = {}
    while q:
        s = q.popleft(); x = f(s); T[x] = [None] * 18
        for k, m in enumerate(MV):
            t = cube.mul(s, cube.MOVES[m]); y = f(t); T[x][k] = y
            if y not in rep: rep[y] = t; q.append(t)
    return T

def bfs_dist(T, goal):
    d = {goal: 0}; q = deque([goal])
    while q:
        x = q.popleft()
        for y in T[x]:
            if y not in d: d[y] = d[x] + 1; q.append(y)
    return d

def load():
    if os.path.exists(CACHE):
        return pickle.load(open(CACHE, 'rb'))
    C = {'eo': {}, 'co': {}, 'sl': {}, 'eo_dist': {}}
    for a in cube.AXES:
        C['eo'][a] = build_table(lambda s, a=a: f_eo(s, a))
        C['co'][a] = build_table(lambda s, a=a: f_co(s, a))
        C['sl'][a] = build_table(lambda s, a=a: f_sl(s, a))
        C['eo_dist'][a] = bfs_dist(C['eo'][a], 0)
    pickle.dump(C, open(CACHE, 'wb'))
    return C

def selftest():
    C = load()
    for a in cube.AXES:
        assert len(C['eo'][a]) == 2048 and len(C['co'][a]) == 2187 and len(C['sl'][a]) == 495, a
    rnd = random.Random(5)
    for _ in range(200):
        s = cube.seq([rnd.choice(MV) for _ in range(30)])
        for k, m in enumerate(MV):
            t = cube.mul(s, cube.MOVES[m])
            for a in cube.AXES:
                assert C['eo'][a][f_eo(s, a)][k] == f_eo(t, a)
                assert C['co'][a][f_co(s, a)][k] == f_co(t, a)
                assert C['sl'][a][f_sl(s, a)][k] == f_sl(t, a)
    from collections import Counter
    print('coords ok; optimal EO length distribution (uniform over 2048):', sorted(Counter(C['eo_dist']['FB'].values()).items()))

if __name__ == '__main__':
    selftest()

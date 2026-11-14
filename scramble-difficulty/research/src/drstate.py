"""DR states of a solution, with the coordinates the exact finish table is indexed by.

The functions below are the ones gaps/research/src/population.py takes from judging-a-dr's many_examples.py (text,
niss, perm, state, View, canon), copied here unchanged so that the DR lists can be made on a machine that has only
this folder; fmccube.py next to this file is judging-a-dr's research/tool/fmccube.py.  `python3 drstate.py` checks
them against the originals on random solutions (needs the repository)."""
import fmccube as fc

AXIS = {'U': 0, 'D': 0, 'R': 1, 'L': 1, 'F': 2, 'B': 2}
SUF = {1: '', 2: '2', 3: "'"}
def text(moves): return ' '.join(b + SUF[t] for b, t in moves)
def niss(n, i): return ' '.join(x for x in (text(n), f'({text(i)})' if i else '') if x)

# ---- a fast sticker simulator (permutations of the 54 stickers)
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

def canon(mv):
    """One side's moves with the quarter turns among its last moves (those about one axis) written clockwise."""
    mv = list(mv); i = len(mv)
    while i > 0 and AXIS[mv[i - 1][0]] == AXIS[mv[-1][0]]: i -= 1
    return mv[:i] + [(b, 1 if t in (1, 3) else t) for b, t in mv[i:]]

def rank(p):
    n = len(p); r = 0; f = [1] * (n + 1)
    for i in range(1, n + 1): f[i] = f[i - 1] * i
    for i in range(n):
        r += sum(1 for x in p[i + 1:] if x < p[i]) * f[n - 1 - i]
    return r
def invperm(p):
    q = [0] * len(p)
    for i, x in enumerate(p): q[x] = i
    return q

if __name__ == '__main__':
    import sys, random
    sys.path.insert(0, '/data/fmc/judging-a-dr/research/src')
    import many_examples as me
    rnd = random.Random(7); n = 0
    for _ in range(300):
        scr = [(rnd.choice('UDRLFB'), rnd.choice((1, 2, 3))) for _ in range(22)]
        a = [(rnd.choice('UDRLFB'), rnd.choice((1, 2, 3))) for _ in range(rnd.randint(0, 7))]
        b = [(rnd.choice('UDRLFB'), rnd.choice((1, 2, 3))) for _ in range(rnd.randint(0, 5))]
        assert perm(scr) == me.perm(scr) and canon(a) == me.canon(a) and niss(a, b) == me.niss(a, b)
        s1 = state(perm(scr), a, b); assert s1 == me.state(me.perm(scr), a, b)
        # a DR state: DR moves on one axis from solved, seen in each view
        dr = [(rnd.choice('UD'), rnd.choice((1, 2, 3))) if rnd.random() < .5 else (rnd.choice('RLFB'), 2) for _ in range(15)]
        for name in VIEWS:
            for st in (s1, perm(dr)):
                assert VIEWS[name].arrays(st) == me.VIEWS[name].arrays(st); n += 1
    print('drstate agrees with many_examples on', n, 'state reads')

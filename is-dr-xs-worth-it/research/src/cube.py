#!/usr/bin/env python3
"""A whole Rubik's cube at the sticker level, centers included, built from geometry so that no permutation is typed
by hand.

  axes      x = R (+) / L (-),  y = U (+) / D (-),  z = F (+) / B (-)
  sticker   (cubie position, outward normal), 54 of them; index order: faces U D R L F B, each face row by row
  state     s[i] = the home index of the sticker now sitting at place i (so its colour is the face of s[i])
  moves     the 18 face turns, the slice turns M E S (M follows L, E follows D, S follows F), the wide turns
            Uw = U E' etc., and the rotations x y z (x follows R, y follows U, z follows F)
  apply     t = s after move m:  t[m[i]] = s[i]     (the sticker at place i is carried to place m[i])

Clockwise seen from outside the face = a rotation by -90 degrees about the outward normal."""
import itertools, re

AX = {'U': (1, 1), 'D': (1, -1), 'R': (0, 1), 'L': (0, -1), 'F': (2, 1), 'B': (2, -1)}   # face -> (axis, sign)
FACES = 'UDRLFB'

def _stickers():
    out = []
    for f in FACES:
        a, sg = AX[f]
        cells = []
        for p in itertools.product((-1, 0, 1), repeat=3):
            if p[a] == sg: cells.append(p)
        for p in sorted(cells):
            n = [0, 0, 0]; n[a] = sg
            out.append((p, tuple(n)))
    return out
ST = _stickers()
IDX = {s: i for i, s in enumerate(ST)}
FACE_OF = [next(f for f in FACES if AX[f] == (max(range(3), key=lambda k: abs(n[k])), n[max(range(3), key=lambda k: abs(n[k]))])) for p, n in ST]

def _rot(v, a, quarter):
    """Rotate vector v about axis a by quarter * (-90 degrees) (i.e. quarter = 1 is clockwise seen from +a)."""
    b, c = [(1, 2), (2, 0), (0, 1)][a]            # (b, c) such that a x b = c in a right-handed frame... rotation in the b-c plane
    v = list(v)
    for _ in range(quarter % 4):
        # -90 degrees about +a: b -> -c ... derived from the U check: about +y, (x, z) -> (-z, x); here a=1, b=2 (z), c=0 (x)
        vb, vc = v[b], v[c]
        v[b], v[c] = vc, -vb
    return tuple(v)

def _layer_move(a, layers, quarter):
    m = list(range(54))
    for i, (p, n) in enumerate(ST):
        if p[a] in layers:
            m[i] = IDX[(_rot(p, a, quarter), _rot(n, a, quarter))]
    return m

def _build():
    M = {}
    def add(name, a, layers, q):       # q = quarter turns clockwise seen from +a
        for k, suf in ((1, ''), (2, '2'), (3, "'")):
            M[name + suf] = _layer_move(a, layers, (q * k) % 4)
    for f in FACES:
        a, sg = AX[f]
        add(f, a, (sg,), sg)                      # clockwise seen from outside
        add(f + 'w', a, (sg, 0), sg)
        add(f.lower(), a, (sg, 0), sg)
    add('M', 0, (0,), -1); add('E', 1, (0,), -1); add('S', 2, (0,), 1)
    add('x', 0, (-1, 0, 1), 1); add('y', 1, (-1, 0, 1), 1); add('z', 2, (-1, 0, 1), 1)
    return M
MOVES = _build()
SOLVED = tuple(range(54))

def apply(s, m):
    t = [0] * 54
    for i in range(54): t[m[i]] = s[i]
    return tuple(t)

TOKEN = re.compile(r"[UDRLFBMESxyz]w?[2']?|[udrlfb][2']?")
def parse(txt):
    txt = txt.replace('’', "'").replace('‘', "'").replace('`', "'")
    toks = TOKEN.findall(txt)
    assert ''.join(toks) == re.sub(r'\s+', '', txt), f'cannot parse {txt!r}'
    return toks
def do(s, seq):
    for t in (parse(seq) if isinstance(seq, str) else seq): s = apply(s, MOVES[t])
    return s
def inv_seq(seq):
    toks = parse(seq) if isinstance(seq, str) else list(seq)
    return [t[:-1] if t.endswith("'") else (t if t.endswith('2') else t + "'") for t in reversed(toks)]
def compose(a, b):
    """State of (a then b) as sequences applied to solved, given the two states."""
    # b[i] is the place the sticker now at i came from when B is done alone, so after A then B place i holds a[b[i]].
    return tuple(a[b[i]] for i in range(54))
def inverse(s):
    t = [0] * 54
    for i in range(54): t[s[i]] = i
    return tuple(t)
def colour(s, i): return FACE_OF[s[i]]
def cancel(seq):
    """A sequence of face turns with all cancelling done: consecutive turns about one axis are merged face by face."""
    import collections
    axf = {'U': 'UD', 'D': 'UD', 'R': 'RL', 'L': 'RL', 'F': 'FB', 'B': 'FB'}
    q = lambda m: 2 if m.endswith('2') else 3 if m.endswith("'") else 1
    seq = parse(seq) if isinstance(seq, str) else list(seq); out = []; i = 0
    while i < len(seq):
        ax = axf[seq[i][0]]; cnt = {}
        while out and axf[out[-1][0]] == ax:
            m = out.pop(); cnt[m[0]] = cnt.get(m[0], 0) + q(m)
        while i < len(seq) and axf[seq[i][0]] == ax:
            cnt[seq[i][0]] = cnt.get(seq[i][0], 0) + q(seq[i]); i += 1
        for f in ax:
            if cnt.get(f, 0) % 4: out.append(f + {1: '', 2: '2', 3: "'"}[cnt[f] % 4])
    return out

if __name__ == '__main__':
    # U clockwise from above carries UFR to UFL: the U-sticker of UFR (1,1,1) goes to (-1,1,1)
    assert MOVES['U'][IDX[((1, 1, 1), (0, 1, 0))]] == IDX[((-1, 1, 1), (0, 1, 0))]
    # R clockwise carries UFR to UBR, F clockwise carries UFR to DFR
    assert MOVES['R'][IDX[((1, 1, 1), (0, 1, 0))]] == IDX[((1, 1, -1), (0, 0, -1))]
    assert MOVES['F'][IDX[((1, 1, 1), (0, 1, 0))]] == IDX[((1, -1, 1), (1, 0, 0))]
    for name, n in (("R U R' U'", 6), ('R U', 105), ("R U2 D' B D'", 1260), ('M', 4)):
        s = SOLVED; k = 0
        while True:
            s = do(s, name); k += 1
            if s == SOLVED: break
            assert k < 2000
        assert k == n, (name, k)
    assert do(SOLVED, "R L' x'") == do(SOLVED, "M"), "R L' = x M"
    assert do(SOLVED, "U D' y'") == do(SOLVED, "E"), "U D' = y E"
    assert do(SOLVED, "F B' z'") == do(SOLVED, "S'")
    assert do(SOLVED, "Rw") == do(SOLVED, "R M'") and do(SOLVED, 'Uw') == do(SOLVED, "U E'") and do(SOLVED, 'Fw') == do(SOLVED, 'F S')
    a = do(SOLVED, "R U F2"); b = do(SOLVED, "D L' B"); assert compose(a, b) == do(SOLVED, "R U F2 D L' B")
    assert compose(a, inverse(a)) == SOLVED and inverse(a) == do(SOLVED, inv_seq("R U F2"))
    print('cube model ok')

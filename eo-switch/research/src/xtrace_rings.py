#!/usr/bin/env python3
"""The two rings of the switched case, read on the normal side, on uniformly random F/B-EO-solved cubes
(niss_checks.py's sampler).  The reading uses only what a solver sees on the normal cube:
  1. each U/D edge sitting in the E slice marks its own edge place (its two colours) as bad;
  2. each misoriented corner marks its own corner place (its three colours) as bad, and points at the edge place of
     its U/D colour and the side colour that is NOT showing on the U/D face (the colours of its two stickers on the
     side faces, as in wen's pair tracing);
  3. each E-slice edge sitting in the U or D layer marks its own slot (its two colours) as a hole.
The truth is the ring picture of the inverse cube's case (rings.rings_of).  For 4c4e the half turns to two bars
computed from the reading are compared with the table.  The control points each corner at the other edge place.
Output: out/checks_trace_rings.tsv.  usage: xtrace_rings.py [cubes]"""
import os, sys, random, collections, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import geom, pop, rings
from geom import cube, coords
from niss_checks import rand_state, F, CF, EF
CL = pickle.load(open(os.path.join(pop.OUT, 'big', 'ring_classes.pkl'), 'rb'))['dist']
Z = rings.load(); HBAR = Z['hbar']
UFACE = rings.U_FACE; DFACE = rings.D_FACE              # side face (= side colour) of edge place k of each ring
def read(s, control=False):
    ue, de = [0] * 4, [0] * 4; uh, dh = [0] * 4, [0] * 4; holes = [0] * 4
    for i, p in enumerate(geom.EDGES):
        cols = {cube.colour(s, EF[i][0]), cube.colour(s, EF[i][1])}
        ud = cols & set('UD')
        if p[1] == 0 and ud:                              # a U/D edge in the E slice
            side = (cols - ud).pop()
            (ue if 'U' in ud else de)[(UFACE if 'U' in ud else DFACE).index(side)] = 1
        if p[1] != 0 and not ud:                          # an E-slice edge in the U or D layer
            holes[next(k for k, n in enumerate(rings.SLOT_NAME) if set(n) == cols)] = 1
    for i in range(8):
        cols = [cube.colour(s, CF[i][k]) for k in range(3)]
        if cols[0] in 'UD': continue
        ud = next(c for c in cols if c in 'UD'); on_ud_face = cols[0]
        other = next(c for c in cols if c not in 'UD' and c != on_ud_face)
        target = on_ud_face if control else other         # the side colour of the edge place it points at
        faces = UFACE if ud == 'U' else DFACE; hk = uh if ud == 'U' else dh
        # the corner's own place in its ring: between the edge places of its two side colours
        a, b = faces.index(on_ud_face), faces.index(other)
        k = a if (a + 1) % 4 == b else b                  # corner k sits between edge k and edge k+1
        hk[k] = 1 if faces[(k + 1) % 4] == target else 2
    return (tuple(ue), tuple(uh)), (tuple(de), tuple(dh)), tuple(holes)
def hbar_of(U, D, H):
    return max(CL[(rings.canon(U), rings.canon(D))], rings.slot_type(H))
if __name__ == '__main__':
    rng = random.Random(13); N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    res = collections.Counter(); tot = collections.Counter()
    for t in range(N):
        for want, tag in ((None, 'uniform'), ((4, 4), '4c4e')):
            s = rand_state(rng, want); ix = geom.ix_of_state(cube.inverse(s)); truth = rings.rings_of(ix)
            got = read(s); ctl = read(s, control=True)
            checks = {'both rings and the holes of the switched case, read on normal by colours': got == truth,
                      'control (not expected): each corner pointed at the other edge place': ctl == truth}
            if want == (4, 4):
                checks['half turns to two bars from the normal-side reading = the table (4c4e)'] = hbar_of(*got) == int(HBAR[ix])
            for k, ok in checks.items(): tot[(k, tag)] += 1; res[(k, tag)] += bool(ok)
    with open(os.path.join(pop.OUT, 'checks_trace_rings.tsv'), 'w') as f:
        f.write('check\tsample\tcubes\tholds\n')
        for (k, tag), n in tot.items():
            f.write(f'{k}\t{tag}\t{n}\t{res[(k, tag)]}\n'); print(f'{res[(k, tag)]:6d}/{n:6d} {tag:8s} {k}')

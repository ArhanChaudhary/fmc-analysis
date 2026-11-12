#!/usr/bin/env python3
"""Tracing checks the rules of the write-up rely on, on uniformly random F/B-EO-solved cubes (niss_checks.py's
sampler; the truth is the feature of the inverse, from features.py):
  1. paired edges on inverse = bad E-slice edges on normal (U/D pieces in the E slice) for which some misoriented
     corner shows the edge's two colours on its two side stickers (the pair tracing of the Hitchhiker's Guide to DR,
     counted per edge instead of per corner);
  2. side pairs on inverse, traced on normal: for each E-slice piece sitting in the U or D layer (its two colours),
     each misoriented corner carrying both colours that shows its F/B colour (the EO axis's colour) on the U/D face
     counts one; the variant with the R/L colour on the U/D face is the control (expected to fail);
  3. edge ARM on inverse = U/D pieces sitting in the E slice on normal whose other colour is an F/B colour (their
     home is in the M slice: UF, UB, DF, DB).
Output: out/checks_trace.tsv.  usage: xtrace.py [cubes]"""
import os, sys, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import geom, pop
from geom import cube, coords
from niss_checks import rand_state, F, CF, EF
def e_cols(s, i): return {cube.colour(s, EF[i][0]), cube.colour(s, EF[i][1])}
def bad_e_in_E(s):      # U/D pieces sitting in the E slice
    return [e_cols(s, i) for i, p in enumerate(geom.EDGES) if p[1] == 0 and e_cols(s, i) & set('UD')]
def E_pieces_in_UD(s):  # E-slice pieces sitting in the U/D layers, with the place
    return [(i, e_cols(s, i)) for i, p in enumerate(geom.EDGES) if p[1] != 0 and not e_cols(s, i) & set('UD')]
def mis_corners(s):
    out = []
    for i in range(8):
        cols = [cube.colour(s, CF[i][k]) for k in range(3)]
        if cols[0] in 'UD': continue
        ud = [k for k in range(3) if cols[k] in 'UD'][0]
        face = geom.FACE_OF_NORMAL[cube.ST[CF[i][ud]][1]]
        out.append((cols, {cols[1], cols[2]}, face))
    return out
def paired_edges_traced(s):
    mc = mis_corners(s)
    return sum(1 for ec in bad_e_in_E(s) if any(side == ec for _, side, _ in mc))
def side_traced(s, v):
    n = 0
    for _, ec in E_pieces_in_UD(s):
        for i in range(8):
            cols = [cube.colour(s, CF[i][k]) for k in range(3)]
            if cols[0] in 'UD' or not ec <= set(cols): continue
            on_ud = [cube.colour(s, CF[i][k]) for k in range(3) if geom.FACE_OF_NORMAL[cube.ST[CF[i][k]][1]] in 'UD'][0]
            if (on_ud in 'FB') == (v == 'fb'): n += 1
    return n
if __name__ == '__main__':
    rng = random.Random(11); N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    res = collections.Counter(); tot = collections.Counter()
    for t in range(N):
        for want, tag in ((None, 'uniform'), ((4, 2), '4c2e'), ((4, 4), '4c4e')):
            s = rand_state(rng, want); si = cube.inverse(s); ix = geom.ix_of_state(si)
            checks = {'paired edges (bad U/D edges with a pair) on inverse = bad E-slice edges on normal with a corner showing their colours on its side stickers': paired_edges_traced(s) == F['edges_paired'][ix],
                      'side pairs on inverse = E-slice pieces in U/D on normal x misoriented corners with both their colours showing the F/B colour on the U/D face': side_traced(s, 'fb') == F['side'][ix],
                      'edge ARM on inverse = U/D pieces in the E slice on normal whose other colour is F/B': sum(1 for ec in bad_e_in_E(s) if ec & set('FB')) == F['earm'][ix],
                      'control (not expected): the same with the R/L colour on the U/D face': side_traced(s, 'rl') == F['side'][ix]}
            for k, ok in checks.items():
                tot[(k, tag)] += 1; res[(k, tag)] += bool(ok)
    with open(os.path.join(pop.OUT, 'checks_trace.tsv'), 'w') as f:
        f.write('check\tsample\tcubes\tholds\n')
        for (k, tag), n in tot.items():
            f.write(f'{k}\t{tag}\t{n}\t{res[(k, tag)]}\n'); print(f'{res[(k, tag)]:6d}/{n:6d} {tag:8s} {k}')

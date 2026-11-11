#!/usr/bin/env python3
"""Write out/kinds.tsv: every kind of DR-xs state for U/D colours with its coordinates (co, eo, sl), the faces the
corners are oriented on, the number of flipped edges, the fewest slices and the fewest turns to a real DR, and a
shortest fix.  Also the target lists for the Rust searcher (out/targets/*.txt)."""
import pickle, os, collections
import cube, fe, coords
from fecosets import path, C
d = pickle.load(open('/data/fmc/is-dr-xs-worth-it/research/out/fecosets.pkl', 'rb'))
rep, nbr, dsl, dmv, bm = d['rep'], d['nbr'], d['dsl'], d['dmv'], d['bm']
OUT = '/data/fmc/is-dr-xs-worth-it/research/out/'
os.makedirs(OUT + 'targets', exist_ok=True)
rows = []
for g in sorted(nbr):
    co, eo, sl = coords.coords(rep[g])
    rows.append(dict(co=co, eo=eo, sl=sl, f='RL UD FB'.split()[g[0]], flips=sum(g[1]), slicebit=g[2][0], slices=dsl[(g, 3)], turns=dmv[(g, 3)],
                     fl=''.join(map(str, g[1])), fix=path(bm, g)))
assert len({(r['co'], r['eo'], r['sl']) for r in rows}) == len(rows), 'two kinds share coordinates'
with open(OUT + 'kinds.tsv', 'w') as f:
    f.write('co\teo\tsl\tfaces\tflips\tslice_bit\tslices\tturns_to_dr\tflip_places\tfix\n')
    for r in rows: f.write('\t'.join(str(r[k]) for k in ('co', 'eo', 'sl', 'f', 'flips', 'slicebit', 'slices', 'turns', 'fl', 'fix')) + '\n')
def target(name, pred):
    sel = [r for r in rows if pred(r)]
    with open(OUT + f'targets/{name}.txt', 'w') as f:
        f.write(f'# {name}: {len(sel)} cosets (co eo sl)\n')
        for r in sel: f.write(f"{r['co']} {r['eo']} {r['sl']}\n")
    return len(sel)
on = lambda r: r['f'] == 'UD'
print('dr', target('dr', lambda r: r['slices'] == 0))
print('1s', target('1s', lambda r: r['slices'] == 1))
print('1s_fix2', target('1s_fix2', lambda r: r['slices'] == 1 and r['turns'] == 2))
print('1s_fix4', target('1s_fix4', lambda r: r['slices'] == 1 and r['turns'] <= 4))
print('2s8fe', target('2s8fe', lambda r: r['slices'] == 2 and r['flips'] == 8 and not on(r)))
print('2s', target('2s', lambda r: r['slices'] == 2))
print('xs', target('xs', lambda r: True))

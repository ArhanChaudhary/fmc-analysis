"""Extra axis-free features: per edge, on how many EO axes it is bad (histogram eb0..eb3); per corner, on how many
DR axes it is twisted (cb0..cb3); axially reduced pieces (every sticker on a face of its own colour's axis):
ar_c, ar_e.  Also the quarter-turn 'distance' features of the corners are left out (see features.py).
usage: features2.py in.tsv out.tsv"""
import sys, cube

def f2(scr):
    st = cube.seq(scr); fl = cube.facelets(st)
    eo = {e: cube.eo_axis(fl, e) for e in cube.AXES}
    co = {a: cube.co_axis(fl, a) for a in cube.AXES}
    D = {}
    eb = [sum(eo[e][i] for e in cube.AXES) for i in range(12)]
    cb = [sum(1 for a in cube.AXES if co[a][i]) for i in range(8)]
    for k in range(4):
        D[f'eb{k}'] = sum(1 for x in eb if x == k); D[f'cb{k}'] = sum(1 for x in cb if x == k)
    ar_c = 0
    for i in range(8):
        if all(cube.faxis(fl[k]) == cube.faxis(cube.FACES[k // 9]) for k in cube.CF[i]): ar_c += 1
    ar_e = 0
    for i in range(12):
        if all(cube.faxis(fl[k]) == cube.faxis(cube.FACES[k // 9]) for k in cube.EF[i]): ar_e += 1
    D['ar_c'] = ar_c; D['ar_e'] = ar_e
    # the same on the inverse
    sti = cube.inv(st); fli = cube.facelets(sti)
    D['ar_c_I'] = sum(1 for i in range(8) if all(cube.faxis(fli[k]) == cube.faxis(cube.FACES[k // 9]) for k in cube.CF[i]))
    D['ar_e_I'] = sum(1 for i in range(12) if all(cube.faxis(fli[k]) == cube.faxis(cube.FACES[k // 9]) for k in cube.EF[i]))
    return D

if __name__ == '__main__':
    with open(sys.argv[2], 'w') as f:
        keys = None
        for l in open(sys.argv[1]):
            if not l.strip(): continue
            k, s = l.rstrip('\n').split('\t')[:2]
            D = f2(s)
            if keys is None: keys = list(D); f.write('id\t' + '\t'.join(keys) + '\n')
            f.write(k + '\t' + '\t'.join(str(D[x]) for x in keys) + '\n')

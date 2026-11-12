#!/usr/bin/env python3
"""Getting to a DR-2s 8fe against getting to a DR.

1. Over every position with a full EO on F/B (1,082,565 of them), the number of moves to the real DR and to the
   DR-2s 8fe on one axis, with moves that keep the EO (tables out/bfs/eo-fb_dr.u8 and eo-fb_2s8fe.u8).
2. The renaming behind it, tested on random positions: move every piece a quarter turn around an axis (centres stay)
   and flip every edge; the distance to the 8fe equals the distance of the renamed position to the DR.
   With a full EO the axis is F/B; with any moves the 8fe distance is the smaller of the two renamings (around F/B and
   around R/L), one for each of the colour's two 8fe targets.

Writes out/eo8_hist.json.  Needs the search tables of run_bfs.sh."""
import json, random, numpy as np
import cube, coords
from coords import EF
O = '/data/fmc/is-dr-xs-worth-it/research/out/'
def idx(c): return (c[0] * 2048 + c[1]) * 495 + c[2]
CENTRES = [i for i in range(54) if sum(1 for v in cube.ST[i][0] if v != 0) == 1]
def rename(s, rot):
    t = list(cube.do(s, cube.parse(rot)))
    for i in CENTRES: t[i] = i
    for a, b in EF: t[a], t[b] = t[b], t[a]
    return tuple(t)
def rand_state(rng, full_eo):
    cp = list(range(8)); rng.shuffle(cp)
    ct = [rng.randrange(3) for _ in range(7)]; ct.append((-sum(ct)) % 3)
    ep = list(range(12)); rng.shuffle(ep)
    ef = [0] * 12
    if not full_eo:
        ef = [rng.randrange(2) for _ in range(11)]; ef.append(sum(ef) % 2)
    return coords.make(cp, ct, ep, ef)

def main():
    dr = np.memmap(O + 'bfs/eo-fb_dr.u8', dtype=np.uint8, mode='r'); e8 = np.memmap(O + 'bfs/eo-fb_2s8fe.u8', dtype=np.uint8, mode='r')
    co = np.arange(2187, dtype=np.int64)[:, None]; sl = np.arange(495, dtype=np.int64)[None, :]
    at = ((co * 2048) * 495 + sl).ravel()                                   # every coset with eo = 0
    a = np.asarray(dr[at]); b = np.asarray(e8[at])
    assert (a < 255).all() and (b < 255).all()
    out = {'positions': int(len(at)), 'dr': np.bincount(a, minlength=11).tolist(), '8fe': np.bincount(b, minlength=11).tolist(),
           'same_in_place': float((a == b).mean())}
    assert out['dr'] == out['8fe']
    rng = random.Random(20261112); n = 2000; ok = 0
    for _ in range(n):
        s = rand_state(rng, True); c = coords.coords(s); c2 = coords.coords(rename(s, 'z'))
        ok += c[1] == 0 and c2[1] == 0 and int(e8[idx(c)]) == int(dr[idx(c2)])
    out['renaming_full_eo'] = [ok, n]
    alld = np.memmap(O + 'bfs/all_dr.u8', dtype=np.uint8, mode='r'); all8 = np.memmap(O + 'bfs/all_2s8fe.u8', dtype=np.uint8, mode='r')
    ok = 0
    for _ in range(n):
        s = rand_state(rng, False)
        ok += int(all8[idx(coords.coords(s))]) == min(int(alld[idx(coords.coords(rename(s, r)))]) for r in ('z', 'x'))
    out['renaming_any_moves'] = [ok, n]
    assert out['renaming_full_eo'][0] == n and out['renaming_any_moves'][0] == n
    json.dump(out, open(O + 'eo8_hist.json', 'w'), indent=1)
    print(out)
if __name__ == '__main__': main()

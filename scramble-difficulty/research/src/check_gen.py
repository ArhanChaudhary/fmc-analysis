"""Check generated TNoodle scrambles: middle reproduces min2phase's state; text split gives a DR of the middle;
the text split matches min2phase's own phase-1 / phase-2 / premove lengths.  usage: check_gen.py gen.tsv"""
import sys, collections, cube, textfeat as tf
rows = [x for x in (l.rstrip("\n").split("\t") for l in open(sys.argv[1])) if len(x) == 12][1:]
c = collections.Counter(); n = 0
for r in rows:
    k, scr, mid, fl, urf, d1, pre, sol = r[:8]
    m, padded = tf.strip(scr); assert padded and m == cube.parse(mid)
    assert cube.facelets(cube.seq(m)) == fl, k
    ax, x, h, y, drl = tf.text_dr(m)
    ok = tf.check_dr(m, ax, x, h)
    c['dr_ok'] += ok
    d1, pre, sol = int(d1), int(pre), int(sol)
    assert sol == len(m)
    # min2phase's own split: urfIdx<3 -> M = q^-1 p2^-1 p1^-1 (phase 1 at the end); else M = p1 p2 q (phase 1 first)
    p1end = int(urf) < 3
    tx, ty = (pre, d1) if p1end else (d1, pre)
    c['split_match'] += (x + y == d1 + pre)
    c['side_match'] += ((y >= x) == p1end) if x != y else 0
    c['ties'] += (x == y)
    n += 1
print(n, dict(c))

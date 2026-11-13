"""Scramble text facts on every padded official 333fm scramble of the WCA export, and on the generated ones.
  1. middle M = X h Y with h the longest run of one axis' DR moves: X^-1 . M . Y^-1 is a DR state (cube model)
  2. on the full scramble P M P: inverse (P X)^-1 = X^-1 F' U R, normal (Y P)^-1 = F' U R Y^-1 gives a DR (cube model)
  3. structure tables by era
out: out/tnoodle_tables.txt, out/tnoodle_examples.txt"""
import collections, cube, textfeat as tf

real = [l.rstrip('\n').split('\t') for l in open('../big/real_unique.tsv')][1:]
gen = [l.rstrip('\n').split('\t') for l in open('../big/gen.tsv')]
O = open('../out/tnoodle_tables.txt', 'w')
def P(*a):
    s = ' '.join(map(str, a)); print(s); O.write(s + '\n')

def analyse(scr):
    m, padded = tf.strip(scr); assert padded
    ax, x, h, y, d = tf.text_dr(m)
    X, H, Y = m[:x], m[x:x + h], m[x + h:]
    ok_mid = tf.check_dr(m, ax, x, h)
    full = cube.parse(scr)
    inv_side = cube.inv_moves(tf.PAD + X)          # premoves
    nor_side = cube.inv_moves(Y + tf.PAD)
    ok_full = cube.is_dr(cube.seq(inv_side + full + nor_side), ax)
    # all axes: is there a second axis with a run giving a DR too?  (report the per-axis run lengths)
    return dict(m=m, ax=ax, X=X, H=H, Y=Y, ok_mid=ok_mid, ok_full=ok_full, inv_side=inv_side, nor_side=nor_side,
                p1_end=len(Y) > len(X))

def table(rows, label):
    n = len(rows)
    A = [analyse(r) for r in rows]
    P(f'\n== {label}: {n} scrambles; the split gives a DR state on the cube model for {sum(a["ok_mid"] for a in A)} (middle) and {sum(a["ok_full"] for a in A)} (full scramble): an identity, a test of the code, not a finding')
    def hist(f):
        c = collections.Counter(f(a) for a in A); return ', '.join(f'{k}: {v} ({100 * v / n:.1f}%)' for k, v in sorted(c.items()))
    P(' middle length (moves):', hist(lambda a: len(a['m'])))
    P(' DR-move run h (moves):', hist(lambda a: len(a['H'])))
    P(' text DR of the middle |X|+|Y| (moves):', hist(lambda a: len(a['X']) + len(a['Y'])))
    P(' shorter outer block (moves):', hist(lambda a: min(len(a['X']), len(a['Y']))))
    P(' longer outer block (moves):', hist(lambda a: max(len(a['X']), len(a['Y']))))
    P(' axis:', hist(lambda a: a['ax']))
    P(' the longer block is at the end of the middle:', hist(lambda a: a['p1_end']))
    P(' text DR of the full scramble |X|+|Y|+6 (moves):', hist(lambda a: len(a['X']) + len(a['Y']) + 6))
    mean = sum(len(a['X']) + len(a['Y']) for a in A) / n
    P(f' mean text DR of the middle {mean:.3f}; mean middle length {sum(len(a["m"]) for a in A) / n:.3f}')
    return A

old = [r[0] for r in real if r[2] < '2020-08']
new = [r[0] for r in real if r[2] >= '2020-08']
table(old, 'official, 2016-04 to 2020-07')
An = table(new, 'official, 2020-08 to 2026-10')
table([r[1] for r in gen], 'generated (tnoodle-lib min2phase, this study)')

# worked examples: the most recent official scramble, and one from the older era
E = open('../out/tnoodle_examples.txt', 'w')
for lab, pick in (('recent', max((r for r in real), key=lambda r: r[2])), ('old', min((r for r in real if r[2] < '2020-08'), key=lambda r: r[2]))):
    a = analyse(pick[0])
    E.write(f'{lab}: {pick[1]} ({pick[2]})\n scramble: {pick[0]}\n middle: {" ".join(a["m"])}\n X: {" ".join(a["X"])}\n h ({a["ax"]}): {" ".join(a["H"])}\n Y: {" ".join(a["Y"])}\n'
            f' NISS DR of the full scramble: normal {" ".join(a["nor_side"])} , inverse ({" ".join(a["inv_side"])}) ; checked {a["ok_full"]}\n\n')
print(open('../out/tnoodle_examples.txt').read())

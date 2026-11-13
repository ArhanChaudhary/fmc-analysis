"""Corner cases of each scramble's DRs (<= 10 moves): histogram of the corner QT (last digit of the corner case, e.g.
4b2 -> 2) and the number in each corner case.   usage: drqt.py raw.tsv label.tsv prefix out.tsv"""
import sys
from collections import defaultdict
raw, lab, prefix, out = sys.argv[1:5]
H = defaultdict(lambda: [0] * 6)
fl = open(lab); next(fl)
for line in open(raw):
    if line.startswith('#') or line.startswith('scr\t'): continue
    r = line.split('\t', 4); l = next(fl)
    if int(r[3]) > 10: continue
    cc = l.split('\t', 1)[0].split()[0]
    H[prefix + r[0]][int(cc[-1])] += 1
with open(out, 'w') as f:
    f.write('id\t' + '\t'.join(f'h{k}' for k in range(6)) + '\n')
    for k, h in H.items(): f.write(k + '\t' + '\t'.join(map(str, h)) + '\n')

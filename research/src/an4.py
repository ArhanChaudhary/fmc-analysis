#!/usr/bin/env python3
import csv, collections, sys
rows=[(r['subset'],r['ab'],int(r['hN']),int(r['hI']),int(r['L']),int(r['Epar']),int(r['depth']),int(r['count'])) for r in csv.DictReader(open('/data/fmc/research/out/census.csv'))]
ORDER=['0c0','4a1','4a2','4b2','0c3','2c3','4c3','0c4','2c4','4c4','2c5','4b5']
def key(n):
    c,e=n.split(); return (ORDER.index(c), int(e[0]))
subs=sorted({r[0] for r in rows}, key=key)
want=sys.argv[1:] or subs
print("For each subset: by corner length L and E-slice parity (0 even, 1 odd):  share% | min finish | mean finish | P(finish<=12)% | P(finish<=13)%")
for s in want:
    R=[r for r in rows if r[0]==s]; tot=sum(r[7] for r in R)
    cell=collections.defaultdict(collections.Counter)
    for r in R: cell[(r[4],r[5])][r[6]]+=r[7]
    print(f"== {s}")
    for (L,par) in sorted(cell):
        c=cell[(L,par)]; n=sum(c.values())
        print(f"   L={L:2d} par={par}: {100*n/tot:6.2f}% | min {min(c):2d} (L+{min(c)-L}) | mean {sum(d*x for d,x in c.items())/n:5.2f} | <=12: {100*sum(x for d,x in c.items() if d<=12)/n:5.2f}% | <=13: {100*sum(x for d,x in c.items() if d<=13)/n:5.2f}%")

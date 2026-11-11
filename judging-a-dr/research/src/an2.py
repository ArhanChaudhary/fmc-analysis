#!/usr/bin/env python3
import csv, collections, sys
rows=[(r['subset'],r['ab'],int(r['hN']),int(r['hI']),int(r['L']),int(r['Epar']),int(r['depth']),int(r['count'])) for r in csv.DictReader(open('/data/fmc/judging-a-dr/research/out/census.csv'))]
def table(sub):
    R=[r for r in rows if r[0]==sub]
    cell=collections.defaultdict(collections.Counter)
    for r in R: cell[(r[2],r[3])][r[6]]+=r[7]
    hs=sorted({k[0] for k in cell}|{k[1] for k in cell})
    tot=sum(sum(c.values()) for c in cell.values())
    print(f"\n=== {sub}: rows hN (shortest HTR on normal), cols hI (shortest HTR on inverse). cell = min finish / mean finish / share of subset %")
    print('hN\\hI '+' '.join(f'{h:>15d}' for h in hs))
    for a in hs:
        line=f'{a:>5d} '
        for b in hs:
            c=cell.get((a,b))
            if not c: line+=' '*16; continue
            n=sum(c.values()); mn=min(c); mean=sum(d*x for d,x in c.items())/n
            line+=f' {mn:>2d}/{mean:5.2f}/{100*n/tot:5.2f}'
        print(line)
for s in sys.argv[1:]: table(s)

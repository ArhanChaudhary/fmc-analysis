#!/usr/bin/env python3
import csv, collections, sys
rows=[(r['subset'],r['ab'],int(r['hN']),int(r['hI']),int(r['L']),int(r['Epar']),int(r['depth']),int(r['count'])) for r in csv.DictReader(open('/data/fmc/research/out/census.csv'))]
ORDER=['0c0','4a1','4a2','4b2','0c3','2c3','4c3','0c4','2c4','4c4','2c5','4b5']
def key(n):
    c,e=n.split(); return (ORDER.index(c), int(e[0]))
subs=sorted({r[0] for r in rows}, key=key)
print("per subset: states, mean finish, min finish, min HTR len, P(finish<=10..13), and  min over states of [finish - max(hN,hI)], max of [hN+hI-finish]")
for s in subs:
    R=[r for r in rows if r[0]==s]
    tot=sum(r[7] for r in R); mean=sum(r[6]*r[7] for r in R)/tot
    mn=min(r[6] for r in R); mh=min(r[2] for r in R)
    p=[sum(r[7] for r in R if r[6]<=k)/tot*100 for k in (10,11,12,13)]
    gap=min(r[6]-max(r[2],r[3]) for r in R); over=max(r[2]+r[3]-r[6] for r in R)
    lpen=min(r[6]-r[4] for r in R)
    print(f"{s:7s} {tot:>12d} mean {mean:5.2f} min {mn:2d} minHTR {mh:2d}  P<=10:{p[0]:6.2f}% <=11:{p[1]:6.2f}% <=12:{p[2]:6.2f}% <=13:{p[3]:6.2f}%  min(d-maxh) {gap}  max(hN+hI-d) {over}  min(d-L) {lpen}")

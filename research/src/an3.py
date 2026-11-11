#!/usr/bin/env python3
import csv, collections, sys
rows=[(r['subset'],int(r['hmax']),int(r['bFn']),int(r['bFi']),int(r['b0']),int(r['depth']),int(r['count'])) for r in csv.DictReader(open('/data/fmc/research/out/census_bounds.csv'))]
ORDER=['0c0','4a1','4a2','4b2','0c3','2c3','4c3','0c4','2c4','4c4','2c5','4b5']
def key(n):
    c,e=n.split(); return (ORDER.index(c), int(e[0]))
subs=sorted({r[0] for r in rows}, key=key)
def stats(R):
    tot=sum(r[6] for r in R)
    m=lambda f: sum(f(r)*r[6] for r in R)/tot
    p=lambda f: 100*sum(r[6] for r in R if f(r))/tot
    return tot,m,p
print("subset   mean: finish | HTR bound max(hN,hI) | KF one side (normal) | KF both sides | K0 both sides ||  exact-hit% : HTR  KF2  K02 || gap<=1 % K02 || P(finish>=14)  P(bound>=14): HTR KF2 K02 || P(finish>=13) P(bound>=13): HTR KF2 K02")
allR=rows
for s in subs+['ALL']:
    R=[r for r in rows if r[0]==s] if s!='ALL' else rows
    tot,m,p=stats(R)
    print(f"{s:7s} {m(lambda r:r[5]):6.2f} | {m(lambda r:r[1]):5.2f} | {m(lambda r:r[2]):5.2f} | {m(lambda r:max(r[2],r[3])):5.2f} | {m(lambda r:r[4]):5.2f} || "
          f"{p(lambda r:r[1]==r[5]):5.1f} {p(lambda r:max(r[2],r[3])==r[5]):5.1f} {p(lambda r:r[4]==r[5]):5.1f} || {p(lambda r:r[5]-r[4]<=1):5.1f} || "
          f"{p(lambda r:r[5]>=14):5.1f}  {p(lambda r:r[1]>=14):5.1f} {p(lambda r:max(r[2],r[3])>=14):5.1f} {p(lambda r:r[4]>=14):5.1f} || {p(lambda r:r[5]>=13):5.1f}  {p(lambda r:r[1]>=13):5.1f} {p(lambda r:max(r[2],r[3])>=13):5.1f} {p(lambda r:r[4]>=13):5.1f}")

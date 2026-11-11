#!/usr/bin/env python3
import csv, collections, sys
H=collections.defaultdict(lambda: collections.Counter())   # (spec,sides,subset) -> {(bound,depth):count}
order=[]
for r in csv.DictReader(open('/data/fmc/judging-a-dr/research/out/lattice.csv')):
    if r['spec'] not in order: order.append(r['spec'])
    H[(r['spec'],int(r['sides']),r['subset'])][(int(r['bound']),int(r['depth']))]+=int(r['count'])
subsets=sorted({k[2] for k in H})
def agg(spec,sides,subs):
    c=collections.Counter()
    for s in subs: c.update(H[(spec,sides,s)])
    return c
def line(c):
    tot=sum(c.values()); mb=sum(b*n for (b,d),n in c.items())/tot; md=sum(d*n for (b,d),n in c.items())/tot
    ex=100*sum(n for (b,d),n in c.items() if b==d)/tot; w1=100*sum(n for (b,d),n in c.items() if d-b<=1)/tot
    p=lambda t:100*sum(n for (b,d),n in c.items() if b>=t)/tot
    q=lambda t:100*sum(n for (b,d),n in c.items() if d>=t)/tot
    return mb,md,ex,w1,p,q
groups={'ALL':subsets,'1-2qt (4a1,4a2,4b2)':[s for s in subsets if s[:3] in('4a1','4a2','4b2')],'3qt (0c3,2c3,4c3)':[s for s in subsets if s[:3] in('0c3','2c3','4c3')],
        '4qt (0c4,2c4,4c4)':[s for s in subsets if s[:3] in('0c4','2c4','4c4')],'5qt (2c5,4b5)':[s for s in subsets if s[:3] in('2c5','4b5')]}
for g,subs in groups.items():
    c0=agg(order[0],2,subs); _,md,_,_,_,q=line(c0)
    print(f"\n### {g}: mean exact finish {md:.2f}; P(finish>=12) {q(12):.1f}%  >=13 {q(13):.1f}%  >=14 {q(14):.1f}%")
    print(f"{'rung':10s} | one side: mean  exact%  within1% | both sides: mean  exact%  within1% | certified >=12   >=13   >=14  (both sides)")
    for sp in order:
        a=line(agg(sp,1,subs)); b=line(agg(sp,2,subs))
        print(f"{sp:10s} |          {a[0]:5.2f}  {a[2]:5.1f}  {a[3]:5.1f}    |            {b[0]:5.2f}  {b[2]:5.1f}  {b[3]:5.1f}    |          {b[4](12):5.1f}  {b[4](13):5.1f}  {b[4](14):5.1f}")

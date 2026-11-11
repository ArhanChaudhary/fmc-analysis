#!/usr/bin/env python3
"""(1) How often is Levi's 1qt formula  (HTR normal) + (HTR inverse) - 1  NOT a lower bound for the optimal DR finish?"""
import csv, collections
rows=[(r['subset'],int(r['hN']),int(r['hI']),int(r['depth']),int(r['count'])) for r in csv.DictReader(open('/data/fmc/judging-a-dr/research/out/census.csv'))]
for sub in ('4a1 4e','4a1 2e','4a1 0e'):
    R=[r for r in rows if r[0]==sub]; tot=sum(r[4] for r in R)
    diff=collections.Counter()
    for _,hn,hi,d,c in R: diff[d-(hn+hi-1)]+=c
    below=sum(c for k,c in diff.items() if k<0)
    print(f"{sub}: states {tot}; optimal finish < hN+hI-1 for {100*below/tot:.2f}% ; equal {100*diff[0]/tot:.2f}% ; above {100*sum(c for k,c in diff.items() if k>0)/tot:.2f}%")
    print("   optimum minus formula:", {k:f"{100*c/tot:.2f}%" for k,c in sorted(diff.items())})
    # restricted to short cases (formula value <= 13), the ones a solver would act on
    for cap in (11,12,13):
        S=[r for r in R if r[1]+r[2]-1<=cap]; t=sum(r[4] for r in S)
        b=sum(r[4] for r in S if r[3]<r[1]+r[2]-1)
        print(f"   formula value <= {cap}: {100*t/tot:.2f}% of the subset; of those, optimum is below the formula in {100*b/max(t,1):.2f}%")

#!/usr/bin/env python3
"""Every computed number of the write-up and the corrections page ({= ... =} in report_build/*.md), evaluated twice:
as the pages print it, and with every formatter left at six decimals all the way down (the generated tables included,
rebuilt into a scratch folder).  A printed number that is not the six-decimal value rounded once is a double rounding
(a difference of two rounded cells, a ratio of a rounded share) or a typed value.

  double_rounding.py --hires DIR   rebuild the tables into DIR at six decimals (tables6.py; the real_* tables are
                                   copied as they are), then print the expressions as JSON
  double_rounding.py --plain       print the expressions as the pages have them, as JSON
  double_rounding.py --compare A.json B.json   the report
Nothing in report/ or research/out/ is changed."""
import sys, os, re, json, shutil, decimal
R = '/data/fmc/insertion-cost/research/src/'; B = R + 'report_build/'
sys.path.insert(0, B); sys.path.insert(0, R)
def expressions():
    out = []
    for src in ('writeup.md', 'bugs.md'):
        doc = open(B + src).read()
        for _ in range(4):
            doc = re.sub(r'\{\{([A-Z][A-Z0-9_]*)\}\}', lambda m: m.group(0) if m.group(1) == 'CONTENTS' else open(f'{B}{m.group(1).lower()}.md').read(), doc)
        for e in re.findall(r'\{=\s*(.+?)\s*=\}', doc):
            if e not in out: out.append(e)
    return out
def evaluate():
    import xenv
    res = {}
    for e in expressions():
        try: v = eval(e, xenv.ENV)
        except Exception as ex: v = 'ERROR ' + repr(ex)[:80]
        res[e] = v if isinstance(v, str) else str(v)
    return res
if '--plain' in sys.argv:
    json.dump(evaluate(), sys.stdout, indent=0)
elif '--hires' in sys.argv:
    D2 = sys.argv[sys.argv.index('--hires') + 1].rstrip('/') + '/'
    shutil.rmtree(D2, ignore_errors=True); shutil.copytree('/data/fmc/insertion-cost/report/data', D2)
    import tables6; tables6.build(D2)                    # also leaves the formatters at six decimals for xenv
    import xenv; xenv.D = D2; xenv.D6 = D2; xenv._table.cache_clear(); xenv._table6.cache_clear()
    json.dump(evaluate(), sys.stdout, indent=0)
elif '--compare' in sys.argv:
    a = json.load(open(sys.argv[-2])); b = json.load(open(sys.argv[-1]))
    sys.path.insert(0, '/data/fmc/judging-a-dr/research/src'); import pv
    NUM = r'[-+]?\d[\d,]*\.?\d*%?'
    def half_up(x, d): return str(decimal.Decimal(repr(round(x, 9))).quantize(decimal.Decimal(1).scaleb(-d), rounding=decimal.ROUND_HALF_UP))
    bad = same = skipped = 0
    for e in a:
        p, h = a[e], b.get(e, '')
        tp = re.findall(NUM, p); th = re.findall(NUM, h)
        if len(tp) != len(th) or 'ERROR' in h or 'ERROR' in p:
            if p != h: skipped += 1; print(f'CANNOT ALIGN  {e[:110]}\n     printed {p[:120]!r}\n     six     {h[:120]!r}')
            continue
        for x, y in zip(tp, th):
            if x == y: same += 1; continue
            if x.endswith('%'):
                want = pv.num(float(y.rstrip('%').replace(',', '')))
                ok = want == x or (x == '99.9%' and want in ('100%', '99.9%'))
            else:
                d = len(x.split('.')[1]) if '.' in x else 0
                want = half_up(float(y.replace(',', '')), d); ok = float(want) == float(x.replace(',', ''))
            if ok: same += 1
            else: bad += 1; print(f'MISMATCH  printed {x}  six decimals {y}  rounds to {want}\n     {e[:150]}')
    print(f'{len(a)} expressions; numbers that agree: {same}; mismatches: {bad}; not aligned: {skipped}')

"""Add scrambles generated on JTuu's subset generator page (https://jtuu.be/subsets.html) to data/generated.jsonl,
for one corner case, until the examples document has TARGET examples of it.

usage: add_generated.py SECTION TARGET BATCH.jsonl [OUTDIR]

BATCH.jsonl: the lines of `node subsets_page.mjs gen SUBSET N` (SUBSET is the page's name for the section; the
doc's 4b3 section is the page's 4c3).  The scrambles are taken in the order the page gave them.  Each one gets its id
(the section's next number) and a DR-move scramble (nissy, as scrambles.py does), is written to data/generated.jsonl
and solved (annotate.py).  It stops as soon as the document, by its own rule (every scramble whose DR has a
within-goal solution, at most annotate.UNSOLVED without), has TARGET examples of the section; the scrambles of the batch after
that are not looked at."""
import sys, os, io, json, subprocess, datetime
import annotate as A

NISSY = '/data/fmc/tools/nissy-2.0.8/nissy'
ENV = dict(os.environ, NISSYDATA='/data/fmc/tools/nissy-data')
PAGE = {'4b3': '4c3'}          # the page's checkbox for a section of the doc


def inv(seq):
    return ' '.join(t[0] + {'': "'", '2': '2', "'": ''}[t[1:]] for t in reversed(seq.split()))


def dr_scramble(scramble):
    out = subprocess.run([NISSY, 'solve', 'drudfin', scramble], capture_output=True, text=True, env=ENV, timeout=600).stdout
    sols = [l.rsplit(' (', 1)[0] for l in out.splitlines() if l.strip().endswith(')') and '(' in l]
    assert sols, ('not DR on U/D', scramble, out[-200:])
    return inv(sols[0])


def solved(x, outdir):
    rows = A.dump(x, outdir)
    text, info, _ = A.render(x, rows, log=io.StringIO())
    open(f'{outdir}/{x["id"]}.md', 'w').write(text)
    return info


def main():
    section, target, batch = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    outdir = sys.argv[4] if len(sys.argv) > 4 else f'{A.HERE}/out'
    have = [x for x in A.scrambles().values() if x['section'] == section]
    infos = [solved(x, outdir) for x in have]
    count = lambda: (n := sum(i['optimal'] <= i['goal'] for i in infos)) + min(len(infos) - n, A.UNSOLVED)
    print(f'{section}: {len(have)} scrambles, {count()} examples in the document, target {target}')
    items = [json.loads(l) for l in open(batch)]
    used = 0
    for t in items:
        if count() >= target:
            break
        used += 1
        if any(x['scramble'] == t['scramble'] for x in have):
            continue
        assert t['subset'] == PAGE.get(section, section) and t['dr_ud'], t
        x = dict(id=f'{section}-{len(have) + 1:02d}', section=section, scramble=t['scramble'], note=None,
                 dr_scramble=dr_scramble(t['scramble']), source='https://jtuu.be/subsets.html',
                 generated=datetime.date.today().isoformat(), page_subset=t['subset'], lib_subset=t['lib_subset'])
        if 'edges' in t:
            x['page_edges'] = t['edges']          # the edge subsets checked on the page
        with open(f'{A.HERE}/data/generated.jsonl', 'a') as f:
            f.write(json.dumps(x) + '\n')
        have.append(x)
        info = solved(x, outdir)
        infos.append(info)
        print(x['id'], x['lib_subset'], info['subset'], 'goal', info['goal'], 'optimal', info['optimal'], 'found', info['lens'], 'hard to find', info['hard'],
              '-> in the document' if info['optimal'] <= info['goal'] else '-> no within-goal solution', flush=True)
    print(f'{section}: {count()} examples in the document; {used} of the {len(items)} scrambles of the batch used')
    sys.exit(0 if count() >= target else 3)


main()

#!/usr/bin/env python3
"""Generator for the Lean project: copies the simulator's exports into data/ (the files the theorems are about, embedded
with `include_str`) and writes two manifests:

    AttemptSim/Manifest.lean        tables and candidate lists: sizes, sha256, the counts the theorems recount, the
                                    exact table's sha256 and the sha256 of the vendored DRBound files
    AttemptSim/SampleManifest.lean  the sampled attempts and the page solutions: the per-policy counts Python reads off
                                    the log, which SampleThm recounts in Lean
    data/MANIFEST.txt               all of it as a table, for the README

The split keeps a new sample from rebuilding the table proofs: a module is rebuilt when a file it imports changes, and
only Sample/SampleThm import SampleManifest.

Sources (all written by the simulator, nothing typed by hand):
    research/out/lean_export/   attemptsim export --out DIR --scrambles ../data/scrambles_uniform.txt --count 12 --eo 4 --cap 9
        model.txt eodist.txt eo_mv.txt co_mv.txt sl_mv.txt htrdist.txt cosets.txt     copied byte for byte
        drdist.u8            1,082,565 bytes -> data/drdist.txt, one letter per entry ('a' + value)
        cands_scrambles.tsv cands_eo.tsv cands_dr.tsv                                  copied byte for byte
        exact_table.sha256   sha256 of the exact table the sample run read (refresh.sh writes it)
    research/out/lean_sample.jsonl          attemptsim run ... --log FILE --logn K     copied byte for byte
    research/out/lean_page_solutions.tsv    scramble TAB solution TAB length           copied byte for byte (empty if absent)

Checks made here (the run stops if one fails):
    DRBound/Cube.lean, DRBound/Certificate.lean    byte-identical to judging-a-dr/lean/DRBound/DRBound/ (sha256)
    AttemptSim/Cube.lean, Pieces.lean, Search.lean identical to eo-switch/lean/EOSwitch/EOSwitch/ once the first comment
                                                   block is dropped and the namespace EOSwitch is renamed AttemptSim

usage: python3 gen.py [--export DIR] [--sample FILE] [--page FILE]
Then build (see README.md).  Python 3, standard library only."""
import sys, os, hashlib, json, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
R = os.path.normpath(os.path.join(HERE, '..', '..', 'research', 'out'))

def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default

def sha(b): return hashlib.sha256(b).hexdigest()

def body(path, ns_from=None, ns_to=None):
    """A Lean file without its first /- ... -/ block, the namespace renamed."""
    t = open(path).read()
    t = re.sub(r'\A/-.*?-/\n', '', t, count=1, flags=re.S)
    if ns_from: t = t.replace(ns_from, ns_to)
    return t

def main():
    exp = arg('--export', os.path.join(R, 'lean_export'))
    sample = arg('--sample', os.path.join(R, 'lean_sample.jsonl'))
    page = arg('--page', os.path.join(R, 'lean_page_solutions.tsv'))
    out = os.path.join(HERE, 'data')
    os.makedirs(out, exist_ok=True)
    man = []          # (data file, source, bytes, sha256 of the data file, sha256 of the source)

    def put(name, data, src, srcdata=None):
        assert all(c < 128 for c in data), f'{name}: not ASCII'
        with open(os.path.join(out, name), 'wb') as f: f.write(data)
        man.append((name, src, len(data), sha(data), sha(srcdata if srcdata is not None else data)))

    for n in ('model.txt', 'eodist.txt', 'eo_mv.txt', 'co_mv.txt', 'sl_mv.txt', 'htrdist.txt', 'cosets.txt',
              'cands_scrambles.tsv', 'cands_eo.tsv', 'cands_dr.tsv'):
        b = open(os.path.join(exp, n), 'rb').read()
        put(n, b, f'lean_export/{n}')
    d = open(os.path.join(exp, 'drdist.u8'), 'rb').read()
    assert len(d) == 2187 * 495 and max(d) < 26
    put('drdist.txt', bytes(97 + v for v in d), 'lean_export/drdist.u8', d)
    ntab = len(man)
    b = open(sample, 'rb').read()
    put('lean_sample.jsonl', b, 'lean_sample.jsonl')
    pb = open(page, 'rb').read() if os.path.exists(page) else b''
    put('lean_page_solutions.tsv', pb, 'lean_page_solutions.tsv' + ('' if os.path.exists(page) else ' (absent: empty)'))
    exact = open(os.path.join(exp, 'exact_table.sha256')).read().split()[0]

    # ---- provenance of the copied Lean files
    vend = []
    for n in ('Certificate.lean', 'Cube.lean'):
        mine = open(os.path.join(HERE, 'DRBound', n), 'rb').read()
        theirs = open(os.path.join(REPO, 'judging-a-dr', 'lean', 'DRBound', 'DRBound', n), 'rb').read()
        assert mine == theirs, f'DRBound/{n} differs from judging-a-dr/lean/DRBound/DRBound/{n}'
        vend.append((f'DRBound/{n}', f'judging-a-dr/lean/DRBound/DRBound/{n}', sha(mine)))
    for n in ('Cube.lean', 'Pieces.lean', 'Search.lean'):
        mine = body(os.path.join(HERE, 'AttemptSim', n))
        theirs = body(os.path.join(REPO, 'eo-switch', 'lean', 'EOSwitch', 'EOSwitch', n), 'EOSwitch', 'AttemptSim')
        assert mine == theirs, f'AttemptSim/{n} differs from eo-switch/lean/EOSwitch/EOSwitch/{n} beyond header and namespace'
        vend.append((f'AttemptSim/{n} (code below the header)', f'eo-switch/lean/EOSwitch/EOSwitch/{n} (namespace renamed)', sha(mine.encode())))

    # ---- the counts Python reads off the files (Lean recounts them)
    rows = [json.loads(l) for l in b.decode().split('\n') if l.strip()]
    pol = {}
    late = 0
    for r in rows:
        p = pol.setdefault(r['policy'], [0, 0, 0, 0])
        p[0] += 1; p[1] += r['len'] == 0; p[2] += r['len']; p[3] += len(r['sols'])
        # attempts in which a solution shorter than the result was found after the last in-time writing began
        ck, t = [], 0
        for _, ms in r['steps']:
            t += ms; ck.append(t)
        wstart = [ck[i - 1] if i else 0 for i, (k, _) in enumerate(r['steps']) if k == 10]
        intime = [j for j, (e, _) in enumerate(r['banks']) if e <= r['budget_ms']]
        start = wstart[intime[-1]] if intime else -1
        res = r['len'] if r['len'] > 0 else 10 ** 6
        if any(c > start and l < res for c, l, _ in r['sols']): late += 1
    pols = sorted(pol.items())
    nsteps = sum(len(r['steps']) for r in rows)
    npage = len([l for l in pb.decode().split('\n') if l.strip()])
    cs = [l for l in open(os.path.join(exp, 'cands_scrambles.tsv')).read().split('\n')[1:] if l.strip()]
    ce = [l.split('\t') for l in open(os.path.join(exp, 'cands_eo.tsv')).read().split('\n')[1:] if l.strip()]
    cd = [l.split('\t') for l in open(os.path.join(exp, 'cands_dr.tsv')).read().split('\n')[1:] if l.strip()]
    eo_max = max(int(r[3]) for r in ce)
    dr_cap = max((int(r[2]) for r in cd), default=0)
    # the caps the export was made with are not in the files: they are passed on the command line and default to
    # what the lists show (longest EO, longest DR)
    eo_k = int(arg('--eo', eo_max)); dr_l = int(arg('--cap', dr_cap))

    def files_def(rows_):
        L = ['def FILES : List (String × Nat × String) := [']
        L += [f'  ("{n}", {size}, "{h}"),' for n, _, size, h, _ in rows_]
        L[-1] = L[-1].rstrip(',')
        return L + [']']

    L = ['/-',
         '  AttemptSim.Manifest — GENERATED by gen.py, do not edit.  What the table and candidate files are, and the counts',
         '  Python reads off them; the theorems recount these in Lean from the embedded files.',
         '-/',
         'namespace AttemptSim', 'namespace manifest', '',
         '/-- (data file, bytes, sha256), for the README; the theorems do not depend on these. -/']
    L += files_def(man[:ntab])
    L += ['',
          '/-- sha256 of judging-a-dr\'s lean_exact_table.u8 (1,339,269,120 bytes) as the simulator read it.  That file was',
          '    written by an `#eval` of `DRBound.Exact.mkTable 18`, the table whose entries DRBound proves are the exact',
          '    optimal DR-move finishes (judging-a-dr/research/src/check_lean_exact.py); the simulator uses it to bound its',
          '    finish search and for the answer key, never to vouch for a solution (every solution is replayed). -/',
          f'def EXACT_SHA256 : String := "{exact}"', '',
          '/-- (copied Lean file, original, sha256 of the copy), checked by gen.py: the DRBound files are byte-identical,',
          '    the two cube files identical to the EO-switch study\'s once header and namespace are set aside. -/',
          'def VENDORED : List (String × String × String) := [' + ', '.join(f'("{a}", "{b_}", "{h}")' for a, b_, h in vend) + ']', '',
          f'/-- scrambles of the completeness check, their EO candidates and DR candidates, and the caps -/',
          f'def CAND_SCRAMBLES : Nat := {len(cs)}', f'def CAND_EOS : Nat := {len(ce)}', f'def CAND_DRS : Nat := {len(cd)}',
          f'def CAND_EO_MAX : Nat := {eo_k}', f'def CAND_DR_CAP : Nat := {dr_l}', '',
          'end manifest', 'end AttemptSim', '']
    open(os.path.join(HERE, 'AttemptSim', 'Manifest.lean'), 'w').write('\n'.join(L))

    S = ['/-',
         '  AttemptSim.SampleManifest — GENERATED by gen.py, do not edit.  The sampled attempts and the page solutions: what',
         '  the files are and the counts Python reads off them; SampleThm recounts these in Lean from the embedded files.',
         '-/',
         'namespace AttemptSim', 'namespace manifest', '',
         '/-- (data file, bytes, sha256) of the sample and the page solutions, for the README. -/']
    S += [l.replace('def FILES', 'def SAMPLE_FILES') for l in files_def(man[ntab:])]
    S += ['',
          f'/-- attempts in the sample file -/', f'def SAMPLE_ATTEMPTS : Nat := {len(rows)}',
          f'/-- per policy, in order of name: (name, attempts, DNFs, sum of the lengths, solutions found) -/',
          'def SAMPLE_POLICIES : List (String × Nat × Nat × Nat × Nat) := [' +
          ', '.join(f'("{k}", {v[0]}, {int(v[1])}, {v[2]}, {v[3]})' for k, v in pols) + ']',
          f'/-- steps in all logs together -/', f'def SAMPLE_STEPS : Nat := {nsteps}',
          f'/-- attempts in which a solution shorter than the result was found after the last in-time writing began -/',
          f'def SAMPLE_LATE_BETTER : Nat := {late}',
          f'/-- solutions printed on the page -/', f'def PAGE_SOLUTIONS : Nat := {npage}', '',
          'end manifest', 'end AttemptSim', '']
    open(os.path.join(HERE, 'AttemptSim', 'SampleManifest.lean'), 'w').write('\n'.join(S))

    with open(os.path.join(out, 'MANIFEST.txt'), 'w') as f:
        f.write('data file\tsource (under research/out)\tbytes\tsha256 of the data file\tsha256 of the source\n')
        for row in man: f.write('\t'.join(map(str, row)) + '\n')
        f.write(f'exact table (not copied)\tjudging-a-dr/research/data/lean_exact_table.u8\t1339269120\t{exact}\t{exact}\n')
        f.write('\ncopied Lean file\toriginal\tsha256\n')
        for row in vend: f.write('\t'.join(row) + '\n')
    print(f'{len(man)} data files; sample: {len(rows)} attempts, {nsteps} steps, policies {[(k, v[0]) for k, v in pols]}, '
          f'late better {late}; page solutions {npage}; candidates: {len(cs)} scrambles, {len(ce)} EOs (<= {eo_k}), '
          f'{len(cd)} DRs (<= {dr_l}); vendored files checked: {len(vend)}')

if __name__ == '__main__':
    main()

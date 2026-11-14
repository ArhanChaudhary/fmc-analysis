#!/usr/bin/env python3
"""Every official FMC attempt from the WCA results export, with its scramble.

Input : the export zip (https://www.worldcubeassociation.org/export/results/v2/tsv), read as a stream.
Output: out/big/wca/fm_attempts.tsv   one row per attempt:
            person_id  competition_id  round_type_id  attempt  value(moves; -1 DNF, -2 DNS)  year month day
        out/big/wca/fm_scrambles.tsv  competition_id round_type_id group_id scramble_num is_extra scramble
        out/big/wca/fm_ranks.tsv      person_id  best_average(x100)  world_rank ; and single ranks
        out/big/wca/fm_persons.tsv    person_id  name
Run with `python3 -I` (the zip is downloaded data)."""
import sys, zipfile, io, csv

def rows(z, name):
    with z.open(name) as f:
        t = io.TextIOWrapper(f, encoding='utf-8', newline='')
        r = csv.reader(t, delimiter='\t', quoting=csv.QUOTE_NONE)
        head = next(r)
        ix = {h: i for i, h in enumerate(head)}
        for row in r:
            yield ix, row

def main():
    zpath, out = sys.argv[1], sys.argv[2]
    z = zipfile.ZipFile(zpath)
    res = {}            # result id -> (person, comp, round)
    for ix, r in rows(z, 'WCA_export_results.tsv'):
        if r[ix['event_id']] == '333fm':
            res[r[ix['id']]] = (r[ix['person_id']], r[ix['competition_id']], r[ix['round_type_id']])
    comp = {}
    for ix, r in rows(z, 'WCA_export_competitions.tsv'):
        comp[r[ix['id']]] = (r[ix['year']], r[ix['month']], r[ix['day']])
    n = 0
    with open(f'{out}/fm_attempts.tsv', 'w') as f:
        f.write('person_id\tcompetition_id\tround_type_id\tattempt\tvalue\tyear\tmonth\tday\n')
        for ix, r in rows(z, 'WCA_export_result_attempts.tsv'):
            k = res.get(r[ix['result_id']])
            if k:
                y, m, d = comp.get(k[1], ('0', '0', '0'))
                f.write(f"{k[0]}\t{k[1]}\t{k[2]}\t{r[ix['attempt_number']]}\t{r[ix['value']]}\t{y}\t{m}\t{d}\n"); n += 1
    print('attempts', n, 'results', len(res))
    n = 0
    with open(f'{out}/fm_scrambles.tsv', 'w') as f:
        f.write('competition_id\tround_type_id\tgroup_id\tscramble_num\tis_extra\tscramble\n')
        for ix, r in rows(z, 'WCA_export_scrambles.tsv'):
            if r[ix['event_id']] == '333fm':
                f.write('\t'.join(r[ix[k]] for k in ('competition_id', 'round_type_id', 'group_id', 'scramble_num', 'is_extra', 'scramble')) + '\n'); n += 1
    print('scrambles', n)
    with open(f'{out}/fm_ranks.tsv', 'w') as f:
        f.write('kind\tperson_id\tbest\tworld_rank\n')
        for kind, name in (('average', 'WCA_export_ranks_average.tsv'), ('single', 'WCA_export_ranks_single.tsv')):
            for ix, r in rows(z, name):
                if r[ix['event_id']] == '333fm':
                    f.write(f"{kind}\t{r[ix['person_id']]}\t{r[ix['best']]}\t{r[ix['world_rank']]}\n")
    ids = {k[0] for k in res.values()}
    with open(f'{out}/fm_persons.tsv', 'w') as f:
        f.write('person_id\tname\n')
        for ix, r in rows(z, 'WCA_export_persons.tsv'):
            if r[ix['wca_id']] in ids and r[ix['sub_id']] == '1':
                f.write(f"{r[ix['wca_id']]}\t{r[ix['name']]}\n")

if __name__ == '__main__':
    main()

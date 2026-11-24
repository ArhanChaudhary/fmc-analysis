//! Section splits of corner skeletons: for each DR of a metarun (both sides), each quarter-turn count q and each
//! HTR corner kind, the moves made by the skeleton up to its states with 1, 2 and 3 quarter turns left, over every
//! shortest corner path (corners only, `rem` tables).  A skeleton read "the solver's way" charges a variant's
//! section with (its length) - (the skeleton's length of the same section); these splits are what it subtracts.
use crate::core::{parse_moves, rank_perm};
use crate::model::*;
use std::collections::{HashMap, HashSet};
use std::io::Write;

/// rem values at the nodes after the current one (r-1 .. 1 quarter turns left), over shortest continuations from
/// corner state c with r quarter turns left, for corner kind k.
fn suffixes(md: &Model, k: usize, c: usize, r: usize, memo: &mut HashMap<(usize, usize), Vec<Vec<u8>>>) -> Vec<Vec<u8>> {
    if r == 0 {
        return vec![vec![]];
    }
    if let Some(v) = memo.get(&(c, r)) {
        return v.clone();
    }
    let rm = &md.rem[k];
    let d0 = rm[r][c];
    assert!(d0 != 255);
    // half-turn run that stays on a shortest path, then a quarter turn
    let mut run = vec![c];
    let mut seen: HashSet<usize> = [c].into_iter().collect();
    let mut i = 0;
    while i < run.len() {
        let z = run[i];
        for &h in &HALF {
            let z2 = md.core.cmove[h][z] as usize;
            if rm[r][z2] != 255 && rm[r][z2] + 1 == rm[r][z] && seen.insert(z2) {
                run.push(z2);
            }
        }
        i += 1;
    }
    let mut out: HashSet<Vec<u8>> = HashSet::new();
    for &z in &run {
        for qt in [0usize, 2, 3, 5] {
            let y = md.core.cmove[qt][z] as usize;
            if rm[r - 1][y] != 255 && rm[r - 1][y] + 1 == rm[r][z] {
                for v in suffixes(md, k, y, r - 1, memo) {
                    let mut w = Vec::with_capacity(v.len() + 1);
                    if r - 1 > 0 {
                        w.push(rm[r - 1][y]);
                    }
                    w.extend(v);
                    out.insert(w);
                }
            }
        }
    }
    let mut res: Vec<Vec<u8>> = out.into_iter().collect();
    res.sort();
    memo.insert((c, r), res.clone());
    res
}

/// drvar metasplit RUN.tsv OUT.tsv : dr side q kind lsk split... where each split is "K1,K2,K3" (moves made by
/// the skeleton up to its states with 1, 2, 3 quarter turns left; 255 = no such state).
pub fn run(md: &Model, tsv: &str, out: &str) {
    let txt = std::fs::read_to_string(tsv).unwrap();
    let mut f = std::io::BufWriter::new(std::fs::File::create(out).unwrap());
    let mut memo: Vec<HashMap<(usize, usize), Vec<Vec<u8>>>> = (0..6).map(|_| HashMap::new()).collect();
    let (mut ngroups, mut nmulti) = (0usize, 0usize);
    for line in txt.lines() {
        let fl: Vec<&str> = line.split('\t').collect();
        if fl[0] != "D" {
            continue;
        }
        let dr: u32 = fl[1].parse().unwrap();
        let m: usize = fl[2].parse().unwrap();
        let x = word(&parse_moves(fl[fl.len() - 1].as_bytes(), 64).unwrap());
        assert_eq!(md.subset(&x), fl[5], "scramble does not give the recorded DR");
        for (side, y) in [(0u8, x), (1u8, x.inv())] {
            let c = rank_perm(&y.c);
            for q in [m, m + 2] {
                if q > 6 {
                    continue;
                }
                for k in 0..6 {
                    let lsk = md.rem[k][q][c];
                    if lsk == 255 {
                        continue;
                    }
                    let sp = suffixes(md, k, c, q, &mut memo[k]);
                    let mut ks: Vec<String> = sp
                        .iter()
                        .map(|v| {
                            // v = rem at nodes with q-1 .. 1 left; K_t = lsk - rem at the node with t left
                            let kt = |t: usize| if t >= 1 && t < q { lsk - v[q - 1 - t] } else { 255 };
                            format!("{},{},{}", kt(1), kt(2), kt(3))
                        })
                        .collect();
                    ks.sort();
                    ks.dedup();
                    ngroups += 1;
                    if ks.len() > 1 {
                        nmulti += 1;
                    }
                    writeln!(f, "{dr}\t{side}\t{q}\t{k}\t{lsk}\t{}", ks.join("\t")).unwrap();
                }
            }
        }
    }
    eprintln!("{ngroups} skeletons, {nmulti} with more than one section split");
}

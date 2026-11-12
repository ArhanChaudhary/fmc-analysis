//! Follow-up passes for questions 8, 9 and the half-turn claims (C11, C13).
//!
//! * `bound2`: per state (same states as `routes`), every finish of length <= max(opt + 1, min(opt + 2, 12)):
//!   its sections s_0..s_N (half turns before the 1st quarter turn, between quarter turns, after the last), its corner
//!   path (corner subset at the start and after each quarter turn, read on normal), and the shortest reduction to 1q
//!   and to 2q that finds it.  Kept per (length - optimum, path): the shortest reductions and the sections of a finish
//!   achieving the 1q one.  Also, over the optimal finishes: whether one ends with the trigger "qt, one half turn,
//!   qt" (C11), and the switch position of the readings that give the shortest HTR (C13).
//! * `alpha`: for corner paths on stdin, the fewest half turns each section must have over all corner permutations
//!   that follow the path (FakeMMAP's alpha_i, T11501).
//! * `redcount2`: the number of reductions a solver writes: pairs (A on normal, B on inverse), each empty or ending
//!   in a quarter turn, |A| + |B| <= R, after which the state is 1q (qt_full = 1) or 2q (qt_full = 2).  B is counted
//!   by a table over HTR cosets (the count only depends on the coset of (X A)^-1), A by enumeration.

use crate::class::{HALF_MOVES, NCCOS, NEPAT};
use crate::core::{MOVE_IS_QT, NC, NMOVES};
use crate::model::{axis_run, canonical_next, is_qt, Model, Rng, Sampler, FACE};
use crate::routes::{finishes, readings};
use rayon::prelude::*;
use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead, BufWriter, Write};
use std::path::Path;
use std::time::Instant;

fn sections(moves: &[u8]) -> Vec<u8> {
    let mut s = vec![0u8];
    for &mv in moves {
        if is_qt(mv) {
            s.push(0);
        } else {
            *s.last_mut().unwrap() += 1;
        }
    }
    s
}
fn win(s: &[u8], len: usize, q: usize) -> u8 {
    let nq = s.len() - 1;
    if nq < q {
        return 99;
    }
    let best = (0..=nq - q).map(|t| s[t..=t + q].iter().map(|&x| x as usize).sum::<usize>()).max().unwrap();
    (len - q - best) as u8
}

pub fn bound2(ex: &str, n: usize, seed: u64, out: &str, subs: Option<&str>) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let sampler = Sampler::new(&m);
    let nsub = m.cls.sub48_name.len();
    let wanted: Vec<usize> = match subs {
        None => (0..nsub).collect(),
        Some(l) => l.split(',').map(|x| m.cls.sub48_name.iter().position(|s| *s == x.replace('_', " ")).unwrap()).collect(),
    };
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "subset\tidx\td\thtrN\thtrI\tniss\tnopt_canon\ttrig_end_normal\ttrig_either_end\ttrig_frac_canon\trur_end_normal\trur_either_end\trur_frac_canon\tbest_any\tlinear_at_best\tminfirst_at_best\tlinear_at_b2\tminfirst_at_b2\tcells")?;
    for sub in wanted {
        let t0 = Instant::now();
        let res: Vec<String> = (0..n)
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0x9E37_79B9_7F4A_7C15));
                let x = sampler.draw(&m, sub, &mut rng);
                let d = m.depth(x.0, x.1, x.2) as usize;
                let budget = (d + 1).max((d + 2).min(12));
                let niss = m.niss_htr(x.0, x.1);
                let mut cell: HashMap<(usize, Vec<u8>), (u8, u8, Vec<u8>)> = HashMap::new();
                let (mut trig_n, mut trig_any) = (false, false);
                let (mut canon, mut canon_trig) = (0u64, 0u64);
                // the R U2 R' shape: last two quarter turns on one face, opposite directions, one half turn between
                let (mut rur_n, mut rur_any, mut canon_rur) = (false, false, 0u64);
                // shortest-HTR readings: (htr, linear exists, min first-part length of a NISS reading)
                let mut best = (99u8, false, 99usize);
                let mut b2 = (false, 99usize);
                let mut rd = Vec::new();
                finishes(&m, x, budget, 2_000_000, &mut |moves, path| {
                    let s = sections(moves);
                    let len = moves.len();
                    let nq = s.len() - 1;
                    let mut cp: Vec<u8> = vec![m.cls.cc_subset[m.cls.ccos[path[0].0] as usize]];
                    for (k, &mv) in moves.iter().enumerate() {
                        if is_qt(mv) {
                            cp.push(m.cls.cc_subset[m.cls.ccos[path[k + 1].0] as usize]);
                        }
                    }
                    let (r1, r2) = (win(&s, len, 1), win(&s, len, 2));
                    let e = cell.entry((len - d, cp)).or_insert((99, 99, vec![]));
                    if r1 < e.0 {
                        e.0 = r1;
                        e.2 = s.clone();
                    }
                    e.1 = e.1.min(r2);
                    if len == d {
                        let tn = nq >= 2 && s[nq - 1] == 1;
                        let t1 = nq >= 2 && s[1] == 1;
                        trig_n |= tn;
                        trig_any |= tn || t1;
                        let qpos: Vec<usize> = (0..len).filter(|&k| is_qt(moves[k])).collect();
                        let opp = |a: usize, b: usize| FACE[moves[a] as usize] == FACE[moves[b] as usize] && moves[a] != moves[b];
                        let rn = tn && opp(qpos[nq - 2], qpos[nq - 1]);
                        let r1_ = t1 && opp(qpos[0], qpos[1]);
                        rur_n |= rn;
                        rur_any |= rn || r1_;
                        let c = moves.windows(2).all(|w| {
                            let (a, b) = (FACE[w[0] as usize], FACE[w[1] as usize]);
                            !(a / 2 == b / 2 && a > b)
                        });
                        if c {
                            canon += 1;
                            canon_trig += tn as u64;
                            canon_rur += rn as u64;
                        }
                        readings(&m, moves, path, &mut rd);
                        for r in &rd {
                            let first = if r.inverse_first { len - r.k } else { r.k };
                            let lin = r.linear;
                            if r.htr_len < best.0 {
                                best = (r.htr_len, false, 99);
                            }
                            if r.htr_len == best.0 {
                                if lin {
                                    best.1 = true;
                                } else {
                                    best.2 = best.2.min(first);
                                }
                            }
                            if r.htr_len <= niss + 2 {
                                if lin {
                                    b2.0 = true;
                                } else {
                                    b2.1 = b2.1.min(first);
                                }
                            }
                        }
                    }
                });
                let mut cells: Vec<String> = cell
                    .iter()
                    .map(|((dl, cp), (r1, r2, s))| {
                        format!(
                            "{}:{}:{}:{}:{}",
                            dl,
                            cp.iter().map(|v| v.to_string()).collect::<Vec<_>>().join("-"),
                            r1,
                            r2,
                            s.iter().map(|v| v.to_string()).collect::<Vec<_>>().join(",")
                        )
                    })
                    .collect();
                cells.sort();
                let (c, e) = (x.0, x.1);
                let (ci, ei) = (m.core.cinv[c] as usize, m.core.einv[e] as usize);
                format!(
                    "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.4}\t{}\t{}\t{:.4}\t{}\t{}\t{}\t{}\t{}\t{}",
                    m.cls.sub48_name[sub], i, d, m.htr(c, e), m.htr(ci, ei), niss, canon, trig_n as u8, trig_any as u8,
                    if canon > 0 { canon_trig as f64 / canon as f64 } else { 0.0 },
                    rur_n as u8, rur_any as u8, if canon > 0 { canon_rur as f64 / canon as f64 } else { 0.0 },
                    best.0, best.1 as u8, best.2, b2.0 as u8, b2.1, cells.join(";")
                )
            })
            .collect();
        for l in res {
            writeln!(f, "{}", l)?;
        }
        f.flush()?;
        eprintln!("bound2 {} {:.1}s", m.cls.sub48_name[sub], t0.elapsed().as_secs_f64());
    }
    Ok(())
}

/// alpha_i of corner paths (one per line on stdin, corner subset indices joined by '-', e.g. "6-3-1-0").
/// Corners only: R_0 = permutations in subset s_0; after each quarter turn the permutations reached by half turns then
/// a quarter turn landing in s_i; alpha_i = fewest half turns, over permutations of R_i, before a quarter turn that
/// lands in s_{i+1}.  alpha_N (after the last quarter turn) = 0.
pub fn alpha(_ex: &str) -> io::Result<()> {
    let m = Model::new(None, None);
    let sub_of = |c: usize| m.cls.cc_subset[m.cls.ccos[c] as usize] as usize;
    let qts: Vec<usize> = (0..NMOVES).filter(|&mv| MOVE_IS_QT[mv]).collect();
    // ht[t][c]: fewest half turns from c to a permutation from which a quarter turn lands in subset t
    let mut ht = vec![vec![0xFFu8; NC]; 14];
    for t in 0..14 {
        let mut q = Vec::new();
        for c in 0..NC {
            if qts.iter().any(|&mv| sub_of(m.core.cmove[mv][c] as usize) == t) {
                ht[t][c] = 0;
                q.push(c);
            }
        }
        let mut h = 0;
        while h < q.len() {
            let c = q[h];
            h += 1;
            for &mv in &HALF_MOVES {
                let c2 = m.core.cmove[mv][c] as usize;
                if ht[t][c2] == 0xFF {
                    ht[t][c2] = ht[t][c] + 1;
                    q.push(c2);
                }
            }
        }
    }
    let stdin = io::stdin();
    let mut out = BufWriter::new(io::stdout().lock());
    for line in stdin.lock().lines() {
        let line = line?;
        let p: Vec<usize> = line.trim().split('-').filter(|s| !s.is_empty()).map(|s| s.parse().unwrap()).collect();
        if p.is_empty() {
            continue;
        }
        let mut cur: Vec<bool> = (0..NC).map(|c| sub_of(c) == p[0]).collect();
        let mut al = Vec::new();
        let mut feasible = true;
        for i in 0..p.len() - 1 {
            let a = (0..NC).filter(|&c| cur[c]).map(|c| ht[p[i + 1]][c]).min().unwrap_or(0xFF);
            al.push(a);
            // next set: half-turn closure of cur, then a quarter turn into p[i+1]
            let mut clo = cur.clone();
            let mut q: Vec<usize> = (0..NC).filter(|&c| cur[c]).collect();
            let mut h = 0;
            while h < q.len() {
                let c = q[h];
                h += 1;
                for &mv in &HALF_MOVES {
                    let c2 = m.core.cmove[mv][c] as usize;
                    if !clo[c2] {
                        clo[c2] = true;
                        q.push(c2);
                    }
                }
            }
            let mut nxt = vec![false; NC];
            for c in 0..NC {
                if clo[c] {
                    for &mv in &qts {
                        let c2 = m.core.cmove[mv][c] as usize;
                        if sub_of(c2) == p[i + 1] {
                            nxt[c2] = true;
                        }
                    }
                }
            }
            if !nxt.iter().any(|&b| b) {
                feasible = false;
            }
            cur = nxt;
        }
        al.push(0);
        writeln!(
            out,
            "{}\t{}\t{}",
            line.trim(),
            al.iter().map(|v| v.to_string()).collect::<Vec<_>>().join(","),
            feasible as u8
        )?;
    }
    Ok(())
}

pub fn redcount2(ex: &str, n: usize, seed: u64, rmax: usize, out: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let sampler = Sampler::new(&m);
    let nsub = m.cls.sub48_name.len();
    let ncos = NCCOS * NEPAT;
    let ctx = |lf: u8, la: u8| ((lf.wrapping_add(1)) as usize % 256) * 4 + if la == 0xFF { 3 } else { la as usize };
    let nctx = 7 * 4;
    let lfs: Vec<(u8, u8)> = {
        let mut v = vec![(0xFFu8, 0xFFu8)];
        for lf in 0..6u8 {
            for la in [0xFFu8, lf / 2] {
                v.push((lf, la));
            }
        }
        v
    };
    // g[q][L][coset * nctx + ctx]: canonical sequences B of length L from a state in coset, following context, whose
    // last move is a quarter turn and after which qt_full = q
    let mut g = vec![vec![vec![0u32; ncos * nctx]; rmax + 1]; 3];
    for q in 1..=2usize {
        for l in 1..=rmax {
            for a in 0..NCCOS {
                for b in 0..NEPAT {
                    let co = a * NEPAT + b;
                    for &(lf, la) in &lfs {
                        let mut s = 0u32;
                        for mv in 0..NMOVES {
                            if !canonical_next(mv, lf, la) {
                                continue;
                            }
                            let (a2, b2) = (m.cls.ccos_mv[a][mv], m.cls.epat_mv[b][mv]);
                            if l == 1 {
                                if MOVE_IS_QT[mv] && m.cls.qt_full[a2][b2] as usize == q {
                                    s += 1;
                                }
                            } else {
                                s += g[q][l - 1][(a2 * NEPAT + b2) * nctx + ctx(FACE[mv], axis_run(mv, lf, la))];
                            }
                        }
                        g[q][l][co * nctx + ctx(lf, la)] = s;
                    }
                }
            }
        }
    }
    eprintln!("coset tables done");
    let c0 = ctx(0xFF, 0xFF);
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "subset\tidx\td\t{}", (1..=2).flat_map(|q| (0..=rmax).map(move |r| format!("q{}_r{}", q, r))).collect::<Vec<_>>().join("\t"))?;
    for sub in 0..nsub {
        let t0 = Instant::now();
        let res: Vec<String> = (0..n)
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0x9E37_79B9_7F4A_7C15));
                let x = sampler.draw(&m, sub, &mut rng);
                let d = m.depth(x.0, x.1, x.2);
                // cnt[q][r]: pairs with |A| + |B| = r
                let mut cnt = vec![vec![0u64; rmax + 1]; 3];
                let mut add = |c: usize, e: usize, alen: usize| {
                    let (ci, ei) = (m.core.cinv[c] as usize, m.core.einv[e] as usize);
                    let (a, b) = (m.cls.ccos[ci] as usize, m.cls.epat[ei] as usize);
                    let co = a * NEPAT + b;
                    for q in 1..=2 {
                        if m.cls.qt_full[a][b] as usize == q {
                            cnt[q][alen] += 1;
                        }
                        for l in 1..=rmax - alen {
                            cnt[q][alen + l] += g[q][l][co * nctx + c0] as u64;
                        }
                    }
                };
                add(x.0, x.1, 0);
                // A: canonical sequences ending in a quarter turn, up to rmax
                fn dfs(m: &Model, c: usize, e: usize, len: usize, rmax: usize, lf: u8, la: u8, add: &mut dyn FnMut(usize, usize, usize)) {
                    if len == rmax {
                        return;
                    }
                    for mv in 0..NMOVES {
                        if !canonical_next(mv, lf, la) {
                            continue;
                        }
                        let (c2, e2) = (m.core.cmove[mv][c] as usize, m.core.emove[mv][e] as usize);
                        if MOVE_IS_QT[mv] {
                            add(c2, e2, len + 1);
                        }
                        dfs(m, c2, e2, len + 1, rmax, FACE[mv], axis_run(mv, lf, la), add);
                    }
                }
                dfs(&m, x.0, x.1, 0, rmax, 0xFF, 0xFF, &mut add);
                let cols: Vec<String> = (1..=2).flat_map(|q| (0..=rmax).map(move |r| (q, r))).map(|(q, r)| cnt[q][r].to_string()).collect();
                format!("{}\t{}\t{}\t{}", m.cls.sub48_name[sub], i, d, cols.join("\t"))
            })
            .collect();
        for l in res {
            writeln!(f, "{}", l)?;
        }
        f.flush()?;
        eprintln!("redcount2 {} {:.1}s", m.cls.sub48_name[sub], t0.elapsed().as_secs_f64());
    }
    Ok(())
}

/// DR bounding as the method states it (coordinator's definition): a reduction to 1q (or 2q) of length r = |A| + |B|
/// (A on normal, B on inverse) followed by the OPTIMAL finish of the reduced state (any number of quarter turns).
/// Read on finishes: a finish S of X with a prefix of k moves and a suffix of j moves whose middle segment's state is
/// within q quarter turns of HTR (qt_full <= q) gives such a reduction of length k + j, and the middle is an optimal
/// finish of the reduced state whenever S is optimal (a segment of a shortest path is shortest).  Per state and per
/// (finish length - optimum) <= max(1, min(2, 12 - opt)): the shortest such reduction to 1q and to 2q, and the
/// "window" reading of bound / bound2 (the middle has exactly q quarter turns) for comparison.
pub fn bound3(ex: &str, n: usize, seed: u64, out: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let sampler = Sampler::new(&m);
    let nsub = m.cls.sub48_name.len();
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "subset\tidx\td\tcells")?;
    for sub in 0..nsub {
        let t0 = Instant::now();
        let res: Vec<String> = (0..n)
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0x9E37_79B9_7F4A_7C15));
                let x = sampler.draw(&m, sub, &mut rng);
                let d = m.depth(x.0, x.1, x.2) as usize;
                let budget = (d + 1).max((d + 2).min(12));
                // dl -> [stated 1q, stated 2q, window 1q, window 2q]
                let mut cell: HashMap<usize, [u8; 4]> = HashMap::new();
                finishes(&m, x, budget, 2_000_000, &mut |moves, _| {
                    let len = moves.len();
                    let s = sections(moves);
                    let mut best = [99u8, 99, win(&s, len, 1), win(&s, len, 2)];
                    if s.len() == 1 {
                        best[2] = 0;
                        best[3] = 0;
                    }
                    for k in 0..=len {
                        let (mut c, mut e) = (0usize, 0usize);
                        let mut segs = vec![(0usize, 0usize); len + 1];
                        segs[k] = (0, 0);
                        for b in k..len {
                            c = m.core.cmove[moves[b] as usize][c] as usize;
                            e = m.core.emove[moves[b] as usize][e] as usize;
                            segs[b + 1] = (c, e);
                        }
                        for end in k..=len {
                            let (c, e) = segs[end];
                            let q = m.cls.qt_full[m.cls.ccos[c] as usize][m.cls.epat[e] as usize];
                            let r = (k + len - end) as u8;
                            if q <= 1 && r < best[0] {
                                best[0] = r;
                            }
                            if q <= 2 && r < best[1] {
                                best[1] = r;
                            }
                        }
                    }
                    let e = cell.entry(len - d).or_insert([99; 4]);
                    for t in 0..4 {
                        e[t] = e[t].min(best[t]);
                    }
                });
                let mut cells: Vec<String> = cell.iter().map(|(dl, v)| format!("{}:{}:{}:{}:{}", dl, v[0], v[1], v[2], v[3])).collect();
                cells.sort();
                format!("{}\t{}\t{}\t{}", m.cls.sub48_name[sub], i, d, cells.join(";"))
            })
            .collect();
        for l in res {
            writeln!(f, "{}", l)?;
        }
        f.flush()?;
        eprintln!("bound3 {} {:.1}s", m.cls.sub48_name[sub], t0.elapsed().as_secs_f64());
    }
    Ok(())
}

/// DR bounding exactly as stated, by search on reductions: the shortest r = |A| + |B| (A on normal, B on inverse, each
/// empty or ending in a quarter turn) such that the reduced state Z = (X A)^-1 B is within q quarter turns of HTR
/// (qt_full <= q) and r + opt(Z) <= M.  Along A and along B, length + optimum of the current state never decreases,
/// so branches with length + optimum > M are cut; this makes the search exact and cheap for M close to opt(X).
/// Targets: opt, opt + 1, and M = 10, 11, 12 (when M >= opt).  Output per state: target:r1q:r2q (99 = none).
pub fn bound4(ex: &str, n: usize, seed: u64, out: &str) -> io::Result<()> {
    let m = Model::new(Some(Path::new(ex)), None);
    let sampler = Sampler::new(&m);
    let nsub = m.cls.sub48_name.len();
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "subset\tidx\td\ttargets")?;
    fn search_b(m: &Model, z: (usize, usize, usize), blen: usize, alen: usize, mt: usize, lf: u8, la: u8, best: &mut [u8; 3], endq: bool) {
        let r = alen + blen;
        // a 1q reduction is also a 2q one, so best[2] <= best[1]: nothing at r >= best[1] can improve either
        if r >= best[1] as usize {
            return;
        }
        if blen == 0 || endq {
            let q = m.cls.qt_full[m.cls.ccos[z.0] as usize][m.cls.epat[z.1] as usize];
            for t in 1..=2usize {
                if q as usize <= t && (r as u8) < best[t] {
                    best[t] = r as u8;
                }
            }
        }
        for mv in 0..NMOVES {
            if !canonical_next(mv, lf, la) {
                continue;
            }
            let z2 = m.mv(mv, z);
            if r + 1 + m.depth(z2.0, z2.1, z2.2) as usize > mt {
                continue;
            }
            search_b(m, z2, blen + 1, alen, mt, FACE[mv], axis_run(mv, lf, la), best, MOVE_IS_QT[mv]);
        }
    }
    fn search_a(m: &Model, y: (usize, usize, usize), alen: usize, mt: usize, lf: u8, la: u8, best: &mut [u8; 3], endq: bool) {
        if alen >= best[1] as usize {
            return;
        }
        if alen == 0 || endq {
            // inverse-side state (X A)^-1
            let g = crate::core::St::unrank(y.0, y.1, y.2).inv();
            let z = (crate::core::rank_perm(&g.c), crate::core::rank_perm(&g.e), crate::core::rank_perm(&g.s));
            search_b(m, z, 0, alen, mt, 0xFF, 0xFF, best, false);
        }
        for mv in 0..NMOVES {
            if !canonical_next(mv, lf, la) {
                continue;
            }
            let y2 = m.mv(mv, y);
            if alen + 1 + m.depth(y2.0, y2.1, y2.2) as usize > mt {
                continue;
            }
            search_a(m, y2, alen + 1, mt, FACE[mv], axis_run(mv, lf, la), best, MOVE_IS_QT[mv]);
        }
    }
    for sub in 0..nsub {
        let t0 = Instant::now();
        let res: Vec<String> = (0..n)
            .into_par_iter()
            .map(|i| {
                let mut rng = Rng(seed ^ ((sub as u64) << 40) ^ (i as u64).wrapping_mul(0x9E37_79B9_7F4A_7C15));
                let x = sampler.draw(&m, sub, &mut rng);
                let d = m.depth(x.0, x.1, x.2) as usize;
                let mut parts = Vec::new();
                for (name, mt) in [("opt", d), ("p1", d + 1), ("M10", 10), ("M11", 11), ("M12", 12)] {
                    if mt < d {
                        parts.push(format!("{}:99:99", name));
                        continue;
                    }
                    // best[1], best[2]: shortest reduction to 1q / 2q (best[1] bounds the search)
                    let mut best = [99u8; 3];
                    search_a(&m, x, 0, mt, 0xFF, 0xFF, &mut best, false);
                    parts.push(format!("{}:{}:{}", name, best[1], best[2]));
                }
                format!("{}\t{}\t{}\t{}", m.cls.sub48_name[sub], i, d, parts.join(";"))
            })
            .collect();
        for l in res {
            writeln!(f, "{}", l)?;
        }
        f.flush()?;
        eprintln!("bound4 {} {:.1}s", m.cls.sub48_name[sub], t0.elapsed().as_secs_f64());
    }
    Ok(())
}

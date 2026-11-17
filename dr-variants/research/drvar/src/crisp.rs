//! The crisper hypothesis, leave-slice solutions only:
//!
//!   "If you reach 2qt and can set up zero bad slices without a long insertion, then the optimal solution (for
//!    that skeleton) shares the same moves from 3/4/5qt to 2qt, and adds at most one long insertion after 2qt."
//!
//! * Skeletons, variants and the U/D freedom are as in `search.rs`.  The finish of an HTR state is its
//!   leave-slice finish (corners and U/D edges solved with half turns, the E slice left as it falls).
//! * A *section* is the run of half turns before a quarter turn; the finish after the last quarter turn is a
//!   section too.  Its *minimum* is the fewest moves any shortest skeleton of the class has there (for the
//!   finish: the corner kind's own HTR corner moves, 0 / 1 / 2 / 3).  Extra moves in a section are an
//!   insertion; 3 or more extra moves is a *long* insertion.
//! * The *prefix* is everything up to and including the quarter turn that reaches 2qt (m-2 quarter turns of
//!   an m-quarter-turn skeleton; empty for a 2qt skeleton).  Only prefixes with at most 2 extra moves in all
//!   are looked at (no long insertion before 2qt).
//! * A prefix *qualifies* if some continuation (two quarter turns, setup and trigger sections each at most 2
//!   over their minimum) is a variant of the skeleton and lands on a NISS@1qt case with zero bad slices.
//! * Part 1 holds for a qualifying prefix if the best leave-slice solution that keeps the prefix equals the
//!   skeleton's best.  Part 2 holds if one of those best solutions has at most one long section after 2qt
//!   (setup, trigger middle, finish).
use crate::core::St;
use crate::model::*;
use crate::search::*;

/// One continuation after the prefix: its two half-turn sections, the quarter turns, and where it lands.
struct Cont {
    w: Vec<usize>,
    sa: usize,
    sb: usize,
    z: u32,
}

/// Continuations from y with exactly two quarter turns that land in HTR, setup at most `ca` and middle at
/// most `cb` half turns, or (if `ca` = usize::MAX) any length with |prefix| + moves + leave-slice optimum <= bound.
#[allow(clippy::too_many_arguments)]
fn continuations(md: &Model, y: &St, lf: usize, ca: usize, cb: usize, plen: usize, bound: usize) -> Vec<Cont> {
    let mut out = Vec::new();
    let mut w = Vec::new();
    #[allow(clippy::too_many_arguments)]
    fn dfs(md: &Model, s: St, w: &mut Vec<usize>, lf: usize, q: usize, run: usize, sa: usize, ca: usize, cb: usize, plen: usize, bound: usize, out: &mut Vec<Cont>) {
        if q == 2 {
            if let Some(zi) = md.hg.get(&s) {
                out.push(Cont { w: w.clone(), sa, sb: run, z: zi });
            }
            return;
        }
        for mv in 0..10 {
            // right after the fixed prefix only the same face is excluded: "D U2" is the same as "U2 D"
            let ok = if w.is_empty() { lf == 6 || FACE[mv] != lf } else { allowed(lf, mv) };
            if !ok {
                continue;
            }
            let s2 = s.apply_move(mv);
            let unbounded = ca == usize::MAX;
            if unbounded && plen + w.len() + 1 + md.lsopt(&s2) as usize > bound {
                continue;
            }
            if is_qt(mv) {
                w.push(mv);
                if q == 0 {
                    dfs(md, s2, w, FACE[mv], 1, 0, run, ca, cb, plen, bound, out);
                } else {
                    dfs(md, s2, w, FACE[mv], 2, run, sa, ca, cb, plen, bound, out);
                }
                w.pop();
            } else {
                let cap = if q == 0 { ca } else { cb };
                if !unbounded && run + 1 > cap {
                    continue;
                }
                w.push(mv);
                dfs(md, s2, w, FACE[mv], q, run + 1, sa, ca, cb, plen, bound, out);
                w.pop();
            }
        }
    }
    dfs(md, *y, &mut w, lf, 0, 0, 0, ca, cb, plen, bound, &mut out);
    out
}

/// Prefixes: canonical sequences with exactly `nq` quarter turns, ending with one, where section a has at most
/// caps[a] half turns.
fn prefixes(md: &Model, x: &St, nq: usize, mins: &[usize], maxextra: usize, kind: usize, m: usize) -> Vec<Vec<usize>> {
    let mut out = Vec::new();
    if nq == 0 {
        out.push(Vec::new());
        return out;
    }
    let mut w = Vec::new();
    #[allow(clippy::too_many_arguments)]
    fn dfs(md: &Model, s: St, w: &mut Vec<usize>, lf: usize, q: usize, run: usize, extra: usize, nq: usize, mins: &[usize], maxextra: usize, kind: usize, m: usize, out: &mut Vec<Vec<usize>>) {
        if q == nq {
            out.push(w.clone());
            return;
        }
        for mv in 0..10 {
            if !allowed(lf, mv) {
                continue;
            }
            let s2 = s.apply_move(mv);
            let q2 = q + is_qt(mv) as usize;
            // the corners must still be able to finish the skeleton's quarter turns
            if md.rem[kind][m - q2][crate::core::rank_perm(&s2.c)] == 255 {
                continue;
            }
            if is_qt(mv) {
                // a section shorter than the minimum is impossible; the extra of this one is final now
                let e = extra + run.saturating_sub(mins[q]);
                if e > maxextra {
                    continue;
                }
                w.push(mv);
                dfs(md, s2, w, FACE[mv], q2, 0, e, nq, mins, maxextra, kind, m, out);
                w.pop();
            } else {
                if (extra + (run + 1).saturating_sub(mins[q])) > maxextra {
                    continue;
                }
                w.push(mv);
                dfs(md, s2, w, FACE[mv], q, run + 1, extra, nq, mins, maxextra, kind, m, out);
                w.pop();
            }
        }
    }
    dfs(md, *x, &mut w, 6, 0, 0, 0, nq, mins, maxextra, kind, m, &mut out);
    out
}

fn sections(w: &[usize]) -> Vec<usize> {
    let mut out = Vec::new();
    let mut run = 0;
    for &mv in w {
        if is_qt(mv) {
            out.push(run);
            run = 0;
        } else {
            run += 1;
        }
    }
    out
}

pub fn analyse(md: &Model, hc: &HcIndex, jcl: &[[u8; 8]], x: &St, id: usize, mlist: &[usize]) -> Vec<String> {
    let lp = skeleton_lengths(md, x, 6);
    let mmin = (1..=6).find(|&m| lp[m].iter().any(|&l| l != 255)).unwrap();
    let lmin = (1..=6).flat_map(|m| lp[m].iter().copied()).min().unwrap();
    let lsx = md.lsopt(x);
    let sub = md.subset(x);
    let scr = wname(&crate::scramble_of(md, x));
    let mut lines = Vec::new();
    for m in mmin..=(mmin + 1).min(6) {
        if !mlist.contains(&m) {
            continue;
        }
        for kind in 0..6 {
            let lpre = lp[m][kind];
            if lpre == 255 || lpre > lmin + 3 {
                continue;
            }
            let tm = std::time::Instant::now();
            let timing = std::env::var_os("DRVAR_TIME").is_some();
            // section minimums over the family's shortest skeletons
            let words = skeletons_of(md, x, m, kind, lpre as usize);
            let mut minsec = vec![usize::MAX; m];
            for w in &words {
                for (a, &l) in sections(w).iter().enumerate() {
                    minsec[a] = minsec[a].min(l);
                }
            }
            // validation (DRVAR_VALIDATE): are the family's paths variants of its shortest skeletons?
            let validate = std::env::var_os("DRVAR_VALIDATE").is_some();
            let sks: Vec<Skeleton> = if validate { words.iter().take(4096).map(|w| make_skeleton(md, hc, jcl, w.clone(), kind as u8)).collect() } else { Vec::new() };
            let minfin = LC[kind] as usize;
            let in_fam = |z: u32| md.cases[md.hcase[z as usize] as usize].kind as usize == kind;
            // the skeleton's best leave-slice solution: deepen from the DR's leave-slice optimum
            let mut best = 255usize;
            let mut bestsol = String::new();
            let mut bound = lsx as usize;
            while bound <= lsx as usize + 5 {
                let sols = paths(md, x, bound, m, |s, _, _| md.lsopt(s) as usize, |_, mm, k, b| mm as usize == m && k as usize == kind && b as usize <= bound);
                if let Some(b) = sols.iter().map(|p| p.best as usize).min() {
                    best = b;
                    // what the skeleton's best solutions look like: extra moves before 2qt, long sections
                    // before and after 2qt (the finish counts as a section after 2qt)
                    let mut shape: Vec<(usize, usize, usize, String)> = Vec::new();
                    for p in sols.iter().filter(|p| p.best as usize == b) {
                        let sec = sections(&p.w);
                        let fe = (md.fin[p.z as usize] as usize).saturating_sub(LC[kind] as usize);
                        let pre_extra: usize = (0..m - 2).map(|a| sec[a].saturating_sub(minsec[a])).sum();
                        let pre_long = (0..m - 2).filter(|&a| sec[a] >= minsec[a] + 3).count();
                        let post_long = (m - 2..m).filter(|&a| sec[a] >= minsec[a] + 3).count() + (fe >= 3) as usize;
                        shape.push((pre_long, post_long, pre_extra, format!("{} | {}", wname(&p.w), wname(&ls_finish(md, p.z)))));
                    }
                    let n_opt = shape.len();
                    let min_pre_extra = shape.iter().map(|s| s.2).min().unwrap();
                    let min_pre_long = shape.iter().map(|s| s.0).min().unwrap();
                    let best_shape = shape.iter().min_by_key(|s| (s.0, s.1, s.2)).unwrap();
                    // which search restrictions still contain a best solution
                    let r_a = shape.iter().any(|s| s.0 == 0 && s.1 <= 1); // no long before 2qt, <= 1 long after
                    let r_b = shape.iter().any(|s| s.2 == 0); // no extra move before 2qt
                    let r_c = shape.iter().any(|s| s.2 == 0 && s.1 <= 1); // no extra before, <= 1 long after
                    let r_d = shape.iter().any(|s| s.2 <= 2 && s.1 <= 1); // <= 2 extra before, <= 1 long after
                    let r_e = shape.iter().any(|s| s.0 + s.1 <= 1); // at most one long insertion anywhere
                    lines.push(format!(
                        "O\t{id}\t{sub}\t{m}\t{}\t{lpre}\t{b}\t{n_opt}\t{min_pre_extra}\t{min_pre_long}\t{}\t{}\t{}\t{}\t{r_a}\t{r_b}\t{r_c}\t{r_d}\t{r_e}",
                        KIND_NAME[kind], best_shape.0, best_shape.1, best_shape.3, wname(&words[0])
                    ));
                    let p = sols.iter().filter(|p| p.best as usize == b).min_by_key(|p| p.w.len()).unwrap();
                    bestsol = format!("{} | {}", wname(&p.w), wname(&ls_finish(md, p.z)));
                    if validate {
                        let more = paths(md, x, b + 1, m, |s, _, _| md.lsopt(s) as usize, |_, mm, k, bb| mm as usize == m && k as usize == kind && bb as usize <= b + 1);
                        let nv = more.iter().filter(|p| sks.iter().any(|sk| is_variant(hc, sk, &p.w))).count();
                        lines.push(format!("V\t{id}\t{m}\t{}\t{}\t{nv}", KIND_NAME[kind], more.len()));
                    }
                    break;
                }
                bound += 1;
            }
            if best == 255 {
                lines.push(format!("S\t{id}\t{sub}\t{m}\t{}\t{lpre}\tunknown", KIND_NAME[kind]));
                continue;
            }
            if validate {
                continue;
            }
            // prefixes down to 2qt with no long section; at most PCAP of them, a fixed pseudo-random sample
            let mut pres = prefixes(md, x, m - 2, &minsec, 2, kind, m);
            let npres = pres.len();
            const PCAP: usize = 80;
            if pres.len() > PCAP {
                let mut r = crate::Rng(0xC0FFEE ^ ((id as u64) << 12) ^ ((m as u64) << 4) ^ kind as u64);
                for i in 0..PCAP {
                    let j = i + r.below((pres.len() - i) as u64) as usize;
                    pres.swap(i, j);
                }
                pres.truncate(PCAP);
            }
            // best leave-slice solution keeping a prefix, and the fewest long sections after 2qt among those
            let keep = |pre: &[usize]| -> (usize, usize, String) {
                let y = x.mul(word(pre));
                let lf = pre.last().map_or(6, |&mv| FACE[mv]);
                let all = continuations(md, &y, lf, usize::MAX, usize::MAX, pre.len(), best + 2);
                let mut r: Option<(usize, usize, &Cont)> = None;
                for c in &all {
                    if !in_fam(c.z) {
                        continue;
                    }
                    let tot = pre.len() + c.w.len() + md.fin[c.z as usize] as usize;
                    let longs = (c.sa >= minsec[m - 2] + 3) as usize + (c.sb >= minsec[m - 1] + 3) as usize + (md.fin[c.z as usize] as usize >= minfin + 3) as usize;
                    if r.map_or(true, |(t, l, _)| (tot, longs) < (t, l)) {
                        r = Some((tot, longs, c));
                    }
                }
                match r {
                    None => (255, 9, String::new()),
                    Some((t, l, c)) => (t, l, format!("{} | {} | {}", wname(pre), wname(&c.w), wname(&ls_finish(md, c.z)))),
                }
            };
            let (mut nq, mut n1, mut n2) = (0usize, 0usize, 0usize);
            for pre in &pres {
                let y = x.mul(word(pre));
                let lf = pre.last().map_or(6, |&mv| FACE[mv]);
                let pextra: usize = sections(pre).iter().zip(&minsec).map(|(&l, &mn)| l.saturating_sub(mn)).sum();
                // qualifies: a cheap continuation in the skeleton with zero bad slices
                let cheap = continuations(md, &y, lf, minsec[m - 2] + 2, minsec[m - 1] + 2, 0, 0);
                let Some(g0) = cheap
                    .iter()
                    .filter(|c| in_fam(c.z) && md.cases[md.hcase[c.z as usize] as usize].bad() == 0)
                    .min_by_key(|c| c.w.len() + md.fin[c.z as usize] as usize)
                else {
                    // not qualifying: does it keep the best anyway? (routes with no extra moves only)
                    if pextra == 0 {
                        let any_cheap = cheap.iter().any(|c| in_fam(c.z));
                        let (pb, _, _) = keep(pre);
                        lines.push(format!("N\t{id}\t{m}\t{}\t{best}\t{pb}\t{}\t{any_cheap}\t{}", KIND_NAME[kind], pb == best, npres as f64 / pres.len() as f64));
                    }
                    continue;
                };
                nq += 1;
                let (pbest, fewest_long, bestw) = keep(pre);
                let part1 = pbest == best;
                let part2 = part1 && fewest_long <= 1;
                n1 += part1 as usize;
                n2 += part2 as usize;
                // if part 1 fails: would the same half turns with the prefix's quarter turns turned keep the best?
                let mut loose = part1;
                if !part1 && m > 2 {
                    let qi: Vec<usize> = (0..pre.len()).filter(|&i| is_qt(pre[i])).collect();
                    let n = qi.len();
                    for code in 0..(1usize << (2 * n)) {
                        let mut p2 = pre.clone();
                        for (k, &i) in qi.iter().enumerate() {
                            p2[i] = [0, 2, 3, 5][(code >> (2 * k)) & 3];
                        }
                        if p2 == *pre || reduce(&p2).len() != p2.len() {
                            continue;
                        }
                        if keep(&p2).0 == best {
                            loose = true;
                            break;
                        }
                    }
                }
                let gfin = ls_finish(md, g0.z);
                lines.push(format!(
                    "P\t{id}\t{sub}\t{m}\t{k}\t{lpre}\t{best}\t{pextra}\t{pb}\t{part1}\t{fl}\t{part2}\t{loose}\t{gw}\t{bw}\t{scr}\t{wt}",
                    k = KIND_NAME[kind],
                    pb = pbest,
                    fl = fewest_long,
                    gw = format!("{} | {} | {} ({})", wname(pre), wname(&g0.w), wname(&gfin), pre.len() + g0.w.len() + gfin.len()),
                    bw = bestw,
                    wt = npres as f64 / pres.len() as f64,
                ));
            }
            if timing {
                eprintln!("state {id} m {m} {}: {npres} prefixes ({} tested), {nq} qualify, {:.2}s", KIND_NAME[kind], pres.len(), tm.elapsed().as_secs_f64());
            }
            lines.push(format!("S\t{id}\t{sub}\t{m}\t{}\t{lpre}\t{best}\t{npres}\t{}\t{nq}\t{n1}\t{n2}\t{}\t{bestsol}", KIND_NAME[kind], pres.len(), wname(&words[0])));
        }
    }
    let _ = scr;
    lines
}

/// A shortest leave-slice half-turn finish of H state z.
pub fn ls_finish(md: &Model, z: u32) -> Vec<usize> {
    let mut s = md.hg.st[z as usize];
    let mut out = Vec::new();
    while md.fin[md.hg.get(&s).unwrap() as usize] > 0 {
        let d = md.fin[md.hg.get(&s).unwrap() as usize];
        let mv = HALF.iter().copied().find(|&mv| md.fin[md.hg.get(&s.apply_move(mv)).unwrap() as usize] + 1 == d).unwrap();
        out.push(mv);
        s = s.apply_move(mv);
    }
    out
}

//! Two follow-ups to the 2qt hypothesis, leave-slice solutions, DRs and skeletons of at most 4 quarter turns.
//!
//! * The 3qt version: "if a 4qt skeleton has a variant leading to zero bad slices with no long insertions, then
//!   the optimal solution for that skeleton shares the same 4qt-to-3qt moves."  The route is the first section
//!   and the first quarter turn (at most 2 extra moves).  It qualifies if some continuation (three quarter
//!   turns, no section 3+ over its minimum) is in the skeleton and lands on zero bad slices.
//! * The skeleton comparison: "If there is a skeleton that has a variant leading to zero bad slices with no long
//!   insertions, the overall-optimal solution will use one such skeleton."  A skeleton is *good* if it has such a
//!   variant (every section at most 2 over its minimum).
//!
//! Skeleton = (quarter turns, NISS@1qt corner kind), section minimums and the leave-slice finish as in `crisp.rs`.
use crate::core::St;
use crate::model::*;
use crate::search::*;
use std::collections::HashSet;

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

/// H elements with a half-turn word of at most `cap` moves, for each cap up to `maxcap`.
pub struct HBalls {
    pub by_cap: Vec<Vec<St>>,
}
impl HBalls {
    pub fn new(md: &Model, maxcap: usize) -> HBalls {
        let by_cap = (0..=maxcap).map(|c| md.hg.st.iter().zip(&md.hg.d3).filter(|(_, &d)| d as usize <= c).map(|(s, _)| *s).collect()).collect();
        HBalls { by_cap }
    }
}

/// Is there a path from `start` with sections at most caps[i] half turns, one quarter turn after each, that lands
/// in HTR on a case of this corner kind with zero bad slices?  Searched layer by layer (states after each
/// quarter turn, duplicates merged), pruned with the corner-only distance to the kind.
pub fn cheap_exists(md: &Model, hb: &HBalls, start: &St, caps: &[usize], kind: usize) -> bool {
    let n = caps.len();
    let mut layer: Vec<St> = vec![*start];
    for i in 0..n {
        let mut seen: HashSet<u64> = HashSet::new();
        let mut next: Vec<St> = Vec::new();
        let left_after = n - i - 1; // quarter turns still to come after this one
        let room_after: usize = caps[i + 1..].iter().sum::<usize>() + left_after;
        for s in &layer {
            for h in &hb.by_cap[caps[i].min(hb.by_cap.len() - 1)] {
                let t = s.mul(*h);
                for qt in [0usize, 2, 3, 5] {
                    let u = t.apply_move(qt);
                    let c = crate::core::rank_perm(&u.c);
                    let r = md.rem[kind][left_after][c];
                    if r == 255 || r as usize > room_after || md.htrd(&u) as usize > room_after {
                        continue;
                    }
                    if left_after == 0 {
                        if let Some(zi) = md.hg.get(&u) {
                            let cs = &md.cases[md.hcase[zi as usize] as usize];
                            if cs.kind as usize == kind && cs.bad() == 0 {
                                return true;
                            }
                        }
                        continue;
                    }
                    if seen.insert(key(&u)) {
                        next.push(u);
                    }
                }
            }
        }
        layer = next;
        if layer.is_empty() {
            return false;
        }
    }
    false
}

/// Best leave-slice total (prefix + n quarter turns and their sections + finish) keeping the prefix, if <= bound.
fn best_keeping(md: &Model, y: &St, lf: usize, nq: usize, kind: usize, plen: usize, bound: usize) -> Option<usize> {
    let mut best: Option<usize> = None;
    let mut w: Vec<usize> = Vec::new();
    #[allow(clippy::too_many_arguments)]
    fn dfs(md: &Model, s: St, w: &mut Vec<usize>, lf: usize, q: usize, nq: usize, kind: usize, plen: usize, bound: usize, best: &mut Option<usize>) {
        if q == nq {
            if let Some(zi) = md.hg.get(&s) {
                if md.cases[md.hcase[zi as usize] as usize].kind as usize == kind {
                    let t = plen + w.len() + md.fin[zi as usize] as usize;
                    if t <= bound && best.map_or(true, |b| t < b) {
                        *best = Some(t);
                    }
                }
            }
            return;
        }
        for mv in 0..10 {
            let ok = if w.is_empty() { lf == 6 || FACE[mv] != lf } else { allowed(lf, mv) };
            if !ok {
                continue;
            }
            let s2 = s.apply_move(mv);
            let lim = best.map_or(bound, |b| b - 1);
            if plen + w.len() + 1 + md.lsopt(&s2) as usize > lim {
                continue;
            }
            w.push(mv);
            dfs(md, s2, w, FACE[mv], q + is_qt(mv) as usize, nq, kind, plen, bound, best);
            w.pop();
        }
    }
    dfs(md, *y, &mut w, lf, 0, nq, kind, plen, bound, &mut best);
    best
}

struct Fam {
    m: usize,
    kind: usize,
    lpre: usize,
    minsec: Vec<usize>,
    best: usize,
    good: bool,
}

pub fn analyse(md: &Model, hb: &HBalls, x: &St, id: usize) -> Vec<String> {
    let mut lines = Vec::new();
    let lp = skeleton_lengths(md, x, 6);
    let mmin = (1..=6).find(|&m| lp[m].iter().any(|&l| l != 255)).unwrap();
    if mmin >= 5 {
        return lines; // 5qt DR subsets are left out
    }
    let lmin = (1..=4).flat_map(|m| lp[m].iter().copied()).min().unwrap() as usize;
    let lsx = md.lsopt(x) as usize;
    let sub = md.subset(x);
    let scr = wname(&crate::scramble_of(md, x));
    // the DR's optimal leave-slice solutions and their skeletons
    let opt_sols = paths(md, x, lsx, 6, |s, _, _| md.lsopt(s) as usize, |_, _, _, b| b as usize <= lsx);
    let mut opt_fams: Vec<(usize, usize)> = opt_sols.iter().map(|p| (p.m as usize, p.kind as usize)).collect();
    opt_fams.sort_unstable();
    opt_fams.dedup();
    assert!(!opt_fams.is_empty(), "no optimal leave-slice solution found");
    // the skeletons looked at: fewest quarter turns or one more (at most 4), at most 3 moves over the shortest,
    // and every skeleton of an optimal solution with at most 4 quarter turns
    let mut want: Vec<(usize, usize)> = Vec::new();
    for m in mmin..=(mmin + 1).min(4) {
        for k in 0..6 {
            if lp[m][k] != 255 && lp[m][k] as usize <= lmin + 3 {
                want.push((m, k));
            }
        }
    }
    for &(m, k) in &opt_fams {
        if m <= 4 && !want.contains(&(m, k)) {
            want.push((m, k));
        }
    }
    let mut fams: Vec<Fam> = Vec::new();
    for &(m, kind) in &want {
        let lpre = lp[m][kind] as usize;
        let words = skeletons_of(md, x, m, kind, lpre);
        let mut minsec = vec![usize::MAX; m];
        for w in &words {
            for (a, &l) in sections(w).iter().enumerate() {
                minsec[a] = minsec[a].min(l);
            }
        }
        let mut best = usize::MAX;
        for bound in lsx..=lsx + 6 {
            let sols = paths(md, x, bound, m, |s, _, _| md.lsopt(s) as usize, |_, mm, k, b| mm as usize == m && k as usize == kind && b as usize <= bound);
            if let Some(b) = sols.iter().map(|p| p.best as usize).min() {
                best = b;
                break;
            }
        }
        let caps: Vec<usize> = minsec.iter().map(|&l| l + 2).collect();
        let good = cheap_exists(md, hb, x, &caps, kind);
        fams.push(Fam { m, kind, lpre, minsec, best, good });
    }
    // ---- the skeleton comparison
    let any_good = fams.iter().any(|f| f.good);
    let opt_good = opt_fams.iter().any(|&(m, k)| fams.iter().any(|f| f.m == m && f.kind == k && f.good));
    let opt_over4 = opt_fams.iter().all(|&(m, _)| m > 4);
    let best_good = fams.iter().filter(|f| f.good).map(|f| f.best).min().unwrap_or(usize::MAX);
    let desc: Vec<String> = fams
        .iter()
        .map(|f| format!("{}qt {} L{} best {}{}{}", f.m, KIND_NAME[f.kind], f.lpre, if f.best == usize::MAX { 99 } else { f.best }, if f.good { " good" } else { "" }, if opt_fams.contains(&(f.m, f.kind)) { " OPT" } else { "" }))
        .collect();
    let osol = opt_sols.iter().min_by_key(|p| p.w.len()).map(|p| format!("{} | {}", wname(&p.w), wname(&crate::crisp::ls_finish(md, p.z)))).unwrap();
    lines.push(format!(
        "B\t{id}\t{sub}\t{mmin}\t{lsx}\t{any_good}\t{opt_good}\t{opt_over4}\t{bg}\t{}\t{osol}\t{scr}",
        desc.join("; "),
        bg = if best_good == usize::MAX { 99 } else { best_good },
    ));
    // ---- the 3qt version on 4qt skeletons
    for f in fams.iter().filter(|f| f.m == 4 && f.best != usize::MAX) {
        // routes to 3qt: the first section (at most 2 over its minimum) and a quarter turn
        let mut routes: Vec<Vec<usize>> = Vec::new();
        let mut w: Vec<usize> = Vec::new();
        fn gen(md: &Model, s: St, w: &mut Vec<usize>, lf: usize, cap: usize, kind: usize, out: &mut Vec<Vec<usize>>) {
            for mv in 0..10 {
                if !allowed(lf, mv) {
                    continue;
                }
                let s2 = s.apply_move(mv);
                if is_qt(mv) {
                    if md.rem[kind][3][crate::core::rank_perm(&s2.c)] != 255 {
                        let mut r = w.clone();
                        r.push(mv);
                        out.push(r);
                    }
                } else if w.len() < cap {
                    w.push(mv);
                    gen(md, s2, w, FACE[mv], cap, kind, out);
                    w.pop();
                }
            }
        }
        gen(md, *x, &mut w, 6, f.minsec[0] + 2, f.kind, &mut routes);
        let caps: Vec<usize> = f.minsec[1..].iter().map(|&l| l + 2).collect();
        for r in &routes {
            let y = x.mul(word(r));
            if !cheap_exists(md, hb, &y, &caps, f.kind) {
                continue;
            }
            let lf = FACE[*r.last().unwrap()];
            let pb = best_keeping(md, &y, lf, 3, f.kind, r.len(), f.best + 2);
            let part1 = pb == Some(f.best);
            // the same half turns with the quarter turn turned
            let mut loose = part1;
            if !part1 {
                for qt in [0usize, 2, 3, 5] {
                    let mut r2 = r.clone();
                    *r2.last_mut().unwrap() = qt;
                    if r2 == *r || reduce(&r2).len() != r2.len() {
                        continue;
                    }
                    let y2 = x.mul(word(&r2));
                    if best_keeping(md, &y2, FACE[qt], 3, f.kind, r2.len(), f.best) == Some(f.best) {
                        loose = true;
                        break;
                    }
                }
            }
            let extra = r.len() - 1 - f.minsec[0];
            lines.push(format!(
                "T\t{id}\t{sub}\t{}\t{}\t{}\t{extra}\t{}\t{}\t{part1}\t{loose}\t{scr}",
                KIND_NAME[f.kind],
                f.lpre,
                f.best,
                wname(r),
                pb.map_or(99, |b| b),
            ));
        }
    }
    lines
}

/// Stricter "good": for slack 0, 1, 2, does the skeleton (m, kind) have a variant landing on zero bad slices with
/// every section before HTR at most `slack` moves over its minimum?  (slack 2 is the `good` of `analyse`.)
pub fn goodness(md: &Model, hb: &HBalls, x: &St, m: usize, kind: usize, lpre: usize) -> (Vec<usize>, [bool; 3]) {
    let words = skeletons_of(md, x, m, kind, lpre);
    let mut minsec = vec![usize::MAX; m];
    for w in &words {
        for (a, &l) in sections(w).iter().enumerate() {
            minsec[a] = minsec[a].min(l);
        }
    }
    let mut g = [false; 3];
    for slack in 0..3 {
        // a skeleton good at a smaller slack is good at every larger one
        if slack > 0 && g[slack - 1] {
            g[slack] = true;
            continue;
        }
        let caps: Vec<usize> = minsec.iter().map(|&l| l + slack).collect();
        g[slack] = cheap_exists(md, hb, x, &caps, kind);
    }
    (minsec, g)
}

/// Like `cheap_exists`, but returns one such path (half-turn sections and quarter turns, as moves).
pub fn cheap_witness(md: &Model, hb: &HBalls, start: &St, caps: &[usize], kind: usize) -> Option<Vec<usize>> {
    let n = caps.len();
    // per layer: (state, parent index in the previous layer, H element, quarter turn)
    let mut layers: Vec<Vec<(St, usize, St, usize)>> = vec![vec![(*start, 0, St::ID, 0)]];
    for i in 0..n {
        let mut seen: HashSet<u64> = HashSet::new();
        let mut next = Vec::new();
        let left_after = n - i - 1;
        let room_after: usize = caps[i + 1..].iter().sum::<usize>() + left_after;
        for (pi, (s, ..)) in layers[i].iter().enumerate() {
            for h in &hb.by_cap[caps[i].min(hb.by_cap.len() - 1)] {
                let t = s.mul(*h);
                for qt in [0usize, 2, 3, 5] {
                    let u = t.apply_move(qt);
                    let c = crate::core::rank_perm(&u.c);
                    let r = md.rem[kind][left_after][c];
                    if r == 255 || r as usize > room_after || md.htrd(&u) as usize > room_after {
                        continue;
                    }
                    if left_after == 0 {
                        let ok = md.hg.get(&u).map_or(false, |zi| {
                            let cs = &md.cases[md.hcase[zi as usize] as usize];
                            cs.kind as usize == kind && cs.bad() == 0
                        });
                        if !ok {
                            continue;
                        }
                        // walk back
                        let mut parts = vec![(*h, qt)];
                        let mut p = pi;
                        for j in (1..=i).rev() {
                            let (_, pp, hh, qq) = layers[j][p];
                            parts.push((hh, qq));
                            p = pp;
                        }
                        parts.reverse();
                        let mut w = Vec::new();
                        for (hh, qq) in parts {
                            w.extend(md.hg.word_of(md.hg.get(&hh).unwrap()));
                            w.push(qq);
                        }
                        return Some(w);
                    }
                    if seen.insert(key(&u)) {
                        next.push((u, pi, *h, qt));
                    }
                }
            }
        }
        if next.is_empty() {
            return None;
        }
        layers.push(next);
    }
    None
}

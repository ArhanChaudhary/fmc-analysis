//! The standard meta against the skeleton/variant meta: which within-goal solutions each one reaches.
//!
//! Standard meta with cap c: every HTR that is at most c moves away is finished.  Those moves are made on normal,
//! on inverse, or with one NISS after a start of one to three moves: the start on one side, the rest of the way to
//! HTR on the other.  The starts (`starts`): a quarter turn (1 move); a side half turn and a quarter turn (2); and,
//! with a first move on the U or D layer, that move, a side half turn and a quarter turn (3: U R2 U', U2 R2 U).
//! Every other start of that many moves reaches the same HTRs as a shorter start or as no NISS at all, sooner: one
//! that ends on a half turn (drop it), one whose half turn is U2 or D2 next to the quarter turn (they commute), and
//! U D or U D' in front (a U2 or nothing as far as a leave-slice finish goes).  `STD_EXTRA=1` runs those other
//! three-move starts too, as a check that the bests by cap don't move.  No bound: every HTR inside the cap counts
//! as finished.
//!
//! Skeleton/variant meta: what of the page's rule needs no lower bound for N, which is P <= 1 and P+S+T <= 5 (an HTR
//! in sight already has L+P+S+T within the goal), on the classes of `Ctx::classes`, read by `tuple::read`.  With
//! `SVM_STD_BOUND=1` the whole rule of the page instead: the mirror floor (step 4) and the corner-case-aware bound
//! as well.  With `SVM_PAIRS=drop` a most-pairs step is
//! added: of the classes those let through on one skeleton with the same (P, S, T, N), only the ones with the most
//! pairs right after the last insertion are finished.  The premove pass comes on top (`pass_side`; `SVM_UNISS=0`
//! leaves it out): for a skeleton of 3 or more quarter turns that ends with its last one, that turn is made first on
//! the other side and what is left is gone through with the cap, the bound and a goal one lower (`tuple::rest`).
//!
//! A solution is a path to an HTR plus a half-turn finish of it, written on normal.  A meta reaches the solution W
//! when it finishes an HTR on W: one that splits W into moves it makes, then half turns only, then moves it makes
//! on the other side.  Paths are looked up by class (`Imager::key`), so which of U and D is turned does not matter.
use crate::core::{rank_perm, St, MOVE_INV};
use crate::meta::{goal_of, htr_like, passes_htr, qt_count, Ctx, Uni};
use crate::model::*;
use crate::tuple::{load_rules, read, read_solution, Sec};
use std::collections::HashMap;

/// The longest way to HTR looked at for the standard meta.
pub const CAPMAX: usize = 14;
const CAPS: std::ops::RangeInclusive<usize> = 7..=CAPMAX;
/// The most moves before the NISS.
const PRE: usize = 3;

fn inv_word(w: &[usize]) -> Vec<usize> {
    w.iter().rev().map(|&m| MOVE_INV[m]).collect()
}

/// Cancelled, and two moves on one axis in the order U D, R L, F B.
fn canon(w: &[usize]) -> Vec<usize> {
    let mut r = reduce(w);
    for i in 0..r.len().saturating_sub(1) {
        let (a, b) = (FACE[r[i]], FACE[r[i + 1]]);
        if a / 2 == b / 2 && a > b {
            r.swap(i, i + 1);
        }
    }
    r
}

/// One solution, however its half-turn stretches are written and whichever of U and D is turned: the quarter
/// turns of the D-free image, and what each stretch of half turns between them does to the corners and the U/D
/// edges.  Two optimal finishes of one HTR give one key.
fn solkey(cx: &Ctx, w: &[usize]) -> Vec<u32> {
    let mut key = Vec::new();
    let mut g = St::ID;
    for &mv in &cx.im.image(w) {
        if is_qt(mv) {
            key.extend([rank_perm(&g.c) as u32, rank_perm(&g.e) as u32, 100_000 + mv as u32]);
            g = St::ID;
        } else {
            g = g.apply_move(mv);
        }
    }
    key.extend([rank_perm(&g.c) as u32, rank_perm(&g.e) as u32]);
    key
}

fn last_qt(w: &[usize]) -> Option<usize> {
    w.iter().rposition(|&m| is_qt(m))
}

/// Every path from `y` of at most `maxlen` moves that ends with a quarter turn on an HTR state, comes through no
/// HTR before, and keeps path + half-turn finish within `glen`: f(path, HTR state index).
fn arrivals<F: FnMut(&[usize], u32)>(md: &Model, y: &St, glen: usize, maxlen: usize, f: &mut F) {
    fn dfs<F: FnMut(&[usize], u32)>(md: &Model, s: St, w: &mut Vec<usize>, lf: usize, glen: usize, maxlen: usize, f: &mut F) {
        if let Some(&last) = w.last() {
            if is_qt(last) {
                if let Some(zi) = md.hg.get(&s) {
                    if w.len() + md.fin[zi as usize] as usize <= glen {
                        f(w, zi);
                    }
                }
                if htr_like(md, &s) {
                    return;
                }
            }
        }
        if w.len() >= maxlen {
            return;
        }
        for mv in 0..10 {
            if !allowed(lf, mv) {
                continue;
            }
            let s2 = s.apply_move(mv);
            let len = w.len() + 1;
            if len + md.htrd(&s2) as usize > maxlen || len + md.lsopt(&s2) as usize > glen {
                continue;
            }
            w.push(mv);
            dfs(md, s2, w, FACE[mv], glen, maxlen, f);
            w.pop();
        }
    }
    let mut w = Vec::with_capacity(16);
    dfs(md, *y, &mut w, 6, glen, maxlen, f);
}

/// The starts of a NISS, each with its number of moves: a quarter turn (1); a side half turn and a quarter turn
/// (2); a move of the U or D layer, a side half turn and a quarter turn (3).  With `extra`, every other canonical
/// start of three moves that begins on the U or D layer as well, marked 4.
fn starts(extra: bool) -> Vec<(u8, Vec<usize>)> {
    const Q: [usize; 4] = [0, 2, 3, 5];
    let mut v: Vec<(u8, Vec<usize>)> = Vec::new();
    for q in Q {
        v.push((1, vec![q]));
    }
    for h in 6..10 {
        for q in Q {
            v.push((2, vec![h, q]));
        }
    }
    for a in 0..6 {
        for h in 6..10 {
            for q in Q {
                v.push((3, vec![a, h, q]));
            }
        }
    }
    if extra {
        for a in 0..6 {
            for b in (0..10).filter(|&b| allowed(FACE[a], b)) {
                for c in (0..10).filter(|&c| allowed(FACE[b], c)) {
                    if !v.iter().any(|s| s.1 == [a, b, c]) {
                        v.push((4, vec![a, b, c]));
                    }
                }
            }
        }
    }
    v
}

/// The ways W can begin with a NISS start: (the first one to three moves, the rest of W), over the ways of writing
/// W that differ in the order of two moves on one axis (U2 D = D U2, U D = D U, R2 L2 = L2 R2).
fn niss_splits(w: &[usize]) -> Vec<(Vec<usize>, Vec<usize>)> {
    let c = canon(w);
    let mut vars = vec![c.clone()];
    for i in 0..PRE.min(c.len().saturating_sub(1)) {
        // two neighbours on one axis; a third can't follow in a cancelled word, so the swaps don't overlap
        if FACE[c[i]] / 2 == FACE[c[i + 1]] / 2 {
            for j in 0..vars.len() {
                let mut v = vars[j].clone();
                v.swap(i, i + 1);
                vars.push(v);
            }
        }
    }
    let mut out: Vec<(Vec<usize>, Vec<usize>)> = Vec::new();
    for v in &vars {
        for k in 1..=PRE.min(v.len().saturating_sub(1)) {
            let split = (v[..k].to_vec(), v[k..].to_vec());
            if !out.contains(&split) {
                out.push(split);
            }
        }
    }
    out
}

struct SvCls {
    q: u8,
    l: u8,
    p: u8,
    s: u8,
    t: u8,
    nb: u8,
    floor: i16,
    /// passes P <= 1 and P+S+T <= 5 (with `SVM_STD_BOUND=1`: the mirror floor and the bound as well)
    adm: bool,
    total: u8,
    /// the skeleton (corner cases at the quarter turns) and the pairs right after the last insertion
    route: u64,
    pairs: u8,
    /// finished: `adm`, and no other `adm` class of the skeleton with the same (P, S, T, N) has more pairs
    fin: bool,
}

fn wvec(a: &[u8; 16], n: u8) -> Vec<usize> {
    a[..n as usize].iter().map(|&m| m as usize).collect()
}

/// `SVM_STD_BOUND=1`: the page's whole rule, with step 4 and the bound (the default leaves out both).
fn with_bound() -> bool {
    std::env::var("SVM_STD_BOUND").is_ok_and(|v| v == "1")
}

/// The classes of one side with the rule of the page applied, and the within-goal solutions (written on this side).
fn sv_side(cx: &Ctx, sec: &Sec, y: &St, goal: usize, qmax: usize) -> (HashMap<u64, SvCls>, Vec<Vec<usize>>) {
    let md = cx.md;
    let cl = cx.classes(y, &Uni { goal, cap_any: 0, qmax });
    let mut map = HashMap::with_capacity(cl.len());
    let mut sols = Vec::new();
    for (k, c) in &cl {
        let w = wvec(&c.w, c.wl);
        let r = read(sec, y, &w, &md.hg.st[c.z as usize]);
        let (p, s, t) = r.pst();
        let (pi, si, ti) = (i16::from(p), i16::from(s), i16::from(t));
        let floor = match r.q {
            2 => si,
            3 => pi,
            4 => pi - ti,
            5 => pi - si - ti,
            _ => pi - i16::from(r.e[3]) - si - ti,
        };
        let nb = c.lbx[1] - c.wl - r.lc;
        let spare = goal as i16 - i16::from(r.l);
        let n = if with_bound() { i16::from(nb).max(floor) } else { 0 };
        let adm = p <= 1 && pi + si + ti <= 5 && pi + si + ti + n <= spare;
        let pairs = crate::annot::pairs_after_insertion(y, &w, &r).0;
        map.insert(*k, SvCls { q: r.q, l: r.l, p, s, t, nb, floor, adm, total: c.total, route: r.route, pairs, fin: false });
        if c.total as usize <= goal {
            let mut full = wvec(&c.tw, c.tl);
            full.extend(crate::crisp::ls_finish(md, c.tz));
            sols.push(full);
        }
    }
    pairs_step(&mut map);
    (map, sols)
}

/// The most-pairs step, with `SVM_PAIRS=drop`: the less-paired classes are not finished.  Without it nothing is
/// dropped (the pairs only order the variants), as in the Python scripts.
fn pairs_step(map: &mut HashMap<u64, SvCls>) {
    let mut top: HashMap<(u64, u8, u8, u8, u8), u8> = HashMap::new();
    for c in map.values().filter(|c| c.adm) {
        let e = top.entry((c.route, c.p, c.s, c.t, c.nb)).or_insert(0);
        *e = (*e).max(c.pairs);
    }
    let drop = std::env::var("SVM_PAIRS").is_ok_and(|v| v == "drop");
    for c in map.values_mut() {
        c.fin = c.adm && (!drop || c.pairs == top[&(c.route, c.p, c.s, c.t, c.nb)]);
    }
}

/// The premove pass on one side (`tuple::rest_side`): the left-over units by the class of their path, with P <= 1
/// and P+S+T <= 5 (and the bound with `SVM_STD_BOUND=1`) applied to the left-over skeleton's reading (L counts the
/// premove; no step 4 in any case, since only one side of what is left is searched), and the within-goal solutions, written on this side with the premove's
/// turn at the end.  A skeleton that starts and ends with a quarter turn gets the pass on both sides; with
/// `SVM_REST_BOTH=0` on inverse only (on normal a left-over skeleton that starts with a quarter turn is left out).
fn pass_side(cx: &Ctx, sec: &Sec, y: &St, m: usize, goal: usize, side: u8) -> (HashMap<u64, SvCls>, Vec<Vec<usize>>) {
    let mut map = HashMap::new();
    let mut sols = Vec::new();
    // (SVM_REST_BOTH=0; by default that skeleton gets the pass on both sides, as in the Python scripts)
    let both = !std::env::var("SVM_REST_BOTH").is_ok_and(|v| v == "0");
    for u in crate::tuple::rest_side(cx, sec, y, m, side, 0, true) {
        let o = &u.out;
        if side == 0 && o.shape & 7 == 0 && !both {
            continue;
        }
        let q = o.q as usize;
        let (s, t) = (o.e[q - 2], o.e[q - 1]);
        let p: u8 = o.e[..q - 2].iter().sum();
        let pst = i16::from(p) + i16::from(s) + i16::from(t);
        let nb = o.nb[1];
        let n = if with_bound() { i16::from(nb) } else { 0 };
        let adm = p <= 1 && pst <= 5 && pst + n <= goal as i16 - i16::from(o.l);
        map.insert(u.key, SvCls { q: o.q, l: o.l, p, s, t, nb, floor: -99, adm, total: o.total, route: o.route, pairs: o.pairs, fin: false });
        sols.extend(u.sol);
    }
    pairs_step(&mut map);
    (map, sols)
}

fn show_sv(c: Option<&SvCls>) -> String {
    match c {
        None => "-".to_string(),
        Some(c) => format!("{},{},{},{},{},{},{},{},{},{},{}", c.q, c.l, c.p, c.s, c.t, c.nb, c.floor, u8::from(c.adm), c.total, c.pairs, u8::from(c.fin)),
    }
}

fn show_read(sec: &Sec, w: &[usize]) -> String {
    let (l, ex) = read_solution(sec, w);
    format!("{l}:{}", ex.iter().map(u8::to_string).collect::<Vec<_>>().join(","))
}

/// One DR: a D line, and an S line for every within-goal solution either meta has in sight.
pub fn one(cx: &Ctx, sec: &Sec, x: &St, dr: u32, extra: bool) -> String {
    let md = cx.md;
    let m = qt_count(md, x);
    let goal = goal_of(m);
    let qmax = (m + 2).min(6);
    let xi = x.inv();
    let solved = |w: &[usize]| md.hg.get(&x.mul(word(w))).is_some_and(|i| md.fin[i as usize] == 0);
    let mut cand: Vec<Vec<usize>> = Vec::new();

    // the skeleton/variant meta
    let (svn, sn) = sv_side(cx, sec, x, goal, qmax);
    let (svi, si) = sv_side(cx, sec, &xi, goal, qmax);
    cand.extend(sn.iter().map(|w| canon(w)));
    cand.extend(si.iter().map(|w| canon(&inv_word(w))));
    // ... and its premove pass (SVM_UNISS: `add`, the default, or `0` for none)
    let pass = match std::env::var("SVM_UNISS").as_deref() {
        Err(_) | Ok("add") => true,
        Ok("0") => false,
        Ok(v) => fatal!("SVM_UNISS={v}: the comparison has the premove pass on top of the full search (add) or not at all (0)"),
    };
    let (rn, rsn) = if pass { pass_side(cx, sec, x, m, goal, 0) } else { (HashMap::new(), Vec::new()) };
    let (ri, rsi) = if pass { pass_side(cx, sec, &xi, m, goal, 1) } else { (HashMap::new(), Vec::new()) };
    cand.extend(rsn.iter().map(|w| canon(w)));
    cand.extend(rsi.iter().map(|w| canon(&inv_word(w))));
    let (mut nadm, mut nadm_ok, mut svbest) = (0u32, 0u32, 255u8);
    for c in svn.values().chain(svi.values()).chain(rn.values()).chain(ri.values()) {
        if c.fin {
            nadm += 1;
            if c.total as usize <= goal {
                nadm_ok += 1;
                svbest = svbest.min(c.total);
            }
        }
    }

    // the standard meta: (view, start, class of the path on the last side) -> fewest moves to HTR.
    // view 0 normal, 1 inverse, 2 a start on normal and the rest on inverse, 3 a start on inverse and the rest on normal
    let st = starts(extra);
    let mut smap: HashMap<(u8, u16, u64), u8> = HashMap::new();
    // best total within each cap, by the moves before the NISS (0 = no NISS, 4 = the extra starts)
    let mut best = [[255u8; CAPMAX + 1]; 5];
    let lso = md.lsopt(x) as usize;
    for view in 0u8..4 {
        let list: Vec<(u16, u8, Vec<usize>)> = if view < 2 { vec![(0, 0, vec![])] } else { st.iter().enumerate().map(|(i, (l, a))| (i as u16 + 1, *l, a.clone())).collect() };
        for (aid, lev, a) in list {
            let base = if view == 0 || view == 2 { *x } else { xi };
            let y = if view < 2 { base } else { base.mul(word(&a)).inv() };
            let al = a.len();
            arrivals(md, &y, goal - al, CAPMAX - al, &mut |w: &[usize], zi: u32| {
                let moves = (al + w.len()) as u8;
                let total = moves + md.fin[zi as usize];
                assert!(total as usize >= lso && total as usize <= goal);
                for b in &mut best[lev as usize][moves as usize..] {
                    *b = (*b).min(total);
                }
                if lev > PRE as u8 {
                    return;
                }
                let e = smap.entry((view, aid, cx.im.key(w, true))).or_insert(255);
                *e = (*e).min(moves);
                // the solution, on normal
                let mut part = w.to_vec();
                part.extend(crate::crisp::ls_finish(md, zi));
                let sol = match view {
                    0 => part,
                    1 => inv_word(&part),
                    2 => {
                        let mut s = a.clone();
                        s.extend(inv_word(&part));
                        s
                    }
                    _ => {
                        part.extend(inv_word(&a));
                        part
                    }
                };
                cand.push(canon(&sol));
            });
        }
    }

    // every solution once
    let mut seen: HashMap<Vec<u32>, usize> = HashMap::new();
    let mut sols: Vec<Vec<usize>> = Vec::new();
    for w in cand {
        assert!(solved(&w), "not a solution: {}", wname(&w));
        assert!(w.len() <= goal);
        let k = solkey(cx, &w);
        match seen.get(&k) {
            Some(&i) => {
                if (w.len(), &w) < (sols[i].len(), &sols[i]) {
                    sols[i] = w;
                }
            }
            None => {
                seen.insert(k, sols.len());
                sols.push(w);
            }
        }
    }
    sols.sort();

    let mut lines = String::new();
    let mut nsv = 0u32;
    let mut nstd = [0u32; CAPMAX + 1];
    for w in &sols {
        let wi = inv_word(w);
        let (pn, pi) = (&w[..=last_qt(w).unwrap()], &wi[..=last_qt(&wi).unwrap()]);
        let (cn, ci) = (svn.get(&cx.im.key(pn, true)), svi.get(&cx.im.key(pi, true)));
        // the premove pass has the solution on a side where it ends with a quarter turn: that turn is the premove,
        // and the HTR is at the last quarter turn before it
        let unit = |ww: &[usize], map: &'_ HashMap<u64, SvCls>| -> Option<u64> {
            let n = ww.len();
            if map.is_empty() || n < 2 || !is_qt(ww[n - 1]) {
                return None;
            }
            last_qt(&ww[..n - 1]).map(|j| cx.im.key(&ww[..=j], true))
        };
        let (dn, di) = (unit(w, &rn).and_then(|k| rn.get(&k)), unit(&wi, &ri).and_then(|k| ri.get(&k)));
        let sv = cn.is_some_and(|c| c.fin) || ci.is_some_and(|c| c.fin) || dn.is_some_and(|c| c.fin) || di.is_some_and(|c| c.fin);
        nsv += u32::from(sv);
        // standard: moves to HTR on normal, on inverse, then with a NISS after 1, 2, 3 moves on normal and after
        // 1, 2, 3 moves on inverse (255 = no such way within CAPMAX)
        let mut mv = [255u8; 2 + 2 * PRE];
        for (v, p) in [(0usize, pn), (1, pi)] {
            if let Some(&a) = smap.get(&(v as u8, 0, cx.im.key(p, true))) {
                mv[v] = a;
            }
        }
        let mut nisstxt = vec![String::from("-"); 2 * PRE];
        for (dir, ww) in [(0usize, w), (1, &wi)] {
            for (a, rest) in niss_splits(ww) {
                let Some(aid) = st.iter().position(|s| s.1 == a) else { continue };
                let b = inv_word(&rest);
                let Some(j) = last_qt(&b) else { continue };
                if let Some(&mm) = smap.get(&(2 + dir as u8, aid as u16 + 1, cx.im.key(&b[..=j], true))) {
                    let slot = dir * PRE + st[aid].0 as usize - 1;
                    if mm < mv[2 + slot] {
                        mv[2 + slot] = mm;
                        nisstxt[slot] = format!("{};{};{};{}", wname(&a), wname(&b[..=j]), wname(&b[j + 1..]), a.len() + j + 1);
                    }
                }
            }
        }
        let all = *mv.iter().min().unwrap();
        for cap in CAPS {
            nstd[cap] += u32::from(all as usize <= cap);
        }
        lines += &format!(
            "S\t{dr}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n",
            w.len(),
            u8::from(sv),
            show_sv(cn),
            show_sv(ci),
            show_read(sec, w),
            show_read(sec, &wi),
            mv.iter().map(|&v| if v == 255 { "-".to_string() } else { v.to_string() }).collect::<Vec<_>>().join(","),
            pn.len(),
            pi.len(),
            nisstxt.join("\t"),
            w.iter().filter(|&&mm| is_qt(mm)).count(),
            wname(w),
            show_sv(dn),
            show_sv(di),
        );
    }
    // best total within each cap with a NISS after at most 0, 1, 2, 3 moves, and with the extra starts on top
    for l in 1..5 {
        for cap in 0..=CAPMAX {
            best[l][cap] = best[l][cap].min(best[l - 1][cap]);
        }
    }
    let fmt = |a: &[u8]| a[7..=CAPMAX].iter().map(|&v| if v == 255 { "-".to_string() } else { v.to_string() }).collect::<Vec<_>>().join(",");
    let head = format!(
        "D\t{dr}\t{m}\t{goal}\t{lso}\t{nadm}\t{nadm_ok}\t{}\t{}\t{}\t{nsv}\t{}\n",
        if svbest == 255 { "-".to_string() } else { svbest.to_string() },
        best.iter().map(|b| fmt(b)).collect::<Vec<_>>().join("\t"),
        sols.len(),
        nstd[7..].iter().map(u32::to_string).collect::<Vec<_>>().join(","),
    );
    head + &lines
}

/// drvar metastd N SEED M RULEFILE OUT : the DRs of `metatuple N SEED M`; for each, what the standard meta and
/// the skeleton/variant meta reach.
pub fn run(md: &Model, n: usize, seed: u64, mwant: usize, rulefile: &str, out: &str) {
    use rayon::prelude::*;
    use std::io::Write;
    let mut cx = Ctx::new(md);
    load_rules(&mut cx, rulefile);
    let sec = Sec::new();
    let mut rng = crate::Rng(seed);
    let mut xs = Vec::new();
    while xs.len() < n {
        let x = crate::random_dr(md, &mut rng);
        if qt_count(md, &x) == mwant {
            xs.push(x);
        }
    }
    let mut f = std::io::BufWriter::new(std::fs::File::create(out).unwrap());
    let extra = std::env::var("STD_EXTRA").is_ok();
    writeln!(f, "# D: dr m goal optimal_leave_slice sv_classes_finished sv_within_goal sv_best std_best_by_cap(7..{CAPMAX})_without_niss the_same_with_a_niss_after_at_most_1_move at_most_2 at_most_3 with_the_extra_starts_too solutions sv_solutions std_solutions_by_cap").unwrap();
    writeln!(f, "# S: dr length sv_reaches sv_class_normal(q,L,P,S,T,N_bound,floor,passes_the_rule,total,pairs,finished) sv_class_inverse own_reading_normal(L:sections) own_reading_inverse std_moves_to_htr(normal,inverse,niss_after_1_2_3_moves_on_normal,niss_after_1_2_3_moves_on_inverse) path_normal path_inverse niss_after_1_on_normal(start;other side;finish there;moves) after_2_on_normal after_3_on_normal after_1_on_inverse after_2_on_inverse after_3_on_inverse quarter_turns solution premove_pass_class_normal(as sv_class; L and total count the premove, floor -99 = no step 4) premove_pass_class_inverse").unwrap();
    let t0 = std::time::Instant::now();
    for (b, chunk) in xs.chunks(64).enumerate() {
        let res: Vec<String> = chunk.par_iter().enumerate().map(|(i, x)| one(&cx, &sec, x, (b * 64 + i) as u32, extra)).collect();
        for r in res {
            f.write_all(r.as_bytes()).unwrap();
        }
        eprintln!("{} / {n}  {:.0}s", (b * 64 + chunk.len()).min(n), t0.elapsed().as_secs_f64());
    }
}

/// drvar metastd1 RULEFILE "SCRAMBLE" [M] : the same for one DR, to the terminal.
pub fn explain(md: &Model, rulefile: &str, scr: &str) {
    let mut cx = Ctx::new(md);
    load_rules(&mut cx, rulefile);
    let sec = Sec::new();
    let x = word(&crate::core::parse_moves(scr.as_bytes(), 64).unwrap_or_else(|| fatal!("not DR moves")));
    print!("{}", one(&cx, &sec, &x, 0, std::env::var("STD_EXTRA").is_ok()));
}

/// drvar metaway < lines of "SCRAMBLE<tab>N|I<tab>START<tab>PATH" : one way of the standard meta per line, START on
/// that side and PATH on the other (START "-": no NISS, PATH on that side).  For each: does it come through an HTR
/// (up to a turn of both layers) before its end, does it end on an HTR, and how long that HTR's finish is.
pub fn way(md: &Model) {
    use std::io::BufRead;
    let parse = |t: &str| crate::core::parse_moves(t.as_bytes(), 64).unwrap_or_else(|| fatal!("not DR moves: {t}"));
    for line in std::io::stdin().lock().lines() {
        let line = line.unwrap();
        let f: Vec<&str> = line.split('\t').collect();
        if f.len() != 4 {
            fatal!("want SCRAMBLE, N or I, START, PATH: {line}");
        }
        let x = word(&parse(f[0]));
        let base = if f[1] == "I" { x.inv() } else { x };
        let y = if f[2] == "-" { base } else { base.mul(word(&parse(f[2]))).inv() };
        let w = parse(f[3]);
        let hit = md.hg.get(&y.mul(word(&w)));
        println!("{}\t{}\t{}", u8::from(passes_htr(md, &y, &w)), u8::from(hit.is_some()), hit.map_or("-".to_string(), |i| md.fin[i as usize].to_string()));
    }
}

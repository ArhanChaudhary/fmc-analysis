//! Routes of finishes: every finish of length <= budget of one DR state, every NISS reading of each, and the
//! chain of labels the reading passes (one label at the start and one after each quarter turn).
//!
//! Notation: X = the DR state, S = a finish (X·S = solved), n = |S|, P_i = X·S[0..i] (normal-side states),
//! seg(a, b) = the permutation of the moves S[a..b] alone.  For a split k:
//!
//! * normal first: A = S[0..k] on normal, then B = inverse of S[k..n] on inverse.  Normal states P_i (i <= k);
//!   inverse-side states (X·A)^-1·B_j = seg(k, n-j).
//! * inverse first: B on inverse first (states X^-1·B_j = seg(0, n-j)), then A on normal
//!   (states seg(i, k)^-1).
//!
//! Two keys per reading:
//! * `F` (full chain): labels at every quarter turn of the whole finish, switch marked.
//! * `H` (route to HTR): labels up to the first state in HTR, switch marked if it happens before, plus one flag:
//!   does the rest of the finish (the post-HTR part, which for a NISS reading is the middle segment S[k..n-j])
//!   contain a quarter turn (an HTR-breaking finish)?
//!
//! Labels only change at quarter turns and are unchanged by half turns on either side, so only splits at a
//! gap boundary are read (k right after a quarter turn for normal first, k at a quarter turn for inverse first);
//! these also give the shortest HTR of that route in that finish.

use crate::model::{axis_run, canonical_next, is_qt, label_name, Model, FACE};
use crate::core::NMOVES;
use std::collections::HashMap;

pub const SW: u8 = 0xFE;

#[derive(Clone, Copy, PartialEq, Eq, Hash, Debug)]
pub struct Key {
    pub len: u8,
    pub b: [u8; 31],
}
impl Key {
    fn new(kind: u8) -> Key {
        let mut k = Key { len: 1, b: [0; 31] };
        k.b[0] = kind;
        k
    }
    #[inline]
    fn push(&mut self, x: u8) {
        self.b[self.len as usize] = x;
        self.len += 1;
    }
    pub fn bytes(&self) -> &[u8] {
        &self.b[..self.len as usize]
    }
    /// "H:4b2 4e > 4a1 4e > (0c0 0e)" ; an H key ends with " | ht" (post-HTR in half turns) or " | qt"
    pub fn to_string(&self) -> String {
        let b = self.bytes();
        let kind = b[0] as char;
        let body = if kind == 'H' { &b[1..b.len() - 1] } else { &b[1..] };
        let mut parts: Vec<String> = Vec::new();
        let mut sw = false;
        for &x in body {
            if x == SW {
                sw = true;
                continue;
            }
            let mut s = label_name(x);
            if sw && !parts.iter().any(|p| p.starts_with('(')) {
                s = format!("({}", s);
            }
            parts.push(s);
        }
        let mut out = parts.join(" > ");
        if sw {
            out.push(')');
        }
        if kind == 'H' {
            out.push_str(if b[b.len() - 1] == 1 { " | qt" } else { " | ht" });
        }
        format!("{}:{}", kind, out)
    }
}

/// One reading of one finish.
#[derive(Clone, Debug)]
pub struct Reading {
    pub inverse_first: bool,
    pub k: usize,
    pub h: Key,
    pub f: Key,
    pub htr_len: u8,
    pub linear: bool,
}

/// Every reading of the finish `moves` of the state with corner/edge coordinates `p[0]`; `p[i]` = after i moves.
pub fn readings(m: &Model, moves: &[u8], p: &[(usize, usize)], out: &mut Vec<Reading>) {
    readings_k(m, moves, p, out, false)
}

/// Readings at every split k that has a quarter turn on both sides (not only at gap boundaries): used to pair a
/// normal-first reading with the inverse-first reading of the same split (mirror aliases, same (A, B) pair).
pub fn readings_all(m: &Model, moves: &[u8], p: &[(usize, usize)], out: &mut Vec<Reading>) {
    readings_k(m, moves, p, out, true)
}

fn readings_k(m: &Model, moves: &[u8], p: &[(usize, usize)], out: &mut Vec<Reading>, all_k: bool) {
    out.clear();
    let n = moves.len();
    let (cx, ex) = p[0];
    // seg[a][b]
    let mut seg = [[(0usize, 0usize); 21]; 21];
    for a in 0..=n {
        let (mut c, mut e) = (0usize, 0usize);
        for b in a..n {
            c = m.core.cmove[moves[b] as usize][c] as usize;
            e = m.core.emove[moves[b] as usize][e] as usize;
            seg[a][b + 1] = (c, e);
        }
    }
    let mut qp = [0usize; 21];
    for i in 0..n {
        qp[i + 1] = qp[i] + is_qt(moves[i]) as usize;
    }
    let anyqt = |a: usize, b: usize| qp[b] > qp[a];
    let x_lab = m.label(cx, ex);
    let x_lab_inv = m.label_inv(cx, ex);
    let x_in_h = m.in_h(cx, ex);

    // normal first
    for k in 1..=n.max(1) {
        let k = k.min(n);
        let ok = k == n || ((all_k || is_qt(moves[k - 1])) && qp[k] > 0 && qp[n] - qp[k] > 0);
        if !ok {
            continue;
        }
        let (mut f, mut h) = (Key::new(b'F'), Key::new(b'H'));
        let mut done: Option<(usize, usize, usize)> = None; // (htr length, post segment a..b)
        f.push(x_lab);
        h.push(x_lab);
        if x_in_h {
            done = Some((0, 0, n));
        }
        for i in 1..=k {
            if is_qt(moves[i - 1]) {
                let (c, e) = p[i];
                let l = m.label(c, e);
                f.push(l);
                if done.is_none() {
                    h.push(l);
                    if m.in_h(c, e) {
                        done = Some((i, i, n));
                    }
                }
            }
        }
        if k < n {
            f.push(SW);
            if done.is_none() {
                h.push(SW);
            }
            for j in 1..=n - k {
                if is_qt(moves[n - j]) {
                    let (c, e) = seg[k][n - j];
                    let l = m.label(c, e);
                    f.push(l);
                    if done.is_none() {
                        h.push(l);
                        if m.in_h(c, e) {
                            done = Some((k + j, k, n - j));
                        }
                    }
                }
            }
        }
        let (hl, pa, pb) = done.expect("a finish ends in HTR");
        h.push(anyqt(pa, pb) as u8);
        out.push(Reading { inverse_first: false, k, h, f, htr_len: hl as u8, linear: k == n });
        if n == 0 {
            break;
        }
    }
    // inverse first
    for k in 0..n {
        let ok = k == 0 || ((all_k || is_qt(moves[k])) && qp[k] > 0 && qp[n] - qp[k] > 0);
        if !ok {
            continue;
        }
        let (mut f, mut h) = (Key::new(b'F'), Key::new(b'H'));
        let mut done: Option<(usize, usize, usize)> = None;
        f.push(x_lab_inv);
        h.push(x_lab_inv);
        if x_in_h {
            done = Some((0, 0, n));
        }
        for j in 1..=n - k {
            if is_qt(moves[n - j]) {
                let (c, e) = seg[0][n - j];
                let l = m.label(c, e);
                f.push(l);
                if done.is_none() {
                    h.push(l);
                    if m.in_h(c, e) {
                        done = Some((j, 0, n - j));
                    }
                }
            }
        }
        if k > 0 {
            f.push(SW);
            if done.is_none() {
                h.push(SW);
            }
            for i in 1..=k {
                if is_qt(moves[i - 1]) {
                    let (c, e) = seg[i][k];
                    let l = m.label_inv(c, e);
                    f.push(l);
                    if done.is_none() {
                        h.push(l);
                        if m.in_h(c, e) {
                            done = Some(((n - k) + i, i, k));
                        }
                    }
                }
            }
        }
        let (hl, pa, pb) = done.expect("a finish ends in HTR");
        h.push(anyqt(pa, pb) as u8);
        out.push(Reading { inverse_first: true, k, h, f, htr_len: hl as u8, linear: k == 0 });
    }
    // the H key of a NISS reading that reached HTR before its switch is a linear key; mark those linear too
    for r in out.iter_mut() {
        if !r.linear && !r.h.bytes().contains(&SW) {
            r.linear = true;
        }
    }
}

/// Enumerate every canonical finish of `x` of length <= budget (none can be shorter than the optimum).
/// `cb(moves, states)` gets the moves and the corner/edge coordinates after each prefix.  Stops after `cap`
/// finishes and returns false in that case.
pub fn finishes(
    m: &Model,
    x: (usize, usize, usize),
    budget: usize,
    cap: u64,
    cb: &mut dyn FnMut(&[u8], &[(usize, usize)]),
) -> bool {
    let mut moves = Vec::with_capacity(24);
    let mut path = Vec::with_capacity(24);
    path.push((x.0, x.1));
    let mut count = 0u64;
    rec(m, x, budget, &mut moves, &mut path, 0xFF, 0xFF, &mut count, cap, cb);
    count <= cap
}

#[allow(clippy::too_many_arguments)]
fn rec(
    m: &Model,
    st: (usize, usize, usize),
    budget: usize,
    moves: &mut Vec<u8>,
    path: &mut Vec<(usize, usize)>,
    lf: u8,
    la: u8,
    count: &mut u64,
    cap: u64,
    cb: &mut dyn FnMut(&[u8], &[(usize, usize)]),
) {
    if *count > cap {
        return;
    }
    if st == (0, 0, 0) {
        *count += 1;
        if *count <= cap {
            cb(moves, path);
        }
        return;
    }
    let r = budget - moves.len();
    if r == 0 {
        return;
    }
    for mv in 0..NMOVES {
        if !canonical_next(mv, lf, la) {
            continue;
        }
        let st2 = m.mv(mv, st);
        if m.depth(st2.0, st2.1, st2.2) as usize + 1 > r {
            continue;
        }
        moves.push(mv as u8);
        path.push((st2.0, st2.1));
        rec(m, st2, budget, moves, path, FACE[mv], axis_run(mv, lf, la), count, cap, cb);
        moves.pop();
        path.pop();
    }
}

/// Leave-slice finishes (corners and U/D edges solved, slice ignored) of optimal length: (count, min qts, max qts).
pub fn ls_optimal(m: &Model, c: usize, e: usize, cap: u64) -> (u8, u64, u8, u8) {
    let d = m.lsdepth(c, e);
    let mut cnt = 0u64;
    let (mut qmin, mut qmax) = (99u8, 0u8);
    fn rec2(m: &Model, c: usize, e: usize, r: usize, q: u8, lf: u8, la: u8, cnt: &mut u64, cap: u64, qmin: &mut u8, qmax: &mut u8) {
        if *cnt > cap {
            return;
        }
        if c == 0 && e == 0 {
            *cnt += 1;
            *qmin = (*qmin).min(q);
            *qmax = (*qmax).max(q);
            return;
        }
        if r == 0 {
            return;
        }
        for mv in 0..NMOVES {
            if !canonical_next(mv, lf, la) {
                continue;
            }
            let (c2, e2) = (m.core.cmove[mv][c] as usize, m.core.emove[mv][e] as usize);
            if m.lsdepth(c2, e2) as usize + 1 > r {
                continue;
            }
            rec2(m, c2, e2, r - 1, q + is_qt(mv as u8) as u8, FACE[mv], axis_run(mv, lf, la), cnt, cap, qmin, qmax);
        }
    }
    rec2(m, c, e, d as usize, 0, 0xFF, 0xFF, &mut cnt, cap, &mut qmin, &mut qmax);
    (d, cnt, qmin, qmax)
}

/// Everything kept about one start state.
#[derive(Default, Clone)]
pub struct StateAgg {
    pub d: u8,
    pub nopt: u64,
    pub nopt_canon: u64,
    pub n1: u64,
    pub capped: bool,
    pub qmin: u8,
    pub qmax: u8,
    pub q1min: u8,
    pub best_lin_n: u8,
    pub best_lin_i: u8,
    pub best_any: u8,
    pub best_any1: u8,
    pub mask_lin: u32,
    pub mask_any: u32,
    pub ht_first_n: u8,
    pub ht_first_i: u8,
    /// route key -> (shortest finish length that follows it (<= d + 1), shortest HTR among those readings)
    pub routes: HashMap<Key, (u8, u8, u8)>,
    /// (normal-first H key, inverse-first H key) of the same split of an optimal finish (mirror aliases)
    pub aliases: std::collections::HashSet<(Key, Key)>,
}

/// finishes in which every pair of commuting opposite-face moves is written in one fixed order (U before D, ...)
fn canonical_order(moves: &[u8]) -> bool {
    moves.windows(2).all(|w| {
        let (a, b) = (FACE[w[0] as usize], FACE[w[1] as usize]);
        !(a / 2 == b / 2 && a > b)
    })
}

pub fn analyse(m: &Model, x: (usize, usize, usize), extra: usize, cap: u64, want_routes: bool) -> StateAgg {
    let d = m.depth(x.0, x.1, x.2);
    let mut agg = StateAgg {
        d,
        qmin: 99,
        q1min: 99,
        best_lin_n: 99,
        best_lin_i: 99,
        best_any: 99,
        best_any1: 99,
        ht_first_n: 99,
        ht_first_i: 99,
        ..Default::default()
    };
    let mut rd = Vec::with_capacity(48);
    let ok = finishes(m, x, d as usize + extra, cap, &mut |moves, path| {
        let n = moves.len() as u8;
        let nq = moves.iter().filter(|&&mv| is_qt(mv)).count() as u8;
        let opt = n == d;
        if opt {
            agg.nopt += 1;
            agg.nopt_canon += canonical_order(moves) as u64;
            agg.qmin = agg.qmin.min(nq);
            agg.qmax = agg.qmax.max(nq);
            let first = moves.iter().position(|&mv| is_qt(mv)).unwrap_or(moves.len()) as u8;
            let last = moves.iter().rev().position(|&mv| is_qt(mv)).unwrap_or(moves.len()) as u8;
            agg.ht_first_n = agg.ht_first_n.min(first);
            agg.ht_first_i = agg.ht_first_i.min(last);
        } else {
            agg.n1 += 1;
        }
        agg.q1min = agg.q1min.min(nq);
        readings(m, moves, path, &mut rd);
        for r in &rd {
            if opt {
                agg.mask_any |= 1 << r.htr_len;
                agg.best_any = agg.best_any.min(r.htr_len);
                if r.linear {
                    agg.mask_lin |= 1 << r.htr_len;
                }
                if !r.inverse_first && r.k == moves.len() {
                    agg.best_lin_n = agg.best_lin_n.min(r.htr_len);
                }
                if r.inverse_first && r.k == 0 {
                    agg.best_lin_i = agg.best_lin_i.min(r.htr_len);
                }
            }
            agg.best_any1 = agg.best_any1.min(r.htr_len);
            if want_routes {
                for key in [r.h, r.f] {
                    // (shortest finish length, shortest HTR among finishes of that length, shortest HTR over every
                    // finish within the budget)
                    let v = agg.routes.entry(key).or_insert((n, r.htr_len, r.htr_len));
                    if n < v.0 {
                        v.0 = n;
                        v.1 = r.htr_len;
                    } else if n == v.0 && r.htr_len < v.1 {
                        v.1 = r.htr_len;
                    }
                    v.2 = v.2.min(r.htr_len);
                }
            }
        }
        if want_routes && opt {
            readings_all(m, moves, path, &mut rd);
            for a in rd.iter().filter(|r| !r.inverse_first && r.k > 0 && r.k < moves.len()) {
                if let Some(b) = rd.iter().find(|r| r.inverse_first && r.k == a.k) {
                    if a.h != b.h {
                        agg.aliases.insert((a.h, b.h));
                    }
                }
            }
        }
    });
    agg.capped = !ok;
    agg
}

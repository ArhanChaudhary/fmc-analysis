//! Per-DR analysis: families (skeletons), variants, the family optimum, and the one-insertion test.
//!
//! * A *path* P is a canonical DR move sequence that ends with a quarter turn and lands in HTR: x·P ∈ H.
//!   Its *finish* is the best half-turn finish of z = x·P, so the solution through P has |P| + d3(z) moves.
//!   Every DR finish is one of these (cut it after its last quarter turn).
//! * The *family* of P is (m, k): its number of quarter turns and the NISS@1qt corner kind of z.  This is
//!   the doc's skeleton: "all variants have the same NISS@1qt corner case", and they keep the skeleton's
//!   quarter turns.  The skeleton length L_pre(m, k) is the shortest corner-only path with m quarter turns
//!   that puts the corners in HTR with kind k; S + T of P is |P| - L_pre(m, k).
//! * P has *zero bad slices* if z's case does (Rodney's sheet: must-have / must-avoid by axis).
//! * One insertion: P's word is A · s · B where s is the half-turn section between two quarter turns (or before
//!   the first), split as s = u · w.  Insert a block j with corner action in J_c between u and w
//!   (slices, corner swaps, pure edge permutations, or a mix), let it cancel, and turn any later quarter turn
//!   the other way.  The result is checked against every optimal path of the target set: W = A·u·j·w·B'
//!   must equal that path as a cube state and be no longer once cancelled.
use crate::core::St;
use crate::model::*;

pub struct PathRec {
    pub w: Vec<usize>,
    pub m: u8,
    pub kind: u8,
    pub case: u8,
    pub z: u32,
    pub best: u8,
}

/// L_pre[m][kind]: fewest moves of a corner-only path with exactly m quarter turns ending in a quarter turn
/// that leaves the corners in HTR with this kind (255 = none within the search).
pub fn skeleton_lengths(md: &Model, x: &St, mmax: usize) -> Vec<[u8; 6]> {
    let nq = mmax + 1;
    let idx = |c: usize, q: usize, lf: usize, lq: usize| ((c * nq + q) * 7 + lf) * 2 + lq;
    let mut dist = vec![255u8; 40320 * nq * 14];
    let mut out = vec![[255u8; 6]; nq];
    let c0 = crate::core::rank_perm(&x.c);
    let mut cur = vec![(c0 as u32, 0u8, 6u8, 0u8)];
    dist[idx(c0, 0, 6, 0)] = 0;
    let mut d = 0u8;
    while !cur.is_empty() && d < 20 {
        let mut nxt = Vec::new();
        for &(c, q, lf, lq) in &cur {
            if lq == 1 {
                let k = md.ckind[c as usize];
                if k != 255 && out[q as usize][k as usize] == 255 {
                    out[q as usize][k as usize] = d;
                }
            }
            for mv in 0..10 {
                if !allowed(lf as usize, mv) {
                    continue;
                }
                let q2 = q as usize + is_qt(mv) as usize;
                if q2 > mmax {
                    continue;
                }
                let c2 = md.core.cmove[mv][c as usize] as usize;
                let i = idx(c2, q2, FACE[mv], is_qt(mv) as usize);
                if dist[i] == 255 {
                    dist[i] = d + 1;
                    nxt.push((c2 as u32, q2 as u8, FACE[mv] as u8, is_qt(mv) as u8));
                }
            }
        }
        cur = nxt;
        d += 1;
    }
    out
}

/// All paths from x with at most `qmax` quarter turns whose length satisfies `keep`, found by a depth-first
/// search pruned with `lb` (a lower bound on the moves still needed to land in HTR / to finish).
pub fn paths<FL, FK>(md: &Model, x: &St, cap: usize, qmax: usize, lb: FL, keep: FK) -> Vec<PathRec>
where
    FL: Fn(&St, usize, usize) -> usize, // (state, length so far, quarter turns so far) -> lower bound
    FK: Fn(usize, u8, u8, u8) -> bool, // (length, m, kind, best) -> record?
{
    let mut out = Vec::new();
    let mut w = Vec::with_capacity(24);
    #[allow(clippy::too_many_arguments)]
    fn dfs<FL: Fn(&St, usize, usize) -> usize, FK: Fn(usize, u8, u8, u8) -> bool>(
        md: &Model, s: St, w: &mut Vec<usize>, q: usize, lf: usize, cap: usize, qmax: usize, lb: &FL, keep: &FK,
        out: &mut Vec<PathRec>,
    ) {
        if let Some(&last) = w.last() {
            if is_qt(last) {
                if let Some(zi) = md.hg.get(&s) {
                    let case = md.hcase[zi as usize];
                    let kind = md.cases[case as usize].kind;
                    let best = (w.len() + md.fin[zi as usize] as usize).min(255) as u8;
                    if keep(w.len(), q as u8, kind, best) {
                        out.push(PathRec { w: w.clone(), m: q as u8, kind, case, z: zi, best });
                    }
                }
            }
        }
        if w.len() >= cap {
            return;
        }
        for mv in 0..10 {
            if !allowed(lf, mv) {
                continue;
            }
            let q2 = q + is_qt(mv) as usize;
            if q2 > qmax {
                continue;
            }
            let s2 = s.apply_move(mv);
            if w.len() + 1 + lb(&s2, w.len() + 1, q2) > cap {
                continue;
            }
            w.push(mv);
            dfs(md, s2, w, q2, FACE[mv], cap, qmax, lb, keep, out);
            w.pop();
        }
    }
    dfs(md, *x, &mut w, 0, 6, cap, qmax, &lb, &keep, &mut out);
    out
}

/// The four elements of <U2, D2> as words; they commute with every U or D quarter turn.
const GAUGE: [&[usize]; 4] = [&[], &[1], &[4], &[1, 4]];

/// Result of the one-insertion test of variant V against one target path P.
#[derive(Clone, Copy, Debug)]
pub struct Hit {
    /// section of V that takes the insertion (0 = before the first quarter turn)
    pub sec: u8,
    /// position inside the section (0 = at its start)
    pub pos: u8,
    /// half-turn length of the inserted block (before cancelling)
    pub jlen: u8,
    /// how many of V's later quarter turns are turned the other way
    pub flips: u8,
}

/// Can one of the target paths `ps` (cube state of the path, its length) be written as V with one insertion
/// (and later quarter turns turned around), at no extra length?  Returns the best hit and the target's index.
/// `faces`: also allow a later quarter turn to move to the opposite face (U <-> D).
pub fn one_insertion(md: &Model, v: &[usize], ps: &[(St, usize)], faces: bool) -> Option<(Hit, usize)> {
    let qpos: Vec<usize> = (0..v.len()).filter(|&i| is_qt(v[i])).collect();
    let m = qpos.len();
    let mut best: Option<(Hit, usize)> = None;
    let rank8 = |p: &[u8; 8]| crate::core::rank_perm(p);
    for a in 0..m {
        let s0 = if a == 0 { 0 } else { qpos[a - 1] + 1 };
        let s1 = qpos[a];
        let aw = &v[..s0];
        let sec = &v[s0..s1];
        let tail = &v[s1..];
        let tq: Vec<usize> = (0..tail.len()).filter(|&i| is_qt(tail[i])).collect();
        let alts: [usize; 4] = [0, 2, 3, 5];
        let per = if faces { 4 } else { 2 };
        let total = per_pow(per, tq.len());
        let ainv = word(aw).inv();
        let uinv: Vec<St> = (0..=sec.len()).map(|i| word(&sec[..i]).inv()).collect();
        let winv: Vec<St> = (0..=sec.len()).map(|i| word(&sec[i..]).inv()).collect();
        for code in 0..total {
            let mut b = tail.to_vec();
            let mut c = code;
            let mut flips = 0u8;
            for &i in &tq {
                let pick = c % per;
                c /= per;
                let orig = b[i];
                b[i] = if faces { alts[pick] } else if pick == 0 { orig } else { [2, 1, 0, 5, 4, 3][orig] };
                if b[i] != orig {
                    flips += 1;
                }
            }
            let binv = word(&b).inv();
            for (pi, (pst, plen)) in ps.iter().enumerate() {
                let t = ainv.mul(*pst).mul(binv);
                if !md.hcorner[rank8(&t.c)] {
                    continue;
                }
                // the insertion point and block: j between u and w, with corner action in J_c
                let mut cand: Option<(u8, u8)> = None;
                for i in 0..=sec.len() {
                    let j = uinv[i].mul(t).mul(winv[i]);
                    if !md.jc[rank8(&j.c)] {
                        continue;
                    }
                    let Some(ji) = md.hg.get(&j) else { continue };
                    let jl = md.hg.d3[ji as usize];
                    if cand.map_or(true, |(l, _)| jl < l) {
                        cand = Some((jl, i as u8));
                    }
                }
                let Some((jlen, pos)) = cand else { continue };
                if best.is_some_and(|(o, _)| (jlen, flips) >= (o.jlen, o.flips)) {
                    continue;
                }
                // the shortest the new section can be once it cancels with the quarter turns around it
                let mut wlen = usize::MAX;
                for g1 in GAUGE {
                    let mut ag = aw.to_vec();
                    ag.extend_from_slice(g1);
                    let la = reduce(&ag).len();
                    for g2 in GAUGE {
                        let mid = word(g1).inv().mul(t).mul(word(g2).inv());
                        let Some(mi) = md.hg.get(&mid) else { continue };
                        let mut gb = g2.to_vec();
                        gb.extend_from_slice(&b);
                        wlen = wlen.min(la + md.hg.d3[mi as usize] as usize + reduce(&gb).len());
                    }
                }
                if wlen <= *plen {
                    best = Some((Hit { sec: a as u8, pos, jlen, flips }, pi));
                }
            }
        }
    }
    best
}

fn per_pow(b: usize, e: usize) -> usize { (0..e).fold(1, |a, _| a * b) }

// ---------------------------------------------------------------------------------------------------------
// Skeletons anchored on a corner solution.
//
// A skeleton is a shortest corner-only path of its family (m quarter turns, NISS@1qt corner kind k): a
// canonical DR sequence that ends with a quarter turn and leaves the corners in HTR with that kind (edges
// ignored).  Its insertion points are the positions inside each half-turn section (before the first move,
// between moves, after the last move).  A path P is a *variant* of skeleton s if P is s with, in each
// section, blocks inserted at s's own insertion points whose corner action is in J_c (slices, corner swaps,
// pure edge permutations, mixed in a block), cancelling as they may.  Edges are free (J contains every pure
// edge permutation).  P's quarter turns must sit on the same faces as s's; turning one the other way is a
// U2 (or D2) that has to be paid for by the insertions, which is how the doc's variants flip U to U'.
// Moves of <U2, D2> can be written on either side of a quarter turn, so P's sections are compared up to
// that shift.

/// The 96 HTR corner permutations, numbered.
pub struct HcIndex {
    pub idx: Vec<u8>, // corner coordinate -> 0..95 or 255
}
impl HcIndex {
    pub fn new(md: &Model) -> HcIndex {
        let mut idx = vec![255u8; 40320];
        for (i, &c) in md.cls.hc.iter().enumerate() {
            idx[c] = i as u8;
        }
        HcIndex { idx }
    }
    pub fn of(&self, c: &[u8; 8]) -> u8 { self.idx[crate::core::rank_perm(c)] }
}

fn cmul(a: &[u8; 8], b: &[u8; 8]) -> [u8; 8] {
    // a then b (same rule as St::mul)
    let mut r = [0u8; 8];
    for p in 0..8 {
        r[p] = a[b[p] as usize];
    }
    r
}
fn cinv(a: &[u8; 8]) -> [u8; 8] {
    let mut r = [0u8; 8];
    for p in 0..8 {
        r[a[p] as usize] = p as u8;
    }
    r
}
fn cword(w: &[usize]) -> [u8; 8] { word(w).c }

pub struct Skeleton {
    pub w: Vec<usize>,
    pub m: usize,
    pub kind: u8,
    /// faces of the quarter turns (0 U, 1 D)
    pub qf: Vec<usize>,
    /// corner element of each section before the last quarter turn
    pub sec: Vec<[u8; 8]>,
    /// allowed (section of the variant) * (section of the skeleton)^-1, as a 96-bit set per section
    pub ins: Vec<u128>,
}

/// The corner elements of J_c.
pub fn jc_list(md: &Model) -> Vec<[u8; 8]> {
    let mut v = Vec::new();
    for c in 0..40320 {
        if md.jc[c] {
            v.push(crate::core::unrank_perm::<8>(c));
        }
    }
    v
}

pub fn make_skeleton(md: &Model, hc: &HcIndex, jcl: &[[u8; 8]], w: Vec<usize>, kind: u8) -> Skeleton {
    let qpos: Vec<usize> = (0..w.len()).filter(|&i| is_qt(w[i])).collect();
    let m = qpos.len();
    let mut sec = Vec::new();
    let mut ins = Vec::new();
    let all: Vec<[u8; 8]> = md.cls.hc.iter().map(|&c| crate::core::unrank_perm::<8>(c)).collect();
    for a in 0..m {
        let s0 = if a == 0 { 0 } else { qpos[a - 1] + 1 };
        let sw = &w[s0..qpos[a]];
        sec.push(cword(sw));
        // I = (J at prefix 0)(J at prefix 1)...(J at the full section), as a set
        let mut set: u128 = 1u128 << hc.of(&[0, 1, 2, 3, 4, 5, 6, 7]);
        for i in 0..=sw.len() {
            let u = cword(&sw[..i]);
            let ui = cinv(&u);
            let conj: Vec<[u8; 8]> = jcl.iter().map(|j| cmul(&cmul(&u, j), &ui)).collect();
            let mut next: u128 = 0;
            for (k, el) in all.iter().enumerate() {
                if set >> k & 1 == 1 {
                    for cj in &conj {
                        next |= 1u128 << hc.of(&cmul(el, cj));
                    }
                }
            }
            set = next;
        }
        ins.push(set);
    }
    let qf = qpos.iter().map(|&i| FACE[w[i]]).collect();
    Skeleton { w, m, kind, qf, sec, ins }
}

const GAMMA: [[usize; 2]; 4] = [[99, 99], [1, 99], [4, 99], [1, 4]];
fn gamma(i: usize) -> [u8; 8] {
    let w: Vec<usize> = GAMMA[i].iter().copied().filter(|&m| m != 99).collect();
    cword(&w)
}

/// Is path p (a word) a variant of skeleton s?  A quarter turn of p may sit on the other U/D face than the
/// skeleton's ("you can freely choose between U and D"): that is an E-slice insertion, which turns the corners
/// about the U/D axis, so the rest of p is compared with the skeleton in the turned frame.
pub fn is_variant(hc: &HcIndex, s: &Skeleton, p: &[usize]) -> bool {
    let qpos: Vec<usize> = (0..p.len()).filter(|&i| is_qt(p[i])).collect();
    if qpos.len() != s.m {
        return false;
    }
    let sq: Vec<usize> = (0..s.w.len()).filter(|&i| is_qt(s.w[i])).map(|i| s.w[i]).collect();
    let id8 = [0u8, 1, 2, 3, 4, 5, 6, 7];
    let rots = [id8, cword(&[0, 5]), cword(&[2, 3]), cword(&[1, 4])];
    let gm: Vec<[u8; 8]> = (0..4).map(gamma).collect();
    // sections of p in the skeleton's frame: conj(R_a, e'_a · s'_a) with q'_a = q_a · r_a · e'_a
    let mut secs: Vec<[u8; 8]> = Vec::new();
    let mut rot = id8;
    for a in 0..s.m {
        let s0 = if a == 0 { 0 } else { qpos[a - 1] + 1 };
        let mut el = cword(&p[s0..qpos[a]]);
        if a > 0 {
            let e = cmul(&cinv(&cword(&[sq[a - 1]])), &cword(&[p[qpos[a - 1]]]));
            let mut done = false;
            for r in &rots {
                let ep = cmul(&cinv(r), &e);
                if gm.contains(&ep) {
                    rot = cmul(&rot, r);
                    el = cmul(&ep, &el);
                    done = true;
                    break;
                }
            }
            assert!(done, "quarter-turn difference is not a U/D-axis rotation times <U2, D2>");
        }
        secs.push(cmul(&cmul(&rot, &el), &cinv(&rot)));
    }
    // search the shifts gamma_1..gamma_m in <U2, D2> at each quarter turn
    fn rec(s: &Skeleton, hc: &HcIndex, secs: &[[u8; 8]], gm: &[[u8; 8]], a: usize, left: &[u8; 8]) -> bool {
        if a == s.m {
            return true;
        }
        let base = cmul(left, &secs[a]); // gamma_a^-1 · section
        let sinv = cinv(&s.sec[a]);
        for g in gm {
            let sig = cmul(&base, g); // · gamma_{a+1}
            let d = cmul(&sig, &sinv);
            let k = hc.of(&d);
            if k != 255 && s.ins[a] >> k & 1 == 1 && rec(s, hc, secs, gm, a + 1, &cinv(g)) {
                return true;
            }
        }
        false
    }
    rec(s, hc, &secs, &gm, 0, &id8)
}

/// All shortest corner-only paths of family (m, kind) from x: canonical DR words of length `len`.
pub fn skeletons_of(md: &Model, x: &St, m: usize, kind: usize, len: usize) -> Vec<Vec<usize>> {
    let mut out = Vec::new();
    let mut w = Vec::new();
    #[allow(clippy::too_many_arguments)]
    fn dfs(md: &Model, c: usize, w: &mut Vec<usize>, q: usize, lf: usize, m: usize, kind: usize, len: usize, out: &mut Vec<Vec<usize>>) {
        if w.len() == len {
            if q == m && is_qt(*w.last().unwrap()) && md.ckind[c] == kind as u8 {
                out.push(w.clone());
            }
            return;
        }
        for mv in 0..10 {
            if !allowed(lf, mv) {
                continue;
            }
            let q2 = q + is_qt(mv) as usize;
            if q2 > m {
                continue;
            }
            let c2 = md.core.cmove[mv][c] as usize;
            let r = md.rem[kind][m - q2][c2];
            if r == 255 || w.len() + 1 + r as usize > len {
                continue;
            }
            w.push(mv);
            dfs(md, c2, w, q2, FACE[mv], m, kind, len, out);
            w.pop();
        }
    }
    let c0 = crate::core::rank_perm(&x.c);
    dfs(md, c0, &mut w, 0, 6, m, kind, len, &mut out);
    out
}

//! Search-meta study: how to prune a DR-to-HTR search with the Advanced DR Bounding lower bound.
//!
//! Setting (leave-slice solutions in DR moves, goals 12 / 13 / 14 for 2qt / 3qt / 4qt DRs):
//!
//! * A *variant* is a canonical DR move sequence P that ends with a quarter turn and lands in HTR, on the
//!   normal scramble (state x) or on the inverse scramble (state x^-1).  Checking it means finishing the HTR
//!   state z it lands on: the solution through P has |P| + ls(z) moves, ls = leave-slice half-turn finish.
//! * Its *skeleton* is (side, quarter turns q, NISS@1qt corner kind of z); the skeleton length L is the
//!   shortest corner-only path of that family (`rem[kind][q][corners]`).  *Extra moves* = |P| - L (the doc's
//!   S + T).  For a prefix A with j quarter turns: extra(A) = |A| + rem[kind][q-j][corners after A] - L, so the
//!   extra moves of each section are how much it lengthened the shortest corner route to HTR.
//! * *Corner bound* = |P| + LC[kind] (LC = the kind's own HTR corner moves, 0 / 1 / 2 / 3).
//!   *Rule bound* = corner bound + Rodney Kinney's rule penalty of z's NISS@1qt case (sheet column
//!   "Heuristic").  *Table bound* = corner bound + the smallest half-turn finish over the case's 3,072 states
//!   minus LC (the best any case-level bound can do for DR-move finishes).
//! * *Pairs* = true corner/edge pairs inside the U and D layers (judging-a-dr's `pair_counts`), on the state
//!   and on its inverse.
use crate::core::{rank_perm, St};
use crate::model::*;

/// Tetrad of a corner position / piece: 0 for UFR UBL DFL DBR, 1 for the others.
const TETRAD: [u8; 8] = [0, 1, 0, 1, 1, 0, 1, 0];
/// Side colours of a corner piece: [F/B colour, R/L colour], faces numbered F 0, L 1, B 2, R 3.
const CORNER_COL: [[u8; 2]; 8] = [[0, 3], [0, 1], [2, 1], [2, 3], [0, 3], [0, 1], [2, 1], [2, 3]];
/// Side face of a U/D-layer edge position = side colour of the edge piece with that home.
const EDGE_FACE: [u8; 8] = [0, 1, 2, 3, 0, 1, 2, 3];
/// The 16 touching (corner position, edge position) pairs inside the U and the D layer.
const ADJ: [(usize, usize); 16] = [(0, 0), (0, 3), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 4), (4, 7), (5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 7)];

/// Bit i set = the corner and edge at the touching positions ADJ[i] form a true pair (both stickers match).
pub fn pair_mask(s: &St) -> u16 {
    let mut m = 0u16;
    for (i, &(p, q)) in ADJ.iter().enumerate() {
        let (cpiece, epiece) = (s.c[p] as usize, s.e[q] as usize);
        let face = EDGE_FACE[q];
        let good = TETRAD[cpiece] == TETRAD[p];
        let axis = (face & 1) as usize ^ usize::from(!good);
        if CORNER_COL[cpiece][axis] == EDGE_FACE[epiece] && (cpiece < 4) == (epiece < 4) {
            m |= 1 << i;
        }
    }
    m
}
/// True pairs in the U and D layers (0..=16).
pub fn pairs(s: &St) -> u8 {
    pair_mask(s).count_ones() as u8
}

/// Fewest quarter turns that bring the corners to HTR (the number in the corner subset's name).
pub fn qt_count(md: &Model, x: &St) -> usize {
    let c = rank_perm(&x.c);
    (0..md.rem[0].len()).find(|&r| (0..6).any(|k| md.rem[k][r][c] != 255)).unwrap_or(99)
}

/// Goal for a DR with m quarter turns: 12 / 13 / 14 for 2 / 3 / 4.
pub fn goal_of(m: usize) -> usize {
    m + 10
}

/// One variant, as the enumeration reports it.
pub struct Var<'a> {
    pub w: &'a [usize],
    pub z: u32,
}

/// Every variant from `x` with at most `qmax` quarter turns whose corner bound is at most `goal`
/// (and |P| <= lencap).  Calls `f` on each.
pub fn variants<F: FnMut(&Var)>(md: &Model, x: &St, goal: usize, lencap: usize, qmax: usize, f: &mut F) {
    let mut w: Vec<usize> = Vec::with_capacity(24);
    #[allow(clippy::too_many_arguments)]
    fn dfs<F: FnMut(&Var)>(md: &Model, s: St, w: &mut Vec<usize>, q: usize, lf: usize, goal: usize, lencap: usize, qmax: usize, f: &mut F) {
        if let Some(&last) = w.last() {
            if is_qt(last) {
                if let Some(zi) = md.hg.get(&s) {
                    let kind = md.cases[md.hcase[zi as usize] as usize].kind as usize;
                    if w.len() + LC[kind] as usize <= goal {
                        f(&Var { w, z: zi });
                    }
                }
            }
        }
        if w.len() >= lencap {
            return;
        }
        for mv in 0..10 {
            if !allowed(lf, mv) {
                continue;
            }
            let q2 = q + usize::from(is_qt(mv));
            if q2 > qmax {
                continue;
            }
            let s2 = s.apply_move(mv);
            let len = w.len() + 1;
            // edges and corners must still reach HTR, and some kind must fit under the goal
            if len + md.htrd(&s2) as usize > lencap {
                continue;
            }
            let c = rank_perm(&s2.c);
            let mut ok = false;
            'k: for k in 0..6 {
                for r in 0..=(qmax - q2) {
                    let need = md.rem[k][r][c];
                    if need == 255 {
                        continue;
                    }
                    // r = 0 only counts when this move is the quarter turn that lands
                    if r == 0 && !is_qt(mv) {
                        continue;
                    }
                    if len + need as usize + LC[k] as usize <= goal && len + need as usize <= lencap {
                        ok = true;
                        break 'k;
                    }
                }
            }
            if !ok {
                continue;
            }
            w.push(mv);
            dfs(md, s2, w, q2, FACE[mv], goal, lencap, qmax, f);
            w.pop();
        }
    }
    dfs(md, *x, &mut w, 0, 6, goal, lencap, qmax, f);
}

/// Base rates: optimal leave-slice length by quarter-turn count, over `n` uniform random DR states.
pub fn base(md: &Model, n: usize, seed: u64) {
    let mut rng = crate::Rng(seed);
    let mut h = vec![[0u64; 24]; 8];
    for _ in 0..n {
        let x = crate::random_dr(md, &mut rng);
        // the number in the corner subset's name (0c0 up to a turn of both layers counts as 0)
        let m = (md.subset(&x).as_bytes()[2] - b'0') as usize;
        h[m.min(7)][md.lsopt(&x) as usize] += 1;
    }
    println!("qt\tn\tshare\tmean_ls\tP(ls<=goal-2)\tP(ls<=goal-1)\tP(ls<=goal)\tP(ls<=goal+1)\thistogram ls=6..20");
    for (m, row) in h.iter().enumerate() {
        let tot: u64 = row.iter().sum();
        if tot == 0 {
            continue;
        }
        let g = goal_of(m);
        let cum = |d: usize| row[..=d.min(23)].iter().sum::<u64>() as f64 / tot as f64;
        let mean = row.iter().enumerate().map(|(d, &c)| d as f64 * c as f64).sum::<f64>() / tot as f64;
        let hist: Vec<String> = (6..=20).map(|d| row[d].to_string()).collect();
        println!("{m}\t{tot}\t{:.4}\t{mean:.3}\t{:.4}\t{:.4}\t{:.4}\t{:.4}\t{}", tot as f64 / n as f64, cum(g - 2), cum(g - 1), cum(g), cum(g + 1), hist.join(" "));
    }
}

/// How many variants a DR has per side and length (sizing the main run).
pub fn count(md: &Model, n: usize, seed: u64, mwant: usize, qextra: usize) {
    use rayon::prelude::*;
    let mut rng = crate::Rng(seed);
    let mut xs = Vec::new();
    while xs.len() < n {
        let x = crate::random_dr(md, &mut rng);
        if qt_count(md, &x) == mwant {
            xs.push(x);
        }
    }
    let g = goal_of(mwant);
    let rows: Vec<String> = xs
        .par_iter()
        .enumerate()
        .map(|(i, x)| {
            let t = std::time::Instant::now();
            let mut out = format!("{i}\tls {}", md.lsopt(x));
            for (side, y) in [(0, *x), (1, x.inv())] {
                let mut by_len = [0u64; 20];
                let mut pass = [0u64; 20];
                let mut succ = [0u64; 20];
                variants(md, &y, g, g, mwant + qextra, &mut |v: &Var| {
                    let cs = &md.cases[md.hcase[v.z as usize] as usize];
                    let l = v.w.len();
                    by_len[l] += 1;
                    if l + (LC[cs.kind as usize] + cs.heur) as usize <= g {
                        pass[l] += 1;
                    }
                    if l + md.fin[v.z as usize] as usize <= g {
                        succ[l] += 1;
                    }
                });
                let fmt = |a: &[u64; 20]| a.iter().enumerate().filter(|(_, &c)| c > 0).map(|(l, c)| format!("{l}:{c}")).collect::<Vec<_>>().join(" ");
                out += &format!("\t{} all[{}] rule_ok[{}] within[{}]", ["N", "I"][side], fmt(&by_len), fmt(&pass), fmt(&succ));
            }
            out + &format!("\t{:.1}s", t.elapsed().as_secs_f64())
        })
        .collect();
    for r in rows {
        println!("{r}");
    }
}

// ---------------------------------------------------------------------------------------------------------
// One HTR, one unit.  For a leave-slice search, U and D are the same quarter turn up to the E slice and a
// rotation of what follows, and the last quarter turn's direction is settled while finishing.  A *class* is
// the set of real paths with the same D-free image up to the last direction; its members land on HTR states
// that differ only by U2 / D2 and the E slice.  Its length is the shortest member's, its total the best
// member's.

pub struct Imager {
    /// rot[d][s]: what the side move s becomes when the D move d (0 D, 1 D2, 2 D') before it is written as U
    rot: [[usize; 10]; 3],
}
impl Imager {
    pub fn new() -> Imager {
        let mut rot = [[0usize; 10]; 3];
        for d in 0..3 {
            let x = word(&[[2, 1, 0][d], d + 3]); // U^-a D^a
            for (s, slot) in rot[d].iter_mut().enumerate() {
                if s < 6 {
                    *slot = s;
                    continue;
                }
                let lhs = x.mul(word(&[s]));
                let hits: Vec<usize> = (6..10)
                    .filter(|&t| {
                        let r = word(&[t]).mul(x);
                        r.c == lhs.c && r.e == lhs.e
                    })
                    .collect();
                assert_eq!(hits.len(), 1, "side-move renaming under U^-a D^a is not unique");
                *slot = hits[0];
            }
        }
        Imager { rot }
    }
    /// The D-free image: D^a written as U^a with the rest renamed, cancelled, commuting side pairs ordered.
    pub fn image(&self, w: &[usize]) -> Vec<usize> {
        let mut rho: [usize; 10] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
        let mut out = Vec::with_capacity(w.len());
        for &mv in w {
            if mv < 3 {
                out.push(mv);
            } else if mv < 6 {
                out.push(mv - 3);
                for s in 6..10 {
                    rho[s] = self.rot[mv - 3][rho[s]];
                }
            } else {
                out.push(rho[mv]);
            }
        }
        let mut r = reduce(&out);
        for i in 0..r.len().saturating_sub(1) {
            let (a, b) = (FACE[r[i]], FACE[r[i + 1]]);
            if a / 2 == b / 2 && a > b {
                r.swap(i, i + 1);
            }
        }
        r
    }
    /// Class key of a path; `twin` folds the direction of a final quarter turn.
    pub fn key(&self, w: &[usize], twin: bool) -> u64 {
        let mut im = self.image(w);
        if twin {
            if let Some(l) = im.last_mut() {
                if *l == 2 {
                    *l = 0;
                }
            }
        }
        im.iter().fold(1u64, |k, &m| k << 4 | (m as u64 + 1))
    }
    /// Self-test: a word and its image agree on corners and U/D edges up to a turn of both layers together.
    pub fn check(&self, n: usize, seed: u64) {
        let mut rng = crate::Rng(seed);
        let y = word(&[2, 3]);
        for _ in 0..n {
            let mut w = Vec::new();
            let mut lf = 6;
            while w.len() < 9 {
                let mv = rng.below(10) as usize;
                if allowed(lf, mv) {
                    w.push(mv);
                    lf = FACE[mv];
                }
            }
            let (a, mut b) = (word(&w), word(&self.image(&w)));
            let mut ok = false;
            for _ in 0..4 {
                ok |= a.c == b.c && a.e == b.e;
                b = b.mul(y);
            }
            assert!(ok, "image differs from the word: {}", wname(&w));
        }
        println!("image check ok: {n} words");
    }
}

/// Home-adjacent (corner piece, edge piece) -> pair number 0..15.
fn pair_id(c: usize, e: usize) -> Option<usize> {
    ADJ.iter().position(|&(p, q)| p == c && q == e)
}
/// Which of the 16 true pairs (by pieces) are formed in s.
pub fn pair_ids(s: &St) -> u16 {
    let pm = pair_mask(s);
    let mut m = 0u16;
    for (i, &(p, q)) in ADJ.iter().enumerate() {
        if pm >> i & 1 == 1 {
            m |= 1 << pair_id(s.c[p] as usize, s.e[q] as usize).expect("a true pair is home-adjacent");
        }
    }
    m
}

/// Shortest corner-only path with exactly r quarter turns to HTR corners of any kind.
pub fn lmin_r(md: &Model, c: usize, r: usize) -> u8 {
    (0..6).map(|k| md.rem[k][r][c]).min().unwrap()
}
/// Shortest corner-only path to HTR corners, any kind, at most rmax quarter turns.
pub fn lmin_any(md: &Model, c: usize, rmax: usize) -> u8 {
    (0..=rmax).map(|r| lmin_r(md, c, r)).min().unwrap()
}

pub struct Uni {
    /// moves left for path + finish
    pub goal: usize,
    /// paths this short are kept whatever their corner case (0 = only corner-feasible ones)
    pub cap_any: usize,
    pub qmax: usize,
}

/// Every real variant from `y` inside the universe: f(word, quarter turns, HTR state index).
pub fn real_variants<F: FnMut(&[usize], usize, u32)>(md: &Model, y: &St, u: &Uni, f: &mut F) {
    let mut w: Vec<usize> = Vec::with_capacity(24);
    fn dfs<F: FnMut(&[usize], usize, u32)>(md: &Model, s: St, w: &mut Vec<usize>, q: usize, lf: usize, u: &Uni, f: &mut F) {
        if let Some(&last) = w.last() {
            if is_qt(last) {
                if let Some(zi) = md.hg.get(&s) {
                    let kind = md.cases[md.hcase[zi as usize] as usize].kind as usize;
                    if w.len() + LC[kind] as usize <= u.goal || w.len() <= u.cap_any {
                        f(w, q, zi);
                    }
                }
            }
        }
        if w.len() >= u.goal {
            return;
        }
        for mv in 0..10 {
            if !allowed(lf, mv) {
                continue;
            }
            let q2 = q + usize::from(is_qt(mv));
            if q2 > u.qmax {
                continue;
            }
            let s2 = s.apply_move(mv);
            let len = w.len() + 1;
            if len + md.htrd(&s2) as usize > u.goal {
                continue;
            }
            let c = rank_perm(&s2.c);
            let mut ok = false;
            'k: for k in 0..6 {
                for r in 0..=(u.qmax - q2) {
                    let need = md.rem[k][r][c];
                    if need == 255 || (r == 0 && !is_qt(mv)) {
                        continue;
                    }
                    let t = len + need as usize;
                    if t + LC[k] as usize <= u.goal || t <= u.cap_any {
                        ok = true;
                        break 'k;
                    }
                }
            }
            if !ok {
                continue;
            }
            w.push(mv);
            dfs(md, s2, w, q2, FACE[mv], u, f);
            w.pop();
        }
    }
    dfs(md, *y, &mut w, 0, 6, u, f);
}

/// One HTR to check (a class of real paths).
#[derive(Clone, Copy)]
pub struct Cls {
    /// the shortest member (ties: best total): the path a solver writes down
    pub w: [u8; 16],
    pub wl: u8,
    pub q: u8,
    pub z: u32,
    wtot: u8,
    /// best path + finish over the members, and the member that gives it
    pub total: u8,
    pub tz: u32,
    pub tw: [u8; 16],
    pub tl: u8,
    /// lower bounds on path + finish over the members: corner, rule, table
    pub lbc: u8,
    pub lbr: u8,
    pub lbt: u8,
    /// bad slices and cs | fr << 1 of the member with the smallest rule bound
    pub bad: u8,
    pub csfr: u8,
}

pub struct Ctx<'a> {
    pub md: &'a Model,
    pub im: Imager,
    /// smallest finish over each case's states, minus the kind's corner moves
    pub tpen: Vec<u8>,
}
impl<'a> Ctx<'a> {
    pub fn new(md: &'a Model) -> Ctx<'a> {
        let mut tfin = vec![255u8; md.cases.len()];
        for (i, &c) in md.hcase.iter().enumerate() {
            tfin[c as usize] = tfin[c as usize].min(md.fin[i]);
        }
        let tpen = tfin.iter().zip(&md.cases).map(|(&f, c)| f - LC[c.kind as usize]).collect();
        Ctx { md, im: Imager::new(), tpen }
    }

    /// The classes of a side, keyed by image.
    pub fn classes(&self, y: &St, u: &Uni) -> std::collections::HashMap<u64, Cls> {
        let md = self.md;
        let mut map: std::collections::HashMap<u64, Cls> = std::collections::HashMap::new();
        real_variants(md, y, u, &mut |w: &[usize], q: usize, zi: u32| {
            let ci = md.hcase[zi as usize] as usize;
            let cs = &md.cases[ci];
            let len = w.len() as u8;
            let tot = len + md.fin[zi as usize];
            let lbc = len + LC[cs.kind as usize];
            let (lbr, lbt) = (lbc + cs.heur, lbc + self.tpen[ci]);
            let key = self.im.key(w, true);
            let e = map.entry(key).or_insert_with(|| {
                let mut a = [0u8; 16];
                for (d, &m) in a.iter_mut().zip(w) {
                    *d = m as u8;
                }
                Cls { w: a, wl: len, q: q as u8, z: zi, wtot: tot, total: tot, tz: zi, tw: a, tl: len, lbc, lbr, lbt, bad: cs.bad(), csfr: cs.cs | cs.fr << 1 }
            });
            if (len, tot) < (e.wl, e.wtot) {
                e.w = [0u8; 16];
                for (d, &m) in e.w.iter_mut().zip(w) {
                    *d = m as u8;
                }
                (e.wl, e.q, e.z, e.wtot) = (len, q as u8, zi, tot);
            }
            if tot < e.total {
                (e.total, e.tz, e.tl) = (tot, zi, len);
                e.tw = [0u8; 16];
                for (d, &m) in e.tw.iter_mut().zip(w) {
                    *d = m as u8;
                }
            }
            e.lbc = e.lbc.min(lbc);
            e.lbt = e.lbt.min(lbt);
            if lbr < e.lbr {
                (e.lbr, e.bad, e.csfr) = (lbr, cs.bad(), cs.cs | cs.fr << 1);
            }
        });
        map
    }
}

/// Most of the true pairs of HTR state z that an optimal leave-slice finish can leave unsplit all the way.
pub fn kept_through_finish(md: &Model, z: u32) -> u8 {
    fn dfs(md: &Model, s: St, zi: u32, mask: u16, best: &mut u8) {
        let d = md.fin[zi as usize];
        if d == 0 || mask == 0 {
            *best = (*best).max(mask.count_ones() as u8);
            return;
        }
        for &mv in &HALF {
            let s2 = s.apply_move(mv);
            let z2 = md.hg.get(&s2).unwrap();
            if md.fin[z2 as usize] + 1 == d {
                dfs(md, s2, z2, mask & pair_ids(&s2), best);
            }
        }
    }
    let s = md.hg.st[z as usize];
    let mut best = 0u8;
    dfs(md, s, z, pair_ids(&s), &mut best);
    best
}

/// A record of the main run (40 bytes, see `Rec::bytes`).
#[derive(Clone, Copy, Default)]
pub struct Rec {
    pub dr: u32,
    pub pre2: u32,
    pub pre1: u32,
    pub side: u8,
    pub q: u8,
    pub kind: u8,
    pub len: u8,
    pub lsk: u8,
    pub e2: u8,
    pub e1: u8,
    pub maxsec: u8,
    pub total: u8,
    pub lbc: u8,
    pub lbr: u8,
    pub lbt: u8,
    pub bad: u8,
    pub csfr: u8,
    pub pn0: u8,
    pub pi0: u8,
    pub pn1: u8,
    pub pi1: u8,
    pub pn2: u8,
    pub pi2: u8,
    pub keep20: u8,
    pub keep10: u8,
    pub keptfin: u8,
    pub sp0: u8,
    pub m: u8,
    pub goal: u8,
    pub sn0: u8,
    pub si0: u8,
}
impl Rec {
    pub fn bytes(&self) -> [u8; 40] {
        let mut b = [0u8; 40];
        b[0..4].copy_from_slice(&self.dr.to_le_bytes());
        b[4..8].copy_from_slice(&self.pre2.to_le_bytes());
        b[8..12].copy_from_slice(&self.pre1.to_le_bytes());
        let t = [
            self.side,
            self.q,
            self.kind,
            self.len,
            self.lsk,
            self.e2,
            self.e1,
            self.maxsec,
            self.total,
            self.lbc,
            self.lbr,
            self.lbt,
            self.bad,
            self.csfr,
            self.pn0,
            self.pi0,
            self.pn1,
            self.pi1,
            self.pn2,
            self.pi2,
            self.keep20,
            self.keep10,
            self.keptfin,
            self.sp0,
            self.m,
            self.goal,
            self.sn0,
            self.si0,
        ];
        b[12..40].copy_from_slice(&t);
        b
    }
}

/// Corners that form a block with the E-slice edge next to them (judging-a-dr's `slice_pairs`).
pub fn slice_pairs(s: &St) -> u8 {
    const E_ADJ: [usize; 8] = [0, 1, 2, 3, 0, 1, 2, 3];
    const SLICE_COL: [[u8; 2]; 4] = [[0, 3], [0, 1], [2, 1], [2, 3]];
    (0..8)
        .filter(|&p| {
            let c = s.c[p] as usize;
            TETRAD[c] == TETRAD[p] && CORNER_COL[c] == SLICE_COL[s.s[E_ADJ[p]] as usize]
        })
        .count() as u8
}

/// The states after each quarter turn of a path (index 0 = the start), with the moves made up to there.
fn nodes(start: &St, w: &[usize]) -> Vec<(St, usize)> {
    let mut out = vec![(*start, 0usize)];
    let mut s = *start;
    for (i, &mv) in w.iter().enumerate() {
        s = s.apply_move(mv);
        if is_qt(mv) {
            out.push((s, i + 1));
        }
    }
    out
}

impl<'a> Ctx<'a> {
    /// Full record of a class on side `side` whose paths start at `y`.
    #[allow(clippy::too_many_arguments)]
    pub fn record(&self, y: &St, c: &Cls, dr: u32, side: u8, m: usize, goal: usize, ids2: &mut std::collections::HashMap<u64, u32>, ids1: &mut std::collections::HashMap<u64, u32>) -> Rec {
        let md = self.md;
        let w: Vec<usize> = c.w[..c.wl as usize].iter().map(|&m| m as usize).collect();
        let q = c.q as usize;
        let kind = md.cases[md.hcase[c.z as usize] as usize].kind as usize;
        let nd = nodes(y, &w);
        assert_eq!(nd.len(), q + 1);
        let l = md.rem[kind][q][rank_perm(&y.c)];
        assert!(l != 255 && l <= c.wl, "skeleton length");
        let ex: Vec<u8> = (0..=q).map(|j| (nd[j].1 as u8 + md.rem[kind][q - j][rank_perm(&nd[j].0.c)]) - l).collect();
        let maxsec = (1..q.saturating_sub(1)).map(|j| ex[j] - ex[j - 1]).max().unwrap_or(0);
        let n2 = q.saturating_sub(2);
        let (s0, s1, s2) = (nd[q].0, nd[q - 1].0, nd[n2].0);
        let (p0, p1, p2) = (pair_ids(&s0), pair_ids(&s1), pair_ids(&s2));
        let id = |map: &mut std::collections::HashMap<u64, u32>, upto: usize| -> u32 {
            let k = self.im.key(&w[..upto], false);
            let n = map.len() as u32;
            *map.entry(k).or_insert(n)
        };
        let pre2 = id(ids2, nd[n2].1);
        let pre1 = id(ids1, nd[q - 1].1);
        Rec {
            dr,
            pre2,
            pre1,
            side,
            q: q as u8,
            kind: kind as u8,
            len: c.wl,
            lsk: l,
            e2: ex[n2],
            e1: ex[q - 1],
            maxsec,
            total: c.total,
            lbc: c.lbc,
            lbr: c.lbr,
            lbt: c.lbt,
            bad: c.bad,
            csfr: c.csfr,
            pn0: p0.count_ones() as u8,
            pi0: pairs(&s0.inv()),
            pn1: p1.count_ones() as u8,
            pi1: pairs(&s1.inv()),
            pn2: p2.count_ones() as u8,
            pi2: pairs(&s2.inv()),
            keep20: (p2 & p0).count_ones() as u8,
            keep10: (p1 & p0).count_ones() as u8,
            keptfin: if c.total as usize <= goal { kept_through_finish(md, c.tz) } else { 255 },
            sp0: pair_ids(&md.hg.st[c.tz as usize]).count_ones() as u8,
            m: m as u8,
            goal: goal as u8,
            sn0: slice_pairs(&s0),
            si0: slice_pairs(&s0.inv()),
        }
    }
}

/// Normal prefixes for a mid-skeleton NISS: classes of paths with exactly j quarter turns, ending with one,
/// at most `emax` extra moves over the shortest corner route with m quarter turns.  Returns (word, extra).
pub fn niss_prefixes(cx: &Ctx, x: &St, m: usize, j: usize, emax: usize) -> Vec<(Vec<usize>, u8)> {
    let md = cx.md;
    let l0 = lmin_r(md, rank_perm(&x.c), m) as usize;
    let mut seen: std::collections::HashMap<u64, (Vec<usize>, u8)> = std::collections::HashMap::new();
    let mut w: Vec<usize> = Vec::new();
    #[allow(clippy::too_many_arguments)]
    fn dfs(cx: &Ctx, s: St, w: &mut Vec<usize>, q: usize, lf: usize, m: usize, j: usize, cap: usize, l0: usize, seen: &mut std::collections::HashMap<u64, (Vec<usize>, u8)>) {
        if q == j {
            let e = (w.len() + lmin_r(cx.md, rank_perm(&s.c), m - j) as usize - l0) as u8;
            seen.entry(cx.im.key(w, false)).or_insert_with(|| (w.clone(), e));
            return;
        }
        for mv in 0..10 {
            if !allowed(lf, mv) {
                continue;
            }
            let q2 = q + usize::from(is_qt(mv));
            let s2 = s.apply_move(mv);
            let need = lmin_r(cx.md, rank_perm(&s2.c), m - q2);
            if need == 255 || w.len() + 1 + need as usize > cap {
                continue;
            }
            w.push(mv);
            dfs(cx, s2, w, q2, FACE[mv], m, j, cap, l0, seen);
            w.pop();
        }
    }
    dfs(cx, *x, &mut w, 0, 6, m, j, l0 + emax, l0, &mut seen);
    let mut v: Vec<(Vec<usize>, u8)> = seen.into_values().collect();
    v.sort();
    v
}

/// The main run on one DR: records of both sides, and the mid-skeleton NISS histogram lines.
pub fn run_one(cx: &Ctx, x: &St, dr: u32, niss: bool) -> (Vec<Rec>, Vec<String>) {
    let md = cx.md;
    let m = qt_count(md, x);
    let goal = goal_of(m);
    let mut recs = Vec::new();
    let mut lines = Vec::new();
    let qmax = (m + 2).min(6);
    let mut info = Vec::new();
    for (side, y) in [(0u8, *x), (1u8, x.inv())] {
        let lmin = lmin_any(md, rank_perm(&y.c), qmax) as usize;
        let u = Uni { goal, cap_any: (goal - 1).min(lmin + 3), qmax };
        let cl = cx.classes(&y, &u);
        let (mut ids2, mut ids1) = (std::collections::HashMap::new(), std::collections::HashMap::new());
        let mut keys: Vec<&u64> = cl.keys().collect();
        keys.sort();
        for k in keys {
            recs.push(cx.record(&y, &cl[k], dr, side, m, goal, &mut ids2, &mut ids1));
        }
        info.push(format!("{lmin}\t{}", cl.len()));
    }
    lines.push(format!("D\t{dr}\t{m}\t{goal}\t{}\t{}\t{}\t{}", md.lsopt(x), md.subset(x), info.join("\t"), wname(&crate::scramble_of(md, x))));
    if niss {
        // NISS after j quarter turns on normal: prefix A (at most 1 extra move), then variants of (x A)^-1
        for j in 1..m {
            let mut hist: std::collections::BTreeMap<(u8, u8, i8), (u32, u32)> = std::collections::BTreeMap::new();
            let mut npre = [0u32; 2];
            for (a, e) in niss_prefixes(cx, x, m, j, 1) {
                npre[e as usize] += 1;
                let y = x.mul(word(&a)).inv();
                let g = goal - a.len();
                let u = Uni { goal: g, cap_any: 0, qmax: (m - j + 2).min(6) };
                for c in cx.classes(&y, &u).values() {
                    let kind = md.cases[md.hcase[c.z as usize] as usize].kind as usize;
                    let l = md.rem[kind][c.q as usize][rank_perm(&y.c)];
                    let extra = (c.wl - l).min(6);
                    let slack = (g as i32 - c.lbr as i32).clamp(-1, 4) as i8;
                    let h = hist.entry((e, extra, slack)).or_insert((0, 0));
                    h.0 += 1;
                    h.1 += u32::from(c.total as usize <= g);
                }
            }
            lines.push(format!("Q\t{dr}\t{m}\t{j}\t{}\t{}", npre[0], npre[1]));
            for ((e, extra, slack), (n, ns)) in hist {
                lines.push(format!("M\t{dr}\t{m}\t{j}\t{e}\t{extra}\t{slack}\t{n}\t{ns}"));
            }
        }
    }
    (recs, lines)
}

/// drvar metarun N SEED M OUTPREFIX NISS : N uniform random DRs with M quarter turns.
pub fn run(md: &Model, n: usize, seed: u64, mwant: usize, out: &str, niss: bool) {
    use rayon::prelude::*;
    use std::io::Write;
    let cx = Ctx::new(md);
    cx.im.check(2000, 5);
    let mut rng = crate::Rng(seed);
    let mut xs = Vec::new();
    while xs.len() < n {
        let x = crate::random_dr(md, &mut rng);
        if qt_count(md, &x) == mwant {
            xs.push(x);
        }
    }
    let mut fb = std::io::BufWriter::new(std::fs::File::create(format!("{out}.rec")).unwrap());
    let mut ft = std::io::BufWriter::new(std::fs::File::create(format!("{out}.tsv")).unwrap());
    writeln!(ft, "# D: dr m goal ls_optimal subset lmin_normal classes_normal lmin_inverse classes_inverse scramble").unwrap();
    writeln!(ft, "# Q: dr m niss_after_qt prefixes_extra0 prefixes_extra1").unwrap();
    writeln!(ft, "# M: dr m niss_after_qt prefix_extra path_extra rule_slack(-1 = fails) classes within_goal").unwrap();
    let t0 = std::time::Instant::now();
    for (b, chunk) in xs.chunks(64).enumerate() {
        let res: Vec<(Vec<Rec>, Vec<String>)> = chunk.par_iter().enumerate().map(|(i, x)| run_one(&cx, x, (b * 64 + i) as u32, niss)).collect();
        for (recs, lines) in res {
            for r in recs {
                fb.write_all(&r.bytes()).unwrap();
            }
            for l in lines {
                writeln!(ft, "{l}").unwrap();
            }
        }
        eprintln!("{} / {n}  {:.0}s", (b * 64 + chunk.len()).min(n), t0.elapsed().as_secs_f64());
    }
}

/// Per NISS@1qt case: the leave-slice penalty (finish minus the kind's corner moves) of its 3,072 states.
pub fn cases(md: &Model) {
    let mut h = vec![[0u32; 16]; md.cases.len()];
    for (i, &c) in md.hcase.iter().enumerate() {
        h[c as usize][(md.fin[i] - LC[md.cases[c as usize].kind as usize]) as usize] += 1;
    }
    println!("case\tkind\tF\tR\tcs\tfr\tbad\trule\tsheet_penalty\thist_penalty_0..15");
    for (c, cs) in md.cases.iter().enumerate() {
        let hs: Vec<String> = h[c].iter().map(u32::to_string).collect();
        println!(
            "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
            cs.name(),
            KIND_NAME[cs.kind as usize],
            ET_NAME[cs.fe as usize],
            ET_NAME[cs.re as usize],
            cs.cs,
            cs.fr,
            cs.bad(),
            cs.heur,
            cs.pen,
            hs.join(" ")
        );
    }
}


/// drvar metax "SCRAMBLE" : every HTR a solver could check on this DR, one line each (TSV), both sides, plus
/// the within-goal solutions a NISS after 1, 2, ... quarter turns finds with at most 1 extra move before it.
pub fn explain(md: &Model, scr: &str) {
    let cx = Ctx::new(md);
    let x = word(&crate::core::parse_moves(scr.as_bytes(), 64).unwrap_or_else(|| fatal!("not DR moves")));
    let m = qt_count(md, &x);
    let goal = goal_of(m);
    println!("# scramble {scr}\n# subset {}  quarter turns {m}  goal {goal}  optimal leave-slice {}", md.subset(&x), md.lsopt(&x));
    println!("side\tpath\tfinish\tq\tkind\tL\textra\te2\tS\tT\tcase\tbad\trule_N\tcorner_bound\trule_bound\ttable_bound\ttotal\tpairs_htr\tpairs_htr_inv\tpairs_2qt\tpairs_2qt_inv\tkept_trigger\tkept_finish");
    let qmax = (m + 2).min(6);
    for (side, y) in [(0u8, x), (1u8, x.inv())] {
        let lmin = lmin_any(md, rank_perm(&y.c), qmax) as usize;
        let u = Uni { goal, cap_any: (goal - 1).min(lmin + 3), qmax };
        let cl = cx.classes(&y, &u);
        let (mut i2, mut i1) = (std::collections::HashMap::new(), std::collections::HashMap::new());
        let mut rows: Vec<(Rec, &Cls)> = cl.values().map(|c| (cx.record(&y, c, 0, side, m, goal, &mut i2, &mut i1), c)).collect();
        rows.sort_by_key(|(r, c)| (r.lbr, r.len - r.lsk, 255 - r.pn0, c.w));
        for (r, c) in rows {
            let tw: Vec<usize> = c.tw[..c.tl as usize].iter().map(|&m| m as usize).collect();
            let cs = &md.cases[md.hcase[c.tz as usize] as usize];
            let fin = crate::crisp::ls_finish(md, c.tz);
            println!(
                "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
                ["N", "I"][side as usize],
                wname(&tw),
                wname(&fin),
                r.q,
                KIND_NAME[r.kind as usize],
                r.lsk,
                r.len - r.lsk,
                r.e2,
                r.e1 - r.e2,
                r.len - r.lsk - r.e1,
                cs.name(),
                r.bad,
                r.lbr - r.lbc,
                r.lbc,
                r.lbr,
                r.lbt,
                r.total,
                r.pn0,
                r.pi0,
                r.pn2,
                r.pi2,
                r.keep20,
                if r.keptfin == 255 { "-".to_string() } else { format!("{}/{}", r.keptfin, r.sp0) }
            );
        }
    }
    for j in 1..m {
        for (a, e) in niss_prefixes(&cx, &x, m, j, 1) {
            let y = x.mul(word(&a)).inv();
            let g = goal - a.len();
            let u = Uni { goal: g, cap_any: 0, qmax: (m - j + 2).min(6) };
            for c in cx.classes(&y, &u).values() {
                if c.total as usize > g {
                    continue;
                }
                let kind = md.cases[md.hcase[c.tz as usize] as usize].kind as usize;
                let tw: Vec<usize> = c.tw[..c.tl as usize].iter().map(|&m| m as usize).collect();
                let l = md.rem[kind][c.q as usize][rank_perm(&y.c)];
                let fin = crate::crisp::ls_finish(md, c.tz);
                println!(
                    "NISS{j}\t{} ({})\t({})\t{}\t{}\tprefix_extra {e}\tpath_extra {}\trule_bound {}\ttotal {}",
                    wname(&a),
                    wname(&tw),
                    wname(&fin),
                    c.q,
                    KIND_NAME[kind],
                    c.wl - l,
                    a.len() + c.lbr as usize,
                    a.len() + c.total as usize
                );
            }
        }
    }
}

/// All 663,552 HTR states: (case, true pairs, leave-slice finish) -> count.
pub fn htr_pairs(md: &Model) {
    let mut h: std::collections::BTreeMap<(u8, u8, u8), u32> = std::collections::BTreeMap::new();
    for (i, s) in md.hg.st.iter().enumerate() {
        *h.entry((md.hcase[i], pairs(s), md.fin[i])).or_insert(0) += 1;
    }
    println!("case\tkind\tbad\trule\tpairs\tfinish\tstates");
    for ((c, p, f), n) in h {
        let cs = &md.cases[c as usize];
        println!("{}\t{}\t{}\t{}\t{p}\t{f}\t{n}", cs.name(), KIND_NAME[cs.kind as usize], cs.bad(), cs.heur);
    }
}

/// Fewest finish moves of any HTR state with this many true pairs (exact over the 663,552 states).
pub fn pair_floor(md: &Model) -> [u8; 17] {
    let mut f = [255u8; 17];
    for (i, s) in md.hg.st.iter().enumerate() {
        let p = pairs(s) as usize;
        f[p] = f[p].min(md.fin[i]);
    }
    f
}

/// drvar metaniss N SEED M OUT : the mid-skeleton NISS candidates of the same DRs as `metarun N SEED M`.
/// After j quarter turns on normal (prefix A with at most 1 extra move), the variants of (x A)^-1.
/// Lines: dr m j prefix_extra path_extra rule_slack(-1 fails ... 3) pair_live classes within_goal.
pub fn run_niss(md: &Model, n: usize, seed: u64, mwant: usize, out: &str) {
    use rayon::prelude::*;
    use std::io::Write;
    let cx = Ctx::new(md);
    let pf = pair_floor(md);
    let mut rng = crate::Rng(seed);
    let mut xs = Vec::new();
    while xs.len() < n {
        let x = crate::random_dr(md, &mut rng);
        if qt_count(md, &x) == mwant {
            xs.push(x);
        }
    }
    let mut ft = std::io::BufWriter::new(std::fs::File::create(out).unwrap());
    writeln!(ft, "# Q: dr m niss_after_qt prefixes_extra0 prefixes_extra1").unwrap();
    writeln!(ft, "# M: dr m niss_after_qt prefix_extra path_extra rule_slack pair_live classes within_goal").unwrap();
    let t0 = std::time::Instant::now();
    for (b, chunk) in xs.chunks(64).enumerate() {
        let res: Vec<Vec<String>> = chunk
            .par_iter()
            .enumerate()
            .map(|(i, x)| {
                let dr = b * 64 + i;
                let m = mwant;
                let goal = goal_of(m);
                let mut lines = Vec::new();
                for j in 1..m {
                    let mut hist: std::collections::BTreeMap<(u8, u8, i8, u8), (u32, u32)> = std::collections::BTreeMap::new();
                    let mut npre = [0u32; 2];
                    for (a, e) in niss_prefixes(&cx, x, m, j, 1) {
                        npre[e as usize] += 1;
                        let y = x.mul(word(&a)).inv();
                        let g = goal - a.len();
                        let u = Uni { goal: g, cap_any: 0, qmax: (m - j + 2).min(6) };
                        for c in cx.classes(&y, &u).values() {
                            let kind = md.cases[md.hcase[c.z as usize] as usize].kind as usize;
                            let l = md.rem[kind][c.q as usize][rank_perm(&y.c)];
                            let extra = (c.wl - l).min(8);
                            let slack = (g as i32 - c.lbr as i32).clamp(-1, 3) as i8;
                            let plive = u8::from(c.wl as usize + pf[pairs(&md.hg.st[c.z as usize]) as usize] as usize <= g);
                            let ok = c.total as usize <= g;
                            assert!(!ok || (plive == 1 && slack >= 0), "a within-goal variant fails a floor");
                            let h = hist.entry((e, extra, slack, plive)).or_insert((0, 0));
                            h.0 += 1;
                            h.1 += u32::from(ok);
                        }
                    }
                    lines.push(format!("Q\t{dr}\t{m}\t{j}\t{}\t{}", npre[0], npre[1]));
                    for ((e, extra, slack, plive), (n, ns)) in hist {
                        lines.push(format!("M\t{dr}\t{m}\t{j}\t{e}\t{extra}\t{slack}\t{plive}\t{n}\t{ns}"));
                    }
                }
                lines
            })
            .collect();
        for lines in res {
            for l in lines {
                writeln!(ft, "{l}").unwrap();
            }
        }
        eprintln!("{} / {n}  {:.0}s", (b * 64 + chunk.len()).min(n), t0.elapsed().as_secs_f64());
    }
}

/// drvar metacheck N SEED M : the within-goal classes of the main run against an independent enumeration
/// (`search::paths`, pruned with the exact leave-slice table instead of the corner tables), both sides.
pub fn check(md: &Model, n: usize, seed: u64, mwant: usize) {
    use rayon::prelude::*;
    let cx = Ctx::new(md);
    let mut rng = crate::Rng(seed);
    let mut xs = Vec::new();
    while xs.len() < n {
        let x = crate::random_dr(md, &mut rng);
        if qt_count(md, &x) == mwant {
            xs.push(x);
        }
    }
    let goal = goal_of(mwant);
    let qmax = (mwant + 2).min(6);
    let res: Vec<(usize, usize)> = xs
        .par_iter()
        .map(|x| {
            let mut tot = (0, 0);
            for y in [*x, x.inv()] {
                let lmin = lmin_any(md, rank_perm(&y.c), qmax) as usize;
                let cl = cx.classes(&y, &Uni { goal, cap_any: (goal - 1).min(lmin + 3), qmax });
                let sols = crate::search::paths(md, &y, goal, qmax, |s, _, _| md.lsopt(s) as usize, |_, _, _, b| b as usize <= goal);
                let mut keys: std::collections::HashMap<u64, u8> = std::collections::HashMap::new();
                for p in &sols {
                    let e = keys.entry(cx.im.key(&p.w, true)).or_insert(255);
                    *e = (*e).min(p.best);
                }
                for (k, best) in &keys {
                    let c = cl.get(k).unwrap_or_else(|| panic!("a within-goal path has no class"));
                    assert_eq!(c.total, *best, "class total differs from the independent enumeration");
                }
                let nwithin = cl.values().filter(|c| c.total as usize <= goal).count();
                assert_eq!(nwithin, keys.len(), "within-goal classes differ");
                tot.0 += sols.len();
                tot.1 += keys.len();
            }
            tot
        })
        .collect();
    let (a, b): (usize, usize) = res.iter().fold((0, 0), |s, r| (s.0 + r.0, s.1 + r.1));
    println!("metacheck ok: {n} DRs with {mwant} quarter turns, both sides: {a} within-goal paths in {b} classes, every class found with the same total");
}

/// drvar metawit : HTR states that show how far pairs and the finish can be apart (half-turn scrambles).
pub fn witnesses(md: &Model) {
    let show = |name: &str, i: usize| {
        let s = &md.hg.st[i];
        let cs = &md.cases[md.hcase[i] as usize];
        let fin = crate::crisp::ls_finish(md, i as u32);
        println!("{name}\tscramble {}\tpairs {}\tleave-slice finish {} ({})\tcase {} rule +{}", wname(&md.hg.word_of(i as u32)), pairs(s), md.fin[i], wname(&fin), cs.name(), cs.heur);
    };
    let pick = |p: u8, f: u8| (0..md.hg.st.len()).filter(|&i| pairs(&md.hg.st[i]) == p && md.fin[i] == f).min_by_key(|&i| md.hg.d3[i]);
    for (name, p, f) in [
        ("16 pairs, long finish", 16u8, 10u8),
        ("16 pairs, 9", 16, 9),
        ("12 pairs, 1 move", 12, 1),
        ("10 pairs at its floor", 10, 3),
        ("8 pairs at its floor", 8, 2),
        ("2 pairs at its floor", 2, 5),
        ("0 pairs at its floor", 0, 4),
        ("12 pairs, 10 moves", 12, 10),
    ] {
        match pick(p, f) {
            Some(i) => show(name, i),
            None => println!("{name}\tnone"),
        }
    }
    // a zero-penalty rule case (zero bad slices, good parity) with the longest finish
    let i = (0..md.hg.st.len()).filter(|&i| md.cases[md.hcase[i] as usize].heur == 0 && md.cases[md.hcase[i] as usize].kind == 0).max_by_key(|&i| md.fin[i]).unwrap();
    show("H-H, rule +0, longest finish", i);
}

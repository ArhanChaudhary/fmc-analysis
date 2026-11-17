//! The cube model and every table the search needs.
//!
//! * The DR group, moves and coordinates are judging-a-dr's (`core.rs`): a state is "which piece sits at each
//!   position" for the 8 corners, 8 U/D-layer edges and 4 E-slice edges; moves 0 U 1 U2 2 U' 3 D 4 D2 5 D'
//!   6 R2 7 L2 8 F2 9 B2; `a.mul(b)` = a then b.
//! * H = <U2 D2 R2 L2 F2 B2> (HTR), with the half-turn length `d3` of each of its 663,552 states.
//! * The 216 NISS@1qt cases are the classes of judging-a-dr's KF quotient on H.  Each one is labelled with
//!   the row of Rodney Kinney's sheet "Adv DR Bounding" whose setup alg lands in it (`data/cases216.tsv`).
//! * `opt` is the optimal DR finish of any DR state, read from judging-a-dr's Lean-certified exact table.
//! * J_c = the corner permutations of slices (R2 L2, F2 B2, U2 D2) and corner swaps (X2 Y2 X2): 24 of them.
//!   An *insertion* in the sense of the Advanced DR Bounding doc (slices, corner swaps, pure edge
//!   permutations, and any mix of them in one block) is a half-turn block whose corner action is in J_c.

use crate::class::Classes;
use crate::core::{rank_perm, Core, St, NMOVES};
use crate::quot::{CornerQuot, E630, NE630};
use crate::reduced::{CornerClasses, SliceIndex, ROW};
use std::collections::HashMap;

/// The half turns U2 D2 R2 L2 F2 B2.
pub const HALF: [usize; 6] = [1, 4, 6, 7, 8, 9];
/// Face of each move: 0 U, 1 D, 2 R, 3 L, 4 F, 5 B.
pub const FACE: [usize; NMOVES] = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5];
/// Quarter turns of each move (U-face and D-face: 1, 2, 3; side faces: 2).
pub const AMT: [usize; NMOVES] = [1, 2, 3, 1, 2, 3, 2, 2, 2, 2];
pub const KIND_NAME: [&str; 6] = ["H-H", "R-D", "F-D", "R-V", "F-V", "D-D"];
pub const ET_NAME: [&str; 3] = ["H", "D", "V"];
/// Moves of the corner HTR section of each corner kind (the sheet's "Penalty" is the finish minus this).
pub const LC: [u8; 6] = [0, 1, 1, 2, 2, 3];

pub fn is_qt(m: usize) -> bool { matches!(m, 0 | 2 | 3 | 5) }

/// May move `m` follow a move on face `prev` (6 = none) in a canonical sequence?
pub fn allowed(prev: usize, m: usize) -> bool {
    let f = FACE[m];
    prev == 6 || (f != prev && !(f % 2 == 0 && prev == f + 1))
}

pub fn key(s: &St) -> u64 {
    (rank_perm(&s.c) as u64 * 40320 + rank_perm(&s.e) as u64) * 24 + rank_perm(&s.s) as u64
}
pub fn word(ms: &[usize]) -> St { ms.iter().fold(St::ID, |g, &m| g.apply_move(m)) }
pub fn wname(ms: &[usize]) -> String {
    ms.iter().map(|&m| crate::core::MOVE_NAME[m]).collect::<Vec<_>>().join(" ")
}
pub fn move_of(face: usize, amt: usize) -> usize {
    match face {
        0 => [0, 1, 2][amt - 1],
        1 => [3, 4, 5][amt - 1],
        f => f + 4,
    }
}

/// Fully cancel a move sequence: merge same-face moves, also across a move on the opposite face.
pub fn reduce(ms: &[usize]) -> Vec<usize> {
    let mut out: Vec<(usize, usize)> = Vec::new(); // (face, quarter turns mod 4)
    for &m in ms {
        let (f, a) = (FACE[m], AMT[m]);
        let n = out.len();
        let hit = if n >= 1 && out[n - 1].0 == f {
            Some(n - 1)
        } else if n >= 2 && out[n - 1].0 / 2 == f / 2 && out[n - 2].0 == f {
            Some(n - 2)
        } else {
            None
        };
        match hit {
            Some(i) => {
                let t = (out[i].1 + a) % 4;
                if t == 0 { out.remove(i); } else { out[i].1 = t; }
            }
            None => out.push((f, a)),
        }
    }
    out.iter().map(|&(f, a)| move_of(f, a)).collect()
}

/// The HTR group: its states, an index, and half-turn length.
pub struct Hgrp {
    pub st: Vec<St>,
    pub idx: HashMap<u64, u32>,
    pub d3: Vec<u8>,
    /// a shortest half-turn word of each state, as the index of its parent and the last move
    pub par: Vec<(u32, u8)>,
}
impl Hgrp {
    pub fn new() -> Hgrp {
        let mut st = vec![St::ID];
        let mut idx = HashMap::new();
        idx.insert(key(&St::ID), 0u32);
        let (mut d3, mut par) = (vec![0u8], vec![(u32::MAX, 0u8)]);
        let mut head = 0;
        while head < st.len() {
            let g = st[head];
            for &m in &HALF {
                let n = g.apply_move(m);
                let k = key(&n);
                if let std::collections::hash_map::Entry::Vacant(v) = idx.entry(k) {
                    v.insert(st.len() as u32);
                    st.push(n);
                    d3.push(d3[head] + 1);
                    par.push((head as u32, m as u8));
                }
            }
            head += 1;
        }
        assert_eq!(st.len(), 663_552);
        Hgrp { st, idx, d3, par }
    }
    pub fn get(&self, s: &St) -> Option<u32> { self.idx.get(&key(s)).copied() }
    /// A shortest half-turn word of H state `i`.
    pub fn word_of(&self, mut i: u32) -> Vec<usize> {
        let mut w = Vec::new();
        while self.par[i as usize].0 != u32::MAX {
            w.push(self.par[i as usize].1 as usize);
            i = self.par[i as usize].0;
        }
        w.reverse();
        w
    }
}

/// One of the 216 NISS@1qt cases, as labelled in Rodney's sheet.
#[derive(Clone, Copy, Debug)]
pub struct Case {
    pub kind: u8,
    pub fe: u8,
    pub re: u8,
    pub cs: u8,
    pub fr: u8,
    pub miss: u8,
    pub avoid: u8,
    pub heur: u8,
    pub pen: u8,
    /// smallest half-turn finish over the case's 3,072 states (computed here)
    pub min_d3: u8,
}
impl Case {
    pub fn bad(&self) -> u8 { self.miss + self.avoid }
    pub fn name(&self) -> String {
        format!("{} F-{} R-{} cs{} fr{}", KIND_NAME[self.kind as usize], ET_NAME[self.fe as usize], ET_NAME[self.re as usize], self.cs, self.fr)
    }
}

/// Bad slices by the doc's must-have / must-avoid table (used to cross-check the sheet's own columns).
pub fn bad_by_rule(kind: u8, fe: u8, re: u8) -> u8 {
    let (h, d, v) = (0u8, 1u8, 2u8);
    let (bf, br) = match kind {
        0 => (fe != h, re != h),
        1 => (fe == v, re != d),
        2 => (fe != d, re == v),
        3 => (fe == d, re != v),
        4 => (fe != v, re == d),
        _ => (fe == h, re == h),
    };
    bf as u8 + br as u8
}

pub struct Model {
    pub core: Core,
    pub cls: Classes,
    pub cq: CornerQuot,
    pub e630: E630,
    pub hg: Hgrp,
    pub cases: Vec<Case>,
    /// KF class -> case number
    pub case_of_kf: Vec<u16>,
    /// case of every H state
    pub hcase: Vec<u8>,
    /// corner coordinate -> corner kind (0..6) for HTR corners, 255 otherwise
    pub ckind: Vec<u8>,
    /// corner coordinate in J_c?
    pub jc: Vec<bool>,
    /// corner coordinate in the HTR corner group?
    pub hcorner: Vec<bool>,
    /// `rem[kind][r][c]`: fewest moves from corner state c, with exactly r quarter turns and ending in one,
    /// to HTR corners of this kind (r = 0: 0 if c already is such a state, else 255)
    pub rem: Vec<Vec<Vec<u8>>>,
    pub exact: Vec<u8>,
    /// finish length of every H state used for a path's total: d3 (full finish) or the leave-slice finish
    pub fin: Vec<u8>,
    /// optimal leave-slice DR finish of every DR state (judging-a-dr's ls_depth.u8), loaded on demand
    pub ls: Vec<u8>,
    pub ccl: CornerClasses,
    pub sidx: SliceIndex,
}

impl Model {
    /// Tables only (no case labels, no exact table).
    pub fn bare() -> Model {
        let core = Core::new();
        let cls = Classes::new(&core);
        let cq = CornerQuot::new(&core, &cls, true);
        let e630 = E630::new(&core, &cls);
        let ccl = CornerClasses::new(&core);
        let sidx = SliceIndex::new(&core);
        Model { core, cls, cq, e630, hg: Hgrp::new(), cases: Vec::new(), case_of_kf: Vec::new(), hcase: Vec::new(), ckind: vec![255; 40320], jc: vec![false; 40320], hcorner: vec![false; 40320], rem: Vec::new(), exact: Vec::new(), fin: Vec::new(), ls: Vec::new(), ccl, sidx }
    }

    pub fn new(cases_tsv: &str, exact_path: &str) -> Model {
        let core = Core::new();
        let cls = Classes::new(&core);
        let cq = CornerQuot::new(&core, &cls, true);
        let e630 = E630::new(&core, &cls);
        let hg = Hgrp::new();
        let ccl = CornerClasses::new(&core);
        let sidx = SliceIndex::new(&core);
        let mut m = Model {
            core,
            cls,
            cq,
            e630,
            hg,
            cases: Vec::new(),
            case_of_kf: Vec::new(),
            hcase: Vec::new(),
            ckind: vec![255; 40320],
            jc: vec![false; 40320],
            hcorner: vec![false; 40320],
            rem: Vec::new(),
            exact: Vec::new(),
            fin: Vec::new(),
            ls: Vec::new(),
            ccl,
            sidx,
        };
        m.load_cases(cases_tsv);
        m.build_jc();
        for &c in &m.cls.hc {
            m.hcorner[c] = true;
        }
        m.build_rem(6);
        eprintln!("reading the exact table {exact_path} ...");
        m.exact = std::fs::read(exact_path).unwrap_or_else(|e| fatal!("{exact_path}: {e}"));
        assert_eq!(m.exact.len(), m.ccl.nclass * ROW);
        m.fin = m.hg.d3.clone();
        m
    }

    pub fn kf(&self, s: &St) -> usize {
        let (c, e, sl) = (rank_perm(&s.c), rank_perm(&s.e), rank_perm(&s.s));
        (self.cq.ccls[c] as usize * NE630 + self.e630.cls[e] as usize) * 2 + self.core.spar[sl] as usize
    }

    /// Diagnostics: KF classes of the sheet rows and of FakeMMAP's listing, on z and on z^-1.
    pub fn diag(&self, sheet: &str, fm: &str) {
        let read = |p: &str, off: usize| -> Vec<(Vec<u8>, St, String)> {
            std::fs::read_to_string(p).unwrap().lines().map(|l| {
                let f: Vec<&str> = l.split('\t').collect();
                let v: Vec<u8> = f[..off + 20].iter().map(|x| x.parse().unwrap()).collect();
                let st = St { c: v[off..off + 8].try_into().unwrap(), e: v[off + 8..off + 16].try_into().unwrap(), s: v[off + 16..off + 20].try_into().unwrap() };
                (v[..off].to_vec(), st, f[off + 20].to_string())
            }).collect()
        };
        let sh = read(sheet, 10);
        let fmr = read(fm, 6);
        for inv in [false, true] {
            let k = |s: &St| if inv { self.kf(&s.inv()) } else { self.kf(s) };
            let mut ds: Vec<usize> = sh.iter().map(|r| k(&r.1)).collect(); ds.sort(); ds.dedup();
            let mut df: Vec<usize> = fmr.iter().map(|r| k(&r.1)).collect(); df.sort(); df.dedup();
            eprintln!("inverse={inv}: sheet rows in {} KF classes, FakeMMAP rows in {} KF classes", ds.len(), df.len());
            // label agreement per class: sheet (kind, F, R, cs, fr) vs FakeMMAP (kind, sign, F, R, parity)
            let mut agree = 0; let mut dis = Vec::new();
            for r in &sh {
                if let Some(q) = fmr.iter().find(|q| k(&q.1) == k(&r.1)) {
                    let a = (r.0[0], r.0[1], r.0[2]);
                    let b = (q.0[0], q.0[2], q.0[3]);
                    if a == b { agree += 1 } else { dis.push(format!("sheet {:?} {} | FM {:?} {}", r.0, r.2, q.0, q.2)); }
                }
            }
            eprintln!("  sheet rows whose (kind, F, R, fr) equals FakeMMAP's in the same class: {agree}");
            for d in dis.iter().take(12) { eprintln!("    {d}"); }
            // parity conventions: sheet (cs, fr) against FakeMMAP (sign, E-parity), by kind
            let mut tab = std::collections::BTreeMap::new();
            for r in &sh { if let Some(q) = fmr.iter().find(|q| k(&q.1) == k(&r.1)) { *tab.entry((r.0[0], r.0[3], r.0[4], q.0[1], q.0[4])).or_insert(0) += 1; } }
            eprintln!("  (kind, cs, fr, FMsign, FMEpar) -> rows: {tab:?}");
            for (i, r) in sh.iter().enumerate() { for (j, q) in sh.iter().enumerate() { if i < j && k(&r.1) == k(&q.1) { eprintln!("  collision: {:?} {} / {:?} {}", r.0, r.2, q.0, q.2); } } }
        }
    }

    fn load_cases(&mut self, path: &str) {
        let txt = std::fs::read_to_string(path).unwrap_or_else(|e| fatal!("{path}: {e}"));
        let nkf = self.cq.ncc * NE630 * 2;
        self.case_of_kf = vec![u16::MAX; nkf];
        let mut kind_of_cc: std::collections::HashMap<usize, u8> = std::collections::HashMap::new();
        for line in txt.lines() {
            let f: Vec<&str> = line.split('\t').collect();
            let v: Vec<u8> = f[..30].iter().map(|x| x.parse().unwrap()).collect();
            let st = St { c: v[10..18].try_into().unwrap(), e: v[18..26].try_into().unwrap(), s: v[26..30].try_into().unwrap() };
            assert!(self.hg.get(&st).is_some(), "sheet row is not an HTR state: {line}");
            let k = self.kf(&st);
            assert_eq!(self.case_of_kf[k], u16::MAX, "two sheet rows in one KF class: {line}");
            self.case_of_kf[k] = self.cases.len() as u16;
            let case = Case { kind: v[0], fe: v[1], re: v[2], cs: v[3], fr: v[4], miss: v[5], avoid: v[6], heur: v[8], pen: v[9], min_d3: 255 };
            assert_eq!(case.bad(), bad_by_rule(case.kind, case.fe, case.re), "sheet bad-slice columns vs the doc's table: {line}");
            self.cases.push(case);
            // corner kind of the KF corner class of the sheet's setup state (that is the inverse of the HTR state
            // an attempt reaches: the sheet's setups are what you see at 1qt on the inverse, "Setup: U + ...")
            let kc = self.cq.ccls[rank_perm(&st.c)] as usize;
            kind_of_cc.insert(kc, case.kind);
        }
        // an HTR state z gets the case (and corner kind) of z^-1
        for c in 0..40320 {
            if self.cls.hc.contains(&c) {
                let inv = crate::core::unrank_perm::<8>(c);
                let mut ci = [0u8; 8];
                for p in 0..8 {
                    ci[inv[p] as usize] = p as u8;
                }
                self.ckind[c] = kind_of_cc[&(self.cq.ccls[rank_perm(&ci)] as usize)];
            }
        }
        assert_eq!(self.cases.len(), 216);
        // every H state falls in a labelled case, 3,072 per case
        let mut cnt = [0usize; 216];
        self.hcase = vec![0; self.hg.st.len()];
        for (i, s) in self.hg.st.iter().enumerate() {
            let c = self.case_of_kf[self.kf(&s.inv())];
            assert!(c != u16::MAX, "an HTR state outside the 216 labelled cases");
            assert_eq!(self.ckind[rank_perm(&s.c)], self.cases[c as usize].kind);
            self.hcase[i] = c as u8;
            cnt[c as usize] += 1;
            let mc = &mut self.cases[c as usize].min_d3;
            *mc = (*mc).min(self.hg.d3[i]);
        }
        assert!(cnt.iter().all(|&n| n == 3072));
        for &hc in &self.cls.hc {
            assert!(self.ckind[hc] != 255);
        }
        let nk = self.ckind.iter().filter(|&&k| k != 255).count();
        eprintln!("216 cases loaded: 3,072 HTR states each; corner kinds defined on {nk} corner permutations");
    }

    fn build_jc(&mut self) {
        // corner permutations of slices and of X2 Y2 X2 corner swaps, closed under products
        let mut gens: Vec<[u8; 8]> = vec![word(&[6, 7]).c, word(&[8, 9]).c, word(&[1, 4]).c];
        let side = [(0usize, 1usize), (1, 4), (2, 6), (3, 7), (4, 8), (5, 9)]; // face -> half-turn move
        for &(fx, mx) in &side {
            for &(fy, my) in &side {
                if fx != fy && fx / 2 != fy / 2 {
                    gens.push(word(&[mx, my, mx]).c);
                }
            }
        }
        let mut seen = vec![false; 40320];
        let mut list = vec![St::ID.c];
        seen[0] = true;
        let mut head = 0;
        while head < list.len() {
            let a = list[head];
            for g in &gens {
                let mut r = [0u8; 8];
                for p in 0..8 {
                    r[p] = a[g[p] as usize];
                }
                let k = rank_perm(&r);
                if !seen[k] {
                    seen[k] = true;
                    list.push(r);
                }
            }
            head += 1;
        }
        assert_eq!(list.len(), 24);
        self.jc = seen;
    }

    fn build_rem(&mut self, rmax: usize) {
        // half-turn corner elements with their lengths, as move-sequence maps on corner coordinates
        let mut hs: Vec<(Vec<usize>, u8)> = Vec::new(); // words for the 96 corner elements
        let mut seen = std::collections::HashMap::new();
        let mut q = std::collections::VecDeque::new();
        q.push_back((Vec::<usize>::new(), 0usize));
        seen.insert(0usize, ());
        while let Some((w, c)) = q.pop_front() {
            hs.push((w.clone(), w.len() as u8));
            for &mv in &HALF {
                let c2 = self.core.cmove[mv][c] as usize;
                if !seen.contains_key(&c2) {
                    seen.insert(c2, ());
                    let mut w2 = w.clone();
                    w2.push(mv);
                    q.push_back((w2, c2));
                }
            }
        }
        assert_eq!(hs.len(), 96);
        let apply = |w: &[usize], c: usize| w.iter().fold(c, |c, &mv| self.core.cmove[mv][c] as usize);
        let mut rem = vec![vec![vec![255u8; 40320]; rmax + 1]; 6];
        for k in 0..6 {
            for c in 0..40320 {
                if self.ckind[c] == k as u8 {
                    rem[k][0][c] = 0;
                }
            }
            for r in 1..=rmax {
                let (lo, hi) = rem[k].split_at_mut(r);
                let prev = &lo[r - 1];
                let cur = &mut hi[0];
                for c in 0..40320 {
                    let mut b = 255u8;
                    for (w, l) in &hs {
                        let ch = apply(w, c);
                        for qt in [0usize, 2, 3, 5] {
                            let p = prev[self.core.cmove[qt][ch] as usize];
                            if p != 255 {
                                b = b.min(l + 1 + p);
                            }
                        }
                    }
                    cur[c] = b;
                }
            }
        }
        self.rem = rem;
    }

    /// Switch to leave-slice solutions: the finish of an HTR state solves corners and U/D edges only, and the
    /// pruning table is the optimal leave-slice DR finish.
    pub fn leave_slice(&mut self, ls_path: &str) {
        // half-turn distance from the 12 slice-only states (E slice an even permutation, all else solved)
        let n = self.hg.st.len();
        let mut d = vec![255u8; n];
        let mut q = Vec::new();
        for (i, s) in self.hg.st.iter().enumerate() {
            if s.c == St::ID.c && s.e == St::ID.e {
                d[i] = 0;
                q.push(i as u32);
            }
        }
        assert_eq!(q.len(), 12);
        let mut head = 0;
        while head < q.len() {
            let i = q[head] as usize;
            head += 1;
            for &mv in &HALF {
                let j = self.hg.get(&self.hg.st[i].apply_move(mv)).unwrap() as usize;
                if d[j] == 255 {
                    d[j] = d[i] + 1;
                    q.push(j as u32);
                }
            }
        }
        self.fin = d;
        self.ls = std::fs::read(ls_path).unwrap_or_else(|e| fatal!("{ls_path}: {e}"));
        assert_eq!(self.ls.len(), self.ccl.nclass * 40320);
    }
    /// Optimal leave-slice DR finish.
    pub fn lsopt(&self, s: &St) -> u8 {
        let (c, e) = (rank_perm(&s.c), rank_perm(&s.e));
        self.ls[self.ccl.cclass[c] as usize * 40320 + self.core.esym[self.ccl.csymto[c] as usize][e] as usize]
    }

    /// Optimal DR finish (exact table).
    pub fn opt(&self, s: &St) -> u8 {
        let (c, e, sl) = (rank_perm(&s.c), rank_perm(&s.e), rank_perm(&s.s));
        let k = self.ccl.cclass[c] as usize;
        let sym = self.ccl.csymto[c] as usize;
        let bit = k * ROW + self.core.esym[sym][e] as usize * 12 + self.sidx.to12[self.core.ssym[sym][sl] as usize] as usize;
        self.exact[bit]
    }
    /// Fewest DR moves to reach HTR.
    pub fn htrd(&self, s: &St) -> u8 {
        self.cls.htr_dist[self.cls.ccos[rank_perm(&s.c)] as usize][self.cls.epat[rank_perm(&s.e)] as usize]
    }
    pub fn subset(&self, s: &St) -> String {
        let (a, b) = (self.cls.ccos[rank_perm(&s.c)] as usize, self.cls.epat[rank_perm(&s.e)] as usize);
        self.cls.sub48_name[self.cls.sub48[a][b] as usize].clone()
    }
}

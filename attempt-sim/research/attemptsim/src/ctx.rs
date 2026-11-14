//! The cube model and every table the search uses.
//!
//! Whole cube: `vendor/cubie.rs` (is-dr-xs-worth-it's cubie model, data in research/data/cubie.txt): faces U D R L F B
//! are 0..5, a move is 3 * face + (quarter turns - 1), axes are 0 R/L, 1 U/D, 2 F/B.
//! A *view* is the cube turned as a whole so that the EO axis is F/B and the DR axis is U/D; every table below is
//! about that one orientation.
//!
//!   eodist[eo]            fewest turns to F/B EO from the flip pattern `eo` (2,048 patterns, any turn)
//!   drdist[co * 495 + sl] fewest EO-keeping turns (U D R L F2 B2) to DR on U/D from corner twists `co` and
//!                         E-slice places `sl`, EO solved (1,082,565 states)
//!   dm                    the DR group (htr-routes' model on judging-a-dr's: vendor/model.rs, core.rs, class.rs,
//!                         reduced.rs) with the exact optimal DR-move finish of every DR state (judging-a-dr's
//!                         lean_exact_table.u8, proved in that study's Lean project), the HTR cosets and subsets

use crate::core::rank_perm;
use crate::cubie::{Cubie, Model, SOLVED};
use crate::model::Model as DrModel;

pub const NCO: usize = 2187;
pub const NEO: usize = 2048;
pub const NSL: usize = 495;
pub const NONE: u8 = 18;
pub const FACE_AXIS: [usize; 6] = [1, 1, 0, 0, 2, 2];
pub const AXIS_NAME: [&str; 3] = ["R/L", "U/D", "F/B"];
pub const NAMES: [&str; 18] = ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'"];
/// The 14 turns that keep F/B EO (view labels).
pub const EOKEEP: [u8; 14] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 16];
/// View move of each of the ten DR moves, in drtools' numbering (U U2 U' D D2 D' R2 L2 F2 B2).
pub const DRMOVE: [u8; 10] = [0, 1, 2, 3, 4, 5, 7, 10, 13, 16];
/// Face (U D R L F B) of each drtools DR move.
pub const DRFACE: [u8; 10] = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5];

pub fn parse(s: &str) -> Vec<u8> {
    s.split_whitespace()
        .map(|t| NAMES.iter().position(|&n| n == t).unwrap_or_else(|| fatal!("bad move {}", t)) as u8)
        .collect()
}
pub fn text(seq: &[u8]) -> String {
    seq.iter().map(|&m| NAMES[m as usize]).collect::<Vec<_>>().join(" ")
}
#[inline]
pub fn inv_move(mv: u8) -> u8 {
    3 * (mv / 3) + 2 - mv % 3
}
pub fn invert(seq: &[u8]) -> Vec<u8> {
    seq.iter().rev().map(|&mv| inv_move(mv)).collect()
}
/// Canonical order: never the same face twice in a row; of two opposite faces in a row, the lower one first.
#[inline]
pub fn canon_ok(last: u8, mv: u8) -> bool {
    if last == NONE {
        return true;
    }
    let (fl, fm) = (last / 3, mv / 3);
    !(fl == fm || (fl / 2 == fm / 2 && fl > fm))
}
/// A quarter turn of a face of axis y.
#[inline]
pub fn axis_quarter(mv: u8, y: usize) -> bool {
    mv % 3 != 1 && FACE_AXIS[(mv / 3) as usize] == y
}

/// Merge turns of one face (also across a turn of the opposite face) until nothing merges: the HTM form.
pub fn cancel(seq: &[u8]) -> Vec<u8> {
    let mut out: Vec<u8> = Vec::with_capacity(seq.len());
    for &m in seq {
        let f = m / 3;
        let amt = m % 3 + 1;
        let mut j = out.len();
        let mut merged = false;
        while j > 0 {
            let p = out[j - 1];
            let pf = p / 3;
            if pf == f {
                let tot = (p % 3 + 1 + amt) % 4;
                if tot == 0 {
                    out.remove(j - 1);
                } else {
                    out[j - 1] = 3 * f + tot - 1;
                }
                merged = true;
                break;
            }
            if pf / 2 != f / 2 {
                break;
            }
            j -= 1;
        }
        if !merged {
            out.push(m);
        }
    }
    out
}

pub struct Ctx {
    pub m: Model,
    pub mvc: Vec<Cubie>,
    pub rot_eo: [usize; 3],
    pub rot_pair: [[usize; 3]; 3],
    /// vmove[r][own move] = the same turn in the labels of view r; umove[r][view move] = own move
    pub vmove: Vec<[u8; 18]>,
    pub umove: Vec<[u8; 18]>,
    pub co_mv: Vec<[u16; 18]>,
    pub eo_mv: Vec<[u16; 18]>,
    pub sl_mv: Vec<[u16; 18]>,
    pub solved_sl: usize,
    pub eodist: Vec<u8>,
    pub drdist: Vec<u8>,
    pub drm_c: Vec<u8>,
    pub drm_e: Vec<u8>,
    /// mean EO-kept distance to DR of the EO-solved states with a given DRM: hmean[bad corners * 5 + bad edges / 2]
    pub hmean: Vec<f32>,
    pub dm: DrModel,
    /// per 48-subset: P(optimal finish <= k), k = 0..=20, and the mean; all DR states (htr-routes dist48.tsv)
    pub sub_cdf: Vec<[f64; 21]>,
    pub sub_mean: Vec<f64>,
    pub all_cdf: [f64; 21],
    pub all_mean: f64,
}

pub fn data_dir() -> String {
    std::env::var("ATTEMPTSIM_DATA").unwrap_or_else(|_| format!("{}/../data", env!("CARGO_MANIFEST_DIR")))
}

impl Ctx {
    pub fn new(exact_path: Option<&str>) -> Ctx {
        let dir = data_dir();
        let m = Model::load(&dir);
        let mvc: Vec<Cubie> = (0..18).map(|mv| m.turn(&SOLVED, mv)).collect();
        let rot_eo = [m.rot_for(0, 2, None), m.rot_for(1, 2, None), m.rot_for(2, 2, None)];
        let mut rot_pair = [[usize::MAX; 3]; 3];
        for x in 0..3 {
            for y in 0..3 {
                if x != y {
                    rot_pair[x][y] = m.rot_for(x, 1, Some((y, 2)));
                }
            }
        }
        let mut vmove = Vec::new();
        let mut umove = Vec::new();
        for r in 0..24 {
            let mut v = [0u8; 18];
            let mut u = [0u8; 18];
            for mv in 0..18 {
                let own = m.unview(r, mv);
                v[own] = mv as u8;
                u[mv] = own as u8;
            }
            vmove.push(v);
            umove.push(u);
        }

        // --- coordinate move tables (as coords() of the cubie model defines them)
        let mut co_mv = vec![[0u16; 18]; NCO];
        for co in 0..NCO {
            let mut c = SOLVED;
            let (mut v, mut s) = (co, 0u8);
            for i in 0..7 {
                c.ct[i] = (v % 3) as u8;
                v /= 3;
                s += c.ct[i];
            }
            c.ct[7] = (3 - s % 3) % 3;
            debug_assert_eq!(m.coords(&c).0, co);
            for mv in 0..18 {
                co_mv[co][mv] = m.coords(&m.turn(&c, mv)).0 as u16;
            }
        }
        let mut eo_mv = vec![[0u16; 18]; NEO];
        for eo in 0..NEO {
            let mut c = SOLVED;
            let mut par = 0u8;
            for i in 0..11 {
                c.ef[i] = ((eo >> i) & 1) as u8;
                par ^= c.ef[i];
            }
            c.ef[11] = par;
            for mv in 0..18 {
                eo_mv[eo][mv] = m.coords(&m.turn(&c, mv)).1 as u16;
            }
        }
        let mut sl_mv = vec![[0u16; 18]; NSL];
        let mut masks = vec![0usize; NSL];
        for mask in 0..(1usize << 12) {
            if mask.count_ones() == 4 {
                masks[m.comb[mask] as usize] = mask;
            }
        }
        let epieces: Vec<u8> = (0..12u8).filter(|&p| m.e_piece[p as usize]).collect();
        let others: Vec<u8> = (0..12u8).filter(|&p| !m.e_piece[p as usize]).collect();
        let mut home_mask = 0usize;
        for &p in &epieces {
            home_mask |= 1 << p;
        }
        let mut drm_e = vec![0u8; NSL];
        for sl in 0..NSL {
            let mut c = SOLVED;
            let (mut a, mut b) = (0, 0);
            for i in 0..12 {
                if masks[sl] >> i & 1 == 1 {
                    c.ep[i] = epieces[a];
                    a += 1;
                } else {
                    c.ep[i] = others[b];
                    b += 1;
                }
            }
            debug_assert_eq!(m.coords(&c).2, sl);
            for mv in 0..18 {
                sl_mv[sl][mv] = m.coords(&m.turn(&c, mv)).2 as u16;
            }
            drm_e[sl] = 2 * (4 - (masks[sl] & home_mask).count_ones() as u8);
        }
        let solved_sl = m.coords(&SOLVED).2;
        let drm_c: Vec<u8> = (0..NCO)
            .map(|co| {
                let (mut v, mut s, mut n) = (co, 0usize, 0u8);
                for _ in 0..7 {
                    if v % 3 != 0 {
                        n += 1;
                    }
                    s += v % 3;
                    v /= 3;
                }
                if s % 3 != 0 {
                    n += 1;
                }
                n
            })
            .collect();

        // --- EO distance (any turn)
        let mut eodist = vec![255u8; NEO];
        eodist[0] = 0;
        let mut frontier = vec![0usize];
        let mut d = 0u8;
        while !frontier.is_empty() {
            let mut next = Vec::new();
            for &e in &frontier {
                for mv in 0..18 {
                    let f = eo_mv[e][mv] as usize;
                    if eodist[f] == 255 {
                        eodist[f] = d + 1;
                        next.push(f);
                    }
                }
            }
            frontier = next;
            d += 1;
        }

        // --- EO-kept distance to DR
        let mut drdist = vec![255u8; NCO * NSL];
        drdist[solved_sl] = 0; // co = 0
        let mut frontier = vec![(0usize, solved_sl)];
        let mut d = 0u8;
        while !frontier.is_empty() {
            let mut next = Vec::new();
            for &(co, sl) in &frontier {
                for &mv in &EOKEEP {
                    let (c2, s2) = (co_mv[co][mv as usize] as usize, sl_mv[sl][mv as usize] as usize);
                    if drdist[c2 * NSL + s2] == 255 {
                        drdist[c2 * NSL + s2] = d + 1;
                        next.push((c2, s2));
                    }
                }
            }
            frontier = next;
            d += 1;
        }
        let mut hsum = vec![0f64; 45];
        let mut hcnt = vec![0f64; 45];
        for co in 0..NCO {
            for sl in 0..NSL {
                let k = drm_c[co] as usize * 5 + drm_e[sl] as usize / 2;
                hsum[k] += drdist[co * NSL + sl] as f64;
                hcnt[k] += 1.0;
            }
        }
        let hmean: Vec<f32> = (0..45).map(|k| if hcnt[k] > 0.0 { (hsum[k] / hcnt[k]) as f32 } else { 9.0 }).collect();

        // --- the DR group, with the exact table if given (1.3 GB in memory)
        let dm = DrModel::new(exact_path.map(std::path::Path::new), None);
        let cls = &dm.cls;

        // --- what the solver knows about a subset: the distribution of the optimal finish (all DR states)
        let nsub = cls.sub48_name.len();
        let mut cnt = vec![[0f64; 21]; nsub];
        let txt = std::fs::read_to_string(format!("{}/dist48.tsv", dir)).unwrap_or_else(|e| fatal!("dist48.tsv: {}", e));
        for line in txt.lines().skip(1) {
            let p: Vec<&str> = line.split('\t').collect();
            let k = cls.sub48_name.iter().position(|n| n == p[0]).unwrap_or_else(|| fatal!("dist48.tsv: unknown subset {}", p[0]));
            cnt[k][p[1].parse::<usize>().unwrap()] += p[2].parse::<f64>().unwrap();
        }
        let mut sub_cdf = vec![[0f64; 21]; nsub];
        let mut sub_mean = vec![0f64; nsub];
        let mut all = [0f64; 21];
        for k in 0..nsub {
            let tot: f64 = cnt[k].iter().sum();
            if tot == 0.0 {
                fatal!("dist48.tsv: subset {} missing", cls.sub48_name[k]);
            }
            let mut acc = 0.0;
            for dd in 0..21 {
                acc += cnt[k][dd];
                sub_cdf[k][dd] = acc / tot;
                sub_mean[k] += dd as f64 * cnt[k][dd] / tot;
                all[dd] += cnt[k][dd];
            }
        }
        let tot: f64 = all.iter().sum();
        if (tot - 19_508_428_800.0).abs() > 0.5 {
            fatal!("dist48.tsv: {} states, expected 19508428800", tot);
        }
        let mut all_cdf = [0f64; 21];
        let (mut acc, mut all_mean) = (0.0, 0.0);
        for dd in 0..21 {
            acc += all[dd];
            all_cdf[dd] = acc / tot;
            all_mean += dd as f64 * all[dd] / tot;
        }

        Ctx {
            m, mvc, rot_eo, rot_pair, vmove, umove, co_mv, eo_mv, sl_mv, solved_sl, eodist, drdist, drm_c, drm_e, hmean,
            dm, sub_cdf, sub_mean, all_cdf, all_mean,
        }
    }

    pub fn apply(&self, s: &Cubie, seq: &[u8]) -> Cubie {
        seq.iter().fold(*s, |a, &mv| self.m.turn(&a, mv as usize))
    }
    /// The state `I^-1 S N` reached with N on the normal side and I on the inverse side (own labels).
    pub fn state_ni(&self, s: &Cubie, n: &[u8], i: &[u8]) -> Cubie {
        let pre = self.apply(&SOLVED, &invert(i));
        pre.then(&self.apply(s, n))
    }
    #[inline]
    pub fn eo_of(c: &Cubie) -> usize {
        let mut e = 0usize;
        for i in 0..11 {
            e |= (c.ef[i] as usize) << i;
        }
        e
    }
    #[inline]
    pub fn h(&self, co: usize, sl: usize) -> f32 {
        self.hmean[self.drm_c[co] as usize * 5 + self.drm_e[sl] as usize / 2]
    }
    /// drtools coordinates (c, e, s) of a view state that is a DR on U/D.
    pub fn dr_coords(&self, v: &Cubie) -> Option<(usize, usize, usize)> {
        let (c, e, s) = self.m.dr_perms(v)?;
        Some((rank_perm(&c), rank_perm(&e), rank_perm(&s)))
    }
    #[inline]
    pub fn sub48(&self, c: usize, e: usize) -> usize {
        self.dm.sub48(c, e)
    }
    pub fn dr_inv(&self, st: (usize, usize, usize)) -> (usize, usize, usize) {
        (self.dm.core.cinv[st.0] as usize, self.dm.core.einv[st.1] as usize, self.dm.core.sinv[st.2] as usize)
    }
    pub fn has_exact(&self) -> bool {
        !self.dm.table.is_empty()
    }
    /// Exact optimal DR-move finish of a DR state (None if the table is not loaded).
    pub fn exact_depth(&self, st: (usize, usize, usize)) -> Option<u8> {
        if self.dm.table.is_empty() {
            None
        } else {
            Some(self.dm.depth(st.0, st.1, st.2))
        }
    }
    /// The smallest (c, e, s) among the 16 symmetric copies of a DR state: a name for the state that does not depend
    /// on which of the rotations about the DR axis was used to look at it.
    pub fn dr_canon(&self, st: (usize, usize, usize)) -> (usize, usize, usize) {
        (0..16)
            .map(|sym| (self.dm.core.csym[sym][st.0] as usize, self.dm.core.esym[sym][st.1] as usize, self.dm.core.ssym[sym][st.2] as usize))
            .min()
            .unwrap()
    }
}

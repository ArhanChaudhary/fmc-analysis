//! The ladder of "visible feature" quotients, from coarse to fine.
//! (Port of `drspec.h`; shared by the `ladder`, `query`, `sharp` and `parity` subcommands.)
//!
//! Each rung is a subgroup K of the DR group described by what it lets you see:
//!
//! ```text
//!   corners : none | HTR coset (420) | exact up to {x2,y2,z2}x{U2} (5040) | up to {x2,y2,z2} (10080) | exact (40320)
//!   edges   : none | which positions hold M-slice edges (70)
//!             | + U/D colour pattern of M and of S edges up to colour swap (630)
//!             | position of the four types white-M, yellow-M, white-S, yellow-S (2520)
//!             | 630 or 2520 classes + the two "double-swap" signs (x4)
//!   E parity: tracked or not
//! ```
//!
//! `T_K` = BFS distance in the coset graph K\G = fewest DR moves to make the visible part look solved.
//! Bound used for a state g:  `max( T_K(g), T_K(g^-1) )`.
//!
//! A table `T_<name>.u8` is one byte per class, indexed by [`Spec::idx`]; 0xFF marks an index that no
//! reachable state maps to.

use crate::class::{Classes, NCCOS, NEPAT};
use crate::core::{e_parity_flip, unrank_perm, Core, NC, NE, NMOVES};
use crate::quot::{CornerQuot, E630, NE630};
use rayon::prelude::*;
use std::fs::File;
use std::io::Read;
use std::path::Path;
use std::sync::atomic::{AtomicU8, Ordering::Relaxed};
use std::sync::Arc;

/// What a rung sees of the corners.
#[derive(Clone, Copy, PartialEq, Eq)]
pub enum CornerView {
    /// nothing
    None,
    /// the HTR corner coset (420)
    Htr,
    /// the permutation up to whole-cube half rotations and U2 (5040, the KF corner classes)
    VU2,
    /// the permutation up to whole-cube half rotations (10080, the K0 corner classes)
    V,
    /// the exact permutation (40320)
    Exact,
}

/// What a rung sees of the U/D-layer edges.
#[derive(Clone, Copy, PartialEq, Eq)]
pub enum EdgeView {
    /// nothing
    None,
    /// which positions hold M-slice edges (70)
    Mask,
    /// the 630 classes of KF / K0
    E630,
    /// layer and slice type of every edge (2520)
    E2520,
    /// 630 classes + double-swap signs (2520)
    E630S,
    /// 2520 classes + double-swap signs (10080)
    E2520S,
}

/// One rung of the ladder.
// Not every table is read by the current subcommands; they are all kept, as in the C header.
#[allow(dead_code)]
pub struct Spec {
    pub name: &'static str,
    /// what the rung sees, in words
    pub desc: &'static str,
    pub cm: CornerView,
    pub em: EdgeView,
    /// whether the E-slice parity is tracked
    pub par: bool,
    /// number of corner classes / edge classes
    pub nc: usize,
    pub ne: usize,
    /// corner coordinate -> corner class ; U/D-edge coordinate -> edge class
    pub cmap: Arc<[u16]>,
    pub emap: Arc<[u16]>,
    /// action of the moves on the classes: `cmv[class * NMOVES + m]`
    pub cmv: Vec<u16>,
    pub emv: Vec<u16>,
    /// number of table entries: `nc * ne * (2 if par else 1)`
    pub n: usize,
    /// the distance table; empty until [`Spec::compute_table`] or [`Spec::load_table`] is called
    pub t: Vec<u8>,
}

/// The rungs, in the order of the C table (this order is also the order of the output columns).
const RUNGS: [(&str, &str, CornerView, EdgeView, bool); 13] = [
    (
        "htr",
        "HTR coset only (optimal DR->HTR length)",
        CornerView::Htr,
        EdgeView::Mask,
        false,
    ),
    (
        "c",
        "corners exact, edges ignored (optimal corner solution length L)",
        CornerView::Exact,
        EdgeView::None,
        false,
    ),
    (
        "c+p",
        "corners exact + E-slice parity",
        CornerView::Exact,
        EdgeView::None,
        true,
    ),
    (
        "e630+p",
        "edges only: bad-edge positions + colour patterns + E parity",
        CornerView::None,
        EdgeView::E630,
        true,
    ),
    (
        "c+bad",
        "corners exact + which edges are bad",
        CornerView::Exact,
        EdgeView::Mask,
        false,
    ),
    (
        "c+bad+p",
        "corners exact + which edges are bad + E parity",
        CornerView::Exact,
        EdgeView::Mask,
        true,
    ),
    (
        "KF",
        "FakeMMAP/Rodney features: corners up to rotation and U2, 630 edge classes, E parity",
        CornerView::VU2,
        EdgeView::E630,
        true,
    ),
    ("K0", "same without U2", CornerView::V, EdgeView::E630, true),
    (
        "c+630+p",
        "corners exact + 630 edge classes + E parity",
        CornerView::Exact,
        EdgeView::E630,
        true,
    ),
    (
        "c+2520+p",
        "corners exact + layer and slice type of every U/D edge + E parity",
        CornerView::Exact,
        EdgeView::E2520,
        true,
    ),
    (
        "K0+F",
        "K0 + double-swap parity (generalises FakeMMAP's OBL++ sheet)",
        CornerView::V,
        EdgeView::E630S,
        false,
    ),
    (
        "c+630+F",
        "corners exact + 630 edge classes + double-swap parity",
        CornerView::Exact,
        EdgeView::E630S,
        false,
    ),
    (
        "c+2520+F",
        "corners exact + layer/slice type of every U/D edge + double-swap parity",
        CornerView::Exact,
        EdgeView::E2520S,
        false,
    ),
];

impl Spec {
    /// Table index of (corner class, edge class, E-slice parity); the parity is ignored if the rung does not track it.
    #[inline]
    pub fn idx(&self, cc: usize, ee: usize, par: usize) -> usize {
        if self.par {
            (cc * self.ne + ee) * 2 + par
        } else {
            cc * self.ne + ee
        }
    }

    /// Table index of the state with corner coordinate `c`, U/D-edge coordinate `e`, E-slice parity `par`.
    #[inline]
    pub fn class_of(&self, c: usize, e: usize, par: usize) -> usize {
        self.idx(self.cmap[c] as usize, self.emap[e] as usize, par)
    }

    /// Move tables on classes via representatives, then verified on every element (the C `build_moves`).
    fn build_moves(&mut self, core: &Core) {
        let mut crep: Vec<Option<usize>> = vec![None; self.nc];
        let mut erep: Vec<Option<usize>> = vec![None; self.ne];
        for c in 0..NC {
            crep[self.cmap[c] as usize].get_or_insert(c);
            erep[self.emap[c] as usize].get_or_insert(c);
        }
        let rep = |r: Option<usize>| r.unwrap_or_else(|| fatal!("{}: empty class", self.name));
        self.cmv = (0..self.nc * NMOVES)
            .map(|x| self.cmap[core.cmove[x % NMOVES][rep(crep[x / NMOVES])] as usize])
            .collect();
        self.emv = (0..self.ne * NMOVES)
            .map(|x| self.emap[core.emove[x % NMOVES][rep(erep[x / NMOVES])] as usize])
            .collect();
        for c in 0..NC {
            for m in 0..NMOVES {
                if self.cmap[core.cmove[m][c] as usize]
                    != self.cmv[self.cmap[c] as usize * NMOVES + m]
                    || self.emap[core.emove[m][c] as usize]
                        != self.emv[self.emap[c] as usize * NMOVES + m]
                {
                    fatal!("{}: class action not well defined", self.name);
                }
            }
        }
    }

    /// Fill the table by a breadth-first search from the solved class (the C `bfs`).
    ///
    /// Level-synchronous and parallel over corner classes: every thread scans for entries equal to the
    /// current depth `d` and writes `d + 1` into unvisited neighbours.  Two threads may write the same
    /// entry, but they write the same value, so the result does not depend on the scheduling.
    pub fn compute_table(&mut self) {
        let planes = if self.par { 2 } else { 1 };
        let t: Vec<AtomicU8> = (0..self.n).map(|_| AtomicU8::new(0xFF)).collect();
        t[self.class_of(0, 0, 0)].store(0, Relaxed);
        let mut d: u8 = 0;
        loop {
            let found: usize = (0..self.nc)
                .into_par_iter()
                .map(|cc| {
                    let t: &[AtomicU8] = &t;
                    let mut found = 0;
                    let cmv = &self.cmv[cc * NMOVES..(cc + 1) * NMOVES];
                    // the entries of corner class cc are contiguous: entry (ee, p) sits at offset ee * planes + p
                    let first = self.idx(cc, 0, 0);
                    for (offset, entry) in t[first..first + self.ne * planes].iter().enumerate() {
                        if entry.load(Relaxed) != d {
                            continue;
                        }
                        let (ee, p) = (offset / planes, offset % planes);
                        let emv = &self.emv[ee * NMOVES..(ee + 1) * NMOVES];
                        for m in 0..NMOVES {
                            let j =
                                self.idx(cmv[m] as usize, emv[m] as usize, p ^ e_parity_flip(m));
                            if t[j].load(Relaxed) == 0xFF {
                                t[j].store(d + 1, Relaxed);
                                found += 1;
                            }
                        }
                    }
                    found
                })
                .sum();
            if found == 0 {
                break;
            }
            d += 1;
        }
        // AtomicU8 -> u8 (same layout; the standard library converts the vector in place)
        self.t = t.into_iter().map(AtomicU8::into_inner).collect();
    }

    /// Read the table from `<tabdir>/T_<name>.u8`.
    pub fn load_table(&mut self, tabdir: &Path) {
        let path = tabdir.join(format!("T_{}.u8", self.name));
        let mut file =
            File::open(&path).unwrap_or_else(|_| fatal!("missing table {}", path.display()));
        let mut t = vec![0u8; self.n];
        if file.read_exact(&mut t).is_err() {
            fatal!("short table {}", path.display());
        }
        self.t = t;
    }
}

/// All rungs with their class maps and class move tables (tables `t` still empty).
pub struct Ladder {
    pub specs: Vec<Spec>,
}

impl Ladder {
    /// The C `specs_init`, without the table part (see [`Spec::compute_table`], [`Spec::load_table`]).
    pub fn new(core: &Core, classes: &Classes, e630: &E630) -> Ladder {
        let qf = CornerQuot::new(core, classes, true);
        let q0 = CornerQuot::new(core, classes, false);

        // trivial maps and 16-bit copies of the HTR maps
        let map_none: Arc<[u16]> = vec![0u16; NC].into();
        let map_exact: Arc<[u16]> = (0..NC as u16).collect::<Vec<u16>>().into();
        let map_ccos: Arc<[u16]> = classes.ccos.clone().into();
        let map_epat: Arc<[u16]> = classes
            .epat
            .iter()
            .map(|&x| x as u16)
            .collect::<Vec<u16>>()
            .into();
        let map_qf: Arc<[u16]> = qf.ccls.clone().into();
        let map_q0: Arc<[u16]> = q0.ccls.clone().into();
        let map_e630: Arc<[u16]> = e630.cls.clone().into();

        // 2520 classes: for every position the slice type (M/S) and home layer (U/D) of the edge sitting there
        let mut e2520 = vec![0u16; NE];
        {
            let mut idx: Vec<Option<u16>> = vec![None; 1 << 16];
            let mut n2520 = 0u16;
            for e in 0..NE {
                let p = unrank_perm::<8>(e);
                let mut key = 0usize;
                for k in 0..8 {
                    key |= ((((p[k] & 1) << 1) | (p[k] >> 2)) as usize) << (2 * k);
                }
                e2520[e] = *idx[key].get_or_insert_with(|| {
                    n2520 += 1;
                    n2520 - 1
                });
            }
            if n2520 != 2520 {
                fatal!("2520 classes expected, got {}", n2520);
            }
        }
        // sign-split refinements: sM / sS = parity of the arrangement of the four M-slice (S-slice) edges read
        // in position order.  Together with the corner class they carry FakeMMAP's "F-parity / R-parity" (the
        // double-swap or H-perm parity, T12070, doc 428).
        let mut e630s = vec![0u16; NE];
        let mut e2520s = vec![0u16; NE];
        for e in 0..NE {
            let p = unrank_perm::<8>(e);
            let mut seq: [Vec<u8>; 2] = [Vec::new(), Vec::new()]; // the M pieces and the S pieces in position order
            for k in 0..8 {
                seq[(p[k] & 1) as usize].push(p[k] >> 1);
            }
            let sign = |q: &[u8]| -> u16 {
                let mut inversions = 0;
                for i in 0..q.len() {
                    for j in i + 1..q.len() {
                        if q[i] > q[j] {
                            inversions += 1;
                        }
                    }
                }
                inversions & 1
            };
            let signs = sign(&seq[0]) * 2 + sign(&seq[1]);
            e630s[e] = e630.cls[e] * 4 + signs;
            e2520s[e] = e2520[e] * 4 + signs;
        }
        let map_e2520: Arc<[u16]> = e2520.into();
        let map_e630s: Arc<[u16]> = e630s.into();
        let map_e2520s: Arc<[u16]> = e2520s.into();

        let mut specs = Vec::with_capacity(RUNGS.len());
        for (name, desc, cm, em, par) in RUNGS {
            let (cmap, nc) = match cm {
                CornerView::None => (map_none.clone(), 1),
                CornerView::Htr => (map_ccos.clone(), NCCOS),
                CornerView::VU2 => (map_qf.clone(), qf.ncc),
                CornerView::V => (map_q0.clone(), q0.ncc),
                CornerView::Exact => (map_exact.clone(), NC),
            };
            let (emap, ne) = match em {
                EdgeView::None => (map_none.clone(), 1),
                EdgeView::Mask => (map_epat.clone(), NEPAT),
                EdgeView::E630 => (map_e630.clone(), NE630),
                EdgeView::E2520 => (map_e2520.clone(), 2520),
                EdgeView::E630S => (map_e630s.clone(), NE630 * 4),
                EdgeView::E2520S => (map_e2520s.clone(), 2520 * 4),
            };
            let n = nc * ne * if par { 2 } else { 1 };
            let mut spec = Spec {
                name,
                desc,
                cm,
                em,
                par,
                nc,
                ne,
                cmap,
                emap,
                cmv: Vec::new(),
                emv: Vec::new(),
                n,
                t: Vec::new(),
            };
            spec.build_moves(core);
            specs.push(spec);
        }
        Ladder { specs }
    }

    /// Position of the rung called `name` (stops the program if there is none).
    pub fn index_of(&self, name: &str) -> usize {
        self.specs
            .iter()
            .position(|s| s.name == name)
            .unwrap_or_else(|| fatal!("no spec {}", name))
    }

    /// Load every table from `tabdir`.
    pub fn load_all(&mut self, tabdir: &Path) {
        for spec in &mut self.specs {
            spec.load_table(tabdir);
        }
    }
}

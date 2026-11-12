//! Everything a route computation needs about one DR state, on top of the first study's model
//! (`core.rs`, `class.rs`, `reduced.rs` of judging-a-dr/research/drtools, included by `#[path]`).
//!
//! * a state is `(c, e, s)`: corner, U/D-edge and E-slice coordinates (ranks of the permutations, core.rs)
//! * `depth(c, e, s)`: exact optimal DR finish, from the Lean-checked table `lean_exact_table.u8`
//!   (one byte per symmetry-reduced state, index `(class * 40320 + e') * 12 + s12`, see reduced.rs)
//! * `ls(c, e)`: optimal leave-slice finish (corners and U/D edges solved, E slice as it falls), from `ls_depth.u8`
//! * labels: the corner subset of the state's own corner coset (study 1's 14 names; for 3 and 4 quarter turns the
//!   letter a/b depends on the side) and the number of bad edges in the frame with <= 4 bad corners, as in
//!   "4a3 2e". Labels only change at quarter turns: they are functions of the HTR coset H·g, and
//!   are also unchanged by multiplying by a half turn on the left.
//! * H membership (the state is in HTR): corner coset = edge pattern = those of the solved cube.

use crate::class::{Classes, NCCOS, NEPAT, SUBSET_NAME};
use crate::core::{Core, MOVE_IS_QT, NC, NE, NMOVES};
use crate::reduced::{CornerClasses, SliceIndex};
use std::fs::File;
use std::io::Read;
use std::path::Path;

pub const NLABEL: usize = 14 * 5;
/// Face of each DR move (U D R L F B = 0..5).
pub const FACE: [u8; NMOVES] = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5];
pub const R2: usize = 6;

pub fn label_name(l: u8) -> String {
    format!("{} {}e", SUBSET_NAME[(l / 5) as usize], 2 * (l % 5))
}

pub struct Model {
    pub core: Core,
    pub cls: Classes,
    pub cc: CornerClasses,
    pub sl: SliceIndex,
    pub table: Vec<u8>,
    pub ls: Vec<u8>,
    /// label of HTR coset (a, b)
    pub lab: Vec<[u8; NEPAT]>,
    pub c0: usize,
    pub e0: usize,
    /// corner-only and edge-only lower bounds for the shortest NISS HTR (see `niss_htr`)
    nc_bound: Vec<u8>,
    ne_bound: Vec<u8>,
}

fn read_all(p: &Path) -> Vec<u8> {
    let mut v = Vec::new();
    File::open(p)
        .and_then(|mut f| f.read_to_end(&mut v))
        .unwrap_or_else(|e| fatal!("cannot read {}: {}", p.display(), e));
    v
}

impl Model {
    pub fn new(exact: Option<&Path>, ls: Option<&Path>) -> Model {
        let core = Core::new();
        let cls = Classes::new(&core);
        let cc = CornerClasses::new(&core);
        let sl = SliceIndex::new(&core);
        let table = exact.map(read_all).unwrap_or_default();
        if exact.is_some() && table.len() != cc.nclass * NE * 12 {
            fatal!("exact table has {} bytes, expected {}", table.len(), cc.nclass * NE * 12);
        }
        let lsv = ls.map(read_all).unwrap_or_default();
        if ls.is_some() && lsv.len() != cc.nclass * NE {
            fatal!("leave-slice table has the wrong size");
        }
        let mut lab = vec![[0u8; NEPAT]; NCCOS];
        for a in 0..NCCOS {
            for b in 0..NEPAT {
                let (nc, ne) = (cls.cc_nbad[a], cls.ep_nbad[b]);
                let ne = if nc > 4 || (nc == 4 && ne > 4) { 8 - ne } else { ne };
                lab[a][b] = cls.cc_subset[a] * 5 + ne / 2;
            }
        }
        let (c0, e0) = (cls.ccos[0] as usize, cls.epat[0] as usize);
        let mut m = Model { core, cls, cc, sl, table, ls: lsv, lab, c0, e0, nc_bound: vec![], ne_bound: vec![] };
        m.build_niss_bounds();
        m
    }

    #[inline]
    pub fn depth(&self, c: usize, e: usize, s: usize) -> u8 {
        let k = self.cc.cclass[c] as usize;
        let sym = self.cc.csymto[c] as usize;
        let i = (k * NE + self.core.esym[sym][e] as usize) * 12
            + self.sl.to12[self.core.ssym[sym][s] as usize] as usize;
        self.table[i]
    }
    #[inline]
    pub fn lsdepth(&self, c: usize, e: usize) -> u8 {
        let k = self.cc.cclass[c] as usize;
        let sym = self.cc.csymto[c] as usize;
        self.ls[k * NE + self.core.esym[sym][e] as usize]
    }
    #[inline]
    pub fn label(&self, c: usize, e: usize) -> u8 {
        self.lab[self.cls.ccos[c] as usize][self.cls.epat[e] as usize]
    }
    /// label of the inverse state
    #[inline]
    pub fn label_inv(&self, c: usize, e: usize) -> u8 {
        self.label(self.core.cinv[c] as usize, self.core.einv[e] as usize)
    }
    #[inline]
    pub fn in_h(&self, c: usize, e: usize) -> bool {
        self.cls.ccos[c] as usize == self.c0 && self.cls.epat[e] as usize == self.e0
    }
    /// shortest linear DR->HTR on this side
    #[inline]
    pub fn htr(&self, c: usize, e: usize) -> u8 {
        self.cls.htr_dist[self.cls.ccos[c] as usize][self.cls.epat[e] as usize]
    }
    #[inline]
    pub fn mv(&self, m: usize, st: (usize, usize, usize)) -> (usize, usize, usize) {
        (
            self.core.cmove[m][st.0] as usize,
            self.core.emove[m][st.1] as usize,
            self.core.smove[m][st.2] as usize,
        )
    }
    pub fn sub48(&self, c: usize, e: usize) -> usize {
        self.cls.sub48[self.cls.ccos[c] as usize][self.cls.epat[e] as usize] as usize
    }

    /// Lower bounds for `niss_htr`: the same quantity for corners alone and for U/D edges alone.
    /// `N(g) = min over A of |A| + htr(inverse of g·A)`, computed by relaxation over the 40320 corner (edge) permutations.
    fn build_niss_bounds(&mut self) {
        // corner-only / edge-only linear HTR distance of a coset
        let bfs = |nn: usize, mvt: &dyn Fn(usize, usize) -> usize, start: usize| -> Vec<u8> {
            let mut d = vec![0xFFu8; nn];
            d[start] = 0;
            let mut q = vec![start];
            let mut h = 0;
            while h < q.len() {
                let x = q[h];
                h += 1;
                for m in 0..NMOVES {
                    let y = mvt(x, m);
                    if d[y] == 0xFF {
                        d[y] = d[x] + 1;
                        q.push(y);
                    }
                }
            }
            d
        };
        let cls = &self.cls;
        let rc = bfs(NCCOS, &|a, m| cls.ccos_mv[a][m], self.c0);
        let re = bfs(NEPAT, &|b, m| cls.epat_mv[b][m], self.e0);
        let core = &self.core;
        let relax = |n: usize, init: &dyn Fn(usize) -> u8, mv: &dyn Fn(usize, usize) -> usize| -> Vec<u8> {
            let mut v: Vec<u8> = (0..n).map(init).collect();
            loop {
                let mut changed = false;
                for x in 0..n {
                    for m in 0..NMOVES {
                        let y = mv(x, m);
                        if v[y] + 1 < v[x] {
                            v[x] = v[y] + 1;
                            changed = true;
                        }
                    }
                }
                if !changed {
                    break;
                }
            }
            v
        };
        self.nc_bound = relax(NC, &|c| rc[cls.ccos[core.cinv[c] as usize] as usize], &|c, m| core.cmove[m][c] as usize);
        self.ne_bound = relax(NE, &|e| re[cls.epat[core.einv[e] as usize] as usize], &|e, m| core.emove[m][e] as usize);
    }

    /// Shortest NISS HTR: min |A| + |B| over A done on normal and B on inverse with (X·A)^-1·B in H.
    /// (Starting on inverse gives the same minimum: (X^-1·B)^-1·A = B^-1·X·A.)  IDA* with the corner-only and
    /// edge-only versions of the same quantity as the bound.
    pub fn niss_htr(&self, c: usize, e: usize) -> u8 {
        let ub = self.htr(c, e).min(self.htr(self.core.cinv[c] as usize, self.core.einv[e] as usize));
        let h0 = self.nc_bound[c].max(self.ne_bound[e]);
        for t in h0..ub {
            if self.niss_dfs(c, e, 0, t, 0xFF, 0xFF) {
                return t;
            }
        }
        ub
    }
    fn niss_dfs(&self, c: usize, e: usize, g: u8, t: u8, lf: u8, la: u8) -> bool {
        if g + self.nc_bound[c].max(self.ne_bound[e]) > t {
            return false;
        }
        if g + self.htr(self.core.cinv[c] as usize, self.core.einv[e] as usize) <= t {
            return true;
        }
        for m in 0..NMOVES {
            if !canonical_next(m, lf, la) {
                continue;
            }
            let (c2, e2) = (self.core.cmove[m][c] as usize, self.core.emove[m][e] as usize);
            if self.niss_dfs(c2, e2, g + 1, t, FACE[m], axis_run(m, lf, la)) {
                return true;
            }
        }
        false
    }
}

/// Canonical sequences: never the same face twice in a row, never three moves in a row on one axis
/// (so "U D" and "D U" are both kept, "U D U" is not).  `lf` = last face, `la` = axis of the last two moves if both
/// were on one axis (0xFF otherwise).
#[inline]
pub fn canonical_next(m: usize, lf: u8, la: u8) -> bool {
    let f = FACE[m];
    f != lf && f / 2 != la
}
#[inline]
pub fn axis_run(m: usize, lf: u8, _la: u8) -> u8 {
    if lf != 0xFF && lf / 2 == FACE[m] / 2 {
        FACE[m] / 2
    } else {
        0xFF
    }
}
#[inline]
pub fn is_qt(m: u8) -> bool {
    MOVE_IS_QT[m as usize]
}

/// splitmix64
pub struct Rng(pub u64);
impl Rng {
    pub fn next(&mut self) -> u64 {
        self.0 = self.0.wrapping_add(0x9E3779B97F4A7C15);
        let mut z = self.0;
        z = (z ^ (z >> 30)).wrapping_mul(0xBF58476D1CE4E5B9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94D049BB133111EB);
        z ^ (z >> 31)
    }
    pub fn below(&mut self, n: usize) -> usize {
        (self.next() % n as u64) as usize
    }
}

/// Uniform sampling inside one of the 48 subsets: every HTR coset (a, b) holds 96 x 576 x 12 states, so pick a
/// coset of the subset uniformly, then a corner permutation of corner coset a, an edge permutation of pattern b and
/// an E-slice permutation of the forced parity, each uniformly.
pub struct Sampler {
    pub pairs: Vec<Vec<(usize, usize)>>,
    cof: Vec<Vec<usize>>,
    eof: Vec<Vec<usize>>,
    /// gaps fork: if the environment variable GAPS_STATES names a file of "c e s" lines (one DR state each, ranks as
    /// in core.rs), every subcommand works on those states instead of uniform draws: per subset, the listed states of
    /// that subset in file order, state i of the subset = the i-th such line (the uniform `n` is ignored).
    pub list: Option<Vec<Vec<(usize, usize, usize)>>>,
}
impl Sampler {
    pub fn new(m: &Model) -> Sampler {
        let nsub = m.cls.sub48_name.len();
        let mut pairs = vec![vec![]; nsub];
        for a in 0..NCCOS {
            for b in 0..NEPAT {
                pairs[m.cls.sub48[a][b] as usize].push((a, b));
            }
        }
        let mut cof = vec![vec![]; NCCOS];
        for c in 0..NC {
            cof[m.cls.ccos[c] as usize].push(c);
        }
        let mut eof = vec![vec![]; NEPAT];
        for e in 0..NE {
            eof[m.cls.epat[e] as usize].push(e);
        }
        let list = std::env::var("GAPS_STATES").ok().map(|p| {
            let txt = std::fs::read_to_string(&p).unwrap_or_else(|e| fatal!("cannot read {}: {}", p, e));
            let mut l = vec![vec![]; nsub];
            for line in txt.lines() {
                if line.starts_with('#') || line.trim().is_empty() {
                    continue;
                }
                let v: Vec<usize> = line.split_whitespace().take(3).map(|x| x.parse().unwrap()).collect();
                let (c, e, s) = (v[0], v[1], v[2]);
                if (m.core.cpar[c] ^ m.core.epar[e]) != m.core.spar[s] {
                    fatal!("state {} {} {} has the wrong parity", c, e, s);
                }
                l[m.sub48(c, e)].push((c, e, s));
            }
            eprintln!("GAPS_STATES {}: {} states", p, l.iter().map(|x| x.len()).sum::<usize>());
            l
        });
        Sampler { pairs, cof, eof, list }
    }
    /// number of states of subset `sub` to process
    pub fn count(&self, sub: usize, n: usize) -> usize {
        match &self.list {
            Some(l) => l[sub].len(),
            None => n,
        }
    }
    /// state i of subset `sub`: the listed one, or a uniform draw
    pub fn draw_i(&self, m: &Model, sub: usize, i: usize, rng: &mut Rng) -> (usize, usize, usize) {
        match &self.list {
            Some(l) => l[sub][i],
            None => self.draw(m, sub, rng),
        }
    }
    pub fn draw(&self, m: &Model, sub: usize, rng: &mut Rng) -> (usize, usize, usize) {
        let (a, b) = self.pairs[sub][rng.below(self.pairs[sub].len())];
        let c = self.cof[a][rng.below(self.cof[a].len())];
        let e = self.eof[b][rng.below(self.eof[b].len())];
        let par = (m.core.cpar[c] ^ m.core.epar[e]) as usize;
        let s = m.sl.from12[par][rng.below(12)] as usize;
        (c, e, s)
    }
}

pub fn moves_str(ms: &[u8]) -> String {
    ms.iter().map(|&m| crate::core::MOVE_NAME[m as usize]).collect::<Vec<_>>().join(" ")
}

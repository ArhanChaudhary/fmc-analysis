//! Finishing a DR-1s: the shortest solution of the form
//!
//!     (turns that keep the DR-1s) (one slice turn, two face turns) (finish of the real DR in DR moves)
//!
//! with the exact optimal finish of every DR state taken from the first study's table
//! (`judging-a-dr/research/data/lean_exact_table.u8`, one byte per symmetry-reduced DR state).
//!
//! A state is handled in the view where its corner colours are the U/D colours (a whole-cube rotation), so that the
//! real DR it reaches is the usual one on U/D; its kind then comes from `out/kinds.tsv`.

use crate::class::{Classes, SUBSET_NAME};
use crate::core::{rank_perm, Core};
use crate::cubie::{Cubie, Model, SOLVED};
use crate::reduced::{CornerClasses, SliceIndex, ROW};
use crate::Tables;
use std::collections::HashMap;
use std::fs;

pub struct Exact {
    pub core: Core,
    pub cc: CornerClasses,
    pub si: SliceIndex,
    pub cls: Classes,
    tab: Vec<u8>,
}

impl Exact {
    pub fn load(path: &str) -> Exact {
        let core = Core::new();
        let cc = CornerClasses::new(&core);
        let si = SliceIndex::new(&core);
        let cls = Classes::new(&core);
        let tab = fs::read(path).expect("exact table");
        assert_eq!(tab.len(), cc.nclass * ROW);
        Exact { core, cc, si, cls, tab }
    }

    /// Optimal finish (DR moves) of the DR state given by its three permutations.
    #[inline]
    pub fn depth(&self, c: &[u8; 8], e: &[u8; 8], s: &[u8; 4]) -> u8 {
        let (cr, er, sr) = (rank_perm(c), rank_perm(e), rank_perm(s));
        let (k, sym) = (self.cc.cclass[cr] as usize, self.cc.csymto[cr] as usize);
        self.tab[k * ROW + self.core.esym[sym][er] as usize * 12 + self.si.to12[self.core.ssym[sym][sr] as usize] as usize]
    }

    /// An optimal finish of a DR state, as face turns (0..18): walk down the exact table.
    pub fn path(&self, c: &[u8; 8], e: &[u8; 8], s: &[u8; 4]) -> Vec<usize> {
        const DR_MOVE: [usize; 10] = [0, 1, 2, 3, 4, 5, 7, 10, 13, 16]; // U U2 U' D D2 D' R2 L2 F2 B2
        let mut st = crate::core::St { c: *c, e: *e, s: *s };
        let mut d = self.depth(c, e, s);
        let mut out = Vec::new();
        while d > 0 {
            let mut stepped = false;
            for mv in 0..10 {
                let nx = st.apply_move(mv);
                if self.depth(&nx.c, &nx.e, &nx.s) == d - 1 {
                    st = nx;
                    d -= 1;
                    out.push(DR_MOVE[mv]);
                    stepped = true;
                    break;
                }
            }
            assert!(stepped, "exact table is not a distance");
        }
        out
    }

    /// Corner subset name of a DR corner permutation ("4a1", "2c3", ..., with 4a3/4b3 and 4a4/4b4 kept apart).
    pub fn corner_subset(&self, c: &[u8; 8]) -> &'static str {
        SUBSET_NAME[self.cls.cc_subset[self.cls.ccos[rank_perm(c)] as usize] as usize]
    }
}

#[derive(Clone, Copy, Debug)]
pub struct Kind {
    pub faces: u8,  // 0 R/L, 1 U/D, 2 F/B: the faces the corners are oriented on
    pub flips: u8,
    pub slices: u8,
    pub turns: u8,  // fewest turns to a real DR
}

pub fn load_kinds(path: &str) -> HashMap<(usize, usize, usize), Kind> {
    let mut out = HashMap::new();
    for line in fs::read_to_string(path).expect("kinds.tsv").lines().skip(1) {
        let f: Vec<&str> = line.split('\t').collect();
        let faces = match f[3] {
            "RL" => 0,
            "UD" => 1,
            _ => 2,
        };
        out.insert(
            (f[0].parse().unwrap(), f[1].parse().unwrap(), f[2].parse().unwrap()),
            Kind { faces, flips: f[4].parse().unwrap(), slices: f[6].parse().unwrap(), turns: f[7].parse().unwrap() },
        );
    }
    out
}

pub struct Finisher<'a> {
    pub m: &'a Model,
    pub t: &'a Tables,
    pub ex: &'a Exact,
    pub kinds: &'a HashMap<(usize, usize, usize), Kind>,
    /// for corners oriented on R/L (index 0) or F/B (index 1): the eo value at which one slice turn gives the DR
    direct: [usize; 2],
    to_ud: [usize; 3], // rotation carrying colour axis c to U/D
}

/// Best solution found: total turns, turns before the slice, the turns before the slice, the slice, finish length.
#[derive(Clone, Debug)]
pub struct Best {
    pub total: u8,
    pub setup: Vec<usize>,
    pub slice: [usize; 2],
    pub finish: u8,
    pub rot: usize,
    pub inverse: bool,
}

impl<'a> Finisher<'a> {
    pub fn new(m: &'a Model, t: &'a Tables, ex: &'a Exact, kinds: &'a HashMap<(usize, usize, usize), Kind>) -> Finisher<'a> {
        let mut direct = [usize::MAX; 2];
        for (&(_, eo, _), k) in kinds {
            if k.slices == 1 && k.turns == 2 {
                let i = if k.faces == 0 { 0 } else { 1 };
                assert!(direct[i] == usize::MAX);
                direct[i] = eo;
            }
        }
        let to_ud = [m.rot_for(0, 1, None), 0, m.rot_for(2, 1, None)];
        assert!(m.rot_axes[0] == [0, 1, 2]);
        Finisher { m, t, ex, kinds, direct, to_ud }
    }

    /// The views (rotation index, rotated state, kind) in which the state is a DR-xs for the U/D colours.
    pub fn views(&self, x: &Cubie) -> Vec<(usize, Cubie, Kind)> {
        let mut out = Vec::new();
        for c in 0..3 {
            let v = self.m.conj(x, self.to_ud[c]);
            if let Some(k) = self.kinds.get(&self.m.coords(&v)) {
                out.push((self.to_ud[c], v, *k));
            }
        }
        out
    }

    /// Over all setups of at most `r` turns that keep the DR-1s: fewest of setup + slice (2) + optimal DR finish.
    /// `v` must be a DR-1s in the U/D-colour view with corners on faces `faces`.
    fn one_side(&self, v: &Cubie, faces: u8, r: usize, best: &mut Option<Best>, rot: usize, inverse: bool) {
        // the ten turns that keep the corners oriented on `faces`: any turn of those two faces, half turns of the rest
        let mut allowed = Vec::new();
        for face in 0..6 {
            let axis = [1u8, 1, 0, 0, 2, 2][face];
            for q in 0..3 {
                if axis == faces || q == 1 {
                    allowed.push(3 * face + q);
                }
            }
        }
        let slice_faces: [usize; 2] = if faces == 2 { [2, 3] } else { [4, 5] }; // R L, or F B
        let direct = self.direct[if faces == 0 { 0 } else { 1 }];
        let (_, eo0, _) = self.m.coords(v);
        let mut seq: Vec<usize> = Vec::with_capacity(r);
        self.dfs(v, eo0, &allowed, slice_faces, direct, r, &mut seq, best, rot, inverse);
    }

    #[allow(clippy::too_many_arguments)]
    fn dfs(&self, v: &Cubie, eo: usize, allowed: &[usize], sf: [usize; 2], direct: usize, left: usize, seq: &mut Vec<usize>,
           best: &mut Option<Best>, rot: usize, inverse: bool) {
        if eo == direct {
            let y = self.m.apply(v, seq);
            for i in [0usize, 2] {
                for j in [0usize, 2] {
                    let z = self.m.turn(&self.m.turn(&y, 3 * sf[0] + i), 3 * sf[1] + j);
                    let (c, e, s) = self.m.dr_perms(&z).expect("slice did not give a DR");
                    let d = self.ex.depth(&c, &e, &s);
                    let total = seq.len() as u8 + 2 + d;
                    if best.as_ref().map_or(true, |b| total < b.total) {
                        *best = Some(Best { total, setup: seq.clone(), slice: [3 * sf[0] + i, 3 * sf[1] + j], finish: d, rot, inverse });
                    }
                }
            }
        }
        if left == 0 {
            return;
        }
        // a longer setup can only help if setup + 2 can still beat the best
        if let Some(b) = best {
            if seq.len() + 1 + 2 >= b.total as usize {
                return;
            }
        }
        let last = seq.last().copied();
        for &mv in allowed {
            if let Some(l) = last {
                let (fl, fm) = (l / 3, mv / 3);
                if fl == fm || (fl / 2 == fm / 2 && fl > fm) {
                    continue; // same face twice, or opposite faces in the wrong order
                }
            }
            seq.push(mv);
            self.dfs(v, self.t.eo[eo][mv] as usize, allowed, sf, direct, left - 1, seq, best, rot, inverse);
            seq.pop();
        }
    }

    /// Shortest finish of a DR-1s of the form setup, slice, DR finish (exact), searching from both ends.
    /// `cap` limits the setup on the state's own side when `own_side_only` (the by-hand version).
    pub fn finish_1s(&self, x: &Cubie) -> Option<Best> {
        let xi = x.inverse();
        let (va, vb) = (self.views(x), self.views(&xi));
        if !va.iter().any(|(_, _, k)| k.slices == 1) {
            return None;
        }
        let mut best: Option<Best> = None;
        let mut r = 4usize;
        loop {
            for (rot, v, k) in &va {
                if k.slices == 1 {
                    self.one_side(v, k.faces, r, &mut best, *rot, false);
                }
            }
            for (rot, v, k) in &vb {
                if k.slices == 1 {
                    self.one_side(v, k.faces, r, &mut best, *rot, true);
                }
            }
            // a shorter solution has setup + finish <= best - 3, so one of the two parts is at most (best - 3) / 2
            let b = best.as_ref().map_or(99, |b| b.total as usize);
            if 2 * r + 1 >= b.saturating_sub(3) || r >= 9 {
                return best;
            }
            r += 1;
        }
    }

    /// A `Best` written out: a sequence T in the labels of the state's own frame with (state)·T = solved.
    pub fn written(&self, x: &Cubie, b: &Best) -> Vec<usize> {
        let base = if b.inverse { x.inverse() } else { *x };
        let v = self.m.conj(&base, b.rot);
        let z = self.m.apply(&self.m.apply(&v, &b.setup), &b.slice);
        let (c, e, s) = self.m.dr_perms(&z).unwrap();
        let view: Vec<usize> = b.setup.iter().chain(&b.slice).copied().chain(self.ex.path(&c, &e, &s)).collect();
        let own: Vec<usize> = view.iter().map(|&mv| self.m.unview(b.rot, mv)).collect();
        if b.inverse { invert(&own) } else { own }
    }

    /// For a DR-1s that one slice turn fixes: the four ways to write that slice, each with an optimal finish
    /// (the slice may cancel against the move before it, which only the caller can see).
    pub fn direct_1s(&self, x: &Cubie) -> Vec<Vec<usize>> {
        let mut out = Vec::new();
        for (rot, v, k) in self.views(x) {
            if k.slices != 1 || k.turns != 2 {
                continue;
            }
            let sf: [usize; 2] = if k.faces == 2 { [2, 3] } else { [4, 5] };
            for i in [0usize, 2] {
                for j in [0usize, 2] {
                    let sl = [3 * sf[0] + i, 3 * sf[1] + j];
                    let z = self.m.apply(&v, &sl);
                    let (c, e, s) = self.m.dr_perms(&z).unwrap();
                    let view: Vec<usize> = sl.iter().copied().chain(self.ex.path(&c, &e, &s)).collect();
                    out.push(view.iter().map(|&mv| self.m.unview(rot, mv)).collect());
                }
            }
        }
        out
    }

    /// The by-hand version: setups of at most `cap` turns on the state's own side only.
    pub fn finish_1s_capped(&self, x: &Cubie, cap: usize) -> Option<Best> {
        let mut best = None;
        for (rot, v, k) in &self.views(x) {
            if k.slices == 1 {
                self.one_side(v, k.faces, cap, &mut best, *rot, false);
            }
        }
        best
    }
}

/// For a DR-xs in the U/D-colour view with corners on `faces` (0 R/L or 2 F/B): how many of the flipped edges
/// belong to the M slice and how many to the S slice (the two kinds of piece that carry a U/D colour).
pub fn split(m: &Model, v: &Cubie, faces: u8) -> (u8, u8) {
    let (mut a, mut b) = (0u8, 0u8);
    for i in 0..12 {
        let piece_kind = m.slot_kind[v.ep[i] as usize];
        if piece_kind == 0 {
            continue; // an E-slice piece: it has no U/D colour
        }
        // the piece's U/D sticker is on the place's reference facelet when ef = 0; that facelet is the U/D one for
        // M and S places and the F/B one for E places
        let on_axis: u8 = match (m.slot_kind[i], v.ef[i]) {
            (0, 0) => 2, // E place: F/B facelet
            (0, _) => 0, // E place: R/L facelet
            (1, 0) | (2, 0) => 1,
            (1, _) => 2, // M place: the other facelet is F/B
            (_, _) => 0, // S place: the other facelet is R/L
        };
        if on_axis != faces {
            if piece_kind == 1 { a += 1 } else { b += 1 }
        }
    }
    (a, b)
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
        // rejection sampling, unbiased
        let n = n as u64;
        let lim = u64::MAX - u64::MAX % n;
        loop {
            let v = self.next();
            if v < lim {
                return (v % n) as usize;
            }
        }
    }
    pub fn perm<const K: usize>(&mut self) -> [u8; K] {
        let mut p = [0u8; K];
        for i in 0..K {
            p[i] = i as u8;
        }
        for i in (1..K).rev() {
            p.swap(i, self.below(i + 1));
        }
        p
    }
}

fn parity(p: &[u8]) -> u8 {
    let mut n = 0;
    for i in 0..p.len() {
        for j in i + 1..p.len() {
            if p[i] > p[j] {
                n ^= 1;
            }
        }
    }
    n
}

/// A uniformly random state of the DR group on U/D.
pub fn random_dr(m: &Model, rng: &mut Rng) -> Cubie {
    loop {
        let (c, e, s): ([u8; 8], [u8; 8], [u8; 4]) = (rng.perm(), rng.perm(), rng.perm());
        if parity(&c) ^ parity(&e) != parity(&s) {
            continue;
        }
        let mut x = SOLVED;
        for k in 0..8 {
            x.cp[m.dr_c[k] as usize] = m.dr_c[c[k] as usize];
            x.ep[m.dr_e[k] as usize] = m.dr_e[e[k] as usize];
        }
        for k in 0..4 {
            x.ep[m.dr_s[k] as usize] = m.dr_s[s[k] as usize];
        }
        return x;
    }
}

pub const NAMES: [&str; 18] = ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'"];
pub fn text(seq: &[usize]) -> String {
    seq.iter().map(|&m| NAMES[m]).collect::<Vec<_>>().join(" ")
}

/// The inverse of a sequence.
pub fn invert(seq: &[usize]) -> Vec<usize> {
    seq.iter().rev().map(|&mv| 3 * (mv / 3) + 2 - mv % 3).collect()
}

/// A sequence with all cancelling done: consecutive turns about one axis are merged face by face.
pub fn cancel(seq: &[usize]) -> Vec<usize> {
    let mut out: Vec<usize> = Vec::new();
    let mut i = 0;
    loop {
        // take the run of turns about one axis starting at i, after merging with the run already at the end of `out`
        if i >= seq.len() {
            break;
        }
        let axis = seq[i] / 6;
        let mut q = [0usize; 2];
        while let Some(&l) = out.last() {
            if l / 6 != axis {
                break;
            }
            q[(l / 3) % 2] += l % 3 + 1;
            out.pop();
        }
        while i < seq.len() && seq[i] / 6 == axis {
            q[(seq[i] / 3) % 2] += seq[i] % 3 + 1;
            i += 1;
        }
        for k in 0..2 {
            if q[k] % 4 != 0 {
                out.push(3 * (2 * axis + k) + q[k] % 4 - 1);
            }
        }
    }
    out
}

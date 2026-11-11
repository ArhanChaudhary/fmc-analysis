//! What DR-xs offers on a real scramble: every DR-1s and DR-2s 8fe reachable from a slice-EO skip or a one-move
//! slice EO (and every DR-2s 8fe reachable from a normal EO), on normal and on inverse, each finished.
//!
//! The route, as in tseitsei89's tutorial: slice EO (the four pieces of one slice all oriented or all misoriented
//! for one axis), then moves that keep every edge's orientation for that axis (no quarter turns of that axis's two
//! faces) until the cube is a DR-xs.  The tables `out/bfs/eo-fb_*.u8` and `eo-ud_*.u8` give the fewest such moves
//! from every coset, so the enumeration below is exhaustive up to the caps.
//!
//! A slice and an axis are handled in a view: the cube turned so that the slice is the E slice (its pieces are the
//! edges without U/D colour) and the axis is F/B, or U/D when the axis is the slice's own.

use crate::cubie::{Cubie, Model, SOLVED};
use crate::finish::{text, Best, Exact, Finisher, Kind, NAMES};
use crate::Tables;
use rayon::prelude::*;
use std::collections::{HashMap, HashSet};
use std::fs::File;

const NEO: usize = 2048;
const NSL: usize = 495;

pub fn parse(s: &str) -> Vec<usize> {
    s.split_whitespace()
        .map(|t| NAMES.iter().position(|&n| n == t).unwrap_or_else(|| panic!("bad move {t}")))
        .collect()
}

/// A distance table held in memory at 4 bits per coset (15 = cannot be reached; real distances are at most 12),
/// or empty when the class is not being searched.
struct Dist {
    nib: Vec<u8>,
}
impl Dist {
    fn open(path: &str) -> Dist {
        use std::io::Read;
        let mut f = File::open(path).unwrap_or_else(|_| panic!("missing {path}"));
        let n = 2187 * NEO * NSL;
        let mut nib = vec![0u8; n / 2];
        let mut buf = vec![0u8; 1 << 24];
        let mut pos = 0usize;
        loop {
            let got = f.read(&mut buf).unwrap();
            if got == 0 {
                break;
            }
            for &b in &buf[..got] {
                let v = b.min(15);
                nib[pos >> 1] |= v << ((pos & 1) * 4);
                pos += 1;
            }
        }
        assert_eq!(pos, n);
        Dist { nib }
    }
    fn none() -> Dist {
        Dist { nib: Vec::new() }
    }
    #[inline]
    fn at(&self, co: usize, eo: usize, sl: usize) -> u8 {
        if self.nib.is_empty() {
            return 255;
        }
        let i = (co * NEO + eo) * NSL + sl;
        let v = (self.nib[i >> 1] >> ((i & 1) * 4)) & 15;
        if v == 15 { 255 } else { v }
    }
}

pub struct Ctx<'a> {
    pub m: &'a Model,
    pub t: &'a Tables,
    pub fin: &'a Finisher<'a>,
    pub ex: &'a Exact,
    pub kinds: &'a HashMap<(usize, usize, usize), Kind>,
    d1s: [Dist; 2],  // rule index 0 = no F/B quarter turns, 1 = no U/D quarter turns
    d8fe: [Dist; 2],
    eo_dist: Vec<u8>, // fewest turns to EO on F/B, per eo coordinate
}

#[derive(Clone)]
pub struct Cand {
    pub side: u8,       // 0 normal, 1 inverse
    pub slice: u8,      // colour axis whose slice pieces were oriented (0 M, 1 E, 2 S in the cube's own frame)
    pub axis: u8,       // the axis of the slice EO, cube frame
    pub flavour: u8,    // 0 all oriented, 1 all misoriented
    pub start: u8,      // 0 slice-EO skip, 1 one-move slice EO, 4 EO of at most 4 moves, 5 EO of 5 moves
    pub class: u8,      // 1 = DR-1s, 8 = DR-2s 8fe
    pub seq: Vec<usize>, // all moves, in the cube's own labels
    pub state: Cubie,   // the DR-xs state, in the view
    pub rot: usize,
    pub last_view: Option<usize>, // last move, in view labels
}

fn rule_mask(rule: usize) -> u32 {
    let all: u32 = (1 << 18) - 1;
    let q = |face: usize| -> u32 { (1 << (3 * face)) | (1 << (3 * face + 2)) };
    if rule == 0 { all & !q(4) & !q(5) } else { all & !q(0) & !q(1) }
}

impl<'a> Ctx<'a> {
    pub fn new(m: &'a Model, t: &'a Tables, fin: &'a Finisher<'a>, ex: &'a Exact, kinds: &'a HashMap<(usize, usize, usize), Kind>, bfs: &str, want1s: bool, want8: bool) -> Ctx<'a> {
        // EO distance on the eo coordinate, all 18 turns
        let mut eo_dist = vec![255u8; NEO];
        eo_dist[0] = 0;
        let mut d = 0;
        loop {
            let mut any = false;
            for e in 0..NEO {
                if eo_dist[e] == d {
                    for mv in 0..18 {
                        let f = t.eo[e][mv] as usize;
                        if eo_dist[f] == 255 {
                            eo_dist[f] = d + 1;
                            any = true;
                        }
                    }
                }
            }
            if !any { break; }
            d += 1;
        }
        Ctx {
            m, t, fin, ex, kinds,
            d1s: if want1s { [Dist::open(&format!("{bfs}/eo-fb_1s.u8")), Dist::open(&format!("{bfs}/eo-ud_1s.u8"))] } else { [Dist::none(), Dist::none()] },
            d8fe: if want8 { [Dist::open(&format!("{bfs}/eo-fb_2s8fe.u8")), Dist::open(&format!("{bfs}/eo-ud_2s8fe.u8"))] } else { [Dist::none(), Dist::none()] },
            eo_dist,
        }
    }

    /// Orientation bits of the four E-slice pieces for the rule's axis (F/B for rule 0, U/D for rule 1).
    fn slice_bits(&self, v: &Cubie, rule: usize) -> Option<u8> {
        let mut first = None;
        for i in 0..12 {
            if self.m.e_piece[v.ep[i] as usize] {
                let b = v.ef[i] ^ ((rule == 1 && self.m.slot_kind[i] == 1) as u8);
                match first {
                    None => first = Some(b),
                    Some(f) if f != b => return None,
                    _ => {}
                }
            }
        }
        first
    }

    /// Every sequence of at most `left` allowed turns from `v` that ends on a state of the class (and does not pass
    /// through one earlier).
    #[allow(clippy::too_many_arguments)]
    fn reach(&self, v: &Cubie, c: (usize, usize, usize), dist: &Dist, mask: u32, left: usize, seq: &mut Vec<usize>, out: &mut Vec<(Vec<usize>, Cubie)>) {
        let d = dist.at(c.0, c.1, c.2) as usize;
        if d > left {
            return;
        }
        if d == 0 {
            out.push((seq.clone(), *v));
            return;
        }
        let last = seq.last().copied();
        let mut a = mask;
        while a != 0 {
            let mv = a.trailing_zeros() as usize;
            a &= a - 1;
            if let Some(l) = last {
                let (fl, fm) = (l / 3, mv / 3);
                if fl == fm || (fl / 2 == fm / 2 && fl > fm) {
                    continue;
                }
            }
            let w = self.m.turn(v, mv);
            let c2 = (self.t.co[c.0][mv] as usize, self.t.eo[c.1][mv] as usize, self.t.sl[c.2][mv] as usize);
            seq.push(mv);
            self.reach(&w, c2, dist, mask, left - 1, seq, out);
            seq.pop();
        }
    }

    /// All EO solutions (F/B axis, view labels) of at most `left` turns.
    fn eos(&self, eo: usize, left: usize, seq: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
        let d = self.eo_dist[eo] as usize;
        if d > left {
            return;
        }
        if d == 0 {
            out.push(seq.clone());
            return;
        }
        let last = seq.last().copied();
        for mv in 0..18 {
            if let Some(l) = last {
                let (fl, fm) = (l / 3, mv / 3);
                if fl == fm || (fl / 2 == fm / 2 && fl > fm) {
                    continue;
                }
            }
            seq.push(mv);
            self.eos(self.t.eo[eo][mv] as usize, left - 1, seq, out);
            seq.pop();
        }
    }

    pub fn candidates(&self, scramble: &[usize], cap1s: usize, cap8: usize, eo_max: usize) -> Vec<Cand> {
        let x = self.m.apply(&SOLVED, scramble);
        let mut out: Vec<Cand> = Vec::new();
        for (side, s) in [(0u8, x), (1u8, x.inverse())] {
            for c in 0..3usize {
                for e in 0..3usize {
                    let (rot, rule) = if e != c { (self.m.rot_for(c, 1, Some((e, 2))), 0usize) } else { (self.m.rot_for(c, 1, None), 1usize) };
                    let v = self.m.conj(&s, rot);
                    let mask = rule_mask(rule);
                    let mut starts: Vec<(Cubie, Vec<usize>, u8, u8)> = Vec::new(); // state, moves so far (view), start type, flavour
                    let here = self.slice_bits(&v, rule);
                    if let Some(f) = here {
                        starts.push((v, vec![], 0, f));
                    }
                    for mv in 0..18 {
                        let w = self.m.turn(&v, mv);
                        if let Some(f) = self.slice_bits(&w, rule) {
                            if here != Some(f) {
                                starts.push((w, vec![mv], 1, f));
                            }
                        }
                    }
                    let mut push = |out: &mut Vec<Cand>, pre: &Vec<usize>, st: u8, fl: u8, class: u8, found: Vec<(Vec<usize>, Cubie)>| {
                        for (seq, state) in found {
                            let all: Vec<usize> = pre.iter().chain(&seq).map(|&mv| self.m.unview(rot, mv)).collect();
                            let last_view = seq.last().or(pre.last()).copied();
                            out.push(Cand { side, slice: c as u8, axis: e as u8, flavour: fl, start: st, class, seq: all, state, rot, last_view });
                        }
                    };
                    for (w, pre, st, fl) in &starts {
                        let co = self.m.coords(w);
                        for (class, dist, cap) in [(1u8, &self.d1s[rule], cap1s), (8u8, &self.d8fe[rule], cap8)] {
                            if cap < pre.len() {
                                continue;
                            }
                            let mut found = Vec::new();
                            self.reach(w, co, dist, mask, cap - pre.len(), &mut Vec::new(), &mut found);
                            push(&mut out, pre, *st, *fl, class, found);
                        }
                    }
                    // DR-2s 8fe after a normal EO on this axis (only when the axis is not the slice's own)
                    if rule == 0 && eo_max > 0 {
                        let (_, eo, _) = self.m.coords(&v);
                        let mut eos = Vec::new();
                        self.eos(eo, eo_max, &mut Vec::new(), &mut eos);
                        for pre in eos {
                            if pre.len() > cap8 || pre.is_empty() && here.is_some() {
                                continue;
                            }
                            let w = self.m.apply(&v, &pre);
                            let mut found = Vec::new();
                            self.reach(&w, self.m.coords(&w), &self.d8fe[0], mask, cap8 - pre.len(), &mut Vec::new(), &mut found);
                            let st = if pre.len() <= 4 { 4 } else { 5 };
                            push(&mut out, &pre, st, 0, 8, found);
                        }
                    }
                }
            }
        }
        // one candidate per (side, state in the cube's frame, length): keep the cheapest start type
        let mut seen: HashMap<(u8, Cubie, usize), usize> = HashMap::new();
        let mut keep: Vec<Cand> = Vec::new();
        for cand in out {
            let real = self.m.apply(&if cand.side == 0 { x } else { x.inverse() }, &cand.seq);
            let key = (cand.side, real, cand.seq.len());
            match seen.get(&key) {
                Some(&i) => {
                    if cand.start < keep[i].start {
                        keep[i] = cand;
                    }
                }
                None => {
                    seen.insert(key, keep.len());
                    keep.push(cand);
                }
            }
        }
        keep
    }
}

/// Finish of a DR-2s 8fe of the form: setup, the two slice turns one after the other (four face turns), DR finish.
/// `v`: the state in the U/D-colour view, corners on faces `faces`.  Searches setups of at most `r` turns.
pub fn eightfe_side(fin: &Finisher, v: &Cubie, faces: u8, r: usize, best: &mut Option<(u8, Vec<usize>, [usize; 4], u8)>) {
    let mut allowed = Vec::new();
    for face in 0..6 {
        let axis = [1u8, 1, 0, 0, 2, 2][face];
        for q in 0..3 {
            if axis == faces || q == 1 {
                allowed.push(3 * face + q);
            }
        }
    }
    let s2: [usize; 2] = if faces == 0 { [2, 3] } else { [4, 5] }; // second slice: about the faces' own axis
    fn go(fin: &Finisher, v: &Cubie, allowed: &[usize], s2: [usize; 2], left: usize, seq: &mut Vec<usize>, best: &mut Option<(u8, Vec<usize>, [usize; 4], u8)>) {
        for i in [0usize, 2] {
            for j in [0usize, 2] {
                let y = fin.m.turn(&fin.m.turn(v, i), 3 + j); // U^i D^j
                for k in [0usize, 2] {
                    for l in [0usize, 2] {
                        let z = fin.m.turn(&fin.m.turn(&y, 3 * s2[0] + k), 3 * s2[1] + l);
                        let (c, e, s) = fin.m.dr_perms(&z).expect("two slices did not give a DR");
                        let d = fin.ex.depth(&c, &e, &s);
                        let total = seq.len() as u8 + 4 + d;
                        if best.as_ref().map_or(true, |b| total < b.0) {
                            *best = Some((total, seq.clone(), [i, 3 + j, 3 * s2[0] + k, 3 * s2[1] + l], d));
                        }
                    }
                }
            }
        }
        if left == 0 {
            return;
        }
        if let Some(b) = best {
            if seq.len() + 1 + 4 >= b.0 as usize {
                return;
            }
        }
        let last = seq.last().copied();
        for &mv in allowed {
            if let Some(l) = last {
                let (fl, fm) = (l / 3, mv / 3);
                if fl == fm || (fl / 2 == fm / 2 && fl > fm) {
                    continue;
                }
            }
            seq.push(mv);
            let w = fin.m.turn(v, mv);
            go(fin, &w, allowed, s2, left - 1, seq, best);
            seq.pop();
        }
    }
    go(fin, v, &allowed, s2, r, &mut Vec::new(), best);
}

type Best8 = (u8, Vec<usize>, [usize; 4], u8);

/// Both ends, exact for the form "setup, the two slices one after the other, DR finish".
/// Returns the total and a written solution T (own labels) with (state)·T = solved.
pub fn finish_8fe(fin: &Finisher, x: &Cubie, rmax: usize) -> Option<(u8, Vec<usize>)> {
    let is8 = |k: &Kind| k.slices == 2 && k.flips == 8 && k.faces != 1;
    let xi = x.inverse();
    let (va, vb) = (fin.views(x), fin.views(&xi));
    if !va.iter().any(|(_, _, k)| is8(k)) {
        return None;
    }
    let mut best: Option<(Best8, usize, Cubie, bool)> = None;
    let mut r = 2usize;
    loop {
        for (inv, views) in [(false, &va), (true, &vb)] {
            for (rot, v, k) in views.iter() {
                if is8(k) {
                    let mut b: Option<Best8> = best.as_ref().map(|x| x.0.clone());
                    let before = b.as_ref().map(|b| b.0);
                    eightfe_side(fin, v, k.faces, r, &mut b);
                    if b.as_ref().map(|b| b.0) != before {
                        best = Some((b.unwrap(), *rot, *v, inv));
                    }
                }
            }
        }
        let b = best.as_ref().map_or(99, |b| b.0 .0 as usize);
        // exact once 2r + 1 >= best - 5; `rmax` cuts the search short (then the result is an upper bound)
        if 2 * r + 1 >= b.saturating_sub(5) || r >= rmax {
            let (bb, rot, v, inv) = best.unwrap();
            let z = fin.m.apply(&fin.m.apply(&v, &bb.1), &bb.2);
            let (c, e, s) = fin.m.dr_perms(&z).unwrap();
            let view: Vec<usize> = bb.1.iter().chain(&bb.2).copied().chain(fin.ex.path(&c, &e, &s)).collect();
            let own: Vec<usize> = view.iter().map(|&mv| fin.m.unview(rot, mv)).collect();
            return Some((bb.0, if inv { crate::finish::invert(&own) } else { own }));
        }
        r += 1;
    }
}

/// For a DR-2s 8fe: the sixteen ways to write the two slices with no setup, each with an optimal finish.
pub fn direct_8fe(fin: &Finisher, x: &Cubie) -> Vec<Vec<usize>> {
    let mut out = Vec::new();
    for (rot, v, k) in fin.views(x) {
        if !(k.slices == 2 && k.flips == 8 && k.faces != 1) {
            continue;
        }
        let s2: [usize; 2] = if k.faces == 0 { [2, 3] } else { [4, 5] };
        for i in [0usize, 2] {
            for j in [0usize, 2] {
                for kq in [0usize, 2] {
                    for l in [0usize, 2] {
                        let sl = [i, 3 + j, 3 * s2[0] + kq, 3 * s2[1] + l];
                        let z = fin.m.apply(&v, &sl);
                        let (c, e, s) = fin.m.dr_perms(&z).unwrap();
                        let view: Vec<usize> = sl.iter().copied().chain(fin.ex.path(&c, &e, &s)).collect();
                        out.push(view.iter().map(|&mv| fin.m.unview(rot, mv)).collect());
                    }
                }
            }
        }
    }
    out
}

/// xstools attempts <tables dir> <kinds.tsv> <exact table> <bfs dir> <scrambles file> <cap 1s> <cap 8fe> <eo max> [first] [count]
pub fn run(a: &[String]) {
    let t = crate::load(&a[0]);
    let m = Model::load(&a[0]);
    let kinds = crate::finish::load_kinds(&a[1]);
    let ex = Exact::load(&a[2]);
    let fin = Finisher::new(&m, &t, &ex, &kinds);
    let (c1, c8): (usize, usize) = (a[5].parse().unwrap(), a[6].parse().unwrap());
    let ctx = Ctx::new(&m, &t, &fin, &ex, &kinds, &a[3], c1 > 0, c8 > 0); // a cap of 0 leaves that class out
    let scr: Vec<String> = std::fs::read_to_string(&a[4]).unwrap().lines().filter(|l| !l.starts_with('#') && !l.trim().is_empty()).map(|l| l.to_string()).collect();
    let (cap1, cap8, eo_max): (usize, usize, usize) = (a[5].parse().unwrap(), a[6].parse().unwrap(), a[7].parse().unwrap());
    // setups searched for a DR-2s 8fe: up to this many moves from either end (7 = exact)
    let r8: usize = std::env::var("XS_R8").ok().map_or(7, |v| v.parse().unwrap());
    let first: usize = a.get(8).map_or(0, |v| v.parse().unwrap());
    let count: usize = a.get(9).map_or(scr.len(), |v| v.parse().unwrap());
    println!("scramble\tside\tslice\taxis\tflavour\tstart\tclass\tlength\tturns_to_dr\tsubset\tfinish\ttotal\tmoves\tsolution");
    for (idx, line) in scr.iter().enumerate().skip(first).take(count) {
        let cands = ctx.candidates(&parse(line), cap1, cap8, eo_max);
        let rows: Vec<String> = cands
            .par_iter()
            .map(|c| {
                let (_, kind) = class_view(&fin, c);
                // the candidate's state in the cube's own frame, and every written finish of it
                let own = m.conj_back(&c.state, c.rot);
                let (finish, mut ways): (u8, Vec<Vec<usize>>);
                if c.class == 1 {
                    let b: Best = fin.finish_1s(&own).unwrap();
                    finish = b.total;
                    ways = vec![fin.written(&own, &b)];
                    ways.extend(fin.direct_1s(&own));
                } else {
                    let (tot, w) = finish_8fe(&fin, &own, r8).unwrap();
                    finish = tot;
                    ways = vec![w];
                    ways.extend(direct_8fe(&fin, &own));
                }
                // whole solution of the scramble: route then finish, inverted if the route was found on inverse
                let best = ways
                    .iter()
                    .map(|w| {
                        let whole: Vec<usize> = c.seq.iter().chain(w).copied().collect();
                        crate::finish::cancel(&if c.side == 1 { crate::finish::invert(&whole) } else { whole })
                    })
                    .min_by_key(|w| w.len())
                    .unwrap();
                let sub = subset_of(&fin, c);
                format!("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}", idx + 1, c.side, ["M", "E", "S"][c.slice as usize], ["RL", "UD", "FB"][c.axis as usize],
                        c.flavour, c.start, c.class, c.seq.len(), kind.turns, sub, finish, best.len(), text(&c.seq), text(&best))
            })
            .collect();
        for r in rows {
            println!("{r}");
        }
        eprintln!("scramble {}: {} candidates", idx + 1, cands.len());
    }
    let _ = HashSet::<u8>::new();
}

/// The colour view of a candidate's state in which it is a DR-xs of its class.
fn class_view(fin: &Finisher, c: &Cand) -> (Cubie, Kind) {
    fin.views(&c.state).into_iter().map(|(_, v, k)| (v, k)).find(|(_, k)| if c.class == 1 { k.slices == 1 } else { k.slices == 2 && k.flips == 8 && k.faces != 1 }).unwrap()
}

/// Corner subset of the DR that the bare slice turn(s) would give.
fn subset_of(fin: &Finisher, c: &Cand) -> &'static str {
    let (v, k) = class_view(fin, c);
    let z = if c.class == 1 {
        let sf: [usize; 2] = if k.faces == 2 { [2, 3] } else { [4, 5] };
        fin.m.apply(&v, &[3 * sf[0], 3 * sf[1] + 2])
    } else {
        let s2: [usize; 2] = if k.faces == 0 { [2, 3] } else { [4, 5] };
        fin.m.apply(&v, &[0, 5, 3 * s2[0], 3 * s2[1] + 2])
    };
    let (cp, _, _) = fin.m.dr_perms_corners(&z);
    fin.ex.corner_subset(&cp)
}


/// A uniformly random cube state.
pub fn random_cube(rng: &mut crate::finish::Rng) -> Cubie {
    fn par(p: &[u8]) -> u8 {
        let mut n = 0;
        for i in 0..p.len() {
            for j in i + 1..p.len() {
                if p[i] > p[j] { n ^= 1; }
            }
        }
        n
    }
    loop {
        let (cp, ep): ([u8; 8], [u8; 12]) = (rng.perm(), rng.perm());
        if par(&cp) != par(&ep) {
            continue;
        }
        let mut x = Cubie { cp, ct: [0; 8], ep, ef: [0; 12] };
        let mut s = 0;
        for i in 0..7 {
            x.ct[i] = rng.below(3) as u8;
            s += x.ct[i];
        }
        x.ct[7] = (3 - s % 3) % 3;
        let mut f = 0;
        for i in 0..11 {
            x.ef[i] = rng.below(2) as u8;
            f ^= x.ef[i];
        }
        x.ef[11] = f;
        return x;
    }
}

/// xstools nearest <tables dir> <bfs dir> <samples> <seed>
/// For uniformly random cube states: the fewest turns (any turns, one side at a time) to a real DR, to a DR-1s, to
/// a DR-2s 8fe and to any DR-xs, minimised over the three colours and over normal and inverse; and over normal only.
/// The tables are read into memory one at a time (2.2 GB each).
pub fn nearest(a: &[String]) {
    let m = Model::load(&a[0]);
    let (n, seed): (usize, u64) = (a[2].parse().unwrap(), a[3].parse().unwrap());
    let to_ud = [m.rot_for(0, 1, None), 0, m.rot_for(2, 1, None)];
    // the six coset indices of every sample: normal x 3 colours, then inverse x 3 colours
    let idx: Vec<[u32; 6]> = (0..n)
        .into_par_iter()
        .map(|i| {
            let mut rng = crate::finish::Rng(seed.wrapping_mul(0x9E3779B97F4A7C15).wrapping_add(i as u64));
            let x = random_cube(&mut rng);
            let mut out = [0u32; 6];
            for (side, s) in [(0, x), (1, x.inverse())] {
                for c in 0..3 {
                    let co = m.coords(&m.conj(&s, to_ud[c]));
                    out[3 * side + c] = ((co.0 * NEO + co.1) * NSL + co.2) as u32;
                }
            }
            out
        })
        .collect();
    println!("what\tsides\tturns\tstates");
    for name in ["dr", "1s", "2s8fe", "xs"] {
        let tab = std::fs::read(format!("{}/all_{}.u8", a[1], name)).expect("table");
        let (mut both, mut normal) = ([0usize; 32], [0usize; 32]);
        for r in &idx {
            let v: Vec<u8> = r.iter().map(|&j| tab[j as usize]).collect();
            both[*v.iter().min().unwrap() as usize] += 1;
            normal[*v[..3].iter().min().unwrap() as usize] += 1;
        }
        for (sides, h) in [("both", both), ("normal", normal)] {
            for (d, c) in h.iter().enumerate() {
                if *c > 0 {
                    println!("{name}\t{sides}\t{d}\t{c}");
                }
            }
        }
    }
}

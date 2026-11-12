//! All reduced sequences of length <= L whose product is a corner-only or an edge-only element of one of the leftover
//! types, by meet in the middle:
//!
//!   join     a sequence A·B (|A| = ceil(l/2), |B| = floor(l/2)) is corner-only exactly when the edge part of A equals
//!            the edge part of B^-1, so the half sequences are sorted by that and joined; the same with the corner part
//!            for edge-only products.  One pass gives every element of every type.
//!   search   (independent of the join) for one element g: depth-first over B^-1 from g, looking the whole state up
//!            among the half sequences A.  Used for the parity family and to check the join class by class.

use crate::cubie::{hash128, Cubie, Model, SOLVED};
use crate::seq::{self, follows, inv_move};
use crate::types::{self, classify, TYPES};
use rayon::prelude::*;
use std::collections::HashMap;
use std::io::{Read, Write};

pub struct Level {
    pub k: usize,
    pub seq: Vec<u32>,
    pub ek: Vec<u64>,
    pub ck: Vec<u64>,
    pub eki: Vec<u64>,
    pub cki: Vec<u64>,
}

/// All reduced sequences of exactly k moves with their states.
pub fn build_level(m: &Model, k: usize) -> Level {
    let mut lv = Level { k, seq: Vec::new(), ek: Vec::new(), ck: Vec::new(), eki: Vec::new(), cki: Vec::new() };
    fn rec(m: &Model, k: usize, depth: usize, s: &Cubie, last: u8, packed: u32, lv: &mut Level) {
        if depth == k {
            let inv = s.inverse();
            lv.seq.push(packed);
            lv.ek.push(s.ekey());
            lv.ck.push(s.ckey());
            lv.eki.push(inv.ekey());
            lv.cki.push(inv.ckey());
            return;
        }
        for mv in 0..18u8 {
            if depth > 0 && !follows(last, mv) {
                continue;
            }
            rec(m, k, depth + 1, &m.turn(s, mv as usize), mv, packed | (mv as u32) << (5 * depth), lv);
        }
    }
    rec(m, k, 0, &SOLVED, 0, 0, &mut lv);
    lv
}

#[inline]
fn mul_c(a: u64, b: u64) -> u64 {
    let mut r = 0u64;
    for i in 0..8 {
        let vb = (b >> (5 * i)) & 31;
        let va = (a >> (5 * (vb & 7))) & 31;
        r |= ((va & 7) | (((va >> 3) + (vb >> 3)) % 3) << 3) << (5 * i);
    }
    r
}
#[inline]
fn mul_e(a: u64, b: u64) -> u64 {
    let mut r = 0u64;
    for i in 0..12 {
        let vb = (b >> (5 * i)) & 31;
        let va = (a >> (5 * (vb & 15))) & 31;
        r |= ((va & 15) | (((va >> 4) ^ (vb >> 4)) & 1) << 4) << (5 * i);
    }
    r
}

#[inline]
fn joined(a: u32, ka: usize, b: u32, kb: usize) -> u64 {
    (((ka + kb) as u64) << 60) | a as u64 | (b as u64) << (5 * ka)
}

/// Every product A·B of the two levels that is corner-only (or edge-only) and of a known type: (type, element, sequence).
fn join(la: &Level, lb: &Level, corner_only: bool, sink: &mut Vec<Vec<(u128, u64)>>) -> u64 {
    let (ka, kb) = (la.k, lb.k);
    let (keya, keyb) = if corner_only { (&la.ek, &lb.eki) } else { (&la.ck, &lb.cki) };
    let mut ia: Vec<u32> = (0..la.seq.len() as u32).collect();
    let mut ib: Vec<u32> = (0..lb.seq.len() as u32).collect();
    ia.par_sort_unstable_by_key(|&i| keya[i as usize]);
    ib.par_sort_unstable_by_key(|&i| keyb[i as usize]);
    let (solved_c, solved_e) = (SOLVED.ckey(), SOLVED.ekey());
    let (mut x, mut y) = (0usize, 0usize);
    let mut pairs = 0u64;
    while x < ia.len() && y < ib.len() {
        let (kx, ky) = (keya[ia[x] as usize], keyb[ib[y] as usize]);
        if kx < ky {
            x += 1;
            continue;
        }
        if ky < kx {
            y += 1;
            continue;
        }
        let (mut x1, mut y1) = (x, y);
        while x1 < ia.len() && keya[ia[x1] as usize] == kx {
            x1 += 1;
        }
        while y1 < ib.len() && keyb[ib[y1] as usize] == kx {
            y1 += 1;
        }
        for &a in &ia[x..x1] {
            let sa = la.seq[a as usize];
            let last_a = ((sa >> (5 * (ka - 1))) & 31) as u8;
            for &b in &ib[y..y1] {
                let sb = lb.seq[b as usize];
                if !follows(last_a, (sb & 31) as u8) {
                    continue;
                }
                pairs += 1;
                let key: u128 = if corner_only {
                    let c = mul_c(la.ck[a as usize], lb.ck[b as usize]);
                    if c == solved_c {
                        continue;
                    }
                    (c as u128) << 64 | solved_e as u128
                } else {
                    let e = mul_e(la.ek[a as usize], lb.ek[b as usize]);
                    if e == solved_e {
                        continue;
                    }
                    (solved_c as u128) << 64 | e as u128
                };
                if let Some(t) = classify(&Cubie::from_key(key)) {
                    sink[t].push((key, joined(sa, ka, sb, kb)));
                }
            }
        }
        x = x1;
        y = y1;
    }
    pairs
}

/// For torchlight's statement (a corner twisted in place with all edges kept takes 12 moves): every corner-only
/// reduced product A·B of the two levels, whatever its type, that leaves at least one corner in its place and twisted.
/// Returns (corner-only reduced products, of them with a corner twisted in place, the corner keys of those).
pub fn join_twisted(la: &Level, lb: &Level) -> (u64, u64, Vec<u64>) {
    let (ka, _kb) = (la.k, lb.k);
    let (keya, keyb) = (&la.ek, &lb.eki);
    let mut ia: Vec<u32> = (0..la.seq.len() as u32).collect();
    let mut ib: Vec<u32> = (0..lb.seq.len() as u32).collect();
    ia.par_sort_unstable_by_key(|&i| keya[i as usize]);
    ib.par_sort_unstable_by_key(|&i| keyb[i as usize]);
    let solved_c = SOLVED.ckey();
    let (mut x, mut y) = (0usize, 0usize);
    let (mut pairs, mut hits) = (0u64, 0u64);
    let mut keys: Vec<u64> = Vec::new();
    while x < ia.len() && y < ib.len() {
        let (kx, ky) = (keya[ia[x] as usize], keyb[ib[y] as usize]);
        if kx < ky {
            x += 1;
            continue;
        }
        if ky < kx {
            y += 1;
            continue;
        }
        let (mut x1, mut y1) = (x, y);
        while x1 < ia.len() && keya[ia[x1] as usize] == kx {
            x1 += 1;
        }
        while y1 < ib.len() && keyb[ib[y1] as usize] == kx {
            y1 += 1;
        }
        for &a in &ia[x..x1] {
            let sa = la.seq[a as usize];
            let last_a = ((sa >> (5 * (ka - 1))) & 31) as u8;
            for &b in &ib[y..y1] {
                let sb = lb.seq[b as usize];
                if !follows(last_a, (sb & 31) as u8) {
                    continue;
                }
                let c = mul_c(la.ck[a as usize], lb.ck[b as usize]);
                if c == solved_c {
                    continue;
                }
                pairs += 1;
                let twisted = (0..8).any(|i| {
                    let v = (c >> (5 * i)) & 31;
                    (v & 7) == i as u64 && (v >> 3) != 0
                });
                if twisted {
                    hits += 1;
                    keys.push(c);
                }
            }
        }
        x = x1;
        y = y1;
    }
    keys.sort_unstable();
    keys.dedup();
    (pairs, hits, keys)
}

/// Lists for every type: (element key, sequence), sorted by element, then length, then sequence.
pub fn build_by_join(m: &Model, lmax: usize, verbose: bool) -> Vec<Vec<(u128, u64)>> {
    let h = (lmax + 1) / 2;
    let levels: Vec<Level> = (0..=h).map(|k| build_level(m, k)).collect();
    let mut sink: Vec<Vec<(u128, u64)>> = vec![Vec::new(); TYPES.len()];
    for l in 2..=lmax {
        let (ka, kb) = ((l + 1) / 2, l / 2);
        let t0 = std::time::Instant::now();
        let p1 = join(&levels[ka], &levels[kb], true, &mut sink);
        let p2 = join(&levels[ka], &levels[kb], false, &mut sink);
        if verbose {
            eprintln!("  join length {l}: {p1} corner-only and {p2} edge-only reduced products  ({:.1}s)", t0.elapsed().as_secs_f64());
        }
    }
    for v in sink.iter_mut() {
        v.par_sort_unstable();
        for w in v.windows(2) {
            assert!(w[0] != w[1], "a sequence was found twice");
        }
    }
    sink
}

pub fn write_file(path: &str, lmax: usize, lists: &[Vec<(u128, u64)>]) {
    let mut f = std::io::BufWriter::new(std::fs::File::create(path).unwrap());
    f.write_all(b"INSALG1\0").unwrap();
    f.write_all(&(lmax as u32).to_le_bytes()).unwrap();
    f.write_all(&(lists.len() as u32).to_le_bytes()).unwrap();
    for v in lists {
        f.write_all(&(v.len() as u64).to_le_bytes()).unwrap();
        for &(k, a) in v {
            f.write_all(&k.to_le_bytes()).unwrap();
            f.write_all(&a.to_le_bytes()).unwrap();
        }
    }
}

pub fn read_file(path: &str) -> (usize, Vec<Vec<(u128, u64)>>) {
    let mut f = std::io::BufReader::new(std::fs::File::open(path).unwrap_or_else(|_| panic!("cannot open {path}: run `instools algs <L>` first")));
    let mut b8 = [0u8; 8];
    let mut b4 = [0u8; 4];
    let mut b16 = [0u8; 16];
    f.read_exact(&mut b8).unwrap();
    assert_eq!(&b8, b"INSALG1\0");
    f.read_exact(&mut b4).unwrap();
    let lmax = u32::from_le_bytes(b4) as usize;
    f.read_exact(&mut b4).unwrap();
    let nt = u32::from_le_bytes(b4) as usize;
    let mut lists = Vec::new();
    for _ in 0..nt {
        f.read_exact(&mut b8).unwrap();
        let n = u64::from_le_bytes(b8) as usize;
        let mut v = Vec::with_capacity(n);
        for _ in 0..n {
            f.read_exact(&mut b16).unwrap();
            f.read_exact(&mut b8).unwrap();
            v.push((u128::from_le_bytes(b16), u64::from_le_bytes(b8)));
        }
        lists.push(v);
    }
    (lmax, lists)
}

// ------------------------------------------------------------------------------------------------------------------
// The table used by the insertion code.

#[derive(Clone, Copy)]
pub struct Elem {
    pub ty: u8,
    pub opt: u8,
    pub g0: u32,
    pub g1: u32,
}
/// The sequences of one element with one length, one kind of first run and one kind of last run
/// (kind of run = axis * 3 + faces present - 1; 9 = the sequence is a single run).
#[derive(Clone, Copy)]
pub struct Group {
    pub len: u8,
    pub fc: u8,
    pub lc: u8,
    pub a0: u32,
    pub a1: u32,
}
pub struct Table {
    pub lmax: usize,
    pub elems: Vec<Elem>,
    pub ekeys: Vec<u128>,
    pub groups: Vec<Group>,
    pub algs: Vec<u64>,
    /// for each sequence, as sets of moves (bit m = move m): its first run, its first two runs, its last run, its last two runs
    pub masks: Vec<[u32; 4]>,
    slots: Vec<u32>,
    mask: usize,
}

pub fn run_masks(a: &[u8]) -> [u32; 4] {
    let n = a.len();
    let mut runs: Vec<u32> = Vec::new();
    let mut i = 0;
    while i < n {
        let ax = a[i] / 6;
        let mut mk = 0u32;
        while i < n && a[i] / 6 == ax {
            mk |= 1 << a[i];
            i += 1;
        }
        runs.push(mk);
    }
    let k = runs.len();
    let (f1, l1) = (runs[0], runs[k - 1]);
    [f1, f1 | if k > 1 { runs[1] } else { 0 }, l1, l1 | if k > 1 { runs[k - 2] } else { 0 }]
}

pub fn run_codes(a: &[u8]) -> (u8, u8) {
    let n = a.len();
    let ax = a[0] / 6;
    let mut i = 0;
    let mut mk = 0u8;
    while i < n && a[i] / 6 == ax {
        mk |= 1 << ((a[i] / 3) % 2);
        i += 1;
    }
    if i == n {
        return (9, 9);
    }
    let ax2 = a[n - 1] / 6;
    let mut j = n;
    let mut mk2 = 0u8;
    while j > 0 && a[j - 1] / 6 == ax2 {
        mk2 |= 1 << ((a[j - 1] / 3) % 2);
        j -= 1;
    }
    (ax * 3 + mk - 1, ax2 * 3 + mk2 - 1)
}

impl Table {
    pub fn from_lists(lmax: usize, lists: &[Vec<(u128, u64)>], keep: usize) -> Table {
        let mut t = Table { lmax: lmax.min(keep), elems: Vec::new(), ekeys: Vec::new(), groups: Vec::new(), algs: Vec::new(), masks: Vec::new(), slots: Vec::new(), mask: 0 };
        let mut tmp: Vec<(u8, u8, u8, u64)> = Vec::new();
        for (ty, v) in lists.iter().enumerate() {
            let mut i = 0;
            while i < v.len() {
                let mut j = i;
                tmp.clear();
                while j < v.len() && v[j].0 == v[i].0 {
                    let a = seq::unpack_vec(v[j].1);
                    if a.len() <= keep {
                        let (fc, lc) = run_codes(&a);
                        tmp.push((a.len() as u8, fc, lc, v[j].1));
                    }
                    j += 1;
                }
                if !tmp.is_empty() {
                    tmp.sort_unstable();
                    let g0 = t.groups.len() as u32;
                    let mut p = 0;
                    while p < tmp.len() {
                        let mut q = p;
                        let a0 = t.algs.len() as u32;
                        while q < tmp.len() && (tmp[q].0, tmp[q].1, tmp[q].2) == (tmp[p].0, tmp[p].1, tmp[p].2) {
                            t.algs.push(tmp[q].3);
                            t.masks.push(run_masks(&seq::unpack_vec(tmp[q].3)));
                            q += 1;
                        }
                        t.groups.push(Group { len: tmp[p].0, fc: tmp[p].1, lc: tmp[p].2, a0, a1: t.algs.len() as u32 });
                        p = q;
                    }
                    t.elems.push(Elem { ty: ty as u8, opt: tmp[0].0, g0, g1: t.groups.len() as u32 });
                    t.ekeys.push(v[i].0);
                }
                i = j;
            }
        }
        let cap = (t.elems.len() * 2 + 16).next_power_of_two();
        t.slots = vec![u32::MAX; cap];
        t.mask = cap - 1;
        for (i, &k) in t.ekeys.iter().enumerate() {
            let mut s = hash128(k) as usize & t.mask;
            while t.slots[s] != u32::MAX {
                s = (s + 1) & t.mask;
            }
            t.slots[s] = i as u32;
        }
        t
    }
    pub fn load(lmax: usize) -> Table {
        let (l, lists) = read_file(&format!("{}/algs_L{}.bin", crate::cubie::out_dir(), lmax));
        assert_eq!(l, lmax);
        Table::from_lists(l, &lists, lmax)
    }
    /// The element with this state, if it has any sequence of length <= lmax.
    #[inline]
    pub fn find(&self, key: u128) -> Option<u32> {
        let mut s = hash128(key) as usize & self.mask;
        loop {
            let i = self.slots[s];
            if i == u32::MAX {
                return None;
            }
            if self.ekeys[i as usize] == key {
                return Some(i);
            }
            s = (s + 1) & self.mask;
        }
    }
    /// The same, if it has a sequence of length <= l.
    pub fn find_le(&self, key: u128, l: usize) -> Option<u32> {
        self.find(key).filter(|&e| self.elems[e as usize].opt as usize <= l)
    }
    pub fn groups_of(&self, e: u32) -> &[Group] {
        let el = &self.elems[e as usize];
        &self.groups[el.g0 as usize..el.g1 as usize]
    }
    /// All sequences of length <= l of the element with this key.
    pub fn algs_of(&self, key: u128, l: usize) -> Vec<u64> {
        let mut out = Vec::new();
        if let Some(e) = self.find(key) {
            for g in self.groups_of(e) {
                if g.len as usize <= l {
                    out.extend_from_slice(&self.algs[g.a0 as usize..g.a1 as usize]);
                }
            }
        }
        out
    }
}

// ------------------------------------------------------------------------------------------------------------------
// The independent search for one element.

pub struct Search {
    pub lmax: usize,
    levels: Vec<Level>,
    start: Vec<Vec<u32>>,
    ord: Vec<Vec<u32>>,
    bits: Vec<u32>,
}

impl Search {
    pub fn new(m: &Model, lmax: usize) -> Search {
        let h = (lmax + 1) / 2;
        let levels: Vec<Level> = (0..=h).map(|k| build_level(m, k)).collect();
        let (mut start, mut ord, mut bits) = (Vec::new(), Vec::new(), Vec::new());
        for lv in &levels {
            let n = lv.seq.len();
            let b = (64 - (2 * n as u64).leading_zeros()).max(4);
            let bucket = |i: usize| (hash128((lv.ck[i] as u128) << 64 | lv.ek[i] as u128) >> (64 - b)) as usize;
            let mut st = vec![0u32; (1usize << b) + 1];
            for i in 0..n {
                st[bucket(i) + 1] += 1;
            }
            for i in 0..(1usize << b) {
                st[i + 1] += st[i];
            }
            let mut pos = st.clone();
            let mut o = vec![0u32; n];
            for i in 0..n {
                let bk = bucket(i);
                o[pos[bk] as usize] = i as u32;
                pos[bk] += 1;
            }
            start.push(st);
            ord.push(o);
            bits.push(b);
        }
        Search { lmax, levels, start, ord, bits }
    }

    /// All reduced sequences of length <= lmax with product g, sorted by length then value.
    pub fn algs_of(&self, m: &Model, g: &Cubie) -> Vec<u64> {
        let mut out = Vec::new();
        let mut c: Vec<u8> = Vec::new();
        self.rec(m, g, &mut c, &mut out);
        out.sort_unstable();
        out
    }

    fn rec(&self, m: &Model, s: &Cubie, c: &mut Vec<u8>, out: &mut Vec<u64>) {
        let kb = c.len();
        let h = self.levels.len() - 1;
        let (ck, ek) = (s.ckey(), s.ekey());
        let hv = hash128((ck as u128) << 64 | ek as u128);
        for ka in [kb, kb + 1] {
            if ka == 0 || ka > h || ka + kb > self.lmax {
                continue;
            }
            let lv = &self.levels[ka];
            let b = (hv >> (64 - self.bits[ka])) as usize;
            for &i in &self.ord[ka][self.start[ka][b] as usize..self.start[ka][b + 1] as usize] {
                let i = i as usize;
                if lv.ck[i] != ck || lv.ek[i] != ek {
                    continue;
                }
                let sa = lv.seq[i];
                if kb > 0 && !follows(((sa >> (5 * (ka - 1))) & 31) as u8, inv_move(c[kb - 1])) {
                    continue;
                }
                let mut v = (((ka + kb) as u64) << 60) | sa as u64;
                for t in 0..kb {
                    v |= (inv_move(c[kb - 1 - t]) as u64) << (5 * (ka + t));
                }
                out.push(v);
            }
        }
        if kb == self.lmax / 2 {
            return;
        }
        for mv in 0..18u8 {
            // B = C^-1 must be reduced: the next move of C comes before the last one in B
            if kb > 0 && !follows(mv, c[kb - 1]) {
                continue;
            }
            c.push(mv);
            self.rec(m, &m.turn(s, mv as usize), c, out);
            c.pop();
        }
    }
}

// ------------------------------------------------------------------------------------------------------------------
// Classes under the 24 rotations and inversion.

/// The smallest key among the 48 images of g, and one (rotation, inverted) with image(g) = that.
pub fn class_rep(m: &Model, g: &Cubie) -> u128 {
    let gi = g.inverse();
    let mut best = u128::MAX;
    for r in 0..24 {
        best = best.min(m.conj(g, r).key()).min(m.conj(&gi, r).key());
    }
    best
}

/// A sequence carried along by a rotation of the cube (and inverted when `inv`).
pub fn transport(m: &Model, a: u64, r: usize, inv: bool) -> u64 {
    let s = seq::unpack_vec(a);
    let s = if inv { seq::invert(&s) } else { s };
    seq::pack(&seq::relabel(m, &s, r, false))
}

pub struct ClassRow {
    pub rep: Cubie,
    pub size: usize,
    pub counts: Vec<u64>, // by length 0..=lmax
    pub shortest: Option<u64>,
}

/// The classes of a type, with the sequences of each class read from the table; checks that the lists of all the
/// elements of a class are the images of the representative's list.
pub fn classes(m: &Model, tab: &Table, elements: &[Cubie], lmax: usize, check_transport: bool) -> Vec<ClassRow> {
    let reps: Vec<u128> = elements.par_iter().map(|g| class_rep(m, g)).collect();
    let mut size: HashMap<u128, usize> = HashMap::new();
    for &r in &reps {
        *size.entry(r).or_insert(0) += 1;
    }
    let mut keys: Vec<u128> = size.keys().copied().collect();
    keys.sort_unstable();
    keys.par_iter()
        .map(|&k| {
            let rep = Cubie::from_key(k);
            let list = tab.algs_of(k, lmax);
            let mut counts = vec![0u64; lmax + 1];
            for &a in &list {
                counts[seq::plen(a)] += 1;
            }
            if check_transport {
                let repi = rep.inverse();
                for r in 0..24 {
                    for inv in [false, true] {
                        let g = m.conj(if inv { &repi } else { &rep }, r);
                        let mut want: Vec<u64> = list.iter().map(|&a| transport(m, a, r, inv)).collect();
                        want.sort_unstable();
                        let mut have = tab.algs_of(g.key(), lmax);
                        have.sort_unstable();
                        assert!(want == have, "the list of an element is not the image of its representative's list");
                    }
                }
            }
            ClassRow { rep, size: size[&k], counts, shortest: list.iter().copied().min() }
        })
        .collect()
}

/// The class of a sequence when rotations, reflections, inversion and cyclic shifts all count as the same:
/// the smallest member, and whether some cyclic shift cancels to something shorter.
pub fn cyclic_class(m: &Model, a: u64, seen: &mut std::collections::HashSet<u64>) -> (u64, bool) {
    let n = seq::plen(a);
    let mut todo = vec![a];
    let mut orbit = std::collections::HashSet::new();
    orbit.insert(a);
    let mut shorter = false;
    while let Some(w) = todo.pop() {
        let s = seq::unpack_vec(w);
        let mut next: Vec<Vec<u8>> = Vec::new();
        for r in 0..24 {
            for mir in [false, true] {
                next.push(seq::relabel(m, &s, r, mir));
            }
        }
        next.push(seq::invert(&s));
        // cyclic shifts: any move of the first run can go to the end
        let ax = s[0] / 6;
        let mut i = 0;
        while i < s.len() && s[i] / 6 == ax {
            let mut t: Vec<u8> = s.iter().enumerate().filter(|&(j, _)| j != i).map(|(_, &x)| x).collect();
            t.push(s[i]);
            let t = seq::cancel(&t);
            if t.len() < n {
                shorter = true;
            } else {
                next.push(t);
            }
            i += 1;
        }
        for t in next {
            let t = seq::cancel(&t);
            let p = seq::pack(&t);
            if orbit.insert(p) {
                todo.push(p);
            }
        }
    }
    let rep = *orbit.iter().min().unwrap();
    for w in orbit {
        seen.insert(w);
    }
    (rep, shorter)
}

pub fn elements_all(t: usize) -> Vec<Cubie> {
    if t == types::T2C2E {
        types::elements_2c2e()
    } else {
        types::elements(t)
    }
}

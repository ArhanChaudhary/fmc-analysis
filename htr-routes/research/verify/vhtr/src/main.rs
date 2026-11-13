//! vhtr: an independent recount for the htr-routes study.
//!
//! Nothing here comes from htrtools.  The model and the table index are ported from the Lean sources of
//! judging-a-dr/lean/DRBound (Cube.lean: positions and `srcC/srcE/srcS`; Exact.lean: `rank8`, the 16
//! symmetries, `classData`, `s12`, `ridx`), so the exact table `lean_exact_table.u8` (written by DRBound's
//! `mkTable 18`, proved by `exact_optimal`) is read the way Lean reads it.  Labels, the HTR test, NISS readings
//! and route keys are rebuilt from the definitions in the study (section 3 of the write-up; the "Definitions in
//! the code" of research/README.md; the sticker checker's docstring).
//!
//! Commands
//!   check                       table sanity: solved = 0, every move 1, |d(x) - d(x m)| <= 1 and some
//!                               neighbour one closer, on random walks; coset count 29,400, |H| corners 96
//!   qtcos                       per HTR coset: label and quarter turns to HTR (0-1 search)
//!   s18                         every table entry of 18: its four side half turns lead to 17
//!   lastmove                    exact share of DR states with d(X R2) < d(X), over the whole table
//!   nissall <file|->            the shortest NISS HTR of every DR state (two-sided search over the whole group)
//!   lsall <lsdist48.tsv>        the leave-slice optimum of every state, per subset x edges, against that file
//!   ex "<moves>" ...            optimum, labels, linear and NISS HTR, every optimal finish with its corner path,
//!                               sections and the shortest HTR over its readings (and where they switch)
//!   red "<moves>" <rmax> <q>    reductions to 1q (q=1) / 2q (q=2) of length <= rmax: distinct states, best total
//!   cmp <states.tsv> <routes.bin> <keys.tsv> <from> <n>
//!                               recompute every H route of states from..from+n (optimal and +1, HTR lengths),
//!                               the optimum, both labels and the NISS HTR, and compare with htrtools' records
//!   b4 <states.tsv> <bound4.tsv> <cell> <from> <n> <rmax>
//!                               bounding as stated, by brute force over every pair of sequences
//!   b2 <states.tsv> <bound2.tsv> <cell> <from> <n>
//!                               late-switch data and per-path window reductions, against bound2.tsv
//!   rc <states.tsv> <redcount2.tsv> <cell> <i,j,...> <rmax>
//!                               reduction counts by brute force
//!   page                        facts for the examples page (driven by check_examples_page.py)
//!   dump <states.tsv> <from> <n> <out>
//!                               per state: optimum, NISS HTR, each corner route with its min HTR
use rayon::prelude::*;
use std::collections::{HashMap, HashSet};
use std::io::{BufRead, Write};

// ---------------------------------------------------------------- model (DRBound/Cube.lean)
//   corners 0 UFR 1 UFL 2 UBL 3 UBR 4 DFR 5 DFL 6 DBL 7 DBR
//   U/D edges 0 UF 1 UL 2 UB 3 UR 4 DF 5 DL 6 DB 7 DR ; E slice 0 FR 1 FL 2 BL 3 BR
//   after move m, position p holds what was at src[p]
const NAMES: [&str; 10] = ["U", "U2", "U'", "D", "D2", "D'", "R2", "L2", "F2", "B2"];
const SRC_C: [[u8; 8]; 10] = [
    [3, 0, 1, 2, 4, 5, 6, 7], [2, 3, 0, 1, 4, 5, 6, 7], [1, 2, 3, 0, 4, 5, 6, 7],
    [0, 1, 2, 3, 5, 6, 7, 4], [0, 1, 2, 3, 6, 7, 4, 5], [0, 1, 2, 3, 7, 4, 5, 6],
    [7, 1, 2, 4, 3, 5, 6, 0], [0, 6, 5, 3, 4, 2, 1, 7], [5, 4, 2, 3, 1, 0, 6, 7], [0, 1, 7, 6, 4, 5, 3, 2],
];
const SRC_E: [[u8; 8]; 10] = [
    [3, 0, 1, 2, 4, 5, 6, 7], [2, 3, 0, 1, 4, 5, 6, 7], [1, 2, 3, 0, 4, 5, 6, 7],
    [0, 1, 2, 3, 5, 6, 7, 4], [0, 1, 2, 3, 6, 7, 4, 5], [0, 1, 2, 3, 7, 4, 5, 6],
    [0, 1, 2, 7, 4, 5, 6, 3], [0, 5, 2, 3, 4, 1, 6, 7], [4, 1, 2, 3, 0, 5, 6, 7], [0, 1, 6, 3, 4, 5, 2, 7],
];
const SRC_S: [[u8; 4]; 10] = [
    [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3],
    [3, 1, 2, 0], [0, 2, 1, 3], [1, 0, 2, 3], [0, 1, 3, 2],
];
const INV: [usize; 10] = [2, 1, 0, 5, 4, 3, 6, 7, 8, 9];
const FACE: [usize; 10] = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5];
fn is_qt(m: usize) -> bool { matches!(m, 0 | 2 | 3 | 5) }
fn axis(m: usize) -> usize { FACE[m] / 2 }

#[derive(Clone, Copy, PartialEq, Eq, Hash, Debug)]
struct St { c: [u8; 8], e: [u8; 8], s: [u8; 4] }
const ID: St = St { c: [0, 1, 2, 3, 4, 5, 6, 7], e: [0, 1, 2, 3, 4, 5, 6, 7], s: [0, 1, 2, 3] };
impl St {
    fn mv(&self, m: usize) -> St {
        let mut r = *self;
        for p in 0..8 { r.c[p] = self.c[SRC_C[m][p] as usize]; r.e[p] = self.e[SRC_E[m][p] as usize]; }
        for p in 0..4 { r.s[p] = self.s[SRC_S[m][p] as usize]; }
        r
    }
    /// self, then b
    fn then(&self, b: &St) -> St {
        let mut r = *self;
        for p in 0..8 { r.c[p] = self.c[b.c[p] as usize]; r.e[p] = self.e[b.e[p] as usize]; }
        for p in 0..4 { r.s[p] = self.s[b.s[p] as usize]; }
        r
    }
    fn inv(&self) -> St {
        let mut r = *self;
        for p in 0..8 { r.c[self.c[p] as usize] = p as u8; r.e[self.e[p] as usize] = p as u8; }
        for p in 0..4 { r.s[self.s[p] as usize] = p as u8; }
        r
    }
    fn apply(&self, w: &[usize]) -> St { w.iter().fold(*self, |g, &m| g.mv(m)) }
}
fn parse(t: &str) -> Vec<usize> {
    t.split_whitespace().map(|x| NAMES.iter().position(|n| *n == x).unwrap_or_else(|| panic!("move {}", x))).collect()
}
fn inv_seq(w: &[usize]) -> Vec<usize> { w.iter().rev().map(|&m| INV[m]).collect() }
fn fmt(w: &[usize]) -> String { w.iter().map(|&m| NAMES[m]).collect::<Vec<_>>().join(" ") }
/// canonical: no two moves on one face in a row, at most two in a row on one axis
fn may_follow(prev2: Option<usize>, prev: Option<usize>, m: usize) -> bool {
    if let Some(p) = prev {
        if FACE[p] == FACE[m] { return false; }
        if let Some(q) = prev2 { if axis(q) == axis(p) && axis(p) == axis(m) { return false; } }
    }
    true
}

// ---------------------------------------------------------------- table index (DRBound/Exact.lean)
fn rank8(v: &[u8; 8]) -> usize {
    let mut r = 0;
    for i in 0..8 {
        let k = (i + 1..8).filter(|&j| v[j] < v[i]).count();
        r = r * (8 - i) + k;
    }
    r
}
fn unrank_n<const N: usize>(mut r: usize) -> [u8; N] {
    let mut fact = [1usize; 9];
    for i in 1..9 { fact[i] = fact[i - 1] * i; }
    let mut avail: Vec<u8> = (0..N as u8).collect();
    let mut out = [0u8; N];
    for i in 0..N {
        let f = fact[N - 1 - i];
        let x = avail.remove(r / f);
        r %= f;
        out[i] = x;
    }
    out
}
fn parity(v: &[u8]) -> usize {
    let mut k = 0;
    for i in 0..v.len() { for j in i + 1..v.len() { if v[j] < v[i] { k += 1; } } }
    k % 2
}
#[derive(Clone, Copy)]
struct PosMap { c: [u8; 8], e: [u8; 8], s: [u8; 4] }
const PM_ONE: PosMap = PosMap { c: [0, 1, 2, 3, 4, 5, 6, 7], e: [0, 1, 2, 3, 4, 5, 6, 7], s: [0, 1, 2, 3] };
const SYM_Y: PosMap = PosMap { c: [1, 2, 3, 0, 5, 6, 7, 4], e: [1, 2, 3, 0, 5, 6, 7, 4], s: [1, 2, 3, 0] };
const SYM_X2: PosMap = PosMap { c: [7, 6, 5, 4, 3, 2, 1, 0], e: [6, 5, 4, 7, 2, 1, 0, 3], s: [3, 2, 1, 0] };
const SYM_M: PosMap = PosMap { c: [1, 0, 3, 2, 5, 4, 7, 6], e: [0, 3, 2, 1, 4, 7, 6, 5], s: [1, 0, 3, 2] };
fn and_then(a: &PosMap, b: &PosMap) -> PosMap {
    let mut r = *a;
    for p in 0..8 { r.c[p] = b.c[a.c[p] as usize]; r.e[p] = b.e[a.e[p] as usize]; }
    for p in 0..4 { r.s[p] = b.s[a.s[p] as usize]; }
    r
}
fn pm_inv(a: &PosMap) -> PosMap {
    let mut r = *a;
    for p in 0..8 { r.c[a.c[p] as usize] = p as u8; r.e[a.e[p] as usize] = p as u8; }
    for p in 0..4 { r.s[a.s[p] as usize] = p as u8; }
    r
}
fn mk_sym(i: usize) -> PosMap {
    let mut a = if i / 8 % 2 == 1 { SYM_M } else { PM_ONE };
    if i / 4 % 2 == 1 { a = and_then(&a, &SYM_X2); }
    for _ in 0..i % 4 { a = and_then(&a, &SYM_Y); }
    a
}
fn conj8(t: &[u8; 8], ti: &[u8; 8], v: &[u8; 8]) -> [u8; 8] {
    let mut r = [0u8; 8];
    for q in 0..8 { r[q] = t[v[ti[q] as usize] as usize]; }
    r
}
fn conj4(t: &[u8; 4], ti: &[u8; 4], v: &[u8; 4]) -> [u8; 4] {
    let mut r = [0u8; 4];
    for q in 0..4 { r[q] = t[v[ti[q] as usize] as usize]; }
    r
}
struct Table {
    syms: Vec<PosMap>,
    sinv: Vec<PosMap>,
    cls: Vec<u32>,
    symto: Vec<u8>,
    s12: Vec<u8>,
    t: Vec<u8>,
}
impl Table {
    fn load(path: &str) -> Table {
        let syms: Vec<PosMap> = (0..16).map(mk_sym).collect();
        let sinv: Vec<PosMap> = syms.iter().map(pm_inv).collect();
        let sym_inv: Vec<u8> = (0..16)
            .map(|i| (0..16).find(|&r| syms[r].c == sinv[i].c).unwrap_or(0) as u8)
            .collect();
        let mut cls = vec![u32::MAX; 40320];
        let mut symto = vec![0u8; 40320];
        let mut nrep = 0u32;
        for r in 0..40320 {
            if cls[r] == u32::MAX {
                let c: [u8; 8] = unrank_n::<8>(r);
                let k = nrep;
                nrep += 1;
                for s in 0..16 {
                    let d = rank8(&conj8(&syms[s].c, &sinv[s].c, &c));
                    if cls[d] == u32::MAX { cls[d] = k; symto[d] = sym_inv[s]; }
                }
            }
        }
        assert_eq!(nrep, 2768);
        // E slice: the 24 arrangements in nested a,b,c,d order, parity 0 then parity 1
        let mut perms4 = vec![];
        for a in 0..4u8 { for b in 0..4u8 { for c in 0..4u8 { for d in 0..4u8 {
            let v = [a, b, c, d];
            let mut seen = [false; 4];
            if v.iter().all(|&x| { let f = !seen[x as usize]; seen[x as usize] = true; f }) { perms4.push(v); }
        }}}}
        let tab: Vec<[u8; 4]> = perms4.iter().filter(|v| parity(&v[..]) == 0)
            .chain(perms4.iter().filter(|v| parity(&v[..]) == 1)).cloned().collect();
        let mut s12 = vec![0u8; 256];
        for (i, v) in tab.iter().enumerate() {
            let code = ((v[0] as usize * 4 + v[1] as usize) * 4 + v[2] as usize) * 4 + v[3] as usize;
            s12[code] = (i % 12) as u8;
        }
        let t = std::fs::read(path).expect("table");
        assert_eq!(t.len(), 2768 * 40320 * 12);
        Table { syms, sinv, cls, symto, s12, t }
    }
    fn d(&self, g: &St) -> u8 {
        let rc = rank8(&g.c);
        let k = self.cls[rc] as usize;
        let s = self.symto[rc] as usize;
        let e = conj8(&self.syms[s].e, &self.sinv[s].e, &g.e);
        let sl = conj4(&self.syms[s].s, &self.sinv[s].s, &g.s);
        let code = ((sl[0] as usize * 4 + sl[1] as usize) * 4 + sl[2] as usize) * 4 + sl[3] as usize;
        self.t[(k * 40320 + rank8(&e)) * 12 + self.s12[code] as usize]
    }
}

// ---------------------------------------------------------------- labels, HTR, cosets (study 1's names)
const TETRAD_A: [bool; 8] = [true, false, true, false, false, true, false, true]; // UFR UBL DFL DBR
const MPOS: [bool; 8] = [true, false, true, false, true, false, true, false]; // UF UB DF DB
const FACES: [[u8; 4]; 6] = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 3, 4, 7], [1, 2, 5, 6], [0, 1, 4, 5], [2, 3, 6, 7]];
fn emask(e: &[u8; 8]) -> usize {
    let mut m = 0;
    for p in 0..8 { if MPOS[e[p] as usize] { m |= 1 << p; } }
    m
}
const HTR_MASK: usize = 0b01010101;
struct Labels {
    qtc: Vec<u8>,     // corner qt count by corner rank
    hc: Vec<bool>,    // corner rank in the half-turn group
    names: Vec<String>,
    lab: Vec<u8>,     // [corner rank * 256 + edge mask] -> name id
    orbit: Vec<u16>,  // corner rank -> orbit under relabelling by HC (left cosets)
    cdist: Vec<u8>,   // [orbit * 256 + mask] -> linear HTR length
    ncos: usize,
}
fn cmove(c: &[u8; 8], m: usize) -> [u8; 8] {
    let mut r = *c;
    for p in 0..8 { r[p] = c[SRC_C[m][p] as usize]; }
    r
}
impl Labels {
    fn new() -> Labels {
        // corner qt count: 0-1 BFS from solved and from U D'
        let mut qtc = vec![u8::MAX; 40320];
        let mut dq = std::collections::VecDeque::new();
        let ud = cmove(&cmove(&ID.c, 0), 5);
        for c in [ID.c, ud] { qtc[rank8(&c)] = 0; dq.push_back(c); }
        while let Some(x) = dq.pop_front() {
            let dx = qtc[rank8(&x)];
            for m in 0..10 {
                let y = cmove(&x, m);
                let w = is_qt(m) as u8;
                let ry = rank8(&y);
                if qtc[ry] == u8::MAX || dx + w < qtc[ry] {
                    qtc[ry] = dx + w;
                    if w == 1 { dq.push_back(y) } else { dq.push_front(y) }
                }
            }
        }
        assert!(qtc.iter().all(|&q| q != u8::MAX));
        let mut hc = vec![false; 40320];
        let mut hcl = vec![ID.c];
        hc[rank8(&ID.c)] = true;
        let mut i = 0;
        while i < hcl.len() {
            let x = hcl[i]; i += 1;
            for m in [1, 4, 6, 7, 8, 9] {
                let y = cmove(&x, m);
                if !hc[rank8(&y)] { hc[rank8(&y)] = true; hcl.push(y); }
            }
        }
        assert_eq!(hcl.len(), 96);
        // shape of a set of 4 corner positions: 'a' if half turns can bring it onto one face
        let mut shape = vec![b'b'; 256];
        for s in 0..256usize {
            if (s as u32).count_ones() != 4 { continue; }
            let mut seen = HashSet::new();
            let mut st = vec![s];
            seen.insert(s);
            while let Some(x) = st.pop() {
                if FACES.iter().any(|f| f.iter().fold(0, |a, &p| a | 1 << p) == x) { shape[s] = b'a'; }
                for m in [1, 4, 6, 7, 8, 9] {
                    // position q goes to p where src[p] = q
                    let mut y = 0;
                    for p in 0..8 { if x >> SRC_C[m][p] & 1 == 1 { y |= 1 << p; } }
                    if seen.insert(y) { st.push(y); }
                }
            }
        }
        let mut names: Vec<String> = vec![];
        let mut ids: HashMap<String, u8> = HashMap::new();
        let mut lab = vec![0u8; 40320 * 256];
        for r in 0..40320 {
            let c: [u8; 8] = unrank_n::<8>(r);
            let mut badpos = 0usize;
            for p in 0..8 { if TETRAD_A[p] != TETRAD_A[c[p] as usize] { badpos |= 1 << p; } }
            let n = badpos.count_ones() as usize;
            for mask in 0..256usize {
                if mask.count_ones() != 4 { continue; }
                let mut ne = 0;
                for p in 0..8 { if MPOS[p] != (mask >> p & 1 == 1) { ne += 1; } }
                let (nb, ne) = if n > 4 || (n == 4 && ne > 4) { (8 - n, 8 - ne) } else { (n, ne) };
                let letter = if nb == 4 { shape[badpos] as char } else { 'c' };
                let name = format!("{}{}{} {}e", nb, letter, qtc[r], ne);
                let id = *ids.entry(name.clone()).or_insert_with(|| { names.push(name.clone()); (names.len() - 1) as u8 });
                lab[r * 256 + mask] = id;
            }
        }
        // left cosets of H: corner orbit under relabelling by HC, and where the M pieces are
        let hcp: Vec<[u8; 8]> = hcl.clone();
        let mut orbit = vec![u16::MAX; 40320];
        let mut no = 0u16;
        for r in 0..40320 {
            if orbit[r] != u16::MAX { continue; }
            let c: [u8; 8] = unrank_n::<8>(r);
            for h in &hcp {
                let mut y = [0u8; 8];
                for p in 0..8 { y[p] = h[c[p] as usize]; }
                orbit[rank8(&y)] = no;
            }
            no += 1;
        }
        assert_eq!(no, 420);
        let mut cdist = vec![u8::MAX; 420 * 256];
        let key = |g: &St| orbit[rank8(&g.c)] as usize * 256 + emask(&g.e);
        cdist[key(&ID)] = 0;
        let mut q = vec![ID];
        let mut i = 0;
        while i < q.len() {
            let g = q[i]; i += 1;
            let dg = cdist[key(&g)];
            for m in 0..10 {
                let y = g.mv(m);
                let k = key(&y);
                if cdist[k] == u8::MAX { cdist[k] = dg + 1; q.push(y); }
            }
        }
        let ncos = q.len();
        Labels { qtc, hc, names, lab, orbit, cdist, ncos }
    }
    fn label(&self, g: &St) -> u8 { self.lab[rank8(&g.c) * 256 + emask(&g.e)] }
    fn name(&self, g: &St) -> &str { &self.names[self.label(g) as usize] }
    fn in_htr(&self, g: &St) -> bool { self.hc[rank8(&g.c)] && emask(&g.e) == HTR_MASK }
    fn lin(&self, g: &St) -> u8 { self.cdist[self.orbit[rank8(&g.c)] as usize * 256 + emask(&g.e)] }
    /// shortest NISS HTR: min |A| + |B| with A on normal and B on inverse reaching HTR
    fn niss(&self, x: &St) -> u8 {
        let xi = x.inv();
        let mut best = self.lin(x).min(self.lin(&xi));
        // either |A| or |B| is at most half of any solution; search each side up to depth 7 (covers <= 15)
        for start in [*x, xi] {
            fn dfs(l: &Labels, g: &St, depth: u8, p2: Option<usize>, p1: Option<usize>, best: &mut u8) {
                let v = depth + l.lin(&g.inv());
                if v < *best { *best = v; }
                if depth + 1 >= *best || depth >= 7 { return; }
                for m in 0..10 {
                    if !may_follow(p2, p1, m) { continue; }
                    dfs(l, &g.mv(m), depth + 1, p1, Some(m), best);
                }
            }
            dfs(self, &start, 0, None, None, &mut best);
        }
        best
    }
}

// ---------------------------------------------------------------- finishes and readings
fn finishes(t: &Table, x: &St, len: usize) -> Vec<Vec<usize>> {
    fn go(t: &Table, g: &St, r: usize, w: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
        if r == 0 { if *g == ID { out.push(w.clone()); } return; }
        let n = w.len();
        for m in 0..10 {
            if !may_follow(if n >= 2 { Some(w[n - 2]) } else { None }, w.last().copied(), m) { continue; }
            let y = g.mv(m);
            if t.d(&y) as usize > r - 1 { continue; }
            w.push(m);
            go(t, &y, r - 1, w, out);
            w.pop();
        }
    }
    let mut out = vec![];
    if t.d(x) as usize <= len { go(t, x, len, &mut vec![], &mut out); }
    out
}
/// One NISS reading: the finish `f` of `x`, split at k, normal first or inverse first.
/// Returns (H key with edge counts, HTR length, corner-only route, switch after this many moves on side 1 or None).
struct Reading { key: String, htr: u8, route: String, sw_after: Option<usize> }
fn reading(l: &Labels, x: &St, xi: &St, f: &[usize], k: usize, inv_first: bool) -> Reading {
    let a: Vec<usize> = f[..k].to_vec();
    let b: Vec<usize> = inv_seq(&f[k..]);
    let (mut s1, mut part1, mut part2) = if inv_first { (*xi, b.clone(), a.clone()) } else { (*x, a.clone(), b.clone()) };
    let s2_of = |p1: &[usize]| -> St { if inv_first { xi.apply(p1).inv() } else { x.apply(p1).inv() } };
    let q1 = part1.iter().any(|&m| is_qt(m));
    let q2 = part2.iter().any(|&m| is_qt(m));
    let mut pre = 0usize;
    let mut folded: Vec<usize> = vec![];
    if !q1 && !part2.is_empty() {
        s1 = s2_of(&part1);
        pre = part1.len();
        part1 = std::mem::take(&mut part2);
    } else if !q2 && !part2.is_empty() {
        folded = std::mem::take(&mut part2);
    }
    let s2 = s2_of(&part1);
    let seq: Vec<(u8, usize)> = part1.iter().map(|&m| (1u8, m)).chain(part2.iter().map(|&m| (2u8, m))).collect();
    let mut hl: Vec<u8> = vec![l.label(&s1)];
    let mut hsw: Option<usize> = None;
    let mut hdone = l.in_htr(&s1);
    let mut htr = if hdone { Some(pre) } else { None };
    let mut done_at = 0usize;
    let mut st = s1;
    let mut side = 1u8;
    let mut moved = pre;
    let mut sw_after = None;
    for (idx, &(sd, m)) in seq.iter().enumerate() {
        if sd == 2 && side == 1 {
            side = 2;
            st = s2;
            if !hdone { hsw = Some(hl.len()); sw_after = Some(moved); }
        }
        st = st.mv(m);
        moved += 1;
        if is_qt(m) && !hdone {
            hl.push(l.label(&st));
            if l.in_htr(&st) { hdone = true; htr = Some(moved); done_at = idx + 1; }
        }
    }
    let post_qt = seq[done_at.min(seq.len())..].iter().any(|&(_, m)| is_qt(m)) || folded.iter().any(|&m| is_qt(m));
    let mut parts = vec![];
    let mut cparts = vec![];
    for (i, &lb) in hl.iter().enumerate() {
        let nm = &l.names[lb as usize];
        let open = if hsw == Some(i) { "(" } else { "" };
        parts.push(format!("{}{}", open, nm));
        cparts.push(format!("{}{}", open, nm.split(' ').next().unwrap()));
    }
    let close = if hsw.is_some() { ")" } else { "" };
    let tail = if post_qt { " | qt" } else { " | ht" };
    Reading {
        key: format!("H:{}{}{}", parts.join(" > "), close, tail),
        htr: htr.expect("finish never reached HTR") as u8,
        route: format!("{}{}{}", cparts.join(" > "), close, tail),
        sw_after,
    }
}
/// (key -> (has an optimal reading, min HTR over optimal readings, min HTR over all readings <= opt+1))
fn route_map(t: &Table, l: &Labels, x: &St, corner: bool) -> (u8, HashMap<String, (bool, u8, u8)>, usize, usize) {
    let d = t.d(x) as usize;
    let xi = x.inv();
    let mut map: HashMap<String, (bool, u8, u8)> = HashMap::new();
    let opt = finishes(t, x, d);
    let p1 = finishes(t, x, d + 1);
    for (lvl, fs) in [(0, &opt), (1, &p1)] {
        for f in fs.iter() {
            for k in 0..=f.len() {
                for invf in [false, true] {
                    let r = reading(l, x, &xi, f, k, invf);
                    let key = if corner { r.route } else { r.key };
                    let e = map.entry(key).or_insert((false, u8::MAX, u8::MAX));
                    if lvl == 0 { e.0 = true; e.1 = e.1.min(r.htr); }
                    e.2 = e.2.min(r.htr);
                }
            }
        }
    }
    (d as u8, map, opt.len(), p1.len())
}

// ---------------------------------------------------------------- commands
const TABLE: &str = "/data/fmc/judging-a-dr/research/data/lean_exact_table.u8";
fn table_path() -> String { std::env::var("VHTR_TABLE").unwrap_or(TABLE.to_string()) }

fn corner_path(l: &Labels, x: &St, f: &[usize]) -> (Vec<String>, Vec<usize>) {
    // labels at the start and after each quarter turn until HTR; half-turn sections between quarter turns
    let mut g = *x;
    let mut path = vec![l.name(&g).to_string()];
    let mut secs = vec![0usize];
    let mut done = l.in_htr(&g);
    for &m in f {
        g = g.mv(m);
        if is_qt(m) {
            if !done { path.push(l.name(&g).to_string()); }
            if l.in_htr(&g) { done = true; }
            secs.push(0);
        } else {
            *secs.last_mut().unwrap() += 1;
        }
    }
    (path, secs)
}

fn cmd_ex(t: &Table, l: &Labels, mv: &str) {
    let x = ID.apply(&parse(mv));
    let xi = x.inv();
    let d = t.d(&x) as usize;
    println!("state: {}", mv);
    println!("label normal {} / inverse {}; optimal {}", l.name(&x), l.name(&xi), d);
    println!("linear HTR normal {} inverse {}; NISS HTR {}", l.lin(&x), l.lin(&xi), l.niss(&x));
    let opt = finishes(t, &x, d);
    println!("optimal finishes: {}", opt.len());
    let mut best = u8::MAX;
    let mut rd = vec![];
    for f in &opt {
        let (path, secs) = corner_path(l, &x, f);
        if opt.len() <= 40 { println!("  {}  path {}  sections {:?}", fmt(f), path.join(" > "), secs); }
        for k in 0..=f.len() {
            for invf in [false, true] {
                let r = reading(l, &x, &xi, f, k, invf);
                best = best.min(r.htr);
                rd.push((r.htr, fmt(f), k, invf, r.sw_after, r.key));
            }
        }
    }
    let mut paths: HashMap<String, usize> = HashMap::new();
    for f in &opt { *paths.entry(corner_path(l, &x, f).0.join(" > ")).or_insert(0) += 1; }
    println!("distinct corner paths of the optimal finishes: {:?}", paths);
    println!("shortest HTR over every reading of every optimal finish: {}", best);
    let mut sws: HashMap<String, usize> = HashMap::new();
    for r in rd.iter().filter(|r| r.0 == best) {
        *sws.entry(format!("{:?}", r.4)).or_insert(0) += 1;
    }
    println!("  readings with that HTR, by moves before the switch (None = no switch before HTR): {:?}", sws);
    for r in rd.iter().filter(|r| r.0 == best).take(6) {
        println!("    {} split {} inverse-first {} switch-after {:?} {}", r.1, r.2, r.3, r.4, r.5);
    }
}

fn cmd_red(t: &Table, l: &Labels, mv: &str, rmax: usize, q: usize) {
    // reductions: P on normal, U on inverse, each empty or ending in a quarter turn; state = U^-1, X, P
    let x = ID.apply(&parse(mv));
    let d = t.d(&x) as usize;
    let mut seqs: Vec<Vec<usize>> = vec![vec![]];
    fn gen(w: &mut Vec<usize>, r: usize, out: &mut Vec<Vec<usize>>) {
        if r == 0 { return; }
        let n = w.len();
        for m in 0..10 {
            if !may_follow(if n >= 2 { Some(w[n - 2]) } else { None }, w.last().copied(), m) { continue; }
            w.push(m);
            if is_qt(m) { out.push(w.clone()); }
            gen(w, r - 1, out);
            w.pop();
        }
    }
    gen(&mut vec![], rmax, &mut seqs);
    let target = |g: &St| -> bool {
        let nm = l.name(g);
        if q == 1 { nm == "4a1 4e" } else { nm.starts_with("4a2") || nm.starts_with("4b2") || (nm.starts_with("0c0") && nm != "0c0 0e") }
    };
    let mut states: HashMap<St, usize> = HashMap::new();
    for p in &seqs {
        let xp = x.apply(p);
        for u in &seqs {
            if p.len() + u.len() > rmax { continue; }
            let g = ID.apply(&inv_seq(u)).then(&xp);
            if target(&g) {
                let e = states.entry(g).or_insert(usize::MAX);
                *e = (*e).min(p.len() + u.len());
            }
        }
    }
    let best = states.iter().map(|(g, &r)| r + t.d(g) as usize).min();
    let mut by_len = vec![0usize; rmax + 1];
    for (_, &r) in &states { by_len[r] += 1; }
    println!("{}: optimal {}; reductions to {}q of length <= {}: {} distinct states (by shortest length {:?}); best total {:?}",
        mv, d, q, rmax, states.len(), by_len, best);
}

fn load_keys(path: &str, need: &HashSet<u32>) -> HashMap<u32, String> {
    let f = std::io::BufReader::new(std::fs::File::open(path).unwrap());
    let mut m = HashMap::new();
    for line in f.lines().skip(1) {
        let line = line.unwrap();
        let (a, b) = line.split_once('\t').unwrap();
        let id: u32 = a.parse().unwrap();
        if need.contains(&id) { m.insert(id, b.to_string()); }
    }
    m
}
struct Row { c: usize, e: usize, s: usize, d: u8, niss: u8, lab_n: String, lab_i: String }
fn read_states(path: &str) -> Vec<Row> {
    let f = std::io::BufReader::new(std::fs::File::open(path).unwrap());
    let mut it = f.lines();
    let hdr: Vec<String> = it.next().unwrap().unwrap().split('\t').map(|s| s.to_string()).collect();
    let col = |n: &str| hdr.iter().position(|h| h == n).unwrap();
    let (ci, ei, si, di, ni, ln, li) = (col("c"), col("e"), col("s"), col("d"), col("htrNiss"), col("lab_n"), col("lab_i"));
    it.map(|l| {
        let l = l.unwrap();
        let v: Vec<&str> = l.split('\t').collect();
        Row { c: v[ci].parse().unwrap(), e: v[ei].parse().unwrap(), s: v[si].parse().unwrap(), d: v[di].parse().unwrap(),
              niss: v[ni].parse().unwrap(), lab_n: v[ln].to_string(), lab_i: v[li].to_string() }
    }).collect()
}
fn st_of(r: &Row) -> St { St { c: unrank_n::<8>(r.c), e: unrank_n::<8>(r.e), s: unrank_n::<4>(r.s) } }

fn cmd_cmp(t: &Table, l: &Labels, states: &str, bin: &str, keys: &str, from: usize, n: usize) {
    let rows = read_states(states);
    let raw = std::fs::read(bin).unwrap();
    let words: Vec<u64> = raw.chunks_exact(8).map(|c| u64::from_le_bytes(c.try_into().unwrap())).collect();
    // per state: [len, recs (X)], [len, recs (X R2)]
    let mut pos = 0usize;
    let mut recs: Vec<Vec<u64>> = vec![];
    for _ in 0..rows.len() {
        let a = words[pos] as usize;
        recs.push(words[pos + 1..pos + 1 + a].to_vec());
        pos += 1 + a;
        let b = words[pos] as usize;
        pos += 1 + b;
    }
    assert_eq!(pos, words.len());
    let sel: Vec<usize> = (from..(from + n).min(rows.len())).collect();
    let mut need = HashSet::new();
    for &i in &sel { for &w in &recs[i] { need.insert((w >> 11) as u32); } }
    let kmap = load_keys(keys, &need);
    let res: Vec<(usize, Vec<String>, usize, usize)> = sel.par_iter().map(|&i| {
        let r = &rows[i];
        let x = st_of(r);
        let mut bad = vec![];
        let d = t.d(&x);
        if d != r.d { bad.push(format!("d {} vs {}", d, r.d)); }
        if l.name(&x) != r.lab_n { bad.push(format!("label {} vs {}", l.name(&x), r.lab_n)); }
        if l.name(&x.inv()) != r.lab_i { bad.push(format!("inverse label {} vs {}", l.name(&x.inv()), r.lab_i)); }
        let nh = l.niss(&x);
        if nh != r.niss { bad.push(format!("NISS HTR {} vs {}", nh, r.niss)); }
        let (_, mine, _, _) = route_map(t, l, &x, false);
        let mut theirs: HashMap<String, (bool, u8, u8)> = HashMap::new();
        for &w in &recs[i] {
            let k = &kmap[&((w >> 11) as u32)];
            if !k.starts_with("H:") { continue; }
            let hl = ((w >> 6) & 31) as u8;
            let hany = ((w >> 1) & 31) as u8;
            let delta = (w & 1) == 1;
            theirs.insert(k.clone(), (!delta, if delta { u8::MAX } else { hl }, hany));
            if delta && hl != hany { bad.push(format!("{}: delta 1 but hl {} != hany {}", k, hl, hany)); }
        }
        for (k, v) in &mine {
            match theirs.get(k) {
                None => bad.push(format!("missing in htrtools: {} {:?}", k, v)),
                Some(w) if w != v => bad.push(format!("differs: {} mine {:?} theirs {:?}", k, v, w)),
                _ => {}
            }
        }
        for (k, v) in &theirs { if !mine.contains_key(k) { bad.push(format!("extra in htrtools: {} {:?}", k, v)); } }
        let nopt = mine.values().filter(|v| v.0).count();
        (i, bad, mine.len(), nopt)
    }).collect();
    let nbad = res.iter().filter(|r| !r.1.is_empty()).count();
    let nk: usize = res.iter().map(|r| r.2).sum();
    let no: usize = res.iter().map(|r| r.3).sum();
    println!("(state, H route) pairs compared: {} ({} with an optimal reading)", nk, no);
    for (i, b, _, _) in res.iter().filter(|r| !r.1.is_empty()).take(10) {
        println!("state {}: {} problems", i, b.len());
        for x in b.iter().take(8) { println!("   {}", x); }
    }
    println!("{}: {} states compared, {} with differences", states, res.len(), nbad);
}

fn cmd_dump(t: &Table, l: &Labels, states: &str, from: usize, n: usize, out: &str) {
    let rows = read_states(states);
    let sel: Vec<usize> = (from..(from + n).min(rows.len())).collect();
    let res: Vec<String> = sel.par_iter().map(|&i| {
        let x = st_of(&rows[i]);
        let (d, map, no, n1) = route_map(t, l, &x, true);
        let nh = l.niss(&x);
        let mut v: Vec<String> = map.iter().map(|(k, &(o, a, b))| format!("{}={}/{}", k, if o { a as i32 } else { -1 }, b)).collect();
        v.sort();
        format!("{}\t{}\t{}\t{}\t{}\t{}\t{}", i, l.name(&x), d, nh, no, n1, v.join(";"))
    }).collect();
    let mut f = std::io::BufWriter::new(std::fs::File::create(out).unwrap());
    for r in res { writeln!(f, "{}", r).unwrap(); }
}

fn cmd_check(t: &Table, l: &Labels) {
    assert_eq!(t.d(&ID), 0);
    for m in 0..10 { assert_eq!(t.d(&ID.mv(m)), 1, "move {}", NAMES[m]); }
    println!("cosets of H reached: {} (29,400 expected); HTR corner group 96", l.ncos);
    let mut hist = [0usize; 20];
    for c in 0..(420 * 256) { if l.cdist[c] != u8::MAX { hist[l.cdist[c] as usize] += 1; } }
    println!("linear HTR length histogram over cosets: {:?}", &hist[..15]);
    let mut seed = 12345u64;
    let mut rnd = || { seed ^= seed << 13; seed ^= seed >> 7; seed ^= seed << 17; seed };
    let mut bad = 0;
    let mut n = 0;
    for _ in 0..2000 {
        let mut g = ID;
        for _ in 0..40 { g = g.mv((rnd() % 10) as usize); }
        let dg = t.d(&g) as i32;
        let ds: Vec<i32> = (0..10).map(|m| t.d(&g.mv(m)) as i32).collect();
        n += 1;
        if ds.iter().any(|&x| (x - dg).abs() > 1) || (dg > 0 && !ds.contains(&(dg - 1))) { bad += 1; }
        // symmetry: conjugates have the same value
    }
    println!("random states checked {}, violations {}", n, bad);
}


/// canonical sequences of length <= rmax that are empty or end in a quarter turn, grouped by length
fn red_seqs(rmax: usize) -> Vec<Vec<St>> {
    let mut out: Vec<Vec<St>> = vec![vec![]; rmax + 1];
    out[0].push(ID);
    fn gen(w: &mut Vec<usize>, g: St, r: usize, out: &mut Vec<Vec<St>>) {
        if r == 0 { return; }
        let n = w.len();
        for m in 0..10 {
            if !may_follow(if n >= 2 { Some(w[n - 2]) } else { None }, w.last().copied(), m) { continue; }
            let y = g.mv(m);
            w.push(m);
            if is_qt(m) { out[w.len()].push(y); }
            gen(w, y, r - 1, out);
            w.pop();
        }
    }
    gen(&mut vec![], ID, rmax, &mut out);
    out
}
/// qt distance to HTR of every coset (0-1 BFS: quarter turns 1, half turns 0), to compare with the labels
fn cmd_qtcos(l: &Labels) {
    let key = |g: &St| l.orbit[rank8(&g.c)] as usize * 256 + emask(&g.e);
    let mut qd = vec![u8::MAX; 420 * 256];
    let mut rep: HashMap<usize, St> = HashMap::new();
    let mut dq = std::collections::VecDeque::new();
    qd[key(&ID)] = 0; rep.insert(key(&ID), ID); dq.push_back(ID);
    while let Some(g) = dq.pop_front() {
        let dg = qd[key(&g)];
        for m in 0..10 {
            let y = g.mv(m); let k = key(&y); let w = is_qt(m) as u8;
            if qd[k] == u8::MAX || dg + w < qd[k] {
                qd[k] = dg + w; rep.insert(k, y);
                if w == 1 { dq.push_back(y) } else { dq.push_front(y) }
            }
        }
    }
    let mut tab: HashMap<(String, u8), (usize, u8, u8)> = HashMap::new();
    for (k, g) in &rep {
        let e = tab.entry((l.name(g).to_string(), qd[*k])).or_insert((0, 99, 0));
        e.0 += 1; e.1 = e.1.min(l.lin(g)); e.2 = e.2.max(l.lin(g));
    }
    let mut v: Vec<_> = tab.into_iter().collect();
    v.sort();
    for ((nm, q), (n, lo, hi)) in v { println!("{}\tqt-to-HTR {}\tcosets {}\tshortest linear HTR {} to {}", nm, q, n, lo, hi); }
}
/// reduction counts by brute force: pairs (A on normal, B on inverse), canonical, each empty or ending in a qt,
/// |A| + |B| = r, after which the state is 1q (qt distance 1) or 2q (qt distance 2), compared with redcount2.tsv
fn cmd_rc(t: &Table, l: &Labels, states: &str, rc: &str, cell: &str, idxs: &str, rmax: usize) {
    let rows = read_states(states);
    let seqs = red_seqs(rmax);
    let seqs_inv: Vec<Vec<St>> = seqs.iter().map(|v| v.iter().map(|g| g.inv()).collect()).collect();
    // qt distance by coset, as in cmd_qtcos
    let key = |g: &St| l.orbit[rank8(&g.c)] as usize * 256 + emask(&g.e);
    let mut qd = vec![u8::MAX; 420 * 256];
    let mut dq = std::collections::VecDeque::new();
    qd[key(&ID)] = 0; dq.push_back(ID);
    while let Some(g) = dq.pop_front() {
        let dg = qd[key(&g)];
        for m in 0..10 {
            let y = g.mv(m); let k = key(&y); let w = is_qt(m) as u8;
            if qd[k] == u8::MAX || dg + w < qd[k] { qd[k] = dg + w; if w == 1 { dq.push_back(y) } else { dq.push_front(y) } }
        }
    }
    let theirs: HashMap<usize, Vec<String>> = std::fs::read_to_string(rc).unwrap().lines().skip(1)
        .map(|l| l.split('\t').map(|s| s.to_string()).collect::<Vec<_>>())
        .filter(|v| v[0] == cell).map(|v| (v[1].parse().unwrap(), v)).collect();
    let idx: Vec<usize> = idxs.split(',').map(|x| x.parse().unwrap()).collect();
    let res: Vec<String> = idx.par_iter().map(|&i| {
        let x = st_of(&rows[i]);
        let mut cnt = vec![[0u64; 2]; rmax + 1];
        for a in 0..=rmax {
            for ga in &seqs[a] {
                let xa = x.then(ga);
                for b in 0..=(rmax - a) {
                    for gbi in &seqs_inv[b] {
                        let g = gbi.then(&xa);
                        let q = qd[key(&g)];
                        if q == 1 { cnt[a + b][0] += 1; } else if q == 2 { cnt[a + b][1] += 1; }
                    }
                }
            }
        }
        let th = &theirs[&i];
        let mut ok = th[2].parse::<u8>().unwrap() == t.d(&x);
        let mut s = format!("{} idx {} d {}:", cell, i, t.d(&x));
        for r in 0..=rmax {
            let a = th[3 + r].parse::<u64>().unwrap(); let b = th[11 + r].parse::<u64>().unwrap();
            if a != cnt[r][0] || b != cnt[r][1] { ok = false; s += &format!(" r{} mine {}/{} theirs {}/{}", r, cnt[r][0], cnt[r][1], a, b); }
        }
        format!("{} {}", s, if ok { "identical" } else { "DIFFERENT" })
    }).collect();
    for r in res { println!("{}", r); }
}


/// Exact share of DR states X with d(X R2) < d(X), over the whole table.  By the y symmetry the count is the
/// same for R2, L2, F2 and B2, so it is a quarter of the sum over the four, which is constant on symmetry classes;
/// a corner class with n arrangements then counts its entries n times (no orbit-stabiliser step).
fn cmd_lastmove(t: &Table) {
    let mut csize = vec![0u64; 2768];
    let mut rep = vec![[0u8; 8]; 2768];
    let mut seen = vec![false; 2768];
    for r in 0..40320 { let k = t.cls[r] as usize; csize[k] += 1; if !seen[k] { seen[k] = true; rep[k] = unrank_n::<8>(r); } }
    let mut perms4 = vec![];
    for a in 0..4u8 { for b in 0..4u8 { for c in 0..4u8 { for d in 0..4u8 {
        let v = [a, b, c, d];
        let mut sn = [false; 4];
        if v.iter().all(|&x| { let f = !sn[x as usize]; sn[x as usize] = true; f }) { perms4.push(v); }
    }}}}
    let tab: Vec<[u8; 4]> = perms4.iter().filter(|v| parity(&v[..]) == 0).chain(perms4.iter().filter(|v| parity(&v[..]) == 1)).cloned().collect();
    let res: Vec<(u64, u64, u64)> = (0..2768usize).into_par_iter().map(|k| {
        let c = rep[k];
        let (mut shorter, mut longer_than_1, mut n) = (0u64, 0u64, 0u64);
        for e in 0..40320usize {
            let ee: [u8; 8] = unrank_n::<8>(e);
            let p = (parity(&c) + parity(&ee)) % 2;
            for s in 0..12 {
                let g = St { c, e: ee, s: tab[p * 12 + s] };
                let dg = t.t[(k * 40320 + e) * 12 + s] as i32;
                for m in 6..10 {
                    let dm = t.d(&g.mv(m)) as i32;
                    if dm < dg { shorter += 1; }
                    if (dm - dg).abs() > 1 { longer_than_1 += 1; }
                }
                n += 4;
            }
        }
        (shorter * csize[k], longer_than_1 * csize[k], n * csize[k])
    }).collect();
    let (a, b, n) = res.iter().fold((0u64, 0u64, 0u64), |x, y| (x.0 + y.0, x.1 + y.1, x.2 + y.2));
    println!("states x 4 side half turns: {}; one shorter: {} ({:.4}%); differ by more than one: {}", n, a, 100.0 * a as f64 / n as f64, b);
}


fn qt_dist_table(l: &Labels) -> Vec<u8> {
    let key = |g: &St| l.orbit[rank8(&g.c)] as usize * 256 + emask(&g.e);
    let mut qd = vec![u8::MAX; 420 * 256];
    let mut dq = std::collections::VecDeque::new();
    qd[key(&ID)] = 0; dq.push_back(ID);
    while let Some(g) = dq.pop_front() {
        let dg = qd[key(&g)];
        for m in 0..10 {
            let y = g.mv(m); let k = key(&y); let w = is_qt(m) as u8;
            if qd[k] == u8::MAX || dg + w < qd[k] { qd[k] = dg + w; if w == 1 { dq.push_back(y) } else { dq.push_front(y) } }
        }
    }
    qd
}
/// Facts for the examples page, one answer line per job line on stdin:
///   S <scramble>                       labels, HTR lengths, optimum, number of optimal finishes, the shortest
///                                      reduction whose middle has exactly 1 / 2 quarter turns over the optimal
///                                      finishes, and every corner route of an optimal reading with its min HTR
///   R <scramble> <finish> <k> <0|1>    the reading of that finish split at k (1 = inverse first)
///   D <scramble> <P> <U> <rest>        the reduction P on normal, U on inverse, then rest
fn cmd_page(t: &Table, l: &Labels) {
    let qd = qt_dist_table(l);
    let key = |g: &St| l.orbit[rank8(&g.c)] as usize * 256 + emask(&g.e);
    let lines: Vec<String> = std::io::stdin().lock().lines().map(|x| x.unwrap()).collect();
    let out: Vec<String> = lines.par_iter().map(|line| {
        let v: Vec<&str> = line.split('\t').collect();
        let x = ID.apply(&parse(v[1]));
        let xi = x.inv();
        match v[0] {
            "S" => {
                let d = t.d(&x) as usize;
                let opt = finishes(t, &x, d);
                let mut map: HashMap<String, u8> = HashMap::new();
                let mut red = [usize::MAX; 2];
                for f in &opt {
                    for k in 0..=f.len() { for invf in [false, true] {
                        let r = reading(l, &x, &xi, f, k, invf);
                        let e = map.entry(r.route).or_insert(u8::MAX);
                        *e = (*e).min(r.htr);
                    }}
                    let secs = corner_path(l, &x, f).1;
                    let n = secs.len() - 1;
                    for q in 1..=2usize {
                        if n < q { continue; }
                        for i in 0..=(n - q) {
                            let w: usize = q + secs[i..=i + q].iter().sum::<usize>();
                            red[q - 1] = red[q - 1].min(f.len() - w);
                        }
                    }
                }
                let mut rv: Vec<String> = map.iter().map(|(k, h)| format!("{}={}", k, h)).collect();
                rv.sort();
                format!("S\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}", l.name(&x), l.name(&xi), l.lin(&x), l.lin(&xi), l.niss(&x), d, opt.len(),
                    red[0] as i64, red[1] as i64, rv.join(";"))
            }
            "R" => {
                let f = parse(v[2]);
                let r = reading(l, &x, &xi, &f, v[3].parse().unwrap(), v[4] == "1");
                format!("R\t{}\t{}\t{}\t{}\t{}", r.route, r.htr, (x.apply(&f) == ID) as u8, f.len(), t.d(&x))
            }
            "D" => {
                let (p, u, rest) = (parse(v[2]), parse(v[3]), parse(v[4]));
                let g = ID.apply(&inv_seq(&u)).then(&x.apply(&p));
                let ends_ok = |w: &Vec<usize>| w.is_empty() || is_qt(*w.last().unwrap());
                format!("D\t{}\t{}\t{}\t{}\t{}\t{}\t{}", l.name(&g), qd[key(&g)], (g.apply(&rest) == ID) as u8,
                    rest.iter().filter(|&&m| is_qt(m)).count(), p.len() + u.len() + rest.len(), t.d(&x),
                    (ends_ok(&p) && ends_ok(&u)) as u8)
            }
            _ => "?".to_string(),
        }
    }).collect();
    for o in out { println!("{}", o); }
}


/// Bounding as the method states it, by brute force over every pair (P on normal, U on inverse), each empty or
/// ending in a quarter turn, |P| + |U| <= rmax: the shortest reduction to a state q quarter turns from HTR
/// (variant "at most q" and variant "exactly q") whose optimal finish completes an optimal finish of the DR
/// (or one within +1).  Compared with htrtools' bound4.tsv (targets opt and p1; 99 = none).
fn cmd_b4(t: &Table, l: &Labels, states: &str, b4: &str, cell: &str, from: usize, n: usize, rmax: usize) {
    let rows = read_states(states);
    let seqs = red_seqs(rmax);
    let seqs_inv: Vec<Vec<St>> = seqs.iter().map(|v| v.iter().map(|g| g.inv()).collect()).collect();
    let qd = qt_dist_table(l);
    let key = |g: &St| l.orbit[rank8(&g.c)] as usize * 256 + emask(&g.e);
    let theirs: HashMap<usize, HashMap<String, (usize, usize)>> = std::fs::read_to_string(b4).unwrap().lines().skip(1)
        .map(|l| l.split('\t').map(|s| s.to_string()).collect::<Vec<_>>())
        .filter(|v| v[0] == cell)
        .map(|v| (v[1].parse().unwrap(), v[3].split(';').map(|x| { let p: Vec<&str> = x.split(':').collect(); (p[0].to_string(), (p[1].parse().unwrap(), p[2].parse().unwrap())) }).collect()))
        .collect();
    let idx: Vec<usize> = (from..from + n).collect();
    let res: Vec<(bool, bool, String)> = idx.par_iter().map(|&i| {
        let x = st_of(&rows[i]);
        let d = t.d(&x) as usize;
        // best[variant][target][q]
        let mut best = [[[99usize; 2]; 2]; 2];
        for r in 0..=rmax {
            for a in 0..=r {
                let b = r - a;
                for ga in &seqs[a] {
                    let xa = x.then(ga);
                    for gbi in &seqs_inv[b] {
                        let g = gbi.then(&xa);
                        let q = qd[key(&g)] as usize;
                        if q > 2 { continue; }
                        // which (variant, q) cells could still improve at this r?
                        let mut need = false;
                        for qq in 1..=2usize {
                            if q <= qq { for tg in 0..2 { if best[0][tg][qq - 1] == 99 { need = true; } } }
                            if q == qq { for tg in 0..2 { if best[1][tg][qq - 1] == 99 { need = true; } } }
                        }
                        if !need { continue; }
                        let tot = r + t.d(&g) as usize;
                        for tg in 0..2 {
                            if tot > d + tg { continue; }
                            for qq in 1..=2usize {
                                if q <= qq && best[0][tg][qq - 1] == 99 { best[0][tg][qq - 1] = r; }
                                if q == qq && best[1][tg][qq - 1] == 99 { best[1][tg][qq - 1] = r; }
                            }
                        }
                    }
                }
            }
        }
        let th = &theirs[&i];
        let cap = |v: usize| if v > rmax { 99 } else { v };
        let same_a = (0..2).all(|tg| { let tt = th[["opt", "p1"][tg]]; cap(tt.0) == best[0][tg][0] && cap(tt.1) == best[0][tg][1] });
        let same_b = (0..2).all(|tg| { let tt = th[["opt", "p1"][tg]]; cap(tt.0) == best[1][tg][0] && cap(tt.1) == best[1][tg][1] });
        (same_a, same_b, format!("{} idx {} d {}: at-most {:?} exactly {:?} theirs opt {:?} p1 {:?}", cell, i, d, best[0], best[1], th["opt"], th["p1"]))
    }).collect();
    let na = res.iter().filter(|r| r.0).count();
    let nb = res.iter().filter(|r| r.1).count();
    for r in res.iter().filter(|r| !r.0).take(5) { println!("  differs (at most q): {}", r.2); }
    for r in res.iter().filter(|r| !r.1).take(2) { println!("  differs (exactly q): {}", r.2); }
    println!("{}: {} states, r <= {}; equal to bound4 with 'at most q quarter turns from HTR': {}; with 'exactly q': {}", cell, res.len(), rmax, na, nb);
}


/// The late-switch data (C13, errata d) and the (corner path -> shortest 1q / 2q window reduction) data that the
/// FakeMMAP tests of section 9 use, recomputed and compared with htrtools' bound2.tsv, state by state:
/// the shortest HTR over every reading of every optimal finish, whether a linear reading has it, the fewest
/// first-side moves of a NISS reading that has it; and for the optimal and the +1 finishes, per corner path
/// (all quarter turns, read on normal), the shortest reduction that leaves a window with exactly 1 / 2 quarter turns.
fn cmd_b2(t: &Table, l: &Labels, states: &str, b2: &str, cell: &str, from: usize, n: usize) {
    const SUB: [&str; 14] = ["0c0", "4a1", "4a2", "4b2", "0c3", "2c3", "4a3", "4b3", "0c4", "2c4", "4a4", "4b4", "2c5", "4b5"];
    let rows = read_states(states);
    let f = std::io::BufReader::new(std::fs::File::open(b2).unwrap());
    let mut theirs: HashMap<usize, Vec<String>> = HashMap::new();
    let mut hdr: Vec<String> = vec![];
    for (k, line) in f.lines().enumerate() {
        let line = line.unwrap();
        if k == 0 { hdr = line.split('\t').map(|s| s.to_string()).collect(); continue; }
        if !line.starts_with(cell) { if !theirs.is_empty() { break; } else { continue; } }
        let v: Vec<String> = line.split('\t').map(|s| s.to_string()).collect();
        let i: usize = v[1].parse().unwrap();
        if i >= from && i < from + n { theirs.insert(i, v); }
    }
    let col = |n: &str| hdr.iter().position(|h| h == n).unwrap();
    let (cb, cl, cm, cc) = (col("best_any"), col("linear_at_best"), col("minfirst_at_best"), col("cells"));
    let (clb, cmb) = (col("linear_at_b2"), col("minfirst_at_b2"));
    let idx: Vec<usize> = (from..from + n).collect();
    let res: Vec<(usize, Vec<String>, usize)> = idx.par_iter().map(|&i| {
        let x = st_of(&rows[i]);
        let xi = x.inv();
        let d = t.d(&x) as usize;
        let mut bad = vec![];
        let mut best = (99u8, false, 99usize);
        let niss = l.niss(&x);
        let mut b2x = (false, 99usize);      // among readings with an HTR within 2 of the shortest NISS HTR
        let mut mine: HashMap<(usize, String), (usize, usize)> = HashMap::new();
        for off in 0..2usize {
            for f in finishes(t, &x, d + off) {
                if off == 0 {
                    for k in 0..=f.len() { for invf in [false, true] {
                        let r = reading(l, &x, &xi, &f, k, invf);
                        if r.htr < best.0 { best = (r.htr, false, 99); }
                        if r.htr == best.0 {
                            match r.sw_after { None => best.1 = true, Some(m) => best.2 = best.2.min(m) }
                        }
                        if r.htr <= niss + 2 {
                            match r.sw_after { None => b2x.0 = true, Some(m) => b2x.1 = b2x.1.min(m) }
                        }
                    }}
                }
                let mut g = x;
                let mut path = vec![l.name(&g).split(' ').next().unwrap().to_string()];
                let mut secs = vec![0usize];
                for &m in &f {
                    g = g.mv(m);
                    if is_qt(m) { path.push(l.name(&g).split(' ').next().unwrap().to_string()); secs.push(0); } else { *secs.last_mut().unwrap() += 1; }
                }
                let nq = secs.len() - 1;
                let mut r = [99usize; 2];
                for q in 1..=2usize {
                    if nq < q { continue; }
                    for a in 0..=(nq - q) { r[q - 1] = r[q - 1].min(f.len() - q - secs[a..=a + q].iter().sum::<usize>()); }
                }
                let e = mine.entry((off, path.join(" > "))).or_insert((99, 99));
                e.0 = e.0.min(r[0]); e.1 = e.1.min(r[1]);
            }
        }
        let th = &theirs[&i];
        if th[cb].parse::<u8>().unwrap() != best.0 { bad.push(format!("best_any {} vs {}", best.0, th[cb])); }
        if (th[cl] == "1") != best.1 { bad.push(format!("linear_at_best {} vs {}", best.1, th[cl])); }
        if th[cm].parse::<usize>().unwrap() != best.2 { bad.push(format!("minfirst_at_best {} vs {}", best.2, th[cm])); }
        if (th[clb] == "1") != b2x.0 { bad.push(format!("linear_at_b2 {} vs {}", b2x.0, th[clb])); }
        if th[cmb].parse::<usize>().unwrap() != b2x.1 { bad.push(format!("minfirst_at_b2 {} vs {}", b2x.1, th[cmb])); }
        let mut tc: HashMap<(usize, String), (usize, usize)> = HashMap::new();
        for c in th[cc].split(';') {
            let p: Vec<&str> = c.split(':').collect();
            let off: usize = p[0].parse().unwrap();
            if off > 1 { continue; }
            let path = p[1].split('-').map(|x| SUB[x.parse::<usize>().unwrap()]).collect::<Vec<_>>().join(" > ");
            let (r1, r2): (usize, usize) = (p[2].parse().unwrap(), p[3].parse().unwrap());
            // the sections printed for the 1q reduction must be a finish of that length with that window
            if r1 != 99 {
                let sc: Vec<usize> = p[4].split(',').map(|x| x.parse().unwrap()).collect();
                let len = sc.iter().sum::<usize>() + sc.len() - 1;
                let w = (0..sc.len() - 1).map(|a| len - 1 - sc[a] - sc[a + 1]).min().unwrap();
                if len != d + off || w != r1 { bad.push(format!("sections {:?} do not give length {} and reduction {}", sc, d + off, r1)); }
            }
            tc.insert((off, path), (r1, r2));
        }
        if tc != mine {
            for (k, v) in &mine { if tc.get(k) != Some(v) { bad.push(format!("path {:?}: mine {:?} theirs {:?}", k, v, tc.get(k))); } }
            for (k, v) in &tc { if !mine.contains_key(k) { bad.push(format!("path {:?} only in bound2: {:?}", k, v)); } }
        }
        (i, bad, mine.len())
    }).collect();
    let nbad = res.iter().filter(|r| !r.1.is_empty()).count();
    for (i, b, _) in res.iter().filter(|r| !r.1.is_empty()).take(6) {
        println!("state {}: {} problems", i, b.len());
        for x in b.iter().take(6) { println!("   {}", x); }
    }
    println!("{}: {} states, {} (state, length, corner path) cells compared, {} states with differences", cell, res.len(), res.iter().map(|r| r.2).sum::<usize>(), nbad);
}


/// The shortest NISS HTR of EVERY DR state, by breadth-first search over the whole group.
/// NISS length D(X) = min |A| + |B| with (B^-1, X, A) in HTR, so D = 0 on HTR and otherwise 1 + the least D over
/// the twenty neighbours X m (a move on normal) and m X (a move on inverse).  D is constant on the classes of the
/// 16 symmetries (they carry moves to moves and HTR to HTR), so one byte per entry of the first study's reduced
/// index is enough, and a class of n corner arrangements counts its entries n times.
fn cmd_nissall(mut t: Table, l: &Labels, out: &str) {
    use std::sync::atomic::{AtomicU8, Ordering};
    t.t = Vec::new();
    let n = 2768usize * 40320 * 12;
    let tab: Vec<AtomicU8> = (0..n).into_par_iter().map(|_| AtomicU8::new(255)).collect();
    let mut csize = vec![0u64; 2768];
    let mut rep = vec![[0u8; 8]; 2768];
    let mut seen = vec![false; 2768];
    for r in 0..40320 { let k = t.cls[r] as usize; csize[k] += 1; if !seen[k] { seen[k] = true; rep[k] = unrank_n::<8>(r); } }
    let mut perms4 = vec![];
    for a in 0..4u8 { for b in 0..4u8 { for c in 0..4u8 { for d in 0..4u8 {
        let v = [a, b, c, d];
        let mut sn = [false; 4];
        if v.iter().all(|&x| { let f = !sn[x as usize]; sn[x as usize] = true; f }) { perms4.push(v); }
    }}}}
    let stab: Vec<[u8; 4]> = perms4.iter().filter(|v| parity(&v[..]) == 0).chain(perms4.iter().filter(|v| parity(&v[..]) == 1)).cloned().collect();
    let eperm: Vec<[u8; 8]> = (0..40320).map(|e| unrank_n::<8>(e)).collect();
    let epar: Vec<usize> = eperm.iter().map(|e| parity(&e[..])).collect();
    let idx = |g: &St| -> usize {
        let rc = rank8(&g.c);
        let k = t.cls[rc] as usize;
        let s = t.symto[rc] as usize;
        let e = conj8(&t.syms[s].e, &t.sinv[s].e, &g.e);
        let sl = conj4(&t.syms[s].s, &t.sinv[s].s, &g.s);
        let code = ((sl[0] as usize * 4 + sl[1] as usize) * 4 + sl[2] as usize) * 4 + sl[3] as usize;
        (k * 40320 + rank8(&e)) * 12 + t.s12[code] as usize
    };
    let state = |k: usize, e: usize, s: usize| -> St {
        let c = rep[k];
        St { c, e: eperm[e], s: stab[((parity(&c) + epar[e]) % 2) * 12 + s] }
    };
    // level 0: HTR
    (0..2768usize).into_par_iter().for_each(|k| {
        if !l.hc[rank8(&rep[k])] { return; }
        for e in 0..40320 { if emask(&eperm[e]) == HTR_MASK { for s in 0..12 {
            let g = state(k, e, s);
            debug_assert!(l.in_htr(&g));
            tab[(k * 40320 + e) * 12 + s].store(0, Ordering::Relaxed);
        }}}
    });
    let mvst: Vec<St> = (0..10).map(|m| ID.mv(m)).collect();
    // A corner representative can be fixed by several symmetries; a state with those corners then has several
    // entries (its images under them), and a neighbour found through one image must mark them all.
    let stabs: Vec<Vec<usize>> = (0..2768usize).map(|k| (0..16).filter(|&q| conj8(&t.syms[q].c, &t.sinv[q].c, &rep[k]) == rep[k]).collect()).collect();
    eprintln!("corner classes with more than the identity fixing the representative: {}", stabs.iter().filter(|v| v.len() > 1).count());
    let mark = |g: &St, val: u8| {
        let rc = rank8(&g.c);
        let k = t.cls[rc] as usize;
        let q = t.symto[rc] as usize;
        let e = conj8(&t.syms[q].e, &t.sinv[q].e, &g.e);
        let sl = conj4(&t.syms[q].s, &t.sinv[q].s, &g.s);
        for &r in &stabs[k] {
            let e2 = conj8(&t.syms[r].e, &t.sinv[r].e, &e);
            let s2 = conj4(&t.syms[r].s, &t.sinv[r].s, &sl);
            let code = ((s2[0] as usize * 4 + s2[1] as usize) * 4 + s2[2] as usize) * 4 + s2[3] as usize;
            let j = (k * 40320 + rank8(&e2)) * 12 + t.s12[code] as usize;
            if tab[j].load(Ordering::Relaxed) == 255 { tab[j].store(val, Ordering::Relaxed); }
        }
    };
    let mut hist: Vec<u64> = vec![];
    let mut lvl = 0u8;
    loop {
        let cnt: u64 = (0..2768usize).into_par_iter().map(|k| {
            let mut c = 0u64;
            for e in 0..40320 { for s in 0..12 {
                if tab[(k * 40320 + e) * 12 + s].load(Ordering::Relaxed) != lvl { continue; }
                c += 1;
                let g = state(k, e, s);
                for m in 0..10 {
                    mark(&g.mv(m), lvl + 1);
                    mark(&mvst[m].then(&g), lvl + 1);
                }
            }}
            c * csize[k]
        }).sum();
        if cnt == 0 { break; }
        eprintln!("NISS HTR {}: {} states", lvl, cnt);
        hist.push(cnt);
        lvl += 1;
    }
    let unreached: u64 = (0..2768usize).into_par_iter().map(|k| {
        (0..40320 * 12).filter(|i| tab[k * 40320 * 12 + i].load(Ordering::Relaxed) == 255).count() as u64 * csize[k]
    }).sum();
    let total: u64 = hist.iter().sum();
    println!("shortest NISS HTR over all DR states: total {} (19,508,428,800 expected), not reached {}", total, unreached);
    for (d, c) in hist.iter().enumerate() { println!("{}\t{}\t{:.6}%", d, c, 100.0 * *c as f64 / total as f64); }
    // by label: the whole distribution, and the shortest linear HTR (better side) minus the shortest NISS HTR
    let agg: Vec<HashMap<(u8, u8, u8), u64>> = (0..2768usize).into_par_iter().map(|k| {
        let mut m: HashMap<(u8, u8, u8), u64> = HashMap::new();
        for e in 0..40320 { for s in 0..12 {
            let v = tab[(k * 40320 + e) * 12 + s].load(Ordering::Relaxed);
            let g = state(k, e, s);
            let lin = l.lin(&g).min(l.lin(&g.inv()));
            *m.entry((l.label(&g), v, (lin - v).min(3))).or_insert(0) += csize[k];
        }}
        m
    }).collect();
    let mut m: HashMap<(String, u8, u8), u64> = HashMap::new();
    for a in agg { for ((lb, v, df), c) in a {
        let nm = &l.names[lb as usize];
        let (sub, e) = nm.split_once(' ').unwrap();
        let sub = match sub { "4a3" | "4b3" => "4c3", "4a4" | "4b4" => "4c4", x => x };
        *m.entry((format!("{} {}", sub, e), v, df)).or_insert(0) += c;
    }}
    let mut diff = [0u64; 4];
    for ((_, _, df), c) in &m { diff[*df as usize] += c; }
    println!("shortest linear HTR (better side) minus shortest NISS HTR: 0: {:.4}%  1: {:.4}%  2: {:.4}%  3+: {:.4}%",
        100.0 * diff[0] as f64 / total as f64, 100.0 * diff[1] as f64 / total as f64, 100.0 * diff[2] as f64 / total as f64, 100.0 * diff[3] as f64 / total as f64);
    println!("subset\tniss_htr\tlinear_minus_niss\tstates");
    let mut rows: Vec<_> = m.into_iter().collect();
    rows.sort();
    for ((sub, v, df), c) in rows { println!("{}\t{}\t{}\t{}", sub, v, df, c); }
    // self-check against the per-state search on random states
    let mut seed = 987654321u64;
    let mut rnd = || { seed ^= seed << 13; seed ^= seed >> 7; seed ^= seed << 17; seed };
    let mut bad = 0;
    for _ in 0..20000 {
        let mut g = ID;
        for _ in 0..40 { g = g.mv((rnd() % 10) as usize); }
        if tab[idx(&g)].load(Ordering::Relaxed) != l.niss(&g) { bad += 1; }
    }
    println!("20000 random states against the per-state NISS search: {} differences", bad);
    if out != "-" {
        let bytes: Vec<u8> = tab.iter().map(|a| a.load(Ordering::Relaxed)).collect();
        std::fs::write(out, bytes).unwrap();
    }
}


/// The optimal leave-slice finish (corners and U/D-layer edges home, E slice ignored) of every DR state, by a
/// plain breadth-first search over the 40320 x 40320 (corner, edge) arrangements, and its distribution per
/// subset x edges (each arrangement pair stands for 12 states), compared with out/checks/lsdist48.tsv.
fn cmd_lsall(l: &Labels, lsdist: &str) {
    use std::sync::atomic::{AtomicU8, Ordering};
    let perm: Vec<[u8; 8]> = (0..40320).map(|r| unrank_n::<8>(r)).collect();
    let cm: Vec<[u32; 10]> = perm.iter().map(|c| { let mut a = [0u32; 10]; for m in 0..10 { a[m] = rank8(&cmove(c, m)) as u32; } a }).collect();
    let em: Vec<[u32; 10]> = perm.iter().map(|e| { let mut a = [0u32; 10]; for m in 0..10 { let mut r = *e; for p in 0..8 { r[p] = e[SRC_E[m][p] as usize]; } a[m] = rank8(&r) as u32; } a }).collect();
    let n = 40320usize * 40320;
    let tab: Vec<AtomicU8> = (0..n).into_par_iter().map(|_| AtomicU8::new(255)).collect();
    tab[0].store(0, Ordering::Relaxed);
    let mut lvl = 0u8;
    loop {
        let cnt: u64 = (0..40320usize).into_par_iter().map(|c| {
            let mut k = 0u64;
            for e in 0..40320usize {
                if tab[c * 40320 + e].load(Ordering::Relaxed) != lvl { continue; }
                k += 1;
                for m in 0..10 {
                    let j = cm[c][m] as usize * 40320 + em[e][m] as usize;
                    if tab[j].load(Ordering::Relaxed) == 255 { tab[j].store(lvl + 1, Ordering::Relaxed); }
                }
            }
            k
        }).sum();
        if cnt == 0 { break; }
        eprintln!("leave slice {}: {} arrangement pairs", lvl, cnt);
        lvl += 1;
    }
    let masks: Vec<usize> = perm.iter().map(|e| emask(e)).collect();
    let agg: Vec<HashMap<(u8, u8), u64>> = (0..40320usize).into_par_iter().map(|c| {
        let mut m: HashMap<(u8, u8), u64> = HashMap::new();
        for e in 0..40320usize { *m.entry((l.lab[c * 256 + masks[e]], tab[c * 40320 + e].load(Ordering::Relaxed))).or_insert(0) += 12; }
        m
    }).collect();
    let mut mine: HashMap<(String, u8), u64> = HashMap::new();
    for a in agg { for ((lb, d), v) in a {
        let nm = &l.names[lb as usize];
        let (sub, e) = nm.split_once(' ').unwrap();
        let sub = match sub { "4a3" | "4b3" => "4c3", "4a4" | "4b4" => "4c4", x => x };
        *mine.entry((format!("{} {}", sub, e), d)).or_insert(0) += v;
    }}
    let mut theirs: HashMap<(String, u8), u64> = HashMap::new();
    for line in std::fs::read_to_string(lsdist).unwrap().lines() {
        let v: Vec<&str> = line.split('\t').collect();
        if v.len() == 3 { if let (Ok(d), Ok(c)) = (v[1].parse::<u8>(), v[2].parse::<u64>()) { if c > 0 { theirs.insert((v[0].to_string(), d), c); } } }
    }
    println!("leave-slice distribution: {} (subset x edges, length) cells here, {} in lsdist48.tsv, identical: {}", mine.len(), theirs.len(), mine == theirs);
    println!("states: {}", mine.values().sum::<u64>());
    let mut mx: HashMap<String, u8> = HashMap::new();
    for ((s, d), _) in &mine { let e = mx.entry(s.clone()).or_insert(0); *e = (*e).max(*d); }
    let mut v: Vec<_> = mx.into_iter().collect(); v.sort();
    println!("longest leave-slice optimum per subset x edges: {:?}", v);
    println!("4a1 4e: {} states", mine.iter().filter(|(k, _)| k.0 == "4a1 4e").map(|(_, v)| *v).sum::<u64>());
}

fn cmd_s18(t: &Table) {
    // every entry with value 18: each of R2 L2 F2 B2 after it gives 17
    let tt = &t.t;
    let idx: Vec<usize> = tt.par_iter().enumerate().filter(|(_, &v)| v == 18).map(|(i, _)| i).collect();
    println!("entries with 18: {}", idx.len());
    // rebuild the state of each entry: corners = representative of the class
    let mut rep = vec![[0u8; 8]; 2768];
    let mut seen = vec![false; 2768];
    for r in 0..40320 { let k = t.cls[r] as usize; if !seen[k] { seen[k] = true; rep[k] = unrank_n::<8>(r); } }
    let mut perms4 = vec![];
    for a in 0..4u8 { for b in 0..4u8 { for c in 0..4u8 { for d in 0..4u8 {
        let v = [a, b, c, d];
        let mut sn = [false; 4];
        if v.iter().all(|&x| { let f = !sn[x as usize]; sn[x as usize] = true; f }) { perms4.push(v); }
    }}}}
    let tab: Vec<[u8; 4]> = perms4.iter().filter(|v| parity(&v[..]) == 0).chain(perms4.iter().filter(|v| parity(&v[..]) == 1)).cloned().collect();
    let mut bad = 0;
    let mut otherwise = [0usize; 20];
    for &i in &idx {
        let s = i % 12; let e = (i / 12) % 40320; let k = i / 12 / 40320;
        let c = rep[k]; let ee: [u8; 8] = unrank_n::<8>(e);
        let p = (parity(&c) + parity(&ee)) % 2;
        let g = St { c, e: ee, s: tab[p * 12 + s] };
        assert_eq!(t.d(&g), 18);
        for m in 6..10 { if t.d(&g.mv(m)) != 17 { bad += 1; } }
        for m in 0..6 { otherwise[t.d(&g.mv(m)) as usize] += 1; }
    }
    println!("side half turns not giving 17: {}; U/D moves give {:?}", bad, &otherwise[15..20]);
}

fn main() {
    let a: Vec<String> = std::env::args().collect();
    if a[1] == "lsall" { cmd_lsall(&Labels::new(), &a[2]); return; }
    let t = Table::load(&table_path());
    let l = Labels::new();
    match a[1].as_str() {
        "check" => cmd_check(&t, &l),
        "ex" => for m in &a[2..] { cmd_ex(&t, &l, m); println!(); },
        "red" => cmd_red(&t, &l, &a[2], a[3].parse().unwrap(), a[4].parse().unwrap()),
        "cmp" => cmd_cmp(&t, &l, &a[2], &a[3], &a[4], a[5].parse().unwrap(), a[6].parse().unwrap()),
        "dump" => cmd_dump(&t, &l, &a[2], a[3].parse().unwrap(), a[4].parse().unwrap(), &a[5]),
        "s18" => cmd_s18(&t),
        "qtcos" => cmd_qtcos(&l),
        "nissall" => { cmd_nissall(t, &l, &a[2]); return; }
        "b2" => cmd_b2(&t, &l, &a[2], &a[3], &a[4], a[5].parse().unwrap(), a[6].parse().unwrap()),
        "b4" => cmd_b4(&t, &l, &a[2], &a[3], &a[4], a[5].parse().unwrap(), a[6].parse().unwrap(), a[7].parse().unwrap()),
        "page" => cmd_page(&t, &l),
        "lastmove" => cmd_lastmove(&t),
        "rc" => cmd_rc(&t, &l, &a[2], &a[3], &a[4], &a[5], a[6].parse().unwrap()),
        _ => eprintln!("unknown command"),
    }
    std::io::stdout().flush().unwrap();
}

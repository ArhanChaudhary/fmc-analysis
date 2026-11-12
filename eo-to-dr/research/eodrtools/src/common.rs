//! Shared pieces: the coset move tables of is-dr-xs-worth-it (out/tables/moves.bin), the distance tables (the full
//! 4-bit packing of attempt.rs, and the small "EO solved" slices), random states, move text, views.
//!
//! Axes are numbered as in cubie.rs: 0 R/L, 1 U/D, 2 F/B.  Faces U D R L F B are 0..5, a move is 3 * face + (quarter
//! turns - 1).  A *view* of a state is `Model::conj(state, r)`: the cube turned by rotation r.  The tables are about a
//! DR on U/D and an EO on F/B, so a DR on axis X is looked up in a view that carries X to U/D, an EO on axis Y in a
//! view that carries Y to F/B, and "EO on Y, then DR on X" in a view that does both.

use crate::cubie::{Cubie, Model, SOLVED};
use std::fs::File;
use std::io::{Read, Seek, SeekFrom, Write};

pub const NCO: usize = 2187;
pub const NEO: usize = 2048;
pub const NSL: usize = 495;
pub const N: usize = NCO * NEO * NSL;
pub const N0: usize = NCO * NSL; // cosets with F/B EO solved

pub const XS: &str = "/data/fmc/is-dr-xs-worth-it/research/out";
pub const NONE: usize = 18; // "no previous move"
pub const FACE_AXIS: [usize; 6] = [1, 1, 0, 0, 2, 2];
pub const AXIS_NAME: [&str; 3] = ["RL", "UD", "FB"];

pub struct Tables {
    pub co: Vec<[u16; 18]>,
    pub eo: Vec<[u16; 18]>,
    pub sl: Vec<[u16; 18]>,
}

pub fn load_tables() -> Tables {
    let mut buf = Vec::new();
    File::open(format!("{XS}/tables/moves.bin")).expect("moves.bin").read_to_end(&mut buf).unwrap();
    assert_eq!(buf.len(), (NCO + NEO + NSL) * 36);
    let row = |i: usize| -> [u16; 18] {
        let mut r = [0u16; 18];
        for m in 0..18 {
            r[m] = u16::from_le_bytes([buf[i * 36 + 2 * m], buf[i * 36 + 2 * m + 1]]);
        }
        r
    };
    Tables {
        co: (0..NCO).map(row).collect(),
        eo: (NCO..NCO + NEO).map(row).collect(),
        sl: (NCO + NEO..NCO + NEO + NSL).map(row).collect(),
    }
}

/// splitmix64 (as in xstools)
pub struct Rng(pub u64);
impl Rng {
    pub fn new(seed: u64, i: u64) -> Rng {
        Rng(seed.wrapping_mul(0x9E3779B97F4A7C15).wrapping_add(i))
    }
    pub fn next(&mut self) -> u64 {
        self.0 = self.0.wrapping_add(0x9E3779B97F4A7C15);
        let mut z = self.0;
        z = (z ^ (z >> 30)).wrapping_mul(0xBF58476D1CE4E5B9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94D049BB133111EB);
        z ^ (z >> 31)
    }
    pub fn below(&mut self, n: usize) -> usize {
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

pub fn parity(p: &[u8]) -> u8 {
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

/// A uniformly random cube state; with `eo_solved`, a uniformly random state with F/B EO solved.
pub fn random_cube(rng: &mut Rng, eo_solved: bool) -> Cubie {
    loop {
        let (cp, ep): ([u8; 8], [u8; 12]) = (rng.perm(), rng.perm());
        if parity(&cp) != parity(&ep) {
            continue;
        }
        let mut x = Cubie { cp, ct: [0; 8], ep, ef: [0; 12] };
        let mut s = 0;
        for i in 0..7 {
            x.ct[i] = rng.below(3) as u8;
            s += x.ct[i];
        }
        x.ct[7] = (3 - s % 3) % 3;
        if !eo_solved {
            let mut f = 0;
            for i in 0..11 {
                x.ef[i] = rng.below(2) as u8;
                f ^= x.ef[i];
            }
            x.ef[11] = f;
        }
        return x;
    }
}

pub const NAMES: [&str; 18] = ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'"];
pub fn parse(s: &str) -> Vec<usize> {
    s.split_whitespace().map(|t| NAMES.iter().position(|&n| n == t).unwrap_or_else(|| panic!("bad move {t}"))).collect()
}
pub fn text(seq: &[usize]) -> String {
    seq.iter().map(|&m| NAMES[m]).collect::<Vec<_>>().join(" ")
}
pub fn inv_move(mv: usize) -> usize {
    3 * (mv / 3) + 2 - mv % 3
}
pub fn invert(seq: &[usize]) -> Vec<usize> {
    seq.iter().rev().map(|&mv| inv_move(mv)).collect()
}
#[inline]
pub fn canon_ok(last: usize, mv: usize) -> bool {
    if last == NONE {
        return true;
    }
    let (fl, fm) = (last / 3, mv / 3);
    !(fl == fm || (fl / 2 == fm / 2 && fl > fm))
}
/// A quarter turn of a face of axis y (the turns that change edge orientation for y).
#[inline]
pub fn y_quarter(mv: usize, y: usize) -> bool {
    mv % 3 != 1 && FACE_AXIS[mv / 3] == y
}

#[inline]
pub fn idx(co: usize, eo: usize, sl: usize) -> usize {
    (co * NEO + eo) * NSL + sl
}

/// A full distance table held at 4 bits per coset (as attempt.rs does): 15 = unreachable.
pub struct Full4 {
    pub nib: Vec<u8>,
}
impl Full4 {
    pub fn open(path: &str) -> Full4 {
        let mut f = File::open(path).unwrap_or_else(|_| panic!("missing {path}"));
        let mut nib = vec![0u8; N / 2];
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
        assert_eq!(pos, N);
        Full4 { nib }
    }
    #[inline]
    pub fn at(&self, c: (usize, usize, usize)) -> u8 {
        let i = idx(c.0, c.1, c.2);
        let v = (self.nib[i >> 1] >> ((i & 1) * 4)) & 15;
        if v == 15 { 255 } else { v }
    }
}

/// The part of a distance table with F/B EO solved (eo = 0): 1,082,565 bytes, index co * 495 + sl.
pub struct Eo0 {
    pub d: Vec<u8>,
}
impl Eo0 {
    pub fn load(path: &str) -> Eo0 {
        let d = std::fs::read(path).unwrap_or_else(|_| panic!("missing {path} (run eodrtools extract)"));
        assert_eq!(d.len(), N0);
        Eo0 { d }
    }
    #[inline]
    pub fn at(&self, co: usize, sl: usize) -> u8 {
        self.d[co * NSL + sl]
    }
}

/// eodrtools extract <src.u8> <dst.u8>: copy the eo = 0 part of a 2.2 GB table (2187 reads of 495 bytes).
pub fn extract_eo0(src: &str, dst: &str) {
    let mut f = File::open(src).expect("table");
    let mut out = vec![0u8; N0];
    for co in 0..NCO {
        f.seek(SeekFrom::Start(idx(co, 0, 0) as u64)).unwrap();
        f.read_exact(&mut out[co * NSL..(co + 1) * NSL]).unwrap();
    }
    File::create(dst).unwrap().write_all(&out).unwrap();
    let mut h = [0u64; 256];
    for &v in &out {
        h[v as usize] += 1;
    }
    println!("{dst}: histogram of the eo = 0 part");
    for (d, c) in h.iter().enumerate() {
        if *c > 0 {
            println!("{d}\t{c}");
        }
    }
}

/// The model plus the rotations and the per-view move maps.
pub struct Ctx {
    pub m: Model,
    pub t: Tables,
    pub rot_dr: [usize; 3],        // carries axis X to U/D
    pub rot_eo: [usize; 3],        // carries axis Y to F/B
    pub rot_pair: [[usize; 3]; 3], // [X][Y], X != Y: carries X to U/D and Y to F/B
    pub vmove: Vec<[usize; 18]>,   // [rotation][own move] = the same turn in the view's labels
    pub mvc: Vec<Cubie>,           // the 18 turns as states
    pub eodist: Vec<u8>,           // fewest turns to F/B EO, per eo coordinate
}
impl Ctx {
    pub fn new() -> Ctx {
        let m = Model::load(&format!("{XS}/tables"));
        let t = load_tables();
        let rot_dr = [m.rot_for(0, 1, None), m.rot_for(1, 1, None), m.rot_for(2, 1, None)];
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
        for r in 0..24 {
            let mut v = [0usize; 18];
            for mv in 0..18 {
                v[m.unview(r, mv)] = mv;
            }
            vmove.push(v);
        }
        let mvc: Vec<Cubie> = (0..18).map(|mv| m.turn(&SOLVED, mv)).collect();
        let mut eodist = vec![255u8; NEO];
        eodist[0] = 0;
        let mut d = 0;
        loop {
            let mut any = false;
            for e in 0..NEO {
                if eodist[e] == d {
                    for mv in 0..18 {
                        let f = t.eo[e][mv] as usize;
                        if eodist[f] == 255 {
                            eodist[f] = d + 1;
                            any = true;
                        }
                    }
                }
            }
            if !any {
                break;
            }
            d += 1;
        }
        Ctx { m, t, rot_dr, rot_eo, rot_pair, vmove, mvc, eodist }
    }
    #[inline]
    pub fn view(&self, s: &Cubie, r: usize) -> Cubie {
        self.m.conj(s, r)
    }
    #[inline]
    pub fn coords(&self, s: &Cubie) -> (usize, usize, usize) {
        self.m.coords(s)
    }
    #[inline]
    pub fn eo(s: &Cubie) -> usize {
        let mut e = 0usize;
        for i in 0..11 {
            e |= (s.ef[i] as usize) << i;
        }
        e
    }
    /// eo coordinate of p.then(s) without composing the corners.
    #[inline]
    pub fn eo_then(p: &Cubie, s: &Cubie) -> usize {
        let mut e = 0usize;
        for i in 0..11 {
            e |= ((p.ef[s.ep[i] as usize] ^ s.ef[i]) as usize) << i;
        }
        e
    }
    #[inline]
    pub fn mv(&self, c: (usize, usize, usize), mv: usize) -> (usize, usize, usize) {
        (self.t.co[c.0][mv] as usize, self.t.eo[c.1][mv] as usize, self.t.sl[c.2][mv] as usize)
    }
    /// Number of edges bad for axis y.
    pub fn bad_edges(&self, s: &Cubie, y: usize) -> u32 {
        let v = self.view(s, self.rot_eo[y]);
        v.ef.iter().map(|&f| f as u32).sum()
    }
    /// Bad corners (twisted for U/D) and bad edges (E-slice places holding a non-E piece, plus the reverse) of a view.
    pub fn drm(&self, v: &Cubie) -> (u8, u8) {
        let c = v.ct.iter().filter(|&&t| t != 0).count() as u8;
        let mut e = 0u8;
        for i in 0..12 {
            if self.m.e_piece[i] != self.m.e_piece[v.ep[i] as usize] {
                e += 1;
            }
        }
        (c, e)
    }
}

/// DRM name of a coset (bad corners, bad edges), from its coordinates.
pub struct DrmOf {
    pub corners: Vec<u8>, // per co: twisted corners
    pub edges: Vec<u8>,   // per sl: bad edges (2 x E-slice pieces out of the slice)
}
impl DrmOf {
    pub fn new(ctx: &Ctx) -> DrmOf {
        let corners = (0..NCO)
            .map(|co| {
                let mut t = [0u8; 8];
                let mut v = co;
                let mut s = 0;
                for i in 0..7 {
                    t[i] = (v % 3) as u8;
                    v /= 3;
                    s += t[i];
                }
                t[7] = (3 - s % 3) % 3;
                t.iter().filter(|&&x| x != 0).count() as u8
            })
            .collect();
        // the E-slice places are those of the solved state's slice coordinate
        let solved_sl = ctx.coords(&SOLVED).2;
        let mut home = [false; 12];
        let mut combs = Vec::new();
        for a in 0..12 {
            for b in a + 1..12 {
                for c in b + 1..12 {
                    for d in c + 1..12 {
                        combs.push([a, b, c, d]);
                    }
                }
            }
        }
        for &p in &combs[solved_sl] {
            home[p] = true;
        }
        let edges = combs.iter().map(|c| 2 * c.iter().filter(|&&p| !home[p]).count() as u8).collect();
        DrmOf { corners, edges }
    }
}

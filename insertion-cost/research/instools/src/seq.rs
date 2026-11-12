//! Move sequences: the 18 face turns numbered 3 * face + (quarter turns - 1), faces U D R L F B (axis = face / 2,
//! and the first face of each axis is the one that comes first in a reduced sequence: U before D, R before L, F before B).

use crate::cubie::Model;

pub const NAMES: [&str; 18] = ["U", "U2", "U'", "D", "D2", "D'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'"];

pub fn text(seq: &[u8]) -> String {
    seq.iter().map(|&m| NAMES[m as usize]).collect::<Vec<_>>().join(" ")
}

/// Parse face turns ("R U2 F'", with or without spaces; typographic apostrophes accepted).
pub fn parse(s: &str) -> Result<Vec<u8>, String> {
    let s: String = s.replace(['’', '‘', '`'], "'");
    let b: Vec<char> = s.chars().collect();
    let mut out = Vec::new();
    let mut i = 0;
    while i < b.len() {
        let c = b[i];
        if c.is_whitespace() {
            i += 1;
            continue;
        }
        let f = "UDRLFB".find(c).ok_or_else(|| format!("cannot parse {s:?} at {c:?}"))?;
        i += 1;
        let mut q = 0;
        if i < b.len() && b[i] == '2' {
            q = 1;
            i += 1;
            if i < b.len() && b[i] == '\'' {
                i += 1;
            }
        } else if i < b.len() && b[i] == '\'' {
            q = 2;
            i += 1;
        }
        out.push((3 * f + q) as u8);
    }
    Ok(out)
}

#[inline]
pub fn inv_move(m: u8) -> u8 {
    3 * (m / 3) + 2 - m % 3
}
pub fn invert(seq: &[u8]) -> Vec<u8> {
    seq.iter().rev().map(|&m| inv_move(m)).collect()
}

/// A sequence with all cancelling done (a port of `cancel` in cube.py): consecutive turns about one axis are merged
/// face by face, repeatedly.
pub fn cancel(seq: &[u8]) -> Vec<u8> {
    let mut out: Vec<u8> = Vec::new();
    let mut i = 0;
    while i < seq.len() {
        let axis = seq[i] / 6;
        let mut q = [0u8; 2];
        while let Some(&l) = out.last() {
            if l / 6 != axis {
                break;
            }
            q[((l / 3) % 2) as usize] += l % 3 + 1;
            out.pop();
        }
        while i < seq.len() && seq[i] / 6 == axis {
            q[((seq[i] / 3) % 2) as usize] += seq[i] % 3 + 1;
            i += 1;
        }
        for k in 0..2u8 {
            if q[k as usize] % 4 != 0 {
                out.push(3 * (2 * axis + k) + q[k as usize] % 4 - 1);
            }
        }
    }
    out
}

/// May move `b` follow move `a` in a reduced sequence?
#[inline]
pub fn follows(a: u8, b: u8) -> bool {
    let (fa, fb) = (a / 3, b / 3);
    fa != fb && !(fa / 2 == fb / 2 && fa > fb)
}
pub fn is_reduced(seq: &[u8]) -> bool {
    seq.windows(2).all(|w| follows(w[0], w[1]))
}

/// Push one move on a reduced sequence, keeping it reduced (the product in normal form).
#[inline]
pub fn push(v: &mut Vec<u8>, m: u8) {
    let (mut low, mut look, mut off) = (usize::MAX, usize::MAX, false);
    push_t(v, m, &mut low, &mut look, &mut off);
}

/// `push` that also records the lowest index changed (`low`), the lowest index read (`look`), whether the push found
/// the sequence empty (`off`); returns true when the move went on top of a move of another axis (or on nothing): after
/// that, further moves of a reduced sequence go on unchanged.
#[inline]
pub fn push_t(v: &mut Vec<u8>, m: u8, low: &mut usize, look: &mut usize, off: &mut bool) -> bool {
    let n = v.len();
    if n == 0 {
        *off = true;
        v.push(m);
        return true;
    }
    let t = v[n - 1];
    if n - 1 < *look {
        *look = n - 1;
    }
    if t / 6 != m / 6 {
        v.push(m);
        return true;
    }
    let idx;
    if t / 3 == m / 3 {
        idx = n - 1;
    } else {
        // the top is the other face of this axis; the move under it may be this face
        if n >= 2 {
            if n - 2 < *look {
                *look = n - 2;
            }
        } else {
            *off = true;
        }
        if n >= 2 && v[n - 2] / 3 == m / 3 {
            idx = n - 2;
        } else {
            // joins the run without merging
            if (m / 3) % 2 == 0 {
                v[n - 1] = m;
                v.push(t);
                if n - 1 < *low {
                    *low = n - 1;
                }
            } else {
                v.push(m);
            }
            return false;
        }
    }
    let q = (v[idx] % 3 + 1 + m % 3 + 1) % 4;
    if q == 0 {
        v.remove(idx);
    } else {
        v[idx] = 3 * (m / 3) + q - 1;
    }
    if idx < *low {
        *low = idx;
    }
    false
}

/// What inserting `a` between `x` and `y` does.
#[derive(Clone, Copy, Debug)]
pub struct Ev {
    pub len: u16,   // length of cancel(x + a + y)
    pub low: u16,   // x[..low] is unchanged at the front of the result
    pub lstart: i16, // lowest index of x that was read (-1: the cancelling ran off the start of x)
    pub r: u16,     // number of moves of y that were read (y.len() + 1: ran off the end)
    pub b: u16,     // y[b..] is unchanged at the end of the result
}

/// cancel(x + a + y) for reduced x, a, y; `buf` receives the result (all of it when `whole`, else without the
/// unchanged tail y[b..]).
#[inline]
pub fn insert(buf: &mut Vec<u8>, x: &[u8], a: &[u8], y: &[u8], whole: bool) -> Ev {
    buf.clear();
    buf.extend_from_slice(x);
    let i = x.len();
    let (mut low, mut look, mut off) = (i, i, false);
    for &m in a {
        push_t(buf, m, &mut low, &mut look, &mut off);
    }
    let mut k = 0;
    let mut stopped = false;
    while k < y.len() {
        stopped = push_t(buf, y[k], &mut low, &mut look, &mut off);
        k += 1;
        if stopped {
            break;
        }
    }
    let len = buf.len() + (y.len() - k);
    if whole {
        buf.extend_from_slice(&y[k..]);
    }
    let low = low.min(i);
    Ev {
        len: len as u16,
        low: low as u16,
        lstart: if off { -1 } else { look.min(i) as i16 },
        r: if stopped { k as u16 } else { y.len() as u16 + 1 },
        b: if stopped { k as u16 - 1 } else { y.len() as u16 },
    }
}

/// The sequence after turning the whole cube by rotation r (and, with `mirror`, reflecting it left-right first),
/// in reduced form.
pub fn relabel(m: &Model, seq: &[u8], r: usize, mirror: bool) -> Vec<u8> {
    let mut out: Vec<u8> = Vec::with_capacity(seq.len());
    for &mv in seq {
        let (mut f, mut q) = ((mv / 3) as usize, mv % 3);
        if mirror {
            f = [0, 1, 3, 2, 4, 5][f];
            q = 2 - q;
        }
        out.push(3 * m.rot_faces[r][f] + q);
    }
    // only the order inside pairs of opposite faces can be wrong
    for i in 1..out.len() {
        if out[i - 1] / 6 == out[i] / 6 && out[i - 1] / 3 > out[i] / 3 {
            out.swap(i - 1, i);
        }
    }
    out
}

/// A sequence of at most 12 moves in 64 bits: 5 bits a move, the length in the top 4 bits.
#[inline]
pub fn pack(seq: &[u8]) -> u64 {
    debug_assert!(seq.len() <= 12);
    let mut v = (seq.len() as u64) << 60;
    for (i, &m) in seq.iter().enumerate() {
        v |= (m as u64) << (5 * i);
    }
    v
}
#[inline]
pub fn plen(v: u64) -> usize {
    (v >> 60) as usize
}
#[inline]
pub fn unpack(v: u64, out: &mut [u8; 12]) -> usize {
    let n = (v >> 60) as usize;
    for i in 0..n {
        out[i] = ((v >> (5 * i)) & 31) as u8;
    }
    n
}
pub fn unpack_vec(v: u64) -> Vec<u8> {
    let mut b = [0u8; 12];
    let n = unpack(v, &mut b);
    b[..n].to_vec()
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
        let n = n as u64;
        let lim = u64::MAX - u64::MAX % n;
        loop {
            let v = self.next();
            if v < lim {
                return (v % n) as usize;
            }
        }
    }
    /// A random reduced sequence: each move uniform among those that keep the sequence reduced.
    pub fn skeleton(&mut self, n: usize) -> Vec<u8> {
        let mut s: Vec<u8> = Vec::with_capacity(n);
        for _ in 0..n {
            let ok: Vec<u8> = (0..18u8).filter(|&m| s.last().map_or(true, |&l| follows(l, m))).collect();
            s.push(ok[self.below(ok.len())]);
        }
        s
    }
}

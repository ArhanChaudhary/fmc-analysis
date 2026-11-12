//! Question B (scramble -> EO), the parts that need no DR table.
//!
//! `eo axis`     exact over the 2048 EO states of one axis: optimal linear EO and the number of EO solutions of each
//!               length 0..8 (canonical sequences that solve EO for the first time at their end, i.e. no shorter
//!               prefix is an EO; their last turn is a quarter turn of the axis).  A random-state scramble has each
//!               of the 2048 states with probability 1/2048, so this is the exact one-axis linear distribution.
//! `eo layouts`  exact counts of the bad-edge triple (F/B, R/L, U/D) over all 12!·2^11 edge states: an edge's badness
//!               on each axis depends on its flip, its place and its piece, and a state's counts only on which kind
//!               of piece (E, M or S slice) sits at each place, so 34650 kind arrangements x 2048 flip patterns,
//!               each standing for 4!^3 permutations.
//! `eo sample`   uniformly random states: per axis the bad edges, the optimal EO linear, on the inverse and with NISS
//!               (exact by the shorter-side argument), aggregated.

use crate::common::*;
use crate::cubie::{Cubie, SOLVED};
use rayon::prelude::*;
use std::collections::BTreeMap;

const L: usize = 9; // lengths 0..8

/// Number of first-reach EO solutions of each length from each eo state (fresh start, canonical).
pub fn eo_counts(c: &Ctx) -> Vec<[u64; L]> {
    // f[r][lastface][eo]
    let mut f = vec![vec![vec![0u64; NEO]; 7]; L];
    for lf in 0..7 {
        f[0][lf][0] = 1;
    }
    for r in 1..L {
        for lf in 0..7 {
            let last = if lf == 6 { NONE } else { 3 * lf };
            for e in 1..NEO {
                let mut s = 0u64;
                for mv in 0..18 {
                    if canon_ok(last, mv) {
                        s += f[r - 1][mv / 3][c.t.eo[e][mv] as usize];
                    }
                }
                f[r][lf][e] = s;
            }
        }
    }
    (0..NEO).map(|e| {
        let mut out = [0u64; L];
        for r in 0..L {
            out[r] = f[r][6][e];
        }
        out
    }).collect()
}

fn axis_cmd(c: &Ctx) {
    let cnt = eo_counts(c);
    print!("eo\tbad\toptimal");
    for r in 0..L {
        print!("\tn{r}");
    }
    println!();
    for e in 0..NEO {
        let bad = (e as u32).count_ones() + ((e as u32).count_ones() & 1); // the twelfth edge makes the count even
        print!("{e}\t{bad}\t{}", c.eodist[e]);
        for r in 0..L {
            print!("\t{}", cnt[e][r]);
        }
        println!();
    }
}

/// For each axis y: g[y][place][piece] = the flip (F/B orientation, ef) that is bad for y is ef ^ g.
fn badness(c: &Ctx) -> [[[u8; 12]; 12]; 3] {
    let mut g = [[[0u8; 12]; 12]; 3];
    for y in 0..3 {
        let mp = &c.m.rots[c.rot_eo[y]];
        for i in 0..12 {
            for p in 0..12 {
                g[y][i][p] = mp.ea[i] ^ mp.ea[p];
            }
        }
    }
    g
}

fn layouts_cmd(c: &Ctx) {
    let g = badness(c);
    // piece kinds: 0 E slice (no U/D colour), 1 M slice, 2 S slice; read off the places of the solved cube
    let kind: Vec<u8> = (0..12).map(|p| if c.m.e_piece[p] { 0 } else { c.m.slot_kind[p] }).collect();
    let mut pieces: [Vec<usize>; 3] = [vec![], vec![], vec![]];
    for p in 0..12 {
        pieces[kind[p] as usize].push(p);
    }
    assert!(pieces.iter().all(|v| v.len() == 4));
    // check: the badness of an edge depends on its piece only through the piece's kind
    for y in 0..3 {
        for i in 0..12 {
            for k in 0..3 {
                let v = g[y][i][pieces[k][0]];
                assert!(pieces[k].iter().all(|&p| g[y][i][p] == v), "badness depends on more than the kind");
            }
        }
    }
    // all arrangements of kinds over the 12 places
    let mut arr = Vec::new();
    fn rec(i: usize, left: [usize; 3], cur: &mut [u8; 12], out: &mut Vec<[u8; 12]>) {
        if i == 12 {
            out.push(*cur);
            return;
        }
        for k in 0..3 {
            if left[k] > 0 {
                let mut l = left;
                l[k] -= 1;
                cur[i] = k as u8;
                rec(i + 1, l, cur, out);
            }
        }
    }
    rec(0, [4, 4, 4], &mut [0; 12], &mut arr);
    assert_eq!(arr.len(), 34650);
    let tally: BTreeMap<(u32, u32, u32), u64> = arr
        .par_iter()
        .map(|a| {
            let mut t: BTreeMap<(u32, u32, u32), u64> = BTreeMap::new();
            let mut mask = [0u32; 3];
            for y in 0..3 {
                for i in 0..12 {
                    mask[y] |= (g[y][i][pieces[a[i] as usize][0]] as u32) << i;
                }
            }
            for f in 0..4096u32 {
                if f.count_ones() % 2 == 1 {
                    continue;
                }
                let b = ((f ^ mask[2]).count_ones(), (f ^ mask[0]).count_ones(), (f ^ mask[1]).count_ones());
                *t.entry(b).or_insert(0) += 1;
            }
            t
        })
        .reduce(BTreeMap::new, |mut a, b| {
            for (k, v) in b {
                *a.entry(k).or_insert(0) += v;
            }
            a
        });
    // cross-check against the view of random states
    let mut rng = Rng::new(7, 0);
    for _ in 0..2000 {
        let s = random_cube(&mut rng, false);
        let mut mask = [0u32; 3];
        let mut f = 0u32;
        for i in 0..12 {
            f |= (s.ef[i] as u32) << i;
            for y in 0..3 {
                mask[y] |= (g[y][i][s.ep[i] as usize] as u32) << i;
            }
        }
        for y in 0..3 {
            assert_eq!((f ^ mask[y]).count_ones(), c.bad_edges(&s, y));
        }
    }
    println!("bad_fb\tbad_rl\tbad_ud\tstates");
    let mut tot = 0u64;
    for ((a, b, d), n) in &tally {
        println!("{a}\t{b}\t{d}\t{n}");
        tot += n;
    }
    eprintln!("{tot} arrangement x flip states (x 4!^3 permutations each)");
}

/// Optimal NISS EO on axis y: min over C on one side of |C| + linear EO of C^-1 base, both bases.
pub fn niss_eo(c: &Ctx, s: &Cubie, si: &Cubie, y: usize) -> (u8, u8, u8) {
    let base = [c.view(s, c.rot_eo[y]), c.view(si, c.rot_eo[y])];
    let lin = c.eodist[Ctx::eo(&base[0])];
    let inv = c.eodist[Ctx::eo(&base[1])];
    let mut b = lin.min(inv);
    let mut k = 1;
    fn pre(c: &Ctx, y: usize, k: usize, last: usize, p: &Cubie, base: &[Cubie; 2], kk: u8, b: &mut u8) {
        if k == 0 {
            let pv = c.view(p, c.rot_eo[y]);
            for side in 0..2 {
                let v = kk + c.eodist[Ctx::eo_then(&pv, &base[side])];
                if v < *b {
                    *b = v;
                }
            }
            return;
        }
        for mv in 0..18 {
            if canon_ok(last, mv) {
                pre(c, y, k - 1, mv, &c.mvc[inv_move(mv)].then(p), base, kk, b);
            }
        }
    }
    while 2 * k < b as usize {
        pre(c, y, k, NONE, &SOLVED, &base, k as u8, &mut b);
        k += 1;
    }
    (lin, inv, b)
}

fn sample_cmd(c: &Ctx, n: usize, seed: u64) {
    // per axis (pooled): (bad, linear, NISS) ; any axis: (best linear, best of linear/inverse, best NISS)
    type Acc = (BTreeMap<(u32, u8, u8, u8), u64>, BTreeMap<(u8, u8, u8), u64>);
    let (per, any): Acc = (0..n)
        .into_par_iter()
        .fold(
            || (BTreeMap::new(), BTreeMap::new()),
            |mut acc: Acc, i| {
                let mut rng = Rng::new(seed, i as u64);
                let s = random_cube(&mut rng, false);
                let si = s.inverse();
                let (mut bl, mut bb, mut bn) = (99u8, 99u8, 99u8);
                for y in 0..3 {
                    let (lin, inv, ni) = niss_eo(c, &s, &si, y);
                    *acc.0.entry((c.bad_edges(&s, y), lin, inv, ni)).or_insert(0) += 1;
                    bl = bl.min(lin);
                    bb = bb.min(lin.min(inv));
                    bn = bn.min(ni);
                }
                *acc.1.entry((bl, bb, bn)).or_insert(0) += 1;
                acc
            },
        )
        .reduce(
            || (BTreeMap::new(), BTreeMap::new()),
            |mut a, b| {
                for (k, v) in b.0 {
                    *a.0.entry(k).or_insert(0) += v;
                }
                for (k, v) in b.1 {
                    *a.1.entry(k).or_insert(0) += v;
                }
                a
            },
        );
    println!("# per axis, pooled over the three axes of {n} random states");
    println!("what\tbad\tlinear\tinverse\tniss\tcount");
    for ((b, l, i, x), v) in per {
        println!("axis\t{b}\t{l}\t{i}\t{x}\t{v}");
    }
    for ((l, b, x), v) in any {
        println!("any\t-\t{l}\t{b}\t{x}\t{v}");
    }
}

pub fn cmd(a: &[String]) {
    let c = Ctx::new();
    match a[0].as_str() {
        "axis" => axis_cmd(&c),
        "layouts" => layouts_cmd(&c),
        "sample" => sample_cmd(&c, a[1].parse().unwrap(), a[2].parse().unwrap()),
        _ => panic!("eo axis | layouts | sample <n> <seed>"),
    }
}

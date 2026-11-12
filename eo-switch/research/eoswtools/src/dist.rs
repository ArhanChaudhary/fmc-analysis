//! Exact EO-kept DR distance over the 1,082,565 cosets, the R/L-axis probabilities, and positions for the nissy check.

use crate::common::*;
use crate::cubie::SOLVED;
use rayon::prelude::*;
use std::io::Write;

/// The 14 turns that keep F/B EO: U D R L (all three powers), F2, B2.
pub const EOK: [usize; 14] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 16];

#[inline]
pub fn cmove(t: &Tables, ix: usize, mv: usize) -> usize {
    t.co[ix / NSL][mv] as usize * NSL + t.sl[ix % NSL][mv] as usize
}

pub fn solved_ix(c: &Ctx) -> usize {
    let (co, _, sl) = c.coords(&SOLVED);
    co * NSL + sl
}

/// Breadth-first search from the DR coset with the 14 EO-keeping turns (a turn set closed under inverses, so the
/// distance from the target equals the distance to it).
pub fn bfs(c: &Ctx) -> Vec<u8> {
    let mut d = vec![255u8; N0];
    d[solved_ix(c)] = 0;
    let mut frontier = vec![solved_ix(c)];
    let mut k = 0u8;
    while !frontier.is_empty() {
        let mut next = Vec::new();
        for &ix in &frontier {
            for &mv in &EOK {
                let j = cmove(&c.t, ix, mv);
                if d[j] == 255 {
                    d[j] = k + 1;
                    next.push(j);
                }
            }
        }
        frontier = next;
        k += 1;
    }
    d
}

pub fn load_d(path: &str) -> Vec<u8> {
    let d = std::fs::read(path).unwrap_or_else(|_| panic!("missing {path} (run eoswtools dist)"));
    assert_eq!(d.len(), N0);
    d
}

/// eoswtools dist <out.u8>: the BFS, its histogram, and the comparison with eo-to-dr's eo = 0 part of eo-fb_dr.u8.
pub fn dist_cmd(a: &[String]) {
    let c = Ctx::new();
    let d = bfs(&c);
    assert!(d.iter().all(|&x| x != 255), "unreachable coset");
    std::fs::write(&a[0], &d).unwrap();
    let mut h = [0u64; 16];
    for &x in &d {
        h[x as usize] += 1;
    }
    let mean = h.iter().enumerate().map(|(k, &n)| k as f64 * n as f64).sum::<f64>() / N0 as f64;
    println!("# EO-kept DR distance over the {N0} cosets (BFS, 14 turns); mean {mean:.6}");
    for (k, &n) in h.iter().enumerate() {
        if n > 0 {
            println!("{k}\t{n}");
        }
    }
    let other = "/data/fmc/eo-to-dr/research/out/big/eo-fb_dr_eo0.u8";
    match std::fs::read(other) {
        Ok(o) => {
            let same = o.iter().zip(&d).filter(|(x, y)| x == y).count();
            println!("# equal to eo-to-dr's {other} on {same} of {N0} cosets");
        }
        Err(_) => println!("# {other} not found"),
    }
}

/// eoswtools twoaxis <d.u8> <out.u32>: for every coset (co_UD, sl_E) of a uniformly random F/B-EO-solved cube, the
/// number of (corner permutation, edge arrangement) completions out of 8! * 70 = 2,822,400 whose R/L-axis EO-kept DR
/// distance is <= k, for k = 4, 5, 6, 7, 8 (five u32 arrays, k-major).  Corners (8! permutations) and the places of
/// the M-slice pieces (70 per E-slice set) are independent and uniform given the coset (as in eo-to-dr's twoaxis).
pub fn twoaxis_cmd(a: &[String]) {
    let c = Ctx::new();
    let d = load_d(&a[0]);
    let r = c.rot_pair[0][2];
    let mut perms: Vec<[u8; 8]> = Vec::new();
    fn heap(k: usize, p: &mut [u8; 8], out: &mut Vec<[u8; 8]>) {
        if k == 1 {
            out.push(*p);
            return;
        }
        for i in 0..k {
            heap(k - 1, p, out);
            if k % 2 == 0 { p.swap(i, k - 1) } else { p.swap(0, k - 1) }
        }
    }
    heap(8, &mut [0, 1, 2, 3, 4, 5, 6, 7], &mut perms);
    assert_eq!(perms.len(), 40320);
    let mp = &c.m.rots[r];
    let cc: Vec<Vec<u32>> = (0..NCO)
        .into_par_iter()
        .map(|co_ud| {
            let mut row = vec![0u32; NCO];
            let mut ct = [0u8; 8];
            let mut v = co_ud;
            let mut s = 0;
            for i in 0..7 {
                ct[i] = (v % 3) as u8;
                v /= 3;
                s += ct[i];
            }
            ct[7] = (3 - s % 3) % 3;
            for cp in &perms {
                let mut tct = [0u8; 8];
                for i in 0..8 {
                    tct[mp.cd[i] as usize] = (ct[i] + mp.ca[i] + 3 - mp.ca[cp[i] as usize]) % 3;
                }
                let mut co = 0usize;
                for i in (0..7).rev() {
                    co = co * 3 + tct[i] as usize;
                }
                row[co] += 1;
            }
            row
        })
        .collect();
    // the corner shortcut against the full view on random states
    let mut rng = Rng::new(11, 0);
    for _ in 0..1000 {
        let s = random_cube(&mut rng, true);
        let v = c.view(&s, r);
        assert_eq!(Ctx::eo(&v), 0);
        let mut tct = [0u8; 8];
        for i in 0..8 {
            tct[mp.cd[i] as usize] = (s.ct[i] + mp.ca[i] + 3 - mp.ca[s.cp[i] as usize]) % 3;
        }
        assert_eq!(tct, v.ct);
    }
    // edge arrangements of E, M, S pieces -> (sl_E, sl_M)
    let kind: Vec<u8> = (0..12).map(|p| if c.m.e_piece[p] { 0 } else { c.m.slot_kind[p] }).collect();
    let mut pieces: [Vec<u8>; 3] = [vec![], vec![], vec![]];
    for p in 0..12 {
        pieces[kind[p] as usize].push(p as u8);
    }
    let mut e = vec![vec![0u32; NSL]; NSL];
    fn rec(i: usize, left: [usize; 3], cur: &mut [u8; 12], f: &mut dyn FnMut(&[u8; 12])) {
        if i == 12 {
            f(cur);
            return;
        }
        for k in 0..3 {
            if left[k] > 0 {
                let mut l = left;
                l[k] -= 1;
                cur[i] = k as u8;
                rec(i + 1, l, cur, f);
            }
        }
    }
    let mut narr = 0;
    rec(0, [4, 4, 4], &mut [0; 12], &mut |arr| {
        let mut used = [0usize; 3];
        let mut s = SOLVED;
        for i in 0..12 {
            let k = arr[i] as usize;
            s.ep[i] = pieces[k][used[k]];
            used[k] += 1;
        }
        e[c.coords(&s).2][c.coords(&c.view(&s, r)).2] += 1;
        narr += 1;
    });
    assert_eq!(narr, 34650);
    for row in &e {
        assert_eq!(row.iter().sum::<u32>(), 70);
    }
    let ks = [4u8, 5, 6, 7, 8];
    let mut out = Vec::with_capacity(ks.len() * N0 * 4);
    for &k in &ks {
        // g[co_rl][sl_e] = completions of the edges with d(co_rl, sl_m) <= k
        let g: Vec<Vec<u32>> = (0..NCO)
            .map(|co| (0..NSL).map(|sle| (0..NSL).filter(|&slm| e[sle][slm] > 0 && d[co * NSL + slm] <= k).map(|slm| e[sle][slm]).sum()).collect())
            .collect();
        let p: Vec<Vec<u32>> = (0..NCO)
            .into_par_iter()
            .map(|co_ud| {
                let mut acc = vec![0u64; NSL];
                for co_rl in 0..NCO {
                    let w = cc[co_ud][co_rl] as u64;
                    if w == 0 {
                        continue;
                    }
                    let gr = &g[co_rl];
                    for i in 0..NSL {
                        acc[i] += w * gr[i] as u64;
                    }
                }
                acc.iter().map(|&x| u32::try_from(x).unwrap()).collect()
            })
            .collect();
        for row in &p {
            for &x in row {
                out.extend_from_slice(&x.to_le_bytes());
            }
        }
        let tot: f64 = p.iter().flatten().map(|&x| x as f64).sum::<f64>() / (N0 as f64 * 2_822_400.0);
        eprintln!("k = {k}: P(R/L distance <= k) over uniform states = {tot:.6}");
    }
    std::fs::write(&a[1], &out).unwrap();
}

/// eoswtools checkpos <d.u8> <n> <seed>: n uniformly random cosets, each written as a scramble (a random DR-group
/// sequence of 12 turns, then the inverse of a shortest EO-kept path from the coset to DR), with the table's value.
pub fn checkpos_cmd(a: &[String]) {
    let c = Ctx::new();
    let d = load_d(&a[0]);
    let (n, seed): (usize, u64) = (a[1].parse().unwrap(), a[2].parse().unwrap());
    const DRG: [usize; 10] = [0, 1, 2, 3, 4, 5, 7, 10, 13, 16];
    let so = std::io::stdout();
    let mut o = so.lock();
    writeln!(o, "ix\texpected\tscramble").unwrap();
    for i in 0..n {
        let mut rng = Rng::new(seed, i as u64);
        let ix = rng.below(N0);
        let mut path = Vec::new();
        let mut x = ix;
        while d[x] > 0 {
            let mv = *EOK.iter().find(|&&mv| d[cmove(&c.t, x, mv)] == d[x] - 1).unwrap();
            path.push(mv);
            x = cmove(&c.t, x, mv);
        }
        let mut pre = Vec::new();
        let mut last = NONE;
        while pre.len() < 12 {
            let mv = DRG[rng.below(10)];
            if canon_ok(last, mv) {
                pre.push(mv);
                last = mv;
            }
        }
        let mut scr = pre.clone();
        scr.extend(invert(&path));
        let s = c.m.apply(&SOLVED, &scr);
        let (co, eo, sl) = c.coords(&s);
        assert_eq!((co * NSL + sl, eo), (ix, 0));
        writeln!(o, "{ix}\t{}\t{}", d[ix], text(&scr)).unwrap();
    }
}

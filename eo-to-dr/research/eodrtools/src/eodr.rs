//! Question C (EO -> DR).  The EO is on F/B (the table's own frame); the first DR axis is U/D, the second R/L.
//!
//! `eodr exact`   over the 1,082,565 cosets with F/B EO solved (each equally likely after a random EO), per DRM of
//!                U/D: the fewest turns keeping EO (eo-fb_dr), with any turns (all_dr), and with last-move inversion
//!                (the better of the coset and the coset after F2, or after B2: an EO ending F' instead of F).
//! `eodr twoaxis` exact distribution of the better of the two DR axes of one EO (U/D or R/L, EO kept), per DRM of
//!                U/D, over all EO-solved states: corners (8!·3^7) and the places of the E- and M-slice pieces
//!                (34650 arrangements) are independent and uniform, and the two distances depend on (co_UD, sl_E)
//!                and (co_RL, sl_M); see `twoaxis` for the sum.
//! `eodr sample`  uniformly random EO-solved states with every option (two axes, inverse, last-move inversion, any
//!                turns, and their combinations), all from exact table lookups.

use crate::common::*;
use crate::cubie::{Cubie, SOLVED};
use rayon::prelude::*;

const NV: usize = 12; // distances 0..11

fn exact_cmd(c: &Ctx, eo_dr: &Eo0, all0: &Eo0) {
    let drm = DrmOf::new(c);
    // tallies [corners][edges][option][distance]
    let opts = ["eo", "any", "eo_switchF", "eo_switchB", "any_switchF"];
    let mut t = vec![[[[0u64; NV]; 5]; 5]; 9];
    for co in 0..NCO {
        for sl in 0..NSL {
            let (bc, be) = (drm.corners[co] as usize, drm.edges[sl] as usize / 2);
            let d = eo_dr.at(co, sl);
            let a = all0.at(co, sl);
            let f2 = (c.t.co[co][13] as usize, c.t.sl[sl][13] as usize);
            let b2 = (c.t.co[co][16] as usize, c.t.sl[sl][16] as usize);
            let v = [d, a, d.min(eo_dr.at(f2.0, f2.1)), d.min(eo_dr.at(b2.0, b2.1)), a.min(all0.at(f2.0, f2.1))];
            for (o, &x) in v.iter().enumerate() {
                t[bc][be][o][x as usize] += 1;
            }
        }
    }
    println!("corners\tedges\toption\t{}", (0..NV).map(|d| format!("d{d}")).collect::<Vec<_>>().join("\t"));
    for bc in 0..9 {
        for be in 0..5 {
            for o in 0..5 {
                let row = &t[bc][be][o];
                if row.iter().sum::<u64>() > 0 {
                    println!("{bc}\t{}\t{}\t{}", 2 * be, opts[o], row.iter().map(|x| x.to_string()).collect::<Vec<_>>().join("\t"));
                }
            }
        }
    }
}

/// The view that carries R/L to U/D and keeps F/B.
fn rot_rl(c: &Ctx) -> usize {
    c.rot_pair[0][2]
}

fn twoaxis_cmd(c: &Ctx, eo_dr: &Eo0) {
    let r = rot_rl(c);
    let drm = DrmOf::new(c);
    let t0 = std::time::Instant::now();
    // joint corner counts C[co_UD][co_RL] over 8! x 3^7 corner states
    let perms: Vec<[u8; 8]> = {
        let mut v = Vec::new();
        let mut p = [0u8, 1, 2, 3, 4, 5, 6, 7];
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
        heap(8, &mut p, &mut v);
        v
    };
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
                // corner part of Model::conj
                let mut tct = [0u8; 8];
                for i in 0..8 {
                    let j = mp.cd[i] as usize;
                    tct[j] = (ct[i] + mp.ca[i] + 3 - mp.ca[cp[i] as usize]) % 3;
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
    // check the corner part against the full conj on a few states
    let mut rng = Rng::new(11, 0);
    for _ in 0..1000 {
        let s = random_cube(&mut rng, true);
        let v = c.view(&s, r);
        assert_eq!(Ctx::eo(&v), 0, "F/B EO must survive the R/L view");
        let mut tct = [0u8; 8];
        for i in 0..8 {
            tct[mp.cd[i] as usize] = (s.ct[i] + mp.ca[i] + 3 - mp.ca[s.cp[i] as usize]) % 3;
        }
        assert_eq!(tct, v.ct);
    }
    eprintln!("corner pairs done {:.1}s", t0.elapsed().as_secs_f64());
    // edge arrangements: kinds of pieces (E, M, S) over the 12 places -> (sl_E, sl_M)
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
    rec(0, [4, 4, 4], &mut [0; 12], &mut |a| {
        let mut used = [0usize; 3];
        let mut s = SOLVED;
        for i in 0..12 {
            let k = a[i] as usize;
            s.ep[i] = pieces[k][used[k]];
            used[k] += 1;
        }
        let sle = c.coords(&s).2;
        let slm = c.coords(&c.view(&s, r)).2;
        e[sle][slm] += 1;
        narr += 1;
    });
    assert_eq!(narr, 34650);
    let nz: Vec<Vec<(usize, u64)>> = (0..NSL).map(|a| (0..NSL).filter(|&b| e[a][b] != 0).map(|b| (b, e[a][b] as u64)).collect()).collect();
    // kb[co_RL][v][sl_E] = sum over sl_M of E[sl_E][sl_M] * [d(co_RL, sl_M) >= v]
    let kb: Vec<Vec<[u64; NSL]>> = (0..NCO)
        .into_par_iter()
        .map(|co| {
            (0..NV)
                .map(|v| {
                    let mut out = [0u64; NSL];
                    for sle in 0..NSL {
                        let mut s = 0u64;
                        for &(slm, k) in &nz[sle] {
                            if eo_dr.at(co, slm) as usize >= v {
                                s += k;
                            }
                        }
                        out[sle] = s;
                    }
                    out
                })
                .collect()
        })
        .collect();
    eprintln!("edge kernel done {:.1}s", t0.elapsed().as_secs_f64());
    // acc[corners][edges][v] = weight of states (DRM of U/D) whose better axis is >= v; also one-axis for checking
    let acc: Vec<[[[u128; NV]; 5]; 2]> = (0..NCO)
        .into_par_iter()
        .map(|co_ud| {
            let mut w = vec![[0u64; NSL]; NV];
            for co_rl in 0..NCO {
                let k = cc[co_ud][co_rl] as u64;
                if k == 0 {
                    continue;
                }
                for v in 0..NV {
                    let src = &kb[co_rl][v];
                    let dst = &mut w[v];
                    for i in 0..NSL {
                        dst[i] += k * src[i];
                    }
                }
            }
            let tot: u64 = cc[co_ud].iter().map(|&x| x as u64).sum();
            let mut out = [[[0u128; NV]; 5]; 2];
            for sle in 0..NSL {
                let d = eo_dr.at(co_ud, sle) as usize;
                let be = drm.edges[sle] as usize / 2;
                let esum: u64 = e[sle].iter().map(|&x| x as u64).sum();
                for v in 0..NV {
                    if d >= v {
                        out[0][be][v] += w[v][sle] as u128;
                        out[1][be][v] += (tot * esum) as u128;
                    }
                }
            }
            out
        })
        .collect();
    eprintln!("sum done {:.1}s", t0.elapsed().as_secs_f64());
    // group by corners of co_UD
    let mut g = [[[[0u128; NV]; 5]; 9]; 2];
    for co in 0..NCO {
        let bc = drm.corners[co] as usize;
        for w in 0..2 {
            for be in 0..5 {
                for v in 0..NV {
                    g[w][bc][be][v] += acc[co][w][be][v];
                }
            }
        }
    }
    println!("# weight of EO-solved states with distance >= v (v = 0..11), by DRM of U/D; total weight = all states");
    println!("option\tcorners\tedges\t{}", (0..NV).map(|v| format!("ge{v}")).collect::<Vec<_>>().join("\t"));
    for (w, name) in [(0, "best_of_two_axes"), (1, "ud_only")] {
        for bc in 0..9 {
            for be in 0..5 {
                if g[w][bc][be][0] > 0 {
                    println!("{name}\t{bc}\t{}\t{}", 2 * be, g[w][bc][be].iter().map(|x| x.to_string()).collect::<Vec<_>>().join("\t"));
                }
            }
        }
    }
}

fn sample_cmd(c: &Ctx, eo_dr: &Eo0, all0: &Eo0, n: usize, seed: u64) {
    let r = rot_rl(c);
    // options: the four EO-kept distances for (normal T, T F2) x (U/D, R/L) x (normal, inverse), and any-turn ones
    let names = [
        "plain", "other_axis", "best_two_axes", "inverse_only", "normal_or_inverse", "switch_last", "two_axes_switch",
        "two_axes_inverse", "all_eo_kept", "any_turns", "any_two_axes", "everything",
    ];
    let no = names.len();
    // tallies per DRM of T on U/D: [bc][be][option][d]; joint normal/inverse (U/D) per DRM; DRM pairs
    struct Acc {
        t: Vec<u64>,
        joint: Vec<u64>,
        pair: Vec<u64>,
    }
    let ix = |bc: usize, be: usize, o: usize, d: usize| ((bc * 5 + be) * 12 + o) * NV + d;
    let jx = |bc: usize, be: usize, a: usize, b: usize| ((bc * 5 + be) * NV + a) * NV + b;
    let px = |a: (usize, usize), b: (usize, usize), d: usize| (((a.0 * 5 + a.1) * 9 + b.0) * 5 + b.1) * NV + d;
    let acc = (0..n)
        .into_par_iter()
        .fold(
            || Acc { t: vec![0; 9 * 5 * 12 * NV], joint: vec![0; 9 * 5 * NV * NV], pair: vec![0; 45 * 45 * NV] },
            |mut a, i| {
                let mut rng = Rng::new(seed, i as u64);
                let t = random_cube(&mut rng, true);
                let tf = c.m.turn(&t, 13); // the same EO with its last F turned the other way
                let mut d = [[[0u8; 2]; 2]; 2]; // [switched][axis U/D, R/L][side]
                let mut any = [[[0u8; 2]; 2]; 2];
                for (wi, w) in [t, tf].iter().enumerate() {
                    for (ai, rot) in [None, Some(r)].iter().enumerate() {
                        let v = match rot { None => *w, Some(r) => c.view(w, *r) };
                        for (si, u) in [v, v.inverse()].iter().enumerate() {
                            let (co, eo, sl) = c.coords(u);
                            debug_assert_eq!(eo, 0);
                            d[wi][ai][si] = eo_dr.at(co, sl);
                            any[wi][ai][si] = all0.at(co, sl);
                        }
                    }
                }
                let (bc, be) = c.drm(&t);
                let (bc, be) = (bc as usize, be as usize / 2);
                let (rc, re) = c.drm(&c.view(&t, r));
                let mn = |xs: &[u8]| *xs.iter().min().unwrap() as usize;
                let vals = [
                    d[0][0][0] as usize,
                    d[0][1][0] as usize,
                    mn(&[d[0][0][0], d[0][1][0]]),
                    d[0][0][1] as usize,
                    mn(&[d[0][0][0], d[0][0][1]]),
                    mn(&[d[0][0][0], d[1][0][0]]),
                    mn(&[d[0][0][0], d[0][1][0], d[1][0][0], d[1][1][0]]),
                    mn(&[d[0][0][0], d[0][1][0], d[0][0][1], d[0][1][1]]),
                    mn(&d.iter().flatten().flatten().copied().collect::<Vec<_>>()),
                    any[0][0][0] as usize,
                    mn(&[any[0][0][0], any[0][1][0]]),
                    mn(&d.iter().chain(any.iter()).flatten().flatten().copied().collect::<Vec<_>>()),
                ];
                for (o, &v) in vals.iter().enumerate() {
                    a.t[ix(bc, be, o, v)] += 1;
                }
                a.joint[jx(bc, be, d[0][0][0] as usize, d[0][0][1] as usize)] += 1;
                a.pair[px((bc, be), (rc as usize, re as usize / 2), vals[2])] += 1;
                a
            },
        )
        .reduce(
            || Acc { t: vec![0; 9 * 5 * 12 * NV], joint: vec![0; 9 * 5 * NV * NV], pair: vec![0; 45 * 45 * NV] },
            |mut a, b| {
                for (x, y) in a.t.iter_mut().zip(b.t) {
                    *x += y;
                }
                for (x, y) in a.joint.iter_mut().zip(b.joint) {
                    *x += y;
                }
                for (x, y) in a.pair.iter_mut().zip(b.pair) {
                    *x += y;
                }
                a
            },
        );
    println!("# {n} uniformly random EO-solved states (F/B), seed {seed}; options, by DRM of U/D");
    println!("table\tcorners\tedges\twhat\t{}", (0..NV).map(|v| format!("d{v}")).collect::<Vec<_>>().join("\t"));
    for bc in 0..9 {
        for be in 0..5 {
            for o in 0..no {
                let row: Vec<u64> = (0..NV).map(|v| acc.t[ix(bc, be, o, v)]).collect();
                if row.iter().sum::<u64>() > 0 {
                    println!("opt\t{bc}\t{}\t{}\t{}", 2 * be, names[o], row.iter().map(|x| x.to_string()).collect::<Vec<_>>().join("\t"));
                }
            }
            for a in 0..NV {
                let row: Vec<u64> = (0..NV).map(|b| acc.joint[jx(bc, be, a, b)]).collect();
                if row.iter().sum::<u64>() > 0 {
                    println!("joint\t{bc}\t{}\tnormal={a}\t{}", 2 * be, row.iter().map(|x| x.to_string()).collect::<Vec<_>>().join("\t"));
                }
            }
        }
    }
    for a in 0..45 {
        for b in 0..45 {
            let row: Vec<u64> = (0..NV).map(|d| acc.pair[(a * 45 + b) * NV + d]).collect();
            if row.iter().sum::<u64>() > 0 {
                println!("pair\t{}\t{}\trl={}c{}e\t{}", a / 5, 2 * (a % 5), b / 5, 2 * (b % 5), row.iter().map(|x| x.to_string()).collect::<Vec<_>>().join("\t"));
            }
        }
    }
}

pub fn cmd(a: &[String]) {
    let c = Ctx::new();
    let here = std::env::var("EODR_OUT").unwrap_or_else(|_| "/data/fmc/eo-to-dr/research/out".into());
    let eo_dr = Eo0::load(&format!("{here}/big/eo-fb_dr_eo0.u8"));
    let all0 = Eo0::load(&format!("{here}/big/all_dr_eo0.u8"));
    match a[0].as_str() {
        "exact" => exact_cmd(&c, &eo_dr, &all0),
        "twoaxis" => twoaxis_cmd(&c, &eo_dr),
        "sample" => sample_cmd(&c, &eo_dr, &all0, a[1].parse().unwrap(), a[2].parse().unwrap()),
        _ => panic!("eodr exact | twoaxis | sample <n> <seed>"),
    }
}

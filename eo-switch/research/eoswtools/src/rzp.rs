//! Population 2: states as reached by an RZP.  For every DRM X and length L = 0..6, the number of ways an RZP of
//! length L reaches each coset t of DRM X for the first time:
//!   w_L(t) = #{(s, F/B ending of the EO, sequence q of L EO-keeping turns) : s a coset (uniform start),
//!              q canonical (also against the EO's last turn), s.q = t, and no state s, s.q1, .., s.q(L-1) in X}.
//! The EO is taken to end in F (weight 1) and in B (weight 1): after F the RZP may not start with F2 (that is the other
//! EO), after B neither F2 nor B2 (F2 B is an EO ending in B).  L = 0 gives 2 per coset of X (uniform).
//! Output: 7 arrays of N0 u64 (L-major); each coset is counted for its own DRM.

use crate::common::*;
use crate::dist::{cmove, EOK};
use rayon::prelude::*;

const NOFACE: usize = 6;

#[inline]
fn canon_face(last: usize, mv: usize) -> bool {
    if last == NOFACE {
        return true;
    }
    let fm = mv / 3;
    !(last == fm || (last / 2 == fm / 2 && last > fm))
}

pub fn cmd(a: &[String]) {
    let c = Ctx::new();
    let lmax = 6;
    let drm = DrmOf::new(&c);
    let class = |ix: usize| -> usize { drm.corners[ix / NSL] as usize * 5 + drm.edges[ix % NSL] as usize / 2 };
    let cls: Vec<u8> = (0..N0).map(|ix| class(ix) as u8).collect();
    let mut present = [false; 45];
    for &k in &cls {
        present[k as usize] = true;
    }
    let targets: Vec<usize> = (0..45).filter(|&k| present[k] && k != 0).collect();
    // move tables on the coset index for the 14 turns
    let mt: Vec<[u32; 14]> = (0..N0)
        .into_par_iter()
        .map(|ix| {
            let mut r = [0u32; 14];
            for (k, &mv) in EOK.iter().enumerate() {
                r[k] = cmove(&c.t, ix, mv) as u32;
            }
            r
        })
        .collect();
    // inverse move index within EOK
    let inv_k: Vec<usize> = EOK.iter().map(|&mv| EOK.iter().position(|&m2| m2 == inv_move(mv)).unwrap()).collect();
    let per_target: Vec<Vec<Vec<(u32, u64)>>> = targets
        .par_iter()
        .map(|&x| {
            // f[ix * 7 + lastface] = number of ways to be at ix after the current length, never in X so far
            let mut f = vec![0u64; N0 * 7];
            for ix in 0..N0 {
                if cls[ix] as usize != x {
                    f[ix * 7 + 4] = 1; // EO ended in F
                    f[ix * 7 + 5] = 1; // EO ended in B
                }
            }
            let mut out: Vec<Vec<(u32, u64)>> = vec![Vec::new(); lmax + 1];
            out[0] = (0..N0).filter(|&ix| cls[ix] as usize == x).map(|ix| (ix as u32, 2u64)).collect();
            for l in 1..=lmax {
                // pull formulation: g[t][face(m)] = sum over s = t.m^-1 with lastface allowing m
                let mut g = vec![0u64; N0 * 7];
                let mut hit = vec![0u64; N0];
                for ix in 0..N0 {
                    let base = ix * 7;
                    if f[base..base + 7].iter().all(|&v| v == 0) {
                        continue;
                    }
                    for (k, &mv) in EOK.iter().enumerate() {
                        let mut ways = 0u64;
                        for lf in 0..7 {
                            let w = f[base + lf];
                            if w != 0 && canon_face(lf, mv) {
                                ways += w;
                            }
                        }
                        if ways == 0 {
                            continue;
                        }
                        let t = mt[ix][k] as usize;
                        if cls[t] as usize == x {
                            hit[t] += ways;
                        } else {
                            g[t * 7 + mv / 3] += ways;
                        }
                    }
                }
                let _ = &inv_k;
                out[l] = (0..N0).filter(|&ix| hit[ix] > 0).map(|ix| (ix as u32, hit[ix])).collect();
                f = g;
            }
            out
        })
        .collect();
    let mut w = vec![0u64; (lmax + 1) * N0];
    for (ti, &x) in targets.iter().enumerate() {
        for l in 0..=lmax {
            for &(ix, v) in &per_target[ti][l] {
                assert_eq!(cls[ix as usize] as usize, x);
                w[l * N0 + ix as usize] += v;
            }
        }
    }
    let mut buf = Vec::with_capacity(w.len() * 8);
    for v in &w {
        buf.extend_from_slice(&v.to_le_bytes());
    }
    std::fs::write(&a[1], &buf).unwrap();
    for l in 0..=lmax {
        let tot: u128 = w[l * N0..(l + 1) * N0].iter().map(|&v| v as u128).sum();
        eprintln!("L = {l}: total ways {tot}");
    }
}

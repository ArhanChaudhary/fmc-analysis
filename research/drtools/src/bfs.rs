//! `drtools bfs <outdir>` — exact optimal length (DR moves, HTM) of every state of the DR group
//! `<U, D, R2, L2, F2, B2>`.  (Port of `drbfs.c`.)
//!
//! 19,508,428,800 states, reduced by the 16 symmetries that keep the U/D axis; one bit per reduced state
//! and per depth.  Memory: three bitsets of `nclass * 60480` bytes (~167 MB each): `vis` (seen so far),
//! `cur` (the current depth) and `nxt` (the next depth).  Each depth's frontier is written to
//! `<outdir>/depth_XX.bits`.  The reduced index and the file formats are described in `reduced.rs`.

use crate::bitset::AtomicBitset;
use crate::core::{Core, NC, NE, NMOVES};
use crate::reduced::{CornerClasses, SliceIndex, ROW};
use rayon::prelude::*;
use std::fs::{self, File};
use std::io::{self, Write};
use std::path::Path;

/// Number of states of the DR group: 8! * 8! * 4! / 2.
const GROUP_ORDER: u64 = 19_508_428_800;

pub fn run(outdir: &Path) -> io::Result<i32> {
    fs::create_dir_all(outdir)?;
    let core = Core::new();
    let classes = CornerClasses::new(&core);
    for c in 0..NC {
        if core.csym[classes.csymto[c] as usize][c] as usize
            != classes.crep[classes.cclass[c] as usize]
        {
            eprintln!("sym table broken");
            return Ok(1);
        }
    }
    let nclass = classes.nclass;
    let crep = &classes.crep;
    let stab = classes.stabilisers(&core);
    let slice = SliceIndex::new(&core);

    let nbits = nclass * ROW;
    let nwords = nbits.div_ceil(64);
    eprintln!(
        "corner symmetry classes: {} ; reduced states: {} ; bitset {:.1} MB",
        nclass,
        nbits,
        (nwords * 8) as f64 / 1e6
    );
    let vis = AtomicBitset::new(nbits);
    let mut cur = AtomicBitset::new(nbits);
    let mut nxt = AtomicBitset::new(nbits);

    // per class: for each move, target class and the symmetry bringing the moved corner perm to its representative
    let mut mcl = vec![[0usize; NMOVES]; nclass];
    let mut msy = vec![[0usize; NMOVES]; nclass];
    for k in 0..nclass {
        for m in 0..NMOVES {
            let c2 = core.cmove[m][crep[k]] as usize;
            mcl[k][m] = classes.cclass[c2] as usize;
            msy[k][m] = classes.csymto[c2] as usize;
        }
    }

    {
        // depth 0: the solved state (class of identity, e = 0, s = 0)
        let i0 = classes.cclass[0] as usize * ROW + slice.to12[0] as usize;
        vis.bits().set(i0);
        cur.bits().set(i0);
    }
    let mut log = File::create(outdir.join("counts.txt"))?;
    let mut total: u64 = 0;
    for depth in 0.. {
        // count + save current frontier
        let (cnt, bits) = (0..nclass)
            .into_par_iter()
            .map(|k| {
                let b = cur.count_ones(k * (ROW / 64), ROW / 64);
                (b * (16 / stab[k].len() as u64), b)
            })
            .reduce(|| (0, 0), |x, y| (x.0 + y.0, x.1 + y.1));
        if cnt == 0 {
            break;
        }
        total += cnt;
        eprintln!(
            "depth {:2}: {} states ({} reduced) total {}",
            depth, cnt, bits, total
        );
        writeln!(log, "{} {} {}", depth, cnt, bits)?;
        cur.write_to(&outdir.join(format!("depth_{:02}.bits", depth)))?;

        // expand: every state of the frontier, every move.  Threads only add bits to `vis` and `nxt`.
        // A neighbour may be tested by two threads before either marks it; both then set the same bits,
        // so the frontier does not depend on the scheduling.
        (0..nclass).into_par_iter().with_max_len(4).for_each(|k| {
            // Plain local views / copies of everything the inner loops read, so that the compiler can keep
            // the table addresses in registers across the atomic updates.
            let (vis, cur, nxt) = (vis.bits(), cur.bits(), nxt.bits());
            let (emove, esym): (&[[u16; NE]], &[[u16; NE]]) = (&core.emove, &core.esym);
            let (smove, ssym) = (core.smove, core.ssym);
            let (to12, from12) = (slice.to12, slice.from12);
            let (mcl_k, msy_k) = (mcl[k], msy[k]);
            let stab: &[Vec<u8>] = &stab;
            let epar: &[u8] = &core.epar;
            let cpar = core.cpar[crep[k]];
            let base = k * ROW;
            for e in 0..NE {
                // the (up to 12) frontier states with corner class k and edge coordinate e
                let w = cur.get12(base + e * 12);
                if w == 0 {
                    continue;
                }
                let par = (cpar ^ epar[e]) as usize;
                for m in 0..NMOVES {
                    // apply move m, then conjugate by `sym` so that the corners are a class representative again
                    let (k2, sym) = (mcl_k[m], msy_k[m]);
                    let e2 = esym[sym][emove[m][e] as usize] as usize;
                    let group = k2 * ROW + e2 * 12; // first bit of the 12 states (k2, e2, *)
                    let mut left = w;
                    while left != 0 {
                        let s12 = left.trailing_zeros() as usize;
                        left &= left - 1;
                        let s = from12[par][s12] as usize;
                        let s2 = ssym[sym][smove[m][s] as usize] as usize;
                        let j = group + to12[s2] as usize;
                        if vis.get(j) {
                            continue;
                        }
                        vis.set(j);
                        nxt.set(j);
                        // mark every image under the stabiliser of the representative (stab[k2][0] is the identity)
                        for &t in &stab[k2][1..] {
                            let t = t as usize;
                            let j2 = k2 * ROW
                                + esym[t][e2] as usize * 12
                                + to12[ssym[t][s2] as usize] as usize;
                            vis.set(j2);
                            nxt.set(j2);
                        }
                    }
                }
            }
        });
        std::mem::swap(&mut cur, &mut nxt);
        nxt.clear();
    }
    eprintln!("total {} (expected {})", total, GROUP_ORDER);
    writeln!(log, "total {}", total)?;

    // save the class tables so later passes agree on the indexing
    let mut bytes = Vec::with_capacity(4 + 5 * nclass);
    bytes.extend_from_slice(&(nclass as i32).to_le_bytes());
    for &c in crep {
        bytes.extend_from_slice(&(c as i32).to_le_bytes());
    }
    bytes.extend(stab.iter().map(|s| s.len() as u8));
    fs::write(outdir.join("classes.bin"), bytes)?;
    Ok(if total == GROUP_ORDER { 0 } else { 2 })
}

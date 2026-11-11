//! `drtools census <bfsdir>` — one pass over the exact distance data: histogram of optimal finish length by
//! (Mallard subset, 4a/4b letter on the normal side, HTR length normal, HTR length inverse, corner-only
//! length, E-slice parity).  (Port of `dragg.c`.)
//!
//! Output: CSV with one line per non-empty cell.  Weights are 16/|stabiliser| so that counts are numbers
//! of DR states.

use crate::class::{corner_only_lengths, Classes};
use crate::core::{Core, NE};
use crate::par;
use crate::reduced::{ExactData, RowDepths, MAXD};
use std::io::{self, BufWriter, Write};
use std::path::Path;

/// Sizes of the histogram axes for the HTR lengths (0..=13) and the corner-only length (0..=13).
const NH: usize = 14;
const NL: usize = 14;

pub fn run(bfsdir: &Path) -> io::Result<i32> {
    let core = Core::new();
    let cls = Classes::new(&core);
    let data = ExactData::open(bfsdir);
    let clen = corner_only_lengths(&core);

    // histogram cell = (((((subset * 2 + ab) * NH + hN) * NH + hI) * NL + L) * 2 + Epar) * MAXD + depth
    let keys = 48 * 2 * NH * NH * NL * 2 * MAXD;
    let parts = par::for_each_with_local(
        data.nclass,
        8,
        || (vec![0u64; keys], RowDepths::new()),
        |(h, row), k| {
            let dep = row.load(&data, k);
            let c = data.crep[k];
            let w = (16 / data.nstab[k]) as u64;
            let a = cls.ccos[c] as usize; // HTR corner coset of the state
            let ai = cls.ccos[core.cinv[c] as usize] as usize; // ... and of its inverse
            let len = clen[c] as usize;
            let ab = cls.cc_shape[a] as usize;
            for e in 0..NE {
                let b = cls.epat[e] as usize;
                let bi = cls.epat[core.einv[e] as usize] as usize;
                let (hn, hi) = (cls.htr_dist[a][b] as usize, cls.htr_dist[ai][bi] as usize);
                let sub = cls.sub48[a][b] as usize;
                let par = (core.cpar[c] ^ core.epar[e]) as usize;
                let base = (((((sub * 2 + ab) * NH + hn) * NH + hi) * NL + len) * 2 + par) * MAXD;
                for s12 in 0..12 {
                    let d = dep[e * 12 + s12];
                    if d == 0xFF {
                        fatal!("unvisited state class {} e {} s {}", k, e, s12);
                    }
                    h[base + d as usize] += w;
                }
            }
        },
    );
    let h = par::sum_histograms(parts.into_iter().map(|(h, _)| h));

    let mut out = BufWriter::new(io::stdout().lock());
    writeln!(out, "subset,ab,hN,hI,L,Epar,depth,count")?;
    let mut total: u64 = 0;
    for (i, &count) in h.iter().enumerate() {
        if count == 0 {
            continue;
        }
        // take the cell number apart again
        let mut x = i;
        let mut split = |radix: usize| {
            let digit = x % radix;
            x /= radix;
            digit
        };
        let (d, par, len, hi, hn, ab) = (
            split(MAXD),
            split(2),
            split(NL),
            split(NH),
            split(NH),
            split(2),
        );
        let sub = x;
        let letter = if cls.sub48_nc[sub] == 4 {
            if ab != 0 {
                'b'
            } else {
                'a'
            }
        } else {
            '-'
        };
        writeln!(
            out,
            "{},{},{},{},{},{},{},{}",
            cls.sub48_name[sub], letter, hn, hi, len, par, d, count
        )?;
        total += count;
    }
    out.flush()?;
    eprintln!("total {}", total);
    Ok(0)
}

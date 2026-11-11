//! `drtools census2 <bfsdir>` — joint histogram of the exact finish length with the visible-feature lower
//! bounds, per Mallard subset.  (Port of `dragg2.c`.)
//!
//! Columns: subset, hmax = max(HTR length normal, inverse), bFn / bFi = KF bound on the normal / inverse
//! state, b0 = max(K0 bound normal, inverse), depth, count.

use crate::class::Classes;
use crate::core::{Core, NE};
use crate::par;
use crate::quot::{Quot, E630};
use crate::reduced::{ExactData, RowDepths, MAXD};
use std::io::{self, BufWriter, Write};
use std::path::Path;

/// Size of the histogram axes for the bounds (0..=16).
const NB: usize = 17;
/// Size of the histogram axis for hmax (0..=13).
const NHM: usize = 14;

pub fn run(bfsdir: &Path) -> io::Result<i32> {
    let core = Core::new();
    let cls = Classes::new(&core);
    let e630 = E630::new(&core, &cls);
    let qf = Quot::new(&core, &cls, &e630, true);
    let q0 = Quot::new(&core, &cls, &e630, false);
    let data = ExactData::open(bfsdir);

    // histogram cell = ((((subset * NHM + hmax) * NB + bFn) * NB + bFi) * NB + b0) * MAXD + depth
    let keys = 48 * NHM * NB * NB * NB * MAXD;
    struct Local {
        h: Vec<u64>,
        viol: u64,
        row: RowDepths,
    }
    let parts = par::for_each_with_local(
        data.nclass,
        8,
        || Local {
            h: vec![0u64; keys],
            viol: 0,
            row: RowDepths::new(),
        },
        |local, k| {
            let dep = local.row.load(&data, k);
            let c = data.crep[k];
            let ci = core.cinv[c] as usize;
            let w = (16 / data.nstab[k]) as u64;
            let (a, ai) = (cls.ccos[c] as usize, cls.ccos[ci] as usize);
            for e in 0..NE {
                let ei = core.einv[e] as usize;
                let (b, bi) = (cls.epat[e] as usize, cls.epat[ei] as usize);
                let hm = cls.htr_dist[a][b].max(cls.htr_dist[ai][bi]) as usize;
                let sub = cls.sub48[a][b] as usize;
                let par = (core.cpar[c] ^ core.epar[e]) as usize;
                let (ee, eei) = (e630.cls[e] as usize, e630.cls[ei] as usize);
                let f_n = qf.t[Quot::idx(qf.corners.ccls[c] as usize, ee, par)] as usize;
                let f_i = qf.t[Quot::idx(qf.corners.ccls[ci] as usize, eei, par)] as usize;
                let z_n = q0.t[Quot::idx(q0.corners.ccls[c] as usize, ee, par)] as usize;
                let z_i = q0.t[Quot::idx(q0.corners.ccls[ci] as usize, eei, par)] as usize;
                let z = z_n.max(z_i);
                let base = ((((sub * NHM + hm) * NB + f_n) * NB + f_i) * NB + z) * MAXD;
                for s12 in 0..12 {
                    let d = dep[e * 12 + s12] as usize;
                    if d >= MAXD {
                        fatal!("unvisited state class {} e {} s {}", k, e, s12);
                    }
                    if d < z || d < f_n || d < f_i || d < hm {
                        local.viol += 1;
                    }
                    local.h[base + d] += w;
                }
            }
        },
    );
    let viol: u64 = parts.iter().map(|local| local.viol).sum();
    let h = par::sum_histograms(parts.into_iter().map(|local| local.h));

    let mut out = BufWriter::new(io::stdout().lock());
    writeln!(out, "subset,hmax,bFn,bFi,b0,depth,count")?;
    for (i, &count) in h.iter().enumerate() {
        if count == 0 {
            continue;
        }
        let mut x = i;
        let mut split = |radix: usize| {
            let digit = x % radix;
            x /= radix;
            digit
        };
        let (d, z, f_i, f_n, hm) = (split(MAXD), split(NB), split(NB), split(NB), split(NHM));
        writeln!(
            out,
            "{},{},{},{},{},{},{}",
            cls.sub48_name[x], hm, f_n, f_i, z, d, count
        )?;
    }
    out.flush()?;
    eprintln!(
        "states where a claimed lower bound exceeds the true optimum: {} (must be 0)",
        viol
    );
    Ok((viol != 0) as i32)
}

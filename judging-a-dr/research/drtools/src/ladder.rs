//! `drtools ladder <bfsdir> <tabledir>` — a ladder of "visible feature" lower bounds for DR finishes, from
//! coarse to fine, and how each compares with the exact optimum on all 19,508,428,800 DR states.
//! (Port of `drlattice.c`; the rungs themselves are described in `spec.rs`.)
//!
//! Writes one table `T_<name>.u8` per rung into `<tabledir>` and prints a CSV histogram
//! `spec,sides,subset,bound,depth,count` where `sides` = 1 uses the bound of the state itself and
//! `sides` = 2 the larger of the bounds of the state and of its inverse.

use crate::class::{Classes, NCCOS, NEPAT};
use crate::core::{Core, NE};
use crate::par;
use crate::quot::E630;
use crate::reduced::{ExactData, RowDepths, MAXD};
use crate::spec::Ladder;
use std::fs;
use std::io::{self, BufWriter, Write};
use std::path::Path;

pub fn run(bfsdir: &Path, tabdir: &Path) -> io::Result<i32> {
    fs::create_dir_all(tabdir)?;
    let core = Core::new();
    let cls = Classes::new(&core);
    let e630 = E630::new(&core, &cls);
    let mut ladder = Ladder::new(&core, &cls, &e630);

    // ---- the tables: BFS of every rung, a summary line on stderr, the table file
    for spec in &mut ladder.specs {
        spec.compute_table();
        let mut hist = [0u64; 256];
        for &v in &spec.t {
            hist[v as usize] += 1;
        }
        let reached: u64 = hist[..24].iter().sum(); // 0xFF = index that no state maps to
        let max = (0..24).rev().find(|&v| hist[v] != 0).unwrap_or(0);
        eprint!(
            "{:<9} {:>10} classes (of {} indexed), max {:>2} :",
            spec.name, reached, spec.n, max
        );
        for count in &hist[..=max] {
            eprint!(" {}", count);
        }
        eprintln!();
        fs::write(tabdir.join(format!("T_{}.u8", spec.name)), &spec.t)?;
    }
    let specs = &ladder.specs;
    // sanity: rung "htr" must equal the HTR distance table
    for a in 0..NCCOS {
        for b in 0..NEPAT {
            if specs[0].t[specs[0].idx(a, b, 0)] != cls.htr_dist[a][b] {
                eprintln!("htr rung mismatch");
                return Ok(1);
            }
        }
    }

    // ---- aggregate against exact distances
    let data = ExactData::open(bfsdir);
    // histogram cell = ((((spec * 2 + one-sided(0)/two-sided(1)) * 48 + subset) * MAXD + bound) * MAXD + depth
    let keys = specs.len() * 2 * 48 * MAXD * MAXD;
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
            let a = cls.ccos[c] as usize;
            for e in 0..NE {
                let ei = core.einv[e] as usize;
                let sub = cls.sub48[a][cls.epat[e] as usize] as usize;
                let par = (core.cpar[c] ^ core.epar[e]) as usize;
                // the 12 states (c, e, *) share every bound: count them by depth first
                let mut cnt = [0u64; MAXD];
                for (s12, &d) in dep[e * 12..e * 12 + 12].iter().enumerate() {
                    if d as usize >= MAXD {
                        fatal!("unvisited state class {} e {} s {}", k, e, s12);
                    }
                    cnt[d as usize] += 1;
                }
                for (i, spec) in specs.iter().enumerate() {
                    let bn = spec.t[spec.class_of(c, e, par)]; // bound from the state
                    let bi = spec.t[spec.class_of(ci, ei, par)]; // bound from its inverse
                    if bn == 0xFF || bi == 0xFF {
                        fatal!("reached an unvisited class in {}", spec.name);
                    }
                    let b2 = bn.max(bi) as usize;
                    let b1k = (((i * 2) * 48 + sub) * MAXD + bn as usize) * MAXD;
                    let b2k = (((i * 2 + 1) * 48 + sub) * MAXD + b2) * MAXD;
                    for d in 0..MAXD {
                        if cnt[d] != 0 {
                            if d < b2 {
                                local.viol += 1;
                            }
                            local.h[b1k + d] += cnt[d] * w;
                            local.h[b2k + d] += cnt[d] * w;
                        }
                    }
                }
            }
        },
    );
    let viol: u64 = parts.iter().map(|local| local.viol).sum();
    let h = par::sum_histograms(parts.into_iter().map(|local| local.h));

    let mut out = BufWriter::new(io::stdout().lock());
    writeln!(out, "spec,sides,subset,bound,depth,count")?;
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
        let (d, b, sub, two) = (split(MAXD), split(MAXD), split(48), split(2));
        writeln!(
            out,
            "{},{},{},{},{},{}",
            specs[x].name,
            two + 1,
            cls.sub48_name[sub],
            b,
            d,
            count
        )?;
    }
    out.flush()?;
    eprintln!("bound violations: {} (must be 0)", viol);
    Ok((viol != 0) as i32)
}

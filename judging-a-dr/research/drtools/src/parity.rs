//! `drtools parity <tabledir>` — the "E-slice parity rule": L = optimal corner length, Lp = optimal corner
//! length among corner solutions whose number of side half turns has the parity of the E-slice
//! permutation.  Distribution of Lp - L per corner subset.  (Port of `drparity.c`.)

use crate::class::{Classes, NSUBSET, SUBSET_NAME};
use crate::core::{Core, NC};
use crate::quot::E630;
use crate::spec::Ladder;
use std::io::{self, BufWriter, Write};
use std::path::Path;

pub fn run(tabdir: &Path) -> io::Result<i32> {
    let core = Core::new();
    let cls = Classes::new(&core);
    let e630 = E630::new(&core, &cls);
    let mut ladder = Ladder::new(&core, &cls, &e630);
    let (ia, ib) = (ladder.index_of("c"), ladder.index_of("c+p"));
    ladder.specs[ia].load_table(tabdir);
    ladder.specs[ib].load_table(tabdir);
    let (a, b) = (&ladder.specs[ia], &ladder.specs[ib]);
    let subset = |c: usize| cls.cc_subset[cls.ccos[c] as usize] as usize;
    let mut out = BufWriter::new(io::stdout().lock());

    let mut h = [[0u64; 8]; NSUBSET];
    for c in 0..NC {
        for p in 0..2 {
            let (len, len_p) = (a.t[a.idx(c, 0, 0)], b.t[b.idx(c, 0, p)]);
            h[subset(c)][(len_p - len) as usize] += 1;
        }
    }
    writeln!(
        out,
        "corner subset: share of (corner state, E parity) pairs with Lp-L = 0,1,2,3,...   [wrong-parity cost: Lp(other parity) - L]"
    )?;
    for s in 0..NSUBSET {
        let total: u64 = h[s].iter().sum();
        write!(out, "  {}:", SUBSET_NAME[s])?;
        for k in 0..8 {
            if h[s][k] != 0 {
                write!(
                    out,
                    "  +{}: {:.1}%",
                    k,
                    100.0 * h[s][k] as f64 / total as f64
                )?;
            }
        }
        writeln!(out)?;
    }

    // for each corner state: which parity is the cheap one, and the extra cost of the other
    let mut d = [[0u64; 8]; NSUBSET];
    for c in 0..NC {
        let (even, odd) = (b.t[b.idx(c, 0, 0)], b.t[b.idx(c, 0, 1)]);
        d[subset(c)][even.abs_diff(odd) as usize] += 1;
    }
    writeln!(
        out,
        "corner subset: |Lp(even) - Lp(odd)| distribution over corner states"
    )?;
    for s in 0..NSUBSET {
        let total: u64 = d[s].iter().sum();
        write!(out, "  {}:", SUBSET_NAME[s])?;
        for k in 0..8 {
            if d[s][k] != 0 {
                write!(
                    out,
                    "  {}: {:.1}%",
                    k,
                    100.0 * d[s][k] as f64 / total as f64
                )?;
            }
        }
        writeln!(out)?;
    }
    out.flush()?;
    Ok(0)
}

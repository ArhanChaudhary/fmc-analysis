//! `drtools sharp <bfsdir> <tabledir> <spec>...` — computational check of sharpness: for every class of a
//! rung, the smallest exact optimum among the states of the class equals the table value ("the bound is
//! the best case of what you see").  (Port of `drsharp.c`.)

use crate::class::Classes;
use crate::core::{Core, NE, NSYM};
use crate::quot::E630;
use crate::reduced::{ExactData, RowDepths};
use crate::spec::{CornerView, Ladder};
use std::io::{self, Write};
use std::path::Path;

pub fn run(bfsdir: &Path, tabdir: &Path, names: &[String]) -> io::Result<i32> {
    let core = Core::new();
    let cls = Classes::new(&core);
    let e630 = E630::new(&core, &cls);
    let mut ladder = Ladder::new(&core, &cls, &e630);
    let data = ExactData::open(bfsdir);
    let mut row = RowDepths::new();
    let mut out = io::stdout().lock();
    for name in names {
        let index = ladder.index_of(name);
        let spec = &mut ladder.specs[index];
        if spec.t.is_empty() {
            spec.load_table(tabdir);
        }
        // mn[class] = smallest exact optimum met in the class
        let mut mn = vec![0xFFu8; spec.n];
        // If classes mix several corner permutations, visit all 16 symmetric images of every reduced state;
        // with exact corners only the classes of the class representatives are met.
        let nsym = if spec.cm != CornerView::Exact {
            NSYM
        } else {
            1
        };
        for k in 0..data.nclass {
            let dep = row.load(&data, k);
            let c = data.crep[k];
            for e in 0..NE {
                let par = (core.cpar[c] ^ core.epar[e]) as usize;
                let dm = dep[e * 12..e * 12 + 12]
                    .iter()
                    .copied()
                    .min()
                    .unwrap_or(0xFF);
                for sym in 0..nsym {
                    let i =
                        spec.class_of(core.csym[sym][c] as usize, core.esym[sym][e] as usize, par);
                    if dm < mn[i] {
                        mn[i] = dm;
                    }
                }
            }
        }
        let (mut seen, mut equal, mut differ) = (0usize, 0usize, 0usize);
        for (i, &m) in mn.iter().enumerate() {
            if m != 0xFF {
                seen += 1;
                if m == spec.t[i] {
                    equal += 1;
                } else {
                    differ += 1;
                }
            }
        }
        writeln!(
            out,
            "{:<9} classes met: {} ; best case of class == table value: {} ; differ: {}",
            spec.name, seen, equal, differ
        )?;
        out.flush()?;
    }
    Ok(0)
}

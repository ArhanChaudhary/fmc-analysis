//! `drtools genlean` — print the move "source" maps (`new[p] = old[src[p]]`) for the Lean model, straight
//! from this model.  (Port of `genlean.c`.)

use crate::core::{St, MOVE_NAME, NMOVES};
use std::io::{self, Write};

pub fn run() -> io::Result<i32> {
    let mut out = io::stdout().lock();
    for m in 0..NMOVES {
        let g = St::ID.apply_move(m); // g.c[pos] = piece now at pos = position it came from
        write!(out, "{:<3} C:", MOVE_NAME[m])?;
        for p in g.c {
            write!(out, " {}", p)?;
        }
        write!(out, "  E:")?;
        for p in g.e {
            write!(out, " {}", p)?;
        }
        write!(out, "  S:")?;
        for p in g.s {
            write!(out, " {}", p)?;
        }
        writeln!(out)?;
    }
    Ok(0)
}

//! `drtools query <bfsdir> <tabledir>` — look up one or more DR states: subset, HTR lengths, every lower
//! bound of the ladder (normal and inverse side), and the exact optimal DR finish (from the full table on
//! disk).  (Port of `drq.c`.)
//!
//! Input, one state per line on stdin:
//!
//! ```text
//!   20 numbers  c0..c7 e0..e7 s0..s3     (piece at each position, see core.rs)
//!   or a sequence of DR moves (applied to the solved cube), e.g.  U R2 U' F2 ...
//! ```
//!
//! Output: one line of `key=value` pairs per state (or `error=...`).  For every rung the pair is
//! `name=<bound of the state>/<bound of its inverse>`.  If the environment variable `DRQ_NOEXACT` is set,
//! the exact lookup is skipped and `exact=-1` is printed.

use crate::class::{Classes, SUBSET_NAME};
use crate::core::{parse_moves, rank_perm, Core, St};
use crate::quot::E630;
use crate::reduced::{exact_depth, open_depth_files, CornerClasses, SliceIndex, ROW};
use crate::spec::Ladder;
use crate::text::{is_c_space, read_line_like_fgets, strtol};
use std::io::{self, Write};
use std::path::Path;

/// The C tool read lines with `fgets` into a buffer of this size and kept at most this many moves.
const LINE_BUFFER: usize = 4096;
const MAX_MOVES: usize = 512;

/// Is `p` a permutation of `0..p.len()`?
fn is_permutation(p: &[u8]) -> bool {
    let mut seen = [false; 8];
    p.iter()
        .all(|&x| (x as usize) < p.len() && !std::mem::replace(&mut seen[x as usize], true))
}

pub fn run(bfsdir: &Path, tabdir: &Path) -> io::Result<i32> {
    let core = Core::new();
    let cls = Classes::new(&core);
    let e630 = E630::new(&core, &cls);
    let mut ladder = Ladder::new(&core, &cls, &e630);
    ladder.load_all(tabdir);
    let corner_classes = CornerClasses::new(&core);
    let slice = SliceIndex::new(&core);
    let depth_files = open_depth_files(bfsdir);
    let clen = &ladder.specs[ladder.index_of("c")].t; // rung "c": corner-only optimal length (40320 entries)
    let kf = &ladder.specs[ladder.index_of("KF")];
    let no_exact = std::env::var_os("DRQ_NOEXACT").is_some();

    let mut input = io::stdin().lock();
    let mut out = io::stdout().lock();
    let mut line = Vec::new();
    while read_line_like_fgets(&mut input, LINE_BUFFER, &mut line)? {
        let Some(start) = line.iter().position(|&b| !is_c_space(b)) else {
            continue; // blank line
        };
        let g = if line[start].is_ascii_digit() {
            // 20 numbers.  Like the C tool (which stored them into bytes), numbers are taken modulo 256.
            let mut nums: Vec<u8> = Vec::with_capacity(20);
            let mut rest = &line[start..];
            while nums.len() < 20 {
                let Some((value, used)) = strtol(rest) else {
                    break;
                };
                nums.push(value as u8);
                rest = &rest[used..];
            }
            if nums.len() != 20 {
                writeln!(out, "error=need 20 numbers")?;
                out.flush()?;
                continue;
            }
            let mut g = St::ID;
            g.c.copy_from_slice(&nums[0..8]);
            g.e.copy_from_slice(&nums[8..16]);
            g.s.copy_from_slice(&nums[16..20]);
            // (The C tool did not check this and ran into undefined behaviour on such input.)
            if !(is_permutation(&g.c) && is_permutation(&g.e) && is_permutation(&g.s)) {
                writeln!(out, "error=not a permutation")?;
                out.flush()?;
                continue;
            }
            g
        } else {
            match parse_moves(&line, MAX_MOVES) {
                Some(moves) => moves.iter().fold(St::ID, |g, &m| g.apply_move(m)),
                None => {
                    writeln!(out, "error=not a DR move sequence")?;
                    out.flush()?;
                    continue;
                }
            }
        };

        let (c, e, s) = (rank_perm(&g.c), rank_perm(&g.e), rank_perm(&g.s));
        let gi = g.inv();
        let (ci, ei) = (rank_perm(&gi.c), rank_perm(&gi.e));
        let par = core.spar[s] as usize; // parity of the E-slice permutation
        if (core.cpar[c] ^ core.epar[e]) as usize != par {
            writeln!(out, "error=parity: not a reachable DR state")?;
            out.flush()?;
            continue;
        }
        // HTR coset of the state (a, b) and of its inverse (ai, bi)
        let (a, b) = (cls.ccos[c] as usize, cls.epat[e] as usize);
        let (ai, bi) = (cls.ccos[ci] as usize, cls.epat[ei] as usize);
        write!(
            out,
            "subset={} corners_normal={} corners_inverse={} bad_corners={} bad_edges={} qt_corners={} qt_min={} \
             E_parity={} htr_normal={} htr_inverse={} corner_len={}",
            cls.sub48_name[cls.sub48[a][b] as usize],
            SUBSET_NAME[cls.cc_subset[a] as usize],
            SUBSET_NAME[cls.cc_subset[ai] as usize],
            cls.cc_nbad[a],
            cls.ep_nbad[b],
            cls.cc_qt[a],
            cls.qt_full[a][b],
            if par != 0 { "odd" } else { "even" },
            cls.htr_dist[a][b],
            cls.htr_dist[ai][bi],
            clen[c]
        )?;
        let mut best = 0;
        for spec in &ladder.specs {
            let bn = spec.t[spec.class_of(c, e, par)];
            let bi = spec.t[spec.class_of(ci, ei, par)];
            write!(out, " {}={}/{}", spec.name, bn, bi)?;
            best = best.max(bn).max(bi);
        }
        write!(out, " kfclass={}", kf.class_of(c, e, par))?;
        let exact = if no_exact {
            None
        } else {
            // conjugate so that the corners become their class representative, then look the bit up
            let (k, sym) = (
                corner_classes.cclass[c] as usize,
                corner_classes.csymto[c] as usize,
            );
            let bit = k * ROW
                + core.esym[sym][e] as usize * 12
                + slice.to12[core.ssym[sym][s] as usize] as usize;
            exact_depth(&depth_files, bit)
        };
        writeln!(
            out,
            " best_bound={} exact={}",
            best,
            exact.map_or(-1, |d| d as i64)
        )?;
        out.flush()?;
    }
    Ok(0)
}

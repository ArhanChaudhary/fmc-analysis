//! `drtools selftest [listing]` — self-checks of the model against numbers stated in the Discord knowledge
//! base (port of `t_class.c`), then the KF / K0 tables and a check of their half-turn-only restriction
//! against FakeMMAP's 216-case BFS listing (port of `t_quot.c`).  Prints what the two C programs print,
//! one after the other.

use crate::class::{corner_only_lengths, Classes, NCCOS, NEPAT, NSUBSET, SUBSET_NAME};
use crate::core::{parse_moves, rank_perm, Core, St, NC, NSYM};
use crate::quot::{Quot, E630};
use crate::text::{find, read_line_like_fgets, strtol};
use std::fs::File;
use std::io::{self, BufReader, BufWriter, Write};
use std::path::Path;

/// FakeMMAP's listing: lines `<case> ... parity: <n> Example scramble: <half turns>`.
pub const DEFAULT_LISTING: &str = "/data/fmc/assets/attachments/1546077758189477989_0_message.txt";

pub fn run(listing: &Path) -> io::Result<i32> {
    let core = Core::new();
    let cls = Classes::new(&core);
    let mut out = BufWriter::new(io::stdout().lock());
    if !class_checks(&core, &cls, &mut out)? {
        out.flush()?;
        return Ok(1);
    }
    quotient_checks(&core, &cls, listing, &mut out)?;
    out.flush()?;
    Ok(0)
}

/// The checks of `t_class.c`.  Returns `false` if a symmetry check fails.
fn class_checks(core: &Core, cls: &Classes, out: &mut impl Write) -> io::Result<bool> {
    let subset_of = |c: usize| cls.cc_subset[cls.ccos[c] as usize] as usize;

    // 1. subset sizes in units of corner cosets; expected from Joba's subsets_without_edges.txt (T6677):
    //    0c0 2, 4a1 12, 4a2 12, 4b2 48, 0c3 6, 2c3 64, 4c3 48, 0c4 4, 2c4 96, 4c4 48, 2c5 32, 4c5 48  (of 420)
    let mut cnt = [0u32; NSUBSET];
    for i in 0..NCCOS {
        cnt[cls.cc_subset[i] as usize] += 1;
    }
    writeln!(out, "corner subset : cosets (of 420)")?;
    for i in 0..NSUBSET {
        writeln!(out, "  {} {}", SUBSET_NAME[i], cnt[i])?;
    }
    let nsub48 = cls.sub48_name.len();
    writeln!(out, "Mallard-style subsets found: {} (expected 48)", nsub48)?;
    {
        let mut n = vec![0u32; nsub48];
        for a in 0..NCCOS {
            for b in 0..NEPAT {
                n[cls.sub48[a][b] as usize] += 1;
            }
        }
        for k in 0..nsub48 {
            let share = 100.0 * n[k] as f64 / 29400.0;
            let end = if k % 3 == 2 { "\n" } else { "" }; // three per line
            write!(
                out,
                "  {:<7} cosets {:>5}  ({:.4}% of DR states){}",
                cls.sub48_name[k], n[k], share, end
            )?;
        }
        writeln!(out)?;
    }

    // 2. quarter-turn class sizes; expected (Oskar, T4615): 1/210, 1/35, 1/7, 59/210, 37/105, 4/21
    let mut q = [0u32; 8];
    for i in 0..NCCOS {
        q[cls.cc_qt[i] as usize] += 1;
    }
    write!(out, "qt class sizes /420:")?;
    for k in 0..8 {
        write!(out, " {}", q[k])?;
    }
    writeln!(out, "   expected 2 12 60 118 148 80")?;

    // 3. bad edges
    let mut be = [0u32; 9];
    for i in 0..NEPAT {
        be[cls.ep_nbad[i] as usize] += 1;
    }
    writeln!(
        out,
        "edge patterns by #bad edges: 0:{} 2:{} 4:{} 6:{} 8:{}",
        be[0], be[2], be[4], be[6], be[8]
    )?;

    // 4. HTR length distribution over the 29,400 cosets
    let mut hd = [0u32; 20];
    let mut hmax = 0usize;
    for a in 0..NCCOS {
        for b in 0..NEPAT {
            let d = cls.htr_dist[a][b] as usize;
            hd[d] += 1;
            hmax = hmax.max(d);
        }
    }
    write!(out, "DR->HTR optimal length over 29400 cosets:")?;
    for k in 0..=hmax {
        write!(out, " {}:{}", k, hd[k])?;
    }
    writeln!(out)?;

    // 5. inverse behaviour of subsets: which subset does the inverse of an element land in?
    writeln!(out, "subset -> subsets of inverses (count of elements)")?;
    for si in 0..NSUBSET {
        let mut inv = [0u64; NSUBSET];
        for c in 0..NC {
            if subset_of(c) == si {
                inv[subset_of(core.cinv[c] as usize)] += 1;
            }
        }
        write!(out, "  {} ->", SUBSET_NAME[si])?;
        for j in 0..NSUBSET {
            if inv[j] != 0 {
                write!(out, " {}:{}", SUBSET_NAME[j], inv[j])?;
            }
        }
        writeln!(out)?;
    }

    // 6. optimal corner-solution length in DR moves (corners only, 40320 states)
    {
        let d = corner_only_lengths(core);
        let mut h = [0u32; 20];
        let mut mx = 0usize;
        for c in 0..NC {
            h[d[c] as usize] += 1;
            mx = mx.max(d[c] as usize);
        }
        write!(
            out,
            "corner-only optimal length (40320 corner states, DR moves):"
        )?;
        for k in 0..=mx {
            write!(out, " {}:{}", k, h[k])?;
        }
        writeln!(out)?;
        let (mut mxs, mut mns) = ([0u8; NSUBSET], [99u8; NSUBSET]);
        for c in 0..NC {
            let s = subset_of(c);
            mxs[s] = mxs[s].max(d[c]);
            mns[s] = mns[s].min(d[c]);
        }
        write!(out, "corner length range per subset:")?;
        for i in 0..NSUBSET {
            write!(out, " {} {}-{}", SUBSET_NAME[i], mns[i], mxs[i])?;
        }
        writeln!(out)?;
    }

    // 7. symmetry sanity: subset labels and HTR distance are invariant under the 16 symmetries
    //    (c is used both as a corner and as an edge coordinate)
    for c in (0..NC).step_by(7) {
        for sym in 0..NSYM {
            let (c2, e2) = (core.csym[sym][c] as usize, core.esym[sym][c] as usize);
            if subset_of(c2) != subset_of(c) {
                writeln!(out, "subset not symmetric!")?;
                return Ok(false);
            }
            let htr = |c: usize, e: usize| cls.htr_dist[cls.ccos[c] as usize][cls.epat[e] as usize];
            if htr(c2, e2) != htr(c, c) {
                writeln!(out, "htr dist not symmetric!")?;
                return Ok(false);
            }
        }
    }
    writeln!(out, "symmetry invariance of labels: ok")?;
    Ok(true)
}

/// The checks of `t_quot.c`.
fn quotient_checks(
    core: &Core,
    cls: &Classes,
    listing: &Path,
    out: &mut impl Write,
) -> io::Result<()> {
    let e630 = E630::new(core, cls);
    let qf = Quot::new(core, cls, &e630, true);
    let q0 = Quot::new(core, cls, &e630, false);
    for (name, q) in [("KF", &qf), ("K0", &q0)] {
        let (mut h, mut hh) = ([0u64; 256], [0u64; 256]);
        for i in 0..q.len() {
            h[q.t[i] as usize] += 1;
            hh[q.th[i] as usize] += 1;
        }
        let mx = q.t.iter().copied().max().unwrap_or(0) as usize;
        write!(
            out,
            "{}: {} classes; DR-move distance distribution:",
            name,
            q.len()
        )?;
        for k in 0..=mx {
            write!(out, " {}:{}", k, h[k])?;
        }
        writeln!(out)?;
        // classes reachable with half turns only (0xFF = not reachable)
        write!(
            out,
            "   half-turn-only component: {} classes:",
            q.len() as u64 - hh[0xFF]
        )?;
        for k in 0..24 {
            if hh[k] != 0 {
                write!(out, " {}:{}", k, hh[k])?;
            }
        }
        writeln!(out)?;
        // does allowing quarter turns shorten any HTR-class?
        let shorter = (0..q.len())
            .filter(|&i| q.th[i] != 0xFF && q.t[i] < q.th[i])
            .count();
        writeln!(
            out,
            "   HTR classes whose distance drops when quarter turns are allowed: {}",
            shorter
        )?;
    }

    // FakeMMAP's listing: "<case>: <n> Example scramble: <half turns>"
    let (mut n, mut ok_h, mut ok_dr, mut distinct) = (0, 0, 0, 0);
    let mut seen = vec![false; qf.len()];
    if let Ok(file) = File::open(listing) {
        let mut input = BufReader::new(file);
        let mut line = Vec::new();
        while read_line_like_fgets(&mut input, 512, &mut line)? {
            let Some(col) = find(&line, b"parity: ") else {
                continue;
            };
            let val = strtol(&line[col + 8..]).map_or(0, |(v, _)| v); // C atoi
            let Some(sc) = find(&line, b"scramble:") else {
                continue;
            };
            // (a scramble that is not a DR move sequence counts as the solved cube, as in the C program)
            let moves = parse_moves(&line[sc + 9..], 64).unwrap_or_default();
            let g = moves.iter().fold(St::ID, |g, &m| g.apply_move(m));
            let id = Quot::idx(
                qf.corners.ccls[rank_perm(&g.c)] as usize,
                e630.cls[rank_perm(&g.e)] as usize,
                core.spar[rank_perm(&g.s)] as usize,
            );
            if !seen[id] {
                seen[id] = true;
                distinct += 1;
            }
            n += 1;
            if qf.th[id] as i64 == val {
                ok_h += 1;
            } else {
                write!(out, "   differs: ")?;
                out.write_all(&line[..line.len().min(40)])?;
                writeln!(out, "  listed {}, ours (half turns) {}", val, qf.th[id])?;
            }
            if qf.t[id] as i64 == val {
                ok_dr += 1;
            }
        }
    }
    writeln!(
        out,
        "FakeMMAP listing: {} cases, {} distinct KF classes, half-turn-only distance equal in {}, DR-move distance equal in {}",
        n, distinct, ok_h, ok_dr
    )?;
    Ok(())
}

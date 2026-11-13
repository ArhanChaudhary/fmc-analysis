//! htfirst — how many half turns come before the first quarter turn of a DR finish.
//!
//! For every sampled DR state X (the 25,000 per subset x edges of `htrtools routes`, read from its
//! `states_<subset>.tsv`: columns subset, idx, c, e, s) and for each side (X and its inverse) and each budget
//! (optimal, optimal + 1), by exact search with the Lean-checked table of optimal finishes:
//!
//!   a     fewest half turns (U2 D2 R2 L2 F2 B2 all count) before the first quarter turn, over every canonical
//!         finish within the budget that has a quarter turn  (99 = no such finish)
//!   b     the same counting only the side half turns R2 L2 F2 B2 (minimised on its own)
//!   noqt  some finish within the budget has no quarter turn at all (only possible from an HTR state)
//!   q     which first moves U, U', D, D' (bits 0..3) start a finish within the budget
//!   p1    which (half turn, quarter turn) pairs start one: bit 4 * (index in U2 D2 R2 L2 F2 B2) + (index in U U' D D')
//!   e     (optimal level only) like a, over the optimal finishes with no extra quarter turn: those whose number of
//!         quarter turns is qt_full, the fewest any finish of the state can have (class.rs: fewest quarter turns of
//!         any DR sequence reaching HTR, corners and edges; half turns never change it and a quarter turn changes it
//!         by one, so such a finish is one on which every quarter turn lowers qt_full).  99 = none with a quarter turn
//!   eq    which first moves U, U', D, D' start such a finish;  hasmin: some optimal finish has no extra quarter turn
//!
//! Method: depth-first over canonical half-turn prefixes P (never the same face twice in a row, never three moves
//! in a row on one axis), kept only while depth(X P) <= budget - |P|.  After each prefix every quarter turn q that is
//! canonical after P is tried: the finish P q T exists iff depth(X P q) <= budget - |P| - 1 and T can be written
//! canonically after q.  When |P| + 1 + depth(X P q) is the optimum the whole sequence is an optimal finish and is
//! canonical for free; when it is the optimum + 1 the tail is searched explicitly (`tail_ok`), so that "U U ..."
//! (= U2) or "U D U ..." are not counted as starting with a quarter turn.
//!
//! Sources shared with the other tools by `#[path]`: judging-a-dr/research/drtools/src/{core,class,reduced}.rs and
//! htrtools/src/model.rs (depth lookup, canonical rule).  Nothing of htrtools' route enumeration is used.
//!
//!   htfirst run <exact.u8> <statesdir> <out.tsv>     per state, both sides, both budgets
//!   htfirst tables <out.json>                        coordinate and coset tables for the Python side
//!   htfirst one <exact.u8>                           stdin: "#c,e,s" lines; prints the same columns
//! Threads: RAYON_NUM_THREADS.
#![forbid(unsafe_code)]
#![allow(dead_code)]

macro_rules! fatal {
    ($($arg:tt)*) => {{
        eprintln!($($arg)*);
        std::process::exit(1)
    }};
}

#[path = "../../../../judging-a-dr/research/drtools/src/core.rs"]
mod core;
#[path = "../../../../judging-a-dr/research/drtools/src/class.rs"]
mod class;
#[path = "../../../../judging-a-dr/research/drtools/src/reduced.rs"]
mod reduced;
#[path = "../../htrtools/src/model.rs"]
mod model;

use crate::core::{NC, NE, NMOVES, NS, NSYM};
use crate::class::{NCCOS, NEPAT};
use model::{axis_run, canonical_next, Model, FACE};
use rayon::prelude::*;
use std::fs::File;
use std::io::{BufRead, BufReader, BufWriter, Write};
use std::path::Path;

const HALF: [usize; 6] = [1, 4, 6, 7, 8, 9];
const QTS: [usize; 4] = [0, 2, 3, 5];
type S3 = (usize, usize, usize);

#[derive(Clone, Copy)]
struct Res {
    a: u8,
    b: u8,
    noqt: bool,
    q: u8,
    p1: u32,
    e: u8,
    eq: u8,
}
const EMPTY: Res = Res { a: 99, b: 99, noqt: false, q: 0, p1: 0, e: 99, eq: 0 };

#[inline]
fn qtf(m: &Model, z: S3) -> u8 {
    m.cls.qt_full[m.cls.ccos[z.0] as usize][m.cls.epat[z.1] as usize]
}

/// Is there an optimal finish of `z` on which every quarter turn lowers qt_full (so it has exactly qt_full(z)
/// quarter turns, the fewest any finish of z can have)?
fn min_qt_path(m: &Model, z: S3) -> bool {
    let dz = m.depth(z.0, z.1, z.2);
    if dz == 0 {
        return true;
    }
    let qz = qtf(m, z);
    for mv in 0..NMOVES {
        let y = m.mv(mv, z);
        if m.depth(y.0, y.1, y.2) + 1 != dz {
            continue;
        }
        if model::is_qt(mv as u8) && qtf(m, y) + 1 != qz {
            continue;
        }
        if min_qt_path(m, y) {
            return true;
        }
    }
    false
}

/// Is there an optimal finish of `z` that is canonical after a last move on face `lf` (axis run `la`)?
fn tail_ok(m: &Model, z: S3, lf: u8, la: u8) -> bool {
    let dz = m.depth(z.0, z.1, z.2);
    if dz == 0 {
        return true;
    }
    for mv in 0..NMOVES {
        if !canonical_next(mv, lf, la) {
            continue;
        }
        let y = m.mv(mv, z);
        if m.depth(y.0, y.1, y.2) + 1 != dz {
            continue;
        }
        // a move on another axis than the last one: whatever optimal finish follows is canonical
        if FACE[mv] / 2 != lf / 2 {
            return true;
        }
        if tail_ok(m, y, FACE[mv], axis_run(mv, lf, la)) {
            return true;
        }
    }
    false
}

#[allow(clippy::too_many_arguments)]
fn search(m: &Model, y: S3, h: u8, sb: u8, first: usize, lf: u8, la: u8, budget: u8, d: u8, res: &mut Res) {
    let dy = m.depth(y.0, y.1, y.2);
    if dy == 0 {
        res.noqt = true;
    }
    if h < budget {
        for (qi, &q) in QTS.iter().enumerate() {
            if !canonical_next(q, lf, la) {
                continue;
            }
            let z = m.mv(q, y);
            let dz = m.depth(z.0, z.1, z.2);
            let total = h + 1 + dz;
            if total > budget {
                continue;
            }
            let ok = total == d || tail_ok(m, z, FACE[q], axis_run(q, lf, la));
            // optimal level: the same start on a finish with no extra quarter turn
            if budget == d && total == d && qtf(m, z) + 1 == qtf(m, y) && min_qt_path(m, z) {
                res.e = res.e.min(h);
                if h == 0 {
                    res.eq |= 1 << qi;
                }
            }
            if ok {
                res.a = res.a.min(h);
                res.b = res.b.min(sb);
                if h == 0 {
                    res.q |= 1 << qi;
                }
                if h == 1 {
                    res.p1 |= 1 << (4 * first + qi);
                }
            }
        }
        for (hi, &mv) in HALF.iter().enumerate() {
            if !canonical_next(mv, lf, la) {
                continue;
            }
            let y2 = m.mv(mv, y);
            if m.depth(y2.0, y2.1, y2.2) + h + 1 > budget {
                continue;
            }
            let f = if h == 0 { hi } else { first };
            search(m, y2, h + 1, sb + (mv >= 6) as u8, f, FACE[mv], axis_run(mv, lf, la), budget, d, res);
        }
    }
}

fn one(m: &Model, x: S3) -> (u8, [Res; 4]) {
    let d = m.depth(x.0, x.1, x.2);
    let xi = (m.core.cinv[x.0] as usize, m.core.einv[x.1] as usize, m.core.sinv[x.2] as usize);
    if m.depth(xi.0, xi.1, xi.2) != d {
        fatal!("inverse has another optimum");
    }
    let mut out = [EMPTY; 4];
    for (k, (st, extra)) in [(x, 0u8), (xi, 0), (x, 1), (xi, 1)].into_iter().enumerate() {
        search(m, st, 0, 0, 0, 0xFF, 0xFF, d + extra, d, &mut out[k]);
    }
    (d, out)
}

const HEADER: &str = "subset\tidx\tc\te\ts\td\ta0n\ta0i\ta1n\ta1i\tb0n\tb0i\tb1n\tb1i\tnoqt0\tnoqt1\tq0n\tq0i\tq1n\tq1i\tp0n\tp0i\tp1n\tp1i\tccn\tcci\tepn\tepi\te0n\te0i\teqn\teqi\thasmin\tqtf";
fn line(m: &Model, sub: &str, idx: &str, x: S3) -> String {
    let (d, r) = one(m, x);
    let (ci, ei) = (m.core.cinv[x.0] as usize, m.core.einv[x.1] as usize);
    format!(
        "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:x}\t{:x}\t{:x}\t{:x}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
        sub, idx, x.0, x.1, x.2, d, r[0].a, r[1].a, r[2].a, r[3].a, r[0].b, r[1].b, r[2].b, r[3].b,
        (r[0].noqt || r[1].noqt) as u8, (r[2].noqt || r[3].noqt) as u8, r[0].q, r[1].q, r[2].q, r[3].q,
        r[0].p1, r[1].p1, r[2].p1, r[3].p1,
        m.cls.ccos[x.0], m.cls.ccos[ci], m.cls.epat[x.1], m.cls.epat[ei],
        r[0].e, r[1].e, r[0].eq, r[1].eq, min_qt_path(m, x) as u8, qtf(m, x)
    )
}

fn run(exact: &str, statesdir: &str, out: &str) -> std::io::Result<()> {
    let m = Model::new(Some(Path::new(exact)), None);
    let mut files: Vec<_> = std::fs::read_dir(statesdir)?
        .filter_map(|e| e.ok())
        .map(|e| e.path())
        .filter(|p| p.file_name().and_then(|s| s.to_str()).map_or(false, |s| s.starts_with("states_") && s.ends_with(".tsv")))
        .collect();
    files.sort();
    let mut f = BufWriter::new(File::create(out)?);
    writeln!(f, "{}", HEADER)?;
    for p in files {
        let rd = BufReader::new(File::open(&p)?);
        let rows: Vec<(String, String, S3)> = rd
            .lines()
            .skip(1)
            .map(|l| {
                let l = l.unwrap();
                let v: Vec<&str> = l.split('\t').collect();
                (v[0].to_string(), v[1].to_string(), (v[2].parse().unwrap(), v[3].parse().unwrap(), v[4].parse().unwrap()))
            })
            .collect();
        let lines: Vec<String> = rows.par_iter().map(|(sub, idx, x)| line(&m, sub, idx, *x)).collect();
        for l in &lines {
            writeln!(f, "{}", l)?;
        }
        eprintln!("{} {}", p.display(), lines.len());
    }
    Ok(())
}

fn stdin_states(exact: &str) -> std::io::Result<()> {
    let m = Model::new(Some(Path::new(exact)), None);
    println!("{}", HEADER);
    for l in std::io::stdin().lock().lines() {
        let l = l?;
        let t = l.trim().trim_start_matches('#');
        if t.is_empty() {
            continue;
        }
        let v: Vec<usize> = t.split(',').map(|x| x.trim().parse().unwrap()).collect();
        println!("{}", line(&m, "-", "-", (v[0], v[1], v[2])));
    }
    Ok(())
}

fn arr<T: std::fmt::Display>(v: impl IntoIterator<Item = T>) -> String {
    let s: Vec<String> = v.into_iter().map(|x| x.to_string()).collect();
    format!("[{}]", s.join(","))
}

/// Coordinate and coset tables as JSON, for the Python feature and check scripts.
fn tables(out: &str) -> std::io::Result<()> {
    let m = Model::new(None, None);
    let (core, cls, cc, sl) = (&m.core, &m.cls, &m.cc, &m.sl);
    let mut f = BufWriter::new(File::create(out)?);
    let mut parts: Vec<String> = Vec::new();
    parts.push(format!("\"nclass\":{}", cc.nclass));
    parts.push(format!("\"cclass\":{}", arr(cc.cclass.iter())));
    parts.push(format!("\"csymto\":{}", arr(cc.csymto.iter())));
    parts.push(format!("\"esym\":{}", arr((0..NSYM).map(|s| arr(core.esym[s].iter())))));
    parts.push(format!("\"ssym\":{}", arr((0..NSYM).map(|s| arr(core.ssym[s].iter())))));
    parts.push(format!("\"to12\":{}", arr(sl.to12.iter())));
    parts.push(format!("\"ccos\":{}", arr(cls.ccos.iter())));
    parts.push(format!("\"epat\":{}", arr(cls.epat.iter())));
    parts.push(format!("\"ccos_mv\":{}", arr((0..NCCOS).map(|a| arr(cls.ccos_mv[a].iter())))));
    parts.push(format!("\"epat_mv\":{}", arr((0..NEPAT).map(|b| arr(cls.epat_mv[b].iter())))));
    parts.push(format!("\"cc_qt\":{}", arr(cls.cc_qt.iter())));
    parts.push(format!("\"qt_full\":{}", arr((0..NCCOS).map(|a| arr(cls.qt_full[a].iter())))));
    parts.push(format!("\"htr_dist\":{}", arr((0..NCCOS).map(|a| arr(cls.htr_dist[a].iter())))));
    parts.push(format!("\"cc_subset\":{}", arr(cls.cc_subset.iter())));
    parts.push(format!("\"cc_nbad\":{}", arr(cls.cc_nbad.iter())));
    parts.push(format!("\"cc_shape\":{}", arr(cls.cc_shape.iter())));
    parts.push(format!("\"ep_nbad\":{}", arr(cls.ep_nbad.iter())));
    parts.push(format!("\"epat_mask\":{}", arr(cls.epat_mask.iter())));
    parts.push(format!("\"ccos_rep\":{}", arr(cls.ccos_rep.iter())));
    parts.push(format!("\"epat_rep\":{}", arr(cls.epat_rep.iter())));
    parts.push(format!("\"lmul_c\":{}", arr(cls.lmul_c.iter())));
    parts.push(format!("\"lmul_e\":{}", arr(cls.lmul_e.iter())));
    parts.push(format!(
        "\"subset_name\":{}",
        arr(class::SUBSET_NAME.iter().map(|s| format!("\"{}\"", s)))
    ));
    parts.push(format!("\"sizes\":[{},{},{}]", NC, NE, NS));
    writeln!(f, "{{{}}}", parts.join(",\n"))?;
    Ok(())
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let a: Vec<&str> = args.iter().map(String::as_str).collect();
    let r = match a.as_slice() {
        ["run", ex, st, out] => run(ex, st, out),
        ["one", ex] => stdin_states(ex),
        ["tables", out] => tables(out),
        _ => {
            eprintln!("usage: htfirst run <exact.u8> <statesdir> <out.tsv> | one <exact.u8> | tables <out.json>");
            std::process::exit(2)
        }
    };
    if let Err(e) = r {
        fatal!("htfirst: {}", e);
    }
}

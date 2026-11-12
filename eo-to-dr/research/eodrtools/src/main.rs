//! eodrtools: the computations of the eo-to-dr study (scramble -> EO -> DR).  See research/README.md.
//!
//! The cube model (`cubie.rs`) is is-dr-xs-worth-it's, used as it is; the coset move tables and the distance tables
//! are read from that study's out/ directory (tables/moves.bin, bfs/all_dr.u8, bfs/eo-fb_dr.u8).

#[allow(dead_code)]
#[path = "../../../../is-dr-xs-worth-it/research/xstools/src/cubie.rs"]
mod cubie;

/// Print a message to stderr and stop (used by the modules shared with judging-a-dr's drtools).
macro_rules! fatal {
    ($($arg:tt)*) => {{
        eprintln!($($arg)*);
        std::process::exit(1)
    }};
}
#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/core.rs"]
mod core;
#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/reduced.rs"]
mod reduced;
mod mkscr;
mod check;
mod common;
mod eo;
mod eodr;
mod scr;

fn main() {
    let a: Vec<String> = std::env::args().collect();
    match a.get(1).map(|s| s.as_str()) {
        Some("selftest") => cubie::selftest(&format!("{}/tables", common::XS)),
        Some("extract") => common::extract_eo0(&a[2], &a[3]),
        Some("scr") => scr::cmd(&a[2..]),
        Some("eo") => eo::cmd(&a[2..]),
        Some("mkscr") => mkscr::cmd(&a[2..]),
        Some("eolist") => scr::eolist(&a[2..]),
        Some("eodr") => eodr::cmd(&a[2..]),
        Some("check") => check::cmd(&a[2..]),
        _ => eprintln!("usage: eodrtools selftest | extract <src> <dst> | scr <scrambles> <cap> <kniss> [first] [count] | eo axis|layouts|sample | eodr exact|twoaxis|sample | check bits|pos"),
    }
}

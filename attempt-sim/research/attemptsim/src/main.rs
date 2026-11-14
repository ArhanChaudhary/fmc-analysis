//! attemptsim — a simulator of human FMC attempts.  See ../README.md.
//!
//! Reading order: ctx.rs (cube model and tables), eo.rs (EOs), line.rs (RZP to DR), finish.rs (HTR and the finish),
//! conf.rs (costs, human limits, policies), solver.rs (the attempt), cmds.rs (the commands).
//! vendor/ holds copies of other studies' sources: cubie.rs (is-dr-xs-worth-it), core.rs, class.rs, reduced.rs
//! (judging-a-dr), model.rs, routes.rs (htr-routes).
#![allow(dead_code)]

macro_rules! fatal {
    ($($arg:tt)*) => {{
        eprintln!($($arg)*);
        std::process::exit(1)
    }};
}

#[path = "vendor/cubie.rs"]
mod cubie;
#[path = "vendor/core.rs"]
mod core;
#[path = "vendor/class.rs"]
mod class;
#[path = "vendor/reduced.rs"]
mod reduced;
#[path = "vendor/model.rs"]
mod model;
#[path = "vendor/routes.rs"]
mod routes;
mod cmds;
mod conf;
mod ctx;
mod eo;
mod finish;
mod line;
mod rngx;
mod solver;

const USAGE: &str = "\
usage: attemptsim <command> ...
  selftest                      checks of the model and tables
  run --costs F --policies F --scrambles F [--first A] [--count N] [--seed S] --out OUT.tsv
      --exact TABLE [--log FILE --logn K] [--set cost.KEY=V | --set human.KEY=V]...
                                simulate every policy on every scramble
  routecurve --exact TABLE [--count N]
                                the route checklists as used here against htr-routes' numbers
  exhaust --scrambles F [--first A] [--count N] --exact TABLE [--eo 5] [--cap 11] --out OUT.tsv
                                the answer key: every EO-first DR finished optimally (computer only)
  cmpgaps --scrambles F --pop POP_RAW.tsv [--count N]
                                the DR lists against cubelib-cli's (gaps study)
Threads: RAYON_NUM_THREADS.  Data directory: ATTEMPTSIM_DATA (default: ../data next to the crate).";

fn main() {
    let a: Vec<String> = std::env::args().skip(1).collect();
    let rest = cmds::args(a.get(1..).unwrap_or(&[]));
    match a.first().map(|s| s.as_str()) {
        Some("selftest") => cmds::selftest(),
        Some("run") => cmds::run(&rest),
        Some("exhaust") => cmds::exhaust(&rest),
        Some("cmpgaps") => cmds::cmpgaps(&rest),
        Some("routecurve") => cmds::routecurve(&rest),
        Some("export") => cmds::export(&rest),
        _ => {
            eprintln!("{}", USAGE);
            std::process::exit(2)
        }
    }
}

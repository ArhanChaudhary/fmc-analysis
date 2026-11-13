//! htrtools — which HTR routes find the optimal DR finish.
//!
//! Reuses the first study's model by `#[path]` (judging-a-dr/research/drtools/src: core.rs, class.rs,
//! reduced.rs) and its exact table of optimal finishes (`lean_exact_table.u8`, `ls_depth.u8`).
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
mod model;
mod routes;
mod cmds;
mod bounding;
mod edgepaths;

const USAGE: &str = "\
usage: htrtools <command> ...
  dist <exact.u8> <outdir>                        optimal finish per subset (all DR states), HTR-state finishes,
                                                  DR->HTR length per subset
  routes <exact.u8> <ls.u8> <n> <seed> <outdir> [subsets]
                                                  n uniform states per subset: every optimal and +1 finish, every
                                                  NISS reading, route sets, HTR / qt statistics; also for X*R2
  trace <exact.u8> [cap]                          stdin: DR scrambles; every optimal finish (up to cap) and its readings
  explain <exact.u8>                              stdin: scramble<TAB>route key<TAB>max length -> a finish that follows it
  tie <exact.u8> <n> <seed> <out.tsv>             one optimal per state, random tie-break: linear chain shares
  tiels <exact.u8> <ls.u8> <n> <seed> <out.tsv>   the same on leave-slice finishes
  bound <exact.u8> <n> <seed> <out.tsv>           DR bounding read on every optimal / +1 finish: shortest reduction
                                                  to 1q / 2q per (length, quarter turns); same states as routes
  redcount <exact.u8> <n> <seed> <rmax> <out.tsv> number of reductions to 1q / 2q of each length a solver writes
  find <exact.u8> <subset> <depth> <seed>         a random state of the subset with that optimal, as #c,e,s
  bound2 <exact.u8> <n> <seed> <out.tsv> [subsets] reductions per finish length and corner path; trigger and switch data
  bound3 <exact.u8> <n> <seed> <out.tsv>          bounding as stated: reduction to 1q / 2q + optimal finish of the reduced state
  bound4 <exact.u8> <n> <seed> <out.tsv>          the same by exact search on reductions (targets opt, +1, 10, 11, 12)
  lsdist <ls_depth.u8>                            leave-slice distance histogram per 48-subset over every DR state
  alpha                                           stdin: corner paths (subset indices a-b-c); FakeMMAP's section bounds
  redcount2 <exact.u8> <n> <seed> <rmax> <out>    reductions to 1q / 2q a solver writes, by length (coset tables)
  edgepaths <exact.u8> <statesdir> <outdir> <subsets>  linear normal-side edge paths of every finish <= opt + 1
  nisshtr <exact.u8>                              stdin: DR scrambles; subset, labels, optimum, shortest linear HTR (normal, inverse), NISS HTR
Threads: RAYON_NUM_THREADS.";

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let a: Vec<&str> = args.iter().map(String::as_str).collect();
    let r = match a.as_slice() {
        ["dist", ex, out] => cmds::dist(ex, out),
        ["lsdist", ls] => cmds::lsdist(ls),
        ["routes", ex, ls, n, seed, out] => cmds::routes(ex, ls, n.parse().unwrap(), seed.parse().unwrap(), out, None),
        ["routes", ex, ls, n, seed, out, subs] => {
            cmds::routes(ex, ls, n.parse().unwrap(), seed.parse().unwrap(), out, Some(subs))
        }
        ["trace", ex] => cmds::trace(ex, 200),
        ["trace", ex, cap] => cmds::trace(ex, cap.parse().unwrap()),
        ["explain", ex] => cmds::explain(ex),
        ["nisshtr", ex] => cmds::nisshtr(ex),
        ["bound", ex, n, seed, out] => cmds::bound(ex, n.parse().unwrap(), seed.parse().unwrap(), out),
        ["redcount", ex, n, seed, r, out] => {
            cmds::redcount(ex, n.parse().unwrap(), seed.parse().unwrap(), r.parse().unwrap(), out)
        }
        ["tiels", ex, ls, n, seed, out] => cmds::tie_ls(ex, ls, n.parse().unwrap(), seed.parse().unwrap(), out),
        ["find", ex, sub, d, seed] => cmds::find(ex, sub, d.parse().unwrap(), seed.parse().unwrap()),
        ["bound2", ex, n, seed, out] => bounding::bound2(ex, n.parse().unwrap(), seed.parse().unwrap(), out, None),
        ["bound2", ex, n, seed, out, subs] => bounding::bound2(ex, n.parse().unwrap(), seed.parse().unwrap(), out, Some(subs)),
        ["bound3", ex, n, seed, out] => bounding::bound3(ex, n.parse().unwrap(), seed.parse().unwrap(), out),
        ["bound4", ex, n, seed, out] => bounding::bound4(ex, n.parse().unwrap(), seed.parse().unwrap(), out),
        ["alpha"] => bounding::alpha(""),
        ["redcount2", ex, n, seed, r, out] => {
            bounding::redcount2(ex, n.parse().unwrap(), seed.parse().unwrap(), r.parse().unwrap(), out)
        }
        ["edgepaths", ex, st, out, subs] => edgepaths::edgepaths(ex, st, out, subs),
        ["tie", ex, n, seed, out] => cmds::tie(ex, n.parse().unwrap(), seed.parse().unwrap(), out),
        _ => {
            eprintln!("{}", USAGE);
            std::process::exit(2)
        }
    };
    if let Err(e) = r {
        fatal!("htrtools: {}", e);
    }
}

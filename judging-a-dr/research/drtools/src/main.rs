//! drtools — exhaustive computations on the Rubik's cube "domino reduction" (DR) group
//! `<U, D, R2, L2, F2, B2>` (19,508,428,800 states).
//!
//! Rust port of the C programs in `research/src`; conventions, indexing and file layouts are the same, so
//! the outputs of the two are interchangeable.
//!
//! Reading order: `core.rs` (cube model and coordinates), `class.rs` (HTR cosets and subset labels),
//! `quot.rs` (the KF / K0 quotients), `spec.rs` (the ladder of quotients), `reduced.rs` (symmetry-reduced
//! index and on-disk data), then one file per subcommand.
#![forbid(unsafe_code)]

/// Print a message to stderr and stop with exit status 1
/// (the C programs' `fprintf(stderr, ...); exit(1);` for failed consistency checks and missing files).
macro_rules! fatal {
    ($($arg:tt)*) => {{
        eprintln!($($arg)*);
        std::process::exit(1)
    }};
}

mod bfs;
mod bitset;
mod census;
mod census2;
mod class;
mod core;
mod genlean;
mod hand;
mod ladder;
mod par;
mod parity;
mod query;
mod quot;
mod reduced;
mod selftest;
mod sharp;
mod spec;
mod text;

use std::path::Path;

const USAGE: &str = "\
usage: drtools <command> [arguments]

  selftest [listing]                  self-checks of the model (t_class.c, t_quot.c)
  bfs <outdir>                        exact optimal length of every DR state (drbfs.c)
  census <bfsdir>                     histogram by subset, HTR lengths, corner length; CSV on stdout (dragg.c)
  census2 <bfsdir>                    histogram by subset and KF / K0 bounds; CSV on stdout (dragg2.c)
  ladder <bfsdir> <tabledir>          writes T_<name>.u8 for every rung, CSV on stdout (drlattice.c)
  sharp <bfsdir> <tabledir> <spec>... check that a rung's table is the best case of each class (drsharp.c)
  parity <tabledir>                   the E-slice parity rule (drparity.c)
  query <bfsdir> <tabledir>           look up the states given on stdin (drq.c)
  genlean                             move maps for the Lean model (genlean.c)
  lsbfs <out.u8>                      optimal leave-slice length of every DR state
  hcensus <bfsdir> <ls.u8> <outdir>   histograms of hand-readable quantities against the optimal finish
  ncensus <bfsdir> <outdir>           invertible last move, number of optimal first moves
  hcensus2 <bfsdir> <outdir>          corner cases and pairs on both sides, edge length, combined reads
  read <bfsdir> <ls.u8>               everything readable off the DR states given on stdin, and their optimal
  witness <bfsdir> <ls.u8> <listing>  an explicit DR state for every existence claim made in the report

The number of threads is taken from RAYON_NUM_THREADS (default: all cores).";

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let args: Vec<&str> = args.iter().map(String::as_str).collect();
    let result = match args.as_slice() {
        ["selftest"] => selftest::run(Path::new(selftest::DEFAULT_LISTING)),
        ["selftest", listing] => selftest::run(Path::new(listing)),
        ["bfs", outdir] => bfs::run(Path::new(outdir)),
        ["census", bfsdir] => census::run(Path::new(bfsdir)),
        ["census2", bfsdir] => census2::run(Path::new(bfsdir)),
        ["ladder", bfsdir, tabdir] => ladder::run(Path::new(bfsdir), Path::new(tabdir)),
        ["sharp", bfsdir, tabdir, specs @ ..] => {
            let specs: Vec<String> = specs.iter().map(|s| s.to_string()).collect();
            sharp::run(Path::new(bfsdir), Path::new(tabdir), &specs)
        }
        ["parity", tabdir] => parity::run(Path::new(tabdir)),
        ["query", bfsdir, tabdir] => query::run(Path::new(bfsdir), Path::new(tabdir)),
        ["genlean"] => genlean::run(),
        ["lsbfs", out] => hand::run_lsbfs(Path::new(out)),
        ["hcensus", bfsdir, lsfile, outdir] => {
            hand::run_hcensus(Path::new(bfsdir), Path::new(lsfile), Path::new(outdir))
        }
        ["ncensus", bfsdir, outdir] => hand::run_ncensus(Path::new(bfsdir), Path::new(outdir)),
        ["hcensus2", bfsdir, outdir] => hand::run_hcensus2(Path::new(bfsdir), Path::new(outdir)),
        ["read", bfsdir, lsfile] => hand::run_read(Path::new(bfsdir), Path::new(lsfile)),
        ["witness", bfsdir, lsfile, listing] => {
            hand::run_witness(Path::new(bfsdir), Path::new(lsfile), Path::new(listing))
        }
        _ => {
            eprintln!("{}", USAGE);
            std::process::exit(2)
        }
    };
    match result {
        Ok(code) => std::process::exit(code),
        // a closed pipe on stdout (e.g. `drtools census ... | head`) is not an error worth a message
        Err(e) if e.kind() == std::io::ErrorKind::BrokenPipe => std::process::exit(0),
        Err(e) => fatal!("drtools: {}", e),
    }
}

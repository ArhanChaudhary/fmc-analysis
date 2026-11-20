//! `htr-cases`: the case list as text, one case in full, or a solver's own DR.
//!
//! ```text
//! htr-cases text FILE                 the shortest generator of every case (the page's htr-cases.txt)
//! htr-cases list                     every case (without its HTRs), as JSON
//! htr-cases case N [--turned]         one case with its HTRs, as JSON
//! htr-cases find SCRAMBLE MOVES       the case of a DR (NISS moves in brackets), as JSON
//! htr-cases all-dist FILE             the fewest face turns from every DR coset to HTR (the library's all_dist.bin)
//! ```
//!
//! `case` and `find` list HTRs up to 2 moves over the optimal, as the page does by default; `--above K` (0 to 4) sets
//! another number.

use htr_cases::{Index, DEFAULT_ABOVE};
use std::fmt::Write as _;

fn usage() -> ! {
    eprintln!("usage: htr-cases text FILE | list | case N [--turned] [--above K] | find SCRAMBLE MOVES [--above K] | all-dist FILE");
    std::process::exit(2);
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let index = Index::new();
    let above = match args.iter().position(|a| a == "--above") {
        Some(k) => args.get(k + 1).and_then(|s| s.parse().ok()).unwrap_or_else(|| usage()),
        None => DEFAULT_ABOVE,
    };
    match args.first().map(String::as_str) {
        Some("text") => {
            let path = args.get(1).unwrap_or_else(|| usage());
            std::fs::write(path, text(&index)).expect("write the text file");
            eprintln!("{} cases written to {path}", index.cases.len());
        }
        Some("all-dist") => {
            let path = args.get(1).unwrap_or_else(|| usage());
            std::fs::write(path, index.fresh_distances()).expect("write the distances");
            eprintln!("{} distances written to {path}", index.cosets.dist.len());
        }
        Some("list") => {
            let all: Vec<_> = (0..index.cases.len()).map(|i| index.info(i)).collect();
            println!("{}", serde_json::to_string(&all).unwrap());
        }
        Some("case") => {
            let n: usize = args
                .get(1)
                .and_then(|s| s.parse().ok())
                .filter(|n| (1..=index.cases.len()).contains(n))
                .unwrap_or_else(|| usage());
            let turned = args.iter().any(|a| a == "--turned");
            let info = index.info(n - 1);
            let x = index.coset(n - 1, turned);
            let solutions = index.solution_texts(x, index.longest(x, above));
            let generator = index.generator_text(x);
            println!(
                "{}",
                serde_json::json!({ "case": info, "turned": turned, "generator": generator, "solutions": solutions })
            );
        }
        Some("find") => {
            let (scramble, moves) =
                (args.get(1).unwrap_or_else(|| usage()), args.get(2).map(String::as_str).unwrap_or(""));
            match index.find(scramble, moves, above) {
                Ok(found) => println!("{}", serde_json::to_string(&found).unwrap()),
                Err(e) => {
                    eprintln!("{e}");
                    std::process::exit(1);
                }
            }
        }
        _ => usage(),
    }
}

/// The text file: a header, then one tab-separated line per case.
fn text(index: &Index) -> String {
    let mut out = String::new();
    let n = index.cases.len();
    writeln!(out, "# HTR cases of a DR on U/D, up to rotations, mirrors and the E slice: {n} cases, numbered as on https://fmc.arhan.sh/htr-cases/").unwrap();
    writeln!(out, "# One line per case, tab-separated:").unwrap();
    writeln!(out, "#   case         the case's number on the page").unwrap();
    writeln!(out, "#   subset       corner subset (4a3 and 4b3 apart: the shape is the one on this side)").unwrap();
    writeln!(out, "#   edges        bad edges, counted like the corners in the frame with few bad pieces").unwrap();
    writeln!(out, "#   htr          the optimal: fewest face turns to HTR, DR-breaking HTRs included").unwrap();
    writeln!(out, "#   label        4b2: no parity / parity; 2c3: clockwise / anticlockwise (the quarter turn to 4b2 with no parity); 2c4, 4a3: good / bad (see the page); else -").unwrap();
    writeln!(out, "#   bad_corners  the bad corners of the state the generator makes").unwrap();
    writeln!(out, "#   bad_edges    its bad U/D-layer edges").unwrap();
    writeln!(out, "#   generator    a shortest sequence that makes the case from a solved cube (as many moves as htr; for some cases it leaves DR on the way)").unwrap();
    writeln!(out, "#   htr_dr       fewest moves to HTR with DR moves only (U D R2 L2 F2 B2)").unwrap();
    writeln!(
        out,
        "# Case 1 is HTR with the E slice a quarter turn off (every corner and edge bad); HTR itself is not listed."
    )
    .unwrap();
    writeln!(
        out,
        "# The HTRs of every case: on the page, or `htr-cases case N [--above K]` (up to K moves over the optimal, {DEFAULT_ABOVE} by default)."
    )
    .unwrap();
    writeln!(out, "case\tsubset\tedges\thtr\tlabel\tbad_corners\tbad_edges\tgenerator\thtr_dr").unwrap();
    for i in 0..n {
        let c = index.info(i);
        let list = |v: &[&str]| if v.is_empty() { "-".to_string() } else { v.join(" ") };
        writeln!(
            out,
            "{}\t{}\t{}e\t{}\t{}\t{}\t{}\t{}\t{}",
            c.number,
            c.subset,
            c.edges,
            c.moves,
            c.label.unwrap_or("-"),
            list(&c.bad_corners),
            list(&c.bad_edges),
            index.generator_text(index.cases[i].coset),
            c.dr_moves
        )
        .unwrap();
    }
    out
}

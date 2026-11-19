//! Corners with DBL fixed and R, U, F turns.
//!
//!   c3d tables OUTDIR        every table the study uses, as flat binary files, and the histograms
//!   c3d show "R U2 F' ..."   what a human sees on the state a sequence makes, and how far it is

mod cube;
mod search;

use cube::{parse, show, Cube, Kind, State, MOVES, N, PLACES};
use search::{distance, fewest_quarters_among_optimal, histogram, Metric};
use std::fmt::Write as _;
use std::fs;
use std::path::Path;

fn usage() -> ! {
    eprintln!("usage: c3d tables OUTDIR | c3d show \"SEQUENCE\"");
    std::process::exit(2)
}

/// The goal sets the study measures distance to.
struct Goals {
    /// The solved state alone.
    solved: Vec<bool>,
    /// HTR: the 24 states half turns reach.
    htr: Vec<bool>,
    /// Every corner shows `Good` (in its tetrad and oriented): the 144 states that are DR on all three axes.
    all_good: Vec<bool>,
    /// The 72 of those with an even permutation: HTR and the two fake-HTR cosets a 3-cycle away.
    good_even: Vec<bool>,
    /// No corner in the wrong tetrad.
    tetrads: Vec<bool>,
    /// Corners oriented on R/L, on U/D, on F/B.
    oriented: [Vec<bool>; 3],
}

fn goals(moves: &[Vec<u32>], kinds: &[[Kind; 7]]) -> Goals {
    let mut solved = vec![false; N];
    solved[State::SOLVED.index()] = true;
    let mut htr = solved.clone();
    let mut stack = vec![State::SOLVED.index()];
    while let Some(s) = stack.pop() {
        for m in [1, 4, 7] {
            let t = moves[m][s] as usize;
            if !htr[t] {
                htr[t] = true;
                stack.push(t);
            }
        }
    }
    let all_good: Vec<bool> = kinds.iter().map(|k| k.iter().all(|&x| x == Kind::Good)).collect();
    let good_even = (0..N)
        .map(|i| all_good[i] && State::from_index(i).is_even())
        .collect();
    let is_out = |x: Kind| matches!(x, Kind::OutX | Kind::OutY | Kind::OutZ);
    let tetrads = kinds.iter().map(|k| !k.iter().any(|&x| is_out(x))).collect();
    let keeps = [Kind::OutX, Kind::OutY, Kind::OutZ];
    let oriented = std::array::from_fn(|axis| {
        kinds
            .iter()
            .map(|k| k.iter().all(|&x| x == Kind::Good || x == keeps[axis]))
            .collect()
    });
    Goals {
        solved,
        htr,
        all_good,
        good_even,
        tetrads,
        oriented,
    }
}

fn write_table(dir: &Path, name: &str, data: &[u8], log: &mut String) {
    fs::write(dir.join(format!("{name}.u8")), data).unwrap_or_else(|e| panic!("writing {name}: {e}"));
    let h = histogram(data);
    let total: usize = h.iter().enumerate().map(|(d, &c)| d * c).sum();
    #[allow(clippy::cast_precision_loss)]
    let mean = total as f64 / data.len() as f64;
    writeln!(log, "{name}\tmax {}\tmean {mean:.6}\t{h:?}", h.len() - 1).expect("write to string");
}

fn tables(dir: &Path) {
    fs::create_dir_all(dir).expect("create the output directory");
    let cube = Cube::new();
    let moves = cube.move_tables();
    let flat: Vec<u8> = moves
        .iter()
        .flat_map(|t| t.iter().flat_map(|v| v.to_le_bytes()))
        .collect();
    fs::write(dir.join("moves.u32"), flat).expect("write moves");
    let states: Vec<State> = (0..N).map(State::from_index).collect();
    let kinds: Vec<[Kind; 7]> = states.iter().map(State::kinds).collect();
    fs::write(
        dir.join("kinds.u8"),
        kinds.iter().flat_map(|k| k.map(|x| x as u8)).collect::<Vec<u8>>(),
    )
    .expect("write kinds");
    fs::write(
        dir.join("perm.u8"),
        states.iter().flat_map(|s| s.perm).collect::<Vec<u8>>(),
    )
    .expect("write perm");
    fs::write(
        dir.join("ori.u8"),
        states.iter().flat_map(|s| s.ori).collect::<Vec<u8>>(),
    )
    .expect("write ori");

    let g = goals(&moves, &kinds);
    let mut log = String::new();
    for (name, goal) in [
        ("solved", &g.solved),
        ("htr", &g.htr),
        ("good", &g.all_good),
        ("goodeven", &g.good_even),
        ("tet", &g.tetrads),
        ("co_x", &g.oriented[0]),
        ("co_y", &g.oriented[1]),
        ("co_z", &g.oriented[2]),
    ] {
        let size = goal.iter().filter(|&&b| b).count();
        writeln!(log, "goal {name}: {size} states").expect("write to string");
        let htm = distance(&moves, goal, Metric::Htm);
        write_table(dir, &format!("d_{name}"), &htm, &mut log);
        write_table(
            dir,
            &format!("qt_{name}"),
            &distance(&moves, goal, Metric::QuarterCount),
            &mut log,
        );
        if name == "solved" || name == "htr" {
            write_table(
                dir,
                &format!("qtm_{name}"),
                &distance(&moves, goal, Metric::Qtm),
                &mut log,
            );
            let qopt = fewest_quarters_among_optimal(&moves, &htm);
            write_table(dir, &format!("qopt_{name}"), &qopt, &mut log);
        }
    }
    fs::write(dir.join("tables.log"), &log).expect("write the log");
    print!("{log}");
}

fn kind_name(k: Kind) -> &'static str {
    match k {
        Kind::Good => "good",
        Kind::TwistCw => "twisted cw",
        Kind::TwistCcw => "twisted ccw",
        Kind::OutX => "out, R/L sticker oriented",
        Kind::OutY => "out, U/D sticker oriented",
        Kind::OutZ => "out, F/B sticker oriented",
    }
}

/// The seven kinds the way the pages print them: UFR UFL UBL UBR DFR DFL DBR, with `.` good, `+` `-` twisted
/// clockwise / counter-clockwise, `r` `u` `f` out with only the R/L, U/D or F/B sticker oriented.
fn kinds_line(s: &State) -> String {
    const ORDER: [usize; 7] = [0, 1, 4, 2, 3, 5, 6];
    const LETTER: [&str; 6] = [".", "+", "-", "r", "u", "f"];
    ORDER
        .iter()
        .map(|&p| LETTER[s.kind(p) as usize])
        .collect::<Vec<_>>()
        .join(" ")
}

fn show_state(seq: &str) {
    let ms = parse(seq).unwrap_or_else(|t| {
        eprintln!("not an R, U or F turn: {t} (the turns are {})", MOVES.join(" "));
        std::process::exit(2)
    });
    let cube = Cube::new();
    let s = cube.apply_all(&State::SOLVED, &ms);
    println!("{}  ->  state {}, types {}", show(&ms), s.index(), kinds_line(&s));
    for (p, name) in PLACES.iter().enumerate() {
        println!(
            "  {name}: piece {}, {}",
            PLACES[s.perm[p] as usize],
            kind_name(s.kind(p))
        );
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    match args.get(1).map(String::as_str) {
        Some("tables") => tables(Path::new(args.get(2).unwrap_or_else(|| usage()))),
        Some("show") => show_state(args.get(2).unwrap_or_else(|| usage())),
        _ => usage(),
    }
}

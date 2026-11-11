//! Searches on the 2,217,093,120 cosets of the DR group, as (co, eo, sl) coordinates (see `research/src/coords.py`):
//!
//!   co  0..2187   twist of the U/D-coloured corner stickers, per place
//!   eo  0..2048   edge orientation for the F/B axis, per place
//!   sl  0..495    the four places holding the E-slice pieces
//!
//! `bfs` computes, for every coset, the fewest face turns to reach a given set of target cosets, under a rule on
//! which turns are allowed:
//!
//!   all      all 18 face turns
//!   eo-fb    no F or B quarter turns                     (the turns that keep every edge's F/B orientation)
//!   eo-ud    no U or D quarter turns
//!   seo-fb   F and B quarter turns only when no E-slice piece is in that layer   (keeps the slice pieces' F/B
//!            orientation, may flip other edges)
//!   seo-ud   the same for U and D quarter turns
//!
//! The move tables come from `out/tables/moves.bin` (written by coords.py from the sticker model), so this file has
//! no cube geometry of its own.  Move numbering: 3 * face + (quarter turns - 1), faces U D R L F B.

/// Print a message to stderr and stop (used by the modules shared with judging-a-dr's drtools).
macro_rules! fatal {
    ($($arg:tt)*) => {{
        eprintln!($($arg)*);
        std::process::exit(1)
    }};
}

// The DR group model and the exact-table index of the first study, used as they are.
#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/class.rs"]
mod class;
#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/core.rs"]
mod core;
#[allow(dead_code)]
#[path = "../../../../judging-a-dr/research/drtools/src/reduced.rs"]
mod reduced;

mod attempt;
mod cubie;
mod finish;

use rayon::prelude::*;
use std::fs::File;
use std::io::{BufRead, BufReader, Read, Write};
use std::sync::atomic::{AtomicU8, Ordering};

const NCO: usize = 2187;
const NEO: usize = 2048;
const NSL: usize = 495;
const N: usize = NCO * NEO * NSL;
const UNSEEN: u8 = 255;

pub struct Tables {
    pub co: Vec<[u16; 18]>,
    pub eo: Vec<[u16; 18]>,
    pub sl: Vec<[u16; 18]>,
    pub layers: Vec<u8>,
}

pub fn load(dir: &str) -> Tables {
    let mut buf = Vec::new();
    File::open(format!("{dir}/moves.bin")).expect("moves.bin").read_to_end(&mut buf).unwrap();
    assert_eq!(buf.len(), (NCO + NEO + NSL) * 36);
    let row = |i: usize| -> [u16; 18] {
        let mut r = [0u16; 18];
        for m in 0..18 {
            r[m] = u16::from_le_bytes([buf[i * 36 + 2 * m], buf[i * 36 + 2 * m + 1]]);
        }
        r
    };
    let co = (0..NCO).map(row).collect();
    let eo = (NCO..NCO + NEO).map(row).collect();
    let sl = (NCO + NEO..NCO + NEO + NSL).map(row).collect();
    let mut layers = Vec::new();
    File::open(format!("{dir}/sl_layers.bin")).expect("sl_layers.bin").read_to_end(&mut layers).unwrap();
    assert_eq!(layers.len(), NSL);
    Tables { co, eo, sl, layers }
}

#[derive(Clone, Copy, PartialEq)]
enum Rule {
    All,
    EoFb,
    EoUd,
    SeoFb,
    SeoUd,
}

fn parse_rule(s: &str) -> Rule {
    match s {
        "all" => Rule::All,
        "eo-fb" => Rule::EoFb,
        "eo-ud" => Rule::EoUd,
        "seo-fb" => Rule::SeoFb,
        "seo-ud" => Rule::SeoUd,
        _ => panic!("unknown rule {s}"),
    }
}

/// Bit m set if move m is allowed from a state whose slice pieces occupy the layers in `layers`.
/// The rules are symmetric: a move is allowed from a state exactly when its inverse is allowed from the result
/// (a quarter turn of a face keeps the set of pieces in that face's layer).
#[inline]
fn allowed(rule: Rule, layers: u8) -> u32 {
    let all: u32 = (1 << 18) - 1;
    let quarter = |face: usize| -> u32 { (1 << (3 * face)) | (1 << (3 * face + 2)) };
    match rule {
        Rule::All => all,
        Rule::EoFb => all & !quarter(4) & !quarter(5),
        Rule::EoUd => all & !quarter(0) & !quarter(1),
        Rule::SeoFb => {
            let mut a = all;
            if layers & (1 << 4) != 0 { a &= !quarter(4); }
            if layers & (1 << 5) != 0 { a &= !quarter(5); }
            a
        }
        Rule::SeoUd => {
            let mut a = all;
            if layers & (1 << 0) != 0 { a &= !quarter(0); }
            if layers & (1 << 1) != 0 { a &= !quarter(1); }
            a
        }
    }
}

#[inline]
fn index(co: usize, eo: usize, sl: usize) -> usize {
    (co * NEO + eo) * NSL + sl
}

fn read_targets(path: &str) -> Vec<(usize, usize, usize)> {
    BufReader::new(File::open(path).expect("targets file"))
        .lines()
        .map(|l| l.unwrap())
        .filter(|l| !l.starts_with('#') && !l.trim().is_empty())
        .map(|l| {
            let v: Vec<usize> = l.split_whitespace().take(3).map(|x| x.parse().unwrap()).collect();
            (v[0], v[1], v[2])
        })
        .collect()
}

fn bfs(t: &Tables, rule: Rule, targets: &[(usize, usize, usize)], out: Option<&str>) {
    let dist: Vec<AtomicU8> = (0..N).into_par_iter().map(|_| AtomicU8::new(UNSEEN)).collect();
    for &(c, e, s) in targets {
        dist[index(c, e, s)].store(0, Ordering::Relaxed);
    }
    let mut hist: Vec<u64> = vec![targets.len() as u64];
    let mut depth: u8 = 0;
    loop {
        // every state at `depth` pushes its unseen neighbours to depth + 1 (rules are symmetric, so forward = backward)
        let found: u64 = (0..NCO)
            .into_par_iter()
            .map(|co| {
                let mut n = 0u64;
                for eo in 0..NEO {
                    let base = (co * NEO + eo) * NSL;
                    for sl in 0..NSL {
                        if dist[base + sl].load(Ordering::Relaxed) != depth {
                            continue;
                        }
                        let mut a = allowed(rule, t.layers[sl]);
                        while a != 0 {
                            let m = a.trailing_zeros() as usize;
                            a &= a - 1;
                            let j = index(t.co[co][m] as usize, t.eo[eo][m] as usize, t.sl[sl][m] as usize);
                            if dist[j].load(Ordering::Relaxed) == UNSEEN
                                && dist[j].compare_exchange(UNSEEN, depth + 1, Ordering::Relaxed, Ordering::Relaxed).is_ok()
                            {
                                n += 1;
                            }
                        }
                    }
                }
                n
            })
            .sum();
        if found == 0 {
            break;
        }
        hist.push(found);
        depth += 1;
        eprintln!("depth {depth}: {found}");
    }
    let total: u64 = hist.iter().sum();
    println!("reached {total} of {N} cosets");
    for (d, c) in hist.iter().enumerate() {
        println!("{d} {c}");
    }
    if let Some(path) = out {
        // AtomicU8 has the layout of u8; write the table without copying it
        let bytes: &[u8] = unsafe { std::slice::from_raw_parts(dist.as_ptr() as *const u8, N) };
        File::create(path).unwrap().write_all(bytes).unwrap();
        eprintln!("wrote {path}");
    }
}

/// xstools sample1s <tables dir> <kinds.tsv> <exact table> <samples> <seed> [dump]
/// Uniformly random DR-1s states; for each, the corner subset (of the DR the bare slice turn would give), the fewest
/// turns to a real DR, and the shortest finish of the form setup + slice + DR finish: exact, and with the setup
/// limited to 4 turns on the state's own side.  With `dump`, also the state itself and the best with setup <= 3.
fn sample1s(a: &[String]) {
    use finish::*;
    let t = load(&a[0]);
    let m = cubie::Model::load(&a[0]);
    let kinds = load_kinds(&a[1]);
    let ex = Exact::load(&a[2]);
    let (n, seed): (usize, u64) = (a[3].parse().unwrap(), a[4].parse().unwrap());
    let dump = a.get(5).map(|v| v.as_str()) == Some("dump");
    let labels = a.get(5).map(|v| v.as_str()) == Some("labels");
    let fin = Finisher::new(&m, &t, &ex, &kinds);
    let to_fb = m.rot_for(1, 2, None);
    let rows: Vec<String> = (0..n)
        .into_par_iter()
        .map(|i| {
            let mut rng = Rng(seed.wrapping_mul(0x9E3779B97F4A7C15).wrapping_add(i as u64));
            // (DR on U/D) then R L' then (DR on F/B): U/D colours end up on the F/B faces, four edges flipped
            let g = random_dr(&m, &mut rng);
            let h = m.conj(&random_dr(&m, &mut rng), to_fb);
            let x = m.apply(&g, &[6, 11]).then(&h);
            let k = kinds[&m.coords(&x)];
            assert!(k.slices == 1 && k.faces == 2);
            // corner subset: of the DR that the bare slice turn gives
            let (c, _, _) = m.dr_perms_corners(&m.apply(&x, &[6, 11]));
            let sub = ex.corner_subset(&c);
            // the four flipped edges by the slice they belong to, on this side and on the other
            let sp = |y: &cubie::Cubie| -> String {
                let (_, v, kk) = fin.views(y).into_iter().find(|(_, _, kk)| kk.slices == 1).unwrap();
                let (p, q) = split(&m, &v, kk.faces);
                assert!(p + q == 4);
                format!("{}-{}", p.max(q), p.min(q))
            };
            let tinv = fin.views(&x.inverse()).into_iter().find(|(_, _, kk)| kk.slices == 1).unwrap().2.turns;
            let splits = format!("{}\t{}\t{}", sp(&x), sp(&x.inverse()), tinv);
            if a.get(5).map(|v| v.as_str()) == Some("labels") {
                return format!("{sub}\t{}\t{splits}", k.turns);
            }
            let b = fin.finish_1s(&x).unwrap();
            assert!(m.apply(&x, &fin.written(&x, &b)) == cubie::SOLVED);
            let c4 = fin.finish_1s_capped(&x, 4).map_or(99, |b| b.total);
            let mut row = format!("{sub}\t{}\t{}\t{}\t{}\t{}\t{}\t{splits}", k.turns, b.total, c4, b.setup.len(), b.finish, b.inverse as u8);
            if dump {
                let c3 = fin.finish_1s_capped(&x, 3).map_or(99, |b| b.total);
                let v: Vec<String> = x.cp.iter().chain(&x.ct).chain(&x.ep).chain(&x.ef).map(|v| v.to_string()).collect();
                row += &format!("\t{c3}\t{}", v.join(" "));
            }
            row
        })
        .collect();
    if labels {
        println!("subset\tturns_to_dr\tsplit\tsplit_inverse\tturns_to_dr_inverse");
    } else {
        println!("subset\tturns_to_dr\tfinish\tfinish_setup4\tsetup\tdr_finish\tfound_on_inverse\tsplit\tsplit_inverse\tturns_to_dr_inverse{}", if dump { "\tfinish_setup3\tstate" } else { "" });
    }
    for r in rows {
        println!("{r}");
    }
}

/// xstools sample8fe <tables dir> <kinds.tsv> <exact table> <samples> <seed>
/// Uniformly random DR-2s 8fe states; for each, the corner subset (of the DR the two bare slice turns would give) and
/// the shortest finish of the form setup + the two slices together + DR finish.
fn sample8fe(a: &[String]) {
    use finish::*;
    let t = load(&a[0]);
    let m = cubie::Model::load(&a[0]);
    let kinds = load_kinds(&a[1]);
    let ex = Exact::load(&a[2]);
    let (n, seed): (usize, u64) = (a[3].parse().unwrap(), a[4].parse().unwrap());
    let fin = Finisher::new(&m, &t, &ex, &kinds);
    let to_rl = m.rot_for(1, 0, None);
    let rows: Vec<String> = (0..n)
        .into_par_iter()
        .map(|i| {
            let mut rng = Rng(seed.wrapping_mul(0x9E3779B97F4A7C15).wrapping_add(i as u64));
            // (DR on U/D) then R L' then U D' then (DR on R/L): U/D colours on the R/L faces, all eight edges flipped
            let g = random_dr(&m, &mut rng);
            let h = m.conj(&random_dr(&m, &mut rng), to_rl);
            let x = m.apply(&g, &[6, 11, 0, 5]).then(&h);
            let k = kinds[&m.coords(&x)];
            assert!(k.slices == 2 && k.flips == 8 && k.faces == 0);
            let (c, _, _) = m.dr_perms_corners(&m.apply(&x, &[0, 5, 6, 11]));
            let (total, sol) = attempt::finish_8fe(&fin, &x, 7).unwrap();
            assert!(m.apply(&x, &sol) == cubie::SOLVED && sol.len() == total as usize);
            let (short, _) = attempt::finish_8fe(&fin, &x, 3).unwrap(); // setups of at most 3 moves from either end
            // with no setup: the two slices at once, then the finish of that DR
            let direct = attempt::direct_8fe(&fin, &x).iter().map(|w| w.len()).min().unwrap();
            format!("{}\t{}\t{}\t{}", ex.corner_subset(&c), total, direct, short)
        })
        .collect();
    println!("subset\tfinish\tdirect\tfinish_setup3");
    for r in rows {
        println!("{r}");
    }
}

/// xstools finish <tables dir> <kinds.tsv> <exact table> "<moves>" ...
/// For the state each move sequence gives (from solved): its kind, and for a DR-1s or a DR-2s 8fe the best finish
/// of the method's form with a written solution.
fn finish_cmd(a: &[String]) {
    use finish::*;
    let t = load(&a[0]);
    let m = cubie::Model::load(&a[0]);
    let kinds = load_kinds(&a[1]);
    let ex = Exact::load(&a[2]);
    let fin = Finisher::new(&m, &t, &ex, &kinds);
    for seq in &a[3..] {
        let x = m.apply(&cubie::SOLVED, &attempt::parse(seq));
        let views = fin.views(&x);
        if views.is_empty() {
            println!("not a DR-xs");
            continue;
        }
        let desc: Vec<String> = views.iter().map(|(_, _, k)| format!("{} slices, {} flipped, {} turns to DR", k.slices, k.flips, k.turns)).collect();
        if let Some(b) = fin.finish_1s(&x) {
            let w = fin.written(&x, &b);
            assert!(m.apply(&x, &w) == cubie::SOLVED);
            println!("DR-1s\t{}\tfinish {}\t{}", desc.join("; "), b.total, text(&w));
        } else if let Some((tot, w)) = attempt::finish_8fe(&fin, &x, 7) {
            println!("DR-2s 8fe\t{}\tfinish {}\t{}", desc.join("; "), tot, text(&w));
        } else {
            println!("other\t{}", desc.join("; "));
        }
    }
}

fn main() {
    let a: Vec<String> = std::env::args().collect();
    match a.get(1).map(|s| s.as_str()) {
        Some("bfs") => {
            // xstools bfs <tables dir> <rule> <targets file> [out file]
            let t = load(&a[2]);
            bfs(&t, parse_rule(&a[3]), &read_targets(&a[4]), a.get(5).map(|s| s.as_str()));
        }
        Some("selftest") => cubie::selftest(&a[2]),
        Some("sample1s") => sample1s(&a[2..]),
        Some("attempts") => attempt::run(&a[2..]),
        Some("sample8fe") => sample8fe(&a[2..]),
        Some("nearest") => attempt::nearest(&a[2..]),
        Some("finish") => finish_cmd(&a[2..]),
        _ => eprintln!("usage: xstools bfs <tables dir> <all|eo-fb|eo-ud|seo-fb|seo-ud> <targets file> [out file]\n       xstools selftest <tables dir>"),
    }
}

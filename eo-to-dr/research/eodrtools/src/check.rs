//! Checks of the table mappings against nissy (run by research/src/check_nissy.py) and of the 4-bit packing.
//!
//! `check bits <n> <seed>`               the 4-bit packing of all_dr against the bytes of the file, at n random cosets
//! `check pos <scrambles> <n> <seed>`    positions with the value each mapping gives, one per line:
//!     kind  nissy-step  moves  expected
//!   dr      dr{ud,rl,fb}        the first n scrambles: fewest turns to DR on each axis (all_dr in the axis's view)
//!   eo      eo{fb,rl,ud}        the first n scrambles: optimal linear EO per axis (eo distance in the axis's view)
//!   eoniss  eo -N               the first n scrambles: optimal EO over all axes with NISS
//!   eodr    dr{X}-eo{Y}         n random 30-turn sequences without quarter turns of Y (so EO on Y is solved), per Y:
//!                               fewest EO-keeping turns to DR on each X != Y (eo-fb_dr, EO-solved part, in the view)
//!   eoany   dr{X}               the same positions: fewest turns of any kind to DR on X (all_dr, EO-solved part)

use crate::common::*;
use crate::cubie::SOLVED;
use std::fs::File;
use std::io::{Read, Seek, SeekFrom};

const AX: [&str; 3] = ["rl", "ud", "fb"];

fn bits(n: usize, seed: u64) {
    let full = Full4::open(&format!("{XS}/bfs/all_dr.u8"));
    let mut f = File::open(format!("{XS}/bfs/all_dr.u8")).unwrap();
    let mut rng = Rng::new(seed, 0);
    let mut bad = 0;
    for _ in 0..n {
        let i = rng.below(N);
        let (co, rest) = (i / (NEO * NSL), i % (NEO * NSL));
        let (eo, sl) = (rest / NSL, rest % NSL);
        f.seek(SeekFrom::Start(i as u64)).unwrap();
        let mut b = [0u8; 1];
        f.read_exact(&mut b).unwrap();
        if full.at((co, eo, sl)) != b[0] {
            bad += 1;
        }
    }
    println!("4-bit packing of all_dr: {n} random cosets, {bad} differ from the file");
    assert_eq!(bad, 0);
}

fn pos(scr: &str, n: usize, seed: u64) {
    let c = Ctx::new();
    let full = Full4::open(&format!("{XS}/bfs/all_dr.u8"));
    let here = std::env::var("EODR_OUT").unwrap_or_else(|_| "/data/fmc/eo-to-dr/research/out".into());
    let eo_dr = Eo0::load(&format!("{here}/big/eo-fb_dr_eo0.u8"));
    let all0 = Eo0::load(&format!("{here}/big/all_dr_eo0.u8"));
    let lines: Vec<String> = std::fs::read_to_string(scr).unwrap().lines().filter(|l| !l.starts_with('#') && !l.trim().is_empty()).take(n).map(|l| l.to_string()).collect();
    println!("kind\tstep\tmoves\texpected");
    for l in &lines {
        let s = c.m.apply(&SOLVED, &parse(l));
        let si = s.inverse();
        for x in 0..3 {
            let d = full.at(c.coords(&c.view(&s, c.rot_dr[x])));
            println!("dr\tdr{}\t{l}\t{d}", AX[x]);
        }
        let mut best = 99;
        for y in 0..3 {
            let d = c.eodist[Ctx::eo(&c.view(&s, c.rot_eo[y]))];
            println!("eo\teo{}\t{l}\t{d}", AX[y]);
            best = best.min(crate::eo::niss_eo(&c, &s, &si, y).2);
        }
        println!("eoniss\teo -N\t{l}\t{best}");
    }
    let mut rng = Rng::new(seed, 0);
    for y in 0..3 {
        let allowed: Vec<usize> = (0..18).filter(|&mv| !y_quarter(mv, y)).collect();
        for _ in 0..n {
            let mut seq = Vec::new();
            let mut last = NONE;
            while seq.len() < 30 {
                let mv = allowed[rng.below(allowed.len())];
                if canon_ok(last, mv) {
                    seq.push(mv);
                    last = mv;
                }
            }
            let s = c.m.apply(&SOLVED, &seq);
            for x in 0..3 {
                if x == y {
                    continue;
                }
                let (co, eo, sl) = c.coords(&c.view(&s, c.rot_pair[x][y]));
                assert_eq!(eo, 0);
                println!("eodr\tdr{}-eo{}\t{}\t{}", AX[x], AX[y], text(&seq), eo_dr.at(co, sl));
                println!("eoany\tdr{}\t{}\t{}", AX[x], text(&seq), all0.at(co, sl));
            }
        }
    }
}

pub fn cmd(a: &[String]) {
    match a[0].as_str() {
        "bits" => bits(a[1].parse().unwrap(), a[2].parse().unwrap()),
        "pos" => pos(&a[1], a[2].parse().unwrap(), a[3].parse().unwrap()),
        _ => panic!("check bits <n> <seed> | pos <scrambles> <n> <seed>"),
    }
}

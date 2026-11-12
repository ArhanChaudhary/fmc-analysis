//! eoswtools: the exact and sampled computations of the EO-switch study (study 6).  See research/README.md.
//!
//! State space: F/B EO solved, DR target U/D, coset = (co, sl) with co = twists of the 8 corner places (2187 values,
//! coords.py of is-dr-xs-worth-it) and sl = the 4 places holding E-slice pieces (495 values); index co * 495 + sl.
//! The cube model (`cubie.rs`, is-dr-xs-worth-it) and the shared helpers (`common.rs`, eo-to-dr) are compiled in
//! unchanged by #[path].

#[allow(dead_code)]
#[path = "../../../../is-dr-xs-worth-it/research/xstools/src/cubie.rs"]
mod cubie;
#[allow(dead_code)]
#[path = "../../../../eo-to-dr/research/eodrtools/src/common.rs"]
mod common;
mod att;
mod dist;
mod rzp;

fn main() {
    let a: Vec<String> = std::env::args().collect();
    match a.get(1).map(|s| s.as_str()) {
        Some("dist") => dist::dist_cmd(&a[2..]),
        Some("twoaxis") => dist::twoaxis_cmd(&a[2..]),
        Some("checkpos") => dist::checkpos_cmd(&a[2..]),
        Some("rzp") => rzp::cmd(&a[2..]),
        Some("att") => att::cmd(&a[2..]),
        _ => eprintln!("usage: eoswtools dist <out.u8> | twoaxis <d.u8> <out.u32> | checkpos <d.u8> <n> <seed> | rzp <d.u8> <out.u64> | att <d.u8> <scrambles> <first> <count> <outprefix>"),
    }
}

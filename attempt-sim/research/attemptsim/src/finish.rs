//! From a DR to solved: routes to HTR from the checklist of the DR's subset, each with its best finish.
//!
//! A DR is the pair (N, I) with `X = I^-1 S N` in the DR group of its axis; in the view where that axis is U/D, X is
//! a state (c, e, s) of judging-a-dr's model.  A finish is a sequence F of DR moves with X F = solved; the solution
//! is N F I^-1.  Every finish can be read as "A on normal, then B on inverse" in several ways (NISS readings), and
//! each reading follows a *route*: the corner subsets it passes at each quarter turn until HTR, with the switch
//! (htr-routes' definition, computed by its own code: vendor/routes.rs).
//!
//! The solver tries the routes of the htr-routes checklist for the DR's subset x edges, in the checklist's order
//! (research/data/checklist.tsv: level C, optimum, HTR budget 2).  Trying a route gives the shortest finish that
//! follows it with an HTR of at most the shortest NISS HTR + 2 moves, if that finish is at most `extra` moves
//! over the DR's optimal finish; otherwise the route gives nothing.  The solver never sees the optimum: only the
//! finishes it has found.

use crate::class::SUBSET_NAME;
use crate::ctx::*;
use crate::routes;
use std::collections::HashMap;

pub const SW: u8 = 0xFE;
pub const HTR_BUDGET: u8 = 2;
/// Finishes up to this many moves over the optimum are found by a route.
pub const EXTRA: usize = 2;
const CAP: u64 = 400_000;

pub struct Step {
    pub key: Vec<u8>,
    pub name: String,
    /// share of the subset's DRs where this route is the first of the list to find the optimal (htr-routes)
    pub marginal: f64,
}

/// The checklist of each of the 48 subsets (index: sub48 id).
pub fn load_checklists(c: &Ctx) -> Vec<Vec<Step>> {
    let path = format!("{}/checklist.tsv", data_dir());
    let txt = std::fs::read_to_string(&path).unwrap_or_else(|e| fatal!("{}: {}", path, e));
    let mut out: Vec<Vec<Step>> = (0..c.dm.cls.sub48_name.len()).map(|_| Vec::new()).collect();
    for line in txt.lines().skip(1) {
        let p: Vec<&str> = line.split('\t').collect();
        let Some(g) = c.dm.cls.sub48_name.iter().position(|n| n == p[0]) else { fatal!("checklist.tsv: unknown group {}", p[0]) };
        out[g].push(Step { key: parse_class(p[2]), name: p[2].to_string(), marginal: p[3].parse().unwrap() });
    }
    for (g, l) in out.iter().enumerate() {
        if l.is_empty() {
            fatal!("checklist.tsv: no routes for {}", c.dm.cls.sub48_name[g]);
        }
    }
    out
}

/// "4a1 > 4b2 > (2c3 > 4b2 > 4a1 > 0c0) | ht" -> subset indices, the switch marker, and 0 (ht) / 1 (qt) at the end.
pub fn parse_class(s: &str) -> Vec<u8> {
    let (body, post) = s.rsplit_once(" | ").unwrap_or_else(|| fatal!("bad route class {}", s));
    let mut k = Vec::new();
    for part in body.split(" > ") {
        let mut q = part;
        if let Some(r) = q.strip_prefix('(') {
            k.push(SW);
            q = r;
        }
        let q = q.trim_end_matches(')');
        k.push(SUBSET_NAME.iter().position(|n| *n == q).unwrap_or_else(|| fatal!("bad subset {} in route {}", q, s)) as u8);
    }
    k.push((post == "qt") as u8);
    k
}

pub struct RouteTable {
    /// exact optimal finish of the state (never shown to the solver)
    pub d: u8,
    pub capped: bool,
    /// route class -> (length, moves in drtools numbering) of the shortest finish that follows it
    pub best: HashMap<Vec<u8>, (u8, Vec<u8>)>,
}

/// Every route that finds a finish of at most optimal + EXTRA on the state, with that finish.
pub fn route_table(c: &Ctx, x: (usize, usize, usize)) -> RouteTable {
    let m = &c.dm;
    let d = m.depth(x.0, x.1, x.2);
    let niss = m.niss_htr(x.0, x.1);
    let mut best: HashMap<Vec<u8>, (u8, Vec<u8>)> = HashMap::new();
    let mut rd = Vec::with_capacity(48);
    let mut key: Vec<u8> = Vec::with_capacity(32);
    let ok = routes::finishes(m, x, d as usize + EXTRA, CAP, &mut |moves, path| {
        routes::readings(m, moves, path, &mut rd);
        for r in &rd {
            if r.htr_len > niss + HTR_BUDGET {
                continue;
            }
            let b = r.h.bytes();
            key.clear();
            for &v in &b[1..b.len() - 1] {
                key.push(if v == SW { SW } else { v / 5 });
            }
            key.push(b[b.len() - 1]);
            match best.get_mut(&key) {
                Some(e) => {
                    if (moves.len() as u8) < e.0 {
                        *e = (moves.len() as u8, moves.to_vec());
                    }
                }
                None => {
                    best.insert(key.clone(), (moves.len() as u8, moves.to_vec()));
                }
            }
        }
    });
    RouteTable { d, capped: !ok, best }
}

/// DR moves (drtools numbering) as own-label moves of the cube, for a DR seen through rotation `rot`.
pub fn dr_to_own(c: &Ctx, rot: usize, seq: &[u8]) -> Vec<u8> {
    seq.iter().map(|&m| c.umove[rot][DRMOVE[m as usize] as usize]).collect()
}

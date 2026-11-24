//! From a DR to solved: routes to HTR from the checklist of the DR's subset, each with its best finish.
//!
//! A DR is a pair (N, I) with `X = I^-1 S N` in the DR group of its axis; in the view where that axis is U/D, X is a
//! state of the DR model.  A finish is a sequence F of DR moves with X·F = solved; the solution is N F I^-1.
//!
//! The solver tries the routes of the checklist of the DR's subset in order.  Trying a route gives the shortest finish
//! that follows it with an HTR of at most the shortest NISS HTR + 2 moves, if that finish is at most 2 moves over the
//! DR's optimal finish; otherwise the route gives nothing.  The solver never sees the optimum, only the finishes it
//! found.

use crate::cube::{Move, View};
use crate::dr::{DrState, AS_CUBE_MOVE};
use crate::routes::readings;
use crate::tables::Tables;
use std::collections::HashMap;

/// A route's HTR may be this many moves longer than the shortest NISS HTR (the research value; `Human::htr_extra`).
pub const HTR_BUDGET: u8 = 2;
/// Finishes up to this many moves over the optimum are found by a route.
pub const EXTRA: usize = 2;
/// At most this many finishes are looked at per DR state.
const CAP: u64 = 400_000;

pub struct RouteTable {
    /// the optimal finish of the state (never shown to the solver)
    pub optimal: u8,
    pub capped: bool,
    /// route -> (length, DR moves) of the shortest finish that follows it
    pub best: HashMap<Vec<u8>, (u8, Vec<u8>)>,
}

/// Every route that finds a finish of at most optimal + EXTRA on the state, with that finish; a route's HTR is at
/// most `htr_extra` moves over the shortest NISS HTR.
pub fn route_table(t: &Tables, x: DrState, htr_extra: u8) -> RouteTable {
    let noe = t.noe();
    let optimal = noe.optimal(&t.dr, x);
    let niss = t.htr.niss_htr(&t.dr, x.0, x.1);
    let mut best: HashMap<Vec<u8>, (u8, Vec<u8>)> = HashMap::new();
    let mut found = Vec::with_capacity(48);
    let complete = noe.for_each_finish(&t.dr, x, optimal as usize + EXTRA, CAP, &mut |moves, path| {
        readings(&t.dr, &t.htr, moves, path, &mut found);
        for r in &found {
            if r.htr_len > niss + htr_extra {
                continue;
            }
            match best.get_mut(&r.route) {
                Some(e) => {
                    if (moves.len() as u8) < e.0 {
                        *e = (moves.len() as u8, moves.to_vec());
                    }
                }
                None => {
                    best.insert(r.route.clone(), (moves.len() as u8, moves.to_vec()));
                }
            }
        }
    });
    RouteTable { optimal, capped: !complete, best }
}

/// DR moves as turns of the cube, for a DR looked at through `view`.
pub fn dr_moves_to_cube(view: &View, moves: &[u8]) -> Vec<Move> {
    moves.iter().map(|&m| view.from_view(Move(AS_CUBE_MOVE[m as usize]))).collect()
}

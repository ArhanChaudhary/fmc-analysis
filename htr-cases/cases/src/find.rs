//! A solver's own DR, from the scramble and the moves done so far: which axis it is on and which coset.

use attempt_sim::cube::{invert, parse_moves, Move, MoveTables, View, DR_VIEW, FACE_NAMES};
use attempt_sim::dr::{rank_perm, AS_CUBE_MOVE};
use attempt_sim::htr::{Htr, NEPAT};

/// A DR found on a scramble: the coset, seen in the view that puts its DR axis on U/D.
pub struct Found {
    pub coset: usize,
    /// DR axis: 0 R/L, 1 U/D, 2 F/B
    pub axis: usize,
    pub view: View,
}

/// The moves of a solution so far, as written in a solve: moves on the normal side, and moves in brackets on the
/// inverse side (NISS); everything after `//` on a line is a comment.  Returns (normal, inverse).
pub fn parse_solution(text: &str) -> Result<(Vec<Move>, Vec<Move>), String> {
    let (mut normal, mut inverse) = (String::new(), String::new());
    let mut on_inverse = false;
    for line in text.lines() {
        let line = line.split("//").next().unwrap_or("");
        for ch in line.chars() {
            match ch {
                '(' if !on_inverse => on_inverse = true,
                ')' if on_inverse => on_inverse = false,
                '(' | ')' => return Err("brackets don't match".into()),
                _ if on_inverse => inverse.push(ch),
                _ => normal.push(ch),
            }
        }
        normal.push(' ');
        inverse.push(' ');
    }
    if on_inverse {
        return Err("a bracket is not closed".into());
    }
    Ok((parse_moves(&normal)?, parse_moves(&inverse)?))
}

/// The state a solver looks at after the scramble, the normal moves and the inverse moves: the inverse moves undone
/// before the scramble, then the scramble, then the normal moves.
pub fn state_moves(scramble: &[Move], normal: &[Move], inverse: &[Move]) -> Vec<Move> {
    let mut all = invert(inverse);
    all.extend_from_slice(scramble);
    all.extend_from_slice(normal);
    all
}

/// The DR of a move sequence (from solved), on whichever axis it is.
pub fn find(htr: &Htr, cube: &MoveTables, moves: &[Move]) -> Result<Found, String> {
    // U/D first; any EO axis other than the DR axis will do for the view
    for (axis, eo_axis) in [(1, 2), (0, 2), (2, 0)] {
        let view = DR_VIEW[axis][eo_axis];
        if let Some((c, e, _)) = cube.state(&view.seq_to_view(moves)).dr_perms() {
            let coset = htr.ccos[rank_perm(&c)] as usize * NEPAT + htr.epat[rank_perm(&e)] as usize;
            return Ok(Found { coset, axis, view });
        }
    }
    Err("that is not a DR on any axis (corners or edges are still misoriented, or E-slice edges are out of their slice)".into())
}

impl Found {
    /// A DR move of the view as a turn of the solver's cube.
    pub fn turn(&self, dr_move: u8) -> Move {
        self.view.from_view(Move(AS_CUBE_MOVE[dr_move as usize]))
    }

    /// A piece named by its view faces (`UFR`), named by the solver's faces, in the order U/D, F/B, R/L.
    pub fn place_name(&self, view_name: &str) -> String {
        let mut faces: Vec<usize> = view_name
            .chars()
            .map(|ch| {
                let g = FACE_NAMES.iter().position(|&f| f == ch).expect("a face letter");
                self.view.from_view(Move::new(g, 1)).face()
            })
            .collect();
        // U D, then F B, then R L
        let rank = |f: &usize| [0, 0, 2, 2, 1, 1][*f];
        faces.sort_by_key(rank);
        faces.iter().map(|&f| FACE_NAMES[f]).collect()
    }
}

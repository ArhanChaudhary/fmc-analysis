//! The route a finish follows to HTR (the notation of *Which HTR routes to try from a DR*).
//!
//! X is the DR state, S a finish (X·S = solved), n = |S|, seg(a, b) the moves S[a..b] alone.  A finish can be done
//! linearly or split with NISS at a point k:
//!
//! * normal first: S[0..k] on normal, then the inverse of S[k..n] on inverse;
//! * inverse first: the inverse of S[k..n] on inverse first, then S[0..k] on normal.
//!
//! A *reading* is one such way of doing the finish.  Its route is the chain of subset labels it passes, one at the
//! start and one after each quarter turn, until the first state in HTR, with the switch marked if it comes before
//! that; plus whether the rest of the finish has a quarter turn in it (`qt`, an HTR-breaking finish) or not (`ht`).
//! Labels only change at quarter turns, so only splits at a quarter turn are read.

use crate::dr::{DrTables, MOVE_IS_QUARTER};
use crate::htr::Htr;

/// Marks the switch to the other side in a route.
pub const SWITCH: u8 = 0xFE;

/// One reading of a finish: its route (corner subsets in order, `SWITCH` where it switches, then 1 for `qt` or 0 for
/// `ht`) and the length of its HTR.
pub struct Reading {
    pub route: Vec<u8>,
    pub htr_len: u8,
}

/// Every reading of the finish `moves` of the state whose corner and edge coordinates after each prefix are `path`.
pub fn readings(dr: &DrTables, htr: &Htr, moves: &[u8], path: &[(usize, usize)], out: &mut Vec<Reading>) {
    out.clear();
    let n = moves.len();
    let quarter = |i: usize| MOVE_IS_QUARTER[moves[i] as usize];
    // seg[a][b]: corner and edge coordinates of the moves a..b alone
    let mut seg = [[(0usize, 0usize); 21]; 21];
    for a in 0..=n {
        let (mut c, mut e) = (0usize, 0usize);
        for b in a..n {
            c = dr.cmove[moves[b] as usize][c] as usize;
            e = dr.emove[moves[b] as usize][e] as usize;
            seg[a][b + 1] = (c, e);
        }
    }
    // quarter turns among the first i moves
    let mut qt_before = [0usize; 21];
    for i in 0..n {
        qt_before[i + 1] = qt_before[i] + quarter(i) as usize;
    }
    let any_qt = |a: usize, b: usize| qt_before[b] > qt_before[a];
    let (cx, ex) = path[0];
    let start_label = htr.label(cx, ex);
    let start_label_inv = htr.label(dr.cinv[cx] as usize, dr.einv[ex] as usize);
    let start_in_htr = htr.in_htr(cx, ex);
    // the subset label of a corner + coset index pair (labels are subset * 5 + bad edges / 2)
    let corner_subset = |label: u8| label / 5;

    /// The route being read: subsets until HTR, then where the post-HTR part of the finish lies.
    struct Chain {
        route: Vec<u8>,
        /// (HTR length, post-HTR segment a..b) once HTR is reached
        done: Option<(usize, usize, usize)>,
    }
    impl Chain {
        fn push(&mut self, subset: u8) {
            if self.done.is_none() {
                self.route.push(subset);
            }
        }
    }

    // normal first (k = n: linear on normal)
    for k in 1..=n.max(1) {
        let k = k.min(n);
        if !(k == n || (quarter(k - 1) && qt_before[k] > 0 && qt_before[n] - qt_before[k] > 0)) {
            continue;
        }
        let mut ch = Chain { route: vec![corner_subset(start_label)], done: start_in_htr.then_some((0, 0, n)) };
        for i in 1..=k {
            if quarter(i - 1) {
                let (c, e) = path[i];
                ch.push(corner_subset(htr.label(c, e)));
                if ch.done.is_none() && htr.in_htr(c, e) {
                    ch.done = Some((i, i, n));
                }
            }
        }
        if k < n {
            ch.push(SWITCH);
            for j in 1..=n - k {
                if quarter(n - j) {
                    let (c, e) = seg[k][n - j];
                    ch.push(corner_subset(htr.label(c, e)));
                    if ch.done.is_none() && htr.in_htr(c, e) {
                        ch.done = Some((k + j, k, n - j));
                    }
                }
            }
        }
        let (htr_len, a, b) = ch.done.expect("a finish ends in HTR");
        ch.route.push(any_qt(a, b) as u8);
        out.push(Reading { route: ch.route, htr_len: htr_len as u8 });
        if n == 0 {
            break;
        }
    }
    // inverse first (k = 0: linear on inverse)
    for k in 0..n {
        if !(k == 0 || (quarter(k) && qt_before[k] > 0 && qt_before[n] - qt_before[k] > 0)) {
            continue;
        }
        let mut ch = Chain { route: vec![corner_subset(start_label_inv)], done: start_in_htr.then_some((0, 0, n)) };
        for j in 1..=n - k {
            if quarter(n - j) {
                let (c, e) = seg[0][n - j];
                ch.push(corner_subset(htr.label(c, e)));
                if ch.done.is_none() && htr.in_htr(c, e) {
                    ch.done = Some((j, 0, n - j));
                }
            }
        }
        if k > 0 {
            ch.push(SWITCH);
            for i in 1..=k {
                if quarter(i - 1) {
                    let (c, e) = seg[i][k];
                    ch.push(corner_subset(htr.label(dr.cinv[c] as usize, dr.einv[e] as usize)));
                    if ch.done.is_none() && htr.in_htr(c, e) {
                        ch.done = Some(((n - k) + i, i, k));
                    }
                }
            }
        }
        let (htr_len, a, b) = ch.done.expect("a finish ends in HTR");
        ch.route.push(any_qt(a, b) as u8);
        out.push(Reading { route: ch.route, htr_len: htr_len as u8 });
    }
}

/// A route written out: `4a1 > 4b2 > (2c3 > 0c0) | ht`.
pub fn route_name(route: &[u8]) -> String {
    let (body, last) = route.split_at(route.len() - 1);
    let mut parts: Vec<String> = Vec::new();
    let mut switched = false;
    for &x in body {
        if x == SWITCH {
            switched = true;
            continue;
        }
        let name = crate::htr::SUBSET_NAMES[x as usize];
        if switched && !parts.iter().any(|p| p.starts_with('(')) {
            parts.push(format!("({name}"));
        } else {
            parts.push(name.to_string());
        }
    }
    let mut s = parts.join(" > ");
    if switched {
        s.push(')');
    }
    s.push_str(if last[0] == 1 { " | qt" } else { " | ht" });
    s
}

/// Read a route name back (the checklist's format).
pub fn parse_route(s: &str) -> Result<Vec<u8>, String> {
    let (body, post) = s.rsplit_once(" | ").ok_or_else(|| format!("bad route {s}"))?;
    let mut route = Vec::new();
    for part in body.split(" > ") {
        let mut q = part;
        if let Some(rest) = q.strip_prefix('(') {
            route.push(SWITCH);
            q = rest;
        }
        let q = q.trim_end_matches(')');
        let i = crate::htr::SUBSET_NAMES.iter().position(|n| *n == q).ok_or_else(|| format!("bad subset {q} in route {s}"))?;
        route.push(i as u8);
    }
    route.push((post == "qt") as u8);
    Ok(route)
}

#[cfg(test)]
mod tests {
    #[test]
    fn route_names_read_back() {
        for line in include_str!("../data/checklist.tsv").lines().skip(1) {
            let name = line.split('\t').nth(2).unwrap();
            assert_eq!(super::route_name(&super::parse_route(name).unwrap()), name);
        }
    }
}

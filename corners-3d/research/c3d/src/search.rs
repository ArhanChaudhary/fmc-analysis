//! Distance tables over all states.  Every table is a distance *to a set of goal states*, found by a search
//! outward from the goal (each turn has its inverse among the turns, so that is the same thing).

use crate::cube::{is_quarter, N};
use std::collections::VecDeque;

/// A distance not yet filled in.
pub const UNSET: u8 = u8::MAX;

/// Which turns count, and what they cost.
#[derive(Clone, Copy, PartialEq, Eq)]
pub enum Metric {
    /// Every turn costs 1 (HTM).
    Htm,
    /// Only quarter turns exist, each costing 1 (QTM: a half turn is two of them).
    Qtm,
    /// Quarter turns cost 1 and half turns are free.
    QuarterCount,
}

/// The fewest turns (in `metric`) from every state to the nearest goal state.
#[must_use]
pub fn distance(moves: &[Vec<u32>], goal: &[bool], metric: Metric) -> Vec<u8> {
    let mut dist = vec![UNSET; N];
    let mut queue = VecDeque::new();
    for (i, _) in goal.iter().enumerate().filter(|&(_, &g)| g) {
        dist[i] = 0;
        queue.push_back(u32::try_from(i).expect("fits"));
    }
    while let Some(s) = queue.pop_front() {
        let d = dist[s as usize];
        for (m, table) in moves.iter().enumerate() {
            let quarter = is_quarter(m);
            if metric == Metric::Qtm && !quarter {
                continue;
            }
            let t = table[s as usize];
            let free = metric == Metric::QuarterCount && !quarter;
            let nd = if free { d } else { d + 1 };
            if dist[t as usize] > nd {
                dist[t as usize] = nd;
                if free {
                    queue.push_front(t);
                } else {
                    queue.push_back(t);
                }
            }
        }
    }
    dist
}

/// Among the shortest HTM solutions of each state (`dist` is the HTM distance to the goal), the fewest quarter
/// turns.
#[must_use]
pub fn fewest_quarters_among_optimal(moves: &[Vec<u32>], dist: &[u8]) -> Vec<u8> {
    let mut order: Vec<u32> = (0..u32::try_from(N).expect("fits")).collect();
    order.sort_by_key(|&s| dist[s as usize]);
    let mut q = vec![UNSET; N];
    for &s in &order {
        let d = dist[s as usize];
        if d == 0 {
            q[s as usize] = 0;
            continue;
        }
        let mut best = UNSET;
        for (m, table) in moves.iter().enumerate() {
            let t = table[s as usize] as usize;
            if dist[t] + 1 == d {
                best = best.min(q[t] + u8::from(is_quarter(m)));
            }
        }
        q[s as usize] = best;
    }
    q
}

/// How many states sit at each distance.
#[must_use]
pub fn histogram(dist: &[u8]) -> Vec<usize> {
    let max = dist.iter().copied().max().unwrap_or(0) as usize;
    let mut h = vec![0; max + 1];
    for &d in dist {
        h[d as usize] += 1;
    }
    h
}

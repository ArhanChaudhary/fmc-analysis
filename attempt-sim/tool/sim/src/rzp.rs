//! From an EO to DRs: the RZP search of one *line* = (EO ending, DR axis).
//!
//! The line is looked at in the view where the EO axis is F/B and the DR axis is U/D.  A node is a state reached from
//! the EO by EO-keeping turns on the side the EO ended on (the RZP), possibly followed by a *switch* to the other side
//! (the state inverted; turns from then on go to the other side) and more turns there.
//!
//! What the solver knows about a node:
//!
//! * its *read*: how far the DR looks from there.  A solver judges that from the DRM, pairs, ARM and experience; here
//!   it is the true distance blurred by a normal error of spread `read_sd` moves, fixed per node.  The read of a state
//!   one turn away, and of the same state on the other side, is available without working that state;
//! * once the node is worked, with a chance that depends on the true distance, the DR itself: `dr_see_glance[d]` for
//!   the EO's own state (the glance that discards an EO), `dr_see_work[d]` for an RZP state that is worked.
//!
//! The true distance is never handed to the plan.  Nodes are worked best first by `rzp_depth_weight * moves so far +
//! read`, a switch ranked `switch_pen` worse.

use crate::cube::{cancel, canonical_after, Cube, Move, View, DR_VIEW};
use crate::eo::{view_state, Ending};
use crate::rng::{h2, hash_bytes, normal, uniform};
use crate::settings::Human;
use crate::tables::{Tables, EO_KEEPING, N_SLICE};
use std::cmp::Reverse;
use std::collections::BinaryHeap;

/// A DR found from a line.
#[derive(Clone, Debug)]
pub struct DrCandidate {
    /// moves on the normal side and on the inverse side, each cancelled
    pub normal: Vec<Move>,
    pub inverse: Vec<Move>,
    /// EO axis, DR axis
    pub eo_axis: usize,
    pub dr_axis: usize,
    pub len: usize,
    pub eo_len: usize,
    /// side (0 normal, 1 inverse) of the DR's last turn when that turn is a quarter turn that can go either way
    pub flip_side: Option<usize>,
    /// how far away the DR was when it was seen, RZP moves before that, and whether the line had switched
    pub seen_from: usize,
    pub rzp_moves: usize,
    pub switched: bool,
}

/// What was worked: the RZP moves (cube labels) on the EO's side and, after a switch, on the other side.
#[derive(Clone, Debug, Default)]
pub struct NodeInfo {
    pub first_side: Vec<Move>,
    pub switched: bool,
    pub second_side: Vec<Move>,
    /// the solver's read of how far the DR is from here, and the truth (never shown to the plan)
    pub read: f64,
    pub true_distance: usize,
    /// the DRM: bad corners and edges out of the E slice
    pub drm: String,
}

#[allow(clippy::large_enum_variant)] // one at a time, straight to the caller
pub enum LineStep {
    /// a state was looked at: was it a switch, what it was, the DR seen from it
    Looked { switch: bool, node: NodeInfo, dr: Option<DrCandidate> },
    Exhausted,
}

struct Node {
    read: f32,
    state: Cube,
    /// view moves on the starting side, and on the other side after the switch
    a: Vec<Move>,
    b: Vec<Move>,
    switched: bool,
    twist: u16,
    slice: u16,
}

pub struct LineSearch {
    pub eo_axis: usize,
    pub dr_axis: usize,
    view: View,
    /// the side the EO ended on (0 normal, 1 inverse)
    start_side: usize,
    root: Ending,
    eo_len: usize,
    /// the EO's last view move on the starting side and on the other side
    last_start: Option<Move>,
    last_other: Option<Move>,
    nodes: Vec<Node>,
    /// nodes not yet worked: (rank in thousandths, order of arrival) -> node, smallest first
    heap: BinaryHeap<(Reverse<(i64, u64)>, usize)>,
    arrivals: u64,
    pub examined: usize,
    pub found: usize,
    seed: u64,
    /// the read of the EO's own state
    pub first_read: f32,
    read_sd: f64,
    depth_weight: f64,
    switch_pen: f64,
}

impl LineSearch {
    #[allow(clippy::too_many_arguments)]
    pub fn new(t: &Tables, human: &Human, scramble: &[Move], root: &Ending, eo_axis: usize, dr_axis: usize, eo_len: usize, seed: u64) -> LineSearch {
        let view = DR_VIEW[dr_axis][eo_axis];
        let v = view_state(t, &view, scramble, &root.normal, &root.inverse);
        let start_side = if root.normal.is_empty() && !root.inverse.is_empty() { 1 } else { 0 };
        let state = if start_side == 1 { v.inverse() } else { v };
        let last_in_view = |q: &[Move]| q.last().map(|&m| view.to_view(m));
        let (last_start, last_other) = if start_side == 0 {
            (last_in_view(&root.normal), last_in_view(&root.inverse))
        } else {
            (last_in_view(&root.inverse), last_in_view(&root.normal))
        };
        let (twist, flips, slice) = t.coords(&state);
        debug_assert_eq!(flips, 0);
        let mut k = vec![eo_axis as u8, dr_axis as u8, 0xFD];
        k.extend(root.normal.iter().map(|m| m.0));
        k.push(0xFF);
        k.extend(root.inverse.iter().map(|m| m.0));
        let mut line = LineSearch {
            eo_axis,
            dr_axis,
            view,
            start_side,
            root: root.clone(),
            eo_len,
            last_start,
            last_other,
            nodes: Vec::new(),
            heap: BinaryHeap::new(),
            arrivals: 0,
            examined: 0,
            found: 0,
            seed: hash_bytes(seed, &k),
            first_read: 0.0,
            read_sd: human.read_sd,
            depth_weight: human.rzp_depth_weight,
            switch_pen: 0.0,
        };
        let r = line.read(t, &[], false, &[], twist, slice);
        line.first_read = r as f32;
        line.push(Node { read: 0.0, state, a: Vec::new(), b: Vec::new(), switched: false, twist: twist as u16, slice: slice as u16 }, r);
        line
    }

    /// The side (0 normal, 1 inverse) the line started on.
    pub fn start_side(&self) -> usize {
        self.start_side
    }

    fn node_key(&self, a: &[Move], switched: bool, b: &[Move]) -> u64 {
        let mut key: Vec<u8> = a.iter().map(|m| m.0).collect();
        key.push(if switched { 0xF1 } else { 0xF0 });
        key.extend(b.iter().map(|m| m.0));
        hash_bytes(self.seed, &key)
    }

    /// How far the DR looks from a node: the true distance plus the solver's reading error.
    fn read(&self, t: &Tables, a: &[Move], switched: bool, b: &[Move], twist: usize, slice: usize) -> f64 {
        let d = t.dr_dist[twist * N_SLICE + slice] as f64;
        (d + self.read_sd * normal(h2(self.node_key(a, switched, b), 2))).max(0.0)
    }

    /// The most promising node not yet worked: (its rank, the total its read promises: EO + moves + read).
    pub fn peek(&self) -> Option<(f64, f64)> {
        self.heap.peek().map(|&(Reverse((rank, _)), i)| {
            let n = &self.nodes[i];
            let g = (n.a.len() + n.b.len()) as f64;
            (rank as f64 / 1000.0, self.eo_len as f64 + g + n.read as f64)
        })
    }

    fn push(&mut self, mut n: Node, rank: f64) {
        // `rank` is depth weight * moves + read (+ switch penalty); keep the bare read with the node
        let g = (n.a.len() + n.b.len()) as f64;
        n.read = (rank - self.depth_weight * g - if n.switched { self.switch_pen } else { 0.0 }) as f32;
        self.nodes.push(n);
        self.arrivals += 1;
        self.heap.push((Reverse(((rank * 1000.0).round() as i64, self.arrivals)), self.nodes.len() - 1));
    }

    fn to_cube_moves(&self, q: &[Move]) -> Vec<Move> {
        self.view.seq_from_view(q)
    }

    /// Work the next state.  `depth`: most RZP moves; `cap`: longest DR accepted.
    pub fn step(&mut self, t: &Tables, human: &Human, depth: usize, switch_pen: f64, cap: usize) -> LineStep {
        self.switch_pen = switch_pen;
        let Some((_, ni)) = self.heap.pop() else { return LineStep::Exhausted };
        self.examined += 1;
        let (state, a, b, switched, twist, slice, read) = {
            let n = &self.nodes[ni];
            (n.state, n.a.clone(), n.b.clone(), n.switched, n.twist as usize, n.slice as usize, n.read)
        };
        let g = a.len() + b.len();
        let d = t.dr_dist[twist * N_SLICE + slice] as usize;
        let info = NodeInfo {
            first_side: self.to_cube_moves(&a),
            switched,
            second_side: self.to_cube_moves(&b),
            read: read as f64,
            true_distance: d,
            drm: t.drm_name(twist, slice),
        };
        let was_switch = switched && b.is_empty();
        // is the DR seen from here?
        let hk = self.node_key(&a, switched, &b);
        let at_root = g == 0 && !switched;
        let see = if at_root { &human.dr_see_glance } else { &human.dr_see_work };
        let seen = self.eo_len + g + d <= cap && d < 8 && uniform(h2(hk, 1)) < see[d];
        if seen {
            let dr = self.complete(t, &a, &b, switched, twist, slice, d, hk);
            return LineStep::Looked { switch: was_switch, node: info, dr: Some(dr) };
        }
        // children: one more turn on this side, and the switch
        if d > 0 && g < depth {
            let cur = if switched { &b } else { &a };
            let last = cur.last().copied().or(if switched { self.last_other } else { self.last_start });
            for m in EO_KEEPING {
                // against the EO's own last turn only the same face is excluded
                let ok = if cur.is_empty() { last.is_none_or(|l| l.face() != m.face()) } else { canonical_after(last, m) };
                if !ok {
                    continue;
                }
                let (tw2, sl2) = (t.twist_move[twist][m.index()] as usize, t.slice_move[slice][m.index()] as usize);
                let (mut a2, mut b2) = (a.clone(), b.clone());
                if switched {
                    b2.push(m);
                } else {
                    a2.push(m);
                }
                let rank = human.rzp_depth_weight * (g + 1) as f64
                    + self.read(t, &a2, switched, &b2, tw2, sl2)
                    + if switched { switch_pen } else { 0.0 };
                let child = Node { read: 0.0, state: t.moves.turn(&state, m), a: a2, b: b2, switched, twist: tw2 as u16, slice: sl2 as u16 };
                self.push(child, rank);
            }
        }
        if d > 0 && !switched && switch_pen < 50.0 {
            let inv = state.inverse();
            let (tw2, _, sl2) = t.coords(&inv);
            let rank = human.rzp_depth_weight * g as f64 + self.read(t, &a, true, &[], tw2, sl2) + switch_pen;
            self.push(Node { read: 0.0, state: inv, a: a.clone(), b: Vec::new(), switched: true, twist: tw2 as u16, slice: sl2 as u16 }, rank);
        }
        LineStep::Looked { switch: was_switch, node: info, dr: None }
    }

    /// The DR seen from a node: one optimal completion on the current side (at each step, among the turns that get
    /// closer, the one a hash picks), written as normal and inverse moves of the whole attempt.
    #[allow(clippy::too_many_arguments)]
    fn complete(&mut self, t: &Tables, a: &[Move], b: &[Move], switched: bool, twist: usize, slice: usize, d: usize, hk: u64) -> DrCandidate {
        let (mut tw, mut sl) = (twist, slice);
        let mut tail: Vec<Move> = Vec::new();
        let mut last = if switched { b.last().copied().or(self.last_other) } else { a.last().copied().or(self.last_start) };
        for left in (1..=d).rev() {
            let closer = |m: Move| {
                let (tw2, sl2) = (t.twist_move[tw][m.index()] as usize, t.slice_move[sl][m.index()] as usize);
                (t.dr_dist[tw2 * N_SLICE + sl2] as usize == left - 1).then_some((tw2, sl2))
            };
            let mut best: Option<(u64, Move, usize, usize)> = None;
            for m in EO_KEEPING {
                if !canonical_after(last, m) {
                    continue;
                }
                if let Some((tw2, sl2)) = closer(m) {
                    let w = h2(hk, 100 + tail.len() as u64 * 32 + m.0 as u64);
                    if best.is_none_or(|bst| w < bst.0) {
                        best = Some((w, m, tw2, sl2));
                    }
                }
            }
            // a canonical descent exists except right after the EO's own last turn: then take the first turn that works
            let (_, m, tw2, sl2) = best.unwrap_or_else(|| {
                EO_KEEPING.iter().find_map(|&m| closer(m).map(|(a2, b2)| (0, m, a2, b2))).expect("some turn gets closer")
            });
            tail.push(m);
            last = Some(m);
            tw = tw2;
            sl = sl2;
        }
        let (mut va, mut vb) = (a.to_vec(), b.to_vec());
        if switched {
            vb.extend(&tail);
        } else {
            va.extend(&tail);
        }
        let (mut n, mut i) = (self.root.normal.clone(), self.root.inverse.clone());
        if self.start_side == 0 {
            n.extend(self.to_cube_moves(&va));
            i.extend(self.to_cube_moves(&vb));
        } else {
            i.extend(self.to_cube_moves(&va));
            n.extend(self.to_cube_moves(&vb));
        }
        let (n, i) = (cancel(&n), cancel(&i));
        let side = if switched { 1 - self.start_side } else { self.start_side };
        // the last turn of the side the DR was finished on can go either way if it is a quarter turn of the third axis
        let third = 3 - self.dr_axis - self.eo_axis;
        let last_move = if side == 0 { n.last() } else { i.last() };
        let flip_side = match last_move {
            Some(m) if m.is_quarter_turn_of(third) => Some(side),
            _ => None,
        };
        self.found += 1;
        DrCandidate {
            len: n.len() + i.len(),
            normal: n,
            inverse: i,
            eo_axis: self.eo_axis,
            dr_axis: self.dr_axis,
            eo_len: self.eo_len,
            flip_side,
            seen_from: d,
            rzp_moves: a.len() + b.len(),
            switched,
        }
    }
}

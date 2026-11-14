//! From an EO to DRs: the RZP search of one *line* = (EO ending, DR axis).
//!
//! The line is looked at in the view where the EO axis is F/B and the DR axis is U/D.  A node is a state reached
//! from the EO by EO-keeping turns on the side the EO ended on (the RZP), optionally followed by a *switch* to the
//! other side (the state inverted, turns from then on go to the other side) and more turns there.
//!
//! What the solver knows about a node:
//!   * its *read*: how far the DR looks from there.  A solver judges that from the DRM, pairs, ARM and experience;
//!     here it is the true distance blurred by a normal error of spread `human.read_sd` moves, fixed per node
//!     (`read_sd` = 1 is about as sharp as the EO-switch study's cards: see the write-up).  The read of a state one
//!     turn away, and of the same state on the other side, is available without working that state.
//!   * once the node is examined, with a chance that depends on the true distance, the DR itself:
//!     `human.dr_see_glance[d]` for the EO's own state (the glance that discards an EO), `human.dr_see_work[d]`
//!     for an RZP state that is worked.
//! The true distance is never handed to the policy.  Nodes are worked best first by
//! `rzp_depth_weight * moves so far + read`, a switch ranked `switch_pen` worse.

use crate::conf::Human;
use crate::ctx::*;
use crate::cubie::Cubie;
use crate::eo::EoRoot;
use crate::rngx::{h2, hseq, normal, unif};
use std::collections::BinaryHeap;

#[derive(Clone, Debug)]
pub struct DrCand {
    /// normal-side and inverse-side moves (own labels), each cancelled
    pub n: Vec<u8>,
    pub i: Vec<u8>,
    pub y: u8,
    pub x: u8,
    pub len: u8,
    pub eo_len: u8,
    /// side (0 normal, 1 inverse) of the DR's last turn when that turn is a quarter turn that can go either way
    pub flip_side: Option<u8>,
    /// distance at which the DR was seen, RZP moves before it, whether the line switched
    pub d_seen: u8,
    pub rzp: u8,
    pub switched: bool,
}

struct Node {
    read: f32,
    st: Cubie,
    a: Vec<u8>, // view moves on the starting side
    b: Vec<u8>, // view moves on the other side (after the switch)
    sw: bool,
    co: u16,
    sl: u16,
}

#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Item(std::cmp::Reverse<(i64, u64)>, usize);

pub struct LineSearch {
    pub y: usize,
    pub x: usize,
    rot: usize,
    side0: u8,
    root_n: Vec<u8>,
    root_i: Vec<u8>,
    eo_len: u8,
    last0: u8, // last view move of the EO on the starting side / on the other side
    last1: u8,
    nodes: Vec<Node>,
    heap: BinaryHeap<Item>,
    seq: u64,
    pub examined: usize,
    pub found: usize,
    seed: u64,
    /// read of the EO's own state
    pub h0: f32,
    read_sd: f64,
    depth_w: f64,
    sw_pen: f64,
}

pub enum Step {
    /// a state was examined: (was it a switch, the DR seen from it and its distance)
    Looked(bool, Option<DrCand>),
    Exhausted,
}

impl LineSearch {
    pub fn new(c: &Ctx, hum: &Human, s: &Cubie, root: &EoRoot, y: usize, x: usize, eo_len: u8, seed: u64) -> LineSearch {
        let rot = c.rot_pair[x][y];
        let v = c.m.conj(&c.state_ni(s, &root.n, &root.i), rot);
        let side0 = if root.n.is_empty() && !root.i.is_empty() { 1 } else { 0 };
        let st = if side0 == 1 { v.inverse() } else { v };
        let lastv = |q: &[u8]| q.last().map_or(NONE, |&mv| c.vmove[rot][mv as usize]);
        let (last0, last1) = if side0 == 0 { (lastv(&root.n), lastv(&root.i)) } else { (lastv(&root.i), lastv(&root.n)) };
        let (co, eo, sl) = c.m.coords(&st);
        debug_assert_eq!(eo, 0);
        let mut k = vec![y as u8, x as u8, 0xFD];
        k.extend(&root.n);
        k.push(0xFF);
        k.extend(&root.i);
        let seed = hseq(seed, &k);
        let mut ls = LineSearch {
            y, x, rot, side0, root_n: root.n.clone(), root_i: root.i.clone(), eo_len, last0, last1,
            nodes: Vec::new(), heap: BinaryHeap::new(), seq: 0, examined: 0, found: 0, seed, h0: 0.0,
            read_sd: hum.read_sd, depth_w: hum.rzp_depth_weight, sw_pen: 0.0,
        };
        let r = ls.read(c, &[], false, &[], co, sl);
        ls.h0 = r as f32;
        ls.push(Node { read: 0.0, st, a: Vec::new(), b: Vec::new(), sw: false, co: co as u16, sl: sl as u16 }, r);
        ls
    }

    fn node_key(&self, a: &[u8], sw: bool, b: &[u8]) -> u64 {
        let mut key = a.to_vec();
        key.push(if sw { 0xF1 } else { 0xF0 });
        key.extend(b);
        hseq(self.seed, &key)
    }
    /// How far the DR looks from a node: the true distance plus the solver's reading error.
    fn read(&self, c: &Ctx, a: &[u8], sw: bool, b: &[u8], co: usize, sl: usize) -> f64 {
        let d = c.drdist[co * NSL + sl] as f64;
        (d + self.read_sd * normal(h2(self.node_key(a, sw, b), 2))).max(0.0)
    }
    /// The most promising node not yet worked: (rank, read of the DR's total length), or None if the line is exhausted.
    pub fn peek(&self) -> Option<(f64, f64)> {
        self.heap.peek().map(|Item(std::cmp::Reverse((p, _)), ni)| {
            let n = &self.nodes[*ni];
            let g = (n.a.len() + n.b.len()) as f64;
            let pen = *p as f64 / 1000.0;
            // rank = depth_w * g + read (+ switch_pen): the total the node promises is EO + g + read
            (pen, self.eo_len as f64 + g + n.read as f64)
        })
    }

    fn push(&mut self, mut n: Node, prio: f64) {
        // `prio` arrives as depth weight * moves + read (+ switch penalty); keep the bare read with the node
        let g = (n.a.len() + n.b.len()) as f64;
        n.read = (prio - self.depth_w * g - if n.sw { self.sw_pen } else { 0.0 }) as f32;
        self.nodes.push(n);
        self.seq += 1;
        self.heap.push(Item(std::cmp::Reverse(((prio * 1000.0).round() as i64, self.seq)), self.nodes.len() - 1));
    }

    fn own(&self, c: &Ctx, q: &[u8]) -> Vec<u8> {
        q.iter().map(|&mv| c.umove[self.rot][mv as usize]).collect()
    }

    /// Examine the next state.  `depth`: most RZP moves; `cap`: longest DR accepted.
    pub fn step(&mut self, c: &Ctx, hum: &Human, depth: usize, switch_pen: f64, cap: usize) -> Step {
        self.sw_pen = switch_pen;
        let Some(Item(_, ni)) = self.heap.pop() else { return Step::Exhausted };
        self.examined += 1;
        let (st, a, b, sw, co, sl) = {
            let n = &self.nodes[ni];
            (n.st, n.a.clone(), n.b.clone(), n.sw, n.co as usize, n.sl as usize)
        };
        let g = a.len() + b.len();
        let d = c.drdist[co * NSL + sl] as usize;
        // is the DR seen from here?
        let hk = self.node_key(&a, sw, &b);
        let is_root = g == 0 && !sw;
        let see = if is_root { &hum.dr_see_glance } else { &hum.dr_see_work };
        let seen = self.eo_len as usize + g + d <= cap && d < 8 && unif(h2(hk, 1)) < see[d];
        if seen {
            // one optimal completion on this side: at each step, among the turns that get closer, the one a hash picks
            let (mut cc, mut ss) = (co, sl);
            let mut tail: Vec<u8> = Vec::new();
            let mut last = if sw { b.last().copied().unwrap_or(self.last1) } else { a.last().copied().unwrap_or(self.last0) };
            let mut dd = d;
            while dd > 0 {
                let mut best: Option<(u64, u8, usize, usize)> = None;
                for &mv in &EOKEEP {
                    if !canon_ok(last, mv) {
                        continue;
                    }
                    let (c2, s2) = (c.co_mv[cc][mv as usize] as usize, c.sl_mv[ss][mv as usize] as usize);
                    if c.drdist[c2 * NSL + s2] as usize == dd - 1 {
                        let w = h2(hk, 100 + tail.len() as u64 * 32 + mv as u64);
                        if best.map_or(true, |bst| w < bst.0) {
                            best = Some((w, mv, c2, s2));
                        }
                    }
                }
                // a canonical descent always exists: a shortest path never repeats a face or orders opposite faces badly
                // except through the EO's own last turn; fall back to any turn if the canonical ones fail
                let (_, mv, c2, s2) = best.unwrap_or_else(|| {
                    EOKEEP
                        .iter()
                        .map(|&mv| (0u64, mv, c.co_mv[cc][mv as usize] as usize, c.sl_mv[ss][mv as usize] as usize))
                        .find(|&(_, _, c2, s2)| c.drdist[c2 * NSL + s2] as usize == dd - 1)
                        .unwrap()
                });
                tail.push(mv);
                last = mv;
                cc = c2;
                ss = s2;
                dd -= 1;
            }
            let (mut va, mut vb) = (a.clone(), b.clone());
            if sw {
                vb.extend(&tail);
            } else {
                va.extend(&tail);
            }
            let (mut n, mut i) = (self.root_n.clone(), self.root_i.clone());
            if self.side0 == 0 {
                n.extend(self.own(c, &va));
                i.extend(self.own(c, &vb));
            } else {
                i.extend(self.own(c, &va));
                n.extend(self.own(c, &vb));
            }
            let (n, i) = (cancel(&n), cancel(&i));
            let cur_side = if sw { 1 - self.side0 } else { self.side0 };
            // the last turn of the side the DR was finished on can go either way if it is a quarter turn of the
            // third axis (the turn that completes the DR)
            let z = 3 - self.x - self.y;
            let lastmv = if cur_side == 0 { n.last() } else { i.last() };
            let flip_side = match lastmv {
                Some(&mv) if axis_quarter(mv, z) => Some(cur_side),
                _ => None,
            };
            self.found += 1;
            let cand = DrCand {
                len: (n.len() + i.len()) as u8,
                n, i, y: self.y as u8, x: self.x as u8, eo_len: self.eo_len, flip_side,
                d_seen: d as u8, rzp: g as u8, switched: sw,
            };
            return Step::Looked(sw && b.is_empty(), Some(cand));
        }
        // children: one more turn on this side, and the switch
        let was_switch = sw && b.is_empty();
        if d > 0 && g < depth {
            let cur: &Vec<u8> = if sw { &b } else { &a };
            let last = cur.last().copied().unwrap_or(if sw { self.last1 } else { self.last0 });
            for &mv in &EOKEEP {
                // against the EO's own last turn only the same face is excluded
                let ok = if cur.is_empty() { last == NONE || last / 3 != mv / 3 } else { canon_ok(last, mv) };
                if !ok {
                    continue;
                }
                let (c2, s2) = (c.co_mv[co][mv as usize] as usize, c.sl_mv[sl][mv as usize] as usize);
                let (mut a2, mut b2) = (a.clone(), b.clone());
                if sw {
                    b2.push(mv);
                } else {
                    a2.push(mv);
                }
                let prio = hum.rzp_depth_weight * (g + 1) as f64 + self.read(c, &a2, sw, &b2, c2, s2) + if sw { switch_pen } else { 0.0 };
                self.push(Node { read: 0.0, st: c.m.turn(&st, mv as usize), a: a2, b: b2, sw, co: c2 as u16, sl: s2 as u16 }, prio);
            }
        }
        if d > 0 && !sw && switch_pen < 50.0 {
            let inv = st.inverse();
            let (c2, _, s2) = c.m.coords(&inv);
            let prio = hum.rzp_depth_weight * g as f64 + self.read(c, &a, true, &[], c2, s2) + switch_pen;
            self.push(Node { read: 0.0, st: inv, a: a.clone(), b: Vec::new(), sw: true, co: c2 as u16, sl: s2 as u16 }, prio);
        }
        Step::Looked(was_switch, None)
    }
}

/// Every DR within `cap` turns that continues an EO ending on one side without breaking the EO and without a
/// switch inside the continuation (cubelib's `DR[niss=before]`): the answer key for the benchmark.
/// Calls `f(side, view moves after the EO)`.
pub fn all_drs(c: &Ctx, v: &Cubie, last: [u8; 2], budget: usize, f: &mut dyn FnMut(usize, &[u8])) {
    fn dfs(c: &Ctx, co: usize, sl: usize, left: usize, last: u8, path: &mut Vec<u8>, side: usize, f: &mut dyn FnMut(usize, &[u8])) {
        let d = c.drdist[co * NSL + sl] as usize;
        if d == 0 {
            // a half turn among the last turns about one axis could have been left out (it commutes to the end
            // and a half turn keeps DR): that is a shorter DR plus a half turn, not a DR of its own
            let ax = path.last().map(|&m| m / 6);
            let redundant = path.iter().rev().take_while(|&&m| Some(m / 6) == ax).any(|&m| m % 3 == 1);
            if !redundant {
                f(side, path);
            }
            return;
        }
        if d > left {
            return;
        }
        for &mv in &EOKEEP {
            // against the EO's own last turn only the same face is excluded (B then F2 is a continuation of its own)
            let ok = if path.is_empty() { last == NONE || last / 3 != mv / 3 } else { canon_ok(last, mv) };
            if !ok {
                continue;
            }
            path.push(mv);
            dfs(c, c.co_mv[co][mv as usize] as usize, c.sl_mv[sl][mv as usize] as usize, left - 1, mv, path, side, f);
            path.pop();
        }
    }
    for side in 0..2 {
        let st = if side == 0 { *v } else { v.inverse() };
        let (co, _, sl) = c.m.coords(&st);
        dfs(c, co, sl, budget, last[side], &mut Vec::new(), side, f);
    }
}

//! One simulated attempt: a clock, a policy, and the search.
//!
//! Every state the solver examines is a *step* with a cost in milliseconds, appended to the log; the clock is the
//! sum of the log.  The steps:
//!
//!   0 look      count the bad edges on the three axes
//!   1 eo_scan   search one axis for EOs one move longer than before
//!   2 eo_write  write down an EO that was found
//!   3 eo_eval   glance at an EO: its DRM on both DR axes for each ending, and any DR that is in plain sight
//!   4 rzp       work one RZP state
//!   5 switch    work a state on the other side (set up the inverse)
//!   6 dr_find   write down a DR that was seen
//!   7 dr_read   read a DR: its subset, for the last turn either way
//!   8 htr       try one route to HTR on a DR
//!   9 tail      write out the finish a route gave
//!  10 write     write the full solution down and check it
//!
//! The policy only uses what those steps reveal: lengths, bad edges per axis, DRMs, the subset of a DR that has
//! been read, the finishes found.

use crate::conf::{Costs, Human, Policy};
use crate::ctx::*;
use crate::cubie::{Cubie, SOLVED};
use crate::eo::EoGroup;
use crate::finish::*;
use crate::line::{DrCand, LineSearch, Step as LStep};
use crate::rngx::{h2, normal, unif};
use std::cell::RefCell;
use std::collections::{HashMap, VecDeque};
use std::rc::Rc;

pub const KIND_NAME: [&str; 11] = ["look", "eo_scan", "eo_write", "eo_eval", "rzp", "switch", "dr_find", "dr_read", "htr", "tail", "write"];

/// Everything about one scramble that does not depend on the policy.
pub struct World<'a> {
    pub c: &'a Ctx,
    pub lists: &'a [Vec<Step>],
    pub id: u64,
    pub seed: u64,
    pub scramble: Vec<u8>,
    pub s: Cubie,
    pub bad: [u32; 3],
    pub max_eo: usize,
    pub eos: Vec<EoGroup>,
    /// scramble features a solver sees early (for the adaptive-budget analysis): the shortest EO of any kind
    /// (`max_eo + 1` if there is none up to `max_eo`), and the number of EOs (groups) of at most 4 moves, all kinds and
    /// with moves on one side only
    pub eo_min: u8,
    pub n_eo4: u32,
    pub n_eo4_lin: u32,
    rt_cache: RefCell<HashMap<(usize, usize, usize), Rc<RouteTable>>>,
}

impl<'a> World<'a> {
    pub fn new(c: &'a Ctx, lists: &'a [Vec<Step>], id: u64, seed: u64, scramble: &[u8], max_eo: usize) -> World<'a> {
        let s = c.apply(&SOLVED, scramble);
        let mut bad = [0u32; 3];
        for y in 0..3 {
            bad[y] = c.m.conj(&s, c.rot_eo[y]).ef.iter().map(|&f| f as u32).sum();
        }
        let eos = crate::eo::enumerate(c, &s, max_eo.max(4), true);
        let eo_min = eos.iter().map(|g| g.len).min().unwrap_or(max_eo.max(4) as u8 + 1);
        let n_eo4 = eos.iter().filter(|g| g.len <= 4).count() as u32;
        let n_eo4_lin = eos.iter().filter(|g| g.len <= 4 && g.kind != 2).count() as u32;
        let eos: Vec<EoGroup> = eos.into_iter().filter(|g| g.len as usize <= max_eo).collect();
        World {
            c, lists, id, seed: h2(seed, id), scramble: scramble.to_vec(), s, bad, max_eo, eos, eo_min, n_eo4, n_eo4_lin,
            rt_cache: RefCell::new(HashMap::new()),
        }
    }
    pub fn routes(&self, st: (usize, usize, usize)) -> Rc<RouteTable> {
        if let Some(v) = self.rt_cache.borrow().get(&st) {
            return v.clone();
        }
        let v = Rc::new(route_table(self.c, st));
        self.rt_cache.borrow_mut().insert(st, v.clone());
        v
    }
}

struct LineSlot {
    search: LineSearch,
    done: bool,
}
struct FoundEo {
    g: usize,
    evaluated: bool,
    lines: Vec<LineSlot>,
    budget: usize,
    worked: usize,
    done: bool,
}
struct Variant {
    n: Vec<u8>,
    i: Vec<u8>,
    st: (usize, usize, usize),
    sub: usize,
    vkey: u64,
    next: usize,
}
struct FoundDr {
    cand: DrCand,
    rot: usize,
    vars: Vec<Variant>,
    read: bool,
    started: bool,
    tries: usize,
    done: bool,
    key: u64,
    /// clock when the DR was written down
    t_found: u64,
}

#[derive(Clone, Debug, Default)]
pub struct Outcome {
    /// HTM of the solution that was written down in time; 0 = DNF
    pub len: usize,
    pub moves: Vec<u8>,
    pub t_end: u64,
    pub count: [u32; 11],
    pub time: [u64; 11],
    pub eos_found: u32,
    pub drs_found: u32,
    pub drs_finished: u32,
    pub best_dr: u32,
    pub first_sol_t: u64,
    pub first_sol_len: u32,
    pub best_found: u32,
    /// DR of the result: length, subset, exact optimal finish, finish used
    pub res_dr_len: u32,
    pub res_sub: u32,
    pub res_exact: u32,
    pub res_fin: u32,
    /// clock when the result's DR was written down, when the result's finish was written out (0 = DNF), when the
    /// last EO and the last new DR were written down (0 = none)
    pub res_dr_t: u64,
    pub res_sol_t: u64,
    pub last_eo_t: u64,
    pub last_dr_t: u64,
    /// best DR length + exact optimal finish over every DR on the page (0 = no DR)
    pub oracle_page: u32,
    pub log: Vec<(u8, u32)>,
    /// (clock, length, moves) of every full solution found, in order
    pub sols: Vec<(u64, u32, Vec<u8>)>,
    /// (clock when the writing ended, length) of every solution written down
    pub banks: Vec<(u64, u32)>,
    pub replay_fail: u32,
}

#[derive(Clone)]
struct Sol {
    len: usize,
    moves: Vec<u8>,
    dr_len: u32,
    sub: u32,
    exact: u32,
    fin: u32,
    dr_t: u64,
    t: u64,
}

pub struct Attempt<'a, 'w> {
    w: &'w World<'a>,
    c: &'a Ctx,
    cost: &'a Costs,
    hum: &'w Human,
    pol: &'a Policy,
    t: u64,
    budget: u64,
    scan_depth: [usize; 3],
    axis_order: [usize; 3],
    pending: VecDeque<usize>,
    eos: Vec<FoundEo>,
    drs: Vec<FoundDr>,
    dr_index: HashMap<(usize, (usize, usize, usize)), usize>,
    best: Option<Sol>,
    banked: Option<Sol>,
    out: Outcome,
    keep_log: bool,
    /// how many times the solver has gone back over its EOs to look deeper
    pass: usize,
    /// this attempt's pace: every step's time is multiplied by it (log-normal, fixed per scramble)
    speed: f64,
    /// the policy's clock times are written for a one-hour attempt; with another budget they scale with it
    tk: f64,
}

enum EoWork {
    Write,
    Scan(usize, usize),
}

impl<'a, 'w> Attempt<'a, 'w> {
    pub fn new(w: &'w World<'a>, cost: &'a Costs, hum: &'w Human, pol: &'a Policy, keep_log: bool) -> Self {
        let mut axis_order = [0usize, 1, 2];
        axis_order.sort_by_key(|&y| (w.bad[y], y));
        let sa = cost.attempt_sigma;
        let speed = (sa * normal(h2(w.seed, 0x5BEED)) - sa * sa / 2.0).exp();
        Attempt {
            speed,
            tk: cost.budget / 3600.0,
            w, c: w.c, cost, hum, pol, t: 0, budget: (cost.budget * 1000.0).round() as u64,
            scan_depth: [0; 3], axis_order, pending: VecDeque::new(), eos: Vec::new(), drs: Vec::new(), dr_index: HashMap::new(),
            best: None, banked: None, out: Outcome::default(), keep_log, pass: 0,
        }
    }

    /// One step: its nominal cost times a log-normal factor fixed by (scramble, kind, object).
    fn pay(&mut self, kind: usize, nominal: f64, key: u64) {
        let sg = self.cost.noise_sigma;
        let z = normal(h2(h2(self.w.seed, 0xC057 + kind as u64), key));
        let ms = (1000.0 * nominal * self.speed * (sg * z - sg * sg / 2.0).exp()).round().max(0.0) as u64;
        self.t += ms;
        self.out.count[kind] += 1;
        self.out.time[kind] += ms;
        if self.keep_log {
            self.out.log.push((kind as u8, ms as u32));
        }
    }

    // ------------------------------------------------------------------------------------------------ EO
    fn eo_target(&self) -> usize {
        let p = self.pol;
        let mut target = p.eo_len;
        if p.eo_len_poor > p.eo_len && self.scan_depth.iter().all(|&d| d >= p.eo_len) && self.pending.is_empty() && self.eos.len() < p.poor_n {
            target = p.eo_len_poor;
        }
        target.min(self.w.max_eo)
    }
    fn next_scan(&self, target: usize) -> Option<(usize, usize)> {
        for level in 1..=target {
            for &y in &self.axis_order {
                if self.scan_depth[y] < level {
                    return Some((y, level));
                }
            }
        }
        None
    }
    fn eo_work(&self, target: usize) -> Option<EoWork> {
        if !self.pending.is_empty() {
            return Some(EoWork::Write);
        }
        self.next_scan(target).map(|(y, l)| EoWork::Scan(y, l))
    }
    fn do_eo(&mut self, w: EoWork) {
        match w {
            EoWork::Scan(y, level) => self.scan_step(y, level),
            EoWork::Write => self.write_eo(),
        }
    }
    fn scan_step(&mut self, y: usize, level: usize) {
        let f = if self.pol.eo_niss { self.cost.eo_niss_factor } else { 1.0 };
        self.pay(1, self.cost.eo_scan[level.min(7)] * f, (y * 16 + level) as u64);
        self.scan_depth[y] = level;
        let w = self.w;
        let mut seen: Vec<(u64, usize)> = Vec::new();
        for (gi, g) in w.eos.iter().enumerate() {
            // level 1 also shows an EO that is already solved
            if g.axis as usize != y || !(g.len as usize == level || (level == 1 && g.len == 0)) {
                continue;
            }
            if g.kind == 2 && !self.pol.eo_niss {
                continue;
            }
            let p = if g.kind == 2 { self.hum.eo_see_niss[level.min(7)] } else { self.hum.eo_see_lin[level.min(7)] };
            if unif(h2(h2(w.seed, 0xE05E), g.key)) < p {
                seen.push((h2(h2(w.seed, 0xE0AD), g.key), gi));
            }
        }
        seen.sort();
        self.pending.extend(seen.into_iter().map(|(_, gi)| gi));
    }
    fn write_eo(&mut self) {
        let gi = self.pending.pop_front().unwrap();
        self.pay(2, self.cost.eo_write, self.w.eos[gi].key);
        self.eos.push(FoundEo { g: gi, evaluated: false, lines: Vec::new(), budget: 0, worked: 0, done: false });
        self.out.eos_found += 1;
        self.out.last_eo_t = self.t;
        let w = self.w;
        self.eos.sort_by_key(|e| w.eos[e.g].len); // shortest first (stable)
    }

    // ------------------------------------------------------------------------------------------------ RZP / DR
    fn dr_work(&self) -> Option<usize> {
        self.eos.iter().position(|e| !e.done)
    }
    fn dr_step(&mut self, ei: usize) {
        let w = self.w;
        let (pol, hum, c) = (self.pol, self.hum, self.c);
        let g = &w.eos[self.eos[ei].g];
        if !self.eos[ei].evaluated {
            // the glance: every ending and both DR axes
            self.pay(3, self.cost.eo_eval, g.key);
            let y = g.axis as usize;
            let mut lines: Vec<LineSlot> = Vec::new();
            for root in &g.roots {
                for x in 0..3 {
                    if x != y {
                        lines.push(LineSlot { search: LineSearch::new(c, hum, &w.s, root, y, x, g.len, w.seed), done: false });
                    }
                }
            }
            for (li, l) in lines.iter_mut().enumerate() {
                if let LStep::Looked(_, Some(cd)) = l.search.step(c, hum, pol.rzp_depth, pol.switch_pen, pol.dr_cap) {
                    let key = h2(g.key, (li as u64) << 32);
                    self.pay(6, self.cost.dr_find[(cd.d_seen as usize).min(7)], key);
                    self.add_dr(cd);
                    l.done = true;
                }
            }
            let e = &mut self.eos[ei];
            e.evaluated = true;
            e.budget = if g.len as usize <= pol.rzp_short { pol.rzp_per_eo } else { pol.rzp_per_eo_long };
            e.lines = lines;
            let open = self.next_node(ei).is_some();
            self.eos[ei].done = !open;
            return;
        }
        let Some(li) = self.next_node(ei) else {
            self.eos[ei].done = true;
            return;
        };
        let res = self.eos[ei].lines[li].search.step(c, hum, pol.rzp_depth, pol.switch_pen, pol.dr_cap);
        self.eos[ei].worked += 1;
        match res {
            LStep::Exhausted => self.eos[ei].lines[li].done = true,
            LStep::Looked(sw, cand) => {
                let key = h2(g.key, (li as u64) << 32 | self.eos[ei].lines[li].search.examined as u64);
                if sw {
                    self.pay(5, self.cost.switch, key);
                } else {
                    self.pay(4, self.cost.rzp, key);
                }
                if let Some(cd) = cand {
                    self.pay(6, self.cost.dr_find[(cd.d_seen as usize).min(7)], key);
                    self.add_dr(cd);
                }
                if self.eos[ei].lines[li].search.found >= pol.dr_per_line + self.pass {
                    self.eos[ei].lines[li].done = true;
                }
            }
        }
        if self.next_node(ei).is_none() {
            self.eos[ei].done = true;
        }
    }

    /// The line of an EO whose best unworked RZP state is the most promising, if the EO still has budget and
    /// that state's read is good enough.
    fn next_node(&self, ei: usize) -> Option<usize> {
        let e = &self.eos[ei];
        if e.worked >= e.budget {
            return None;
        }
        let read_max = self.pol.read_max + self.pass as f64;
        let mut best: Option<(f64, usize)> = None;
        for (li, l) in e.lines.iter().enumerate() {
            if l.done {
                continue;
            }
            if let Some((rank, total)) = l.search.peek() {
                if total <= read_max && best.map_or(true, |b| rank < b.0) {
                    best = Some((rank, li));
                }
            }
        }
        best.map(|b| b.1)
    }

    /// Out of things to examine: go back over every EO with `rzp_more` more RZP states and a read limit one higher.
    fn deepen(&mut self) -> bool {
        if self.pass >= 4 || self.pol.rzp_more == 0 {
            return false;
        }
        self.pass += 1;
        let (w, pol) = (self.w, self.pol);
        for e in self.eos.iter_mut().filter(|e| e.evaluated) {
            let base = if w.eos[e.g].len as usize <= pol.rzp_short { pol.rzp_per_eo } else { pol.rzp_per_eo_long };
            e.budget = base + self.pass * pol.rzp_more;
            for l in e.lines.iter_mut() {
                l.done = false;
            }
        }
        let mut any = false;
        for ei in 0..self.eos.len() {
            if self.eos[ei].evaluated {
                let open = self.next_node(ei).is_some();
                self.eos[ei].done = !open;
                any |= open;
            }
        }
        any
    }

    fn dr_state(&self, n: &[u8], i: &[u8], rot: usize) -> (usize, usize, usize) {
        let v = self.c.m.conj(&self.c.state_ni(&self.w.s, n, i), rot);
        self.c.dr_coords(&v).unwrap_or_else(|| fatal!("not a DR: {} / ({})", text(n), text(i)))
    }

    fn add_dr(&mut self, cd: DrCand) {
        let c = self.c;
        let rot = c.rot_pair[cd.x as usize][cd.y as usize];
        let mut seqs = vec![(cd.n.clone(), cd.i.clone())];
        if let Some(fs) = cd.flip_side {
            let (mut n, mut i) = (cd.n.clone(), cd.i.clone());
            let l = if fs == 0 { n.last_mut() } else { i.last_mut() };
            let l = l.unwrap();
            *l = inv_move(*l);
            seqs.push((n, i));
        }
        let mut vars: Vec<Variant> = Vec::new();
        for (n, i) in seqs {
            let st = self.dr_state(&n, &i, rot);
            let cn = c.dr_canon(st);
            let vkey = h2(h2(self.w.seed, 0x47 + cd.x as u64), (cn.0 * 40320 + cn.1) as u64 * 24 + cn.2 as u64);
            vars.push(Variant { sub: c.sub48(st.0, st.1), n, i, st, vkey, next: 0 });
        }
        let dkey = (cd.x as usize, c.dr_canon(vars[0].st));
        if let Some(&j) = self.dr_index.get(&dkey) {
            if self.drs[j].cand.len <= cd.len {
                return; // the same DR again
            }
            self.drs[j].done = true; // a shorter way to the same DR replaces the old entry
        }
        // a DR and its twin are one entry, named by the smaller of the two states
        let km = vars.iter().map(|v| c.dr_canon(v.st)).min().unwrap();
        let key = h2(h2(self.w.seed, 0xD2 + cd.x as u64), (km.0 * 40320 + km.1) as u64 * 24 + km.2 as u64);
        self.out.drs_found += 1;
        if self.out.best_dr == 0 || (cd.len as u32) < self.out.best_dr {
            self.out.best_dr = cd.len as u32;
        }
        let j = self.drs.len();
        for v in &vars {
            self.dr_index.insert((cd.x as usize, c.dr_canon(v.st)), j);
        }
        self.out.last_dr_t = self.t;
        self.drs.push(FoundDr { cand: cd, rot, vars, read: false, started: false, tries: 0, done: false, key, t_found: self.t });
        if self.pol.read_on_find {
            self.pay(7, self.cost.dr_read, key);
            self.drs[j].read = true;
        }
    }

    // ------------------------------------------------------------------------------------------------ finishing
    /// Expected total of a DR from what has been read of it.
    fn est(&self, d: &FoundDr) -> f64 {
        if d.read {
            d.cand.len as f64 + d.vars.iter().map(|v| self.c.sub_mean[v.sub]).fold(f64::MAX, f64::min)
        } else {
            d.cand.len as f64 + self.c.all_mean
        }
    }
    /// Chance, by subset, that the DR's optimal finish beats the best solution so far.
    fn p_improve(&self, d: &FoundDr) -> f64 {
        let Some(b) = &self.best else { return 1.0 };
        let need = b.len as i64 - 1 - d.cand.len as i64;
        if need < 0 {
            return 0.0;
        }
        let k = (need as usize).min(20);
        if d.read {
            d.vars.iter().map(|v| self.c.sub_cdf[v.sub][k]).fold(0.0, f64::max)
        } else {
            self.c.all_cdf[k]
        }
    }
    /// The DR to work on next: lowest expected total among those worth it.  `eager`: only DRs good enough to be
    /// finished ahead of the finishing phase, and only their first `eager_routes` routes.
    fn pick_finish(&self, eager: bool) -> Option<usize> {
        let p = self.pol;
        let started = self.drs.iter().filter(|d| d.started).count();
        let mut best: Option<(usize, f64)> = None;
        for (j, d) in self.drs.iter().enumerate() {
            if d.done || (!d.started && started >= p.fin_max) {
                continue;
            }
            if self.p_improve(d) < p.fin_min_p {
                continue;
            }
            let e = self.est(d);
            if eager && !(e <= p.eager_finish && d.tries < p.eager_routes) {
                continue;
            }
            if best.map_or(true, |b| e < b.1) {
                best = Some((j, e));
            }
        }
        best.map(|b| b.0)
    }

    fn finish_step(&mut self, j: usize) {
        let (c, w) = (self.c, self.w);
        if !self.drs[j].read {
            let key = self.drs[j].key;
            self.pay(7, self.cost.dr_read, key);
            self.drs[j].read = true;
            return;
        }
        // the next route: over the two endings, the one whose next checklist line finds the optimal most often
        let mut pick: Option<(f64, usize)> = None;
        for (vi, v) in self.drs[j].vars.iter().enumerate() {
            if let Some(st) = w.lists[v.sub].get(v.next) {
                if pick.map_or(true, |p| st.marginal > p.0) {
                    pick = Some((st.marginal, vi));
                }
            }
        }
        let Some((_, vi)) = pick else {
            self.drs[j].done = true;
            return;
        };
        if !self.drs[j].started {
            self.drs[j].started = true;
            self.out.drs_finished += 1;
        }
        let (vkey, step, sub, st) = {
            let v = &mut self.drs[j].vars[vi];
            v.next += 1;
            (v.vkey, v.next - 1, v.sub, v.st)
        };
        self.pay(8, self.cost.htr, h2(vkey, step as u64));
        self.drs[j].tries += 1;
        let rt = w.routes(st);
        if let Some((_, fin)) = rt.best.get(&w.lists[sub][step].key) {
            if unif(h2(vkey, 1000 + step as u64)) < self.hum.route_see {
                self.pay(9, self.cost.tail, h2(vkey, step as u64));
                let own = dr_to_own(c, self.drs[j].rot, fin);
                let v = &self.drs[j].vars[vi];
                let mut full = v.n.clone();
                full.extend(&own);
                full.extend(invert(&v.i));
                let full = cancel(&full);
                if c.apply(&w.s, &full) != SOLVED {
                    self.out.replay_fail += 1;
                } else {
                    self.out.sols.push((self.t, full.len() as u32, full.clone()));
                    if self.out.first_sol_len == 0 {
                        self.out.first_sol_len = full.len() as u32;
                        self.out.first_sol_t = self.t;
                    }
                    if self.best.as_ref().map_or(true, |b| full.len() < b.len) {
                        self.best = Some(Sol {
                            len: full.len(), moves: full, dr_len: self.drs[j].cand.len as u32, sub: sub as u32, exact: rt.d as u32,
                            fin: fin.len() as u32, dr_t: self.drs[j].t_found, t: self.t,
                        });
                    }
                }
            }
        }
        if self.drs[j].tries >= self.pol.htr_per_dr {
            self.drs[j].done = true;
        }
    }

    fn bank(&mut self) {
        let s = self.best.clone().unwrap();
        self.pay(10, self.cost.write, self.out.banks.len() as u64 + 1);
        self.out.banks.push((self.t, s.len as u32));
        if self.t <= self.budget {
            self.banked = Some(s);
        }
    }

    fn better(&self) -> bool {
        match (&self.best, &self.banked) {
            (Some(b), Some(k)) => b.len < k.len,
            (Some(_), None) => true,
            _ => false,
        }
    }

    pub fn run(mut self) -> Outcome {
        let p = self.pol;
        self.pay(0, self.cost.look, 0);
        let write_ms = (self.cost.write * 1000.0) as u64;
        let tk = self.tk;
        let mut guard = 0u32;
        loop {
            guard += 1;
            if self.t >= self.budget || guard > 2_000_000 {
                break;
            }
            let left = self.budget - self.t;
            let better = self.better();
            // the time kept for writing: `reserve`, or `reserve_rewrite` once a solution is on the sheet (a rewrite that
            // runs over the hour leaves the old solution standing)
            let rs = self.cost.reserve_scale * 1000.0;
            let reserve = if self.banked.is_some() { (p.reserve_rewrite * rs) as u64 } else { (p.reserve * rs) as u64 };
            let bl = self.best.as_ref().map_or(99, |b| b.len);
            if better && (left <= reserve || p.bank_always || (p.bank_first && self.banked.is_none()) || (p.bank_at > 0 && bl <= p.bank_at)) {
                self.bank();
                continue;
            }
            let desperate = left <= reserve && self.best.is_none() && left > write_ms;
            if left <= reserve && !desperate {
                break;
            }
            if p.stop_at > 0 && self.banked.as_ref().map_or(false, |b| b.len <= p.stop_at) {
                break;
            }
            let ts = self.t as f64 / 1000.0;
            let fin = self.pick_finish(false);
            let fin_eager = if p.eager_finish > 0.0 { self.pick_finish(true) } else { None };
            let line = self.dr_work();
            let target = self.eo_target();
            let eo = if self.eos.len() >= p.eo_cap { None } else { self.eo_work(target) };
            let eo_over = ts >= p.t_eo * tk || eo.is_none();
            let mut t_dr = p.t_dr * tk;
            if p.rich_n > 0 && p.t_dr_rich > 0.0 && self.eos.len() >= p.rich_n {
                t_dr = p.t_dr_rich * tk;
            }
            if p.t_dr_backup > 0.0 && self.banked.as_ref().map_or(false, |b| b.len <= p.backup_len) {
                t_dr = t_dr.max(p.t_dr_backup * tk);
            }
            if p.t_dr_late > 0.0 && ts >= t_dr && (self.out.best_dr == 0 || self.out.best_dr as usize > p.late_len) {
                t_dr = t_dr.max(p.t_dr_late * tk);
            }
            let enough = p.dr_enough > 0 && self.drs.iter().filter(|d| d.cand.len as usize <= p.dr_enough_len).count() >= p.dr_enough;
            let dr_over = ts >= t_dr || enough || desperate;
            let backup_due = p.backup_time > 0.0 && self.best.is_none() && ts >= p.backup_time * tk;
            // 1. finishing, when it is due
            if let Some(j) = fin {
                if dr_over || backup_due || (line.is_none() && eo_over) {
                    self.finish_step(j);
                    continue;
                }
            }
            if let Some(j) = fin_eager {
                self.finish_step(j);
                continue;
            }
            // 2. DRs
            if let Some(e) = line {
                let eager = self.w.eos[self.eos[e].g].len as usize <= p.eager_eo;
                if !dr_over && (eo_over || eager) {
                    self.dr_step(e);
                    continue;
                }
            }
            // 3. EOs
            if let Some(wk) = eo {
                if !eo_over && !dr_over {
                    self.do_eo(wk);
                    continue;
                }
                // 4. nothing is due in the planned order: do what is left, most downstream first
                if fin.is_none() && line.is_none() {
                    self.do_eo(wk);
                    continue;
                }
            }
            if let Some(j) = fin {
                self.finish_step(j);
                continue;
            }
            if let Some(e) = line {
                self.dr_step(e);
                continue;
            }
            if let Some(wk) = self.eo_work(self.w.max_eo) {
                self.do_eo(wk);
                continue;
            }
            if self.deepen() {
                continue;
            }
            // nothing at all left to examine
            if better {
                self.bank();
            }
            break;
        }
        // a last chance to write down what was found (it counts only if it ends inside the hour)
        if self.better() && self.t < self.budget {
            self.bank();
        }
        let mut out = self.out;
        out.t_end = self.t;
        out.best_found = self.best.as_ref().map_or(0, |b| b.len as u32);
        if let Some(b) = &self.banked {
            out.len = b.len;
            out.moves = b.moves.clone();
            out.res_dr_len = b.dr_len;
            out.res_sub = b.sub;
            out.res_exact = b.exact;
            out.res_fin = b.fin;
            out.res_dr_t = b.dr_t;
            out.res_sol_t = b.t;
        }
        // the answer key for the page: best DR length + exact finish over every DR found
        let mut oracle = 0u32;
        for d in &self.drs {
            for v in &d.vars {
                if let Some(x) = self.c.exact_depth(v.st) {
                    let tot = d.cand.len as u32 + x as u32;
                    if oracle == 0 || tot < oracle {
                        oracle = tot;
                    }
                }
            }
        }
        out.oracle_page = oracle;
        out
    }
}

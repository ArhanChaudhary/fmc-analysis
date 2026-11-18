//! One simulated attempt: a clock, a plan, and the search.
//!
//! Every state the solver examines is a *step* with a time cost; the clock is the sum of the steps.  The steps:
//!
//! | kind        | what the solver does                                                                         |
//! |-------------|----------------------------------------------------------------------------------------------|
//! | look        | count the bad edges on the three axes                                                        |
//! | eo_scan     | search one axis for EOs one move longer than before                                          |
//! | eo_write    | write down an EO that was found                                                              |
//! | eo_eval     | glance at an EO: its DRM on both DR axes for each ending, and any DR in plain sight          |
//! | rzp         | work one RZP state                                                                           |
//! | switch      | work a state on the other side (set the inverse up)                                          |
//! | dr_find     | write down a DR that was seen                                                                |
//! | dr_read     | read a DR: its subset, for the last turn either way                                          |
//! | htr         | try one route to HTR on a DR                                                                 |
//! | tail        | write out the finish a route gave                                                            |
//! | write       | write the full solution down and check it                                                    |
//!
//! The plan only uses what those steps reveal: lengths, bad edges per axis, DRMs, the subset of a DR that has been
//! read, the finishes found.  When asked to, the attempt keeps a [`Step`] for each of them, saying what it was.

use crate::cube::{cancel, format_moves, invert, Cube, Move, View, DR_VIEW, EO_VIEW};
use crate::dr::{rank_perm, DrState};
use crate::eo::{enumerate, niss_text, view_state, Eo, EoKind};
use crate::finish::{dr_moves_to_cube, route_table, RouteTable};
use crate::rng::{h2, lognormal, normal, uniform};
use crate::rzp::{DrCandidate, LineSearch, LineStep, NodeInfo};
use crate::settings::{Costs, Human, Plan};
use crate::tables::Tables;
use serde::Serialize;
use std::cell::RefCell;
use std::collections::{HashMap, VecDeque};
use std::rc::Rc;

/// The kinds of step, in the order of the research program's output columns.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Serialize)]
#[serde(rename_all = "snake_case")]
pub enum StepKind {
    Look,
    EoScan,
    EoWrite,
    EoEval,
    Rzp,
    Switch,
    DrFind,
    DrRead,
    Htr,
    Tail,
    Write,
}

impl StepKind {
    pub const ALL: [StepKind; 11] = [
        StepKind::Look, StepKind::EoScan, StepKind::EoWrite, StepKind::EoEval, StepKind::Rzp, StepKind::Switch,
        StepKind::DrFind, StepKind::DrRead, StepKind::Htr, StepKind::Tail, StepKind::Write,
    ];
    pub fn name(self) -> &'static str {
        ["look", "eo_scan", "eo_write", "eo_eval", "rzp", "switch", "dr_find", "dr_read", "htr", "tail", "write"][self as usize]
    }
}

/// Everything about one scramble that does not depend on the plan.
pub struct Scramble<'t> {
    pub t: &'t Tables,
    pub moves: Vec<Move>,
    pub state: Cube,
    /// the seed of this attempt's random draws
    pub seed: u64,
    /// bad edges on R/L, U/D, F/B
    pub bad: [u32; 3],
    pub max_eo: usize,
    /// every EO up to `max_eo` moves
    pub eos: Vec<Eo>,
    /// what a solver sees early: the shortest EO of any kind (`max(max_eo, 4) + 1` if none), and the number of EOs of
    /// at most 4 moves, all kinds and with moves on one side only
    pub eo_min: usize,
    pub n_eo4: usize,
    pub n_eo4_lin: usize,
    routes: RefCell<HashMap<DrState, Rc<RouteTable>>>,
    optimal: RefCell<HashMap<DrState, u8>>,
}

impl<'t> Scramble<'t> {
    pub fn new(t: &'t Tables, moves: &[Move], seed: u64, attempt: u64, max_eo: usize) -> Scramble<'t> {
        let state = t.moves.state(moves);
        let bad = std::array::from_fn(|y| t.moves.state(&EO_VIEW[y].seq_to_view(moves)).bad_edges());
        let all = enumerate(t, moves, max_eo.max(4), true);
        let eo_min = all.iter().map(|g| g.len).min().unwrap_or(max_eo.max(4) + 1);
        let n_eo4 = all.iter().filter(|g| g.len <= 4).count();
        let n_eo4_lin = all.iter().filter(|g| g.len <= 4 && g.kind != EoKind::Niss).count();
        let eos = all.into_iter().filter(|g| g.len <= max_eo).collect();
        Scramble {
            t,
            moves: moves.to_vec(),
            state,
            seed: h2(seed, attempt),
            bad,
            max_eo,
            eos,
            eo_min,
            n_eo4,
            n_eo4_lin,
            routes: RefCell::new(HashMap::new()),
            optimal: RefCell::new(HashMap::new()),
        }
    }

    /// The routes of a DR state (computed once per scramble).
    pub fn routes(&self, st: DrState) -> Rc<RouteTable> {
        if let Some(r) = self.routes.borrow().get(&st) {
            return r.clone();
        }
        let r = Rc::new(route_table(self.t, st));
        self.optimal.borrow_mut().insert(st, r.optimal);
        self.routes.borrow_mut().insert(st, r.clone());
        r
    }

    /// The optimal finish of a DR state (computer only).
    pub fn optimal(&self, st: DrState) -> u8 {
        if let Some(&d) = self.optimal.borrow().get(&st) {
            return d;
        }
        let d = self.t.noe().optimal(&self.t.dr, st);
        self.optimal.borrow_mut().insert(st, d);
        d
    }
}

// ------------------------------------------------------------------------------------------------ what is recorded

/// One step of the attempt, for the timeline.
#[derive(Clone, Debug, Serialize)]
pub struct Step {
    /// clock at the start of the step and its length, in milliseconds
    pub start: u64,
    pub ms: u64,
    pub kind: StepKind,
    #[serde(flatten)]
    pub action: Action,
}

/// An EO as the timeline names it.
#[derive(Clone, Debug, Serialize)]
pub struct EoRef {
    /// number in the order the EOs were written down (1 = first)
    pub number: usize,
    pub text: String,
    pub axis: &'static str,
    pub kind: &'static str,
    pub len: usize,
}

/// A DR as the timeline names it.
#[derive(Clone, Debug, Serialize)]
pub struct DrRef {
    /// number in the order the DRs were written down (1 = first)
    pub number: usize,
    pub text: String,
    pub len: usize,
    pub axis: &'static str,
}

#[derive(Clone, Debug, Serialize)]
pub struct LineGlance {
    /// the EO's ending and the DR axis looked at
    pub ending: String,
    pub dr_axis: &'static str,
    pub drm: String,
    /// what the read promises: EO + read distance to DR
    pub read_total: f64,
    /// the true EO-keeping distance to DR (computer only)
    pub true_distance: usize,
}

#[derive(Clone, Debug, Serialize)]
pub struct RouteTry {
    pub route: String,
    /// the subset of the ending tried
    pub subset: String,
    /// the finish the route gave (DR moves turned into cube moves), if any
    pub finish: Option<String>,
    pub finish_len: Option<usize>,
    pub total: Option<usize>,
    /// the route had a finish this short but the solver did not find it (`route_see`)
    pub missed: bool,
    /// the DR's optimal finish (computer only)
    pub optimal: u8,
}

#[derive(Clone, Debug, Serialize)]
#[serde(tag = "type", rename_all = "snake_case")]
pub enum Action {
    Look { bad_edges: [u32; 3] },
    EoScan { axis: &'static str, length: usize, niss: bool, spotted: Vec<String> },
    EoWrite { eo: EoRef },
    EoGlance { eo: EoRef, lines: Vec<LineGlance> },
    Rzp { eo: EoRef, dr_axis: &'static str, side: &'static str, node: NodeView },
    Switch { eo: EoRef, dr_axis: &'static str, side: &'static str, node: NodeView },
    DrFind { dr: DrRef, eo: EoRef, seen_from: usize, rzp_moves: usize, switched: bool, outcome: &'static str },
    DrRead { dr: DrRef, subsets: Vec<String> },
    Htr { dr: DrRef, attempt: RouteTry },
    Tail { dr: DrRef, solution: String, len: usize, best_so_far: bool },
    Write { len: usize, solution: String, in_time: bool },
}

/// An RZP state as the timeline shows it.
#[derive(Clone, Debug, Serialize)]
pub struct NodeView {
    /// the RZP moves after the EO on the side it ended on, and (after a switch) on the other side
    pub moves: String,
    pub switched: bool,
    pub moves_after_switch: String,
    pub read_total: f64,
    pub true_distance: usize,
    pub drm: String,
}

/// A full solution found during the attempt.
#[derive(Clone, Debug, Serialize)]
pub struct Solution {
    /// clock when its finish was written out
    pub found_at: u64,
    pub len: usize,
    pub moves: String,
    /// the parts: EO, DR (normal and inverse moves of the whole skeleton), the finish
    pub eo: String,
    pub eo_len: usize,
    pub dr_normal: String,
    pub dr_inverse: String,
    pub dr_len: usize,
    pub dr_axis: &'static str,
    pub subset: String,
    pub route: String,
    pub finish: String,
    pub finish_len: usize,
    /// the DR's optimal finish (computer only)
    pub optimal_finish: u8,
    /// clock when the DR was written down
    pub dr_found_at: u64,
    /// clock when it was written on the sheet, if it was
    pub written_at: Option<u64>,
}

/// What happened, in numbers (one row of the research program's output).
#[derive(Clone, Debug, Default, Serialize)]
pub struct Outcome {
    /// HTM of the solution written down in time; 0 = DNF
    pub len: usize,
    pub moves: Vec<Move>,
    pub t_end: u64,
    pub budget_ms: u64,
    pub count: [u32; 11],
    pub time: [u64; 11],
    pub eos_found: u32,
    pub drs_found: u32,
    pub drs_finished: u32,
    pub best_dr: u32,
    pub first_sol_t: u64,
    pub first_sol_len: u32,
    pub best_found: u32,
    /// the result's DR: length, subset, optimal finish, finish used; clocks when the DR and the finish were found
    pub res_dr_len: u32,
    pub res_subset: Option<usize>,
    pub res_optimal: u32,
    pub res_fin: u32,
    pub res_dr_t: u64,
    pub res_sol_t: u64,
    /// clocks when the last EO and the last new DR were written down (0 = none)
    pub last_eo_t: u64,
    pub last_dr_t: u64,
    /// best DR length + optimal finish over every DR on the page (0 = no DR): what a computer would make of the page
    pub oracle_page: u32,
    /// (clock when the writing ended, length) of every solution written down
    pub writes: Vec<(u64, u32)>,
    pub replay_failures: u32,
}

/// The attempt with everything recorded.
pub struct Report {
    pub outcome: Outcome,
    pub steps: Vec<Step>,
    pub solutions: Vec<Solution>,
}

// ------------------------------------------------------------------------------------------------ the attempt

struct LineSlot {
    search: LineSearch,
    done: bool,
}

struct FoundEo {
    /// index into the scramble's EO list
    g: usize,
    evaluated: bool,
    lines: Vec<LineSlot>,
    budget: usize,
    worked: usize,
    done: bool,
}

/// One ending of a DR (the last quarter turn either way).
struct Variant {
    normal: Vec<Move>,
    inverse: Vec<Move>,
    st: DrState,
    subset: usize,
    key: u64,
    next_route: usize,
}

struct FoundDr {
    cand: DrCandidate,
    /// the EO it came from (index into the scramble's EO list)
    eo: usize,
    view: View,
    variants: Vec<Variant>,
    read: bool,
    started: bool,
    tries: usize,
    done: bool,
    key: u64,
    /// clock when it was written down
    found_at: u64,
}

#[derive(Clone)]
struct Sol {
    len: usize,
    moves: Vec<Move>,
    dr_len: u32,
    subset: usize,
    optimal: u32,
    fin: u32,
    dr_t: u64,
    /// index into the solutions found
    index: usize,
}

enum EoWork {
    Write,
    Scan { axis: usize, level: usize },
}

pub struct Attempt<'s, 't> {
    w: &'s Scramble<'t>,
    t: &'t Tables,
    cost: &'s Costs,
    hum: Human,
    plan: &'s Plan,
    clock: u64,
    budget: u64,
    scan_depth: [usize; 3],
    axis_order: [usize; 3],
    pending: VecDeque<usize>,
    eos: Vec<FoundEo>,
    eo_number: HashMap<usize, usize>,
    drs: Vec<FoundDr>,
    dr_index: HashMap<(usize, DrState), usize>,
    best: Option<Sol>,
    banked: Option<Sol>,
    out: Outcome,
    /// how many times the solver has gone back over its EOs to look deeper
    pass: usize,
    /// this attempt's pace: every step's time is multiplied by it
    speed: f64,
    /// the plan's clock times are for a one-hour attempt; with another budget they scale with it
    time_scale: f64,
    record: bool,
    steps: Vec<Step>,
    solutions: Vec<Solution>,
}

impl<'s, 't> Attempt<'s, 't> {
    /// `record`: keep a [`Step`] for everything the solver does.
    pub fn new(w: &'s Scramble<'t>, cost: &'s Costs, human: &Human, plan: &'s Plan, record: bool) -> Self {
        let mut axis_order = [0usize, 1, 2];
        axis_order.sort_by_key(|&y| (w.bad[y], y));
        // this attempt's form, the same under every plan
        let hum = human.on_form(normal(h2(w.seed, 0xF0F0)));
        let speed = lognormal(cost.attempt_sigma, normal(h2(w.seed, 0x5BEED)));
        Attempt {
            w,
            t: w.t,
            cost,
            hum,
            plan,
            clock: 0,
            budget: (cost.budget * 1000.0).round() as u64,
            scan_depth: [0; 3],
            axis_order,
            pending: VecDeque::new(),
            eos: Vec::new(),
            eo_number: HashMap::new(),
            drs: Vec::new(),
            dr_index: HashMap::new(),
            best: None,
            banked: None,
            out: Outcome::default(),
            pass: 0,
            speed,
            time_scale: cost.budget / 3600.0,
            record,
            steps: Vec::new(),
            solutions: Vec::new(),
        }
    }

    /// One step: its nominal cost times a log-normal factor fixed by (scramble, kind, object).
    fn pay(&mut self, kind: StepKind, nominal: f64, key: u64, action: impl FnOnce(&Self) -> Action) {
        let sigma = self.cost.noise_sigma;
        let z = normal(h2(h2(self.w.seed, 0xC057 + kind as u64), key));
        let ms = libm::round(1000.0 * nominal * self.speed * lognormal(sigma, z)).max(0.0) as u64;
        let start = self.clock;
        self.clock += ms;
        self.out.count[kind as usize] += 1;
        self.out.time[kind as usize] += ms;
        if self.record {
            let action = action(self);
            self.steps.push(Step { start, ms, kind, action });
        }
    }

    // -------------------------------------------------------------------------------- names for the timeline

    fn eo_ref(&self, g: usize) -> EoRef {
        let e = &self.w.eos[g];
        EoRef {
            number: self.eo_number.get(&g).copied().unwrap_or(0),
            text: e.text(),
            axis: crate::cube::AXIS_NAMES[e.axis],
            kind: e.kind.name(),
            len: e.len,
        }
    }

    fn dr_ref(&self, j: usize) -> DrRef {
        let d = &self.drs[j];
        DrRef {
            number: j + 1,
            text: niss_text(&d.cand.normal, &d.cand.inverse),
            len: d.cand.len,
            axis: crate::cube::AXIS_NAMES[d.cand.dr_axis],
        }
    }

    // -------------------------------------------------------------------------------- EO

    fn eo_target(&self) -> usize {
        let p = self.plan;
        let mut target = p.eo_len;
        if p.eo_len_poor > p.eo_len
            && self.scan_depth.iter().all(|&d| d >= p.eo_len)
            && self.pending.is_empty()
            && self.eos.len() < p.poor_n
        {
            target = p.eo_len_poor;
        }
        target.min(self.w.max_eo)
    }

    fn next_scan(&self, target: usize) -> Option<EoWork> {
        for level in 1..=target {
            for &axis in &self.axis_order {
                if self.scan_depth[axis] < level {
                    return Some(EoWork::Scan { axis, level });
                }
            }
        }
        None
    }

    fn eo_work(&self, target: usize) -> Option<EoWork> {
        if !self.pending.is_empty() {
            return Some(EoWork::Write);
        }
        self.next_scan(target)
    }

    fn do_eo(&mut self, work: EoWork) {
        match work {
            EoWork::Scan { axis, level } => self.scan(axis, level),
            EoWork::Write => self.write_eo(),
        }
    }

    fn scan(&mut self, axis: usize, level: usize) {
        let niss = self.plan.eo_niss;
        let factor = if niss { self.cost.eo_niss_factor } else { 1.0 };
        self.pay(StepKind::EoScan, self.cost.eo_scan[level.min(7)] * factor, (axis * 16 + level) as u64, |_| Action::EoScan {
            axis: crate::cube::AXIS_NAMES[axis],
            length: level,
            niss,
            spotted: Vec::new(),
        });
        self.scan_depth[axis] = level;
        let w = self.w;
        let mut seen: Vec<(u64, usize)> = Vec::new();
        for (gi, g) in w.eos.iter().enumerate() {
            // level 1 also shows an EO that is already solved
            if g.axis != axis || !(g.len == level || (level == 1 && g.len == 0)) {
                continue;
            }
            if g.kind == EoKind::Niss && !niss {
                continue;
            }
            let chance = if g.kind == EoKind::Niss { self.hum.eo_see_niss[level.min(7)] } else { self.hum.eo_see_lin[level.min(7)] };
            if uniform(h2(h2(w.seed, 0xE05E), g.key)) < chance {
                seen.push((h2(h2(w.seed, 0xE0AD), g.key), gi));
            }
        }
        seen.sort();
        if self.record {
            if let Some(Step { action: Action::EoScan { spotted, .. }, .. }) = self.steps.last_mut() {
                *spotted = seen.iter().map(|&(_, gi)| w.eos[gi].text()).collect();
            }
        }
        self.pending.extend(seen.into_iter().map(|(_, gi)| gi));
    }

    fn write_eo(&mut self) {
        let g = self.pending.pop_front().unwrap();
        let number = self.eo_number.len() + 1;
        self.eo_number.insert(g, number);
        self.pay(StepKind::EoWrite, self.cost.eo_write, self.w.eos[g].key, |a| Action::EoWrite { eo: a.eo_ref(g) });
        self.eos.push(FoundEo { g, evaluated: false, lines: Vec::new(), budget: 0, worked: 0, done: false });
        self.out.eos_found += 1;
        self.out.last_eo_t = self.clock;
        let w = self.w;
        self.eos.sort_by_key(|e| w.eos[e.g].len); // shortest first (stable)
    }

    // -------------------------------------------------------------------------------- RZP and DR

    fn dr_work(&self) -> Option<usize> {
        self.eos.iter().position(|e| !e.done)
    }

    fn rzp_budget(&self, g: usize) -> usize {
        if self.w.eos[g].len <= self.plan.rzp_short {
            self.plan.rzp_per_eo
        } else {
            self.plan.rzp_per_eo_long
        }
    }

    fn dr_step(&mut self, ei: usize) {
        let w = self.w;
        let t = self.t;
        let plan = self.plan;
        let g = self.eos[ei].g;
        let eo = &w.eos[g];
        if !self.eos[ei].evaluated {
            // the glance: every ending and both DR axes
            let mut lines: Vec<LineSlot> = Vec::new();
            for root in &eo.endings {
                for x in (0..3).filter(|&x| x != eo.axis) {
                    lines.push(LineSlot { search: LineSearch::new(t, &self.hum, &w.moves, root, eo.axis, x, eo.len, w.seed), done: false });
                }
            }
            // two lines per ending (the two DR axes)
            let glance: Vec<LineGlance> = if self.record {
                lines.iter().enumerate().map(|(li, l)| line_glance(t, &w.moves, &eo.endings[li / 2], eo.axis, l)).collect()
            } else {
                Vec::new()
            };
            self.pay(StepKind::EoEval, self.cost.eo_eval, eo.key, move |a| Action::EoGlance { eo: a.eo_ref(g), lines: glance });
            for li in 0..lines.len() {
                if let LineStep::Looked { dr: Some(cand), .. } =
                    lines[li].search.step(t, &self.hum, plan.rzp_depth, plan.switch_pen, plan.dr_cap)
                {
                    let key = h2(eo.key, (li as u64) << 32);
                    self.find_dr(cand, g, key);
                    lines[li].done = true;
                }
            }
            let budget = self.rzp_budget(g);
            let e = &mut self.eos[ei];
            e.evaluated = true;
            e.budget = budget;
            e.lines = lines;
            let open = self.next_line(ei).is_some();
            self.eos[ei].done = !open;
            return;
        }
        let Some(li) = self.next_line(ei) else {
            self.eos[ei].done = true;
            return;
        };
        let result = self.eos[ei].lines[li].search.step(t, &self.hum, plan.rzp_depth, plan.switch_pen, plan.dr_cap);
        self.eos[ei].worked += 1;
        match result {
            LineStep::Exhausted => self.eos[ei].lines[li].done = true,
            LineStep::Looked { switch, node, dr } => {
                let line = &self.eos[ei].lines[li].search;
                let key = h2(eo.key, (li as u64) << 32 | line.examined as u64);
                let (kind, nominal) = if switch { (StepKind::Switch, self.cost.switch) } else { (StepKind::Rzp, self.cost.rzp) };
                let dr_axis = crate::cube::AXIS_NAMES[line.dr_axis];
                let side = if line.start_side() == 0 { "normal" } else { "inverse" };
                let view = node_view(&node, eo.len);
                self.pay(kind, nominal, key, move |a| {
                    let eo = a.eo_ref(g);
                    if switch {
                        Action::Switch { eo, dr_axis, side, node: view }
                    } else {
                        Action::Rzp { eo, dr_axis, side, node: view }
                    }
                });
                if let Some(cand) = dr {
                    self.find_dr(cand, g, key);
                }
                if self.eos[ei].lines[li].search.found >= plan.dr_per_line + self.pass {
                    self.eos[ei].lines[li].done = true;
                }
            }
        }
        if self.next_line(ei).is_none() {
            self.eos[ei].done = true;
        }
    }

    /// The line of an EO whose best unworked RZP state is the most promising, if the EO still has budget and that
    /// state's read is good enough.
    fn next_line(&self, ei: usize) -> Option<usize> {
        let e = &self.eos[ei];
        if e.worked >= e.budget {
            return None;
        }
        let read_max = self.plan.read_max + self.pass as f64;
        let mut best: Option<(f64, usize)> = None;
        for (li, l) in e.lines.iter().enumerate() {
            if l.done {
                continue;
            }
            if let Some((rank, total)) = l.search.peek() {
                if total <= read_max && best.is_none_or(|b| rank < b.0) {
                    best = Some((rank, li));
                }
            }
        }
        best.map(|b| b.1)
    }

    /// Out of things to examine: go back over every EO with `rzp_more` more RZP states and a read limit one higher.
    fn deepen(&mut self) -> bool {
        if self.pass >= 4 || self.plan.rzp_more == 0 {
            return false;
        }
        self.pass += 1;
        for ei in 0..self.eos.len() {
            if self.eos[ei].evaluated {
                let budget = self.rzp_budget(self.eos[ei].g) + self.pass * self.plan.rzp_more;
                let e = &mut self.eos[ei];
                e.budget = budget;
                for l in e.lines.iter_mut() {
                    l.done = false;
                }
            }
        }
        let mut any = false;
        for ei in 0..self.eos.len() {
            if self.eos[ei].evaluated {
                let open = self.next_line(ei).is_some();
                self.eos[ei].done = !open;
                any |= open;
            }
        }
        any
    }

    fn dr_state(&self, view: &View, normal: &[Move], inverse: &[Move]) -> DrState {
        let v = view_state(self.t, view, &self.w.moves, normal, inverse);
        let (c, e, s) = v.dr_perms().expect("a DR candidate is a DR");
        (rank_perm(&c), rank_perm(&e), rank_perm(&s))
    }

    /// Write down a DR that was seen (and read it, if the plan reads on finding).
    fn find_dr(&mut self, cand: DrCandidate, eo: usize, key: u64) {
        let cost = self.cost.dr_find[cand.seen_from.min(7)];
        let (seen_from, rzp_moves, switched) = (cand.seen_from, cand.rzp_moves, cand.switched);
        let placeholder = DrRef { number: 0, text: niss_text(&cand.normal, &cand.inverse), len: cand.len, axis: crate::cube::AXIS_NAMES[cand.dr_axis] };
        // the step is recorded here; its DR number is known once the DR is on the page (reading it may add a step)
        let at = self.steps.len();
        self.pay(StepKind::DrFind, cost, key, |a| Action::DrFind {
            dr: placeholder,
            eo: a.eo_ref(eo),
            seen_from,
            rzp_moves,
            switched,
            outcome: "",
        });
        let (number, outcome) = self.add_dr(cand, eo);
        if self.record {
            if let Some(Step { action: Action::DrFind { dr, outcome: o, .. }, .. }) = self.steps.get_mut(at) {
                dr.number = number;
                *o = outcome;
            }
        }
    }

    /// Returns the DR's number and whether it was new.
    fn add_dr(&mut self, cand: DrCandidate, eo: usize) -> (usize, &'static str) {
        let t = self.t;
        let view = DR_VIEW[cand.dr_axis][cand.eo_axis];
        let mut seqs = vec![(cand.normal.clone(), cand.inverse.clone())];
        if let Some(side) = cand.flip_side {
            let (mut n, mut i) = (cand.normal.clone(), cand.inverse.clone());
            let last = if side == 0 { n.last_mut() } else { i.last_mut() }.unwrap();
            *last = last.the_other_way();
            seqs.push((n, i));
        }
        let x = cand.dr_axis as u64;
        let name = |st: DrState| (st.0 * 40320 + st.1) as u64 * 24 + st.2 as u64;
        let variants: Vec<Variant> = seqs
            .into_iter()
            .map(|(normal, inverse)| {
                let st = self.dr_state(&view, &normal, &inverse);
                let canonical = t.dr.canonical(st);
                Variant {
                    subset: t.htr.subset(st.0, st.1),
                    key: h2(h2(self.w.seed, 0x47 + x), name(canonical)),
                    normal,
                    inverse,
                    st,
                    next_route: 0,
                }
            })
            .collect();
        let dkey = (cand.dr_axis, t.dr.canonical(variants[0].st));
        if let Some(&j) = self.dr_index.get(&dkey) {
            if self.drs[j].cand.len <= cand.len {
                return (j + 1, "the same DR again");
            }
            self.drs[j].done = true; // a shorter way to the same DR replaces the old entry
        }
        let replaced = self.dr_index.contains_key(&dkey);
        // a DR and its twin are one entry, named by the smaller of the two states
        let smallest = variants.iter().map(|v| t.dr.canonical(v.st)).min().unwrap();
        let key = h2(h2(self.w.seed, 0xD2 + x), name(smallest));
        self.out.drs_found += 1;
        if self.out.best_dr == 0 || (cand.len as u32) < self.out.best_dr {
            self.out.best_dr = cand.len as u32;
        }
        let j = self.drs.len();
        for v in &variants {
            self.dr_index.insert((cand.dr_axis, t.dr.canonical(v.st)), j);
        }
        self.out.last_dr_t = self.clock;
        self.drs.push(FoundDr { cand, eo, view, variants, read: false, started: false, tries: 0, done: false, key, found_at: self.clock });
        if self.plan.read_on_find {
            self.read_dr(j);
        }
        (j + 1, if replaced { "a shorter way to a DR already found" } else { "new" })
    }

    fn read_dr(&mut self, j: usize) {
        let key = self.drs[j].key;
        self.pay(StepKind::DrRead, self.cost.dr_read, key, |a| Action::DrRead {
            dr: a.dr_ref(j),
            subsets: a.drs[j].variants.iter().map(|v| a.t.htr.sub48_names[v.subset].clone()).collect(),
        });
        self.drs[j].read = true;
    }

    // -------------------------------------------------------------------------------- finishing

    /// Expected total of a DR from what has been read of it.
    fn expected_total(&self, d: &FoundDr) -> f64 {
        if d.read {
            d.cand.len as f64 + d.variants.iter().map(|v| self.t.subset_mean[v.subset]).fold(f64::MAX, f64::min)
        } else {
            d.cand.len as f64 + self.t.all_mean
        }
    }

    /// Chance, by subset, that the DR's optimal finish beats the best solution so far.
    fn chance_to_improve(&self, d: &FoundDr) -> f64 {
        let Some(b) = &self.best else { return 1.0 };
        let need = b.len as i64 - 1 - d.cand.len as i64;
        if need < 0 {
            return 0.0;
        }
        let k = (need as usize).min(20);
        if d.read {
            d.variants.iter().map(|v| self.t.subset_cdf[v.subset][k]).fold(0.0, f64::max)
        } else {
            self.t.all_cdf[k]
        }
    }

    /// The DR to work on next: lowest expected total among those worth it.  `eager`: only DRs good enough to be
    /// finished ahead of the finishing phase, and only their first `eager_routes` routes.
    fn pick_finish(&self, eager: bool) -> Option<usize> {
        let p = self.plan;
        let started = self.drs.iter().filter(|d| d.started).count();
        let mut best: Option<(usize, f64)> = None;
        for (j, d) in self.drs.iter().enumerate() {
            if d.done || (!d.started && started >= p.fin_max) {
                continue;
            }
            if self.chance_to_improve(d) < p.fin_min_p {
                continue;
            }
            let e = self.expected_total(d);
            if eager && !(e <= p.eager_finish && d.tries < p.eager_routes) {
                continue;
            }
            if best.is_none_or(|b| e < b.1) {
                best = Some((j, e));
            }
        }
        best.map(|b| b.0)
    }

    fn finish_step(&mut self, j: usize) {
        let t = self.t;
        let w = self.w;
        if !self.drs[j].read {
            self.read_dr(j);
            return;
        }
        // the next route: over the two endings, the one whose next checklist line finds the optimum most often
        let mut pick: Option<(f64, usize)> = None;
        for (vi, v) in self.drs[j].variants.iter().enumerate() {
            if let Some(r) = t.checklists[v.subset].get(v.next_route) {
                if pick.is_none_or(|p| r.marginal > p.0) {
                    pick = Some((r.marginal, vi));
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
        let (vkey, step, subset, st) = {
            let v = &mut self.drs[j].variants[vi];
            v.next_route += 1;
            (v.key, v.next_route - 1, v.subset, v.st)
        };
        let routes = w.routes(st);
        let checklist_route = &t.checklists[subset][step];
        let finish = routes.best.get(&checklist_route.route).map(|(_, fin)| fin.clone());
        let seen = finish.is_some() && uniform(h2(vkey, 1000 + step as u64)) < self.hum.route_see;
        let cube_finish = finish.as_ref().map(|fin| dr_moves_to_cube(&self.drs[j].view, fin));
        let dr_len = self.drs[j].cand.len;
        let attempt = RouteTry {
            route: checklist_route.name.clone(),
            subset: t.htr.sub48_names[subset].clone(),
            finish: cube_finish.as_ref().filter(|_| seen).map(|f| format_moves(f)),
            finish_len: cube_finish.as_ref().filter(|_| seen).map(|f| f.len()),
            total: None,
            missed: finish.is_some() && !seen,
            optimal: routes.optimal,
        };
        self.pay(StepKind::Htr, self.cost.htr, h2(vkey, step as u64), |a| Action::Htr { dr: a.dr_ref(j), attempt });
        self.drs[j].tries += 1;
        if let (true, Some(fin), Some(own)) = (seen, finish, cube_finish) {
            let v = &self.drs[j].variants[vi];
            let mut full = v.normal.clone();
            full.extend(&own);
            full.extend(invert(&v.inverse));
            let full = cancel(&full);
            if self.record {
                if let Some(Step { action: Action::Htr { attempt, .. }, .. }) = self.steps.last_mut() {
                    attempt.total = Some(full.len());
                }
            }
            let improves = self.best.as_ref().is_none_or(|b| full.len() < b.len);
            let text = format_moves(&full);
            let len = full.len();
            self.pay(StepKind::Tail, self.cost.tail, h2(vkey, step as u64), |a| Action::Tail {
                dr: a.dr_ref(j),
                solution: text,
                len,
                best_so_far: improves,
            });
            if t.moves.apply(&w.state, &full) != Cube::SOLVED {
                self.out.replay_failures += 1;
            } else {
                let d = &self.drs[j];
                let v = &d.variants[vi];
                let eo = &w.eos[d.eo];
                self.solutions.push(Solution {
                    found_at: self.clock,
                    len,
                    moves: format_moves(&full),
                    eo: eo.text(),
                    eo_len: eo.len,
                    dr_normal: format_moves(&v.normal),
                    dr_inverse: format_moves(&v.inverse),
                    dr_len,
                    dr_axis: crate::cube::AXIS_NAMES[d.cand.dr_axis],
                    subset: t.htr.sub48_names[subset].clone(),
                    route: checklist_route.name.clone(),
                    finish: format_moves(&own),
                    finish_len: fin.len(),
                    optimal_finish: routes.optimal,
                    dr_found_at: d.found_at,
                    written_at: None,
                });
                if self.out.first_sol_len == 0 {
                    self.out.first_sol_len = len as u32;
                    self.out.first_sol_t = self.clock;
                }
                if improves {
                    self.best = Some(Sol {
                        len,
                        moves: full,
                        dr_len: dr_len as u32,
                        subset,
                        optimal: routes.optimal as u32,
                        fin: fin.len() as u32,
                        dr_t: self.drs[j].found_at,
                        index: self.solutions.len() - 1,
                    });
                }
            }
        }
        if self.drs[j].tries >= self.plan.htr_per_dr {
            self.drs[j].done = true;
        }
    }

    /// Write the best solution down.
    fn write(&mut self) {
        let s = self.best.clone().unwrap();
        let in_time_if = self.budget;
        let text = format_moves(&s.moves);
        self.pay(StepKind::Write, self.cost.write, self.out.writes.len() as u64 + 1, |a| Action::Write {
            len: s.len,
            solution: text,
            in_time: a.clock <= in_time_if,
        });
        self.out.writes.push((self.clock, s.len as u32));
        if self.clock <= self.budget {
            if let Some(sol) = self.solutions.get_mut(s.index) {
                sol.written_at = Some(self.clock);
            }
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

    pub fn run(mut self) -> Report {
        let p = self.plan;
        let bad = self.w.bad;
        self.pay(StepKind::Look, self.cost.look, 0, |_| Action::Look { bad_edges: bad });
        let write_ms = (self.cost.write * 1000.0) as u64;
        let tk = self.time_scale;
        let mut guard = 0u32;
        loop {
            guard += 1;
            if self.clock >= self.budget || guard > 2_000_000 {
                break;
            }
            let left = self.budget - self.clock;
            let better = self.better();
            // the time kept for writing: `reserve`, or `reserve_rewrite` once a solution is on the sheet (a rewrite that
            // runs over the hour leaves the old solution standing)
            let reserve = 1000.0 * if self.banked.is_some() { p.reserve_rewrite() } else { p.reserve };
            let reserve = reserve as u64;
            let best_len = self.best.as_ref().map_or(99, |b| b.len);
            if better
                && (left <= reserve || p.bank_always || (p.bank_first && self.banked.is_none()) || (p.bank_at > 0 && best_len <= p.bank_at))
            {
                self.write();
                continue;
            }
            let desperate = left <= reserve && self.best.is_none() && left > write_ms;
            if left <= reserve && !desperate {
                break;
            }
            if p.stop_at > 0 && self.banked.as_ref().is_some_and(|b| b.len <= p.stop_at) {
                break;
            }
            let now = self.clock as f64 / 1000.0;
            let fin = self.pick_finish(false);
            let fin_eager = if p.eager_finish > 0.0 { self.pick_finish(true) } else { None };
            let line = self.dr_work();
            let target = self.eo_target();
            let eo = if self.eos.len() >= p.eo_cap { None } else { self.eo_work(target) };
            let eo_over = now >= p.t_eo * tk || eo.is_none();
            let mut t_dr = p.t_dr * tk;
            if p.rich_n > 0 && p.t_dr_rich > 0.0 && self.eos.len() >= p.rich_n {
                t_dr = p.t_dr_rich * tk;
            }
            if p.t_dr_backup > 0.0 && self.banked.as_ref().is_some_and(|b| b.len <= p.backup_len) {
                t_dr = t_dr.max(p.t_dr_backup * tk);
            }
            if p.t_dr_late > 0.0 && now >= t_dr && (self.out.best_dr == 0 || self.out.best_dr as usize > p.late_len) {
                t_dr = t_dr.max(p.t_dr_late * tk);
            }
            let enough = p.dr_enough > 0 && self.drs.iter().filter(|d| d.cand.len <= p.dr_enough_len).count() >= p.dr_enough;
            let dr_over = now >= t_dr || enough || desperate;
            let backup_due = p.backup_time > 0.0 && self.best.is_none() && now >= p.backup_time * tk;
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
                let eager = self.w.eos[self.eos[e].g].len <= p.eager_eo;
                if !dr_over && (eo_over || eager) {
                    self.dr_step(e);
                    continue;
                }
            }
            // 3. EOs
            if let Some(work) = eo {
                if !eo_over && !dr_over {
                    self.do_eo(work);
                    continue;
                }
                // 4. nothing is due in the planned order: do what is left, most downstream first
                if fin.is_none() && line.is_none() {
                    self.do_eo(work);
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
            if let Some(work) = self.eo_work(self.w.max_eo) {
                self.do_eo(work);
                continue;
            }
            if self.deepen() {
                continue;
            }
            // nothing at all left to examine
            if better {
                self.write();
            }
            break;
        }
        // a last chance to write down what was found (it counts only if it ends inside the hour)
        if self.better() && self.clock < self.budget {
            self.write();
        }
        self.wrap_up()
    }

    fn wrap_up(mut self) -> Report {
        let mut out = std::mem::take(&mut self.out);
        out.t_end = self.clock;
        out.budget_ms = self.budget;
        out.best_found = self.best.as_ref().map_or(0, |b| b.len as u32);
        if let Some(b) = &self.banked {
            out.len = b.len;
            out.moves = b.moves.clone();
            out.res_dr_len = b.dr_len;
            out.res_subset = Some(b.subset);
            out.res_optimal = b.optimal;
            out.res_fin = b.fin;
            out.res_dr_t = b.dr_t;
            out.res_sol_t = self.solutions.get(b.index).map_or(0, |s| s.found_at);
        }
        // what a computer would make of the page: best DR length + optimal finish over every DR found
        let mut oracle = 0u32;
        for d in &self.drs {
            for v in &d.variants {
                let total = d.cand.len as u32 + self.w.optimal(v.st) as u32;
                if oracle == 0 || total < oracle {
                    oracle = total;
                }
            }
        }
        out.oracle_page = oracle;
        Report { outcome: out, steps: self.steps, solutions: self.solutions }
    }
}

/// What the glance shows of one line: the ending, the DR axis, the DRM and the read.
fn line_glance(t: &Tables, scramble: &[Move], root: &crate::eo::Ending, eo_axis: usize, l: &LineSlot) -> LineGlance {
    let view = DR_VIEW[l.search.dr_axis][eo_axis];
    let v = view_state(t, &view, scramble, &root.normal, &root.inverse);
    let v = if l.search.start_side() == 1 { v.inverse() } else { v };
    let (twist, _, slice) = t.coords(&v);
    LineGlance {
        ending: niss_text(&root.normal, &root.inverse),
        dr_axis: crate::cube::AXIS_NAMES[l.search.dr_axis],
        drm: t.drm_name(twist, slice),
        read_total: l.search.peek().map_or(f64::NAN, |(_, total)| total),
        true_distance: t.dr_dist[twist * crate::tables::N_SLICE + slice] as usize,
    }
}

fn node_view(node: &NodeInfo, eo_len: usize) -> NodeView {
    NodeView {
        moves: format_moves(&node.first_side),
        switched: node.switched,
        moves_after_switch: format_moves(&node.second_side),
        read_total: eo_len as f64 + (node.first_side.len() + node.second_side.len()) as f64 + node.read,
        true_distance: node.true_distance,
        drm: node.drm.clone(),
    }
}

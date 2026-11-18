//! The three sets of numbers behind an attempt:
//!
//! * [`Costs`]: seconds per state examined (`[cost]` of the research `costs.toml`);
//! * [`Human`]: what the simulated solver can see (`[human]`);
//! * [`Plan`]: how the hour is spent (one `[policy.NAME]` section of a policy file).
//!
//! The defaults are the research values.  Every key is checked: an unknown one is an error, so a typo cannot fall
//! back to a default unnoticed.

use serde::{Deserialize, Serialize};

/// Seconds per state examined.  A step's real time is its nominal time times a log-normal factor (mean 1) with spread
/// `noise_sigma`, fixed per scramble and object, and times the attempt's pace (spread `attempt_sigma`).
#[derive(Clone, Debug, Serialize, Deserialize, PartialEq)]
#[serde(default, deny_unknown_fields)]
pub struct Costs {
    /// length of the attempt
    pub budget: f64,
    /// spread of one step's real time around its nominal time
    pub noise_sigma: f64,
    /// spread of the solver's pace from one attempt to the next
    pub attempt_sigma: f64,
    /// count the bad edges on the three axes before anything else
    pub look: f64,
    /// search one axis (both sides) for EOs one move longer than before; index = EO length 0..7
    pub eo_scan: [f64; 8],
    /// the same search when EOs with moves on both sides are looked for too: this factor
    pub eo_niss_factor: f64,
    /// write one EO down
    pub eo_write: f64,
    /// glance at one EO: bad corners and edges on its two DR axes, both endings
    pub eo_eval: f64,
    /// work one RZP state
    pub rzp: f64,
    /// work a state on the other side (set the inverse up first)
    pub switch: f64,
    /// write down a DR that was seen; index = how many moves away it was (0..7)
    pub dr_find: [f64; 8],
    /// read a DR: corner case and bad edges, for the last turn either way
    pub dr_read: f64,
    /// try one route to HTR on a DR
    pub htr: f64,
    /// write out the finish a route gave
    pub tail: f64,
    /// write the full solution down and check it on the cube
    pub write: f64,
}

impl Default for Costs {
    fn default() -> Self {
        Costs {
            budget: 3600.0,
            noise_sigma: 0.25,
            attempt_sigma: 0.15,
            look: 15.0,
            eo_scan: [0.0, 2.0, 3.0, 5.0, 10.0, 30.0, 120.0, 400.0],
            eo_niss_factor: 1.5,
            eo_write: 8.0,
            eo_eval: 5.0,
            rzp: 15.0,
            switch: 25.0,
            dr_find: [3.0, 3.0, 5.0, 8.0, 12.0, 20.0, 30.0, 45.0],
            dr_read: 15.0,
            htr: 40.0,
            tail: 30.0,
            write: 150.0,
        }
    }
}

/// What the simulated solver can see.
#[derive(Clone, Debug, Serialize, Deserialize, PartialEq)]
#[serde(default, deny_unknown_fields)]
pub struct Human {
    /// chance that an EO of a given length (index 0..7) is found when its axis is searched to that length: all moves on
    /// one side, and with moves on both sides
    pub eo_see_lin: [f64; 8],
    pub eo_see_niss: [f64; 8],
    /// chance that the DR is seen from a state d EO-keeping moves away from it (index d = 0..7): at the glance that
    /// discards an EO, and at an RZP state that is worked
    pub dr_see_glance: [f64; 8],
    pub dr_see_work: [f64; 8],
    /// chance that a route that has a short finish is finished that well when tried
    pub route_see: f64,
    /// the read of how far the DR is: the true EO-keeping distance plus a normal error with this spread, in moves
    pub read_sd: f64,
    /// RZP states are ranked by this * moves so far + their read
    pub rzp_depth_weight: f64,
    /// spread of the solver's form from attempt to attempt: on a day with form f = exp(form_sigma * z) every miss chance
    /// m becomes m^f and the reading error read_sd / f (0 = the same solver every attempt)
    pub form_sigma: f64,
}

impl Default for Human {
    fn default() -> Self {
        Human {
            eo_see_lin: [1.0, 1.0, 1.0, 1.0, 0.95, 0.75, 0.3, 0.1],
            eo_see_niss: [1.0, 1.0, 0.9, 0.9, 0.7, 0.3, 0.05, 0.0],
            dr_see_glance: [1.0, 1.0, 1.0, 0.9, 0.6, 0.25, 0.05, 0.0],
            dr_see_work: [1.0, 1.0, 1.0, 1.0, 0.95, 0.8, 0.5, 0.15],
            route_see: 0.9,
            read_sd: 1.0,
            rzp_depth_weight: 0.6,
            form_sigma: 0.0,
        }
    }
}

impl Human {
    /// The limits on an attempt whose form is z standard deviations from the solver's usual (z > 0: a good day).
    pub fn on_form(&self, z: f64) -> Human {
        if self.form_sigma == 0.0 {
            return self.clone();
        }
        let f = libm::exp(self.form_sigma * z);
        let see = |p: f64| 1.0 - libm::pow(1.0 - p.clamp(0.0, 1.0), f);
        let arr = |a: [f64; 8]| -> [f64; 8] { std::array::from_fn(|i| see(a[i])) };
        Human {
            eo_see_lin: arr(self.eo_see_lin),
            eo_see_niss: arr(self.eo_see_niss),
            dr_see_glance: arr(self.dr_see_glance),
            dr_see_work: arr(self.dr_see_work),
            route_see: see(self.route_see),
            read_sd: self.read_sd / f,
            rzp_depth_weight: self.rzp_depth_weight,
            form_sigma: self.form_sigma,
        }
    }
}

/// How the hour is spent.  Times are seconds on the clock of a one-hour attempt; with another budget they scale with
/// it.
#[derive(Clone, Debug, Serialize, Deserialize, PartialEq)]
#[serde(default, deny_unknown_fields)]
pub struct Plan {
    // --- EO
    /// look for EOs of up to this many moves on every axis
    pub eo_len: usize,
    /// also EOs with moves on both sides
    pub eo_niss: bool,
    /// write down at most this many EOs
    pub eo_cap: usize,
    /// if fewer than `poor_n` EOs were found, extend the search to this length (0 = off)
    pub eo_len_poor: usize,
    pub poor_n: usize,
    /// stop collecting EOs at this time
    pub t_eo: f64,
    /// EOs of at most this length are taken to DR as soon as they are written (0 = off)
    pub eager_eo: usize,
    // --- RZP and DR
    /// RZP states (switches included) worked per EO after the glance, most promising first
    pub rzp_per_eo: usize,
    /// ... for EOs of at most this length; longer EOs get `rzp_per_eo_long`
    pub rzp_short: usize,
    pub rzp_per_eo_long: usize,
    /// work an RZP state only if EO + RZP moves + its read of the DR is at most this
    pub read_max: f64,
    /// when nothing is left to examine: this many more RZP states per EO, and read_max + 1, per pass
    pub rzp_more: usize,
    /// most RZP moves before the DR is seen
    pub rzp_depth: usize,
    /// how much worse (in moves) a look on the other side is ranked; 50 or more = never switch
    pub switch_pen: f64,
    /// ignore DRs longer than this
    pub dr_cap: usize,
    /// DRs taken from one line (EO ending and DR axis) before it is dropped
    pub dr_per_line: usize,
    /// read a DR's subset when it is written down (otherwise only when it is its turn to be finished)
    pub read_on_find: bool,
    /// stop looking for DRs at this time
    pub t_dr: f64,
    /// ... or at this time if at least `rich_n` EOs were written (0 = off)
    pub t_dr_rich: f64,
    pub rich_n: usize,
    /// ... or at this time if no DR of at most `late_len` moves is on the page at t_dr (0 = off)
    pub t_dr_late: f64,
    pub late_len: usize,
    /// ... or at this time if a solution of at most `backup_len` is already written down (0 = off)
    pub t_dr_backup: f64,
    pub backup_len: usize,
    /// stop looking for DRs once this many of at most `dr_enough_len` moves are on the page (0 = off)
    pub dr_enough: usize,
    pub dr_enough_len: usize,
    // --- finishing
    /// a DR whose expected total is at most this is finished as soon as it is found (0 = off)
    pub eager_finish: f64,
    /// ... with this many routes (the rest of its routes wait for the finishing phase)
    pub eager_routes: usize,
    /// routes to HTR tried per DR
    pub htr_per_dr: usize,
    /// skip a DR whose chance (by subset) of beating the best solution is below this
    pub fin_min_p: f64,
    /// most DRs taken to a finish
    pub fin_max: usize,
    // --- safety
    /// if no full solution exists at this time, finish the best DR at once (0 = off)
    pub backup_time: f64,
    /// write the first full solution down as soon as it is found
    pub bank_first: bool,
    /// write every improvement down as soon as it is found
    pub bank_always: bool,
    /// write a solution down as soon as one of at most this length is found (0 = off)
    pub bank_at: usize,
    /// time kept at the end for writing the solution down
    pub reserve: f64,
    /// ... once a solution is already on the sheet (a rewrite that runs over leaves the old one); none = `reserve`
    pub reserve_rewrite: Option<f64>,
    /// stop as soon as a solution of at most this many moves is written down (0 = off)
    pub stop_at: usize,
}

impl Default for Plan {
    /// The defaults of the research program (the baseline plan differs only in `reserve`, see [`Plan::baseline`]).
    fn default() -> Self {
        Plan {
            eo_len: 5,
            eo_niss: true,
            eo_cap: 40,
            eo_len_poor: 0,
            poor_n: 0,
            t_eo: 480.0,
            eager_eo: 0,
            rzp_per_eo: 3,
            rzp_short: 4,
            rzp_per_eo_long: 1,
            read_max: 11.5,
            rzp_more: 2,
            rzp_depth: 3,
            switch_pen: 0.3,
            dr_cap: 11,
            dr_per_line: 1,
            read_on_find: true,
            t_dr: 2100.0,
            t_dr_rich: 0.0,
            rich_n: 0,
            t_dr_late: 0.0,
            late_len: 0,
            t_dr_backup: 0.0,
            backup_len: 0,
            dr_enough: 0,
            dr_enough_len: 0,
            eager_finish: 0.0,
            eager_routes: 99,
            htr_per_dr: 4,
            fin_min_p: 0.03,
            fin_max: 99,
            backup_time: 0.0,
            bank_first: false,
            bank_always: false,
            bank_at: 0,
            reserve: 240.0,
            reserve_rewrite: None,
            stop_at: 0,
        }
    }
}

impl Plan {
    /// The baseline: the hour the way the guides describe it.  EOs until minute 8, DRs until minute 35, then the best
    /// DRs finished, the solution written in the last five minutes.
    pub fn baseline() -> Plan {
        Plan { reserve: 300.0, ..Plan::default() }
    }

    /// The tuned plan of the write-up: the baseline with three changes (work an RZP state only if the read says a DR of
    /// 10 or less, keep 7 minutes to write, be as happy to switch as to stay).
    pub fn tuned() -> Plan {
        Plan { read_max: 10.0, reserve: 420.0, switch_pen: 0.0, ..Plan::baseline() }
    }

    pub fn reserve_rewrite(&self) -> f64 {
        self.reserve_rewrite.unwrap_or(self.reserve)
    }

    /// The longest EO the plan can ever look for.
    pub fn max_eo_len(&self) -> usize {
        self.eo_len.max(self.eo_len_poor).clamp(1, 7)
    }
}

/// Everything about one simulated attempt.
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Settings {
    #[serde(default)]
    pub costs: Costs,
    #[serde(default)]
    pub human: Human,
    #[serde(default = "Plan::tuned")]
    pub plan: Plan,
    /// the random draws (what is seen, how long each step takes) follow from this and the attempt number
    #[serde(default = "one")]
    pub seed: u64,
    #[serde(default)]
    pub attempt: u64,
}

fn one() -> u64 {
    1
}

impl Default for Settings {
    fn default() -> Self {
        Settings { costs: Costs::default(), human: Human::default(), plan: Plan::tuned(), seed: 1, attempt: 0 }
    }
}

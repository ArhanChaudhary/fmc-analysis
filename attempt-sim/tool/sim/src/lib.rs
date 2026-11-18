//! A simulator of human FMC attempts: EO, RZP, DR, HTR and the finish, with a time cost for every state the solver
//! examines and the human limits on what it sees.  It plays one hour on a scramble the way a plan says and keeps
//! what it wrote down.
//!
//! Reading order: [`cube`] (the cube), [`eo`] (EOs), [`rzp`] (RZP to DR), [`dr`], [`htr`], [`prune`], [`routes`] and
//! [`finish`] (DR to solved), [`settings`] (costs, human limits, plans), [`attempt`] (one attempt), [`simulate`] (the
//! whole thing from a scramble).

// Cube code indexes several parallel arrays by place; index loops say that more plainly than zipped iterators.
#![allow(clippy::needless_range_loop)]

pub mod attempt;
pub mod cube;
pub mod dr;
pub mod eo;
pub mod finish;
pub mod htr;
pub mod prune;
pub mod rng;
pub mod routes;
pub mod rzp;
pub mod settings;
pub mod tables;

pub use attempt::{Attempt, Outcome, Report, Scramble, Solution, Step, StepKind};
pub use settings::{Costs, Human, Plan, Settings};
pub use tables::Tables;

/// Play one attempt on a scramble with everything recorded.  The tables need their finish bound
/// ([`Tables::build_prune`]).
pub fn simulate(tables: &Tables, scramble: &[cube::Move], settings: &Settings) -> Report {
    let s = Scramble::new(tables, scramble, settings.seed, settings.attempt, settings.plan.max_eo_len());
    Attempt::new(&s, &settings.costs, &settings.human, &settings.plan, true).run()
}

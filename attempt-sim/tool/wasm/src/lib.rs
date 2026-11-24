//! The simulator for a web page (wasm-bindgen).  Everything goes in and out as JSON text.
//!
//! ```js
//! const sim = new Simulator();                 // small tables, well under a second
//! while (sim.build_step(64) < 1) { ... }       // the finish table, a slice at a time (a few seconds in all)
//! const defaults = JSON.parse(Simulator.defaults());
//! const report = JSON.parse(sim.simulate(JSON.stringify({ scramble: "R' U' F ...", settings: defaults.settings })));
//! ```
//!
//! The finish table (56 MB) can be kept between visits: `table_bytes()` gives it, `load_table(bytes)` takes it back
//! (and checks it).

use attempt_sim::cube::{format_moves, parse_moves};
use attempt_sim::prune::{NoETable, NoETableBuilder, NOE_CHECKSUM};
use attempt_sim::{Plan, Settings, StepKind, Tables};
use serde::Deserialize;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Simulator {
    tables: Tables,
    builder: Option<NoETableBuilder>,
}

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct Request {
    scramble: String,
    #[serde(default)]
    settings: Settings,
}

#[wasm_bindgen]
impl Simulator {
    /// Builds the small tables; the finish table comes from [`Simulator::build_step`] or [`Simulator::load_table`].
    #[wasm_bindgen(constructor)]
    pub fn new() -> Simulator {
        let tables = Tables::new();
        let builder = Some(tables.prune_builder());
        Simulator { tables, builder }
    }

    /// Work on the finish table for up to `classes` corner classes (of 2,768 per pass, about 14 passes).  Returns the
    /// progress, 1 when the table is ready.
    pub fn build_step(&mut self, classes: usize) -> f64 {
        let Some(b) = self.builder.as_mut() else { return 1.0 };
        if b.step(&self.tables.dr, classes) {
            self.tables.noe = Some(self.builder.take().unwrap().finish());
            return 1.0;
        }
        b.progress()
    }

    pub fn ready(&self) -> bool {
        self.tables.noe.is_some()
    }

    /// The finish table, to keep between visits.
    pub fn table_bytes(&self) -> Result<Vec<u8>, JsError> {
        Ok(self.tables.noe.as_ref().ok_or_else(|| JsError::new("the table is not built yet"))?.as_bytes().to_vec())
    }

    /// Take a kept table back; false if it is not the right table (then build it).
    pub fn load_table(&mut self, bytes: Vec<u8>) -> bool {
        match NoETable::from_bytes(&self.tables.dr, bytes) {
            Ok(t) => {
                self.tables.noe = Some(t);
                self.builder = None;
                true
            }
            Err(_) => false,
        }
    }

    /// A name for the table's contents, for the cache key.
    pub fn table_version() -> String {
        format!("noe-{NOE_CHECKSUM:016x}")
    }

    /// The default settings and the two plans, as JSON:
    /// `{settings, plans: {tuned, baseline, research_defaults}, kinds}`.
    pub fn defaults() -> String {
        serde_json::json!({
            "settings": Settings::default(),
            "plans": { "tuned": Plan::tuned(), "baseline": Plan::baseline() },
            "kinds": StepKind::ALL.iter().map(|k| k.name()).collect::<Vec<_>>(),
        })
        .to_string()
    }

    /// A scramble as the simulator reads it (face turns only), or an error saying what is wrong.
    pub fn check_scramble(text: &str) -> Result<String, JsError> {
        let moves = parse_moves(text).map_err(|e| JsError::new(&e))?;
        if moves.is_empty() {
            return Err(JsError::new("the scramble is empty"));
        }
        Ok(format_moves(&moves))
    }

    /// One attempt.  Request: `{scramble, settings}`; the report: `{scramble, outcome, solutions, steps, kinds,
    /// subset}`.
    pub fn simulate(&self, request: &str) -> Result<String, JsError> {
        if self.tables.noe.is_none() {
            return Err(JsError::new("the finish table is not built yet"));
        }
        let req: Request = serde_json::from_str(request).map_err(|e| JsError::new(&format!("settings: {e}")))?;
        let moves = parse_moves(&req.scramble).map_err(|e| JsError::new(&e))?;
        if moves.is_empty() {
            return Err(JsError::new("the scramble is empty"));
        }
        let s = &req.settings;
        check_settings(s).map_err(|e| JsError::new(&e))?;
        let r = attempt_sim::simulate(&self.tables, &moves, s);
        let subset = r.outcome.res_subset.map(|k| self.tables.htr.sub48_names[k].clone());
        Ok(serde_json::json!({
            "scramble": format_moves(&moves),
            "outcome": r.outcome,
            "subset": subset,
            "solutions": r.solutions,
            "steps": r.steps,
            "kinds": StepKind::ALL.iter().map(|k| k.name()).collect::<Vec<_>>(),
        })
        .to_string())
    }
}

impl Default for Simulator {
    fn default() -> Self {
        Self::new()
    }
}

/// Values the simulator cannot work with.
fn check_settings(s: &Settings) -> Result<(), String> {
    let c = &s.costs;
    let costs = [c.look, c.eo_niss_factor, c.eo_write, c.eo_eval, c.rzp, c.switch, c.dr_read, c.htr, c.tail, c.write];
    if costs.iter().chain(&c.eo_scan).chain(&c.dr_find).any(|&x| x.is_nan() || x < 0.0 || x.is_infinite()) {
        return Err("every cost must be a number of seconds, 0 or more".into());
    }
    if !(c.budget >= 60.0 && c.budget <= 4.0 * 3600.0) {
        return Err("the attempt must last between 1 minute and 4 hours".into());
    }
    if !(c.noise_sigma >= 0.0 && c.noise_sigma <= 3.0 && c.attempt_sigma >= 0.0 && c.attempt_sigma <= 3.0) {
        return Err("the spreads must be between 0 and 3".into());
    }
    let h = &s.human;
    let chances = h.eo_see_lin.iter().chain(&h.eo_see_niss).chain(&h.dr_see_glance).chain(&h.dr_see_work).chain([&h.route_see]);
    if chances.copied().any(|p| !(0.0..=1.0).contains(&p)) {
        return Err("every chance must be between 0 and 1".into());
    }
    if !(h.read_sd >= 0.0 && h.read_sd <= 10.0 && h.rzp_depth_weight >= 0.0 && h.form_sigma >= 0.0 && h.form_sigma <= 3.0) {
        return Err("read_sd must be between 0 and 10, form_sigma between 0 and 3, rzp_depth_weight 0 or more".into());
    }
    if h.finish_see > 5 || h.htr_extra > 6 {
        return Err("finish_see is at most 5 and htr_extra at most 6".into());
    }
    let p = &s.plan;
    if p.eo_len > 7 || p.eo_len_poor > 7 {
        return Err("EOs are searched up to 7 moves at most".into());
    }
    if p.rzp_depth > 8 || p.dr_cap > 16 {
        return Err("rzp_depth is at most 8 and dr_cap at most 16".into());
    }
    Ok(())
}

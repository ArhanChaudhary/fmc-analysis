//! The three parameter sets, read from small TOML files (a subset of TOML: `[section]`, `key = number | true | false
//! | "text" | [n, n, ...]`, `#` comments):
//!
//!   * `Costs`  — seconds per state examined (research/costs.toml, `[cost]`)
//!   * `Human`  — what the simulated solver can see (research/costs.toml, `[human]`)
//!   * `Policy` — how the hour is spent (research/policies/*.toml, one `[policy.NAME]` section each)
//!
//! Unknown keys are an error, so a typo cannot silently fall back to a default.

use std::collections::HashSet;

#[derive(Clone, Debug)]
pub enum Val {
    Num(f64),
    Bool(bool),
    Str(String),
    Arr(Vec<f64>),
}

pub struct Section {
    pub name: String,
    pub kv: Vec<(String, Val)>,
    used: std::cell::RefCell<HashSet<String>>,
}

pub fn parse(text: &str, origin: &str) -> Vec<Section> {
    let mut out: Vec<Section> = Vec::new();
    for (ln, raw) in text.lines().enumerate() {
        // strip a comment (no '#' inside strings in our files except within quotes)
        let mut line = String::new();
        let mut inq = false;
        for ch in raw.chars() {
            if ch == '"' {
                inq = !inq;
            }
            if ch == '#' && !inq {
                break;
            }
            line.push(ch);
        }
        let line = line.trim();
        if line.is_empty() {
            continue;
        }
        if line.starts_with('[') && line.ends_with(']') && !line.contains('=') {
            out.push(Section { name: line[1..line.len() - 1].trim().to_string(), kv: Vec::new(), used: Default::default() });
            continue;
        }
        let Some(eq) = line.find('=') else { fatal!("{}:{}: expected key = value", origin, ln + 1) };
        let key = line[..eq].trim().to_string();
        let v = line[eq + 1..].trim();
        let val = if v == "true" {
            Val::Bool(true)
        } else if v == "false" {
            Val::Bool(false)
        } else if v.starts_with('"') && v.ends_with('"') && v.len() >= 2 {
            Val::Str(v[1..v.len() - 1].to_string())
        } else if v.starts_with('[') && v.ends_with(']') {
            Val::Arr(
                v[1..v.len() - 1]
                    .split(',')
                    .filter(|x| !x.trim().is_empty())
                    .map(|x| x.trim().parse::<f64>().unwrap_or_else(|_| fatal!("{}:{}: bad number {}", origin, ln + 1, x)))
                    .collect(),
            )
        } else {
            Val::Num(v.parse::<f64>().unwrap_or_else(|_| fatal!("{}:{}: bad value {}", origin, ln + 1, v)))
        };
        match out.last_mut() {
            Some(s) => s.kv.push((key, val)),
            None => fatal!("{}:{}: key before any [section]", origin, ln + 1),
        }
    }
    out
}

impl Section {
    fn get(&self, key: &str) -> Option<&Val> {
        self.used.borrow_mut().insert(key.to_string());
        self.kv.iter().rev().find(|(k, _)| k == key).map(|(_, v)| v)
    }
    pub fn f(&self, key: &str, default: f64) -> f64 {
        match self.get(key) {
            Some(Val::Num(x)) => *x,
            Some(Val::Bool(b)) => *b as u8 as f64,
            Some(_) => fatal!("[{}] {}: expected a number", self.name, key),
            None => default,
        }
    }
    pub fn b(&self, key: &str, default: bool) -> bool {
        match self.get(key) {
            Some(Val::Bool(b)) => *b,
            Some(Val::Num(x)) => *x != 0.0,
            Some(_) => fatal!("[{}] {}: expected true/false", self.name, key),
            None => default,
        }
    }
    pub fn arr<const N: usize>(&self, key: &str, default: [f64; N]) -> [f64; N] {
        match self.get(key) {
            Some(Val::Arr(a)) => {
                if a.len() > N {
                    fatal!("[{}] {}: at most {} values", self.name, key, N);
                }
                // shorter arrays are padded with their last value
                let mut r = [*a.last().unwrap_or(&0.0); N];
                r[..a.len()].copy_from_slice(a);
                r
            }
            Some(_) => fatal!("[{}] {}: expected [a, b, ...]", self.name, key),
            None => default,
        }
    }
    pub fn s(&self, key: &str, default: &str) -> String {
        match self.get(key) {
            Some(Val::Str(x)) => x.clone(),
            Some(_) => fatal!("[{}] {}: expected \"text\"", self.name, key),
            None => default.to_string(),
        }
    }
    pub fn finish(&self) {
        let used = self.used.borrow();
        for (k, _) in &self.kv {
            if !used.contains(k) {
                fatal!("[{}]: unknown key '{}'", self.name, k);
            }
        }
    }
    /// A copy with some keys overridden (`key=value` pairs from the command line or a sweep).
    pub fn with(&self, name: &str, over: &[(String, Val)]) -> Section {
        let mut kv = self.kv.clone();
        kv.extend(over.iter().cloned());
        Section { name: name.to_string(), kv, used: Default::default() }
    }
}

/// Seconds per state examined (nominal; each step's real cost is the nominal one times a log-normal factor).
#[derive(Clone, Debug)]
pub struct Costs {
    pub budget: f64,
    pub look: f64,
    pub eo_scan: [f64; 8],
    pub eo_niss_factor: f64,
    pub eo_write: f64,
    pub eo_eval: f64,
    pub rzp: f64,
    pub switch: f64,
    pub dr_find: [f64; 8],
    pub dr_read: f64,
    pub htr: f64,
    pub tail: f64,
    pub write: f64,
    pub noise_sigma: f64,
    pub attempt_sigma: f64,
    /// multiplies every policy's writing reserve (a solver who writes slower keeps more time for it): sensitivity runs
    pub reserve_scale: f64,
}

/// What the simulated solver can see.
#[derive(Clone, Debug)]
pub struct Human {
    pub eo_see_lin: [f64; 8],
    pub eo_see_niss: [f64; 8],
    pub dr_see_glance: [f64; 8],
    pub dr_see_work: [f64; 8],
    pub route_see: f64,
    pub read_sd: f64,
    pub rzp_depth_weight: f64,
    /// spread of the solver's form from one attempt to the next (log-normal factor f on what they see): on a day with
    /// form f every miss chance m becomes m^f and the reading error read_sd / f (0 = the same solver every attempt)
    pub form_sigma: f64,
}

impl Human {
    /// The limits on an attempt whose form is z standard deviations from the solver's usual (z > 0: a good day).
    pub fn on_form(&self, z: f64) -> Human {
        if self.form_sigma == 0.0 {
            return self.clone();
        }
        let f = (self.form_sigma * z).exp();
        let see = |p: f64| 1.0 - (1.0 - p.clamp(0.0, 1.0)).powf(f);
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

pub fn load_costs(path: &str, over: &[(String, Val)]) -> (Costs, Human) {
    let text = std::fs::read_to_string(path).unwrap_or_else(|e| fatal!("cannot read {}: {}", path, e));
    let secs = parse(&text, path);
    let find = |n: &str| -> Section {
        let s = secs.iter().find(|s| s.name == n).unwrap_or_else(|| fatal!("{}: no [{}] section", path, n));
        // overrides are written section.key=value
        let ov: Vec<(String, Val)> = over
            .iter()
            .filter_map(|(k, v)| k.strip_prefix(&format!("{}.", n)).map(|kk| (kk.to_string(), v.clone())))
            .collect();
        s.with(n, &ov)
    };
    let c = find("cost");
    // `scale`: every cost of the listed kinds times a factor (sensitivity runs): cost.scale_KIND=2
    let sc = |k: &str| c.f(&format!("scale_{}", k), 1.0) * c.f("scale_all", 1.0);
    let arr_scale = |a: [f64; 8], f: f64| -> [f64; 8] { std::array::from_fn(|i| a[i] * f) };
    let costs = Costs {
        budget: c.f("budget", 3600.0),
        look: c.f("look", 15.0) * sc("eo"),
        eo_scan: arr_scale(c.arr("eo_scan", [0.0, 2.0, 3.0, 5.0, 10.0, 30.0, 120.0, 400.0]), sc("eo")),
        eo_niss_factor: c.f("eo_niss_factor", 1.5),
        eo_write: c.f("eo_write", 8.0) * sc("eo"),
        eo_eval: c.f("eo_eval", 5.0) * sc("dr"),
        rzp: c.f("rzp", 15.0) * sc("dr"),
        switch: c.f("switch", 25.0) * sc("dr"),
        dr_find: arr_scale(c.arr("dr_find", [3.0, 3.0, 5.0, 8.0, 12.0, 20.0, 30.0, 45.0]), sc("dr")),
        dr_read: c.f("dr_read", 15.0) * sc("fin"),
        htr: c.f("htr", 40.0) * sc("fin"),
        tail: c.f("tail", 30.0) * sc("fin"),
        write: c.f("write", 150.0) * sc("write"),
        noise_sigma: c.f("noise_sigma", 0.25),
        attempt_sigma: c.f("attempt_sigma", 0.15),
        reserve_scale: c.f("reserve_scale", 1.0),
    };
    c.finish();
    let h = find("human");
    let human = Human {
        eo_see_lin: h.arr("eo_see_lin", [1.0, 1.0, 1.0, 1.0, 0.95, 0.75, 0.3, 0.1]),
        eo_see_niss: h.arr("eo_see_niss", [1.0, 1.0, 0.9, 0.9, 0.7, 0.3, 0.05, 0.0]),
        dr_see_glance: h.arr("dr_see_glance", [1.0, 1.0, 1.0, 0.9, 0.6, 0.25, 0.05, 0.0]),
        dr_see_work: h.arr("dr_see_work", [1.0, 1.0, 1.0, 1.0, 0.95, 0.8, 0.5, 0.15]),
        route_see: h.f("route_see", 0.9),
        read_sd: h.f("read_sd", 1.0),
        rzp_depth_weight: h.f("rzp_depth_weight", 0.6),
        form_sigma: h.f("form_sigma", 0.0),
    };
    h.finish();
    for k in over {
        if !k.0.starts_with("cost.") && !k.0.starts_with("human.") {
            fatal!("override {}: expected cost.KEY or human.KEY", k.0);
        }
    }
    (costs, human)
}

/// How the hour is spent.  Times are seconds on the attempt clock.
#[derive(Clone, Debug)]
pub struct Policy {
    pub name: String,
    // --- EO
    pub eo_len: usize,      // look for EOs of up to this many moves on every axis
    pub eo_niss: bool,      // also EOs with moves on both sides
    pub eo_cap: usize,      // write down at most this many EOs
    pub eo_len_poor: usize, // if fewer than `poor_n` EOs were found, extend the search to this length (0 = off)
    pub poor_n: usize,
    pub t_eo: f64,          // stop collecting EOs at this time
    pub eager_eo: usize,    // EOs of at most this length are taken to DR as soon as they are written (0 = off)
    // --- RZP / DR
    pub rzp_per_eo: usize,   // RZP states (switches included) worked per EO after the glance, most promising first
    pub rzp_short: usize,    // ... for EOs of at most this length; longer EOs get `rzp_per_eo_long`
    pub rzp_per_eo_long: usize,
    pub read_max: f64,       // work an RZP state only if EO + RZP moves + its read of the DR is at most this
    pub rzp_more: usize,     // when nothing is left to examine: this many more RZP states per EO, and read_max + 1, per pass
    pub rzp_depth: usize,    // most RZP moves before the DR is seen
    pub switch_pen: f64,     // how much worse (in moves) a look on the other side is ranked; 99 = never switch
    pub dr_cap: usize,       // ignore DRs longer than this
    pub dr_per_line: usize,
    pub read_on_find: bool,  // read a DR's subset when it is written down (otherwise only when it is its turn to be finished)
    pub t_dr: f64,           // stop looking for DRs at this time
    pub t_dr_rich: f64,      // ... or at this time if at least `rich_n` EOs were written (0 = off)
    pub rich_n: usize,
    pub t_dr_late: f64,      // ... or at this time if no DR of at most `late_len` moves is on the page at t_dr (0 = off)
    pub late_len: usize,
    pub t_dr_backup: f64,    // ... or at this time if a solution of at most `backup_len` is already written down (0 = off)
    pub backup_len: usize,
    pub dr_enough: usize,    // stop looking for DRs once this many of at most `dr_enough_len` moves are on the page (0 = off)
    pub dr_enough_len: usize,
    // --- finishing
    pub eager_finish: f64,   // a DR whose expected total is at most this is finished as soon as it is found (0 = off)
    pub eager_routes: usize, // ... with this many routes (the rest of its routes wait for the finishing phase)
    pub htr_per_dr: usize,   // routes to HTR tried per DR
    pub fin_min_p: f64,      // skip a DR whose chance (by subset) of beating the best solution is below this
    pub fin_max: usize,      // most DRs taken to a finish
    // --- safety
    pub backup_time: f64,    // if no full solution exists at this time, finish the best DR at once (0 = off)
    pub bank_first: bool,    // write the first full solution down as soon as it is found
    pub bank_always: bool,   // write every improvement down as soon as it is found
    pub bank_at: usize,      // write a solution down as soon as one of at most this length is found (0 = off)
    pub reserve: f64,        // time kept at the end for writing the solution down
    pub reserve_rewrite: f64, // ... once a solution is already on the sheet (a rewrite that runs over leaves the old one)
    pub stop_at: usize,      // stop as soon as a solution of at most this many moves is written down (0 = off)
}

impl Policy {
    pub fn from(s: &Section) -> Policy {
        let name = s.name.strip_prefix("policy.").unwrap_or(&s.name).to_string();
        let u = |k: &str, d: usize| -> usize { s.f(k, d as f64).round() as usize };
        let reserve = s.f("reserve", 240.0);
        let p = Policy {
            name,
            eo_len: u("eo_len", 5),
            eo_niss: s.b("eo_niss", true),
            eo_cap: u("eo_cap", 40),
            eo_len_poor: u("eo_len_poor", 0),
            poor_n: u("poor_n", 0),
            t_eo: s.f("t_eo", 480.0),
            eager_eo: u("eager_eo", 0),
            rzp_per_eo: u("rzp_per_eo", 3),
            rzp_short: u("rzp_short", 4),
            rzp_per_eo_long: u("rzp_per_eo_long", 1),
            read_max: s.f("read_max", 11.5),
            rzp_more: u("rzp_more", 2),
            rzp_depth: u("rzp_depth", 3),
            switch_pen: s.f("switch_pen", 0.3),
            dr_cap: u("dr_cap", 11),
            dr_per_line: u("dr_per_line", 1),
            read_on_find: s.b("read_on_find", true),
            t_dr: s.f("t_dr", 2100.0),
            t_dr_rich: s.f("t_dr_rich", 0.0),
            rich_n: u("rich_n", 0),
            t_dr_late: s.f("t_dr_late", 0.0),
            late_len: u("late_len", 0),
            t_dr_backup: s.f("t_dr_backup", 0.0),
            backup_len: u("backup_len", 0),
            dr_enough: u("dr_enough", 0),
            dr_enough_len: u("dr_enough_len", 0),
            eager_finish: s.f("eager_finish", 0.0),
            eager_routes: u("eager_routes", 99),
            htr_per_dr: u("htr_per_dr", 4),
            fin_min_p: s.f("fin_min_p", 0.03),
            fin_max: u("fin_max", 99),
            backup_time: s.f("backup_time", 0.0),
            bank_first: s.b("bank_first", false),
            bank_always: s.b("bank_always", false),
            bank_at: u("bank_at", 0),
            reserve,
            reserve_rewrite: s.f("reserve_rewrite", reserve),
            stop_at: u("stop_at", 0),
        };
        s.finish();
        p
    }
}

/// Policies of a file: every `[policy.NAME]` section; a `base = "NAME"` key copies an earlier section first.
pub fn load_policies(path: &str) -> Vec<Policy> {
    let text = std::fs::read_to_string(path).unwrap_or_else(|e| fatal!("cannot read {}: {}", path, e));
    let secs = parse(&text, path);
    let mut out: Vec<Policy> = Vec::new();
    let mut full: Vec<Section> = Vec::new();
    for s in secs.iter().filter(|s| s.name.starts_with("policy.")) {
        let base = s.kv.iter().find(|(k, _)| k == "base").map(|(_, v)| match v {
            Val::Str(b) => b.clone(),
            _ => fatal!("[{}] base: expected \"NAME\"", s.name),
        });
        let own: Vec<(String, Val)> = s.kv.iter().filter(|(k, _)| k != "base").cloned().collect();
        let sec = match base {
            Some(b) => {
                let bs = full.iter().find(|f| f.name == format!("policy.{}", b)).unwrap_or_else(|| fatal!("[{}]: base {} not found above it", s.name, b));
                bs.with(&s.name, &own)
            }
            None => Section { name: s.name.clone(), kv: own, used: Default::default() },
        };
        out.push(Policy::from(&sec));
        full.push(sec);
    }
    if out.is_empty() {
        fatal!("{}: no [policy.NAME] section", path);
    }
    out
}

pub fn parse_overrides(args: &[String]) -> Vec<(String, Val)> {
    args.iter()
        .map(|a| {
            let Some(eq) = a.find('=') else { fatal!("override {}: expected KEY=VALUE", a) };
            let v = &a[eq + 1..];
            let val = if v.starts_with('[') {
                Val::Arr(v[1..v.len() - 1].split(',').map(|x| x.trim().parse().unwrap()).collect())
            } else if v == "true" || v == "false" {
                Val::Bool(v == "true")
            } else {
                Val::Num(v.parse().unwrap_or_else(|_| fatal!("override {}: bad number", a)))
            };
            (a[..eq].to_string(), val)
        })
        .collect()
}

//! The simulator from the command line: batch runs in the research program's output format (to check the port
//! against it), single attempts as JSON, and checks of the finish table.

use attempt_sim::cube::{format_moves, parse_moves, Move};
use attempt_sim::dr::{DrTables, NC, NE, NS};
use attempt_sim::prune::CornerClasses;
use attempt_sim::{Attempt, Costs, Human, Outcome, Plan, Scramble, Settings, StepKind, Tables};
use std::collections::HashMap;
use std::io::Write;
use std::time::Instant;

const USAGE: &str = "\
usage: attempt-sim <command> ...
  table                          build the finish table, print its distances, time and checksum
  check-optimal --exact TABLE [--count N]
                                 optimal finishes from the search against the exact table of Judging a DR
  run --costs FILE --policies FILE --scrambles FILE [--first A] [--count N] [--seed S] --out OUT.tsv
      [--log FILE --logn K] [--threads T]
                                 every plan of the file on every scramble (the research program's output format)
  trace --scramble \"R' U' F ...\" [--settings FILE.json]
                                 one attempt, everything recorded, as JSON";

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let opts = Opts::parse(args.get(1..).unwrap_or(&[]));
    let result = match args.first().map(String::as_str) {
        Some("table") => table(),
        Some("check-optimal") => check_optimal(&opts),
        Some("run") => run(&opts),
        Some("trace") => trace(&opts),
        _ => Err(USAGE.to_string()),
    };
    if let Err(e) = result {
        eprintln!("{e}");
        std::process::exit(1);
    }
}

struct Opts(HashMap<String, String>);

impl Opts {
    fn parse(a: &[String]) -> Opts {
        let mut m = HashMap::new();
        let mut i = 0;
        while i < a.len() {
            if let Some(k) = a[i].strip_prefix("--") {
                m.insert(k.to_string(), a.get(i + 1).cloned().unwrap_or_default());
                i += 2;
            } else {
                i += 1;
            }
        }
        Opts(m)
    }
    fn need(&self, k: &str) -> Result<&str, String> {
        self.0.get(k).map(String::as_str).ok_or_else(|| format!("--{k} is required\n{USAGE}"))
    }
    fn num(&self, k: &str, default: usize) -> usize {
        self.0.get(k).and_then(|v| v.parse().ok()).unwrap_or(default)
    }
}

fn tables() -> Tables {
    let t0 = Instant::now();
    let mut t = Tables::new();
    let t1 = Instant::now();
    t.build_prune();
    eprintln!("tables {:.2} s, finish table {:.2} s", (t1 - t0).as_secs_f64(), t1.elapsed().as_secs_f64());
    t
}

fn table() -> Result<(), String> {
    let t = tables();
    let noe = t.noe();
    let mut hist = [0u64; 16];
    for (i, &b) in noe.as_bytes().iter().enumerate() {
        hist[(b & 0xF) as usize] += 1;
        if 2 * i + 1 < noe.len_entries() {
            hist[(b >> 4) as usize] += 1;
        }
    }
    let ok = if noe.checksum() == attempt_sim::prune::NOE_CHECKSUM { "matches" } else { "DOES NOT MATCH" };
    println!("entries {}  bytes {}  checksum {:#018x} ({ok} NOE_CHECKSUM)", noe.len_entries(), noe.as_bytes().len(), noe.checksum());
    for (d, n) in hist.iter().enumerate().filter(|(_, &n)| n > 0) {
        println!("{d:2} {n}");
    }
    Ok(())
}

/// The exact table of *Judging a DR* (one byte per state, index (corner class * 40320 + edges) * 12 + slice among 12).
struct Exact {
    bytes: Vec<u8>,
    classes: CornerClasses,
    to12: [u8; NS],
}

impl Exact {
    fn load(path: &str, dr: &DrTables) -> Result<Exact, String> {
        let bytes = std::fs::read(path).map_err(|e| format!("{path}: {e}"))?;
        let classes = CornerClasses::new(dr);
        if bytes.len() != classes.rep.len() * NE * 12 {
            return Err(format!("{path}: {} bytes, not the exact table", bytes.len()));
        }
        let mut to12 = [0u8; NS];
        let mut n = [0u8; 2];
        for (s, slot) in to12.iter_mut().enumerate() {
            let p = dr.spar[s] as usize;
            *slot = n[p];
            n[p] += 1;
        }
        Ok(Exact { bytes, classes, to12 })
    }
    fn depth(&self, dr: &DrTables, c: usize, e: usize, s: usize) -> u8 {
        let k = self.classes.class[c] as usize;
        let sym = self.classes.to_rep[c] as usize;
        self.bytes[(k * NE + dr.esym[sym][e] as usize) * 12 + self.to12[dr.ssym[sym][s] as usize] as usize]
    }
}

fn check_optimal(o: &Opts) -> Result<(), String> {
    let t = tables();
    let exact = Exact::load(o.need("exact")?, &t.dr)?;
    let n = o.num("count", 2000);
    let mut x = 2026u64;
    let mut next = || {
        x = attempt_sim::rng::mix(x);
        x
    };
    let t0 = Instant::now();
    let (mut gap, mut by_depth) = (0u64, [0u64; 20]);
    for i in 0..n {
        let (c, e) = ((next() % NC as u64) as usize, (next() % NE as u64) as usize);
        let parity = t.dr.cpar[c] ^ t.dr.epar[e];
        let s = loop {
            let s = (next() % NS as u64) as usize;
            if t.dr.spar[s] == parity {
                break s;
            }
        };
        let want = exact.depth(&t.dr, c, e, s);
        let got = t.noe().optimal(&t.dr, (c, e, s));
        if want != got {
            return Err(format!("state {i} ({c}, {e}, {s}): search {got}, exact table {want}"));
        }
        gap += (want - t.noe().bound(&t.dr, (c, e, s))) as u64;
        by_depth[want as usize] += 1;
    }
    println!(
        "{n} random DR states: optimal finish identical to the exact table; mean bound gap {:.3}; {:.2} ms per state",
        gap as f64 / n as f64,
        1000.0 * t0.elapsed().as_secs_f64() / n as f64
    );
    println!("by optimal length: {:?}", &by_depth[..19]);
    Ok(())
}

fn read_toml(path: &str) -> Result<toml::Table, String> {
    let text = std::fs::read_to_string(path).map_err(|e| format!("{path}: {e}"))?;
    text.parse::<toml::Table>().map_err(|e| format!("{path}: {e}"))
}

fn load_costs(path: &str) -> Result<(Costs, Human), String> {
    #[derive(serde::Deserialize)]
    #[serde(deny_unknown_fields)]
    struct File {
        cost: Costs,
        human: Human,
    }
    let f: File = read_toml(path)?.try_into().map_err(|e| format!("{path}: {e}"))?;
    Ok((f.cost, f.human))
}

/// Every `[policy.NAME]` of a file; `base = "OTHER"` copies an earlier section first.
fn load_plans(path: &str) -> Result<Vec<(String, Plan)>, String> {
    let doc = read_toml(path)?;
    let sections = doc.get("policy").and_then(|v| v.as_table()).ok_or_else(|| format!("{path}: no [policy.NAME]"))?;
    let mut merged: Vec<(String, toml::Table)> = Vec::new();
    // toml::Table keeps the file's order
    for (name, v) in sections {
        let own = v.as_table().ok_or_else(|| format!("{path}: [policy.{name}] is not a table"))?;
        let mut table = match own.get("base").and_then(|b| b.as_str()) {
            Some(b) => merged.iter().find(|(n, _)| n == b).map(|(_, t)| t.clone()).ok_or_else(|| format!("{path}: base {b} not found above [policy.{name}]"))?,
            None => toml::Table::new(),
        };
        for (k, v) in own {
            if k != "base" {
                table.insert(k.clone(), v.clone());
            }
        }
        merged.push((name.clone(), table));
    }
    merged
        .into_iter()
        .map(|(name, table)| {
            // the research program's own defaults (not the baseline's), so that files mean what they meant there
            let mut full = toml::Table::try_from(Plan::default()).map_err(|e| e.to_string())?;
            full.remove("reserve_rewrite");
            full.extend(table);
            let plan: Plan = full.try_into().map_err(|e| format!("{path} [policy.{name}]: {e}"))?;
            Ok((name, plan))
        })
        .collect()
}

fn read_scrambles(path: &str, first: usize, count: usize) -> Result<Vec<(u64, Vec<Move>)>, String> {
    let text = std::fs::read_to_string(path).map_err(|e| format!("{path}: {e}"))?;
    // one scramble per line, or "id<TAB>scramble"; lines starting with # are comments
    text.lines()
        .filter(|l| !l.trim().is_empty() && !l.starts_with('#'))
        .enumerate()
        .skip(first)
        .take(count)
        .map(|(i, l)| {
            let body = l.rsplit('\t').next().unwrap();
            parse_moves(body).map(|m| (i as u64, m)).map_err(|e| format!("{path}, scramble {}: {e}", i + 1))
        })
        .collect()
}

fn run(o: &Opts) -> Result<(), String> {
    let (costs, human) = load_costs(o.need("costs")?)?;
    let plans = load_plans(o.need("policies")?)?;
    let first = o.num("first", 0);
    let scrambles = read_scrambles(o.need("scrambles")?, first, o.num("count", 1000))?;
    let seed = o.num("seed", 1) as u64;
    let logn = o.num("logn", 0);
    let threads = o.num("threads", std::thread::available_parallelism().map_or(1, |n| n.get()));
    let t = tables();
    let max_eo = plans.iter().map(|(_, p)| p.max_eo_len()).max().unwrap();
    let t0 = Instant::now();
    type Row = (String, Vec<(Outcome, Vec<(StepKind, u64)>)>);
    let mut rows: Vec<Option<Row>> = (0..scrambles.len()).map(|_| None).collect();
    let chunk = scrambles.len().div_ceil(threads).max(1);
    std::thread::scope(|sc| {
        for (part, out) in scrambles.chunks(chunk).zip(rows.chunks_mut(chunk)) {
            let (t, plans, costs, human) = (&t, &plans, &costs, &human);
            sc.spawn(move || {
                for ((id, moves), slot) in part.iter().zip(out.iter_mut()) {
                    let w = Scramble::new(t, moves, seed, *id, max_eo);
                    let mut b = w.bad;
                    b.sort();
                    let feat = format!("{}-{}-{}\t{}\t{}\t{}", b[0], b[1], b[2], w.eo_min, w.n_eo4, w.n_eo4_lin);
                    let keep = (*id as usize) < first + logn;
                    let res = plans
                        .iter()
                        .map(|(_, p)| {
                            let r = Attempt::new(&w, costs, human, p, keep).run();
                            (r.outcome, r.steps.iter().map(|s| (s.kind, s.ms)).collect())
                        })
                        .collect();
                    *slot = Some((feat, res));
                }
            });
        }
    });
    let rows: Vec<Row> = rows.into_iter().map(Option::unwrap).collect();
    let secs = t0.elapsed().as_secs_f64();
    let path = o.need("out")?;
    let mut out = std::io::BufWriter::new(std::fs::File::create(path).map_err(|e| format!("{path}: {e}"))?);
    let names: Vec<&str> = StepKind::ALL.iter().map(|k| k.name()).collect();
    let mut header = String::from("policy\tscr\tbad\teo_min\tn_eo4\tn_eo4_lin\tlen\tt_end_ms\tbest_found\teos\tdrs\tdrs_finished\tbest_dr\tfirst_sol_ms\tfirst_sol_len\tres_dr_len\tres_subset\tres_exact\tres_fin\tres_dr_ms\tres_sol_ms\tlast_eo_ms\tlast_dr_ms\toracle_page\tbanks");
    for k in &names {
        header += &format!("\tn_{k}");
    }
    for k in &names {
        header += &format!("\tms_{k}");
    }
    header += "\treplay_fail\tsolution";
    writeln!(out, "{header}").unwrap();
    let mut failures = 0;
    for (pi, (name, _)) in plans.iter().enumerate() {
        for (si, (id, _)) in scrambles.iter().enumerate() {
            let (feat, res) = &rows[si];
            let o = &res[pi].0;
            failures += o.replay_failures;
            let subset = if o.len > 0 { t.htr.sub48_names[o.res_subset.unwrap()].as_str() } else { "-" };
            write!(
                out,
                "{name}\t{id}\t{feat}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{subset}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",
                o.len, o.t_end, o.best_found, o.eos_found, o.drs_found, o.drs_finished, o.best_dr, o.first_sol_t,
                o.first_sol_len, o.res_dr_len, o.res_optimal, o.res_fin, o.res_dr_t, o.res_sol_t, o.last_eo_t, o.last_dr_t,
                o.oracle_page, o.writes.len()
            )
            .unwrap();
            for k in 0..11 {
                write!(out, "\t{}", o.count[k]).unwrap();
            }
            for k in 0..11 {
                write!(out, "\t{}", o.time[k]).unwrap();
            }
            writeln!(out, "\t{}\t{}", o.replay_failures, format_moves(&o.moves)).unwrap();
        }
    }
    if let Some(lp) = o.0.get("log") {
        let mut lf = std::io::BufWriter::new(std::fs::File::create(lp).map_err(|e| format!("{lp}: {e}"))?);
        for (pi, (name, _)) in plans.iter().enumerate() {
            for (si, (id, moves)) in scrambles.iter().enumerate() {
                let (o, steps) = &rows[si].1[pi];
                if steps.is_empty() {
                    continue;
                }
                let steps: Vec<String> = steps.iter().map(|(k, ms)| format!("[{},{}]", *k as usize, ms)).collect();
                let banks: Vec<String> = o.writes.iter().map(|(t, l)| format!("[{t},{l}]")).collect();
                writeln!(
                    lf,
                    "{{\"policy\":\"{name}\",\"scr\":{id},\"scramble\":\"{}\",\"len\":{},\"solution\":\"{}\",\"t_end_ms\":{},\"steps\":[{}],\"banks\":[{}]}}",
                    format_moves(moves), o.len, format_moves(&o.moves), o.t_end, steps.join(","), banks.join(",")
                )
                .unwrap();
            }
        }
    }
    eprintln!("{} scrambles x {} plans in {:.1} s ({} threads); replay failures: {}", scrambles.len(), plans.len(), secs, threads, failures);
    if failures > 0 {
        return Err("a solution did not solve its scramble".into());
    }
    Ok(())
}

fn trace(o: &Opts) -> Result<(), String> {
    let moves = parse_moves(o.need("scramble")?)?;
    let settings: Settings = match o.0.get("settings") {
        Some(p) => serde_json::from_str(&std::fs::read_to_string(p).map_err(|e| format!("{p}: {e}"))?).map_err(|e| format!("{p}: {e}"))?,
        None => Settings::default(),
    };
    let t = tables();
    let t0 = Instant::now();
    let r = attempt_sim::simulate(&t, &moves, &settings);
    eprintln!("attempt in {:.3} s", t0.elapsed().as_secs_f64());
    let json = serde_json::json!({
        "outcome": r.outcome,
        "solutions": r.solutions,
        "steps": r.steps,
    });
    println!("{}", serde_json::to_string_pretty(&json).unwrap());
    Ok(())
}

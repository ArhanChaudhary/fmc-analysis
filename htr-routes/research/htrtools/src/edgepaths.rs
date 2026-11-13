//! Edge paths of the linear finish: for each sampled DR state (the states of `htrtools routes`, read back from
//! `states_<subset>.tsv`, columns c, e, s), every finish of length <= optimum + 1 read forward on the normal side
//! only (no NISS, no inverse reading), and its *edge path*: the label (corner subset and bad edges, `Model::label`)
//! of the start state and of the state after each quarter turn, up to the first state in HTR.  A start state already
//! in HTR has the one-label path.
//!
//! Output per subset, `ep_<subset>.tsv`: idx, d (optimum), capped (finish enumeration stopped at the cap), nopt
//! (optimal finishes), then one field per distinct path: `id:delta:hopt:hany`
//!   delta  shortest finish with this path minus the optimum (0 or 1)
//!   hopt   shortest HTR (moves until the first HTR state) among the optimal finishes with this path (99 if none)
//!   hany   the same among every finish of length <= optimum + 1
//! and the global `ep_keys.tsv` (id, path), labels joined by " > ".
use crate::model::{is_qt, label_name, Model};
use rayon::prelude::*;
use std::collections::HashMap;
use std::fs::{self, File};
use std::io::{self, BufRead, BufReader, BufWriter, Write};
use std::path::Path;
use std::sync::Mutex;
use std::time::Instant;

pub fn path_of(m: &Model, moves: &[u8], p: &[(usize, usize)]) -> (Vec<u8>, u8) {
    let (c, e) = p[0];
    let mut v = vec![m.label(c, e)];
    if m.in_h(c, e) {
        return (v, 0);
    }
    for i in 1..=moves.len() {
        if is_qt(moves[i - 1]) {
            let (c, e) = p[i];
            v.push(m.label(c, e));
            if m.in_h(c, e) {
                return (v, i as u8);
            }
        }
    }
    unreachable!("a finish ends in HTR")
}

pub fn edgepaths(ex: &str, states: &str, out: &str, subs: &str) -> io::Result<()> {
    let out = Path::new(out);
    fs::create_dir_all(out)?;
    let t0 = Instant::now();
    let m = Model::new(Some(Path::new(ex)), None);
    eprintln!("tables loaded in {:.1}s", t0.elapsed().as_secs_f64());
    let interner: Mutex<(HashMap<Vec<u8>, u32>, Vec<Vec<u8>>)> = Mutex::new((HashMap::new(), Vec::new()));
    let cap: u64 = 3_000_000;
    for name in subs.split(',') {
        let ts = Instant::now();
        let f = BufReader::new(File::open(Path::new(states).join(format!("states_{}.tsv", name)))?);
        let mut lines = f.lines();
        let head: Vec<String> = lines.next().unwrap()?.split('\t').map(String::from).collect();
        let col = |k: &str| head.iter().position(|h| h == k).unwrap();
        let (ci, ei, si, ii, di) = (col("c"), col("e"), col("s"), col("idx"), col("d"));
        let rows: Vec<(usize, usize, usize, usize, u8)> = lines
            .map(|l| {
                let l = l.unwrap();
                let v: Vec<&str> = l.split('\t').collect();
                (v[ii].parse().unwrap(), v[ci].parse().unwrap(), v[ei].parse().unwrap(), v[si].parse().unwrap(), v[di].parse().unwrap())
            })
            .collect();
        let res: Vec<String> = rows
            .par_iter()
            .map(|&(idx, c, e, s, d0)| {
                let x = (c, e, s);
                let d = m.depth(c, e, s);
                assert_eq!(d, d0, "optimum differs from the states file");
                let mut agg: HashMap<Vec<u8>, (u8, u8, u8)> = HashMap::new();
                let mut nopt = 0u64;
                let ok = crate::routes::finishes(&m, x, d as usize + 1, cap, &mut |moves, path| {
                    let delta = (moves.len() as u8) - d;
                    if delta == 0 {
                        nopt += 1;
                    }
                    let (k, h) = path_of(&m, moves, path);
                    let en = agg.entry(k).or_insert((9, 99, 99));
                    en.0 = en.0.min(delta);
                    if delta == 0 {
                        en.1 = en.1.min(h);
                    }
                    en.2 = en.2.min(h);
                });
                let mut g = interner.lock().unwrap();
                let mut fields: Vec<(u32, (u8, u8, u8))> = agg
                    .into_iter()
                    .map(|(k, v)| {
                        let id = match g.0.get(&k) {
                            Some(&id) => id,
                            None => {
                                let id = g.1.len() as u32;
                                g.0.insert(k.clone(), id);
                                g.1.push(k);
                                id
                            }
                        };
                        (id, v)
                    })
                    .collect();
                drop(g);
                fields.sort_unstable();
                let mut line = format!("{}\t{}\t{}\t{}", idx, d, (!ok) as u8, nopt);
                for (id, (dl, ho, ha)) in fields {
                    line.push_str(&format!("\t{}:{}:{}:{}", id, dl, ho, ha));
                }
                line
            })
            .collect();
        let mut f = BufWriter::new(File::create(out.join(format!("ep_{}.tsv", name)))?);
        writeln!(f, "idx\td\tcapped\tnopt\tpaths")?;
        for l in &res {
            writeln!(f, "{}", l)?;
        }
        eprintln!("{:7} {} states in {:.1}s", name, rows.len(), ts.elapsed().as_secs_f64());
    }
    let g = interner.lock().unwrap();
    let mut f = BufWriter::new(File::create(out.join("ep_keys.tsv"))?);
    writeln!(f, "id\tpath")?;
    for (i, k) in g.1.iter().enumerate() {
        let s: Vec<String> = k.iter().map(|&l| label_name(l)).collect();
        writeln!(f, "{}\t{}", i, s.join(" > "))?;
    }
    eprintln!("total {:.1}s", t0.elapsed().as_secs_f64());
    Ok(())
}

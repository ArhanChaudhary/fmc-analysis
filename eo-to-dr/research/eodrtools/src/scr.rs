//! Questions A1-A3 and the per-scramble part of B4: what a scramble offers on the way to DR.
//!
//! For each scramble S (a line of moves):
//!   A1  the fewest turns to DR on each axis, normal and inverse (the full 4-bit `all_dr` table, one view per axis);
//!       the NISS length min over pre-moves B of |B| + d(B S), exact (see `niss_dr`); the number of DR solutions of
//!       each length on the normal side (canonical sequences that reach DR for the first time at their end, per axis);
//!       every optimal DR on the normal side, and in each the shortest EO it starts with (`estar`).
//!   A2  the best DR through an EO of at most k turns, k = 0..6: EO E (canonical, EO reached for the first time at
//!       its end), then turns keeping that EO to a DR on one of the two other axes (the eo-fb_dr table, EO-solved
//!       part); on the normal side, on the inverse side, and NISS EOs (moves on both sides, each side ending in a
//!       quarter turn of the EO axis, DR on either side).  Also the same with any turns after the EO.
//!   A3  the number of (EO, DR axis) pairs with EO of at most 4 or 5 turns and EO + DR at most N, N = 9..12.
//!   B4  the number of EOs of each length per axis and kind, and the optimal EO per axis, linear / inverse / NISS.

use crate::common::*;
use crate::cubie::{Cubie, SOLVED};
use rayon::prelude::*;

pub const K: usize = 6; // longest EO enumerated
const NV: usize = 3; // kinds of EO: 0 normal, 1 inverse, 2 NISS (both sides used)

pub struct Scr<'a> {
    pub c: &'a Ctx,
    pub full: &'a Full4,
    pub eo_dr: &'a Eo0,
    pub all0: &'a Eo0,
    pub cap: usize,
    pub kniss: usize,
}

#[derive(Clone)]
pub struct Route {
    pub total: u8,
    pub y: usize,
    pub x: usize,
    pub eo: Vec<usize>,
    pub dr: Vec<usize>,
}

pub struct Out {
    pub d6: [[u8; 3]; 2],
    pub dniss: u8,
    pub niss_wit: (Vec<usize>, Vec<usize>, usize), // normal moves, inverse moves, axis
    pub counts: [[u64; 16]; 3],                     // [axis][length] DR solutions, normal side
    pub nopt: u64,
    pub estar: u8,
    pub estar_wit: (Vec<usize>, usize, usize, usize), // optimal DR solution with the shortest EO start, axis, EO axis, EO length
    pub best: [[[u8; K + 1]; 3]; NV],
    pub brk: [[u8; K + 1]; 3],
    pub pairs: [[[[u32; 4]; 2]; 3]; NV],
    pub neo: [[[u32; K + 1]; 3]; NV],
    pub eo_opt: [[u8; 3]; 3], // [kind][axis]
    pub bad: [u32; 3],
    pub routes: Vec<Option<Route>>, // best normal-side route through an EO of at most 4, 5, 6
}

impl<'a> Scr<'a> {
    fn dr_dist(&self, s: &Cubie, x: usize) -> u8 {
        self.full.at(self.c.coords(&self.c.view(s, self.c.rot_dr[x])))
    }

    /// Shortest path to DR on U/D in a view, with the full table (all turns), as view moves.
    fn full_path(&self, v: &Cubie) -> Vec<usize> {
        let mut c = self.c.coords(v);
        let mut out = Vec::new();
        let mut last = NONE;
        loop {
            let d = self.full.at(c);
            if d == 0 {
                return out;
            }
            let mv = (0..18).find(|&mv| canon_ok(last, mv) && self.full.at(self.c.mv(c, mv)) == d - 1).expect("no descent");
            c = self.c.mv(c, mv);
            out.push(mv);
            last = mv;
        }
    }

    /// Shortest path to DR on U/D keeping F/B EO, from an EO-solved view, as view moves.
    pub fn eo_path(&self, v: &Cubie) -> Vec<usize> {
        let mut c = self.c.coords(v);
        assert_eq!(c.1, 0);
        let mut out = Vec::new();
        let mut last = NONE;
        loop {
            let d = self.eo_dr.at(c.0, c.2);
            if d == 0 {
                return out;
            }
            let mv = (0..18)
                .find(|&mv| !y_quarter(mv, 2) && canon_ok(last, mv) && { let n = self.c.mv(c, mv); self.eo_dr.at(n.0, n.2) == d - 1 })
                .expect("no descent");
            c = self.c.mv(c, mv);
            out.push(mv);
            last = mv;
        }
    }

    fn unview(&self, r: usize, seq: &[usize]) -> Vec<usize> {
        seq.iter().map(|&mv| self.c.m.unview(r, mv)).collect()
    }

    /// DR solutions on the normal side, axis x, up to `cap` turns: counts per length; `opt` = the optimal length,
    /// whose solutions are handed to `f` (own labels).
    #[allow(clippy::too_many_arguments)]
    fn dr_dfs(&self, x: usize, c: (usize, usize, usize), depth: usize, last: usize, path: &mut Vec<usize>, counts: &mut [u64; 16], opt: usize, f: &mut dyn FnMut(&[usize])) {
        let d = self.full.at(c) as usize;
        if d == 0 {
            counts[depth] += 1;
            if depth == opt {
                let own = self.unview(self.c.rot_dr[x], path);
                f(&own);
            }
            return;
        }
        if depth + d > self.cap {
            return;
        }
        for mv in 0..18 {
            if !canon_ok(last, mv) {
                continue;
            }
            path.push(mv);
            self.dr_dfs(x, self.c.mv(c, mv), depth + 1, mv, path, counts, opt, f);
            path.pop();
        }
    }

    /// All canonical sequences C of exactly `k` turns (own labels), with P = C^-1 as a state: `f(C, P)`.
    fn premoves(&self, k: usize, last: usize, c: &mut Vec<usize>, p: &Cubie, f: &mut dyn FnMut(&[usize], &Cubie)) {
        if c.len() == k {
            f(c, p);
            return;
        }
        for mv in 0..18 {
            if !canon_ok(last, mv) {
                continue;
            }
            let q = self.c.mvc[inv_move(mv)].then(p);
            c.push(mv);
            self.premoves(k, mv, c, &q, f);
            c.pop();
        }
    }

    /// Fewest turns to DR with NISS: min over C (turns on the other side) of |C| + d(C^-1 base), both bases.
    /// A solution with |C| = k on one side and k' on the other has its shorter side <= total / 2, so once
    /// 2k >= best every shorter solution has been seen.
    fn niss_dr(&self, sides: &[Cubie; 2], d6: &[[u8; 3]; 2]) -> (u8, (Vec<usize>, Vec<usize>, usize)) {
        let mut best = 99u8;
        let mut wit = (0usize, Vec::new(), 0usize); // base side, C, axis
        for side in 0..2 {
            for x in 0..3 {
                if d6[side][x] < best {
                    best = d6[side][x];
                    wit = (side, Vec::new(), x);
                }
            }
        }
        let mut k = 1;
        while 2 * k < best as usize {
            for side in 0..2 {
                let base = sides[side];
                let mut f = |c: &[usize], p: &Cubie| {
                    let st = p.then(&base);
                    for x in 0..3 {
                        let v = k as u8 + self.dr_dist(&st, x);
                        if v < best {
                            best = v;
                            wit = (side, c.to_vec(), x);
                        }
                    }
                };
                self.premoves(k, NONE, &mut Vec::new(), &SOLVED, &mut f);
            }
            k += 1;
        }
        // write the solution out: C on one side, the rest on the other
        let (side, c, x) = wit;
        let p = invert(&c).iter().fold(SOLVED, |a, &mv| a.then(&self.c.mvc[mv]));
        let state = p.then(&sides[side]);
        let a = self.unview(self.c.rot_dr[x], &self.full_path(&self.c.view(&state, self.c.rot_dr[x])));
        assert_eq!(c.len() + a.len(), best as usize);
        let (normal, inverse) = if side == 0 { (a, c) } else { (c, a) };
        (best, (normal, inverse, x))
    }

    /// EOs on axis y from the views v (for the two DR axes), first reach, at most `left` more turns.
    #[allow(clippy::too_many_arguments)]
    fn eo_dfs(&self, y: usize, rot: [usize; 2], v: &[Cubie; 2], depth: usize, left: usize, last: usize, path: &mut Vec<usize>, f: &mut dyn FnMut(usize, &[Cubie; 2], &[usize])) {
        let e = Ctx::eo(&v[0]);
        if e == 0 {
            f(depth, v, path);
            return;
        }
        if self.c.eodist[e] as usize > left {
            return;
        }
        for mv in 0..18 {
            if !canon_ok(last, mv) {
                continue;
            }
            let w = [self.c.m.turn(&v[0], self.c.vmove[rot[0]][mv]), self.c.m.turn(&v[1], self.c.vmove[rot[1]][mv])];
            path.push(mv);
            self.eo_dfs(y, rot, &w, depth + 1, left - 1, mv, path, f);
            path.pop();
        }
    }

    pub fn run(&self, s: &Cubie) -> Out {
        let c = self.c;
        let si = s.inverse();
        let sides = [*s, si];
        let mut d6 = [[0u8; 3]; 2];
        for side in 0..2 {
            for x in 0..3 {
                d6[side][x] = self.dr_dist(&sides[side], x);
            }
        }
        let dlin = *d6[0].iter().min().unwrap() as usize;
        let (dniss, niss_wit) = self.niss_dr(&sides, &d6);

        // DR solutions on the normal side; optimal ones and the EO they start with
        let mut counts = [[0u64; 16]; 3];
        let mut nopt = 0u64;
        let mut estar = 99u8;
        let mut estar_wit = (Vec::new(), 0, 0, 0);
        for x in 0..3 {
            let v = c.view(s, c.rot_dr[x]);
            let mut f = |sol: &[usize]| {
                nopt += 1;
                for y in 0..3 {
                    if y == x {
                        continue;
                    }
                    // the EO ends at the last quarter turn of y; a half turn of the opposite face just before it
                    // commutes with it, so the EO can end one turn earlier (F2 B -> B F2)
                    let mut e = sol.iter().rposition(|&mv| y_quarter(mv, y)).map_or(0, |i| i + 1);
                    if e >= 2 && sol[e - 2] / 6 == sol[e - 1] / 6 && !y_quarter(sol[e - 2], y) {
                        e -= 1;
                    }
                    let e = e as u8;
                    if e < estar {
                        estar = e;
                        estar_wit = (sol.to_vec(), x, y, e as usize);
                    }
                }
            };
            self.dr_dfs(x, c.coords(&v), 0, NONE, &mut Vec::new(), &mut counts[x], dlin, &mut f);
        }

        // EOs
        let mut best = [[[99u8; K + 1]; 3]; NV];
        let mut brk = [[99u8; K + 1]; 3];
        let mut pairs = [[[[0u32; 4]; 2]; 3]; NV];
        let mut neo = [[[0u32; K + 1]; 3]; NV];
        let mut routes: Vec<Option<Route>> = vec![None, None, None];
        for y in 0..3 {
            let xs: Vec<usize> = (0..3).filter(|&x| x != y).collect();
            let rot = [c.rot_pair[xs[0]][y], c.rot_pair[xs[1]][y]];
            let mut record = |kind: usize, len: usize, tot: [u8; 2], brk_t: Option<[u8; 2]>, best: &mut [[[u8; K + 1]; 3]; NV], brk: &mut [[u8; K + 1]; 3]| {
                neo[kind][y][len] += 1;
                let t = tot[0].min(tot[1]);
                if t < best[kind][y][len] {
                    best[kind][y][len] = t;
                }
                if let Some(b) = brk_t {
                    let bb = b[0].min(b[1]);
                    if bb < brk[y][len] {
                        brk[y][len] = bb;
                    }
                }
                for (ki, k) in [4usize, 5].iter().enumerate() {
                    if len <= *k {
                        for (ni, n) in (9u8..=12).enumerate() {
                            pairs[kind][y][ki][ni] += tot.iter().filter(|&&t| t <= n).count() as u32;
                        }
                    }
                }
            };
            // normal and inverse sides, linear
            for kind in 0..2 {
                let base = sides[kind];
                let v = [c.view(&base, rot[0]), c.view(&base, rot[1])];
                let mut f = |len: usize, w: &[Cubie; 2], path: &[usize]| {
                    let mut tot = [0u8; 2];
                    let mut bt = [0u8; 2];
                    for i in 0..2 {
                        let (co, eo, sl) = c.coords(&w[i]);
                        debug_assert_eq!(eo, 0);
                        tot[i] = len as u8 + self.eo_dr.at(co, sl);
                        bt[i] = len as u8 + self.all0.at(co, sl);
                    }
                    record(kind, len, tot, if kind == 0 { Some(bt) } else { None }, &mut best, &mut brk);
                    if kind == 0 {
                        for (ri, k) in [4usize, 5, 6].iter().enumerate() {
                            for i in 0..2 {
                                if len <= *k && routes[ri].as_ref().map_or(true, |r| tot[i] < r.total) {
                                    let dr = self.unview(rot[i], &self.eo_path(&w[i]));
                                    routes[ri] = Some(Route { total: tot[i], y, x: xs[i], eo: path.to_vec(), dr });
                                }
                            }
                        }
                    }
                };
                self.eo_dfs(y, rot, &v, 0, K, NONE, &mut Vec::new(), &mut f);
            }
        }
        // NISS EOs: C on the inverse side (last turn a quarter turn of y), then A >= 1 turn on the normal side
        if self.kniss >= 2 {
            let sv: Vec<Cubie> = (0..3).map(|y| c.view(s, c.rot_eo[y])).collect();
            for clen in 1..self.kniss {
                let mut f = |cseq: &[usize], p: &Cubie| {
                    let lastc = *cseq.last().unwrap();
                    let mut ps: Option<Cubie> = None;
                    for y in 0..3 {
                        if !y_quarter(lastc, y) {
                            continue;
                        }
                        let pv = c.view(p, c.rot_eo[y]);
                        let e = Ctx::eo_then(&pv, &sv[y]);
                        let dist = c.eodist[e] as usize;
                        if dist == 0 || clen + dist > self.kniss {
                            continue;
                        }
                        let st = *ps.get_or_insert_with(|| p.then(s));
                        let xs: Vec<usize> = (0..3).filter(|&x| x != y).collect();
                        let rot = [c.rot_pair[xs[0]][y], c.rot_pair[xs[1]][y]];
                        let v = [c.view(&st, rot[0]), c.view(&st, rot[1])];
                        let mut g = |alen: usize, w: &[Cubie; 2], _path: &[usize]| {
                            let len = clen + alen;
                            let mut tot = [0u8; 2];
                            for i in 0..2 {
                                let (co, _, sl) = c.coords(&w[i]);
                                let (co2, _, sl2) = c.coords(&w[i].inverse());
                                tot[i] = len as u8 + self.eo_dr.at(co, sl).min(self.eo_dr.at(co2, sl2));
                            }
                            neo[2][y][len] += 1;
                            let t = tot[0].min(tot[1]);
                            if t < best[2][y][len] {
                                best[2][y][len] = t;
                            }
                            for (ki, k) in [4usize, 5].iter().enumerate() {
                                if len <= *k {
                                    for (ni, n) in (9u8..=12).enumerate() {
                                        pairs[2][y][ki][ni] += tot.iter().filter(|&&t| t <= n).count() as u32;
                                    }
                                }
                            }
                        };
                        self.eo_dfs(y, rot, &v, 0, self.kniss - clen, NONE, &mut Vec::new(), &mut g);
                    }
                };
                self.premoves(clen, NONE, &mut Vec::new(), &SOLVED, &mut f);
            }
        }
        // cumulative minima: best with an EO of at most k turns
        for kind in 0..NV {
            for y in 0..3 {
                for k in 1..=K {
                    best[kind][y][k] = best[kind][y][k].min(best[kind][y][k - 1]);
                    if kind == 0 {
                        brk[y][k] = brk[y][k].min(brk[y][k - 1]);
                    }
                }
            }
        }

        // optimal EO per axis: linear, inverse, NISS (exact, same argument as niss_dr)
        let mut eo_opt = [[0u8; 3]; 3];
        let mut bad = [0u32; 3];
        for y in 0..3 {
            let base = [c.view(s, c.rot_eo[y]), c.view(&si, c.rot_eo[y])];
            eo_opt[0][y] = c.eodist[Ctx::eo(&base[0])];
            eo_opt[1][y] = c.eodist[Ctx::eo(&base[1])];
            bad[y] = base[0].ef.iter().map(|&f| f as u32).sum();
            let mut b = eo_opt[0][y].min(eo_opt[1][y]);
            let mut k = 1;
            while 2 * k < b as usize {
                for side in 0..2 {
                    let mut f = |_: &[usize], p: &Cubie| {
                        let pv = c.view(p, c.rot_eo[y]);
                        let v = k as u8 + c.eodist[Ctx::eo_then(&pv, &base[side])];
                        if v < b {
                            b = v;
                        }
                    };
                    self.premoves(k, NONE, &mut Vec::new(), &SOLVED, &mut f);
                }
                k += 1;
            }
            eo_opt[2][y] = b;
        }
        Out { d6, dniss, niss_wit, counts, nopt, estar, estar_wit, best, brk, pairs, neo, eo_opt, bad, routes }
    }
}

pub fn header(cap: usize) -> String {
    let mut h: Vec<String> = vec!["i".into()];
    for side in ["n", "i"] {
        for x in AXIS_NAME {
            h.push(format!("d_{side}_{x}"));
        }
    }
    h.push("dniss".into());
    for x in AXIS_NAME {
        for l in 0..=cap {
            h.push(format!("ndr_{x}_{l}"));
        }
    }
    h.push("nopt".into());
    h.push("estar".into());
    for kind in ["n", "i", "x"] {
        for y in AXIS_NAME {
            for k in 0..=K {
                h.push(format!("best_{kind}_{y}_{k}"));
            }
        }
    }
    for y in AXIS_NAME {
        for k in 0..=K {
            h.push(format!("brk_{y}_{k}"));
        }
    }
    for kind in ["n", "i", "x"] {
        for y in AXIS_NAME {
            for k in [4, 5] {
                for n in 9..=12 {
                    h.push(format!("pairs_{kind}_{y}_{k}_{n}"));
                }
            }
        }
    }
    for kind in ["n", "i", "x"] {
        for y in AXIS_NAME {
            for l in 0..=K {
                h.push(format!("neo_{kind}_{y}_{l}"));
            }
        }
    }
    for kind in ["n", "i", "x"] {
        for y in AXIS_NAME {
            h.push(format!("eoopt_{kind}_{y}"));
        }
    }
    for y in AXIS_NAME {
        h.push(format!("bad_{y}"));
    }
    for w in ["niss_normal", "niss_inverse", "niss_axis", "opt_solution", "opt_axis", "estar_eo_axis", "route4", "route5", "route6"] {
        h.push(w.into());
    }
    h.join("\t")
}

fn route_text(r: &Option<Route>) -> String {
    match r {
        None => "-".into(),
        Some(r) => format!("{}:{}>{}:{} | {}", r.total, AXIS_NAME[r.y], AXIS_NAME[r.x], text(&r.eo), text(&r.dr)),
    }
}

pub fn row(i: usize, o: &Out, cap: usize) -> String {
    let mut v: Vec<String> = vec![i.to_string()];
    for side in 0..2 {
        for x in 0..3 {
            v.push(o.d6[side][x].to_string());
        }
    }
    v.push(o.dniss.to_string());
    for x in 0..3 {
        for l in 0..=cap {
            v.push(o.counts[x][l].to_string());
        }
    }
    v.push(o.nopt.to_string());
    v.push(o.estar.to_string());
    for kind in 0..NV {
        for y in 0..3 {
            for k in 0..=K {
                v.push(o.best[kind][y][k].to_string());
            }
        }
    }
    for y in 0..3 {
        for k in 0..=K {
            v.push(o.brk[y][k].to_string());
        }
    }
    for kind in 0..NV {
        for y in 0..3 {
            for ki in 0..2 {
                for ni in 0..4 {
                    v.push(o.pairs[kind][y][ki][ni].to_string());
                }
            }
        }
    }
    for kind in 0..NV {
        for y in 0..3 {
            for l in 0..=K {
                v.push(o.neo[kind][y][l].to_string());
            }
        }
    }
    for kind in 0..3 {
        for y in 0..3 {
            v.push(o.eo_opt[kind][y].to_string());
        }
    }
    for y in 0..3 {
        v.push(o.bad[y].to_string());
    }
    v.push(text(&o.niss_wit.0));
    v.push(text(&o.niss_wit.1));
    v.push(AXIS_NAME[o.niss_wit.2].into());
    v.push(text(&o.estar_wit.0));
    v.push(AXIS_NAME[o.estar_wit.1].into());
    v.push(format!("{}:{}", AXIS_NAME[o.estar_wit.2], o.estar_wit.3));
    for r in &o.routes {
        v.push(route_text(r));
    }
    v.iter().map(|s| if s.is_empty() { "-".to_string() } else { s.clone() }).collect::<Vec<_>>().join("\t")
}

/// eodrtools scr <scrambles file> <cap> <kniss> [first] [count]
pub fn cmd(a: &[String]) {
    let ctx = Ctx::new();
    let cap: usize = a[1].parse().unwrap();
    let kniss: usize = a[2].parse().unwrap();
    assert!(cap <= 15 && kniss <= K);
    let scr: Vec<String> = std::fs::read_to_string(&a[0]).unwrap().lines().filter(|l| !l.starts_with('#') && !l.trim().is_empty()).map(|l| l.to_string()).collect();
    let first: usize = a.get(3).map_or(0, |v| v.parse().unwrap());
    let count: usize = a.get(4).map_or(scr.len(), |v| v.parse().unwrap());
    let t0 = std::time::Instant::now();
    let full = Full4::open(&format!("{XS}/bfs/all_dr.u8"));
    let here = std::env::var("EODR_OUT").unwrap_or_else(|_| "/data/fmc/eo-to-dr/research/out".into());
    let eo_dr = Eo0::load(&format!("{here}/big/eo-fb_dr_eo0.u8"));
    let all0 = Eo0::load(&format!("{here}/big/all_dr_eo0.u8"));
    eprintln!("tables loaded in {:.1}s", t0.elapsed().as_secs_f64());
    let sc = Scr { c: &ctx, full: &full, eo_dr: &eo_dr, all0: &all0, cap, kniss };
    println!("{}", header(cap));
    let todo: Vec<(usize, &String)> = scr.iter().enumerate().skip(first).take(count).collect();
    for chunk in todo.chunks(400) {
        let rows: Vec<String> = chunk
            .par_iter()
            .map(|(i, line)| {
                let s = ctx.m.apply(&SOLVED, &parse(line));
                row(*i + 1, &sc.run(&s), cap)
            })
            .collect();
        for r in rows {
            println!("{r}");
        }
        eprintln!("{} scrambles, {:.0}s", chunk.last().unwrap().0 + 1, t0.elapsed().as_secs_f64());
    }
}

/// eodrtools eolist <k> "<scramble>" ...: every linear EO of at most k turns on the normal side, with, for each of
/// the two DR axes, the case and the fewest turns to DR (and one way) in five ways: EO kept; EO kept after the EO's
/// last turn is inverted; EO kept on the inverse side; any turns; and the case of the inverse.
/// Columns: scramble, eo axis, eo, dr axis, case, plain, plain route, switched, switched route (EO with last turn
/// inverted, then DR), inverse, inverse moves (to be done on the inverse scramble after the EO's inverse... written
/// as NISS: normal = EO, inverse = these), any, any-turn route.
pub fn eolist(a: &[String]) {
    let ctx = Ctx::new();
    let k: usize = a[0].parse().unwrap();
    let full = Full4::open(&format!("{XS}/bfs/all_dr.u8"));
    let here = std::env::var("EODR_OUT").unwrap_or_else(|_| "/data/fmc/eo-to-dr/research/out".into());
    let eo_dr = Eo0::load(&format!("{here}/big/eo-fb_dr_eo0.u8"));
    let all0 = Eo0::load(&format!("{here}/big/all_dr_eo0.u8"));
    let sc = Scr { c: &ctx, full: &full, eo_dr: &eo_dr, all0: &all0, cap: 0, kniss: 0 };
    println!("scramble\teo_axis\teo\tdr_axis\tcase\tplain\tplain_dr\tswitched\tswitched_eo\tswitched_dr\tinverse\tinverse_dr\tany\tany_dr\tinverse_case");
    for line in &a[1..] {
        let s = ctx.m.apply(&SOLVED, &parse(line));
        for y in 0..3 {
            let xs: Vec<usize> = (0..3).filter(|&x| x != y).collect();
            let rot = [ctx.rot_pair[xs[0]][y], ctx.rot_pair[xs[1]][y]];
            let v = [ctx.view(&s, rot[0]), ctx.view(&s, rot[1])];
            let mut f = |len: usize, w: &[Cubie; 2], path: &[usize]| {
                let _ = len;
                for i in 0..2 {
                    let r = rot[i];
                    let t = w[i];
                    let (bc, be) = ctx.drm(&t);
                    let plain = sc.unview(r, &sc.eo_path(&t));
                    // last EO turn the other way
                    let (sw_eo, sw_dr) = if let Some(&lm) = path.last() {
                        let mut e2 = path.to_vec();
                        *e2.last_mut().unwrap() = inv_move(lm);
                        let t2 = ctx.view(&ctx.m.apply(&s, &e2), r);
                        (e2, sc.unview(r, &sc.eo_path(&t2)))
                    } else {
                        (vec![], plain.clone())
                    };
                    let ti = t.inverse();
                    let inv = sc.unview(r, &sc.eo_path(&ti));
                    let (ic, ie) = ctx.drm(&ti);
                    let any = sc.unview(r, &sc.full_path(&t));
                    println!(
                        "{line}\t{}\t{}\t{}\t{bc}c{be}e\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{ic}c{ie}e",
                        AXIS_NAME[y], text(path), AXIS_NAME[xs[i]], plain.len(), text(&plain), sw_dr.len(), text(&sw_eo), text(&sw_dr),
                        inv.len(), text(&inv), any.len(), text(&any)
                    );
                }
            };
            sc.eo_dfs(y, rot, &v, 0, k, NONE, &mut Vec::new(), &mut f);
        }
    }
}

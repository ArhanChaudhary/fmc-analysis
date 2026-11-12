//! eodrtools mkscr <n> <seed>: n uniformly random cube states (splitmix64, as is-dr-xs-worth-it's samples), each
//! written as a scramble: a shortest path to DR on U/D (all_dr) and an optimal DR finish (judging-a-dr's exact
//! table), inverted.  Not short scrambles, but exact random states; replayed by src/check_scrambles.py.
//! (nissy 2.0.8's `scramble` was the first choice; it draws the edge permutation as rand() % 12!, a modulo bias that
//! makes low permutation indices 25% more likely, and its twisted-corner counts are off too; see README.)

use crate::common::*;
use crate::core::{rank_perm, Core, St};
use crate::cubie::SOLVED;
use crate::reduced::{CornerClasses, SliceIndex, ROW};
use rayon::prelude::*;

struct Exact {
    core: Core,
    cc: CornerClasses,
    si: SliceIndex,
    tab: Vec<u8>,
}
impl Exact {
    fn depth(&self, c: &[u8; 8], e: &[u8; 8], s: &[u8; 4]) -> u8 {
        let (cr, er, sr) = (rank_perm(c), rank_perm(e), rank_perm(s));
        let (k, sym) = (self.cc.cclass[cr] as usize, self.cc.csymto[cr] as usize);
        self.tab[k * ROW + self.core.esym[sym][er] as usize * 12 + self.si.to12[self.core.ssym[sym][sr] as usize] as usize]
    }
    fn path(&self, c: &[u8; 8], e: &[u8; 8], s: &[u8; 4]) -> Vec<usize> {
        const DR_MOVE: [usize; 10] = [0, 1, 2, 3, 4, 5, 7, 10, 13, 16];
        let mut st = St { c: *c, e: *e, s: *s };
        let mut d = self.depth(c, e, s);
        let mut out = Vec::new();
        while d > 0 {
            let mv = (0..10).find(|&mv| { let nx = st.apply_move(mv); self.depth(&nx.c, &nx.e, &nx.s) == d - 1 }).expect("not a distance");
            st = st.apply_move(mv);
            d -= 1;
            out.push(DR_MOVE[mv]);
        }
        out
    }
}

pub fn cmd(a: &[String]) {
    let (n, seed): (usize, u64) = (a[0].parse().unwrap(), a[1].parse().unwrap());
    let c = Ctx::new();
    let full = Full4::open(&format!("{XS}/bfs/all_dr.u8"));
    let core = Core::new();
    let cc = CornerClasses::new(&core);
    let si = SliceIndex::new(&core);
    let tab = std::fs::read("/data/fmc/judging-a-dr/research/data/lean_exact_table.u8").expect("exact table");
    assert_eq!(tab.len(), cc.nclass * ROW);
    let ex = Exact { core, cc, si, tab };
    let lines: Vec<String> = (0..n)
        .into_par_iter()
        .map(|i| {
            let mut rng = Rng::new(seed, i as u64);
            let s = random_cube(&mut rng, false);
            // shortest path to DR on U/D
            let mut x = s;
            let mut path = Vec::new();
            let mut last = NONE;
            loop {
                let d = full.at(c.coords(&x));
                if d == 0 {
                    break;
                }
                let mv = (0..18).find(|&mv| canon_ok(last, mv) && full.at(c.mv(c.coords(&x), mv)) == d - 1).unwrap();
                x = c.m.turn(&x, mv);
                path.push(mv);
                last = mv;
            }
            let (cp, ep, sp) = c.m.dr_perms(&x).expect("not a DR");
            path.extend(ex.path(&cp, &ep, &sp));
            assert_eq!(c.m.apply(&s, &path), SOLVED);
            let scr = invert(&path);
            assert_eq!(c.m.apply(&SOLVED, &scr), s);
            text(&scr)
        })
        .collect();
    for l in lines {
        println!("{l}");
    }
}

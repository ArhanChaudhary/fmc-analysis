//! Checks of the case index against the whole-cube model of `attempt_sim::cube` (built from the geometry of the
//! turns, independent of the coset tables) and against the examples in the *Hitchhiker's Guide to HTR*.

use attempt_sim::cube::{parse_moves, Cube, Move, MoveTables};
use attempt_sim::dr::{St, AS_CUBE_MOVE, MOVE_FACE, MOVE_NAMES};
use htr_cases::cosets::modulo_e;
use htr_cases::{Index, DEFAULT_ABOVE, LONGEST, MOST_ABOVE};

/// The checks look at every HTR of up to this many moves, or the shortest ones when there are none that short.
const LIST_LEN: usize = 8;
use std::collections::HashSet;
use std::sync::OnceLock;

fn index() -> &'static Index {
    static INDEX: OnceLock<Index> = OnceLock::new();
    INDEX.get_or_init(Index::new)
}

fn cube() -> &'static MoveTables {
    static CUBE: OnceLock<MoveTables> = OnceLock::new();
    CUBE.get_or_init(MoveTables::new)
}

type Key = ([u8; 8], [u8; 12]);

/// The half-turn group, all 663,552 states of it, by breadth-first search on the whole cube.
fn half_turn_group() -> &'static HashSet<Key> {
    static H: OnceLock<HashSet<Key>> = OnceLock::new();
    H.get_or_init(|| {
        let mt = cube();
        let key = |c: &Cube| (c.cp, c.ep);
        let mut seen = HashSet::from([key(&Cube::SOLVED)]);
        let mut frontier = vec![Cube::SOLVED];
        while !frontier.is_empty() {
            let mut next = Vec::new();
            for c in &frontier {
                for f in 0..6 {
                    let d = mt.turn(c, Move::new(f, 2));
                    if seen.insert(key(&d)) {
                        next.push(d);
                    }
                }
            }
            frontier = next;
        }
        assert_eq!(seen.len(), 663_552);
        seen
    })
}

fn in_htr(c: &Cube) -> bool {
    c.co == [0; 8] && c.eo == [0; 12] && half_turn_group().contains(&(c.cp, c.ep))
}

/// In HTR or in HTR with the E slice turned (D U' away from HTR): HTR up to the E slice.
fn in_htr_up_to_e(c: &Cube) -> bool {
    in_htr(c) || in_htr(&cube().apply(c, &moves("D U'")))
}

fn moves(text: &str) -> Vec<Move> {
    parse_moves(text).unwrap()
}

/// The coset drawn for a case is made by its generator from solved; the turned one by U D' and then the generator.
fn start(i: usize, turned: bool) -> Cube {
    let info = index().info(i);
    let mut seq = if turned { moves("U D'") } else { Vec::new() };
    seq.extend(moves(&info.generator));
    cube().state(&seq)
}

#[test]
fn case_count() {
    let ix = index();
    assert_eq!(ix.cases.len(), 1272);
    assert_eq!(ix.cases.iter().map(|c| c.members.len()).sum::<usize>(), 29_400);
}

#[test]
fn every_member_of_a_case_is_as_far_from_htr() {
    let ix = index();
    for (i, c) in ix.cases.iter().enumerate() {
        let lengths: HashSet<u8> = c.members.iter().map(|&x| ix.cosets.dist[x]).collect();
        if i == 0 {
            assert_eq!(lengths, HashSet::from([0, 2]), "HTR and HTR with the E slice turned");
        } else {
            assert_eq!(lengths.len(), 1, "case {}", i + 1);
        }
    }
}

#[test]
fn generators_make_their_cases() {
    let ix = index();
    for i in 0..ix.cases.len() {
        let info = ix.info(i);
        assert_eq!(moves(&info.generator).len(), info.moves as usize, "case {}", i + 1);
        let found = ix.find(&info.generator, "", DEFAULT_ABOVE).unwrap();
        assert_eq!((found.number, found.axis, found.moves), (i + 1, "U/D", info.moves));
        assert_eq!(found.bad, (info.bad_corners.len() as u32, info.bad_edges.len() as u32));
        let x = ix.coset(i, false);
        assert_eq!(found.solutions, ix.solution_texts(x, ix.longest(x, DEFAULT_ABOVE)));
        if i == 0 {
            assert_eq!(ix.find(&info.turned.generator, "", DEFAULT_ABOVE).unwrap_err(), "that is already HTR");
            continue;
        }
        let turned = ix.find(&info.turned.generator, "", DEFAULT_ABOVE).unwrap();
        assert_eq!(turned.number, i + 1, "the E slice turned is the same case");
        let x = ix.coset(i, true);
        assert_eq!(turned.solutions, ix.solution_texts(x, ix.longest(x, DEFAULT_ABOVE)));
    }
}

/// A listed HTR: at most `max_len` moves, reaches HTR at its end and not before, ends in U or D (or U D).
fn check_listed(start: &Cube, text: &str, max_len: usize) {
    let seq = moves(text);
    assert!(!seq.is_empty() && seq.len() <= max_len, "{text}");
    let mut c = *start;
    for (k, &m) in seq.iter().enumerate() {
        assert!(k == 0 || !in_htr_up_to_e(&c), "{text} is in HTR up to the E slice after {k} moves");
        assert!(!in_htr(&c), "{text} is in HTR after {k} moves");
        c = cube().turn(&c, m);
    }
    assert!(in_htr(&c), "{text} does not reach HTR");
    let last = *seq.last().unwrap();
    assert!(last == Move::new(0, 1) || last == Move::new(1, 1), "{text} ends in {last}");
}

#[test]
fn every_listed_htr_reaches_htr() {
    let ix = index();
    let mut total = 0;
    for i in 0..ix.cases.len() {
        for turned in [false, true] {
            let s = start(i, turned);
            let x = ix.coset(i, turned);
            let list = all_texts(ix, x);
            let distinct: HashSet<&String> = list.iter().collect();
            assert_eq!(distinct.len(), list.len());
            let longest = LIST_LEN.max(ix.cosets.dist[x] as usize);
            for text in &list {
                check_listed(&s, text, longest);
            }
            if !(i == 0 && turned) {
                let shortest = list.iter().map(|t| moves(t).len()).min().unwrap();
                assert_eq!(shortest, ix.cosets.dist[x] as usize, "case {} turned {turned}", i + 1);
                if ix.cosets.dist[x] as usize > LIST_LEN {
                    assert!(list.iter().all(|t| moves(t).len() == shortest), "only the shortest past {LIST_LEN}");
                }
            }
            total += list.len();
        }
    }
    println!("listed HTRs checked, both versions: {total}");
    assert!(total > 100_000);
}

/// Every HTR of up to `max_len` DR moves, by trying every sequence on the whole cube, in the listed form.
fn brute_force(start: &Cube, max_len: usize) -> HashSet<String> {
    fn go(c: &Cube, path: &mut Vec<usize>, max_len: usize, out: &mut HashSet<String>) {
        if !path.is_empty() && in_htr_up_to_e(c) && !in_htr(c) {
            return;
        }
        if !path.is_empty() && in_htr(c) {
            let n = path.len();
            let block = if n >= 2 && MOVE_FACE[path[n - 1]] / 2 == MOVE_FACE[path[n - 2]] / 2 { 2 } else { 1 };
            if path[n - block..].iter().all(|&m| m == 0 || m == 3) {
                let text: Vec<String> = path.iter().map(|&m| Move(AS_CUBE_MOVE[m]).to_string()).collect();
                out.insert(text.join(" "));
            }
            return;
        }
        if path.len() == max_len {
            return;
        }
        for m in 0..10 {
            if let Some(&l) = path.last() {
                let (f, g) = (MOVE_FACE[l], MOVE_FACE[m]);
                if f == g || (f / 2 == g / 2 && g < f) {
                    continue;
                }
            }
            path.push(m);
            go(&cube().turn(c, Move(AS_CUBE_MOVE[m])), path, max_len, out);
            path.pop();
        }
    }
    let mut out = HashSet::new();
    go(start, &mut Vec::new(), max_len, &mut out);
    out
}

/// Every HTR in the listed form, before one is kept per set that is the same up to the E slice.
fn all_texts(ix: &Index, coset: usize) -> Vec<String> {
    ix.all_solutions(coset, LIST_LEN)
        .iter()
        .map(|p| p.iter().map(|&m| MOVE_NAMES[m as usize]).collect::<Vec<_>>().join(" "))
        .collect()
}

#[test]
fn lists_are_complete() {
    let ix = index();
    // a spread of cases up to 7 moves, and three to the full 8; case 1 (HTR up to the E slice) lists its 2-movers only
    let sample: Vec<(usize, usize)> =
        (53..ix.cases.len()).step_by(53).map(|i| (i, 7)).chain([(0, 2), (1, 8), (300, 8), (900, 8)]).collect();
    for (i, max_len) in sample {
        let listed: HashSet<String> =
            all_texts(ix, ix.coset(i, false)).into_iter().filter(|t| moves(t).len() <= max_len).collect();
        assert_eq!(brute_force(&start(i, false), max_len), listed, "case {}", i + 1);
    }
}

/// The setups of the *Hitchhiker's Guide to HTR* ("How to recognize HTR"), DR on R/L.
#[test]
fn the_guides_setups_have_their_subsets() {
    let ix = index();
    let setups = [
        ("R", "4a1"),
        ("R U2 R2 F2 R", "4a2"),
        ("R U2 R' U2 R2 F2 R", "4a3"),
        ("R U2 R' U2 R2 F2 R F2 R", "4a4"),
        ("R U2 R", "4b2"),
        ("R U2 R2 F2 R F2 R", "4b3"),
        ("R U2 R' U2 R2 F2 R D2 R", "4b4"),
        ("R D2 R F2 R' D2 R D2 R", "4b5"),
        ("L' B2 R' U2 R'", "2c3"),
        ("L' B2 R' U2 R U2 L", "2c4"),
        ("L' B2 R' U2 R U2 L' U2 L", "2c5"),
        ("R U2 R2 F2 R F2 R2 U2 R", "0c3"),
        ("R U2 R' F2 R2 U2 L' U2 L", "0c4"),
    ];
    for (setup, subset) in setups {
        // (the 0c4 setup is a DR on U/D as well, and is found there first)
        let found = ix.find(setup, "", DEFAULT_ABOVE).unwrap();
        assert_eq!(found.subset, subset, "{setup}");
    }
}

/// The guide's 4b2 and 2c3 examples ("How to solve 4b2", "How to solve 2c3").
#[test]
fn the_guides_parity_and_direction_examples() {
    let ix = index();
    let label = |setup: &str| {
        let f = ix.find(setup, "", DEFAULT_ABOVE).unwrap();
        (f.subset, f.edges, f.label.unwrap())
    };
    // "R U2 R' U2 L2 F2: This is 4b2 with 2 bad edges ... if you do the trigger, you will end up with fake HTR"
    assert_eq!(label("R U2 R' U2 L2 F2"), ("4b2", 2, "parity"));
    // "... B2 U2 L2 B2 R2 U2 ... you can do B2 L B2 L' or F2 R B2 R' to see that this 4b2 has parity"
    assert_eq!(label("R U2 R' U2 L2 F2 B2 U2 L2 B2 R2 U2"), ("4b2", 2, "parity"));
    // the trigger shape itself
    assert_eq!(label("R U2 R").2, "no parity");
    // "L' B2 R' U2 R' U2 F2 R2 B2 ... do a F2. Then you can do L or L' ... Let's do L ... In this case we have parity
    // ... just do qt that you did for reduction in the other direction": after F2, L' is the way, so before it the
    // direction is the other one (every half turn flips it), clockwise
    let setup = "L' B2 R' U2 R' U2 F2 R2 B2";
    assert_eq!(label(setup).0, "2c3");
    assert_eq!(label(&format!("{setup} F2 L")), ("4b2", 2, "parity"));
    assert_eq!(label(&format!("{setup} F2 L'")), ("4b2", 2, "no parity"));
    assert_eq!(label(&format!("{setup} F2")).2, "anticlockwise");
    assert_eq!(label(setup).2, "clockwise");
}

/// NISS: moves in brackets are on the inverse side, so they count before the scramble, undone.
#[test]
fn niss_moves_count_on_the_inverse() {
    let ix = index();
    let g = ix.info(400).generator;
    // R + g with R on the inverse is g; the other axes: F + g with (F) as well, written with a comment
    assert_eq!(ix.find(&format!("R {g}"), "(R)", DEFAULT_ABOVE).unwrap().number, 401);
    assert_eq!(ix.find(&format!("F {g}"), "(F) // EO\n", DEFAULT_ABOVE).unwrap().number, 401);
    assert!(ix.find(&format!("R {g}"), "R", DEFAULT_ABOVE).is_err(), "not a DR without NISS");
    assert!(ix.find(&format!("R {g}"), "(R", DEFAULT_ABOVE).is_err(), "an open bracket");

    // the page's one field: the scramble on the first line and the moves after it, labels and comments left out; or
    // a setup, on one line or several
    let attempt = |text: &str| ix.find_attempt(text, DEFAULT_ABOVE).map(|f| f.number);
    assert_eq!(attempt(&format!("Scramble: F {g}\n\nEO: (F) // the inverse\n")), Ok(401));
    assert_eq!(attempt(&format!("R {g}\n(R)")), Ok(401));
    assert_eq!(attempt(&g), Ok(401));
    let (first, rest) = g.split_at(g.find(' ').unwrap());
    assert_eq!(attempt(&format!("{first}\n{rest}")), Ok(401), "a setup on two lines");
    assert!(attempt("  // nothing\n").is_err());
}

/// 2c4 and 4a3, good or bad: every case has its label but the 4a3s with their corners on diagonals, and the two
/// versions of a case (the E slice turned) have the same.
#[test]
fn good_and_bad_2c4_and_4a3() {
    let ix = index();
    let mut labels = std::collections::BTreeMap::new();
    for i in 0..ix.cases.len() {
        let c = ix.info(i);
        if c.subset != "2c4" && c.subset != "4a3" {
            continue;
        }
        *labels.entry((c.subset, c.label)).or_insert(0) += 1;
        assert_eq!(c.turned.label, c.label, "case {}: the same with the E slice turned", c.number);
        let corners = ix.cosets.corner_mask[ix.cases[i].coset];
        let diagonals = [0b0101, 0b1010].contains(&(corners & 0x0F));
        assert_eq!(c.label.is_none(), c.subset == "4a3" && diagonals, "case {}", c.number);
    }
    let expected =
        [(("2c4", Some("bad")), 160), (("2c4", Some("good")), 96), (("4a3", None), 15), (("4a3", Some("bad")), 50)];
    assert_eq!(labels, expected.into_iter().chain([(("4a3", Some("good")), 50)]).collect());
}

/// How long the page lists HTRs: `above` moves over the optimal (at most 4), never past 12 moves unless the optimal
/// is; case 1 (HTR up to the E slice) lists only the E slice.
#[test]
fn the_slider_over_the_optimal() {
    let ix = index();
    let (two, nine, thirteen) = (ix.cases[1].coset, ix.cases[300].coset, ix.cases[922].coset);
    assert_eq!(ix.cosets.dist[two], 5);
    assert_eq!((ix.longest(two, 0), ix.longest(two, 2), ix.longest(two, MOST_ABOVE), ix.longest(two, 9)), (5, 7, 9, 9));
    assert_eq!(ix.cosets.dist[nine], 9);
    assert_eq!((ix.longest(nine, 2), ix.longest(nine, 4)), (11, LONGEST));
    assert_eq!(ix.cosets.dist[thirteen], 13);
    assert_eq!(ix.longest(thirteen, 4), 13);
    let found = ix.find(&ix.info(0).generator, "", MOST_ABOVE).unwrap();
    assert_eq!((found.longest, found.solutions.as_slice()), (2, ["U D".to_string()].as_slice()));
    let five: Vec<usize> = ix.solutions(two, ix.longest(two, 0)).iter().map(|s| s.len()).collect();
    assert!(!five.is_empty() && five.iter().all(|&n| n == 5));
}

/// What the page says about the E slice: the shortest HTRs of the turned case are those of the case with the last
/// quarter turn moved to the other layer (U for D, D for U), so up to the E slice the two lists have the same shortest
/// HTRs.  Counted here and printed (`cargo test -- --nocapture`): how often the whole lists agree.
#[test]
fn turning_the_e_slice_moves_the_last_quarter_turn() {
    let ix = index();
    let words = |t: &String| t.split(' ').map(String::from).collect::<Vec<_>>();
    let moved = |mut w: Vec<String>| {
        let last = w.last_mut().unwrap();
        *last = if last == "U" { "D".into() } else { "U".into() };
        w
    };
    let ud_ending =
        |w: &Vec<String>| w.len() >= 2 && (w[w.len() - 2].starts_with('U') || w[w.len() - 2].starts_with('D'));
    let (mut listed, mut carried, mut cases_exact, mut same_up_to_e) = (0, 0, 0, 0);
    let forms =
        |x: usize| -> HashSet<Vec<(u8, u8)>> { ix.solutions(x, LIST_LEN).iter().map(|s| modulo_e(s)).collect() };
    for i in 1..ix.cases.len() {
        let a: Vec<Vec<String>> = all_texts(ix, ix.coset(i, false)).iter().map(words).collect();
        let b: HashSet<Vec<String>> = all_texts(ix, ix.coset(i, true)).iter().map(words).collect();
        let shortest = a.iter().map(|w| w.len()).min().unwrap();
        let mut exact = a.len() == b.len();
        for w in &a {
            let ok = !ud_ending(w) && b.contains(&moved(w.clone()));
            if w.len() == shortest {
                assert!(ok, "case {}: shortest {} does not carry over", i + 1, w.join(" "));
            }
            listed += 1;
            carried += ok as usize;
            exact &= ok;
        }
        cases_exact += exact as usize;
        same_up_to_e += (forms(ix.coset(i, false)) == forms(ix.coset(i, true))) as usize;
    }
    println!(
        "E slice: {carried} of {listed} HTRs carry over; every one on {cases_exact} of {} cases; the listed HTRs are the same up to the E slice on {same_up_to_e}",
        ix.cases.len() - 1
    );
}

/// The listed HTRs: one per set that is the same up to the E slice.  The four 5-movers of case 310 are one; and HTRs
/// with the same form end with the same corners and U/D-layer edges up to U D' (a quarter turn of U and D together),
/// which is what the E slice and a rotation of the cube do to them.
#[test]
fn one_htr_per_set_the_same_up_to_the_e_slice() {
    let ix = index();
    let five: Vec<String> = all_texts(ix, ix.coset(309, false)).into_iter().filter(|t| moves(t).len() == 5).collect();
    assert_eq!(five, ["U R2 U R2 U", "U R2 D B2 D", "D B2 U B2 D", "D B2 D L2 U"]);
    let kept: Vec<String> =
        ix.solution_texts(ix.coset(309, false), LIST_LEN).into_iter().filter(|t| moves(t).len() == 5).collect();
    assert_eq!(kept, ["U R2 U R2 U"]);

    let ud = St::ID.apply_move(0).apply_move(5);
    let state = |p: &[u8]| p.iter().fold(St::ID, |s, &m| s.apply_move(m as usize));
    let (mut sets, mut dropped) = (0, 0);
    for i in 0..ix.cases.len() {
        for turned in [false, true] {
            let x = ix.coset(i, turned);
            let all = ix.all_solutions(x, LIST_LEN);
            let kept = ix.solutions(x, LIST_LEN);
            let forms: HashSet<Vec<(u8, u8)>> = kept.iter().map(|s| modulo_e(s)).collect();
            assert_eq!(forms.len(), kept.len(), "one per set");
            let mut first: std::collections::HashMap<Vec<(u8, u8)>, St> = std::collections::HashMap::new();
            for s in &all {
                let f = modulo_e(s);
                assert!(forms.contains(&f), "every HTR's set is listed");
                let st = state(s);
                let mut r = *first.entry(f).or_insert(st);
                let same = (0..4).any(|_| {
                    let hit = r.c == st.c && r.e == st.e;
                    r = r.then(ud);
                    hit
                });
                assert!(same, "case {}: {s:?} does not end like its set's first, up to U D'", i + 1);
            }
            sets += kept.len();
            dropped += all.len() - kept.len();
        }
    }
    println!("up to the E slice: {sets} HTRs listed, {dropped} left out as the same as one of them");
}

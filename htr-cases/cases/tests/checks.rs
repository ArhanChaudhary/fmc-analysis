//! Checks of the case index against the whole-cube model of `attempt_sim::cube` (built from the geometry of the
//! turns, independent of the coset tables) and against the examples in the *Hitchhiker's Guide to HTR*.

use attempt_sim::cube::{format_moves, parse_moves, Cube, Move, MoveTables};
use attempt_sim::dr::{St, AS_CUBE_MOVE, MOVE_FACE};
use htr_cases::cosets::modulo_e;
use htr_cases::{allmoves, dr_text, Index, DEFAULT_ABOVE, LONGEST, MOST_ABOVE};

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
    let ix = index();
    let mut seq = if turned { moves("U D'") } else { Vec::new() };
    seq.extend(moves(&ix.generator_text(ix.coset(i, false))));
    cube().state(&seq)
}

/// The case a setup makes (its index in `cases`).
fn case_of_setup(setup: &str) -> usize {
    index().find(setup, "", 0).unwrap().number - 1
}

/// Does a sequence leave DR on the way (a quarter turn of R, L, F or B)?
fn breaks_dr(text: &str) -> bool {
    moves(text).iter().any(|m| m.axis() != 1 && !m.is_half_turn())
}

/// 1,272 classes (cosets up to the symmetries and the E slice) cover the 29,400 cosets, one listed case each.
#[test]
fn case_count() {
    let ix = index();
    assert_eq!(ix.classes.len(), 1272);
    assert_eq!(ix.classes.iter().map(|c| c.members.len()).sum::<usize>(), 29_400);
    assert_eq!(ix.cases.len(), 1272);
}

/// The list is exhaustive: every DR state is a listed case, rotated, mirrored or with the E slice turned, and "Find
/// your case" finds how, on the whole-cube model (a rotation and a mirror rename the turns that make the state; the E
/// slice is E).  Every coset, made from solved by DR moves (a breadth-first tree), is related so to the listed case of
/// its class, and is that case as it is (no step) exactly when it is the listed coset.  A lookalike of a listed case
/// (the same bad corners and edges in the same places, the same subset) that is not listed takes other HTRs (some
/// optimal HTR of the listed case does not solve it, on the cube) and is related to its case by at least one step.
#[test]
fn the_list_is_exhaustive() {
    let ix = index();
    let cs = &ix.cosets;
    // a path of DR moves from HTR to every coset
    let mut path: Vec<Option<(usize, u8)>> = vec![None; cs.dist.len()];
    let mut seen = vec![false; cs.dist.len()];
    seen[cs.solved] = true;
    let mut queue = std::collections::VecDeque::from([cs.solved]);
    while let Some(x) = queue.pop_front() {
        for m in 0..10u8 {
            let y = cs.mv[x][m as usize] as usize;
            if !seen[y] {
                seen[y] = true;
                path[y] = Some((x, m));
                queue.push_back(y);
            }
        }
    }
    let moves_to = |mut x: usize| {
        let mut out = Vec::new();
        while let Some((from, m)) = path[x] {
            out.push(Move(AS_CUBE_MOVE[m as usize]));
            x = from;
        }
        out.reverse();
        out
    };
    let listed: HashSet<usize> = ix.cases.iter().map(|c| c.coset).collect();
    let picture = |x: usize| (cs.corner_mask[x], cs.edge_mask[x], cs.subset[x]);
    let (mut kinds, mut lookalikes) = (std::collections::BTreeMap::new(), 0);
    let mut optimal: std::collections::HashMap<usize, Vec<String>> = std::collections::HashMap::new();
    for x in (0..cs.dist.len()).filter(|&x| x != cs.solved) {
        let seq = moves_to(x);
        let (i, relation) = ix.relation(&seq).unwrap_or_else(|| panic!("coset {x} is no listed case from any side"));
        assert_eq!(i, ix.case_of(x));
        assert_eq!(relation.identical(), listed.contains(&x), "coset {x}: {relation:?}");
        *kinds.entry((!relation.rotation.is_empty(), relation.mirror, relation.slice)).or_insert(0) += 1;
        let y = ix.cases[i].coset;
        if !listed.contains(&x) && picture(x) == picture(y) {
            let htrs = optimal.entry(i).or_insert_with(|| ix.solution_texts(y, ix.longest(y, 0)));
            let start = cube().state(&seq);
            assert!(
                htrs.iter().any(|t| !in_htr(&cube().apply(&start, &moves(t)))),
                "coset {x} takes case {}'s HTRs",
                i + 1
            );
            lookalikes += 1;
        }
    }
    println!("relations (rotation, mirror, E slice): {kinds:?}; unlisted lookalikes of a listed case: {lookalikes}");
}

/// "Find your case" says how a DR is the listed case: the anticlockwise 2c3 U R2 U R2 U is the clockwise
/// U' R2 U' R2 U' rotated y2 and mirrored; the guide's DR on R/L is its case rotated z'; a 4a4 4e is another with the
/// E slice turned (and rotated y2).
#[test]
fn find_says_how_a_dr_is_its_case() {
    let ix = index();
    let relation = |setup: &str| {
        let f = ix.find(setup, "", 0).unwrap();
        (f.number, f.relation)
    };
    let steps = |list: &[&str]| list.iter().map(|s| s.to_string()).collect::<Vec<_>>();
    let clockwise = relation("U' R2 U' R2 U'");
    assert_eq!(clockwise.1, steps(&[]));
    assert_eq!(relation("U R2 U R2 U"), (clockwise.0, steps(&["rotate y2", "mirror it (left and right swapped)"])));
    assert_eq!(relation("R U2 R' U2 L2 F2").1, steps(&["rotate z'"]));
    let drawn = relation("D' L' F' L B2 L' F L' U");
    assert_eq!(drawn.1, steps(&[]));
    assert_eq!(relation("U' R' B' R F2 R' B R' U"), (drawn.0, steps(&["rotate y2", "turn the E slice a quarter (E)"])));
}

/// With DR moves, every coset of a case is as far from HTR as the others, except HTR itself (case 1).  With every
/// face turn, the symmetric copies still are, but for 25 more cases the two versions (the E slice turned) are not: 23
/// a move apart, 2 two moves apart.
#[test]
fn every_member_of_a_case_is_as_far_from_htr() {
    let ix = index();
    let mut apart = std::collections::BTreeMap::new();
    for (i, c) in ix.classes.iter().enumerate() {
        let lengths: HashSet<u8> = c.members.iter().map(|&x| ix.cosets.dist[x]).collect();
        if i == 0 {
            assert_eq!(lengths, HashSet::from([0, 2]), "HTR and HTR with the E slice turned");
        } else {
            assert_eq!(lengths.len(), 1, "case {}", i + 1);
        }
        let (x, t) = (c.coset, ix.cosets.eslice[c.coset] as usize);
        for &y in &c.members {
            let twin_side = !(0..attempt_sim::dr::NSYM).any(|s| ix.cosets.sym[x][s] as usize == y);
            assert_eq!(ix.dist[y], ix.dist[if twin_side { t } else { x }], "case {}: symmetric copies", i + 1);
        }
        if i > 0 && ix.dist[x] != ix.dist[t] {
            *apart.entry(ix.dist[x].abs_diff(ix.dist[t])).or_insert(0) += 1;
        }
    }
    assert_eq!(apart, [(1, 23), (2, 2)].into());
    // and with every face turn, never further than with DR moves; shorter for 155 cases
    assert!((0..ix.dist.len()).all(|x| ix.dist[x] <= ix.cosets.dist[x]));
    let shorter = ix.classes.iter().filter(|c| ix.dist[c.coset] < ix.cosets.dist[c.coset]).count();
    assert_eq!(shorter, 155);
}

/// The distances shipped in `all_dist.bin` are the ones the search finds now.
#[test]
fn the_distance_table_is_right() {
    let ix = index();
    assert_eq!(ix.fresh_distances(), ix.dist);
}

/// The example asked about: the case of U' L2 U' F2 U L2 U' L2 is 8 moves from HTR with DR moves, 7 with
/// F U B' U2 F U' B, which leaves DR on the way.
#[test]
fn a_dr_breaking_htr_is_shorter() {
    let ix = index();
    let i = case_of_setup("U' L2 U' F2 U L2 U' L2");
    let x = ix.coset(i, false);
    assert_eq!((ix.cosets.dist[x], ix.dist[x]), (8, 7));
    let start = cube().state(&moves("U' L2 U' F2 U L2 U' L2"));
    let found = ix.find("U' L2 U' F2 U L2 U' L2", "", 0).unwrap();
    assert!(found.solutions.iter().any(|t| t == "F U B' U2 F U' B"), "{:?}", found.solutions);
    assert!(in_htr(&cube().apply(&start, &moves("F U B' U2 F U' B"))));
}

#[test]
fn generators_make_their_cases() {
    let ix = index();
    for i in 0..ix.cases.len() {
        let info = ix.info(i);
        let generator = ix.generator_text(ix.coset(i, false));
        assert_eq!(moves(&generator).len(), info.moves as usize, "case {}", i + 1);
        let found = ix.find(&generator, "", 0).unwrap();
        assert_eq!((found.number, found.axis, found.moves), (i + 1, "U/D", info.moves));
        assert_eq!(found.bad, (info.bad_corners.len() as u32, info.bad_edges.len() as u32));
        let x = ix.coset(i, false);
        assert_eq!(found.solutions, ix.solution_texts(x, ix.longest(x, 0)));
        let turned_generator = ix.generator_text(ix.coset(i, true));
        if i == 0 {
            assert_eq!(ix.find(&turned_generator, "", 0).unwrap_err(), "that is already HTR");
            continue;
        }
        assert!(found.relation.is_empty(), "case {} is itself: {:?}", i + 1, found.relation);
        let turned = ix.find(&turned_generator, "", 0).unwrap();
        assert_eq!((turned.number, turned.moves), (i + 1, info.turned.moves), "the E slice turned is the same case");
        let x = ix.coset(i, true);
        assert_eq!(turned.solutions, ix.solution_texts(x, ix.longest(x, 0)));
    }
}

/// A listed HTR: at most `max_len` moves, reaches HTR at its end and not before (nor HTR up to the E slice), and its
/// last block (the last turn, or the last two on one axis) is quarter turns, all clockwise.
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
    let n = seq.len();
    let block = if n >= 2 && seq[n - 2].axis() == seq[n - 1].axis() { 2 } else { 1 };
    assert!(seq[n - block..].iter().all(|m| m.quarter_turns() == 1), "{text} ends in a half turn or anticlockwise");
}

#[test]
fn every_listed_htr_reaches_htr() {
    let ix = index();
    let (mut total, mut breaking) = (0, 0);
    for i in 0..ix.cases.len() {
        for turned in [false, true] {
            let s = start(i, turned);
            let x = ix.coset(i, turned);
            let list = all_texts(ix, x);
            let distinct: HashSet<&String> = list.iter().collect();
            assert_eq!(distinct.len(), list.len());
            let longest = LIST_LEN.max(ix.dist[x] as usize);
            for text in &list {
                check_listed(&s, text, longest);
            }
            breaking += list.iter().filter(|t| breaks_dr(t)).count();
            if !(i == 0 && turned) {
                let shortest = list.iter().map(|t| moves(t).len()).min().unwrap();
                assert_eq!(shortest, ix.dist[x] as usize, "case {} turned {turned}", i + 1);
                if ix.dist[x] as usize > LIST_LEN {
                    assert!(list.iter().all(|t| moves(t).len() == shortest), "only the shortest past {LIST_LEN}");
                }
            }
            total += list.len();
        }
    }
    println!("listed HTRs checked, both versions: {total}, of them leaving DR on the way {breaking}");
    assert!(total > 100_000 && breaking > 10_000);
}

/// Every HTR of up to `max_len` face turns, by trying every sequence on the whole cube, in the listed form.
fn brute_force_all(start: &Cube, max_len: usize) -> HashSet<String> {
    fn go(c: &Cube, path: &mut Vec<Move>, max_len: usize, out: &mut HashSet<String>) {
        let oriented = c.co == [0; 8] && c.eo == [0; 12];
        if !path.is_empty() && oriented && in_htr_up_to_e(c) {
            if in_htr(c) {
                let n = path.len();
                let block = if n >= 2 && path[n - 2].axis() == path[n - 1].axis() { 2 } else { 1 };
                if path[n - block..].iter().all(|m| m.quarter_turns() == 1) {
                    out.insert(format_moves(path));
                }
            }
            return;
        }
        if path.len() == max_len {
            return;
        }
        for m in Move::all() {
            if attempt_sim::cube::canonical_after(path.last().copied(), m) {
                path.push(m);
                go(&cube().turn(c, m), path, max_len, out);
                path.pop();
            }
        }
    }
    let mut out = HashSet::new();
    go(start, &mut Vec::new(), max_len, &mut out);
    out
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
    ix.all_solutions(coset, LIST_LEN).iter().map(|p| format_moves(p)).collect()
}

/// The same with DR moves only.
fn dr_texts(ix: &Index, coset: usize) -> Vec<String> {
    ix.dr_solutions(coset, LIST_LEN).iter().map(|p| dr_text(p)).collect()
}

#[test]
fn lists_are_complete() {
    let ix = index();
    // every face turn: a spread of cases up to 6 moves, and two to 7 (one of them with a DR-breaking 7-mover)
    let breaking = case_of_setup("U' L2 U' F2 U L2 U' L2");
    let sample: Vec<(usize, usize)> =
        (53..ix.cases.len()).step_by(53).map(|i| (i, 6)).chain([(1, 7), (breaking, 7)]).collect();
    for (i, max_len) in sample {
        let listed: HashSet<String> =
            all_texts(ix, ix.coset(i, false)).into_iter().filter(|t| moves(t).len() <= max_len).collect();
        assert_eq!(brute_force_all(&start(i, false), max_len), listed, "case {}", i + 1);
    }
    // DR moves only: the spread to 7, three to the full 8; case 1 (HTR up to the E slice) lists its 2-movers only
    let sample: Vec<(usize, usize)> =
        (53..ix.cases.len()).step_by(53).map(|i| (i, 7)).chain([(0, 2), (1, 8), (300, 8), (900, 8)]).collect();
    for (i, max_len) in sample {
        let listed: HashSet<String> =
            dr_texts(ix, ix.coset(i, false)).into_iter().filter(|t| moves(t).len() <= max_len).collect();
        assert_eq!(brute_force(&start(i, false), max_len), listed, "case {}", i + 1);
    }
}

/// Pairs a U2 apart: 185, never more than two cases together, and the two always have the same subset, edges and
/// optimal (they are one case after their first quarter turn).
#[test]
fn pairs_a_u2_apart() {
    let ix = index();
    let infos: Vec<_> = (0..ix.cases.len()).map(|i| ix.info(i)).collect();
    let mut sizes = std::collections::BTreeMap::new();
    for c in &infos {
        *sizes.entry(c.u2_group.len() + 1).or_insert(0) += 1;
        assert!(c.u2_mates.iter().all(|m| c.u2_group.contains(m) && infos[m - 1].u2_mates.contains(&c.number)));
        for &m in &c.u2_group {
            let o = &infos[m - 1];
            assert_eq!((o.subset, o.edges, o.moves), (c.subset, c.edges, c.moves), "#{} and #{m}", c.number);
        }
    }
    assert_eq!(sizes, [(1, 1272 - 2 * 185), (2, 2 * 185)].into());
    // the first pair found: U' R2 U' R2 U' and U' F2 U F2 U'
    let (a, b) = (case_of_setup("U' R2 U' R2 U'"), case_of_setup("U' F2 U F2 U'"));
    assert!(infos[a].u2_mates.contains(&(b + 1)), "#{} {:?}", a + 1, infos[a].u2_mates);
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
        (f.subset, f.edges, f.labels.join(" "))
    };
    // "R U2 R' U2 L2 F2: This is 4b2 with 2 bad edges ... if you do the trigger, you will end up with fake HTR"
    assert_eq!(label("R U2 R' U2 L2 F2"), ("4b2", 2, "parity".to_string()));
    // "... B2 U2 L2 B2 R2 U2 ... you can do B2 L B2 L' or F2 R B2 R' to see that this 4b2 has parity"
    assert_eq!(label("R U2 R' U2 L2 F2 B2 U2 L2 B2 R2 U2"), ("4b2", 2, "parity".to_string()));
    // the trigger shape itself
    assert_eq!(label("R U2 R").2, "no parity");
    // "L' B2 R' U2 R' U2 F2 R2 B2 ... do a F2. Then you can do L or L' ... Let's do L ... In this case we have parity
    // ... just do qt that you did for reduction in the other direction": after F2, L' is the way, so before it the
    // direction is the other one (every half turn flips it), clockwise
    let setup = "L' B2 R' U2 R' U2 F2 R2 B2";
    assert_eq!(label(setup).0, "2c3");
    assert_eq!(label(&format!("{setup} F2 L")), ("4b2", 2, "parity".to_string()));
    assert_eq!(label(&format!("{setup} F2 L'")), ("4b2", 2, "no parity".to_string()));
    assert_eq!(label(&format!("{setup} F2")).2, "anticlockwise");
    assert_eq!(label(setup).2, "clockwise");
}

/// NISS: moves in brackets are on the inverse side, so they count before the scramble, undone.
#[test]
fn niss_moves_count_on_the_inverse() {
    let ix = index();
    let g = ix.generator_text(ix.coset(400, false));
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

/// The labels of 0c3, 2c4 and 4a3: one type for a 0c3, a swap type and good, mid or bad for a 2c4, good or bad for a
/// 4a3 (none for one with its corners on diagonals); the same on both versions of a case (the E slice turned).  U and
/// Swap-U are the same from every side; R and F are read on the case as drawn (a y rotation swaps them, and turns the
/// bad edges with them: every R or F case has both among its copies, with the same good, mid or bad).
#[test]
fn labels_of_0c3_2c4_and_4a3() {
    let ix = index();
    let mut labels = std::collections::BTreeMap::new();
    for i in 0..ix.cases.len() {
        let c = ix.info(i);
        if !["0c3", "2c4", "4a3"].contains(&c.subset) {
            continue;
        }
        assert_eq!(c.turned.labels, c.labels, "case {}: the same with the E slice turned", c.number);
        *labels.entry((c.subset, c.labels.join(" "))).or_insert(0) += 1;
        let corners = ix.cosets.corner_mask[ix.cases[i].coset];
        let diagonals = [0b0101, 0b1010].contains(&(corners & 0x0F));
        assert_eq!(c.labels.is_empty(), c.subset == "4a3" && diagonals, "case {}", c.number);

        let sides: HashSet<Vec<&str>> =
            (0..attempt_sim::dr::NSYM).map(|s| ix.labels.of(ix.cosets.sym[ix.cases[i].coset][s] as usize)).collect();
        let letter = c.labels.first().map(|l| l.trim_start_matches("Swap-")).unwrap_or("");
        let expected = match letter {
            "R" | "F" => 2,
            _ => 1,
        };
        assert_eq!(sides.len(), expected, "case {}: {sides:?}", c.number);
    }
    let expected = [
        ("0c3", "F", 3),
        ("0c3", "R", 13),
        ("0c3", "U", 13),
        ("2c4", "Swap-F bad", 27),
        ("2c4", "Swap-F good", 31),
        ("2c4", "Swap-F mid", 11),
        ("2c4", "Swap-R bad", 49),
        ("2c4", "Swap-R good", 11),
        ("2c4", "Swap-R mid", 31),
        ("2c4", "Swap-U bad", 42),
        ("2c4", "Swap-U good", 54),
        ("4a3", "", 15),
        ("4a3", "bad", 50),
        ("4a3", "good", 50),
    ];
    assert_eq!(labels, expected.iter().map(|&(s, l, n)| ((s, l.to_string()), n)).collect());

    // in a solver's own frame: the case of R U2 R2 F2 R F2 R2 U2 R (DR on R/L) is a 0c3; the same moves rotated onto U/D
    // (R to U, U to F, F to R: a rotation about the UFR corner), its type letter rotates with it
    let on_rl = ix.find("R U2 R2 F2 R F2 R2 U2 R", "", 0).unwrap();
    let on_ud = ix.find("U F2 U2 R2 U R2 U2 F2 U", "", 0).unwrap();
    assert_eq!((on_rl.subset, on_ud.subset, on_rl.number), ("0c3", "0c3", on_ud.number));
    let turn = |l: &str| match l {
        "R" => "U".to_string(),
        "U" => "F".to_string(),
        "F" => "R".to_string(),
        other => other.to_string(),
    };
    assert_eq!(on_rl.labels.iter().map(|l| turn(l)).collect::<Vec<_>>(), on_ud.labels);
}

/// How long the page lists HTRs: `above` moves over the optimal (at most 4), never past the longest listed unless the
/// optimal is; case 1 (HTR up to the E slice) lists only the E slice.
#[test]
fn the_slider_over_the_optimal() {
    let ix = index();
    let optimal = |d: u8| ix.cases.iter().map(|c| c.coset).find(|&x| ix.dist[x] == d).unwrap();
    let (five, nine, eleven) = (optimal(5), optimal(9), optimal(11));
    assert_eq!(
        (ix.longest(five, 0), ix.longest(five, 2), ix.longest(five, MOST_ABOVE), ix.longest(five, 9)),
        (5, 7, 9, 9)
    );
    assert_eq!((ix.longest(nine, 1), ix.longest(nine, 4)), (10, (9 + 4).clamp(9, LONGEST)));
    assert_eq!(ix.longest(eleven, 4), (11 + 4).clamp(11, LONGEST));
    let found = ix.find("U' D'", "", MOST_ABOVE).unwrap();
    assert_eq!((found.number, found.longest, found.solutions.as_slice()), (1, 2, ["U D".to_string()].as_slice()));
    let shortest: Vec<usize> = ix.solutions(five, ix.longest(five, 0)).iter().map(|s| s.len()).collect();
    assert!(!shortest.is_empty() && shortest.iter().all(|&n| n == 5));
}

/// What the page says about the E slice, with DR moves: the shortest HTRs of the turned case are those of the case with
/// the last quarter turn moved to the other layer (U for D, D for U), so up to the E slice the two lists have the same
/// shortest HTRs.  Counted here and printed (`cargo test -- --nocapture`): how often the whole lists agree.  (With
/// DR-breaking HTRs it fails for 25 cases: see `every_member_of_a_case_is_as_far_from_htr`.)
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
        |x: usize| -> HashSet<Vec<(u8, u8)>> { ix.dr_solutions(x, LIST_LEN).iter().map(|s| modulo_e(s)).collect() };
    for i in 1..ix.cases.len() {
        let a: Vec<Vec<String>> = dr_texts(ix, ix.coset(i, false)).iter().map(words).collect();
        let b: HashSet<Vec<String>> = dr_texts(ix, ix.coset(i, true)).iter().map(words).collect();
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

/// The listed HTRs: one per set that is the same up to the E slice.  The four 5-movers of U' R2 U' R2 U' are one;
/// with DR moves, HTRs with the same form end with the same corners and U/D-layer edges up to U D' (a quarter turn of U
/// and D together), which is what the E slice and a rotation of the cube do to them; and the form of every face turn
/// (`allmoves::modulo_e`) is the DR-move one (`cosets::modulo_e`) on DR moves.
#[test]
fn one_htr_per_set_the_same_up_to_the_e_slice() {
    let ix = index();
    let x = ix.coset(case_of_setup("U' R2 U' R2 U'"), false);
    let five: Vec<String> = all_texts(ix, x).into_iter().filter(|t| moves(t).len() == 5).collect();
    assert_eq!(five, ["U R2 U R2 U", "U R2 D B2 D", "D B2 U B2 D", "D B2 D L2 U"]);
    let kept: Vec<String> = ix.solution_texts(x, LIST_LEN).into_iter().filter(|t| moves(t).len() == 5).collect();
    assert_eq!(kept, ["U R2 U R2 U"]);

    let ud = St::ID.apply_move(0).apply_move(5);
    let state = |p: &[u8]| p.iter().fold(St::ID, |s, &m| s.apply_move(m as usize));
    let as_moves = |p: &[u8]| p.iter().map(|&m| Move(AS_CUBE_MOVE[m as usize])).collect::<Vec<_>>();
    let (mut sets, mut dropped) = (0, 0);
    for i in 0..ix.cases.len() {
        for turned in [false, true] {
            let x = ix.coset(i, turned);
            // (the DR-move ones as long as the page's list goes: a DR-breaking optimal can be shorter)
            let reach = LIST_LEN.max(ix.dist[x] as usize);
            let all: Vec<Vec<u8>> = ix.dr_solutions(x, LIST_LEN).into_iter().filter(|s| s.len() <= reach).collect();
            let mut forms: HashSet<Vec<(u8, u8)>> = HashSet::new();
            let mut first: std::collections::HashMap<Vec<(u8, u8)>, St> = std::collections::HashMap::new();
            for s in &all {
                let f = modulo_e(s);
                assert_eq!(allmoves::modulo_e(&as_moves(s)), f, "the two forms agree on DR moves");
                forms.insert(f.clone());
                let st = state(s);
                let mut r = *first.entry(f).or_insert(st);
                let same = (0..4).any(|_| {
                    let hit = r.c == st.c && r.e == st.e;
                    r = r.then(ud);
                    hit
                });
                assert!(same, "case {}: {s:?} does not end like its set's first, up to U D'", i + 1);
            }
            // the page's list: one per form, every face turn
            let kept = ix.solutions(x, LIST_LEN);
            let kept_forms: HashSet<Vec<(u8, u8)>> = kept.iter().map(|s| allmoves::modulo_e(s)).collect();
            assert_eq!(kept_forms.len(), kept.len(), "one per set");
            assert!(forms.is_subset(&kept_forms), "case {}: every DR-move set is listed", i + 1);
            sets += kept.len();
            dropped += ix.all_solutions(x, LIST_LEN).len() - kept.len();
        }
    }
    println!("up to the E slice: {sets} HTRs listed, {dropped} left out as the same as one of them");
}

//! Whole attempts against the research program's own output (`research/attemptsim`, with the 1.3 GB exact table).
//! The port was compared with it on 73,034 attempts; these few keep the comparison alive in `cargo test`.

use attempt_sim::cube::{format_moves, parse_moves, Cube};
use attempt_sim::{simulate, Plan, Settings, StepKind, Tables};
use std::sync::OnceLock;

fn tables() -> &'static Tables {
    static T: OnceLock<Tables> = OnceLock::new();
    T.get_or_init(|| {
        let mut t = Tables::new();
        t.build_prune();
        assert_eq!(t.noe().checksum(), attempt_sim::prune::NOE_CHECKSUM);
        t
    })
}

/// (scramble number in research/data/scrambles_uniform.txt, scramble, plan, length, end of the attempt in ms, solution)
const GOLDEN: [(u64, &str, &str, usize, u64, &str); 3] = [
    (0, "U2 R2 D L2 R2 D' R2 U' L2 D R2 U F2 R' D' F2 L' D R D' B' R2 D'", "tuned", 21, 3342455,
        "L2 U' L D2 R' F2 D U2 F2 L R2 B2 L F2 B2 L2 F2 U2 B' U L'"),
    (0, "U2 R2 D L2 R2 D' R2 U' L2 D R2 U F2 R' D' F2 L' D R D' B' R2 D'", "baseline", 22, 3439254,
        "R' D B L' R U' R F2 D' F2 B2 D2 R2 F2 L' D2 R2 B2 L' F2 U2 L"),
    (7, "B2 U2 L2 R2 D B2 D F2 U2 L2 U' R2 U' R2 U' B' D2 R' B2 F' R2 U F2 L R'", "tuned", 22, 3367000,
        "R U B2 U R2 U2 F2 L2 U' R2 D' B2 D' B2 F' U' B' U' L F B2 D"),
];

#[test]
fn attempts_match_the_research_program() {
    for (number, scramble, plan, len, t_end, solution) in GOLDEN {
        let settings = Settings {
            plan: if plan == "tuned" { Plan::tuned() } else { Plan::baseline() },
            attempt: number,
            ..Settings::default()
        };
        let r = simulate(tables(), &parse_moves(scramble).unwrap(), &settings);
        assert_eq!((r.outcome.len, r.outcome.t_end, format_moves(&r.outcome.moves).as_str()), (len, t_end, solution), "scramble {number}, {plan}");
    }
}

#[test]
fn the_record_adds_up() {
    let scramble = parse_moves(GOLDEN[2].1).unwrap();
    let r = simulate(tables(), &scramble, &Settings { attempt: 7, ..Settings::default() });
    // the steps follow each other on the clock and add up to the totals per kind
    let mut clock = 0;
    let mut time = [0u64; 11];
    for s in &r.steps {
        assert_eq!(s.start, clock);
        clock += s.ms;
        time[s.kind as usize] += s.ms;
    }
    assert_eq!(clock, r.outcome.t_end);
    assert_eq!(time, r.outcome.time);
    assert_eq!(r.steps.iter().filter(|s| s.kind == StepKind::Write).count(), r.outcome.writes.len());
    // every solution found solves the scramble, and the result is one of them, written down in time
    let t = tables();
    for sol in &r.solutions {
        let moves = parse_moves(&sol.moves).unwrap();
        assert_eq!(moves.len(), sol.len);
        assert_eq!(t.moves.apply(&t.moves.state(&scramble), &moves), Cube::SOLVED);
    }
    let result = r.solutions.iter().filter(|s| s.written_at.is_some()).last().unwrap();
    assert_eq!(result.moves, format_moves(&r.outcome.moves));
    assert!(result.written_at.unwrap() <= r.outcome.budget_ms);
}

#[test]
fn settings_travel_as_json() {
    let s = Settings::default();
    let text = serde_json::to_string(&s).unwrap();
    let back: Settings = serde_json::from_str(&text).unwrap();
    assert_eq!((back.costs, back.human, back.plan), (s.costs, s.human, s.plan));
    // an unknown key is an error, not a silent default
    assert!(serde_json::from_str::<Settings>(r#"{"costs": {"rzpp": 3}}"#).is_err());
}

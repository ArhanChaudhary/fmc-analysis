//! Build the finish table and time each call: `cargo run --release --example build_table --features profile`.
fn main() {
    let t = attempt_sim::Tables::new();
    let mut b = t.prune_builder();
    let start = std::time::Instant::now();
    let mut last = std::time::Instant::now();
    loop {
        let done = b.step(&t.dr, usize::MAX);
        eprintln!("  {:.2} s, progress {:.3}", last.elapsed().as_secs_f64(), b.progress());
        last = std::time::Instant::now();
        if done {
            break;
        }
    }
    let noe = b.finish();
    eprintln!("total {:.2} s, checksum {:#018x}", start.elapsed().as_secs_f64(), noe.checksum());
}

#!/bin/bash
# Build the page's data: the WebAssembly module and its JavaScript glue (web/pkg/), and the text file of generators
# (web/htr-cases.txt).  Needs cargo with the wasm32-unknown-unknown target and wasm-bindgen-cli 0.2.130 (the version of
# the crate in wasm/Cargo.toml): rustup target add wasm32-unknown-unknown; cargo install wasm-bindgen-cli --version 0.2.130
set -euo pipefail
cd "$(dirname "$0")"
cargo build -p htr-cases-wasm --release --target wasm32-unknown-unknown
wasm-bindgen --target web --no-typescript --out-dir web/pkg target/wasm32-unknown-unknown/release/htr_cases_wasm.wasm
cargo run -q --release -p htr-cases-cli -- text web/htr-cases.txt
ls -l web/pkg web/htr-cases.txt

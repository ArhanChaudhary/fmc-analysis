#!/bin/bash
# Build the simulator for the web page: the WebAssembly module and its JavaScript glue, into web/pkg/.
# Needs cargo with the wasm32-unknown-unknown target and wasm-bindgen-cli 0.2.130 (the version of the crate in
# wasm/Cargo.toml): rustup target add wasm32-unknown-unknown; cargo install wasm-bindgen-cli --version 0.2.130
set -euo pipefail
cd "$(dirname "$0")"
cargo build -p attempt-sim-wasm --release --target wasm32-unknown-unknown
wasm-bindgen --target web --no-typescript --out-dir web/pkg target/wasm32-unknown-unknown/release/attempt_sim_wasm.wasm
ls -l web/pkg

//! The HTR case index for a web page (wasm-bindgen).  Everything comes out as JSON text.
//!
//! ```js
//! const index = new Index();                       // every table and the case list, a fraction of a second
//! const cases = JSON.parse(index.cases());         // [{number, subset, edges, moves, label, bad_corners, ...}]
//! const htrs = JSON.parse(index.solutions(17, false, 8));   // case 17's HTRs of 8 moves or less
//! const mine = JSON.parse(index.find("R' U' F ...\nU F2 (L' B) R' ...", 8));   // scramble, then moves to DR
//! ```

use htr_cases::Index as Cases;

/// The longest the page lists HTRs to (with at most 4 over a case's shortest, still up to 375,000 before the dedupe).
pub const LONGEST: usize = 12;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Index {
    inner: Cases,
}

#[wasm_bindgen]
impl Index {
    #[wasm_bindgen(constructor)]
    pub fn new() -> Index {
        Index { inner: Cases::new() }
    }

    /// Every case, in the order of the index: `[{number, subset, edges, moves, label, bad_corners, bad_edges,
    /// lookalikes, corner_test, generator, solutions, turned}]`.
    pub fn cases(&self) -> String {
        let all: Vec<_> = (0..self.inner.cases.len()).map(|i| self.inner.info(i)).collect();
        serde_json::to_string(&all).unwrap()
    }

    /// The HTRs of up to `max_len` moves (at most [`LONGEST`], and 4 over the shortest) of case `number` (1-based),
    /// or of the case with the E slice turned; the shortest ones if there are none that short.
    pub fn solutions(&self, number: usize, turned: bool, max_len: usize) -> Result<String, JsError> {
        if !(1..=self.inner.cases.len()).contains(&number) {
            return Err(JsError::new("no such case"));
        }
        let x = self.inner.coset(number - 1, turned);
        Ok(serde_json::to_string(&self.inner.solution_texts(x, max_len.min(LONGEST))).unwrap())
    }

    /// A solver's own DR from one text: the scramble, then the moves so far (NISS moves in brackets); or a setup.
    pub fn find(&self, text: &str, max_len: usize) -> Result<String, JsError> {
        let found = self.inner.find_attempt(text, max_len.min(LONGEST)).map_err(|e| JsError::new(&e))?;
        Ok(serde_json::to_string(&found).unwrap())
    }
}

impl Default for Index {
    fn default() -> Self {
        Self::new()
    }
}

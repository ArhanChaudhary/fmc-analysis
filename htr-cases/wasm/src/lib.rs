//! The HTR case index for a web page (wasm-bindgen).  Everything comes out as JSON text.
//!
//! ```js
//! const index = new Index();                       // every table and the case list, a fraction of a second
//! const cases = JSON.parse(index.cases());         // [{number, subset, edges, moves, label, bad_corners, ...}]
//! const htrs = JSON.parse(index.solutions(17, false));   // case 17's HTRs of 8 moves or less
//! const mine = JSON.parse(index.find("R' U' F ...", "U F2 (L' B) R' ..."));
//! ```

use htr_cases::Index as Cases;
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

    /// The HTRs of up to 8 moves of case `number` (1-based), or of the case with the E slice turned.
    pub fn solutions(&self, number: usize, turned: bool) -> Result<String, JsError> {
        if !(1..=self.inner.cases.len()).contains(&number) {
            return Err(JsError::new("no such case"));
        }
        Ok(serde_json::to_string(&self.inner.solution_texts(self.inner.coset(number - 1, turned))).unwrap())
    }

    /// A solver's own DR: the scramble and the moves so far (NISS moves in brackets).
    pub fn find(&self, scramble: &str, moves: &str) -> Result<String, JsError> {
        let found = self.inner.find(scramble, moves).map_err(|e| JsError::new(&e))?;
        Ok(serde_json::to_string(&found).unwrap())
    }
}

impl Default for Index {
    fn default() -> Self {
        Self::new()
    }
}

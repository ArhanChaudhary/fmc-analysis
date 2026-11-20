//! The HTR case index for a web page (wasm-bindgen).  Everything comes out as JSON text.
//!
//! ```js
//! const index = new Index();                       // every table and the case list, a fraction of a second
//! const cases = JSON.parse(index.cases());         // [{number, subset, edges, moves, label, bad_corners, ...}]
//! const htrs = JSON.parse(index.solutions(17, false, 2));   // case 17's HTRs up to 2 moves over its optimal
//! const mine = JSON.parse(index.find("R' U' F ...\nU F2 (L' B) R' ...", 2));   // scramble, then moves to DR
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
    /// lookalikes, u2_mates, corner_test, turned}]`.
    pub fn cases(&self) -> String {
        let all: Vec<_> = (0..self.inner.cases.len()).map(|i| self.inner.info(i)).collect();
        serde_json::to_string(&all).unwrap()
    }

    /// Build the search with every face turn now (it is built anyway the first time it is needed).
    pub fn prepare(&self) {
        self.inner.allmoves();
    }

    /// The HTRs of case `number` (1-based), or of the case with the E slice turned, up to `above` moves over its
    /// optimal (`Index::longest`): `{longest, htrs}`.
    pub fn solutions(&self, number: usize, turned: bool, above: usize) -> Result<String, JsError> {
        if !(1..=self.inner.cases.len()).contains(&number) {
            return Err(JsError::new("no such case"));
        }
        let x = self.inner.coset(number - 1, turned);
        let longest = self.inner.longest(x, above);
        Ok(serde_json::json!({ "longest": longest, "htrs": self.inner.solution_texts(x, longest) }).to_string())
    }

    /// A solver's own DR from one text: the scramble, then the moves so far (NISS moves in brackets); or a setup.
    /// Its HTRs go up to `above` moves over its optimal.
    pub fn find(&self, text: &str, above: usize) -> Result<String, JsError> {
        let found = self.inner.find_attempt(text, above).map_err(|e| JsError::new(&e))?;
        Ok(serde_json::to_string(&found).unwrap())
    }
}

impl Default for Index {
    fn default() -> Self {
        Self::new()
    }
}

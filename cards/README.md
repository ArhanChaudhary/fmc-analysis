# Decision cards

The page [decision-cards.html](https://fmc.arhan.sh/decision-cards.html): six in-attempt questions answered from the
studies' data. `decision-cards.md` is generated; edit `src/cards.md` and rerun `src/build.py`.

| File | What |
|---|---|
| `src/cards.md` | the page's text, with `{= study: expression =}` (a number evaluated in that study's own report environment, so the card prints what the study prints), `{= expression =}` (this page's numbers), `{{name}}` (tables made by `build.py`), `{{sec study N}}` (link to a study's section) and `[[T123]]` (dated Discord links) |
| `src/build.py` | fills the template, writes `decision-cards.md`; checks the variants card's rule (one route to +2 beats three routes at shortest HTRs, every subset) |
| `src/eo_stop.py` → `data/eo_stop.tsv` | "Should I stop looking for EOs": best DR through EOs of 4 or less vs what EOs of 5 and 6 add, from eo-to-dr's 50,000-scramble table (`eo-to-dr/research/out/big/scr50k.tsv`, not in git) |
| `src/switch44.py` → `data/switch44.tsv`, `data/switch44_rules.tsv` | "Should I switch this EO?", 4c4e: the current rule (2+ top pairs, or 1 top pair with ARM 21) split by half turns to two bars, with DR in 6 / 5 or less after the switch, JZP apart; from the EO-switch study's exact tables (`eo-switch/research/out/big`, not in git) |
| `src/niss_mid.py` → `data/niss_mid.tsv` | "Should I NISS in the middle of this route": after each quarter turn of each subset's first route, keep going on normal vs switch now, from htr-routes' per-state route files (`htr-routes/research/out/big/run1`, not in git) |

Other numbers come from the studies' committed results: `htr-routes/research/out/q2_checklist_budget.tsv`,
`q1_routes.tsv`, `eo-to-dr/research/out/c6_by_case.tsv`, `eo-switch/report/data/rule_cards.md`.

    source /data/fmc/env.sh
    python cards/src/eo_stop.py; python cards/src/niss_mid.py; python cards/src/build.py

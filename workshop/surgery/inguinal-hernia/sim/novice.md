# Sim: novice
path: S1.hook → S1.hook_t1 (TR1, Guessing) → S1.hook (Indirect, Guessing) → S1.explain_route → S1.retest_route (hint) → S1.retest_ok → S1.femoral_probe → … → S6.p12 → S6.recap → END  (215 steps; full path in `novice.json`)

## Friction
- S1.hook: cold-open exam stem uses "inferior epigastric vessels" before any teaching; "Go with your first instinct" invites a guess. A learner who read the topic once can only guess.
- S1.hook_t1 and other "Try again" retries: return to the same bare stem with no new information. The only real help is the hint or "Show me why".
- S1.tim_probe: four long options differ by one qualifier ("relatively"); the lesson on that word arrives only after the trap is taken.
- S5.emerg_t12, S5.nerve_t1, S5.adult_t1, S5.adult_t2: feedback ends with a question ("What would a scan change…?", "Which detail here is about the surgeon?") and there is no answer slot, so the question hangs.
- S2.conj_probe: option labels are long clauses; hard to scan.
- S3.contrast_t22: feedback states the invagination rule but does not say why the chosen tip option is wrong for a direct hernia.
- Length: 215 steps, 89 probes, 20 traps met. I kept going, but the middle of S4–S5 felt like a quiz, not teaching. Engagement 3.
- S6.recap: three-line recap, then END; a learner who fell into several traps gets no summary of what to rehearse.

## Traps
Every trap in the module was offered to me at least once (20 of 20). I took most on a first attempt, corrected them on the spot, and only sometimes got a later re-offer right.
- Fixed (fell, then answered right on a later offer): TR7, TR8, TR9, TR14, TR16, TR21, TR22, TR25, TR34.
- Refuted, not retested (wrong on first attempt, corrected only on the spot): TR1, TR2, TR5, TR11, TR12, TR17, TR23, TR28, TR31, TR39, TR40.
- TR1 came back at S2.route_predict, S2.final_probe and S3.lap, and I fell again on my first attempt each time; that is a sign the lesson is not holding for a novice.

## Report check
- Rendered report (`factory.py render-report`) headline: weak. Accurate for this walk? Mostly yes. The `calibration: underconfident`, `guess_right: 9` and `hinted_only: O1` lines match my Guessing taps and hint use. The `fell_open` labels correctly say my on-the-spot corrections did not count.
- What it misses: it reads only first attempts, so it does not show that I got most re-asked items right after feedback (S6 final check: 8 of 12 cold). The "gap" on O1–O4 reads harsher than my end state, though I accept that a Guessing novice would have that gap.

## Cards
- 12 of 12 answerable from the path. Weakest: card 9 (most common hernia in children; mentioned once, in S4.c1_ok) and card 11 (TEP/TAPP named only in passing).
- Holes: none that the walk did not prepare me for.

## Verdict
- engagement 1–5: 3
- would finish the module: yes, but it is long
- biggest fix: teach the vessel landmarks (inferior epigastric vessels, deep ring, posterior wall) before the cold-open stem at S1.hook, and have "Try again" after a trap re-show a one-line rule rather than the same bare question, so the novice is not guessing twice.

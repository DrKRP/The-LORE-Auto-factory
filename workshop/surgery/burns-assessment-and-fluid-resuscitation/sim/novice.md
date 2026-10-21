# Sim: novice
path: S1.gate → S1.gate_hint → S1.gate → S1.gate_ok → S1.intub → S1.intub_t30a → S1.intub_why → S1.intub → … → S8.p9 → S8.p9_t1  (220 steps, cap reached; module not at END, about 10 nodes short)
persona note: read once months ago; picked the most intuitive option; said Guessing almost throughout; took one hint (S1.gate), otherwise used Try again and Show me the answer.

## Friction
- S5.t1_c_ok: says 'no qualifier in the stem, so the exam answer stays 4 mL', but the stem I was given said 'as per current ATLS practice' and the node before called 2 mL current. I could not tell which figure to carry forward.
- S5.t1_teach: presents 2 mL as current and 4 mL as only the exam key, and never says the two are contested. S5.wx1 and S5.c_try then switch to the 4 mL key without a bridge.
- S7.spot_t0: marks the correct hydrofluoric acid pairing 'not right'. The second line ('pairs the poison with its own antidote') reads like praise.
- S2.co_ok: carboxyhaemoglobin half-life numbers (4 to 5 h, about 1 h) in a correct-answer node. Jargon, three ideas.
- S3.colloid_ok: correct-answer node adds a new fact about dextrose the question did not ask about.
- S4.adult_chart: 'eighteens for the trunk sides and legs' is ambiguous (front or back?).
- S7.a1_t0: convoluted sentence; had to reread it.
- S3.depth_ok, S4.child_chart: three messages each, third one lost me.
- Repeats: child TBSA asked at S4.child_q, S6.child_tbsa, S6.tb_vig; Parkland running-drip at S5.c_seq and S6.drip; shock type at S3.shock_case, S3.cold_check, S5.d_try; escharotomy at S6.escharotomy, S7.d1, S7.legs, S7.cold; topicals at S7.b1, S7.b2, S8.p5, S8.p11. Feels like a drill.
- 'Show me the answer' exits (S2.entry_t12x, S2.p4_t13b, S4.case_t37, S5.wx3_show) end the question with no retest, so I left feeling I had it.
- Length: about 220 nodes to reach S8.p9 with the module still going. A novice would most likely drop out in S7 or S8.

## Traps
- TR1: met at S5.t1_tr1. Refuted, but the 2 mL vs 4 mL messaging left it unclear. REFUTED, NOT CLEAR
- TR2: met at S5.b_tr2 and S5.clock. Refuted; not retested on a fresh stem. REFUTED, NOT RETESTED
- TR3, TR4, TR6, TR8, TR12/13, TR14, TR16, TR18, TR19, TR22, TR23, TR25, TR27, TR29, TR30, TR31: met, refuted, and answered correctly on retry or a later retest. FIXED
- TR17: met only at S8.p9_t1, the last node before the cap. NOT TESTED (no retest reached)

## Report check
- Rendered report (`factory.py render-report`) headline: weak. Partly accurate. It is right that I guessed (guess_right 11, sure_wrong 0, underconfident) and that the first attempts fell open. It is wrong about what I left believing: I corrected most of those errors on retry, yet 10 of 11 objectives read 'gap' and most traps read 'fell_open' with no credit for the retry. 'hints: 3' does not match my path (one hint). The 'weak' headline would send a novice back to the start of the module, which overstates this walk.
- Cards: the report's card order puts card 8 (topical agents) near the end, though I had just answered that pairing correctly on the path. Order looks driven by the objective status, not by what I was least sure of.

## Cards
- 17 of 18 answerable from the path. Hole: card 2 (electrical urine target in mL/kg/h); the path only showed 75 to 100 mL/h for an adult.
- Card 7 (Brooke vs Evans) answerable from S7.q3_ok and S3.colloid_ok.

## Verdict
- engagement 1–5: 3
- would finish the module: no (would most likely drop in S7 or S8 from repetition and length)
- biggest fix: cut the repeated drills (each escharotomy, child TBSA, shock, Parkland-drip and topical question asked once), and state once which fluid figure the module carries and why, so the Parkland drill stops contradicting itself.

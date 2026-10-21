# Sim: misconceived
path: S1.gate → S1.gate_t29 (TR29, Sure) → S1.gate_why → S1.gate (correct, Guessing) → … → S8.p12 (correct, Sure) → S8.close → END  (166 steps, 166 recorded nodes in `misconceived.json`)

Walk shape: I tapped the trap option at every probe where one was offered and said Sure when a trap was held. Each refutation I took ("Show me why", "Show me the answer", or "Try again") changed my belief, and I answered the next retest or cold question correctly. I did not take any skip or fast lane. Full node-by-node path is in `sim/misconceived.json`.

## Friction
- S7.spot_t0 and S7.spot_t1: in "Which order is wrong?", the two trap options are the two correct orders. Their feedback opens "That is not right" and then says "this order is correct". I read this twice to make sense of it. Worst item on the walk.
- S3.fluid_t8: a wrong answer asks "when does colloid come in?" and withholds the answer. Only "Show me why" supplies it.
- S3.fluid_ok: three ideas in one message (crystalloid choice, hyperchloraemic acidosis, Evans and Brooke colloid). I lost the thread on the colloid line.
- S3.depth_ok: the third message adds "simple erythema is not counted", an unrelated idea on a depth question.
- S4.adult_chart: the summary says "eighteens for the trunk sides", but the chart is 18 front and 18 back. S4.close_ok then re-adds a child Lund and Browder line.
- S5.t1_ok: the exam note names "ATLS 10th" as a source. That goes against the notes rule of naming no sources.
- S7.cold_ok: four correction points in one message after a four-line quiz.
- S3.shock_septic and S3.fluid_t8 have no SURE_NOTE, so a Sure learner gets the same generic correction as a Guessing learner.
- S6.electrical: the electrical urine-target trap was refuted only at its own node. The earlier child reveal did not cover it, so my belief survived until the second trap.

## Traps
- TR1: held at S5.t1_check (4 mL for current practice). Refuted at S5.t1_c_t1, retested correct at S5.t1_check. FIXED
- TR2: held at S5.b_try (8 h from arrival). Refuted at S5.b_tr2, retested correct at S5.clock and in S6.ambulance. FIXED
- TR3: held at S5.t1_try (halved total). Refuted at S5.t1_tr1, retested at S5.wx2, S5.wx3, S8.p6, S8.p7. FIXED
- TR4: held at S5.c_try (ambulance fluid not deducted). Refuted at S5.c_tr4, retested correct at S5.c_try. FIXED
- TR6: held at S4.child_q (adult rule of nines for a child). Refuted at S4.child_t_adult, retested by arithmetic at S4.child_num and at S6.child_tbsa. FIXED
- TR8: held at S3.fluid_probe (albumin from the start). Refuted at S3.fluid_t8. Re-held at S7.q3 (Brooke as Parkland plus colloid), refuted, retested correct. FIXED
- TR12: held at S2.entry (chest X-ray confirms). Refuted at S2.entry_t12x, retested at S2.entry. FIXED
- TR13: held at S2.p4 (SpO2 excludes CO). Refuted at S2.p4_t13a, retested at S2.p4. FIXED
- TR14: held at S7.q6 (Marjolin/Curling swapped). Refuted at S7.q6_t1, retested at S7.q6 and S7.c2. FIXED
- TR16: held at S6.start (keep formula rate). Refuted at S6.start_t16, retested at S6.start. FIXED
- TR17: held at S6.contrast (raise rate when urine high). Refuted at S6.co_t17, retested at S6.contrast. FIXED
- TR18: held at S3.depth_case (least painful = full thickness). Refuted at S3.depth_t_full, retested at S3.depth_case and S3.depth_contrast. FIXED
- TR19: held at S6.child_urine (adult 30–50 mL/h in a child), then at S6.electrical (routine adult target). Each refuted at its own node and retested. FIXED
- TR22: held at S4.case (37% for the adult chart). Refuted at S4.case_t37, which led to S4.adult_chart and not back to S4.case. Retested correct at S4.close and S8.p3. FIXED (refuted, not retested at its own node)
- TR23: held at S6.escharotomy (deep partial circumferential). Refuted at S6.es_t_partial, reveal taken, not retested there. Retested correct at S7.d1. FIXED
- TR25: held at S7.b1 (silver sulfadiazine causes acidosis). Refuted at S7.b1_t0, retested correct at S7.b1 and S8.p5, S8.p11. FIXED
- TR27: held at S7.hf (hydroxocobalamin for HF). Refuted at S7.hf_t0; earlier CO/cyanide refuted at S2.cn_case and S2.co_contrast. Retested correct at S7.hf and S7.spot. FIXED
- TR29: held at S1.gate (Parkland before primary survey). Refuted at S1.gate_t29 and S1.gate_why, retested at S1.gate and S1.final. FIXED
- TR30: held at S1.intub (wait for distress). Refuted at S1.intub_t30a, retested at S1.intub and S8.p12. FIXED
- TR31: held at S3.shock_case (septic). Refuted at S3.shock_septic and S3.shock_septic_why, retested at S3.shock_case and S3.cold_check. The cardiogenic variant was never picked, so it was not separately tested. FIXED (variant not tested)

All 20 traps were offered and taken on this path. None survived a refutation on retest. The weakest refutations are TR8 (the S3.fluid_t8 hint is a question) and TR31 (the cardiogenic variant was never taken).

## Report check
- Rendered report (`factory.py render-report`) headline: mixed.
- Accurate about what I believed: yes. The headline is mixed, the calibration reads overconfident, and the confident-error list matches the traps I held on Sure.
- Not accurate about where I ended: no. All 20 traps were corrected on retest, but all 11 objectives still read shaky. The text tells me to revisit the airway, inhalation and TBSA cards as if I had not fixed them. The "Under pressure" lines describe stress I did not feel on this walk.
- Useful as a list of errors to fix, less useful as a verdict on where I stand.

## Cards
- 16 of 16 answerable from the path. Card 13 gives "painless to a pin", which I did not see on my path. I answered from "painless, dry, leathery, does not blanch" and counted it.
- Holes: none that block an answer.

## Verdict
- engagement 1–5: 3
- would finish the module: yes
- biggest fix: rewrite S7.spot so the trap options are wrong orders, and make the feedback stop saying "not right" before "this order is correct".

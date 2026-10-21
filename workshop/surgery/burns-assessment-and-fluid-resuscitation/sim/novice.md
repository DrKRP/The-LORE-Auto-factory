# Sim: novice
path: S1.gate → S1.gate_ok → S1.intub → S1.intub_ok → S1.final → S1.final_ok → S2.entry (hint) → S2.entry_ok → S2.worked → S2.p7 → S2.p4 (TR13, retry) → S2.p4_ok → S2.err_step → … → S8.p12 → S8.p12_ok → S8.close → END  (198 steps; every probe answered as Guessing; hints taken at 9 probes)

## Friction
- S2.worked: three ideas in one explain message (CO half-life, oximeter blind spot, normal chest film). Lost the thread on the first read.
- S3.fluid_ok: Ringer lactate, hyperchloraemic acidosis and the Parkland/Evans/Brooke colloid split in one feedback.
- S3.cold_check: "No hints now" and no hint button at all. As a novice I was stranded on a four-part plan, and the three wrong lines get no explanation.
- S4.adult_chart: "eighteens for the trunk sides and legs" muddles the trunk figure. I could not tell what a trunk side was; S8.p3_t0 repeats the wording.
- S5.why: re-asks why burns leak plasma, already taught at S3.shock_why. It felt like a repeat, and the same mechanism is re-explained.
- S5.t1_check: no hint option here, unlike the neighbouring probes.
- S7.a1_t0: refers to "Brooke and Evans recipes" before the colloid formulae are introduced at S7.q3.
- S7.cold_ok: six claims in one feedback message. Dense, and it does not say why the other three lines are wrong.
- S7.spot_t0: "That is not right. That choice is not right: this order is correct" says no and yes in one breath.
- Length: 198 steps for one topic, with long hint/retry/show-working loops in S5. Felt heavy by S6.

## Traps
- TR1 (S5.t1_c_t1, 4 mL for "current"): fell, retry, correct. FIXED
- TR2 (S5.b_tr2, S6.am_t2 clock start): fell, correct on the next window. FIXED
- TR3 (S5.wx2_t3a, S5.wx3_t3a halving and divisor): fell twice, correct on retry. FIXED
- TR4 (S5.c_tr4, forgot prehospital fluid): fell, retry, correct. FIXED
- TR6 (S4.child_t_adult, S6.tb_t_small): fell, retry, correct. FIXED
- TR8 (S3.fluid_t8 albumin, S7.a1_t0, S7.q3_t1, S7.a2_t0): fell four times, each corrected within the node. FIXED
- TR13 (S2.p4_t13a, S2.why_t13b, S8.p4_t0): fell three times; the reassuring SpO2 is still tempting. FIXED
- TR14 (S7.c2_t0 Curling vs Marjolin): fell, retry, correct. FIXED
- TR16/TR17 (S6.start_t16 formula held, S6.co_t17 urine direction, S8.p9_t0): fell, corrected. FIXED
- TR18 (S3.depth_t_full, S3.contrast_t_pain, S8.p2_t0): fell three times, each corrected. FIXED
- TR19 (S6.child_t30, S6.elec_t_adult, S8.p10_t0): fell, corrected. FIXED
- TR22 (S8.p3_t0 TBSA doubling): fell, retry, correct. FIXED
- TR23 (S6.es_t_partial escharotomy depth): fell, retry, correct. FIXED
- TR25 (S7.b1_t0, S8.p5_t0, S8.p11): fell, revealed, then correct on a later probe. FIXED
- TR27 (S2.cn_t27a, S7.hf_t0, S7.spot_t0): fell, corrected. FIXED
- TR30 (S8.p1_t2 wait for voice change): fell, retry, correct. FIXED
- TR31 (S5.why_t31a heart as cause): fell, retry, correct. FIXED
- TR12 (S8.p8_t0 chest film first): fell, retry, correct. FIXED
- TR29: never chosen on my path. NOT TESTED (I picked the airway option at S1.gate and S8.p1)

## Report check
- Rendered report (`factory.py render-report`) headline: weak; calibration underconfident; every objective gap except O1, O9 and O11 (shaky).
- Accurate for this walk? Partly. Underconfident is fair: I guessed and was right 21 times. But "weak" overstates it. I recovered inside the node on most traps and answered antidotes, depth, TBSA and spot-check right after one retry, yet O3, O5, O6 and O10 read gap. Traps I corrected within the node are listed fell_open, with no credit for the retry. The report never separates right-after-feedback from right-first-time, so my guesses read as weakness. The next-step advice (airway card, then the opening segment) is sensible.

## Cards
- 16 of 16 answerable at the core level from the path.
- Partial: card 5 (escharotomy, "incise through the eschar only") and card 13 (full thickness "painless to a pin") go beyond what I was shown; I answered the indication and the signs only.

## Verdict
- engagement 1–5: 3
- would finish the module: yes, though the S5 loops and the S7 packed feedback made me want to skip
- biggest fix: cut the repeats and packed feedback (remove the S5 re-run of capillary leak, split S7.cold_ok and S2.worked into one idea each) and give the no-hint cold checks a hint option so a novice is not stranded.

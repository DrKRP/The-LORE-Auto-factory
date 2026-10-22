# Sim: misconceived
path: S1.start → S1.t_scan (TR1, Sure) → S1.x_key → S1.p2 → S1.p2_ok → S1.x2 → S1.p3 → S1.p3_frozen (TR4, Sure) → S1.x3 → S1.p4 → S1.p4_ok → S1.p5 → S1.p5_tg (TR30, Sure) → S1.x5 → S2.pap_ask → S2.pap_t5a (TR5, Sure) → S2.pap_ask → S2.pap_ok → … → S8.k6_ok → END  (153 taps; full path in `sim/misconceived.json`)

## Friction
- S2.pap_t5a: refutation with only "Try again" and no "Show me why" exit. A learner who keeps the belief goes straight back to the same probe. My walk looped 103 times here before the feedback changed my belief. The same dead end holds on 58 retry-only feedback nodes in the module (5 on this path).
- S1.t_scan (and the other trap feedback nodes): every wrong answer opens with "That choice is not right." Across about 20 traps this repeats until the tone goes flat by the middle of S2.
- S8.h1 to S8.k6_ok: a cold-check segment of 24 nodes re-asks traps already fixed in S1 to S7, with near-identical options. For a learner who has corrected each belief it is dead weight.
- S3.dtc_ok: two ideas in one message (the definition of DTC and the list of DTC types), then the exclusions (medullary, anaplastic). The exclusions could be their own node.
- S6.w1: a four-step worked case in three messages, with steps 3 and 4 in one message. Hard to keep the count while reading.
- S1.x_key: asks the learner to hold two keys at once (PYQ "first" versus current practice). Workable on this path, but it depends on the reader already knowing the exam key.

## Traps
- TR1: refuted at S1.start (tapped, Sure), held at re-test S1.p2. FIXED
- TR3: refuted at S2.common_ask, held at re-test S2.iodine_ask. FIXED
- TR4: refuted at S1.p3, held at re-test S1.p4. FIXED
- TR5: refuted at S2.pap_ask, held at re-test S2.side_ask. FIXED
- TR6: refuted at S2.side_ask, held at re-test S2.niftp_ask. FIXED
- TR7: refuted at S6.fade5, held at re-test S6.fade6. FIXED
- TR8: refuted at S4.t2, held at re-test S4.t1. FIXED
- TR10: refuted at S3.lat_probe, held at re-test S3.lat_retest. FIXED
- TR11: refuted at S3.fol_predict, held at re-test S3.pap_contrast. FIXED
- TR12: refuted at S3.fol_explain, held at re-test S3.dtc_which. FIXED
- TR16: refuted at S6.fade1, held at re-test S6.fade4. FIXED
- TR20: refuted at S5.u5, held at re-test S5.u6. FIXED
- TR21: refuted at S4.d0, held at re-test S4.f1. FIXED
- TR22: refuted at S4.f2, held at re-test S4.f3. FIXED
- TR24: refuted at S7.singer, held at re-test S7.voice. FIXED
- TR25: refuted at S7.dayone, held at re-test S7.pairs. FIXED
- TR26: refuted at S7.neck, held at re-test S7.airway. FIXED
- TR27: refuted at S5.u1, held at re-test S5.u2. FIXED
- TR28: refuted at S6.fade2, held at re-test S8.k5. FIXED
- TR30: refuted at S1.p5, held at re-test S6.pre. FIXED
- Merged into other traps (not separate on the path): TR2 into TR1, TR9 into TR5, TR13 into TR12, TR17 into TR27, TR19 into TR8.
- No trap was NOT TESTED or SURVIVED on this path.

Caveat: the walk changed belief after one refutation, as the persona rules allow. That is the reason every trap is FIXED. A learner who needs the "Show me why" text before changing belief would not get there from the S2.pap_t5a-style nodes.

## Report check
- Rendered report (`factory.py render-report surgery/thyroid-nodule-and-differentiated-thyroid-cancer sim/misconceived.json --module-file module.json`) headline: mixed. Accurate for this walk: yes.
- The trap, objective, calibration and hint lines match the walk: 20 of 20 traps fell_recovered, 20 confident errors, 15 hints (agency taps), 6 of 6 cold probes right, calibration overconfident (20 wrong Sure answers).
- The "mixed" headline and "shaky" for all 10 objectives fit a walk that corrected every fall. No objective is a gap, since no trap is fell_open.
- Missed: the per-trap texts ("Under pressure the X can return…") are accurate but read the same across traps. The report does not say which wrong model to drop first beyond the card order.

## Cards
- 9 of 9 answerable from the path. Card 1 (TSH and ultrasound first, FNAC for nature): S1.start, S8.h1. Card 2 (papillary nuclei, follicular invasion): S2.pap_ok, S8.h2. Card 3 (commonest DTC, iodine): S2.common_ok, S2.iodine_ok. Card 4 (spread routes): S3.fol_explain_ok, S3.pap_ok. Card 5 (Bethesda II, IV): S4.d0, S4.f2_ok, S8.k2. Card 6 (1 to 4 cm surgery): S4.t2_ok, S8.k3. Card 7 (radioiodine, TSH): S5.u1, S5.u2, S5.u5. Card 8 (thyroglobulin, antibodies): S6.fade2, S8.k5. Card 9 (complications, neck haematoma): S7.dayone_show, S7.neck_show.
- Coverage holes: none.

## Verdict
- engagement 1–5: 3
- would finish the module: yes, but the path is long (153 taps) and repetitive
- biggest fix: give every trap refutation a "Show me why" exit, or a second line that names the right model. Right now a learner who holds the belief is stuck on "Try again" with no new information (58 such nodes; S2.pap_t5a is the clearest).
- R9 (Diagnosticity) score: 4. Each wrong option separates one named wrong model from the right one, so the path tells a teacher what I believe. The report says it clearly by trap, though the per-trap wording is generic.

# Sim: strong
path: S1.hook (correct, Sure) → S1.hook_ok (skip) → S1.femoral_probe (correct, Sure) → S1.fem_ok → S1.tim_probe (correct, Sure) → S1.tim_ok → S1.close_s1 → S2.route_predict (skip) → S2.final_probe (correct, Sure) → S2.final_ok → S3.predict (correct, Sure) → S3.predict_ok → S3.start (correct, Sure) → S3.start_ok (skip) → S3.occl_v (correct, Sure) → S3.occl_ok → S3.lap → S3.zieman → S3.tr31 → S3.contrast → S3.wall2 → S3.close_s3 → S4.a_probe (correct, Sure) → S4.a_ok (skip) → S4.f_probe (correct, Sure) → S4.f_ok → S4.c1_probe → S4.d1_probe (correct, Sure) → S4.d3_probe (correct, Sure) → S4.d4_probe (correct, Sure) → S4.e1_probe → S4.e2_probe → S5.emerg (correct, Sure) → S5.taxis_why → S5.child → S5.adult (correct, Sure) → S5.ex2 → S5.lap → S5.nerve → S5.lfcn → S5.tri → S5.occ → S5.tdef → S5.tmesh → S6.p1 (correct, Sure) → S6.p2 → S6.p3 → S6.p4 → S6.p5 → S6.p6 → S6.p7 → S6.p8 (correct) → S6.p9 → S6.p10 → S6.p11 → S6.p12 → S6.recap → END  (92 steps; every choice was correct, four skips taken, no hints, no "Try again")

I answered every probe correctly and said Sure on every confidence prompt. I took the fast lane (skip) whenever offered. I used my own knowledge where the module was silent, as the strong persona may.

## Friction
- S2.route_predict: the skip sends me straight to S2.final_probe. Hesselbach's triangle boundaries (core O2, a high-yield trap) are never taught on this path. The first time they appear is a fresh stem at S6.p1, with no teaching before it. The recap then asserts the triangle's sides as known. A skipper gets no lesson on a core objective.
- S1.hook_ok and S3.start_ok: the skips bypass the route lesson and the pattern lesson, so the later direct/indirect probes (S3.contrast, S6.p3) test those ideas cold.
- S4.d1_probe and S5.emerg: near-verbatim repeat (same stem, same answer). Reads as padding.
- S5.tdef, S5.tmesh and S6.p9: herniorrhaphy vs hernioplasty vs herniotomy tested three times with near-identical stems.
- S4.d3_probe and S5.occ: the occult-hernia ultrasound question asked twice in a row.
- S5.adult and S6.p8: Lichtenstein as the standard open repair asked twice.
- S5.ex2: "which step is wrong" labels two correct steps as trap options. The 'Not quite' feedback on the correct step 1 ("A groin you cannot see into makes a scan feel careful") is muddled. I picked the right answer, but the correction reads badly.
- S4.c1_probe: no Sure/Guessing prompt and no "Not sure" option, unlike the rest of the module.
- S6.recap: asserts triangle and nerve rules that a skipper has not been taught. Fine for me, but unreliable as a summary for skippers.

## Traps
- Trap options offered on this path: TR1, TR2, TR5, TR7, TR8, TR9, TR11, TR12, TR14, TR16, TR17, TR21, TR22, TR23, TR25, TR28, TR31, TR34, TR39, TR40 (20 of 20).
- I never picked a trap option, so no trap was refuted or retested. The strong persona is not holding any of them, so the trap status is not meaningful for this run.
- Coverage note: TR2 (triangle boundaries) was offered only cold at S6.p1, after the skip removed its teaching. Its "avoided" status is one cold answer, not a learned belief.

## Report check
- Rendered report (`factory.py render-report`) headline: strong. Accurate for this walk: yes, mostly.
- Accurate: calibration 'calibrated', zero sure-wrong, all 12 cold answers right, fast lane flagged, and the note that skipped lessons should be checked by the review cards.
- Overreach: O2 'secure' rests on one cold probe after I skipped the teaching. The report should say "one cold answer, lesson skipped" rather than "secure".
- Contradiction: "No gaps" at the end sits two lines below "You skipped a lesson". Pick one.

## Cards
- 12 of 12 answerable from the path, but card 8 (Hesselbach's boundaries) is answerable only from the one cold probe at S6.p1 and its feedback, not from a lesson. Card 9 (most common hernia in children) is answerable by inference from S5.child (patent processus means indirect), not stated outright.

## Verdict
- engagement 1–5: 3
- would finish the module: yes
- biggest fix: make the fast lanes safe. A skip should still deliver the core O2 triangle boundaries (or force a cold probe with a teach-back), and cut S5/S6 consolidation from twelve near-repeat probes to one cold retest per objective that was not already probed earlier on the path.

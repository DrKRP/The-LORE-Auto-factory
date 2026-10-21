# Sim: misconceived
path: S1.case → S1.case_t4 (TR4, Sure) → S1.case_why → S1.contrast → S1.pain (TR4, Sure) → S1.pain_t4 → S1.pain_why → S1.first_test → S1.first_t2 (TR2, Sure) → S1.first_why → S1.sens → S1.sens_t2 (TR2, Sure) → S1.sens_why → S1.ladder → S2.start (TR15, Sure) → S2.start_t1 → S2.show_start → S2.c2 → S2.c3 (TR15, Sure) → S2.c3_t1 → S2.c3 → S2.c3_ok → … → S8.p12 (TR16, Sure) → S8.p12_t0 → S8.p12 → S8.p12_ok → END  (251 steps; every trap taken on first encounter with Sure where asked, then corrected on retry)

Note on step count: the persona rules cap a walk at 220 steps. I went past that cap (251 steps) without a loop, because the module kept offering new probes and retries. I reached END, so this is a length finding, not a loop, but it is outside the rule and should be read as such.

## Friction
- S5.fit_t11a: says the PYQ key and current practice differ and that many keys still carry the 6–8 week plan, but never says what the exam key expects for this item. S8.p4_ok later says the key expected interval surgery. The teach-both point is incomplete on first contact and only completed three nodes later.
- S7.p2_t3, S7.p3_t1, S7.p4_t1: the SURE_NOTE repeats the main feedback sentence almost word for word. The "You were sure" line adds nothing and reads like a duplicated message.
- S7.p10_t3: the SURE_NOTE ("together is not one type") does not address the belief in the option I chose ("the key is simply outdated"). The main text does refute it; the sure note points somewhere else.
- The colic-versus-cholecystitis refutation runs four times in near-identical wording (S1.case_t4, S1.pain_t4, S3.open_waves, S3.pain2_t2). By the third I was reading for the one changed word.
- S8.p1 to S8.p12: twelve single-question probes in a row, with almost no teaching between them, and most have no confidence prompt. The cold consolidation becomes a grind with no change of pace.
- S2.start_t1 and S2.c5_t1: after "Show me the answer" the path moves on without re-asking. The belief is refuted in the explanation but not retested on the same question; the retest comes only two or more nodes later.
- Overall the walk is long (251 steps). Most of the length is retries and repeated refutations, not new teaching.

## Traps
- TR1: offered at S7.pp and S7.p10. Took the trap at S7.p10 (outdated key), refuted, retried, correct. FIXED
- TR2: offered at S1.first_test, S1.sens, S4.case_a, S4.case_b, S8.p3. Refuted at S1.first_t2 and S1.sens_t2, held on S4.case_a and S4.case_b, then correct at S4.case_b retest and S8.p3 retry. FIXED
- TR3: offered at S4.case_c and S8.p2. Refuted at S4.case_c, corrected on retry; CT variant at S8.p2 refuted, corrected. FIXED
- TR4: offered at S1.case, S1.pain, S3.open, S3.pain2, S2.c6 (TR4 option). Refuted at S1.case_t4, S1.pain_t4, S3.open_waves, S3.pain2_t2; correct on retry at S3.open and S3.pain2. FIXED
- TR5: offered at S3.cv_a, S3.cv_c, S7.p9. Refuted each time; correct on retry at S3.cv_c and S7.p9. FIXED
- TR7: offered at S3.tg_a, S3.tg_b, S3.tg_c, S4.case_d. Refuted each time; correct on retry. FIXED
- TR8: offered at S5.grade_vignette, S5.numbers_ii, S5.numbers_iii, S8.p1. Refuted each time; correct on retry at all four. FIXED
- TR10: offered at S5.fit_plan, S5.unfit_plan, S5.unfit_seq, S8.p5. Refuted at S5.unfit_t10a and S8.p5; correct on retry. FIXED
- TR11: offered at S5.fit_plan, S5.unfit_seq, S8.p4. Refuted at S5.fit_t11a and S5.unfit_seq_t11; correct at S5.fit_retest and S8.p4. FIXED
- TR12: offered at S6.asym, S6.b, S8.p6. Refuted at S6.asym_t0; correct on retry; correct at S8.p6. FIXED
- TR14: offered at S6.c. Took the trap (large calcified stone), refuted, correct on retry. FIXED
- TR15: offered at S2.start, S2.c3, S2.c4q, S7.p8. Refuted each time; correct on retry at S2.c3, S2.c4q, S7.p8. FIXED
- TR16: offered at S7.p1, S7.p2, S8.p12. Refuted; correct on retry at S7.p1 and S8.p12. FIXED
- TR17: offered at S7.p4, S7.p5, S8.p7. Refuted; correct on retry at S7.p4 and S7.p5, and at S8.p7. FIXED
- TR18: offered at S7.p6, S7.p7, S8.p8. Refuted; correct on retry at S7.p6, S7.p7 and S8.p8. FIXED
- TR19: offered at S6.h, S6.i, S8.p10. Refuted; correct on retry at S6.h and S6.i. FIXED
- TR20: offered at S6.bail, S6.j, S8.p9. Refuted; correct on retry at S6.j and S8.p9. FIXED
- TR22: offered at S7.p2, S7.p3. Refuted; correct on retry at S7.p2 and S7.p3. FIXED
- TR23: offered at S2.c5, S2.c6, S6.f. Refuted; correct on retry at S2.c6 and S6.f. FIXED
- TR24: offered at S6.e, S8.p11. Refuted; correct on retry at both. FIXED

Every trap on the module was offered on my path and every one was corrected on retry. The fixes are real in the walk but they are immediate retries. A misconceived learner who was refuted once and then answered right is not the same as one who holds the correction a week later. The cards are the only later check, and there is no spaced retest inside the module.

## Report check
- Rendered report (`factory.py render-report`) headline: weak. The headline matches what I went through: cold answers were wrong almost everywhere and I said Sure to 47 wrong answers. Accurate for the cold picture.
- Trap statuses: the report lists all 20 traps as `fell_open` and says "meet it again on a fresh question". For me that is not accurate: each trap was refuted and I answered correctly on the retry. The report only reads first encounters, so it cannot see the in-walk correction. It should credit corrected-on-retry traps.
- Hints: the report says 12 hints. I tapped no "Not sure, give me a hint" option. The 12 are "Show me why" explanations, so the label is wrong.
- Calibration (overconfident) and the 47 sure-wrong count match the walk.
- Review-card order and the "do the card" lines are useful and point to the right objectives.
- Verdict on the report: partly accurate. It is useful, but it would tell me my beliefs survived when I corrected each one in the walk.

## Cards
- 7 of 7 answerable from the path (the module has 7 review cards, not 11):
  1. Complication test (CT): S8.p3_ok, S1.ladder.
  2. Non-invasive CBD test (MRCP): S4.case_c_ok, S8.p2_ok.
  3. TG18 Grade III respiratory criterion (P/F below 300): S8.p1_ok, S8.p1_show.
  4. Fit calculous patient (early lap chole, within 72 h): S5.fit_ok, S8.p4_ok.
  5. Asymptomatic stones (expectant management): S6.asym_ok, S8.p6_ok.
  6. Gallstone ileus site and Rigler's triad: S7.p2_ok.
  7. Commonest major duct injury (misidentification): S6.j_ok, S8.p9_ok.
- Holes: none on the cards. The weak spot is that the cards are answerable only because I was re-asked the same thing on other nodes.

## Verdict
- engagement 1–5: 3
- would finish the module: yes, but it dragged. The 251-step walk is over the persona cap and the cold consolidation run (S8.p1 to S8.p12) is the main reason.
- biggest fix: state the exam key on S5.fit_t11a (early surgery is current practice; the PYQ key expected interval surgery), matching S8.p4_ok, and cut the S8 consolidation run to a short mixed set.

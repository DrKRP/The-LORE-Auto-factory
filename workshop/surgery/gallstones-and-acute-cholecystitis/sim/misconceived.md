# Sim: misconceived
path: S1.case → S1.case_t4 → S1.case_why → S1.contrast → S1.pain → S1.pain_t4 → S1.pain_why → S1.first_test → … → S8.p10_show → S8.p11 → S8.p11_t1 → S8.p11 → S8.p11_ok → S8.p12  (220 steps; the full path with choice indices and Sure/Guessing is in `sim/misconceived.json`)

Stop reason: the 220-step cap. The walk stopped at S8.p12 (I tapped the correct option, choice 0), one node short of the feedback S8.p12_ok and END. This was not a loop. The length came from retries on almost every probe.

## Friction
- S1.case_t4 and most wrong-answer feedback: "That choice is not right." and a "You were sure, so …" opener repeat on nearly every wrong tap (about 60 times on this path). It reads as a stock response by the middle of the module.
- S1.sens_t2: "Show me why" goes to an explanation and then on to the next item. The same question is never asked again, so the correction is not tested. This pattern repeats at S5.fit_t11a, S5.unfit_t10a, S6.asym_t0, S6.i_t0, S6.bail_t0, S7.pp_t1, S7.p8_t3, S8.p3_t1, S8.p10_t0.
- S5.grade3_teach: six organ thresholds (heart, brain, lung, kidney, liver, blood) in two messages. I lost track of which number belongs to which organ.
- S8 (S8.p1 to S8.p12): eleven probes in a row with feedback only and no teaching between them. The run is long and the thread is lost. This is most of the 220 steps.
- S6.bail_t0: TR19 is refuted here, then "Show me why" with no retry. The critical-view rule is not checked again before the module moves on.
- S7.p10_t1: the sure_note data includes a `flag: "unverified"` field. It is not shown on screen, but it is in the node data. Check that it is stripped before publishing.

## Traps
Status is taken from the last encounter on the path. "Fixed" means a correct answer after a refutation at the last encounter. "Refuted-not-retested" means the last encounter was a refutation with no correct re-answer.

- TR1 (most common stone is cholesterol): refuted-not-retested. Corrected at S2.c8 with a retry. Re-held at S7.pp ("alcohol first"), refuted, then "Show me why" with no retry.
- TR2 (ultrasound is most sensitive; CT first): refuted-not-retested. Corrected at S4.case_a and S4.case_b retries. Re-held at S8.p3 (ultrasound for complications), refuted, then "Show the answer".
- TR3 (ultrasound/CT/ERCP for CBD stones): FIXED. Corrected at S4.case_c retry. Re-held at S8.p2 (ERCP), refuted, then correct at the retry.
- TR4 (day-long pain is still colic): FIXED. Refuted at S1.case_t4 and S1.pain_t4. Corrected at S3.open. Re-held at S3.pain2 (day-long stone pain), then correct at the retry.
- TR5 (any palpable gallbladder means cancer): refuted-not-retested. Corrected at S3.cv_a, S3.cv_b and S3.cv_c retries. Re-held at S7.p9 ("drop jaundiced"), refuted, then "Show me why" with no retry.
- TR7 (suspected vs definite set): FIXED. Corrected at S3.tg_a, S3.tg_c and S4.case_d retries.
- TR8 (TG18 numbers swapped with lab cut-offs): refuted-not-retested. Corrected at S5.numbers_ii and S5.numbers_iii retries. Re-held at S8.p1 (PaO2 below 60), refuted, then "Show the answer".
- TR10 (early lap chole in every grade): refuted-not-retested. Picked at S5.unfit_plan, refuted, then "Show me why". Never answered correctly on the same item. It was offered again at S5.unfit_seq, S6.e and S8.p11, and I picked other traps there.
- TR11 (interval surgery at 6-8 weeks): FIXED. Refuted at S5.fit_t11a and S5.unfit_seq_t11. Correct at S5.fit_retest. Re-held at S8.p4, then correct at the retry.
- TR12 (asymptomatic stones should be removed): refuted-not-retested. Refuted at S6.asym_t0. Corrected at S6.b. Re-held at S7.p10 ("operate now, diabetic"), refuted, then "Show me why".
- TR14 (UDCA dissolves any stone): FIXED. Refuted at S6.c_t0. Re-held at S8.p6, then correct at the retry.
- TR15 (black and brown stones swapped): refuted-not-retested. Corrected at S2.c3 and S2.c4q retries. Re-held at S7.p8 (black stones in ducts), refuted, then "Show me why".
- TR16 (Bouveret vs gallstone ileus): FIXED (provisional). Refuted at S7.p1 and explained with "Show me why". Answered correctly at S8.p12 (step 220). The feedback was beyond the cap, so this is not confirmed by a visible correction.
- TR17 (Charcot's triad vs Reynolds' pentad): refuted-not-retested. Corrected at S7.p5. Re-held at S8.p7 (hypotension is not in the pentad), refuted, then "Show the answer".
- TR18 (E. coli in emphysematous cholecystitis): refuted-not-retested. Corrected at S7.p7 retry. Re-held at S8.p8 (Clostridium with no gas), refuted, then "Show the answer".
- TR19 (two structures are enough): refuted-not-retested. Corrected at S6.h retry. Re-held at S8.p10 ("two structures is the whole view"), refuted, then "Show the answer".
- TR20 (commonest duct injury is vascular): FIXED. Corrected at S6.j retry. Re-held at S8.p9 (blind clip), refuted, then correct at the retry.
- TR22 (Mirizzi is a stone in the CBD): FIXED (provisional). Refuted at S7.p2 and S7.p3. Corrected at S7.p3 retry. Answered correctly at S8.p12 (step 220). Same cap caveat as TR16.
- TR23 (acalculous milder than calculous): FIXED. Corrected at S2.c5 and S2.c6 retries. Re-held at S6.f ("mild course"), refuted, then correct at the retry.
- TR24 (early surgery for acalculous disease): FIXED. Refuted at S6.e_t0. Re-held at S8.p11 ("early lap tomorrow"), refuted, then correct at the retry.

Totals: 10 fixed (including 2 provisional), 10 refuted-not-retested, 0 survived, 0 not-tested. All 20 traps were offered on this path.

## Report check
- Rendered report (`factory.py render-report`) headline: **weak**. The rendered file is `sim/misconceived.report.json`. Accurate for this walk? **No, partly.**
  - Accurate: calibration is "overconfident" (I said Sure on all 76 probes; 49 were trap picks). The `sure_wrong` count of 49 matches. `guess_right: 0` is correct because I never guessed.
  - Not accurate: it labels 18 traps "fell_open", but I corrected TR3, TR4, TR7, TR11, TR14, TR20, TR23 and TR24 on a retry that was answered correctly. It does not credit retry corrections.
  - Mislabeled: "hints: 29" is actually my 29 "Show me why / Show the answer" taps. I never tapped a hint option.
  - Harsh: the headline "weak" and "gap" for all twelve objectives come from first-try answers only. A "mixed" headline that credits retries would describe this walk better.
  - Useful: the action lines ("Do the O4 card", "rebuild A, B, C from scratch") point at the right lessons.
- Note for the factory: the trap-status logic should count a correct retry as recovery. A "show me why" tap with no re-ask should count as "not retested", which is the second case in my trap list.

## Cards
- 12 of 12 answerable from the path. Each card's answer appeared in a `correct` or `ok` feedback node I actually saw: card 1 at S8.p3_ok, card 2 at S4.case_c_ok, card 3 at S8.p1_ok, card 4 at S5.fit_ok, card 5 at S6.asym_ok, card 6 at S7.p2_ok, card 7 at S6.j_ok, card 8 at S1.pain_ok and S3.pain2_ok, card 9 at S2.c8_ok, card 10 at S2.start_ok and S2.c3_ok, card 11 at S3.tg_a_ok and S3.tg_c_ok, card 12 at S3.cv_c_ok.
- Holes: none. Caveat: I was confident in the cards mostly because the correct answer was shown after a retry, not because I retained the trap items.

## Verdict
- engagement 1–5: 3. The content is clear and the traps are well chosen. The repeated feedback text, the "show me why" dead ends and the eleven-probe S8 run wear it down.
- would finish the module: yes, but only with effort. The walk reached 220 steps without reaching END.
- biggest fix: after any "Show me why" or "Show the answer" explanation, re-ask the same item (or a variant) before moving on. Ten of 20 traps were refuted but never retested, and the walk ended on explanations.

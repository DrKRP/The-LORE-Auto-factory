# Sim: novice
module: surgery/acute-intestinal-obstruction
persona: novice (read the topic once, months ago; picks the intuitive option; says Guessing)
path: S1.start[0] → S1.hint_adh[1] → S1.start_b[2] → S1.expl_adh[0] → S1.both[0] → S1.expl_same[0] → S1.sort[0] → S1.expl_sort_intra[0] → S1.which[0] → S1.expl_which_int[0] → S1.virgin[0] → S1.hint_virgin[0] → S1.virgin_b[2] → S1.ok_virgin[0] → S1.recap[0] → S2.start[0] → S2.a_h1[0] → S2.start_b[2] → S2.a_ok[0] → S2.why[1] → S2.why_x2[0] → S2.snd[0] → S2.snd_h1[0] → S2.snd_b[0] → S2.snd_ok[0] → S2.ile[0] → S2.ile_x1[0] → S2.pain[0] → S2.pain_h1[0] → S2.pain_b[1] → S2.pain_ok[0] → S2.cnot[1] → S2.cnot_x1[0] → S3.film[0] → S3.film_hA[1] → S3.film_xA[0] → S3.num[0] → S3.num_h6[0] → S3.num[1] → S3.num_ok[0] → S3.film2[0] → S3.film2_xA[0] → S3.caecum[2] → S3.caecum_h2[0] → S3.caecum[1] → S3.caecum_ok[0] → S3.inv[0] → S3.inv_hX[1] → S3.inv_xX[0] → S3.inv2[0] → S3.inv2_xA[0] → S3.inv2c[0] → S3.inv2c_xA[0] → S3.coffee[0] → S3.coffee_hC[0] → S3.coffee[1] → S3.coffee_ok[0] → S3.sign[0] → S3.sign_xA[0] → S4.c1[0] → S4.c1_t31[1] → S4.w1[0] → S4.w2[0] → S4.c3[0] → S4.c3_t22[0] → S4.c3[2] → S4.c3_ok[0] → S4.c2[0] → S4.c2_t26[0] → S4.c2[1] → S4.c2_ok[0] → S4.c4[1] → S4.c4_t22[1] → S4.c5[1] → S4.c5_p[0] → S4.c5[2] → S4.c5_ok[0] → S4.c7[0] → S4.c7_t26[0] → S4.c7[1] → S4.c7_ok[0] → S4.c6[1] → S4.c6_p[0] → S4.c6[2] → S4.c6_ok[0] → S4.c8[0] → S4.c8_t31[1] → S4.c9[0] → S4.c9_t23[0] → S4.c9[2] → S4.c9_ok[0] → S4.c10[0] → S4.c10_t31[1] → S5.virgin_case[0] → S5.virgin_h[1] → S5.virgin_f[0] → S5.femoral_case[0] → S5.femoral_h[0] → S5.femoral_case[1] → S5.femoral_ok[0] → S5.richter_case[1] → S5.richter_h_full[0] → S5.richter_case[0] → S5.richter_ok[0] → S5.littre_case[0] → S5.littre_f_r[0] → S5.maydl_case[2] → S5.maydl_f_sac[0] → S5.intus_case[1] → S5.intus_h[0] → S5.intus_case[0] → S5.intus_ok[0] → S5.intus_why_case[0] → S5.intus_why_f1[0] → S5.child_case[0] → S5.child_h[0] → S5.child_case[2] → S5.child_ok[0] → S5.theatre_case[1] → S5.theatre_h_dx[0] → S5.theatre_case[0] → S5.theatre_ok[0] → S5.lbo_case[2] → S5.lbo_h_volv[0] → S5.lbo_case[1] → S5.lbo_ok[0] → S5.sites_case[0] → S5.sites_h_caecum[1] → S5.sites_f_caecum[0] → S5.sites_case2[0] → S5.sites_h_sigmoid[1] → S5.sites_f_sigmoid[0] → S5.sig_case[1] → S5.sig_h_discharge[0] → S5.sig_case[0] → S5.sig_ok[0] → S5.caecal_case[1] → S5.caecal_h_stent[0] → S5.caecal_case[2] → S5.caecal_ok[0] → S5.coffee_case[0] → S5.coffee_h_caecal[0] → S5.coffee_case[1] → S5.coffee_ok[0] → S5.signs_case[1] → S5.signs_h_swap[0] → S5.signs_case[0] → S5.signs_ok[0] → S6.q1[1] → S6.q1_f1[0] → S6.q2[0] → S6.q2_f0[0] → S6.q3[0] → S6.q3_f0[0] → S6.q4[2] → S6.q4_f2[0] → S6.q5[2] → S6.q5_f2[0] → S6.q6[0] → S6.q6_f0[0] → S6.q7[0] → S6.q7_f0[0] → S6.q8[1] → S6.q8_f1[0] → S6.q9[0] → S6.q9_f0[0] → S6.q10[0] → S6.q10_f0[0] → S6.q11[2] → S6.q11_f2[0] → S6.q12[0] → S6.q12_f0[0] → S6.close[0]  (173 steps, reached END)

Choice index is the position in each node's `choices` list. Feedback nodes are recorded as `[0]` (Next). Sure was asked on 41 probes, all answered Guessing; the rest had no confidence prompt.

## Friction
- S2.why_x2, S2.ile_x1, S2.cnot_x1, S2.cnot_x2, S2.pain_x1: wrong-answer feedback opens with "Right:" and then explains the correct answer, so the tone flips mid-message.
- S4.c5_p: in a NOT question, the feedback says it "is correct to name it as an indication" for the wrong option; I re-read it to see why I was wrong.
- S5.littre_f_r: wrong-answer feedback never names the right eponym (Littre's); I was left guessing.
- S5.theatre_h_dx, S5.lbo_h_volv, S5.sites_h_caecum, S5.signs_h_swap: hint says only "Try again, or see why." with no new cue.
- S5.coffee_case and S5.signs_case: coffee-bean and claw/target questions repeat S3.coffee and S3.sign almost verbatim; it felt like the same item with no new teaching.
- S6.q12: NOT-intramural item repeats S1.which. S6 as a whole re-asks S1 to S5 content (about 40 steps); I got most of them wrong, so the earlier corrections did not hold.
- S3 (about 25 single-question probes, short feedback, little connecting explanation): it reads as a quiz, and I lost the thread of why each marker matters.
- S1.both: the PYQ-key versus current-practice idea is first named after I had already picked two wrong answers.

## Traps
All 20 module traps were offered on this path and I fell for each one at least once. Status for a novice is "met", not fixed or survived, because the persona does not hold beliefs to be refuted. Retries after hint text got me to the correct answer on 23 occasions, but the S6 re-quiz then reversed most of those corrections.
- TR1, TR2, TR3, TR4, TR5, TR8, TR11, TR12, TR13, TR14, TR17, TR18, TR21, TR22, TR23, TR26, TR31, TR35, TR36, TR40: met.

## Report check
- Rendered report (`factory.py render-report`) headline: weak. Accurate for the belief picture: yes. It names the right models (one answer for every setting, fixed rules, look-alike signs, superlatives stretched beyond their qualifier, order of management).
- What it got wrong or missed:
  - It says "You used no hints", but I took 23 retries after hint text and 7 "show me why" explanations. `hinted_only` is empty even though most of my correct answers came after a hint.
  - The calibration line "Sure answers were right" describes Sure answers I never gave. All of my asked answers were Guessing.
  - It does not say that my S6 re-quiz reversed most of the S1 to S5 corrections. That is the main thing a novice needs to hear.

## Cards
- 11 of 11 answerable from the path, with the teaching nodes I actually reached: PYQ key (S1.recap), early features (S2.a_ok, S6.q9_ok), strangulation (S2.pain_ok), plain-film markers (S3.film_xA, S3.num_ok), first and definitive test (S3.inv_xX, S3.inv2_xA), coffee bean (S3.coffee_ok), trial timings (S4.c2_ok, S4.c7_ok), femoral and Richter (S5.femoral_ok, S5.richter_ok), intussusception (S5.intus_ok, S5.child_ok), volvulus and right hemicolectomy (S5.sig_ok, S5.caecal_ok), ileus (S4.c8_t31 names neostigmine and potassium first; S4.c10_t31 and S6.q10_f0 for the sound and potassium cues).
- Card 11 is answerable only in part-by-part form: I got the potassium-first step and the neostigmine name from feedback I was shown on wrong answers, not from a correct answer of my own.
- Caveat: "answerable" means the walk taught it. My recall of the card answers was not tested; I got most of the matching questions wrong first time.

## Verdict
- engagement 1–5: 3
- would finish the module: yes
- biggest fix: Cut the repeated re-quiz in S6 and the repeated coffee-bean and claw questions in S5, and replace "Try again, or see why." with a real cue, so the module teaches each idea once and tests it once.

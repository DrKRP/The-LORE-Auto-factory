# Sim: misconceived
path: S1.start (TR1, Sure) → S1.hint_adh → S1.start_b (TR1) → S1.expl_adh → S1.both (TR1, Sure) → S1.expl_same → S1.sort (TR40) → S1.expl_sort_intra → S1.which (TR40) → S1.expl_which_int → S1.virgin (TR2, Sure) → S1.hint_virgin → S1.virgin_b (TR2) → S1.expl_virgin_adh → S1.recap → S2.start (TR17, Sure) → S2.a_h2 → S2.start_b (TR17) → S2.a_x2 → S2.why (TR17, Sure) → S2.why_x1 → S2.snd (TR18, Sure) → S2.snd_h1 → S2.snd_b (TR18) → S2.snd_x1 → S2.ile (TR18) → S2.ile_x1 → S2.pain (TR22, Sure) → S2.pain_h1 → S2.pain_b (TR22) → S2.pain_x1 → S2.cnot (TR22, Sure) → S2.cnot_x1 → S3.film (TR11) → S3.film_hA → S3.film_xA → S3.num (TR12) → S3.num_h6 → S3.num_x6 → S3.film2 → S3.film2_ok → S3.caecum (correct, Sure) → S3.caecum_ok → S3.inv (TR5, Sure) → S3.inv_hX → S3.inv_xX → S3.inv2 (correct) → S3.inv2_ok → S3.inv2c (TR5, Sure) → S3.inv2c_xA → S3.coffee (TR8, Sure) → S3.coffee_hC → S3.coffee_xC → S3.sign (TR8) → S3.sign_xA → S4.c1 (TR31, Sure) → S4.c1_t31 → S4.c1 (correct, Sure) → S4.c1_ok → S4.w2 → S4.c3 (TR22) → S4.c3_t22 → S4.w2b → S4.c3 (correct, Sure) → S4.c3_ok → S4.c2 (TR26) → S4.c2_t26 → S4.c2 (correct) → S4.c2_ok → S4.c4 (correct, Sure) → S4.c4_ok → S4.c5 (TR23) → S4.c5_p → S4.c5 (correct) → S4.c5_ok → S4.c7 (TR26, Sure) → S4.c7_t26 → S4.c7 (correct) → S4.c7_ok → S4.c6 (TR31, Sure) → S4.c6_t31 → S4.c6 (correct, Sure) → S4.c6_ok → S4.c8 (correct, Sure) → S4.c8_ok → S4.c9 (TR23, Sure) → S4.c9_t23 → S4.c9 (correct, Sure) → S4.c9_ok → S4.c10 (correct, Sure) → S4.c10_ok → S5.virgin_case (correct, Sure) → S5.virgin_ok → S5.femoral_case (TR13, Sure) → S5.femoral_h → S5.femoral_f → S5.richter_case (TR14, Sure) → S5.richter_h_full → S5.richter_f_full → S5.littre_case (TR14, Sure) → S5.littre_f_r → S5.maydl_case (TR14, Sure) → S5.maydl_f_wall → S5.intus_case (TR3, Sure) → S5.intus_h → S5.intus_f → S5.intus_why_case (correct, Sure) → S5.intus_why_ok → S5.child_case (TR4, Sure) → S5.child_h → S5.child_f → S5.theatre_case (TR4, Sure) → S5.theatre_h_dx → S5.theatre_f_dx → S5.lbo_case (TR35, Sure) → S5.lbo_h_div → S5.lbo_f_div → S5.sites_case (TR35) → S5.sites_h_caecum → S5.sites_f_caecum → S5.sites_case2 (TR35) → S5.sites_h_sigmoid → S5.sites_f_sigmoid → S5.sig_case (TR21, Sure) → S5.sig_h_discharge → S5.sig_f_discharge → S5.caecal_case (TR36, Sure) → S5.caecal_h_stent → S5.caecal_f_stent → S5.coffee_case (correct, Sure) → S5.coffee_ok → S5.signs_case (correct, Sure) → S5.signs_ok → S6.q1 … S6.q12 (all correct, Sure where asked) → S6.close → END  (158 steps; full list with node, choice index and Sure flag in sim/misconceived.json)

## Friction
- S1.start, S2.start, S2.snd, S2.pain: a trap tap goes to a hint that does not refute. 25 of 59 hints offer only "Try again", and 8 trap options route into that kind of hint. The correction only lands when the same wrong option is tapped again on the re-asked probe. A holder of the belief has to make the same error twice.
- S2.start_b, S2.snd_b, S2.pain_b, S1.virgin_b: "Same high block, asked again" re-asks the identical stem with identical options. It reads as a drill, not a new case.
- S2.a_x1, S2.a_x2, S2.pain_x1, S2.snd_x1: feedback packs three ideas into one message (why the trap tempts, why it fails, a "Right:" clause that gives the answer). I had to re-read it.
- S1.both: one probe asks for two answers at once (PYQ key and current practice). The hook segment also carries relation to the wall, NOT-intramural and the virgin abdomen, so it holds four concepts.
- S4.c1_ok and S4.c3_ok: case order is hard to follow. "On to the next case" from the dry patient goes to the strangulation case (c3), and c3 returns to the simple trial case (c2) before the fever case (c4). I could not see why that order.
- S6.q1 to S6.q12: twelve consecutive quiz probes after every trap was already tested. They re-ask the virgin abdomen, volvulus sites, timings and sign questions from S1, S3, S4 and S5. It reads as a second exam and is dead weight for a learner who already has the answers.
- S1.virgin choice 2 (Crohn's): routes to S1.hint_virgin, which talks about examining the abdomen and never says why Crohn's is wrong. The Crohn's feedback (S1.expl_virgin_crohn) is reached only on the retry.

## Traps
- TR1: offered S1.start (adhesions), refuted at S1.expl_adh and S1.expl_same, retested S6.q1 (correct). FIXED
- TR2: offered S1.virgin (adhesive band), refuted at S1.expl_virgin_adh, retested S5.virgin_case (correct) and S6.q1. FIXED
- TR3: offered S5.intus_case (enema), refuted at S5.intus_f, retested S5.intus_why_case and S6.q11. FIXED
- TR4: offered S5.child_case and S5.theatre_case, refuted at S5.child_f and S5.theatre_f_dx, retested S6.q2. FIXED
- TR5: offered S3.inv (X-ray) and S3.inv2c (enema), refuted at S3.inv_xX and S3.inv2c_xA, retested S3.inv2 and S6.q2. FIXED
- TR8: offered S3.coffee and S3.sign, refuted at S3.coffee_xC and S3.sign_xA, retested S5.coffee_case, S5.signs_case and S6.q5. FIXED
- TR11: offered S3.film, refuted at S3.film_xA, retested S3.film2 and S6.q3. FIXED
- TR12: offered S3.num, refuted at S3.num_x6, retested S3.caecum and S6.q3. FIXED
- TR13: offered S5.femoral_case, refuted at S5.femoral_f, retested S6.q4. FIXED
- TR14: offered S5.richter_case, S5.littre_case and S5.maydl_case, refuted at S5.richter_f_full, S5.littre_f_r and S5.maydl_f_wall, retested S6.q4. FIXED
- TR17: offered S2.start and S2.why, refuted at S2.a_x2 and S2.why_x1, retested S6.q9. FIXED
- TR18: offered S2.snd and S2.ile, refuted at S2.snd_x1 and S2.ile_x1, retested S6.q10. FIXED
- TR21: offered S5.sig_case, refuted at S5.sig_f_discharge, retested S6.q5. FIXED
- TR22: offered S2.pain, S2.cnot and S4.c3, refuted at S2.pain_x1, S2.cnot_x1 and S4.c3_t22, retested S4.c4 and S6.q8. FIXED
- TR23: offered S4.c5 and S4.c9, refuted at S4.c5_p and S4.c9_t23, retested S4.c4 path, S6.q6 and S6.q8. FIXED
- TR26: offered S4.c2 and S4.c7, refuted at S4.c2_t26 and S4.c7_t26, retested S6.q7. FIXED
- TR31: offered S4.c1 and S4.c6, refuted at S4.c1_t31 and S4.c6_t31, retested S4.c8, S4.c10 and S6.q6. FIXED
- TR35: offered S5.lbo_case and S5.sites_case2, refuted at S5.lbo_f_div and S5.sites_f_sigmoid, retested S6.q11. FIXED
- TR36: offered S5.caecal_case, refuted at S5.caecal_f_stent, retested S6.q11. FIXED
- TR40: offered S1.sort and S1.which, refuted at S1.expl_sort_intra and S1.expl_which_int, retested S6.q12. FIXED

Every trap was refuted before it came back, so none survived. Most refutations came after a second wrong tap or a "Show me why" choice, not from the first feedback.

## Report check
- Rendered headline: "weak". Accurate about my starting beliefs: I was overconfident (24 wrong Sure taps), cold_right was 19 of 45, and I used no hints. Not accurate about where I ended. All 20 traps were corrected and answered right on re-test, but the headline still says several core objectives need rebuilding, and O1, O3, O4, O6, O7, O8, O9 and O11 are marked "gap". Texts such as "You are missing strangulation cues" describe my pre-correction state. The traps show "fell_recovered" but do not feed the headline. report_accurate: false.

## Cards
- 11 of 11 answerable from the path. Each card's topic was taught and corrected on the walk: PYQ key versus current practice, the level-based feature timeline, strangulation pain, plain-film markers and the 3-6-9 rule, first and definitive tests, coffee bean, the adhesive trial timings, groin hernias, intussusception, volvulus and colon cancer, and paralytic ileus.
- Holes: none.

## Verdict
- engagement 1–5: 3 (accurate content, but the repetition, retry loops and S6 recap make it long at 158 steps)
- would finish the module: yes
- biggest fix: refute each trap on the first tap (say why it fails, then offer the hint), instead of hint, then re-ask, because a holder of the belief gets no correction until the same wrong answer is tapped twice.

# Sim: strong
path: S1.open → S1.open_ok (skip) → S1.age_a → S1.age_a_ok → S1.age_b → S1.age_b_ok → S2.pain_a → S2.pain_ok (skip) → S2.chain_probe → S2.chain_ok → S2.teach_end → S2.end_probe → S2.end_ok → S2.sym_probe → S2.sym_ok → S2.teach_sym → S2.vig_probe → S2.vig_ok → S2.age_probe → S2.age_ok → S3.case → S3.case_ok → S3.contrast → S3.rov → S3.rov_ok → S3.obt → S3.obt_ok → S3.pos → S3.pos_ok → S3.mech → S3.mech_ok → S3.alv → S3.alv_ok → S3.alv2 → S3.alv2_ok → S3.ttr → S3.ttr_ok → S3.cl → S3.cl_ok → S4.d1 → S4.d1_ok (skip) → S4.c2 → S4.c2_ok → S4.c2b → S4.c2b_ok → S4.c3 → S4.c3_ok → S4.c4 → S4.c4_ok → S4.a1 → S4.a1_ok → S4.a2 → S4.a2_ok → S4.a3 → S4.a3_ok → S4.a6 → S4.a6_ok → S5.p1 → S5.p1_ok → S5.p2 → S5.p2_ok → S5.p3 → S5.p3_ok → S5.p3b → S5.p4 → S5.p4_ok → S5.p5 → S5.p5_ok → S5.p6 → S5.p6_ok → S5.p7 → S5.p7_ok → S5.p8 → S5.p8_ok → S5.p9 → S5.p9_ok → S6.p1 → S6.p1_ok → S6.p2 → S6.p2_ok → S6.p3 → S6.p3_ok → S6.p4 → S6.p4_ok → S6.p5 → S6.p5_ok → S6.p6 → S6.p6_ok → S6.p7 → S6.p7_ok → S6.p8 → S6.p8_ok → S6.p9 → S6.p9_ok → S6.p10 → S6.p10_ok → S6.p11 → S6.p11_ok → S6.p12 → S6.p12_ok → S6.p13 → S6.p13_ok → END  (102 steps)

Walked as the strong persona: answered every probe correctly, said Sure every time, took every skip and fast lane (S1.open_ok, S2.pain_ok, S4.d1_ok). Did not open any "Show me why" or hint. Skipped the worked case (S4.w1) and the first teaching blocks (S1.teach1, S2.teach_pain). Reached END without a loop or dead end.

## Friction
- S2.age_probe: asks the child-vs-adult obstruction question a second time, with the same answer as S1.age_a. A fast learner gets no new step from it.
- S2.end_probe: trap option text is garbled ("Gangrene sets in first, then the lumen blocks, as ischaemia leads"; "as the artery leads"). It reads as a broken sentence, not a plausible wrong belief.
- S4.a1: the stem names no patient group ("investigation of choice for acute appendicitis"). CT is marked correct, and the same feedback then says "Keep the old key too: past papers expected ultrasound". The key contradicts itself. I could not tell whether the module wants the age-less answer to be CT or ultrasound, and I had to pick CT on current-practice grounds. This needs one explicit rule.
- Repetition across the walk, the largest friction for this persona:
  - Adult negative ultrasound does not exclude appendicitis: taught at S4.a1, S4.a2, S4.a3, and again as S6.p6 (four times).
  - Alvarado: S3.alv, S3.alv2, S4.a6, S6.p3. S4.a6_ok repeats the "score of 7 or more makes appendicitis likely" line from S3.alv2_ok word for word.
  - Pregnancy imaging ladder: S4.c3, S4.c4, S6.p7 (three times, S4.c3_ok and S4.c4 are back to back).
  - Beta-hCG first: S4.c2, S4.c2b back to back, then S6.p8.
  - Symptom order: S2.sym_probe, S2.vig_probe, S6.p2.
- S4.c2 and S4.c2b are two probes in a row that teach the same rule. The second adds nothing.
- S5.p6: the stem asks which is NOT a complication of the disease "before any operation". The correct answer is a surgical complication, so the qualifier carries the whole question. Works, but it is easy to misread.
- S6.p5: stem asks "What is wrong with this?" but the correct option states the right sign ("Press the left fossa, and the pain is felt on the right"). It does not name the error.
- S3.ttr_ok: three ideas in one feedback message (the mittelschmerz definition, the three look-alike lists, and "Appendicitis is one item on each list"). The last line is unclear.
- Teaching blocks I skipped: S1.teach1 (the dead-end lane device) and S2.teach_pain. Both are fine to skip for this learner, but S1.teach1 is the only place the module gives the device for the appendix as a lane,; I did not see the device return on this walk.

## Traps
Strong holds no beliefs, so trap status here is "offered and avoided". Every trap in the module was offered on this walk, so no trap is untested on the path:
- TR1 avoided at S3.case, S3.obt, S3.cl, S6.p4
- TR2 avoided at S3.mech, S3.pos, S3.cl, S6.p4
- TR3 avoided at S3.case, S3.rov, S3.obt, S6.p5
- TR4 avoided at S2.pain_a, S2.chain_probe, S2.end_probe, S6.p1
- TR5 avoided at S2.sym_probe, S2.vig_probe, S6.p2
- TR6 avoided at S3.alv, S3.alv2, S6.p3, S4.a6
- TR8 avoided at S4.a2, S4.a3, S6.p6
- TR9 avoided at S4.d1, S4.c3, S4.a1, S6.p7
- TR10 avoided at S4.d1, S4.c3, S4.c4, S4.a1, S6.p7
- TR11 avoided at S4.a1, S4.a2, S4.a3, S6.p6
- TR12 avoided at S4.c2, S4.c2b, S6.p8
- TR13 avoided at S1.open, S1.open_ok, S6.p12, S6.p13
- TR14 avoided at S3.ttr, S6.p8
- TR15 avoided at S1.age_a, S2.age_probe
- TR16 avoided at S5.p6, S5.p7, S6.p11
- TR18 avoided at S5.p8, S6.p11
- TR22 avoided at S5.p1, S5.p9, S6.p9
- TR23 avoided at S5.p1, S5.p2, S6.p9
- TR24 avoided at S5.p4, S6.p10
- TR25 avoided at S5.p3, S5.p5, S6.p10

Caveat: a strong learner avoids traps by knowing the answer, so this run cannot show whether the feedback would fix a misconception. The misconceived sim covers that.

## Report check
- Rendered report (`factory.py render-report`) headline: strong ("You came through with no gaps"). Accurate for this walk: every objective is marked secure, no confident errors, fast lane taken, Sure matched answers. Those match what I did.
- Missed: the report says "you chose the first test by patient" for O7. On S4.a1 I chose CT for a stem with no patient group, so that credit is over-claimed. The report also does not mention the S4.a1 key conflict, or that the same adult-ultrasound point came back four times.
- Count mismatch: `cold_total` is 10 but `card_order` lists 11 cards, and the module has 11 cards. One card is not counted in the cold test.
- Usefulness: "revisit in a week" and "practise mixed-age stems" are reasonable, but for this learner the report gives no reason to slow down or review the repeated content.

## Cards
- 11 of 11 answerable from the path. Each card's topic was taught or tested on this walk: antibiotics-first (S5.p1, p2, p9), mass and abscess (S5.p3, p4, p5), complications and nerve (S5.p7, p8), obstruction-to-gangrene (S2 chain, S6.p1), Alvarado (S3.alv, S3.alv2), psoas/obturator/Rovsing (S3, S6.p4, p5), imaging by group (S4.d1, S4.c3, S4.c4, S6.p7), beta-hCG (S4.c2, S6.p8), carcinoid and the 2 cm rule (S6.p12, p13).
- Caveat on card 9 ("adult: contrast CT"): the walk taught it, but the S4.a1 contradiction means I could not be sure of the answer the module wants for an age-less stem.

## Verdict
- engagement 1–5: 3 (the core path is tight, but the repeated probes and the S4.a1 contradiction would lose a strong learner by the middle of S4)
- would finish the module: yes
- biggest fix: cut the repeats (one adult-ultrasound probe, one Alvarado, one pregnancy ladder, one symptom-order probe, each with a fast lane for someone who already gets it right) and state the age-less answer for S4.a1 explicitly.

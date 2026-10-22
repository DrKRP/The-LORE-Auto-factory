# Sim: misconceived
module: surgery/carcinoma-breast (v1, draft). Walk: S1.gate → END, 178 nodes (177 taps plus END). Notation: (TRn) = trap option tapped, Sure = said Sure.

path: S1.gate (TR4, Sure) → S1.gate_t4 → S1.gate_reveal → S1.re4 (Sure) → S1.re4_ok → S1.tissue (TR1, Sure) → S1.tissue_t1 → S1.tissue_reveal → S1.vig (TR17, Sure) → S1.vig_t17 → S1.vig_reveal → S1.triple → S2.entry (TR10, Sure) → S2.entry_t10 → S2.entry (Sure) → S2.entry_ok → S2.contrast → S2.vign (Sure) → S2.vign_ok → S2.brca_q (TR8, Sure) → S2.brca_t8 → S2.brca_why → S2.brca_q (Sure) → S2.brca_ok → S2.numbers_q (Sure) → S2.numbers_ok → S2.male_q (TR9, Sure) → S2.male_t9 → S2.male_q (Sure) → S2.male_ok → S2.brca_contrast → S2.family_q (Sure) → S2.family_ok → S2.peau_q (TR12, Sure) → S2.peau_t12 → S2.peau_why → S2.peau_q (Sure) → S2.peau_ok → S2.pred_q (Sure) → S2.pred_ok → S3.nipple (TR20, Sure) → S3.nipple_t20 → S3.nipple (Sure) → S3.nipple_ok → S3.skin (Sure) → S3.skin_ok → S3.imaging (Sure) → S3.imaging_ok → S3.mri → S3.tissue (Sure) → S3.tissue_ok → S3.staging (TR5, Sure) → S3.staging_t5 → S3.staging (Sure) → S3.staging_ok → S3.closing (Sure) → S3.closing_ok → S4.t_pair (Sure) → S4.t_pair_ok → S4.t_which (TR13, Sure) → S4.t_which_a → S4.t_which_reveal → S4.t_vig (Sure) → S4.t_vig_ok → S4.t_n (TR2, Sure) → S4.t_n_both → S4.t_n_reveal → S4.t_img (Sure) → S4.t_img_ok → S4.t_prog → S5.r1 (TR3, Sure) → S5.r1_t → S5.r1_e → S5.t1_op (Sure) → S5.t1_ok → S5.r2 (TR14, Sure) → S5.r2_t → S5.r2_e → S5.t2_size (Sure) → S5.t2_ok → S5.r3 (TR27, Sure) → S5.r3_t → S5.r3_e → S5.t3_why (Sure) → S5.t3_ok → S5.r4 (TR15, Sure) → S5.r4_t → S5.r4_e → S5.t4_nerve (Sure) → S5.t4_ok → S6.ls_p1 (TR16, Sure) → S6.ls_p1_t16 → S6.ls_show → S6.ls_p1 (Sure) → S6.ls_p1_ok → S6.ls_w1 → S6.ls_w2 → S6.ls_p2 (Sure) → S6.ls_p2_ok → S6.why_p (Sure) → S6.why_ok → S6.ts_p1 (TR7, Sure) → S6.ts_p1_t7 → S6.ts_show → S6.ts_p1 (Sure) → S6.ts_p1_ok → S6.ts_p2 (Sure) → S6.ts_p2_ok → S6.tt_p1 (TR22, Sure) → S6.tt_p1_t22 → S6.tt_show → S6.tt_p1 (Sure) → S6.tt_p1_ok → S6.tt_p2 (Sure) → S6.tt_p2_ok → S6.tr_p1 (TR6, Sure) → S6.tr_p1_t6 → S6.tr_p1 (Sure) → S6.tr_p1_ok → S6.tr_p2 (Sure) → S6.tr_p2_ok → S6.lc_p1 (TR25, Sure) → S6.lc_p1_t25 → S6.lc_p1 (Sure) → S6.lc_p1_ok → S6.lc_p2 (Sure) → S6.lc_p2_ok → S6.im_a (Sure) → S6.im_a_ok → S6.im_b (Sure) → S6.im_b_ok → S7.p1 (Sure) → S7.p1_ok → S7.p2 (Sure) → S7.p2_ok → S7.p3 (Sure) → S7.p3_ok → S7.p4 (Sure) → S7.p4_ok → S7.p5 (Sure) → S7.p5_ok → S7.p6 (Sure) → S7.p6_ok → S7.p7 (Sure) → S7.p7_ok → S7.p8 (Sure) → S7.p8_ok → S7.p9 (Sure) → S7.p9_ok → S7.p10 (Sure) → S7.p10_ok → S7.p11 (Sure) → S7.p11_ok → S7.p12 (Sure) → S7.p12_ok → S7.p13 (Sure) → S7.p13_ok → S7.p14 (Sure) → S7.p14_ok → S8.tis (Sure) → S8.tis_ok → S8.reg (Sure) → S8.reg_ok → S8.bone (Sure) → S8.bone_ok → S8.cut (Sure) → S8.cut_ok → S8.axil (Sure) → S8.axil_ok → S8.numb (Sure) → S8.numb_ok → S8.tam (Sure) → S8.tam_ok → S8.labc (Sure) → S8.labc_ok → S8.male (Sure) → S8.male_ok → END  (178 steps)

Walk rule used (per persona file): hold a trap until its feedback has been shown on the path; after that answer correctly. Two walk errors were caught and corrected before writing this: at S1.re4 I held the trap after refutation, and at S3.imaging I re-picked a refuted trap. A third error (S4.t_pair_ok leads to S4.t_which, not S4.t_img) was also corrected, and the S4 branch and the S7.p7 and S7.p9 taps were redone. The path above is the corrected walk.

## Friction
- S5.t2_t14: the 'Step 2' trap (shrink to 2 cm, then conserve) is refuted only as 'a loophole around a fixed size rule'. It never says why step 2 is wrong, so a careful learner stays unsure. The correct answer is also a negative claim ('which step is wrong').
- S7.p1 to S7.p14: a 14-probe drill of one shape (question, trap, partial, correct, Next). For a learner who already fixed the beliefs it is about 40 taps that re-ask refuted traps with the same options. Dead weight.
- S7.p5 (and S5.t4_nerve, S7.p11, S7.p14): negative stems ('which is NOT correct') where the 'correct' option is the false statement. Easy to misread on a fast tap.
- S2.entry_t10 (sure note): says 'a common type is not the answer to a question about spread', but the stem asked about the pattern of tissue, not spread.
- S4.t_n_reveal: three ideas in one message (AJCC counts contralateral nodes as M1; older PYQs expected M1 for any supraclavicular node; same-side nodes are N3c). Lost the thread on the first read.
- S3.imaging_why: repeats S3.imaging_ok almost word for word.
- S6.why_show: repeats S6.ls_show word for word (inflammatory order, chemotherapy first).
- S1.re4: the re-test restates the S1.gate cervix-to-breast point after the reveal already gave the answer. It tests the sentence, not a new case.

## Traps
- TR1 (FNAC is the investigation of choice): FIXED. Fell at S1.tissue (Sure), refuted at S1.tissue_t1, shown S1.tissue_reveal. Answered correctly at S3.tissue, S7.p2, S8.tis.
- TR2 (supraclavicular node = M1): FIXED. Fell at S4.t_n (Sure), refuted at S4.t_n_both, shown S4.t_n_reveal. Answered correctly at S7.p7.
- TR3 (Halsted is standard): FIXED. Fell at S5.r1, refuted at S5.r1_t, shown S5.r1_e. Correct at S5.t1_op and S7.p10.
- TR4 (cervix most common): FIXED. Fell at S1.gate, refuted at S1.gate_t4, shown S1.gate_reveal. Correct at S1.re4.
- TR5 (routine bone scan/CT): FIXED. Fell at S3.staging, refuted at S3.staging_t5. Correct at S4.t_img, S6.im_a, S6.im_b, S8.bone.
- TR6 (trastuzumab dose-dependent, irreversible): FIXED. Fell at S6.tr_p1, refuted at S6.tr_p1_t6. Correct at S6.tr_p2 and S7.p11.
- TR7 (tamoxifen for every ER+): FIXED. Fell at S6.ts_p1, refuted at S6.ts_p1_t7. Correct at S6.ts_p2 and S7.p12.
- TR8 (BRCA1 13q, BRCA2 17q): FIXED. Fell at S2.brca_q, refuted at S2.brca_t8, shown S2.brca_why. Correct at S2.brca_q, S2.numbers_q, S7.p5.
- TR9 (BRCA1 male breast cancer): FIXED. Fell at S2.male_q, refuted at S2.male_t9. Correct at S2.family_q and S8.male.
- TR10 (lobular behaves like ductal): FIXED. Fell at S2.entry, refuted at S2.entry_t10. Correct at S2.vign and S7.p4.
- TR12 (peau d'orange = T4d): FIXED. Fell at S2.peau_q, refuted at S2.peau_t12. Correct at S2.pred_q, S3.skin, S4.t_pair, S7.p8.
- TR13 (pectoralis major alone = T4a): FIXED. Fell at S4.t_which, refuted at S4.t_which_a, shown S4.t_which_reveal. Correct at S4.t_vig and S7.p9.
- TR14 (size over 5 cm = no BCS): FIXED. Fell at S5.r2, refuted at S5.r2_t, shown S5.r2_e. Correct at S5.t2_size and S8.cut.
- TR15 (long thoracic most often injured): FIXED. Fell at S5.r4, refuted at S5.r4_t. Correct at S5.t4_nerve and S8.numb.
- TR16 (surgery first in advanced disease): FIXED. Fell at S6.ls_p1, refuted at S6.ls_p1_t16, shown S6.ls_show. Correct at S6.ls_p2, S6.why_p, S8.labc.
- TR17 (mammography first under 35): FIXED. Fell at S1.vig, refuted at S1.vig_t17. Correct at S3.imaging and S8.reg.
- TR20 (carcinoma is the common cause of bloody discharge): FIXED. Fell at S3.nipple, refuted at S3.nipple_t20. Correct at S3.nipple and S7.p3.
- TR22 (tamoxifen protects the endometrium): FIXED. Fell at S6.tt_p1, refuted at S6.tt_p1_t22. Correct at S6.tt_p1, S6.tt_p2, S7.p13, S8.tam.
- TR25 (classic LCIS needs mastectomy): FIXED. Fell at S6.lc_p1, refuted at S6.lc_p1_t25. Correct at S6.lc_p2 and S7.p14.
- TR27 (clear the axilla first, SLNB only if it fails): FIXED. Fell at S5.r3, refuted at S5.r3_t, shown S5.r3_e. Correct at S5.t3_why and S8.axil.

All 20 traps were offered and fell once. Every one was corrected by its feedback, and every one was answered correctly on a later return. Caveat: the later returns are mostly the same question shape with new wording, so they test recognition more than a changed belief. The S7 drill is the bulk of them.

## Report check
- Rendered report (`factory.py render-report`) headline: mixed. Accurate for this walk? Mostly yes. The belief picture is right: 20 trap taps, all 20 with Sure, all 20 recovered, 'overconfident' calibration.
- What it gets wrong or misses:
  - All 12 objectives come out 'shaky'. Nothing is 'secure' or 'gap', so the per-objective list gives no way to prioritise.
  - 'hints: 14' counts my 'Show me why' and 'Explain it to me' taps. I never opened a hint, so the label overstates hint use. The closing line ('Redo the review cards without opening a hint') fits, but 'hints' is the wrong word.
  - The last text says 'Start with the cards for objectives marked gap'. No objective is marked gap, so the instruction points at nothing.
  - 'fell_recovered' is accurate for this path, but it does not say the recovery was tested only by recognition.
- Usefulness: the trap-specific lines ('You moved from the old FNAC key to core biopsy...') are the most useful part. They name the belief I held and the one to check.

## Cards
- 11 of 11 answerable from the path. Holes: none. Each card's content was shown on the path: card 1 (S2.entry_ok, S2.contrast), card 2 (S2.brca_ok), card 3 (S2.male_ok, S2.family_ok), card 4 (S2.peau_ok, S2.pred_ok), card 5 (S1.tissue_reveal, S3.tissue_ok, S1.vig_reveal), card 6 (S3.staging_ok, S4.t_prog, S6.im_b_ok), card 7 (S5.r1_e, S7.p10_ok), card 8 (S5.r3_e, S8.axil_ok), card 9 (S6.ls_p1_ok, S6.why_ok, S8.labc_ok), card 10 (S6.ts_p1_ok, S6.tt_p1_ok), card 11 (S5.r4_ok, S8.numb_ok).

## Verdict
- engagement 1–5: 3. The first half is tight, with a refutation and reason on every trap. Segment 7 is a repeat drill that I would skim.
- would finish the module: yes
- biggest fix: replace the segment 7 drill's repeats of refuted traps with one new-context vignette per trap, and give the S5.t2_t14 'Step 2' refutation its own reason.

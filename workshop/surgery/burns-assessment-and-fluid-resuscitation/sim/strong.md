# Sim: strong
path: S1.gate → S1.gate_ok → S1.final → S1.final_ok → S2.entry → S2.entry_ok → S2.p4 → S2.p4_ok → S2.err_step → S2.err_ok → S2.err_why → S2.err_why_ok → S2.cn_case → S2.cn_ok → S2.co_contrast → S2.co_ok → S3.shock_case → S3.shock_ok → S3.fluid_probe → S3.fluid_ok → S3.colloid_probe → S3.colloid_ok → S3.depth_case → S3.depth_ok → S3.depth_contrast → S3.contrast_ok → S3.cold_check → S3.cold_ok → S4.case → S4.case_ok → S4.close → S4.close_ok → S5.why → S5.why_ok → S5.t1_try → S5.t1_ok → S5.t1_check → S5.t1_c_ok → S5.wx1 → S5.wx2 → S5.wx2_ok → S5.wx3 → S5.wx3_ok → S5.b_try → S5.b_ok → S5.clock → S5.clock_ok → S5.c_try → S5.c_ok → S5.c_seq → S5.c_seq_ok → S5.d_try → S5.d_ok → S5.d_recap → S6.start → S6.start_ok → S6.child_urine → S6.child_ok → S6.electrical → S6.elec_ok → S6.child_tbsa → S6.tb_ok → S6.ambulance → S6.am_ok → S6.drip → S6.drip_ok → S6.contrast → S6.co_ok → S6.tb_vig → S6.tb_vig_ok → S6.escharotomy → S6.esc_ok → S6.mechanism → S6.me_ok → S7.a1 → S7.a1_ok → S7.b1 → S7.b1_ok → S7.hf → S7.hf_ok → S7.spot → S7.spot_ok → S7.q6 → S7.q6_ok → S7.c2 → S7.c2_ok → S7.d1 → S7.d1_ok → S7.cold → S7.cold_ok → S8.p1 → S8.p1_ok → S8.p2 → S8.p2_ok → S8.p3 → S8.p3_ok → S8.p4 → S8.p4_ok → S8.p5 → S8.p5_ok → S8.p6 → S8.p6_ok → S8.p7 → S8.p7_ok → S8.p8 → S8.p8_ok → S8.p9 → S8.p9_ok → S8.p10 → S8.p10_ok → S8.p11 → S8.p11_ok → S8.p12 → S8.p12_ok → S8.close  (115 steps, reached END)
persona note: knows the topic, impatient. Picked the correct option at every probe, said Sure throughout, took every fast-lane skip offered (S1.gate_ok, S2.entry_ok, S4.case_ok, S5/S7 skips), used no hints. Used outside knowledge only to judge whether a correct-answer node was itself accurate.

## Friction
- S5.t1_ok and S5.t1_c_ok: the stem says "as per current ATLS practice" and the node calls about 2 mL current. The next node then says "with no qualifier in the stem, the exam answer stays 4 mL". Inside one node I was told the qualifier changes the answer and that it does not. Not resolved by S5.recap either, which repeats both rules.
- S5.wx1 then S6.start: the worked key is 4 mL (11,200 mL in 24 h, 700 mL/h in the first window is the 2 mL figure). S6.start then calls 700 mL/h "the formula's starting rate" for the same 70 kg 40% adult. Two fluid figures carried through one segment, and I could not tell which one the module carries.
- S5.t1_check: asks the same "current starting figure" question straight after S5.t1_try. Redundant.
- Drills: the deduct-fluid-already-given idea is asked at S5.c_try, S5.c_seq, S6.ambulance and S6.drip. The shock type at S3.shock_case, S5.d_try and S3.cold_check with near-identical vignettes. The airway question at S1.gate, S1.final, S8.p1 and S8.p12. Depth at S3.depth_case and S8.p2. Curling vs Marjolin at S7.q6, S7.c2 and S7.cold. For a strong learner each repeat is a tap I could make without reading.
- Fast-lane skip labels read "Sure of this? Skip ..." on correct-answer nodes. It sounds like the module doubting my confidence, not offering a shortcut. A plain "I know this, skip ahead" would read better.
- The skip targets drop content silently. From S7.a1_ok, "Skip to the topical agents" jumps over S7.q3, so Brooke vs Evans numbers were never shown on my path. From S4.close_ok I never saw the child chart.
- S3.colloid_ok: says Evans and Brooke "both add dextrose in water" in a correct-answer node. A strong learner would question this, and it is not what the node is teaching.
- S3.colloid_probe: the 5% dextrose distractor is labelled TR8 (colloid in first 24 h). Dextrose is not a colloid, so the trap label does not match what the distractor does.
- S2.p7_ok (viewed in the graph, not walked): continues to S2.p4, the CO question already answered if you came through the skip. Not reached on this path, so I cannot say it loops in practice.
- S5.t1_try: "as per current ATLS practice" is an odd source for 2 mL. A strong learner would say ATLS still teaches 4 mL per kg per %TBSA, so the stem reads as contestable.

## Traps
Every trap was offered as a distractor on my path. I took none of them (I am strong), so no trap was refuted in front of me, and none is "fixed" by my walk.
- TR1, TR2, TR3, TR4, TR6, TR8, TR12, TR13, TR14, TR16, TR17, TR18, TR19, TR22, TR23, TR25, TR27, TR29, TR30, TR31: offered-not-taken. Status recorded as offered-not-taken in the JSON. Not a refutation test.
- Note: TR17 (urine high, cut fluid) was offered at S6.start and S8.p9 and I avoided it. TR4 (running drip) was offered at S5.c_seq and S6.drip.

## Report check
- Rendered report (`factory.py render-report`) headline: strong. Calibrated, fast_lane true, hints 0, sure_wrong 0. These match my walk.
- Accurate on what I believed: yes. I was confident, correct, and used the skips.
- Overstated: "TBSA estimation is secure ... switch to child proportions or Lund and Browder". I skipped the child rule-of-nines and never saw the Lund and Browder figures. The text praises a skill the path did not show.
- Missed: the 2 mL vs 4 mL contradiction. Parkland arithmetic is called secure with no caveat, but the one thing I would not call secure is which figure to carry.
- The skip sentence ("the skipped lesson's content is untested for you") is generic. It does not name Brooke vs Evans or the child chart, so the holes do not surface.
- Verdict on the report: accurate for the walk, useful headline, weak on the gap I actually had.

## Cards
- 16 of 18 answerable from the path. Holes:
  - Card 4 (Lund and Browder, head about 18%, each leg about 14%): the chart was named but the figures never appeared on my path.
  - Card 7 (Brooke vs Evans, 1.5+0.5 vs 1+1 per kg per %TBSA): the numbers were skipped with S7.q3.
- Card 11 (escharotomy, "incise through the eschar only"): answerable in outline ("release the eschar"), the "only" qualifier was not taught on my path.
- With outside knowledge (allowed for strong), all 18 are answerable.

## Verdict
- engagement 1–5: 3
- would finish the module: yes (reached END at 115 steps), though the repeats make it a grind for a learner who already knows the topic.
- biggest fix: settle one fluid rule and state it once. A stem qualifier (current or modified) changes the starting figure; the worked key and S6.start must use the same figure, and the stem "as per current ATLS practice" must not key 4 mL. Then cut the repeats so each concept (airway, shock type, depth, Curling vs Marjolin, deduct-given-fluid) is asked once in a new vignette.

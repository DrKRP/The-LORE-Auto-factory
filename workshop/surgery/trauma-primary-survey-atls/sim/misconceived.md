# Sim: misconceived
path: S1.gate (Sure) → S1.gate_t1a → S1.why_gate → S1.rank (Sure) → S1.rank_ok → S1.talk (Sure) → S1.talk_t2a → S1.why_talk → S2.open (Sure) → S2.open_t30 → S2.why_peaks → S2.order (Sure) → S2.order_ok → S2.vignette (Sure) → S2.vignette_ok → S2.close → S3.open (Sure) → S3.p1_ok → S3.teach1 → S3.p2 (Sure) → S3.p2_ok → S3.teach_airway → S3.p3 (Sure) → S3.t22a → S3.why_t22 → S3.teach3 → S3.p4 (Sure) → S3.p4_ok → S4.pair (Sure) → S4.pair_t8 → S4.pair_why → S4.pair (Sure) → S4.pair_ok → S4.tp_next (Sure) → S4.tp_next_t3 → S4.tp_next_why → S4.tp_next (Sure) → S4.tp_next_ok → S4.ppv (Sure) → S4.ppv_t5 → S4.ppv_why → S4.ppv (Sure) → S4.ppv_ok → S4.tp_dx (Sure) → S4.tp_dx_ok → S4.site_adult (Sure) → S4.site_adult_t11a → S4.site_adult_why → S4.site_adult (Sure) → S4.site_adult_ok → S4.site_child (Sure) → S4.site_child_ok → S4.mediast (Sure) → S4.mediast_t16a → S4.mediast_why → S4.mediast (Sure) → S4.mediast_ok → S4.right_pair → S4.right_pair_ok → S4.flail_cause (Sure) → S4.flail_cause_t14 → S4.flail_cause_why → S4.flail_cause (Sure) → S4.flail_cause_ok → S4.flail_mgmt → S4.flail_mgmt_ok → S4.tamp (Sure) → S4.tamp_t7 → S4.tamp_why → S4.tamp (Sure) → S4.tamp_ok → S4.not_list → S4.not_list_t35a → S4.not_list_why → S4.not_list → S4.not_list_ok → S4.circ → S4.circ_ok → S5.case1 → S5.why (Sure) → S5.why_t9 → S5.why_show → S5.fade1 (Sure) → S5.fade1_ok → S5.fade2 (Sure) → S5.fade2_t17 → S5.fade2_show → S5.fade3 (Sure) → S5.fade3_t6a → S5.fade3_show → S5.fade4 (Sure) → S5.fade4_t4a → S5.fade4_show → S5.fade5 (Sure) → S5.fade5_t23a → S5.fade5_show → S6.case → S6.wx → S6.peer (Sure) → S6.peer_t10 → S6.peer (Sure) → S6.peer_t27 → S6.peer (Sure) → S6.peer_ok → S6.cath_why (Sure) → S6.cath_ok → S6.child_air (Sure) → S6.child_ok → S6.site (Sure) → S6.site_ok → S6.site_pair (Sure) → S6.pair_ok → S6.flail (Sure) → S6.flail_ok → S6.brain (Sure) → S6.brain_t18 → S6.brain (Sure) → S6.brain_ok → S6.txa (Sure) → S6.txa_ok → S6.fluid (Sure) → S6.fluid_t10 → S6.fluid (Sure) → S6.fluid_ok → S6.ssurvey (Sure) → S6.ssurvey_ok → S6.cath2 (Sure) → S6.cath2_ok → S7.open → S7.p1 (Sure) → S7.p1_ok → S7.p2 (Sure) → S7.p2_ok → S7.p3 → S7.p3_ok → S7.p4 (Sure) → S7.p4_ok → S7.p5 (Sure) → S7.p5_ok → S7.p6 → S7.p6_ok → S7.p7 → S7.p7_ok → S7.p8 → S7.p8_ok → S7.p9 → S7.p9_ok → S7.p10 → S7.p10_ok → S7.p11 → S7.p11_ok → S7.p12 → S7.p12_ok  (153 steps; Sure marks probe answers I gave as Sure, all others not asked. Full node/choice list in sim/misconceived.json)

## Friction
- S4.not_list: asks which chest injury is NOT one of "the five" before the five are listed; the list only appears in S4.not_list_why after a miss.
- S6.peer_t10: the TR10 correction says older keys printed 2 litres and to check the dose against the edition, but gives no corrected dose and has no "Show me why". The 2 L belief survived it and only changed on the second miss at S6.fluid_t10.
- S4.site_adult_t11a: two exam keys (classic 2nd-space site vs ATLS 10th edition 4th/5th space) with "hold both keys" and no rule for which the exam uses.
- S6.wx: four numbered steps across three messages, two steps packed into one message; hard to hold.
- S6.brain_t18 and S6.peer_t27: wrong-answer feedback has only "Try again", so the reason is one sentence or absent.
- S7.open: says "you can ask for the answer", but no answer control appears on any quiz stem.
- S4.pair_why, S4.tp_next_why, S4.flail_cause_why, S4.mediast_why, S4.site_adult_why: explanations whose only exit is "Try again", returning straight to the same question. Each is a forced retest with no forward move.
- S7 quiz (S7.p1 to S7.p12): most stems re-ask beliefs already corrected earlier, so it reads as repetition more than transfer.

## Traps
- TR1: Sure at S1.gate; refuted at S1.why_gate; correct at S1.rank, S2.order, S2.vignette, S7.p2. FIXED
- TR2: Sure at S1.talk; refuted at S1.why_talk; correct at S3.open, S3.p2, S6.ssurvey, S7.p2. FIXED
- TR3: Sure at S4.tp_next; refuted at S4.tp_next_why; correct at S4.tp_dx, S6.site, S7.p5. FIXED
- TR4: Sure at S5.fade4; refuted at S5.fade4_show; correct at S7.p12. FIXED
- TR5: Sure at S4.ppv; refuted at S4.ppv_why; correct at S7.p5. FIXED
- TR6: Sure at S5.fade3; refuted at S5.fade3_show; correct at S7.p3. FIXED
- TR7: Sure at S4.tamp; refuted at S4.tamp_why; correct at S4.tamp retest, S7.p7, S7.p8. FIXED
- TR8: Sure at S4.pair; refuted at S4.pair_why; correct at S4.pair retest, S7.p8. FIXED
- TR9: Sure at S5.why; refuted at S5.why_show; correct at S5.fade1, S7.p9. FIXED
- TR10: Sure at S6.peer; S6.peer_t10 did not refute it. Sure again at S6.fluid; refuted at S6.fluid_t10; correct at S6.fluid, S7.p9. FIXED, on the second correction only
- TR11: Sure at S4.site_adult; refuted at S4.site_adult_why; correct at S4.site_adult retest, S4.site_child, S6.site, S6.site_pair. FIXED
- TR14: Sure at S4.flail_cause; refuted at S4.flail_cause_why; correct at S4.flail_cause retest, S4.flail_mgmt, S6.flail, S7.p6. FIXED
- TR16: Sure at S4.mediast; refuted at S4.mediast_why; correct at S4.mediast retest, S4.right_pair, S7.p7. FIXED
- TR17: Sure at S5.fade2; refuted at S5.fade2_show; correct at S7.p11. FIXED
- TR18: Sure at S6.brain; refuted only by the "Try again" feedback; correct at S6.brain retest, S7.p10. FIXED (weak correction)
- TR22: Sure at S3.p3; refuted at S3.why_t22; correct at S3.p4, S6.child_air, S7.p4. FIXED
- TR23: Sure at S5.fade5; refuted at S5.fade5_show; correct at S6.cath_why, S6.cath2, S7.p12. FIXED
- TR27: Sure at the S6.peer retry (second visit); refuted at S6.peer_t27 ("Try again" only); correct at the S6.peer retest, S6.txa, S7.p9. FIXED (weak correction)
- TR30: Sure at S2.open; refuted at S2.why_peaks; correct at S2.vignette, S7.p1. FIXED
- TR35: Sure at S4.not_list; refuted at S4.not_list_why; correct at the S4.not_list retest, S4.circ, S7.p6. FIXED

Caveat: I changed belief after one explanation or one clear refutation each time, so all 20 read as fixed. This is an upper bound. A misconceived learner who only taps Try again would probably hold several of these, and this walk cannot show that.

## Report check
- Rendered report (`factory.py render-report`) headline: mixed. Accurate for this walk? no. The headline and every objective "shaky" is harsher than what I took away: all 20 traps recovered and the 9 cold quiz stems were all correct, but no text mentions the 9/9 result.
- TR27 is reported "avoided". I fell into it on the retry at S6.peer with Sure. The report reads only first encounters per probe, so retries are invisible.
- "hints: 17" counts "Show me why" taps as hints. I never tapped a hint option.
- Accurate: calibration "overconfident" with 19 sure-wrong; the "You first X, then changed" trap texts match my path.

## Cards
- 9 of 9 answerable from the path. Card 1 (order), 2 (talking patient), 3 (airway by age), 4 (tension site), 5 (chest contrasts), 6 (shock class and qualifiers), 7 (fluid and brain target), 8 (FAST and urethrogram), 9 (TXA window). No holes.

## Verdict
- engagement 1–5: 3
- would finish the module: yes
- biggest fix: Put the corrected fact in the wrong-answer line itself (S6.peer_t10 gives no dose; S6.brain_t18 and S6.peer_t27 have no "Show me why"), so a Sure misconception is refuted on the first miss.

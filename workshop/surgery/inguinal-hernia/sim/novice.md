# Sim: novice
path: S1.hook → S1.hook_help (hint) → S1.hook (Indirect, Guessing) → S1.explain_route → S1.deep_ring → S1.retest_route → S1.femoral_probe → S1.tim_probe (trap TR5, Guessing) → S1.tim_t_fem → S1.tim_probe (correct) → S1.close_s1 → S2.route_predict (trap TR1) → S2.route_t1 → S2.route_predict (correct) → S2.observe_triangle → S2.tri_probe (trap TR2, Cooper's) → S2.tri_t2a → S2.tri_probe2 (hint) → S2.tri_help2 → S2.tri_probe2 (correct) → S2.conj_probe (trap TR28) → S2.conj_t28a → S2.conj_probe (correct) → S2.cause_predict → S2.pic_probe (trap TR23) → S2.pic_t23a → S2.pic_probe (correct) → S2.final_probe (trap TR1) → S2.final_t1 → S2.final_probe (correct) → S3 (predict, start, occlusion, route, lap, zieman by hint, tr31, contrast, tr40, wall, wall2) → S4 (a, b, f, c1, c2, d1–d4, e1, e2) → S5 (emerg, taxis, child, adult, ex2, lap, nerve, lfcn, tri, occ, tdef, tmesh) → S6 (p1–p12, recap) → END

(182 steps. Guessing on every probe, Sure never tapped. Hints used on S1.hook, S2.tri_probe2, S3.zieman, and a few more. Reached END.)

## Friction
- S1.hook: "Go with your first instinct" is followed by a hint button on the same node. The novice is told to guess and given help in the same breath.
- S1.tim_probe, S4.c1_probe, S4.c2_probe: the same "which hernia is most common in women" question comes back three times with near-identical stems. I had already answered it in S1, so it felt like drilling.
- S3.route, S1.retest_route, S1.hook: the same vessel-side question is asked three times, all in different wording but with the same answer.
- S3.wall then S3.wall2 (one node later): the same posterior-wall conjoint question, nearly word for word.
- S4.d1_probe and S5.emerg: the same tense-groin first-action question. S4.d2_probe and S5.taxis_why: the same "why avoid taxis" question. Each repeat landed after I had already answered it.
- S5.tdef, S5.tmesh and S6.p9: herniotomy, herniorrhaphy and hernioplasty are asked three times. S5.lap repeats the laparoscopic-qualifier explanation from S5.adult_t1 almost word for word.
- S2.tri_t2a, S2.conj_t28a, S2.pic_t23a: "Show me why" on a trap jumps to the next probe and skips the explanation of the thing I got wrong. The learner is left without the lesson they asked for.
- S2.observe_triangle: "Device:" is a heading I could not parse.
- "exam keys" is used as if known, in S2.tri_t2a, S2.tri_ok, S5.adult_t2 and S6.p1ok. A novice does not know what it refers to.
- S5.adult_t1 and S5.nerve_t1: a rhetorical question ("Which detail here is about the surgeon?", "Does the approach change where the dissection runs?") is asked in feedback with no answer slot. It reads as if I should answer it.
- S6.p1: the intro says "the last six give no hints", but the probe still has "Not sure, give me a hint".
- S6.p2ok calls the ring finger Zieman's "femoral site". S3.zieman_ok said it was the "saphenous opening". I read both, and they disagree.
- S3.contrast: no Sure/Guess question and no hint option, unlike the probes around it.
- S6.recap: three short lines, then END. There is no pointer to what I got wrong or where to revisit it.

## Traps
(The novice persona does not hold traps as beliefs, so these are the ones I met and how I came out of each.)
- TR1 (direct/indirect by vessel side): fell at S2.route_predict and at S2.final_probe. Corrected on Try again each time, but never retested on a fresh question after the second fall.
- TR2 (triangle boundaries, Cooper's): fell at S2.tri_probe and S2.tri_probe2. Corrected after the hint.
- TR5 (sex and type): fell at S1.tim_probe. Corrected on Try again.
- TR7 (adult repair for a child): fell at S5.child. Corrected on Try again.
- TR8 (direct more likely to strangulate): fell at S4.b_probe and S6.p4. Corrected.
- TR9 (indirect for groin strangulation): fell at S4.a_probe. Corrected.
- TR11 (taxis in strangulation): fell at S4.d1 and S4.d2. Corrected at S5.taxis_why.
- TR12 (imaging choice): fell at S4.d3, S5.occ and S5.ex2. Corrected each time.
- TR14 (nerve by approach): fell at S5.nerve. Corrected on Try again.
- TR16 (laparoscopy for everything): fell at S5.adult and S6.p7. The second fall was resolved with Show me the answer, so it did not come back on my own.
- TR17 (Bassini): fell at S6.p8. Corrected on Try again.
- TR21 (occlusion test): fell at S3.predict, S3.occl_v and S6.p3. The last one was resolved with Show me the answer.
- TR23, TR25, TR28, TR34, TR39, TR40: each fell at least once and was corrected on retry or with an explanation.
- TR22, TR31: offered, not chosen.

## Report check
- Rendered report (`factory.py render-report`) headline: weak. Accurate for the first attempts: the Hesselbach and inguinal-vs-femoral gaps, the underconfident calibration, the guess and hint counts, and the card order all match my path.
- Harsher than my experience. The report counts only each probe's first answer. Where I fell and then got the same probe right on Try again (TR1, TR2, TR12, TR14, TR21 at S3.occl), it still says the trap "fell open". That follows the by-design rule ("fixed on the spot, not shown to hold"), but the report never says I corrected it on the spot, so "weak" overstates what I still lack.
- It does not mention the repeated questions, which were my main friction.
- Verdict on the report: accurate about what was recorded, but not a fair picture of a learner who got most items on the second try.

## Cards
- 15 of 15 answerable from the path, but card 11 (TEP/TAPP) and card 13 (child herniotomy) rest on one or two passing mentions, and most answers were reached on a retry. Lower confidence than the count suggests.
- Holes: none that I could find.

## Verdict
- engagement 1–5: 3
- would finish the module: yes
- biggest fix: cut the repeats. The same vessel-side, sex-and-type, taxis, conjoint, and classification questions return 2–4 times with near-identical stems, so a novice feels drilled rather than taught. Keep one teach and one fresh-form retest per idea.

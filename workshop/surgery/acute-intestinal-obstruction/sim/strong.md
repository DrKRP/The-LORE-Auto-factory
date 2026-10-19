# Sim: strong
path: S1.start → S1.ok_key → S1.both → S1.ok_both → (skip) S1.which → S1.ok_which → S1.virgin → S1.ok_virgin → S1.recap → S2.start → S2.a_ok → (skip) S2.pain → … → S6.summary → S6.summary_ok → END (117 steps: 116 choice steps plus END)

Every probe answered correctly and Sure. The path took the three skip options offered (S1.ok_both, S2.a_ok, S4.c1_ok) and never opened a hint. Traps were offered on many probes and avoided; the strong persona does not measure traps, so `traps` is left empty.

## Friction
- S1.ok_both: the "I know the wall sort, skip it" fast lane leads to S1.which, which is the wall-sort question it says to skip. A skip that lands on the content it skips is a bug, not a pace choice.
- S3.inv2: three questions (first test, definitive test, child's test) in one message, followed by a "which ladder" choice. Lost the thread on a first read.
- S3.sign_end: a recap that repeats S3.sign_ok and S3.inv2_ok almost word for word. Reads as padding to a strong learner.
- S6 cold check: not cold. The coffee-bean, Richter's, femoral hernia, sigmoid volvulus, caecal cancer and intussusception questions were answered in S3/S5 and come back in S6 with near-identical wording, minutes later. By the third time (S3.coffee, S5.coffee_case, S6.coffee) I was bored and was only matching.
- S1.ok_key and similar correct feedback: the Sure answer gets no confirmation. Sure-related feedback only appears on wrong answers (hint nodes), so a strong learner never sees what calibration looks like.
- END: "the cards that follow" and the report are promised, but nothing on the path points to them before END.

## Traps
- Offered and avoided (not a persona measure): TR1, TR2, TR3, TR4, TR5, TR8, TR11, TR12, TR13, TR14, TR17, TR18, TR21, TR22, TR23, TR26, TR31, TR35, TR36, TR40. Not tested for beliefs on this path.

## Report check
- Rendered report (`factory.py render-report`) headline: "strong". Calibrated; fast_lane true; all 12 objectives secure; cold_right 42 of 42.
- Accurate about what I did: yes for the answers, Sure, fast lanes and calibration.
- Missed or overstated: "cold" 42/42 is inflated. These are repeats of items I had just answered, so the report reads them as retention when they are not. The text "you derived the cardinal features from the level rather than recalling a table" credits a reasoning style the walk never showed; I was choosing from options. The rest of the text is fair.
- Verdict on report: report_accurate false. Its headline is right, but the retention claim is not.

## Cards
- 11 of 11 answerable from the path. The PYQ-versus-current-practice card was taught at S1 and S6.pyq; the other ten each have a probe on the path. Retention was never tested at a real gap, so this is answerability, not durable recall.

## Verdict
- engagement 1–5: 4 (correct and quick, but the S6 repeats pulled it down)
- would finish the module: yes
- biggest fix: cut the S6 cold check to vignettes not used in S3 or S5 (or move it to a card return), because a strong learner meets the same questions three times in one sitting.

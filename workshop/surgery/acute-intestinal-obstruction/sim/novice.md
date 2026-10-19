# Sim: novice
path: S1.start → S1.hint_adh → S1.start_b → S1.expl_adh → S1.both → S1.ok_both → S1.sort → S1.expl_sort_intra → S1.which → S1.expl_which_ca → S1.virgin → S1.hint_virgin → S1.virgin_b → S1.expl_virgin_adh → S1.recap → S2.start → … → S6.summary_ok → END  (197 steps, Guessing on every confidence prompt)

Persona behaviour: picks the most familiar-sounding option (adhesions, the 72-hour trial, enema for intussusception, colic as simple obstruction), takes hints and "Show me why" when stuck, never says Sure.

## Friction
- S1.expl_virgin_adh: after two wrong picks on the virgin-abdomen case the walk returns to recap without stating the answer. I left knowing "adhesions are unlikely" but not what to pick.
- S1.recap: three ideas in two messages (PYQ columns, wall sort, orifices).
- S2.start: the level idea needed a re-read before the question made sense.
- S3.inv2: "a ladder for three questions" in one stem. I read it twice.
- S3.sign_end: a closing recap of four tests and six signs in one message. It reads as a list to memorise, not a takeaway.
- S4.w2: "Step two" with no step one shown. The worked case starts mid-way.
- S4.c5_h: "Sort each option" does not say what to sort by. Too thin after a guess.
- S5.theatre_h_pain: "ask which finding is more than the usual presentation" is vague. I did not know what to look for.
- S5.sig_f_discharge, S5.coffee_f_caecal and others: "Wrong model:" opens the feedback. Jargon that reads as a code word, used about six times.
- S5.coffee_case: near-verbatim repeat of S3.coffee (coffee bean, pelvis, sigmoid versus caecal).
- S6 (about 50 probes): restates S1 to S5 almost item for item (Richter, femoral, coffee bean, intussusception, sigmoid, caecal, timing). No new content. This is where I got bored and started clicking Next.
- S6.why: "You just named strangulation" but I was never asked to name it on this path.
- S6.summary_t1: the hint says "pick the line that puts screening first", which does not address the setting trap.

## Traps
Traps I met on this path (20 of 20 in `module.json`). Status is the walk's outcome: "fixed" means I answered the same node correctly on a retry or later re-test; "refuted-not-retested" means feedback refuted me and the path never offered it again; "survived" means I picked it again after refutation.
- TR1: survived. Picked adhesions on the PYQ stem, then again on the retry at S1.start_b. The module later gave a correct PYQ answer at S1.both, but never re-offered TR1.
- TR2: fixed. Picked adhesive band for the virgin abdomen at S1.virgin and again at S1.virgin_b. Recovered at S5.virgin_case after a hint.
- TR3: fixed. Picked enema reduction for an adult at S5.intus_case, retried, correct. Then picked "adult bowel wall too thick" at S5.intus_why_case (refuted, not retested).
- TR4: fixed at S5.child_case after a retry.
- TR5: fixed at S3.inv after a retry.
- TR8: fixed at S3.coffee and S5.coffee_case after retries. Sign-swap trap S3.sign picked and refuted, not retested.
- TR11: fixed at S3.film after a hint.
- TR12: fixed at S3.num and S3.caecum after hints.
- TR13: fixed at S5.femoral_case after a hint.
- TR14: fixed at S5.richter_case after a hint. Maydl trap at S5.maydl_case refuted, not retested.
- TR17: refuted-not-retested. Picked constipation-as-early at S2.why and read the feedback, but S2.why_x1 led straight to Next.
- TR18: fixed at S2.snd after a retry. Silent-bowel trap at S2.ile and S6.silent refuted without a retest.
- TR21: refuted-not-retested. Picked detorsion then discharge at S5.sig_case and S6.sig. Feedback refuted it each time, nothing re-tested it.
- TR22: fixed at S2.pain after a hint and retry.
- TR23: fixed at S4.c3 after a hint and retry.
- TR26: fixed at S4.c2 after a retry; timing trap at S6.timing refuted, then not retested.
- TR31: fixed at S4.c1 after a retry.
- TR35: refuted-not-retested. Picked sigmoid volvulus as commonest cause at S6.large; correct at S5.lbo_case first time.
- TR36: fixed at S5.caecal_case after a hint.
- TR40: refuted-not-retested. Picked intramural at S1.sort and carcinoma as intramural-not at S1.which. Adhesive band trap at S6.wall also refuted, not retested.

## Report check
- Rendered report (`factory.py render-report`) headline: "weak". Accurate: yes. I guessed through most probes and got 4 of 47 cold probes right first time, which matches "weak".
- Calibration "underconfident": accurate. I was right 8 times on Guessing, and never said Sure, so it reads as underconfident. The report should say that calibration is not measurable without Sure answers.
- Traps: 19 of 20 show "fell_open". This under-credits me. TR3, TR4, TR5, TR8, TR11, TR12, TR13, TR14, TR17, TR18, TR22, TR23, TR26, TR31 and TR36 were all answered correctly on a retry at the same node, and the report does not count it as recovery. Only TR2 shows "fell_recovered", because that trap was re-offered on a later segment. The report is accurate about first encounters but misses the in-node recoveries, which is most of what the walk taught.
- Hints: "1". Accurate only as a count of "Not sure, give me a hint" taps. I read roughly 25 hint and "Show me why" messages through retries, and the report counts none of them. Misses what the learner actually needed.
- Objectives: all 12 shown as "gap". Harsh but matches the cold-correct rate. Not wrong for this path, but it does not separate "never got it" from "got it on a retry".
- Texts: "Start with the review cards... in the order shown" is practical. The end text ("Redo the module in a week") is sensible.

## Cards
- 11 of 11 answerable from the path. Each card's topic was taught at least once in S1 to S6, sometimes twice. Holes: none on the path. Caveat: the Richter and Littre cards were answered from S5 rather than S6, and I got both wrong first time.
## Verdict
- engagement 1–5: 3
- would finish the module: yes, but only because I could see the end; S6 was a slog
- biggest fix: cut S6 (about 50 probes re-asking S1 to S5) to a short mixed quiz of 8 to 10 items, and state the answer after any second wrong pick.

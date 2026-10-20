# Sim: guesser
path: S1.open → S1.open_t1 → S1.open_2 → S1.open_x2 → S1.teach1 → S1.age_a → … → S6.p13 → S6.p13_ok → END  (193 steps; all probes answered Guessing, Why? never opened)

## Friction
- S4.d1_t9 and S4.c2_t12: a wrong choice gets a "hint"-style node ("Tempting: … look again") that never says the choice is wrong. I could not tell I had been wrong, so I just clicked Try again.
- The age rule (S1.age_a/b, S2.age_probe), the negative-ultrasound rule (S4.a2, S4.a3, S6.p6), the Alvarado score (S3.alv2, S4.a6, S6.p3) and beta-hCG (S4.c2, S4.c2b, S6.p8) each come up 2-3 times with near-identical wording. For a fast clicker that is dead weight after the first.
- S5.p6: "Which of these is NOT a complication of acute appendicitis itself, before any operation?" is a double negative. I re-read it and still guessed.
- Wrong-answer feedback often restates the correct answer in full (S6.p2, S5.p9), so the retry is answered by reading the feedback, not by thinking.
- The mechanism chain (S2) is only checked by probes; I never took "Show me why", so the explanation nodes were skipped by my path.

## Traps
- Traps met (guesser does not hold beliefs, so no FIXED/SURVIVED status): TR1, TR2, TR3, TR4, TR5, TR6, TR8, TR9, TR10, TR11, TR12, TR13, TR14, TR15, TR16, TR18, TR22, TR23, TR24, TR25. I fell for most on first try and got the right answer on Try again.
- Not met on this path: TR7, TR17, TR19, TR20, TR21.

## Report check
- Rendered report (`factory.py render-report`) headline: weak. Accurate for this walk? No, mostly. It is right that I fell on many first tries and that my calibration was underconfident (I guessed and was often right). It misses that I corrected most on Try again. Its trap statuses (fell_open for TR1, TR3, TR4) and objective gaps are built from first-attempt answers only, so they overstate what I left with.

## Cards
- 11 of 11 answerable from the path, with low confidence. No coverage holes: each card's topic had a probe and feedback on my path (antibiotics-first, mass, interval surgery, abscess, complications, Murphy's order, Alvarado, psoas/obturator/Rovsing, imaging by group, beta-hCG, carcinoid size).

## Verdict
- engagement 1–5: 3
- would finish the module: yes
- biggest fix: Say plainly 'That is not right' on every trap feedback, and collapse the repeated age, negative-ultrasound, Alvarado and beta-hCG probes so a fast clicker meets each rule once, plus a test that asks for the rule after the second miss instead of the third.

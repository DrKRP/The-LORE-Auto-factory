# Sim: novice
path: S1.open → S1.open_hint → S1.open_2 → S1.open_x1 → S1.teach1 → S1.age_a → … → S5.p9 → S6.p1 → … → S6.p12_ok → END  (198 steps; every probe answered as Guessing; no Sure taps)

Walk style: I picked the most intuitive option first ("most common" read as "most serious", vomiting first, RIF pain as appendicitis, CT first everywhere). I used retry after most traps and took the hint on the first probe. Feedback nodes were read only as the Guessing path shows them (no sure_note).

## Friction
- S1.open_2 and every `*_2` retry node: "Same question, one more look" re-asks the identical stem with identical options and no new teaching. As a novice I could only pick by position or guess again. The retry carries no new information.
- S3.alv: the Alvarado (MANTRELS) probe is asked cold before any table has been shown on this path. The mnemonic is not explained.
- S2.sym_probe: "Murphy's sequence" is named in the question with no definition, so I could not tell what was being asked.
- S4.d1: the first imaging probe is asked cold. Nothing on the path taught imaging choice before the question.
- S3.ttr_ok: look-alike lists for children, women and adults arrive in one long message. I lost the thread after the second list.
- S3.ttr: mittelschmerz is offered as an answer before it has been taught on this path (only the probe's correct answer names it).
- Repetition, dead weight: S2.age_probe repeats the S1 age-cause lesson; S4.c4 repeats S4.c3 nearly verbatim; S4.a5 repeats the S3.alv2 vignette and answer; S6.p3 repeats it a third time. S4.a2 and S4.a3 teach the same point back to back. Felt like padding by the S4 block.
- S6.p12_ok: the path ends on one carcinoid probe. The PYQ size rule (under 2 cm / over 2 cm) arrives as one sentence in the last feedback, with no recap or closing message.
- Hint escalation: S5.p5_h ("drainable collection… least invasive route") nearly gives the answer, so the retry after the hint is trivial.

## Traps
Novice has no trap list to close, so I record the ones I met (first attempt in brackets):
- TR13 (S1.open_2): read "most common" as severity. Corrected by S1.open_x1 teaching, held on re-ask. Recovered.
- TR15 (S1.age_a, S1.age_b, S2.adult_probe): age-blind cause. Met three times, corrected on retry, held at the adult probe.
- TR4 (S2.pain_a, S2.chain_probe): pain pathway and causal chain reversed. Corrected on retry at the chain probe.
- TR5 (S2.sym_probe): vomiting before pain. Corrected on retry.
- TR1, TR2, TR3 (S3.case, S3.obt, S3.rov, S3.pos, S3.mech): psoas/obturator/Rovsing confusions. Corrected on retry each time.
- TR6 (S3.alv, S3.alv2, S4.a5): Alvarado weights. Corrected on retry, met again at S4.a5.
- TR8, TR9, TR10, TR11 (S4.a2, S4.d1, S4.c3/c4, S4.a1): imaging ladder by group and old key. Corrected on retry.
- TR12 (S4.c2, S4.c2b): imaging before beta-hCG. Corrected on retry.
- TR14 (S3.ttr): RIF pain equals appendicitis. Corrected on retry.
- TR16 (S5.p6): peritonitis listed as operative. Corrected on retry.
- TR18 (S5.p8, S6.p11): femoral versus ilioinguinal. Corrected on retry.
- TR22, TR23 (S5.p1, S5.p2, S5.p9, S6.p9): "only treatment" and antibiotics for every case. Corrected on retry.
- TR24 (S5.p4): routine interval surgery. Corrected on retry.
- TR25 (S5.p3): emergency appendicectomy for a settled mass. Corrected on retry.
Every met trap was corrected on the same stem. None was re-tested later in another segment except TR13, TR15 and TR6.

## Report check
- Rendered report (`factory.py render-report`) headline: **weak**. Calibration: underconfident (18 Guessing answers were right; 0 Sure-wrong).
- Accurate for this walk? Mostly yes. Every trap I fell into is named, the confusions I made are the ones it describes (psoas/obturator, Rovsing reversed, gridiron nerve, old key versus current practice), and the "guessing when right" note fits the path.
- What it missed or overstated:
  1. The headline "weak" and objectives O3 to O11 all marked "gap" come from first attempts only. I answered most of those probes correctly after one retry and finished the walk with near-complete answers. The report does not credit that. A learner who reads "weak" would think they had learned nothing.
  2. Traps are all "fell_open" except TR13 and TR15. That is the rule (no later correct on another node), but it treats an immediate retry on the same stem as no recovery. Reasonable, but I would have liked to see "corrected on retry" as a distinct state.
  3. Card order starts with pathophysiology, which matches the walk's largest first-attempt errors, so it is useful.
- Net: accurate about what I believed, harsher than my walk warrants on the overall headline.

## Cards
- 11 of 11 answerable from the path. Note: card 11 (carcinoid size rule) was delivered once in a closing feedback sentence and was not practised, so it is the thinnest. Card 6 (order of events) was answerable but only after two retries.
- Holes: none found.

## Verdict
- engagement 1–5: 3
- would finish the module: yes (I reached the end), but I would expect drop-off in the S4 block, where the repeats start.
- biggest fix: replace "Same question, one more look" with a one-line teaching reminder, and cut the repeat probes (S2.age_probe, S4.c4, S4.a5, S6.p3) so retries carry new information.

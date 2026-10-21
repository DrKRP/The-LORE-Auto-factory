# Sim: guesser
path: S1.gate → S1.gate_t30 (Try again) → S1.gate → S1.gate_ok → S1.intub → S1.intub_ok → S1.final → S1.final_t30 → S1.final → S1.final_ok → S2.entry → S2.entry_t12x → S2.entry → S2.entry_ok → S2.worked → S2.p7 → … → S8.p2 → S8.p2_t0 → S8.p2 → S8.p2_ok → S8.p3 (cap)  (220 steps; end node not reached)

Every probe answered "Guessing". Clicked the first plausible option, took "Try again" after each wrong answer, never opened "Why?" or "Show me" except where it was the only way forward. One skip used (S7.d1_ok, "Skip to the final check"). Full path with choice indices is in `guesser.json`; every transition was checked against the module's `next` fields.

## Friction
- S5.t1_c_ok: contradicts the rule given two nodes earlier. It says current practice starts at 2 mL, then says that with no qualifier in the stem "the exam answer stays 4 mL, so the next steps use the 4 mL key". I could not tell which number to use. The recap at S5.d_recap sides with the 4 mL key, which makes it worse.
- S5.t1_c_t1: "That is not right" with no correct figure and only a Try again. Guessing became the only strategy.
- S5.wx2_part: a partial answer is labelled "not right"; "350 mL/h … belongs to the other window" is opaque.
- S6.me_partial: partial answer treated the same way, with only Try again or Show me the answer.
- S3.colloid_t8d: the wrong option is explained by which formula owns it, not why it fails this stem.
- S2.entry: the vignette is nearly the same as S1.gate (40-year-old, fire, hoarse voice), so it reads as a repeat.
- Repeats: S6.drip repeats S5.c_seq (subtract fluid already given); S6.tb_vig repeats S4.child_q (age-based chart for a 2-year-old); S5.d_try repeats S3.shock_case (shock type at 6 hours).
- S5.wx1 to S5.d_recap is about 40 arithmetic clicks with many retries and no change of pace.
- Feedback choice order is inconsistent: S3.shock_septic lists "Show me why" before "Try again"; most trap nodes put Try again first.
- The 220-step cap was reached at S8.p2 with about 10 more probes in S8 before the end. The walk was not looping; it was long.

## Traps
Mapped by content from the trap text in `module.json`; the guesser has no trap list of its own. Each trap met was refuted on the spot, and I answered it correctly on the retry unless noted.
- TR1 (Parkland 4 mL always): met at S5.t1_tr1 and S5.t1_c_t1, and again at S7.a2_t2. Refuted and retried correctly, but the S5.t1_c_ok line then restores the 4 mL key for an unqualified stem. REFUTED, NOT CLEAR.
- TR2 (8 h counted from arrival): met at S5.b_tr2. FIXED.
- TR4 (pre-hospital fluid not deducted): met at S5.c_tr4. FIXED.
- TR6 (adult rule of nines for a child): met at S4.child_t_adult and S4.child_num_t45. FIXED.
- TR8 (colloid on day one, or Parkland confused with Brooke/Evans): met at S3.fluid_t8, S3.colloid_t8, S7.a1_t0. FIXED.
- TR12 (chest film or ABG as the inhalation test): met at S2.entry_t12x and S2.p7_t12b. FIXED.
- TR13 (SpO2 as reassurance for CO): met at S2.p4_t13b. FIXED.
- TR23 (escharotomy for any deep burn): met at S6.es_t_partial and S7.d1_t1. FIXED.
- TR25 (topical agent paired with wrong side effect): met at S7.b1_t0 and S7.b2_t1. FIXED.
- TR27 (antidote paired with wrong poison): met at S2.cn_t27a and S2.co_t27a. FIXED.
- TR30 (intubate only after failure): met at S1.gate_t30 and S1.final_t30. FIXED.
- TR31 (burn shock called septic or cardiogenic): met at S3.shock_septic and S5.d_t31b. FIXED.
- Not offered on this path: TR3, TR14, TR16–TR19, TR22, TR29 (S1.gate_t29 was on offer but I did not tap it).

## Report check
- Rendered report (`factory.py render-report`) headline: weak. The aggregate picture is fair for a guesser: first-try misses across most objectives, no hints, one skip, no Sure answers. But the report does not separate what I corrected on the retry from what I never fixed.
- Trap statuses are wrong: every trap is "fell_open", including TR3, TR14, TR16–TR19, TR22 and TR29, which this walk never offered. That is a report bug, not a finding about me.
- Objectives are all "gap", including depth grading and urine targets where I got the retry right. The per-trap texts say "not on a later question" for all of them, which is not true for the ideas that came back.
- Texts that fit me: the arrival-clock and team-clock slips (`S5.b_tr2`, `S5.clock_t2a`), "Burn numbers before ABCDE", "wait for stridor", the no-hints note, and the skip note.
- Report accurate for this walk: no. Details in `guesser.json` under `report_note`.

## Cards
- 16 of 18 answerable from the path.
- Partial: card 1 (adult urine target) and card 16 (adult urine target again). The adult 30–50 mL/h figure only appeared as a distractor label, never as a correct answer on this walk. The child and electrical targets were taught.
- All others were taught on the path, including escharotomy (S6.esc_ok and S7.d1_ok), the Parkland clock (S5.clock_ok), the TBSA chart (S4.case_ok, S4.child_num_ok), the topical and antidote pairs, and the Curling/Marjolin split.

## Verdict
- engagement 1–5: 3. The content is clear and the retry-and-correct loop works, but the S5 arithmetic stretch is long, repetitive, and contradicts itself on the 2 mL / 4 mL rule.
- would finish the module: no as walked. The walk hit the 220-step cap before the end, and a guesser who clicks fast but retries a lot would probably drop out somewhere in S5 or S6.
- biggest fix: make the fluid rule consistent. S5.t1_c_ok must not say the exam answer stays 4 mL without a qualifier when S5.t1_ok and S5.d_recap say 2 mL is current practice. State one rule (4 mL key unless the stem says modified or current) and use it in S5.t1_ok, S5.t1_c_ok and S5.d_recap.

# Sim: guesser
path: S1.start → S1.hint_adh → S1.start_b → S1.ok_key → S1.both → S1.expl_same → S1.sort → … → S6.summary → S6.summary_ok → END  (202 steps, END included)

Persona: clicks fast, reads little, picks among plausible options, rarely opens "Why?" or hints. Walk used index 0 on about half of the probes (fast clicking), skipped worked-explanation "Show me why" links, and took fast lanes where offered (S2.a_ok skip).

## Friction
- S1.expl_sort_intra: learner-facing claim codes (K19, K20, K22) in feedback text; no meaning for a learner.
- S1.ok_key: "I know the wall sort, skip it" uses "wall sort" before it is defined (defined later at S1.sort).
- S2.pain, S4.c3, S4.c4, S6.adh: the same constant-pain-with-tachycardia strangulation picture asked four times in different wording.
- S3.coffee, S5.coffee_case, S6.coffee: coffee-bean sign asked three times with the same three options.
- S5.femoral_case and S6.femoral: which groin hernia strangulates asked twice.
- S5.sig_case and S6.sig: sigmoid volvulus management asked twice with the same trap.
- S6 "Cold check and summary" (104 nodes): re-asks about 60 questions already answered in S1 to S5. This is most of the 202 steps and adds little new teaching.
- S3.film2: "Which feature is NOT seen" with three options is a double negative on a plain-film question. I had to re-read it.
- S2.a_x1, S2.a_x2, S4.c5_p: feedback stacks three messages (why it fails, the right answer, sure note) in one node. A fast reader loses the key line.
- END report: 43 text items (headline, 12 objective lines, 19 trap lines, extras). Too long to read as one wall; I skimmed it.

## Traps
All 20 trap options in the module were offered on my path and I tapped a trap option on each one at least once. Feedback refuted every one on that tap.
- TR1, TR2, TR3, TR4, TR5, TR8, TR11, TR12, TR13, TR14, TR17, TR18, TR21, TR22, TR23, TR31, TR35, TR36, TR40: fell_open (tapped, refuted by feedback, not reliably re-tested with a correct answer on a later offer)
- TR26: fell_recovered (tapped at S4.c2 and S4.c7, later correct on S6.timing)
- Note: for a guesser, trap taps are a clicking pattern, not held beliefs, so "fixed" does not apply here.

## Report check
- Rendered report (`factory.py render-report`) headline: **weak**, all 12 objectives "gap", 19 traps fell_open, TR26 fell_recovered.
- Accurate for this walk: mostly yes. I fell into most traps on first tap, and the headline "weak" matches a walk that guessed on most probes.
- Two claims are wrong for me:
  1. "You used no hints, even on the questions you missed." The renderer counts only tapped "Not sure, give me a hint" options. I read the hint text that follows every miss on retry, so the claim misleads.
  2. The fast-lane line says "You answered a diagnostic correctly and confidently". That was S2.start (wrong), then S2.start_b (correct, no confidence prompt), then skip. Not confident.
- Renderer bug: `render-report` crashes with `KeyError: 'choices'` if the path file ends at an end node (END). I rendered from the same path with END removed.

## Cards
- 11 of 11 answerable from the path. Each card's answer appeared in at least one feedback line I read, though I skimmed many of them.
- Caveat: several answers came from second tries after a wrong first tap, so my recall is shallow.

## Verdict
- engagement 1–5: 3 (fast clicking, skimmed, got bored in S6)
- would finish the module: yes, but only because I am clicking fast; 202 steps is too long
- biggest fix: cut the S6 "cold check" repetition. Replace the ~60 re-asked questions with one spaced recall of only the traps the learner actually fell into, so the walk ends in under 100 steps.
- Sure/Guessing labels were assigned by me, not randomly: I tagged Sure mostly on picks that happened to be correct. The calibration reading in the report is therefore not a fair test of this persona.

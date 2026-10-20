# Sim: guesser
path: S1.open → S1.open_t2 (TR13, Sure) → S1.open_2 → S1.open_x2 (Guessing) → … → S6.p12_ok → END  (200 taps; full path in guesser.json)

Walk summary: I clicked through quickly, picked among the plausible options with little reading, never opened "Show me why", and never opened a hint. First-try answers were right on 13 of 24 probes. I tapped Sure on 39 answers, of which 25 were wrong. On almost every wrong pick I took the Try again tap and got the right answer on the second go, usually by elimination.

## Friction
- S6.p1_t1 to S6.p12_t2 (segment 6): wrong-answer feedback is one bare correction line with no reason or cue, and the sure_note is the same boilerplate ("give it a second look before you move on") on about 13 nodes. Segments 1 to 5 use a Tempting/Nudge pattern; segment 6 drops it, so the feedback gets weaker just where the traps are densest.
- Try again loops (S1.open_2, S3.case_2, S4.c3, S6.p3 and many more): the same stem comes back with the options reshuffled, so the second tap is solvable by elimination or by memory of the line I had just read. I passed several probes this way without any sign that the idea had stuck. Nothing later re-asks them cold in the same segment.
- Show me why branches: 53 of 349 nodes (about 15 percent) are reachable only through "Show me why". A guesser never meets them, and three claims (K10, K28, K84) appear only there. The module does not tell a fast clicker that the richest explanation is behind that button.
- S2.pain_a_t1x and similar: "Show me why" is listed before "Next" on some feedback nodes; a quick tapper hits the first button.
- S1.age_b_p: partial feedback under a Sure answer shows no sure_note, while full-trap feedback does. Confidence is acknowledged inconsistently.
- Not friction, but noted: the walker prints sure_note on every feedback node, so I ignored it on Guessing paths. A real learner would see it only on Sure paths, which is the intended behaviour.

## Traps
The guesser holds no beliefs, so I record only whether each trap was offered and tapped. All 20 traps in `module.json` were met on this path:
- TR1, TR2, TR3, TR4, TR5, TR6, TR8, TR9, TR10, TR11, TR12, TR13, TR14, TR15, TR16, TR18, TR22, TR23, TR24, TR25: met. Each was tapped at least once; the trap was then corrected on Try again (TR15 was also re-tested on a later probe in segment 1, which is why the report marks it recovered).
- Not tested: none.

## Report check
- Rendered report (`factory.py render-report`) headline: **weak**. Partly accurate. The per-probe counts match my path: sure_wrong 25, guess_right 10, cold 13 of 24, calibration overconfident, no hints, no fast lane. The "tap Sure on wrong answers is costly" and "you never opened a hint" lines are true of me.
- What it missed: it scores first attempts only. It marks 19 of 20 traps as fell_open and nearly every objective as gap or shaky, and it never says that most of those were corrected on the Try again tap a few seconds later. It also does not separate "guessed and recovered on the spot" from "still open". That is why the headline reads harsher than the walk did. I could answer all 11 cards after the walk, which the report does not reflect.
- Verdict on the report: report_accurate = false. The factual items are correct, but the framing and headline overstate the gap.

## Cards
- 11 of 11 answerable from the path. Each card was prepared by a probe I had answered, or by feedback I had read after a wrong pick. Several (cards 3, 9, 11) I got only after a Guessing miss and a Try again, so the recall is shaky; I would not count it as firm.
- Holes: none on the path. Every card's answer appeared in a probe, a feedback line or an explain node I visited, without opening Show me why.

## Verdict
- engagement 1–5: 3
- would finish the module: yes (reached END at 200 taps; the module is long but the clicks are fast and the feedback never stops me)
- biggest fix: in segment 6 and on any node with generic feedback, replace the one-line correction and the boilerplate sure_note with the specific reason and cue, and make Try again change the stem or re-ask the idea cold later, so a fast clicker cannot pass by elimination.

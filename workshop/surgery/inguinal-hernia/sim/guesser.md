# Sim: guesser
path: S1.hook → S1.hook_t40 → S1.hook → S1.hook_t40 → S1.hook → S1.hook_t1 → S1.hook → S1.hook_ok → S1.explain_route → … → S5.tmesh → S6.p12 → S6.recap → END  (220 steps, reached END exactly at the cap)

Walk method: seeded random choice among plausible options (help and Why? excluded), every probe answered Guessing. Full step list is in `sim/guesser.json`.

## Friction
- S1.hook / S1.hook_t40 / S1.hook_t1: a wrong answer returns the same stem with the same wording. "Try again" gives nothing new, so without opening Why? the walk cycles until a lucky click.
- S2.tri_probe / S2.tri_t2b: "The deep ring is not the triangle's lower edge" is a one-line verdict with no reason. Retry repeats the question unchanged; "Show me why" is the only route to a rule.
- S3.route / S3.route_t: the same route question came back three times with identical feedback. The feedback never states the rule the learner needs.
- S3.wall then S3.wall2: the conjoint tendon / posterior wall question is asked again right after it was answered correctly.
- S4.d2_probe and S5.taxis_why: the identical "why is forceful reduction avoided" question appears about 30 nodes apart.
- S4.e1_probe / S4.e1_t34a: Amyand's wrong-answer feedback repeated word for word three times on the same stem.
- S5.tmesh / S5.tmesh_t1 / S5.tmesh_t2: the herniotomy/herniorrhaphy/hernioplasty stem repeats five times, with two feedback texts alternating. Long and repetitive for a fast clicker.
- S5.ex2 / S5.ex2_t14: the four-step stem repeats three times with identical options. The only gain is the reveal.
- S6.p2 / S6.p2t0 and S6.p6 / S6.p6t2: the same probe answered wrongly three times with identical feedback before the reveal lane.
- S6.p10 / S6.p10t1: the open-repair nerve probe repeats four times. The wrong-answer feedback names only the wrong option's nerve, not the right one.
- S1.hook_ok: "I have it, skip the route lesson" sits next to Next. A fast clicker will skip the one lesson that explains the naming trap.
- Whole walk: random retries consume most of the 220-step budget. A slower real learner would hit the loop report before the end.
- Cards: duplicates. Card 2 and card 13 (child herniotomy), card 4 and card 12 (nerves), card 5 and card 14 (triangles).

## Traps
- Not a trap-holding persona. I met 18 trap options on this path (TR1, TR2, TR5, TR7, TR8, TR9, TR12, TR14, TR16, TR17, TR22, TR23, TR25, TR28, TR31, TR34, TR39, TR40). TR11 and TR21 were not offered.
- Each met trap was answered wrongly on first contact and then corrected on retry. Several corrections were reached by guessing, not by reasoning, so none of them is a durable fix I can vouch for.

## Report check
- Rendered report (`factory.py render-report`) headline: **weak**. Calibration: underconfident. Fast lane: yes.
- Accurate for this walk? **Partly, no on three points.**
  - It says "You opened many hints". I opened zero hints. The count of 16 is the number of "Show me the answer" reveals, which the report labels as hints.
  - It says "You earned the fast lane by answering the diagnostic correctly and sure". I was Guessing throughout, and I skipped at S4.a_ok, not at the diagnostic.
  - "Cold 3 of 13" is driven by reveals, so it reads as a verdict on recall the walk never tested cold.
  - Direction is right: direct versus indirect, triangle, femoral position and nerves are the weak areas for a guesser. Underconfidence is right because I tapped Guessing on correct answers.
  - It misses the real cause of my long path: repeated identical stems and identical retry feedback.

## Cards
- 14 of 15 answerable from the path. Card 11 (TEP or TAPP) is only partly answerable: TEP appears in my path only as a distractor label, and TAPP is not named in any node I saw.
- Duplicates (2/13, 4/12, 5/14) mean the card deck tests the same three ideas twice.

## Verdict
- engagement 1–5: 3 (correct answers came quickly, but retries and repeats made the walk drag)
- would finish the module: yes, though only just within the step budget
- biggest fix: make a wrong answer teach the rule on the second miss (or vary the retry text), and stop re-asking a stem verbatim after two misses.

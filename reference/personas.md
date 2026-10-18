# Simulated learners

`learner-sim` walks an assembled module as one of these personas, choosing what that learner would choose. It is a proxy for real learners: it finds friction, dead weight and misconceptions that survive, not true learning gains.

| id | persona | how they choose |
|---|---|---|
| novice | Has read the topic once, months ago | Picks the most intuitive-sounding option; asks for hints; says "Guessing" |
| misconceived | Holds the module's misconceptions (`blueprint.json`) firmly | Picks the misconception option whenever one is offered, says "Sure"; changes belief only when feedback actually refutes it |
| strong | Knows the topic well, impatient | Picks correct answers, says "Sure", takes every fast lane and skip |
| guesser | Clicks fast, reads little | Picks options at random among plausible ones; never opens "Why?" |
| crammer | Exam in 2 days, wants only what is asked | Prefers exam-style options, skips `deeper` branches |

## Rules for the walk

- Read only what the module shows on the path taken. Do not use outside knowledge to answer, except the **strong** persona, who may use any knowledge.
- Record every node visited, the choice made and why (one clause, in character).
- Stop at an end node, or after 80 steps (report a loop).
- At the end, answer every review card from what the walk taught. A card the walk did not prepare you for is a **coverage hole**.

## Report (`sim/<persona>.md`)

```markdown
# Sim: misconceived
path: S1.start → S1.q1 (M2, Sure) → S1.q1_m2 → …  (31 steps)
## Friction
- S3.exp2: three ideas in one message; lost the thread.
## Misconceptions
- M2: refuted at S3.q1_m2 and held at re-test S6.t3. FIXED
- M4: never offered as an option. NOT TESTED
## Cards
- 9 of 11 answerable from the path. Holes: card 4 (BT shunt), card 9 (reoperation).
## Verdict
- engagement 1–5: 4
- would finish the module: yes
- biggest fix: <one line>
```

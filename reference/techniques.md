# Conversation-building techniques

Each segment is authored several times, once per technique, and the versions compete (`.claude/skills/lore-factory/SKILL.md`, stage `author`). `scripts/pick_techniques.py` chooses which techniques compete from this table and `factory/technique-stats.json`: the best performers for the segment type plus one exploration pick, so the factory keeps learning which techniques win where.

The table is machine-read: keep one row per technique, IDs `T<n>`, segment types comma-separated from `hook, retrieve, mechanism, clinical, diagnosis, management, traps, consolidate`.

| id | name | fits |
|---|---|---|
| T1 | Socratic ladder | mechanism, diagnosis, management, retrieve |
| T2 | Case-first vignette | hook, clinical, diagnosis, management, traps |
| T3 | Predict–observe–explain | mechanism, clinical, diagnosis |
| T4 | Productive failure | hook, mechanism, management |
| T5 | Worked example, then fade | diagnosis, management, mechanism |
| T6 | Refutation (misconception-first) | mechanism, traps, clinical, retrieve |
| T7 | Contrasting cases | diagnosis, clinical, traps, mechanism |
| T8 | Self-explanation pick | mechanism, management, consolidate |
| T9 | Retrieval gate | retrieve, consolidate, hook |
| T10 | Exam-trap drill | traps, consolidate |
| T11 | Erroneous example (spot the mistake) | management, diagnosis, traps |
| T12 | Learner-built summary | consolidate |

## Recipes

**T1 Socratic ladder.** A chain of 3–5 small questions, each a step the learner can just reach, ending at the idea. Wrong steps get a nudge question, not the answer.

**T2 Case-first vignette.** Open with a short NEET PG-style vignette (age, presentation, one or two findings). The learner makes the clinical call; facts arrive as feedback on that call. Vignette details that are not claims must be presentation only (age, setting), never findings the claims do not support.

**T3 Predict–observe–explain.** Ask the learner to predict what happens (to the shunt, the murmur, the saturation) when something changes; show what the claim says happens; ask them to pick the explanation.

**T4 Productive failure.** Pose a problem slightly beyond the learner before teaching it; let them try; then teach the idea using their attempt ("You picked X. Here's what X misses …"). Keep it short: one problem, one explanation.

**T5 Worked example, then fade.** Walk one case fully with reasoning visible, then a second similar case with the last step left to the learner, then a third with more steps left out.

**T6 Refutation.** Name the common wrong belief, explain why it is tempting, refute it with the claim, state the correct idea. Strong for traps that survive ordinary teaching.

**T7 Contrasting cases.** Put two near-neighbours side by side (pink vs blue tet, one finding vs another) and ask what distinguishes them. Facts about another topic need cross-module claims (`reference/module-format.md`).

**T8 Self-explanation pick.** After a fact, offer 3 explanations of *why*; the learner picks the right one. Wrong explanations are plausible mechanisms the claims rule out.

**T9 Retrieval gate.** Before any teaching, ask what the learner already remembers; route by answer (fast lane for correct and sure).

**T10 Exam-trap drill.** Rapid PYQ-style stems built on `pattern.md` asks and their distractors, with ⚠ Exam notes where the key and the current source disagree.

**T11 Erroneous example.** Show a worked case or a peer's answer with one planted error; the learner finds it. The planted error must be a real trap, and the correction cites claims. Use it only after the learner has seen a correct worked example of the same idea, and ask "which step is wrong" then "why" as two probes (DP17).

**T12 Learner-built summary.** The learner assembles the take-home: pick the true statements, order the steps, or choose the best one-line summary. Ends with review cards.

## Adding a technique

Add a row and a recipe. `pick_techniques.py` gives new techniques exploration turns automatically, and the stats decide whether they stay in rotation.

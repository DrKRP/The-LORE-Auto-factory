# The LORE conversation contract

What every module must do, why, and how it is checked. Agents read this before authoring, judging or editing. `scripts/factory.py validate` enforces the rules marked **[V]**; judges score the rest with `reference/rubric.md`.

## 0. Product constraints (non-negotiable)

- **Buttons only.** Every learner turn is a tap on one of 2–4 pre-written replies. No typing, no free recall. **[V]** (unknown node or choice fields are rejected)
- **No runtime AI.** No AI grading, AI feedback or AI verification while the learner uses the module. Everything shown, feedback and the final report included, is written in advance and selected by the path. AI is used only to *build* modules in this factory.
- **Distractor-first.** A module is designed from its trap brief (`reference/traps.md`): every probe offers at least one trap **[V]**, every trap is offered on at least two probes in different forms **[V]**, and every distractor maps to exactly one trap.
- **Maximum pre-authored feedback at the end.** The module carries a complete report (`reference/report.md`) for every objective level, trap outcome, error-type pattern, calibration and help pattern. **[V]**

## 1. Facts

- Content comes from the module's note, written from the factory's own knowledge (`CLAUDE.md`). Messages that teach a fact cite the note's claim IDs, so cards and the report can link back. There is no fact-checking stage.
- Mnemonics, analogies and image cues are welcome when marked `device: true`.
- Where the note's ⚠ Exam notes show the PYQ key differs from current practice, teach both: "PYQs have expected X; current practice is Y." Learners must be able to answer the exam *and* know the truth.

## 2. The learner does the thinking

- **Ask before tell.** A new idea opens with a probe (predict, recall, choose) before the explanation. At most 2 non-interactive nodes in a row. **[V]**
- **One idea per node, one question per node.** ≤ 3 messages per node, ≤ 60 words per message; a probe ends on its question. **[V]** (DP26)
- **Commit, then feedback.** Every probe has a correct reply and at least one trap reply. **[V]**

## 3. Wrong answers are where the teaching happens

- Each wrong option is a trap from `trap-map.json` (PYQ distractors, ⚠ Exam notes, predictable wrong models), never a filler option. One error per option: if an option could be wrong for two reasons, it diagnoses nothing.
- The repair follows the trap's error type (`reference/traps.md`): contrast for look-alikes, rebuild the set for list errors, predict-then-show for reversed mechanisms, and so on.
- Feedback on a wrong option says why it is *tempting*, then why it is wrong (refutation), then what is right, with claims. Never "Wrong!", never empty or ability praise, no controlling words. **[V]** phrase scan (DP14)
- Feedback on a *correct* pick says why it is right, with a claim, so a lucky guess still learns the reason. **[V]** (DP13)
- **No telegraphing.** The key must not be findable by form: not systematically the longest, not the only option with a number or an absolute word, not always in the same position; no "all / none of the above". **[V]** (DP1)
- **Distractors are comparably tempting.** No option is dominated: someone with surface knowledge cannot eliminate any of them (DP2).
- **Hint ladder.** A first miss on a key probe gets a hint and a retry, not the answer. Hints never contain the answer. **[V]** (DP9) A second miss gets the explanation, and the same idea is re-tested later in a different form (delayed re-test).
- **A second explanation differs from the first.** If the first explanation did not land, the remediation uses a different technique (a case instead of a mechanism, a contrast instead of a definition). Folded variants from the tournament supply these.
- Every trap is re-tested later in a different form; recovery is credited only on the re-test. **[V]** (≥ 2 probes per trap)

## 4. Adapt to the learner

- **Fast lane.** A segment may open with a diagnostic probe; a correct and confident answer can `skip` the worked explanation (expertise reversal: what helps novices slows experts).
- **Confidence.** Key probes set `ask_confidence`. A confident error gets a `sure_note` (hypercorrection: high-confidence errors, once corrected, are remembered best).
- **Agency.** Explanation nodes may offer "Why?" (`agency`) or "Go deeper" (`deeper`) next to "Next".
- Every core objective is taught or tested on **every** path from start to end, fast lanes included. **[V]**
- **Cold evidence.** The last segment has at least one probe with no hint option, so the report can tell hinted success from unaided success. **[V]** (DP11)

## 5. Shape of the journey

A module runs 5–8 segments, typically:

1. **Hook**: a short clinical vignette or puzzle the learner cannot fully answer yet (productive failure / curiosity gap).
2. **Retrieve**: activate prior knowledge; bridge from earlier published modules when there are any (interleaving).
3. **Core mechanism / definition**: build the mental model.
4. **Clinical picture and diagnosis**: vignette-led, NEET PG style.
5. **Management**: decisions in a case.
6. **Exam traps**: PYQ keys, look-alike distractors, "which is NOT".
7. **Consolidate**: the learner builds the summary (choose / order), then review cards.

The architect may change this when the topic calls for it, and must say why in the blueprint.

## 6. Voice

A warm senior resident tutoring a final-year MBBS student in India the night before an exam: direct, plain English, no filler, no lecturing paragraphs. One term per concept, and expand an abbreviation the first time it appears (DP25). Bold the word the exam would test. Indian units and drug names. Address the learner as "you".

## 7. Measures the factory tracks

`scripts/factory.py validate` reports, per module: node and probe counts, interactivity (share of nodes where the learner chooses between ≥ 2 replies), longest run of non-interactive nodes, shortest / longest path, words per message, high-yield claim coverage, objective guarantee on every path, trap coverage and re-tests, report completeness. `scripts/factory.py score` folds these, the judges' review and the simulated learners into one composite score.

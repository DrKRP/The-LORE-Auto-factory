# The LORE conversation contract

What every module must do, why, and how it is checked. Agents read this before authoring, judging or editing. `scripts/validate.py` enforces the rules marked **[V]**; judges score the rest with `reference/rubric.md`.

## 1. Facts

- Every factual sentence the tutor says cites claim IDs from `claim-bank.json`, and says only what those claims say: same numbers, same qualifiers. **[V]** for IDs; dialogue-verifier for wording.
- A message with `claims: []` states no fact. Questions, prompts, encouragement and signposting only.
- Unverified claims never sit on the core path. They may appear only in a `deeper` branch or an exam-trap node, with `flag: "unverified"` so the learner sees ⚠. **[V]**
- Mnemonics, analogies and image cues are welcome when marked `device: true`; they restate cited facts, never add one.
- Where the note's ⚠ Exam notes show the PYQ key differs from the current source, teach both: "PYQs have expected X; current <source> says Y." Learners must be able to answer the exam *and* know the truth.

## 2. The learner does the thinking

- **Ask before tell.** A new idea opens with a probe (predict, recall, choose) before the explanation. At most 2 non-interactive nodes in a row. **[V]**
- **One idea per node.** ≤ 3 messages per node, ≤ 60 words per message. **[V]**
- **Commit, then feedback.** Every probe has a correct reply and at least one misconception reply. **[V]**

## 3. Wrong answers are where the teaching happens

- Each wrong option is a real misconception: a PYQ distractor from `pattern.md`, a trap from ⚠ Exam notes, or one the architect lists in the blueprint, never a filler option.
- Feedback on a wrong option says why it is *tempting*, then why it is wrong (refutation), then what is right, with claims. Never "Wrong!", never empty praise.
- **Hint ladder.** A first miss on a key probe gets a hint and a retry, not the answer. A second miss gets the explanation, and the same idea is re-tested later in a different form (delayed re-test).
- **A second explanation differs from the first.** If the first explanation did not land, the remediation uses a different technique (a case instead of a mechanism, a contrast instead of a definition). Folded variants from the tournament supply these.
- Every misconception in the blueprint is targeted by at least one choice. **[V]**

## 4. Adapt to the learner

- **Fast lane.** A segment may open with a diagnostic probe; a correct and confident answer can `skip` the worked explanation (expertise reversal: what helps novices slows experts).
- **Confidence.** Key probes set `ask_confidence`. A confident error gets a `sure_note` (hypercorrection: high-confidence errors, once corrected, are remembered best).
- **Agency.** Explanation nodes may offer "Why?" (`agency`) or "Go deeper" (`deeper`) next to "Next".
- Every core objective is taught or tested on **every** path from start to end, fast lanes included. **[V]**

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

A warm senior resident tutoring a final-year MBBS student in India the night before an exam: direct, plain English, no filler, no lecturing paragraphs. Bold the word the exam would test. Indian units and drug names. Address the learner as "you".

## 7. Measures the factory tracks

`scripts/validate.py` reports, per module: node and probe counts, interactivity (share of nodes where the learner chooses between ≥ 2 replies), longest run of non-interactive nodes, shortest / longest path, words per message, high-yield claim coverage, objective guarantee on every path, misconception coverage. `scripts/score.py` folds these, the judges' review and the simulated learners into one composite score.

# Efficacy test queue

One experiment per `test-first` principle in `design-refinement/principles.md`, ordered by value / cost. Every experiment compares **arm A** (current LORE rules: `reference/pedagogy.md`, `traps.md`, `techniques.md`, `rubric.md`, `report.md`) with **arm B** (the same rules plus the addendum written out below, pasted at the end of the author prompt). Everything else is held fixed: same claim bank, trap map, blueprint, technique and segment brief.

## Honesty first: these are proxies

Blind judges (`dialogue-judge`, three lenses) and simulated learners (`learner-sim`, `reference/personas.md`) are language models reading text. They measure whether a segment *looks* like good teaching to a model and whether a scripted persona's walk goes as designed. They do not measure learning, retention or exam scores. Three specific weaknesses:

- Judges and authors share a model family, so a rule that makes text sound more like what models expect can score well without helping anyone.
- The `misconceived` persona "changes belief only when feedback actually refutes it", which is a judgement the sim model makes. A "fixed" trap is the model's verdict, not a corrected belief.
- Samples are tiny (3 segments × 2 replicates per arm). Decision rules below demand consistency across segments for that reason, and every "adopt" is provisional.

Each experiment therefore names the **real-learner check**: what the exported session records (`reference/report.md`, "The session record": `{module, version, started, finished, path: [{node, choice, kind, trap, sure, objectives}], report}`) would later confirm or overturn. That needs the app owner to ship A and B as two `version`s of the same module and assign learners at random; without randomisation the comparison is confounded by who chooses which module.

Real-learner measures used below (all computable from session records):
- **recovery rate**: per trap, `fell_recovered / (fell_recovered + fell_repeated)`.
- **re-test accuracy**: first-answer correct on the later probe offering a trap, among learners who fell into it earlier.
- **confident-error repair**: re-test accuracy among learners who fell with `sure: true`.
- **completion**: share of started sessions with `finished` set; **path length** in steps and minutes (`finished − started`).
- **help use**: `kind: "help"` steps per session; **branch use**: share of sessions taking each choice.
- **card outcomes**: only if the app also records review-card answers (not in the current record; flag as needed for retention claims).

## Common protocol

1. **Test set.** Three segments of the named type, from three different modules (different subjects where possible), each with a finished claim bank and trap map. Prefer segments whose trap map has the trap kind the experiment targets.
2. **Authoring.** For each segment, `dialogue-author` writes 2 replicates per arm with the segment's existing technique (4 variants). Arm B's prompt = arm A's prompt + the addendum.
3. **Gates.** `scripts/factory.py check-segment` and `dialogue-verifier` on every variant. A gate failure (G1–G4, validator error, verifier FAIL) counts against the arm; failed variants are scored 0 as in normal judging.
4. **Blind judging.** `scripts/blind.py` over the 4 variants; three judges (learning-scientist, examiner, learner-advocate) score R1–R9 per `reference/rubric.md`. An arm's score per segment = mean over its 2 replicates and 3 judges.
5. **Simulation.** For each module, assemble version A and version B that differ only in the tested segment (replicate 1 of each arm, chosen before judging to avoid selection bias); run `misconceived`, `novice`, `guesser`, `strong` on both (8 sim runs per module). Report-related experiments also read `sim/<persona>.report.json`.
6. **Validator metrics** from `factory.py validate` on both versions: errors, `words_per_message_mean/max`, `max_tell_run`, `interactivity`, `longest_path`, plus the DP28 metrics once added.
7. **Decision.** Apply the experiment's rule. "Adopt" means: write the addendum into the reference file named in the principle, then watch the real-learner check. Record result and rule in `design-refinement/experiments/results.md` (one row per experiment).

**Cost units (agent runs).** Segment unit = 4 author + 4 verifier + 3 judge = 11 per segment. Sim unit = 8 per module. **Standard experiment** (3 segments in 3 modules, with sims) = 33 + 24 = **57 runs**. **Light** (judges plus a 2-persona sim) = 33 + 12 = **45**. **Report experiment** (report-author 2 arms × 3 modules = 6, judges 9, sim report re-reads 3 personas × 2 arms × 3 modules = 18) = **33**.

## Queue

| order | ID | principle | value | cost (runs) |
|---|---|---|---|---|
| 1 | EXP-001 | DP4 wrong-pick feedback anatomy | very high: every trap path | 57 |
| 2 | EXP-002 | DP12 stricter objective levels | high: every report, cheap | 33 + a flagged `render_report` |
| 3 | EXP-003 | DP8 stuck protocol | high: key probes, novices | 57 |
| 4 | EXP-004 | DP10 variation sweep | high: E1 is the commonest NEET PG trap kind | 57 |
| 5 | EXP-005 | DP31 technique candidates via tournament | medium, near-free | ~0 extra (exploration slots) |
| 6 | EXP-006 | DP22 if-then plan | medium, cheap | 33 |
| 7 | EXP-007 | DP16 cognitive conflict (E3) | high for E3 traps only | 57 |
| 8 | EXP-008 | DP15 self-explanation pick | medium | 57 |
| 9 | EXP-009 | DP24 second-miss normalising line | low-medium, cheap | 45 |
| 10 | EXP-010 | DP18 unlabelled stems, interleaved consolidate | medium | 57 |
| 11 | EXP-011 | DP23 under/over distractor pairing | medium, management only | 45 |
| 12 | EXP-012 | DP21 transfer bridge | medium, needs published modules | 57 |
| 13 | EXP-013 | DP19 observe–infer–conclude | medium, emerging evidence | 57 |
| 14 | EXP-014 | DP20 error-type self-diagnosis | uncertain, friction risk | 57 |
| 15 | EXP-015 | DP30 goal line and difficulty ramp | low-medium | 45 |
| 16 | EXP-016 | DP29 exemplar triples | medium later, blocked until ≥ 3 published modules per error type | 60 |
| 17 | EXP-017 | DP32 intensity fork | expected null | ~70 |

Total if all run: about 840 agent runs. Running EXP-001 to EXP-004 first (about 200 runs) covers the four largest expected effects.

---

## EXP-001 Wrong-pick feedback anatomy (DP4)

**Hypothesis.** Trap feedback written as consequence, credit, first wrong step, refutation, one correction and a next-step signpost will score higher on trap work than current tempting-refute-right feedback, without hurting clarity.

**Segment types.** traps, clinical, mechanism.

**Arms.** A = current rules. B = current rules + addendum:

> **Addendum EXP-001 (feedback anatomy).**
> 1. For every `kind: "trap"` choice, write its feedback node in this order, in at most 3 messages: (a) what this pick leads to in the case, only when a claim supports that outcome, otherwise "That does not deal with <the problem in the stem>." with `claims: []`; (b) why it was tempting, crediting the part of the learner's reasoning that was right ("You spotted the cyanosis; that part is right."); (c) the first wrong step, taken from the trap's `first_wrong_step` in `trap-map.json` (or its `diagnoses` line if that field is missing), named in one clause; (d) the refutation, using the repair for the trap's error type in `reference/traps.md`, citing claims.
> 2. Correct one thing per feedback node. If the pick is also wrong for a second reason, leave it out here.
> 3. End the last message with what comes next ("Try it again with that in mind." or "Next: the same idea in a new case.").
> 4. Stay within 60 words per message. Cut the credit clause before you cut the refutation.
> 5. Call a wrong pick "tempting"; never "wrong", "careless" or similar. No praise words.
> 6. For each `kind: "correct"` choice, the feedback names the step the learner got right in one line, with its claim. "Yes." alone is not enough.

**Measures.** Judges: R2 (primary), R9, R4, R8. Sims: `misconceived` trap fixed rate on the segment's traps; `novice` engagement; friction count on feedback nodes. Validator: `words_per_message_mean`, `words_per_message_max`, errors; verifier FAIL count (consequence sentences are the G1 risk).

**Decision rule.** Adopt if B beats A on mean R2 by ≥ 0.3 in ≥ 2 of 3 segments, B's weighted judge score is not lower than A's in any segment by more than 0.2, R4 does not drop by more than 0.2, B has no more gate failures or verifier FAILs than A, and the pooled `misconceived` fixed rate for B is ≥ A's. Otherwise keep A and record which part (consequence, credit, signpost) judges flagged.

**Cost.** 57 runs.

**Real-learner check.** Higher recovery rate and re-test accuracy on traps whose feedback follows B, with no fall in completion. Overturned if recovery is unchanged while time per session rises.

---

## EXP-002 Stricter, honest objective levels (DP12)

**Hypothesis.** Reports that require a held re-test for "secure", name "right but guessing" as fragile, and give one next step per level will be judged more accurate and more useful than current reports.

**Segment types.** None (module-mode report). Use 3 assembled modules with existing sim paths.

**Arms.** A = current `reference/report.md` rules and texts. B = B rules (implemented behind a flag in `render_report`, a one-off code change, not an agent run) + report-author addendum:

> **Addendum EXP-002 (report levels).**
> 1. Write a `fragile` text for every objective: the learner was right the first time but tapped Guessing, or has not yet passed a re-test. Say it is right but not yet secure, and name the kind of probe to retry.
> 2. Write `secure` texts that claim only what the path shows: "You held this on the re-test in this module." Never "mastered" or "you know this".
> 3. End every level text with one concrete next step: a named review card, or the segment to redo.
> 4. Where a level can rest on one or two answers, add a short honest clause ("one right answer can be a lucky guess").
> 5. Keep every text within 90 words; cite claims for any fact.

**Measures.** Judges (module mode): R9 (primary, report part), learner-advocate's actionability verdict, and a count of "over-claim" flags (sentences that claim more than the path shows, per `principles.md` "What a path cannot prove"). Sims: `report_accurate` across `misconceived`, `novice`, `guesser`; headline separation between `strong` and `misconceived` (as in `factory.py score`). Validator: `check_report` errors.

**Decision rule.** Adopt if `report_accurate` for B ≥ A in ≥ 2 of 3 modules, R9 for B ≥ A + 0.3 on the mean, over-claim flags for B ≤ A, and headline separation is kept. Otherwise keep A.

**Cost.** 33 runs, plus the flagged `render_report` change.

**Real-learner check.** Among learners rated `secure` by B, re-test accuracy in a later module on the same objective (or card answers, if recorded) should be higher than among learners rated `secure` by A only. If B's `secure` learners do no better, the stricter rule adds words without information.

---

## EXP-003 Stuck protocol (DP8)

**Hypothesis.** Key probes with a two-rung hint ladder, a partial worked example after the second miss, and a near-transfer probe after the explanation will raise recovery for struggling learners more than "hint, then explanation".

**Segment types.** mechanism, diagnosis, management.

**Arms.** A = current rules. B = current rules + addendum:

> **Addendum EXP-003 (stuck protocol).**
> 1. Choose the 2–3 key probes in the segment (those with `ask_confidence`). Apply steps 2–6 only to them.
> 2. The probe's `help` choice leads to hint 1 (`role: "hint"`): a question that points at the trap's `first_wrong_step` without naming any option. Choices: "Try again" (`retry`, back to the probe) and "Another hint" (`help`, to hint 2).
> 3. Hint 2 names the governing rule, with claims, still without any option's label. Choices: "Try again" and "Show me a worked example".
> 4. A trap pick after a retry leads to a partial worked example: a parallel case walked in at most two messages, with its last step asked as a probe (2–3 options, including the same trap).
> 5. A miss on that step leads to the full explanation, using a different technique from the segment's main one, then straight to one near-transfer probe on the same objective: new patient or setting, same trap offered.
> 6. No hint text may contain the correct option's label. Each rung is at most 40 words.

**Measures.** Judges: R5 (primary), R1, R4. Sims: `novice` and `misconceived` recovery (correct at the near-transfer probe or the later re-test after at least one miss on that objective); `steps`; `novice` engagement. Validator: `longest_path`, `max_tell_run`, hint depth per key probe, errors.

**Decision rule.** Adopt if R5 for B ≥ A + 0.5 in ≥ 2 of 3 segments, pooled sim recovery for B ≥ A + 10 percentage points, R1 and R4 do not drop by more than 0.2, `longest_path` grows by ≤ 25%, `novice` engagement drops by ≤ 0.5, and no gate failures.

**Cost.** 57 runs.

**Real-learner check.** Recovery rate and re-test accuracy among learners who used `help` at least once, B versus A; help use per session (a ladder that is simply clicked through to the answer would show high help use with no gain). Overturned if completion falls or recovery is flat.

---

## EXP-004 Variation sweep for look-alike pairs (DP10)

**Hypothesis.** Teaching a high-yield E1 look-alike pair with a four-beat variation sweep will repair the confusion better than contrasting cases alone.

**Segment types.** diagnosis, clinical, traps (segments containing an E1 trap).

**Arms.** A = T7 Contrasting cases under current rules. B = T7 + addendum:

> **Addendum EXP-004 (variation sweep).**
> 1. Take the highest-yield E1 (look-alike) trap in this segment's trap list and its pair.
> 2. Beat 1, contrast: two short cases side by side (at most 2 sentences each); the learner taps which label fits the first case.
> 3. Beat 2, separation: the same case with only the critical feature changed; ask again. The options differ only in that feature.
> 4. Beat 3, generalisation: keep the critical feature, change age, setting and incidental details; ask again.
> 5. Beat 4, fusion: two features change together; the learner picks the label.
> 6. State the discriminating rule, with claims, only in the feedback after beat 3.
> 7. Every beat is a probe offering the E1 trap. Case findings are either cited claims or presentation-only details (age, setting).

**Measures.** Judges: R2 (primary), R9, R6, R4. Sims: `misconceived` fixed rate on E1 traps; `guesser` accuracy on the pair's re-test. Validator: probes per segment, `longest_path`.

**Decision rule.** Adopt (add `T13 Variation sweep` to `reference/techniques.md` as a full row) if B's weighted judge score ≥ A + 0.3 in ≥ 2 of 3 segments, the E1 fixed rate for B ≥ A, no drop in R4 above 0.2 and no gate failures. If B wins on R2 but loses on R4, add it as an exploration row only (EXP-005 route).

**Cost.** 57 runs.

**Real-learner check.** Recovery rate for E1 traps and re-test accuracy on the pair's later probe, B versus A. Overturned if E1 recovery is unchanged; the extra probes then cost time for nothing.

---

## EXP-005 New technique candidates through the tournament (DP31)

**Hypothesis.** At least one of five lower-evidence button techniques will win or be merged often enough in normal tournaments to earn a permanent row.

**Segment types.** As listed per technique below.

**Arms.** A = current technique table. B = table plus five exploration rows; `scripts/pick_techniques.py` gives each exploration turns. The addendum is the five recipes, pasted into `reference/techniques.md`:

> **Addendum EXP-005 (technique candidates).**
> 1. **Name–recognise–recall** (retrieve, consolidate, hook): at most 3 new terms or classes; name one with nothing else; then "tap the X" among look-alikes; then "what is this called?" with 3–4 plausible names. A recall miss drops back to the recognise step for that item, and the item returns later.
> 2. **Concreteness fade** (mechanism, management): a case first, then a schematic in words, then the abstract rule, with a one-line bridge between stages ("the shunt you just traced is this arrow"). A miss at the rule stage routes back one stage, not forward.
> 3. **Inversion probe** (traps, diagnosis): once per module, ask "What would have to be true for <the trap answer> to be right?" with three conditions as options; the correct condition links to a cited claim showing it does not hold here.
> 4. **Step-down prerequisite** (mechanism, diagnosis, management): after a second miss, one probe on the simplest prerequisite of the idea; right → a contrast explanation and back; wrong → a short refresher node, then rejoin.
> 5. **Source clash** (traps, consolidate): for an E5 trap, two sourced statements (the PYQ key and the current source); ask which you would tick in the exam and which is current; then why they differ.

**Measures.** `factory/technique-stats.json` win and merge counts; mean weighted judge score per candidate versus the segment type's mean; gate failures.

**Decision rule.** Keep a candidate in rotation if, in its first 5 exploration turns, it wins or is merged into the selection at least twice and its mean weighted score is ≥ the segment-type mean − 0.2. Drop it otherwise. Re-check after 15 turns.

**Cost.** About 0 extra runs: each exploration turn replaces a variant the tournament would author anyway. The real cost is time (25+ tournament turns) and fewer turns for known-good techniques.

**Real-learner check.** For modules where a candidate won a segment, recovery rate and branch use in that segment versus the module average. A technique that wins with judges but shows high abandonment in the segment is dropped.

---

## EXP-006 If-then plan at the end (DP22)

**Hypothesis.** Ending with a tapped if-then plan keyed to the learner's likely error types will make the report more actionable without lowering engagement.

**Segment types.** consolidate (plus the report).

**Arms.** A = current consolidate segment and report. B = addendum (author and report-author); the report echo needs a small render rule behind a flag:

> **Addendum EXP-006 (if-then plan).**
> 1. Just before the end node, add one node: "One habit to take into the next stem?" with three choices (`continue`), each an if-then plan.
> 2. Write one plan for each of the three error types used by most of this module's traps. The "if" is a situation in a stem ("If a stem says NOT or EXCEPT"); the "then" is one small action ("I underline it before I read the options").
> 3. Plans state no facts (`claims: []`). If a plan mentions a fact, cite it.
> 4. Report-author: write one line per plan for the report to echo ("Your plan: …"), and say which of the learner's falls it addresses.

**Measures.** Judges (module mode): R9 and the learner-advocate's actionability verdict; R8. Sims: engagement, `would_finish`, friction at the plan node. Validator: `max_tell_run`, errors.

**Decision rule.** Adopt if learner-advocate R9 for B ≥ A + 0.5 in ≥ 2 of 3 modules, engagement does not drop, and no friction is reported at the plan node by more than one persona.

**Cost.** 33 runs.

**Real-learner check.** Distribution of plan taps (a plan nobody picks is dropped). Overturning or confirming the effect needs linked sessions across modules: learners who chose the "NOT/EXCEPT" plan should fall less often into E2 "which is NOT" traps in their next module. Without a learner ID across session records this cannot be checked; say so.

---

## EXP-007 Cognitive conflict for reversed mechanisms (DP16)

**Hypothesis.** For E3 reversed-mechanism traps, predict–contradict–reconcile will fix the wrong model more often than plain refutation.

**Segment types.** mechanism, clinical, traps (segments with an E3 trap).

**Arms.** A = current rules (T6 refutation for E3). B = current rules + addendum:

> **Addendum EXP-007 (cognitive conflict).**
> 1. Pick this segment's E3 trap (or, if none, the trap the trap map marks highest yield with a mechanism behind it).
> 2. Open with a prediction probe that sets `ask_confidence`; the trap is one of the options.
> 3. A trap pick leads to a `feedback` node that does not yet refute. It asks "If that were so, what would we see?" with 2–3 `continue` choices, each a consequence. Whatever is tapped, the next node shows the cited outcome that contradicts the wrong model.
> 4. Then a probe: "So what is really happening?" with the correct mechanism, the same trap, and one other trap.
> 5. Name the distinction in one sentence, with claims.
> 6. Add at most 3 nodes to the trap path; a learner who answers correctly at step 2 skips all of it.
> 7. Re-test the trap later in a different form, as usual.

**Measures.** Judges: R2 (primary), R1, R5, R4. Sims: `misconceived` fixed rate on E3 traps (primary sim measure); `steps`. Validator: `longest_path`, errors.

**Decision rule.** Adopt (add `T14 Cognitive conflict` and the E3 repair text) if pooled E3 fixed rate for B ≥ A + 15 percentage points, R2 for B ≥ A in ≥ 2 of 3 segments, R4 drop ≤ 0.2, no gate failures.

**Cost.** 57 runs.

**Real-learner check.** Confident-error repair on E3 traps (learners who fell with `sure: true`), B versus A: the case where conflict should matter most. Overturned if repair is no better and completion of the segment falls.

---

## EXP-008 Self-explanation pick after key correct answers (DP15)

**Hypothesis.** A "why does that work?" pick after key correct answers will cut lucky-guess passes, shown as fewer right-then-wrong patterns at the re-test.

**Segment types.** mechanism, management, diagnosis.

**Arms.** A = current rules. B = current rules + addendum:

> **Addendum EXP-008 (self-explanation pick).**
> 1. Find 1–2 points of conceptual density in the segment: a new principle or a step that is not obvious. Do not add picks anywhere else.
> 2. After the correct-pick feedback at those points, add a probe: "Why does that work?" with three options: the real mechanism (`correct`) and two wrong mechanisms that are `trap` choices from the trap map (prefer E3).
> 3. Add a fourth choice, "I know why, next" (`continue`), so a sure learner can move on; the objective must still be tested elsewhere on that path.
> 4. Feedback on a wrong explanation follows tempting, refute, right, with claims.
> 5. No more than two such picks per segment.

**Measures.** Judges: R1 (primary), R2, R4. Sims: among sims who were right first time while Guessing, the share also right at the re-test (`guesser`, `novice`); `strong` friction and engagement. Validator: interactivity, `longest_path`.

**Decision rule.** Adopt if the guess-then-hold share for B ≥ A + 10 percentage points pooled, R1 for B ≥ A + 0.3 in ≥ 2 of 3 segments, `strong` engagement drops ≤ 0.5, no gate failures.

**Cost.** 57 runs.

**Real-learner check.** Re-test accuracy among learners whose first answer was right with `sure: false`; share choosing "I know why, next" (if nearly everyone skips, the pick does nothing).

---

## EXP-009 Second-miss normalising line (DP24)

**Hypothesis.** A one-line normalising, strategy-attributing line after a second miss will make feedback feel warmer without seeming patronising.

**Segment types.** traps, clinical, mechanism.

**Arms.** A = current rules. B = current rules + addendum:

> **Addendum EXP-009 (normalising line).**
> 1. On each key probe, when the learner picks a trap again after a retry, open that feedback with one line of at most 15 words that names the trap as common and tempting ("This is the one most people fall for: …"). `claims: []` unless it states a fact.
> 2. When a learner gets it right after a retry or hint, credit the strategy in one clause ("Checking the age settled it.").
> 3. Never mention ability, effort or intelligence; no praise words.
> 4. At most one normalising line on any single path through the segment.

**Measures.** Judges: R8 (primary, all lenses, learner-advocate weighted in the reading), R4; judges' `flaws` mentioning "patronising". Sims: `novice` engagement and `would_finish`.

**Decision rule.** Adopt if R8 for B ≥ A + 0.3 in ≥ 2 of 3 segments, no "patronising" flag from the learner-advocate on any B variant, R4 drop ≤ 0.1.

**Cost.** 45 runs (light: `novice` and `misconceived` sims only).

**Real-learner check.** Completion after a second miss (share of sessions with a repeated trap pick that still finish), B versus A.

---

## EXP-010 Unlabelled-situation stems and interleaved consolidate (DP18)

**Hypothesis.** Probes that hide the concept name, and a consolidate segment that mixes all earlier objectives, will align better with NEET PG stems and expose traps that topic-labelled probes hide.

**Segment types.** diagnosis, traps, consolidate.

**Arms.** A = current rules. B = current rules + addendum:

> **Addendum EXP-010 (unlabelled stems).**
> 1. In diagnosis and traps segments, write at least half the probes as findings only: neither the stem nor any message in the node names the disease, topic or concept being tested.
> 2. Their options are 3–4 concept or diagnosis names: the key plus traps from the trap map (prefer E1 and E10).
> 3. In consolidate, include at least one probe for each earlier segment's core objectives, in an order that does not follow the segment order.
> 4. At least one consolidate stem does not name the module's topic at all.
> 5. Every probe still offers a trap listed in the trap map.

**Measures.** Judges: R6 (primary), R2, R1, R4. Sims: `guesser` and `misconceived` accuracy on the tested segments; cards answerable. Validator: share of objectives probed in the last segment; errors.

**Decision rule.** Adopt if R6 for B ≥ A + 0.3 in ≥ 2 of 3 segments, R4 does not drop by more than 0.2, cards answerable does not fall, no gate failures.

**Cost.** 57 runs.

**Real-learner check.** First-answer accuracy on unlabelled probes versus labelled ones within B (expected lower: they are harder), and re-test accuracy later. Overturned if learners do worse at re-test after unlabelled practice than after labelled practice.

---

## EXP-011 Under- and over-reaction distractor pairing (DP23)

**Hypothesis.** Management probes whose two wrong options are one under-reaction and one over-reaction will be more diagnostic than probes with two errors in the same direction.

**Segment types.** management.

**Arms.** A = current rules. B = current rules + addendum:

> **Addendum EXP-011 (direction pairing).**
> 1. For each management probe with two or more wrong options, check the trap map for an under-reaction trap (too little, too late, too conservative) and an over-reaction trap (too much, too early, too aggressive).
> 2. If both exist, offer one of each. Never offer two wrong options in the same direction when an opposite-direction trap exists.
> 3. In each trap's feedback, name the direction first ("This waits too long." / "This goes too far, too soon."), then refute with claims.
> 4. Never invent a trap to fill a direction; use only traps in the trap map.

**Measures.** Judges: R9 (primary), R2, R7. Sims: `guesser` first-answer accuracy (lower means the options are harder to eliminate by form). Validator: trap choices per probe.

**Decision rule.** Adopt if R9 for B ≥ A + 0.3 and R2 for B ≥ A in ≥ 2 of 3 segments, no gate failures.

**Cost.** 45 runs.

**Real-learner check.** Spread of wrong picks across options (pick entropy over trap choices per probe) and whether direction errors cluster by learner. Overturned if one direction is almost never picked (a dominated distractor).

---

## EXP-012 Near and far transfer bridge (DP21)

**Hypothesis.** A short transfer bridge after a secure idea will make learners do more of the thinking and prepare them for new stems, at an acceptable cost in length.

**Segment types.** consolidate, management.

**Arms.** A = current rules. B = current rules + addendum:

> **Addendum EXP-012 (transfer bridge).**
> 1. For each core objective already re-tested in the module, add one near-transfer probe (same principle, new patient and setting).
> 2. Add one far-transfer probe (different context, same structure). Facts about another topic come only as cross-module claims (`<subject>/<slug>#K<n>`); if none exist, use near transfer only.
> 3. After the far probe, a probe "Which principle carries over?" with the principle (`correct`) and a trap.
> 4. Both transfer probes offer the objective's trap.
> 5. The whole bridge is at most 5 nodes.

**Measures.** Judges: R1 (primary), R6, R3, R4. Sims: accuracy on the far probe; `steps`; engagement. Validator: `longest_path`.

**Decision rule.** Adopt if R1 for B ≥ A + 0.3 in ≥ 2 of 3 modules, steps grow by ≤ 15%, engagement drops by ≤ 0.3, no gate failures.

**Cost.** 57 runs. Needs published modules for far-transfer claims; otherwise run with near transfer only and say so.

**Real-learner check.** Near-right / far-wrong rate; accuracy on the same objectives in a later module (needs linked sessions).

---

## EXP-013 Observe, infer, conclude for vignettes (DP19)

**Hypothesis.** Splitting a diagnosis vignette into observe, infer and conclude taps, with reasoning-error distractors, will reduce anchoring and premature-closure picks.

**Segment types.** clinical, diagnosis.

**Arms.** A = T2 Case-first vignette under current rules. B = T2 + addendum:

> **Addendum EXP-013 (observe–infer–conclude).**
> 1. Present the vignette as findings only (cited claims or presentation-only details).
> 2. Probe 1, observe: "Which finding matters most here?" The options are the discriminating finding and findings that lead to traps (anchoring).
> 3. Probe 2, infer: "What does that finding point to?" The options are the right inference and a trap's inference.
> 4. Probe 3, conclude: the diagnosis or decision, with traps as options, including a premature-closure option where the trap map has one.
> 5. After the call, one probe: "Which rule does this case show?" (correct and a trap).
> 6. Every wrong option is a trap from the trap map.

**Measures.** Judges: R7 (primary), R1, R2, R4. Sims: `misconceived` fixed rate; `steps`. Validator: `longest_path`, interactivity.

**Decision rule.** Adopt (add `T15 Observe–infer–conclude`) if B's weighted score ≥ A + 0.3 in ≥ 2 of 3 segments, steps grow by ≤ 20%, no gate failures.

**Cost.** 57 runs.

**Real-learner check.** Which rung learners fail on (observe, infer or conclude) and whether recovery on those traps beats A. Overturned if learners fail mostly at rung 1 and drop out.

---

## EXP-014 Error-type self-diagnosis tap (DP20)

**Hypothesis.** A one-tap "what went wrong?" after a first miss will improve second attempts without adding friction for tired learners.

**Segment types.** diagnosis, management, traps.

**Arms.** A = current rules. B = current rules + addendum (the report comparison is not tested here; it needs a new report rule):

> **Addendum EXP-014 (self-diagnosis).**
> 1. On at most two key probes per segment, a first trap pick leads to a `feedback` node, "What went wrong?", with four `continue` choices: "I didn't know this", "I knew it but slipped", "I used the wrong approach", "I misread the question".
> 2. Each choice leads to a repair node of at most 2 messages: concept → the refutation; slip → a check habit; approach → when each approach applies; misread → the qualifier the stem contained.
> 3. Every route also gives the trap's refutation with claims, so the learner is corrected whatever they tapped. Then "Try again".
> 4. Name the diagnosis node `<probe>_why` so a later report rule can find it.

**Measures.** Judges: R5 (primary), R4, R8. Sims: `novice` and `guesser` second-attempt accuracy; engagement; friction at the diagnosis node. Validator: `longest_path`, `max_tell_run`.

**Decision rule.** Adopt only if second-attempt accuracy for B ≥ A + 10 percentage points pooled, engagement drops by ≤ 0.3, learner-advocate R8 does not drop, no gate failures.

**Cost.** 57 runs.

**Real-learner check.** Agreement between learners' self-diagnosis and each trap's authored error type, and second-attempt accuracy by self-diagnosis. Overturned if most learners tap one answer regardless (e.g. "slipped"), which would make the node noise.

---

## EXP-015 Segment goal line and difficulty ramp (DP30)

**Hypothesis.** A one-line exam goal at the start of each non-hook segment and a steady difficulty ramp will raise engagement without reducing learner-led thinking.

**Segment types.** retrieve, mechanism, clinical, diagnosis, management, traps.

**Arms.** A = current rules. B = current rules + addendum:

> **Addendum EXP-015 (goal line).**
> 1. In every segment except the hook, the entry node's first message is one line of at most 20 words stating the goal as an exam ability ("By the end: tell pink from blue tet in a stem."), `claims: []`.
> 2. Put that line in the same node as the segment's first probe; do not add a node.
> 3. Make the first probe answerable by a learner who did the earlier segments; raise difficulty one step per probe; end the traps segment on its hardest probe.
> 4. No goal line in the hook: it stays a puzzle.

**Measures.** Judges: R8 (primary), R1, R4. Sims: engagement, `would_finish`. Validator: `max_tell_run`, words per message.

**Decision rule.** Adopt if R8 for B ≥ A + 0.3 in ≥ 2 of 3 segments and R1 does not drop.

**Cost.** 45 runs.

**Real-learner check.** Completion and mid-module drop-off by segment, B versus A.

---

## EXP-016 Exemplar triples at authoring time (DP29)

**Hypothesis.** Showing authors three published (wrong model, option, feedback) triples of the same error type will raise trap-work quality without leaking facts.

**Segment types.** any; choose segments whose traps share error types with published modules.

**Precondition.** At least 3 published modules containing traps of each error type used. Until then, this experiment waits.

**Arms.** A = current author prompt. B = author prompt + three retrieved triples + addendum:

> **Addendum EXP-016 (exemplars).**
> 1. Before writing, read the three exemplar triples below (wrong model, option, feedback). They come from other topics.
> 2. Copy their form only: the order of tempting, refute and right; their length; their tone.
> 3. Never copy a fact, number, finding or drug from an exemplar. Every fact comes from this module's claim bank, cited.
> 4. Do not reuse exemplar wording in your options.

**Measures.** Judges: R2 (primary), R9. Verifier: FAIL count; G1 failures (fact leakage). Validator: errors.

**Decision rule.** Adopt if R2 for B ≥ A + 0.3 in ≥ 2 of 3 segments and B has no more G1 failures or verifier FAILs than A.

**Cost.** 60 runs (57 + 3 retrieval steps by the orchestrator).

**Real-learner check.** Recovery rate in modules built with exemplars versus without, matched by subject and error type.

---

## EXP-017 Intensity fork at the hook (DP32)

**Hypothesis (null).** A tapped "walk me through it / test me straight" fork will not beat the single track with fast lanes once authoring size is accounted for.

**Segment types.** hook, plus the first three segments of one module (pilot).

**Arms.** A = single track with fast lanes. B = addendum:

> **Addendum EXP-017 (intensity fork).**
> 1. End the hook with a node: "How do you want to run this?" with "Walk me through it" and "Test me straight".
> 2. In the "test me" track, each segment opens with its hardest probe; explanations appear only after a miss.
> 3. The "walk" track is the current module.
> 4. Both tracks must teach or test every core objective on every path (the validator checks this).

**Measures.** Composite score (`factory.py score`), R5, node count, `strong` persona steps and engagement.

**Decision rule.** Adopt only if composite for B ≥ A + 0.3 with node count growth ≤ 30%. Otherwise record DP32 as rejected on evidence.

**Cost.** About 70 runs (one module, three segments authored twice over, full sims and module-mode judging).

**Real-learner check.** Share choosing each track, and completion and recovery by track. If nearly everyone picks one track, the fork is dead weight.

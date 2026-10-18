# Design principles: merged catalogue

Synthesis of the seven analyses in `design-refinement/analysis/` against the LORE constraints (`design-refinement/analysis-brief.md`) and the current references (`reference/pedagogy.md`, `traps.md`, `report.md`, `techniques.md`, `rubric.md`, `module-format.md`). The analyses predate the trap vocabulary: their "misconception M<n>" is LORE's trap `TR<n>` with `kind: "trap"`, and their "error" is the trap's wrong model (`trap-map.json` `diagnoses`). Every efficacy figure below is what a repo cites, **claimed, not verified by LORE**.

## Summary: top items

| # | ID | principle | status | what changes |
|---|---|---|---|---|
| 1 | DP1 | No-telegraph option hygiene | adopt-now | validator lint: key not systematically longest, no lone absolute, position spread |
| 2 | DP2 | Comparably tempting distractors | adopt-now | R2 anchor + blind pairwise "which would a tired student pick" judge step |
| 3 | DP3 | One trap per option, own feedback node | adopt-now | validator: same trap twice in a probe = error; shared `next` across traps = warning |
| 4 | DP7 | Confident errors first in the report | adopt-now | report rule: sure-and-wrong traps listed first, their cards first |
| 5 | DP14 | Banned praise, scolding and controlling phrases | adopt-now | validator phrase scan over `say`, `sure_note`, report texts |
| 6 | DP4 | Wrong-pick feedback anatomy | test-first | EXP-001 |
| 7 | DP12 | Stricter, honest objective levels | test-first | EXP-002 |
| 8 | DP8 | Stuck protocol (multi-rung hints, partial worked example, near-transfer) | test-first | EXP-003 |
| 9 | DP10 | Variation sweep for look-alike pairs | test-first | EXP-004 |
| 10 | DP16 | Cognitive conflict for reversed mechanisms | test-first | EXP-007 |

Counts: adopt-now 15, test-first 17, already-in-lore 7, rejected 5 (44 merged principles from about 100 repo-level principles).

### Source codes

| code | repository | analysis file |
|---|---|---|
| UM | umass-ml4ed/prompt_distractor_generation_NAACL | `analysis/umass-ml4ed__prompt_distractor_generation_NAACL.md` |
| AC | lowwwbank/anything-to-course | `analysis/lowwwbank__anything-to-course.md` |
| AT | Bhala-Srinivash/agent-tutor-skill | `analysis/Bhala-Srinivash__agent-tutor-skill.md` |
| SO | UderMoreiraDeAssis/socrates | `analysis/UderMoreiraDeAssis__socrates.md` |
| GM1 | GarethManning/education-agent-skills (part 1) | `analysis/GarethManning__education-agent-skills__part1.md` |
| GM2 | GarethManning/education-agent-skills (part 2) | `analysis/GarethManning__education-agent-skills__part2.md` |
| SC | b-urge/scenario-skill | `analysis/b-urge__scenario-skill.md` |

Each source line reads `<code> P<n>: <file in that repo>`, where P<n> is the principle number in the analysis file.

Ordering: by expected impact on a NEET PG learner, adopt-now and test-first interleaved by impact; `already-in-lore` and `rejected` entries follow at the end because they change nothing.

---

## DP1 No-telegraph option hygiene
**Rule.** A learner must not be able to find the key from the form of the options. In every probe the correct label is not systematically the longest, most hedged, most fluent or most specific; it is not the only label with an absolute word (always, never, only, all, none, most common, first-line) or the only one with a number or dose; the key's position varies across the module; options are grammatically parallel; no "all/none of the above". "Which is NOT" stems are allowed because NEET PG uses them, but they are deliberate, not accidental. For a tired learner who scans options, a telegraphed key teaches nothing and makes the path (and the report) meaningless.
**Sources.** AC P10: `references/practice-design.md` ("Multiple choice done right"); AT P1: `references/quiz-rules.md` (Zero-Hint Policy); GM1 P2: `skills/questioning-discussion/hinge-question-designer/SKILL.md`; GM2 P5: `skills/ai-literacy/ai-output-critical-audit-designer/SKILL.md`; SC P4: `SKILL.md` Steps 3–4.
**Evidence claimed.** Haladyna et al. 2002 item-writing rules (GM1); Koriat & Bjork 2005 framing (AC); the rest none (claimed, not verified by LORE).
**LORE change.** `scripts/factory.py` `validate_module`: (a) warning per probe when the `correct` label is the unique longest by words; error-level module metric `key_longest_share` > 0.4; (b) warning when the correct label alone contains a word from an absolutes list or alone contains a digit; (c) metric `key_position_max_share` (share of probes whose key sits at the most common index), warning above 0.5; (d) error on "all of the above" / "none of the above". `reference/pedagogy.md` §3: one bullet stating the rule. `reference/rubric.md` R2 5-anchor: "no option can be eliminated or chosen by form alone".
**Status.** adopt-now.

## DP2 Comparably tempting distractors (non-dominated options)
**Rule.** Every wrong option must be one a learner holding that trap's wrong model would pick, and no option should be dismissable by someone with only superficial knowledge. Within a probe, the wrong options should be roughly equally tempting: a probe where one distractor is obviously wrong has, in effect, one fewer option. Judges test this blind, one probe at a time, by asking pairwise "which of these two wrong options would a tired final-year student pick?" in both orders; a distractor that loses every pairing is flagged for rewrite.
**Sources.** UM P8, P10: `README.md` (`proportion`), `utils.py` `compute_ranking_pairs`, `ranking_model.py`; AT P2: `references/quiz-rules.md` rule 5; GM1 P1: `hinge-question-designer/SKILL.md`; GM2 P2: `skills/montessori-alternative-approaches/three-part-lesson-designer/SKILL.md`; SC P9: `SKILL.md` Step 5 (key withheld from reviewers).
**Evidence claimed.** UM's premise is real-student pick proportions (Eedi data, no numbers in repo); Wiliam 2011, Haladyna et al. 2002 (GM1) (claimed, not verified by LORE).
**LORE change.** `reference/rubric.md` R2: add to the 5-anchor "no option is dominated: a learner with superficial knowledge cannot eliminate any distractor"; add to the 1-anchor "a distractor is the right answer to no question and tempts no one". `.claude/agents/dialogue-judge.md` segment mode: one extra step, "for each probe, compare wrong options pairwise in both orders; list any option that loses every pairing in `flaws`". `scripts/blind.py` already withholds `kind` and `trap` (keep it so).
**Status.** adopt-now.

## DP3 One trap per option, distinct within a probe, each with its own feedback
**Rule.** Each wrong option diagnoses exactly one trap; two wrong options in the same probe never carry the same trap; two different traps never share one feedback node (there is no generic "incorrect" node); and the explanation that follows a wrong pick refers to that pick ("You picked X; X misses ..."). This is what makes the path diagnostic at all.
**Sources.** UM P5, P11: `PromptFactory.py` `_zeroShotPrompt`, `utils.py` `normalize_candidate_distractors`; SC P3: `SKILL.md` Step 4 ("not three shades of the same action"); GM1 P1, P3: `hinge-question-designer/SKILL.md`, `skills/ai-learning-science/formative-assessment-loop-designer/SKILL.md`; AC P1: `references/course-blueprint.md` steps 2–3.
**Evidence claimed.** Black & Wiliam 1998; VanLehn 2006 (step-level feedback); Wiliam 2011 (claimed, not verified by LORE).
**LORE change.** Already in LORE: "one error per option" (`reference/traps.md` rules, `pedagogy.md` §3), duplicate labels are an error (`factory.py` `check_nodes`, "two choices share a label"), R2 1-anchor penalises generic "incorrect". Add to `check_nodes`: error when two `kind: "trap"` choices in one node carry the same `trap`; warning when two trap choices with different `trap` IDs share the same `next`; warning when two labels in one probe share their first three words.
**Status.** adopt-now.

## DP4 Wrong-pick feedback anatomy
**Rule.** Feedback on a wrong pick follows a fixed order in at most three messages: (1) the consequence of that pick in the case, where a claim supports it ("her saturation keeps falling"), (2) why it was tempting, crediting the part of the reasoning that was right, (3) the first wrong step or belief, named, (4) the refutation using the error type's repair, with claims, (5) one correction only, (6) a last line saying what comes next. LORE already requires tempting, refute, right-with-claims; the new parts are consequence-first, credit, the named first wrong step, a single correction and a next-step signpost.
**Sources.** AC P4: `references/practice-design.md` (Feedback structure); GM1 P9: `skills/ai-learning-science/ai-feedback-design-principles/SKILL.md`, `skills/memory-learning-science/feedback-quality-analyser/SKILL.md`; SO P10: `.claude/skills/socratic-inquiry/SKILL.md` Phase 3 rule 5; UM P4: `PromptFactory.py` `_disAllInfoReasoningPrompt`; SC P1: `SKILL.md` Step 4.
**Evidence claimed.** Wisniewski, Zierer & Hattie 2020 (d≈0.48); Shute 2008; Hattie & Timperley 2007; Kluger & DeNisi 1996; Narciss 2008 (claimed, not verified by LORE). SC and UM cite nothing.
**LORE change (if adopted).** `reference/pedagogy.md` §3: replace the feedback bullet with the six-part order. `reference/rubric.md` R2 5-anchor: name the parts; judges count parts present on three sampled feedback nodes. `reference/techniques.md` T6 recipe: add "name the first wrong step". Risk: more words per node against the 60-word cap, and consequences need claims (G1).
**Status.** test-first (EXP-001).

## DP5 The re-test is a variation that tests the distinction
**Rule.** The later probe that re-tests a trap uses a new vignette or a new question form (new presenting situation, not just new numbers, never the same stem or the same option order), and it asks for the distinction the trap blurs, so a correct answer cannot come from remembering an option's position or wording.
**Sources.** AC P5: `references/study-mode.md` item 5, `course-blueprint.md` step 10; AT P3: `references/quiz-rules.md` (Drilling Weak Concepts); GM1 P12: `skills/memory-learning-science/retrieval-practice-generator/SKILL.md`; GM2 P7: `skills/environmental-experiential-learning/experiential-learning-cycle-designer/SKILL.md`.
**Evidence claimed.** General transfer literature (AC); Roediger & Karpicke 2006 (GM1) (claimed, not verified by LORE).
**LORE change.** The rule exists (`reference/traps.md`: "at least two probes in different forms"; `pedagogy.md` §3), but `factory.py` only counts ≥ 2 probes. Add to `validate_module`: for each trap, the probes offering it must not share their first `say` text, and must not have identical label sets (normalised); warning when the two `trap-map.json` probe `form` values are equal.
**Status.** adopt-now.

## DP6 Trap record carries the wrong model and the first wrong step; derive options from it
**Rule.** In the trap analysis, each trap is written error-first: a one-line conceptual statement of the wrong belief that names no vignette details (so it can be re-used across probes and in the report), then the first wrong inference a learner holding it makes, then the option text that belief produces, then the feedback. Options are never invented first and justified later. The first wrong step feeds hint 1 (point at it) and the feedback (name it).
**Sources.** UM P1, P2, P3, P4, P7: `README.md` (Data Format), `PromptFactory.py` `_zeroShotAllInfoErrorPrompt`, `_disAllInfoErrorPrompt`, `rule_based_selection_prompt`, `misconception_selection.py`; GM1 P1: `hinge-question-designer/SKILL.md`; SC P7: `SKILL.md` Step 2.
**Evidence claimed.** None in UM or SC; Wiliam 2011, Christodoulou 2017 (GM1) (claimed, not verified by LORE).
**LORE change.** `reference/traps.md` `trap-map.json` schema: add `"first_wrong_step": "…"` per trap; state in the distractor-analyst rules that `diagnoses` is written without case-specific numbers or findings and that `distractor_set` is derived from it. Validator (`factory.py`, trap-map check if present): warn on empty `first_wrong_step`, warn when two traps have identical `diagnoses`. Optional: mark each trap `origin: pool | invented` (UM P7) and warn when more than half are invented.
**Status.** adopt-now.

## DP7 Confident errors first: per-trap sure-and-wrong list and path-rated card order
**Rule.** The report leads its trap section with traps the learner fell into while saying "Sure" (the hypercorrection targets), and orders review cards from a fixed lookup over path facts: wrong twice → Again; wrong then right, or hint used → Hard; right first → Good; right first and Sure (or fast lane) → Easy. Cards for Sure-and-wrong traps come first, at day 1. Intervals are labelled "suggested", never a retention claim.
**Sources.** AC P7, P8: `references/study-mode.md` (The calibration log), `examples/example-course/sql-for-analysts/review-schedule.md`, `references/practice-design.md`; GM1 P10: `skills/student-learning/confidence-calibration-check/SKILL.md`; AT P8: `references/quiz-rules.md` (FSRS Rating After Quiz), `references/fsrs.md`; GM2 report rules (calibration): `skills/wellbeing-motivation-agency/self-efficacy-builder-sequence/SKILL.md` context.
**Evidence claimed.** Koriat & Bjork 2005; Bjork & Bjork 2011; Butterfield & Metcalfe hypercorrection (as used by LORE); FSRS constants marked unverified by the repo itself (claimed, not verified by LORE).
**LORE change.** `reference/report.md`: add a "Confident errors" rule (traps with any encounter `sure: true` on a trap choice, listed before other trap statuses) and change "Next steps" ordering to: cards of sure-wrong traps' objectives, then `gap`, then `shaky`, then the rest, with the Again/Hard/Good/Easy label shown from the lookup table. Update `render_report` in `scripts/factory.py` and `player/index.html` in sync. No new module fields (computed from `sure` and `kind` already in the path).
**Status.** adopt-now.

## DP8 Stuck protocol: multi-rung hint ladder, partial worked example, near-transfer after the explanation
**Rule.** On key probes, help escalates in fixed pre-written rungs, each doing one thing and none stating the answer: hint 1 points at the first wrong step (from DP6) as a question; hint 2 links to a known case or names the governing rule; then a partial worked example whose last step is a probe; only then the full explanation (by a different technique than the first), followed at once by one near-transfer probe on the same objective. A prerequisite step-down probe may replace hint 2 when the trap rests on a missing prerequisite.
**Sources.** GM1 P4, P5, P6: `skills/student-learning/progressive-hint-ladder/SKILL.md`, `skills/ai-learning-science/adaptive-hint-sequence-designer/SKILL.md`; SO P1, P3, P4: `.claude/skills/socratic-inquiry/SKILL.md` Phase 3 rule 4, `references/question-taxonomy.md`, `.claude/agents/socratic-tutor.md`; UM P4: `PromptFactory.py`; AT P4, P7: `references/teaching-loop.md`, `SKILL.md` (Sequencing Protocol).
**Evidence claimed.** VanLehn 2011 (ITS d=0.76); Aleven & Koedinger 2002; Koedinger & Aleven 2007; Wood, Bruner & Ross 1976; Wood & Wood 1999; Kirschner, Sweller & Clark 2006 (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/pedagogy.md` §3 "Hint ladder": rewrite as the rung sequence; `reference/techniques.md`: amend T1 and T5 recipes; `factory.py`: metrics `hint_depth_max` per key probe and "explain node reached only via second miss is followed by a probe with the same objective" (warning). Cost: 3–5 extra nodes per key probe.
**Status.** test-first (EXP-003).

## DP9 Hints never leak the answer
**Rule.** A hint node never contains the correct label's text, never eliminates all options but one, and always offers a way back to the probe ("Try again") as well as a further rung or the explanation. Hints are reached only from the probe's `help` choice, so the learner has seen the question before getting help; the first hint restates what the stem gives and what it asks.
**Sources.** GM1 P4, P5: `progressive-hint-ladder/SKILL.md` (warm-start protocol), `adaptive-hint-sequence-designer/SKILL.md`; AT P1: `references/quiz-rules.md`.
**Evidence claimed.** Aleven & Koedinger 2002 (help abuse); Razzaq & Heffernan 2010 (claimed, not verified by LORE).
**LORE change.** `factory.py` `check_nodes`: for `role: "hint"` nodes, warning when any `say` text contains (case-insensitive) the label of a `correct` choice of the probe that links to it; error when a hint node has no choice routing back to a probe or forward to an explain node. `reference/pedagogy.md` §3: one sentence.
**Status.** adopt-now.

## DP10 Variation sweep for look-alike pairs
**Rule.** For each look-alike pair the trap map lists (error type E1), author a short fixed sequence of probes: contrast (two cases side by side), separation (vary only the critical feature), generalisation (hold the critical feature, vary age, setting and incidental findings), fusion (two features vary together). Options within each beat differ in one critical feature only. The discriminating rule is stated only after the learner has seen it vary.
**Sources.** GM2 P1, P2: `skills/global-cross-cultural-pedagogies/variation-theory-task-designer/SKILL.md`, `skills/montessori-alternative-approaches/three-part-lesson-designer/SKILL.md`; AC P6: `SKILL.md` Step 4, `references/course-blueprint.md` steps 4–5.
**Evidence claimed.** Marton & Booth 1997; Marton 2015; Lo 2012; Kullberg et al. 2017 (repo rates "strong"); Fyfe et al. 2014 (AC) (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/techniques.md`: new row `T13 Variation sweep | diagnosis, clinical, traps, mechanism` with the four-beat recipe; `reference/traps.md` E1 repair: "contrasting cases, extended to a variation sweep when the pair is high-yield". The technique tournament then measures it in production.
**Status.** test-first (EXP-004).

## DP11 Hinted versus cold evidence in the report
**Rule.** The report separates what the learner answered unaided from what they answered after a hint or retry, and every module has at least one late probe with no `help` choice so there is cold evidence. A learner who was right only after hints is told so plainly and given a cold retry card. Hint level is described as evidence, not a grade.
**Sources.** GM1 P18, P22: `skills/student-learning/unassisted-evidence-checkpoint/SKILL.md`, `progressive-hint-ladder/SKILL.md`, `skills/student-learning/stuck-and-error-diagnosis-coach/SKILL.md`; AT P6: `SKILL.md` (Dashboard).
**Evidence claimed.** Bastani et al. 2025 PNAS (assisted vs unassisted gap with AI help); the repo says its own checkpoint protocol is untested; Karabenick & Berger 2013 (claimed, not verified by LORE).
**LORE change.** `reference/report.md`: new rule "Cold evidence": over probes in the last two segments that offer no `help` choice, count first answers correct; new `help` outcome `hinted_only` (≥ 1 objective answered correctly only after a `help` step, and wrong or unseen cold) with its pre-authored text; extend the `report` block schema with `help.hinted_only`. `factory.py` `validate_module`: error when no probe in the last segment lacks a `help` choice. Keep `render_report` and the player in sync.
**Status.** adopt-now.

## DP12 Stricter, honest objective levels
**Rule.** "Secure" means the learner was right first time, did not say Sure on any wrong answer, and held the objective at its re-test (where a re-test exists); right-but-Guessing is named "right, not yet secure"; a fast lane counts as secure only if a later probe on the same objective was also right; every level carries one pre-written next step. Each level's text admits what one tap cannot prove.
**Sources.** AT P6: `SKILL.md` (Dashboard), `references/fsrs.md` (Status Badges); GM2 P16: `skills/original-frameworks/coherent-rubric-logic-builder/SKILL.md`, `docs/brief.md`; GM1 P10, P18: `confidence-calibration-check/SKILL.md`, `unassisted-evidence-checkpoint/SKILL.md`; AC P7: `references/study-mode.md`.
**Evidence claimed.** Sadler 1989; Haring 1978 instructional hierarchy; Manning's own framework labelled "emerging" (GM2); AT cites none (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/report.md` objective-mastery table: redefine `secure`, add `fragile` (right first time, Guessing, re-test not yet passed); `report` block gains `objectives.O<n>.fragile`; `render_report` and player updated.
**Status.** test-first (EXP-002).

## DP13 Correct-pick feedback says why it worked
**Rule.** Feedback on a correct pick names the step the learner got right and gives the one-line reason with claims ("Yes: knee-chest raises SVR, so less blood shunts right to left"). "Yes.", "Correct." or "Right!" alone is not feedback. Where a probe has two correct routes, each gets its own line.
**Sources.** AT P5: `references/teaching-loop.md` (EVALUATE); SC P5: `SKILL.md` Step 4; GM1 P9: `ai-feedback-design-principles/SKILL.md`; GM2 P10: `skills/wellbeing-motivation-agency/self-efficacy-builder-sequence/SKILL.md`.
**Evidence claimed.** Hattie & Timperley 2007 (task and process level) (claimed, not verified by LORE).
**LORE change.** `reference/pedagogy.md` §3: one bullet. `factory.py` `check_nodes`: warning when a node reached from a `kind: "correct"` choice has total `say` text under 8 words or cites no claims.
**Status.** adopt-now.

## DP14 Banned praise, scolding, controlling and pseudo-science phrases
**Rule.** No self-level praise ("Great job", "Well done", "Amazing", "Genius", "Good effort"), no scolding ("Wrong!", "Careless", "Obviously"), no controlling language ("you must", "you have to"), no timers, points, streaks or badges, and no learning-styles, brain-hemisphere or growth-mindset slogans in any tutor text, `sure_note` or report text. Errors are "tempting", attributed to a step or belief, never to ability.
**Sources.** GM1 P9: `ai-feedback-design-principles/SKILL.md`, `feedback-quality-analyser/SKILL.md`; GM2 P10, P11, P13 and EXCLUSIONS: `self-efficacy-builder-sequence/SKILL.md`, `skills/wellbeing-motivation-agency/motivation-diagnostic-task-redesign/SKILL.md`, `skills/wellbeing-motivation-agency/trauma-informed-practice-designer/SKILL.md`, `docs/EXCLUSIONS.md`; AT P10: `references/teaching-loop.md` (Anti-Patterns 5); SO P2: `references/evidence-base.md`.
**Evidence claimed.** Kluger & DeNisi 1996; Butler 1988; Deci, Koestner & Ryan 1999; Lepper & Woolverton 2002; Sisk et al. 2018 (claimed, not verified by LORE).
**LORE change.** `pedagogy.md` §3 already says "Never 'Wrong!', never empty praise" but nothing checks it. Add a phrase list to `factory.py` (or config) and scan every `say[].text`, `sure_note.text` and report `text`: warning per hit, error for the scolding and pseudo-science sets. `reference/rubric.md` R8 1-anchor: add "ability praise or controlling words".
**Status.** adopt-now.

## DP15 Self-explanation pick at points of conceptual density
**Rule.** After a correct answer on a new principle or a non-obvious step (not at every step), the learner picks why it is right from three explanations: the real mechanism and two wrong mechanisms that are traps from the trap map (usually E3 reversed mechanism). A correct-but-Guessing learner is the main target; since the player cannot route on confidence, the pick is offered to everyone after key correct answers, with "Skip, I know why" as a fast exit.
**Sources.** SO P1: `.claude/skills/socratic-inquiry/SKILL.md` Phase 3 rule 4, `references/question-taxonomy.md`; GM1 P15, P6: `skills/ai-learning-science/self-explanation-prompt-designer/SKILL.md`, `adaptive-hint-sequence-designer/SKILL.md`.
**Evidence claimed.** Chi et al. 1989, 1994; Wylie & Chi 2014; Hausmann & VanLehn 2007; GM1 notes generation beats picking, so the button form is a weaker proxy (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/pedagogy.md` §2: rule for where self-explanation picks go; `reference/techniques.md` T8 recipe: "place after key correct answers; wrong explanations are trap options". Every such pick is a probe, so it must carry a trap choice (already enforced).
**Status.** test-first (EXP-008).

## DP16 Cognitive conflict and consequence picks for entrenched traps
**Rule.** For reversed-mechanism (E3) and other entrenched traps, do not just tell. Elicit a prediction with a confidence tap; show the case whose cited outcome contradicts the wrong model; ask the learner to pick the consequence that would follow if their belief were true ("If that were so, what would happen to the saturation after the spell?"); then pick the reconciliation; then name the distinction. In feedback, a wrong pick can lead to such a consequence pick before the refutation.
**Sources.** GM1 P8: `skills/ai-learning-science/intelligent-tutoring-dialogue-designer/SKILL.md`; SO P2: `SKILL.md` Phase 3 rule 4, `references/evidence-base.md`; SC P1: `SKILL.md` Step 4.
**Evidence claimed.** Chi et al. 2001; Chi & Wylie 2014 ICAP; Graesser et al. 2005; Lepper & Woolverton 2002 (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/techniques.md`: new row `T14 Cognitive conflict | mechanism, clinical, traps` and a "consequence pick" variant in T6; `reference/traps.md` E3 repair: "predict, contradict, reconcile".
**Status.** test-first (EXP-007).

## DP17 Erroneous examples come after a correct worked example
**Rule.** A planted-error case (T11) appears only after the learner has seen a correct worked example of the same reasoning in the same segment, never as first exposure. The learner first taps the wrong step, then picks why it is wrong (one option is the real trap), then sees the corrected version. Its benefit may show only at the delayed re-test.
**Sources.** GM1 P14: `skills/ai-learning-science/erroneous-example-designer/SKILL.md`.
**Evidence claimed.** McLaren, Adams & Mayer 2012, 2015 (delayed benefit); Große & Renkl 2007 (needs prior knowledge, else the error can be learned) (claimed, not verified by LORE).
**LORE change.** `reference/techniques.md` T11 recipe: add the sequencing rule and the "which step, then why" pair. Judges check it under R2; no validator field (would need a new node field).
**Status.** adopt-now.

## DP18 Unlabelled-situation stems and an interleaved consolidate segment
**Rule.** Some probes give only findings and ask what is going on, with the concept hidden from the stem and the node, as NEET PG stems do. The consolidate segment mixes probes from every earlier segment in shuffled order and includes at least one stem that does not name the topic, so the learner must recognise which idea applies.
**Sources.** AC P2, P12: `references/practice-design.md` (Tasks that don't name the method), `quality-rubrics.md`, `course-blueprint.md` (Checkpoint level); GM1 P21: `skills/memory-learning-science/spaced-practice-scheduler/SKILL.md`, interleaving-unit-planner; SO P5: `references/question-taxonomy.md` (evidence questions).
**Evidence claimed.** Brunmair & Richter 2019 interleaving (g≈0.42, material-dependent); transfer-appropriate processing (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/pedagogy.md` §5 Consolidate: "≥ 1 probe per earlier segment's objectives, ≥ 1 stem without the topic name"; `reference/techniques.md` T10 and T12 recipes; `factory.py` metric: share of objectives probed in the last segment.
**Status.** test-first (EXP-010).

## DP19 Observe, infer, conclude for vignettes, then reflect and generalise
**Rule.** Diagnosis vignettes run in three taps: which finding matters (observe), what it supports (infer), what the diagnosis or decision is (conclude). Wrong options at each rung are named reasoning errors (anchoring on one finding, premature closure, ignoring a qualifier) mapped to traps. After the call, three short reflection taps (decisive finding, mechanism, general rule) precede a transfer case. Probes span question types (evidence, assumption, implication), not recall only.
**Sources.** GM2 P6, P7: `skills/systems-thinking/ladder-of-inference-reflection/SKILL.md`, `experiential-learning-cycle-designer/SKILL.md`; SO P5, P6: `references/question-taxonomy.md`, `SKILL.md` Phase 3 rule 2.
**Evidence claimed.** Argyris/Senge (practitioner level, GM2 rates it emerging); Boud, Keogh & Walker 1985; Hattie 2009 simulation d=0.33; Graesser & Person 1994; the 70% deep-question figure is SO's own target (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/techniques.md`: new row `T15 Observe–infer–conclude | clinical, diagnosis`; `reference/traps.md`: allow trap entries for reasoning errors where the trap brief documents them (they still need a refuting claim).
**Status.** test-first (EXP-013).

## DP20 Error-type self-diagnosis tap
**Rule.** After a first miss on a key probe, one node asks "What went wrong?" with four pre-written answers (did not know the idea / knew it, slipped / used the wrong approach / misread the stem); each routes to a short repair of that kind before the retry. The report compares the learner's self-diagnosis with the trap's authored error type ("you called it a slip, but the mistake was the idea itself").
**Sources.** GM1 P7, P22: `skills/student-learning/stuck-and-error-diagnosis-coach/SKILL.md`, `skills/self-regulated-learning/error-analysis-protocol/SKILL.md`, `progressive-hint-ladder/SKILL.md`.
**Evidence claimed.** Hattie & Timperley 2007; Tulis et al. 2016; Metcalfe 2017; Siegler 2002 (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/techniques.md`: new technique row; `reference/report.md`: new "self-diagnosis" rule keyed on the choice index of the diagnosis node (needs a role or naming convention the report can find, e.g. node ID suffix `_why`); `report` block gains `self_diagnosis` texts. Risk: friction for tired learners, extra node on every miss path.
**Status.** test-first (EXP-014).

## DP21 Near and far transfer bridge
**Rule.** After a key idea is secure, one near-transfer probe (same principle, new surface) and one far-transfer probe (different context, same structure, using a cross-module claim when needed), then three taps: what is the same, what differs, which principle travels. Near right with far wrong is a named report pattern ("works on the cases you saw, not yet on new settings").
**Sources.** GM1 P17: `skills/student-learning/transfer-bridge/SKILL.md`; GM2 P7: `experiential-learning-cycle-designer/SKILL.md`; SO P9: `SKILL.md` Phase 4.
**Evidence claimed.** Gick & Holyoak 1983; Perkins & Salomon 1992; Bransford & Schwartz 1999 (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/techniques.md`: new row `T16 Transfer bridge | consolidate, management`; `reference/report.md`: transfer pattern rule.
**Status.** test-first (EXP-012).

## DP22 If-then plan and metacognitive close
**Rule.** The last node before the end offers 2–3 pre-written implementation intentions keyed to the learner's dominant error type ("If a stem says NOT or EXCEPT, I underline it before reading the options"); the learner taps one and the report repeats it. Optionally, a one-tap "Which idea would you re-check tomorrow?" whose answer the report compares with the path evidence.
**Sources.** GM2 P14: `skills/wellbeing-motivation-agency/implementation-intention-designer/SKILL.md`; SO P9: `SKILL.md` Phase 4; GM1 P22: `stuck-and-error-diagnosis-coach/SKILL.md`.
**Evidence claimed.** Gollwitzer & Sheeran 2006 (d=0.65, 94 studies); Oettingen & Gollwitzer 2010; Flavell 1979; Zimmerman 2002 (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/report.md`: plan rule (the plan options shown are chosen by the module's dominant `error_type` on the path, so the end node's options must be pre-authored per error type; easiest as a fixed set of three per module); `report` block gains `plans`.
**Status.** test-first (EXP-006).

## DP23 Distractor set composition: under- and over-reaction, reasoning levels
**Rule.** Where the topic admits both, a key management probe's two wrong options are one under-reaction (too little, too late, too conservative) and one over-reaction (too much, too early, too aggressive), each a different trap. More generally, the wrong options of a probe represent different kinds of thinking (surface: matches one finding; developing: notices but misapplies; proficient-but-wrong: uses the feature in the wrong setting), so the path reveals the level of reasoning.
**Sources.** SC P2: `SKILL.md` Step 4, `README.md` demo; GM2 P9: `skills/historical-thinking/historical-thinking-assessment-designer/SKILL.md`.
**Evidence claimed.** SC none; Wiliam 2011; Gottlieb & Wineburg 2012 (GM2) (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/traps.md` trap-map probe entries gain `direction: under | over | wrong-target`; `reference/rubric.md` R9 5-anchor mentions it.
**Status.** test-first (EXP-011).

## DP24 Second-miss normalising line and strategy attribution
**Rule.** After a second miss on a key probe, before the second explanation, one short line normalises the difficulty and attributes it to the trap, not the learner ("This one catches most people: the cyanosis points the wrong way"). Feedback after success credits the strategy used ("you used the contrast from earlier"), never ability.
**Sources.** AT P10: `references/teaching-loop.md` (Anti-Patterns 5); GM2 P10, P13: `self-efficacy-builder-sequence/SKILL.md`, `trauma-informed-practice-designer/SKILL.md`; SO P2: `references/evidence-base.md`.
**Evidence claimed.** Bandura 1977/1997; Schunk & Pajares 2009; Lepper & Woolverton 2002 (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/pedagogy.md` §6 Voice: one rule; `reference/techniques.md` T6: second-miss line. Risk: the learner-advocate lens may find it patronising, and it costs words.
**Status.** test-first (EXP-009).

## DP25 Plain language, one term per concept, defined at first use
**Rule.** Many NEET PG candidates read English as an additional language. Tutor lines use plain everyday words around the exam terms (which stay, bolded); one term per concept for the whole module, never alternating synonyms; no idioms or phrasal verbs; an eponym, scoring system or new abbreviation is expanded the first time it carries load, never first inside an option or feedback.
**Sources.** AC P9: `SKILL.md` Step 4 (First-use rule), `references/quality-rubrics.md`; GM2 P15: `skills/eal-language-development/language-demand-analyser/SKILL.md`, `vocabulary-tiering-tool/SKILL.md`, `academic-language-sentence-frame-generator/SKILL.md`.
**Evidence claimed.** Mayer 2017 pre-training; Beck, McKeown & Kucan 2013; Cummins BICS/CALP (claimed, not verified by LORE).
**LORE change.** `reference/pedagogy.md` §6 Voice: add the rule. `factory.py`: warning when an all-caps token (≥ 2 letters) appears in a choice label or feedback before any `say` text in the module shows it with an expansion in parentheses (warning only; common units and drug abbreviations can be whitelisted in config). `reference/rubric.md` R4 5-anchor: "one term per concept". GM2's idea of reply buttons as full reasoning sentences is not adopted: it conflicts with the 12-word label cap and with DP1.
**Status.** adopt-now.

## DP26 One question per node; a vignette ends at the decision
**Rule.** A node asks at most one question, and a case or probe vignette is at most five sentences, ending on the decision question.
**Sources.** SO P7: `SKILL.md` Phase 3 rule 1; SC P8: `SKILL.md` Step 3.
**Evidence claimed.** Graesser & Person 1994; Sweller 1988 (SO); SC none (claimed, not verified by LORE).
**LORE change.** `factory.py` `check_nodes`: error when more than one `say` message ends in "?"; for `role: "probe"`, warning when the last message does not end in "?" (allowing labels like "Your first move?"); warning when the node's messages total more than five sentences. `reference/pedagogy.md` §2 "One idea per node": add "one question".
**Status.** adopt-now.

## DP27 Objectives are observable decisions
**Rule.** Every core objective is written as what the learner does in a situation ("In a tet spell, chooses knee-chest as the first step"), not "understand", "know" or "be aware of". This forces probes that test decisions and makes the report's objective lines concrete.
**Sources.** SC P6: `SKILL.md` Step 1; GM1 (hinge question "what each tap means"): `hinge-question-designer/SKILL.md`.
**Evidence claimed.** None (claimed, not verified by LORE).
**LORE change.** `.claude/agents/module-architect.md` and `reference/module-format.md` objectives: rule text; `factory.py`: warning when a `core` objective's `text` starts with understand / know / be aware / appreciate.
**Status.** adopt-now.

## DP28 Distractor and coverage numbers in the validator
**Rule.** The factory should see, per module, how many distractors each probe offers, how evenly traps are spread, and how many probes test recall only, so weak modules show in numbers before judging.
**Sources.** UM P9: `utils.py` `relaxed_metric`, `hard_metric`, `proportional_metric`, `evaluation.py`; SO P6: `SKILL.md` Phase 3 rule 2; AC P10: `references/practice-design.md`.
**Evidence claimed.** None (claimed, not verified by LORE).
**LORE change.** `factory.py` `validate_module` metrics: `traps_per_probe_mean` (trap choices per probe), `probes_single_trap_share` (target: most probes with 2–3 traps), `key_longest_share` and `key_position_max_share` (from DP1), `retest_form_distinct_share` (from DP5). Metrics only; no score change until thresholds are calibrated on published modules.
**Status.** adopt-now.

## DP29 Exemplar triples at authoring time
**Rule.** Before authoring a segment, the author is shown up to three (wrong model, option, feedback) triples from published modules with similar traps or error types, as models of form only; facts still come only from the claim bank.
**Sources.** UM P6: `RetrieverFactory.py` `KNNRetriever`, `conf/main.yaml`.
**Evidence claimed.** None in repo (claimed, not verified by LORE).
**LORE change (if adopted).** `.claude/skills/lore-factory/SKILL.md` author stage: retrieval step over published modules' traps by `error_type` and wording; author-prompt rule "exemplars show form, never facts". Needs enough published modules first.
**Status.** test-first (EXP-016).

## DP30 Segment goal line, rationale and difficulty ramp
**Rule.** Each non-hook segment opens with a one-line goal ("By the end you can tell pink from blue tet in a stem") and why it matters for the exam; its first probe is answerable by a prepared learner, and difficulty then rises one step at a time; traps segments are mostly hard. The hook keeps its productive-failure design.
**Sources.** GM2 P10, P11, P12: `self-efficacy-builder-sequence/SKILL.md`, `motivation-diagnostic-task-redesign/SKILL.md`, `skills/wellbeing-motivation-agency/flow-state-condition-designer/SKILL.md`; AT P9: `references/quiz-rules.md` (Difficulty Balancing).
**Evidence claimed.** Bandura 1997; Jang, Reeve & Deci 2010; Csikszentmihalyi 1990; Shernoff et al. 2003 (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/pedagogy.md` §5: goal line and difficulty profile per segment type. Conflicts to watch: "ask before tell" (a goal line is a tell message, it must share the node with the first probe) and the tell-run limit.
**Status.** test-first (EXP-015).

## DP31 New technique candidates through the tournament
**Rule.** Lower-evidence button techniques enter the technique table as exploration candidates and survive only if they win: name-recognise-recall for terminology and classifications (GM2 P3); concreteness fading for mechanisms with a route back one stage on error (GM2 P4); a single inversion probe in traps ("what would have to be true for the other answer to be right?", SO P8); a step-down prerequisite probe after a second miss (AT P4, P7); a dedicated source-clash node for PYQ-key conflicts (GM2 P8).
**Sources.** GM2 P3, P4, P8: `three-part-lesson-designer/SKILL.md`, `skills/global-cross-cultural-pedagogies/cpa-sequence-designer/SKILL.md`, `skills/historical-thinking/corroboration-skill-builder/SKILL.md`; SO P8: `SKILL.md` (Perspective-shift battery); AT P4, P7: `references/teaching-loop.md`, `SKILL.md`.
**Evidence claimed.** Lillard 2005; Fyfe et al. 2014; Wineburg 1991, Reisman 2012 (no significant corroboration effect); SO and AT none (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/techniques.md`: one row and recipe each; `scripts/pick_techniques.py` already gives new rows exploration turns and `factory/technique-stats.json` records wins.
**Status.** test-first (EXP-005).

## DP32 Intensity fork at the hook
**Rule.** An opening tap lets the learner choose "walk me through it" or "test me straight", each a pre-authored track.
**Sources.** SO P11: `SKILL.md` Phase 2.
**Evidence claimed.** Kalyuga et al. 2003 expertise reversal (claimed, not verified by LORE).
**LORE change (if adopted).** `reference/pedagogy.md` §5 optional fork. The fast lane already serves the same purpose at lower cost; SO's own analyst predicts a null result.
**Status.** test-first (EXP-017, a null-result check before anyone builds it).

---

## Already in LORE

## DP33 Ask before tell, attempt first
**Rule.** A new idea opens with a probe the learner can attempt; the explanation follows promptly and uses the attempt.
**Sources.** AC P1: `references/course-blueprint.md`, `SKILL.md` Step 4; GM1 P16, P11: `skills/student-learning/productive-failure-protocol/SKILL.md`, `skills/student-learning/retrieve-first-gate/SKILL.md`; SO P1: `SKILL.md`.
**Evidence claimed.** Sinha & Kapur 2021 (g≈0.36); Pan & Carpenter 2023; Rowland 2014 (claimed, not verified by LORE).
**LORE change.** None: `reference/pedagogy.md` §2 (ask before tell, validator-enforced tell-run ≤ 2), T4 and T9 in `reference/techniques.md`. "Explanation refers to the pick" is covered by DP3.
**Status.** already-in-lore.

## DP34 A second explanation differs from the first
**Sources.** AT P4: `references/teaching-loop.md` Anti-Patterns 6; GM1 P20: `skills/explicit-instruction/checking-for-understanding-protocol-designer/SKILL.md`.
**Evidence claimed.** Rosenshine 2012; Wiliam 2011 (claimed, not verified by LORE).
**LORE change.** None: `reference/pedagogy.md` §3, supplied by folded tournament variants.
**Status.** already-in-lore.

## DP35 Confidence taps and hypercorrection notes
**Sources.** GM1 P10: `confidence-calibration-check/SKILL.md`; AC P7: `references/study-mode.md`.
**Evidence claimed.** Koriat & Bjork 2005; Hacker et al. 2008 (claimed, not verified by LORE).
**LORE change.** None: `ask_confidence` and `sure_note` (`reference/module-format.md`), calibration rule in `reference/report.md`. DP7 extends the report side.
**Status.** already-in-lore.

## DP36 Fast lane with objectives guaranteed on every path; within-module fading
**Sources.** AC P11: `SKILL.md` Step 2, `references/practice-design.md`; GM1 P19, P13: `skills/student-learning/fading-manager/SKILL.md`, `skills/memory-learning-science/worked-example-fading-designer/SKILL.md`.
**Evidence claimed.** Kalyuga 2003; van Gog, Paas & Sweller 2010; Renkl & Atkinson 2003 (claimed, not verified by LORE).
**LORE change.** None: `pedagogy.md` §4 fast lane, the validator's "core objective can be skipped" check (`factory.py` `validate_module`), T5 backward fade in `techniques.md`.
**Status.** already-in-lore.

## DP37 Spaced retrieval cards
**Sources.** AC P8: `references/practice-design.md`; GM1 P21: `spaced-practice-scheduler/SKILL.md`; AT P8: `references/fsrs.md`.
**Evidence claimed.** Cepeda et al. 2006; Dunlosky et al. 2013 (claimed, not verified by LORE).
**LORE change.** None: `cards` with `schedule_days: [1, 3, 7, 21]` (`reference/module-format.md`); cards are questions, not re-reading. Path-derived ordering is DP7.
**Status.** already-in-lore.

## DP38 PYQ key versus current source: teach both
**Sources.** GM2 P8: `corroboration-skill-builder/SKILL.md`; SO P5 (viewpoint questions): `references/question-taxonomy.md`.
**Evidence claimed.** Wineburg 1991; Reisman 2012 (claimed, not verified by LORE).
**LORE change.** None: `reference/pedagogy.md` §1 and error type E5 in `reference/traps.md`. A dedicated node form is a DP31 candidate.
**Status.** already-in-lore.

## DP39 Distractor-first design and a path-derived per-trap report
**Sources.** SC P7: `SKILL.md` Step 2; UM P7, P12: `misconception_selection.py`, `PromptFactory.py`; GM1 P1, P3: `hinge-question-designer/SKILL.md`, `formative-assessment-loop-designer/SKILL.md`.
**Evidence claimed.** None in SC/UM; Black & Wiliam 1998 (claimed, not verified by LORE).
**LORE change.** None: `reference/traps.md` (trap brief, trap map, ≥ 2 probes per trap, validator-enforced) and `reference/report.md` trap statuses (`avoided`, `fell_recovered`, `fell_repeated`) with texts that name the wrong model.
**Status.** already-in-lore.

---

## Rejected

## DP40 Free recall or generation before options
Typed recall, teach-back, "explain in your own words", free-recall summaries. **Sources.** AC (rejected list): `references/study-mode.md`; GM1 P11, P15 preference: `retrieve-first-gate/SKILL.md`, `skills/student-learning/teach-back-evaluator/SKILL.md`; SO Phase 4: `SKILL.md`; AT: `references/teaching-loop.md`. **Violates** constraint 1 (buttons only). The honest substitute is T12 chip-building and DP15 picks; the report must not claim recall strength (see below). **Status.** rejected.

## DP41 Runtime generation or grading
Live distractor, hint, contradiction-question or feedback generation; an LLM ranker or grader as a live gate; AI-generated checkpoint items. **Sources.** UM: `ranking_model.py`, `openai_finetune/`; SO: `SKILL.md` Phase 0–3; GM1: `skills/student-learning/*`. **Violates** constraint 2 (no runtime AI). Usable only at build time (DP2's pairwise check, DP29). **Status.** rejected.

## DP42 Cross-session learner state
FSRS state per learner in files, mastery over 90 days, fading across sessions, calibration trends across weeks. **Sources.** AT: `references/fsrs.md`, `SKILL.md` (Dashboard); GM1: `fading-manager/SKILL.md`, `skills/student-learning/srl-session-wrapper/SKILL.md`, `weekly-agency-review/SKILL.md`. **Violates** constraint 4 (feedback computed only from this module's path) and, as built, constraint 2. Only the fixed lookup in DP7 survives. **Status.** rejected.

## DP43 Learner-profile and learning-style adaptation
Style questionnaires, analogy-domain matching, generated explanations per profile. **Sources.** AT: `SKILL.md` (learner profile); GM2: `docs/EXCLUSIONS.md`. **Violates** constraint 2 (per-learner generation) and the evidence (the repo itself excludes learning styles); banned text in DP14. **Status.** rejected.

## DP44 Timing-based behaviour
Detecting rapid clicking, wait time, "silence as a move". **Sources.** AT: `references/teaching-loop.md`; GM1: `intelligent-tutoring-dialogue-designer/SKILL.md`. **Violates** constraint 4: the path records choices, retries, confidence, hints and fast lanes, not timing, and a tap UI gives silence no meaning. **Status.** rejected.

---

## What a path cannot prove

The report must say these things plainly, in its fixed texts, and never imply more:

1. **One correct tap can be a guess.** With 3–4 options a random tap is right 25–33% of the time; "Sure" lowers but does not remove this. A level built on one or two first answers is weak evidence, and the report says so.
2. **Recognition is not recall.** Every answer is a choice among shown options. The path shows the learner can pick the right option, not that they could produce it unprompted, as the exam's harder stems and the ward demand.
3. **Same-session is not retention.** The "delayed" re-test comes minutes later in the same module. `fell_recovered` means repaired for now; whether it holds at day 7 or on exam day is unknown until the review cards are answered (and those answers are outside this module's path).
4. **Confidence is self-report.** Sure / Guessing is what the learner tapped, not a measured certainty; some learners always tap one of them.
5. **Not met is not known.** A trap never offered on the learner's path (fast lane, `deeper` skipped) is `not_met`, not `avoided`. The report lists it neutrally and makes no claim of strength.
6. **A wrong tap has more than one cause.** The path cannot tell a misconception from a misread stem, a slip of the finger or a lapse of attention. The authored wrong model ("you treated TOF as a list of shunts") is the most likely reading, so the report phrases it as "your answers fit ...", not as fact, especially after a single fall.
7. **Hint use is ambiguous.** A hint may be help-seeking, curiosity or caution. Hint counts describe behaviour, not ability.
8. **The path shows nothing about reading.** A learner may tap through feedback without reading it; the report cannot know whether a repair was read.
9. **Small numbers.** An error-type profile built from two falls, or a calibration label built from three confidence answers, is a hint for what to review, not a diagnosis.
10. **No exam prediction.** No level or headline predicts a NEET PG score or rank, and the thresholds in `reference/report.md` are authored rules, not validated cut-offs.
11. **The tutor can be wrong too.** Feedback is only as good as the verified claim bank; ⚠ unverified items and PYQ-key conflicts are marked, and the report's fact sentences cite claims like any tutor message.
12. **Factory scores are not learning.** Judge scores and simulated learners (`reference/personas.md`) are proxies. Only the exported session records (`reference/report.md`, "The session record") across real learners, especially re-test and review-card outcomes, can show whether a design choice helps.

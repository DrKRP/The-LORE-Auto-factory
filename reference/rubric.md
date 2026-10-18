# Judging rubric

Used by `dialogue-judge` to score segment variants (segment mode) and whole modules (module mode). Scores are 1–5 per criterion; anchors below. Judges see variants under blind labels and never learn which technique wrote which.

## Gates (any failure disqualifies the variant)

| Gate | Fails when |
|---|---|
| G1 Fidelity | A message states a fact with no claim, or says more than its claims (numbers, qualifiers, "most common", "first-line") |
| G2 Unverified on core path | An unverified claim is taught outside a `deeper` branch or exam-trap node, or without `flag: "unverified"` |
| G3 Broken graph | A `next` points nowhere, or a node has no way forward |
| G4 Not buttons-only | Anything asks the learner to type, or depends on a model at run time |

## Criteria

| id | criterion | weight | 1 | 3 | 5 |
|---|---|---|---|---|---|
| R1 | Learner does the thinking | 3 | Mostly telling; choices are "Next" | Probes before most ideas | Every idea is reached by the learner's own commitment before it is told |
| R2 | Trap work | 3 | Filler distractors, generic "incorrect" | Real traps, short feedback | Each wrong option is one trap from the trap map, as plausible as the key to someone holding that wrong model; feedback names the wrong model, says why tempting, refutes with the error type's repair, re-tests later in another form |
| R3 | Objective coverage | 2 | Objectives missed | All covered on main path | All covered on every path, at the right depth |
| R4 | Clarity and load | 2 | Long, dense, several ideas per node | Mostly one idea per node | Every node one idea, tight, ≤ 60 words, plain words |
| R5 | Adaptivity | 2 | One path for all | Some remediation | Fast lane, hint ladder, a different second explanation |
| R6 | Exam alignment | 2 | Ignores PYQ asks | High-yield covered | High-yield drilled in exam form, traps explicit |
| R7 | Clinical authenticity | 1 | Abstract recitation | Some cases | Decisions framed as real clinical moments |
| R8 | Voice and engagement | 1 | Flat or patronising | Pleasant | Warm, sharp, makes the learner want the next node |
| R9 | Diagnosticity | 2 | The path says little about what the learner believes | Most choices reveal something | Every choice separates one wrong model from the right one, so the path alone tells a teacher what this learner believes; the report (module mode) says it precisely and usefully |

Weighted score = Σ(score × weight) / Σ(weight), on the 1–5 scale.

## Judge output (`judging/<S>-<judge>.json`)

```json
{
  "segment": "S3",
  "judge": "j1",
  "lens": "learning-scientist",
  "variants": {
    "a": {"gates": [], "scores": {"R1": 4, "R2": 5, "R3": 4, "R4": 3, "R5": 4, "R6": 4, "R7": 5, "R8": 4},
           "weighted": 4.19, "best_parts": ["node case_m2: tempting-then-refute feedback"], "flaws": ["node exp1: 84 words"]},
    "b": {"gates": ["G1: node k2 says 'always' but K44 does not"], "scores": {}, "weighted": 0}
  },
  "ranking": ["a", "c", "b"],
  "merge_ideas": ["a's vignette with c's fast lane"]
}
```

`best_parts` and `merge_ideas` feed the editor's merge and fold decisions.

## Module mode (`review.json`)

Same criteria for the assembled module, plus `segments`: a 1–5 score and one-line reason per segment, and `weakest`: the segment IDs most worth rebuilding.

## Lenses

Run each judge under a different lens so the panel disagrees usefully:

- **learning-scientist**: retrieval, generation, feedback quality, cognitive load.
- **examiner**: NEET PG / INI-CET alignment, PYQ traps, precision of wording.
- **learner-advocate**: a tired final-year student at 1 a.m.: is it clear, quick, motivating, never patronising?

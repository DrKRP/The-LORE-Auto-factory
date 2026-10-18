# Traps: the brief, the branch analysis, the error taxonomy

LORE modules are **distractor-first**. Before any conversation is designed, the factory writes a primary brief of the mistakes learners make and the traps exams set for this topic (`trap-brief.md`), then analyses every trap as a branch (`trap-map.json`). Segments, probes, feedback and the end-of-module report are all built on that analysis.

## Error taxonomy

Every trap gets exactly one primary error type. The type drives the repair strategy and the report's "how you tend to go wrong" profile.

| id | error type | the learner… | repair that works |
|---|---|---|---|
| E1 | Look-alike confusion | mixes this up with a similar disease, sign, drug or structure | contrasting cases: put both side by side, name the discriminating feature |
| E2 | List error | adds an item that is not part of a set, or drops one that is | rebuild the set from its logic; "which is NOT" retest |
| E3 | Reversed mechanism | gets a direction, cause or effect backwards | predict-then-show; trace the mechanism step by step |
| E4 | Over-generalised superlative | stretches "most common", "classic", "gold standard" or "always" beyond what the source says | show the exact qualifier; a counter-case |
| E5 | Outdated or PYQ-key conflict | answers with an old key that current sources no longer support (or the reverse) | teach both: "PYQs expected X; current source says Y" |
| E6 | Number swap | confuses figures, ranges, percentages, timings | anchor the number to something meaningful; retest in another form |
| E7 | Qualifier blindness | ignores age group, setting, first-line vs drug of choice, adult vs child | highlight the qualifier; contrast the two settings |
| E8 | Wrong investigation level | picks a screening or supportive test where the confirmatory / gold standard is asked, or the reverse | ladder of tests with what each answers |
| E9 | Sequence or priority error | does the right things in the wrong order, or misses the first step | order the steps; ask "what first, and why" |
| E10 | Association mismatch | links a syndrome, gene, sign, organism or eponym to the wrong condition | pair recall; contrast with the condition it really belongs to |

Add a type only when a trap fits none of these; give it the next ID.

## `trap-brief.md` (written by `trap-scout`)

```markdown
# Trap brief: <Topic>

## TR1
- trap: ASD is one of the four components of TOF
- wrong_answer: "Atrial septal defect" offered as a component
- where: "Which of the following is NOT a component of TOF" stems; component lists
- error_type: E2
- why_tempting: ASD is a common, familiar shunt lesion and appears in "pentalogy"
- frequency: 2 recall sources (RUHS 2022 key; cerebellumacademy)   # pattern-only evidence
- seen_at: https://…, https://…
- refuted_by: K3, K13, K77            # claim-bank IDs; verified ones first
- yield: high                          # high | medium | low
```

- Sources: `pattern.md`, the note's ⚠ Exam notes, and new searches on exam-pattern sites (`reference/sources.md`, "Exam-pattern only"). These decide *which traps exist*; they never supply facts.
- A trap no verified claim can refute is listed under `## Unrefutable` and does not become a branch. A trap refuted only by unverified claims may become an exam-trap branch shown with ⚠.

## `trap-map.json` (written by `distractor-analyst`)

The branch analysis: for each trap, how it will be surfaced, diagnosed, repaired, re-tested and reported.

```json
{"traps": [{
  "id": "TR1", "trap": "ASD is one of the four components of TOF", "error_type": "E2", "yield": "high",
  "refuted_by": ["K3", "K13", "K77"],
  "objectives": ["O2"],
  "probes": [
    {"form": "recognition", "stem_idea": "Which is NOT part of classic TOF?",
     "correct": "Atrial septal defect", "distractor_set": ["Overriding aorta", "RV hypertrophy", "VSD"],
     "note": "the trap here is answering one of the true components"},
    {"form": "vignette", "stem_idea": "Echo report lists four findings; which one does not belong to TOF?"}
  ],
  "diagnoses": "Learner holds a 'list of shunts' model rather than the outflow-obstruction model.",
  "repair": {"strategy": "E2: rebuild the four from one malaligned septum", "claims": ["K3", "K13"]},
  "retest": "later probe in a different form (vignette or 'which is NOT')",
  "co_traps": ["TR4"],
  "report_hint": "If fallen twice: they are memorising lists, not the anatomy."
}],
 "probe_plan": "one paragraph: which traps share probes, the order, which traps are the backbone"}
```

Rules:

- Every trap gets **at least two probes in different forms**: the first surfaces it, the later one re-tests it. Recovery is only credited on the re-test.
- **One error per distractor.** Each distractor option corresponds to exactly one trap (or is clearly a correct-adjacent `partial`). An option that could be wrong for two reasons diagnoses nothing.
- Distractors are written in the exam's own vocabulary and must be plausible to someone holding the trap's wrong model.

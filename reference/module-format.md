# Module formats

A **module** is one topic taught as a pre-authored, clickable, branched conversation: the tutor speaks, the learner taps one of 2–4 pre-written replies, and each reply leads to its own next node. **Buttons only, no runtime AI**: the learner never types, and nothing the learner sees is generated or judged by a model at run time. Modules are self-contained: the file carries its claims, traps, references, review cards and the pre-authored end-of-module report, so the player needs nothing else.

All work files for one module live in `workshop/<subject>/<topic-slug>/`; the finished module is `modules/<subject>/<topic-slug>.json`.

| File | Written by | Purpose |
|---|---|---|
| `claim-bank.json` | `scripts/factory.py bank` | Every cited sentence of the note, as a claim `K<n>`: the only facts a module may teach |
| `trap-brief.md` | trap-scout | The primary brief: every common mistake and exam trap for the topic (`reference/traps.md`) |
| `trap-map.json` | distractor-analyst | Branch analysis: how each trap is surfaced, diagnosed, repaired, re-tested, reported |
| `blueprint.md`, `blueprint.json` | module-architect | Objectives, traps, segments, routing |
| `variants/<S>/<tech>.json` | dialogue-author | One technique's version of one segment |
| `blind/<S>/<label>.json`, `blind/<S>/map.json` | `scripts/blind.py` | The same variants under shuffled labels, techniques stripped |
| `judging/<S>-<judge>.json` | dialogue-judge | Rubric scores per blind variant |
| `segments/<S>.json` | module-editor | The chosen / merged / folded segment |
| `selection/<S>.json` | module-editor | Decision, labels used, lesson |
| `report.json` | report-author | The pre-authored end-of-module report texts (`reference/report.md`) |
| `module.json` | `scripts/factory.py assemble` | Segments stitched into one graph |
| `validation.json` | `scripts/factory.py validate` | Errors, warnings, metrics |
| `dialogue-verification.md` | dialogue-verifier | PASS / FAIL per fact-bearing message |
| `sim/<persona>.md` | learner-sim | One simulated learner's walk |
| `review.json` | dialogue-judge (module mode) | Whole-module rubric scores, weakest segments |
| `scorecard.json` | `scripts/factory.py score` | Composite score per round; best round |
| `best/` | orchestrator | Copy of `segments/` and `module.json` from the best round so far |
| `run-log.md` | orchestrator | Stages run, decisions, scores |

## Claim bank (`claim-bank.json`)

Built from the **finished note**, not from the ledger: the note is what survived verification and rescue.

```json
{
  "module": "paediatrics/tetralogy-of-fallot",
  "note": "notes/paediatrics/tetralogy-of-fallot.md",
  "references": {"1": {"title": "StatPearls — Tetralogy of Fallot …", "url": "https://…", "tier": 1}},
  "claims": {
    "K4": {"text": "Classic TOF has four components: …", "refs": ["1"], "status": "verified",
            "section": "High-yield", "hy": true, "kind": "fact"}
  }
}
```

- `status`: `verified`, or `unverified` when the note tags the sentence ⚠ Unverified.
- `hy`: the sentence sits in High-yield or the Most-common table.
- `kind`: `fact`, `exam-note` (from ⚠ Exam notes), or `table`.

## Segment (`variants/<S>/<tech>.json`, `segments/<S>.json`)

A segment is one stage of the learning journey (see `blueprint.json`). Node IDs are local to the segment; the assembler prefixes them with the segment ID.

```json
{
  "segment": "S3",
  "technique": "T2",
  "entry": "case",
  "nodes": {
    "case": {
      "role": "probe",
      "objectives": ["O3"],
      "ask_confidence": true,
      "say": [
        {"text": "A 2-year-old with known TOF turns deeply blue and limp after a long crying bout.", "claims": []},
        {"text": "Your very first move?", "claims": []}
      ],
      "choices": [
        {"label": "Knee-chest position", "next": "case_ok", "kind": "correct"},
        {"label": "Start IV furosemide", "next": "case_t7", "kind": "trap", "trap": "TR7"},
        {"label": "Not sure, give me a hint", "next": "case_hint", "kind": "help"}
      ]
    },
    "case_ok": {
      "role": "feedback",
      "say": [{"text": "Yes. Knee-chest positioning raises systemic vascular resistance.", "claims": ["K44"]}],
      "choices": [{"label": "Next", "next": "@next", "kind": "continue"}]
    },
    "case_t7": {
      "role": "feedback",
      "say": [{"text": "…", "claims": ["K44"]}],
      "sure_note": {"text": "You were sure, so this one is worth a second look: …", "claims": ["K44"]},
      "choices": [{"label": "Try again", "next": "case", "kind": "retry"}]
    }
  },
  "cards": [
    {"q": "First manoeuvre in a tet spell?", "a": "Knee-chest position, to raise SVR.", "claims": ["K44"], "objective": "O3"}
  ]
}
```

### Node fields

| Field | Required | Meaning |
|---|---|---|
| `role` | yes | `probe` (learner commits to an answer; must offer a correct choice and at least one trap), `explain`, `feedback`, `hint`, `case`, `recap`, `bridge`, `end` |
| `say` | yes | 1–3 messages. Each has `text` and `claims` (claim IDs; `[]` for questions, prompts, encouragement) |
| `say[].device` | no | `true` for a mnemonic, analogy or image cue. It may not state a fact the cited claims do not |
| `say[].flag` | no | `"unverified"`; required when the message cites an unverified claim. The player shows ⚠ |
| `choices` | yes unless `end` | 1–4 replies. Each has `label`, `next`, `kind` |
| `objectives` | probes | Objective IDs this node teaches or tests |
| `ask_confidence` | no | Player asks "Sure / Guessing" after the choice and before the next node |
| `sure_note` | no | Extra message shown on a feedback node only when the learner said "Sure" (hypercorrection) |
| `end` | end node | `true`; no choices |

### Choice fields

| Field | Meaning |
|---|---|
| `label` | What the learner taps; ≤ 12 words. A distractor label is an option, not an assertion, so it carries no claims |
| `next` | A node ID in this segment, or `@next` (next segment's entry), `@S<k>` (a route the blueprint allows), `@end` |
| `kind` | `correct`, `partial`, `trap` (needs `trap: "TR<n>"`; probe nodes only), `help` (hint), `continue`, `retry`, `skip` (fast lane), `deeper` (optional detail), `agency` ("why?", "tell me more") |
| `trap` | On `kind: "trap"`: the trap this option diagnoses. One trap per option |

No other node or choice fields exist: the validator rejects anything else, so nothing can ask the learner to type or call a model.

### Cross-module claims

A bridge or contrast node may cite a claim from another **published** module as `<subject>/<slug>#K<n>`. Facts about another topic come only that way.

## Assembled module (`module.json`, `modules/<subject>/<slug>.json`)

```json
{
  "schema": "lore.module/v1",
  "id": "paediatrics/tetralogy-of-fallot",
  "title": "Tetralogy of Fallot",
  "subject": "paediatrics",
  "exam": "NEET PG / INI-CET",
  "version": 1,
  "built": "2026-10-18",
  "status": "published",
  "quality": {"composite": 4.2, "round": 2},
  "objectives": [{"id": "O1", "kud": "know", "text": "…", "core": true}],
  "traps": [{"id": "TR1", "trap": "…", "error_type": "E2", "objectives": ["O2"], "yield": "high"}],
  "segments": [{"id": "S1", "title": "…", "type": "hook", "entry": "S1.start", "technique": "T2+T6", "decision": "merge"}],
  "start": "S1.start",
  "nodes": {"S1.start": {"…": "…"}},
  "claims": {"K4": {"text": "…", "refs": ["1"], "status": "verified"}},
  "references": {"1": {"title": "…", "url": "…", "tier": 1}},
  "cards": [{"q": "…", "a": "…", "claims": ["K44"], "objective": "O3", "schedule_days": [1, 3, 7, 21]}],
  "report": {"…": "pre-authored texts, see reference/report.md"}
}
```

`claims` holds only the claims the module cites; `references` only the references those claims use.

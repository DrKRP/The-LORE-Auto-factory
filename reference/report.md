# The end-of-module report

When a learner finishes a module, the app shows a report built **only from their path**: the buttons they tapped, retries, Sure / Guessing taps, hints, fast lanes. Every sentence is pre-authored inside the module (`report` block); the app only counts and selects. No AI runs at report time.

`scripts/factory.py render-report` and `player/index.html` implement the same rules below; keep them in sync.

## What the path records

Each step: `{node, choice, kind, trap, sure, objectives}`, in order. `kind` is the choice kind (`correct`, `partial`, `trap`, `help`, `skip`, …); `trap` is the trap ID on a `kind: "trap"` choice; `sure` is true, false or null.

## Rules

**Encounters.** A probe node is *encountered* the first time the learner answers it; only that first answer counts for mastery (retries count for help-seeking).

**Trap status** for each trap in the module, over the probes that offer it, in path order:

| status | when |
|---|---|
| `not_met` | no probe offering the trap was encountered |
| `avoided` | encountered, never chosen |
| `fell_recovered` | chosen at least once, and the **last** encounter of a probe offering it was answered correctly |
| `fell_open` | chosen, and not followed by a correct answer on a later probe offering it (fallen and not yet shown fixed) |

**Objective mastery** for each objective, over first answers on probes tagged with it:

| level | when |
|---|---|
| `secure` | all first answers correct, none "Sure" and wrong; or a fast lane was earned (correct + Sure on the diagnostic) |
| `gap` | at least half the first answers wrong and the latest one still wrong, or any trap linked to the objective is `fell_open` |
| `shaky` | anything else (some misses, or right but Guessing on most) |
| `unseen` | no tagged probe answered |

**Error-type profile.** Count traps fallen into (`fell_recovered` + `fell_open`) by `error_type`. Each type with ≥ 2 falls shows its `error_types` text; with exactly one, the trap's own text covers it.

**Calibration.** Over first answers on probes that asked for confidence: `sure_wrong` ≥ 2 → `overconfident`; `guess_right` ≥ 3 and `sure_wrong` = 0 → `underconfident`; otherwise `calibrated` if at least one answer was "Sure", else no calibration line (only when at least 3 confidence answers exist).

**Confident errors (DP7).** Traps the learner fell into while tapping Sure are listed first, marked "you were sure", and their objectives' cards come first in the review order.

**Cold evidence (DP11).** A first answer is *hinted* if the learner opened a hint on that probe before answering, and *cold* if the probe offers no hint at all. The report shows cold right / cold total. `hinted_only` = objectives answered right only after a hint, never right unaided.

**Help.** Hints used (taps on a `help` or `agency` choice, e.g. "Show me why") ≥ 3 → `hints_heavy`; else any `hinted_only` objective → `hinted_only`; else 0 hints and ≥ 1 trap fallen → `hints_none`; otherwise nothing.

**Pace.** Any fast lane taken → `fast_lane`.

**Next steps.** Review cards for confident-error objectives first, then `gap`, then `shaky`, then the rest. Plus `next_steps.gap` text if any gap exists, else `next_steps.clear`.

## The `report` block (pre-authored by `report-author`)

```json
"report": {
  "headline": {"strong": {"text": "…", "claims": []}, "mixed": {…}, "weak": {…}},
  "objectives": {"O2": {"secure": {"text": "…", "claims": []}, "shaky": {…}, "gap": {…}}},
  "traps": {"TR1": {"avoided": {…}, "fell_recovered": {…}, "fell_open": {…}}},
  "error_types": {"E2": {"text": "You tend to add familiar items to fixed lists …", "claims": []}},
  "calibration": {"overconfident": {…}, "underconfident": {…}, "calibrated": {…}},
  "help": {"hints_heavy": {…}, "hints_none": {…}, "hinted_only": {…}},
  "pace": {"fast_lane": {…}},
  "next_steps": {"gap": {…}, "clear": {…}}
}
```

- Headline: `strong` = no gaps and ≤ 1 shaky; `weak` = gaps in ≥ 1/3 of core objectives; else `mixed`.
- Each entry is a message `{text, claims}`. Texts that restate a fact cite claims like any tutor message and are fact-checked by the dialogue-verifier.
- Trap texts name the wrong model, not just the wrong answer ("You treated TOF as a list of shunts…"), and say what to do next.
- `error_types` covers every error type used by the module's traps.
- `not_met` and `unseen` need no text; the app lists them neutrally.

## The session record (for the app owner)

The player can export the session: `{module, version, started, finished, path: [...], report: {computed statuses, levels and the selected texts}}`. That record is the raw material for later analytics: which traps learners fall into, which repairs work, which branches nobody takes.

The `strong` headline is shown with zero or one shaky objective, so its text must not assume a shaky item exists.

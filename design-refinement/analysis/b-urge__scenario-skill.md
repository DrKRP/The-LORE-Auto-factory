# Analysis: b-urge/scenario-skill

## 1. What it is
- A very small Claude skill (`/scenario`, MIT-ish: the README says "MIT (or replace with your preferred license)") that takes one learning objective and outputs a single-step branching scenario: a 3-5 sentence workplace dilemma, exactly three distinct choices (one correct, two realistic failure modes), and for each a Consequence plus Corrective Feedback, as a Markdown table and a JSON block with `is_correct`.
- It is one decision deep (no second-level branching), contains no research citations and no tracking. Its value is a tight authoring recipe, and it is already pre-authored and button-shaped, so nearly all of it transfers.
- Demo in the README: AI-assistant-generated code the learner does not understand. Choices: move on, ask for an explanation, or delete everything and hand-write it.

Files read: `SKILL.md`, `README.md` (the whole repo is these two files).

## 2. Transferable principles

- P1 Consequence before correction: each option leads to a concrete, situation-specific consequence ("a login error appears and you lose 40 minutes"), and only then to the corrective takeaway. In LORE: the feedback node's first message shows what happens next in the case, the second explains the principle. For wrong picks the consequence is the tempting-then-refute opening, made vivid; for NEET PG, the consequence is the patient outcome ("the child's saturation keeps falling"). Needs claims where the consequence is a clinical fact; presentation details (the setting, the time lost) need none. — source: `SKILL.md` Step 4 "Consequence ... Concrete and specific to the situation, not a generic 'this was wrong.'" — evidence claimed: none.
- P2 Over-correction as a first-class distractor: of the two wrong options, one is the "too little" mistake and one the "too much" mistake (do nothing, versus throw everything out). The demo's option 3 ("delete everything and rebuild by hand") is an overcorrection that costs the lesson. In clinical terms: undertreatment versus overtreatment, too-early versus too-late, a conservative step versus an over-aggressive one. Author checklist: each key probe has one under-reaction and one over-reaction misconception where both exist. — source: `SKILL.md` Step 4 ("Two that represent different, realistic failure modes"); `README.md` demo — evidence claimed: none.
- P3 Distinct failure modes, not shades of one action: the two wrong options must differ in kind, each tied to a different misconception ID. LORE requires "at least one choice per misconception"; add the rule "no two wrong options in one probe map to the same `misconception`". — source: `SKILL.md` Step 4 "genuinely distinct, not three shades of the same action" — evidence claimed: none.
- P4 Don't telegraph the answer: neither the dilemma text nor the choice text signals which is right (no hedges on wrong options, no "best", no length asymmetry). Add the lint and a blind-judge check. — source: `SKILL.md` Step 3 "Avoid telegraphing", Step 4 "Don't label which is correct in the choice text" — evidence claimed: none.
- P5 Corrective feedback without shame, per option: the correct choice's feedback reinforces why it worked; wrong choices' feedback names the misstep and points to the better approach. Already in LORE pedagogy §3; this repo adds "reinforce on the correct pick too" (a short why-it-worked, not "Yes."). — source: `SKILL.md` Step 4 — evidence claimed: none.
- P6 Objective sharpening gate before authoring: reject objectives that are not observable ("communication") and rewrite them into "does X in situation Y" before any dialogue is written. LORE's architect writes objectives; this adds a check that each objective is an observable decision. In the blueprint, each objective gets a `decision` field ("In a tet spell, the learner chooses knee-chest as the first step"). — source: `SKILL.md` Step 1 — evidence claimed: none.
- P7 Analyse the objective for the common ways people get it wrong before writing: this is LORE's distractor-first brief, so it confirms the approach. Specifically: the failure modes become the options. — source: `SKILL.md` Step 2 — evidence claimed: none.
- P8 Dilemma length and endpoint: 3-5 sentences, ends at the moment the decision must be made, in a realistic role, setting and stakes. For hook and clinical vignettes: every vignette's last message is the decision question, and the vignette is at most 5 sentences across at most 2 messages (<= 60 words each already). — source: `SKILL.md` Step 3 — evidence claimed: none.
- P9 Two-artifact output (human-reviewable table plus machine JSON with a hidden key): for the factory, a per-probe review table for human or judge reading with the answer key withheld, so blind judges cannot be biased by labels. Matches `blind.py`. Add the consequence and feedback columns to what `blind.py` shows. — source: `SKILL.md` Step 5 — evidence claimed: none.

## 3. Rejected

- Exactly three choices every time: LORE allows 2-4. Three is a good default, but a fixed three would remove the two-option fast-lane probes and four-option NEET PG stems, which match the exam format.
- A single decision with no second-level consequences: LORE needs multi-step branches with retry, hint and re-test. The scenario is a one-shot; its form must be extended, not copied.
- Workplace framing: the domain is clinical; only the structure carries over.
- Asking the user for the objective and inferring one if vague at runtime: the factory architect owns objectives from research.
- `is_correct` boolean: too coarse. LORE's choice `kind` (correct, partial, misconception) with a misconception ID is richer.
- No confidence, no hints, no tracking: the repo has no adaptive mechanism to port.
- Licence: unclear ("MIT or replace with your preferred license"). Take no text verbatim.

## 4. Concrete changes for the LORE factory

| Principle | Where | Change |
|---|---|---|
| P1 | `reference/pedagogy.md` §3 and `reference/rubric.md` R2 | Rule: feedback on a wrong pick opens with the consequence of that action in the case (one message), then the tempting-why and refutation. R2 anchor 5 adds "feedback shows what happens next in the case, specific to the pick". Where the consequence is a clinical fact it cites claims; if no claim supports it, the consequence is stated as "this does not address X" with no outcome. |
| P2 | `reference/techniques.md` T2 and `blueprint.json` | Add to the misconception list a `direction` field: `under`, `over`, or `wrong-target`. Authoring rule: each key probe with 2+ wrong options has at least one `under` and one `over` where the topic admits both. Validator: count key probes with 3+ choices that have two wrong options with the same `direction` (warning). |
| P3 | Validator | Error if two choices in one probe carry the same `misconception` ID; warning if two wrong options have near-identical labels (shared first 3 words). |
| P4 | Validator and `reference/rubric.md` | Lint: a probe whose correct label contains a hedge-free absolute while distractors contain hedges, or the reverse, or whose correct label is the only one with a number or a drug dose. Add a judge question "could you pick the answer without reading the vignette?" to R1 anchors. |
| P5 | `reference/pedagogy.md` §3 | Add: correct-pick feedback gives one line of why it worked (cited), not "Yes." |
| P6 | `reference/module-format.md` blueprint section and validator | Objectives carry `decision`: a sentence of the form "In <situation> the learner <chooses/identifies/orders> <X>". Validator: every `core` objective has non-empty `decision`; reject if it starts with "understand", "know", "be aware". |
| P7 | None | Confirms the distractor-first constraint; no change. |
| P8 | Validator | Vignette node length: at most 5 sentences across the node's messages for `case`-role nodes (warning); last message of a `case` node must end with "?" (error). |
| P9 | `scripts/blind.py` | Render for judges a per-probe table: situation, options (unlabelled), consequence, feedback; withhold `kind` and `misconception` fields. Judges score "plausible wrong options" blind. |

## 5. Testable hypotheses

- H1: Probes where the two wrong options are one under-reaction and one over-reaction (P2) will score higher on R2 (misconception work) than probes whose wrong options are two shades of the same error, blind-judged.
- H2: Feedback nodes that open with the case consequence of the wrong pick (P1) will be rated higher on R7 (clinical authenticity) and R8 (engagement) than feedback that opens with the explanation, with no loss on gate G1 (fidelity) when unsupported consequences are phrased as "does not address X".
- H3: Probes passing the no-telegraph lint (P4) will show a lower simulated-learner rate of "right for the wrong reason" (correct tap on a probe whose underlying misconception the sim also shows in a later probe) than probes failing it.

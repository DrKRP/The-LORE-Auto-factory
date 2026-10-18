# LORE Auto-factory

Part of **LORE** (Learn Once, Remember Effortlessly). This repository is an **autonomous factory** that turns NEET PG / INI-CET topics into self-contained learning **modules**: pre-authored, clickable, branched tutoring conversations. It runs as a loop of short ticks, each advancing one module by one stage, and it improves its own methods as it goes.

Two pipelines, one accuracy rule:

1. **Research** (`/lore-research`, `.claude/skills/lore-research/SKILL.md`): turns a topic into a **source-first** study note. Every fact is fetched and quoted from an authoritative source *before* it is written, never recalled from memory and cited afterwards.
2. **Conversation** (`/lore-factory`, `.claude/skills/lore-factory/SKILL.md`): turns the verified note into a module, **distractor-first**: a trap brief of the common mistakes and exam traps comes first, then a branch analysis of every trap, then the journey. Several techniques author each segment, blind judges score them, an editor picks, merges or folds the best, then the module gets its pre-authored end-of-module report, is validated, fact-checked against the note, walked by simulated learners and refined until it stops improving.
3. **Design refinement** (`design-refinement/`): studies educational-skills repositories, turns their ideas into hypotheses, and tests them on real segments before they change the factory's rules.

**Product constraints.** Modules are clickable buttons only. There is no AI at run time: no AI grading, feedback or verification while a learner uses a module. Everything the learner sees, including the detailed report on their path, is pre-authored. AI is used only inside this factory, to build and check modules.

Run one tick with `/lore-factory`; run the factory unattended with `scripts/run-factory.sh` (see `README.md`). These are the only research and module workflows in this repository; they take precedence over any general-purpose research or tutoring skill.

## Config

Change limits and models here only; the skills, agents and `scripts/factory.py` read them from this block.

```yaml
budget:
  max_scouts_per_topic: 4        # 1 exam-pattern scout + up to 3 content scouts
  max_fetches_per_scout: 6       # WebFetch calls per scout
  verifier_passes: 1
  max_rescue_claims: 40          # failed claims + gaps sent to the rescue agent per topic
  rescue_fetches: 10             # total WebFetch calls for the rescue agent
models:                          # set in each agent's frontmatter; keep in sync
  scouts: haiku                  # .claude/agents/source-scout.md, exam-pattern-scout.md
  verifier: haiku                # .claude/agents/claim-verifier.md
  rescue: sonnet                 # .claude/agents/rescue-scout.md
  writer: opus                   # .claude/agents/note-writer.md
  planner: sonnet                # .claude/agents/curriculum-planner.md
  trap_scout: sonnet             # .claude/agents/trap-scout.md
  distractor_analyst: opus       # .claude/agents/distractor-analyst.md
  report_author: opus            # .claude/agents/report-author.md
  architect: opus                # .claude/agents/module-architect.md
  author: sonnet                 # .claude/agents/dialogue-author.md
  judge: sonnet                  # .claude/agents/dialogue-judge.md
  editor: opus                   # .claude/agents/module-editor.md
  dialogue_verifier: haiku       # .claude/agents/dialogue-verifier.md
  learner_sim: haiku             # .claude/agents/learner-sim.md
chapter_mode:
  confirm_subtopics_with_user: true   # interactive /lore-research only; the factory never waits
factory:
  max_modules_in_progress: 1     # finish a module before starting the next
  queue_min: 3                   # below this many waiting topics, the planner refills the queue
  planner_batch: 8               # topics the planner adds per refill
  subjects_focus: []             # e.g. [paediatrics, pharmacology]; empty = all 19 subjects
  refresh_after_days: 180        # re-research and rebuild a published module after this long
  max_stage_attempts: 2          # a stage that fails this often blocks its module
tournament:
  variants_per_segment: 3        # techniques competing on each segment
  explore_picks: 1               # of those, how many go to the least-tried techniques
  min_trials_before_exploit: 3   # trials before a technique's win rate is trusted
  judges_per_segment: 2          # blind judges per segment, each with a different lens
refine:
  max_rounds: 2                  # rebuild rounds after the first build
  publish_threshold: 4.0         # composite score (1–5) a module should reach
  min_improvement: 0.1           # a round must beat the best by this much to replace it
module:
  segments: [5, 8]
  max_words_per_message: 60
  max_messages_per_node: 3
  max_tell_run: 2                # most non-interactive nodes in a row
  card_schedule_days: [1, 3, 7, 21, 60]
  sim_personas: [novice, misconceived, strong, guesser]
design_refinement:
  every_n_modules: 2             # after this many published modules, one tick runs a design experiment
```

## Layout

| Path | Holds |
|---|---|
| `modules/<subject>/<topic-slug>.json` | Finished modules (the deliverable) |
| `notes/<subject>/<topic-slug>.md` | Verified study notes (research deliverable, module source) |
| `evidence/<subject>/<topic-slug>/` | Scout quote files, claim ledger, verification, rescue, run log |
| `workshop/<subject>/<topic-slug>/` | Module work files: claim bank, trap brief, trap map, blueprint, variants, judging, segments, report, sims, scorecard |
| `design-refinement/` | Pulled educational-skills repos (not committed), analyses, principles, efficacy experiments |
| `factory/` | Queue, per-module state, technique stats, playbook, status, tick log |
| `sources/` | Tier-0 PDFs the user drops in (textbooks). Empty is normal |
| `reference/` | Source tiers, file formats, note template, pedagogy contract, traps and error taxonomy, report rules, techniques, rubric, personas |
| `scripts/factory.py` | Deterministic steps: state, claim bank, picks, blinding, assembly, validation, scoring |
| `scripts/run-factory.sh` | The unattended loop |
| `player/index.html` | Click through any module in a browser |

`<subject>` is one of the 19 MBBS subject slugs: `anatomy`, `physiology`, `biochemistry`, `pathology`, `pharmacology`, `microbiology`, `forensic-medicine`, `community-medicine`, `ent`, `ophthalmology`, `medicine`, `surgery`, `obgyn`, `paediatrics`, `orthopaedics`, `dermatology`, `psychiatry`, `anaesthesia`, `radiology`.

## The accuracy rule

1. A fact enters the notes only if an agent fetched the page (or read the tier-0 PDF) and captured a **verbatim quote** that supports it.
2. Tier 0 or tier 1: one source suffices. Tier 2 only: two independent sources must agree.
3. Coaching sites and PYQ recalls decide *what to cover* and feed **⚠ Exam notes**; they are never a fact source.
4. Two trusted sources disagree: show both, attributed. For Indian programme / PSM questions list Indian sources (MoHFW, ICMR, NTEP, NACO, NHM) first.
5. A claim that fails verification and cannot be rescued stays in the note tagged **⚠ Unverified** and is listed under "Unverified claims".
6. A module teaches only claims from its note's claim bank, citing their IDs, and says no more than they say. Unverified claims stay off the core path and are shown with ⚠. Conversation agents' own knowledge decides pedagogy, wording, vignette framing and distractors; it never supplies a fact.

## Autonomy rules

- The factory never waits for the user. Where interactive `/lore-research` would ask, the factory decides, logs the decision in the module's `run-log.md`, and moves on.
- The user steers by editing `factory/queue.md` (add or reorder topics), `subjects_focus`, or this config, and stops the loop by creating `factory/STOP`.
- One tick, one stage, one module. Each tick ends by updating `factory/state/` through `scripts/factory.py`, so any tick can be the last and the next session resumes cleanly.
- A stage that fails twice blocks its module (shown in `factory/status.md`); the factory moves on to other work instead of looping.

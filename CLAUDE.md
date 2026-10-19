# LORE Auto-factory

Part of **LORE** (Learn Once, Remember Effortlessly). This repository is an **autonomous factory** that builds **LORE journeys**: self-contained NEET PG / INI-CET learning modules, each a pre-authored, clickable, branched tutoring conversation. It runs as a loop of short ticks, each advancing one module by one stage, and it improves its own methods as it goes.

**Knowledge only (user's rule, 2026-10-19).** Content comes from the factory's own medical knowledge. Nothing is fetched, nothing is fact-checked: no source scouts, no claim verifier, no knowledge checker, no dialogue fact-check. The factory's effort goes into the *journey*: traps, branches, technique tournaments, feedback and the end-of-module report.

The pipeline (`/lore-factory`, `.claude/skills/lore-factory/SKILL.md`):

**note** (written from knowledge) → **trap brief** → **branch analysis** → **design** → **author tournament** → **blind judging** → **pick / merge / fold** → **assemble** → **pre-authored report** → **simulated learners** → **refine** → **publish**.

**Design refinement** (`design-refinement/`) studies educational-skills repositories, turns their ideas into hypotheses, and tests them on real segments before they change the rules.

**Product constraints.** Clickable buttons only. No AI at run time: no AI grading, feedback or verification while a learner uses a module. Everything the learner sees, including the detailed report on their path, is pre-authored.

Run one tick with `/lore-factory`; run the factory unattended with `scripts/run-factory.sh` (see `README.md`).

## Config

Change limits and models here only; the skills, agents and `scripts/factory.py` read them from this block.

```yaml
research:
  mode: knowledge               # knowledge only; no fetching, no fact-checking (user's rule)
concurrency:
  max_parallel_agents: 5         # never more than 5 agents at once (also set in .claude/settings.json)
models:                          # cheap models for grunt work; set in each agent's frontmatter, keep in sync
  knowledge_writer: sonnet       # .claude/agents/knowledge-writer.md
  planner: haiku                 # .claude/agents/curriculum-planner.md
  trap_scout: haiku              # .claude/agents/trap-scout.md
  distractor_analyst: sonnet     # .claude/agents/distractor-analyst.md
  architect: sonnet              # .claude/agents/module-architect.md
  author: haiku                  # .claude/agents/dialogue-author.md
  judge: haiku                   # .claude/agents/dialogue-judge.md
  editor: sonnet                 # .claude/agents/module-editor.md
  report_author: sonnet          # .claude/agents/report-author.md
  learner_sim: haiku             # .claude/agents/learner-sim.md
factory:
  max_modules_in_progress: 11    # modules advanced in parallel (agents are still capped at 5)
  queue_min: 3                   # below this many waiting topics, the planner refills the queue
  planner_batch: 8               # topics the planner adds per refill
  subjects_focus: []             # e.g. [surgery]; empty = all 19 subjects
  refresh_after_days: 180        # rebuild a published module after this long
  max_stage_attempts: 2          # a stage that fails this often blocks its module
tournament:
  variants_per_segment: 3        # techniques competing on each segment
  explore_picks: 1               # of those, how many go to the least-tried techniques
  min_trials_before_exploit: 3   # trials before a technique's win rate is trusted
  judges_per_segment: 1          # blind judges per segment (lens rotates by segment)
refine:
  max_rounds: 1                  # rebuild rounds after the first build
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
| `modules/<subject>/<topic-slug>.json` | Finished LORE journeys (the deliverable) |
| `notes/<subject>/<topic-slug>.md` | Notes written from knowledge (the content each journey teaches) |
| `evidence/<subject>/<topic-slug>/` | `pattern.md` (exam asks) and run logs |
| `workshop/<subject>/<topic-slug>/` | Module work files: claim bank, trap brief, trap map, blueprint, variants, judging, segments, report, sims, scorecard |
| `design-refinement/` | Pulled educational-skills repos (not committed), analyses, principles, efficacy experiments |
| `factory/` | Queue, per-module state, technique stats, playbook, status, tick log |
| `reference/` | Formats, note template, pedagogy contract, traps and error taxonomy, report rules, techniques, rubric, personas |
| `scripts/factory.py` | Deterministic steps: state, claim bank, picks, blinding, assembly, structural validation, scoring |
| `scripts/run-factory.sh` | The unattended loop |
| `player/index.html` | Click through any module in a browser |

`<subject>` is one of the 19 MBBS subject slugs: `anatomy`, `physiology`, `biochemistry`, `pathology`, `pharmacology`, `microbiology`, `forensic-medicine`, `community-medicine`, `ent`, `ophthalmology`, `medicine`, `surgery`, `obgyn`, `paediatrics`, `orthopaedics`, `dermatology`, `psychiatry`, `anaesthesia`, `radiology`.

## Content rules

1. Each topic's note is written by `knowledge-writer` from its own medical knowledge, at standard-textbook level for NEET PG. It names no sources, invents no citations, and states classic exam answers. Where the classic PYQ key differs from current practice, it gives both in ⚠ Exam notes.
2. The note is the content of the journey. Conversation agents teach from it, citing its claim IDs so cards and the report can link back. Their own knowledge decides pedagogy, wording, vignettes and distractors.
3. No fact-checking stage exists. Judges score teaching quality, not factual accuracy.
4. Notes and modules carry `provenance: model-knowledge`.

The source-first research agents (`source-scout`, `claim-verifier`, `rescue-scout`, `note-writer`, `exam-pattern-scout`, `/lore-research`) are kept but unused while `research.mode` is `knowledge`.

## Structural checks (kept)

`scripts/factory.py validate` still checks the graph, because a broken graph is a broken app: no dead ends or unreachable nodes, buttons-only fields, trap coverage, word limits, report completeness. It checks structure only, never facts.

## Autonomy rules

- The factory never waits for the user. Where a choice is needed it decides, logs the decision in the module's `run-log.md`, and moves on.
- **At most 5 agents run at once.** Dispatch in batches of up to 5, and start the next batch only as agents finish.
- The user steers by editing `factory/queue.md` (add or reorder topics), `subjects_focus`, or this config, and stops the loop by creating `factory/STOP`.
- One tick, one stage, one module. Each tick ends by updating `factory/state/` through `scripts/factory.py`, so any tick can be the last and the next session resumes cleanly.
- A stage that fails twice blocks its module (shown in `factory/status.md`); the factory moves on to other work instead of looping.

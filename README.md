# LORE Auto-factory

An autonomous factory that researches NEET PG / INI-CET topics from authoritative sources and turns each one into a **self-contained learning module**: a pre-authored, clickable, branched tutoring conversation. It runs unattended, one small step at a time, and it gets better at teaching as it goes.

**Product constraints.** Buttons only: the learner never types. No AI at run time: no AI grading, feedback or verification in the app. Everything, including the detailed report a learner gets on their path, is written in advance. **Distractor-first:** every module starts from a brief of the topic's common mistakes and exam traps; every branch exists to surface, diagnose and repair one of them.

`CLAUDE.md` holds the config and the rules; this file explains how to run it.

## How it works

```
queue ► research ► traps ► analysis ► design ► author ► judge ► edit ► assemble ► report ► verify ► evaluate ► refine ► publish
         notes,    trap     branch     journey  3 tech-  blind   pick/  stitch +   pre-     every    sims +     rebuild   modules/
         claims    brief    per trap   + traps  niques   panel   merge/ validate   authored line vs  module     weak,     *.json
                   (E1–E10)            per seg  per seg          fold              feedback claims   judge      keep best
```

1. **Queue.** `factory/queue.md` lists topics. When fewer than `queue_min` are waiting, the `curriculum-planner` picks the next high-yield chapter and appends its topics in teaching order.
2. **Research.** Your original pipeline, unchanged in substance: exam-pattern scout → source scouts → note writer → claim verifier → rescue. In auto mode it never waits for you; it decides and logs why.
3. **Trap brief.** `scripts/factory.py bank` turns the finished note into a **claim bank** (`K1…`, each verified or ⚠ unverified, high-yield flagged). The `trap-scout` then writes the primary brief of every common mistake and exam trap for the topic, from PYQ recalls, coaching material, ⚠ Exam notes and the predictable wrong models. Each trap is typed with the error taxonomy (look-alike, list error, reversed mechanism, over-generalised superlative, outdated key, number swap, qualifier blindness, wrong test level, wrong sequence, wrong association) and tied to the claims that refute it.
4. **Branch analysis.** The `distractor-analyst` designs each trap as a branch: the probes that surface it (at least two, in different forms, so recovery is credited only on a re-test), the distractor wording (one error per option), what choosing it diagnoses, the repair for its error type, and what the report should say.
5. **Design.** The `module-architect` arranges the traps into a journey: objectives (Know / Understand / Do, core or not) and 5–8 segments (hook → retrieve → mechanism → clinical → management → traps → consolidate).
6. **Author (the tournament).** Each segment is written several times by `dialogue-author`s, each with a different technique from `reference/techniques.md` (Socratic ladder, case-first vignette, predict–observe–explain, productive failure, worked example and fading, refutation, contrasting cases, self-explanation, retrieval gate, exam-trap drill, erroneous example, learner-built summary).
7. **Judge.** Variants are stripped of their technique and shuffled (`blind`). A panel of `dialogue-judge`s, each with a different lens (learning scientist, examiner, learner advocate), scores them on `reference/rubric.md`. Fidelity is a gate: one invented fact disqualifies a variant.
8. **Edit.** The `module-editor` **picks** the winner, **merges** the best parts of several (a better vignette from one, a fast lane from another), or **folds** them: a losing technique becomes the *remediation path*, so a learner who misses the first explanation gets a different kind of explanation, not the same one again.
9. **Assemble and validate.** Segments are stitched into one graph and checked deterministically: no dead ends, no unreachable nodes, every core objective on *every* path (fast lanes included), every probe offering a trap, every trap re-tested, the report complete, no field that could ask the learner to type, ≤ 60 words a message, at most 2 non-interactive nodes in a row, unverified claims off the core path.
10. **Report.** The `report-author` pre-writes the end-of-module feedback: for every objective (secure / shaky / gap), every trap (avoided / fell then fixed / fell and still open), every error-type pattern, calibration (overconfident, underconfident) and help-seeking. The app picks among these texts from the learner's path alone (`reference/report.md`), and can export the session record (the path plus the computed report) for you.
11. **Verify.** The `dialogue-verifier` checks every tutor line and every report text against the claims it cites, and flags facts slipped in without a claim (the conversation-side twin of your claim verifier).
12. **Evaluate.** `learner-sim`s walk the module as a novice, a learner holding the traps, a strong student and a guesser; a module-mode judge scores the whole. `score` folds judges, sims and metrics into one composite (1–5).
13. **Refine.** Weak segments get a fresh tournament with the critique, small problems get patched, and the round is kept only if it beats the best so far. Publish at `publish_threshold` or after `max_rounds`.

### How it improves itself

- **Technique stats.** Every tournament updates `factory/technique-stats.json`: per segment type, how often each technique wins and its mean score. `pick` gives most slots to proven winners and one slot to the least-tried technique, so the factory keeps exploring.
- **Playbook.** The editor writes one lesson per tournament to `factory/playbook.md` ("for traps segments, a vignette with the PYQ distractor beat a bare drill because…"). Architects and authors read it before they start.
- **Hill-climbing.** Refinement never ships a regression: the best round is snapshotted and restored if a rebuild scores lower.
- **New techniques** are one table row and a recipe in `reference/techniques.md`; they get exploration turns automatically.

### Design refinement

`design-refinement/` studies educational-skills repositories (listed in `repos.txt`, pulled by `pull-repos.sh`, not committed), analyses each against the constraints, merges the ideas into `principles.md`, and tests the test-first ones as A/B experiments on real segments (`experiments/plan.md`). The factory runs one experiment every few published modules; only winners change the rules. See `design-refinement/README.md`.

### Pedagogy built in

Ask before tell, one idea per node, trap-derived distractors (one error per option) with tempting → wrong → right feedback matched to the error type, re-tests in a different form, hint ladder before the answer, confidence checks with hypercorrection notes for confident errors, fast lanes for strong learners (expertise reversal), a different second explanation, delayed re-tests, vignette-led clinical decisions, explicit "PYQs expected X; current source says Y" traps, a summary the learner builds, and spaced review cards (days 1, 3, 7, 21, 60). See `reference/pedagogy.md`.

## Running it

Requirements: Claude Code (`claude`) logged in, Python 3, git.

```bash
# One tick, interactively (watch what it does):
claude            # then type: /lore-factory

# Unattended: 30 ticks, committing after each
scripts/run-factory.sh 30

# Unattended in a cloud container that may be reclaimed: also push each tick
scripts/run-factory.sh 30 --push

# Stop gracefully (the loop exits before the next tick)
touch factory/STOP
```

A tick is one stage of one module, so a whole module takes roughly 10–14 ticks (more with refinement rounds). Progress: `factory/status.md` (modules, queue, technique leaderboard) and `factory/log.md` (one line per tick). Full transcripts go to `factory/ticks.log` (not committed).

For a schedule, run the loop from cron or a CI job, e.g. nightly: `0 1 * * * cd /path/to/repo && scripts/run-factory.sh 20 --push`.

## Steering

| You want | Do |
|---|---|
| A topic built next | Add a row to `factory/queue.md` with priority 1 |
| Only some subjects | `subjects_focus: [paediatrics, pharmacology]` in `CLAUDE.md` |
| More variety per segment | Raise `variants_per_segment` (cost grows linearly) |
| Higher quality bar | Raise `publish_threshold` or `max_rounds` |
| A blocked module retried | `python3 scripts/factory.py unblock <subject>/<slug>` |
| Textbook-grade facts | Drop PDFs in `sources/` (tier 0) |

## Looking at modules

```bash
python3 -m http.server 8000     # from the repository root
# open http://localhost:8000/player/
# drafts: http://localhost:8000/player/?m=../workshop/paediatrics/tetralogy-of-fallot/module.json
```

The player shows citations (tap `[n]` for the claim and source), ⚠ on unverified lines, Sure / Guessing on key probes, and at the end the full pre-authored report: headline, each objective's level, each trap you fell into and whether you fixed it, your error pattern, calibration, review cards weakest first, and a button to download the session record. Tick **IDs** to see node and claim IDs while reviewing.

## Files

| Path | What |
|---|---|
| `CLAUDE.md` | Config, layout, accuracy rule, autonomy rules |
| `.claude/skills/lore-factory/SKILL.md` | The tick orchestrator (state machine) |
| `.claude/skills/lore-research/SKILL.md` | The research pipeline (also usable alone: `/lore-research <topic>`) |
| `.claude/agents/` | Research agents (5) and conversation agents (10) |
| `reference/module-format.md` | Claim bank, segment and module JSON formats |
| `reference/pedagogy.md` | The conversation contract (constraints first) |
| `reference/traps.md` | Error taxonomy, trap brief and trap map formats |
| `reference/report.md` | End-of-module report rules and the session record |
| `reference/techniques.md` | Authoring techniques (machine-read table) |
| `reference/rubric.md` | Judging gates, criteria, lenses |
| `reference/personas.md` | Simulated learners |
| `scripts/factory.py` | All deterministic steps (`-h` for commands) |
| `scripts/run-factory.sh` | Unattended loop |
| `player/index.html` | Module player |
| `design-refinement/` | Repo analyses, principles, efficacy experiments |

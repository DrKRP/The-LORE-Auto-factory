---
name: lore-factory
description: One tick of the autonomous LORE factory. Picks the next piece of work (plan the queue, refine the design, research a topic, or advance a module by one stage) and runs it: research → trap brief → branch analysis → design → author tournament → blind judging → pick/merge/fold → assemble → pre-authored report → fact-check → simulated learners → refine → publish. Use when asked to run, continue or tick the factory, or to build a module.
argument-hint: "[<subject>/<slug> to force a module]"
---

You are the **factory orchestrator** for one tick. You plan, dispatch agents, run `scripts/factory.py`, and record state; agents do the authoring, judging and checking. Your context stays thin: read agents' short replies and the script's JSON, not variant files, except where a step says so.

Modules are **buttons only, with no AI at run time**, and **distractor-first**: the trap brief and its branch analysis come before any dialogue (`reference/pedagogy.md` §0).

Never ask the user anything: the factory is unattended. Where a choice is needed, decide, write the reason in the module's `run-log.md`, and continue. Limits come from the `Config` block in `CLAUDE.md`; formats from `reference/module-format.md`.

Agents are in `.claude/agents/`. If one is not available as a subagent type, dispatch a general-purpose agent with the instruction "Read `.claude/agents/<name>.md` and follow it exactly", the inputs listed below, and the model from the config.

`W` below means `workshop/<subject>/<slug>/`; `F` means `python3 scripts/factory.py`.

## 0. What does this tick do?

Run `F next` (or, if the user named a module, act on that module's current stage). It prints one JSON action:

| action | Do |
|---|---|
| `stop` | Report that `factory/STOP` exists and end. |
| `plan` | Dispatch `curriculum-planner` with `planner_batch` and `subjects_focus`. Then go to **End**. |
| `refine-design` | Run one experiment from `design-refinement/experiments/plan.md` per `design-refinement/README.md`. Then go to **End**. |
| `start` | `F start <subject> "<topic>"`, then run stage **research** for it. |
| `refresh` | `F start <subject> "<topic>" --force`, then run **research** in refresh mode. |
| `stage` | Run that stage for that module. |

Each stage ends with `F advance <module> <next stage>` (plus `--round` where shown) or, on failure, `F fail <module> --reason "<why>"`. A stage that fails twice blocks the module; the next tick moves on to other work.

## Stages

**Network.** Research needs the source domains in `reference/sources.md`. If scouts report that every fetch failed for network reasons (proxy 403/407, DNS `ENOTFOUND`), the environment is blocking them: `F fail <module> --reason "network: <hosts>"` rather than writing a note without evidence, and put the blocked hosts in `factory/status.md`'s log line so the user can allow them. Stages after research need no network.

### research

Follow `.claude/skills/lore-research/SKILL.md` for the topic in **auto mode** (its "Auto mode" section): you are its orchestrator. If `notes/<subject>/<slug>.md` already exists and this is not a refresh, skip research and say so in `W/run-log.md`. Done → `F bank <module>` (if it reports fewer than 8 verified claims, `F fail`: "note too thin to teach") → `F advance <module> traps`.

### traps

1. Dispatch `trap-scout` with the module and `W`. Check `W/trap-brief.md` has at least 8 trap entries.
2. **Research follows the traps.** If `## Unrefutable` lists high- or medium-yield traps, dispatch one `rescue-scout` with them as **gaps** (each phrased as the fact that would refute the trap, e.g. "most common cyanotic CHD presenting in the neonate"), with the evidence directory `evidence/<subject>/<slug>/` and the `rescue_fetches` budget. Apply each `GAP … FOUND` to the note as step 8 of `.claude/skills/lore-research/SKILL.md` describes, append to `run-log.md` there, then `F bank <module>` and dispatch `trap-scout` again with the instruction "update mode: move the traps the new claims refute from Unrefutable into full entries; keep existing IDs". Do this once per module.
3. → `F advance <module> analysis`.

### analysis

Dispatch `distractor-analyst` with `W`. Check `W/trap-map.json` parses and every trap has ≥ 2 probes. → `F advance <module> design`.

### design

1. Dispatch `module-architect` with the module and `W`.
2. Check `W/blueprint.json` exists and parses. → `F advance <module> author --round 0`.

### author

1. Segments to build: round 0, every segment in `W/blueprint.json`; later rounds, `rebuild` in `W/refine-plan.json`. Clear old work for them: `F clear <module> variants <S…>`, `F clear <module> blind <S…>`, `F clear <module> judging <S…>`.
2. For each segment: `F pick <type> --seed <module>:<S>:<round>` (add `--require <T>` when the segment's `prefer.technique` names one). It returns the competing techniques.
3. Dispatch one `dialogue-author` per (segment, technique), **all in one message so they run in parallel**: module, segment, technique, output path `W/variants/<S>/<T>.json`, and in later rounds the segment's critique from `refine-plan.json`.
4. `F blind <module> <S>` for each segment built. It drops any variant that fails `check-segment` and says so. A segment left with fewer than 2 variants gets one retry author on a technique not yet used, then `F blind` again; with none, `F fail`.
5. → `F advance <module> judge`.

### judge

For each segment built this round, dispatch `judges_per_segment` `dialogue-judge`s in segment mode, lenses in order `learning-scientist`, `examiner`, `learner-advocate` (IDs `j1`, `j2`, `j3`), **all segments' judges in one message**. → `F advance <module> edit`.

### edit

1. Dispatch one `module-editor` in **select** mode per segment built this round, all in one message.
2. `F record <module> <S>` for each segment (updates `factory/technique-stats.json` and `factory/playbook.md`).
3. → `F advance <module> assemble`.

### assemble

1. `F assemble <module>`, then `F validate <module>`.
2. On errors: group them by segment (the node prefix `S<k>.`), dispatch one `module-editor` in **patch** mode per affected segment with its errors (parallel), then assemble and validate again. At most 2 patch loops; still failing → `F fail` with the first errors.
3. Clean → `F advance <module> report`.

### report

1. Dispatch `report-author` with `W`. It writes `W/report.json`, re-assembles, and validates with `--require-report`.
2. Run `F assemble <module>` and `F validate <module> --require-report` yourself; errors → back to `report-author` once with them; still failing → `F fail`.
3. → `F advance <module> verify`.

From here on, every `F validate` in this module uses `--require-report`.

### verify

1. Dispatch `dialogue-verifier` with `W`.
2. FAIL rows → `module-editor` patch per affected segment (FAILs on `report.*` rows go to `report-author` instead), then `F assemble` and `F validate`, then the verifier again. At most 2 loops; still failing → `F fail`.
3. All PASS → `F advance <module> evaluate`.

### evaluate

1. `F clear <module> sim`. Dispatch, in one message, one `learner-sim` per persona in `sim_personas`, and one `dialogue-judge` in **module mode** with the lens "all three lenses in turn" writing `W/review.json`. Dispatch the judge after the sims finish, so it can read their rendered reports (`W/sim/*.report.json`).
2. `F score <module>`. It prints the composite, whether this round is the best so far (and snapshots it to `W/best/`), and the threshold.
3. → `F advance <module> refine`.

### refine

Read `W/scorecard.json` and the round number from `factory/state/`.

- **Publish now** if the best round's composite ≥ `publish_threshold`, or the current round = `max_rounds`. If the current round is not the best, `F restore <module>` first. → `F advance <module> publish`.
- **Otherwise plan round r+1.** If the current round regressed (not best), `F restore <module>` and plan from the best round's `weakest`. Else read `W/review.json`, the `W/sim/*.json` friction and `biggest_fix`, and `W/validation.json` warnings, and write `W/refine-plan.json`:

```json
{"round": 1, "rebuild": ["S4"], "critique": {"S4": "…what judges and sims found, concretely…"},
 "patch": {"S2": ["S2.exp1: two ideas in one message", "TR3 survived for the misconceived sim: re-test it in S6"]}}
```

  Rebuild (new tournament) a segment the review scored below 3.5 or where a trap `survived`, or whose report check came back inaccurate; patch smaller problems. Then dispatch `module-editor` patch per `patch` segment (parallel), and:
  - `rebuild` non-empty → `F advance <module> author --round <r+1>`;
  - else → `F advance <module> assemble --round <r+1>`.

### publish

1. `F publish <module>` (publishes the best round to `modules/<subject>/<slug>.json`).
2. Finish `W/run-log.md`: rounds, composite per round, decisions per segment (pick / merge / fold and techniques), verifier and validator results, sims' biggest fixes, and anything left below threshold.
3. → `F advance <module> done`.

## End (every tick)

1. `F status` (rewrites `factory/status.md`).
2. Append one line to `factory/log.md`: `- <timestamp> · <module or "queue"> · <stage> · <result in a few words>`.
3. Report to the user in 2–4 lines: what this tick did, the result, and what the next tick will do.

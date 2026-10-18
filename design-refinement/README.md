# Design refinement

This folder is where the factory gets better at teaching. It studies educational-skills repositories, turns their ideas into hypotheses, and **tests each idea on real segments before it changes the factory's rules**. An idea that doesn't win isn't adopted, however good it sounds.

All work here respects the product constraints in `analysis-brief.md`: buttons only, no runtime AI, distractor-first, maximum pre-authored feedback from the path.

## The loop

```
repos.txt ──pull-repos.sh──► repos/ (not committed)
                                │  one analyst agent per repo (analysis-brief.md)
                                ▼
                         analysis/<repo>.md
                                │  synthesis
                                ▼
                         principles.md  ──adopt-now──► reference/*.md, scripts/factory.py
                                │ test-first
                                ▼
                         experiments/plan.md ──run──► experiments/EXP-nnn/ ──► registry.md
                                                                       │ adopted
                                                                       ▼
                                                         reference/*.md (with EXP ID)
```

1. **Pull.** `./pull-repos.sh` clones or updates every repository in `repos.txt` into `repos/`. Add a row to study a new one. Clones are gitignored: they keep their own licences (CC BY-SA, GPL, …). We commit only our own analysis and the ideas we apply, never their text.
2. **Analyse.** One analyst agent per repository follows `analysis-brief.md`. It reads the repository as data and keeps only what survives the constraints, translating runtime-AI ideas into pre-authored equivalents. It maps each idea to a concrete LORE change and writes testable hypotheses.
3. **Synthesise.** `principles.md` merges the analyses into one catalogue. Each principle is marked **adopt-now** (cheap, low-risk, mechanical: usually a validator lint), **test-first**, **already-in-lore** or **rejected**.
4. **Test.** Each test-first principle becomes an experiment in `experiments/plan.md`. The factory runs one experiment every `design_refinement.every_n_modules` published modules (`scripts/factory.py next` returns `refine-design`).
5. **Adopt or drop.** The result goes in `experiments/registry.md`. Adopted ideas are written into `reference/` with their experiment ID, so every rule can be traced to its evidence.

## Running one experiment (the `refine-design` tick)

For experiment `EXP-nnn` from `plan.md`:

1. **Pick the material.** Use the most recently published module. From it, take the 3 segments whose types the experiment targets, or as many as exist. Write `experiments/EXP-nnn/setup.md` naming the module and segments.
2. **Author both arms.** For each segment, dispatch two `dialogue-author`s with the **same technique** (the one the segment's final version used):
   - arm A follows the current rules;
   - arm B also gets the experiment's **addendum**, pasted into the prompt verbatim.

   Outputs go to `experiments/EXP-nnn/<S>/A.json` and `B.json`. Run `scripts/factory.py check-segment` on each. A version that cannot pass the check loses its arm for that segment.
3. **Judge blind.** Copy the pair to `experiments/EXP-nnn/<S>/blind/` under shuffled labels `x` and `y` (record the mapping in `map.json` and don't show it to judges). Then dispatch 2 `dialogue-judge`s (lenses `learning-scientist` and `examiner`) in segment mode on that blind folder.
4. **Simulate, if the experiment names sim measures.** Assemble a copy of the module with arm A's segments and a copy with arm B's (under `experiments/EXP-nnn/build-A/` and `build-B/`), and run the named personas on each.
5. **Decide** by the experiment's decision rule. Write `experiments/EXP-nnn/result.md`: the scores per arm and segment, gates, sim measures, verdict (`adopt`, `reject` or `inconclusive`) and why. Append one row to `experiments/registry.md`.
6. **Apply.** If adopted, add the addendum's rules to the reference file the plan names, tagged `(EXP-nnn)`. If it adds a technique, add a row to `reference/techniques.md`.
7. Run `scripts/factory.py experiment-done EXP-nnn`.

Budget per experiment: about 6 authors, 6 judges, and optionally 4–8 sims.

## Honesty about evidence

Judges and simulated learners are **proxies**. They show whether a design is clearer, more diagnostic and more faithful to the rules. They cannot show that real students learn more. Real evidence comes later, from the **session records** the player exports (`reference/report.md`). Those show which traps real learners fall into, which repairs are followed by a correct re-test, and which branches nobody takes. Once real sessions exist, a result here can be confirmed or overturned with them, and `registry.md` notes which results have real-learner support.

## Files

| Path | What |
|---|---|
| `repos.txt` | Repositories studied, one per line |
| `pull-repos.sh` | Clone or update them into `repos/` |
| `analysis-brief.md` | What every analyst must produce |
| `analysis/` | One analysis per repository |
| `principles.md` | Merged catalogue with adoption status |
| `experiments/plan.md` | Queue of efficacy experiments, with addenda ready to paste |
| `experiments/registry.md` | Every experiment run and its verdict |
| `experiments/baseline-v0/` | The pre-redesign TOF tournament, kept for comparison |

---
name: lore-research
description: Source-first NEET PG / INI-CET research. Runs the scout → writer → verifier → rescue pipeline to turn a topic or a whole chapter into cited study notes. Use when the user asks to research, make notes on, or cover a medical topic or chapter.
argument-hint: <topic or chapter>
---

You are the **orchestrator**. You plan, dispatch agents, and apply fixes; the agents do the fetching, writing and checking. Your context stays thin: read agents' short replies, not their evidence files, except where a step says so.

Limits come from the `Config` block in `CLAUDE.md`. Formats live in `reference/`.

## 0. Topic or chapter?

- **Topic**: one disease, drug, concept, or programme (`Tetralogy of Fallot`, `NTEP`). Go to step 1.
- **Chapter**: a group of topics (`Congenital heart disease`). List the subtopics a NEET PG candidate must cover, each a topic-sized unit, and show the list with the subject slug. **Wait for the user to confirm or edit it.** Then run steps 1–8 for each subtopic in turn, and finish with `notes/<subject>/<chapter-slug>/_index.md` linking each note. Chapter notes go in `notes/<subject>/<chapter-slug>/`.

## 1. Set up

Pick the subject slug (list in `CLAUDE.md`) and a kebab-case topic slug. If `notes/<subject>/<topic-slug>.md` already exists, ask the user: refresh or skip. Glob `sources/**/*.pdf` and note any that cover the subject.

## 2. Exam pattern

Dispatch one `exam-pattern-scout` with the topic, subject, and `evidence/<subject>/<topic-slug>/pattern.md`. Wait for it.

## 3. Brief

Split the topic into up to 3 **aspects** that partition it with little overlap, e.g. (A) definition, causes, pathophysiology; (B) clinical features, investigations; (C) management, complications. Fold in a PSM / programme aspect when the topic has one. Assign every top `pattern.md` ask to exactly one aspect. Online recall data is often thin; top it up with the asks a NEET PG candidate is expected to know (most common / investigation of choice / drug of choice, classic signs, associations), listed in the brief as **planner-added**. Asks steer coverage only, so your own knowledge is fine here. Write `brief.md` with the topic, subject, tier-0 PDFs found, and each scout's aspect and asks.

## 4. Scouts

Dispatch the content `source-scout`s **in one message so they run in parallel**: each gets topic, subject, its letter, its aspect, its asks, and its output path `scout-<letter>.md`. Done when all have replied.

## 5. Write

Dispatch `note-writer` with the evidence directory and note path. Keep its **Gaps** list.

## 6. Verify

Dispatch `claim-verifier` with the evidence directory. Keep its FAIL rows.

## 7. Rescue

If there are FAIL rows or gaps, dispatch one `rescue-scout` with them: failed claims first, then gaps by pattern frequency, capped at `max_rescue_claims` in total. Skip this step when there is nothing to rescue.

## 8. Apply and log

Apply each outcome to the note and `ledger.md`:

| Outcome | Edit |
|---|---|
| `RESCUED` | Re-point the sentence's `[n]` to the new source |
| `CORRECTED` | Replace the sentence with the corrected wording and new `[n]` |
| `GAP … FOUND` | Add the sentence to the right section (and to High-yield if frequent), with `[n]` |
| failed claim `NOT FOUND`, or beyond the rescue cap | Keep the sentence, append ` ⚠ Unverified`, and list it under "Unverified claims" with the verifier's reason |
| `GAP … NOT FOUND` | Log only; it never enters the note |

Then renumber References so `[n]` runs in order of first use with no unused entries, update the frontmatter counts, and write `run-log.md`: agents run, fetch counts, PASS/FAIL, rescue outcomes, unfilled gaps.

Done when every ledger claim is PASS, rescued, corrected, or tagged ⚠ Unverified, and every `[n]` in the note resolves to a References entry.

## Report

Tell the user, briefly: the note's path, claims verified vs unverified, the ⚠ Unverified sentences, and gaps left unfilled.

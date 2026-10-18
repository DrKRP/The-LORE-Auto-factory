# LORE Research Agent

Part of **LORE** (Learn Once, Remember Effortlessly). This folder turns a NEET PG / INI-CET topic into **source-first** study notes: every fact is fetched and quoted from an authoritative source *before* it is written, never recalled from memory and cited afterwards.

To research a topic or chapter, run the project skill `/lore-research <topic or chapter>` (`.claude/skills/lore-research/SKILL.md`). It is the only research workflow in this folder; it takes precedence over any general-purpose research skill.

## Config

Change limits and models here only; the skill and agents read them from this block.

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
chapter_mode:
  confirm_subtopics_with_user: true
```

## Layout

| Path | Holds |
|---|---|
| `notes/<subject>/<topic-slug>.md` | Finished study notes (the deliverable) |
| `evidence/<subject>/<topic-slug>/` | Scout quote files, claim ledger, verification, rescue, run log |
| `sources/` | Tier-0 PDFs the user drops in (textbooks). Empty is normal |
| `reference/sources.md` | Source tiers and domain whitelist |
| `reference/evidence-format.md` | Evidence, ledger and verification file formats |
| `reference/note-template.md` | The fixed note skeleton |

`<subject>` is one of the 19 MBBS subject slugs: `anatomy`, `physiology`, `biochemistry`, `pathology`, `pharmacology`, `microbiology`, `forensic-medicine`, `community-medicine`, `ent`, `ophthalmology`, `medicine`, `surgery`, `obgyn`, `paediatrics`, `orthopaedics`, `dermatology`, `psychiatry`, `anaesthesia`, `radiology`.

## The accuracy rule

1. A fact enters the notes only if an agent fetched the page (or read the tier-0 PDF) and captured a **verbatim quote** that supports it.
2. Tier 0 or tier 1: one source suffices. Tier 2 only: two independent sources must agree.
3. Coaching sites and PYQ recalls decide *what to cover* and feed **⚠ Exam notes**; they are never a fact source.
4. Two trusted sources disagree: show both, attributed. For Indian programme / PSM questions list Indian sources (MoHFW, ICMR, NTEP, NACO, NHM) first.
5. A claim that fails verification and cannot be rescued stays in the note tagged **⚠ Unverified** and is listed under "Unverified claims".

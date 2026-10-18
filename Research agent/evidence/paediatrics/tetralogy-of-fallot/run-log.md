# Run log: Tetralogy of Fallot

Date: 2026-10-18. This was the pipeline's first test run, with the orchestrator in the build session (the agents ran as general-purpose agents with their definition files, on the configured models).

| Stage | Model | Result |
|---|---|---|
| exam-pattern-scout | haiku | 4 pattern entries, 6 fetches (sparse recall data online); planner topped up the asks |
| source-scout A/B/C | haiku ×3 | 17 + 18 + 28 entries, 6 fetches each; several bot-check / 403 dead ends |
| note-writer | opus | 81 claims, 5 sources; gaps: P1 (not part of TOF), P2 (pentalogy) |
| claim-verifier | haiku | 45 PASS, 36 FAIL (28 single tier-2, 2 same-review, 3 overstatement/mismatch, 4 exam-note pattern clauses) |
| rescue-scout | sonnet | 10 fetches; 6 rescued, 8 corrected, gap P1 found, 20 not found |

## Applied
- C2, C24 → corrected to StatPearls wording (C24 merged into the summary as a duplicate).
- C5, C33, C36, C38, C40 → second independent tier-2 source (Apostolopoulou, PMC6323806).
- C6, C77 → pentalogy = TOF + ASD (CDC toolkit).
- C21 → reworded to radiograph finding, two tier-2 sources.
- C23 → "pink Tet" redefined per StatPearls.
- C66, C75 → "most frequent causes include" (was an overstatement).
- C78 → passes under the pattern-clause rule (only its PYQ clause had failed).
- Gap P1 → added to Definition (StatPearls + CDC).

## Tagged ⚠ Unverified (22)
C3, C8, C15, C16, C17, C18, C34, C37, C39, C41, C42, C52, C53, C54, C56, C57, C58, C59, C71, C72, C76, C79. All are single-source tier-2 claims.

## Unfilled
- Embryology (anterocephalad deviation of the outlet septum), clubbing, polycythaemia by name, propranolol / sodium bicarbonate for spells, paradoxical embolism, PVR / ICD criteria. No eligible page was reachable within budget.

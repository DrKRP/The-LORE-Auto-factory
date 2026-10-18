# Evidence file formats

All files for one topic live in `evidence/<subject>/<topic-slug>/`.

| File | Written by | Purpose |
|---|---|---|
| `brief.md` | orchestrator | Topic, subject, scout assignments |
| `pattern.md` | exam-pattern-scout | What gets asked; exam-expected answers |
| `scout-a.md`, `scout-b.md`, `scout-c.md` | source-scout | Quotes from authoritative sources |
| `ledger.md` | note-writer | Every cited sentence → evidence IDs |
| `verification.md` | claim-verifier | PASS / FAIL per claim |
| `rescue.md` | rescue-scout | New evidence for failed claims |
| `run-log.md` | orchestrator | Counts, failures, what was tagged unverified |

## Evidence entry (scout-*.md, rescue.md)

One entry per fact. The ID is the scout letter plus a number (`A1`, `B7`, `R3` for rescue). The quote is copied character-for-character from the fetched page; shorten only with `…` between verbatim fragments.

```markdown
## A3
- fact: Tetralogy of Fallot is the most common cyanotic congenital heart disease.
- quote: "Tetralogy of Fallot (TOF) is the most common cyanotic congenital heart defect"
- source: StatPearls — Tetralogy of Fallot
- url: https://www.ncbi.nlm.nih.gov/books/NBK513288/
- tier: 1
- date: 2026-10-18   # page's last-updated date if shown, else access date
```

A source page that was fetched but yielded nothing usable gets one line at the bottom under `## Dead ends` with the URL and why.

## Pattern entry (pattern.md)

```markdown
## P2
- ask: Most common cyanotic CHD beyond the neonatal period
- frequency: repeatedly asked (seen in 3 recall sources)
- exam_answer: Tetralogy of Fallot      # only when the recall states one
- seen_at: https://…, https://…
```

Pattern entries steer coverage and **⚠ Exam notes**; they never support a fact.

## Ledger (ledger.md)

One row per cited sentence in the note. `ref` is the note's `[n]`; `evidence` lists the IDs that support it.

```markdown
| claim | sentence (as written in the note) | ref | evidence |
|---|---|---|---|
| C1 | TOF is the most common cyanotic congenital heart disease. | [1] | A3 |
| C2 | The hypercyanotic ("tet") spell is treated with knee-chest position … | [2] | B4, B5 |
| C3 | PYQs have expected X; current StatPearls says Y. | [1] | P2 (pattern), A5 |
```

In ⚠ Exam notes rows, list the pattern ID marked `(pattern)` for the "PYQs have expected" clause. The verifier checks only the non-pattern IDs.

## Verification (verification.md)

```markdown
| claim | quote_found | supports | verdict | reason |
|---|---|---|---|---|
| C1 | yes | yes | PASS | |
| C7 | yes | no | FAIL | Quote gives 5–10%; note says 10–15% |
| C9 | no | – | FAIL | Passage not on page |
```

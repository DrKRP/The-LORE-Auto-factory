# Source tiers

A source's tier is decided by **domain and path**, never by how confident the page sounds. A domain not listed here is not a fact source.

## Tier 0: user PDFs

Anything in `sources/` (standard textbooks the user supplied). Highest authority for "what the exam expects". Cite as `Book title, edition, page`.

## Tier 1: one source suffices

| Domain / path | What it is |
|---|---|
| `ncbi.nlm.nih.gov/books/` | NCBI Bookshelf, incl. StatPearls |
| `who.int` | WHO guidelines, fact sheets, ICD |
| `mohfw.gov.in`, `main.mohfw.gov.in` | Ministry of Health & Family Welfare (India) |
| `icmr.gov.in`, `main.icmr.nic.in`, `icmr.nic.in` | ICMR guidelines and STWs |
| `tbcindia.gov.in`, `tbcindia.mohfw.gov.in` | NTEP (TB) |
| `naco.gov.in` | NACO (HIV) |
| `nhm.gov.in` | National Health Mission programmes |
| `ncdc.mohfw.gov.in`, `ncvbdc.mohfw.gov.in` | NCDC, vector-borne disease programme |
| `cdc.gov` | CDC |
| `nih.gov` (excluding patient-facing MedlinePlus) | NIH institutes |
| `nice.org.uk` | NICE guidelines |
| `escardio.org`, `ahajournals.org`, `acc.org` | ESC / AHA / ACC guidelines |
| `diabetesjournals.org` | ADA Standards of Care |
| `kdigo.org` | KDIGO |
| `goldcopd.org` | GOLD (COPD) |
| `ginasthma.org` | GINA (asthma) |
| `figo.org`, `acog.org`, `fogsi.org`, `rcog.org.uk` | Obstetrics & gynaecology bodies |
| `idsociety.org` | IDSA |
| `iapindia.org` | Indian Academy of Pediatrics |

## Tier 2: needs a second independent source

| Domain / path | What it is |
|---|---|
| `pubmed.ncbi.nlm.nih.gov`, `pmc.ncbi.nlm.nih.gov` | Peer-reviewed **review articles** only (not case reports, not single trials) |
| `radiopaedia.org` | Radiology reference |
| `dermnetnz.org` | Dermatology reference |
| `merckmanuals.com/professional/` | Merck Manual, professional edition only |

Two tier-2 sources are *independent* only if they are on different domains, or are different review articles by different author groups.

## Exam-pattern only (never a fact source)

Coaching and recall material: `prepladder.com`, `marrow`/`mymarrow`, `damsdelhi.com`, `cerebellumacademy.com`, `egurucool`, PYQ recall PDFs, Telegram/Reddit/Quora, YouTube. Use them only to learn **which facts get asked** and **which answer the exam expects**.

Everything else (Wikipedia, Medscape, blogs, health portals, AI-written pages, hospital websites) is out of scope for facts.

## Fetch tips

Bot checks block some canonical URLs. Before declaring a dead end:
- NCBI Bookshelf / StatPearls: `ncbi.nlm.nih.gov/books/NBKxxxx/` often returns reCAPTCHA; `https://www.ncbi.nlm.nih.gov/sites/books/NBKxxxx/` usually works.
- PMC articles: try the same article on Europe PMC, `https://europepmc.org/article/PMC/PMCxxxxxxx` (same tier as PMC).
- `ahajournals.org` and `acc.org` usually return 403; search for the same guideline on PMC instead.

## WebSearch domain lists

Content scouts pass these as `allowed_domains`:

```
ncbi.nlm.nih.gov, who.int, mohfw.gov.in, icmr.gov.in, icmr.nic.in, tbcindia.gov.in, naco.gov.in, nhm.gov.in, ncdc.mohfw.gov.in, cdc.gov, nih.gov, nice.org.uk, escardio.org, ahajournals.org, diabetesjournals.org, kdigo.org, goldcopd.org, ginasthma.org, figo.org, acog.org, rcog.org.uk, idsociety.org, radiopaedia.org, dermnetnz.org, merckmanuals.com
```

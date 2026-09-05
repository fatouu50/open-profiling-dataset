# Sourcing Policy

## The tiers

### Tier 1 — Primary record

Documents produced by the legal or investigative process itself.

- Appellate opinions with reporter citations — `Bundy v. State, 471 So. 2d 9 (Fla. 1985)`
- Trial transcripts and docket filings
- Indictments, judgments, sentencing orders
- Official investigative reports and commission findings
- Coroner and inquest records
- Government statistical publications
- Prison and corrections records

Cite these in a form a reader can retrieve. A reporter citation, a docket number, or an archive reference — not "court records".

### Tier 2 — Peer-reviewed literature

Articles in peer-reviewed journals and academic monographs with editorial review. Give author, title, journal, volume, year, pages.

Note that a peer-reviewed paper is authoritative for *its own findings*, not for background facts it recites in passing from secondary sources.

### Tier 3 — Book-length journalism with a sourcing apparatus

Books with footnotes, endnotes, or a documented method. The apparatus is what makes them admissible — a book without one is tier 4 at best.

Give author, title, publisher, year, and page or chapter.

Two cautions:

- Authors with a personal connection to the case (Ann Rule knew Bundy; Robert Keppel investigated him) are valuable primary witnesses to what they saw, and unreliable narrators of their own significance. Cite them for what they observed.
- A book that reports another book's claim is not an independent source for it.

### Tier 4 — Contemporaneous news reporting

Reporting from an established outlet, dated close to the events. Useful for chronology and for what was known at the time.

Contemporaneous reporting frequently contains errors that later reporting corrects, and frequently propagates investigative theories that did not survive. Prefer higher tiers where they exist.

## Inadmissible at any tier

**Dramatisations.** Films, television series, docudramas, dramatised reconstructions. These invent, compress, composite and reorder by design — that is what dramatisation means. *Black Bird*, *Mindhunter*, *Monster*, *The Serpent*, *Des*, *Extremely Wicked* and everything like them are inadmissible. So are the "based on a true story" framings around them.

This is the specific vector that contaminated the inherited drafts: the Larry Hall profile reproduced the series' invented details as documented fact. The validator rejects known titles by pattern.

**Podcasts and video essays without published sourcing.** Some true-crime podcasts do real archival work and publish their sources; those sources are citable at their own tier. The podcast itself is not.

**Wikis.** Wikipedia, Murderpedia, Fandom wikis, and every aggregator of the same kind. Wikipedia is a good *finding aid* — follow its references, retrieve them, read them, cite them.

**Language model output.** A model's assertion is not evidence, and a model's citation is not a citation until you have opened it. This is not a general position on AI; it is the specific finding of [`roster-audit.md`](roster-audit.md), where model-generated content produced eight fabricated offenders indistinguishable in style from the real entries.

**Aggregator sites** that restate claims without citing their own sources.

## Independence

`established` requires two **independent** sources. Not independent:

- Two books drawing on the same trial record
- Two outlets running the same wire copy
- A book and a documentary by the same author
- Any source and something that cites it

Independence means the sources could each have been wrong without the other being wrong.

## Circular sourcing

A large amount of what "everyone knows" about these cases traces to a single unsourced assertion that has been restated until it feels established. Bundy's IQ is a clean example: figures between 124 and 136 circulate widely, none attached to an instrument, an administrator or a date.

When a claim is everywhere and sourced nowhere, that is the signature of circular sourcing. Mark it `unverified` and say so in the note. Do not launder consensus into evidence.

## Writing a citation

Bad:

```
"citation": "court records"
"citation": "Wikipedia"
"citation": "various sources"
"citation": "documentary about the case"
```

Good:

```
"citation": "Bundy v. State, 455 So. 2d 330 (Fla. 1984)"
"citation": "Canter, David and Paul Larkin. 'The Environmental Range of Serial Rapists.' Journal of Environmental Psychology 13(1), 1993, 63-69."
"citation": "Sullivan, Kevin M. The Bundy Murders: A Comprehensive History. Jefferson NC: McFarland, 2009, ch. 4."
```

Include a `url` where a stable one exists, and an `accessed` date with it.

## When you cannot find a source

Record the absence:

```json
{
  "value": null,
  "confidence": "unverified",
  "sources": [],
  "notes": "Searched the Utah trial record and Sullivan (2009). No instrument, administrator or date located for any IQ figure."
}
```

This is a real contribution. It saves the next contributor the same search and prevents a plausible number from drifting in later.

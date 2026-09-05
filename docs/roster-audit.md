# Roster Audit — Provenance Review of the Inherited 200-Subject List

**Audit date:** 2026-09-05
**Auditor:** project maintainer
**Input:** a 200-entry candidate list produced with the assistance of a large language model
**Method:** entry-by-entry verification against reference sources; targeted web search on entries that could not be corroborated from general knowledge

---

## Summary

The inherited list has a **defect rate of approximately 20%**. Roughly forty of the two hundred entries are unusable as written: fabricated names, duplicates, offenders misattributed to the wrong country, people who are not serial offenders, at least one person who was **exonerated**, and at least one **living private individual with no criminal record of violence at all**.

None of these defects are visible from reading the list. Every entry is formatted identically and every entry reads plausibly. That is the characteristic failure mode of LLM-generated reference lists: **fluency is uniform across true and false entries**, so the false ones inherit the credibility of the true ones.

This document records every defect found, so that the error is not repeated and so that reviewers can audit the audit.

### Why this matters more than the count suggests

A dataset is not judged by its best entries. A reviewer who finds one fabricated name stops trusting the other 199 — correctly, because they have no way to tell which category any given entry falls into without redoing the whole verification themselves. **One fabrication destroys the utility of the entire artefact.** This is why the schema in `schema/profile.schema.json` makes unsourced assertion structurally impossible rather than merely discouraged.

---

## Category 1 — Fabricated subjects (verified non-existent)

These names do not correspond to any documented offender. Each was checked by search.

| Entry as listed | Finding |
|---|---|
| `Émile de Maupas (Venezuela) — "le tueur des ranchs"` | No such offender. **Émile Maupas** was a French zoologist and protozoologist; **Charlemagne Émile de Maupas** was a French prefect of police under the Second Empire. The name appears to have been assembled from unrelated historical figures. |
| `Émile de Maupas (Venezuela) — "le boucher de Caracas"` | Same fabrication, **listed a second time** under a different epithet. |
| `Félicien Tremblay (Canada) — "le sédentaire du Québec"` | No such offender. Quebec's documented cases include Léopold Dion and William Fyfe, both already present in the list. |
| `Michel Stocker (Suisse) — "le prédateur des cantons"` | No such offender. Switzerland's principal documented case is **Michel Peiry** ("le sadique de Romont") — the first name is preserved, the surname invented. |
| `Jochum Sjöblom (Finlande)` | No such offender. Finland's documented cases include Michael Penttilä, Ismo Junni, Reijo Hammar and Juhani Aataminpoika. |
| `Elias Pical (Philippines)` | No such offender. **Elias Pical** is a well-known Indonesian boxer, the country's first world champion. |
| `Anwar Ali (Bangladesh) — "le prédateur des chantiers navals"` | Not corroborated. No documented offender of this name and description. |
| `Ivan Podkopaev & Cellule (Russie) — "The Grand Gland Gang"` | No such offender or group. The epithet does not correspond to any documented case. |

## Category 2 — Naming a real, living, non-violent person

> **`Asisipho Mbekela (Afrique du Sud) — "le sédentaire des Townships"`**
>
> This entry must be removed immediately and must never be republished. Asisipho Mbekela is a **real, living South African woman** who was convicted of **falsifying academic qualifications** — she worked as a radiographer using forged university documents. She has no connection to homicide of any kind.
>
> Publishing her name in a serial-killer dataset would be **defamatory**, would be trivially discoverable by searching her name, and would expose the project and its author to legal liability. It is also, simply, a serious harm to a private individual.

This single entry is the strongest argument for the sourcing policy. It survived because nothing in the original workflow required a source before a name entered the list.

## Category 3 — Duplicates

Nine entries appear twice, several under different countries or epithets, which would silently double-count them in any statistical analysis.

| Subject | Appears as |
|---|---|
| Arthur Shawcross | `Arthur Shawcross (USA)` and `Arthur John Shawcross (USA)` |
| Samuel Little | `Samuel Little (USA)` and `Samuel Little (Égypte/International)` — he is American and has no Egyptian connection |
| Charles Ng | `Charles Ng & Leonard Lake (USA)` and `Charles Ng (Hong Kong/USA)` |
| Belle Gunness | `Belle Gunness (USA)` and `Belle Gunness (Norvège/USA)` |
| Rodney Alcala | `Rodney Alcala (USA)` and `Rodney Alcala (USA/Europe)` |
| Pedro Alonso López | `Pedro Alonso López (Colombie/Équateur)` and `Pedro Alonso López (Pérou/Colombie/Équateur)` |
| Carlos Robledo Puch | `Carlos Robledo Puch (Argentine)` and `Robledo Puch (Argentine)` |
| Alexander Pichushkin | `Alexander Pichushkin (Russie)` and `Alexandre Pitchouchkine (Russie)` — same person, transliterated twice |
| Émile de Maupas | fabricated, and duplicated (see Category 1) |

## Category 4 — Exonerated: must never appear as an offender

> **`Thomas Quick / Sture Bergwall (Suède)`**
>
> Bergwall confessed to more than thirty murders while institutionalised and under heavy psychoactive medication. **Every conviction was subsequently overturned.** He was fully exonerated and is not an offender.
>
> The list correctly describes him as "le faux coupable / erreur de profilage massive" — but places him in an offender roster anyway. He belongs in a **separate table of investigative failures**, which is where this dataset now puts him. He is one of the most instructive cases in the entire corpus, precisely because he demonstrates how confession-driven investigation manufactures false offenders.

## Category 5 — Presumption of innocence

> **`Long Island Serial Killer / Rex Heuermann (USA)`**
>
> As of this audit, proceedings are ongoing. He has not been convicted. The dataset's `judicial_status` field must record charges as charges. No behavioural profile may be published for a person who has not been convicted — the `record_status` for such subjects is capped at `stub`.

## Category 6 — Not serial offenders (category error)

These are real, documented, convicted individuals, but they do not meet any standard definition of serial homicide (typically: two or more victims in separate events with an emotional cooling-off period). Including them silently corrupts every aggregate statistic the dataset would later support.

| Subject | Actual classification |
|---|---|
| Ted Kaczynski | Ideological bomber / domestic terrorism |
| Charles Manson | Convicted under joint responsibility; did not personally kill the Tate–LaBianca victims |
| Bradley John Murdoch | Single murder (Peter Falconio) |
| Raymond John Denning | Prison escapee and armed robber — **not a killer at all** |
| Arthur Lucas | Single incident with organised-crime context |
| Luka Magnotta | Single murder |
| Yuka Takaoka | **Attempted** murder, single victim — living person, remove |
| Satoshi Uematsu | Mass murder, single event |
| Woo Bum-kon | Spree/mass shooting, single event |
| Mona Fandey | Single ritual murder |
| Roch Thériault | Cult leader, one murder conviction |
| Majid Kavousifard | Single political assassination |

## Category 7 — Unsolved or unidentified

These are **cases**, not offenders. They cannot carry an offender profile because no offender has been identified. They move to `index/unsolved-cases.csv`.

- Jack the Ripper (UK, 1888)
- The Monster of Florence (Italy) — attributions contested, convictions disputed
- The Brabant killers (Belgium)
- West Mesa Bone Collector (USA)

## Category 8 — Misattributions and name corruptions

| As listed | Correction |
|---|---|
| `Patrick Mackay (USA)` | **British.** Convicted in England. |
| `Erno Soto (Chili)` | **American.** New York; a suspect in the "Charlie Chopoff" case. No Chilean connection. |
| `Samuel Little (Égypte)` | American. |
| `Gennady Mikhasevich (URSS)` | Belarus (Vitebsk). Notable because roughly a dozen men were **wrongly convicted** for his offences. |
| `Juan Coronado (USA)` | Almost certainly a corruption of **Juan Corona**. |
| `Sergey Tkachev (Ukraine)` | Almost certainly **Sergei Tkach**. |
| `Ivan Milat — "The Backpack Killer"` | The epithet is **"Backpacker Killer"**. |
| `Charles Sobhraj (France)` | Born in Saigon to an Indian father and Vietnamese mother; holds French citizenship. "France" as country of offences is wrong — he offended across South and Southeast Asia. |

## Category 9 — Held for verification

Not demonstrably false, but not corroborated during this audit. These sit in `index/quarantine.csv` until a contributor supplies an admissible source.

Macario Alcalá Canchola (Mexico) · Jeong Du-yeong (South Korea — possibly a corruption of Jeong Nam-gyu) · Jimmy Maketta (South Africa) · Tsang Tsan-lam (Hong Kong) · Giorgio William Vizzardelli (Italy) · Marcelo Antelo (Argentina)

---

## Defects in the three drafted profiles

The same review was applied to the three narrative profiles already drafted. Errors found:

**Bundy**
- Bite-mark odontology is described as having "proven mathematically, to the millimetre". This is false and is the single most damaging claim in the draft. Bite-mark comparison has since been **formally discredited**; the Texas Forensic Science Commission recommended a moratorium in 2016 and multiple convictions resting on it have been vacated. The dataset now carries a mandatory `method_now_disputed` field for exactly this.
- "First time in American judicial history that such evidence secured a death sentence" — not established; bite-mark evidence was admitted earlier (e.g. *People v. Marx*, 1975).
- "Mont Taylor" → **Taylor Mountain**, Washington.
- "Joni Lenz" is a **press pseudonym**. The survivor's name is Karen Sparks. A dataset should not propagate a pseudonym as a legal name.
- IQ of 124 and blood type O+ are asserted flatly. Both are contested in the literature and neither is given with an instrument, date or administering clinician. Both are now recorded as `contested` or `unverified`.
- Clinical diagnoses are asserted as formal findings. Bundy was never comprehensively diagnosed by a court-appointed clinician in the terms given; most of these labels come from commentators. They move to `commentary_attributions`.

**Ridgway**
- Sentenced to **48** consecutive life terms in December 2003. A 49th conviction followed in **2011**. The draft merges the two.
- "Passed a polygraph" — polygraphy has no established validity as a lie-detection instrument; reporting it as a meaningful investigative datum without that caveat is misleading.
- IQ 82 is widely cited but should carry its instrument and source.

**Larry Hall**
- **"Dodge Falcon" is not a vehicle that exists.** The Falcon is a Ford. Hall drove a Dodge van. This is a diagnostic error: it indicates the text was generated rather than transcribed from a record.
- Substantial portions of the profile — the carved wooden falcons marking grave sites, the testicular atrophy, the emotional arc of the Jimmy Keene operation — track the **television dramatisation** *Black Bird* rather than the underlying record. Dramatisations are inadmissible under the sourcing policy at any tier.
- Hall was convicted of **kidnapping**. The draft asserts a murder conviction.
- "40 to 50 victims" is presented as a dataset estimate. No investigating agency has published that figure with a traceable methodology.

---

## Constructs carried forward with warnings

**The Macdonald triad** (enuresis, firesetting, animal cruelty) is retained as a coded variable because the historical literature uses it and replication studies need it. It is **not** a predictor. Parfitt & Alleyne's 2020 critical review found no support for the triad as a predictive instrument. The schema documents this at the field level so that no downstream user can mistake it for a risk indicator.

**Offender self-report** — confessions, victim counts, biographical accounts given after arrest — is systematically unreliable. Henry Lee Lucas confessed to hundreds of murders, almost all of which were later shown to be false; the confessions nonetheless closed cases across multiple states. The schema separates `confirmed_victim_count`, `attributed_victim_count` and `claimed_victim_count` for this reason. They are not interchangeable and must never be summed.

---

## Sources consulted for this audit

- [Radford/FGCU Annual Report on Serial Killer Statistics: 2023](https://scholarscommons.fgcu.edu/esploro/outputs/report/RadfordFGCU-Annual-Report-on-Serial-Killer/99383951932606570) — Florida Gulf Coast University
- [Parfitt & Alleyne, "Not the Sum of Its Parts: A Critical Review of the MacDonald Triad" (2020)](https://pubmed.ncbi.nlm.nih.gov/29631500/) — *Trauma, Violence & Abuse*
- [Innocence Project — Why Bite Mark Evidence Should Never Be Used in Criminal Trials](https://innocenceproject.org/news/why-bite-mark-evidence-should-never-be-used-in-criminal-trials/)
- [Texas Forensic Science Commission moratorium on bite-mark evidence (2016)](https://innocenceproject.org/news/in-a-landmark-decision-texas-forensic-science-commission-issues-moratorium-on-the-use-of-bite-mark-evidence/)
- [Thomas Holst — Wikipedia (DE/EN)](https://en.wikipedia.org/wiki/Thomas_Holst) — corroborating a list entry that was initially doubted
- [List of serial killers in South Africa — Wikipedia](https://en.wikipedia.org/wiki/List_of_serial_killers_in_South_Africa)
- [Émile Maupas — Wikipedia](https://en.wikipedia.org/wiki/%C3%89mile_Maupas) and [Charlemagne de Maupas — Wikipedia](https://en.wikipedia.org/wiki/Charlemagne_de_Maupas) — establishing the origin of a fabricated entry

# The Master Grid and How It Became the Schema

This project began from a hand-built analytical grid: seven chronological phases (A–G) and a set of numbered behavioural axes. The schema in `schema/profile.schema.json` is that grid, reworked so that every element can be sourced, validated and audited.

This document exists so that the correspondence is public. Anyone using the dataset should be able to see which parts of the original design survived, which were renamed, which were dropped, and why — without having to reconstruct it from the field names.

---

## What the grid was

**Seven phases**

| Phase | Subject |
|---|---|
| A | Origins and biographical antecedents (0–15) |
| B | Social façade and clinical profile |
| C | Onset — trigger and first offence |
| D | Predation logistics — the routine modus operandi |
| E | Psychological signature |
| F | Investigation, systemic failures, capture |
| G | Interrogation, adjudication, outcome |

**Behavioural axes**

| Axis | Subject |
|---|---|
| 1 | Underlying motive — hedonistic / power–control / mission / instrumental |
| 2 | Executive methodology — organized / disorganized / hybrid |
| 3 | Geospatial dynamic — commuter / marauder |
| 5 | Psychological signature |
| 6 | Target vulnerability matrix |

---

## What the schema kept

| Grid element | Schema location |
|---|---|
| Phase A — family, trauma | `background.family_structure`, `background.documented_head_injury` |
| Phase A — Macdonald triad | `background.macdonald_triad` — kept, **labelled non-predictive** |
| Phase B — social mask | `background.education`, `background.employment_history`, `background.military_service` |
| Phase B — clinical profile | `clinical.formal_diagnoses`, `clinical.competency_findings`, `clinical.psychometric_results` |
| Phase D — hunting, execution, evidence | `offence_behaviour.victim_selection`, `approach_method`, `weapon_or_method`, `forensic_countermeasures` |
| Phase F — failures, detection, arrest | `investigation.detection_delay_factors`, `identifying_evidence`, `forensic_methods_used`, `arrest` |
| Phase G — interrogation, verdict, outcome | `adjudication.*` |
| **Axis 1** — motive | `offence_behaviour.motive_classification` |
| **Axis 3** — geospatial | `offence_behaviour.spatial_pattern` |
| **Axis 5** — signature | `offence_behaviour.signature_behaviour` |
| **Axis 6** — target vulnerability | `offence_behaviour.victim_selection` |

Axes 1 and 5 were absent from the first schema draft and were restored at the maintainer's instruction. Both carry guards described below.

---

## What the schema changed, and why

### Phase C was dissolved

The grid treated onset as a phase with two components: a "stress trigger" and a "fantasy incubator". Neither survived as a field.

Both are recovered almost entirely from what offenders said after arrest. A trigger identified retrospectively by the person it supposedly acted on is not evidence of causation; it is a narrative the person constructed, usually while facing sentence and often while being interviewed by someone who wanted a story. The dataset records what is left when that is removed: `offence_period.first_known_offence`, which is a date, and `adjudication.confession_reliability`, which is where the unreliability of the account itself is recorded.

This is the largest single departure from the original grid. It removes the part of the design that reads most like explanation.

### Axis 2 was dropped entirely

The organized/disorganized dichotomy is not recorded as a variable. Canter, Alison, Alison and Wentink (2004) tested it against 100 cases and could not recover it from the data. Recording it would mean carrying a classification that its own field has failed to replicate.

It is *discussed* in `docs/detection-mechanisms.md` and referenced in every `motive_classification` note, because contributors need to know why it is absent.

### The physical profile was dropped

Height, weight, blood type, and distinguishing features are not fields. In practice these are almost never sourceable to a record, and the versions that circulate come from press description. A schema field that can only ever be filled from inadmissible sources is an invitation to fill it from inadmissible sources.

### Axis 5 was rebuilt with a hard limit

`signature_behaviour` records conduct that was not logistically necessary and that recurred — **as established by scene documentation, post-mortem findings or charging material only**. The offender's stated reasons and any inferred psychological need are excluded, because they cannot be falsified.

The consequence is visible in the data: this field is `null` for every subject currently in the dataset. That is not the field failing. It is the field reporting that the most famous "signatures" in the profiling literature rest on what the offenders said afterwards.

### Axis 1 was rebuilt as an explicit interpretation

`motive_classification` codes against Holmes & Holmes and always carries, in its own notes, the statement that it is maintainer interpretation rather than a source-attested fact, plus the Canter et al. (2004) caution. Two subjects illustrate the range: `USA-008-RAMIREZ` is coded and flagged as a poor fit; `USA-010-BERKOWITZ` is deliberately left `null`, because the only motive evidence is an account the offender himself repudiated.

### Axis 6 was reframed

The grid described a "target vulnerability matrix" — a ratio of risk taken by the offender. `victim_selection` instead describes **the access conditions the offender exploited**, and `ETHICS.md` forbids describing victims' characteristics as if they explained their own deaths.

The analytic content survives and is sharper for it. In `USA-002-RIDGWAY` and `USA-007-DAHMER` the access condition was institutional: a population whose disappearances were not investigated. That is a finding about policing. "High vulnerability, low risk" was a finding about the offender's cleverness.

---

## What the schema added

These have no counterpart in the original grid.

| Field | Why it exists |
|---|---|
| `conviction_record.confirmed_victim_count` / `attributed_victim_count` / `claimed_victim_count` | The grid had a single count and a "dark figure". Three separate fields make it impossible to sum a conviction total with a press estimate. |
| `investigation.method_now_disputed` | Records where a conviction rested on a technique later found unreliable. Added after the first draft described bite-mark comparison as mathematically conclusive. |
| `data_quality.excluded_material` | Names widely circulated claims the record deliberately does not carry. A record that merely omits a falsehood leaves it intact in the reader's mind. |
| `search_exhausted` | Distinguishes an absence that is a finding from an absence nobody has investigated. |
| `provenance.ai_assisted` | Mandatory disclosure. |
| The whole of `schema/case.schema.json` | Subjects who fail the inclusion criteria but merit documentation. |

---

## The shape of the difference

The grid was organised around **the offender**: origins, mask, awakening, method, signature, fall, judgement. It is a biography with slots.

The schema is organised around **what can be established, and by whom**: identity, conviction, offence period, background, clinical, behaviour, investigation, adjudication, and a section stating the record's own limits.

The reordering is the point. In the grid, an unfillable slot is an incomplete story and there is pressure to fill it. In the schema, an unfillable field is a recorded finding about the evidentiary record, and filling it without a source fails validation.

Both describe the same cases. Only one of them can be checked.

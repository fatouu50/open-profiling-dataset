# Co-offenders

**One record per person. Always.**

Where two or more people offended together, this dataset gives each of them their own record and links them with the `co_offenders` field in `schema/profile.schema.json`. There is no `team` entry, no combined record, and no shared id. The `team` classification that existed in the first roster draft has been removed, and `scripts/build_index.py` now fails if it reappears.

---

## Why

The inherited roster carried eight entries of the form *"Bittaker & Norris"*, *"Bianchi & Buono"*, *"Brady & Hindley"*. Each looked like one subject. Each was two people whose legal positions were not merely different but frequently opposed.

**They were tried separately, convicted of different offences, and sentenced differently — often because one testified against the other.**

| Pair | What actually happened |
|---|---|
| Bittaker & Norris | Bittaker was convicted on 26 felony counts and sentenced to death. Norris pleaded to five murders *without* special circumstances, plus two rapes and a robbery, and testified against Bittaker. The plea is why he avoided the death penalty. |
| Bianchi & Buono | Bianchi was convicted in two states, pleaded guilty, and testified against Buono. Buono was convicted in California only. |
| Henley & Brooks | Henley: six counts of murder with malice, 99 years on each, consecutive. Brooks: one count, life. Corll, the third, was never charged at all — he was dead. |

A single record cannot express any of that. It has one `conviction_record`, one `disposition`, one `judicial_status`. Whichever version it stores is false about at least one of the two people.

## The counting problem

The second reason is arithmetic, and it is worse.

If Bittaker and Norris share one record with a `confirmed_victim_count`, that count belongs to two people. Any per-offender statistic computed from the dataset — victims per offender, series length per offender, anything with offenders in the denominator — is then wrong, and wrong in a direction that cannot be corrected after the fact, because the record no longer contains the information needed to split it.

Splitting the records does not create double counting, because the count each record carries is **the count that person was convicted of**, and those counts are different. Norris's five and Bittaker's twenty-six are not the same five victims counted twice; they are two different judicial findings about the same series. That difference is data.

## The rule

- Each convicted person gets a record in `dataset/`, with their own convictions, sentence and disposition.
- `co_offenders` on each record lists the ids of the others.
- Never merge. Never sum across linked records to obtain a series total — the schema deliberately provides no field for that, because no court produced one.
- A co-offender who was never convicted does not get a roster record. They get a case record under `schema/case.schema.json`, and the surviving co-offenders still link to them.

That last point is what `USA-011-CORLL` is. Corll was shot by Henley before any arrest; Henley and Brooks were both convicted. So Henley and Brooks sit on the roster, Corll sits in `cases/` as `died_before_trial`, and all three link to each other. The series stays intact as a set of linked records; the roster stays a list of people a court actually convicted.

## Subjects moved to `cases/` under this rule

Applying the conviction criterion consistently moved four subjects off the roster. In each, the evidentiary basis may be strong; none of them was ever adjudicated.

| Id | Subject | Why |
|---|---|---|
| `USA-011-CORLL` | Dean Corll | Shot dead 8 August 1973 by Henley, before any arrest |
| `USA-019-LAKE` | Leonard Lake | Died by self-administered poison in custody, 1985, before trial |
| `USA-038-KEYES` | Israel Keyes | Died in custody, 2012, before trial |
| `GBR-004-FWEST` | Fred West | Died on remand, 1995, before trial. Rosemary West was tried and convicted, and remains on the roster as `GBR-005-RWEST` |

`died_before_trial` is not a statement of doubt. It records that the case was never tested by a court, which is the only thing this dataset is willing to treat as established.

## Renumbering

The USA block was renumbered from `USA-011` onward to accommodate the split. **`USA-001` through `USA-010` did not move**, because they carry populated records. The Canada, UK and Australia blocks were renumbered where a split required it.

Anyone holding an id from before this change should re-derive it from `index/roster.csv` and `index/cases.csv` rather than assuming.

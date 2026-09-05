# Inclusion Criteria

A subject enters `index/roster.csv` only when all four conditions hold. The inherited list failed on each of them at least once.

## 1. The person exists

Corroborated by at least one admissible source that the named individual is a real, documented person.

This condition sounds trivial. Eight entries on the inherited list failed it. One was assembled from a French zoologist and a nineteenth-century prefect of police, and appeared twice under different epithets.

## 2. The person was convicted

A conviction for homicide, in a court, on the record.

**Not sufficient:** charges, arrest, suspicion, a confession, an investigative attribution, or press consensus.

Consequences:

- **Charges pending** → stub only. `judicial_status` records the charges. No behavioural profile. The validator enforces this.
- **Died before trial** → not an offender record. Cases like Pierre Chanal and Yvan Keller require separate treatment as unadjudicated investigations.
- **Exonerated** → never an offender record, in any circumstance. See [`investigative-failures.md`](investigative-failures.md).
- **Unidentified offender** → `index/unsolved-cases.csv`. The Whitechapel murders are a case, not a person.

## 3. The case meets the definition of serial homicide

Two or more victims, in separate events, separated in time.

This dataset uses the conventional criminological definition rather than the FBI's 2005 revision (which lowered the threshold to two victims and dropped the cooling-off requirement), because the older definition is what the comparative literature uses. The choice is recorded here so that anyone recoding the dataset knows which convention applies.

**Excluded by this criterion:**

| Type | Why | Example from the inherited list |
|---|---|---|
| Mass murder | Single event | Satoshi Uematsu |
| Spree killing | Continuous sequence, no cooling-off period | Woo Bum-kon |
| Single homicide | One event | Luka Magnotta, Bradley Murdoch |
| Terrorism | Ideological campaign, different behavioural class | Ted Kaczynski |
| Joint responsibility without personal commission | Legal category, not behavioural | Charles Manson |
| Non-homicide offences | Not homicide | Raymond Denning (armed robbery) |

These exclusions are not judgements about severity. They are about keeping the dataset's aggregate statistics meaningful. A dataset that mixes spree shooters with serial offenders cannot support inference about either.

**Included as distinct classes,** flagged in `classification`:

- `team` — two or more offenders acting together
- `healthcare` — offences committed within a care setting against patients
- `poisoner` — where method materially changes the behavioural and detection profile

## 4. The record is sufficient

Enough documented material exists to populate identity, conviction record, and adjudication from admissible sources.

A case where the entire published record consists of a paragraph in a list of serial killers is not ready. It goes to quarantine as `needs-verification` until someone locates the underlying documentation.

## Failing a criterion is not the end of the record

A subject who fails these criteria may still deserve full documentation. Since v0.1.0 the project holds those in `cases/` under [`schema/case.schema.json`](../schema/case.schema.json), with a mandatory `exclusion_rationale` naming the criteria failed.

Use a case record — not quarantine — where the subject is real, the record is substantial, and the gap between public claim and judicial finding is itself worth studying. `USA-003-HALL` is the worked example: convicted of kidnapping, never charged with homicide, publicly credited with forty-plus victims that no agency has ever attributed.

Quarantine remains for entries that should not be documented at all: fabrications, defamation risks, duplicates, and subjects nobody has corroborated exists.

## Quarantine

Failing any condition sends an entry to [`index/quarantine.csv`](../index/quarantine.csv) with a category and a reason:

| Category | Meaning |
|---|---|
| `fabricated` | No such person |
| `defamation-risk` | Names a real person with no such conviction — permanently excluded |
| `exonerated` | Convictions overturned |
| `sub-judice` | Proceedings ongoing |
| `category-mismatch` | Real, convicted, but not serial homicide |
| `unreliable-record` | Attributed counts have no evidentiary basis |
| `needs-verification` | Not yet corroborated |
| `needs-recoding` | Valid subject, wrong metadata |
| `duplicate-listing` | Already on the roster |

Nothing moves from quarantine to roster without a citable source. `defamation-risk` entries never move at all.

## Geographic and temporal scope

No restriction. The dataset is deliberately broad geographically, because the comparative literature is overwhelmingly Anglophone and North American, and that skew is itself worth documenting.

But note what the skew means: the roster is not a map of where serial homicide occurs. It is a map of **where it has been documented in sources this project can reach**. Countries with less press freedom, less developed forensic infrastructure, or less English-language coverage are under-represented for reasons that have nothing to do with offending rates.

Any cross-national analysis of this dataset that does not account for that is measuring documentation, not crime. This is the single most important caveat on the dataset and should be restated in any publication using it.

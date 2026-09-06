# Detection Mechanisms

**Status: maintainer interpretation, n = 9.** This document classifies the `investigation.detection_delay_factors` field across the offender profiles. The classification is not in the data — it is an analytical layer over it, and it is stated separately for that reason. Run `python3 scripts/detection_table.py --full` to read the underlying fields and check the reading against them.

Nine records is not a sample. Every subject here is American, all were eventually identified, and the selection came from a popular-notoriety list rather than any sampling frame. Nothing below supports inference to serial homicide generally. What it does support is a claim about **this literature**: that the standard explanation for delayed detection does not fit most of these cases.

---

## The cases

| Record | Series length | What ended it |
|---|---|---|
| `USA-009-KEMPER` | ~11 months | He surrendered by telephone |
| `USA-010-BERKOWITZ` | ~12 months | A parking citation issued near the last shooting |
| `USA-008-RAMIREZ` | ~14 months | His photograph was published; the public detained him |
| `USA-001-BUNDY` | ~4 years | Traffic stops, survivor identification, cross-state investigation |
| `USA-005-GACY` | ~6 years | An investigation into one disappearance reached his property |
| `USA-007-DAHMER` | ~13 years | A victim escaped and was, that time, believed |
| `USA-002-RIDGWAY` | ~19 years | A 1987 sample became testable in 2001 |
| `USA-006-RADER` | ~31 years | He resumed writing to police after 13 years of silence |
| `USA-004-DEANGELO` | ~32 years | Investigative genetic genealogy, 2018 |

---

## The mechanisms

### 1. Jurisdictional fragmentation — `USA-001-BUNDY`

Offences across six states with no shared records system. This is *linkage blindness* in Egger's (1984) sense: the offences were not recognised as one series because no mechanism existed to compare them.

### 2. Institutional neglect plus forensic limits — `USA-002-RIDGWAY`

The series was linked almost immediately and the correct suspect was in the file by 1983, having given a sample in 1987. What failed was the capacity to convert suspicion into proof, and the priority given to cases whose victims the system had already decided not to notice.

**This is the counter-example to linkage blindness as a general explanation.** The linkage was made. Detection still took nineteen years.

### 3. Absent technology — `USA-004-DEANGELO`

Biological evidence was retained from the beginning. The offender was not in any criminal database, and no method existed to identify him from it until 2018. Neither fragmentation nor neglect: the victims were the class institutions mobilise for most readily, and the series was linked across counties. The binding constraint was an instrument that did not exist.

### 4. An unconnected conviction record — `USA-005-GACY`

A convicted sex offender, paroled, with a further arrest during the offending period, in a single county, with the remains beneath his own house. The information existed in state records and was never brought alongside the disappearances. Of the nine, this is the most straightforwardly preventable: no capability was missing.

### 5. Present information actively dismissed — `USA-007-DAHMER`

On 27 May 1991 officers stood inside the apartment with a bleeding, drugged fourteen-year-old in front of them and returned him to the man who killed him half an hour later. The offender was at that moment a registered sex offender on probation for an offence against a child.

Not a failure of records or capability — a failure of belief, inseparable from who the victims were taken to be. Documented at tier 1 in *Estate of Sinthasomphone v. City of Milwaukee*, 838 F. Supp. 1320 (E.D. Wis. 1993).

### 6. None — the offender surfaced — `USA-006-RADER`, `USA-009-KEMPER`

Rader had not offended for thirteen years, was not a suspect, and no investigative avenue was converging on him when he resumed writing to police. Kemper drove to Colorado and telephoned a confession, reportedly having to persuade the officer it was genuine.

### 7. None — the public identified him — `USA-008-RAMIREZ`

Fingerprints identified him and his photograph was released; members of the public recognised him the next day and physically detained him. The shortest series in the dataset, ended outside the investigation.

### 8. An unrelated municipal record — `USA-010-BERKOWITZ`

One of the largest investigations in the city's history did not identify him. A parking enforcement system, operating for entirely unrelated purposes, produced the datum that did.

---

## Two observations

### Most of these cases were not closed by investigation

Three of nine ended because the offender surrendered or was delivered by the public. A fourth turned on a parking citation. **Five of nine** were closed by investigative work reaching a conclusion.

Any analysis of detection effectiveness computed from this dataset must treat the other four as censored observations. Counting them as successes measures something other than what investigation achieved. The relevant records say so in their own `detection_delay_factors` notes.

### Geographic range does not predict delay

The dataset codes `spatial_pattern` per Canter & Larkin (1993):

| Pattern | Records | Delay range |
|---|---|---|
| Commuter | Bundy, DeAngelo, Ramirez | 14 months – 32 years |
| Marauder | Ridgway, Gacy, Rader, Dahmer, Kemper, Berkowitz | 11 months – 31 years |

The ranges overlap almost completely. The shortest delay belongs to a commuter; the second shortest to a marauder. The longest belongs to a commuter; the second longest to a marauder.

Mobility is the standard narrative explanation for evasion — the offender who crosses jurisdictions outruns the records. On these nine cases it explains nothing. What separates the long delays from the short ones is whether an identifying record existed and whether anyone was willing to act on it.

---

## What would make this real

This is a comparative reading of nine cases, not a finding. To become one it would need:

- **A sampling frame.** These subjects were selected by notoriety, which correlates with everything.
- **Undetected and unsolved cases.** A dataset of caught offenders cannot measure detection. `index/unsolved-cases.csv` and `docs/investigative-failures.md` exist as the beginning of a correction and are nowhere near sufficient.
- **A coded variable.** Right now the classification lives in this document. If it holds up across more records it should become a field, with the same sourcing discipline as everything else.
- **Non-US cases.** Every observation here is from one country's institutions across one half-century.

Until then this document is a hypothesis with its evidence attached, which is the most it can honestly claim to be.

---

## Sources

- Egger, Steven A. 'A Working Definition of Serial Murder and the Reduction of Linkage Blindness.' *Journal of Police Science and Administration* 12(3), 1984, 348–357.
- Canter, David and Paul Larkin. 'The Environmental Range of Serial Rapists.' *Journal of Environmental Psychology* 13(1), 1993, 63–69.
- Canter, David V., Laurence J. Alison, Emily Alison and Natalia Wentink. 'The Organized/Disorganized Typology of Serial Murder: Myth or Model?' *Psychology, Public Policy, and Law* 10(3), 2004, 293–320.
- Per-record citations are in the `detection_delay_factors` field of each profile. `scripts/detection_table.py --full` prints them.

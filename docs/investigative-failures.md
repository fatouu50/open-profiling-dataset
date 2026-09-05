# Investigative Failures

Cases where the criminal justice system produced a wrong answer. These are recorded separately from the offender roster and carry **no offender profile**, because the people named here are not offenders.

This file exists because the inherited list contained an exonerated man among the offenders. That is not a clerical error — it is the exact harm the dataset should be documenting, reproduced by the dataset itself.

Methodologically, these cases are as valuable as any conviction. A dataset containing only successful detections cannot support any claim about detection, because it is selected on the outcome.

---

## False confession

### Sture Bergwall ("Thomas Quick") — Sweden

Bergwall confessed to more than thirty murders while detained in a secure psychiatric hospital, under substantial psychoactive medication, during therapy oriented toward recovering repressed memory. He was convicted of eight.

**Every conviction was overturned.** He was fully exonerated. He had committed none of them.

What makes the case instructive is that the confessions were not obviously false. They were refined over time through interaction with investigators and therapists, incorporating details that appeared to be independent knowledge and were in fact fed back to him. Multiple courts, prosecutors and expert witnesses accepted them across more than a decade.

Relevant fields: `confession_reliability`, `interrogation_method`.

### Henry Lee Lucas — United States

Lucas confessed to hundreds of murders across many states. Task forces closed cases on his word. Investigators travelled to interview him and left with confessions matching their open files.

Subsequent review established that the overwhelming majority were false — he had been elsewhere, sometimes demonstrably. Cases closed on his confessions were reopened; some remain unsolved.

Lucas is on the roster as `USA-037-LUCAS` because he was convicted of homicide. But his `claimed_victim_count` and `confirmed_victim_count` diverge by orders of magnitude, and the case is the standing argument for why those fields exist separately.

### Larry DeWayne Hall — United States

**This is not an exoneration case.** Hall's conviction stands. It appears here because of what the appellate record establishes about the evidence, and because of how badly the popular account diverges from it.

What the record establishes ([*United States v. Hall*, 93 F.3d 1337 (7th Cir. 1996)](https://law.justia.com/cases/federal/appellate-courts/F3/93/1337/641657/); [165 F.3d 1095 (7th Cir. 1999)](https://caselaw.findlaw.com/court/us-7th-circuit/1436146.html)):

- He was convicted of **kidnapping** under 18 U.S.C. § 1201(a)(1) — transporting Jessica Roach across a state line for sexual gratification — and sentenced to life. **There is no homicide conviction.**
- **Cause of death was never determined.** The body was recovered six weeks later and had been severely damaged by farm machinery.
- There was **no physical evidence** connecting anyone to the offence.
- The case rested on a confession obtained over roughly **17 hours of interrogation across two sessions**, handwritten by an FBI agent and signed by Hall. There were **no notes, no audio and no video** of the interrogation.
- The Seventh Circuit itemised specific reliability problems: Hall "knew" the victim was strangled, though no cause of death could be established; his apparent knowledge of the body's location tracked the fact that the questioning officer was from that area; the statement contained nothing genuinely incriminating that investigators did not already have.
- The 1996 panel **vacated the conviction and ordered a new trial**, holding that expert testimony on false confessions — Ofshe on coercive interrogation, Traugott on Hall's suggestibility — had been wrongly excluded.
- Hall was retried, convicted again, and the 1999 panel affirmed. On remand the false-confession expert evidence was admitted after a proper *Daubert* analysis, and the jury convicted anyway.
- The defence theory throughout was that Hall's personality made him "pathologically eager to please" interrogators. He also sought to introduce statements by two other named men implicating them; that evidence was excluded.

Why this matters for the dataset: Hall is routinely described as one of the most prolific offenders in American history, with forty to fifty victims. **No agency has published such an attribution, and the record contains one conviction, for kidnapping, with no established cause of death.** A dataset that recorded him as a serial killer with forty-plus victims would be asserting, as fact, exactly what a federal appellate court held required expert scrutiny before a jury could even evaluate it.

He is therefore in `index/quarantine.csv` as a category mismatch, not on the offender roster. That is a statement about what the evidentiary record supports, not a claim that he is innocent.

**A note on sources.** The widely circulated details — carved wooden falcons marking grave sites on a map, the emotional arc of the informant operation — come from a television dramatisation, not from the record. They are inadmissible here at any tier. This case is the reason `scripts/validate.py` rejects dramatisations by pattern.

---

## Wrongful conviction through investigative tunnel

### The Mikhasevich case — Belarus

While Gennady Mikhasevich was offending in the Vitebsk region, roughly a dozen men were convicted for his crimes. At least one was executed. At least one served a lengthy sentence. Confessions were obtained; the convictions were treated as closed.

Mikhasevich was eventually identified and convicted. The men wrongly convicted are named in the case literature; **this dataset does not name them.** They are not offenders and their names have no analytic function here.

Relevant field: `detection_delay_factors` — the system's confidence that it had already solved the case was itself the mechanism of delay.

---

## Discredited forensic science

Techniques admitted at trial, relied on by juries, later found to lack scientific validity.

### Bite-mark comparison

Presented for decades as capable of identifying an individual. Found by the [National Research Council (2009)](https://www.ojp.gov/pdffiles1/nij/grants/228091.pdf) to have no scientific basis for individual identification; the same conclusion was reached by PCAST in 2016. The [Texas Forensic Science Commission recommended a moratorium in 2016](https://innocenceproject.org/news/in-a-landmark-decision-texas-forensic-science-commission-issues-moratorium-on-the-use-of-bite-mark-evidence/). Multiple convictions resting on it have been vacated.

It featured prominently in the Bundy Chi Omega prosecution. The dataset records this in `investigation.method_now_disputed`. Any account describing it as having conclusively matched dentition is propagating discredited science.

### Microscopic hair comparison

The FBI acknowledged in 2015 that examiners had overstated the significance of hair comparison in the great majority of trials reviewed, across a period spanning decades.

### Polygraphy

No established validity as a lie-detection instrument. Gary Ridgway passed a polygraph in 1984 and continued offending for years. Reporting a passed or failed polygraph as an investigative finding, without that caveat, is misleading.

Relevant field: `investigation.method_now_disputed`.

---

## Structural detection failure

Not errors of individual investigators, but properties of the system.

### Linkage blindness

Offences across jurisdictions with no shared records system are not recognised as connected. The Bundy investigations spanned six states with no mechanism for linking them; ViCAP was established in 1985 partly in response.

### Victim-class neglect

Several of the longest-running cases involved victims whose disappearances were not investigated with urgency — sex workers, unhoused people, runaways, people whose immigration status limited their recourse to police. The Green River, Pickton, and Grim Sleeper investigations all involved extended periods in which reports were not acted on.

The offenders in these cases are routinely described as having evaded detection through skill. The record generally shows something else: they selected victims whose disappearance the system had already decided not to notice. This is a finding about institutions, not about offender competence, and the dataset should support stating it that way.

Relevant field: `detection_delay_factors`.

---

## Why this file is part of the dataset

Any analysis using only the offender roster is analysing a sample selected on the outcome: offenders who were caught and convicted. Conclusions drawn from it describe **detected** offending, which is a fact about policing before it is a fact about offenders.

These cases are the visible portion of the correction. They are not an appendix.

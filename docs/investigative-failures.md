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

# Ethics Policy

This dataset concerns real crimes against real people, most of whom have surviving family. Several subjects are alive. The people wrongly implicated in these investigations are almost all alive. These constraints are not optional and are enforced in review.

## 1. Victims are not content

**Named victims are not described in graphic detail.** The dataset records what is analytically necessary — cause of death, whether the offence involved sexual violence as a legal classification, the structural conditions that made access possible. It does not record the sequence of injuries, the duration of suffering, or post-mortem detail. None of that supports any research question this dataset is built to answer, and reproducing it serves only the appetite that true-crime media already serves adequately.

Where a source describes such detail, contributors summarise its legal classification and cite the source. They do not transcribe it.

**Surviving victims are not named.** People who survived these offences did not choose public life. Where a survivor's testimony is analytically necessary — as with the Utah identification in the Bundy record — the record cites the testimony without reproducing the name, even where contemporary press used one. Note that press pseudonyms should also not be propagated as if they were real names.

**Victim demographics are recorded structurally, not causally.** A field describing who was targeted describes *the access conditions the offender exploited* — unsupervised movement through semi-public space, work in settings without oversight, housing insecurity, immigration status limiting recourse to police. It does not describe victims' characteristics as though they explained their own deaths. Many of these cases went undetected for years precisely because institutions treated certain victims as unremarkable; a dataset that reproduces that framing reproduces the failure it should be documenting.

## 2. Living persons

**No behavioural profile without a conviction.** A person facing charges is presumed innocent. Such subjects may exist in the roster as a stub with `judicial_status` recording the charges, and nothing more. The validator blocks `offence_behaviour` for any subject whose status shows charges pending, acquittal, or exoneration.

**Exonerated persons are never listed as offenders.** Sture Bergwall confessed to more than thirty murders while institutionalised and medicated; every conviction was overturned. He belongs in [`docs/investigative-failures.md`](docs/investigative-failures.md), which is where this dataset puts him. The same applies to the men wrongly convicted for Gennady Mikhasevich's offences.

**Third parties are not profiled.** Family members, former partners, and associates appear only where they are part of the adjudicated record. Their private lives, health, and current whereabouts are out of scope. Children of offenders are never named.

**The defamation case.** The inherited list contained the name of a living South African woman convicted of falsifying academic qualifications, presented as a serial killer. She has no connection to homicide. Any contributor who cannot immediately see why that entry was catastrophic should not be contributing. It is the reason nothing enters the roster without corroboration that the person exists and was convicted.

## 3. Against the genre

This dataset is deliberately unglamorous. Specific editorial choices follow from that:

- **Press epithets are recorded as media artefacts**, in a field named for what they are, not adopted as descriptors. This project does not call anyone "the Night Stalker" in its own voice.
- **No language of admiration.** Terms like *mastermind*, *genius*, *elite*, *evil genius*, *monster*, and framings that treat offending as skilled performance are excluded. Most of these men were caught by traffic stops. Several had documented cognitive impairment. The competence attributed to them is largely retrospective narrative.
- **Offender self-report is not treated as testimony about the world.** It is treated as a datum about what the offender said, under what circumstances, with what incentive. Henry Lee Lucas's confessions closed hundreds of cases across multiple states and were almost entirely false.
- **The dataset does not reconstruct interior experience.** Fields describing fantasy, motive, or psychological need are limited to what a clinician recorded or what the offender stated, with the reliability of both marked. Speculative interiority — the kind that reads well in a profile and cannot be falsified — is out of scope.

## 4. Scientific honesty

**Discredited methods are marked as discredited.** Bite-mark comparison, microscopic hair comparison, and several arson "indicators" were used to convict people and have since been found unreliable by the National Research Council (2009) and PCAST (2016). A dataset that records these as successful forensic work without their current standing is teaching bad science. The `method_now_disputed` field is mandatory where applicable.

**Discredited constructs are marked as constructs.** The Macdonald triad is coded because the literature uses it, and labelled as non-predictive because it is. Contributors must not present it as a risk indicator.

**Profiling's own record is in scope.** Behavioural profiling has a mixed and contested empirical record. This dataset is a resource for evaluating it, not a monument to it. Cases where profiling misdirected an investigation belong in the dataset as prominently as cases where it helped.

## 5. Research use

This dataset is intended for retrospective analysis of adjudicated cases and of institutional detection failure.

It is **not** suitable, and must not be used, for:

- predicting individual future dangerousness
- screening, scoring, or flagging individuals
- any operational or law-enforcement decision about a specific person
- training generative models to produce offender narratives

The sample is small, non-random, and selected on the outcome — it contains only offenders who were caught and convicted. Any model trained on it learns the characteristics of *detected* offenders, which is a statement about policing, not about offending. Inference from this dataset to living individuals is invalid, and the dataset's structure will not stop anyone from doing it anyway; only this notice and reviewer vigilance will.

## 6. If you are researching this material at length

Sustained exposure to this material has documented effects on the people who work with it professionally, which is why agencies that handle it provide structured support. If you are working through these cases alone, at volume, take that seriously — set limits on session length, and talk to your supervisor about it rather than treating it as a test of endurance.

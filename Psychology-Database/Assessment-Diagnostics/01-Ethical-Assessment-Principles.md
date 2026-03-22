# Ethical Assessment Principles: APA Standard 9

**Source:** American Psychological Association (2017) Ethical Principles of Psychologists and Code of Conduct, Standard 9: Assessment  
**Status:** Active standard; foundation for all assessment ethics  
**Scope:** All psychological testing, evaluation, and diagnostic applications

---

## Overview: What Makes Assessment Different?

Assessment is an **act of measurement and labeling with power.** Unlike therapy (which is collaborative), assessment is evaluative—the psychologist/system makes judgments about the person being tested.

This power creates ethical obligations:

| Standard | Intent | Why It Matters |
|----------|--------|---|
| 9.01 | Basis for Assessment | Tests must be scientifically sound & appropriate for use |
| 9.02 | Use of Assessments | Only use assessments for purposes it was designed for |
| 9.03 | Informed Consent | User understands purpose, procedures, limitations, risks |
| 9.04 | Release of Assessment Data | Only share results with those authorized & who need to know |
| 9.05 | Test Security | Prevent unauthorized access to test materials/algorithms |
| 9.06 | Interpreting Assessment Results | Interpretation based on evidence, avoiding bias |
| 9.07 | Assessment by Unqualified Persons | Only qualified professionals conduct assessment |
| 9.08 | Obsolete Tests & Outdated Results | Don't use tests no longer valid or results older than appropriate |
| 9.09 | Test Scoring & Interpretation Services | If outsourcing scoring, maintain responsibility & accuracy |
| 9.10 | Explaining Assessment Results | Explain results in understandable language; ensure comprehension |
| 9.11 | Maintaining Test Security | Safeguard test materials from unauthorized reproduction/use |

---

## Standard 9.01: Basis for Assessments

### The Core Requirement

**"Psychologists base the opinions contained in their written and oral reports, forensic testimony, and diagnostic or evaluative statements, in whole or in substantial part, on information and techniques sufficient to substantiate their findings."**

### What This Means

- Assessment tools must have **published evidence** for reliability & validity
- Evidence must be **relevant to your specific use case**
- You must understand the **limitations** of the tool
- "No evidence" ≠ "No harm"—if you can't support it, don't use it

### Application to Digital Assessment

✅ **DO:**
- Use established psychometric tests with published validation studies
- Document which tool you're using (e.g., "PHQ-9 for depression screening")
- Review validation studies for YOUR population (not just normative sample)
- Understand what the test measures (depression, anxiety, one dimension or many?)
- Know the base rates (what % of general population has this condition?)
- If using AI/ML, validate the algorithm against gold-standard assessment

❌ **DON'T:**
- Use homemade "diagnostics" without any validation
- Assume a test validated on college students works for elderly/children
- Use tests with outdated norms (pre-2010) without updating
- Train AI on biased data and claim "objective diagnosis"
- Use proprietary algorithms without demonstrating accuracy vs. gold standard

### Critical Questions (Ask Before Using Any Assessment)

1. **Is there a peer-reviewed validation study?** If not, it's experimental—disclose that.
2. **Was validation done on people like YOUR users?** (same age, culture, language, condition prevalence)
3. **What does it actually measure?** (Read the manual; don't assume from the name)
4. **What's the accuracy?** (Sensitivity/specificity/PPV/NPV vs. clinical diagnosis)
5. **What are known limitations?** (e.g., "PHQ-9 over-identifies in non-depressed populations")
6. **Has it been validated in digital format?** (Paper ≠ App; scoring may differ online)
7. **Is the manual current?** (Published within last 10 years?)

### Red Flag Indicators
- [ ] "Proprietary assessment algorithm" with no published validation
- [ ] Test validated only on undergraduate psychology majors; using with diverse population
- [ ] Marketing claims exceed research support (e.g., "95% diagnostic accuracy" without citation)
- [ ] No explanation of what the test measures
- [ ] Test norms older than 15 years
- [ ] Different administration format (paper→digital) without re-validation

---

## Standard 9.02: Use of Assessments

### The Core Requirement

**"Psychologists use assessment instruments in a manner and for purposes that are appropriate in light of the research on or evidence of the usefulness and proper application of the instruments."**

### What This Means

- Just because a test EXISTS doesn't mean you should USE it
- Tests have **designed purposes**—don't repurpose them
- Different assessment tools measure different things
- Wrong tool for the job = wrong results

### Examples of Misuse

| Test | Designed For | WRONG Use (Never Do This) |
|------|---|---|
| **PHQ-9** | Depression screening (2-week symptoms) | Lifetime diagnosis, personality traits |
| **AUDIT** | Alcohol use disorder screening | Predicting job performance |
| **IQ test (WAIS-IV)** | Measuring cognitive ability | Determining job fitness (without specificity) |
| **MMPI-2** | Clinical psychopathology | Employee pre-screening (if no clinical concern) |
| **GAD-7** | Anxiety symptom screening (1-week) | Generalized anxiety disorder diagnosis (alone) |

### Application to Digital Assessment

✅ **DO:**
- Use PHQ-9 for depression SCREENING (not diagnosis)
- Use GAD-7 + clinical interview for anxiety assessment
- Use structured interviews/validated tools for ADHD
- Use validated culture-specific assessments (e.g., "Cultural Formulation Interview" for cultural context)
- Document the PURPOSE in your app (e.g., "This tool screens for depression; talk to a doctor for diagnosis")

❌ **DON'T:**
- Use depression screening to diagnose PTSD
- Use personality inventory to assess fitness for duty (without validation for that purpose)
- Combine unvalidated algorithms into a "super-predictor"
- Use a research tool designed for one sample on a different population
- Assume that a screener = diagnosis

### Decision Tree: Is This the Right Assessment?

```
1. What's your PURPOSE?
   ├─ Screening (identify who might need help)?
   ├─ Diagnosis (confirm presence of disorder)?
   ├─ Measurement (track symptom severity)?
   ├─ Prognosis (predict course/outcome)?
   └─ Treatment planning (guide intervention choice)?

2. What POPULATION?
   ├─ Age range
   ├─ Cultural/linguistic background
   ├─ Clinical vs. non-clinical
   └─ Known risk factors/comorbidities

3. Is there a VALIDATED TOOL for this purpose + population?
   ├─ YES → Use it. Document evidence.
   ├─ PARTIAL (tool designed for different population) → Validate on your population first
   └─ NO → Use best available + disclose limitations

4. What's the CONSEQUENCE of error?
   ├─ Low (informal screening) → More flexibility
   ├─ High (diagnostic label, legal decision) → Require gold-standard validation
```

---

## Standard 9.03: Informed Consent for Assessment

### The Core Requirement

**"Psychologists obtain informed consent for assessment, evaluation, personal interview, observational, and other data collection procedures, unless such activity is mandated by law or court order, or as otherwise provided in this Ethics Code."**

### What "Informed" Really Means

Not just "user clicks agree." Real informed consent requires:

1. **Comprehension:** User understands in plain language (not legalese)
2. **Voluntariness:** No pressure or coercion
3. **Disclosure:** All material information provided
4. **Capacity:** User able to consent (not intoxicated, confused, etc.)
5. **Documentation:** Record that consent was obtained

### Critical Disclosures for Assessment

- **What is being measured?** (e.g., "symptoms of depression")
- **Why?** (clinical decision, treatment planning, research)
- **What will happen with results?** (stored, shared, deleted)
- **What are the risks?** (false diagnosis, emotional distress, privacy breach)
- **What are limitations?** (not a formal diagnosis, requires professional review)
- **Who can see the results?** (therapist only? shared with employer? insurer?)
- **How long are results kept?** (1 year? 7 years? permanently?)
- **Can I withdraw?** (stop assessment mid-way; delete my data)
- **What if results suggest crisis?** (will you contact emergency services?)

### Application to Digital Assessment Apps

✅ **DO:**
- Show consent BEFORE assessment starts (not buried in Terms)
- Use **plain language** (8th-grade reading level)
- Explain results will be "screened by a clinician" (if they will be)
- Tell users "This is not a diagnosis" clearly
- Explain data retention: "Your answers will be deleted after [X time]"
- Ask separately for data sharing: "May we use your results in research?" (optional)
- Provide summary of consent (users can print/save)
- Allow users to decline without penalty

❌ **DON'T:**
- Bury consent in 10 pages of legal terms
- Use phrases like "by using this app, you consent to all uses" (too vague)
- Assume therapy consent = assessment consent (they're different)
- Share results without explicit consent (even with spouse/caregiver)
- Use results for purpose not disclosed (e.g., disclosed for therapy; used for marketing)
- Continue assessment despite user discomfort
- Collect data "just in case" for future research without consent

### Sample Consent Language (Plain Language)

```
BEFORE YOU TAKE THIS ASSESSMENT

What is this?
This app screens for symptoms of depression using the PHQ-9, a short questionnaire. 
It is NOT a diagnosis.

Why?
To help you understand whether you might benefit from talking to a doctor or therapist.

What happens next?
- You answer 9 questions about your mood (3-5 minutes)
- We show you your score + what it might mean
- We encourage you to see a doctor if concerned
- Your answers are stored on our secure servers

Who sees this?
Only you can see your results. We do NOT share with anyone without your permission.

How long do we keep it?
We delete your answers after 1 year. You can request deletion anytime.

Risks?
- The assessment might suggest you have depression when you don't (false positive)
- Reading results might make you feel sad or anxious
- We are not a substitute for talking to a real doctor

Is this a real diagnosis?
No. Only a doctor can diagnose depression. This is a screening tool.

Do I have to do this?
No. You can skip it anytime without penalty.

Questions?
Email [support email]

Do you understand and agree? [CONFIRM] [DECLINE]
```

---

## Standard 9.06: Interpretation of Assessment Results

### The Core Requirement

**"When interpreting assessment results, including automated interpretations by computers or other devices, psychologists take into account the various test factors, test-taking abilities, and other characteristics of the person being assessed, such as situational, personal, linguistic, and cultural differences, that might affect psychologists' judgments or reduce the accuracy of their interpretations."**

### What This Means

- Context matters: Same score = different meaning in different people
- Bias can hide in interpretation, not just the test itself
- Automated interpretations are still YOUR responsibility
- Cultural/linguistic differences affect how to interpret

### Common Interpretation Errors

| Error | Example | Why It's Wrong |
|-------|---------|---|
| **Ignoring context** | Depressive score = depression diagnosis, without asking if person just experienced loss | Loss-related sadness ≠ clinical depression |
| **Missing cultural meaning** | Spiritual hearing voices → psychosis diagnosis (in some cultures, spiritual experience is normal) | What's pathology in one culture = normal in another |
| **Language barrier** | Non-native English speaker scores low on anxiety test (ambiguous items) → diagnosed with severe anxiety | Actually struggling with language, not anxiety |
| **Opposite direction bias** | Older adult with high cognitive test score assumed "normal" when baseline was higher (normal aging) | Misses mild decline |
| **Assumption of stability** | Using 5-year-old assessment to diagnose current ADHD | Symptoms change; need current data |

### Application to Digital Assessment

✅ **DO:**
- Add **contextual questions:** "Have you experienced any major losses/stressors recently?"
- Include **cultural/linguistic screen:** "What is your primary language? Was this assessment translated/adapted for you?"
- **Never use automated interpretation alone** for clinical decisions
- **Always require human review** for results that suggest serious condition
- Include **caveats in results** (e.g., "This screening suggests possible depression; see a doctor for diagnosis")
- **Document rationale** for interpretation (if you override automated score)

❌ **DON'T:**
- Show automated diagnosis without clinician review
- Interpret results identically for monolingual English speaker & bilingual English/Spanish speaker
- Assume young = low depression risk, old = high risk (ignores individual differences)
- Use algorithm output as "objective truth" (algorithms can be biased too)
- Ignore when results don't fit clinical presentation

### The Interpretation Checklist (Before Releasing Results)

```
For each assessment result, ask:

[ ] Context: Have major stressors/losses happened?
[ ] Language: Was this assessment appropriate for user's language/literacy?
[ ] Culture: How do I interpret this in the user's cultural context?
[ ] Comorbidity: Could other conditions explain this score?
[ ] Validity: Did user respond honestly/attentively (or guess randomly)?
[ ] Age-appropriateness: Is this score normal for this age?
[ ] Comparison: How does this compare to baseline (if available)?
[ ] Alternative explanation: What else could explain this?
[ ] Human review: Has a clinician looked at this result?
[ ] Uncertainty: Am I over-confident in this interpretation?

If you answer NO to ANY, pause before sharing results with user.
```

---

## Standard 9.07: Assessment by Unqualified Persons

### The Core Requirement

**"Psychologists do not base their assessment or intervention decisions or recommendations on data or test results that are considered obsolete or outdated for the current purpose."**

### What This Means

- Only **qualified professionals** can interpret assessments
- Qualification requires **training + supervision**
- Technology doesn't replace professional judgment
- Bad interpretation causes harm

### Qualification Requirements (Varies by Assessment)

| Assessment Type | Minimum Qualification | Why |
|---|---|---|
| **Depression/anxiety screening (PHQ-9, GAD-7)** | Master's-level mental health provider or supervised trainee | Moderate risk of false positive/negative |
| **IQ testing (WAIS, Stanford-Binet)** | Licensed psychologist + formal psychoeducational training | Complex scoring, interpretation requires expertise |
| **Personality (MMPI-2, Rorschach)** | Licensed psychologist + specialized training in test | High misuse potential; requires nuance |
| **ADHD diagnosis** | Licensed psychologist or psychiatrist + clinical training | Requires differential diagnosis from 10+ other conditions |
| **Forensic assessment** | Licensed psychologist + forensic psychology training | Legal consequences; ethical/competence bar is very high |

### Application to Digital Assessment

✅ **DO:**
- Staff assessment review with **licensed professionals** (MA psychology minimum, PhD/PsyD preferred)
- Include **supervision chain** (clinician reviews results; supervisor reviews clinician)
- Train assessors on the **specific tool** (not just general psychology)
- Document assessor **credentials & training**
- Have clear **scope of practice** (what clinician CAN & CANNOT assess/diagnose)

❌ **DON'T:**
- Use non-licensed staff to interpret assessments
- Let customer service or AI alone make clinical determinations
- Skip training because "the test is simple"
- Assume a therapist can interpret any assessment (they're specialized)
- Hire anyone with a psychology degree without vetting expertise in assessment

### Red Flag Indicators
- [ ] Chat bot interprets results without human review
- [ ] Non-licensed staff providing clinical recommendations
- [ ] "Clinician review" is actually an automated flag system
- [ ] Assessment interpreter trained only via app tutorials (not formal training)
- [ ] No documentation of who did interpretation or their credentials

---

## Standard 9.10: Explaining Assessment Results to Users

### The Core Requirement

**"Psychologists ensure that explanations of results are presented in language that is understandable to the person being assessed, unless there is a compelling professional reason not to do so. Regardless of whether the assessment was conducted for clinical or evaluative purposes, psychologists do not misrepresent test results or the degree to which test results are definitive."**

### What This Means

- **Explain results in plain language** (no jargon)
- **Honest about limitations** ("This is a screening, not diagnosis")
- **Avoid false certainty** ("Your score means you definitely have depression" is wrong)
- **Check for understanding** (don't assume user understood)

### Common Mistakes in Explaining Results

| Mistake | Wrong | Right |
|---|---|---|
| **Over-certainty** | "You have depression" | "Your score suggests symptoms of depression; talk to a doctor" |
| **Jargon** | "Your somatic symptom index is elevated" | "You reported physical symptoms like headaches and stomach pain" |
| **Wrong comparison** | "You score higher than 75% of Americans" | "Your score suggests moderate symptoms" |
| **Ignoring context** | "You screen positive for PTSD" | "Your score suggests trauma-related symptoms. Trauma can mean many things; talking to a counselor can help clarify" |
| **Too much detail** | Show raw score + standard deviation + percentile + interpretation | Show simple category (mild/moderate/severe) + explanation |
| **Creating shame** | "Your depression score means you're broken" | "These are common symptoms; many people experience them; help is available" |

### Application to Digital Assessment

✅ **DO:**
- Use **simple language** (explain what "depression" means, not technical jargon)
- Show results in **categories** (mild/moderate/severe) not raw scores
- **Acknowledge limitations:** "This is a screening tool, not a diagnosis"
- **Provide context:** "About 1 in 5 people score in this range; many don't have a disorder"
- **Offer next steps:** "Consider talking to a doctor if concerned"
- **Normalize:** "These symptoms are common; you're not alone"
- **Provide resources:** Links to evidence-based info, therapist directory, crisis lines

❌ **DON'T:**
- Use technical jargon (percentile, standard deviation, item response theory)
- Show raw scores without explaining what they mean
- Diagnose ("You have GAD")—say "suggest symptoms of GAD"
- Create false certainty ("You definitely need medication")
- Make definitive claims about personality/character ("You're extroverted")
- Shame or pathologize normal variation

### Sample Result Explanation

```
YOUR DEPRESSION SCREENING RESULTS

YOUR SCORE: 18 (Moderate)

WHAT THIS MEANS:
Your answers suggest you may be experiencing symptoms of depression. 
This is common—about 1 in 12 people experience depression at some point.

WHAT WE MEASURED:
We asked about your mood, sleep, energy, and ability to enjoy things.
Your answers suggest some struggle in these areas.

IMPORTANT LIMITS:
- This is a screening tool, not a diagnosis
- Only a doctor can diagnose depression
- Your score could mean many things (grief, stress, medical condition, etc.)
- This tool works better for some people than others

WHAT TO DO NEXT:
If you're concerned:
1. Talk to your doctor or a therapist
2. Learn more: [link to reputable info]
3. Get support: [crisis line if high risk]

If you're not concerned:
- That's okay. You know yourself best.
- Reach out anytime if things change

QUESTIONS?
Email [support]
```

---

## Integration: How Standards 9.01-9.10 Work Together

| Phase | Standard | Action |
|---|---|---|
| **Design** | 9.01, 9.02 | Choose valid test for your purpose |
| **Preparation** | 9.07 | Ensure qualified staff will interpret |
| **Administration** | 9.03, 9.05 | Get informed consent; secure test materials |
| **Scoring** | 9.09 | If using service, verify accuracy |
| **Interpretation** | 9.06, 9.10 | Interpret in context; explain clearly |
| **Reporting** | 9.04 | Share only with authorized recipients |
| **Maintenance** | 9.08, 9.11 | Update norms; secure old tests |

---

## Implementation Guide: Using Standard 9 in Your App

### Pre-Launch Checklist

```
STANDARD 9.01: SCIENTIFIC BASIS
[ ] Selected assessment has peer-reviewed validation study
[ ] Validation includes population like yours (age, culture, language)
[ ] Test manual is current (within 10 years)
[ ] Known limitations documented
[ ] If using AI, validation study against gold-standard assessment

STANDARD 9.02: APPROPRIATE USE
[ ] Documented purpose of assessment (screening/diagnosis/measurement)
[ ] Assessment designed for that purpose
[ ] Documentation visible to users
[ ] No scope creep (not using for unauthorized purposes)

STANDARD 9.03: INFORMED CONSENT
[ ] Consent obtained BEFORE assessment
[ ] Language is plain language (8th grade reading level)
[ ] All material risks/benefits disclosed
[ ] Users can withdraw anytime
[ ] Separate consent for data sharing (if applicable)

STANDARD 9.06: INTERPRETATION IN CONTEXT
[ ] Process includes human review (not automation alone)
[ ] Contextual questions included (recent stressors, language, etc.)
[ ] Clinician trained on the specific assessment
[ ] Supervisor reviews sample interpretations
[ ] Cultural factors considered

STANDARD 9.07: QUALIFIED PERSONNEL
[ ] Licensed clinician reviews all results
[ ] Clinician trained in assessment interpretation
[ ] Credentials documented
[ ] Supervision/oversight clear
[ ] Scope of practice defined

STANDARD 9.10: EXPLAINING RESULTS
[ ] Results explained in plain language
[ ] Limitations acknowledged ("not a diagnosis")
[ ] No false certainty
[ ] Resources provided
[ ] Check for user understanding
```

---

## References

- American Psychological Association (2017). Ethical Principles of Psychologists and Code of Conduct. https://www.apa.org/ethics/code/
- American Educational Research Association, American Psychological Association, & National Council on Measurement in Education (2014). Standards for Educational and Psychological Testing. Washington, DC: AERA.
- Code of Fair Testing Practices in Education (2004). https://www.apa.org/science/programs/testing/fair-testing.pdf

---

**Last reviewed:** 2026-03-21  
**Confidence level:** High (primary source: APA Ethics Code)  
**Cross-references:** Ethics-Guardrails; 02-Bias-in-Diagnostics-and-AI.md; 07-Assessment-Ethics-Audit-Framework.md

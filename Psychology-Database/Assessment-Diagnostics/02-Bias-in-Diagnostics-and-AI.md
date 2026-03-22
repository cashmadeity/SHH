# Bias in Diagnostics & AI: Detection & Mitigation

**Source:** APA Standards 9.01, 9.06; Research literature on fairness in assessment & algorithmic bias  
**Status:** Critical for ethical assessment deployment  
**Scope:** Bias in assessment design, implementation, interpretation, and AI systems

---

## What is Bias in Assessment?

Bias = **systematic error that favors one group over another, leading to inaccurate or unfair results.**

### Three Sources of Bias

| Source | Example | Result |
|--------|---------|--------|
| **Test Design** | Depression screening written for Western individualistic culture | Over-identifies in collectivist cultures (values family obligation, not individual mood) |
| **Norms/Interpretation** | IQ test norms based only on White middle-class sample | Black students appear lower IQ (actually: test biased, not ability) |
| **AI/Algorithm** | Depression classifier trained on 90% White data | Misses depression in Black patients (underdiagnosis disparities) |

### Why Assessment Bias Matters

Biased assessment leads to:
- **False positives** (labeled sick when healthy) → unnecessary treatment, stigma
- **False negatives** (missed genuine disorder) → denied needed care
- **Diagnostic disparities** (same symptoms → different diagnosis by race/ethnicity)
- **Treatment inequities** (unequal access to care based on biased screening)
- **Compounding harm** (label follows person through system; reduces opportunities)

---

## Types of Bias in Assessment

### 1. Construct Bias: Test Measures Different Things in Different Groups

**Example:** Depression screening item: "I feel useless and guilty"
- Western interpretation: Clinical depression symptom ✓
- Collectivist culture: Normal response if burdening family (shame/guilt is relational)
- Result: Same response = pathology in one group, not the other

**How to Detect:**
- Compare item responses by demographic group
- Does item discriminate (predicts diagnosis) equally across groups?
- If item predicts diagnosis in White sample but not Black sample → construct bias

**How to Mitigate:**
- Conduct differential item functioning (DIF) analysis
- Remove/modify items that show construct bias
- Adapt assessment for cultural meaning (see 05-Cultural-Adaptation)
- Include contextual questions (e.g., "Is guilt related to family obligation or internal failure?")

### 2. Method Bias: Assessment Conditions Favor One Group

**Example:** Computer-based cognitive test
- English-fluent college student: Reads instructions quickly ✓
- Non-native English speaker: Takes 2x longer reading; runs out of time
- Result: Language barrier masquerades as cognitive deficit

**How to Detect:**
- Compare performance by language/reading level
- Do lower-performing groups report time pressure, comprehension issues?
- Time-limited vs. untimed performance gap by group?

**How to Mitigate:**
- Provide multilingual support/clear language
- Allow extra time (if time isn't what you're measuring)
- Give practice items to ensure comprehension
- Test in user's preferred language
- Screen for literacy/comprehension separately

### 3. Criterion Bias: Comparison Standard is Wrong

**Example:** ADHD diagnosis criteria based on school behavior
- Affluent White child with hyperactivity: Teacher notes, early intervention ✓
- Black child with same hyperactivity in under-resourced school: "Just how boys are"; no documentation; later labeled "discipline problem" instead of diagnosed
- Result: Same trait, different diagnostic path by race/SES

**How to Detect:**
- Compare diagnosis rates by demographic group controlling for symptom severity
- Are diagnosis rates proportional to symptom severity, or do disparities exist?
- What's the clinical utility of diagnosis across groups? (Does diagnosis → treatment for everyone?)

**How to Mitigate:**
- Use objective criteria (checklist vs. subjective judgment)
- Monitor diagnosis rates by demographic group
- Require same evidentiary standard for everyone
- Audit for unequal diagnostic practices

### 4. Interpretation Bias: Clinician Interprets Same Data Differently by Group

**Example:** Same anxiety score on GAD-7
- White patient, clinician thinks: "Generalized anxiety disorder" → refers to therapy
- Black patient, clinician thinks: "Just stressed from discrimination/poverty" → doesn't refer
- Result: Same pathology, different interpretation → different treatment path

**How to Detect:**
- Blind review (clinician doesn't know patient demographics)
- Compare interpretations/treatment recommendations for identical case vignettes
- Track whether diagnosis → referral equally across groups
- Audit clinician notes for language (e.g., "overwhelmed by life" vs. "psychiatric disorder")

**How to Mitigate:**
- Use **structured interpretation guidelines** (not subjective)
- Train clinicians on **implicit bias** in assessment
- Require documentation of interpretation rationale
- Use **objective scoring** algorithms (reduces subjective bias)
- Blind demographic data during interpretation when possible

### 5. Algorithm Bias: ML Model Perpetuates/Amplifies Bias

**Example:** Risk prediction algorithm trained on mental health data
- Training data reflects historical bias: Black patients underdiagnosed with depression historically
- Algorithm learns this bias: Predicts lower risk for depression in Black patients
- Deployment: Algorithm perpetuates underdiagnosis (now systematized & harder to catch)

**How to Detect:**
- Compare model accuracy across demographic groups
- Does accuracy differ? (e.g., 85% accurate for White users, 72% for Black users)
- Compute fairness metrics (equalized odds, demographic parity, calibration)
- Check for spurious correlations (model uses zip code → proxy for race)

**How to Mitigate:**
- **Diverse training data** (not 90% one demographic)
- **Fairness-aware ML** (optimize for accuracy across all groups, not just overall)
- **Validation on separate diverse samples** (before deployment)
- **Regular audits** post-launch (does bias emerge over time?)
- **Human-in-the-loop** (algorithm recommends; clinician decides)

---

## Fairness Frameworks for Assessment

### Framework 1: Equalized Odds (Equal Accuracy Across Groups)

**Definition:** Test predicts equally well for all demographic groups (same sensitivity/specificity).

**Formula:**
```
Sensitivity (true positive rate) same for:
  - White & Black patients
  - Men & women
  - Different age groups
  - Language groups
```

**Example:**
- Depression screening 90% sensitive in White sample, 72% in Black sample = NOT equalized odds
- Fix: Retrain model, adjust cutoff scores, use different criteria

**When to use:**
- High-stakes assessment (diagnosis, treatment decision)
- Large disparities acceptable?

### Framework 2: Demographic Parity (Same Diagnosis Rates Across Groups)

**Definition:** Same % diagnosed in each group, regardless of underlying prevalence.

**Problem:** If depression is actually MORE common in one group (e.g., due to systemic stress), enforcing equal rates = underdiagnosis.

**When to use:**
- Rarely alone
- Useful as red flag ("Why are diagnosis rates different?")

### Framework 3: Calibration (Predictions Equally Reliable Across Groups)

**Definition:** When model predicts "80% risk," it means same thing (80% actually develop) in all groups.

**Example:**
- Model says "80% depression risk" for White patient → 80 out of 100 actually have depression
- Same model says "80% depression risk" for Black patient → actually only 45 out of 100 have depression (miscalibrated)

**When to use:**
- When using probability predictions to make decisions
- Most important for clinical decision-making

### Choosing a Framework: Decision Tree

```
What's your purpose?

A. Diagnosis with equal accuracy across groups?
   → Use EQUALIZED ODDS
   
B. Preventing harm to underdiagnosed groups?
   → Use CALIBRATION + sensitivity analysis
   
C. Detecting unfairness in how assessment is used?
   → Use DEMOGRAPHIC PARITY as diagnostic
   
D. Assessment + Treatment matching?
   → Use CALIBRATION + outcome tracking
```

---

## Pre-Launch Bias Audit Checklist

### Phase 1: Test/Tool Selection (Before You Code)

```
CONSTRUCT & VALIDITY
[ ] Assessment validated on population like yours (same age, culture, language)
[ ] Validation study examined fairness/bias explicitly (or you've assessed it)
[ ] Known limitations in cultural groups documented
[ ] Item-level analysis shows no DIF for your population
[ ] If test is recent, no newer version with better fairness profile?

DATA SOURCES (if building proprietary assessment/AI)
[ ] Training data is demographically diverse (not 80%+ one group)
[ ] No proxy variables that correlate with protected attributes (e.g., zip code)
[ ] Excluded biased/labeled data (e.g., historical underdiagnosis data)
[ ] Separate, diverse validation set for fairness testing
```

### Phase 2: Implementation (During Development)

```
DESIGN & METHOD BIAS
[ ] Assessment available in multiple languages (or plan for it)
[ ] Clear instructions (readable at 8th-grade level)
[ ] No time limits unless timing is what you're measuring
[ ] No literacy barriers (if assessing other constructs)
[ ] Accessibility for cognitive/visual/hearing disability
[ ] Tested with actual target population (diverse users, not just team members)

SCORING & ALGORITHM
[ ] Scoring rules identical across all groups (not personalized cutoffs by demographics)
[ ] If using ML, model accuracy tested on balanced demographic groups
[ ] Fairness metrics computed (equalized odds, calibration, demographic parity)
[ ] Sensitivity analysis done (what if we adjusted algorithm threshold by group? effect?)
[ ] Clinician review process doesn't amplify algorithmic bias
```

### Phase 3: Interpretation & Deployment (Before Launch)

```
INTERPRETATION BIAS
[ ] Clinicians trained on assessment use + bias awareness
[ ] Structured interpretation guidelines (not subjective judgment)
[ ] Case vignettes tested: Identical symptoms, different demographic → same interpretation?
[ ] Audit sample of interpretations for demographic bias in language/recommendations
[ ] Optional: Blind demographic data during clinician interpretation review

MONITORING POST-LAUNCH
[ ] Diagnosis rates tracked by demographic group (monthly reports)
[ ] Accuracy re-computed on diverse user population (quarterly)
[ ] User feedback solicited on experiences across demographics
[ ] Disparities trigger investigation: Why? (Real difference? Bias? Method?)
[ ] Fairness improvement plan if disparities found
```

---

## Common Bias Patterns & Fixes

### Pattern 1: Underdiagnosis in Minority Populations

**Symptom:**
- Depression diagnosed in 12% of White users, 7% of Black users (same symptoms asked)
- Not explained by prevalence differences (if anything, depression more common in underresourced communities)

**Root causes:**
- Historical underdiagnosis (training data reflects this bias)
- Construct bias (symptoms culturally expressed differently)
- Method bias (assessment not translated/culturally adapted)
- Interpretation bias (clinician attributes symptoms to "stress," not disorder)

**Fixes (in order of priority):**
1. **Interpret ≠ diagnose.** Change app language from "You have depression" to "Your symptoms suggest depression; see a doctor"
2. **Check for construct bias.** Do depression symptoms show differently by culture? Adapt items/interpretation.
3. **Retrain algorithm** on diverse data, optimize for equalized sensitivity.
4. **Implement bias monitoring.** Flag if diagnosis rate drops below threshold in any demographic group.

### Pattern 2: Overdiagnosis in Majority Population

**Symptom:**
- Anxiety diagnosed in 15% of White college students, 8% of other demographic
- Real difference? Or test capturing White anxiety while missing other groups' expressions?

**Root causes:**
- Test designed by/for one demographic
- Norms based on that group
- Algorithm trained predominantly on that group
- Interpretation standards biased toward that group's presentation

**Fixes:**
1. **Validate across groups.** Does test discriminate (correctly predict clinical anxiety) equally?
2. **If DIF found,** remove/modify items or compute group-specific cutoffs.
3. **Rebalance training data.** Ensure algorithm sees diverse expressions of anxiety.
4. **Reinterpret.** Teach clinicians: Same score may mean different things in different groups.

### Pattern 3: Algorithm Accuracy Varies Widely by Group

**Symptom:**
- Depression classifier: 90% accurate for White users, 65% accurate for Asian users
- Not OK—fairness violation

**Root causes:**
- Training data mostly White (90%)
- Model optimized for overall accuracy, not group fairness
- No validation on diverse hold-out set

**Fixes:**
1. **Rebalance training data.** 70/30 split: 70% from underrepresented group for fairness retraining
2. **Retrain with fairness loss.** Optimize for equalized odds, not overall accuracy.
3. **Test on diverse hold-out set.** Ensure accuracy threshold met for all groups before deployment.
4. **Post-deployment monitoring.** If accuracy drops for any group, trigger retraining.

---

## Fairness Metrics: How to Compute & Interpret

### Metric 1: Sensitivity (True Positive Rate) by Group

**What it measures:** Of people who actually have the condition, what % does assessment correctly identify?

**Formula:**
```
Sensitivity = (True Positives) / (True Positives + False Negatives)
            = % correctly identified with condition
```

**Fairness check:**
```
Group A sensitivity: 85% (of 100 people with depression, 85 identified)
Group B sensitivity: 72% (of 100 people with depression, 72 identified)

Difference of 13% = fairness concern (Group B underdiagnosed)
```

**Fix:** Adjust algorithm threshold to increase Group B sensitivity (may decrease specificity for Group B, but acceptable for screening).

### Metric 2: Specificity (True Negative Rate) by Group

**What it measures:** Of people who DON'T have the condition, what % correctly not diagnosed?

**Formula:**
```
Specificity = (True Negatives) / (True Negatives + False Positives)
            = % correctly identified without condition
```

**Fairness check:**
```
Group A specificity: 92% (of 100 without depression, 92 correctly identified)
Group B specificity: 88% (of 100 without depression, 88 correctly identified)

Difference of 4% = smaller concern but worth monitoring
```

### Metric 3: Positive Predictive Value (PPV) by Group

**What it measures:** If assessment says someone has the condition, how likely is it true?

**Formula:**
```
PPV = (True Positives) / (True Positives + False Positives)
    = How confident can user/clinician be in a positive result?
```

**Fairness check:**
```
Group A PPV: 88% (if app says "depression," 88% actually have it)
Group B PPV: 76% (if app says "depression," only 76% actually have it)

Group B users get false alarms more often = fairness concern
```

### Metric 4: Demographic Parity (Equal Diagnosis Rates)

**What it measures:** Are diagnosis rates the same across groups?

**Formula:**
```
Rate_GroupA = (# diagnosed in A) / (total in A)
Rate_GroupB = (# diagnosed in B) / (total in B)

Fairness check: Are rates within 10% of each other?
(If not, investigate why)
```

**Caution:** Equal rates ≠ fair, if underlying condition prevalence differs.

---

## Building Fairness into the Development Process

### Step 1: Fairness Requirements Document

Before coding, write down:

```
FAIRNESS REQUIREMENTS

Minimum sensitivity (catch disease correctly):
  [ ] 85% overall
  [ ] 85% minimum in EVERY demographic group
  
Minimum specificity (avoid false alarms):
  [ ] 90% overall
  [ ] 88% minimum in EVERY demographic group
  
Calibration (predictions reliable):
  [ ] If algorithm says "80% risk," true risk within [75%-85%]
  [ ] Calibration error <5% in all demographic groups
  
Demographic parity:
  [ ] Diagnosis rate difference between largest & smallest group <10%
  [ ] If larger: Investigate & document reason
```

### Step 2: Fairness Testing Protocol

**Before launch, run:**

```
1. OVERALL PERFORMANCE
   - Accuracy, sensitivity, specificity, PPV, NPV
   - Compute on balanced test set (equal # from each demographic group)

2. STRATIFIED PERFORMANCE
   - Repeat metrics separately for each demographic group
   - Create fairness report (compare across groups)
   
3. CALIBRATION CHECK
   - For "high risk" (80%+) predictions: What % actually positive?
   - For "low risk" (20%-) predictions: What % actually negative?
   - Should match stated probabilities in all groups

4. BIAS ANALYSIS
   - Run DIF analysis (if using published test)
   - Check for spurious correlations (does model use proxy for demographics?)
   - Sensitivity analysis: If we change algorithm threshold by group, does fairness improve?
   
5. HUMAN REVIEW
   - Clinician reviews sample results (n=50) from each demographic group
   - Consistent interpretation standards applied?
   - Any patterns in who gets referred, who doesn't?
```

### Step 3: Fairness Decision Tree

```
Does assessment meet fairness requirements?

YES → Green light for deployment
      Plan quarterly fairness audits

NO → What's wrong?

  A. Sensitivity too low in Group B?
     → Adjust algorithm threshold (lower cutoff) for Group B
     → Accept lower specificity for Group B (more false positives) to catch more true positives
     
  B. Spurious correlations (model using proxy variables)?
     → Remove correlated features
     → Retrain model without them
     
  C. Training data imbalanced?
     → Rebalance: Oversample underrepresented groups OR
     → Use fairness-aware ML (downweight majority group in loss function)
     → Retrain & retest
     
  D. Construct bias (test itself biased)?
     → Item-level modification or cultural adaptation needed (see 05)
     → Revalidation required
     
If unfixable → Don't deploy for that demographic group yet
              (Deploy only for groups where fairness met)
              (Disclose limitation: "Not yet validated for Group B")
```

---

## Post-Launch Fairness Monitoring

### Monthly Dashboard (Track These)

```
DIAGNOSIS RATES BY DEMOGRAPHIC GROUP
- % diagnosed (condition present/absent)
- Red flag: Rate drops >10% for any group → investigate

ACCURACY BY DEMOGRAPHIC GROUP
- Sensitivity, specificity, PPV by group
- Red flag: Drops >5% for any group → investigate

USER FEEDBACK BY DEMOGRAPHIC GROUP
- "Results felt accurate/relevant?" by race, gender, age, language
- Qualitative: Any patterns in criticism?

CLINICIAN INTERPRETATION CONSISTENCY
- Sample audit (n=20): Same scenario, different demographics
- Do clinicians interpret identically?
```

### Quarterly Deep Dive (Every 3 Months)

```
1. Re-compute fairness metrics on new data
2. Compare to baseline (launch metrics)
3. Identify any emerging disparities
4. Root cause analysis (data drift? algorithm learned bias? cultural change?)
5. Plan remediation if needed
```

### What Triggers Investigation?

```
RED FLAGS (Investigate Immediately):
[ ] Diagnosis rate drops >15% for any group
[ ] Sensitivity drops >10% for any group
[ ] PPV below threshold (e.g., <80%) in any group
[ ] Clinician interpretation differs by demographics (even unintentionally)
[ ] User complaints cluster by demographic (e.g., "results feel off")
[ ] New demographic group shows different accuracy (algorithm drift)
```

---

## Summary: Bias Prevention Checklist

### ✅ TEST/TOOL SELECTION
- [ ] Validated for your population (same age, culture, language, condition)
- [ ] No known construct/method bias for your demographics
- [ ] Norms current (within 10 years)

### ✅ ALGORITHM DEVELOPMENT
- [ ] Diverse training data (not 80%+ one group)
- [ ] Fairness metrics computed (equalized odds, calibration)
- [ ] Accuracy tested separately for each demographic group
- [ ] Validation on separate, diverse hold-out set

### ✅ IMPLEMENTATION
- [ ] Multiple language support
- [ ] No literacy/accessibility barriers
- [ ] Structured interpretation (not subjective)
- [ ] Clinician bias training

### ✅ DEPLOYMENT
- [ ] Fairness report generated
- [ ] Requirements met in all demographic groups
- [ ] Monitoring dashboard set up
- [ ] Remediation plan if disparities found

### ✅ ONGOING
- [ ] Monthly fairness metrics tracked
- [ ] Quarterly deep dive audits
- [ ] Annual bias re-testing
- [ ] User feedback solicited & analyzed

---

## References

- Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in gender classification. Conference on Fairness, Accountability and Transparency, 77-91.
- Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. Science, 366(6464), 447-453.
- Dreisbach, C. & Dorner, N. (2019). Fairness in machine learning systems. [AWS ML Fair Lending Guide](https://pages.awscloud.com/aws-machine-learning-fairness-lending.html)
- APA Standards for Educational and Psychological Testing (2014)
- Code of Fair Testing Practices (2004)

---

**Last reviewed:** 2026-03-21  
**Confidence level:** High (research-based + APA standards)  
**Cross-references:** 01-Ethical-Assessment-Principles.md; 05-Cultural-Adaptation-of-Assessments.md; 07-Assessment-Ethics-Audit-Framework.md

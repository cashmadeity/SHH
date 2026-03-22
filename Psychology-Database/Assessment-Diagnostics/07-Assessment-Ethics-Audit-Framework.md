# Assessment Ethics Audit Framework

**Source:** APA Standards 1.04-1.05 (Ethical Standards), 9.01-9.11 (Assessment); Best practices in clinical governance  
**Status:** Pre-launch & post-deployment audit tool  
**Scope:** Self-audit, internal review, external validation before deployment

---

## The 5-Level Audit Model

Assessment ethics requires iterative validation. Use this framework:

```
Level 1: Self-Audit (Your team, internal)
         ↓
Level 2: Internal Expert Review (Ethicist/clinician on staff)
         ↓
Level 3: External Expert Review (Independent evaluator)
         ↓
Level 4: User Testing (50+ diverse users)
         ↓
Level 5: Post-Launch Monitoring (Ongoing surveillance)
```

Launch only when **Levels 1-2 passed** with **plan for Level 4**. Level 3 highly recommended.

---

## Level 1: Self-Audit (You Do It)

**Time:** 4-6 hours for assessment team  
**Output:** Checklist + gap report  
**Decision:** Go/no-go to Level 2

### Section 1.1: Assessment Selection & Validity

```
ASSESSMENT VALIDITY
[ ] Assessment selected (name & version documented)
[ ] Published validation study exists (peer-reviewed)
[ ] Validation includes YOUR population (age, culture, language)
[ ] Reliability coefficients (α > 0.70 minimum) documented
[ ] Validity evidence (sensitivity/specificity or r > 0.60) documented
[ ] Manual current (published within 15 years)
[ ] If digital format, digital validation study exists
[ ] Known limitations documented (false positive/negative rates)

If any unchecked:
→ STOP. Do not proceed without addressing.
→ Either use different assessment, or conduct validation study.
→ Document decision.
```

### Section 1.2: Scope of Practice & Competence

```
TEAM COMPETENCE
[ ] Lead assessor licensed (psychologist, licensed counselor, etc.)
[ ] Lead assessor has formal training in assessment (not self-taught)
[ ] Lead assessor has supervised experience (25+ cases)
[ ] Supervision plan in place (external supervisor, ongoing)
[ ] Team trained on THIS specific assessment
[ ] Scope of practice clearly defined (what we assess, what we don't)
[ ] Scope documented in app/website
[ ] Referral criteria identified (when to refer)
[ ] Referral network established (tested, not just links)

If any unchecked:
→ You're not competent yet. Do more training.
→ Plan training; document when complete.
→ Re-audit after training.
```

### Section 1.3: Bias Screening

```
BIAS PREVENTION
[ ] Assessment tested for bias (DIF analysis or research review)
[ ] Training data diverse (if ML, not 80%+ one demographic)
[ ] Model accuracy tested separately by demographic group
[ ] Fairness metrics computed (equalized odds, calibration)
[ ] Cutoff scores justified (not just default)
[ ] Cultural adaptation considered (if serving diverse populations)
[ ] Language adaptation completed (if offering in other languages)
[ ] Sensitivity analysis done (what if we adjusted by demographics?)

If any unchecked:
→ Plan bias audit (2 weeks)
→ Document findings
→ Mitigate (modify items, adjust cutoffs, resample data, etc.)
→ Re-audit after mitigation.
```

### Section 1.4: Informed Consent

```
CONSENT DESIGN
[ ] Consent screen created (separate, not in Terms)
[ ] Plain language (8th-grade reading level)
[ ] All 10 elements included (purpose, procedures, risks, etc.)
[ ] "What it is NOT" explicitly stated
[ ] Voluntariness clear (can decline without penalty)
[ ] Data use disclosed (who sees results? How long kept?)
[ ] Comprehension check included (user explains back)
[ ] Easy to decline (one click, no barriers)
[ ] Consent documented (recorded with results)
[ ] Optional uses separated (research consent ≠ assessment consent)

If any unchecked:
→ Revise consent (1-2 hours)
→ Have clinician review for clarity
→ Flesch reading ease test (should be 80+)
→ Test with 3-5 target users for comprehension
→ Document revisions
```

### Section 1.5: Data Security

```
ENCRYPTION & ACCESS
[ ] Data encrypted at rest (AES-256)
[ ] Data encrypted in transit (TLS 1.2+)
[ ] Access control implemented (MFA for staff)
[ ] Role-based access (clinicians see only own clients)
[ ] Audit logging in place (all access logged)
[ ] Session timeout configured (15 min inactivity)

RETENTION & DELETION
[ ] Retention policy documented (how long kept)
[ ] Automatic deletion after retention period
[ ] User deletion request process (easy, 30-day window)
[ ] Secure deletion method (cryptographic, not just delete)

VENDOR COMPLIANCE
[ ] Vendors identified (cloud host, payment processor, etc.)
[ ] Vendors audited (SOC 2 or ISO 27001)
[ ] BAAs signed (Business Associate Agreements)
[ ] Breach notification plan (what do we do?)

If any unchecked:
→ Security review (1-2 weeks, involve IT/security team)
→ Fix gaps (encryption, access control, etc.)
→ Document fixes
→ Re-audit security section
```

### Section 1.6: Interpretation & Results

```
RESULTS DESIGN
[ ] Results explained in plain language (no jargon)
[ ] Limitations stated ("Not a diagnosis")
[ ] "What it is NOT" clearly stated
[ ] No false certainty (not "You have X")
[ ] Interpretation includes context (recent stressors? language?)
[ ] Referral path clear (when to see doctor/therapist)
[ ] Resources provided (links to help, therapist directory)
[ ] User understanding checked (do they get it?)

CLINICAL REVIEW PROCESS
[ ] All results reviewed by licensed clinician
[ ] Clinician trained on assessment
[ ] Concerning results flagged (red flags defined)
[ ] High-risk results trigger immediate response (crisis protocol)
[ ] Documentation of review (who reviewed, when, findings)

If any unchecked:
→ Revise results page (with clinician)
→ Define review process (SOP)
→ Train clinician
→ Document process
```

### Section 1.7: Crisis Handling

```
CRISIS PROTOCOL
[ ] Suicidal/homicidal ideation detected (criteria defined)
[ ] 988 crisis line information displayed (button to call)
[ ] Crisis resources provided (crisis text line, local ER)
[ ] User encouraged to seek help immediately
[ ] If possible, emergency contact notified (if info available)
[ ] Documentation of crisis event (what user said, what we did)

If any unchecked:
→ Design crisis protocol (1 hour)
→ Add crisis button & resources to app
→ Test with non-crisis user (make sure it works, doesn't alarm)
→ Brief team on protocol
```

### Self-Audit Output

Create a report:

```
LEVEL 1 SELF-AUDIT REPORT

Date: [date]
Assessment: [name & version]
Team lead: [name, credentials]

SUMMARY:
[ ] Validity: PASS / FAIL / CONDITIONAL
[ ] Competence: PASS / FAIL / CONDITIONAL
[ ] Bias: PASS / FAIL / CONDITIONAL
[ ] Consent: PASS / FAIL / CONDITIONAL
[ ] Security: PASS / FAIL / CONDITIONAL
[ ] Interpretation: PASS / FAIL / CONDITIONAL
[ ] Crisis: PASS / FAIL / CONDITIONAL

OVERALL: READY FOR LEVEL 2 / NOT YET

GAPS IDENTIFIED:
[List any "not checked" items]

TIMELINE TO FIX:
[Plan for addressing gaps]

SIGNED: _________________ DATE: _______
```

---

## Level 2: Internal Expert Review

**Time:** 3-4 hours  
**Reviewer:** Internal ethicist, licensed clinician, or external consultant  
**Decision:** Go/no-go for Level 3 & 4

### What Reviewer Checks

```
QUESTIONS FOR REVIEWER:

1. VALIDITY QUESTION
   "Does the assessment measure what we claim it measures?
   Is it valid for this population?"
   
   Look for:
   - Peer-reviewed evidence
   - Population match
   - Known limitations acknowledged
   
   Verdict: Safe to use? YES / NO / WITH CAVEATS

2. COMPETENCE QUESTION
   "Is this team qualified to interpret results?
   Would I trust them with MY assessment?"
   
   Look for:
   - Clinician credentials
   - Training specificity
   - Supervision plan
   - Evidence of other successful assessments
   
   Verdict: Team competent? YES / NO / NEED MORE TRAINING

3. BIAS QUESTION
   "Could this assessment harm people because of bias?
   Is fairness addressed?"
   
   Look for:
   - Diversity in training/validation data
   - Fairness metrics (if ML)
   - DIF analysis or research review
   - Mitigation plans
   
   Verdict: Bias acceptable? YES / NO / NEEDS WORK

4. CONSENT QUESTION
   "Would I feel comfortable consenting to this?
   Is it truly informed?"
   
   Look for:
   - Plain language (reviewer tries to understand)
   - All material info disclosed
   - Comprehension check present
   - No hidden coercion
   
   Verdict: Consent adequate? YES / NO / REVISE

5. SECURITY QUESTION
   "If breached, could I defend this in court?
   Are we protecting data appropriately?"
   
   Look for:
   - Encryption (at rest & in transit)
   - Access control (not everyone sees everything)
   - Audit trails (evidence of who did what)
   - Breach response plan
   
   Verdict: Security acceptable? YES / NO / GAPS

6. INTERPRETATION QUESTION
   "Would I trust the results explanation?
   Could it be misunderstood?"
   
   Look for:
   - Plain language
   - No false certainty
   - Appropriate caveats
   - Referral path clear
   
   Verdict: Results explanation safe? YES / NO / REVISE

7. CRISIS HANDLING QUESTION
   "If someone reports suicidal thoughts, are we safe?
   Will they get help?"
   
   Look for:
   - Crisis detection (how do you identify risk?)
   - Immediate resources (988, local ER)
   - Documentation
   
   Verdict: Crisis response adequate? YES / NO / NEEDS IMPROVEMENT
```

### Level 2 Output

Reviewer completes report:

```
LEVEL 2 INTERNAL EXPERT REVIEW

Date: [date]
Assessment: [name]
Team lead: [name]
Reviewer: [name, credentials, affiliation]

REVIEW VERDICT:

Overall: APPROVED FOR LAUNCH / APPROVED WITH CONDITIONS / NOT APPROVED

Specific verdicts:
- Validity: ________
- Competence: ________
- Bias: ________
- Consent: ________
- Security: ________
- Interpretation: ________
- Crisis: ________

CRITICAL ISSUES (must fix before launch):
1. [Issue]
   → Recommendation: [Fix]
   → Timeline: [By when?]

2. [Issue]
   → Recommendation: [Fix]
   → Timeline: [By when?]

CONDITIONAL APPROVALS (address before Level 4):
1. [Issue]
   → Recommendation: [Fix]
   → Timeline: [By when?]

RECOMMENDATIONS (optional, quality improvement):
1. [Suggestion]
2. [Suggestion]

RISK ASSESSMENT:
Risk of this assessment causing harm: LOW / MODERATE / HIGH

If MODERATE/HIGH, explain:
[Explanation]

Mitigation:
[What will reduce risk?]

NEXT STEPS:
[ ] Fix critical issues (timeline: ___)
[ ] Address conditional issues (timeline: ___)
[ ] Plan Level 3 external review? YES / NO
[ ] Plan Level 4 user testing? (required) YES / NO, scheduled for ___

SIGNED: _________________ DATE: _______
(Reviewer)
```

---

## Level 3: External Expert Review (Recommended)

**Time:** 1-2 weeks  
**Reviewer:** Independent psychologist, ethicist, or assessment specialist (not on your team)  
**Cost:** $2,000-5,000 typical  
**Output:** Written report + recommendations

### Helps With

- **Credibility:** External validation strengthens defense if legal challenge
- **Fresh eyes:** Catches blind spots your team missed
- **Liability:** Insurance may require it; documentation helps defense
- **Marketing:** "Reviewed by [Expert Name], PhD" is credible

### How to Select External Reviewer

```
CRITERIA:

[ ] Licensed psychologist or equivalent credential
[ ] Assessment expertise (not just general psychology)
[ ] No financial interest in your product (independent)
[ ] Willing to be critical (not just rubber-stamp)
[ ] Available in timeline
[ ] References from previous work

QUESTIONS TO ASK:

1. "Have you reviewed similar assessments before?"
2. "What's your process?" (Do they actually test it, or just read?)
3. "How will you report findings?" (Written? Presentation? Both?)
4. "What if you find major issues?" (Are they honest?)
5. "Can we use your name in marketing?" (If positive review)
6. "What's your conflict of interest policy?" (No undisclosed ties)
```

---

## Level 4: User Testing (Required Before Launch)

**Time:** 4-8 weeks  
**Sample size:** 50-100+ users (diverse demographics)  
**Cost:** $5,000-15,000 typical  
**Output:** User feedback report + revisions

### What to Test

```
USABILITY:
- Can users understand consent? (% who misunderstand?)
- Can users complete assessment? (dropout rates?)
- Can users understand results? (% confused?)

ACCURACY:
- Do assessment scores match therapist assessment? (convergent validity)
- Do high-risk users identified by app match therapist assessment?

FAIRNESS:
- Do results feel fair/accurate to different demographic groups?
- Are any groups reporting bias/misidentification?

EMOTIONAL IMPACT:
- Did results distress users? (% reporting distress?)
- Did users feel stigmatized? (% reporting shame/judgment?)
- Would they recommend to friend? (% yes?)
```

### User Testing Protocol

```
SAMPLE RECRUITMENT:
[ ] Recruit 50-100 users (target demographics represented)
[ ] Diverse: Race, gender, age, education, socioeconomic status, language
[ ] Condition representative (if assessing depression, recruit people with/without depression)
[ ] Informed consent (they know they're testing a new tool)

PROCEDURES:
1. User takes assessment (actual experience)
2. Qualitative interview (30 min)
   - "What was that like?"
   - "Did you understand the questions?"
   - "Do the results feel accurate?"
   - "Would you use this again?"
   - "What would make it better?"
3. Quantitative survey (10 questions)
   - Clarity (1-5 scale)
   - Fairness (1-5 scale)
   - Would recommend (yes/no)
4. Compare results to gold-standard (clinician assessment)
   - Sensitivity (catch people with condition)
   - Specificity (don't falsely diagnose)

ANALYSIS:
- Quantitative: % met clarity threshold, accuracy metrics
- Qualitative: Common themes (what do users like/dislike?)
- Demographic breakdown: Do scores vary by group?
- Red flags: Any subgroup significantly disadvantaged?

REPORT:
[User Testing Report]
- User demographics
- Quantitative results (tables)
- Qualitative themes
- Red flags & mitigation
- Recommendations
```

---

## Level 5: Post-Launch Monitoring

**Ongoing, forever**  
**Frequency:** Monthly review; quarterly deep dive; annual comprehensive audit  
**Decision:** Continue as-is / Minor improvements / Major overhaul

### Monthly Monitoring Metrics

```
USAGE METRICS:
- # of assessments completed
- Completion rate (% who finish assessment)
- Dropout points (where do users quit?)
- Time to complete (is it too long?)

ACCURACY METRICS:
- # of users who report results felt accurate/inaccurate
- False positive rate (labeled as having condition, don't)
- False negative rate (missed people with condition)
- Correlation with independent clinician assessment

FAIRNESS METRICS:
- Diagnosis rates by demographic group (any disparities emerging?)
- User satisfaction by demographic group (any group less satisfied?)
- Any pattern in complaints by demographic?

SAFETY METRICS:
- # of crisis/suicidal reports
- Crisis protocol invoked (# times)
- Were crisis users safely referred? (# reached crisis line)
- Any adverse events (user harmed by false diagnosis, missed diagnosis)?

RED FLAGS (Trigger Investigation):
[ ] Dropout rate increases >5% (tool getting worse?)
[ ] Complaint cluster (3+ users same issue in month)
[ ] Diagnosis rate changes >10% (algorithm drift?)
[ ] Accuracy drops in any demographic group
[ ] Crisis cases increase (more or fewer than expected?)
```

### Quarterly Deep Dive Review

```
Every 3 months, spend 4 hours reviewing:

1. TRENDS
   - Are metrics stable? Improving? Worsening?
   - Any emerging patterns?
   
2. INCIDENTS
   - Review adverse events (missed diagnoses, crisis cases)
   - Root cause analysis (why did it happen?)
   - Preventive measures (how to avoid next time?)
   
3. USER FEEDBACK
   - Aggregate qualitative feedback (surveys, app reviews)
   - Common themes (what do people want?)
   - Demographic differences (does feedback vary by group?)
   
4. CLINICAL UPDATES
   - Have assessment standards changed?
   - New research on construct?
   - Norms updated?
   - Algorithm improvements available?
   
5. COMPLIANCE CHECK
   - Are we still following protocol?
   - Staff still trained?
   - Consent still compliant?
   - Data security still solid?
   
6. DECISION POINT
   - Continue as-is? (all metrics good)
   - Minor improvements? (tweak something small)
   - Major overhaul? (something broken, need redesign)
```

### Annual Comprehensive Audit

Once per year, redo Level 1 audit:

```
ANNUAL AUDIT:
[ ] Re-run self-audit (all sections)
[ ] Review external expert findings (if Level 3 done)
[ ] Analyze post-launch monitoring data (12 months)
[ ] User satisfaction survey (sample of 20+ users)
[ ] Team competence check (staff still trained?)
[ ] Compliance verification (HIPAA, GDPR, state laws)
[ ] Benchmark against new research (assessment still best option?)

OUTPUT:
- Annual audit report
- Recommendations for next year
- Updated risk assessment
- Plan for next year improvements
```

---

## Quick Reference: Pre-Launch Checklist

```
PRE-LAUNCH CHECKLIST (Use Before Going Live)

LEVEL 1: SELF-AUDIT ✓
[ ] Completed by team
[ ] All sections addressed
[ ] Gaps identified & plan to fix
[ ] Timeline established
[ ] Signed off

LEVEL 2: INTERNAL REVIEW ✓
[ ] External clinician/ethicist assigned
[ ] Review completed
[ ] No critical issues remaining
[ ] Conditional issues addressed
[ ] Plan for Level 3 & 4 (required)

LEVEL 3: EXTERNAL EXPERT REVIEW (Recommended)
[ ] Expert selected & contracted
[ ] Review completed
[ ] Major issues addressed
[ ] Report filed

LEVEL 4: USER TESTING (Required)
[ ] Protocol designed
[ ] Sample recruited (50+ diverse users)
[ ] Testing completed
[ ] Analysis done
[ ] Results fed back into design
[ ] Revisions made based on feedback

FINAL CHECKS:
[ ] All critical issues resolved
[ ] All team trained & certified
[ ] Consent process final
[ ] Security verified
[ ] Crisis protocol tested
[ ] Monitoring dashboard set up
[ ] Launch date set
[ ] Insurance/legal cleared
[ ] Marketing claims reviewed for accuracy

LAUNCH APPROVAL: _________________ DATE: _______
(Executive sponsor)
```

---

## References

- American Psychological Association (2017). Ethical Principles of Psychologists and Code of Conduct, Standards 1.04-1.05, 9.01-9.11
- American Educational Research Association, APA, NCME (2014). Standards for Educational and Psychological Testing
- FDA Guidance on Clinical Decision Support Software (2019)

---

**Last reviewed:** 2026-03-21  
**Confidence level:** High (APA standards-based, peer-reviewed frameworks)  
**Cross-references:** All 01-06 documents; Ethics-Guardrails KB

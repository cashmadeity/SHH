# Validation Framework: Auditing Psychology Apps for Ethical Standards

**Purpose:** Systematic process to validate that psychology applications meet ethical standards before launch and during operation.

**Who uses this:** Developers, product managers, ethics reviewers, independent auditors.

**How often:** Before launch, then annually minimum.

---

## The 5-Level Validation Model

### Level 1: Self-Audit (Developer)
**What:** Developer reviews own app against standards  
**Time:** 4-6 hours  
**Pass rate needed:** 90%+ on critical items

### Level 2: Expert Review (Internal Ethics Board)
**What:** Internal team (therapist, ethicist, legal) reviews against standards  
**Time:** 1-2 weeks  
**Pass rate needed:** 95%+ on critical items

### Level 3: External Expert Review
**What:** Independent licensed therapist/psychologist reviews  
**Time:** 2-4 weeks  
**Cost:** $5-15K typically  
**Pass rate needed:** 100% on critical items

### Level 4: User Testing (Diverse Populations)
**What:** Testing with 50+ users across demographic groups  
**Time:** 4-8 weeks  
**Cost:** $10-25K typically  
**Pass rate needed:** 95%+ user satisfaction on safety/trust

### Level 5: Post-Launch Monitoring
**What:** Ongoing audit via user feedback, incident tracking, annual review  
**Time:** Continuous  
**Cost:** Built into operations  
**Pass rate needed:** <0.1% harm reports per user

---

## Level 1: Self-Audit Checklist

### Phase 1A: Core Ethics Review (yes/no/N/A)

#### 1. Beneficence & Non-maleficence
- [ ] Is there a clear, evidence-based clinical rationale for each feature?
- [ ] Have we tested for psychological harms (anxiety, shame, dependence)?
- [ ] Can users exit gracefully (not penalized for leaving)?
- [ ] Are crisis resources integrated and accessible?
- [ ] Is the app scope clearly defined (what it helps with)?

**If no to any:** Cannot launch. Redesign required.

#### 2. Fidelity & Responsibility
- [ ] Is it clear what the app is (not a licensed therapist)?
- [ ] Are limitations stated on homepage/signup?
- [ ] Is there 24/7 support for serious issues?
- [ ] Is there an incident response plan?
- [ ] Are terms of service honest about what app will/won't do?

**If no to any:** Cannot launch. Fix disclosures.

#### 3. Integrity
- [ ] Are all marketing claims supported by evidence?
- [ ] Is AI/algorithm methodology transparent or documented?
- [ ] Are data practices disclosed accurately?
- [ ] Are research findings reported honestly?
- [ ] Is the privacy policy understandable (not legal jargon)?

**If no to any:** Cannot launch. Remove unsupported claims or add evidence.

#### 4. Justice
- [ ] Has the app been tested with diverse populations (race, age, gender, disability, SES)?
- [ ] Are there accessibility features (WCAG 2.1 AA)?
- [ ] Is pricing equitable (free/low-cost tier available)?
- [ ] Is the app available in at least 2 languages?
- [ ] Have we checked AI/recommendations for bias across groups?

**If no to majority:** Cannot launch. Redesign for equity.

#### 5. Respect for Rights & Dignity
- [ ] Is informed consent genuine (plain language, not forced)?
- [ ] Can users delete data easily?
- [ ] Are dark patterns absent?
- [ ] Is data encrypted?
- [ ] Can users say no to research/marketing without penalty?

**If no to any:** Cannot launch. Fix consent/privacy.

---

### Phase 1B: Manipulation Check

Go through [Red-Flags/Manipulative-Patterns.md](Red-Flags/Manipulative-Patterns.md) and answer:

For each red flag category:
1. **Addiction mechanics** → App avoids all items? ✅ Pass / ❌ Fail
2. **Dark patterns** → App avoids all items? ✅ Pass / ❌ Fail
3. **Exploiting vulnerabilities** → App avoids all items? ✅ Pass / ❌ Fail
4. **Consent violations** → App avoids all items? ✅ Pass / ❌ Fail
5. **Competence violations** → App avoids all items? ✅ Pass / ❌ Fail
6. **No escalation path** → App has escalation path? ✅ Pass / ❌ Fail
7. **Diversity failures** → App tested with diverse users? ✅ Pass / ❌ Fail
8. **Bias in AI** → AI tested for bias? ✅ Pass / ❌ Fail
9. **Pathologizing culture** → Content reviewed for bias? ✅ Pass / ❌ Fail
10. **Research exploitation** → Consent separate for research? ✅ Pass / ❌ Fail

**If fail on any critical item (competence, escalation, consent, bias):** Fix before launch.

---

### Phase 1C: Legal & Compliance Check

- [ ] **HIPAA:** Does app handle health data?
  - If yes: encrypted at rest? ✅ / ❌
  - If yes: TLS in transit? ✅ / ❌
  - If yes: access controls? ✅ / ❌
  - If yes: breach notification plan? ✅ / ❌
  - If yes: vendors have BAAs? ✅ / ❌

- [ ] **GDPR (if EU users):** Explicit consent before data collection? ✅ / ❌
- [ ] **CCPA (if CA users):** Right to delete, privacy policy? ✅ / ❌
- [ ] **Terms of Service:** Honest about app limitations? ✅ / ❌
- [ ] **Privacy Policy:** Readable in <5 minutes? ✅ / ❌

**If no to legal items:** Consult healthcare attorney before launch.

---

### Phase 1D: Therapeutic Alliance Check

Using [Best-Practices/Therapeutic-Alliance.md](Best-Practices/Therapeutic-Alliance.md):

- [ ] Does app reflect back user's concerns (not generic)?
- [ ] Are user's goals (not app's) central?
- [ ] Is the app honest about what it is?
- [ ] Does it respect user autonomy (options, not directives)?
- [ ] Is tone warm and boundaried (not clinical-robotic)?
- [ ] Does it escalate appropriately to human help?

**If failing majority:** Redesign tone/collaboration.

---

## Level 2: Expert Review (Internal Ethics Board)

### Composition
- **Minimum team:**
  - Licensed mental health professional (LMHP) or psychologist
  - Ethicist (or someone trained in research ethics)
  - Legal counsel (healthcare attorney, ideally)
  - Product manager / developer

- **Recommended additions:**
  - Data scientist (for AI/bias review)
  - Accessibility specialist
  - Diversity consultant (cultural competence)

### Process

**Step 1: Briefing (1 hour)**
- Developers present: What does the app do? Who is it for? What claims do we make?
- Board asks clarifying questions

**Step 2: Independent Review (1 week)**
- Each board member uses Level 1 checklist independently
- They also read:
  - Privacy policy
  - Terms of service
  - Any clinical claims / research cited
  - Feature walkthroughs (demo video preferred)

**Step 3: Discussion (2 hours)**
- Board meets and compares findings
- Debate disagreements
- Reach consensus on pass/fail

**Step 4: Report (1 week)**
- Written report with:
  - Pass/fail overall
  - Critical issues (must fix to launch)
  - Major issues (should fix before launch)
  - Minor issues (can fix post-launch)
  - Recommendations

**Step 5: Remediation & Re-review (2-4 weeks)**
- Developers fix issues
- Board re-reviews critical items
- Approves final version

---

## Level 3: External Expert Review

### When to do it
- Before Series A/B fundraising
- Before major marketing campaign
- If internal board is non-existent or weak
- If controversy/harm reported
- If app makes significant clinical claims

### How to find reviewers
- **Academic clinical psychology departments** (universities)
- **Mental health professional organizations** (APA, NAMI, therapist associations)
- **Ethical AI consultancies**
- **Healthcare compliance firms**

### What to expect
- **Cost:** $5-15K
- **Timeline:** 2-4 weeks
- **Deliverable:** Written audit report

### Reviewer's scope
- Full app functionality review
- Evidence checking (are clinical claims supported?)
- User testing with representative sample (often included)
- Bias/equity audit
- Privacy/legal compliance review
- Recommendations for improvement

---

## Level 4: User Testing (Diverse Populations)

### Who to test with

**Minimum sample:** 50+ users  
**Composition:** Represent actual user demographic + oversampling marginalized groups

| Demographic | Minimum users | Rationale |
|-------------|---------------|-----------|
| Age 18-25 | 10 | Young adults (common users) |
| Age 26-40 | 10 | Established adults |
| Age 41+ | 10 | Older adults (often under-tested) |
| Women/femme | 15-20 | Often majority of mental health users |
| Men/masc | 10-15 | Often underrepresented in mental health |
| Non-binary/trans | 5-10 | Needs specific testing (often excluded) |
| Non-English speakers | 5-10 | Language access critical |
| People with disabilities | 5-10 | Accessibility critical |
| Low SES | 5-10 | Equity focus |
| Diverse races/ethnicities | Mix across all | Representative of actual user base |

### Testing protocol

**Recruitment:**
- Paid user testing (offer $25-50 gift card)
- Diverse recruitment (not just college students)
- Minimal screening (no heavy exclusions; app should work for diversity of users)

**Session (1 hour per user):**
1. Intro & consent (10 min)
2. Unmoderated walkthrough (30 min)
   - User explores app naturally
   - Researcher observes, asks clarifying questions
3. Structured interview (20 min)
   - "Was anything confusing?"
   - "Did you trust this app with your mental health data?"
   - "What did you like? Dislike?"
   - "Would you use this?"

**Key questions for every user:**
- [ ] "Did the app feel safe to use?" (rate 1-10)
- [ ] "Did you feel understood?" (rate 1-10)
- [ ] "Did you trust the app with your information?" (rate 1-10)
- [ ] "Would you recommend this to a friend?" (yes/no)
- [ ] "Did you notice anything harmful or concerning?"

### Analysis

**Pass criteria:**
- ≥80% report feeling safe
- ≥80% report feeling understood
- ≥70% report trusting the app with data
- ≥60% would recommend to friend
- No critical harm reports

**Fail criteria:**
- Reports of harm, triggering, or distress
- Accessibility barriers that prevent use
- Demographic-specific bias ("This doesn't work for me as a trans person")

---

## Level 5: Post-Launch Monitoring

### Ongoing Audit Process

#### Monthly
- [ ] Review support tickets for harm reports
- [ ] Monitor app crash/error rates
- [ ] Check for unusual user feedback patterns
- [ ] Verify crisis escalation logs (are we catching crisis cases?)

#### Quarterly
- [ ] User satisfaction survey (random 10% of users)
  - "Did using the app help you?" (yes/no)
  - "Did anything feel harmful?" (yes/no)
  - "Would you recommend?" (yes/no/unsure)
- [ ] Audit access logs for unauthorized data access
- [ ] Review privacy/HIPAA incidents (zero should happen; >0 = crisis)

#### Annually
- [ ] Full re-audit using Level 1 & 2 checklists
- [ ] Update for new APA ethical guidelines
- [ ] Re-check AI for bias (retrain if drift detected)
- [ ] Legal compliance review (HIPAA/GDPR/CCPA updates)
- [ ] Diverse user testing (20-30 new users, diverse sample)

#### When harm reported
- [ ] Immediate response (within 24 hours)
- [ ] Investigation (what happened? why?)
- [ ] User support (apology, remediation)
- [ ] Prevention (fix to prevent recurrence)
- [ ] Transparency (inform other users if relevant)

---

## Validation Report Template

### Executive Summary
- **App name & version:**
- **Validation date:**
- **Validation level:** (1/2/3/4/5)
- **Overall pass/fail:** ✅ / ⚠️ / ❌
- **Summary:** [1-2 sentences on readiness]

### Results by Category

**Beneficence & Non-maleficence:** ✅ / ⚠️ / ❌
- [ ] Features are evidence-based
- [ ] Tested for harms
- [ ] Crisis escalation in place
- **Issues:** [if any]

**Fidelity & Responsibility:** ✅ / ⚠️ / ❌
- [ ] Clear disclosures
- [ ] Support available
- [ ] Incident response plan
- **Issues:** [if any]

**Integrity:** ✅ / ⚠️ / ❌
- [ ] Claims supported by evidence
- [ ] Methodology transparent
- [ ] Data practices disclosed
- **Issues:** [if any]

**Justice:** ✅ / ⚠️ / ❌
- [ ] Tested with diverse populations
- [ ] Accessible
- [ ] Equitable pricing
- [ ] No bias in AI
- **Issues:** [if any]

**Respect:** ✅ / ⚠️ / ❌
- [ ] Genuine informed consent
- [ ] Data privacy protected
- [ ] No dark patterns
- [ ] Autonomy respected
- **Issues:** [if any]

### Red Flags
- [ ] Addiction mechanics: ✅ No / ⚠️ Minor / ❌ Major
- [ ] Dark patterns: ✅ No / ⚠️ Minor / ❌ Major
- [ ] Consent violations: ✅ No / ⚠️ Minor / ❌ Major
- [ ] Competence issues: ✅ No / ⚠️ Minor / ❌ Major
- [ ] Escalation gaps: ✅ No / ⚠️ Minor / ❌ Major
- [ ] Diversity failures: ✅ No / ⚠️ Minor / ❌ Major
- [ ] Bias in AI: ✅ No / ⚠️ Minor / ❌ Major

### Legal & Compliance
- **HIPAA:** ✅ Compliant / ⚠️ Partial / ❌ Non-compliant
- **GDPR:** ✅ Compliant / ⚠️ Partial / ❌ Non-compliant / N/A
- **CCPA:** ✅ Compliant / ⚠️ Partial / ❌ Non-compliant / N/A
- **Other:** [state laws, etc.]

### Critical Issues (Must Fix)
1. [Issue & impact]
2. [Recommended fix]
3. [Timeline]

### Major Issues (Should Fix)
1. [Issue & impact]
2. [Recommended fix]
3. [Timeline]

### Minor Issues (Can Fix Post-Launch)
1. [Issue & impact]
2. [Recommended fix]

### Recommendations
- [Priority 1]
- [Priority 2]
- [Priority 3]

### Conclusion
[Validator's professional opinion on launch readiness]

**Signed by:** [Validator name, credentials, date]

---

## Decision Framework

### If validation = ✅ PASS
- **Action:** Proceed to launch
- **Condition:** Commit to Level 5 ongoing monitoring
- **Required:** Public summary of validation (transparency)

### If validation = ⚠️ CONDITIONAL PASS
- **Action:** Launch with conditions
- **Example:** "Fix crisis escalation before Day 30. Continue with daily monitoring."
- **Required:** Specific remediation plan with deadlines

### If validation = ❌ FAIL
- **Action:** Do not launch
- **Required:** Major redesign + re-validation before launch

---

**Last reviewed:** 2026-03-20  
**Cross-references:** All other sections in Ethics-Guardrails/

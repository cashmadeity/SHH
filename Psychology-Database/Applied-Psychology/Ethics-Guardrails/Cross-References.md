# Cross-References & Integration Map

**Purpose:** Show how the ethics knowledge base components interconnect and reinforce each other.

**Use this to:** Understand the big picture, navigate related standards, validate your app holistically.

---

## The Ethics Web: How It All Connects

```
                    ┌─────────────────────────────────────┐
                    │   5 APA CORE PRINCIPLES (Foundation) │
                    │                                      │
                    │ • Beneficence & Non-maleficence    │
                    │ • Fidelity & Responsibility         │
                    │ • Integrity                         │
                    │ • Justice                           │
                    │ • Respect for Rights & Dignity      │
                    └─────────────────────────────────────┘
                                  ▲
                  ┌───────────────┼───────────────┐
                  │               │               │
                  ▼               ▼               ▼
            ┌──────────┐    ┌──────────┐    ┌──────────┐
            │ RED      │    │ LEGAL    │    │ BEST     │
            │ FLAGS    │    │COMPLIANCE│   │PRACTICES │
            │          │    │          │    │          │
            │ What NOT │    │ HIPAA    │    │ Therapeutic
            │ to do    │    │ GDPR     │    │ Alliance
            │          │    │ CCPA     │    │ Cultural
            │ Patterns │    │          │    │ Competence
            │ violating│    │ Consent  │    │ Harm
            │ ethics   │    │ Privacy  │    │ Reduction
            │          │    │ Data     │    │ Tech Ethics
            │ • Addic. │    │ Security │    │
            │ • Dark   │    │          │    │ ✅ What to DO
            │ • Exploi-│    │ Breach   │    │
            │   tation │    │ Notifi-  │    │
            │ • Consent│    │ cation   │    │
            │ • Compet-│    │          │    │
            │   ence   │    │ Business │    │
            │ • Crises │    │ Assoc.   │    │
            │ • Divers.│    │ Agreements    │
            │ • Bias   │    │          │    │
            │ • Culture│    │          │    │
            │ • Exploit│    │          │    │
            └──────────┘    └──────────┘    └──────────┘
                  │               │               │
                  └───────────────┼───────────────┘
                                  ▼
                    ┌──────────────────────────┐
                    │  VALIDATION FRAMEWORK    │
                    │                          │
                    │ Level 1: Self-Audit     │
                    │ Level 2: Expert Review  │
                    │ Level 3: External Audit │
                    │ Level 4: User Testing   │
                    │ Level 5: Monitoring     │
                    └──────────────────────────┘
                                  ▼
                    ┌──────────────────────────┐
                    │  DEPLOYMENT & IMPACT    │
                    │                          │
                    │ ✅ Therapist-worthy app  │
                    │ ✅ Ethical, non-harmful  │
                    │ ✅ User trust & safety   │
                    │ ✅ Legal compliance      │
                    │ ✅ Sustainable practice  │
                    └──────────────────────────┘
```

---

## Principle-by-Principle Mapping

### 1. Beneficence & Nonmaleficence: Do Good; Avoid Harm

**Definition:** Strive to benefit; take care to do no harm

**Key Documents:**
- [Red-Flags/Manipulative-Patterns.md](Red-Flags/Manipulative-Patterns.md) — What violates beneficence
  - Addiction mechanics (engagement over wellbeing)
  - Exploiting vulnerabilities
  - Competence overreach (claiming to treat what you can't)
  - No crisis escalation

- [Best-Practices/Therapeutic-Alliance.md](Best-Practices/Therapeutic-Alliance.md) — How to do genuine good
  - Collaboration toward user's goals (not app's)
  - Evidence-based features
  - Recognizing harm and escalating

- [Legal-Compliance/HIPAA-Requirements.md](Legal-Compliance/HIPAA-Requirements.md) — Protecting from legal harm
  - Data security (prevents breaches = prevents harm)
  - Informed consent (user knows what they're agreeing to)
  - Breach notification (minimize damage if breach occurs)

- [Validation-Framework.md](Validation-Framework.md) — Testing for harm
  - Phase 1B: Manipulation check
  - Phase 4: User testing for adverse effects

**In Practice:**
```
Q: "Does this feature do good?"
↓
Check: Evidence-based? [Best-Practices/] ✅
Check: Could it harm? [Red-Flags/] ✅
Check: Is it consensual? [Legal-Compliance/] ✅
Check: Tested with users? [Validation-Framework/] ✅
→ PASS: Safe to include

Q: "Could this inadvertently cause harm?"
↓
Check: Addiction mechanics? [Red-Flags/Manipulative-Patterns#addiction] ❌
Check: Exploiting vulnerabilities? [Red-Flags/Manipulative-Patterns#exploiting] ❌
→ FAIL: Remove or redesign before launch
```

---

### 2. Fidelity & Responsibility: Build Trust; Own Your Impact

**Definition:** Be honest; maintain professional standards; accept responsibility

**Key Documents:**
- [APA-Standards/Five-Core-Principles.md#2-fidelity](APA-Standards/Five-Core-Principles.md) — What fidelity means
  - Being transparent about what you are
  - Clear responsibility chains
  - Honest about limitations
  - Boundaried relationship

- [Red-Flags/Manipulative-Patterns.md#category-2](Red-Flags/Manipulative-Patterns.md) — Fidelity violations
  - Dark patterns (hidden unsubscribe, etc.)
  - Vague informed consent
  - Pretending to be licensed therapist
  - No escalation path for serious issues

- [Legal-Compliance/](Legal-Compliance/) — Legal responsibility
  - Breach notification (owning up when something goes wrong)
  - Business Associate Agreements (taking responsibility with vendors)
  - Terms of service (being honest about limitations)

- [Best-Practices/Therapeutic-Alliance.md#3-authentic-presence](Best-Practices/Therapeutic-Alliance.md) — Building trust
  - Clear about what you are
  - Honest about limitations
  - Responsive support
  - Consistent presence

**In Practice:**
```
Q: "Am I being honest and taking responsibility?"
↓
Homepage: "This app is NOT therapy" [✅ transparent]
Privacy policy: Plain language, clear data practices [✅ honest]
Support: 24/7 escalation for serious issues [✅ responsible]
Marketing: Claims supported by evidence [✅ integrity]
Incident response: Immediate action if breach [✅ responsible]
→ PASS: Trustworthy

Q: "Could I be hiding something?"
↓
Check: Dark patterns in UX? [Red-Flags/Manipulative-Patterns#dark-patterns] 
  Unsubscribe hidden? ❌
  Data deletion requires intervention? ❌
  Auto-renewal without reminder? ❌
→ FIX: Make exit easy
```

---

### 3. Integrity: Be Honest; Don't Deceive

**Definition:** Promote accuracy, honesty, truthfulness; avoid deception

**Key Documents:**
- [APA-Standards/Five-Core-Principles.md#3-integrity](APA-Standards/Five-Core-Principles.md) — Integrity in psychology
  - Claims require evidence
  - Be transparent about AI/algorithms
  - Disclose data use honestly
  - Don't misrepresent research findings

- [Red-Flags/Manipulative-Patterns.md#category-2](Red-Flags/Manipulative-Patterns.md) — Integrity violations
  - Vague informed consent (users don't understand what they're agreeing to)
  - Unsupported marketing claims ("Cure depression in 4 weeks")
  - Hidden AI behavior ("Proprietary algorithm")
  - Cherry-picked research

- [Legal-Compliance/](Legal-Compliance/) — Legal honesty
  - Privacy policy must accurately describe practices
  - Consent must be explicit (no hidden pre-checks)
  - Data practices must match disclosures

**In Practice:**
```
Q: "Am I being fully honest?"
↓
Marketing claim: "This app treats depression"
  → Evidence: RCT showing effectiveness? [search]
     If yes: OK to claim with citation [✅]
     If no: Remove claim or say "May help" [❌ need evidence]

AI recommendation: "You should meditate"
  → User can see: Why is app suggesting this? [✅ transparent]
     or: Magic black box [❌ deceptive]

Privacy: "We use your data to improve the app"
  → Specific: "We analyze your journal to personalize recommendations"
     or: Vague [❌ not honest enough]
```

---

### 4. Justice: Equitable Access; No Discrimination

**Definition:** Ensure equal access and quality; avoid unjust practices from bias or incompetence

**Key Documents:**
- [APA-Standards/Five-Core-Principles.md#4-justice](APA-Standards/Five-Core-Principles.md) — Justice in psychology
  - Equitable access (price, language, accessibility)
  - Test across diverse populations
  - Audit AI for bias
  - Recognize diverse mental health models

- [Red-Flags/Manipulative-Patterns.md#category-4-diversity](Red-Flags/Manipulative-Patterns.md) — Justice violations
  - One-size-fits-all design (tested with only white, educated users)
  - No accessibility features
  - Pathologizing cultural/spiritual beliefs
  - Bias in AI (different outcomes by demographic)

- [Best-Practices/Therapeutic-Alliance.md](Best-Practices/Therapeutic-Alliance.md) — Justice in practice
  - Recognizing diverse mental health frameworks (not just Western)
  - Honoring cultural/spiritual values
  - Accessible communication (plain language, not jargon)

- [Validation-Framework.md#level-4](Validation-Framework.md) — Testing for justice
  - User testing with diverse populations (50+ users across demographics)
  - Bias testing in AI/recommendations
  - Accessibility audit

**In Practice:**
```
Q: "Is my app equitable?"
↓
Demographics tested: [How many users of each group?]
  - Age 18-25: 10 ✅
  - Age 26-40: 10 ✅
  - Age 41+: 10 ✅
  - Women: 15 ✅
  - Men: 10 ✅
  - Trans/NB: 8 ✅
  - People with disabilities: 10 ✅
  - Low SES: 8 ✅
  - BIPOC: 25 (across all groups) ✅

Accessibility: WCAG 2.1 AA compliant?
  - Color contrast tested ✅
  - Screen reader compatible ✅
  - Keyboard navigation ✅

Pricing: Free/low-cost tier available? ✅

AI Bias: Different outcomes by demographic?
  - Recommendation accuracy tested by group ✅
  - No significant disparities ✅
→ PASS: Equitable

Q: "Could my app discriminate?"
↓
Check: Diverse testing? [Validation-Framework/#level-4] 
  Only college students tested? ❌
  Only English speakers? ❌
→ FIX: Expand testing before launch
```

---

### 5. Respect for People's Rights & Dignity

**Definition:** Respect autonomy, privacy, and cultural context; protect from discrimination

**Key Documents:**
- [APA-Standards/Five-Core-Principles.md#5-respect](APA-Standards/Five-Core-Principles.md) — Respect in psychology
  - Informed consent (genuine, not forced)
  - Privacy protection
  - Respect for autonomy (options, not directives)
  - Cultural sensitivity

- [Legal-Compliance/HIPAA-Requirements.md](Legal-Compliance/HIPAA-Requirements.md) — Legal respect
  - User rights (access, delete, restrict use)
  - Privacy security
  - Informed consent (explicit, plain language)
  - Breach notification
  - No discrimination for declining consent

- [Legal-Compliance/Informed-Consent.md](Legal-Compliance/Informed-Consent.md) (if created) — Consent best practices
  - Plain language
  - Separate consent for: care, research, marketing
  - Right to say no without penalty
  - Easy withdrawal

- [Red-Flags/Manipulative-Patterns.md#category-2](Red-Flags/Manipulative-Patterns.md) — Respect violations
  - Dark patterns (tricking users)
  - Vague consent (users don't understand what they agree to)
  - Data exploitation (selling mental health data)
  - Forcing participation

- [Best-Practices/Therapeutic-Alliance.md#4-autonomy](Best-Practices/Therapeutic-Alliance.md) — Respecting autonomy
  - Offering options (not directives)
  - Respecting user's choices
  - Honoring cultural/spiritual values
  - No shame or judgment

**In Practice:**
```
Q: "Am I respecting user rights?"
↓
Signup consent form:
  Plain language? ✅ (reading level 8th grade)
  Separate sections? ✅ (care vs. research vs. marketing)
  Pre-checked boxes? ❌ (should be unchecked)
  One-click withdrawal? ✅
  No penalty for saying no? ✅

Data deletion: User requests data export
  Response time? <30 days ✅
  Automated or manual? Automated preferred ✅
  All data included? ✅
  Verification of deletion? ✅

Privacy: What data is collected?
  Explicitly disclosed? ✅
  User understands implications? ✅
  Data encrypted? ✅

Autonomy: Features offered
  Exercise recommendations: Option ("What appeals to you?") ✅
  Or Directive ("You should exercise") ❌
→ PASS: Respectful

Q: "Could I be violating dignity?"
↓
Check: Dark patterns? [Red-Flags/Manipulative-Patterns#dark-patterns]
  Hidden unsubscribe ❌
  Shaming language ❌
  Exploiting vulnerabilities ❌
→ FIX: Redesign before launch
```

---

## Feature-by-Feature Ethics Mapping

### Example: "Mood Tracking Journaling Feature"

| Ethical Principle | Question | Check | Status |
|-------------------|----------|-------|--------|
| **Beneficence** | Does journaling genuinely help this user's goal? | Is evidence-based? Feature tested? | [Red-Flags/] [Best-Practices/] |
| **Fidelity** | Are we honest about what this feature does? | Disclaimer: "Journaling helps some people; not therapy" | [APA-Standards/] |
| **Integrity** | Is the AI analysis of mood data transparent? | User can see why app made recommendation | [APA-Standards/] |
| **Justice** | Does journaling work for diverse populations? | Tested with different ages/cultures/abilities | [Validation-Framework/] |
| **Respect** | Can user delete their journals? | One-click deletion; encryption; no dark patterns | [Legal-Compliance/] |
| **Red Flags** | Could this create addiction? | No streak punishment; no shame for missing days | [Red-Flags/] |
| **Best Practice** | Does this support therapeutic alliance? | App reflects back user's concerns; user-driven goal | [Best-Practices/] |

---

## Integration Example: User Requests Data Deletion

**Scenario:** User wants all their mental health data deleted.

**What should happen:**

```
1. REQUEST RECEIVED [Day 1]
   ↓
2. VERIFY IDENTITY [Immediate]
   Principle: Respect (ensure requesting user actually owns account)
   Check: [Legal-Compliance/HIPAA-Requirements.md#user-rights]
   ↓
3. CONFIRM REQUEST [Within 24h]
   User gets email: "Confirm you want to delete all data"
   Principle: Respect for autonomy (not automatic; user confirms)
   Check: [Best-Practices/Therapeutic-Alliance.md#authentic-presence]
   ↓
4. EXECUTE DELETION [Within 30 days]
   - Delete from all databases [Principle: Respect for privacy]
   - Delete from backups (or ensure encrypted beyond use)
   - Delete from third-party vendors [Principle: Fidelity]
   Check: [Legal-Compliance/HIPAA-Requirements.md#security-rule]
   ↓
5. VERIFY & CONFIRM [Day 30]
   User receives: "Your account and all data deleted as of [date]"
   Include: What data was deleted, verification of deletion
   Principle: Transparency, respect
   Check: [Legal-Compliance/HIPAA-Requirements.md#privacy-rule]
   ↓
6. RETAIN ONLY [Legal holds]
   - If court subpoena: Keep for legal requirement [Principle: Fidelity]
   - Notify user if legally required [Principle: Respect]
   Check: [Legal-Compliance/] + legal counsel
```

**Ethical principles enforced throughout:**
- ✅ Respect: User controls own data
- ✅ Beneficence: User's autonomy over their health data
- ✅ Fidelity: Being honest and following through
- ✅ Integrity: Transparent about deletion
- ✅ No red flags: No dark patterns; easy process

---

## Common Integration Failures

### Failure 1: Beneficence vs. Fidelity Conflict

**Scenario:** App detects user in crisis. Should it hospitalize them?

```
❌ WRONG CHOICE:
Beneficence only: Force hospitalization referral
  → Violates Respect (autonomy)
  → Violates Fidelity (exceeding competence)

✅ RIGHT CHOICE:
Beneficence + Fidelity + Respect:
  1. App shows crisis resources clearly
  2. Explains risk and next steps
  3. Offers 988 Lifeline (trained crisis counselors)
  4. Offers user options (call, text, chat)
  5. Respects user's decision (they can decline)
  6. Documents effort (if harm occurs, shows good faith)

Check: [APA-Standards/Five-Core-Principles.md#integration]
       [Red-Flags/Manipulative-Patterns.md#category-3-competence]
       [Best-Practices/Therapeutic-Alliance.md]
```

### Failure 2: Justice vs. Timeline Conflict

**Scenario:** App ready to launch, but haven't tested with diverse populations yet.

```
❌ WRONG CHOICE:
Speed over justice: Launch with majority demographic only
  → Violates Justice (inequitable)
  → Risk of bias harming minorities

✅ RIGHT CHOICE:
Justice-first: Delay launch 4 weeks for diverse testing
  1. Recruit 50+ users across demographics
  2. Audit AI for bias
  3. Test accessibility
  4. Then launch
  5. Monitor for disparities post-launch

Cost: $10-15K, 4 weeks
Benefit: App works equitably for all users; reduces legal risk

Check: [Validation-Framework.md#level-4]
       [APA-Standards/Five-Core-Principles.md#4-justice]
       [Red-Flags/Manipulative-Patterns.md#category-4]
```

---

## Navigation Quick Links

**I want to...**

- ✅ **Build an ethical psychology app**
  → Start with [APA-Standards/Five-Core-Principles.md](APA-Standards/Five-Core-Principles.md)
  → Then [Red-Flags/Manipulative-Patterns.md](Red-Flags/Manipulative-Patterns.md)
  → Then [Validation-Framework.md](Validation-Framework.md)

- ✅ **Know what NOT to do**
  → Go to [Red-Flags/](Red-Flags/) folder

- ✅ **Protect user privacy**
  → Start with [Legal-Compliance/HIPAA-Requirements.md](Legal-Compliance/HIPAA-Requirements.md)

- ✅ **Build a trustworthy relationship with users**
  → Start with [Best-Practices/Therapeutic-Alliance.md](Best-Practices/Therapeutic-Alliance.md)

- ✅ **Audit my existing app**
  → Use [Validation-Framework.md](Validation-Framework.md) Level 1 checklist

- ✅ **Understand how everything connects**
  → You're reading it now! (This file)

---

## The Ethical Hierarchy: When Principles Conflict

When two principles conflict, use this hierarchy to decide:

```
Level 1: SAFETY (Non-maleficence)
  Does this choice prevent serious harm?
  If yes, it overrides other principles
  
  Example: Violate Respect (autonomy) to prevent suicide
           = Call crisis line even if user says no

Level 2: BENEFICENCE (Do good)
  Does this choice help the user?
  Generally aligns with other principles
  
  Example: Offer therapy support (helps user, builds trust)

Level 3: JUSTICE (Equity)
  Does this choice treat users fairly?
  Ensures no one is harmed by design
  
  Example: Test with diverse populations before launch

Level 4: RESPECT (Autonomy, Privacy)
  Does this choice honor user choice?
  Does this choice protect user data?
  
  Example: Let user decline research participation

Level 5: FIDELITY (Honesty, Trust)
  Does this choice maintain professional integrity?
  Does this choice build long-term trust?
  
  Example: Be transparent about limitations
```

**In practice:**

```
Conflict: User wants to stop medication; you think it's harmful

Level 1 (Safety): Is user in immediate danger? [Assess]
  If YES → Escalate (overrides autonomy)
  If NO → Proceed

Level 2 (Beneficence): Can you help them decide wisely?
  Provide: Information, resources, encouragement to consult doctor
  Not: Directive "You should/shouldn't stop meds"

Level 3-5: Respect their autonomy, maintain honesty, build trust
  Outcome: User makes informed choice (app supports, not commands)
```

---

## Continuous Improvement Cycle

```
Build App
  ↓
Level 1: Self-Audit [Red-Flags/ + APA-Standards/]
  ↓
PASS? → Level 2: Expert Review [Validation-Framework/]
  ↓
PASS? → Level 3: External Audit [if needed]
  ↓
PASS? → Level 4: User Testing [Validation-Framework/]
  ↓
PASS? → LAUNCH with Level 5: Monitoring [Validation-Framework/]
  ↓
Monthly: Support tickets [Check for harm]
  ↓
Quarterly: User survey [Satisfaction, safety]
  ↓
Annually: Full re-audit [All principles]
  ↓
Update for new APA guidelines [2025 Draft → adopt new principles]
  ↓
Continuous improvement
```

---

## Related Knowledge Bases

This KB cross-references with (once created):
- [Psychology-Database/Applied-Psychology/Communication-Patterns/](../Communication-Patterns/) — How to communicate therapeutically
- [Psychology-Database/Research-Methods/](../) — Conducting ethical psychology research
- [Psychology-Database/Therapeutic-Modalities/](../) — Specific therapy approaches and their ethics
- [Psychology-Database/Clinical-Assessment/](../) — Ethical assessment practices

---

**Last reviewed:** 2026-03-20  
**Status:** Foundational cross-reference document  
**Validation needed:** Cross-check with other agents' content when available

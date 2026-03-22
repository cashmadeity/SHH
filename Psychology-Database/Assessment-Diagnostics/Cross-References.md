# Cross-References: Assessment KB ↔ Ethics-Guardrails KB

**Purpose:** Show how Assessment-Diagnostics KB builds on Ethics-Guardrails KB  
**Use case:** Understand which KB covers what, avoid duplication, find integrated guidance

---

## When to Use Which KB

### Ethics-Guardrails KB Best For:

- General psychology app ethics (therapy apps, wellness, coaching)
- Manipulative pattern detection (dark patterns, addiction mechanics)
- Therapeutic alliance & trust building
- Privacy/HIPAA foundations
- Red flags in psychology apps generally
- 5 core APA principles (Beneficence, Fidelity, Integrity, Justice, Respect)

### Assessment-Diagnostics KB Best For:

- Measurement validity & psychometrics
- Assessment-specific ethics (Standard 9)
- Fairness in measurement & algorithms
- Competence in assessment (different from general clinical competence)
- Informed consent for assessment (different from therapy)
- Cross-cultural validity of tests
- Clinical decision support based on assessment

---

## Principle-by-Principle Alignment

### Beneficence & Nonmaleficence

| Layer | Guidance | Where to Find |
|-------|----------|---|
| **General** | Do good; avoid manipulation | Ethics-Guardrails: README + Beneficence section |
| **Assessment-specific** | Use valid tests; don't create false diagnosis | This KB: [01](01-Ethical-Assessment-Principles.md) Standard 9.01 |
| **Fairness** | Assess fairly across demographic groups | This KB: [02](02-Bias-in-Diagnostics-and-AI.md) Bias types |
| **Crisis** | Catch high-risk people; don't miss suicide | This KB: [07](07-Assessment-Ethics-Audit-Framework.md) Crisis protocol |

**Action:** Use Ethics-Guardrails for app-level safety; use this KB for assessment-level validity.

### Fidelity & Responsibility

| Layer | Guidance | Where to Find |
|-------|----------|---|
| **General** | Be honest about what your app is | Ethics-Guardrails: Fidelity section |
| **Assessment-specific** | Be honest about test limitations | This KB: [01](01-Ethical-Assessment-Principles.md) Standard 9.10 |
| **Scope** | Stay in competence; refer when needed | This KB: [03](03-Competence-Boundaries-and-Referral.md) |
| **Supervision** | Have oversight; don't claim independence if trained | This KB: [03](03-Competence-Boundaries-and-Referral.md) Training section |

**Action:** Use Ethics-Guardrails for app transparency; use this KB for assessment competence/scope.

### Integrity

| Layer | Guidance | Where to Find |
|-------|----------|---|
| **General** | Don't make false claims | Ethics-Guardrails: Integrity section |
| **Assessment** | Don't claim validity without evidence | This KB: [01](01-Ethical-Assessment-Principles.md) Standard 9.01 |
| **Algorithm** | Don't hide how AI makes decisions | This KB: [02](02-Bias-in-Diagnostics-and-AI.md) Transparency |
| **Results** | Don't over-interpret; state limits | This KB: [01](01-Ethical-Assessment-Principles.md) Standard 9.10 |

**Action:** Use Ethics-Guardrails for general honesty; use this KB for assessment evidence/transparency.

### Justice

| Layer | Guidance | Where to Find |
|-------|----------|---|
| **General** | Ensure equitable access | Ethics-Guardrails: Justice section |
| **Assessment fairness** | Validate across demographic groups | This KB: [02](02-Bias-in-Diagnostics-and-AI.md) Fairness frameworks |
| **Cultural** | Adapt for cultural validity | This KB: [05](05-Cultural-Adaptation-of-Assessments.md) |
| **Accessibility** | Ensure assessment accessible to diverse users | This KB: [04](04-Informed-Consent-in-Assessment.md) Plain language |

**Action:** Use Ethics-Guardrails for app-level equity; use this KB for assessment-level fairness validation.

### Respect for Rights & Dignity

| Layer | Guidance | Where to Find |
|-------|----------|---|
| **General** | Respect privacy, autonomy, culture | Ethics-Guardrails: Respect section |
| **Assessment consent** | Get REAL informed consent (not just checkbox) | This KB: [04](04-Informed-Consent-in-Assessment.md) |
| **Data security** | Protect assessment data (highly sensitive) | This KB: [06](06-Data-Security-and-Confidentiality.md) |
| **Interpretation** | Respect cultural meaning of symptoms | This KB: [05](05-Cultural-Adaptation-of-Assessments.md) CFI approach |

**Action:** Use Ethics-Guardrails for consent basics; use this KB for assessment-specific consent design.

---

## Feature Integration Matrix

### Building a Depression Screening App

| Component | Ethics-Guardrails | Assessment KB | Action |
|-----------|---|---|---|
| **What not to do** | Dark patterns, manipulation | Over-certainty, false diagnosis | Review both: [EG](../Applied-Psychology/Ethics-Guardrails/Red-Flags/Manipulative-Patterns.md) + [01](01-Ethical-Assessment-Principles.md) |
| **Pick the tool** | Privacy-respecting | Validated for your population | Review [01](01-Ethical-Assessment-Principles.md) Standard 9.01 |
| **Design consent** | Transparent disclosures | Plain language, comprehension check | Review both: [EG](../Applied-Psychology/Ethics-Guardrails/Legal-Compliance/Informed-Consent.md) + [04](04-Informed-Consent-in-Assessment.md) |
| **Avoid bias** | Fairness in design | Fairness in measurement | Review both: [EG README](../Applied-Psychology/Ethics-Guardrails/README.md) Justice section + [02](02-Bias-in-Diagnostics-and-AI.md) |
| **Explain results** | Honest about app limits | Honest about test limits | Review both: [01](01-Ethical-Assessment-Principles.md) Standard 9.10 + [EG](../Applied-Psychology/Ethics-Guardrails/Best-Practices/Therapeutic-Alliance.md) |
| **Protect data** | Privacy basics | HIPAA/encryption details | Review both: [EG](../Applied-Psychology/Ethics-Guardrails/Legal-Compliance/HIPAA-Requirements.md) + [06](06-Data-Security-and-Confidentiality.md) |
| **Handle crisis** | Escalation to human | Suicidal ideation protocol | Review [07](07-Assessment-Ethics-Audit-Framework.md) Crisis protocol |
| **Pre-launch** | Self-audit by team | Level 1-2 audit ([07](07-Assessment-Ethics-Audit-Framework.md)) | Run both assessments |

---

## Conflict Resolution: When Principles Clash

### Scenario: Assessment shows potential depression; user says "I don't want this label"

**Guidance from Ethics-Guardrails:**
- Respect (user's autonomy)
- Beneficence (is diagnosis helpful?)
- Fidelity (honest about what assessment means)

**Guidance from Assessment KB:**
- [01](01-Ethical-Assessment-Principles.md) Standard 9.10 (explain results; user can disagree)
- [03](03-Competence-Boundaries-and-Referral.md) (can't force diagnosis; offer referral)

**Resolution:**
1. Show results clearly (beneficence)
2. Acknowledge user disagreement (respect)
3. Explain this is screening, not diagnosis (fidelity)
4. Offer professional consultation (referral protocol)
5. Don't insist on diagnosis (respect autonomy)

---

## Competence Boundaries: Assessment vs. Therapy

### When You Need Assessment Competence (This KB)

- Using psychometric tests (PHQ-9, WAIS, personality assessments)
- Making diagnostic recommendations
- Interpreting assessment results
- Scoring structured instruments
- Adapting tests cross-culturally
- Auditing assessment for fairness

**Minimum training:** Assessment-specific course + supervision

### When General Clinical Competence Suffices (Ethics-Guardrails)

- Providing therapeutic support
- Listening empathetically
- Discussing coping strategies
- Offering psychoeducation
- Crisis support/connection to help

**Minimum training:** Master's level mental health training

### When You Need BOTH

- Therapy apps with pre-screening
- Clinical decision support for therapists
- Assessment + treatment monitoring
- Diagnostic clarification in therapy

**Training:** Both assessment + therapeutic competence required

---

## Risk Hierarchy: When Assessment Goes Wrong

```
HIGHEST RISK (Life safety):
1. Missed suicide risk assessment → User harm → USE [07](07-Assessment-Ethics-Audit-Framework.md) Crisis protocol
2. False diagnosis of severe condition → Wrong treatment path → USE [02](02-Bias-in-Diagnostics-and-AI.md) Bias audit

MEDIUM RISK (Professional):
3. Assessment used outside competence → License revocation → USE [03](03-Competence-Boundaries-and-Referral.md)
4. Consent violations → Legal liability → USE [04](04-Informed-Consent-in-Assessment.md)
5. Data breach of assessment results → HIPAA fine → USE [06](06-Data-Security-and-Confidentiality.md)

LOWER RISK (Ethical):
6. Unfair assessment for minority group → Disparate impact → USE [02](02-Bias-in-Diagnostics-and-AI.md) Fairness audit
7. Cultural misfit (test for U.S., using in Kenya) → Invalid results → USE [05](05-Cultural-Adaptation-of-Assessments.md)
```

---

## Audit Integration: Combined Checklist

### Pre-Launch Audit (Use Both KBs)

```
ETHICS-GUARDRAILS AUDIT:
[ ] No dark patterns (addiction mechanics, hidden friction)
[ ] Manipulation-free design
[ ] Clear app boundaries ("Not a substitute for therapy")
[ ] Privacy disclosures complete
[ ] Crisis escalation path present

ASSESSMENT-DIAGNOSTICS AUDIT (ADD TO ABOVE):
[ ] Assessment validity confirmed (9.01)
[ ] Competence verified (team trained, supervised)
[ ] Bias screened (fairness audit)
[ ] Consent designed (comprehension-tested)
[ ] Data secured (encryption, access control)
[ ] Crisis protocol tested (suicidal ideation handled)
[ ] Pre-launch audit passed (Level 1-2)

INTEGRATION:
- Results shown honestly (both KBs)
- User can't be manipulated by assessment (both KBs)
- Data secured highly (this KB, stronger)
- Consent addresses both app + assessment (both KBs)
```

---

## Resource Mapping

### If You Have Access to Ethics-Guardrails KB

```
You need Assessment ethics? → START WITH:
1. This KB README ([README.md](README.md))
2. Cross-reference to Ethics-Guardrails (this document)
3. Read relevant Assessment-Diagnostics docs (01-07)
4. Reference back to Ethics-Guardrails as needed

This ensures:
- No duplicating ethics knowledge
- Building on solid foundation (E-G principles)
- Going deeper on assessment-specific issues
```

### If Building a Psychology App

```
DECISION TREE:

Does your app assess/diagnose?
├─ YES → You need BOTH KBs
│        Read order: Ethics-Guardrails first, then this KB
│        Use both in pre-launch audit
│
└─ NO (e.g., wellness, support)
         → Primarily Ethics-Guardrails
         → Consider this KB for assessment sections
```

---

## Cross-Reference Quick Links

### From Ethics-Guardrails to Assessment-Diagnostics

If you're reading Ethics-Guardrails and encounter assessment topics:

| Topic | In Ethics-Guardrails | Jump To |
|-------|---|---|
| **Assessment tool selection** | Mentioned in integrity | [01](01-Ethical-Assessment-Principles.md) Standard 9.01 |
| **Test fairness** | Justice section | [02](02-Bias-in-Diagnostics-and-AI.md) |
| **Competence in assessment** | Standards 2.04 | [03](03-Competence-Boundaries-and-Referral.md) |
| **Assessment consent** | Standards 9.03 | [04](04-Informed-Consent-in-Assessment.md) |
| **Cultural assessment** | Justice + diversity section | [05](05-Cultural-Adaptation-of-Assessments.md) |
| **Assessment data privacy** | HIPAA section | [06](06-Data-Security-and-Confidentiality.md) |
| **Pre-launch audit** | Validation framework | [07](07-Assessment-Ethics-Audit-Framework.md) |

---

## Summary: Using Both KBs Together

```
COMPLETE PSYCHOLOGY APP ETHICS FRAMEWORK:

ETHICS-GUARDRAILS KB (Foundation)
├─ 5 core APA principles
├─ General psychology app ethics
├─ Privacy/consent/confidentiality basics
└─ Red flags across all apps

    ↓ If your app includes ASSESSMENT:

ASSESSMENT-DIAGNOSTICS KB (Specialized)
├─ APA Standard 9 (Assessment-specific)
├─ Measurement validity & fairness
├─ Assessment competence
├─ Cross-cultural test validity
├─ Deep-dive on assessment consent/security
└─ Pre-launch audit framework

RESULT: Fully ethical assessment app ✓
```

---

**Last reviewed:** 2026-03-21  
**Related:** [INDEX.md](INDEX.md) (Navigation guide)  
**Main KB:** Psychology-Database/Applied-Psychology/Ethics-Guardrails/README.md

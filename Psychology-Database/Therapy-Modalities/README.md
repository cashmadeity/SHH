# Therapy Modalities & Specific Ethics Knowledge Base

**Purpose:** Modality-specific ethical guidance for digital therapeutics, apps, and AI-assisted counseling tools.

**Status:** Comprehensive; covers 6 major therapeutic approaches  
**Last Updated:** 2026-03-21  
**Foundation:** Ethics-Guardrails KB (APA standards, HIPAA compliance, best practices)  
**Audience:** Therapists, clinical advisors, developers building modality-specific apps

---

## Overview

This knowledge base extends the **Ethics-Guardrails KB** with **modality-specific ethical frameworks**, red flags, and implementation guidance for:

1. **Cognitive Behavioral Therapy (CBT)** — Structured thought/behavior work
2. **Dialectical Behavior Therapy (DBT)** — Skills, validation, crisis support
3. **Acceptance & Commitment Therapy (ACT)** — Values, mindfulness, psychological flexibility
4. **Psychodynamic Therapy** — Transference, defense mechanisms, relationship depth
5. **Humanistic/Person-Centered Therapy** — Congruence, authenticity, growth
6. **Integrative Approaches** — Multi-model flexibility, synthesis, and ethical complexity

Each modality has **unique ethical challenges** when digitized. This KB helps you navigate them.

---

## Quick Start

### I'm building a CBT app
→ [01-CBT-Ethics-Safety-Planning.md](01-CBT-Ethics-Safety-Planning.md)

### I'm building a DBT app  
→ [02-DBT-Safety-Crisis-Protocols.md](02-DBT-Safety-Crisis-Protocols.md)

### I'm building an ACT app
→ [03-ACT-Acceptance-Mindfulness-Ethics.md](03-ACT-Acceptance-Mindfulness-Ethics.md)

### I'm building a psychodynamic app
→ [04-Psychodynamic-Transference-Boundaries.md](04-Psychodynamic-Transference-Boundaries.md)

### I'm building a humanistic/person-centered app
→ [05-Humanistic-Congruence-Authenticity.md](05-Humanistic-Congruence-Authenticity.md)

### I'm combining modalities
→ [06-Integrative-Ethics-Model-Conflicts.md](06-Integrative-Ethics-Model-Conflicts.md)

### I want to know what can go wrong in ANY modality
→ [07-Modality-Specific-Red-Flags.md](07-Modality-Specific-Red-Flags.md)

### I want to understand how modalities connect to core ethics
→ [08-Cross-Reference-to-Core-Ethics.md](08-Cross-Reference-to-Core-Ethics.md)

---

## Directory Structure

```
Therapy-Modalities/
├── README.md (this file)
├── INDEX.md (detailed navigation & document map)
│
├── 01-CBT-Ethics-Safety-Planning.md
│   ├── CBT principles & ethical foundations
│   ├── Automation in CBT (thought records, behavioral activation)
│   ├── Safety planning in digital context
│   ├── Homework compliance & client autonomy
│   ├── Red flags specific to CBT
│   └── Implementation checklist
│
├── 02-DBT-Safety-Crisis-Protocols.md
│   ├── DBT principles & ethical foundations
│   ├── Crisis response in digital DBT
│   ├── Skills coaching vs. crisis care
│   ├── Phone coaching ethics (text/chat simulation)
│   ├── Chains analysis & vulnerability
│   ├── Red flags specific to DBT
│   └── Implementation checklist
│
├── 03-ACT-Acceptance-Mindfulness-Ethics.md
│   ├── ACT principles & ethical foundations
│   ├── Values work in digital context
│   ├── Mindfulness: guidance, commercialization, "McMinfulness"
│   ├── Experiential avoidance vs. healthy coping
│   ├── Ethical use of metaphors & defusion techniques
│   ├── Red flags specific to ACT
│   └── Implementation checklist
│
├── 04-Psychodynamic-Transference-Boundaries.md
│   ├── Psychodynamic principles & ethical foundations
│   ├── Transference in digital context (can it happen in apps?)
│   ├── Relationship depth & attachment safety
│   ├── Defense mechanism recognition
│   ├── Boundaries with automated interventions
│   ├── Red flags specific to psychodynamic work
│   └── Implementation checklist
│
├── 05-Humanistic-Congruence-Authenticity.md
│   ├── Humanistic principles & ethical foundations
│   ├── AI authenticity: can an AI be congruent?
│   ├── Unconditional positive regard in automation
│   ├── Presence & the therapeutic relationship
│   ├── Growth-oriented design vs. symptom suppression
│   ├── Red flags specific to humanistic approaches
│   └── Implementation checklist
│
├── 06-Integrative-Ethics-Model-Conflicts.md
│   ├── Integration as an ethical approach
│   ├── When modalities conflict (CBT directiveness vs. humanistic acceptance)
│   ├── Matching modalities to user needs
│   ├── Flexibility without eclecticism
│   ├── Avoiding "therapeutic kitchen sink" fallacy
│   ├── Integration in digital context
│   └── Implementation checklist
│
├── 07-Modality-Specific-Red-Flags.md
│   ├── Cross-modality harm patterns
│   ├── Premature termination signals
│   ├── Misdiagnosis & inappropriate modality matching
│   ├── Over-automation in relationship-dependent modalities
│   ├── Competence & scope violations
│   ├── Crisis readiness checklist (all modalities)
│   └── Audit framework
│
└── 08-Cross-Reference-to-Core-Ethics.md
    ├── How each modality applies APA 5 principles
    ├── Beneficence/Nonmaleficence by modality
    ├── Fidelity/Responsibility by modality
    ├── Integrity by modality
    ├── Justice by modality
    ├── Respect for Rights & Dignity by modality
    ├── Quick-access principle mapping
    └── Conflict resolution framework (when principles clash by modality)
```

---

## Key Differences Across Modalities

| Aspect | CBT | DBT | ACT | Psychodynamic | Humanistic |
|--------|-----|-----|-----|---------------|-----------|
| **Goal** | Symptom reduction | Distress tolerance + behavior change | Values alignment | Insight, self-awareness | Growth, authenticity |
| **Process** | Structured, directive | Skills + validation | Acceptance + action | Exploratory, unstructured | Collaborative, explorative |
| **Relationship role** | Collaborative, teacher | Validating coach | Mindful companion | Depth of attachment | Non-directive partner |
| **Safety focus** | Behavioral (suicide contracts) | Chains, crisis planning | Values-based living | Insight into vulnerability | Empathic connection |
| **Danger in digital** | Over-automation of thought work | Missing crisis escalation | Spiritual bypassing of real problems | Loss of relational depth | Hollow "authenticity" |
| **Ethics strength** | Clear, measurable outcomes | Strong crisis protocols | Values-centered autonomy | Self-awareness, non-judgment | Respect for dignity |

---

## Critical Questions Before Building

1. **What is my modality?** (Pure CBT? DBT? Integrative?)
   - Different ethics apply to each
   
2. **What cannot be automated in this modality?**
   - The therapeutic relationship itself is often the medicine
   - Identify human-only elements before digitizing

3. **What is my crisis protocol?**
   - Every app must escalate to human care within X minutes
   - Modality affects HOW you escalate (e.g., DBT crisis line, CBT therapist)

4. **How do I match users to this modality?**
   - Not everyone benefits from CBT structure
   - Some people need humanistic validation first, then CBT
   - ACT may trigger trauma in some populations

5. **How do I preserve the relationship without a human?**
   - AI can't truly do psychodynamic work (no real transference)
   - AI can facilitate DBT skills (which are tools, not relationship)
   - Humanistic approach needs real human for its core value

---

## Ethical Hierarchy: When Modalities Conflict

**Safety > Efficacy > Preference**

1. **Safety first:** If user is unsafe, escalate to human crisis care (regardless of modality)
2. **Then efficacy:** Which modality has strongest evidence for this person?
3. **Then preference:** Let user choose among safe, effective options

Example: User with trauma + suicidal ideation
- **Safety:** Activate crisis protocol (not CBT thought work, not ACT values work)
- **Efficacy:** DBT + trauma-informed care > CBT alone
- **Preference:** Once safe, let user choose trauma modality (EMDR, CPT, etc.)

---

## Before You Launch: Modality-Specific Checklist

- [ ] **Modality identified:** I can name my primary approach
- [ ] **Scope defined:** What I do + don't do in this modality
- [ ] **Relationship depth:** Is this modality relational? How preserved digitally?
- [ ] **Automation limits:** What cannot be automated? Is my tech respecting that?
- [ ] **Crisis protocol:** Escalation path tested & documented
- [ ] **Outcome measurement:** How will I know if this helps? (Modality-specific metrics)
- [ ] **Harm monitoring:** What could go wrong specific to this modality? Am I watching for it?
- [ ] **Expert review:** Clinical advisor for this modality has reviewed the app
- [ ] **User testing:** Tested with at least 20 users who practice/benefit from this modality
- [ ] **Cross-reference:** Confirmed alignment with APA 5 core principles (see [08-Cross-Reference-to-Core-Ethics.md](08-Cross-Reference-to-Core-Ethics.md))

---

## Integration with Ethics-Guardrails KB

**Relationship to parent KB:**

- Ethics-Guardrails provides **universal principles** (APA standards, HIPAA, therapeutic alliance, cultural competence)
- Therapy-Modalities provides **modality-specific applications** of those principles
- Start with Ethics-Guardrails for foundation
- Use Therapy-Modalities to deep-dive your specific approach

**Cross-references throughout:** Each document links back to Ethics-Guardrails on related topics

**Example flow:**
1. Read [Ethics-Guardrails/APA-Standards/Five-Core-Principles.md](../Applied-Psychology/Ethics-Guardrails/APA-Standards/Five-Core-Principles.md) for foundation
2. Read [08-Cross-Reference-to-Core-Ethics.md](08-Cross-Reference-to-Core-Ethics.md) to see your modality's specific take
3. Read your modality-specific document ([01-CBT...](01-CBT-Ethics-Safety-Planning.md), [02-DBT...](02-DBT-Safety-Crisis-Protocols.md), etc.)
4. Use [07-Modality-Specific-Red-Flags.md](07-Modality-Specific-Red-Flags.md) for continuous monitoring

---

## Document Statistics

| Document | Focus | Length | Key Takeaway |
|----------|-------|--------|--------------|
| CBT | Thought/behavior, safety planning | ~9 KB | Structure & measurement; automation risks |
| DBT | Skills, crisis, validation | ~10 KB | Dialectic balance; crisis isn't optional |
| ACT | Values, acceptance, mindfulness | ~9 KB | Avoid spiritual bypassing; honor autonomy |
| Psychodynamic | Transference, insight, depth | ~8 KB | Relationship is medicine; hard to digitize |
| Humanistic | Congruence, authenticity, growth | ~8 KB | "I-Thou" relationship; AI limitations |
| Integrative | Multi-model, flexibility, conflicts | ~8 KB | Integration ≠ everything at once |
| Red Flags | Cross-modality harm patterns | ~8 KB | What to watch for; audit framework |
| Cross-Reference | Principle mapping, conflicts | ~8 KB | How modalities meet APA 5 principles |
| **TOTAL** | **All modalities, comprehensive** | **~68 KB** | Modality-specific ethical practice guide |

---

## How to Use This Knowledge Base

### Clinical Advisors & Therapists
1. Read your modality-specific doc (skip to "Red Flags" section)
2. Review [07-Modality-Specific-Red-Flags.md](07-Modality-Specific-Red-Flags.md)
3. Audit the app using checklists provided
4. Flag ethical violations before launch

### Developers & Product Managers
1. Start with [README.md](README.md) (this file)
2. Read your modality-specific doc (all sections)
3. Use implementation checklists to build features
4. Cross-check with [08-Cross-Reference-to-Core-Ethics.md](08-Cross-Reference-to-Core-Ethics.md)

### Ethics Officers
1. Read all 8 documents (3-4 hours)
2. Use [07-Modality-Specific-Red-Flags.md](07-Modality-Specific-Red-Flags.md) for audit
3. Ensure all modality-specific checklists are met
4. Cross-validate with Ethics-Guardrails KB

---

## Next Steps

1. **Identify your modality** — Which docs apply to you?
2. **Read your modality's doc** — Full dive into ethics, automation, and red flags
3. **Review red flags** — Know what can go wrong specific to your approach
4. **Run the checklist** — Verify your implementation matches ethical standards
5. **Get expert review** — Have a clinical advisor in your modality validate
6. **Monitor outcomes** — Post-launch, ensure no unexpected harms emerge

---

## When in Doubt

- **General ethics question?** → Ethics-Guardrails KB
- **My modality specific?** → Corresponding doc (01-08)
- **Is this harm happening?** → [07-Modality-Specific-Red-Flags.md](07-Modality-Specific-Red-Flags.md)
- **How does my modality apply APA principles?** → [08-Cross-Reference-to-Core-Ethics.md](08-Cross-Reference-to-Core-Ethics.md)
- **Unsure about my approach?** → Consult a licensed therapist in that modality

---

**Built by:** Therapy Modalities Agent  
**For:** Ethically sound, modality-specific digital therapeutics  
**Foundation:** APA Ethics Code (2017), draft 2025 updates, empirical psychotherapy research  
**Status:** Complete & ready for clinical validation

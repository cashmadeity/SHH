# Implementation Guide: Using This Knowledge Base

**For:** Product managers, developers, founders, clinical advisors building mental health apps

**Time to read:** 10 minutes  
**Time to implement:** 3 hours to 3 months (depending on app maturity)

---

## Quick Start (15 Minutes)

### If you're just starting out:

1. **Read [README.md](README.md)** — Understand the scope (5 min)
2. **Skim [Red-Flags/Manipulative-Patterns.md](Red-Flags/Manipulative-Patterns.md)** — Know what NOT to do (5 min)
3. **Bookmark [Validation-Framework.md](Validation-Framework.md)** — You'll need this before launch (2 min)

**Action:** Create a Slack channel or doc called "Ethics Audit" and drop links there.

---

### If you're building actively:

1. **Read [APA-Standards/Five-Core-Principles.md](APA-Standards/Five-Core-Principles.md)** (20 min)
2. **Do [Validation-Framework.md](Validation-Framework.md) Level 1 self-audit** (2 hours)
3. **Assign someone to flag blockers** (1 hour)

**Action:** Schedule ethics review meeting for next week. Share findings.

---

### If you're launching soon:

1. **Complete [Validation-Framework.md](Validation-Framework.md) Level 2 expert review** (1-2 weeks)
2. **Fix critical issues** (1-4 weeks)
3. **Do user testing** with diverse populations (4 weeks)

**Do not launch until pass Level 2.**

---

## Implementation by Role

### Product Manager

**Your job:** Ensure ethics is integrated into roadmap.

**Month 1:**
- [ ] Read: [README.md](README.md), [Five-Core-Principles.md](APA-Standards/Five-Core-Principles.md)
- [ ] Create ethics checklist for features (use [Red-Flags/](Red-Flags/) as template)
- [ ] Set up ethics review as part of feature approval process
- [ ] Assign ethics owner (developer or designer)

**Ongoing:**
- [ ] Every feature: Ask "Does this violate any red flags?"
- [ ] Monthly: Ethics checklist review
- [ ] Quarterly: User safety check-in

**Tools:**
- Use [Validation-Framework.md](Validation-Framework.md) checklist in PRs
- Reference [Red-Flags/](Red-Flags/) when designing features
- Measure: "% of features reviewed for ethics" (goal: 100%)

---

### Developer / Engineer

**Your job:** Implement ethical principles in code.

**Month 1:**
- [ ] Read: [Legal-Compliance/HIPAA-Requirements.md](Legal-Compliance/HIPAA-Requirements.md)
- [ ] Audit current code:
  - [ ] Is data encrypted at rest? ✅ / ❌
  - [ ] Is data encrypted in transit? ✅ / ❌
  - [ ] Are access logs kept? ✅ / ❌
  - [ ] Can users delete data? ✅ / ❌
- [ ] Fix critical gaps

**Month 2-3:**
- [ ] Implement audit logging
- [ ] Add data deletion feature
- [ ] Review vendor agreements (BAAs)
- [ ] Incident response plan

**Ongoing:**
- [ ] Security testing (quarterly pen tests minimum)
- [ ] Access log monitoring
- [ ] Breach detection system
- [ ] Keep dependencies updated

**Tools:**
- Use HIPAA checklist to audit infrastructure
- Implement encryption everywhere (AES-256 at rest, TLS 1.2+ in transit)
- Automate security testing (SAST/DAST)

---

### Designer / Product

**Your job:** Prevent manipulative design patterns.

**Month 1:**
- [ ] Read: [Red-Flags/Manipulative-Patterns.md](Red-Flags/Manipulative-Patterns.md)
- [ ] Audit current design:
  - [ ] No addiction mechanics ✅ / ❌
  - [ ] No dark patterns ✅ / ❌
  - [ ] One-click exit ✅ / ❌
  - [ ] Clear crisis resources ✅ / ❌
- [ ] Fix dark patterns immediately

**Month 2:**
- [ ] Implement accessibility (WCAG 2.1 AA)
  - [ ] Color contrast tested
  - [ ] Screen reader compatible
  - [ ] Keyboard navigation
- [ ] Plain-language consent screens

**Ongoing:**
- [ ] User research with diverse populations
- [ ] Quarterly: Accessibility audit
- [ ] A/B test to measure true benefit (not just engagement)

**Tools:**
- WAVE accessibility auditor
- Color contrast checker (Webaim)
- Dark pattern checklist ([Red-Flags/](Red-Flags/))

---

### Clinical Advisor / Therapist

**Your job:** Ensure clinical soundness & therapeutic alliance.

**Month 1:**
- [ ] Read: [Best-Practices/Therapeutic-Alliance.md](Best-Practices/Therapeutic-Alliance.md), [APA-Standards/Five-Core-Principles.md](APA-Standards/Five-Core-Principles.md)
- [ ] Review all content for:
  - [ ] Clinical accuracy ✅ / ❌
  - [ ] Therapeutic tone ✅ / ❌
  - [ ] Cultural sensitivity ✅ / ❌
  - [ ] Crisis escalation ✅ / ❌

**Month 2:**
- [ ] Develop crisis detection criteria
- [ ] Create escalation protocol
- [ ] Train team on therapeutic approach

**Ongoing:**
- [ ] Quarterly: Content audit
- [ ] Monitor user feedback for harm
- [ ] User testing sessions
- [ ] Quarterly: Team training on new research

**Tools:**
- Therapeutic Alliance checklist ([Best-Practices/](Best-Practices/))
- Crisis criteria documentation
- Content review template

---

### Ethics Officer / Compliance

**Your job:** Overall ethics governance and audit.

**Month 1:**
- [ ] Read: Everything (3-4 hours)
- [ ] Set up ethics committee (product, engineering, clinical, legal)
- [ ] Create ethics review process
- [ ] Assign owners to each domain

**Month 2:**
- [ ] Do [Validation-Framework.md](Validation-Framework.md) Level 2 expert review
- [ ] Identify gaps and remediation plan
- [ ] Create incident response process

**Month 3+:**
- [ ] Monthly: Ethics committee meetings
- [ ] Quarterly: User safety surveys
- [ ] Annually: Full re-audit
- [ ] Continuous: Monitor for harm reports

**Tools:**
- [Validation-Framework.md](Validation-Framework.md) (all levels)
- Incident response plan template
- Ethics audit calendar
- Red flag monitoring dashboard

---

## Feature-by-Feature Ethics Review

**Use this for every feature before launch:**

### Step 1: Propose Feature
*PM/Design writes 1-pager:*
- What is it?
- Who is it for?
- What problem does it solve?
- What are potential harms?

### Step 2: Red Flag Check
*Designer + Developer:*
- Go through [Red-Flags/Manipulative-Patterns.md](Red-Flags/Manipulative-Patterns.md)
- Checklist each category
- Flag any issues

**Fail on any critical item?** → Redesign before proceeding

### Step 3: Principle Alignment
*Clinical Advisor:*
- Does it align with all 5 APA principles?
- Any conflicts?
- How to resolve?

**Use [Cross-References.md](Cross-References.md) to map feature to principles**

### Step 4: Legal Check
*Legal/Compliance:*
- Privacy implications? (Read [Legal-Compliance/HIPAA-Requirements.md](Legal-Compliance/HIPAA-Requirements.md))
- Consent needed? (What's the disclosure?)
- Data security required? (How sensitive is the data?)

### Step 5: Approval
*Ethics committee signs off:*
- ✅ Pass: Implement as designed
- ⚠️ Conditional: Implement with modifications
- ❌ Fail: Reject; redesign required

**Document the decision** (you'll need it for audits)

---

## Pre-Launch Checklist (Critical)

**Do NOT launch until all critical items pass:**

### Red Flags (Critical)
- [ ] No addiction mechanics
- [ ] No dark patterns
- [ ] No consent violations
- [ ] No competence overreach
- [ ] Crisis escalation in place
- [ ] No unintended discrimination

### Legal (Critical)
- [ ] Informed consent (plain language)
- [ ] Privacy policy (understandable)
- [ ] Data encryption (at rest & in transit)
- [ ] Breach notification plan
- [ ] Vendors have BAAs (if applicable)

### Clinical (Critical)
- [ ] Clear scope (what app does/doesn't do)
- [ ] No claims beyond evidence
- [ ] Crisis resources current & accessible
- [ ] Therapeutic alliance features present

### Quality (Critical)
- [ ] No major bugs
- [ ] Tested on multiple devices
- [ ] Performance acceptable
- [ ] Accessibility tested (WCAG 2.1 AA minimum)

### Validation (Critical)
- [ ] Level 1 self-audit: PASS
- [ ] Level 2 expert review: PASS (or conditional pass + plan)
- [ ] Level 3 external review: Recommended (if possible)
- [ ] Level 4 user testing: PASS (minimum 20 users, diverse)

**If any critical item fails:** Fix it. Do not launch. Period.

---

## Post-Launch Monitoring

**Month 1:**
- [ ] Daily: Monitoring for crashes/errors
- [ ] Daily: Support ticket review (any harm reports?)
- [ ] Weekly: Access log review (suspicious activity?)

**Month 2-3:**
- [ ] Weekly user feedback review
- [ ] Incident investigation protocol
- [ ] Harm response procedure

**Quarterly (Every 3 months):**
- [ ] User satisfaction survey
- [ ] Harm event review (any reports?)
- [ ] Ethics committee meeting
- [ ] Feature request analysis (any concerning themes?)

**Annually:**
- [ ] Full re-audit against [Validation-Framework.md](Validation-Framework.md)
- [ ] User testing with new diverse sample (20-30 users)
- [ ] Update for new APA guidance
- [ ] Bias testing for AI (if applicable)
- [ ] Legal compliance review (HIPAA/GDPR/CCPA updates)

---

## Common Mistakes & How to Avoid Them

### Mistake 1: Treating Ethics as Checkbox

❌ **BAD:**
- "We did ethics review once. Check!"
- Ethics as separate from product (not integrated)
- Ethics committee meets once/year

✅ **GOOD:**
- Ethics review integrated into every feature
- Ethics as ongoing practice, not event
- Ethics committee meets monthly
- Ethics metrics tracked (% features reviewed, harm reports, etc.)

### Mistake 2: Not Including Clinical Input

❌ **BAD:**
- Developers building therapy features without therapist input
- Clinical review only at the end
- No therapist on team

✅ **GOOD:**
- Therapist involved in feature design (not just review)
- Clinical advisor attends weekly standups
- Co-design with therapists and users

### Mistake 3: Ignoring Diverse Voices

❌ **BAD:**
- Testing only with college-educated, English-speaking users
- Homogeneous team building for diverse population
- No disability accessibility

✅ **GOOD:**
- Diverse beta testers (minimum 20-30 per demographic)
- Diverse team (ideally reflecting user base)
- Accessibility built in from day 1 (not after launch)

### Mistake 4: Pretending Neutrality

❌ **BAD:**
- "Our app is neutral; we don't make value judgments"
- Ignoring systemic issues
- Assuming Western psychology is universal

✅ **GOOD:**
- "Our app reflects evidence AND user values"
- Acknowledging systemic issues (poverty, discrimination, etc.)
- Honoring diverse cultural mental health approaches

### Mistake 5: Prioritizing Growth Over Safety

❌ **BAD:**
- "We'll fix ethics issues later"
- Scaling before safety tested
- Engagement metrics prioritized over user wellbeing

✅ **GOOD:**
- Safety first; scale only after validated
- Measure impact not just engagement
- Revenue model aligns with user welfare

---

## Getting Help

### Need clinical input?
- Contact psychology departments at nearby universities
- NAMI (National Alliance on Mental Illness) can recommend clinicians
- Psychology licensing boards have consultation lists

### Need legal review?
- Healthcare attorneys (search: "healthcare attorney near me")
- Law firms with digital health practice
- Cost: ~$5-10K for initial review

### Need ethics expertise?
- University research ethics boards (IRBs) sometimes consult
- Ethics consultants (search: "research ethics consultant")
- Professional organizations (APA, ACA, etc.)

### Need to understand new APA code?
- Watch for official APA guidance documents (2025-2026)
- Join APA (get monthly updates)
- Subscribe to ethics-focused journals & newsletters

---

## Success Metrics: How to Know You're Doing Ethics Right

### Metric 1: Governance
- [ ] Ethics committee exists, meets monthly
- [ ] Every major feature has ethics review
- [ ] Issues are documented and tracked

**Target:** 100% of features reviewed before launch

### Metric 2: Safety
- [ ] User harm reports < 0.1% of user base
- [ ] Crisis escalation success rate > 95%
- [ ] No data breaches

**Target:** Zero preventable harms

### Metric 3: Equity
- [ ] App works equally well across demographic groups
- [ ] No disparities in recommendations by demographic
- [ ] Accessible (WCAG 2.1 AA compliant)

**Target:** No significant disparities; >90% accessibility score

### Metric 4: User Trust
- [ ] >80% of users trust the app with their data
- [ ] >75% of users feel understood by the app
- [ ] Net Promoter Score (NPS) >50

**Target:** High trust; users recommend to others

### Metric 5: Compliance
- [ ] Zero regulatory violations
- [ ] 100% HIPAA/GDPR/CCPA compliant
- [ ] Insurance coverage available (if applicable)

**Target:** Full compliance, ready for audits

---

## Roadmap Template

**Use this to plan your ethics work:**

```
MONTH 1: FOUNDATION
└── [ ] Assign ethics owner
    [ ] Read core docs (README, Principles, Red Flags)
    [ ] Identify current gaps (self-audit)
    [ ] Create ethics checklist

MONTH 2-3: FIXES
└── [ ] Fix critical issues (red flags, consent, data security)
    [ ] Implement crisis escalation
    [ ] Improve consent forms
    [ ] Accessibility audit & fixes

MONTH 4-6: VALIDATION
└── [ ] Expert ethics review
    [ ] Diverse user testing (50+ users)
    [ ] Incident response plan
    [ ] Documentation & evidence

MONTH 6+: LAUNCH READY
└── [ ] All critical items pass
    [ ] Legal review complete
    [ ] User testing complete
    [ ] Monitoring system set up

ONGOING: POST-LAUNCH
└── [ ] Monthly ethics committee
    [ ] Quarterly user safety surveys
    [ ] Quarterly harm review
    [ ] Annually full audit
```

---

## Final Checklist: Are You Ready?

Before you launch, answer these:

- [ ] Can you explain how your app follows all 5 APA principles?
- [ ] Can you list your red flag vulnerabilities and how you mitigated them?
- [ ] Do you have informed consent that users actually understand?
- [ ] Have you tested with diverse populations (race, age, gender, disability)?
- [ ] Do you have a crisis escalation protocol?
- [ ] Is all user data encrypted?
- [ ] Can users easily delete their data?
- [ ] Do you know who your ethics advisors are?
- [ ] Do you have an incident response plan?
- [ ] Have you read the APA Ethics Code (2017)?
- [ ] Are you tracking user safety metrics?
- [ ] Is ethics integrated into your culture (not just checkbox)?

**If you answered NO to 3+ of these: Not ready to launch.**

---

**Last reviewed:** 2026-03-20  
**Next update:** When 2025 APA Code is finalized (expected 2025-2026)

**Start here:** Pick your role above and follow the Month 1 checklist. Done in a day.

# Red Flags: Manipulative Patterns in Psychology Apps

**Purpose:** Identify psychological manipulation tactics that violate ethical principles.

**Why this matters:** Users in vulnerable states (depression, anxiety, trauma) are susceptible to manipulation. Apps claiming to help must actively avoid these patterns.

---

## Category 1: Engagement-Over-Wellbeing Patterns

### Pattern: Addiction-by-Design Mechanics

**What it is:**
Apps use variable reward schedules, streak systems, notifications, or gamification explicitly designed to create habit-loops—regardless of therapeutic benefit.

**Red flags:**
- [ ] Notifications timed for maximum engagement (based on user behavior data, not therapeutic need)
- [ ] Streak systems that punish users for missing a day (even if they're in crisis)
- [ ] Rewards for frequency of use, not quality of progress
- [ ] FOMO-inducing messages ("Others are making progress, you're not")
- [ ] Push notifications increased when engagement drops (reactivity, not helpfulness)

**Why it's harmful:**
- Vulnerable users confuse app engagement with actual healing
- Creates anxiety/shame when missing usage streaks
- Diverts energy from real therapeutic work
- Can exacerbate compulsive disorders

**Ethical principle violated:** Beneficence (doing good → doing harm instead)

**Mitigation:**
- Design for *healing frequency*, not *usage frequency*
- If streaks exist, they're optional and never shaming
- Notifications sent only for user-defined goals (not when engagement drops)
- Reward *progress*, not *participation*

---

### Pattern: Dark Patterns & Hidden Friction

**What it is:**
Making helpful features easy and harmful features hard to find. Using UX to trick users.

**Red flags:**
- [ ] Unsubscribe buried in settings (not one-click)
- [ ] Auto-renewal without clear reminder before charging
- [ ] "Continue as Guest" less visible than "Sign Up" (pushes data collection)
- [ ] Confirmation dialogs that discourage leaving ("Are you SURE you want to quit therapy?")
- [ ] Data export requires manual intervention (not automated)
- [ ] Privacy controls scattered across 5 different menus

**Why it's harmful:**
- Users stay in app against their interest
- Violates autonomy and dignity
- Erodes trust when users feel tricked
- Can be illegal under GDPR, CCPA, etc.

**Ethical principle violated:** Respect for Rights & Dignity, Fidelity

**Mitigation:**
- One-click unsubscribe/data deletion
- Auto-renewal requires active annual re-consent
- Privacy settings consolidated and clear
- Honest language ("Delete all my data" not "Manage account preferences")

---

### Pattern: Exploiting Psychological Vulnerabilities

**What it is:**
Deliberately using user's mental health struggles to drive engagement.

**Red flags:**
- [ ] Notifications that reference user's recorded symptoms ("We noticed you haven't journaled about your anxiety in 3 days")
- [ ] Messaging designed to induce guilt/shame if user stops using app
- [ ] Features that encourage isolation ("Just talk to me, I understand you better")
- [ ] Exploiting trauma history to create emotional dependence
- [ ] Suggesting app can replace therapy/medication ("You don't need meds, just use this")
- [ ] Micro-dosing negative emotions in messaging to keep users dependent

**Why it's harmful:**
- Creates artificial psychological dependency on app
- Delays real therapeutic help
- Traumatizes further (if based on trauma history)
- Violates fundamental trust in mental health tools

**Ethical principle violated:** Beneficence, Non-maleficence, Respect for Dignity

**Mitigation:**
- Notifications are purely informational (scheduling reminders, crisis resources)
- Messaging celebrates user progress and real-world connections
- Clear: "This complements therapy; it doesn't replace it"
- No messaging based on recorded vulnerabilities/trauma
- Users control all notification content (not system-generated)

---

## Category 2: Consent & Privacy Violations

### Pattern: Vague or Deceptive Informed Consent

**What it is:**
Users don't actually understand what they're agreeing to.

**Red flags:**
- [ ] Privacy policy uses legalese; average user can't understand it
- [ ] "We use your data to improve the app" (too vague)
- [ ] No clear explanation of how AI/algorithms use data
- [ ] Pre-checked boxes for data sharing/marketing
- [ ] "By using the app, you consent to..." (buried in settings, not at signup)
- [ ] No distinction between data used for care vs. marketing
- [ ] Consent buried in 40-page terms nobody reads

**Why it's harmful:**
- Users don't actually consent; they just accept friction
- Violates HIPAA, GDPR, CCPA
- Betrays trust when users later discover data practices
- Vulnerable users may not understand implications

**Ethical principle violated:** Respect for Rights & Dignity, Integrity, Fidelity

**Mitigation:**
- Plain-language consent (write for high school reading level)
- Explicit opt-in for any data sharing (no pre-checks)
- Separate consent for: care, research, marketing, analytics
- Renewal of consent annually
- Option to use full features without research/marketing consent

---

### Pattern: Data Exploitation

**What it is:**
Collecting intimate mental health data and using it in ways users didn't agree to.

**Red flags:**
- [ ] Mental health data sold to third parties (advertisers, employers, insurers)
- [ ] Data retention longer than necessary (keeping 10 years of depression logs)
- [ ] No user control over deletion ("We need 7 years for legal compliance")
- [ ] AI trained on user data without explicit consent
- [ ] Data breaches disclosed weeks/months later
- [ ] No encryption of mental health data at rest
- [ ] Data shared with "partners" (undefined)

**Why it's harmful:**
- Mental health data is uniquely sensitive (can be used to discriminate in hiring, insurance)
- Violates HIPAA right to access/delete
- Creates liability for data breaches
- Betrays vulnerability users trusted to app

**Ethical principle violated:** Respect for Rights & Dignity, Non-maleficence, Integrity

**Mitigation:**
- End-to-end encryption (user data never visible to platform)
- Data deletion on request within 30 days
- No third-party data sharing without explicit consent
- Data retention policy clearly stated (e.g., "deleted after 1 year inactivity")
- Regular security audits; breach notification <48h

---

## Category 3: Competence & Boundary Violations

### Pattern: Overstepping Clinical Boundaries

**What it is:**
App claims or implies it can do things it can't (diagnose, treat severe disorders, replace meds).

**Red flags:**
- [ ] Marketing: "Your AI therapist" (implies licensed therapist)
- [ ] Features: Providing differential diagnosis without disclaimer
- [ ] Claims: "Treat depression in 4 weeks" (unsupported)
- [ ] Encouraging users to stop medication ("The app works better")
- [ ] Claiming to diagnose conditions (only doctors can)
- [ ] No clear boundaries on what app can/can't handle
- [ ] Continuing service for severe disorders app isn't designed for

**Why it's harmful:**
- Users delay real medical care
- Can cause serious harm if they follow app's advice over doctor's
- Violates scope of practice
- Illegal practice of medicine/psychology

**Ethical principle violated:** Beneficence, Non-maleficence, Fidelity, Justice

**Mitigation:**
- Clear disclaimers: "This is NOT therapy. NOT a substitute for medication. NOT a diagnosis tool."
- Explicit scope: "This app helps with mild anxiety and stress. If you have bipolar disorder, PTSD, or active suicidality, talk to a doctor."
- Red-line escalation: Detect suicidality/psychosis → immediate crisis resources, not continued use
- Avoid language: "Your therapist," "Your psychiatrist," "We treat depression"

---

### Pattern: No Escalation Path for Serious Issues

**What it is:**
App fails to recognize or respond to users in crisis.

**Red flags:**
- [ ] No crisis detection (suicide assessment, psychosis indicators, abuse disclosure)
- [ ] Crisis resources outdated or incomplete
- [ ] No 24/7 escalation path
- [ ] Chatbot tries to handle serious issues instead of escalating
- [ ] No clear "talk to a human" button
- [ ] Crisis line numbers not verified/current
- [ ] No follow-up after crisis disclosure (abandonment)

**Why it's harmful:**
- Users in crisis get non-clinical response (chatbot)
- Delayed escalation = delayed help
- User loses trust in app and mental health tools generally
- Liability for harm

**Ethical principle violated:** Non-maleficence, Fidelity, Beneficence

**Mitigation:**
- Crisis detection algorithm (validated against gold-standard assessment)
- Immediate escalation: "Let me connect you with the 988 Suicide & Crisis Lifeline"
- Direct phone dialing option (not web form)
- 24/7 human support for serious issues
- Follow-up: "How are you doing?" within 24h (human outreach)

---

## Category 4: Diversity & Representation Failures

### Pattern: One-Size-Fits-All Design

**What it is:**
App designed for one demographic; deployed for everyone without testing.

**Red flags:**
- [ ] No testing with diverse populations (race, gender, age, disability, SES)
- [ ] Mental health model assumes Western individualism (doesn't honor collectivism, spirituality)
- [ ] Language support only English (or not tested with non-native speakers)
- [ ] No accessibility features (color contrast, screen reader, keyboard nav)
- [ ] Examples/vignettes use only one demographic
- [ ] AI/recommendations show bias by demographic group
- [ ] Assumptions about family structure (assumes nuclear family)

**Why it's harmful:**
- App ineffective or harmful for marginalized groups
- Perpetuates healthcare disparities
- Violates Justice principle
- Misses cultural mental health frameworks

**Ethical principle violated:** Justice, Respect for Dignity

**Mitigation:**
- Diverse beta testing before launch (minimum 20% each: race, gender, disability status)
- Cross-cultural mental health review (including lived experience)
- WCAG 2.1 AA accessibility compliance
- Support multiple languages (at least 2; plan for more)
- Audit AI/recommendations for bias across groups
- Representation in marketing materials

---

### Pattern: Pathologizing Cultural/Spiritual Beliefs

**What it is:**
App treats cultural or spiritual practices as symptoms/pathology.

**Red flags:**
- [ ] Questioning spirituality as symptom of mental illness
- [ ] Dismissing cultural healing practices ("That's just folk medicine")
- [ ] Assuming religious faith = delusion
- [ ] Not recognizing cultural mental health concepts (e.g., *hwa-byung* in Korean culture)
- [ ] Recommending medication/therapy as replacement for cultural/spiritual practice
- [ ] Valuing Western psychology over community/family-based healing

**Why it's harmful:**
- Invalidates user identity
- Disrespects cultural wisdom
- Damages therapeutic alliance
- Can increase psychological harm

**Ethical principle violated:** Respect for Dignity, Beneficence

**Mitigation:**
- Cultural competence training for all design/clinical staff
- Co-design with cultural community members
- Honoring diverse mental health frameworks (not just DSM-5)
- Integrating spiritual/cultural practices into content (not replacing them)
- Asking: "How do you and your community understand this issue?"

---

## Category 5: Research & Bias Failures

### Pattern: Using Biased Training Data

**What it is:**
AI trained primarily on one demographic; recommendations biased as a result.

**Red flags:**
- [ ] Research data 80%+ from one demographic
- [ ] No bias testing across groups
- [ ] "Proprietary algorithm" used to hide methodology
- [ ] Recommendations show different outcomes by demographic (e.g., certain groups get told to exercise, others referred to meds)
- [ ] Dataset sourced from university clinic (non-representative sample)
- [ ] No external validation on diverse populations

**Why it's harmful:**
- App perpetuates historical mental health disparities
- "Algorithmic racism" in recommendations
- Violates Justice principle
- Creates harm through bias

**Ethical principle violated:** Justice, Integrity, Non-maleficence

**Mitigation:**
- Audit training data for demographic representation
- Test model outputs across demographic groups
- Document bias findings and mitigation
- Use representative datasets or balance retrospectively
- Publish validation results (including disparities found)
- Regular bias audits (annually minimum)

---

## Category 6: Research Exploitation

### Pattern: Using Clinical Data for Marketing Without Consent

**What it is:**
User mental health data collected for care, then used for marketing/research without explicit re-consent.

**Red flags:**
- [ ] "Improving the app" means marketing A/B tests (not clinical outcomes)
- [ ] User case studies published without consent
- [ ] De-identified data shared with researchers (without consent)
- [ ] Behavioral data (not mental health data) used for targeting ads
- [ ] Research papers published about users without their knowledge
- [ ] "Research findings" are really marketing claims

**Why it's harmful:**
- Violates informed consent
- Users feel exploited
- Can identify users even when "de-identified"
- Violates HIPAA

**Ethical principle violated:** Respect for Rights, Integrity, Fidelity

**Mitigation:**
- Separate consent: care vs. research vs. marketing
- Users can use app without research participation
- Clear opt-in for any publication (with veto rights)
- Research reviewed by IRB (independent ethics review)
- No selling behavioral data to advertisers

---

## The Audit Checklist

Use this to review your app **before launch:**

### Engagement Ethics
- [ ] No addiction-design mechanics
- [ ] Notifications user-controlled, not system-driven
- [ ] Rewards progress, not frequency
- [ ] No dark patterns in UX
- [ ] One-click exit/data deletion

### Consent & Privacy
- [ ] Plain-language privacy policy
- [ ] Explicit informed consent (separate for care/research/marketing)
- [ ] No pre-checked data-sharing boxes
- [ ] User controls all notifications
- [ ] Data encrypted at rest and in transit

### Competence
- [ ] Clear scope statement ("What this app does/doesn't do")
- [ ] No diagnosing/prescribing claims
- [ ] Crisis detection + 24/7 escalation
- [ ] Red-line criteria clearly defined (when to escalate)
- [ ] No encouraging medication changes

### Diversity
- [ ] Tested with diverse demographics
- [ ] WCAG accessibility compliance
- [ ] Multiple languages (≥2, expandable)
- [ ] Culturally reviewed content (not just Western psychology)
- [ ] AI audited for bias

### Research
- [ ] All data collection disclosed
- [ ] Training data demographic representation documented
- [ ] Bias testing results published (including disparities)
- [ ] IRB review (if research component)
- [ ] Users can decline research participation

---

## Red Flag Summary: Quick Reference

| Red Flag | Principle | Fix |
|----------|-----------|-----|
| Addiction mechanics | Beneficence | Use therapeutic frequency, not engagement |
| Dark patterns | Respect/Fidelity | One-click exit, clear controls |
| Vague consent | Respect | Plain language, explicit opt-in |
| Data sales | Respect | No third-party sharing without consent |
| Clinical overreach | Beneficence | Clear scope, escalation path |
| No crisis handling | Non-maleficence | Crisis detection + 24/7 escalation |
| One-size design | Justice | Diverse testing, accessibility |
| Biased AI | Justice | Dataset audit, bias testing |
| Pathologizing culture | Respect | Cultural competence, co-design |
| Exploiting data | Integrity | Separate research consent |

---

## When to Stop Deployment

**DO NOT LAUNCH** if:
- [ ] No crisis escalation path and app handles serious issues
- [ ] Data collection not disclosed/consented
- [ ] Clinical claims not evidence-based
- [ ] Tested with <50 users, no diverse demographic sampling
- [ ] Algorithm behavior unexplainable (black box AI)
- [ ] No plan for handling harm reports

---

**Last reviewed:** 2026-03-20  
**Confidence level:** High (synthesized from APA Ethics Code + HIPAA + FDA guidelines)  
**Validation status:** Ready for cross-reference with other agents

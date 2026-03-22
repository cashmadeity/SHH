# Technology-Mediated Communication Ethics

**Purpose:** Define ethical communication in digital/technology contexts—apps, chatbots, AI therapy, text-based counseling, and asynchronous mental health support.

**Foundation:** APA ethics + technology + research on how digital mediums change therapeutic relationship.

**Target audience:** App developers, AI/ML designers, digital therapeutics creators, therapists integrating technology.

---

## Core Principle: The Medium Changes the Message

In-person therapy is synchronous, present, embodied. Technology disrupts that. Each medium has unique ethical implications.

**Key question for every tech implementation:** "What am I gaining? What am I losing?"

---

## 1. Medium-Specific Considerations

### Medium 1: Chatbots & AI Conversational Agents

**What it is:** Person converses with AI that responds conversationally (feels like talking to a therapist).

#### Ethical Issues

**Issue 1: False Intimacy**
```
PROBLEM:
Chatbot remembers every session. Person feels "known."
But chatbot doesn't actually know them—it processes patterns.
This false intimacy can prevent real connection.

EXAMPLE:
Person: "I haven't told you this before, but I was abused as a child."
Chatbot: "Thank you for trusting me with something so personal.
I remember how hard things have been for you."

↳ Sounds like genuine relationship
↳ Actually: database lookup + NLP response

ETHICAL RESPONSE:
"I have access to what you've shared before, and that helps me understand context.
And I'm an AI, not a person. I can't truly know you the way a human therapist can.
What I can do is help you explore these experiences and point you toward real support."
```

**Issue 2: Liability Confusion**
```
PROBLEM:
Person thinks chatbot can handle crisis. Chatbot escalates poorly. Person harmed.
Who's responsible? Person expected tool they trusted to work.

SAFEGUARD:
Clear, visible disclaimer:
"This is an AI tool. It's NOT therapy. It's NOT a substitute for a therapist.
In crisis: Call 988. Don't rely only on this app."

Placement: Visible on launch, not buried in terms of service.
```

**Issue 3: Preference for Bot Over Human**
```
PROBLEM:
Person prefers chatbot (always available, non-judgmental, consistent).
Never seeks human therapy. Condition worsens.

SAFEGUARD:
"If you're struggling with [serious issue], you need human support.
Let me help you find a therapist."

Don't let app prevent real care by being "convenient."
```

#### Good Practice: Chatbot with Escalation Guardrails

```
✅ DESIGN:
1. Clear scope: "I help with [X]. I don't handle [serious issues]."
2. Crisis detection: Recognize keywords → escalate immediately
3. Regular escalation suggestion: "You've been dealing with this a while.
   A human therapist might help more than I can."
4. Therapist integration (if possible): Share insights with their therapist
5. Honest about limits: "I'm an AI. I can't truly understand your experience."
```

---

### Medium 2: Text-Based Counseling (Asynchronous)

**What it is:** Person texts therapist; therapist responds within hours/days (not real-time).

#### Ethical Issues

**Issue 1: Delayed Crisis Response**
```
PROBLEM:
Person: "I'm thinking about hurting myself."
Therapist sees it 8 hours later (after work, asleep, etc.).
By then, crisis has escalated or passed.

SAFEGUARD:
- Set clear expectations: "I respond within 24 hours."
- Train person: "For crisis, use [crisis line, not text]."
- Have escalation protocol: If crisis is detected, immediate call (not text back)
- Provide emergency number on every message
```

**Issue 2: Tone Misinterpretation**
```
PROBLEM:
Text lacks tone/body language. Easy to misinterpret.

PERSON WRITES: "I did what we talked about."
THERAPIST READS: Resistance or success? Sarcasm or genuine?

SAFEGUARD:
- Clarify: "How did it go? I'm wondering if you felt it helped."
- Use more specific language (not assuming tone)
- Video check-ins periodically (not just text)
```

**Issue 3: Record-Keeping Liability**
```
PROBLEM:
Text lives forever. Searchable. Discoverable in legal proceedings.
Person's most vulnerable moments are archived and accessible.

SAFEGUARD:
- Clear data retention policy: "Messages deleted after [timeframe]"
- Encryption in transit AND at rest
- Person can request deletion anytime
- Separate consent for archival (if needed for safety)
```

#### Good Practice: Text Counseling Protocol

```
✅ CLEAR EXPECTATIONS:
- Response time ("I respond within 24 hours, weekdays only")
- Crisis escalation ("For emergency, call 988 first, then text me")
- Frequency ("Check in 1x/week")
- Session continuity ("These texts replace our weekly session" vs. "addition")

✅ TECHNICAL:
- Encrypted messaging only (HIPAA-compliant platform)
- No SMS (not HIPAA-compliant)
- Archive policy stated and consented
- Easy access to own records

✅ THERAPEUTIC:
- Longer, more thoughtful messages (not brief)
- Check tone: "I want to make sure this landed right..."
- Video calls every [X weeks] to sustain connection
- Clear escalation path (when text isn't enough)
```

---

### Medium 3: Video Therapy (Synchronous, Remote)

**What it is:** Real-time therapy via video (Zoom, Telehealth platform).

#### Ethical Issues

**Issue 1: Privacy & Home Settings**
```
PROBLEM:
Person joining from home where roommates/family can listen.
Home setting reveals information (poverty, hoarding, etc.) person didn't disclose.

SAFEGUARD:
- Ask at start: "Are you in a private space?"
- Provide guidance: "You need 15 minutes of privacy. Can you find that?"
- If NO: "Let's reschedule. We need privacy for this to work."
- Don't therapize from your home (power imbalance of seeing your space while they're vulnerable)
```

**Issue 2: Technical Failures = Relationship Rupture**
```
PROBLEM:
Internet cuts out mid-session. Person feels abandoned.
Therapist can't get back. Person's vulnerable moment is broken.

SAFEGUARD:
- Test technology before session starts
- Have backup plan: "If we drop, I'll call you on [phone number]"
- Debrief technical rupture: "That's frustrating. Let's rebuild connection."
- Have protocol if you can't reconnect: "I'm trying. Here's what we'll do..."
```

**Issue 3: Digital Fatigue**
```
PROBLEM:
Video therapy lacks embodied presence.
Staring at faces exhausts differently than in-person.
Non-verbal cues are flattened (harder to read).

SAFEGUARD:
- Shorter sessions may be better (50 min → 40 min)
- Periodic in-person sessions (if possible) for deeper work
- Acknowledge: "I know video is different. Tell me if you need adjustment."
```

#### Good Practice: Video Therapy Standards

```
✅ BEFORE SESSION:
- Test technology together
- Confirm privacy on both ends
- Agree on backup communication if dropped
- Set expectations on timing (no late-start grace)

✅ DURING SESSION:
- Start with connection (not jumping to content)
- Watch for tech issues ("You're freezing a little...")
- Take intentional pauses (longer than in-person, to account for video lag)
- End with check-in (connection recovery)

✅ AFTER SESSION:
- Follow-up text if technical issues happened
- Document: "Session on video; quality was [good/fair/poor]"
- If repeated issues: propose switching to phone or in-person
```

---

### Medium 4: AI Mental Health Assessment Tools

**What it is:** Questionnaire/algorithm that assesses mental health and recommends treatment.

#### Ethical Issues

**Issue 1: Algorithmic Bias**
```
PROBLEM:
AI trained on majority demographic. Minority groups get different/worse recommendations.

EXAMPLE:
- White patients with depression → "Therapy recommended"
- Black patients with same symptoms → "Medication recommended"
(Historical: Black patients over-prescribed psychiatric meds)

SAFEGUARD:
- Test algorithm across demographic groups
- Publish bias findings (transparency)
- Use representative training data
- Include lived-experience experts in validation
```

**Issue 2: False Precision**
```
PROBLEM:
Algorithm generates: "Based on your responses, you have Major Depressive Disorder."
(Implies diagnosis. But only a doctor can diagnose.)

SAFEGUARD:
Use language:
"Your responses are consistent with depression.
A doctor/therapist needs to confirm this diagnosis."

NOT: "You have depression."
```

**Issue 3: One-Size-Fits-All Recommendations**
```
PROBLEM:
Algorithm recommends standard treatment (e.g., "Take SSRIs").
Doesn't account for: pregnancy, cultural beliefs, other medications, trauma history.

SAFEGUARD:
- Recommendations include: "Talk to your doctor because..."
- Acknowledge exclusions: "This doesn't apply if you're pregnant / have heart disease / etc."
- Include alternatives: "If medication doesn't feel right, therapy is also evidence-based."
- No overconfidence
```

#### Good Practice: Responsible AI Assessment

```
✅ TRANSPARENCY:
- Explain what algorithm does (plain language)
- Disclose: trained on [demographic information]
- State: "This is screening, not diagnosis"
- List limitations: "Doesn't detect [X], can't substitute for doctor visit"

✅ HUMAN INVOLVEMENT:
- Never recommend treatment without human clinician review
- Always recommend professional follow-up
- Provide resources: "Here's how to find a therapist..."

✅ ACCOUNTABILITY:
- Regular bias audits (quarterly min.)
- User feedback mechanism ("This recommendation was wrong because...")
- Willingness to remove assessment if it's harmful
```

---

## 2. Synchronous vs. Asynchronous: Ethical Differences

### Synchronous (Real-Time: Calls, Video, Chat)

**Advantages:**
- Immediate crisis response possible
- Read tone/emotion in real-time
- Can adjust pace to person's needs
- Rupture/repair can happen same session

**Ethical challenges:**
- High availability expectations (person wants instant response)
- Technical failure = relationship rupture
- Therapist burnout (always "on")

### Asynchronous (Delayed: Text, Email, App Journaling)

**Advantages:**
- Lower therapist burden (can batch responses)
- Person can process and revise before sending
- Accessible for people with social anxiety
- Written record (helpful for memory)

**Ethical challenges:**
- Crisis detection is harder
- Tone misinterpretation
- Person feels abandoned if response is delayed
- Harder to read cues (is this urgent or routine?)

**Ethical guideline: Match medium to risk level**

```
LOW RISK (ongoing therapy, stable person):
✅ Asynchronous acceptable (text, app check-ins)

MODERATE RISK (suicidal ideation, trauma processing):
✅ Synchronous required (video, phone, immediate response)

HIGH RISK (acute crisis, active self-harm):
✅ Synchronous + in-person or escalation to emergency
❌ Asynchronous only is unethical
```

---

## 3. Data Privacy & Technology

### Rule 1: Encryption

```
✅ DO:
- End-to-end encryption (your servers can't read messages)
- Data encrypted at rest (not just in transit)
- Test encryption regularly
- Disclose encryption method (not secret = more trustworthy)

❌ DON'T:
- Store unencrypted mental health data
- Use personal email/texts (not HIPAA-compliant)
- Claim privacy without encryption
```

### Rule 2: Data Retention

```
✅ DO:
- Clear policy: "We delete data after [X months/years]"
- Person can request deletion anytime
- Automatic deletion (not manual, so nothing gets "forgotten")
- Exception: If legally required to keep longer, be transparent

❌ DON'T:
- Keep data "just in case" (indefinite retention = increased risk)
- Make deletion difficult (require lawyers, paperwork, etc.)
- Vague policy ("We keep your data secure" - for how long?)
```

### Rule 3: Third-Party Sharing

```
✅ DO:
- NO third-party data sharing without explicit consent
- Separate consent forms: care vs. research vs. marketing
- Clear: "We don't sell your data"
- Exception: Legal mandate (then disclose what was shared)

❌ DON'T:
- Share data with "business partners" (undefined)
- Use "improving the app" as excuse for data mining
- Pre-checked boxes for data sharing
- Sell de-identified data (can still be re-identified)
```

---

## 4. AI & Automation Ethics

### Challenge 1: When Humans Are Replaced

```
SCENARIO:
App uses AI to respond to all routine messages.
Human therapist reviews complex ones.

ISSUE:
Person doesn't know which is which.
Feels intimate connection to "therapist."
Actually talking to chatbot most of the time.

ETHICAL RESPONSE:
"Your primary support is AI. [Name] is your human therapist.
Here's how we work together."

Transparency about role. Not pretending bot = therapist.
```

### Challenge 2: Algorithmic Decision-Making

```
SCENARIO:
Algorithm decides: "This person should be escalated to human therapist
because risk score is [X]."

ISSUE:
Algorithm's decision process is unexplainable.
Therapist doesn't know why escalation was recommended.
Person feels singled out, unsure why.

ETHICAL RESPONSE:
- Explainable AI (can say: "You mentioned [X] which raised concern")
- Not: "Our proprietary algorithm decided" (black box)
- Person knows: "You were escalated because you mentioned suicide"
- Therapist knows: Why escalation happened
```

### Challenge 3: Consent for AI Use

```
❌ VAGUE CONSENT:
"We use advanced technology to improve your care."
(What technology? What improvement? How is data used?)

✅ SPECIFIC CONSENT:
"We use an AI chatbot to provide support between therapy sessions.
The AI:
- Can recognize crisis language
- Learns from your patterns
- Sometimes misunderstands (is an AI)
- Never makes diagnosis/treatment decisions alone

Your data trains our AI [YES / NO - choose]"

(Specific enough person understands what they're agreeing to)
```

---

## 5. Technology-Mediated Relationship Challenges

### Challenge 1: Over-Reliance on Technology

```
PERSON: "I text you more than I talk to real people now.
You're my main support."

THERAPIST (RED FLAG): Not addressing this

THERAPIST (GOOD): 
"I notice you're relying heavily on our text connection.
That's understandable because I'm available and safe.
And I'm worried you're not building real-world connection.
Let's talk about that."

(Using technology awareness as therapeutic material)
```

### Challenge 2: Boundary Blurring

```
PROBLEM:
Person texts therapist personal updates that aren't therapy.
Therapist responds. Feels like friendship.
Person expects availability like a friend.
Therapist gets drained.

BOUNDARY SETTING:
"I love hearing good news from you. And I want to be clear:
Our relationship is professional/therapeutic. I have capacity for [frequency].
Outside of that, you have friends/family for ongoing connection.

Does that work for you?"
```

### Challenge 3: The Always-On Expectation

```
PROBLEM:
Person expects instant response (app available 24/7).
Therapist responds within 24 hours.
Person feels abandoned.

PREVENTION:
Set clear expectations UP FRONT:
"I respond within 24 business hours.
For crisis: Use 988, not this app.
I'm not available nights/weekends."

(Prevents resentment)
```

---

## 6. Technology Accessibility & Ethics

### Challenge 1: Not Everyone Has Tech Access

```
PROBLEM:
"Download the app" assumes smartphone + data + literacy with tech.
Excludes: elderly, rural, low-income, digital immigrants, people without tech access.

SOLUTION:
- Offer non-app option (phone, in-person, paper)
- Don't force digital-only
- Test with people with limited tech access
- Make app work on basic smartphones (not just newest tech)
```

### Challenge 2: Digital Divide & Equity

```
PROBLEM:
Rich people get video therapy (more effective?).
Poor people get chatbot (cheaper/less effective?).

ETHICAL RESPONSE:
- Chatbot quality should match video therapy quality
- OR: Subsidize video for low-income people
- Don't use cost-cutting as excuse for lower-quality care
```

---

## 7. Therapy-Specific Tech Ethics

### Remote Therapy with Vulnerable Populations

```
CHILD/ADOLESCENT:
- Parental involvement rules (varies by state)
- How to handle mandated reporting if remote?
- What if parent is abuser? (can't safely disclose at home)

MITIGATION:
- Clear policy on parental involvement
- Private space for sensitive disclosures
- Escalation protocol for abuse disclosure
- Consultation with legal/clinical supervisors
```

### Digital Records & Litigation

```
PROBLEM:
Text messages are discoverable in legal proceedings.
Child custody case: therapist's notes about "concerning parental involvement"
gets used against parent.

ETHICAL COMPLEXITY:
Balance: Person's privacy vs. legal process

MITIGATION:
- Clear documentation standards (not inflammatory language)
- Regular review with supervision
- Advocate for person's privacy (challenge discovery if possible)
- Transparency: "This might be used in court"
```

---

## 8. Technology-Mediated Communication Checklist

Before launching any technology-mediated mental health service, ask:

### Privacy & Security
- [ ] End-to-end encryption for all mental health data
- [ ] Data retention policy clear and automatic
- [ ] No third-party data sharing without explicit consent
- [ ] Regular security audits (at least quarterly)
- [ ] Breach notification plan (<48 hours to person)

### Clarify Relationship
- [ ] Clear: "This is NOT therapy" OR "This is therapy, but [limitations]"
- [ ] Transparent: Who/what is responding (human vs. AI)
- [ ] Honest: What can/can't this medium do
- [ ] Escalation: When to use it vs. crisis line vs. therapist

### Crisis Safety
- [ ] Crisis detection (if relevant)
- [ ] Immediate escalation protocol
- [ ] 24/7 access to crisis resources
- [ ] No delayed response for crisis content

### Accessibility
- [ ] Works on basic phones (not just latest tech)
- [ ] Accessible to people with disabilities (WCAG compliance)
- [ ] Multiple languages (minimum 2, planned expansion)
- [ ] Non-digital option available (phone, in-person)

### Human Oversight
- [ ] Clinician reviews for risks/red flags
- [ ] Not fully automated (human in the loop)
- [ ] Escalation to human available
- [ ] Regular supervision/consultation

### Consent
- [ ] Specific informed consent (not vague)
- [ ] Separate consent for: care, research, AI training
- [ ] Easy to withdraw consent
- [ ] Renewal of consent (at least annually)

### Testing
- [ ] Tested with diverse users (not just early adopters)
- [ ] Tested with vulnerable populations (if targeting them)
- [ ] AI bias testing (if using algorithms)
- [ ] User feedback mechanism for problems

---

## 9. Research on Technology-Mediated Therapy

**What we know:**
- **Video therapy ≈ in-person** (outcomes similar for most issues)
- **Text/asynchronous** works well for stable, low-risk populations
- **AI chatbots** can help with psychoeducation; no evidence they replace therapy
- **Crisis detection algorithms** miss ~20-30% of risk (not perfect)
- **People prefer human** when vulnerable; prefer tech when stable/educational

**What we don't know:**
- Long-term outcomes of app-based therapy (studies mostly 8-12 weeks)
- How AI affects therapeutic relationship quality
- Whether digital-first mental health widens/narrows equity gaps
- Generalization across cultures (most studies are Western, educated samples)

**Implication:** Be humble. Your tech probably works for stable people with tech access. For crisis/complex/vulnerable: include human support.

---

## 10. Integration with Ethics Framework

| APA Principle | Tech-Mediated Application |
|---------------|-----------------------|
| **Beneficence** | Does this tech actually help? For whom? (Not just engagement) |
| **Non-maleficence** | What harms could happen? (Tech failure, false intimacy, isolation) |
| **Fidelity** | Be honest: Human vs. AI? Therapy vs. app? Crisis vs. routine? |
| **Integrity** | Transparent: How does it work? What data? What happens to it? |
| **Justice** | Who has access? Does it widen or narrow equity gaps? |
| **Respect** | Person controls their data. Understands what they're agreeing to. |

---

## Next Steps

1. **Audit your tech** - Does it meet these ethical standards?
2. **Get feedback** - Ask users: Do you feel safe? Do you understand what's happening?
3. **Test crisis handling** - Can your escalation system handle real crisis?
4. **Plan for failure** - What if tech fails mid-session? Have backup plan.
5. **Review quarterly** - Technology & threats evolve. Update accordingly.
6. **Stay grounded in relationship** - Technology serves therapy. Therapy doesn't serve technology.

---

**Last reviewed:** 2026-03-21  
**Confidence level:** High (based on APA ethics + telehealth research + digital safety frameworks)  
**Cross-references:** Ethics-Guardrails/README.md, Five-Core-Principles.md, Red-Flags/Manipulative-Patterns.md

**Key research citations:**
- Hilty et al. (2013): Telepsychiatry: Effectiveness and impact
- Brooks et al. (2020): COVID-19 and telehealth: Benefits vs. risks
- Torous et al. (2020): Digital mental health and COVID-19
- FDA guidance on digital health: https://www.fda.gov/medical-devices/digital-health

# DBT Safety & Crisis Protocols for Digital Applications

**Modality:** Dialectical Behavior Therapy  
**Focus:** Skills coaching, distress tolerance, crisis survival, and the DBT philosophy  
**Status:** Comprehensive guide for DBT-based apps and crisis-aware digital therapeutics  
**Last Updated:** 2026-03-21

---

## DBT Core Principles & Ethical Foundations

### What Makes DBT Distinctive

**Core Theory:**
- **Dialectic:** Balance acceptance (validation) + change (skills)
- **Skills:** Four main modules (Mindfulness, Distress Tolerance, Emotion Regulation, Interpersonal Effectiveness)
- **Structure:** Individual therapy + skills group + phone coaching + therapist consultation team
- **Population:** Originally developed for Borderline Personality Disorder (BPD); now used for suicidality, self-harm, substance abuse, eating disorders

**Ethical Strengths:**
- **Validation:** Explicitly values acceptance & understanding
- **Specificity:** Concrete skills, teachable, measurable progress
- **Crisis-aware:** Built on assumption that crisis is likely; plans for it
- **Responsibility:** Team approach (therapist accountable to team)

**Ethical Vulnerabilities:**
- **Complexity:** Requires coordination (skills group + therapist + coach). Digital simplification may miss dialectic.
- **Skills without safety:** Teaching coping skills doesn't prevent self-harm if crisis isn't addressed
- **Phone coaching simulation:** Text-based "coaching" isn't real phone coaching—different dynamic
- **Chains analysis intensity:** Detailed self-disclosure about self-harm can be retraumatizing

---

## DBT in Digital Context: Opportunities & Risks

### What CAN Be Effectively Automated in DBT

✅ **Skills Teaching & Psychoeducation**
- Mindfulness basics (breathing, grounding, present-moment awareness)
- Distress tolerance skills (TIPP, self-soothing, distracting, radical acceptance)
- Emotion regulation (ABC PLEASE, opposite action, check-the-facts)
- Interpersonal effectiveness (DEAR MAN, GIVE, FAST)

✅ **Structured Skill Practice**
- Guided breathing exercises with timer
- Grounding exercises (5 senses, ice dive, cold water)
- Worksheets for self-soothing planning
- Emotion regulation chain analysis prompts

✅ **Crisis Resource Access**
- Crisis hotline numbers (988, Crisis Text Line)
- In-app crisis de-escalation tools (if supplementing real therapy)
- Safety planning template & storage
- Skills quick-reference during distress

✅ **Tracking & Accountability**
- Self-harm urges vs. acts (with behavioral definition)
- Skill use tracking (which skills helped?)
- Behavioral chain tracking (A-B-C-D-E format)
- Homework completion (skills group worksheets)

### What CANNOT & SHOULD NOT Be Automated

❌ **Crisis Assessment & Intervention (without human)**
- Assessment of suicide risk requires clinical judgment, not algorithm
- "Are you safe?" requires real human who can escalate
- DBT assumes user is high-risk for self-harm; automation must never replace human decision-making
- **Risk:** User in crisis, app says "you're OK," user harms self

❌ **Phone Coaching (unless with real therapist)**
- DBT phone coaching = real-time support between sessions
- Text-based "coaching" is fundamentally different (no voice, tone, presence)
- Coaching is **brief, concrete, skills-focused** — not therapy
- **Risk:** User thinks text coaching replaces human coaching; doesn't escalate in crisis

❌ **Individual Therapy Component**
- DBT individual therapy = relationship + case formulation + suicide risk management
- Relationship is **vehicle for change** in DBT, not optional
- Cannot be replaced by chatbot or algorithm
- **Risk:** User has untreated suicidal ideation because "app is my therapy"

❌ **Chains Analysis (Detailed)**
- Chains analysis = detailed exploration of self-harm antecedents
- Requires skilled therapist to guide (intrusive memories, shame)
- Self-directed chains work can increase distress without therapeutic support
- **Risk:** User does chains, triggers trauma, no therapist to help integrate

---

## Ethical Deep Dives: DBT-Specific Challenges

### Challenge 1: The Dialectic in Digital Context

**The DBT Stance:**
"I accept you exactly as you are, AND I expect you to change."

**The Risk in Digital:**
- Apps push either acceptance ("you're fine as is") OR change ("fix yourself")
- Few achieve true dialectic
- User feels either unsupported or pressured

**Example of Dialectic Failure:**
- **Pure acceptance:** "Your self-harm is a valid coping strategy. Use it as needed." → Enables harm
- **Pure change:** "Self-harm is bad. Stop immediately." → Invalidating, causes shame, increases self-harm

**Example of Dialectic Success:**
- "Your self-harm makes sense—it helps you regulate. AND it has costs. Let's learn skills that work AND keep you safer. Skill-building is possible for you."
- This is **acceptance + change simultaneously**

**App Design Implementation:**
- [ ] Features are explicitly both validating AND change-focused
- [ ] Tone never shames self-harm, but never encourages it
- [ ] Skills are framed as "additions," not "replacements" (you can still use old coping, AND try new skills)
- [ ] User's autonomy to not change is explicitly respected

---

### Challenge 2: Skills Teaching Without Real Therapist Relationship

**The Risk:**
- DBT skills are tools, teachable in digital format (✅ can be done)
- BUT their effectiveness depends on therapeutic relationship & commitment to change (⚠️ hard to achieve digitally)
- User learns skill, doesn't practice or use it because relationship/motivation missing

**DBT Principle:**
**Skills + Motivation + Relationship = Change**

Digital can provide skills, but relationship is harder, motivation may falter.

**Solution: Motivation & Accountability Built In**

✅ **DO:**
- Explain WHY each skill matters (chain to user's values)
- Example: "You want to stay alive. Self-harm puts you at risk. These skills keep you alive AND reduce pain."
- Track skill practice (not as surveillance, but as accountability)
- Celebrate effort, not just outcomes
- Connect to life values: "This skill moves you toward ___ (what matters to you)"

❌ **DON'T:**
- Teach skills without motivation ("Just do it")
- Assume user will use skills because "they work"
- Track without context ("You did 3 skills this week")
- Shame non-use ("You didn't practice")
- Leave user alone with skills (no relationship)

**Implementation:**
- [ ] Each skill explicitly tied to user's stated goals/values
- [ ] App asks: "What will you use this skill for?" (motivation check)
- [ ] Practice is encouraged but optional (user autonomy)
- [ ] Therapist involvement encouraged (app notes: "Please discuss this with your DBT therapist")

---

### Challenge 3: Crisis Protocol (Non-Optional)

**The DBT Reality:**
- Users in DBT are **high-risk for self-harm, suicide, crises**
- Crisis protocol is not optional; it's fundamental
- Failure to escalate = abandonment + potential harm

**What DBT Does (In-Person):**
1. **Therapist assessment:** Is user safe right now? (real clinical judgment)
2. **Safety planning:** Collaborative; specific to user
3. **Crisis response:** Phone coaching → therapist → hospitalization if needed
4. **Post-crisis:** Therapy continues; crisis is normalized, analyzed via chains

**What Digital DBT Must Do:**

**Level 1: Prevention (Always)**
- [ ] Safety plan created WITH therapist (not in app alone)
- [ ] Safety plan stored in app (user can access anytime)
- [ ] Skills accessible during crisis (quick-reference, crisis de-escalation tools)
- [ ] User educated: "Urges to self-harm are normal in DBT. You can learn to tolerate them."

**Level 2: Escalation Trigger (If user indicates crisis)**
- [ ] Crisis screening: "Are you safe right now?" "Are you thinking about harming yourself?"
- [ ] If YES: Immediate escalation (no delays)
- [ ] Escalation options:
  - [ ] 988 Suicide & Crisis Lifeline (call, chat, text)
  - [ ] Crisis Text Line (text HOME to 741741)
  - [ ] Call DBT therapist (if within office hours; must be 24/7protocol)
  - [ ] Go to emergency department
  - [ ] Call 911 if immediate danger

**Level 3: Response (Therapist takes over)**
- [ ] Therapist calls/emails user (SLA: within 1 hour if office hours, 24h if not)
- [ ] Safety plan reviewed & updated
- [ ] Chains analysis if user is stable (understanding what happened)
- [ ] Decision: Continue DBT? Hospitalize? Change level of care?

**Level 4: Post-Crisis (Normalize & Learn)**
- [ ] Therapy continues (DBT doesn't abandon in crisis)
- [ ] Chains analysis: What was the function of the urge? What led up to it?
- [ ] Skills review: Which skills helped? Which ones weren't used? Why?
- [ ] Relationship: "I'm glad you reached out. Let's keep you safe."

**App Implementation:**
- [ ] Crisis screening present at every session start
- [ ] Clear escalation pathway (not hidden, tested)
- [ ] Contact with therapist automatic (app notifies therapist)
- [ ] No "we'll check on you later"—escalation is immediate

---

### Challenge 4: Self-Harm Tracking Without Reinforcement

**The Risk:**
- Tracking self-harm serves clinical purpose (understanding patterns)
- But tracking can become compulsive, shame-inducing, or reinforcing of behavior
- User self-reports harm → app charts it → user feels judged OR tracked

**DBT Principle:**
- Self-harm is data, not moral failure
- Tracking = understanding, not punishment

**Implementation:**
- [ ] Tracking is **behavioral** not **moral**: "3 cutting incidents" (not "failed 3 times")
- [ ] Tracking includes **function**: "Cut to relieve emotional pain; lasted 10 min; urge resolved"
- [ ] Therapist reviews data collaboratively (not "here's your graph of shame")
- [ ] Non-harm is celebrated (not as triumph, but as data): "0 incidents this week; 5 skills used instead"

**Important Nuance:**
Some users benefit from tracking; others find it reinforcing. This **must** be user + therapist choice, not app default.

**App Feature:**
- [ ] Tracking is optional
- [ ] User & therapist explicitly agree: "Do you want to track self-harm in this app?"
- [ ] If yes: Behavioral language, not moral
- [ ] If no: App respects choice (no pressure to track)

---

### Challenge 5: Phone Coaching Simulation vs. Real Coaching

**What DBT Phone Coaching Actually Is:**
- Real-time, brief (10-15 min call)
- Skills-focused ("Tell me what skill you're using right now")
- Supportive ("You can do this. Try TIP skills.")
- Therapist voice + presence = calming

**The Risk of "Text Coaching":**
- Text-based coaching fundamentally different (no voice, tone, presence)
- User might think "this is DBT phone coaching" (it's not)
- User relies on text coach, doesn't escalate properly

**What Text-Based Coaching CAN Do Well:**
- Provide skill reminders during crisis
- Offer psychoeducation
- Direct user to resources
- Prompt reflection ("What skill might help right now?")

**What Text-Based Coaching CANNOT Do:**
- Provide real therapeutic relationship
- Assess crisis safety in real-time
- Offer voice-based reassurance & grounding
- Replace actual phone coaching with therapist

**App Design Responsibility:**
- [ ] If app includes coaching-like features, clearly state: "This is not phone coaching. It's a skill reminder."
- [ ] Never position text as substitute for real therapist coaching
- [ ] Escalation to real therapist easy & encouraged
- [ ] User training: "This app is a tool between sessions. Therapist is still your primary coach."

---

## Safety Planning in DBT Digital Context

### DBT-Specific Safety Plan Components

**Standard: Collaborative plan created WITH DBT therapist (not app alone)**

**Contents:**
1. **Warning signs** (when crisis likely)
   - Increased isolation
   - Stopped using skills
   - Rumination about self-harm
   - Withdrawal from commitments

2. **Internal coping** (skills used first)
   - Grounding (5 senses)
   - Cold water/TIPP
   - Opposite action
   - Mindfulness

3. **Social supports** (people to contact)
   - DBT therapist
   - Skills group members
   - Trusted friend
   - Family member

4. **Professional help** (escalation)
   - Therapist: [phone]
   - Crisis line: 988
   - Crisis text: HOME to 741741
   - Emergency: 911

5. **Ways to make environment safer**
   - Remove means (if relevant; therapist assesses)
   - Increase structure
   - Reduce access to harm (keys to friend, etc.)

**Digital Storage & Access:**
- [ ] Plan stored in app (user + therapist can access)
- [ ] Plan accessible during crisis (quick, no login needed)
- [ ] Plan reviewed monthly (at therapy session)
- [ ] Plan updated when circumstances change
- [ ] User can print/download (multiple copies, multiple locations)

---

## Red Flags: When DBT Is Going Wrong

### Red Flag 1: Crisis Escalation Failure

**Sign:**
- User reports self-harm in app; no therapist response
- Crisis hotline number provided; user doesn't know how to use it
- User says "I told the app I wanted to hurt myself and nothing happened"
- Therapist unaware of in-app crisis reports

**Why It's Critical:**
- DBT users are high-risk; escalation failure = abandonment
- Digital distance makes escalation even more essential

**Fix:**
- [ ] Crisis escalation tested before launch (actually call 988; confirm someone answers)
- [ ] App notifies therapist immediately when crisis screening positive
- [ ] Therapist response protocol in writing (must call within 1 hour if office hours)
- [ ] If therapist unavailable: Automatic escalation to crisis line
- [ ] User gets confirmation: "Your therapist has been notified. [Crisis line] is available 24/7."

---

### Red Flag 2: Skills Taught Without Relationship or Accountability

**Sign:**
- App has 40 skills modules; user never completes one
- User learns skill, never practices or uses it
- User doesn't know which skills work for them because no therapist feedback
- App says "Great job learning!" but user hasn't actually changed behavior

**Why It's a Problem:**
- DBT skills are only valuable if used
- Without relationship/accountability, skills become abstract knowledge
- User spends time in app, doesn't get better

**Fix:**
- [ ] Skills are connected to user goals (not just "learn this skill")
- [ ] Therapist discusses which skills user tried & which helped
- [ ] App tracks practice (accountability without shame)
- [ ] Progress is measured by skill use, not module completion
- [ ] If user isn't using skills after 2 weeks, therapist & user problem-solve why

---

### Red Flag 3: Chains Analysis Retraumatization

**Sign:**
- App asks user to describe self-harm incident in detail
- No therapist present to process/integrate
- User becomes triggered describing the incident
- User stops using app because chains are upsetting

**Why It's a Problem:**
- Chains analysis without therapeutic support can be retraumatizing
- User needs therapist to help integrate & make sense of it

**Fix:**
- [ ] Chains analysis is **brief & therapist-guided**, not detailed self-report in app
- [ ] App can prompt: "What were you feeling right before? What happened after?"
- [ ] But detailed chains happen **in therapy session**, not app
- [ ] If app includes chains, therapist reviews before/after

---

### Red Flag 4: Mixing Prevention & Intervention

**Sign:**
- App has "self-harm prevention tips" but lacks crisis escalation
- User learns skills but has no safety plan or escalation
- App assumes prevention is enough (it's not for DBT population)

**Why It's a Problem:**
- DBT population will likely experience crisis despite prevention
- App must plan for crisis, not just prevent

**Fix:**
- [ ] Prevention features (skills) paired with crisis protocol
- [ ] Safety plan is prominent & accessible
- [ ] Crisis escalation tested & operational
- [ ] User educated: "These skills help. AND, if you're in crisis, call 988."

---

### Red Flag 5: Therapist Unaware of App Use

**Sign:**
- User using app extensively but therapist doesn't know
- App data doesn't inform therapy (therapist isn't reviewing it)
- User makes decisions based on app advice that contradicts therapy
- No coordination between app skills & therapy goals

**Why It's a Problem:**
- DBT is coordinated care; app is separate silo
- Therapist can't assess safety or progress if unaware of app data

**Fix:**
- [ ] App explicitly designed FOR use with DBT therapist
- [ ] Data shareable with therapist (user chooses what to share)
- [ ] Therapist can access/review app data (with user consent)
- [ ] In-session: Therapist asks "What app did you use this week?"
- [ ] Coordination: Therapist & app aligned on goals/skills

---

## DBT-Specific Implementation Checklist

### Before Launch

**DBT Fidelity:**
- [ ] Developer/advisor has DBT training (not just knowledge of DBT)
- [ ] Skills teaching is DBT-accurate (consult DBT manual)
- [ ] Dialectic is maintained (acceptance + change, both present)
- [ ] Modality constraints respected (skills are scaffolding, not replacement for therapy)

**Safety (Critical):**
- [ ] Crisis screening present & tested (actually works)
- [ ] Escalation protocol written & tested (call 988, confirm answer)
- [ ] Therapist notification automatic (app → therapist in <5 min)
- [ ] 24/7 crisis resource available (not just office hours)
- [ ] Safety plan template provided (user + therapist create it)
- [ ] Safety plan storage accessible during crisis (no login)

**Skills & Features:**
- [ ] Skills are concrete, teachable, DBT-accurate
- [ ] Each skill has rationale (why this skill? what does it do?)
- [ ] Practice is encouraged but optional (user autonomy)
- [ ] Tracking is behavioral, not moral ("incidents," not "failures")
- [ ] Chains analysis (if included) is brief, not detailed

**Relationship:**
- [ ] App explicitly supports therapy, doesn't replace it
- [ ] "Talk to your DBT therapist" appears throughout
- [ ] Data shareable with therapist (user consent)
- [ ] Therapist guidance visible ("Your therapist recommended...")

**User Testing:**
- [ ] Tested with ≥10 people in active DBT
- [ ] At least 1 DBT therapist tested & approved
- [ ] At least 1 person tested crisis escalation (actually called 988)
- [ ] Users report skills are helpful AND therapist is primary resource

---

### Post-Launch Monitoring

**Safety Monitoring:**
- [ ] Crisis escalations tracked (frequency, outcomes)
- [ ] Follow-up: Did escalations lead to appropriate care?
- [ ] Adverse events: Any self-harm or suicide linked to app?
- [ ] Therapist feedback: Are they seeing users improve?

**Engagement:**
- [ ] Skill use tracked (which skills used? which ignored?)
- [ ] Session attendance: Does app use correlate with therapy attendance?
- [ ] Dropout: Why do users stop using app?

**Efficacy:**
- [ ] Self-harm tracking (if consented): Trends over time
- [ ] Suicidal ideation: Any change in frequency/intensity?
- [ ] User satisfaction: Do users feel app helps?
- [ ] Therapist satisfaction: Do therapists find it useful?

---

## Integration with Core Ethics Principles

(See [08-Cross-Reference-to-Core-Ethics.md](08-Cross-Reference-to-Core-Ethics.md) for full details)

**Beneficence & Nonmaleficence:**
- DBT is evidence-based for self-harm, suicidality → Beneficence ✅
- BUT crisis must be managed properly → Nonmaleficence requires perfect escalation ⚠️

**Fidelity & Responsibility:**
- DBT is team-based, coordinated → App must support coordination ✅
- Owner responsible for crisis response → Can't delegate to algorithm ✅

**Integrity:**
- DBT is transparent about skill limitations → Be honest about app limitations ✅
- Don't overstate efficacy of digital skills coaching ✅

**Justice:**
- DBT accessible but intensive → Digital version must not exclude (cost, access) ⚠️
- Test across demographics (gender, race, trauma history) ✅

**Respect for Rights & Dignity:**
- DBT validates → App must validate (not just problem-solve) ✅
- User autonomy: Choice in whether to use skills, app ✅

---

## References & Further Reading

**DBT Foundations:**
- Linehan, M. M. (1993). *Cognitive-Behavioral Treatment of Borderline Personality Disorder.* Guilford Press.
- Linehan, M. M. (2015). *DBT Skills Training Manual* (2nd ed.). Guilford Press.

**Safety Planning:**
- Stanley, B., & Brown, G. K. (2012). Safety planning intervention: A brief intervention to mitigate suicide risk. *Cognitive and Behavioral Practice*, 19(2), 256–264.

**Crisis Response:**
- National Suicide Prevention Lifeline: https://suicidepreventionlifeline.org/
- Crisis Text Line: Text HOME to 741741

**Research on Digital DBT:**
- Cuijpers, P., et al. (2019). Internet-based psychotherapy for adults with depression and anxiety. *Cochrane Database of Systematic Reviews*.

---

**Last reviewed:** 2026-03-21  
**Confidence level:** High (DBT manual, empirical research, crisis standards)  
**Cross-references:** Ethics-Guardrails KB, Red Flags document, Cross-Reference document

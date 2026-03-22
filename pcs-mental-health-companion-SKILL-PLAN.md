# PCS Mental Health Companion Skill - Creation Plan

**Status:** Ready for Skill Builder Integration  
**Created:** 2026-03-21 01:27 UTC  
**Skill Type:** Personal Health Companion (Daily Check-in + Adaptive Support)  
**Integration Path:** Load into Personal CEO memory + daily agent interaction

---

## 🎯 Skill Purpose

Create a personal mental & physical health companion that:
- Tracks daily PCS symptoms
- Identifies personalized trigger patterns
- Provides adaptive recommendations
- Synthesizes progress over time
- Integrates with personal memory system
- Evolves based on user's unique PCS profile

---

## 📋 Skill Structure (clawhub/skill-creator ready)

### SKILL.md (Frontmatter)

```yaml
name: pcs-mental-health-companion
description: Personal post-concussion syndrome (PCS) companion providing daily symptom tracking, personalized trigger analysis, and adaptive recovery recommendations. Use when: (1) Daily PCS symptom check-in, (2) Analyzing symptom patterns, (3) Planning recovery strategies, (4) Managing emotional/cognitive symptoms, (5) Coordinating care with specialists, (6) Tracking progress over time. Includes evidence-based management strategies from Mayo Clinic, NIH, and clinical guidelines.
```

### SKILL.md (Body - Key Sections)

1. **Daily Symptom Check-In**
   - 5-minute structured interview
   - Physical, cognitive, emotional, environmental factors
   - Stores to personal memory
   - Identifies red flags

2. **Pattern Recognition Engine**
   - Tracks triggers over time
   - Identifies correlations (sleep → headaches, stress → fog, etc.)
   - Generates personalized trigger profile
   - Predicts high-risk days

3. **Adaptive Recommendations**
   - Suggests strategies based on tracked patterns
   - Prioritizes highest-impact interventions
   - Scales recommendations by energy level
   - Integrates professional guidance

4. **Recovery Progress Synthesis**
   - Weekly summary of trends
   - Milestone celebrations
   - Adjustment recommendations
   - Specialist coordination updates

5. **Crisis Support**
   - Escalation protocols
   - When to contact professionals
   - Emergency resource access
   - Grounding techniques for anxiety

---

## 📁 Directory Structure (clayhub-ready)

```
pcs-mental-health-companion/
├── SKILL.md (required)
│   ├── Frontmatter (name, description)
│   └── Body (5 key sections above)
│
├── scripts/
│   ├── daily-checkin.py (structured symptom survey)
│   ├── pattern-analyzer.py (trigger correlation engine)
│   └── recommendation-engine.py (adaptive suggestions)
│
├── references/
│   ├── symptom-database.md (complete PCS symptom guide)
│   ├── trigger-patterns.md (common trigger combinations)
│   ├── management-strategies.md (evidence-based interventions)
│   ├── specialist-guide.md (when to involve professionals)
│   └── recovery-milestones.md (progress tracking framework)
│
└── assets/
    ├── symptom-tracking-template.json (check-in data structure)
    ├── trigger-correlation-matrix.json (pattern analysis data)
    └── daily-summary-template.md (output format)
```

---

## 🧠 Core Functionality

### Daily Check-In Process
**Input:** User responses to structured questions  
**Output:** Symptom profile + trigger identification + recommendations

**Questions:**
1. Physical: Headache (0-10), dizziness, fatigue, vision, other?
2. Cognitive: Focus/memory clarity (0-10), brain fog, speed?
3. Emotional: Mood (0-10), anxiety, irritability level?
4. Sleep: Hours slept, sleep quality (0-10)?
5. Activities: What did you do today? Any triggers?
6. Medications: Taken any medications?
7. Accomplishments: What went well today?

### Pattern Recognition
**Analyzes Over Time:**
- Symptom trends (improving? plateaued? cycling?)
- Trigger correlations (sleep deprivation → headaches?)
- Activity thresholds (exercise amount → fatigue?)
- Temporal patterns (time of day effects?)
- Environmental factors (weather, noise, light?)

**Generates:**
- Personal trigger profile
- Risk alert system (high-risk days predicted)
- Coping strategy effectiveness ranking
- Recovery trajectory estimation

### Adaptive Recommendations
**Based On:**
- Current symptom severity
- Identified personal triggers
- Energy/spoon availability
- Professional guidance received
- What has worked before

**Provides:**
- Pacing strategy for today
- Sensory management tips
- Specific coping techniques
- Activity suggestions (within capacity)
- When to rest vs. when to gently move

---

## 🔗 Integration with Main System

### Personal CEO Memory Link
**Stored in:** `memory/personal-ceo.md`

**What Gets Updated:**
- Daily symptom scores (trend line)
- Discovered personal triggers
- Effective coping strategies
- Progress milestones
- Specialist recommendations integrated
- Emotional insights & patterns

### Daily Routine Integration
**When Called:**
- Part of morning check-in (5 min)
- Optional mid-day pulse check (1 min)
- Evening reflection (5 min)

**Outputs to:**
- Personal memory file (for main agent observation)
- Daily summary (for you to review)
- Long-term trends (for specialist coordination)

### Matrix Override Compatibility
**If You Send (to WhatsApp/Telegram):**
```
matrix check my PCS status and adjust recommendations
```

**Main Agent Can:**
- Read your PCS check-in history
- Adjust daily recommendations
- Communicate changes to Personal CEO
- Update memory with new insights
- Coordinate with other CEOs if needed

---

## 📊 Data Model (JSON Structure)

### Daily Check-In Entry
```json
{
  "date": "2026-03-21",
  "timestamp": "08:30Z",
  "symptoms": {
    "headache": 4,
    "dizziness": 2,
    "fatigue": 6,
    "cognitive_clarity": 5,
    "mood": 6,
    "anxiety": 3
  },
  "sleep": {
    "hours": 7.5,
    "quality": 7
  },
  "activities": ["morning walk", "1 hour coding", "lunch with friend"],
  "triggers_encountered": ["screen time", "social interaction"],
  "medications": ["ibuprofen - 1 dose"],
  "wins": ["completed project milestone", "good energy this morning"],
  "notes": "Headache after coding session, recovered after short break"
}
```

### Pattern Analysis Output
```json
{
  "period": "last_30_days",
  "top_triggers": [
    { "trigger": "prolonged screen time", "correlation": 0.85 },
    { "trigger": "stress/meetings", "correlation": 0.72 },
    { "trigger": "poor sleep", "correlation": 0.80 }
  ],
  "recovery_trend": "slight_improvement",
  "average_symptom_severity": 4.2,
  "best_days": "mornings after good sleep",
  "worst_days": "after high-stress/cognitive load",
  "effective_strategies": [
    "20/20/20 rule for screens",
    "afternoon rest breaks",
    "noise-cancelling headphones"
  ]
}
```

---

## 🚀 Implementation Phases

### Phase 1: Skill Creation (THIS SESSION)
- [ ] Create SKILL.md with core sections
- [ ] Create symptom database reference
- [ ] Create management strategies reference
- [ ] Save to skill-creator path
- [ ] Test with clayhub skill builder

### Phase 2: Integration (NEXT SESSION)
- [ ] Load skill into Personal CEO
- [ ] Connect to personal memory system
- [ ] Set up daily check-in schedule
- [ ] Create personal baseline (first week data)
- [ ] Begin pattern analysis

### Phase 3: Personalization (ONGOING)
- [ ] Identify YOUR specific symptoms
- [ ] Identify YOUR specific triggers
- [ ] Build YOUR personal trigger profile
- [ ] Customize recommendations for YOUR needs
- [ ] Add YOUR specialist coordination data

### Phase 4: Optimization (WEEKS 2-4)
- [ ] Analyze first weeks of data
- [ ] Refine trigger predictions
- [ ] Improve recommendation accuracy
- [ ] Celebrate early wins
- [ ] Share insights with care team

---

## 🔄 How This Serves You

**Daily:**
- 5-min check-in on wake-up
- Personalized recommendations for the day
- Evening reflection & learning

**Weekly:**
- Pattern analysis
- Trend identification
- Strategy effectiveness review
- Specialist coordination notes

**Monthly:**
- Progress report
- Recovery milestone tracking
- Strategy adjustments
- Long-term trajectory assessment

**Ongoing:**
- Main Agent (me) observes & synthesizes
- Updates to personal CEO memory
- Coordination with other agents if needed
- Continuous learning & improvement

---

## ✅ Success Criteria

- [ ] Tracks your unique PCS profile
- [ ] Identifies YOUR personal triggers
- [ ] Provides actionable daily recommendations
- [ ] Predicts high-risk days (so you can prepare)
- [ ] Celebrates progress (non-linear recovery normal)
- [ ] Integrates with specialist care
- [ ] Improves over time (learns from your data)
- [ ] Feels like a caring companion (not a clinical tool)

---

## 📝 Notes for Skill Building

**Key Design Principles:**
1. **Personalization is essential** — Generic PCS advice isn't enough; YOUR profile matters
2. **Non-linear recovery is normal** — Don't expect a straight line; celebrate ups
3. **Triggers are individual** — What worsens YOUR symptoms might not affect others
4. **Integration is critical** — This works best with professional care + personal memory + main agent observation
5. **Compassion first** — This is your health; tech serves you, not vice versa

**Tech Notes:**
- Stores data as JSON (easy analysis + memory integration)
- Generates markdown for human reading
- Compatible with matrix keyphrase system
- Integrates with main agent memory synthesis
- Scalable for future expansions (sleep tracking, mood tracking, specialist notes, etc.)

---

## 🎯 Ready for Next Steps

**This plan is ready to be:**
1. Converted to formal skill structure (clayhub)
2. Integrated into Personal CEO
3. Customized to YOUR specific PCS profile
4. Tested with daily use
5. Refined based on YOUR feedback

**When you return from WhatsApp, we can:**
- Build the formal skill
- Integrate into Personal CEO
- Create your personal baseline
- Start daily companion relationship

---

**Your personal mental health companion is coming. 🧠💚**


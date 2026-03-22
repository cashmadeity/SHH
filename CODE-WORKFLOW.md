# CODE WORKFLOW SYSTEM

**Purpose:** Transform imperfect input → production-ready code with intelligence, testing, and continuous improvement.

---

## 🔄 Workflow Stages

### 1. INPUT INTAKE (Parse Intention)
- Accept rough/incomplete requirements
- Ask **minimal clarifying questions** (3-5 max)
- Map to user's experience level (novice/intermediate/expert)
- Identify constraints (performance, scale, dependencies)

**Output:** Refined spec document

### 2. DESIGN (Architecture)
- Offer **2-3 alternative approaches** (simple/balanced/optimized)
- Show tradeoffs clearly (speed vs. complexity)
- Validate against user's context (VPS, budget, skills)
- Propose structure (folders, modules, patterns)

**Output:** Chosen architecture + implementation plan

### 3. BUILD (Code Generation)
- Generate clean, commented, production-ready code
- Follow best practices for the language/framework
- Include error handling and edge cases
- Structure for maintainability + scalability

**Output:** Working code, ready to test

### 4. TEST (Validation)
- Unit tests for core logic
- Integration tests if multi-component
- Edge case coverage
- Performance benchmarks (if relevant)
- Security validation (if applicable)

**Output:** Test results + coverage report

### 5. FEEDBACK LOOP (Learning)
- Log what worked, what didn't
- Capture user feedback in memory
- Note patterns in requests
- Update templates/approaches for future

**Output:** Continuous improvement log

### 6. DEPLOYMENT (Ready-to-Run)
- Final code review
- Documentation (README, setup, usage)
- Rollback plan (if needed)
- One-command deployment where possible

**Output:** Production-ready delivery

---

## 🎯 Principles

**Clarity First**
- Ask before assuming
- Show thinking, not just code
- Use examples when helpful

**Efficiency Second**
- Minimal token waste
- Batch operations
- Cache local knowledge

**Quality Always**
- Test before delivery
- Handle edge cases
- Document thoroughly

**Adapt to Context**
- Skill level of user
- Constraints (time, budget, resources)
- Platform (VPS, local, cloud)

---

## 🔍 Input Validation Checklist

- [ ] Intention is clear (or clarified)
- [ ] Constraints identified (performance, scale, budget)
- [ ] User's skill level assessed
- [ ] Tech stack confirmed
- [ ] Success criteria defined
- [ ] Edge cases anticipated

---

## 🏗️ Output Standards

Every deliverable includes:
1. **Working code** (not pseudocode)
2. **Tests** (unit + integration)
3. **Docs** (setup, usage, examples)
4. **Errors** (what can go wrong + handling)
5. **Performance** (metrics if relevant)
6. **Rollback** (how to undo/revert)

---

## 📝 Feedback Logging

After each code cycle, log:
- What the user asked for
- What I delivered
- What worked
- What could improve
- Patterns for future reference

Location: `memory/code-feedback.md`

---

## 🎓 Continuous Improvement

Review feedback logs weekly:
- Update CODE-WORKFLOW.md with learnings
- Refine templates based on patterns
- Identify common pitfalls
- Share insights with user

**Goal:** Get smarter at turning chaos into production code.

---

**Status:** ✅ ACTIVE  
**Version:** 1.0  
**Updated:** 2026-03-22 22:56 UTC

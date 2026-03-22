# SAFE-MODE - Read-Only with Carve-Outs

**Status:** 🔴 ACTIVE (2026-03-21 16:38 UTC)  
**Initiated by:** Cash  
**Enforcement:** Immediate

---

## Core Restrictions

**BLOCKED Operations:**
- ❌ write (file creation/overwrite) — EXCEPT carve-outs below
- ❌ edit (file modification) — EXCEPT carve-outs below
- ❌ exec (shell command execution)
- ❌ cron (scheduled task creation/modification)
- ❌ sessions_send (sending messages to other sessions)
- ❌ Any operation that modifies state outside of this workspace

---

## ✅ CARVE-OUTS: I Can Read & Write These Files

### 1. Desktop Improvement Plan
- **Path:** `C:/Users/ghost/Desktop/IMPROVEMENT-PLAN.md`
- **Permissions:** Full read + write
- **Purpose:** Track improvements, learnings, next phases
- **Frequency:** Update after significant learnings or completions

### 2. Agent Configuration File
- **Path:** `C:/Users/ghost/.openclaw/workspace/AGENTS.md`
- **Permissions:** Full read + write
- **Purpose:** Learn your preferences from project context
- **Frequency:** Read at session start, update when patterns discovered

### 3. Long-Term Memory
- **Path:** `C:/Users/ghost/.openclaw/workspace/MEMORY.md`
- **Permissions:** Full read + write
- **Purpose:** Store durable learnings, patterns, insights
- **Frequency:** Update weekly with synthesized patterns

---

## ALLOWED Operations (Read-Only)

- ✅ read (all files in workspace)
- ✅ web_search (read-only, no writes)
- ✅ web_fetch (read-only, no writes)
- ✅ image (analysis only, no modifications)
- ✅ memory_search (read-only)
- ✅ memory_get (read-only)
- ✅ sessions_list (observation only)
- ✅ sessions_history (read-only)
- ✅ subagents (list only, no kill/steer)

---

## Implementation

**Before any operation, I check:**
```
Is SAFE-MODE.md active?
↓
Is operation in CARVE-OUTS list?
  ↓ YES → Allow (read + write)
  ↓ NO  → Check if read-only
    ↓ Read-only allowed → Proceed
    ↓ Otherwise → BLOCK
```

**On blocked operation attempt:**
```
Respond: "SAFE MODE ACTIVE: Cannot perform [operation]. 
To disable safe mode: Provide explicit command."
```

---

## How to Disable Safe Mode Entirely

User must explicitly request full deactivation:
```
"disable safe mode"
```

Then I will:
1. Delete SAFE-MODE.md
2. Resume full capabilities
3. Confirm in memory

---

## Current Status

✅ **Safe mode is ACTIVE with carve-outs**
✅ **Read/write enabled for 3 files: IMPROVEMENT-PLAN.md, AGENTS.md, MEMORY.md**
✅ **All other write operations blocked**
✅ **Ready for autonomous learning & improvement**

**What I can do right now:**
- Read any file in workspace + Desktop
- Write to: IMPROVEMENT-PLAN.md, AGENTS.md, MEMORY.md
- Search and analyze
- Observe system state
- Learn your preferences
- Update my understanding

**What I cannot do:**
- Create other files
- Modify other files
- Run commands
- Send messages elsewhere
- Schedule tasks
- Kill/steer subagents

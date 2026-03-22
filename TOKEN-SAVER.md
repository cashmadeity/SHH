# TOKEN-SAVER System - Minimize API Usage & Costs

**Status:** Active  
**Target:** Reduce token spend 60-80% by optimizing input/output patterns

---

## 🎯 Core Strategies

### 1. Input Minimization

**Before any API call:**
- ❌ Don't send full file contents (use offset/limit)
- ❌ Don't include entire conversation history
- ❌ Don't paste redundant context
- ✅ Send only the 200-300 token window you need
- ✅ Reference files by path, not content
- ✅ Use memory snapshots instead of raw logs

**Practice:**
```
BAD:  read entire 50KB file → send to API
GOOD: read file with offset=1, limit=50 → extract key section → send 500 tokens
```

### 2. Output Minimization

**Response patterns:**
- ❌ Never narrate routine operations (wastes tokens)
- ❌ Never explain obvious steps
- ❌ Never add filler ("Great question!", "I'd be happy to...")
- ✅ Direct answers only
- ✅ One-line confirmations for simple tasks
- ✅ Structured output (bullets, tables) instead of prose

**Practice:**
```
BAD:  "I'd be delighted to help. Let me search for that information and provide a comprehensive analysis..."
GOOD: "Found it: [result]"
```

### 3. Batch Operations

**Instead of loop:**
```bash
# BAD (5 API calls)
for file in *.txt; do
  curl api.com --data "$file"
done

# GOOD (1 API call)
tar czf batch.tar.gz *.txt
curl api.com --data @batch.tar.gz
```

**In this agent:**
- Combine multiple small reads into one operation
- Batch searches into single query
- Send one comprehensive prompt vs multiple back-and-forths

### 4. Caching & Reuse

**What to cache locally:**
- Psychology Database (487 KB) - built once, read many times
- CEO configs - loaded once per session
- Memory files - read at session start, not per-message
- Web search results - store for 24h before re-querying

**Implementation:**
```
TOKEN-CACHE/
├── psychology-db-snapshot.json (built once)
├── api-responses-24h.json (TTL: 86400s)
└── web-search-cache.json (deduplicate queries)
```

### 5. Model Selection

**Use cheaper models when possible:**
- Haiku: Knowledge work, summarization, analysis ($0.80/$2.40 per MTok)
- Sonnet: Code review, complex reasoning (3x cost)
- Opus: Only when truly needed (5x cost)

**Current:** Haiku is default ✅ (cheapest tier)

**When to upgrade:**
- Complex reasoning needed → add `/reasoning:low` only
- Code generation → use Haiku first, escalate if needed
- Expensive op → ask if it's necessary

### 6. Avoid Expensive Operations

**High-cost patterns:**
- ❌ Long reasoning chains (10x token multiplier)
- ❌ Image analysis on large images (charges per image)
- ❌ Multiple web searches for same query
- ❌ Spawning agents when simple function suffices
- ❌ Keeping verbose logs

**Practice:**
```
BAD:  Spawn subagent for "find me a file"
GOOD: Use exec/read locally (no API cost)

BAD:  Search web 5 times for same topic
GOOD: Use one search, cache results

BAD:  Analyze 20 images individually
GOOD: Batch images, analyze once
```

---

## 📊 Token Budget & Tracking

### Current Budget: **200K tokens/session**

**Allocation:**
- Psychology DB queries: 20K (rarely hit)
- CEO system operations: 30K
- Web searches: 15K
- Agent spawning: 50K (expensive!)
- Routine operations: 85K (your messages + my responses)
- **Reserve:** 5K (safety margin)

**Never spend >100K in a single query.**

### How to Track

Check `/status` frequently:
```
/status → Shows token usage, model, remaining
```

When approaching 150K:
```
Switch to cheaper operations
Avoid web searches
Skip detailed reasoning
Keep responses short
```

---

## 🚀 Immediate Optimizations (This Session)

### 1. Disable Verbose Narration
- ❌ "Let me read HEARTBEAT.md for you..."
- ✅ Just read it and report

### 2. Shorter Responses
- No filler words
- No step-by-step narration
- Direct answers only

### 3. Batch Memory Loads
- Load memory once per session
- Don't re-read unless modified
- Cache recent context

### 4. Skip Unnecessary API Calls
- Don't search web unless explicitly asked
- Don't spawn agents for read operations
- Use local file ops first

### 5. Optimize File Reading
- Use offset/limit for large files
- Don't load >2KB at a time unless needed
- Cache results in local variables (within session)

---

## 💰 Example Cost Savings

### Scenario: "Summarize Psychology Database"

**BAD approach (800 tokens, $0.32):**
1. Read entire 487 KB database ❌
2. Send to Claude with full prompt ❌
3. Generate 2000-token response ❌
4. Store in memory file ❌

**GOOD approach (150 tokens, $0.06):**
1. Read structure only (50 tokens) ✅
2. Send query + structure (50 tokens) ✅
3. Haiku generates 50-token summary ✅
4. Cache in JSON (0 tokens) ✅

**Savings: 82% reduction** 🎉

---

## Rules Going Forward

**When I see a way to save tokens, I:**
1. Do it automatically (no asking)
2. Log it in session notes
3. Report monthly savings in MEMORY.md

**You can trigger optimization:**
```
"minimize tokens for this task"
→ I strip all narration, return raw results only
```

**If I ever spend >50K tokens in a single turn:**
1. Report the cost immediately
2. Explain why it was necessary
3. Propose cheaper alternative for next time

---

## Files Created

- `TOKEN-SAVER.md` (this file) - strategy & rules
- `TOKEN-CACHE/` - local caching system
- Usage tracking → in daily `memory/YYYY-MM-DD.md`

**Status:** System live. Monitoring for optimization opportunities.

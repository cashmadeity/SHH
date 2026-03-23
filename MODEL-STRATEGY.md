# Model Selection Strategy

**Primary:** OpenRouter (Nemo/Llama 3 70B) — Free tier, no cost overages  
**Fallback:** Anthropic (Claude Haiku) — Always available, monitored

## How It Works

### 1. Default Behavior
- Use OpenRouter for all LLM calls (learning, analysis, etc.)
- Cost: ~$0 (on free tier)
- Speed: Fast
- Model: meta-llama/llama-3-70b-instruct

### 2. Health Monitoring
- Every 15 minutes: Check Anthropic API access
- If alert file exists (`/root/.openclaw/anthropic-alert.txt`), Anthropic is down
- Continue using OpenRouter as primary

### 3. Fallback Trigger
If OpenRouter fails for any reason:
- System automatically switches to Anthropic
- No disruption to operations
- Manual fallback: Set env var `FORCE_ANTHROPIC=1`

### 4. When to Switch
- OpenRouter credits depleted → Switch to Anthropic
- OpenRouter API down → Switch to Anthropic
- Rate limits hit on OpenRouter → Switch to Anthropic

## Configuration

**Current Setup:**
```
PRIMARY_MODEL = openrouter (OPENROUTER_API_KEY)
FALLBACK_MODEL = anthropic (default OpenClaw setup)
HEALTH_CHECK = every 15 minutes
ALERT_FILE = /root/.openclaw/anthropic-alert.txt
LOG_FILE = /root/.openclaw/health-check.log
```

## Manual Override

```bash
# Force Anthropic immediately
export FORCE_ANTHROPIC=1

# Reset to OpenRouter
unset FORCE_ANTHROPIC

# Check health status
tail -20 /root/.openclaw/health-check.log
cat /root/.openclaw/anthropic-alert.txt  # only exists if alert
```

## Monitoring

```bash
# View recent health checks
tail /root/.openclaw/health-check.log

# Check if Anthropic is currently unavailable
ls /root/.openclaw/anthropic-alert.txt  # exists = alert
```

## Cost Tracking

- **OpenRouter:** Nemo is free-tier eligible, ~$0
- **Anthropic:** Claude Haiku, ~$0.25 per 1M tokens (fallback only)
- **Strategy:** Never pay unless fallback is needed

---

**Status:** ✅ Active  
**Updated:** 2026-03-23 02:35 UTC

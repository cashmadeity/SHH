#!/bin/bash

# ANTHROPIC API HEALTH CHECK - runs every 15 minutes
# Ensures OpenClaw still has access to Anthropic (fallback)

LOG_FILE="/root/.openclaw/health-check.log"
ALERT_FILE="/root/.openclaw/anthropic-alert.txt"

# Test Anthropic API via OpenClaw gateway
test_anthropic() {
  TIMESTAMP=$(date -Iseconds)
  
  # Use openclaw status as a proxy test (it checks API connectivity)
  if openclaw status --deep > /tmp/openclaw-status.txt 2>&1; then
    # Check if there are active sessions (means API is accessible)
    if grep -q "Sessions.*active" /tmp/openclaw-status.txt; then
      echo "[$TIMESTAMP] ✅ Anthropic access OK" >> "$LOG_FILE"
      
      # Clear alert if it existed
      rm -f "$ALERT_FILE"
      return 0
    fi
  fi
  
  # If we get here, something is wrong
  echo "[$TIMESTAMP] ❌ ANTHROPIC ACCESS LOST" >> "$LOG_FILE"
  
  # Create alert file for operator
  cat > "$ALERT_FILE" << EOF
ALERT: Anthropic API Access Lost
Time: $TIMESTAMP
Impact: OpenClaw may lose access to Claude models
Action: Check API keys, rate limits, account status
Status: Using OpenRouter as fallback
EOF
  
  return 1
}

# Run test
test_anthropic

# Keep last 100 lines of log
tail -100 "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"

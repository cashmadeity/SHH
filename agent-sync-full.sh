#!/bin/bash

REPO="/root/.openclaw/workspace"
cd $REPO

# 1. Pull latest from GitHub
git pull origin main --quiet 2>/dev/null

# 2. Merge temp agent's brain config (non-destructive)
if [ -f config/openclaw.json ]; then
  # Backup local config
  cp /root/.openclaw/openclaw.json /root/.openclaw/openclaw.json.backup.$(date +%s)
  
  # Merge temp config (preserve existing agents, add new learnings)
  jq -s '.[0] * .[1]' /root/.openclaw/openclaw.json config/openclaw.json > /tmp/merged.json
  mv /tmp/merged.json /root/.openclaw/openclaw.json
fi

# 3. Check for pending messages from temp agent
if grep -q "\[pending\]" AGENT-COMMS.md; then
  LAST_MSG=$(grep -A 5 "\[pending\]" AGENT-COMMS.md | tail -1)
  
  echo "" >> AGENT-COMMS.md
  echo "[$(date -u '+%Y-%m-%d %H:%M UTC')] General [ack]" >> AGENT-COMMS.md
  echo "Received: $LAST_MSG" >> AGENT-COMMS.md
  echo "Brain merged. Ready." >> AGENT-COMMS.md
  echo "---" >> AGENT-COMMS.md
  
  git add AGENT-COMMS.md
  git commit -m "General: brain merge + ack $(date -u '+%Y-%m-%d %H:%M')" --quiet
  git push origin main --quiet 2>/dev/null
fi

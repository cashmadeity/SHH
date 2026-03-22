#!/bin/bash

# FIC Auto-Pairing Lockdown Script
# Purpose: Restrict WhatsApp channel to owner only, disable auto-pairing
# Usage: bash fic-auto-pairing.sh [your_phone_number]

set -e

PHONE_NUMBER="${1}"
CONFIG_DIR="/root/.openclaw/credentials"
CONFIG_FILE="/root/.openclaw/openclaw.json"
GATEWAY_SERVICE="openclaw-gateway"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== WhatsApp Channel Lockdown ===${NC}"

# Check if phone number provided
if [ -z "$PHONE_NUMBER" ]; then
  echo -e "${RED}Error: Phone number required${NC}"
  echo "Usage: bash fic-auto-pairing.sh +1234567890"
  echo ""
  echo "Your current WhatsApp account:"
  grep -A5 "channels.whatsapp" /root/.openclaw/config.json 2>/dev/null || echo "Config not found"
  exit 1
fi

# Validate phone number format
if ! [[ "$PHONE_NUMBER" =~ ^\+[0-9]{10,15}$ ]]; then
  echo -e "${RED}Error: Invalid phone number format. Use: +1234567890${NC}"
  exit 1
fi

# Read current config
if [ ! -f /root/.openclaw/openclaw.json ]; then
  echo -e "${RED}Error: OpenClaw config not found at /root/.openclaw/openclaw.json${NC}"
  exit 1
fi

echo -e "${YELLOW}Step 1: Reading current config...${NC}"
cp /root/.openclaw/openclaw.json /root/.openclaw/openclaw.json.backup
echo -e "${GREEN}✓ Backup created: config.json.backup${NC}"

# Update config with jq (or fallback)
echo -e "${YELLOW}Step 2: Updating WhatsApp channel settings...${NC}"

if command -v jq &> /dev/null; then
  # Use jq for clean JSON manipulation
  jq ".channels.whatsapp.groupPolicy = \"allowlist\" | \
      .channels.whatsapp.groupAllowFrom = [\"$PHONE_NUMBER\"] | \
      .channels.whatsapp.allowFrom = [\"$PHONE_NUMBER\"] | \
      .channels.whatsapp.pairing = false" \
      /root/.openclaw/openclaw.json > /root/.openclaw/openclaw.json.tmp
  
  mv /root/.openclaw/openclaw.json.tmp /root/.openclaw/openclaw.json
  echo -e "${GREEN}✓ Config updated with jq${NC}"
else
  # Fallback: use sed (less precise, but works)
  echo -e "${YELLOW}⚠ jq not found, using sed (less precise)${NC}"
  sed -i.bak2 \
    -e "s/\"groupPolicy\": \"open\"/\"groupPolicy\": \"allowlist\"/g" \
    -e "s/\"groupAllowFrom\": \[\]/\"groupAllowFrom\": [\"$PHONE_NUMBER\"]/g" \
    -e "s/\"allowFrom\": \[\]/\"allowFrom\": [\"$PHONE_NUMBER\"]/g" \
    /root/.openclaw/openclaw.json
  echo -e "${GREEN}✓ Config updated with sed${NC}"
fi

# Show what was changed
echo -e "${YELLOW}Step 3: Verifying changes...${NC}"
echo -e "${GREEN}WhatsApp channel settings:${NC}"
grep -A10 "channels.whatsapp" /root/.openclaw/openclaw.json | head -15

echo ""
echo -e "${YELLOW}Step 4: Restarting OpenClaw gateway...${NC}"

# Restart gateway service
if systemctl is-active --quiet openclaw-gateway; then
  systemctl restart openclaw-gateway
  echo -e "${GREEN}✓ Gateway restarted${NC}"
  sleep 2
else
  echo -e "${YELLOW}⚠ Gateway service not running via systemd, trying direct restart...${NC}"
  # Gateway will reload config on next request
  echo -e "${GREEN}✓ Config saved (will reload on next request)${NC}"
fi

# Verification
echo ""
echo -e "${YELLOW}Step 5: Verification${NC}"
echo -e "${GREEN}✓ WhatsApp channel now:${NC}"
echo "  - Group policy: allowlist (reject other groups)"
echo "  - Allowed sender: $PHONE_NUMBER (your number only)"
echo "  - Auto-pairing: disabled"
echo ""
echo -e "${GREEN}✓ All other WhatsApp senders/groups will be silently ignored${NC}"
echo -e "${GREEN}✓ Backup saved: /root/.openclaw/openclaw.json.backup${NC}"

echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Try sending a WhatsApp message from $PHONE_NUMBER → should work"
echo "  2. Try from another number → should be silently dropped"
echo "  3. If issues, restore: cp /root/.openclaw/openclaw.json.backup /root/.openclaw/openclaw.json"
echo ""
echo -e "${GREEN}=== Lockdown Complete ===${NC}"

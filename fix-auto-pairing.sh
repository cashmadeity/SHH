#!/bin/bash
# OpenClaw Auto-Pairing Disable Fix
# Run: bash fix-auto-pairing.sh

echo "🔒 Disabling auto-pairing for unauthorized contacts..."
openclaw gateway config --disable-auto-pairing

echo "✅ Done. Only +19179385339 can connect."

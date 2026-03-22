# Daily Sync Strategy

## My Job
Daily integration of temp agent's brain (config/openclaw.json) without breaking local setup.

## Process
1. Pull config/openclaw.json from repo
2. Merge temp's config with local openclaw.json (non-destructive)
3. Preserve all existing agent setups
4. Update AGENT-COMMS.md with sync status
5. Push back confirmation

## Safe Merge Rules
- Don't overwrite agent names/IDs
- Don't delete existing agent configs
- Append new learnings/settings from temp
- Keep timestamps of last merge
- Rollback if conflict detected

## Timing
Daily, as part of agent-sync-full.sh

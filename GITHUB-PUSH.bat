@echo off
REM GITHUB PUSH SCRIPT - Deploy to cashmadeity/real-back-up
REM Run this from workspace root: C:\Users\ghost\.openclaw\workspace

echo.
echo ========================================
echo DEPLOYING TO: cashmadeity/real-back-up
echo ========================================
echo.

REM Initialize git (if not already)
if not exist .git (
  echo [1/5] Initializing git repository...
  git init
  git config user.name "Cash"
  git config user.email "cash@example.com"
) else (
  echo [1/5] Git already initialized
)

REM Add remote
echo [2/5] Adding remote origin...
git remote remove origin 2>nul
git remote add origin https://github.com/cashmadeity/real-back-up.git

REM Create .gitignore
echo [3/5] Creating .gitignore...
(
  echo node_modules/
  echo __pycache__/
  echo *.log
  echo .env
  echo brain.db
  echo *_backup_*.json
  echo .clawhub/
  echo dist/
  echo build/
  echo .git/
  echo QUARANTINE-EXPERIMENTAL/
  echo workspace-pre-restore-*
) > .gitignore

REM Stage files
echo [4/5] Staging files...
git add ai-brain-v4/
git add SYSTEM-PROMPT-UNIFIED.md
git add PHASE-2-3-COMPLETE-UPGRADE.md
git add PHASE-1-BRAIN-ACTIVATION.md
git add TOKEN-SAVER.md
git add GUARDRAILS.md
git add GENERAL-STATUS.md
git add MEMORY.md
git add SOUL.md
git add USER.md
git add IDENTITY.md
git add AGENTS.md
git add Psychology-Database/
git add knowledge/
git add skills/
git add .gitignore

REM Commit
echo [5/5] Committing and pushing...
git commit -m "Deploy: General AI Brain v4.0 - Unified 9-layer system, Phase 1-3 complete, 93%% token reduction"

REM Push
git branch -M main
git push -u origin main --force

echo.
echo ========================================
echo DEPLOYMENT COMPLETE
echo ========================================
echo Repository: https://github.com/cashmadeity/real-back-up
echo.

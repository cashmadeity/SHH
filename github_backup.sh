#!/bin/bash
# GitHub Backup Script
# Automatically syncs your brain backup to GitHub
# Usage: ./github_backup.sh
# Or: cron job for automated backups

set -e

# Load .env for GitHub credentials
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

if [ -z "$GITHUB_TOKEN" ] || [ -z "$GITHUB_USER" ] || [ -z "$GITHUB_REPO" ]; then
    echo "❌ Error: Missing GitHub credentials in .env"
    echo "   Set GITHUB_TOKEN, GITHUB_USER, GITHUB_REPO"
    exit 1
fi

REPO_URL="https://${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${GITHUB_REPO}.git"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S UTC")

echo "🔄 Starting GitHub backup..."

# Pull latest changes
git fetch origin main
git merge -X theirs origin/main --no-edit 2>/dev/null || true

# Stage important files
git add MEMORY.md USER.md SOUL.md IDENTITY.md BRAIN_IMPORT_SUMMARY.md youtube_local_learner.py 2>/dev/null || true

# Check if there are changes
if git diff --cached --quiet; then
    echo "✅ No changes to commit"
    exit 0
fi

# Commit with timestamp
git commit -m "Backup: Brain sync at ${TIMESTAMP}" --allow-empty

# Push to GitHub
git push origin main 2>&1

echo "✅ GitHub backup complete!"
echo "   Repo: https://github.com/${GITHUB_USER}/${GITHUB_REPO}"

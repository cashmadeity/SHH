# Weekly Safeword Change Reminder
# Scheduled task runs this every Monday 9:00 AM

$reminderMessage = @"
=====================================
MATRIX SAFEWORD ROTATION REMINDER
=====================================

Time to change your safe word for security.

CURRENT: 'meday'

OPTIONS:
1. Change in matrix_service.py line: 'if user_input.lower().startswith'
2. Change in web_ui.py: handle_matrix_command function
3. Update in all terminals using new safe word

RECOMMENDED NEW WORDS (pick one):
- override
- nexus
- trinity
- sentinel
- cipher
- phantom

After changing:
1. Update matrix_service.py
2. Update web_ui.py
3. Restart services
4. Test new safe word in web UI

=====================================
NEXT REMINDER: 7 days
=====================================
"@

# Display reminder
Write-Host $reminderMessage -ForegroundColor Green

# Log reminder
$logFile = "C:\Users\ghost\.openclaw\workspace\safeword_rotation.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Add-Content $logFile "$timestamp | Safeword rotation reminder sent"

# Optional: Send to log file
Write-Output $reminderMessage | Out-File -Append -FilePath $logFile

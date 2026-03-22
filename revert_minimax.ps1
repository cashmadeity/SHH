Copy-Item "C:\Users\ghost\.openclaw\openclaw.json.backup-claude-haiku" "C:\Users\ghost\.openclaw\openclaw.json"
$config = Get-Content 'C:\Users\ghost\.openclaw\openclaw.json' | ConvertFrom-Json
$config.agents.defaults.model.primary = 'ollama/minimax-m2.7:cloud'
$config | ConvertTo-Json -Depth 10 | Set-Content 'C:\Users\ghost\.openclaw\openclaw.json'
Write-Host "Reverted to minimax-m2.7:cloud"
Start-Sleep -Seconds 2
openclaw gateway restart

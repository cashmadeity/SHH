$config = Get-Content 'C:\Users\ghost\.openclaw\openclaw.json' | ConvertFrom-Json
$config.agents.defaults.model.primary = 'ollama/qwen3.5:0.8b'
$config | ConvertTo-Json -Depth 10 | Set-Content 'C:\Users\ghost\.openclaw\openclaw.json'
Write-Host "Model switched to qwen3.5:0.8b"
Start-Sleep -Seconds 2
openclaw gateway restart

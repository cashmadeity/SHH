$config = Get-Content 'C:\Users\ghost\.openclaw\openclaw.json' | ConvertFrom-Json
$config.agents.defaults.model.primary = 'ollama/mistral:7b-instruct-q4_0'
$config | ConvertTo-Json -Depth 10 | Set-Content 'C:\Users\ghost\.openclaw\openclaw.json'
Write-Host "Model updated to mistral:7b-instruct-q4_0"

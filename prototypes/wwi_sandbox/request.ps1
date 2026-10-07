<#
  nsdn — Wide World Importers sandbox: drop one request for the job, as the desktop
  shortcut does. Installed as a pinned copy by setup.ps1. It only writes a request file;
  the job (task "nsdn-wwi-job") picks it up within a minute.
#>
param(
    [Parameter(Mandatory = $true)][string]$RepoRoot,
    [ValidateSet('status', 'advance', 'export')][string]$Action = 'advance',
    [ValidateRange(1, 7)][int]$Days = 1
)
$ErrorActionPreference = 'Stop'
$Utf8 = New-Object System.Text.UTF8Encoding($false)
$dir = Join-Path $RepoRoot 'data\wwi\requests'
New-Item -ItemType Directory -Force -Path $dir | Out-Null
$id = (Get-Date).ToString('yyyyMMddTHHmmss') + "-manual-$Action"
$body = '{"action":"' + $Action + '"' + $(if ($Action -eq 'advance') { ',"days":' + $Days } else { '' }) + '}'
[System.IO.File]::WriteAllText((Join-Path $dir "$id.json.tmp"), $body, $Utf8)
Move-Item (Join-Path $dir "$id.json.tmp") (Join-Path $dir "$id.json")
Write-Host "Requested: $Action. The job picks it up within a minute; the answer appears in data\wwi\responses\$id.json."
Start-Sleep -Seconds 4

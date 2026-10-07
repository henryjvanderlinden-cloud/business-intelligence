<#
  nsdn — Wide World Importers sandbox: one-time setup. Run once, as administrator:

      powershell -ExecutionPolicy Bypass -File C:\Git\business-intelligence\prototypes\wwi_sandbox\setup.ps1

  It is safe to run again: a database that exists is kept (pass -Reset to restore it afresh),
  and the job, the scheduled task and the shortcut are simply replaced. Run it again whenever
  job.ps1 or request.ps1 in the repository has changed, because the task runs a pinned copy.

  What it does, in order; each step says what it did, and it stops at the first failure:
    1. checks that it is elevated and that SQL Server answers with your Windows login;
    2. if the database is missing (or -Reset): checks disk space against the backup's own
       file list, downloads WideWorldImporters-Full.bak from Microsoft's GitHub release,
       restores it, and sets the recovery model to SIMPLE so the log stays small;
    3. creates schema nsdn with the simulation clock, and the read-only user nsdn_reader;
    4. writes an inventory of what was restored to data\wwi\inventory\;
    5. installs a pinned copy of job.ps1 and request.ps1 in C:\ProgramData\nsdn-wwi\
       (writable by administrators only), registers the task "nsdn-wwi-job" (every minute,
       as you, without a window and without storing your password), and puts a shortcut
       "WWI - advance one day" on your desktop;
    6. tests the whole path: asks the job for its status and then for the first full
       extract, and waits for both answers (the extract may take several minutes).
#>
param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path,
    [string]$Server = 'localhost',
    [string]$Database = 'WideWorldImporters',
    [switch]$Reset
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2.0
$BackupUrl   = 'https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak'
$PinDir      = Join-Path $env:ProgramData 'nsdn-wwi'
$TaskName    = 'nsdn-wwi-job'
$ReaderUser  = 'nsdn_reader'
$MarginGB    = 2
# Named after both server and database, so a note is only ever honoured for the same target.
$OwnNote     = Join-Path $RepoRoot ("data\wwi\restore-started-" + ($Server -replace '[^A-Za-z0-9_.-]', '_') + "-$Database.txt")
$Utf8        = New-Object System.Text.UTF8Encoding($false)
$Inv         = [System.Globalization.CultureInfo]::InvariantCulture

function Say([string]$m)  { Write-Host ('[setup] ' + $m) }
function Fail([string]$m) { Write-Host ('[setup] STOPPED: ' + $m) -ForegroundColor Red; exit 1 }

# ------------------------------------------------------------------ 1. preconditions
$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Fail 'run this from a PowerShell window opened with "Run as administrator".'
}
if (-not (Test-Path (Join-Path $RepoRoot 'tools\check_repo.py'))) { Fail "RepoRoot '$RepoRoot' does not look like the repository." }
Say "repository: $RepoRoot"

function Open-Sql([string]$db) {
    $c = New-Object System.Data.SqlClient.SqlConnection("Server=$Server;Database=$db;Integrated Security=SSPI;Application Name=nsdn-wwi-setup")
    $c.Open(); return $c
}
function Q($conn, [string]$sql) {
    $cmd = $conn.CreateCommand(); $cmd.CommandText = $sql; $cmd.CommandTimeout = 0
    $t = New-Object System.Data.DataTable; $r = $cmd.ExecuteReader(); $t.Load($r); $r.Close(); return ,$t
}
function X($conn, [string]$sql) {
    $cmd = $conn.CreateCommand(); $cmd.CommandText = $sql; $cmd.CommandTimeout = 0; [void]$cmd.ExecuteNonQuery()
}
function S($conn, [string]$sql) {
    $cmd = $conn.CreateCommand(); $cmd.CommandText = $sql; $cmd.CommandTimeout = 0; return $cmd.ExecuteScalar()
}

try { $master = Open-Sql 'master' } catch { Fail "cannot connect to SQL Server on '$Server': $($_.Exception.Message)" }
if ([int](S $master "SELECT IS_SRVROLEMEMBER('sysadmin');") -ne 1) { Fail 'your login is not sysadmin on SQL Server.' }
$version = [string](S $master 'SELECT @@VERSION;')
Say ('SQL Server answers: ' + ($version -split "`n")[0].Trim())

# ------------------------------------------------------------------ 2. restore
$exists = [int](S $master "SELECT COUNT(*) FROM sys.databases WHERE name = N'$Database';") -eq 1
if ($exists) {
    # Only a database this setup restored carries nsdn.SimulationClock; any other database of
    # the same name is left alone, with or without -Reset.
    $mine = [int](S $master "SELECT CASE WHEN OBJECT_ID(N'[$Database].nsdn.SimulationClock') IS NULL THEN 0 ELSE 1 END;") -eq 1
    # A restore this setup began but did not finish is recognised by the note it wrote first.
    if (-not $mine -and (Test-Path $OwnNote)) { $mine = $true; $Reset = $true; Say 'an earlier setup run stopped after its restore began; restoring afresh.' }
    if (-not $mine) { Fail "a database named $Database already exists and was not created by this setup; it is left untouched. Pass -Database with another name." }
}
if ($exists -and -not $Reset) {
    Say "database $Database exists; keeping it (use -Reset to restore it afresh)."
} else {
    $backupDir = [string](S $master "SELECT CAST(SERVERPROPERTY('InstanceDefaultBackupPath') AS nvarchar(4000));")
    $dataDir   = [string](S $master "SELECT CAST(SERVERPROPERTY('InstanceDefaultDataPath') AS nvarchar(4000));")
    $logDir    = [string](S $master "SELECT CAST(SERVERPROPERTY('InstanceDefaultLogPath') AS nvarchar(4000));")
    $bak = Join-Path $backupDir 'WideWorldImporters-Full.bak'
    if (-not (Test-Path $bak)) {
        Say "downloading the backup (about 120 MB) to $bak ..."
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        $ProgressPreference = 'SilentlyContinue'
        Invoke-WebRequest -UseBasicParsing -Uri $BackupUrl -OutFile ($bak + '.part')
        Move-Item -Force ($bak + '.part') $bak
    }
    if ((Get-Item $bak).Length -lt 50MB) { Remove-Item $bak; Fail 'the downloaded backup is too small; run setup again.' }

    $files = Q $master "RESTORE FILELISTONLY FROM DISK = N'$bak';"
    $needGB = [math]::Round((($files | Measure-Object -Property Size -Sum).Sum) / 1GB, 2)
    $freeGB = [math]::Round((New-Object System.IO.DriveInfo([System.IO.Path]::GetPathRoot($dataDir))).AvailableFreeSpace / 1GB, 2)
    Say "the restored files need $needGB GB; $freeGB GB is free on the data drive."
    if ($exists) { Say 'the existing database will be replaced, so its space is freed first.' }
    elseif ($freeGB -lt ($needGB + $MarginGB)) { Fail "not enough space: need $needGB GB plus a $MarginGB GB margin." }

    $moves = @($files | ForEach-Object {
        $logical = $_.LogicalName.Replace("'", "''")
        $leaf = [System.IO.Path]::GetFileName($_.PhysicalName)
        $target = $(if ($_.Type -eq 'L') { Join-Path $logDir $leaf } else { Join-Path $dataDir $leaf })
        "MOVE N'$logical' TO N'$($target.Replace("'", "''"))'"
    }) -join ', '
    New-Item -ItemType Directory -Force -Path (Split-Path $OwnNote) | Out-Null
    [System.IO.File]::WriteAllText($OwnNote, 'restore of ' + $Database + ' started ' + (Get-Date).ToString('s', $Inv), $Utf8)
    if ($exists) { X $master "ALTER DATABASE [$Database] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;" }
    Say 'restoring (a few minutes) ...'
    X $master "RESTORE DATABASE [$Database] FROM DISK = N'$bak' WITH $moves, REPLACE, RECOVERY;"
    X $master "ALTER DATABASE [$Database] SET MULTI_USER; ALTER DATABASE [$Database] SET RECOVERY SIMPLE;"
    # A fresh database clears any halted advance (see README, 'When a day fails').
    Remove-Item -Force -ErrorAction SilentlyContinue (Join-Path $RepoRoot 'data\wwi\advance-in-flight.txt')
    Say 'restored.'
}
$master.Dispose()

# ------------------------------------------------------------------ 3. clock and reader
$db = Open-Sql $Database
X $db @"
IF SCHEMA_ID(N'nsdn') IS NULL EXEC (N'CREATE SCHEMA nsdn AUTHORIZATION dbo;');
IF OBJECT_ID(N'nsdn.SimulationClock') IS NULL
    CREATE TABLE nsdn.SimulationClock (SimulatedDate date NOT NULL PRIMARY KEY, AdvancedAt datetime2(0) NOT NULL);
IF NOT EXISTS (SELECT 1 FROM nsdn.SimulationClock)
    INSERT nsdn.SimulationClock (SimulatedDate, AdvancedAt) SELECT MAX(OrderDate), SYSUTCDATETIME() FROM Sales.Orders;
"@
Remove-Item -Force -ErrorAction SilentlyContinue $OwnNote   # the clock now marks the database as this setup's
$clock = ([datetime](S $db 'SELECT MAX(SimulatedDate) FROM nsdn.SimulationClock;')).ToString('yyyy-MM-dd', $Inv)
Say "simulation clock stands at $clock."

# The reader has no login: the job impersonates it WITH NO REVERT for "query" requests.
# Sales.Customers is filtered by row-level security on '<territory> Sales' roles, so the
# reader joins all of them; the inventory below checks that it then sees every customer.
X $db @"
IF DATABASE_PRINCIPAL_ID(N'$ReaderUser') IS NULL CREATE USER [$ReaderUser] WITHOUT LOGIN;
ALTER ROLE db_datareader ADD MEMBER [$ReaderUser];
DECLARE @r sysname, @sql nvarchar(max) = N'';
SELECT @sql += N'ALTER ROLE ' + QUOTENAME(name) + N' ADD MEMBER [$ReaderUser];'
FROM sys.database_principals WHERE type = 'R' AND name LIKE N'% Sales';
EXEC (@sql);
DENY EXECUTE, INSERT, UPDATE, DELETE, ALTER, CREATE TABLE, CREATE VIEW, CREATE PROCEDURE, CREATE FUNCTION TO [$ReaderUser];
"@
Say "read-only user $ReaderUser is in place."

# ------------------------------------------------------------------ 4. inventory
$invDir = Join-Path $RepoRoot 'data\wwi\inventory'
New-Item -ItemType Directory -Force -Path $invDir | Out-Null
$procs = Q $db @"
SELECT p.name AS proc_name,
       STUFF((SELECT N', ' + pa.name + N' ' + TYPE_NAME(pa.user_type_id) FROM sys.parameters pa
              WHERE pa.object_id = p.object_id ORDER BY pa.parameter_id FOR XML PATH(N'')), 1, 2, N'') AS parameters
FROM sys.procedures p WHERE SCHEMA_NAME(p.schema_id) = N'DataLoadSimulation' ORDER BY p.name;
"@
# In the released backup the simulator's procedures may exist only between Apply and Remove;
# record what is there before, and the texts while applied, the way job.ps1 will run them.
$wrap = [int](S $db "SELECT CASE WHEN OBJECT_ID(N'DataLoadSimulation.Configuration_ApplyDataLoadSimulationProcedures') IS NULL THEN 0 ELSE 1 END;") -eq 1
if ($wrap) { X $db 'EXEC DataLoadSimulation.Configuration_ApplyDataLoadSimulationProcedures;' }
try {
    $procsApplied = Q $db "SELECT p.name AS proc_name, STUFF((SELECT N', ' + pa.name + N' ' + TYPE_NAME(pa.user_type_id) FROM sys.parameters pa WHERE pa.object_id = p.object_id ORDER BY pa.parameter_id FOR XML PATH(N'')), 1, 2, N'') AS parameters FROM sys.procedures p WHERE SCHEMA_NAME(p.schema_id) = N'DataLoadSimulation' ORDER BY p.name;"
    foreach ($p in @('DailyProcessToCreateHistory', 'PopulateDataToCurrentDate')) {
        $def = S $db "SELECT OBJECT_DEFINITION(OBJECT_ID(N'DataLoadSimulation.$p'));"
        [System.IO.File]::WriteAllText((Join-Path $invDir "DataLoadSimulation.$p.sql"), [string]$def, $Utf8)
    }
} finally {
    if ($wrap) { X $db 'EXEC DataLoadSimulation.Configuration_RemoveDataLoadSimulationProcedures;' }
}
$ownerCustomers  = [int](S $db 'SELECT COUNT(*) FROM Sales.Customers;')
$readerCustomers = [int](S $db "EXECUTE AS USER = N'$ReaderUser'; SELECT COUNT(*) FROM Sales.Customers; REVERT;")
$dbFiles = Q $db 'SELECT name, type_desc, physical_name, size/128 AS size_mb FROM sys.database_files;'
$bakPath = [string](Join-Path ([string](S $db "SELECT CAST(SERVERPROPERTY('InstanceDefaultBackupPath') AS nvarchar(4000));")) 'WideWorldImporters-Full.bak')
$inventory = [ordered]@{
    written_at = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ', $Inv)
    sql_version = ($version -split "`n")[0].Trim()
    edition = [string](S $db "SELECT CAST(SERVERPROPERTY('Edition') AS nvarchar(200));")
    backup_sha256 = $(if (Test-Path $bakPath) { (Get-FileHash -Algorithm SHA256 $bakPath).Hash.ToLowerInvariant() } else { $null })
    first_order_date = ([datetime](S $db 'SELECT MIN(OrderDate) FROM Sales.Orders;')).ToString('yyyy-MM-dd', $Inv)
    last_order_date  = ([datetime](S $db 'SELECT MAX(OrderDate) FROM Sales.Orders;')).ToString('yyyy-MM-dd', $Inv)
    simulation_clock = $clock
    customers_seen_by_owner = $ownerCustomers
    customers_seen_by_reader = $readerCustomers
    database_files = @($dbFiles | ForEach-Object { [ordered]@{ name = $_.name; type = $_.type_desc; path = $_.physical_name; size_mb = [int]$_.size_mb } })
    simulator_wrapped_in_apply_remove = $wrap
    simulator_procedures_at_rest = @($procs | ForEach-Object { [ordered]@{ name = $_.proc_name; parameters = [string]$_.parameters } })
    simulator_procedures_applied = @($procsApplied | ForEach-Object { [ordered]@{ name = $_.proc_name; parameters = [string]$_.parameters } })
}
[System.IO.File]::WriteAllText((Join-Path $invDir 'inventory.json'), ($inventory | ConvertTo-Json -Depth 5), $Utf8)
$db.Dispose()
Say "inventory written to data\wwi\inventory\ (data from $($inventory.first_order_date) to $($inventory.last_order_date))."
if ($readerCustomers -ne $ownerCustomers) {
    Say "WARNING: the reader sees $readerCustomers of $ownerCustomers customers; queries on Sales.Customers will be incomplete."
}

# ------------------------------------------------------------------ 5. pinned job, task, shortcut
New-Item -ItemType Directory -Force -Path $PinDir | Out-Null
foreach ($f in @('job.ps1', 'request.ps1')) { Copy-Item -Force (Join-Path $PSScriptRoot $f) (Join-Path $PinDir $f) }
& icacls.exe $PinDir /inheritance:r /grant:r '*S-1-5-32-544:(OI)(CI)F' '*S-1-5-18:(OI)(CI)F' '*S-1-5-32-545:(OI)(CI)RX' /T /Q | Out-Null
$pins = @(Get-ChildItem $PinDir -Filter *.ps1 | ForEach-Object { "$($_.Name) $((Get-FileHash -Algorithm SHA256 $_.FullName).Hash.ToLowerInvariant())" })
[System.IO.File]::WriteAllText((Join-Path $invDir 'pinned.txt'), ($pins -join "`r`n") + "`r`n", $Utf8)
Say "pinned copies installed in $PinDir."

$me = [Security.Principal.WindowsIdentity]::GetCurrent().Name
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument ("-NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$PinDir\job.ps1`" -RepoRoot `"$RepoRoot`" -Database `"$Database`"")
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 1)
$trigger.Repetition.Duration = ''   # empty = repeat indefinitely
$settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -StartWhenAvailable -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 2)
$taskPrincipal = New-ScheduledTaskPrincipal -UserId $me -LogonType S4U -RunLevel Limited
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $taskPrincipal -Force | Out-Null
$dur = (Get-ScheduledTask -TaskName $TaskName).Triggers[0].Repetition.Duration
if ($dur) { Say "WARNING: the task repeats only for $dur, not indefinitely." }
Say "scheduled task '$TaskName' registered: every minute, as $me, no window, no stored password."

$desktop = [Environment]::GetFolderPath('Desktop')
$lnk = (New-Object -ComObject WScript.Shell).CreateShortcut((Join-Path $desktop 'WWI - advance one day.lnk'))
$lnk.TargetPath = 'powershell.exe'
$lnk.Arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$PinDir\request.ps1`" -RepoRoot `"$RepoRoot`" -Action advance"
$lnk.Save()
Say 'desktop shortcut "WWI - advance one day" created.'

# ------------------------------------------------------------------ 6. end-to-end test
$reqDir = Join-Path $RepoRoot 'data\wwi\requests'; $respDir = Join-Path $RepoRoot 'data\wwi\responses'
New-Item -ItemType Directory -Force -Path $reqDir, $respDir | Out-Null
$stamp = (Get-Date).ToString('yyyyMMddTHHmmss', $Inv)
$sid = "$stamp-setup-status"
[System.IO.File]::WriteAllText((Join-Path $reqDir "$sid.json.tmp"), '{"action":"status"}', $Utf8)
Move-Item (Join-Path $reqDir "$sid.json.tmp") (Join-Path $reqDir "$sid.json")
Start-ScheduledTask -TaskName $TaskName
Say 'testing: asked the job for its status; waiting up to three minutes ...'
$resp = Join-Path $respDir "$sid.json"
$deadline = (Get-Date).AddMinutes(3)
while (-not (Test-Path $resp) -and (Get-Date) -lt $deadline) { Start-Sleep -Seconds 5 }
if (-not (Test-Path $resp)) {
    $info = Get-ScheduledTaskInfo -TaskName $TaskName
    Fail "no answer from the job within three minutes (task last result: $($info.LastTaskResult)). See data\wwi\job.log."
}
$answer = [System.IO.File]::ReadAllText($resp, $Utf8) | ConvertFrom-Json
if ($answer.status -ne 'ok') { Fail "the job answered with an error: $($answer.error)" }
Say "the job answers: simulated date $($answer.result.simulated_date), $($answer.result.free_gb) GB free."

$eid = "$stamp-setup-export"
[System.IO.File]::WriteAllText((Join-Path $reqDir "$eid.json.tmp"), '{"action":"export"}', $Utf8)
Move-Item (Join-Path $reqDir "$eid.json.tmp") (Join-Path $reqDir "$eid.json")
Say 'asked the job for the first full extract; waiting up to thirty minutes ...'
$eresp = Join-Path $respDir "$eid.json"
$deadline = (Get-Date).AddMinutes(30)
while (-not (Test-Path $eresp) -and (Get-Date) -lt $deadline) { Start-Sleep -Seconds 10 }
if (-not (Test-Path $eresp)) {
    Fail 'the first extract has not finished after thirty minutes. It continues in the background; tell the agent, which will check it.'
} else {
    $eanswer = [System.IO.File]::ReadAllText($eresp, $Utf8) | ConvertFrom-Json
    if ($eanswer.status -ne 'ok') { Fail "the first extract failed: $($eanswer.error)" }
    Say ("first extract written: {0} tables, {1:N0} MB, in data\raw\wwi\{2}; {3} GB free." -f $eanswer.result.tables, ($eanswer.result.total_bytes / 1MB), $eanswer.result.simulated_date, $eanswer.result.free_gb)
}
Say 'DONE. Nothing else is needed from you; you can close this window.'

<#
  nsdn — Wide World Importers sandbox: the request-folder job.

  Runs every minute under Task Scheduler as the author (S4U, no window). It reads request
  files the agent (or the author's desktop shortcut) drops into data\wwi\requests\, carries
  out one of a FIXED list of actions, and writes a response file. It never runs code that
  arrives in a request: the only free text it accepts is the SQL of a "query" request, and
  that runs as a read-only database user that cannot revert to the author's rights.

  Actions (request = one JSON file, data\wwi\requests\<id>.json):
    {"action":"status"}
    {"action":"advance", "days":1}          one simulated day by default; each day is exported
    {"action":"export"}                     full extract of the current simulated day
    {"action":"query", "sql":"SELECT ..."}  read-only; result as CSV beside the response
    {"action":"generate", "date":"YYYY-MM-DD"}  the customer system's extract for a date whose WWI
                                            extract is present (note 430 section 4); also run
                                            after every export
    {"action":"freeze", "experiment":"E1", "date":"YYYY-MM-DD"}   freeze an experiment (430 5.1)
    {"action":"score", "experiment":"E1", "part":"development", "proposals":"data/proposals/...csv",
     "duplicates":"data/proposals/...csv"}  figures only (430 5.3)
    {"action":"score", "experiment":"E1", "part":"holdback", "cheap":"...csv", "model":"...csv",
     "cheap_cutoff":"0.9", "model_cutoff":"none", ...}  the one-time release (430 5.4); a
                                            cutoff is the decimal string the scorer reported, or "none"

  The last three run Python scripts that the author's setup.ps1 copied from C:\nsdn-holdout\code
  into the pinned folder's holdout\. They are not in this repository, so that the model proposing
  matches never sees how the customer system's differences are made (ADR-0043, ADR-0044). Their
  standard error is drained and never reported: it may hold hidden content. A response carries
  only a result rebuilt from each action's allowed fields and plain values, or a fixed error code.

  This file is installed by setup.ps1 as a pinned copy in C:\ProgramData\nsdn-wwi\. Editing
  the copy in the repository changes nothing until setup.ps1 is run again.
  Windows PowerShell 5.1; .NET Framework's System.Data.SqlClient; no modules.
#>
param(
    [Parameter(Mandatory = $true)][string]$RepoRoot,
    [string]$Server = 'localhost',
    [string]$Database = 'WideWorldImporters'
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2.0

# ---------------------------------------------------------------- settings
$OrdersPerDay      = 60     # Microsoft's documented example value
$SaturdayPercent   = 50
$SundayPercent     = 0
$MaxDaysPerRequest = 7
$KeepExtracts      = 3      # dated extract folders kept; older ones are deleted
$MinFreeGBExport   = 2      # an export is refused below this
$QueryRowCap       = 100000
$QueryTimeoutSec   = 300
$QueryMaxMB        = 200    # a query result larger than this is cut off
$QueryCellMaxChars = 100000 # a longer text or binary value in a query result is cut off
$ReaderUser        = 'nsdn_reader'
$HoldoutRoot       = 'C:\nsdn-holdout'                        # the hidden folder (430 section 3)
$HoldoutPin        = Join-Path $PSScriptRoot 'holdout'        # pinned copies of its scripts
$HoldoutPy         = Join-Path $PSScriptRoot 'venv\Scripts\python.exe'
$HoldoutTimeoutSec = 1800

$WwiDir      = Join-Path $RepoRoot 'data\wwi'
$RequestDir  = Join-Path $WwiDir 'requests'
$ProcessedDir= Join-Path $WwiDir 'processed'
$ResponseDir = Join-Path $WwiDir 'responses'
$ExtractRoot = Join-Path $RepoRoot 'data\raw\wwi'
$CrmRoot     = Join-Path $RepoRoot 'data\raw\crm'
$LogFile     = Join-Path $WwiDir 'job.log'
$Heartbeat   = Join-Path $WwiDir 'heartbeat.json'
$InFlight    = Join-Path $WwiDir 'advance-in-flight.txt'
$Inv         = [System.Globalization.CultureInfo]::InvariantCulture
$Utf8        = New-Object System.Text.UTF8Encoding($false)

foreach ($d in @($WwiDir, $RequestDir, $ProcessedDir, $ResponseDir, $ExtractRoot)) {
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d | Out-Null }
}

function Write-Log([string]$msg) {
    $line = (Get-Date).ToString('yyyy-MM-ddTHH:mm:ssK', $Inv) + '  ' + $msg
    [System.IO.File]::AppendAllText($LogFile, $line + "`r`n", $Utf8)
}

function Write-JsonAtomic([string]$path, $obj) {
    $tmp = $path + '.tmp'
    [System.IO.File]::WriteAllText($tmp, ($obj | ConvertTo-Json -Depth 6), $Utf8)
    Move-Item -Force -Path $tmp -Destination $path
}

function Get-FreeGB {
    $drive = [System.IO.Path]::GetPathRoot($RepoRoot)
    return [math]::Round((New-Object System.IO.DriveInfo($drive)).AvailableFreeSpace / 1GB, 2)
}

function Write-Heartbeat([int]$handled, [datetime]$since) {
    Write-JsonAtomic $Heartbeat @{
        last_run = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ', $Inv)
        handled = $handled; seconds = [int]((Get-Date) - $since).TotalSeconds; job = $PSCommandPath
    }
}

# Most runs find nothing to do: write the heartbeat and stop before compiling anything.
$started = Get-Date
$pending = @(Get-ChildItem -File -Path $RequestDir -Filter '*.json' -ErrorAction SilentlyContinue | Sort-Object Name)
if ($pending.Count -eq 0) { Write-Heartbeat 0 $started; exit 0 }

# ---------------------------------------------------------------- SQL helpers
function New-Conn {
    $cs = "Server=$Server;Database=$Database;Integrated Security=SSPI;Application Name=nsdn-wwi-job"
    $c = New-Object System.Data.SqlClient.SqlConnection($cs)
    $c.Open()
    return $c
}

function Invoke-Scalar($conn, [string]$sql, [hashtable]$params = @{}) {
    $cmd = $conn.CreateCommand(); $cmd.CommandText = $sql; $cmd.CommandTimeout = 0
    foreach ($k in $params.Keys) { [void]$cmd.Parameters.AddWithValue($k, $params[$k]) }
    return $cmd.ExecuteScalar()
}

function Invoke-NonQuery($conn, [string]$sql, [hashtable]$params = @{}) {
    $cmd = $conn.CreateCommand(); $cmd.CommandText = $sql; $cmd.CommandTimeout = 0
    foreach ($k in $params.Keys) { [void]$cmd.Parameters.AddWithValue($k, $params[$k]) }
    [void]$cmd.ExecuteNonQuery()
}

function Invoke-Rows($conn, [string]$sql) {
    $cmd = $conn.CreateCommand(); $cmd.CommandText = $sql; $cmd.CommandTimeout = 0
    $t = New-Object System.Data.DataTable
    $r = $cmd.ExecuteReader(); $t.Load($r); $r.Close()
    return ,$t
}

# CSV: RFC 4180, UTF-8 without BOM, header row, CRLF. NULL is an empty unquoted field;
# every non-NULL value is quoted, so an empty string ("") stays distinct from NULL.
# Compiled once per run: a PowerShell loop is too slow for the multi-million-row archives.
Add-Type -ReferencedAssemblies System.Data -TypeDefinition @'
using System; using System.Data; using System.Globalization; using System.IO; using System.Text;
public static class NsdnCsv {
    static string Q(string s) { return "\"" + s.Replace("\"", "\"\"") + "\""; }
    public static string Fmt(object v) {
        if (v == null || v is DBNull) return "";
        CultureInfo inv = CultureInfo.InvariantCulture; string s;
        if (v is DateTime) s = ((DateTime)v).ToString("yyyy-MM-ddTHH:mm:ss.fffffff", inv);
        else if (v is DateTimeOffset) s = ((DateTimeOffset)v).ToString("yyyy-MM-ddTHH:mm:ss.fffffffzzz", inv);
        else if (v is bool) s = ((bool)v) ? "1" : "0";
        else if (v is byte[]) s = "0x" + BitConverter.ToString((byte[])v).Replace("-", "");
        else if (v is IFormattable) s = ((IFormattable)v).ToString(null, inv);
        else s = v.ToString();
        return Q(s);
    }
    // Reads one field. With a cell limit (query results, read with SequentialAccess) text and
    // binary values are read in chunks and cut at the limit, so no single value is ever
    // materialised whole; export passes 0 and reads values as they are.
    static object Field(IDataReader r, int i, long cellLimit, ref bool cut) {
        if (r.IsDBNull(i)) return DBNull.Value;
        if (cellLimit <= 0) return r.GetValue(i);
        Type t = r.GetFieldType(i);
        if (t == typeof(string) || t == typeof(char[])) {
            StringBuilder sb = new StringBuilder(); char[] buf = new char[8192]; long off = 0; long n;
            try {
                while ((n = r.GetChars(i, off, buf, 0, buf.Length)) > 0) {
                    if (off + n > cellLimit) { sb.Append(buf, 0, (int)(cellLimit - off)); cut = true; break; }
                    sb.Append(buf, 0, (int)n); off += n;
                }
            } catch (InvalidCastException) {
                // Readers that do not stream text (not SqlDataReader): read whole, then cut.
                string whole = Convert.ToString(r.GetValue(i), CultureInfo.InvariantCulture);
                if (whole.Length > cellLimit) { whole = whole.Substring(0, (int)cellLimit); cut = true; }
                return whole;
            }
            return sb.ToString();
        }
        if (t == typeof(byte[])) {
            MemoryStream ms = new MemoryStream(); byte[] buf = new byte[8192]; long off = 0; long n;
            while ((n = r.GetBytes(i, off, buf, 0, buf.Length)) > 0) {
                if (off + n > cellLimit) { ms.Write(buf, 0, (int)(cellLimit - off)); cut = true; break; }
                ms.Write(buf, 0, (int)n); off += n;
            }
            return ms.ToArray();
        }
        return r.GetValue(i);
    }
    // Writes rows until the end, the row cap or the byte budget (UTF-8). The budget is checked
    // cell by cell while a row is built, so memory stays within the budget plus one cell, and
    // a row that would cross it is not written. truncated reports either cap.
    public static long Write(IDataReader r, TextWriter w, long cap, long maxBytes, long cellLimit, out bool cellsCut, out bool truncated) {
        cellsCut = false; truncated = false;
        int n = r.FieldCount; string[] cells = new string[n];
        for (int i = 0; i < n; i++) cells[i] = Q(r.GetName(i));
        string head = string.Join(",", cells) + "\r\n";
        w.Write(head);
        long rows = 0, bytes = Encoding.UTF8.GetByteCount(head);
        while (r.Read()) {
            if (cap > 0 && rows >= cap) { truncated = true; return rows; }
            bool cut = false; long rowBytes = 2;
            for (int i = 0; i < n; i++) {
                cells[i] = Fmt(Field(r, i, cellLimit, ref cut));
                rowBytes += Encoding.UTF8.GetByteCount(cells[i]) + 1;
                if (maxBytes > 0 && bytes + rowBytes > maxBytes) { truncated = true; return rows; }
            }
            if (cut) cellsCut = true;
            string line = string.Join(",", cells) + "\r\n";
            w.Write(line); bytes += Encoding.UTF8.GetByteCount(line); rows++;
        }
        return rows;
    }
}
'@

function Write-ReaderCsv($reader, [System.IO.TextWriter]$w, [long]$cap, [long]$maxBytes = 0, [long]$cellLimit = 0) {
    $cut = $false; $trunc = $false
    $n = [NsdnCsv]::Write($reader, $w, $cap, $maxBytes, $cellLimit, [ref]$cut, [ref]$trunc)
    return @{ rows = $n; truncated = $trunc; cells_cut = $cut }
}

# ---------------------------------------------------------------- state
function Get-SimulatedDate($conn) {
    $d = Invoke-Scalar $conn 'SELECT MAX(SimulatedDate) FROM nsdn.SimulationClock;'
    if ($d -is [System.DBNull]) { throw 'nsdn.SimulationClock is empty; run setup.ps1 again.' }
    return [datetime]$d
}

# ---------------------------------------------------------------- actions
# ---------------------------------------------------------------- the hidden folder's scripts
# The scripts' contract (their build reports): exactly one JSON line on standard output; exit 0
# with status "ok" and the action's fields, or exit 1 with {"status":"error","code":...}. Only a
# result rebuilt from allowed fields reaches a response or the log, never the child's object as
# printed; anything else becomes the fixed code PROTOCOL. Standard error is drained and dropped.
$HoldoutCodes = @('ARGUMENTS','BUSY','PATH','SPACE','STATE','IDENTITY','MANIFEST','INTEGRITY','EXISTS','NOT_READY',
    'FROZEN_HASH','CSV_SCHEMA','CSV_FORMAT','UNKNOWN_RECORD','REPEATED_RECORD','MISSING_RECORD','UNKNOWN_CUSTOMER',
    'CONFIDENCE','METHOD','SELF_PAIR','REPEATED_PAIR','RUN_LIMIT','VERSION_USED','HOLDBACK_CONSUMED',
    'DEVELOPMENT_REQUIRED','DEVELOPMENT_MISMATCH','CUTOFF_MISMATCH','IO','INTERNAL')

function New-HoldoutError([string]$code) { return [pscustomobject]@{ status = 'error'; code = $code } }

# Reads a property without tripping StrictMode on objects that lack it (or have none at all).
function Get-Prop($o, [string]$name) {
    if ($null -eq $o -or -not ($o -is [System.Management.Automation.PSCustomObject])) { return $null }
    $p = $o.PSObject.Properties[$name]
    if ($null -eq $p) { return $null }
    return $p.Value
}

# Windows command-line quoting as the C runtime decodes it (backslashes before a quote and at the end doubled).
function ConvertTo-WindowsArg([string]$a) {
    if ($a.Length -gt 0 -and $a -notmatch '[\s"]') { return $a }
    $sb = New-Object System.Text.StringBuilder
    [void]$sb.Append('"'); $bs = 0
    foreach ($ch in $a.ToCharArray()) {
        if ($ch -eq [char]'\') { $bs++ }
        elseif ($ch -eq [char]'"') { [void]$sb.Append([char]'\', 2 * $bs + 1); [void]$sb.Append('"'); $bs = 0 }
        else { if ($bs -gt 0) { [void]$sb.Append([char]'\', $bs) }; $bs = 0; [void]$sb.Append($ch) }
    }
    if ($bs -gt 0) { [void]$sb.Append([char]'\', 2 * $bs) }
    [void]$sb.Append('"')
    return $sb.ToString()
}

# Copies a nested result keeping only plain keys and short, plain values: no free text can pass.
function Copy-Plain($v, [int]$depth) {
    if ($depth -gt 5) { throw 'too deep' }
    if ($null -eq $v -or $v -is [bool] -or $v -is [int] -or $v -is [long] -or $v -is [double] -or $v -is [decimal]) { return $v }
    if ($v -is [string]) {
        if ($v -match '^[A-Za-z0-9_.:\-]{0,64}$') { return $v }
        throw 'string not plain'
    }
    if ($v -is [System.Management.Automation.PSCustomObject]) {
        $o = [ordered]@{}
        foreach ($p in $v.PSObject.Properties) {
            if ($p.Name -notmatch '^[a-z0-9_]{1,40}$') { throw 'key not plain' }
            $o[$p.Name] = Copy-Plain $p.Value ($depth + 1)
        }
        return [pscustomobject]$o
    }
    if ($v -is [System.Array]) { return @($v | ForEach-Object { Copy-Plain $_ ($depth + 1) }) }
    throw 'type not plain'
}

# What each action may return on success: these fields, and nothing else.
$HoldoutFields = @{
    'generate_crm.py' = @('status', 'date', 'rows', 'manifest_sha256')
    'freeze.py'       = @('status', 'experiment', 'date', 'scorer_version')
    'score.py'        = @('status', 'experiment', 'date', 'scorer_version', 'part', 'method', 'version', 'figures',
                          'cheap', 'model', 'automatic_recall_gain', 'threshold_3')
}

function ConvertTo-HoldoutResult([string]$script, $obj, [int]$exitCode) {
    $status = Get-Prop $obj 'status'
    if ($exitCode -eq 1 -and $status -eq 'error') {
        $code = [string](Get-Prop $obj 'code')
        if ($HoldoutCodes -contains $code) { return New-HoldoutError $code }
        return New-HoldoutError 'PROTOCOL'
    }
    if ($exitCode -ne 0 -or $status -ne 'ok') { return New-HoldoutError 'PROTOCOL' }
    $allowed = $HoldoutFields[$script]
    $out = [ordered]@{}
    try {
        foreach ($p in $obj.PSObject.Properties) {
            if ($allowed -notcontains $p.Name) { return New-HoldoutError 'PROTOCOL' }
            $out[$p.Name] = Copy-Plain $p.Value 0
        }
    } catch { return New-HoldoutError 'PROTOCOL' }
    if ($script -eq 'generate_crm.py' -and -not ([string]$out['date'] -match '^\d{4}-\d{2}-\d{2}$' -and [string]$out['manifest_sha256'] -match '^[0-9a-f]{64}$')) {
        return New-HoldoutError 'PROTOCOL'
    }
    return [pscustomobject]$out
}

# Runs one pinned script under one deadline for exit and both drains; on timeout the whole
# process tree is killed. Never reads a stream result that has not completed.
function Invoke-Holdout([string]$script, [string[]]$argList) {
    if (-not (Test-Path $HoldoutPy)) { return New-HoldoutError 'NO_PYTHON' }
    $path = Join-Path $HoldoutPin $script
    if (-not (Test-Path $path)) { return New-HoldoutError 'NOT_INSTALLED' }
    $p = $null
    try {
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = $HoldoutPy
        $psi.Arguments = (@(@('-I', $path) + $argList) | ForEach-Object { ConvertTo-WindowsArg ([string]$_) }) -join ' '
        $psi.UseShellExecute = $false; $psi.CreateNoWindow = $true
        $psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true
        $deadline = (Get-Date).AddSeconds($HoldoutTimeoutSec)
        $p = [System.Diagnostics.Process]::Start($psi)
        $outTask = $p.StandardOutput.ReadToEndAsync()
        $errTask = $p.StandardError.ReadToEndAsync()
        $left = [int][math]::Max(0, ($deadline - (Get-Date)).TotalMilliseconds)
        if (-not $p.WaitForExit($left)) {
            try { & taskkill.exe /T /F /PID $p.Id 2>&1 | Out-Null } catch { }
            try { if (-not $p.HasExited) { $p.Kill() } } catch { }
            try { [void]$p.WaitForExit(10000) } catch { }
            return New-HoldoutError 'TIMEOUT'
        }
        $left = [int][math]::Max(10000, ($deadline - (Get-Date)).TotalMilliseconds)
        if (-not [System.Threading.Tasks.Task]::WaitAll([System.Threading.Tasks.Task[]]@($outTask, $errTask), $left)) {
            return New-HoldoutError 'TIMEOUT'
        }
        $exitCode = $p.ExitCode
        $lines = @($outTask.Result -split "`r?`n" | Where-Object { $_.Trim() -ne '' })
        if ($lines.Count -ne 1) { return New-HoldoutError 'PROTOCOL' }
        try { $obj = $lines[0] | ConvertFrom-Json } catch { return New-HoldoutError 'PROTOCOL' }
        return ConvertTo-HoldoutResult $script $obj $exitCode
    } catch {
        return New-HoldoutError 'START_FAILED'
    } finally {
        if ($null -ne $p) { try { $p.Dispose() } catch { } }
    }
}

function Test-DateText([string]$d) {
    $out = [datetime]::MinValue
    return ($d -match '^\d{4}-\d{2}-\d{2}$') -and [datetime]::TryParseExact($d, 'yyyy-MM-dd', $Inv, [System.Globalization.DateTimeStyles]::None, [ref]$out)
}

function Get-ReqText($req, [string]$name, [bool]$required) {
    $v = Get-Prop $req $name
    if ($null -eq $v) { if ($required) { throw "$name is required" } else { return $null } }
    return [string]$v
}

function Get-Experiment($req) {
    $e = Get-ReqText $req 'experiment' $true
    if ($e -notmatch '^E[1-9][0-9]{0,5}$') { throw "experiment must be E followed by a number without leading zeros" }
    return $e
}

# A request may name only CSV files under data\proposals\, by a plain relative path.
function Resolve-Proposal([string]$rel) {
    if ($rel -notmatch '^data/proposals/[A-Za-z0-9_\-]+(/[A-Za-z0-9_\-][A-Za-z0-9_\-.]*)*\.csv$' -or $rel -match '\.\.') {
        throw "a proposals path must be a relative path under data/proposals/ ending in .csv: '$rel'"
    }
    $full = Join-Path $RepoRoot ($rel -replace '/', '\')
    if (-not (Test-Path -LiteralPath $full -PathType Leaf)) { throw "no such proposals file: '$rel'" }
    return $full
}

# A cutoff is passed on exactly as the scorer reported it: a decimal from 0 to 1 as a string, or "none"
# for a method with no automatic tier (430 section 6). A JSON number is accepted only if it is short.
function Get-Cutoff($req, [string]$name) {
    $v = Get-Prop $req $name
    if ($null -eq $v) { throw "$name is required" }
    if ($v -is [double] -or $v -is [int] -or $v -is [long] -or $v -is [decimal]) { $v = ([double]$v).ToString('R', $Inv) }
    $t = [string]$v
    if ($t -eq 'none') { return 'none' }
    if ($t -notmatch '^(0(\.[0-9]{1,60})?|1(\.0{1,60})?)$') {
        throw "$name must be a decimal from 0 to 1 written as the scorer reported it, or none"
    }
    return $t
}

# Joint retention (430 section 4): a customer extract lives exactly as long as its WWI extract.
# Never throws; run before and after every generation and after every export.
function Remove-CrmOrphans {
    try {
        if (-not (Test-Path $CrmRoot)) { return }
        foreach ($d in @(Get-ChildItem -Directory $CrmRoot | Where-Object { $_.Name -match '^\d{4}-\d{2}-\d{2}$' })) {
            if (-not (Test-Path (Join-Path $ExtractRoot $d.Name))) {
                try { Remove-Item -Recurse -Force $d.FullName } catch { Write-Log "could not remove orphaned customer extract $($d.Name)" }
            }
        }
    } catch { Write-Log 'customer-extract retention could not run' }
}

function Do-Generate([string]$date) {
    if (-not (Test-DateText $date)) { throw "date must be YYYY-MM-DD" }
    $wwi = Join-Path $ExtractRoot $date
    if (-not (Test-Path (Join-Path $wwi 'manifest.json'))) { throw "no WWI extract for $date" }
    if (-not (Test-Path $CrmRoot)) { New-Item -ItemType Directory -Path $CrmRoot | Out-Null }
    Remove-CrmOrphans
    try { return Invoke-Holdout 'generate_crm.py' @('--wwi', $wwi, '--publish-root', $CrmRoot, '--holdout', $HoldoutRoot) }
    finally { Remove-CrmOrphans }
}

function Do-Freeze($req) {
    $exp = Get-Experiment $req
    $date = Get-ReqText $req 'date' $true
    if (-not (Test-DateText $date)) { throw "date must be YYYY-MM-DD" }
    $r = Invoke-Holdout 'freeze.py' @('--holdout', $HoldoutRoot, '--repo', $RepoRoot, '--experiment', $exp, '--date', $date)
    if ((Get-Prop $r 'status') -ne 'ok') { throw "freeze failed: $(Get-Prop $r 'code')" }
    return $r
}

function Do-Score($req) {
    $exp = Get-Experiment $req
    $part = Get-ReqText $req 'part' $true
    $a = @('--holdout', $HoldoutRoot, '--repo', $RepoRoot, '--experiment', $exp, '--part', $part)
    if ($part -eq 'development') {
        $a += @('--proposals', (Resolve-Proposal (Get-ReqText $req 'proposals' $true)))
        $dup = Get-ReqText $req 'duplicates' $false
        if ($null -ne $dup) { $a += @('--duplicates', (Resolve-Proposal $dup)) }
    } elseif ($part -eq 'holdback') {
        $a += @('--cheap', (Resolve-Proposal (Get-ReqText $req 'cheap' $true)), '--model', (Resolve-Proposal (Get-ReqText $req 'model' $true)))
        foreach ($k in @('cheap_duplicates', 'model_duplicates')) {
            $dup = Get-ReqText $req $k $false
            if ($null -ne $dup) { $a += @(('--' + $k.Replace('_', '-')), (Resolve-Proposal $dup)) }
        }
        $a += @('--cheap-cutoff', (Get-Cutoff $req 'cheap_cutoff'), '--model-cutoff', (Get-Cutoff $req 'model_cutoff'))
    } else { throw "part must be development or holdback" }
    $r = Invoke-Holdout 'score.py' $a
    if ((Get-Prop $r 'status') -ne 'ok') { throw "scoring refused or failed: $(Get-Prop $r 'code')" }
    return $r
}

function Do-Status($conn) {
    $counts = Invoke-Rows $conn @"
SELECT s.name + '.' + t.name AS [table], SUM(p.rows) AS [rows]
FROM sys.tables t JOIN sys.schemas s ON s.schema_id = t.schema_id
JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0,1)
WHERE s.name IN ('Sales','Purchasing','Warehouse','Application')
GROUP BY s.name, t.name ORDER BY 1;
"@
    $size = Invoke-Rows $conn 'SELECT name, type_desc, size/128 AS size_mb FROM sys.database_files;'
    $sim = Get-SimulatedDate $conn
    return @{
        simulated_date = $sim.ToString('yyyy-MM-dd', $Inv)
        max_order_date = ([datetime](Invoke-Scalar $conn 'SELECT MAX(OrderDate) FROM Sales.Orders;')).ToString('yyyy-MM-dd', $Inv)
        free_gb        = Get-FreeGB
        database_files = @($size | ForEach-Object { @{ name = $_.name; type = $_.type_desc; size_mb = [int]$_.size_mb } })
        row_counts     = @($counts | ForEach-Object { @{ table = $_.table; rows = [long]$_.rows } })
    }
}

function Do-Export($conn) {
    if ((Get-FreeGB) -lt $MinFreeGBExport) { throw "Export refused: less than $MinFreeGBExport GB free." }
    $sim = (Get-SimulatedDate $conn).ToString('yyyy-MM-dd', $Inv)
    $dir = Join-Path $ExtractRoot $sim
    $tmpDir = $dir + '.partial'
    if (Test-Path $tmpDir) { Remove-Item -Recurse -Force $tmpDir }
    New-Item -ItemType Directory -Path $tmpDir | Out-Null

    $tables = Invoke-Rows $conn @"
SELECT t.object_id, s.name AS schema_name, t.name AS table_name, t.temporal_type_desc
FROM sys.tables t JOIN sys.schemas s ON s.schema_id = t.schema_id
WHERE t.is_ms_shipped = 0 AND s.name NOT IN ('DataLoadSimulation','nsdn')
ORDER BY s.name, t.name;
"@
    $files = @()
    foreach ($t in $tables) {
        $oid = [int]$t.object_id
        $cols = Invoke-Rows $conn @"
SELECT c.name, ty.name AS type_name, c.column_id
FROM sys.columns c JOIN sys.types ty ON ty.user_type_id = c.user_type_id
WHERE c.object_id = $oid ORDER BY c.column_id;
"@
        # CLR types (geography, geometry, hierarchyid) are rendered server-side as text,
        # because the client has no Microsoft.SqlServer.Types assembly.
        $select = @($cols | ForEach-Object {
            $q = '[' + $_.name.Replace(']', ']]') + ']'
            if ($_.type_name -in @('geography', 'geometry', 'hierarchyid')) { "$q.ToString() AS $q" } else { $q }
        }) -join ', '
        $pk = Invoke-Rows $conn @"
SELECT c.name FROM sys.indexes i
JOIN sys.index_columns ic ON ic.object_id = i.object_id AND ic.index_id = i.index_id
JOIN sys.columns c ON c.object_id = ic.object_id AND c.column_id = ic.column_id
WHERE i.object_id = $oid AND i.is_primary_key = 1 ORDER BY ic.key_ordinal;
"@
        $order = ''
        if ($pk.Rows.Count -gt 0) { $order = ' ORDER BY ' + (@($pk | ForEach-Object { '[' + $_.name.Replace(']', ']]') + ']' }) -join ', ') }
        $full = '[' + $t.schema_name + '].[' + $t.table_name + ']'
        $name = $t.schema_name + '.' + $t.table_name + '.csv.gz'
        $path = Join-Path $tmpDir $name

        $cmd = $conn.CreateCommand(); $cmd.CommandTimeout = 0
        $cmd.CommandText = "SELECT $select FROM $full$order;"
        $fs = [System.IO.File]::Create($path)
        $gz = New-Object System.IO.Compression.GZipStream($fs, [System.IO.Compression.CompressionLevel]::Optimal)
        $w = New-Object System.IO.StreamWriter($gz, $Utf8)
        $r = $cmd.ExecuteReader()
        try { $res = Write-ReaderCsv $r $w 0 } finally { $r.Close(); $w.Close() }
        $hash = (Get-FileHash -Algorithm SHA256 -Path $path).Hash.ToLowerInvariant()
        $files += @{ file = $name; table = "$($t.schema_name).$($t.table_name)"; temporal = $t.temporal_type_desc
                     rows = $res.rows; bytes = (Get-Item $path).Length; sha256 = $hash }
    }
    $manifest = @{
        source = 'WideWorldImporters'; simulated_date = $sim
        extracted_at = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ', $Inv)
        extract = 'full'; format = 'csv, RFC 4180, UTF-8, gzip; NULL = empty unquoted field'
        files = $files
    }
    Write-JsonAtomic (Join-Path $tmpDir 'manifest.json') $manifest
    if (Test-Path $dir) { Remove-Item -Recurse -Force $dir }
    Move-Item -Path $tmpDir -Destination $dir      # the folder appears complete or not at all

    # Retention: keep the newest $KeepExtracts dated folders. Anything under data\frozen is never touched.
    $dated = @(Get-ChildItem -Directory $ExtractRoot | Where-Object { $_.Name -match '^\d{4}-\d{2}-\d{2}$' } | Sort-Object Name -Descending)
    if ($dated.Count -gt $KeepExtracts) { $dated[$KeepExtracts..($dated.Count - 1)] | ForEach-Object { Remove-Item -Recurse -Force $_.FullName } }

    # The customer system's extract for the same date (430 section 4). Its failure leaves this
    # export standing; a "generate" request repeats it.
    Remove-CrmOrphans
    $generation = $null
    try { $generation = Do-Generate $sim }
    catch { $generation = New-HoldoutError 'JOB' }
    if ((Get-Prop $generation 'status') -ne 'ok') { Write-Log "customer extract for $sim not generated: $(Get-Prop $generation 'code')" }

    # Summed by hand: Measure-Object -Property does not read hashtable keys in PowerShell 5.1.
    $totalBytes = [long]0; foreach ($x in $files) { $totalBytes += [long]$x.bytes }
    return @{ simulated_date = $sim; folder = "data/raw/wwi/$sim"; tables = $files.Count
              total_bytes = $totalBytes; free_gb = Get-FreeGB; generation = $generation }
}

function Do-Advance($conn, $req) {
    $days = 1
    if ($req.PSObject.Properties.Name -contains 'days') { $days = [int]$req.days }
    if ($days -lt 1 -or $days -gt $MaxDaysPerRequest) { throw "days must be 1..$MaxDaysPerRequest" }

    # A day that started and never reached the clock leaves this marker behind. Running the
    # same date again could double it, so advancing stops until the database is restored
    # afresh (setup.ps1 -Reset) or the agent has reconciled it with the author.
    if (Test-Path $InFlight) {
        throw ("an earlier advance did not finish: " + [System.IO.File]::ReadAllText($InFlight, $Utf8) +
               ". Advancing is halted; see README, 'When a day fails'.")
    }

    # In the released 2016 backup the simulator procedures may exist only between
    # Configuration_ApplyDataLoadSimulationProcedures and ...Remove...; if Apply exists,
    # call it first, inspect the procedure after it, and always call Remove afterwards.
    $wrap = [int](Invoke-Scalar $conn "SELECT CASE WHEN OBJECT_ID(N'DataLoadSimulation.Configuration_ApplyDataLoadSimulationProcedures') IS NULL THEN 0 ELSE 1 END;") -eq 1

    $results = @(); $passed = @()
    for ($i = 0; $i -lt $days; $i++) {
        $next = (Get-SimulatedDate $conn).AddDays(1)
        $nextText = $next.ToString('yyyy-MM-dd', $Inv)
        $temporalSql = "SELECT ISNULL((SELECT SCHEMA_NAME(schema_id) + N'.' + name + N',' FROM sys.tables WHERE temporal_type = 2 ORDER BY 1 FOR XML PATH(N'')), N'');"
        $temporalBefore = [string](Invoke-Scalar $conn $temporalSql)
        # The marker goes down before anything changes the database's configuration.
        [System.IO.File]::WriteAllText($InFlight, "simulated date $nextText, started " + (Get-Date).ToString('s', $Inv), $Utf8)
        if ($wrap) { Invoke-NonQuery $conn 'EXEC DataLoadSimulation.Configuration_ApplyDataLoadSimulationProcedures;' }
        try {
            $declared = @((Invoke-Rows $conn "SELECT name FROM sys.parameters WHERE object_id = OBJECT_ID(N'DataLoadSimulation.DailyProcessToCreateHistory');") | ForEach-Object { $_.name })
            if ($declared.Count -eq 0) { throw 'DataLoadSimulation.DailyProcessToCreateHistory not found.' }
            $want = @{ '@StartDate' = $next; '@EndDate' = $next
                       '@AverageNumberOfCustomerOrdersPerDay' = $OrdersPerDay
                       '@SaturdayPercentageOfNormalWorkDay' = $SaturdayPercent
                       '@SundayPercentageOfNormalWorkDay' = $SundayPercent
                       '@UpdateCustomFields' = $false; '@IsSilentMode' = $true; '@AreDatesPrinted' = $false }
            $cmd = $conn.CreateCommand(); $cmd.CommandTimeout = 0
            $cmd.CommandType = [System.Data.CommandType]::StoredProcedure
            $cmd.CommandText = 'DataLoadSimulation.DailyProcessToCreateHistory'
            $passed = @($want.Keys | Where-Object { $declared -contains $_ } | Sort-Object)
            foreach ($k in $passed) { [void]$cmd.Parameters.AddWithValue($k, $want[$k]) }

            $before = [long](Invoke-Scalar $conn 'SELECT COUNT_BIG(*) FROM Sales.Orders;')
            $t0 = Get-Date
            [void]$cmd.ExecuteNonQuery()
            Invoke-NonQuery $conn 'INSERT nsdn.SimulationClock (SimulatedDate, AdvancedAt) VALUES (@d, SYSUTCDATETIME());' @{ '@d' = $next }
        } finally {
            if ($wrap) { Invoke-NonQuery $conn 'EXEC DataLoadSimulation.Configuration_RemoveDataLoadSimulationProcedures;' }
        }
        # Only a day that ran, moved the clock, cleaned up and left every temporal table
        # system-versioned again clears the marker; anything else leaves advancing halted.
        $temporalAfter = [string](Invoke-Scalar $conn $temporalSql)
        if ($temporalAfter -ne $temporalBefore) {
            throw "after $nextText the system-versioned tables differ from before (before: $temporalBefore; after: $temporalAfter); advancing is halted."
        }
        Remove-Item -Force $InFlight
        $after = [long](Invoke-Scalar $conn 'SELECT COUNT_BIG(*) FROM Sales.Orders;')
        $day = @{ simulated_date = $nextText; weekday = $next.DayOfWeek.ToString()
                  new_orders = $after - $before; seconds = [int]((Get-Date) - $t0).TotalSeconds }
        Write-Log ("advanced to {0}: {1} new orders in {2}s" -f $nextText, $day.new_orders, $day.seconds)
        # The clock has moved: if the export fails, a plain "export" request repeats it for this date.
        try { $day.export = Do-Export $conn }
        catch { throw ("advanced to $nextText, but its export failed (request 'export' to repeat it): " + $_.Exception.Message) }
        $results += $day
    }
    return @{ days = $results; wrapped_in_apply_remove = $wrap; parameters_passed = $passed }
}

function Do-Query($conn, $req, [string]$id) {
    if (-not ($req.PSObject.Properties.Name -contains 'sql') -or [string]::IsNullOrWhiteSpace($req.sql)) { throw 'query needs "sql".' }
    if ((Get-FreeGB) -lt $MinFreeGBExport) { throw "Query refused: less than $MinFreeGBExport GB free." }
    $out = Join-Path $ResponseDir ($id + '.csv')
    $cmd = $conn.CreateCommand(); $cmd.CommandTimeout = $QueryTimeoutSec
    # WITH NO REVERT: the query cannot switch back to the author's rights in this session.
    $cmd.CommandText = "EXECUTE AS USER = N'$ReaderUser' WITH NO REVERT;`r`n" + [string]$req.sql
    $tmp = $out + '.tmp'
    $w = New-Object System.IO.StreamWriter($tmp, $false, $Utf8)
    $r = $cmd.ExecuteReader([System.Data.CommandBehavior]::SequentialAccess)
    try { $res = Write-ReaderCsv $r $w $QueryRowCap ([long]$QueryMaxMB * 1MB) $QueryCellMaxChars } finally { $r.Close(); $w.Close() }
    Move-Item -Force $tmp $out
    return @{ result_file = "data/wwi/responses/$id.csv"; rows = $res.rows; truncated = $res.truncated; cells_cut = $res.cells_cut; row_cap = $QueryRowCap; max_mb = $QueryMaxMB; cell_max_chars = $QueryCellMaxChars }
}

# ---------------------------------------------------------------- main
$handled = 0
foreach ($f in $pending) {
    $id = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    $resp = @{ id = $id; received_at = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ', $Inv) }
    # Move the request out of the queue first, so a crash can never make it run twice.
    $claimed = Join-Path $ProcessedDir $f.Name
    try { Move-Item -Force -Path $f.FullName -Destination $claimed } catch { continue }
    $conn = $null
    try {
        $req = [System.IO.File]::ReadAllText($claimed, $Utf8) | ConvertFrom-Json
        $resp.action = [string]$req.action
        Write-Log "request $id : $($resp.action)"
        $conn = New-Conn
        switch ($resp.action) {
            'status'  { $resp.result = Do-Status $conn }
            'export'  { $resp.result = Do-Export $conn }
            'advance' { $resp.result = Do-Advance $conn $req }
            'query'   { $resp.result = Do-Query $conn $req $id }
            'generate' {
                $g = Do-Generate (Get-ReqText $req 'date' $true)
                if ((Get-Prop $g 'status') -ne 'ok') { throw "generation failed: $(Get-Prop $g 'code')" }
                $resp.result = $g
            }
            'freeze'  { $resp.result = Do-Freeze $req }
            'score'   { $resp.result = Do-Score $req }
            default   { throw "unknown action '$($resp.action)'; allowed: status, advance, export, query, generate, freeze, score" }
        }
        $resp.status = 'ok'
    } catch {
        $resp.status = 'error'
        $resp.error = $_.Exception.Message
        Write-Log "request $id failed: $($_.Exception.Message)"
    } finally {
        if ($conn) { $conn.Dispose() }
    }
    $resp.finished_at = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ', $Inv)
    Write-JsonAtomic (Join-Path $ResponseDir ($id + '.json')) $resp
    $handled++
}
Write-Heartbeat $handled $started

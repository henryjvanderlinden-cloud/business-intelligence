"""nsdn - Wide World Importers sandbox: the warehouse runner.

Runs every minute under Task Scheduler as the author, from a pinned copy installed by setup.ps1, with the
pinned Python environment. It is deterministic machinery (ADR-0004): no model takes part.

What it does, each run:
  1. Finds complete extracts in data/raw/wwi/<date>/ (a folder appears only once its manifest.json is written)
     that are newer than the last date loaded into the warehouse.
  2. For each, oldest first: checks that the date is the next one expected and that every file matches the
     manifest (SHA-256, row count); lands the files as text into the schema `landing`, replacing the previous
     day's; then runs `dbt build` on the dbt project in the repository, as it stands.
  3. Records every attempt in nsdn_meta.load_log, and after a successful load publishes a copy of the warehouse
     (data/warehouse/published/wwi.duckdb) for readers.
  4. If the dbt project has changed since the last successful load and no new extract is waiting, rebuilds the
     latest date with the new project, so that new SQL goes live without waiting for the next day.
  It writes data/warehouse/status.json on every run and an alert file under data/warehouse/alerts/ on every
  failure. A failed date is not retried until the dbt project or the extract changes; it is never skipped.

Confinement (ADR-0015, 420 §12 C): only the landing step, which is this file, reads files. dbt runs with a pinned
profile whose DuckDB connection has file-system access switched off and locked, so the project's SQL can read and
write only tables in the warehouse. Python models and dbt packages are refused, because they would run code here.

Usage: python runner.py --repo-root C:\\Git\\business-intelligence [--profiles-dir DIR] [--once-date YYYY-MM-DD]
Exit code 0 when nothing failed, 1 when a load failed, 2 when the runner itself could not run.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
import shutil
import sys
import time
import traceback
from pathlib import Path

RUNNER_VERSION = "1"
PROFILE_NAME = "nsdn_wwi"


def utcnow():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def iso(t):
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


class Paths:
    def __init__(self, repo, profiles_dir):
        self.repo = repo
        self.extracts = repo / "data" / "raw" / "wwi"
        self.wh_dir = repo / "data" / "warehouse"
        self.warehouse = self.wh_dir / "wwi.duckdb"
        # Same file name as the warehouse, so that its catalog is also called "wwi" and its views resolve.
        self.published = self.wh_dir / "published" / "wwi.duckdb"
        self.status = self.wh_dir / "status.json"
        self.log = self.wh_dir / "runner.log"
        self.alerts = self.wh_dir / "alerts"
        self.lock = self.wh_dir / "runner.lock"
        self.publish_pending = self.wh_dir / "publish-pending"
        self.target = self.wh_dir / "dbt-target"
        self.dbt_logs = self.wh_dir / "dbt-logs"
        self.project = repo / "prototypes" / "wwi_sandbox" / "dbt"
        self.profiles = profiles_dir


def write_json_atomic(path, obj):
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2, default=str), encoding="utf-8")
    os.replace(tmp, path)


def log(p, msg):
    with open(p.log, "a", encoding="utf-8") as f:
        f.write(iso(utcnow()) + "  " + msg + "\n")


def alert(p, kind, detail):
    p.alerts.mkdir(parents=True, exist_ok=True)
    stamp = utcnow().strftime("%Y%m%dT%H%M%SZ")
    write_json_atomic(p.alerts / f"{stamp}-{kind}.json", {"at": iso(utcnow()), "kind": kind, **detail})
    log(p, f"ALERT {kind}: {detail.get('message', '')}")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def project_hash(project):
    """Hash of every file of the dbt project that dbt reads, so a change to the SQL is noticed."""
    h = hashlib.sha256()
    skip = {"target", "logs", "dbt_packages", ".user.yml"}
    for f in sorted(project.rglob("*")):
        rel = f.relative_to(project)
        if f.is_file() and not (set(rel.parts) & skip):
            h.update(str(rel.as_posix()).encode() + b"\0")
            h.update(f.read_bytes() + b"\0")
    return h.hexdigest()


def refused_files(project):
    """Files that would let the project run code outside DuckDB's confinement."""
    bad = [f for f in project.rglob("*.py")]
    bad += [project / n for n in ("packages.yml", "dependencies.yml", "profiles.yml") if (project / n).exists()]
    return [str(f.relative_to(project).as_posix()) for f in bad]


def dated_extracts(p):
    out = []
    if p.extracts.is_dir():
        for d in sorted(p.extracts.iterdir()):
            try:
                day = dt.date.fromisoformat(d.name)
            except ValueError:
                continue
            if d.is_dir() and (d / "manifest.json").is_file():
                out.append((day, d))
    return out


def read_status(p):
    try:
        return json.loads(p.status.read_text(encoding="utf-8"))
    except Exception:
        return {}


def acquire_lock(p, stale_hours=3):
    try:
        fd = os.open(p.lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        age = time.time() - p.lock.stat().st_mtime
        if age < stale_hours * 3600:
            return False
        p.lock.unlink()
        fd = os.open(p.lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.write(fd, f"pid {os.getpid()} at {iso(utcnow())}".encode())
    os.close(fd)
    return True


# ------------------------------------------------------------------ warehouse bookkeeping
LOAD_LOG_DDL = """
CREATE SCHEMA IF NOT EXISTS nsdn_meta;
CREATE TABLE IF NOT EXISTS nsdn_meta.load_log (
    load_date        DATE      NOT NULL,
    attempt_at       TIMESTAMP NOT NULL,
    mode             VARCHAR   NOT NULL,   -- 'load' (new extract) or 'rebuild' (changed project)
    status           VARCHAR   NOT NULL,   -- 'ok' or 'failed'
    stage            VARCHAR,              -- where a failure happened: arrival, landing, dbt, publish
    manifest_sha256  VARCHAR,
    project_sha256   VARCHAR,
    runner_version   VARCHAR,
    files            INTEGER,
    rows_landed      BIGINT,
    dbt_summary      VARCHAR,
    message          VARCHAR,
    seconds          DOUBLE
);
CREATE SCHEMA IF NOT EXISTS landing;
CREATE TABLE IF NOT EXISTS landing._load (
    load_date DATE, source_table VARCHAR, landing_table VARCHAR, file VARCHAR, sha256 VARCHAR,
    manifest_rows BIGINT, landed_rows BIGINT, temporal VARCHAR, landed_at TIMESTAMP
);
"""


def connect_rw(p):
    import duckdb
    return duckdb.connect(str(p.warehouse))


def warehouse_state(p):
    con = connect_rw(p)
    try:
        con.execute(LOAD_LOG_DDL)
        last_ok = con.execute(
            "SELECT load_date, project_sha256 FROM nsdn_meta.load_log WHERE status = 'ok' "
            "ORDER BY load_date DESC, attempt_at DESC LIMIT 1").fetchone()
        failures = con.execute(
            "SELECT load_date, manifest_sha256, project_sha256 FROM nsdn_meta.load_log l WHERE status = 'failed' "
            "AND attempt_at = (SELECT max(attempt_at) FROM nsdn_meta.load_log WHERE load_date = l.load_date)").fetchall()
    finally:
        con.close()
    return last_ok, {(r[0], r[1], r[2]) for r in failures}


def record(p, **row):
    con = connect_rw(p)
    try:
        cols = list(row)
        con.execute(f"INSERT INTO nsdn_meta.load_log ({', '.join(cols)}) VALUES ({', '.join('?' * len(cols))})",
                    [row[c] for c in cols])
    finally:
        con.close()


# ------------------------------------------------------------------ the stages of one load
class StageError(Exception):
    def __init__(self, stage, message):
        super().__init__(message)
        self.stage = stage


def check_arrival(folder, expected_date, day):
    """Delivery identity (162): the manifest is for this date and source, and every file matches it."""
    raw = (folder / "manifest.json").read_bytes()
    manifest = json.loads(raw.decode("utf-8-sig"))
    if manifest.get("source") != "WideWorldImporters" or manifest.get("simulated_date") != day.isoformat():
        raise StageError("arrival", f"manifest is for {manifest.get('source')} {manifest.get('simulated_date')}, "
                                    f"not WideWorldImporters {day}")
    if manifest.get("extract") != "full":
        raise StageError("arrival", f"extract type {manifest.get('extract')!r}; this runner handles full extracts only")
    if expected_date and day != expected_date:
        raise StageError("arrival", f"expected {expected_date} next, found {day}; a day is missing or out of order")
    listed = {f["file"] for f in manifest["files"]}
    present = {f.name for f in folder.iterdir() if f.name != "manifest.json"}
    if listed != present:
        raise StageError("arrival", f"files differ from the manifest: missing {sorted(listed - present)}, "
                                    f"extra {sorted(present - listed)}")
    for f in manifest["files"]:
        if sha256_file(folder / f["file"]) != f["sha256"]:
            raise StageError("arrival", f"{f['file']} does not match its SHA-256 in the manifest")
    return manifest, hashlib.sha256(raw).hexdigest()


def landing_name(source_table):
    schema, table = source_table.split(".", 1)
    return (schema + "__" + table).lower()


def land(p, folder, manifest, day):
    """Load every file as text into landing.<schema>__<table>, replacing the previous day's. Types are dbt's job."""
    con = connect_rw(p)
    total = 0
    try:
        con.execute("BEGIN")
        con.execute("DELETE FROM landing._load")
        for f in manifest["files"]:
            name = landing_name(f["table"])
            path = str(folder / f["file"]).replace("'", "''")
            con.execute(f"""
                CREATE OR REPLACE TABLE landing."{name}" AS
                SELECT *, DATE '{day.isoformat()}' AS _nsdn_load_date
                FROM read_csv('{path}', header = true, delim = ',', quote = '"', escape = '"',
                              all_varchar = true, allow_quoted_nulls = false, compression = 'gzip',
                              max_line_size = 8388608, auto_detect = true, sample_size = -1)""")
            n = con.execute(f'SELECT count(*) FROM landing."{name}"').fetchone()[0]
            if n != f["rows"]:
                raise StageError("landing", f"{f['table']}: landed {n} rows, manifest says {f['rows']}")
            con.execute("INSERT INTO landing._load VALUES (?, ?, ?, ?, ?, ?, ?, ?, now())",
                        [day, f["table"], name, f["file"], f["sha256"], f["rows"], n, f.get("temporal")])
            total += n
        con.execute("COMMIT")
    except Exception:
        try:
            con.execute("ROLLBACK")
        except Exception:
            pass
        raise
    finally:
        con.close()
    return total


def run_dbt(p, day):
    """Run `dbt build` in a separate process, so its locked DuckDB connection never mixes with the runner's."""
    import subprocess
    env = dict(os.environ, NSDN_WAREHOUSE=str(p.warehouse), DBT_SEND_ANONYMOUS_USAGE_STATS="False",
               DBT_PROFILES_DIR=str(p.profiles), PYTHONIOENCODING="utf-8")
    args = [sys.executable, "-c", "import sys; from dbt.cli.main import cli; sys.exit(cli())",
            "build", "--project-dir", str(p.project), "--profiles-dir", str(p.profiles),
            "--profile", PROFILE_NAME, "--target-path", str(p.target), "--log-path", str(p.dbt_logs),
            "--vars", json.dumps({"load_date": day.isoformat()}), "--no-use-colors"]
    results = p.target / "run_results.json"
    results.unlink(missing_ok=True)
    proc = subprocess.run(args, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace",
                          timeout=3 * 3600)
    counts, failed = {}, []
    if results.exists():
        for r in json.loads(results.read_text(encoding="utf-8")).get("results", []):
            counts[r["status"]] = counts.get(r["status"], 0) + 1
            if r["status"] in ("error", "fail", "runtime error"):
                failed.append(f"{r['unique_id']}: {(r.get('message') or '')[:300]}")
    summary = ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "no results"
    if proc.returncode != 0:
        detail = "; ".join(failed[:5]) or proc.stdout[-1500:] + proc.stderr[-1500:]
        raise StageError("dbt", f"dbt build (exit {proc.returncode}): {summary}. {detail}")
    return summary


def publish(p):
    """Copy the warehouse for readers, in one move, so a reader never sees a half-written file."""
    p.published.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.published.with_name(p.published.name + ".tmp")
    shutil.copyfile(p.warehouse, tmp)
    try:
        os.replace(tmp, p.published)
        p.publish_pending.unlink(missing_ok=True)
        return True
    except OSError:
        p.publish_pending.write_text("published copy was in use; retried on the next run", encoding="utf-8")
        tmp.unlink(missing_ok=True)
        return False


# ------------------------------------------------------------------ one run
def run(p, once_date=None):
    started = utcnow()
    status = {"runner_version": RUNNER_VERSION, "last_run": iso(started), "result": "idle"}
    previous = read_status(p)
    phash = project_hash(p.project)
    extracts = dated_extracts(p)

    # Fast path: nothing new and the project unchanged - do not touch the warehouse.
    if (not once_date and previous.get("last_ok_date") and previous.get("last_ok_project") == phash
            and not p.publish_pending.exists()
            and all(d.isoformat() <= previous["last_ok_date"] for d, _ in extracts)
            and previous.get("blocked") is None):
        previous.update(last_run=iso(started), result="idle")
        write_json_atomic(p.status, previous)
        return 0

    last_ok, failures = warehouse_state(p)
    last_date, last_project = (last_ok if last_ok else (None, None))

    todo = []
    if once_date:
        todo = [(d, f, "rebuild" if last_date and d <= last_date else "load") for d, f in extracts if d == once_date]
    else:
        todo = [(d, f, "load") for d, f in extracts if last_date is None or d > last_date]
        if not todo and last_date and last_project != phash:
            todo = [(d, f, "rebuild") for d, f in extracts if d == last_date]
            if not todo:
                status["note"] = f"the dbt project changed, but the extract for {last_date} is no longer kept"

    code = 0
    blocked = None
    loaded = []
    for day, folder, mode in todo:
        t0 = time.time()
        expected = None
        if mode == "load" and last_date is not None:
            expected = last_date + dt.timedelta(days=1)
        row = dict(load_date=day, attempt_at=utcnow().replace(tzinfo=None), mode=mode,
                   project_sha256=phash, runner_version=RUNNER_VERSION)
        try:
            bad = refused_files(p.project)
            if bad:
                raise StageError("dbt", f"refused: the dbt project contains {bad}; Python models and packages "
                                        "would run outside the warehouse's confinement")
            manifest, mhash = check_arrival(folder, expected, day)
            row.update(manifest_sha256=mhash, files=len(manifest["files"]))
            if (day, mhash, phash) in failures:
                blocked = {"date": day.isoformat(), "message": "this date failed before with the same extract and "
                           "the same dbt project; waiting for a change to either"}
                break
            row["rows_landed"] = land(p, folder, manifest, day)
            row["dbt_summary"] = run_dbt(p, day)
            row.update(status="ok", seconds=round(time.time() - t0, 1))
            record(p, **row)
            log(p, f"{mode} {day}: ok, {row['rows_landed']} rows landed, dbt {row['dbt_summary']}, "
                   f"{row['seconds']}s")
            loaded.append(day.isoformat())
            last_date, last_project = day, phash
            p.publish_pending.write_text("a load finished; not yet published", encoding="utf-8")
        except Exception as e:
            stage = getattr(e, "stage", "runner")
            msg = str(e) if isinstance(e, StageError) else f"{type(e).__name__}: {e}"
            row.update(status="failed", stage=stage, message=msg[:2000], seconds=round(time.time() - t0, 1))
            try:
                record(p, **row)
            except Exception:
                msg += " (could not record the failure in the load log)"
            alert(p, f"load-failed-{stage}", {"date": day.isoformat(), "mode": mode, "message": msg,
                                               "trace": traceback.format_exc()[-3000:]})
            blocked = {"date": day.isoformat(), "stage": stage, "message": msg[:500]}
            code = 1
            break

    if p.publish_pending.exists():
        if not publish(p):
            status["note"] = "the published copy was in use and is behind the warehouse; retried next run"

    status.update(
        result="failed" if code else ("loaded" if loaded else ("blocked" if blocked else "idle")),
        loaded=loaded, blocked=blocked,
        last_ok_date=last_date.isoformat() if last_date else None, last_ok_project=last_project,
        project_sha256=phash, extracts_present=[d.isoformat() for d, _ in extracts],
        warehouse_mb=round(p.warehouse.stat().st_size / 2**20, 1) if p.warehouse.exists() else None,
        free_gb=round(shutil.disk_usage(p.wh_dir).free / 2**30, 2), seconds=round((utcnow() - started).total_seconds()))
    write_json_atomic(p.status, status)
    return code


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", required=True)
    ap.add_argument("--profiles-dir", default=str(Path(__file__).resolve().parent / "profiles"))
    ap.add_argument("--once-date", help="load or rebuild this one date only (for a manual test)")
    a = ap.parse_args()
    p = Paths(Path(a.repo_root).resolve(), Path(a.profiles_dir).resolve())
    p.wh_dir.mkdir(parents=True, exist_ok=True)
    if not acquire_lock(p):
        return 0
    try:
        once = dt.date.fromisoformat(a.once_date) if a.once_date else None
        return run(p, once)
    except Exception as e:
        try:
            alert(p, "runner-error", {"message": f"{type(e).__name__}: {e}", "trace": traceback.format_exc()[-3000:]})
        except Exception:
            pass
        return 2
    finally:
        p.lock.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())

"""nsdn - the cloud test suite of the vault generator (143 section 10 items 7 to 9; section 9 item 3).

Loads kept WWI extracts into fresh DuckDB warehouses exactly as the runner does (its own landing code, its pinned
profile, `dbt build` with the variable load_date, a row in nsdn_meta.load_log), and checks:

  1. clean       every extract in date order, each build passing its tests;
  2. twice       loading the last extract again changes no row of any vault table;
  3. failed      a batch that fails halfway with a wrong model, then succeeds after the fix, equals the clean load;
  4. rebuild     every satellite reconstructs each delivered source version exactly (149 Rule 10);
  5. late        a constructed late arrival is followed by a restatement of the next version (143 section 6 item 6).

Usage: python test_load.py --root REPO --extracts DIR [--work DIR]
DIR holds dated folders as the runner's data/raw/wwi/ does; a folder may hold only some of the manifest's files,
and only those are landed. Exit 0 when every check passes.
"""
import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


class P:
    """The attributes of runner.Paths that runner.land and runner.run_dbt use."""
    def __init__(self, work, project, profiles):
        self.warehouse = os.path.join(work, "wwi.duckdb")
        self.target = os.path.join(work, "dbt-target")
        self.dbt_logs = os.path.join(work, "dbt-logs")
        self.project = project
        self.profiles = profiles


def runner_module(root):
    sys.path.insert(0, os.path.join(root, "prototypes", "wwi_sandbox"))
    import runner
    return runner


def land(runner, p, folder, day):
    from pathlib import Path
    with open(os.path.join(folder, "manifest.json"), encoding="utf-8-sig") as f:
        manifest = json.load(f)
    present = set(os.listdir(folder))
    manifest["files"] = [f for f in manifest["files"] if f["file"] in present]
    con = runner.connect_rw(Pw(p))
    con.execute(runner.LOAD_LOG_DDL)
    con.close()
    return runner.land(Pw(p), Path(folder), manifest, day)


class Pw:
    def __init__(self, p):
        from pathlib import Path
        self.warehouse = Path(p.warehouse)
        self.target = Path(p.target)
        self.dbt_logs = Path(p.dbt_logs)
        self.project = Path(p.project)
        self.profiles = Path(p.profiles)


def dbt_build(runner, p, day):
    try:
        return True, runner.run_dbt(Pw(p), day)
    except runner.StageError as e:
        return False, str(e)


def log_row(runner, p, day, status):
    con = runner.connect_rw(Pw(p))
    con.execute("INSERT INTO nsdn_meta.load_log (load_date, attempt_at, mode, status) VALUES (?, now(), 'load', ?)",
                [day, status])
    con.close()


def load_day(runner, p, folder, day, expect_ok=True):
    land(runner, p, folder, day)
    ok, summary = dbt_build(runner, p, day)
    log_row(runner, p, day, "ok" if ok else "failed")
    if ok != expect_ok:
        raise SystemExit("load %s: expected %s, got %s: %s" % (day, expect_ok, ok, summary))
    return summary


def vault_tables(con):
    return [r[0] for r in con.execute("select table_name from information_schema.tables "
                                      "where table_schema = 'raw_vault' order by 1").fetchall()]


def compare(a_path, b_path):
    import duckdb
    con = duckdb.connect()
    con.execute("ATTACH '%s' AS a (READ_ONLY)" % a_path)
    con.execute("ATTACH '%s' AS b (READ_ONLY)" % b_path)
    ta = [r[0] for r in con.execute("select table_name from information_schema.tables where table_catalog='a' "
                                    "and table_schema='raw_vault' order by 1").fetchall()]
    tb = [r[0] for r in con.execute("select table_name from information_schema.tables where table_catalog='b' "
                                    "and table_schema='raw_vault' order by 1").fetchall()]
    diffs = [] if ta == tb else ["table lists differ"]
    for t in ta:
        n = con.execute("select count(*) from ((select * from a.raw_vault.%s except all select * from b.raw_vault.%s) "
                        "union all (select * from b.raw_vault.%s except all select * from a.raw_vault.%s))"
                        % (t, t, t, t)).fetchone()[0]
        if n:
            diffs.append("%s: %d rows differ" % (t, n))
    con.close()
    return ta, diffs


def fresh(work, name, project, profiles):
    d = os.path.join(work, name)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    return P(d, project, profiles)


def reconstruction(db, root):
    """Every satellite at every delivered source version equals the staging row of that version."""
    sys.path.insert(0, os.path.join(root, "tools"))
    import model_lib
    import duckdb
    con = duckdb.connect(db, read_only=True)
    problems, checked = [], 0
    for rel, f, s, prose, errs in model_lib.load(root):
        if f.get("kind") not in ("satellite", "reference"):
            continue
        name = f["name"]
        exists = con.execute("select count(*) from information_schema.tables where table_schema='raw_vault' "
                             "and table_name=?", [name]).fetchone()[0]
        if not exists:
            continue
        table = f["source_table"]
        stg = "staging.stg_wwi__" + table.replace(".", "__").lower()
        cols = [subj for subj, fl in s["Columns"] if not fl.get("load", "").startswith("never")]
        key = '"%s"' % f["key"].split(".")[-1] if f["kind"] == "reference" else "hk_" + f["parent"][4:]
        on = " and ".join('st."%s" is not distinct from v."%s"' % (c, c) for c in cols)
        milestone = f.get("satellite_kind") == "milestone"
        sql = """
            with versions as (select {key} as k, source_ts, source_seq, {cols} from {stg} where {key} is not null),
            as_of as (
                select v.k, v.source_ts, v.source_seq,
                       (select struct_pack({pack}) from raw_vault.{name} st
                        where st.{key} = v.k and (st.source_ts, st.source_seq) <= (v.source_ts, v.source_seq)
                        order by st.source_ts desc, st.source_seq desc limit 1) as got,
                       struct_pack({vpack}) as want
                from versions v)
            select count(*), count(*) filter (where got is distinct from want {ms}) from as_of
        """.format(key=key, cols=", ".join('"%s"' % c for c in cols), stg=stg, name=name,
                   pack=", ".join('"%s" := st."%s"' % (c, c) for c in cols),
                   vpack=", ".join('"%s" := v."%s"' % (c, c) for c in cols),
                   ms="and not (got is null and want = struct_pack(%s))" % ", ".join(
                       '"%s" := null::%s' % (c, "varchar") for c in cols) if milestone else "")
        try:
            n, bad = con.execute(sql).fetchone()
        except Exception as e:
            problems.append("%s: %s" % (name, str(e)[:300]))
            continue
        checked += n
        if bad:
            problems.append("%s: %d of %d versions do not reconstruct" % (name, bad, n))
    con.close()
    return checked, problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--extracts", required=True)
    ap.add_argument("--work", default="/tmp/nsdn_vault_test")
    ap.add_argument("--project", default=None, help="generated dbt project (default: the repository's)")
    args = ap.parse_args()
    runner = runner_module(args.root)
    project = args.project or os.path.join(args.root, "prototypes", "wwi_sandbox", "dbt")
    profiles = os.path.join(args.root, "prototypes", "wwi_sandbox", "profiles")
    days = sorted(d for d in os.listdir(args.extracts) if os.path.isfile(os.path.join(args.extracts, d, "manifest.json")))
    os.makedirs(args.work, exist_ok=True)
    results = {}

    # 1. clean
    pc = fresh(args.work, "clean", project, profiles)
    for d in days:
        s = load_day(runner, pc, os.path.join(args.extracts, d), dt.date.fromisoformat(d))
        print("clean %s: %s" % (d, s))
    results["clean"] = "ok, %d days" % len(days)

    # 2. twice: the last extract again (its batch already succeeded, so nothing may change)
    p2 = fresh(args.work, "twice", project, profiles)
    shutil.copy(pc.warehouse, p2.warehouse)
    ok, s = dbt_build(runner, p2, dt.date.fromisoformat(days[-1]))
    tables, diffs = compare(pc.warehouse, p2.warehouse)
    results["twice"] = "ok, %d tables unchanged" % len(tables) if ok and not diffs else "FAILED %s %s" % (s, diffs)

    # 3. failed: last batch built first with a wrong model that fails a test, then with the right project
    p3 = fresh(args.work, "failed", project, profiles)
    for d in days[:-1]:
        load_day(runner, p3, os.path.join(args.extracts, d), dt.date.fromisoformat(d))
    bad_project = os.path.join(args.work, "bad_project")
    shutil.rmtree(bad_project, ignore_errors=True)
    shutil.copytree(project, bad_project)
    victim = [os.path.join(dp, f) for dp, dn, fs in os.walk(os.path.join(bad_project, "models", "raw_vault"))
              for f in fs if f.startswith("sat_customer__wwi.sql")][0]
    text = open(victim, encoding="utf-8").read()
    text = text.replace('case when i.hk is not null then i."CustomerName"', 'case when i.hk is not null then upper(i."CustomerName")')
    open(victim, "w", encoding="utf-8").write(text)
    with open(os.path.join(bad_project, "tests", "generated", "zz_fail_halfway.sql"), "w") as f:
        f.write("select 1 as always_fails\n")
    last = dt.date.fromisoformat(days[-1])
    land(runner, p3, os.path.join(args.extracts, days[-1]), last)
    p3.project = bad_project
    ok_bad, s_bad = dbt_build(runner, p3, last)
    log_row(runner, p3, last, "ok" if ok_bad else "failed")
    p3.project = project
    ok_fix, s_fix = dbt_build(runner, p3, last)
    log_row(runner, p3, last, "ok" if ok_fix else "failed")
    tables, diffs = compare(pc.warehouse, p3.warehouse)
    results["failed"] = ("ok, failed run removed and batch rebuilt: %d tables equal the clean load" % len(tables)
                         if (not ok_bad) and ok_fix and not diffs else
                         "FAILED bad_ok=%s fix_ok=%s %s %s" % (ok_bad, ok_fix, s_fix[:300], diffs))

    # 4. reconstruction
    n, problems = reconstruction(pc.warehouse, args.root)
    results["rebuild"] = "ok, %d versions reconstructed" % n if not problems else "FAILED %s" % problems

    # 5. late arrival, constructed on two synthetic days after the last extract:
    #    day +1: one order edited at t1 + 2h with nothing visible changed (audit row, no satellite row);
    #    day +2: the same order arrives at t1 + 1h with other comments (late).
    #    Expected in sat_sales_order__wwi: t1 as before, t1 + 1h with the late comments, and a restatement of t1 + 2h
    #    carrying the values of t1 (143 section 6 item 6).
    p5 = fresh(args.work, "late", project, profiles)
    shutil.copy(pc.warehouse, p5.warehouse)
    import duckdb
    con = duckdb.connect(p5.warehouse, read_only=True)
    order_id, hk, t1, comments = con.execute(
        'select "OrderID", hk_sales_order, "LastEditedWhen", "Comments" from staging.stg_wwi__sales__orders '
        'order by "OrderID" limit 1').fetchone()
    con.close()
    base = dt.date.fromisoformat(days[-1])
    steps = [(base + dt.timedelta(days=1), 2, None), (base + dt.timedelta(days=2), 1, "LATE ARRIVAL")]
    for day, hours, new_comments in steps:
        land(runner, p5, os.path.join(args.extracts, days[-1]), day)
        con = duckdb.connect(p5.warehouse)
        ts = (t1 + dt.timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%S.0000000")
        sets = ['"LastEditedWhen" = \'%s\'' % ts]
        if new_comments:
            sets.append('"Comments" = \'%s\'' % new_comments)
        con.execute('update landing.sales__orders set %s where "OrderID" = \'%s\'' % (", ".join(sets), order_id))
        con.close()
        ok, s = dbt_build(runner, p5, day)
        log_row(runner, p5, day, "ok" if ok else "failed")
        if not ok:
            results["late"] = "FAILED build %s: %s" % (day, s[:400])
            break
    else:
        con = duckdb.connect(p5.warehouse, read_only=True)
        rows = con.execute('select source_ts, "Comments", batch_id from raw_vault.sat_sales_order__wwi '
                           'where hk_sales_order = ? order by source_ts', [hk]).fetchall()
        warned = s
        con.close()
        expect = [(t1, comments), (t1 + dt.timedelta(hours=1), "LATE ARRIVAL"), (t1 + dt.timedelta(hours=2), comments)]
        got = [(r[0], r[1]) for r in rows]
        results["late"] = ("ok, late version and restatement inserted (%s)" % warned if got == expect
                           else "FAILED expected %s, got %s" % (expect, rows))

    for k, v in results.items():
        print("%-8s %s" % (k, v))
    return 0 if all(v.startswith("ok") for v in results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())

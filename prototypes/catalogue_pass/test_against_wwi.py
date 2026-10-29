"""Test the Postgres catalogue pass against the Wide World Importers reference case.

Rebuilds the structure of WWI's 48 tables in an empty PostgreSQL database from WWI's own catalogue evidence in
analysis/wwi/ (columns in order, nullability, primary and unique keys, foreign keys, descriptions), runs
catalogue_postgres.sql on it, ingests the result into a temporary analysis record as source `wwi_pg`, and compares
what came back with what went in. SQL Server types are mapped to their nearest PostgreSQL types, so types are compared
through that mapping; computed columns are created as plain columns, which the comparison reports and allows.

Needs psql on the path and a PostgreSQL server where the given user may create schemas in the given database, which
should be empty. Run from the root of the nsdn repository:

    python prototypes/catalogue_pass/test_against_wwi.py --host <socket dir or host> --port <port> --user <user> --db <db>

Exits nonzero if anything other than the expected differences is found. Written in session S11.
"""
import argparse
import glob
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ia_lib  # noqa: E402


def wwi_catalogue():
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "analysis/wwi/tables/*/*/evidence/*.json"))):
        with open(f, encoding="utf-8") as fh:
            d = json.load(fh)
        r = d.get("result")
        if d.get("kind") == "catalogue query" and isinstance(r, dict) and "columns" in r:
            t = r["table"][0]
            out[(t["schema_name"], t["table_name"])] = r
    return out


# WWI has no views or triggers; one of each, in a schema of their own, tests that part of the pass.
EXTRA = """
CREATE SCHEMA zz_test;
CREATE VIEW zz_test.order_customers AS
  SELECT o."OrderID", c."CustomerName" FROM "Sales"."Orders" o JOIN "Sales"."Customers" c ON c."CustomerID" = o."CustomerID";
COMMENT ON VIEW zz_test.order_customers IS 'Test view over two WWI tables';
CREATE FUNCTION zz_test.touch() RETURNS trigger LANGUAGE plpgsql AS $$ BEGIN RETURN NEW; END $$;
CREATE TRIGGER touch_orders BEFORE UPDATE ON "Sales"."Orders" FOR EACH ROW EXECUTE FUNCTION zz_test.touch();
CREATE TABLE zz_test.sales (id integer, sold date) PARTITION BY RANGE (sold);
CREATE TABLE zz_test.sales_2025 PARTITION OF zz_test.sales FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
CREATE UNIQUE INDEX people_email_ci ON "Application"."People" (lower("EmailAddress"));
"""
EXTRA_15 = """
CREATE UNIQUE INDEX people_logon_nnd ON "Application"."People" ("LogonName") NULLS NOT DISTINCT;
"""


def pg_type(c):
    t = c["type_name"]
    n = int(c["max_length"]) if c["max_length"] not in ("", None) else 0
    if t in ("nvarchar", "nchar"):
        return "text" if n == -1 else "varchar(%d)" % (n // 2)
    if t in ("varchar", "char"):
        return "text" if n == -1 else "varchar(%d)" % n
    if t in ("decimal", "numeric"):
        return "numeric(%s,%s)" % (c["precision"], c["scale"])
    if t == "datetime2":
        return "timestamp(%d)" % min(int(c["scale"]), 6)   # PostgreSQL keeps at most 6 fractional digits
    return {"int": "integer", "bigint": "bigint", "smallint": "smallint", "tinyint": "smallint", "bit": "boolean",
            "date": "date", "geography": "text", "varbinary": "bytea", "uniqueidentifier": "uuid",
            "datetime": "timestamp(3)", "money": "numeric(19,4)", "time": "time"}[t]


def q(name):
    return '"%s"' % name.replace('"', '""')


def lit(s):
    return "'%s'" % s.replace("'", "''")


def ddl(cat):
    lines = ["SET client_min_messages = warning;"]
    for s in sorted({k[0] for k in cat}):
        lines.append("CREATE SCHEMA %s;" % q(s))
    for (s, t), r in sorted(cat.items()):
        cols = ["  %s %s%s" % (q(c["column_name"]), pg_type(c), "" if c["is_nullable"] == "1" else " NOT NULL")
                for c in sorted(r["columns"], key=lambda c: int(c["column_id"]))]
        lines.append("CREATE TABLE %s.%s (\n%s\n);" % (q(s), q(t), ",\n".join(cols)))
        if r["table"][0].get("description"):
            lines.append("COMMENT ON TABLE %s.%s IS %s;" % (q(s), q(t), lit(r["table"][0]["description"])))
        for c in r["columns"]:
            if c.get("description"):
                lines.append("COMMENT ON COLUMN %s.%s.%s IS %s;" % (q(s), q(t), q(c["column_name"]), lit(c["description"])))
    for (s, t), r in sorted(cat.items()):
        for name, cols, pk in keysets(r):
            lines.append("ALTER TABLE %s.%s ADD CONSTRAINT %s %s (%s);" % (
                q(s), q(t), q(name[:63]), "PRIMARY KEY" if pk else "UNIQUE", ", ".join(q(c) for c in cols)))
    for (s, t), r in sorted(cat.items()):
        for name, (cols, rs, rt, rcols) in fks(r).items():
            lines.append("ALTER TABLE %s.%s ADD CONSTRAINT %s FOREIGN KEY (%s) REFERENCES %s.%s (%s);" % (
                q(s), q(t), q(name[:63]), ", ".join(q(c) for c in cols), q(rs), q(rt), ", ".join(q(c) for c in rcols)))
    return "\n".join(lines) + "\n"


def keysets(r):
    """Primary keys and unique constraints: [(name, [columns in order], is_pk)]."""
    by = {}
    for k in r["keys"]:
        if k.get("is_included_column") == "1":
            continue
        if k["is_primary_key"] == "1" or k.get("is_unique_constraint") == "1":
            by.setdefault(k["index_name"], []).append(k)
    return [(n, [k["column_name"] for k in sorted(ks, key=lambda k: int(k["key_ordinal"]))], ks[0]["is_primary_key"] == "1")
            for n, ks in sorted(by.items())]


def fks(r):
    by = {}
    for f in r["foreign_keys_out"]:
        by.setdefault(f["fk_name"], []).append(f)
    out = {}
    for n, fs in by.items():
        fs = sorted(fs, key=lambda f: int(f["constraint_column_id"]))
        out[n] = ([f["column_name"] for f in fs], fs[0]["ref_schema"], fs[0]["ref_table"], [f["ref_column"] for f in fs])
    return out


def psql(a, args, cwd=None, stdin=None):
    cmd = ["psql", "-X", "-q", "-v", "ON_ERROR_STOP=1", "-h", a.host, "-p", str(a.port), "-U", a.user, "-d", a.db] + args
    p = subprocess.run(cmd, cwd=cwd, input=stdin, capture_output=True, text=True)
    if p.returncode:
        sys.exit("psql failed: %s" % p.stderr.strip()[:2000])
    return p.stdout


def main():
    ap = argparse.ArgumentParser()
    for k, v in (("--host", "localhost"), ("--port", "5432"), ("--user", "postgres"), ("--db", "postgres")):
        ap.add_argument(k, default=v)
    ap.add_argument("--reader", default="", help="create this login with no table privileges and run the pass as it")
    a = ap.parse_args()
    cat = wwi_catalogue()
    if len(cat) != 48:
        sys.exit("expected the 48 tables of the WWI record, found %d" % len(cat))
    version = int(psql(a, ["-tAc", "SHOW server_version_num"]).strip())
    psql(a, ["-f", "-"], stdin=ddl(cat) + EXTRA + (EXTRA_15 if version >= 150000 else ""))
    # every object query must leave the temporary schemas out (review finding 5)
    with open(os.path.join(HERE, "catalogue_postgres.sql"), encoding="utf-8") as fh:
        blocks = fh.read().split("-- @query ")[1:]
    for b in blocks:
        name = b.split("\n", 1)[0].strip()
        if name != "manifest" and "pg_temp_%" not in b:
            sys.exit("query %s does not leave out the temporary schemas" % name)
    if a.reader:   # the pass runs as a login with no privilege on any table (review finding 1)
        psql(a, ["-c", "DROP ROLE IF EXISTS %s; CREATE ROLE %s LOGIN; GRANT CONNECT ON DATABASE %s TO %s;"
                 % (a.reader, a.reader, q(a.db), a.reader)])
    work = tempfile.mkdtemp(prefix="nsdn_catpass_")
    csvdir = os.path.join(work, "csv")
    os.makedirs(csvdir)
    run_as = argparse.Namespace(**dict(vars(a), user=a.reader or a.user))
    psql(run_as, ["-f", os.path.join(HERE, "catalogue_postgres.sql")], cwd=csvdir)
    rec_root = os.path.join(work, "record")
    p = subprocess.run([sys.executable, os.path.join(HERE, "ingest_catalogue.py"), "--source", "wwi_pg", "--root", rec_root,
                        csvdir], capture_output=True, text=True)
    if p.returncode:
        sys.exit("ingest failed: %s" % p.stderr)
    print(p.stdout.strip())

    back = {}
    for f in glob.glob(os.path.join(rec_root, "analysis/wwi_pg/tables/*/*/evidence/*.json")):
        with open(f, encoding="utf-8") as fh:
            d = json.load(fh)
        t = d["result"]["table"][0]
        back[(t["schema_name"], t["table_name"])] = d["result"]
        # the evidence must pass the record's own rule: named by its content hash
        if ia_lib.evidence_hash(d) != os.path.basename(f)[:-5]:
            sys.exit("evidence %s is not named by its content hash" % f)

    problems, allowed, checked = [], [], {"tables": 0, "columns": 0, "keys": 0, "foreign keys": 0, "descriptions": 0}
    view = back.pop(("zz_test", "order_customers"), None)
    reads = sorted((x["ref_schema"], x["ref_table"]) for x in (view or {}).get("view_reads", []))
    if not view or reads != [("Sales", "Customers"), ("Sales", "Orders")] or view["table"][0]["table_kind"] != "view" \
            or [c["column_name"] for c in view["columns"]] != ["OrderID", "CustomerName"]:
        problems.append("the test view did not come back with its columns and the two tables it reads: %r" % (reads,))
    part = back.pop(("zz_test", "sales_2025"), None)
    back.pop(("zz_test", "sales"), None)
    if not part or part["table"][0]["partition_of"] != "zz_test.sales" \
            or "FROM ('2025-01-01') TO ('2026-01-01')" not in part["table"][0]["partition_bound"]:
        problems.append("the test partition did not come back with its parent and bound")
    pk = {k["index_name"]: k for k in back.get(("Application", "People"), {}).get("keys", [])}
    if pk.get("people_email_ci", {}).get("key_expression") != "lower(\"EmailAddress\"::text)":
        problems.append("the unique expression index did not come back with its expression: %r" % pk.get("people_email_ci"))
    if version >= 150000 and pk.get("people_logon_nnd", {}).get("nulls_not_distinct") != "1":
        problems.append("the NULLS NOT DISTINCT index did not come back as such")
    if any(k.get("nulls_not_distinct") == "1" for n, k in pk.items() if n != "people_logon_nnd"):
        problems.append("an ordinary unique key came back as NULLS NOT DISTINCT")
    trig = [t["trigger_name"] for t in back.get(("Sales", "Orders"), {}).get("triggers", [])]
    if trig != ["touch_orders"]:
        problems.append("the test trigger on Sales.Orders did not come back: %r" % (trig,))
    if set(back) != set(cat):
        problems.append("tables differ: missing %s, extra %s" % (sorted(set(cat) - set(back)), sorted(set(back) - set(cat))))
    for k in sorted(set(cat) & set(back)):
        r, b = cat[k], back[k]
        checked["tables"] += 1
        rc = sorted(r["columns"], key=lambda c: int(c["column_id"]))
        bc = sorted(b["columns"], key=lambda c: int(c["column_id"]))
        if [c["column_name"] for c in rc] != [c["column_name"] for c in bc]:
            problems.append("%s.%s: columns or their order differ" % k)
            continue
        for x, y in zip(rc, bc):
            checked["columns"] += 1
            if pg_type(x) != y["type_name"].replace("character varying", "varchar").replace(" without time zone", ""):
                problems.append("%s.%s.%s: type %s came back as %s" % (k + (x["column_name"], pg_type(x), y["type_name"])))
            if x["is_nullable"] != y["is_nullable"]:
                problems.append("%s.%s.%s: nullability differs" % (k + (x["column_name"],)))
            if x.get("description", "") != y["description"]:
                problems.append("%s.%s.%s: description differs" % (k + (x["column_name"],)))
            elif x.get("description"):
                checked["descriptions"] += 1
            if x.get("is_computed") == "1":
                allowed.append("%s.%s.%s: computed in WWI, created as a plain column" % (k + (x["column_name"],)))
        want = sorted((tuple(cols), pk) for n, cols, pk in keysets(r))
        got = sorted((tuple(cols), pk) for n, cols, pk in keysets(b))
        checked["keys"] += len(want)
        if want != got:
            problems.append("%s.%s: keys differ: %s vs %s" % (k + (want, got)))
        wf = sorted(fks(r).values())
        gf = sorted(fks(b).values())
        checked["foreign keys"] += len(wf)
        if wf != gf:
            problems.append("%s.%s: foreign keys differ" % k)
        if r["table"][0].get("description", "") != b["table"][0]["description"]:
            problems.append("%s.%s: table description differs" % k)
    print("compared: " + ", ".join("%d %s" % (v, k) for k, v in checked.items()))
    print("allowed differences: %d (computed columns created as plain columns)" % len(allowed))
    for p_ in problems:
        print("  x " + p_)
    print("FAILED" if problems else "OK: the pass gives back the structure of the WWI reference case")
    print("record written to %s" % rec_root)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

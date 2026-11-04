"""nsdn - the vault generator (note 143, ADR-0032, ADR-0037).

Reads the model declarations under model/ (model/README.md, ADR-0034) and the source catalogue, and writes the raw
vault as plain-SQL dbt models into the sandbox's dbt project, with their tests. Deterministic: the same declarations,
catalogue and templates always give the same files, byte for byte, and no file carries a date. Run by a person or the
agent layer, never by the runner (ADR-0032 decision 6). Standard library only.

Usage:
    python prototypes/vault_generator/generate.py [--root REPO] [--project DBT_PROJECT] [--check]

Which source tables are generated is listed in scope.txt beside this file; everything declared from those tables is
generated, and a link only when both its hubs are. A pattern this version does not support stops the run with a
message: the generator never guesses (143 section 4 item 4).

--check regenerates in memory and exits 1 if any generated file differs from the one on disk, is missing, or if a file
in the generated folders was not written by the generator.
"""
import argparse
import hashlib
import os
import string
import sys

GENERATOR_VERSION = "0.2.1"
HERE = os.path.dirname(os.path.abspath(__file__))
GENERATED_DIRS = ("models/staging/wwi", "models/raw_vault", "tests/generated")

# 143 section 4 item 4: source type -> DuckDB type. A type not here stops the generator.
TYPE_MAP = {"int": "INTEGER", "bigint": "BIGINT", "smallint": "SMALLINT", "tinyint": "UTINYINT", "bit": "BOOLEAN",
            "nvarchar": "VARCHAR", "varchar": "VARCHAR", "nchar": "VARCHAR", "char": "VARCHAR", "date": "DATE",
            "datetime2": "TIMESTAMP_NS", "geography": "VARCHAR", "varbinary": "VARCHAR"}
INTEGER_TYPES = {"int", "bigint", "smallint", "tinyint"}
TEXT_TYPES = {"nvarchar", "varchar", "nchar", "char"}
NULL_MARK = "\\N"
LOAD_RUN = "'{{ invocation_id }}' as load_run"   # the dbt run that wrote the row (143 section 8 item 3)


class Unsupported(Exception):
    pass


def sha12(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def q(col):
    return '"%s"' % col


def bare(name, prefix):
    return name[len(prefix):] if name.startswith(prefix) else name


def landing_name(table):
    schema, t = table.split(".", 1)
    return (schema + "__" + t).lower()


def staging_name(source, table):
    return "stg_%s__%s" % (source, landing_name(table))


def duck_type(c):
    t = c["type_name"]
    if t in ("decimal", "numeric"):
        return "DECIMAL(%s,%s)" % (c["precision"], c["scale"])
    if t not in TYPE_MAP:
        raise Unsupported("source type %r of column %s has no DuckDB type in TYPE_MAP" % (t, c["column_name"]))
    return TYPE_MAP[t]


def escaped(expr):
    """The escaping of 143 section 3 item 3, so that no two different values give the same hash input."""
    return "replace(replace(%s, '\\', '\\\\'), '|', '\\|')" % expr


def hash_text(raw_cols):
    """Hash input over delivered text: each value escaped, empty marked, joined by |."""
    parts = ["coalesce(%s, '%s')" % (escaped(q(c)), NULL_MARK) for c in raw_cols]
    return " || '|' || ".join(parts) if parts else "''"


def null_hashdiff(n):
    return "sha256('%s')" % "|".join([NULL_MARK] * n)


class Model:
    def __init__(self, root):
        sys.path.insert(0, os.path.join(root, "tools"))
        import model_lib
        self.ml = model_lib
        self.root = root
        self.decls = model_lib.load(root)
        bad = [(r, e) for r, f, s, p, e in self.decls if e]
        if bad:
            raise Unsupported("declarations do not parse: %s" % bad[:3])
        self.by_name = {f["name"]: (r, f, s) for r, f, s, p, e in self.decls}
        self.text = {}
        for r, f, s, p, e in self.decls:
            with open(os.path.join(root, r), encoding="utf-8") as fh:
                self.text[r] = fh.read()
        sources = [(r, f, s) for r, f, s, p, e in self.decls if f["kind"] == "source"]
        if len(sources) != 1:
            raise Unsupported("this version handles exactly one source; found %d" % len(sources))
        self.src_rel, self.src, src_sections = sources[0]
        self.base = {t: fl for t, fl in src_sections["Base tables"]}
        self.cat = {}

    def accepted(self, kind):
        return [(r, f, s) for r, f, s, p, e in self.decls if f["kind"] == kind and f.get("status") == "accepted"]

    def catalogue(self, table):
        if table not in self.cat:
            fl = self.base[table]
            self.cat[table] = self.ml.catalogue(self.root, fl["catalogue"])
        return self.cat[table]

    def columns(self, table):
        return {c["column_name"]: c for c in self.catalogue(table)["columns"]}

    def pk(self, table):
        keys = [k for k in self.catalogue(table)["keys"] if k.get("is_primary_key") == "1"
                and k.get("is_included_column") != "1"]
        keys.sort(key=lambda k: int(k["key_ordinal"]))
        if not keys:
            raise Unsupported("%s has no primary key in its catalogue" % table)
        return [k["column_name"] for k in keys]


def split_qualified(value):
    parts = value.strip().split(".")
    return ".".join(parts[:2]), parts[2]


def key_parts(subject):
    """'Sales.X.A + Sales.X.B' -> ('Sales.X', ['A', 'B'])."""
    tables, cols = set(), []
    for comp in subject.split(" + "):
        t, c = split_qualified(comp)
        tables.add(t)
        cols.append(c)
    if len(tables) != 1:
        raise Unsupported("key parts from more than one table: %s" % subject)
    return tables.pop(), cols


class Generator:
    def __init__(self, root, scope):
        self.m = Model(root)
        self.root = root
        self.scope = scope
        self.source = self.m.src["name"]
        self.key_case = self.m.src["key_case"]
        self.templates = {}
        self.files = {}
        self.staging = {}         # table -> what its staging view must compute
        self.lookup_sources = set()
        for t in scope:
            if t not in self.m.base:
                raise Unsupported("scope table %s is not a base table of %s" % (t, self.m.src_rel))

    # ------------------------------------------------------------------ helpers
    def template(self, name):
        if name not in self.templates:
            with open(os.path.join(HERE, "templates", name), encoding="utf-8") as f:
                self.templates[name] = f.read()
        return self.templates[name]

    def header(self, rel, decl_id, tpl, comment="--"):
        decl_text = self.m.text.get(rel, "")
        tpl_text = self.template(tpl) if tpl.endswith(".sql") else ""
        return ("%s GENERATED by nsdn vault generator %s from %s\n"
                "%s   declaration %s, sha256 %s   template %s, sha256 %s\n"
                "%s DO NOT EDIT. Change the declaration or the template and regenerate (143 section 2).\n"
                % (comment, GENERATOR_VERSION, rel, comment, decl_id, sha12(decl_text), tpl, sha12(tpl_text), comment))

    def emit(self, path, text):
        if path in self.files:
            raise Unsupported("two objects generate %s" % path)
        self.files[path] = text

    def stg(self, table):
        if table not in self.staging:
            self.staging[table] = {"hash_keys": {}, "hashdiffs": {}, "never": set(), "lookups": {}}
        return self.staging[table]

    def rs(self, table):
        return "%s:%s" % (self.source, table)

    def has_versions(self, table):
        fl = self.m.base[table]
        return fl.get("system_time", "none") != "none" or fl.get("audit", "none") != "none"

    def prep(self, table, col, expr=None):
        """143 section 3 item 3: the fixed text form of one key part, or NULL when empty."""
        c = self.m.columns(table)[col]
        t = c["type_name"]
        e = expr or q(col)
        if t in INTEGER_TYPES:
            return "cast(%s as varchar)" % e
        if t in TEXT_TYPES:
            inner = "upper(trim(%s))" % e if self.key_case == "fold" else "trim(%s)" % e
            return "nullif(%s, '')" % escaped(inner)
        raise Unsupported("key column %s.%s of type %s: key preparation not defined in this version" % (table, col, t))

    def hk_expr(self, table, ends):
        """ends: [(key_space, parts)]; a part is a column of the table, or (type_table, column, expression) for a
        value found by lookup. The hash input is the key space and parts of each end, joined by |."""
        pieces, checks = [], []
        for ks, parts in ends:
            pieces.append("'%s'" % ks)
            for part in parts:
                p = self.prep(*part) if isinstance(part, tuple) else self.prep(table, part)
                pieces.append(p)
                checks.append("%s is null" % p)
        return "case when %s then null else sha256(%s) end" % (" or ".join(checks), " || '|' || ".join(pieces))

    def hub_key(self, hub_name):
        rel, f, s = self.m.by_name[hub_name]
        lines = s["Business key"]
        if len(lines) != 1:
            raise Unsupported("%s: more than one mapping is not supported in this version" % hub_name)
        subj, flags = lines[0]
        table, cols = key_parts(subj)
        return table, cols, flags["key_space"]

    def pre_hook(self):
        # 143 section 8 item 3: delete this batch's rows written by any dbt run that did not succeed (a failed
        # attempt, also of a date that succeeded before); rows of a successful run are never deleted.
        return ("{% if is_incremental() %}delete from {{ this }} where batch_id = '" + self.source +
                ":{{ var('load_date') }}' and load_run not in (select invocation_id from nsdn_meta.dbt_invocations "
                "where ok){% endif %}")

    # ------------------------------------------------------------------ selection
    def select(self):
        hubs = {}
        for rel, f, s in self.m.accepted("hub"):
            table, cols, ks = self.hub_key(f["name"])
            if table in self.scope:
                hubs[f["name"]] = (rel, f, table, cols, ks)
        links = {}
        for rel, f, s in self.m.accepted("link"):
            if f["from"] in hubs and f["to"] in hubs:
                ends = {fl.get("end"): (subj, fl) for subj, fl in s["Columns"] if fl.get("end")}
                kept = [(subj, fl) for subj, fl in s["Columns"] if "kept" in fl]
                if len(ends) != 2 or len([x for x in s["Columns"] if x[1].get("end")]) != 2:
                    raise Unsupported("%s: more than one mapping is not supported in this version" % f["name"])
                t_from, c_from = key_parts(ends["from"][0])
                t_to, c_to = key_parts(ends["to"][0])
                if t_from != t_to:
                    raise Unsupported("%s: ends from different tables" % f["name"])
                if t_from not in self.scope:
                    continue
                bridge = f.get("driving") in (None, "none")
                kept_cols = []
                for subj, fl in kept:
                    kt, kc = split_qualified(subj)
                    if not (bridge and fl["kept"].startswith("effectivity satellite") and kt == t_from):
                        raise Unsupported("%s: kept=%s is supported only on a bridge, in its effectivity" % (f["name"], fl["kept"]))
                    kept_cols.append(kc)
                resolve = None
                if "resolve" in ends["to"][1]:
                    resolve = self.parse_resolve(f["name"], ends["to"][1]["resolve"], t_from, c_to)
                links[f["name"]] = dict(rel=rel, f=f, table=t_from, c_from=c_from, c_to=c_to,
                                        from_flags=ends["from"][1], bridge=bridge, kept=kept_cols, resolve=resolve)
        sats = {}
        for rel, f, s in self.m.accepted("satellite"):
            if f["source_table"] in self.scope:
                if f["parent"] not in hubs:
                    raise Unsupported("%s: parent %s is not generated (its table is not in scope, or it is a link)"
                                      % (f["name"], f["parent"]))
                if f["satellite_kind"] not in ("payload", "milestone", "reading"):
                    raise Unsupported("%s: %s satellites are not supported" % (f["name"], f["satellite_kind"]))
                sats[f["name"]] = (rel, f, s)
        refs = {}
        for rel, f, s in self.m.accepted("reference"):
            if f["source_table"] in self.scope:
                refs[f["name"]] = (rel, f, s)
        return hubs, links, sats, refs

    def parse_resolve(self, name, value, table, c_to):
        """'Application.Countries.CountryID to Application.Countries.IsoAlpha3Code, same extract'."""
        try:
            spec, where = [x.strip() for x in value.split(",", 1)]
            a, b = [x.strip() for x in spec.split(" to ")]
        except ValueError:
            raise Unsupported("%s: resolve=%r not understood" % (name, value))
        (ta, ca), (tb, cb) = split_qualified(a), split_qualified(b)
        if ta != tb or where != "same extract" or len(c_to) != 1:
            raise Unsupported("%s: only a lookup within one table of the same extract is supported" % name)
        return dict(table=ta, key=ca, value=cb, own=c_to[0])

    # ------------------------------------------------------------------ the objects
    def gen_hub(self, name, rel, f, table, cols, ks):
        st = self.stg(table)
        hk = "hk_" + bare(name, "hub_")
        st["hash_keys"][hk] = self.hk_expr(table, [(ks, cols)])
        sel = ",\n        ".join(["%s" % hk, "'%s' as key_space" % ks] + [q(c) for c in cols] +
                                 ["load_date", "batch_id", "record_source", "source_ts", "source_seq", LOAD_RUN])
        incoming = ("    select\n        %s\n    from {{ ref('%s') }}\n    where %s is not null"
                    % (sel, staging_name(self.source, table), hk))
        cols_out = ", ".join([hk, "key_space"] + [q(c) for c in cols] +
                             ["load_date", "batch_id", "record_source", "source_ts", "source_seq", "load_run"])
        body = string.Template(self.template("hub.sql")).substitute(
            pre_hook=self.pre_hook(), incoming=incoming, hk=hk, columns=cols_out)
        self.emit("models/raw_vault/hubs/%s.sql" % name, self.header(rel, f["id"], "hub.sql") + "\n" + body)
        return hk

    def gen_audit(self, name, rel, decl_id, owner_kind, hk, tables):
        """One audit satellite for a hub (or a bridge link), over every table that delivers versions of it."""
        audit_cols = sorted({self.m.base[t].get("audit") for t in tables} - {"none", None})
        if len(audit_cols) > 1:
            raise Unsupported("%s: tables name their audit column differently: %s" % (name, audit_cols))
        selects = []
        for t in tables:
            ac = self.m.base[t].get("audit", "none")
            if audit_cols:
                typ = duck_type(self.m.columns(t)[ac]) if ac != "none" else duck_type(
                    self.m.columns([x for x in tables if self.m.base[x].get("audit", "none") != "none"][0])[audit_cols[0]])
                col = "%s as %s, " % (q(ac), q(audit_cols[0])) if ac != "none" else "cast(null as %s) as %s, " % (typ, q(audit_cols[0]))
            else:
                col = ""
            selects.append("    select %s, load_date, batch_id, record_source, source_ts, source_seq, %srow_hash,\n"
                           "           '{{ invocation_id }}' as load_run\n    from {{ ref('%s') }}\n    where %s is not null"
                           % (hk, col, staging_name(self.source, t), hk))
        body = string.Template(self.template("audit.sql")).substitute(
            pre_hook=self.pre_hook(), hk=hk, owner_kind=owner_kind, incoming="\n    union all by name\n".join(selects))
        self.emit("models/raw_vault/satellites/%s/%s.sql" % (self.source, name),
                  self.header(rel, decl_id + " (by rule: audit, 149 Rule 3)", "audit.sql") + "\n" + body)

    def gen_status(self, name, rel, decl_id, title, table, hk, kept=()):
        body = string.Template(self.template("status.sql")).substitute(
            pre_hook=self.pre_hook(), hk=hk, staging=staging_name(self.source, table), source=self.source,
            record_source=self.rs(table), title=title,
            kept_present="".join(", any_value(%s) as %s" % (q(c), q(c)) for c in kept),
            kept_select="".join("\n    p.%s," % q(c) for c in kept))
        self.emit("models/raw_vault/satellites/%s/%s.sql" % (self.source, name),
                  self.header(rel, decl_id, "status.sql") + "\n" + body)

    def gen_link(self, name, L, hubs):
        f, table = L["f"], L["table"]
        st = self.stg(table)
        lb = bare(name, "lnk_")
        hk = "hk_" + lb
        ks_from, ks_to = hubs[f["from"]][4], hubs[f["to"]][4]
        to_parts = L["c_to"]
        if L["resolve"]:
            r = L["resolve"]
            alias = "lk_" + landing_name(r["table"])
            st["lookups"][alias] = (r, self.m.base[r["table"]])
            self.lookup_sources.add(r["table"])
            to_parts = [(r["table"], r["value"], "%s._value" % alias)]
        st["hash_keys"][hk] = self.hk_expr(table, [(ks_from, L["c_from"]), (ks_to, to_parts)])
        st["hash_keys"][hk + "__from"] = self.hk_expr(table, [(ks_from, L["c_from"])])
        st["hash_keys"][hk + "__to"] = self.hk_expr(table, [(ks_to, to_parts)])
        from_col = "hk_" + bare(f["from"], "hub_")
        to_col = "hk_" + bare(f["to"], "hub_")
        if to_col == from_col:
            to_col = "hk_" + lb.split("__", 1)[1]
        sel = ",\n        ".join([hk, "%s__from as %s" % (hk, from_col), "%s__to as %s" % (hk, to_col),
                                  "load_date", "batch_id", "record_source", "source_ts", "source_seq", LOAD_RUN])
        incoming = ("    select\n        %s\n    from {{ ref('%s') }}\n    where %s is not null"
                    % (sel, staging_name(self.source, table), hk))
        cols_out = ", ".join([hk, from_col, to_col, "load_date", "batch_id", "record_source", "source_ts", "source_seq",
                              "load_run"])
        body = string.Template(self.template("link.sql")).substitute(
            pre_hook=self.pre_hook(), incoming=incoming, hk=hk, columns=cols_out)
        self.emit("models/raw_vault/links/%s.sql" % name, self.header(L["rel"], f["id"], "link.sql") + "\n" + body)
        return hk, from_col, to_col

    def gen_satellite_like(self, path, rel, decl_id, kind_note, table, hk_src, hk_out, valid_from, basis,
                           hashdiff, null_hd, payload, audit_union, tpl_label):
        """payload: [(output column, incoming expression)]."""
        payload_incoming = ",\n".join("        %s as %s" % (expr, q(col)) for col, expr in payload)
        payload_plain = ",\n".join("        %s" % q(col) for col, expr in payload)
        payload_select = ",\n".join("    case when i.hk is not null then i.%s else s.%s end as %s" % (q(c), q(c), q(c))
                                    for c, e in payload)
        body = string.Template(self.template("satellite.sql")).substitute(
            pre_hook=self.pre_hook(), kind_note=kind_note, hk_src=hk_src, hk_out=hk_out, valid_from=valid_from,
            basis=basis, hashdiff=hashdiff, null_hd=null_hd, payload_incoming=payload_incoming,
            payload_plain=payload_plain, payload_select=payload_select, known_audit=audit_union, source=self.source,
            staging=staging_name(self.source, table))
        self.emit(path, self.header(rel, decl_id, tpl_label) + "\n" + body)

    def audit_union(self, audit, hk_in_audit, table):
        """The versions the audit satellite knows of this table (143 section 6 item 6), if there is an audit."""
        if not audit or table not in audit[2]:
            return ""
        return ("\n    union\n    select %s, record_source, source_ts, source_seq from {{ ref('%s') }}\n"
                "    where record_source = '%s'" % (hk_in_audit, audit[0], self.rs(table)))

    def valid_from_expr(self, table, value):
        """The declared valid time: its leading term only; what follows it is a note for people."""
        v = value.strip()
        if v.startswith("unknown"):
            return "cast(null as timestamp_ns)", "unknown"
        if v.startswith("none"):
            return "cast(null as timestamp_ns)", "sampled"
        t, col = split_qualified(v.split()[0])
        if t != table:
            raise Unsupported("valid time %s from another table" % value)
        return q(col), "column"

    def satellite_parent(self, name, f, hubs, mandatory):
        """The staging column with the parent's hash key; computed when the satellite's table is not the hub's own."""
        table, parent = f["source_table"], f["parent"]
        h_table, h_cols, ks = hubs[parent][2], hubs[parent][3], hubs[parent][4]
        p_table, p_cols = key_parts(f["parent_key"])
        if p_table != table:
            raise Unsupported("%s: parent_key from another table" % name)
        hk = "hk_" + bare(parent, "hub_")
        if table == h_table and p_cols == h_cols:
            return hk
        if table == h_table:
            raise Unsupported("%s: a parent key other than the hub's key in the hub's own table" % name)
        st = self.stg(table)
        expr = self.hk_expr(table, [(ks, p_cols)])
        if st["hash_keys"].get(hk, expr) != expr:
            raise Unsupported("%s: two different keys of %s in %s" % (name, parent, table))
        st["hash_keys"][hk] = expr
        mandatory.setdefault(table, set()).add("%s is null" % hk)
        return hk

    def gen_satellite(self, name, rel, f, s, hk, audit):
        table = f["source_table"]
        st = self.stg(table)
        cols = []
        for subj, fl in s["Columns"]:
            cols.append(subj)
            for flag in fl:
                if flag not in ("as_delivered", "code", "load", "valid_time"):
                    raise Unsupported("%s: column flag %s not supported in this version" % (name, flag))
            if fl.get("load", "").startswith("never"):
                st["never"].add(subj)
        hashed = [c for c in cols if c not in st["never"]]
        vf, basis = self.valid_from_expr(table, f["valid_time"])
        if basis == "column" and vf.strip('"') not in hashed:
            hashed.append(vf.strip('"'))
        hd = "hd_" + name
        st["hashdiffs"][hd] = "sha256(%s)" % hash_text(hashed)
        milestone = f["satellite_kind"] == "milestone"
        null_hd = null_hashdiff(len(hashed)) if milestone else "cast(null as varchar)"
        note = ("Milestone satellite (143 section 5 item 4): the version before the first is taken to be all empty."
                if milestone else "Payload satellite (143 section 5 item 3).")
        self.gen_satellite_like("models/raw_vault/satellites/%s/%s.sql" % (self.source, name), rel, f["id"], note,
                                table, hk, hk, vf, basis, hd, null_hd, [(c, q(c)) for c in cols],
                                self.audit_union(audit, hk, table), "satellite.sql")

    def gen_reading(self, name, rel, f, s, hk):
        table = f["source_table"]
        cols, keys = [], []
        for subj, fl in s["Columns"]:
            cols.append(subj)
            for flag in fl:
                if flag not in ("reading_key", "repeats"):
                    raise Unsupported("%s: column flag %s not supported on a reading" % (name, flag))
            if fl.get("reading_key") == "yes":
                keys.append(subj)
        if len(keys) != 1:
            raise Unsupported("%s: a reading needs exactly one reading_key" % name)
        vf, basis = self.valid_from_expr(table, f["valid_time"])
        body = string.Template(self.template("reading.sql")).substitute(
            pre_hook=self.pre_hook(), hk_src=hk, hk_out=hk, valid_from=vf, basis=basis, reading_key=q(keys[0]),
            payload=",\n".join("        %s" % q(c) for c in cols), payload_out=",\n".join("    %s" % q(c) for c in cols),
            staging=staging_name(self.source, table))
        self.emit("models/raw_vault/satellites/%s/%s.sql" % (self.source, name),
                  self.header(rel, f["id"], "reading.sql") + "\n" + body)
        return keys[0]

    def gen_effectivity(self, name, L, hubs, audit):
        f, table, c_from = L["f"], L["table"], L["c_from"]
        driving = f["driving"]
        h_table, h_cols = hubs[driving][2], hubs[driving][3]
        if table != h_table or c_from != h_cols:
            raise Unsupported("%s: effectivity whose driving end is not its hub's key in the same table" % name)
        lb = bare(name, "lnk_")
        hk_link = "hk_" + lb
        hk_drv = "hk_" + bare(driving, "hub_")
        start = L["from_flags"].get("effectivity_start", "unknown")
        if start == "load":
            vf, basis = "load_date", "load"
        elif start == "unknown":
            vf, basis = "cast(null as timestamp_ns)", "unknown"
        else:
            vf, basis = self.valid_from_expr(table, start)
        eff = "eff_%s__%s" % (lb, self.source)
        note = ("Effectivity satellite (143 section 5 item 8; 149 Rule 6): per driving key, which link is current from "
                "each source version; empty when none. Ended is derived from the next row. Milestone rule: starts at "
                "the first version with a link.")
        self.gen_satellite_like("models/raw_vault/satellites/%s/%s.sql" % (self.source, eff), L["rel"],
                                f["id"] + " (by rule: effectivity, 149 Rule 6)", note, table, hk_link + "__from",
                                hk_drv, vf, basis, "coalesce(%s, '%s')" % (hk_link, NULL_MARK), "'%s'" % NULL_MARK,
                                [(hk_link, hk_link)], self.audit_union(audit, hk_drv, table), "satellite.sql")
        return eff

    def gen_reference(self, name, rel, f, s):
        table = f["source_table"]
        k_table, k_cols = key_parts(f["key"])
        if k_table != table or len(k_cols) != 1:
            raise Unsupported("%s: reference key must be one column of its own table" % name)
        cols = [subj for subj, fl in s["Columns"]]
        st = self.stg(table)
        hd = "hd_" + name
        st["hashdiffs"][hd] = "sha256(%s)" % hash_text(cols)
        key = k_cols[0]
        self.gen_satellite_like("models/raw_vault/reference/%s/%s.sql" % (self.source, name), rel, f["id"],
                                "Reference table (143 section 5 item 9; 149 Rule 8): every version, keyed by the code.",
                                table, q(key), q(key), "cast(null as timestamp_ns)", "unknown", hd,
                                "cast(null as varchar)", [(c, q(c)) for c in cols], "", "satellite.sql")

    def gen_staging(self, table):
        st = self.staging[table]
        fl = self.m.base[table]
        cols = self.m.catalogue(table)["columns"]
        names = [c["column_name"] for c in cols]
        sys_time = self.m.ml.split_list(fl.get("system_time", "none"))
        end_col = sys_time[1] if len(sys_time) == 2 else None
        delivered = "    select *, false as _is_history from {{ source('landing_%s', '%s') }}" % (self.source, landing_name(table))
        if fl.get("history", "none") != "none":
            delivered += ("\n    union all by name\n    select *, true as _is_history from {{ source('landing_%s', '%s') }}"
                          % (self.source, landing_name(fl["history"])))
        if sys_time == ["none"] or not sys_time:
            src_ts, src_end = "cast(null as timestamp_ns)", "cast(null as varchar)"
        else:
            src_ts = "cast(%s as timestamp_ns)" % q(sys_time[0])
            # The period end is kept as delivered text: SQL Server's open end, 9999-12-31, lies beyond TIMESTAMP_NS,
            # and the fixed ISO form with seven decimals sorts correctly as text (143 section 13 item 2).
            src_end = q(end_col) if end_col else "cast(null as varchar)"
        pk = self.m.pk(table)
        typed = []
        for c in cols:
            t = duck_type(c)
            n = c["column_name"]
            if n == end_col:
                typed.append("        %s /* period end, as delivered text */ as %s" % (q(n), q(n)))
            elif n in st["never"]:
                typed.append("        cast(null as %s) /* load=never, ADR-0033 */ as %s" % (t, q(n)))
            else:
                typed.append("        cast(%s as %s) as %s" % (q(n), t, q(n)))
        lookups = ""
        for alias, (r, rfl) in sorted(st["lookups"].items()):
            kt = duck_type(self.m.columns(r["table"])[r["key"]])
            vt = duck_type(self.m.columns(r["table"])[r["value"]])
            # 143 section 13 item 10: a key named by another identifier is resolved in the same extract, from the
            # current rows of the named table.
            lookups += ("\nleft join (\n    select distinct cast(%s as %s) as _key, cast(%s as %s) as _value\n"
                        "    from {{ source('landing_%s', '%s') }}\n) %s on %s._key = typed.%s"
                        % (q(r["key"]), kt, q(r["value"]), vt, self.source, landing_name(r["table"]),
                           alias, alias, q(r["own"])))
        hashdiffs = "".join("        %s as %s,\n" % (e, k) for k, e in sorted(st["hashdiffs"].items()))
        hash_keys = "".join(",\n    %s as %s" % (e, k) for k, e in sorted(st["hash_keys"].items()))
        body = string.Template(self.template("staging.sql")).substitute(
            source=self.source, pk_raw=", ".join(q(c) for c in pk), period_end_raw=(", " + q(end_col)) if end_col else "",
            delivered=delivered, row_hash_input=hash_text([n for n in names if n != end_col]),
            pk_typed=", ".join("typed.%s" % q(c) for c in pk),
            record_source=self.rs(table), source_ts=src_ts, source_end=src_end,
            hashdiffs=hashdiffs.rstrip("\n"), typed_columns=",\n".join(typed), hash_keys=hash_keys,
            select_all="typed.*" if lookups else "*", lookups=lookups)
        self.emit("models/staging/%s/%s.sql" % (self.source, staging_name(self.source, table)),
                  self.header(self.m.src_rel, self.m.src["id"] + " / " + table + " (catalogue " + fl["catalogue"] + ")",
                              "staging.sql") + "\n" + body)

    # ------------------------------------------------------------------ tests
    def gen_tests(self, hubs, links, sats_all, audits, mandatory):
        y = ["version: 2", "", "sources:", "  - name: landing_%s" % self.source, "    schema: landing",
             "    description: The latest complete extract as landed by runner.py (text), replaced every load.",
             "    tables:"]
        for t in sorted(set(self.staging) | self.lookup_sources):
            y.append("      - name: %s" % landing_name(t))
            h = self.m.base[t].get("history", "none")
            if h != "none" and t in self.staging:
                y.append("      - name: %s" % landing_name(h))
        self.emit("models/staging/%s/_sources.yml" % self.source,
                  self.header(self.m.src_rel, self.m.src["id"], "(sources)", "#") + "\n" + "\n".join(y) + "\n")

        def rel_test(to_model, field):
            return "          - relationships: {arguments: {to: \"ref('%s')\", field: %s}}" % (to_model, field)

        y = ["version: 2", "", "models:"]
        for name, (hk, from_col, to_col, from_hub, to_hub) in sorted(links.items()):
            y += ["  - name: %s" % name, "    columns:",
                  "      - name: %s" % hk, "        data_tests: [unique, not_null]",
                  "      - name: %s" % from_col, "        data_tests:", rel_test(from_hub, "hk_" + bare(from_hub, "hub_")),
                  "      - name: %s" % to_col, "        data_tests:", rel_test(to_hub, "hk_" + bare(to_hub, "hub_"))]
        for name, hk in sorted(hubs.items()):
            y += ["  - name: %s" % name, "    columns:", "      - name: %s" % hk, "        data_tests: [unique, not_null]"]
        for name, (hk, parent, field, kind) in sorted(sats_all.items()):
            y += ["  - name: %s" % name, "    columns:", "      - name: %s" % hk, "        data_tests:",
                  "          - not_null", rel_test(parent, field)]
        self.emit("models/raw_vault/_generated.yml",
                  self.header(self.m.src_rel, "all generated raw-vault models", "(tests)", "#") + "\n" + "\n".join(y) + "\n")

        def test(name, sql, rel="(tests)", severity=None):
            cfg = "{{ config(severity='%s') }}\n\n" % severity if severity else ""
            self.emit("tests/generated/%s.sql" % name, self.header(self.m.src_rel, name, rel) + "\n" + cfg + sql)

        for name, (hk, parent, field, kind) in sorted(sats_all.items()):
            key = {"status": "%s, load_date" % hk, "reading": "%s, %s" % (hk, kind[1] if isinstance(kind, tuple) else ""),
                   }.get(kind if isinstance(kind, str) else kind[0], "%s, record_source, source_ts, source_seq" % hk)
            test("%s__version_unique" % name,
                 "-- 143 section 10 item 2: one row per parent and source version (per reading for a reading).\n"
                 "select %s, count(*) as n\nfrom {{ ref('%s') }}\ngroup by all\nhaving count(*) > 1\n" % (key, name))
        for owner, (audit, hk, tables) in sorted(audits.items()):
            for table in tables:
                stg = staging_name(self.source, table)
                tag = "%s__%s" % (audit, landing_name(table))
                test("%s__complete" % tag,
                     "-- 143 section 10 item 3: every source version delivered now is in the audit satellite, exactly once.\n"
                     "select s.%s, s.record_source, s.source_ts, s.source_seq\nfrom {{ ref('%s') }} s\n"
                     "where s.%s is not null\n  and (select count(*) from {{ ref('%s') }} a\n"
                     "       where a.%s = s.%s and a.record_source = s.record_source\n"
                     "         and a.source_ts is not distinct from s.source_ts and a.source_seq = s.source_seq) <> 1\n"
                     % (hk, stg, hk, audit, hk, hk))
                test("%s__rewritten_version" % tag,
                     "-- 143 section 6 item 5 and section 10 item 4: the same source version delivered with different content.\n"
                     "select s.%s, s.source_ts, s.source_seq\nfrom {{ ref('%s') }} s\njoin {{ ref('%s') }} a\n"
                     "  on a.%s = s.%s and a.record_source = s.record_source\n"
                     " and a.source_ts is not distinct from s.source_ts and a.source_seq = s.source_seq\n"
                     "where a.row_hash <> s.row_hash\n" % (hk, stg, audit, hk, hk))
            test("%s__late_arrivals" % audit,
                 "-- 143 section 6 item 6 and section 10 item 5: versions of this batch older than the latest one loaded\n"
                 "-- before it, per key and source table (compared with that one version only, so the cost is linear).\n"
                 "with latest_before as (\n    select %s, record_source, source_ts, source_seq\n"
                 "    from {{ ref('%s') }}\n    where batch_id < '%s:{{ var('load_date') }}'\n"
                 "    qualify row_number() over (partition by %s, record_source order by source_ts desc, source_seq desc) = 1\n)\n"
                 "select n.%s, n.record_source, n.source_ts, n.source_seq\nfrom {{ ref('%s') }} n\n"
                 "join latest_before o on o.%s = n.%s and o.record_source = n.record_source\n"
                 "where n.batch_id = '%s:{{ var('load_date') }}'\n"
                 "  and (o.source_ts, o.source_seq) > (n.source_ts, n.source_seq)\n"
                 % (hk, audit, self.source, hk, hk, audit, hk, hk, self.source), severity="warn")
        for table in sorted(self.staging):
            stg = staging_name(self.source, table)
            fl = self.m.base[table]
            h = fl.get("history", "none")
            names = [c["column_name"] for c in self.m.catalogue(table)["columns"]]
            st_cols = self.m.ml.split_list(fl.get("system_time", "none"))
            end_col = st_cols[1] if len(st_cols) == 2 else None
            pk = ", ".join(q(c) for c in self.m.pk(table))
            delivered = "select *, false as h from {{ source('landing_%s', '%s') }}" % (self.source, landing_name(table))
            twice = "0"
            if h != "none":
                delivered += ("\n    union all by name\n    select *, true as h from {{ source('landing_%s', '%s') }}"
                              % (self.source, landing_name(h)))
                twice = ("(select count(*) from k a where a.h and exists (select 1 from k b where not b.h "
                         "and b.pk = a.pk and b.rh = a.rh and b.e is not distinct from a.e))")
            test("%s__nothing_dropped" % stg,
                 "-- 143 section 10: every delivered row reaches staging, except a history row identical to a current\n"
                 "-- row (the same row delivered twice, 149 section 5).\n"
                 "with d as (\n    %s\n),\nk as (\n    select h, (%s) as pk, sha256(%s) as rh, %s as e from d\n)\n"
                 "select (select count(*) from k) - %s as expected, (select count(*) from {{ ref('%s') }}) as staged\n"
                 "where (select count(*) from k) - %s <> (select count(*) from {{ ref('%s') }})\n"
                 % (delivered, pk, hash_text([n for n in names if n != end_col]),
                    q(end_col) if end_col else "null", twice, stg, twice, stg))
        for table, checks in sorted(mandatory.items()):
            stg = staging_name(self.source, table)
            cond = "\n   or ".join(sorted(checks))
            test("%s__mandatory_keys" % stg,
                 "-- 143 section 3 item 5 and section 10 item 6: a hub key, a parent key or a mandatory link end that\n"
                 "-- arrived empty, or that a lookup did not resolve.\n"
                 "select *\nfrom {{ ref('%s') }}\nwhere %s\n" % (stg, cond))

    # ------------------------------------------------------------------ all
    def run(self):
        hubs, links, sats, refs = self.select()
        hub_hk, sats_all, link_info, mandatory, audits = {}, {}, {}, {}, {}
        for name, (rel, f, table, cols, ks) in sorted(hubs.items()):
            hub_hk[name] = self.gen_hub(name, rel, f, table, cols, ks)
            mandatory.setdefault(table, set()).add("%s is null" % hub_hk[name])
        # Satellite parents first, so that every table's hash keys are known.
        sat_hk = {}
        for name, (rel, f, s) in sorted(sats.items()):
            sat_hk[name] = self.satellite_parent(name, f, hubs, mandatory)
        # Audit satellites: per hub, over its own table and every other table delivering non-reading satellites of it.
        for name, (rel, f, table, cols, ks) in sorted(hubs.items()):
            tables = [table] if self.has_versions(table) else []
            for sn, (srel, sf, ss) in sorted(sats.items()):
                t = sf["source_table"]
                if sf["parent"] == name and sf["satellite_kind"] != "reading" and t != table and self.has_versions(t) \
                        and t not in tables:
                    tables.append(t)
            if tables:
                a = "sat_%s__%s__audit" % (bare(name, "hub_"), self.source)
                self.gen_audit(a, rel, f["id"], "hub", hub_hk[name], tables)
                audits[name] = (a, hub_hk[name], tables)
                sats_all[a] = (hub_hk[name], name, hub_hk[name], "version")
            if self.m.base[table].get("extract") == "full":
                sts = "sts_%s__%s" % (bare(name, "hub_"), self.source)
                self.gen_status(sts, rel, f["id"] + " (by rule: status tracking, 149 Rule 7)",
                                "Status-tracking satellite (143 section 5 item 7; 149 Rule 7)", table, hub_hk[name])
                sats_all[sts] = (hub_hk[name], name, hub_hk[name], "status")
        for name, L in sorted(links.items()):
            f, table = L["f"], L["table"]
            hk, from_col, to_col = self.gen_link(name, L, hubs)
            link_info[name] = (hk, from_col, to_col, f["from"], f["to"])
            if f.get("optional") != "yes":
                mandatory.setdefault(table, set()).add("%s__to is null" % hk)
            if L["bridge"]:
                if L["from_flags"].get("effectivity_start") != "presence in a complete extract" \
                        or self.m.base[table].get("extract") != "full":
                    raise Unsupported("%s: a bridge's effectivity is supported by presence in a full extract only" % name)
                lb = bare(name, "lnk_")
                eff = "eff_%s__%s" % (lb, self.source)
                self.gen_status(eff, L["rel"], f["id"] + " (by rule: effectivity of a bridge, by presence, 149 Rule 6)",
                                "Effectivity of a bridge by presence (143 section 5 item 8; 149 section 4, link 15)",
                                table, hk, L["kept"])
                sats_all[eff] = (hk, name, hk, "status")
                mandatory.setdefault(table, set()).add("%s__from is null" % hk)
                if self.has_versions(table):
                    a = "sat_%s__%s__audit" % (lb, self.source)
                    self.gen_audit(a, L["rel"], f["id"], "bridge link", hk, [table])
                    audits[name] = (a, hk, [table])
                    sats_all[a] = (hk, name, hk, "version")
            else:
                eff = self.gen_effectivity(name, L, hubs, audits.get(f["driving"]))
                drv = f["driving"]
                sats_all[eff] = (hub_hk[drv], drv, hub_hk[drv], "version")
        for name, (rel, f, s) in sorted(sats.items()):
            parent = f["parent"]
            if f["satellite_kind"] == "reading":
                rk = self.gen_reading(name, rel, f, s, sat_hk[name])
                sats_all[name] = (sat_hk[name], parent, hub_hk[parent], ("reading", q(rk)))
            else:
                self.gen_satellite(name, rel, f, s, sat_hk[name], audits.get(parent))
                sats_all[name] = (sat_hk[name], parent, hub_hk[parent], "version")
        for name, (rel, f, s) in sorted(refs.items()):
            self.gen_reference(name, rel, f, s)
            self.stg(f["source_table"])
        for table in sorted(self.staging):
            self.gen_staging(table)
        self.gen_tests(hub_hk, link_info, sats_all, audits, mandatory)
        return self.files


def existing_generated(project):
    out = set()
    for d in GENERATED_DIRS:
        base = os.path.join(project, d)
        for dirpath, dirnames, filenames in os.walk(base):
            for fn in filenames:
                out.add(os.path.relpath(os.path.join(dirpath, fn), project).replace(os.sep, "/"))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=os.path.abspath(os.path.join(HERE, "..", "..")))
    ap.add_argument("--project", default=None, help="the dbt project (default: prototypes/wwi_sandbox/dbt)")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    project = args.project or os.path.join(args.root, "prototypes", "wwi_sandbox", "dbt")
    with open(os.path.join(HERE, "scope.txt"), encoding="utf-8") as f:
        scope = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    try:
        files = Generator(args.root, scope).run()
    except Unsupported as e:
        print("generator stopped: %s" % e, file=sys.stderr)
        return 2
    on_disk = existing_generated(project)
    stray = sorted(on_disk - set(files))
    if args.check:
        bad = []
        for p, text in sorted(files.items()):
            full = os.path.join(project, p)
            if not os.path.isfile(full):
                bad.append("missing: " + p)
            else:
                with open(full, encoding="utf-8", newline="") as f:
                    if f.read() != text:
                        bad.append("differs from the generator's output (edited?): " + p)
        bad += ["not written by the generator: " + p for p in stray]
        for b in bad:
            print(b)
        print("%d generated files, %d problem(s)" % (len(files), len(bad)))
        return 1 if bad else 0
    for p in stray:
        os.remove(os.path.join(project, p))
    for p, text in sorted(files.items()):
        full = os.path.join(project, p)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print("%d files written, %d removed, into %s" % (len(files), len(stray), project))
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""The business vault, the marts and the analyses of note 141 (ADR-0039, ADR-0040), written from model/.

Called by generate.py. Every object is one query with a knowledge date as its parameter (141 section 2), written twice:
as a dbt model (a table at the load date, reading the tables of the objects it depends on) and as a DuckDB table macro
`<schema>.<object>__as_known(known_on)` (reading their macros), created after the table by a generated dbt macro. A
generated test compares the two at the load date. A pattern this module does not support stops the generator.
"""
import re

UNKNOWN = "0" * 64
SCHEMA = {"pit": "business_vault", "bridge": "business_vault", "computed": "business_vault",
          "dimension": "marts", "fact": "marts", "analysis": "analyses"}
ORDER = "source_ts desc, source_seq desc"          # the last row in source order (141 section 3 rule 2)
CALENDAR = ["date", "year", "quarter", "month", "month_start", "is_complete_month"]
LOAD = "cast('{{ var('load_date') }}' as date)"
MONTH = "'%Y-%m'"


def q(col):
    return '"%s"' % col


def rv(name):
    return "{{ ref('%s') }}" % name


def ind(sql, n=4):
    return "\n".join(" " * n + l if l else l for l in sql.split("\n"))


class MartGenerator:
    def __init__(self, gen, unsupported, staging_name):
        self.g, self.m, self.U, self.source = gen, gen.m, unsupported, gen.source
        self.staging_name = staging_name
        self.kinds = {f["name"]: f["kind"] for r, f, s, p, e in self.m.decls}

    # ---- helpers -----------------------------------------------------------------------------------------------
    def decl(self, name, kind=None):
        if name not in self.m.by_name:
            raise self.U("%s is not declared" % name)
        r, f, s = self.m.by_name[name]
        if kind and f["kind"] != kind:
            raise self.U("%s is a %s, not a %s" % (name, f["kind"], kind))
        if f.get("status") != "accepted":
            raise self.U("%s is not accepted" % name)
        return r, f, s

    def K(self, mode):
        return LOAD if mode == "T" else "known_on"

    def obj(self, name, mode):
        if mode == "T":
            return rv(name)
        return "%s.%s__as_known(known_on)" % (SCHEMA[self.kinds[name]], name)

    def bk(self, hub):
        """(source table, [business key columns]) of a hub with one mapping."""
        r, f, s = self.decl(hub, "hub")
        lines = s["Business key"]
        if len(lines) != 1:
            raise self.U("%s has %d mappings; the marts handle one" % (hub, len(lines)))
        parts = [p.strip() for p in lines[0][0].split(" + ")]
        return ".".join(parts[0].split(".")[:2]), [p.split(".")[2] for p in parts]

    def present(self, hub, mode):
        """The rows of a hub that are known and present as known (141 section 3 rules 1 and 4)."""
        hk, k = "hk_" + hub[4:], self.K(mode)
        sts = "sts_%s__%s" % (hub[4:], self.source)
        if "models/raw_vault/satellites/%s/%s.sql" % (self.source, sts) not in self.g.files:
            raise self.U("%s has no status-tracking satellite, so presence cannot be known (141 section 3 rule 4)" % hub)
        return ("select h.* from %s h\n"
                "join (select %s, status from %s where load_date <= %s\n"
                "      qualify row_number() over (partition by %s order by load_date desc) = 1) s on s.%s = h.%s\n"
                "where h.load_date <= %s and s.status in ('present', 'reappeared')"
                % (rv(hub), hk, rv(sts), k, hk, hk, hk, k))

    def sat_join(self, alias, sat, pa, hk, mode="T"):
        # The pointer names one source version, which the raw vault stores once (its version_unique tests); the
        # knowledge-date bound is a second guard, so that a macro can never read a row loaded after its date
        # (review of the build, finding 1).
        return ("left join %s %s on %s.%s = %s.%s and %s.record_source = %s.%s__record_source\n"
                "    and %s.source_ts is not distinct from %s.%s__source_ts and %s.source_seq = %s.%s__source_seq\n"
                "    and %s.load_date <= %s"
                % (rv(sat), alias, alias, hk, pa, hk, alias, pa, sat, alias, pa, sat, alias, pa, sat, alias, self.K(mode)))

    def sat_cols(self, sat):
        return [c for c, fl in self.decl(sat, "satellite")[2]["Columns"]]

    def expr(self, text, alias, sat):
        if not re.fullmatch(r"[A-Za-z0-9_ +\-*()]+", text):
            raise self.U("expression %r is beyond basic arithmetic (ADR-0024)" % text)
        cols = self.sat_cols(sat)
        def one(m):
            if m.group(0) not in cols:
                raise self.U("%s is not a column of %s" % (m.group(0), sat))
            return "%s.%s" % (alias, q(m.group(0)))
        return re.sub(r"[A-Za-z_][A-Za-z0-9_]*", one, text)

    def walk(self, brg):
        """[(name, link, from name, from hub, to hub)] of a bridge, checked."""
        r, f, s = self.decl(brg, "bridge")
        hubs, out = {"start": f["start"]}, []
        for name, fl in s["Walk"]:
            lr, lf, ls = self.decl(fl["link"], "link")
            frm = hubs.get(fl.get("from"))
            if frm is None:
                raise self.U("%s: step %s leaves %r, which is not reached before it" % (brg, name, fl.get("from")))
            if lf["from"] != frm or lf["driving"] != frm:
                raise self.U("%s: %s is not driven by %s, so a step over it could give several keys" % (brg, fl["link"], frm))
            if lf["to"] == frm:
                raise self.U("%s: %s joins a hub to itself; not supported" % (brg, fl["link"]))
            hubs[name] = lf["to"]
            out.append((name, fl["link"], fl["from"], frm, lf["to"]))
        return f["start"], out

    def attr(self, fl, pit, hub, brg, joins, seen, mode, where):
        """The SQL expression of one attribute, adding the joins it needs. p is the object's own point-in-time table."""
        src, via = fl.get("from"), fl.get("via")
        alias, apit, ahub = "p", pit, hub
        if via is not None:
            reached = {n: t for n, l, fr, fh, t in self.walk(brg)[1]} if brg else {}
            if via not in reached:
                raise self.U("%s: %s is not reached by %s" % (where, via, brg))
            apit = fl.get("pit")
            if apit is None or self.decl(apit, "pit")[1]["hub"] != reached[via]:
                raise self.U("%s: via=%s needs pit= of %s" % (where, via, reached[via]))
            alias, ahub = "v_" + via, reached[via]
            if alias not in seen:
                seen.add(alias)
                joins.append("left join %s %s on %s.hk_%s = b.hk_%s" % (self.obj(apit, mode), alias, alias, ahub[4:], via))
        kind, col = src.split(".", 1)
        if kind == "key":
            if col not in self.bk(ahub)[1]:
                raise self.U("%s: %s is not the business key of %s" % (where, col, ahub))
            return "%s.%s" % (alias, q(col))
        if self.kinds.get(kind) == "satellite":
            if kind not in [n for n, _ in self.decl(apit, "pit")[2].get("Satellites", [])] or col not in self.sat_cols(kind):
                raise self.U("%s: %s.%s is not reachable through %s" % (where, kind, col, apit))
            sa = "s_%s_%s" % (alias, kind)
            if sa not in seen:
                seen.add(sa)
                joins.append(self.sat_join(sa, kind, alias, "hk_" + ahub[4:], mode))
            return "%s.%s" % (sa, q(col))
        if self.kinds.get(kind) == "computed" and via is None:
            cr, cf, cs = self.decl(kind, "computed")
            if cf["hub"] != hub or col not in [n for n, _ in cs["Values"]]:
                raise self.U("%s: %s.%s is not a value on %s" % (where, kind, col, hub))
            ca = "c_" + kind
            if ca not in seen:
                seen.add(ca)
                joins.append("left join %s %s on %s.hk_%s = p.hk_%s" % (self.obj(kind, mode), ca, ca, hub[4:], hub[4:]))
            return "%s.%s" % (ca, col)
        raise self.U("%s: from=%s is not supported" % (where, src))

    # ---- the six kinds -----------------------------------------------------------------------------------------
    def pit_sql(self, f, s, mode):
        hub = f["hub"]
        hk, k = "hk_" + hub[4:], self.K(mode)
        ctes = ["keys as (\n%s\n)" % ind(self.present(hub, mode))]
        cols = ["k." + hk] + ["k." + q(c) for c in self.bk(hub)[1]]
        joins = []
        for i, (sat, fl) in enumerate(s.get("Satellites", [])):
            if self.decl(sat, "satellite")[1]["parent"] != hub:
                raise self.U("%s is not a satellite of %s" % (sat, hub))
            ctes.append("s%d as (\n    select %s, record_source, source_ts, source_seq from %s where load_date <= %s\n"
                        "    qualify row_number() over (partition by %s order by %s) = 1\n)" % (i, hk, rv(sat), k, hk, ORDER))
            cols += ["s%d.%s as %s__%s" % (i, c, sat, c) for c in ("record_source", "source_ts", "source_seq")]
            joins.append("left join s%d on s%d.%s = k.%s" % (i, i, hk, hk))
        return "with " + ",\n".join(ctes) + "\nselect " + ",\n    ".join(cols) + "\nfrom keys k" + "".join("\n" + j for j in joins)

    def bridge_sql(self, f, s, mode, name):
        start, steps = self.walk(name)
        hk0, k = "hk_" + start[4:], self.K(mode)
        ctes = ["st as (\n%s\n)" % ind(self.present(start, mode))]
        cols, joins, expr = ["st." + hk0], [], {"start": "st." + hk0}
        for n, link, frm, fh, th in steps:
            a, b, l = "hk_" + fh[4:], "hk_" + th[4:], "hk_" + link[4:]
            eff = "eff_%s__%s" % (link[4:], self.source)
            ctes.append("e_%s as (\n    select e.%s as hk_from, l.%s as hk_to\n"
                        "    from (select %s, %s as hk_link from %s where load_date <= %s\n"
                        "          qualify row_number() over (partition by %s order by %s) = 1) e\n"
                        "    join %s l on l.%s = e.hk_link and l.load_date <= %s\n)"
                        % (n, a, b, a, q(l), rv(eff), k, a, ORDER, rv(link), l, k))
            ctes.append("p_%s as (\n    select h.%s as hk from (\n%s\n    ) h\n)" % (n, b, ind(self.present(th, mode), 8)))
            joins.append("left join e_%s on e_%s.hk_from = %s" % (n, n, expr[frm]))
            joins.append("left join p_%s on p_%s.hk = e_%s.hk_to" % (n, n, n))
            cols.append("p_%s.hk as hk_%s" % (n, n))
            cols.append("case when %s is null then 'not walked' when e_%s.hk_to is null then 'no link'\n"
                        "         when p_%s.hk is null then 'not present' else 'reached' end as %s__status" % (expr[frm], n, n, n))
            expr[n] = "p_%s.hk" % n
        return "with " + ",\n".join(ctes) + "\nselect " + ",\n    ".join(cols) + "\nfrom st" + "".join("\n" + j for j in joins)

    def computed_sql(self, f, s, mode):
        hub, pit, sat = f["hub"], f["pit"], f["satellite"]
        hk = "hk_" + hub[4:]
        if self.decl(pit, "pit")[1]["hub"] != hub or sat not in [n for n, _ in self.decl(pit)[2].get("Satellites", [])]:
            raise self.U("%s does not point at %s" % (pit, sat))
        vals = ["cast(%s as %s) as %s" % (self.expr(fl["expr"], "s", sat), fl["type"], n) for n, fl in s["Values"]]
        return ("select p.%s, '%s' as rule, %d as rule_version,\n    %s\nfrom %s p\n%s"
                % (hk, f["rule"], int(f["rule_version"]), ",\n    ".join(vals), self.obj(pit, mode), self.sat_join("s", sat, "p", hk, mode)))

    def dimension_sql(self, f, s, mode, name):
        if f.get("rule") == "calendar":
            if [n for n, _ in s["Attributes"]] != CALENDAR:
                raise self.U("%s: a calendar has exactly the attributes %s" % (name, CALENDAR))
            k = self.K(mode)
            return ("select cast(t.d as date) as date, cast(year(t.d) as integer) as year, cast(quarter(t.d) as integer) as quarter,\n"
                    "    strftime(t.d, %s) as month, cast(date_trunc('month', t.d) as date) as month_start,\n"
                    "    last_day(cast(t.d as date)) <= %s as is_complete_month\n"
                    "from generate_series(cast('%s' as timestamp), cast(last_day(%s) as timestamp), interval 1 day) as t(d)"
                    % (MONTH, k, f["first_date"], k))
        hub, pit, brg = f["hub"], f["pit"], f.get("bridge")
        hk = "hk_" + hub[4:]
        joins, seen = [], set()
        if brg:
            joins.append("left join %s b on b.%s = p.%s" % (self.obj(brg, mode), hk, hk))
        cols, unk = ["p." + hk], ["'%s' as %s" % (UNKNOWN, hk)]
        for n, fl in s["Attributes"]:
            e = self.attr(fl, pit, hub, brg, joins, seen, mode, name + "." + n)
            if "when_none" in fl:
                e = "case when b.%s__status = 'no link' then '%s' else %s end" % (fl["via"], fl["when_none"].replace("'", "''"), e)
            cols.append("%s as %s" % (e, n))
            unk.append(("'%s'" % fl["unknown"].replace("'", "''") if "unknown" in fl else "null") + " as " + n)
        return ("select " + ",\n    ".join(cols) + "\nfrom %s p" % self.obj(pit, mode) + "".join("\n" + j for j in joins)
                + "\nunion all\n-- the unknown member, so that every fact row finds exactly one row (146 consideration 8)\nselect "
                + ", ".join(unk))

    def fact_sql(self, f, s, mode, name):
        pit, brg = f["pit"], f["bridge"]
        hub = self.decl(pit, "pit")[1]["hub"]
        hk = "hk_" + hub[4:]
        if self.walk(brg)[0] != hub:
            raise self.U("%s does not start at %s" % (brg, hub))
        joins, seen, cols = ["left join %s b on b.%s = p.%s" % (self.obj(brg, mode), hk, hk)], set(), ["p." + hk]
        for n, fl in s["Keys"]:
            if "from" in fl:
                e = self.attr(fl, pit, hub, brg, joins, seen, mode, name + "." + n)
            else:
                if n != "hk_" + fl.get("via", ""):
                    raise self.U("%s: a reached key is named hk_<step>" % n)
                e = "b." + n
                if "dimension" in fl:   # unplaced lines stay, on the unknown member (ADR-0040 decision 1)
                    e = "coalesce(%s, '%s')" % (e, UNKNOWN)
            cols.append("%s as %s" % (e, n))
        for n, fl in s["Measures"]:
            if not fl.get("additive"):
                raise self.U("%s.%s has no aggregation contract (146 consideration 6)" % (name, n))
            if "via" in fl:
                raise self.U("%s.%s: a measure is measured at the grain, not reached over a link (146 consideration 5)" % (name, n))
            cols.append("%s as %s" % (self.attr(fl, pit, hub, brg, joins, seen, mode, name + "." + n), n))
        return "select " + ",\n    ".join(cols) + "\nfrom %s p" % self.obj(pit, mode) + "".join("\n" + j for j in joins)

    def dim_join(self, fact_sections, dim):
        ks = [(k, kf) for k, kf in fact_sections["Keys"] if kf.get("dimension") == dim and "role" not in kf]
        if len(ks) != 1:
            raise self.U("the fact table has %d default keys for %s" % (len(ks), dim))
        df = self.decl(dim, "dimension")[1]
        return ks[0][0], ("date" if df.get("rule") == "calendar" else "hk_" + df["hub"][4:])

    def analysis_sql(self, f, s, mode, name):
        fr, ff, fs = self.decl(f["fact"], "fact")
        measures, keys = dict(fs["Measures"]), dict(fs["Keys"])
        joins, rows, vals = {}, [], []
        for n, fl in s["Rows"]:
            dim, col = fl["from"].split(".", 1)
            if col not in [a for a, _ in self.decl(dim, "dimension")[2]["Attributes"]]:
                raise self.U("%s: %s has no attribute %s" % (name, dim, col))
            k, dk = self.dim_join(fs, dim)
            joins[dim] = "left join %s d_%s on d_%s.%s = f.%s" % (self.obj(dim, mode), dim[4:], dim[4:], dk, k)
            rows.append(("d_%s.%s" % (dim[4:], col), n))
        for n, fl in s["Values"]:
            if "sum" in fl:
                if measures.get(fl["sum"], {}).get("additive") != "all":
                    raise self.U("%s: %s may not be summed along every dimension (146 consideration 6)" % (name, fl["sum"]))
                vals.append("sum(f.%s) as %s" % (fl["sum"], n))
            elif "count_distinct" in fl and fl["count_distinct"] in keys:
                vals.append("count(distinct f.%s) as %s" % (fl["count_distinct"], n))
            else:
                raise self.U("%s: value %s is not supported" % (name, n))
        return ("select " + ",\n    ".join(["%s as %s" % r for r in rows] + vals) + "\nfrom %s f" % self.obj(f["fact"], mode)
                + "".join("\n" + j for j in joins.values()) + "\ngroup by " + ", ".join(e for e, n in rows))

    # ---- tests --------------------------------------------------------------------------------------------------
    def stg(self, table):
        return "(select * from %s where not _is_history)" % rv(self.staging_name(self.source, table))

    def lineage_sql(self, name, f, s):
        """141 section 9 item 10: the fact table against the delivered rows, joined on the source's own identifiers."""
        hub = self.decl(f["pit"], "pit")[1]["hub"]
        t0 = self.bk(hub)[0]
        node, joins = {"start": ("t0", t0)}, []
        tocol = {}
        def link_to(link, table):
            cols = [(subj, fl) for subj, fl in self.decl(link, "link")[2]["Columns"] if fl.get("end") == "to"]
            if len(cols) != 1 or "resolve" in cols[0][1] or ".".join(cols[0][0].split(".")[:2]) != table:
                raise self.U("lineage: %s is not one plain column of %s" % (link, table))
            return cols[0][0].split(".")[2]
        for n, link, frm, fh, th in self.walk(f["bridge"])[1]:
            fa, ft = node[frm]
            tt, tk = self.bk(th)
            if len(tk) != 1:
                raise self.U("lineage: %s has a composite key" % th)
            joins.append("left join %s n_%s on n_%s.%s = %s.%s" % (self.stg(tt), n, n, q(tk[0]), fa, q(link_to(link, ft))))
            node[n] = ("n_" + n, tt)
        exp, act, ajoins = [], [], []
        for n, fl in s["Keys"] + s["Measures"]:
            via, src = fl.get("via"), fl.get("from")
            a = node[via][0] if via else "t0"
            if src is None:
                dim = fl.get("dimension")
                if not dim:
                    continue
                dr, df, ds = self.decl(dim, "dimension")
                da, dhub = "d_" + n, df["hub"]
                ajoins.append("left join %s %s on %s.hk_%s = f.%s" % (rv(dim), da, da, dhub[4:], n))
                if node[via][1] != self.bk(dhub)[0]:
                    raise self.U("lineage: %s reaches %s, not the table of %s" % (n, node[via][1], dhub))
                own = "%s.%s" % (a, q(self.bk(dhub)[1][0]))      # empty when the row was not delivered
                steps = {st[0]: st for st in self.walk(df["bridge"])[1]} if df.get("bridge") else {}
                # Every attribute the dimension shows, its labels included (review of the build, finding 5): the value
                # the delivered rows give, the unknown member's label where the row was not delivered, and the label
                # for 'no link' where the delivered relationship is empty.
                for an, afl in ds["Attributes"]:
                    kind2, col = afl["from"].split(".", 1)
                    unk = ("'%s'" % afl["unknown"].replace("'", "''")) if "unknown" in afl else "null"
                    w = afl.get("via")
                    if w is None:
                        val = "%s.%s" % (a, q(col))
                    else:
                        lcol = "%s.%s" % (a, q(link_to(steps[w][1], node[via][1])))
                        if kind2 == "key":
                            val = lcol
                        else:
                            xt, xk = self.bk(steps[w][4])
                            xa = "x_%s_%s" % (n, w)
                            joins.append("left join %s %s on %s.%s = %s" % (self.stg(xt), xa, xa, q(xk[0]), lcol))
                            val = "%s.%s" % (xa, q(col))
                        if "when_none" in afl:
                            val = "case when %s is null then '%s' else %s end" % (lcol, afl["when_none"].replace("'", "''"), val)
                    exp.append("case when %s is null then %s else %s end" % (own, unk, val))
                    act.append("%s.%s" % (da, an))
                continue
            kind, col = src.split(".", 1)
            if self.kinds.get(kind) == "computed":
                cf, cs = self.decl(kind)[1], dict(self.decl(kind)[2]["Values"])
                exp.append("cast(%s as %s)" % (self.expr(cs[col]["expr"], "t0", cf["satellite"]), cs[col]["type"]))
            else:
                exp.append("%s.%s" % (a, q(col)))
            act.append("f." + n)
        e = "select " + ", ".join(exp) + "\n    from %s t0" % self.stg(t0) + "".join("\n    " + j for j in joins)
        a = "select " + ", ".join(act) + "\n    from %s f" % rv(name) + "".join("\n    " + j for j in ajoins)
        return "with delivered as (\n    %s\n),\nmart as (\n    %s\n)\n(select 'delivered, not in the mart' as problem, * from (select * from delivered except all select * from mart))\nunion all\n(select 'in the mart, not delivered' as problem, * from (select * from mart except all select * from delivered))" % (e, a)

    def tests(self, rel, f, s):
        name, kind = f["name"], f["kind"]
        schema = SCHEMA[kind]
        out = []   # (test name, severity, comment, sql)
        macro = "%s.%s__as_known(%s)" % (schema, name, LOAD)
        out.append(("equals_as_known", "error", "141 section 2: the table is its own table macro at the load date, row for row\n-- with multiplicity (except all; review of the build, finding 2).",
                    "(select * from %s except all select * from %s)\nunion all\n(select * from %s except all select * from %s)"
                    % (rv(name), macro, macro, rv(name))))
        hub = f.get("hub") or (self.decl(f["pit"])[1]["hub"] if f.get("pit") else f.get("start"))
        if hub and kind != "analysis":
            hk = "hk_" + hub[4:]
            out.append(("key_unique", "error", "141 section 9 items 1 and 2: one row per key.",
                        "select %s from %s group by 1 having count(*) > 1" % (hk, rv(name))))
        if kind in ("pit", "bridge", "computed") or (kind == "dimension" and f.get("rule") != "calendar"):
            hk = "hk_" + hub[4:]
            if kind in ("pit", "bridge"):
                expected = "select %s from (\n%s\n)" % (hk, ind(self.present(hub, "T")))
                what = "the keys of %s known and present" % hub
            else:
                expected = "select %s from %s" % (hk, rv(f["pit"]))
                what = "the keys of %s" % f["pit"]
            actual = "select %s from %s" % (hk, rv(name)) + (" where %s <> '%s'" % (hk, UNKNOWN) if kind == "dimension" else "")
            out.append(("keys_complete", "error",
                        "141 section 9 item 2: exactly %s, none lost and none added (review of the build, finding 4)." % what,
                        "(select 'missing' as problem, * from (%s except all %s))\nunion all\n(select 'extra', * from (%s except all %s))"
                        % (expected, actual, actual, expected)))
        if kind == "pit":
            for sat, fl in s.get("Satellites", []):
                out.append(("pointer_resolves_once__" + sat, "error",
                            "141 section 3 rule 2: every pointer names exactly one satellite row loaded by the load date\n"
                            "-- (review of the build, findings 1 and 3; the raw vault's version_unique tests are the first guard).",
                            "select p.%s, count(s.%s) as rows_found from %s p\n%s\nwhere p.%s__record_source is not null\n"
                            "group by p.%s having count(s.%s) <> 1"
                            % (hk, hk, rv(name), self.sat_join("s", sat, "p", hk), sat, hk, hk)))
                out.append(("one_source_order__" + sat, "error",
                            "141 section 3 rule 2: the last row in source order is defined only within one source table.",
                            "select 'more than one record source' as problem from (select count(distinct record_source) as n from %s) where n > 1\n"
                            "union all\nselect 'a row without source_ts' from (select count(*) as n from %s where source_ts is null) where n > 0"
                            % (rv(sat), rv(sat))))
        if kind == "computed":
            hk = "hk_" + f["hub"][4:]
            for n, fl in s["Values"]:
                if "oracle" in fl:
                    out.append(("oracle__" + n, "error", "141 section 4: the derived value against the source's own arithmetic.",
                                "select c.%s, c.%s from %s c\njoin %s p on p.%s = c.%s\n%s\nwhere c.%s is distinct from cast(%s as %s)"
                                % (hk, n, rv(name), rv(f["pit"]), hk, hk, self.sat_join("s", f["satellite"], "p", hk), n,
                                   self.expr(fl["oracle"], "s", f["satellite"]), fl["type"])))
        if kind == "fact":
            hk = "hk_" + hub[4:]
            out.append(("grain", "error", "141 section 9 item 1: as many rows as there are keys known and present.",
                        "select * from (select (select count(*) from %s) as fact_rows, (select count(*) from %s) as keys) where fact_rows <> keys"
                        % (rv(name), rv(f["pit"]))))
            rec = []
            for n, fl in s["Measures"]:
                kind2, col = fl["from"].split(".", 1)
                if self.kinds.get(kind2) == "computed":
                    cf, cs = self.decl(kind2)[1], dict(self.decl(kind2)[2]["Values"])
                    sat, e = cf["satellite"], "cast(%s as %s)" % (self.expr(cs[col]["expr"], "t", cf["satellite"]), cs[col]["type"])
                else:
                    sat, e = kind2, "t." + q(col)
                table = self.decl(sat, "satellite")[1]["source_table"]
                rec.append("select '%s' as measure, (select sum(%s) from %s) as mart, (select sum(%s) from %s t) as delivered"
                           % (n, n, rv(name), e, self.stg(table)))
            out.append(("reconciles_with_delivery", "error",
                        "141 section 9 item 3: each measure's total against the current rows delivered in this load. Totals only.",
                        "select * from (\n" + "\nunion all\n".join(rec) + "\n) where mart is distinct from delivered"))
            look, unplaced = [], []
            for n, fl in s["Keys"]:
                dim = fl.get("dimension")
                if not dim:
                    continue
                df = self.decl(dim, "dimension")[1]
                if df.get("rule") == "calendar":
                    look.append("select '%s' as key, cast(f.%s as varchar) as value from %s f where f.%s is not null and f.%s not in (select date from %s)"
                                % (n, n, rv(name), n, n, rv(dim)))
                    unplaced.append("f.%s is null" % n)
                else:
                    dk = "hk_" + df["hub"][4:]
                    look.append("select '%s' as key, f.%s as value from %s f left join %s d on d.%s = f.%s group by f.%s, f.%s having count(d.%s) <> 1"
                                % (n, n, rv(name), rv(dim), dk, n, hk, n, dk))
                    unplaced.append("f.%s = '%s'" % (n, UNKNOWN))
            out.append(("lookups", "error", "141 section 9 item 4: every key finds exactly one row of its dimension.", "\nunion all\n".join(look)))
            out.append(("unplaced_rows", "warn",
                        "ADR-0040 decision 1: lines kept on the unknown member or without a date; a data quality issue, kept visible.",
                        "select f.* from %s f where %s" % (rv(name), "\n   or ".join(unplaced))))
            for n, fl in s["Keys"]:
                if fl.get("expect") == "false":
                    out.append(("unexpected__" + n, "warn", "141 section 9 item 6: none exists today, and what it would mean for the amounts is unknown.",
                                "select f.* from %s f where f.%s" % (rv(name), n)))
            out.append(("lineage", "error",
                        "141 section 9 item 10: row by row against the delivered rows, joined on the source's own identifiers;\n-- no hash key, link, effectivity row, point-in-time table or bridge is used on the delivered side.",
                        self.lineage_sql(name, f, s)))
        if kind == "analysis":
            rows = dict(s["Rows"])
            for n, fl in s.get("Plausibility", []):
                p = fl.get("period")
                if p not in rows or "is_complete_" + p not in rows:
                    raise self.U("%s: plausibility needs the rows %s and is_complete_%s" % (name, p, p))
                dim = rows[p]["from"].split(".")[0]
                if n == "every_complete_period_has_rows":
                    sql = ("select distinct d.%s from %s d where d.is_complete_%s\n  and d.%s not in (select %s from %s where %s is not null)"
                           % (p, rv(dim), p, p, p, rv(name), p))
                elif n == "latest_complete_period_within":
                    v = fl["value"]
                    sql = ("with m as (select %s, sum(%s) as v from %s where is_complete_%s group by 1),\n"
                           "r as (select %s, v, row_number() over (order by %s desc) as rn from m)\n"
                           "select l.%s, l.v, x.med from (select * from r where rn = 1) l\n"
                           "cross join (select median(v) as med from r where rn between 2 and %d) x\n"
                           "where x.med is not null and (l.v < %s * x.med or l.v > %s * x.med)"
                           % (p, v, rv(name), p, p, p, p, int(fl["of"]) + 1, float(fl["low"]), float(fl["high"])))
                else:
                    raise self.U("%s: plausibility check %s is not supported" % (name, n))
                out.append(("plausible__" + n, "warn", "141 section 9 item 6: a plausibility check, a warning while ARC-OP-31 is open.", sql))
        return out

    # ---- run ----------------------------------------------------------------------------------------------------
    def run(self):
        order = ["pit", "bridge", "computed", "dimension", "fact", "analysis"]
        n = 0
        for kind in order:
            for rel, f, s in sorted(self.m.accepted(kind), key=lambda x: x[1]["name"]):
                name, schema = f["name"], SCHEMA[kind]
                build = {"pit": lambda m: self.pit_sql(f, s, m), "bridge": lambda m: self.bridge_sql(f, s, m, name),
                         "computed": lambda m: self.computed_sql(f, s, m), "dimension": lambda m: self.dimension_sql(f, s, m, name),
                         "fact": lambda m: self.fact_sql(f, s, m, name), "analysis": lambda m: self.analysis_sql(f, s, m, name)}[kind]
                head = self.g.header(rel, f["id"], "generate_marts.py")
                self.g.emit("models/%s/%s.sql" % (schema, name),
                            head + "\n{{ config(materialized='table', schema='%s', post_hook=\"{{ nsdn_as_known__%s() }}\") }}\n\n"
                            "-- %s (141). This table is the query below at the load date. The same query with the knowledge date as a\n"
                            "-- parameter is the table macro %s.%s__as_known(known_on), created after the table (141 section 2).\n%s\n"
                            % (schema, name, kind.capitalize(), schema, name, build("T")))
                self.g.emit("macros/generated/as_known__%s.sql" % name,
                            "{%% macro nsdn_as_known__%s() %%}\n%s"
                            "create or replace macro %s.%s__as_known(known_on) as table (\n%s\n)\n{%% endmacro %%}\n"
                            % (name, head, schema, name, build("M")))
                for tname, sev, comment, sql in self.tests(rel, f, s):
                    cfg = "{{ config(severity='warn') }}\n\n" if sev == "warn" else ""
                    self.g.emit("tests/generated/%s__%s.sql" % (name, tname), head + "\n" + cfg + "-- " + comment + "\n" + sql + "\n")
                n += 1
        if n:
            self.g.emit("tests/generated/nsdn__loads_in_date_order.sql",
                        self.g.header(self.m.src_rel, "nsdn__loads_in_date_order", "generate_marts.py")
                        + "\n-- 141 section 2 item 5 and section 9 item 9: 'as known on' holds only if no batch was first loaded\n"
                        "-- successfully after a later-dated one.\n"
                        "with first_ok as (\n    select load_date, min(finished_at) as first_ok from nsdn_meta.dbt_invocations where ok group by 1\n)\n"
                        "select a.load_date, b.load_date as later_date from first_ok a\n"
                        "join first_ok b on a.load_date < b.load_date and a.first_ok > b.first_ok\n")

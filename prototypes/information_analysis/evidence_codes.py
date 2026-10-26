"""Evidence for step A (handover 10): do the source's country and state-province codes conform to the published
ISO lists, so that they may be read as identifiers from a governed namespace (144 section 3)?

The reference lists below were read on the web on 2026-10-26 through a summarising fetch (WebFetch) of the pages
named in REFERENCES, and are recorded as web-source evidence beside the profile. The profile compares every current
row of the extract with them. Aggregates only (analysis/README.md section 7).

    python prototypes/information_analysis/evidence_codes.py
"""
import csv
import gzip
import inspect
import os
import sys

csv.field_size_limit(sys.maxsize)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from profile_tables import ROOT, RAW, write, blob, now, sha  # noqa: E402
import ia_lib as ia  # noqa: E402

SCRIPT = "prototypes/information_analysis/evidence_codes.py"
DAY = os.environ.get("IA_DAY", "2016-06-02")
FETCHED = "2026-10-26T17:45:00Z"
REFERENCES = {
    "iso3166-1": {"url": "https://en.wikipedia.org/wiki/ISO_3166-1",
                  "title": "ISO 3166-1 (Wikipedia), table of current codes"},
    "iso3166-2-us": {"url": "https://en.wikipedia.org/wiki/ISO_3166-2:US",
                     "title": "ISO 3166-2:US (Wikipedia), current subdivision codes"},
}
ISO3166_1 = [  # "alpha-3,numeric", 249 entries
    "AFG,4", "ALA,248", "ALB,8", "DZA,12", "ASM,16", "AND,20", "AGO,24", "AIA,660", "ATA,10", "ATG,28",
    "ARG,32", "ARM,51", "ABW,533", "AUS,36", "AUT,40", "AZE,31", "BHS,44", "BHR,48", "BGD,50", "BRB,52",
    "BLR,112", "BEL,56", "BLZ,84", "BEN,204", "BMU,60", "BTN,64", "BOL,68", "BES,535", "BIH,70", "BWA,72",
    "BVT,74", "BRA,76", "IOT,86", "BRN,96", "BGR,100", "BFA,854", "BDI,108", "CPV,132", "KHM,116", "CMR,120",
    "CAN,124", "CYM,136", "CAF,140", "TCD,148", "CHL,152", "CHN,156", "CXR,162", "CCK,166", "COL,170", "COM,174",
    "COG,178", "COD,180", "COK,184", "CRI,188", "CIV,384", "HRV,191", "CUB,192", "CUW,531", "CYP,196", "CZE,203",
    "DNK,208", "DJI,262", "DMA,212", "DOM,214", "ECU,218", "EGY,818", "SLV,222", "GNQ,226", "ERI,232", "EST,233",
    "SWZ,748", "ETH,231", "FLK,238", "FRO,234", "FJI,242", "FIN,246", "FRA,250", "GUF,254", "PYF,258", "ATF,260",
    "GAB,266", "GMB,270", "GEO,268", "DEU,276", "GHA,288", "GIB,292", "GRC,300", "GRL,304", "GRD,308", "GLP,312",
    "GUM,316", "GTM,320", "GGY,831", "GIN,324", "GNB,624", "GUY,328", "HTI,332", "HMD,334", "VAT,336", "HND,340",
    "HKG,344", "HUN,348", "ISL,352", "IND,356", "IDN,360", "IRN,364", "IRQ,368", "IRL,372", "IMN,833", "ISR,376",
    "ITA,380", "JAM,388", "JPN,392", "JEY,832", "JOR,400", "KAZ,398", "KEN,404", "KIR,296", "PRK,408", "KOR,410",
    "KWT,414", "KGZ,417", "LAO,418", "LVA,428", "LBN,422", "LSO,426", "LBR,430", "LBY,434", "LIE,438", "LTU,440",
    "LUX,442", "MAC,446", "MDG,450", "MWI,454", "MYS,458", "MDV,462", "MLI,466", "MLT,470", "MHL,584", "MTQ,474",
    "MRT,478", "MUS,480", "MYT,175", "MEX,484", "FSM,583", "MDA,498", "MCO,492", "MNG,496", "MNE,499", "MSR,500",
    "MAR,504", "MOZ,508", "MMR,104", "NAM,516", "NRU,520", "NPL,524", "NLD,528", "NCL,540", "NZL,554", "NIC,558",
    "NER,562", "NGA,566", "NIU,570", "NFK,574", "MKD,807", "MNP,580", "NOR,578", "OMN,512", "PAK,586", "PLW,585",
    "PSE,275", "PAN,591", "PNG,598", "PRY,600", "PER,604", "PHL,608", "PCN,612", "POL,616", "PRT,620", "PRI,630",
    "QAT,634", "REU,638", "ROU,642", "RUS,643", "RWA,646", "BLM,652", "SHN,654", "KNA,659", "LCA,662", "MAF,663",
    "SPM,666", "VCT,670", "WSM,882", "SMR,674", "STP,678", "SAU,682", "SEN,686", "SRB,688", "SYC,690", "SLE,694",
    "SGP,702", "SXM,534", "SVK,703", "SVN,705", "SLB,90", "SOM,706", "ZAF,710", "SGS,239", "SSD,728", "ESP,724",
    "LKA,144", "SDN,729", "SUR,740", "SJM,744", "SWE,752", "CHE,756", "SYR,760", "TWN,158", "TJK,762", "TZA,834",
    "THA,764", "TLS,626", "TGO,768", "TKL,772", "TON,776", "TTO,780", "TUN,788", "TUR,792", "TKM,795", "TCA,796",
    "TUV,798", "UGA,800", "UKR,804", "ARE,784", "GBR,826", "USA,840", "UMI,581", "URY,858", "UZB,860", "VUT,548",
    "VEN,862", "VNM,704", "VGB,92", "VIR,850", "WLF,876", "ESH,732", "YEM,887", "ZMB,894", "ZWE,716",
]
ISO3166_2_US = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC', 'AS', 'GU', 'MP', 'PR', 'UM', 'VI']  # 50 states, DC, 6 outlying areas


def conformance(table, columns, reference):
    """Rows of the table whose code (or code pair) is in the reference list, and the distinct codes that are not."""
    f = gzip.open(os.path.join(RAW, DAY, table + ".csv.gz"), "rt", encoding="utf-8", newline="")
    r = csv.reader(f)
    head = next(r)
    idx = [head.index(c) for c in columns]
    rows = conforming = 0
    outside = set()
    for row in r:
        rows += 1
        code = ",".join(row[i] for i in idx)
        if code in reference:
            conforming += 1
        else:
            outside.add(code)
    f.close()
    return {"columns": columns, "rows": rows, "conforming_rows": conforming, "reference_size": len(reference),
            "distinct_codes_outside_reference": len(outside)}


def main():
    manifest = sha(os.path.join(RAW, DAY, "manifest.json"))
    checks = [("Application.Countries", ["IsoAlpha3Code", "IsoNumericCode"], "iso3166-1", ISO3166_1),
              ("Application.StateProvinces", ["StateProvinceCode"], "iso3166-2-us", ISO3166_2_US)]
    for table, cols, ref, values in checks:
        web = {"kind": "web source", "tool": "WebFetch (a summarising fetch; the list was returned by the fetch's model "
               "and not checked against the page by hand)", "tool_version": "n/a", "ran_at": FETCHED,
               "inputs": REFERENCES[ref], "excerpt": values,
               "result": {"entries": len(values)}}
        s, n = table.split(".")
        out = os.path.join(ROOT, "analysis", "wwi", "tables", ia.escape(s), ia.escape(n), "evidence")
        w = write(out, web)
        rec = {"kind": "profile", "tool": SCRIPT, "tool_version": blob(SCRIPT), "code": inspect.getsource(conformance),
               "inputs": {"source": "wwi", "extract": DAY, "manifest_sha256": manifest, "table": table,
                          "reference_evidence": w},
               "ran_at": now(), "result": conformance(table, cols, set(values))}
        print(w, write(out, rec), table, rec["result"])


if __name__ == "__main__":
    main()

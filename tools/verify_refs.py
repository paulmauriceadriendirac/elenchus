#!/usr/bin/env python3
"""Check that every reference exists and that its metadata is right, using Crossref
(primary) and OpenAlex (fallback). Books and older chapters are often missing from both;
those come back NOT_FOUND and must be verified by the citation-auditor by other means
(publisher page, PhilPapers record, library catalogue) before they may stay in the essay.

Input: JSON list of reference objects, e.g. state/bib/refs.json
  [{"key": "Lewis1973", "authors": ["David Lewis"], "year": 1973, "title": "Causation",
    "venue": "Journal of Philosophy", "volume": "70", "pages": "556-567",
    "doi": "10.2307/2025310", "type": "article"}]

Usage:
    python3 tools/verify_refs.py state/bib/refs.json [--out state/bib/verification.json] [--md state/bib/verification.md]

Statuses:
  VERIFIED   title, first-author surname and year all match a registry record
  PROBABLE   close match; a field differs (reported) — fix metadata or confirm by hand
  MISMATCH   DOI resolves to a different work, or key fields conflict
  NOT_FOUND  no adequate registry match (common for books) — verify manually or drop
  ERROR      network failure — rerun, or verify manually
"""
import argparse
import difflib
import json
import re
import sys
import time
import unicodedata
import urllib.parse

try:
    import requests
except ImportError:
    print("pip install requests", file=sys.stderr)
    sys.exit(2)

UA = {"User-Agent": "elenchus-harness/1.0 (reference verification; academic use)"}
SESSION = requests.Session()
SESSION.headers.update(UA)


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    s = re.sub(r"<[^>]+>", " ", s)          # strip JATS/HTML tags in Crossref titles
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def sim(a, b):
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0.0
    # compare on the main title (before a subtitle colon) as well as the full title
    full = difflib.SequenceMatcher(None, a, b).ratio()
    main_a, main_b = a.split(" ")[:12], b.split(" ")[:12]
    head = difflib.SequenceMatcher(None, " ".join(main_a), " ".join(main_b)).ratio()
    return max(full, head)


def surname(name):
    name = (name or "").strip()
    if "," in name:
        return norm(name.split(",")[0])
    parts = name.split()
    return norm(parts[-1]) if parts else ""


def get(url, tries=4):
    delay = 2.0
    for _ in range(tries):
        try:
            r = SESSION.get(url, timeout=25)
        except requests.RequestException as e:
            last = str(e)
            time.sleep(delay)
            delay *= 2
            continue
        if r.status_code == 429 or r.status_code >= 500:
            last = f"HTTP {r.status_code}"
            time.sleep(delay)
            delay *= 2
            continue
        if r.status_code == 404:
            return None
        if r.status_code == 403:
            raise RuntimeError("HTTP 403 (network policy?) for " + url.split("?")[0])
        r.raise_for_status()
        return r.json()
    raise RuntimeError(last)


def crossref_by_doi(doi):
    d = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    return d["message"] if d else None


def crossref_search(ref):
    q = " ".join(str(x) for x in [ref.get("title", ""), " ".join(ref.get("authors", [])[:2]), ref.get("year", "")] if x)
    params = {"query.bibliographic": q, "rows": 6,
              "select": "DOI,title,author,issued,container-title,type,page,volume,publisher"}
    if ref.get("authors"):
        params["query.author"] = surname(ref["authors"][0])
    d = get("https://api.crossref.org/works?" + urllib.parse.urlencode(params))
    return (d or {}).get("message", {}).get("items", [])


def openalex_search(ref):
    q = ref.get("title", "")
    d = get("https://api.openalex.org/works?" + urllib.parse.urlencode({"search": q, "per-page": 6}))
    return (d or {}).get("results", [])


def cr_fields(it):
    title = (it.get("title") or [""])[0]
    authors = [a.get("family") or a.get("name", "") for a in it.get("author", [])]
    year = None
    for k in ("issued", "published-print", "published-online"):
        dp = (it.get(k) or {}).get("date-parts")
        if dp and dp[0] and dp[0][0]:
            year = dp[0][0]
            break
    venue = (it.get("container-title") or [""])[0] or it.get("publisher", "")
    return {"title": title, "authors": authors, "year": year, "venue": venue,
            "doi": it.get("DOI"), "type": it.get("type"), "volume": it.get("volume"), "pages": it.get("page")}


def oa_fields(it):
    authors = [((a.get("author") or {}).get("display_name") or "").split()[-1:] for a in it.get("authorships", [])]
    authors = [a[0] if a else "" for a in authors]
    src = ((it.get("primary_location") or {}).get("source") or {}).get("display_name", "")
    doi = (it.get("doi") or "").replace("https://doi.org/", "") or None
    return {"title": it.get("title") or "", "authors": authors, "year": it.get("publication_year"),
            "venue": src, "doi": doi, "type": it.get("type")}


def judge(ref, cand):
    t = sim(ref.get("title", ""), cand["title"])
    want = surname(ref["authors"][0]) if ref.get("authors") else ""
    have = [norm(a) for a in cand["authors"]]
    author_ok = (not want) or any(want == h or want in h or h in want for h in have if h)
    y_ref, y_c = ref.get("year"), cand.get("year")
    try:
        year_ok = (y_ref is None or y_c is None) or abs(int(y_ref) - int(y_c)) <= 1
    except (TypeError, ValueError):
        year_ok = True
    return t, author_ok, year_ok


def verify(ref):
    notes = []
    if ref.get("doi"):
        try:
            it = crossref_by_doi(ref["doi"])
        except RuntimeError as e:
            return {"status": "ERROR", "notes": [str(e)]}
        if it:
            c = cr_fields(it)
            t, a_ok, y_ok = judge(ref, c)
            if t >= 0.85 and a_ok and y_ok:
                return {"status": "VERIFIED", "match": c, "title_similarity": round(t, 3), "source": "crossref-doi"}
            return {"status": "MISMATCH", "match": c, "title_similarity": round(t, 3),
                    "notes": [f"DOI resolves to a different/conflicting record (title sim {t:.2f}, author ok {a_ok}, year ok {y_ok})"]}
        notes.append("DOI not found in Crossref")
    best = None
    queried = False
    try:
        for it in crossref_search(ref):
            c = cr_fields(it)
            score = judge(ref, c)
            if best is None or score[0] > best[1][0]:
                best = (c, score, "crossref-search")
        queried = True
    except RuntimeError as e:
        notes.append("crossref unavailable: " + str(e))
    if not best or best[1][0] < 0.9:
        try:
            for it in openalex_search(ref):
                c = oa_fields(it)
                score = judge(ref, c)
                if best is None or score[0] > best[1][0]:
                    best = (c, score, "openalex-search")
            queried = True
        except RuntimeError as e:
            notes.append("openalex unavailable: " + str(e))
    if not queried:
        return {"status": "ERROR", "notes": notes + ["no registry could be queried; rerun later or verify by hand"]}
    if not best:
        return {"status": "NOT_FOUND", "notes": notes}
    c, (t, a_ok, y_ok), src = best
    out = {"match": c, "title_similarity": round(t, 3), "source": src, "notes": notes}
    if t >= 0.9 and a_ok and y_ok:
        out["status"] = "VERIFIED"
    elif t >= 0.75 and a_ok:
        out["status"] = "PROBABLE"
        if not y_ok:
            out["notes"].append(f"year differs: ref {ref.get('year')} vs registry {c.get('year')}")
    else:
        out["status"] = "NOT_FOUND"
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--out", default="")
    ap.add_argument("--md", default="")
    ap.add_argument("--sleep", type=float, default=1.0)
    a = ap.parse_args()
    refs = json.load(open(a.path, encoding="utf-8"))
    results = []
    for ref in refs:
        r = verify(ref)
        r["key"] = ref.get("key")
        r["ref"] = ref
        results.append(r)
        m = r.get("match") or {}
        print(f"{r['status']:9} {ref.get('key')}: {ref.get('title','')[:70]}"
              + (f"  -> {m.get('title','')[:60]} ({m.get('year')}) doi:{m.get('doi')}" if m else "")
              + (f"  [{'; '.join(r.get('notes', []))}]" if r.get("notes") else ""))
        time.sleep(a.sleep)
    summary = {}
    for r in results:
        summary[r["status"]] = summary.get(r["status"], 0) + 1
    print("summary:", summary)
    if a.out:
        json.dump(results, open(a.out, "w", encoding="utf-8"), indent=2)
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Reference verification\n\n" + ", ".join(f"{k}: {v}" for k, v in summary.items()) + "\n\n")
            f.write("| key | status | registry match | DOI | notes |\n|---|---|---|---|---|\n")
            for r in results:
                m = r.get("match") or {}
                f.write(f"| {r['key']} | {r['status']} | {m.get('title','')[:70]} ({m.get('year','')}) | {m.get('doi') or ''} | {'; '.join(r.get('notes', []))} |\n")
    sys.exit(0 if all(r["status"] == "VERIFIED" for r in results) else 1)


if __name__ == "__main__":
    main()
